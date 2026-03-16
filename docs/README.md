# 📚 n8n-workflows Documentation

> Tài liệu dự án tự động hóa đăng video TikTok → Facebook Reels + Comment Shopee Affiliate.

## Mục lục

| Tài liệu | Mô tả |
|-----------|--------|
| [1. Tổng quan Workflow](./01-workflow-overview.md) | Workflow "Bếp nhà" làm gì, luồng hoạt động chi tiết |
| [2. Kiến trúc Multi-tenant](./02-architecture.md) | Phương án phục vụ nhiều khách trên 1 server |
| [3. Hướng dẫn Setup Server](./03-server-setup.md) | Cài đặt VPS, Docker, n8n, domain |
| [4. Hướng dẫn Onboard Khách](./04-customer-onboarding.md) | Quy trình thêm khách mới, thu thập thông tin |
| [5. Google Sheet Template](./05-google-sheet-template.md) | Cấu trúc Sheet Admin + Sheet Khách |
| [6. Mô hình Kinh doanh](./06-business-model.md) | Bảng giá, doanh thu, chi phí |

## Quick Start

```bash
# Yêu cầu: Node.js >= 22.16, Docker (cho production)
nvm use 22
npx -y n8n@latest
# Mở http://localhost:5678
```

## Tech Stack

- **n8n** v2.11+ — Workflow automation
- **Facebook Graph API** v23.0 — Upload Reels, Comment
- **Google Sheets API** — Config store + Data management
- **TikWM API** — Download TikTok video
- **Zalo Bot API** — Thông báo kết quả
