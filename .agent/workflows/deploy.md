---
description: Lệnh deploy cho production. Kiểm tra trước khi deploy và thực thi deployment.
---

# /deploy - Triển Khai Production

$ARGUMENTS

---

## Mục Đích

Lệnh này xử lý việc deploy production với các kiểm tra trước khi deploy (pre-flight checks), thực thi deploy và xác minh.

---

## Các Lệnh Con (Sub-commands)

```
/deploy            - Trình hướng dẫn deploy tương tác
/deploy check      - Chỉ chạy kiểm tra trước khi deploy
/deploy preview    - Deploy lên preview/staging
/deploy production - Deploy lên production
/deploy rollback   - Rollback về phiên bản trước
```

---

## Danh Sách Kiểm Tra Trước Khi Deploy

Trước bất kỳ lần deploy nào:

```markdown
## 🚀 Pre-Deploy Checklist

### Chất lượng Code
- [ ] Không có lỗi TypeScript (`npx tsc --noEmit`)
- [ ] ESLint passing (`npx eslint .`)
- [ ] Tất cả test đều qua (`npm test`)

### Bảo mật
- [ ] Không có secrets hardcoded
- [ ] Biến môi trường được tài liệu hóa
- [ ] Các phụ thuộc (dependencies) đã được kiểm toán (`npm audit`)

### Hiệu năng
- [ ] Kích thước bundle chấp nhận được
- [ ] Không có câu lệnh console.log
- [ ] Hình ảnh được tối ưu hóa

### Tài liệu
- [ ] README được cập nhật
- [ ] CHANGELOG được cập nhật
- [ ] API docs hiện hành

### Sẵn sàng deploy? (y/n)
```

---

## Quy Trình Deployment

```
┌─────────────────┐
│  /deploy        │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Kiểm tra       │
│  Pre-flight     │
└────────┬────────┘
         │
    Qua? ──Ko──► Sửa lỗi
         │
        Có
         │
         ▼
┌─────────────────┐
│  Build          │
│  ứng dụng       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Deploy lên     │
│  nền tảng       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Check health   │
│  & xác minh     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  ✅ Hoàn tất    │
└─────────────────┘
```

---

## Định Dạng Đầu Ra

### Deploy Thành Công

```markdown
## 🚀 Deployment Complete

### Tổng hợp
- **Phiên bản:** v1.2.3
- **Môi trường:** production
- **Thời gian:** 47 giây
- **Nền tảng:** Vercel

### URLs
- 🌐 Production: https://app.example.com
- 📊 Dashboard: https://vercel.com/project

### Những Thay Đổi
- Đã thêm tính năng hồ sơ người dùng
- Sửa lỗi đăng nhập
- Cập nhật dependencies

### Kiểm Tra Sức Khỏe (Health Check)
✅ API phản hồi (200 OK)
✅ Database đã kết nối
✅ Tất cả dịch vụ khỏe mạnh
```

### Deploy Thất Bại

```markdown
## ❌ Deployment Failed

### Lỗi
Build thất bại tại bước: TypeScript compilation

### Chi tiết
```
error TS2345: Argument of type 'string' is not assignable...
```

### Cách Giải Quyết
1. Sửa lỗi TypeScript trong `src/services/user.ts:45`
2. Chạy `npm run build` cục bộ để xác minh
3. Thử `/deploy` lại

### Có Thể Rollback
Phiên bản trước (v1.2.2) vẫn đang hoạt động.
Chạy `/deploy rollback` nếu cần.
```

---

## Hỗ Trợ Nền Tảng

| Nền Tảng | Lệnh | Ghi Chú |
|----------|------|---------|
| Vercel | `vercel --prod` | Tự động phát hiện cho Next.js |
| Railway | `railway up` | Cần Railway CLI |
| Fly.io | `fly deploy` | Cần flyctl |
| Docker | `docker compose up -d` | Cho self-hosted |

---

## Ví Dụ

```
/deploy
/deploy check
/deploy preview
/deploy production --skip-tests
/deploy rollback
```
