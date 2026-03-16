# 2. Kiến trúc Multi-tenant

## Phương án đã chốt

**1 Master Workflow + Google Sheet Config** — Không cần clone workflow cho mỗi khách.

```
┌─────────────────────────────────────────────────────────────┐
│                      n8n Server (1 instance)                │
│                                                             │
│  ┌───────────────────────────────────────────────────────┐  │
│  │              1 MASTER WORKFLOW DUY NHẤT               │  │
│  │                                                       │  │
│  │  Schedule → Đọc Config → Loop khách → Xử lý video    │  │
│  └───────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
            │                        │
            ▼                        ▼
┌──────────────────┐    ┌─────────────────────────┐
│  SHEET ADMIN     │    │  SHEET KHÁCH (mỗi khách │
│  (chỉ bạn thấy) │    │  1 file riêng)          │
│                  │    │                         │
│  Tab "Config":   │    │  Tab "Video TikTok":    │
│  - Tên khách     │    │  - Link video           │
│  - FB Token      │    │  - Trạng thái (auto)    │
│  - Sheet ID      │    │  - Thời gian (auto)     │
│  - Zalo Token    │    │                         │
│  - Chat ID       │    │  Tab "Link Shopee":     │
│  - Trạng thái    │    │  - Tên sản phẩm         │
│                  │    │  - Link affiliate        │
└──────────────────┘    └─────────────────────────┘
```

## Tại sao chọn phương án này?

| Tiêu chí | Phương án A (Clone WF) | **Phương án B (Config Sheet) ✅** |
|-----------|----------------------|----------------------------------|
| Số workflow | N (= số khách) | **1 duy nhất** |
| Thêm khách mới | Clone WF + config credentials | **Thêm 1 dòng vào Sheet Config** |
| Update logic | Sửa N workflow | **Sửa 1 workflow** |
| Credentials | Lưu trong n8n | **Lưu trong Sheet Admin (tập trung)** |
| Khách thấy gì | Không | **Google Sheet của họ** |
| Scale | ~30 khách | **100+ khách** |

## Thay đổi kỹ thuật so với workflow gốc

### 1. Thêm bước đầu: Đọc Config + Loop

```
[Schedule Trigger]
    │
    ▼
[Đọc Sheet Admin - Tab "Config"]  ← MỚI
    │
    ▼
[Filter: chỉ khách "active"]      ← MỚI
    │
    ▼
[Loop từng khách]                  ← MỚI
    │
    ▼
[...flow xử lý video như cũ, nhưng dùng token động...]
```

### 2. Thay Facebook Graph API node → HTTP Request

**Lý do:** Facebook Graph API node trong n8n dùng credential cố định (lưu trong n8n). Không thể đổi token theo từng khách khi loop. Phải chuyển sang HTTP Request + truyền token từ Config Sheet.

**Trước (workflow gốc):**
```
Node: facebookGraphApi
Credential: "bếp nhà rơm" (hardcode)
```

**Sau (workflow mới):**
```
Node: httpRequest
URL: https://graph.facebook.com/v23.0/me/video_reels
Header: Authorization = Bearer {{ $json.facebook_token }}  ← token từ Config
```

### 3. Google Sheets đọc động

**Trước:** Sheet ID hardcode trong node
**Sau:** Sheet ID lấy từ Config, truyền vào node qua expression

```
Document ID: {{ $('Đọc Config').item.json.sheet_id }}
```

### 4. Zalo Bot gửi động

**Trước:** Token + Chat ID hardcode
**Sau:**
```
URL: https://bot-api.zapps.me/bot{{ $json.zalo_token }}/sendMessage
Body: { "chat_id": "{{ $json.chat_id }}", ... }
```

## Luồng hoạt động mới (chi tiết)

```
1. Schedule Trigger (mỗi 4h)
2. Đọc Sheet Admin → Tab "Config" → Lấy danh sách khách active
3. Loop từng khách:
   a. Lấy facebook_token, sheet_id, zalo_token, chat_id từ Config
   b. Đọc Sheet Khách (sheet_id) → Tab "Video TikTok" → Lấy video chưa đăng
   c. Nếu có video chưa đăng:
      - Download video từ TikWM
      - Upload Session (HTTP Request + facebook_token)
      - Upload video
      - Publish
      - Wait 30s → Check status
      - Nếu ready:
        - Update Sheet Khách (trạng thái = "thành công")
        - Đọc Tab "Link Shopee" → Comment links
        - Gửi thông báo Zalo (zalo_token + chat_id)
      - Nếu error:
        - Gửi thông báo lỗi Zalo
      - Nếu processing:
        - Wait 30s → Check lại
   d. Chuyển sang khách tiếp theo
```

## Rủi ro & Xử lý

| Rủi ro | Giải pháp |
|--------|-----------|
| 1 khách lỗi → ảnh hưởng khách khác | Wrap mỗi khách trong try/catch (Error Trigger node) |
| Facebook Token hết hạn | Cột "token_expiry" trong Config + workflow kiểm tra + alert |
| Quá nhiều khách → timeout | Chia batch: lần 1 chạy khách 1-10, lần 2 chạy 11-20 |
| Rate limit Facebook | Mỗi khách cách nhau 5 phút, giới hạn 1 video/khách/lần |
| Sheet Admin bị sửa nhầm | Protect Sheet, chỉ bạn có quyền edit |

## TODO: Refactor workflow

- [ ] Tạo Google Sheet Admin template
- [ ] Tạo Google Sheet Khách template
- [ ] Refactor workflow: thêm bước đọc Config + Loop
- [ ] Thay Facebook Graph API nodes → HTTP Request
- [ ] Thay Google Sheets nodes → dynamic Sheet ID
- [ ] Thay Zalo nodes → dynamic token
- [ ] Thêm error handling per customer
- [ ] Test với 2-3 khách thử
- [ ] Viết script tạo Sheet Khách tự động từ template
