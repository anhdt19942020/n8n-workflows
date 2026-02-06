---
name: api-patterns
description: API design principles and decision-making. REST vs GraphQL vs tRPC selection, response formats, versioning, pagination.
allowed-tools: Read, Write, Edit, Glob, Grep
---

# API Patterns

> Các nguyên tắc thiết kế API và ra quyết định cho năm 2025.
> **Học cách TƯ DUY, đừng sao chép các mẫu cố định.**

## 🎯 Quy Tắc Đọc Chọn Lọc

**CHỈ đọc các file liên quan đến yêu cầu!** Kiểm tra bản đồ nội dung, tìm cái bạn cần.

---

## 📑 Bản Đồ Nội Dung (Content Map)

| File | Mô Tả | Khi Nào Đọc |
|------|-------|-------------|
| `api-style.md` | Cây quyết định REST vs GraphQL vs tRPC | Chọn loại API |
| `rest.md` | Đặt tên Resource, phương thức HTTP, status codes | Thiết kế REST API |
| `response.md` | Envelope pattern, định dạng lỗi, phân trang | Cấu trúc phản hồi |
| `graphql.md` | Thiết kế Schema, khi nào dùng, bảo mật | Cân nhắc GraphQL |
| `trpc.md` | TypeScript monorepo, an toàn kiểu (type safety) | Dự án TS fullstack |
| `versioning.md` | Versioning qua URI/Header/Query | Lên kế hoạch phát triển API |
| `auth.md` | JWT, OAuth, Passkey, API Keys | Chọn pattern xác thực |
| `rate-limiting.md` | Token bucket, sliding window | Bảo vệ API |
| `documentation.md` | Các thực hành tốt nhất OpenAPI/Swagger | Tài liệu hóa |
| `security-testing.md` | OWASP API Top 10, kiểm thử auth/authz | Kiểm toán bảo mật |

---

## 🔗 Các Skill Liên Quan

| Nhu Cầu | Skill |
|---------|-------|
| Triển khai API | `@[skills/backend-development]` |
| Cấu trúc dữ liệu | `@[skills/database-design]` |
| Chi tiết bảo mật | `@[skills/security-hardening]` |

---

## ✅ Checklist Quyết Định

Trước khi thiết kế một API:

- [ ] **Đã hỏi người dùng về các bên tiêu thụ API (API consumers)?**
- [ ] **Đã chọn phong cách API cho ngữ cảnh NÀY chưa?** (REST/GraphQL/tRPC)
- [ ] **Đã xác định định dạng phản hồi nhất quán chưa?**
- [ ] **Đã lên kế hoạch chiến lược phiên bản hóa (versioning)?**
- [ ] **Đã cân nhắc nhu cầu xác thực (authentication)?**
- [ ] **Đã lên kế hoạch giới hạn tốc độ (rate limiting)?**
- [ ] **Đã xác định cách tiếp cận tài liệu hóa?**

---

## ❌ Anti-Patterns (Các Mẫu Chống Chỉ Định)

**ĐỪNG (DON'T):**
- Mặc định chọn REST cho mọi thứ
- Dùng động từ trong các endpoint REST (/getUsers)
- Trả về định dạng phản hồi không nhất quán
- Để lộ lỗi nội bộ (internal errors) cho client
- Bỏ qua rate limiting

**NÊN (DO):**
- Chọn phong cách API dựa trên ngữ cảnh
- Hỏi về yêu cầu của client
- Tài liệu hóa kỹ lưỡng
- Sử dụng status codes phù hợp

---

## Script

| Script | Mục Đích | Lệnh |
|--------|----------|------|
| `scripts/api_validator.py` | Xác thực endpoint API | `python scripts/api_validator.py <project_path>` |
