# Image-Hand Cloud Run Microservice

Microservice chuyên dụng cho n8n xử lý ảnh (remove background) và ghép ảnh (compose).

## 🚀 Quick Start (Deployment)

### 1. Cài đặt môi trường

- Cài đặt [Google Cloud SDK (gcloud)](https://cloud.google.com/sdk/docs/install).
- Login và cấu hình:
  ```bash
  gcloud auth login
  gcloud config set project YOUR_PROJECT_ID
  ```

### 2. Kích hoạt dịch vụ cần thiết

```bash
gcloud services enable run.googleapis.com artifactregistry.googleapis.com cloudbuild.googleapis.com
```

### 3. Deploy lên Cloud Run

Bạn có thể sử dụng script có sẵn hoặc chạy lệnh trực tiếp:

**Windows (PowerShell):**

```powershell
.\scripts\deploy.ps1 -ProjectId YOUR_PROJECT_ID -Region asia-southeast1
```

**Ubuntu/macOS (Bash):**

```bash
chmod +x scripts/deploy.sh
./scripts/deploy.sh YOUR_PROJECT_ID asia-southeast1
```

**Lệnh deploy trực tiếp:**

```bash
gcloud run deploy image-hand --source . --region asia-southeast1 --allow-unauthenticated --memory 1Gi --cpu 1 --timeout 300
```

---

## 🛠 Endpoints

### 1. Health Check

`GET /health`

```bash
curl https://image-hand-xxxx.a.run.app/health
```

### 2. Remove Background

`POST /remove-bg`

**Cách 1: Gửi URL ảnh (JSON body)**

```bash
curl -X POST https://image-hand-xxxx.a.run.app/remove-bg \
     -H "Content-Type: application/json" \
     -d '{"image_url": "https://example.com/shirt.jpg"}' \
     --output shirt_no_bg.png
```

**Cách 2: Upload file (Multipart)**

```bash
curl -X POST https://image-hand-xxxx.a.run.app/remove-bg \
     -F "file=@shirt.jpg" \
     --output shirt_no_bg.png
```

### 3. Compose (Gói ảnh)

`POST /compose`

```bash
curl -X POST https://image-hand-xxxx.a.run.app/compose \
     -H "Content-Type: application/json" \
     -d '{
       "product_png_base64": "...",
       "bg_image_base64": "...",
       "scale": 0.8,
       "x": 0.5,
       "y": 0.6,
       "shadow": true
     }' \
     --output final_composite.png
```

---

## 🔗 Tích hợp n8n

Trong node **HTTP Request** của n8n:

- **Method:** POST
- **URL:** `{{$json.CLOUD_RUN_BASE}}/remove-bg`
- **Body Content Type:** JSON
- **Body Parameters:** `image_url` set to the image URL.
- **Response Format:** File (Binary)

---

## 🔒 Bảo mật (TODO)

Hiện tại service được set `--allow-unauthenticated` để n8n gọi dễ dàng.
Để bảo mật hơn:

1. Thêm biến môi trường `API_KEY` trong Cloud Run console.
2. Cập nhật logic `main.py` để kiểm tra header `X-API-KEY`.
3. Thay đổi deploy command thành `--no-allow-unauthenticated` và sử dụng IAM authentication nếu n8n có hỗ trợ Service Account.

---

## 📦 Cấu trúc Project

```text
cloudrun-image-hand/
├── main.py            # FastAPI Logic
├── requirements.txt   # Python Dependencies
├── Dockerfile         # Container Config
├── .dockerignore      # Exclude items
├── README.md          # Hướng dẫn này
├── scripts/
    ├── deploy.sh      # Bash script deploy
    └── deploy.ps1     # PowerShell script deploy
```
