import io
import time
import uuid
import base64
import requests
import logging
from typing import Optional
from fastapi import FastAPI, File, UploadFile, HTTPException, Depends, Request, Body
from fastapi.responses import Response, StreamingResponse
from pydantic import BaseModel
from PIL import Image, ImageOps, ImageFilter
from rembg import remove
import numpy as np

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("image-hand")

app = FastAPI(title="Cloud Run Image Hand")

MAX_SIZE_MB = 10
MAX_DIMENSION = 2048

class ImageUrlRequest(BaseModel):
    image_url: str

class ComposeRequest(BaseModel):
    product_png_base64: str
    bg_image_base64: str
    scale: float = 0.78
    x: float = 0.5
    y: float = 0.58
    shadow: bool = True

def generate_request_id():
    return str(uuid.uuid4())[:8]

def resize_if_needed(image: Image.Image) -> Image.Image:
    width, height = image.size
    if width > MAX_DIMENSION or height > MAX_DIMENSION:
        if width > height:
            new_width = MAX_DIMENSION
            new_height = int(height * (MAX_DIMENSION / width))
        else:
            new_height = MAX_DIMENSION
            new_width = int(width * (MAX_DIMENSION / height))
        logger.info(f"Resizing image from {width}x{height} to {new_width}x{new_height}")
        return image.resize((new_width, new_height), Image.LANCZOS)
    return image

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/remove-bg")
async def remove_background(
    request: Request,
    image_request: Optional[ImageUrlRequest] = None,
    file: Optional[UploadFile] = File(None)
):
    req_id = generate_request_id()
    start_time = time.perf_counter()
    input_type = "unknown"
    
    try:
        image_data = None
        
        # Priority 1: File Upload
        if file:
            input_type = "file"
            content = await file.read()
            if len(content) > MAX_SIZE_MB * 1024 * 1024:
                raise HTTPException(status_code=413, detail="File too large (max 10MB)")
            image_data = content
            logger.info(f"[{req_id}] Received file upload: {file.filename}, size: {len(content)} bytes")
            
        # Priority 2: URL in Body
        elif image_request and image_request.image_url:
            input_type = "url"
            logger.info(f"[{req_id}] Fetching image from URL: {image_request.image_url}")
            response = requests.get(image_request.image_url, timeout=30)
            if response.status_code != 200:
                raise HTTPException(status_code=400, detail="Could not fetch image from URL")
            image_data = response.content
            if len(image_data) > MAX_SIZE_MB * 1024 * 1024:
                raise HTTPException(status_code=413, detail="Image at URL too large (max 10MB)")

        if not image_data:
            raise HTTPException(status_code=400, detail="No image provided (URL or file)")

        # Open image
        try:
            img = Image.open(io.BytesIO(image_data))
            img = ImageOps.exif_transpose(img) # Fix rotation
        except Exception:
            raise HTTPException(status_code=415, detail="Invalid image file")

        # Resize if too large
        img = resize_if_needed(img)
        
        # Remove background
        img_array = np.frombuffer(image_data, np.uint8)
        # We use PIL image directly for rembg
        output_img = remove(img)
        
        # Save to buffer
        buf = io.BytesIO()
        output_img.save(buf, format="PNG")
        byte_im = buf.getvalue()

        elapsed_ms = int((time.perf_counter() - start_time) * 1000)
        logger.info(f"[{req_id}] Success: type={input_type}, size={len(byte_im)}, time={elapsed_ms}ms")
        
        return Response(content=byte_im, media_type="image/png")

    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"[{req_id}] Error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal processing error: {str(e)}")

@app.post("/compose")
async def compose_image(payload: ComposeRequest):
    req_id = generate_request_id()
    start_time = time.perf_counter()
    
    try:
        # Decode images
        try:
            p_data = base64.b64decode(payload.product_png_base64)
            b_data = base64.b64decode(payload.bg_image_base64)
            product = Image.open(io.BytesIO(p_data)).convert("RGBA")
            background = Image.open(io.BytesIO(b_data)).convert("RGBA")
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Invalid base64 data: {str(e)}")

        # Resize product based on scale relative to background
        bg_w, bg_h = background.size
        target_h = int(bg_h * payload.scale)
        p_aspect = product.width / product.height
        target_w = int(target_h * p_aspect)
        
        product_resized = product.resize((target_w, target_h), Image.LANCZOS)
        
        # Create shadow if requested
        if payload.shadow:
            shadow_color = (0, 0, 0, 150) # Semi-transparent black
            shadow_blur = 20
            # Create a shadow image from alpha channel
            alpha = product_resized.getchannel('A')
            shadow = Image.new("RGBA", product_resized.size, shadow_color)
            shadow.putalpha(alpha)
            shadow = shadow.filter(ImageFilter.GaussianBlur(shadow_blur))
            
            # Create a canvas for the composite
            composite = Image.new("RGBA", background.size, (0, 0, 0, 0))
            
            # Position (X, Y are ratios 0..1)
            pos_x = int(bg_w * payload.x - target_w / 2)
            pos_y = int(bg_h * payload.y - target_h / 2)
            
            # Paste shadow with slight offset
            background.alpha_composite(shadow, (pos_x + 5, pos_y + 10))
        else:
            pos_x = int(bg_w * payload.x - target_w / 2)
            pos_y = int(bg_h * payload.y - target_h / 2)

        # Paste product
        background.alpha_composite(product_resized, (pos_x, pos_y))
        
        # Save output
        buf = io.BytesIO()
        background.save(buf, format="PNG")
        byte_im = buf.getvalue()
        
        elapsed_ms = int((time.perf_counter() - start_time) * 1000)
        logger.info(f"[{req_id}] Compose Success: time={elapsed_ms}ms")
        
        return Response(content=byte_im, media_type="image/png")
        
    except Exception as e:
        logger.error(f"[{req_id}] Compose Error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Compose error: {str(e)}")
