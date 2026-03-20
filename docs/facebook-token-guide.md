# Hướng Dẫn Lấy 60-Day Facebook Page Access Token

Tài liệu này hướng dẫn cách lấy token 60 ngày cho trang (Page Access Token) từ Facebook Graph API sử dụng ứng dụng "Tiktok perfect", lưu phục vụ quy trình automation qua hệ thống `n8n` ở dự án `n8n-workflows`.

## 📌 Chuẩn Bị
- Tên Ứng Dụng: `Tiktok perfect`
- App ID: `918028547640118`
- App Secret: (*Lấy tại: `developers.facebook.com` → App "Tiktok perfect" → **Settings → Basic** - BẢO MẬT, TUYỆT ĐỐI KHÔNG SHARE!*)

## 🎯 Các Bước Lấy Token

### Bước 1: Lấy Token Ngắn Hạn (1-2 Giờ)
1. Truy cập **[Graph API Explorer](https://developers.facebook.com/tools/explorer/)**.
2. **Ứng dụng Metadata**: Chọn `Tiktok perfect`.
3. **Người dùng hoặc Trang**: Chọn Trang của bạn: `Trang Sách Cuộc Đời`.
4. **Quyền (Permissions)**: Thêm các quyền quan trọng, cụ thể như:
    - `pages_manage_posts`
    - `pages_read_engagement`
    - `pages_manage_metadata`
5. Click **"Generate Access Token"** (nút màu xanh).
6. Copy token được tạo ra (bắt đầu bằng `EAANC...`) - đây được đánh dấu là `YOUR_SHORT_TOKEN`.

### Bước 2: Gọi API Quy Đổi Sang Token 60 Ngày (Long-Lived)
Sao chép liên kết dưới đây, đổi biến số rồi dán vào trình duyệt (Browser):

```http
https://graph.facebook.com/v25.0/oauth/access_token?grant_type=fb_exchange_token&client_id=YOUR_APP_ID&client_secret=YOUR_APP_SECRET&fb_exchange_token=YOUR_SHORT_TOKEN
```

⚠️ Thay thế các thông số:
- `YOUR_APP_ID`: Nhập `918028547640118`
- `YOUR_APP_SECRET`: Lấy từ Setting App
- `YOUR_SHORT_TOKEN`: Paste đoạn token bạn copy ở Bước 1.

Kết quả trả về qua trình duyệt sẽ là 1 cục JSON, tìm đoạn text của biến `access_token` - Đây chính là **Long-Lived Page Token** (sống ~60 ngày).

### Bước 3: Kiểm Tra Lại Token (Debug Token)
Để đảm bảo chắc chắn token đã đạt hiệu lực 60 ngày:
1. Quay lại trang thiết lập hoặc truy cập url sau để debug (nhớ thay `{YOUR_LONG_TOKEN}` bằng token copy tại bước 2):
```http
https://graph.facebook.com/v25.0/debug_token?input_token={YOUR_LONG_TOKEN}&access_token=918028547640118|YOUR_APP_SECRET
```
2. Nếu tại giá trị `expires_at` hiển thị ngày sau khoảng 60 ngày, và có phần `type: "PAGE"` — Chúc mừng bạn, token đã có thể áp dụng!

---

## ⚙️ Thiết Lập Mặc Định

Sử dụng Token này cấu hình vào Node **Facebook/Meta** (hoặc `http request` API facebook) trên quy trình N8N cho project.

⏰ **Lời Khuyên**: Nên đặt hẹn tự động cập nhật lại token trước khi 60 ngày kết thúc (khoảng 3-5 ngày). Quá trình trên cần được tiến hành theo cách thủ công. Mật khẩu thay đổi sẽ lập tức "revoke" token này.
