# 6. Mô hình Kinh doanh

## Bảng giá gợi ý

| Gói | Số Page | Video/ngày | Comment Shopee | Thông báo Zalo | Giá/tháng |
|-----|---------|------------|----------------|---------------|-----------|
| **Basic** | 1 Page | 4 video | ❌ | ✅ | 200,000đ |
| **Pro** | 3 Page | 6 video/page | ✅ (5 link) | ✅ | 500,000đ |
| **Premium** | 10 Page | 10 video/page | ✅ (unlimited) | ✅ | 1,500,000đ |

### Phí khác

| Phí | Giá | Ghi chú |
|-----|-----|---------|
| Setup ban đầu | 300,000đ - 500,000đ | 1 lần duy nhất |
| Renew token (làm hộ) | 100,000đ | ~2 tháng/lần (nếu không dùng permanent token) |
| Thêm Page ngoài gói | 100,000đ/page/tháng | |
| Custom workflow | Thỏa thuận | Thêm tính năng riêng |

## Chi phí vận hành

| Hạng mục | Chi phí/tháng | Ghi chú |
|----------|--------------|---------|
| VPS 2GB (Contabo) | ~120,000đ | Đủ cho 20 khách |
| VPS 4GB (Contabo) | ~240,000đ | Đủ cho 100 khách |
| Domain .com | ~25,000đ/tháng | (~300k/năm) |
| SSL | Miễn phí | Let's Encrypt |
| Google Sheets API | Miễn phí | Quota mặc định đủ dùng |
| TikWM API | Miễn phí | Third-party, có thể thay đổi |
| **Tổng (20 khách)** | **~150,000đ** | |
| **Tổng (100 khách)** | **~270,000đ** | |

## Ước tính doanh thu

### Kịch bản 1: 10 khách Basic

| | Số liệu |
|--|---------|
| Doanh thu | 10 × 200k = **2,000,000đ/tháng** |
| Chi phí server | 120,000đ |
| **Lợi nhuận** | **~1,880,000đ/tháng** |
| Biên lợi nhuận | 94% |

### Kịch bản 2: 30 khách hỗn hợp

| Gói | Số khách | Doanh thu |
|-----|----------|-----------|
| Basic | 20 | 4,000,000đ |
| Pro | 8 | 4,000,000đ |
| Premium | 2 | 3,000,000đ |
| **Tổng** | **30** | **11,000,000đ/tháng** |
| Chi phí | | 240,000đ |
| **Lợi nhuận** | | **~10,760,000đ/tháng** |

### Kịch bản 3: 100 khách

| Gói | Số khách | Doanh thu |
|-----|----------|-----------|
| Basic | 60 | 12,000,000đ |
| Pro | 30 | 15,000,000đ |
| Premium | 10 | 15,000,000đ |
| **Tổng** | **100** | **42,000,000đ/tháng** |
| Chi phí | | 500,000đ |
| **Lợi nhuận** | | **~41,500,000đ/tháng** |

## Kênh bán hàng

| Kênh | Cách tiếp cận | Chi phí |
|------|--------------|---------|
| Group Facebook MMO | Đăng bài + video demo | Miễn phí |
| Group Affiliate Marketing | Chia sẻ case study | Miễn phí |
| Zalo Group kiếm tiền online | Giới thiệu tool | Miễn phí |
| YouTube | Video hướng dẫn + demo | Miễn phí |
| TikTok | Short video giới thiệu | Miễn phí |
| Referral (giới thiệu) | Chiết khấu 20% tháng đầu | Mất 20% doanh thu |

## Roadmap phát triển sản phẩm

### Q1: MVP (Tháng 1-2)
- [x] Workflow "Bếp nhà" hoạt động
- [ ] Refactor sang Master Workflow + Config Sheet
- [ ] Setup VPS production
- [ ] 5-10 khách đầu tiên
- [ ] Thu thập feedback

### Q2: Tối ưu (Tháng 3-4)
- [ ] Auto token refresh (permanent token)
- [ ] Dashboard monitoring đơn giản
- [ ] Thêm tính năng: đăng YouTube Shorts
- [ ] Thêm tính năng: đăng Instagram Reels
- [ ] 30-50 khách

### Q3: Scale (Tháng 5-6)
- [ ] Build web dashboard cho khách tự quản lý
- [ ] Tích hợp payment (Momo/VNPay)
- [ ] Analytics per customer
- [ ] API public
- [ ] 100+ khách

## Rủi ro kinh doanh

| Rủi ro | Xác suất | Ảnh hưởng | Giải pháp |
|--------|---------|-----------|-----------|
| Facebook thay đổi API | Trung bình | Cao | Theo dõi changelog, update nhanh |
| TikWM ngừng hoạt động | Trung bình | Trung bình | Backup: SnapTik, yt-dlp self-host |
| Khách bị block Page | Thấp | Thấp (per khách) | Giới hạn tần suất, disclaimer |
| Vi phạm bản quyền | Trung bình | Cao | Disclaimer, chỉ repost video sở hữu |
| Cạnh tranh | Cao | Trung bình | Giá cạnh tranh, hỗ trợ tốt, thêm tính năng |
