# 4. Hướng dẫn Onboard Khách Hàng Mới

## Quy trình tổng quan

```
Khách liên hệ → Thu thập thông tin → Tạo Sheet → Thêm vào Config → Test → Bàn giao
     (1)              (2)                (3)           (4)          (5)      (6)
```

## Bước 1: Thu thập thông tin từ khách

### Gửi form cho khách điền (Google Form hoặc Zalo):

| Thông tin | Bắt buộc | Hướng dẫn cho khách |
|-----------|----------|---------------------|
| **Tên khách / Tên Page** | ✅ | Tên để quản lý |
| **Facebook Page Access Token** | ✅ | Xem hướng dẫn bên dưới |
| **Email Google** | ✅ | Để share Google Sheet |
| **Số điện thoại Zalo** | ✅ | Để thêm vào group + nhận thông báo |
| **Tần suất đăng** | ✅ | Mỗi 2h / 4h / 6h |
| **Link Shopee affiliate** | ❌ | Nếu có, điền vào Sheet sau |

### Hướng dẫn khách lấy Facebook Page Access Token

```
1. Truy cập: https://developers.facebook.com/tools/explorer/
2. Chọn ứng dụng (hoặc tạo mới)
3. Chọn "Get Page Access Token"
4. Chọn Page cần đăng video
5. Cấp quyền:
   - pages_manage_posts
   - pages_read_engagement
   - pages_show_list
   - publish_video
6. Copy token → Gửi cho bạn
```

> ⚠️ Token mặc định hết hạn sau 60 ngày.
> Để lấy token dài hạn (không hết hạn), dùng System User trong Business Manager.

### Hướng dẫn lấy Long-lived Token (khuyên dùng)

```
1. Lấy short-lived token từ Graph API Explorer (như trên)
2. Đổi sang long-lived token:
   GET https://graph.facebook.com/v23.0/oauth/access_token
     ?grant_type=fb_exchange_token
     &client_id={app-id}
     &client_secret={app-secret}
     &fb_exchange_token={short-lived-token}
3. Kết quả: long-lived user token (60 ngày)
4. Dùng user token để lấy page token (vĩnh viễn):
   GET https://graph.facebook.com/v23.0/me/accounts
     ?access_token={long-lived-user-token}
5. Page token trong response → vĩnh viễn (không hết hạn)
```

## Bước 2: Tạo Google Sheet cho khách

### Từ template, copy ra Sheet mới cho khách:

**Tab "Video TikTok":**

| Video Tiktok | Video Facebook | Trạng thái | Thời gian |
|--------------|---------------|------------|-----------|
| (khách dán link) | (auto fill) | (auto fill) | (auto fill) |

**Tab "Link Shopee":**

| Tên sản phẩm | Link |
|-------------|------|
| (khách điền) | (khách điền) |

### Set quyền:
- Share cho **email khách**: Editor
- Share cho **email Google của bạn (service account)**: Editor
- Đặt tên Sheet: `[Tên khách] - Bếp nhà Tool`

## Bước 3: Thêm khách vào Sheet Admin Config

Mở Sheet Admin → Tab "Config" → Thêm 1 dòng mới:

| Tên khách | facebook_token | sheet_id | zalo_token | chat_id | interval | status | token_expiry | ghi_chu |
|-----------|---------------|----------|------------|---------|----------|--------|-------------|---------|
| Khách X | EAABx... | 1abc2d... | bot123... | 456... | 4 | active | 2026-05-15 | |

### Giải thích các cột:

| Cột | Mô tả |
|-----|--------|
| `ten_khach` | Tên hiển thị |
| `facebook_token` | Page Access Token (long-lived) |
| `sheet_id` | Google Sheet ID của khách (lấy từ URL) |
| `zalo_token` | Zalo Bot Token |
| `chat_id` | Zalo Chat ID nhận thông báo |
| `interval` | Tần suất đăng (giờ): 2, 4, 6... |
| `status` | `active` hoặc `paused` |
| `token_expiry` | Ngày token hết hạn (để nhắc renew) |
| `ghi_chu` | Ghi chú tùy ý |

### Cách lấy Sheet ID từ URL:

```
URL: https://docs.google.com/spreadsheets/d/1sym6y6jbEinNUN8MiGY03-hRLpQIAY4yqnSFTTdNNvM/edit
                                              ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
                                              ĐÂY LÀ SHEET ID
```

## Bước 4: Test

1. Khách dán 1-2 link TikTok vào Sheet
2. Chạy workflow thủ công (Execute Workflow trong n8n)
3. Kiểm tra:
   - Video có upload lên Facebook không?
   - Status có update trên Sheet không?
   - Zalo có nhận được thông báo không?
   - Comment Shopee có đúng không?
4. Nếu OK → Bật Schedule Trigger

## Bước 5: Bàn giao cho khách

Gửi cho khách:
- [ ] Link Google Sheet của họ
- [ ] Hướng dẫn cách dán link TikTok vào Sheet
- [ ] Hướng dẫn cách thêm link Shopee
- [ ] Thông tin group hỗ trợ Zalo
- [ ] Lịch nhắc renew token (nếu dùng token 60 ngày)

## Template tin nhắn bàn giao

```
Chào anh/chị [Tên],

Tool đăng video tự động đã được kích hoạt cho Page [Tên Page]. 

📋 Google Sheet của anh/chị: [Link Sheet]

Cách sử dụng:
1. Mở Sheet → Tab "Video TikTok"
2. Dán link video TikTok vào cột "Video Tiktok"
3. Hệ thống sẽ tự động đăng mỗi [X] giờ
4. Kết quả sẽ hiển thị ở cột "Trạng thái" và "Video Facebook"
5. Thông báo sẽ được gửi qua Zalo

Nếu muốn comment link Shopee:
1. Mở Tab "Link Shopee"
2. Điền tên sản phẩm + link

⚠️ Token Facebook sẽ hết hạn vào [Ngày]. Tôi sẽ liên hệ trước để renew.

Mọi thắc mắc liên hệ: [SĐT/Zalo]
```
