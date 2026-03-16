# 5. Google Sheet Template

## Tổng quan cấu trúc

```
SHEET ADMIN (1 file - chỉ bạn truy cập)
└── Tab "Config" → Thông tin tất cả khách

SHEET KHÁCH (1 file/khách - khách + bạn truy cập)
├── Tab "Video TikTok" → Danh sách video cần đăng
└── Tab "Link Shopee" → Link sản phẩm shopee (để comment)
```

## Sheet Admin — Tab "Config"

### Cấu trúc cột:

| Cột | Tên cột | Kiểu | Bắt buộc | Mô tả |
|-----|---------|------|----------|--------|
| A | `ten_khach` | Text | ✅ | Tên khách hàng / Tên Page |
| B | `facebook_token` | Text | ✅ | Facebook Page Access Token |
| C | `page_id` | Text | ❌ | Facebook Page ID (auto detect từ token) |
| D | `sheet_id` | Text | ✅ | Google Sheet ID của khách |
| E | `sheet_tab_video` | Text | ❌ | Tên tab video (mặc định: "Video TikTok") |
| F | `sheet_tab_shopee` | Text | ❌ | Tên tab shopee (mặc định: "Link Shopee") |
| G | `zalo_token` | Text | ✅ | Zalo Bot Token |
| H | `chat_id` | Text | ✅ | Zalo Chat ID |
| I | `interval_hours` | Number | ✅ | Tần suất đăng (giờ) |
| J | `status` | Text | ✅ | `active` / `paused` / `expired` |
| K | `token_expiry` | Date | ❌ | Ngày token hết hạn |
| L | `last_run` | DateTime | ❌ | Lần chạy cuối (auto fill bởi n8n) |
| M | `total_videos` | Number | ❌ | Tổng video đã đăng (auto fill) |
| N | `ghi_chu` | Text | ❌ | Ghi chú |

### Dữ liệu mẫu:

```
| ten_khach    | facebook_token | page_id     | sheet_id           | zalo_token | chat_id | interval | status | token_expiry |
|-------------|---------------|-------------|--------------------|-----------:|---------|----------|--------|-------------|
| Bếp nhà rơm | EAABx12345... | 12345678    | 1sym6y6jbEin...    | bot_abc... | 999111  | 4        | active | 2026-05-15  |
| Review phim | EAABy67890... | 87654321    | 2abc7z8kLmn...     | bot_def... | 999222  | 6        | active | 2026-06-01  |
| Test khách  | EAABz11111... | 11111111    | 3def8a9bOpq...     | bot_ghi... | 999333  | 2        | paused |             |
```

## Sheet Khách — Tab "Video TikTok"

### Cấu trúc cột:

| Cột | Tên cột | Kiểu | Người điền | Mô tả |
|-----|---------|------|-----------|--------|
| A | `Video Tiktok` | URL | 👤 Khách | Link video TikTok cần repost |
| B | `Video Facebook` | URL | 🤖 Auto | Link video Facebook sau khi đăng |
| C | `Trạng thái` | Text | 🤖 Auto | "thành công" / "lỗi" / trống |
| D | `Thời gian` | DateTime | 🤖 Auto | Thời điểm đăng thành công |

### Dữ liệu mẫu:

```
| Video Tiktok                              | Video Facebook                    | Trạng thái  | Thời gian          |
|------------------------------------------|----------------------------------|------------|-------------------|
| https://www.tiktok.com/@user/video/123   | fb.com/12345678_9876543210       | thành công | 14:30:00 16-03-2026|
| https://www.tiktok.com/@user/video/456   | fb.com/12345678_1234567890       | thành công | 18:30:00 16-03-2026|
| https://www.tiktok.com/@user/video/789   |                                  |            |                   |
```

### Quy tắc:
- Khách chỉ cần dán link TikTok vào cột A
- Các cột B, C, D do n8n tự điền
- Video có Trạng thái "thành công" sẽ bị skip (không đăng lại)
- Video có Trạng thái trống hoặc "lỗi" sẽ được xử lý

## Sheet Khách — Tab "Link Shopee"

### Cấu trúc cột:

| Cột | Tên cột | Kiểu | Người điền | Mô tả |
|-----|---------|------|-----------|--------|
| A | `Tên sản phẩm` | Text | 👤 Khách | Tên sản phẩm (sẽ hiển thị trong comment) |
| B | `Link` | URL | 👤 Khách | Link Shopee affiliate |

### Dữ liệu mẫu:

```
| Tên sản phẩm           | Link                                    |
|------------------------|-----------------------------------------|
| Nồi chiên không dầu   | https://shope.ee/abc123                 |
| Bếp từ Sunhouse       | https://shope.ee/def456                 |
| Chảo chống dính        | https://shope.ee/ghi789                 |
```

### Quy tắc:
- Mỗi video đăng thành công sẽ comment TẤT CẢ link trong tab này
- Format comment: `{Tên sản phẩm}\n{Link}`
- Các comment cách nhau 15 giây (tránh spam)

## Phân quyền

| Sheet | Bạn (Admin) | Khách | n8n Service Account |
|-------|-------------|-------|---------------------|
| Sheet Admin | ✅ Owner | ❌ Không thấy | ✅ Editor |
| Sheet Khách A | ✅ Editor | ✅ Editor (chỉ sheet của họ) | ✅ Editor |
| Sheet Khách B | ✅ Editor | ✅ Editor (chỉ sheet của họ) | ✅ Editor |

## Tạo Sheet mới cho khách (Manual)

```
1. Mở Google Sheet template
2. File → Make a copy
3. Đổi tên: "[Tên khách] - Bếp nhà Tool"
4. Share → Thêm email khách (Editor)
5. Copy Sheet ID từ URL
6. Thêm Sheet ID vào Sheet Admin Config
```
