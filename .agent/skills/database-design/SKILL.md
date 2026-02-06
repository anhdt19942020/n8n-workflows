---
name: database-design
description: Database design principles and decision-making. Schema design, indexing strategy, ORM selection, serverless databases.
allowed-tools: Read, Write, Edit, Glob, Grep
---

# Thiết Kế Cơ Sở Dữ Liệu (Database Design)

> **Học cách TƯ DUY, đừng sao chép các mẫu SQL.**

## 🎯 Quy Tắc Đọc Chọn Lọc

**CHỈ đọc các file liên quan đến yêu cầu!** Kiểm tra bản đồ nội dung, tìm cái bạn cần.

| File | Mô Tả | Khi Nào Đọc |
|------|-------|-------------|
| `database-selection.md` | PostgreSQL vs Neon vs Turso vs SQLite | Chọn cơ sở dữ liệu |
| `orm-selection.md` | Drizzle vs Prisma vs Kysely | Chọn ORM |
| `schema-design.md` | Chuẩn hóa, PKs, quan hệ (relationships) | Thiết kế schema |
| `indexing.md` | Các loại Index, composite indexes | Tinh chỉnh hiệu năng |
| `optimization.md` | N+1, EXPLAIN ANALYZE | Tối ưu truy vấn |
| `migrations.md` | Migrations an toàn, serverless DBs | Thay đổi schema |

---

## ⚠️ Nguyên Tắc Cốt Lõi

- HỎI người dùng về sở thích database nếu không rõ ràng
- Chọn database/ORM dựa trên NGỮ CẢNH
- Đừng mặc định dùng PostgreSQL cho mọi thứ

---

## Checklist Quyết Định

Trước khi thiết kế schema:

- [ ] Đã hỏi người dùng về sở thích database chưa?
- [ ] Đã chọn database cho ngữ cảnh NÀY chưa?
- [ ] Đã cân nhắc môi trường deployment chưa?
- [ ] Đã lên kế hoạch chiến lược index chưa?
- [ ] Đã xác định các loại quan hệ chưa?

---

## Anti-Patterns

❌ Mặc định dùng PostgreSQL cho app đơn giản (SQLite có thể là đủ)
❌ Bỏ qua việc đánh index
❌ Dùng SELECT * trong môi trường production
❌ Lưu JSON khi dữ liệu có cấu trúc thì tốt hơn
❌ Phớt lờ truy vấn N+1
