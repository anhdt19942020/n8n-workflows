# 1. Tổng quan Workflow "Bếp nhà"

## Mục đích

Tự động hóa quy trình:
1. Lấy video từ TikTok
2. Đăng lên Facebook Reels
3. Comment link Shopee affiliate
4. Thông báo kết quả qua Zalo

## Sơ đồ luồng

```
Schedule Trigger (mỗi 4h)
    │
    ▼
Get List Video (Google Sheets - tab "bếp")
    │
    ▼
If (Trạng thái chưa "thành công")
    │
    ▼
Limit (1 video/lần)
    │
    ▼
Download Video (TikWM API - lấy video HD từ TikTok)
    │
    ▼
Upload Session (Facebook Graph API v23 - tạo upload session cho Reels)
    │
    ▼
Upload video (HTTP Request - upload file từ TikWM URL lên Facebook)
    │
    ▼
Publish (Facebook Graph API - publish reel + description)
    │
    ▼
Wait 30s → Get status (kiểm tra video xử lý xong chưa)
    │
    ├── ready → Get Page ID → Update Status (Google Sheets)
    │              → Wait 10s → Get Link Shopee
    │              → Loop Over Items → Comment (link Shopee)
    │              → Send message (Zalo thông báo thành công)
    │
    ├── error → Send Error (Zalo thông báo lỗi)
    │
    └── processing → Wait 30s (loop lại check status)
```

## Danh sách Nodes

| # | Node | Type | Chức năng |
|---|------|------|-----------|
| 1 | Schedule Trigger | scheduleTrigger | Chạy tự động mỗi 4 giờ |
| 2 | Get List Video | googleSheets | Đọc danh sách video TikTok từ Sheet |
| 3 | If | if | Kiểm tra video chưa đăng (Trạng thái trống hoặc ≠ "thành công") |
| 4 | Limit | limit | Giới hạn 1 video mỗi lần chạy |
| 5 | Download Video | httpRequest | Gọi TikWM API download video TikTok HD |
| 6 | Upload Session | facebookGraphApi | Tạo upload session cho Facebook Reels |
| 7 | Upload video | httpRequest | Upload video lên Facebook |
| 8 | Publish | facebookGraphApi | Publish reel với description từ TikTok |
| 9 | Wait 30s | wait | Chờ Facebook xử lý video |
| 10 | Get status | facebookGraphApi | Kiểm tra trạng thái video |
| 11 | Switch | switch | Phân nhánh: ready / error / processing |
| 12 | Get Page ID | facebookGraphApi | Lấy Page ID |
| 13 | Update Status | googleSheets | Cập nhật trạng thái "thành công" + link video |
| 14 | Wait 10s | wait | Chờ trước khi comment |
| 15 | Get Link Shopee | googleSheets | Đọc danh sách link Shopee |
| 16 | Loop Over Items | splitInBatches | Loop qua từng link Shopee |
| 17 | Comment | facebookGraphApi | Comment link Shopee dưới video |
| 18 | Wait 15s | wait | Chờ giữa các comment |
| 19 | Send message | httpRequest | Thông báo thành công qua Zalo Bot |
| 20 | Send Error | httpRequest | Thông báo lỗi qua Zalo Bot |

## Credentials cần thiết (workflow gốc)

| Credential | Type | Sử dụng tại |
|------------|------|-------------|
| Facebook Graph API "bếp nhà rơm" | facebookGraphApi | Upload Session, Upload video, Publish |
| Facebook Graph API "review phim" | facebookGraphApi | Get status, Get Page ID, Comment |
| Google Sheets OAuth2 "bếp nhà rơm" | googleSheetsOAuth2Api | Get List Video, Update Status, Get Link Shopee |

## APIs bên ngoài

| API | URL | Auth | Ghi chú |
|-----|-----|------|---------|
| TikWM | https://tikwm.com/api/ | Không cần | Free, download video TikTok |
| Zalo Bot | https://bot-api.zapps.me/bot{token}/sendMessage | Bot token trong URL | Thông báo kết quả |
| Facebook Graph API | https://graph.facebook.com/v23.0/ | Page Access Token | Upload + Publish Reels |

## Google Sheet cấu trúc gốc

**Document:** `1sym6y6jbEinNUN8MiGY03-hRLpQIAY4yqnSFTTdNNvM`

### Tab "Tiktok" (gid=0) — Danh sách video
| Cột | Mô tả |
|-----|--------|
| Video Tiktok | Link video TikTok cần repost |
| Video Facebook | Link video Facebook sau khi đăng (auto fill) |
| Trạng thái | "thành công" hoặc trống (auto fill) |
| Thời gian | Thời điểm đăng thành công (auto fill) |

### Tab "bếp" (gid=1795330513) — Link Shopee
| Cột | Mô tả |
|-----|--------|
| Tên sản phẩm | Tên sản phẩm Shopee |
| Link | Link Shopee affiliate |
