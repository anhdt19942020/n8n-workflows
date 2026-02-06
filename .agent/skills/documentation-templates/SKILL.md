---
name: documentation-templates
description: Documentation templates and structure guidelines. README, API docs, code comments, and AI-friendly documentation.
allowed-tools: Read, Glob, Grep
---

# Template Tài Liệu (Documentation Templates)

> Template và hướng dẫn cấu trúc cho các loại tài liệu phổ biến.

---

## 1. Cấu Trúc README

### Các Phần Thiết Yếu (Thứ Tự Ưu Tiên)

| Phần | Mục Đích |
|------|----------|
| **Tiêu đề + One-liner** | Đây là cái gì? |
| **Bắt Đầu Nhanh** | Chạy trong <5 phút |
| **Tính Năng** | Tôi có thể làm gì? |
| **Cấu Hình** | Cách tùy chỉnh |
| **Tham Khảo API** | Link đến tài liệu chi tiết |
| **Đóng Góp** | Cách giúp đỡ |
| **Giấy Phép** | Pháp lý |

### Template README

```markdown
# Tên Dự Án

Mô tả ngắn gọn một dòng.

## Bắt Đầu Nhanh

[Các bước tối thiểu để chạy]

## Tính Năng

- Tính năng 1
- Tính năng 2

## Cấu Hình

| Biến | Mô Tả | Mặc Định |
|------|-------|----------|
| PORT | Cổng Server | 3000 |

## Tài Liệu

- [Tham Khảo API](./docs/api.md)
- [Kiến Trúc](./docs/architecture.md)

## Giấy Phép

MIT
```

---

## 2. Cấu Trúc Tài Liệu API

### Template Cho Mỗi Endpoint

```markdown
## GET /users/:id

Lấy thông tin người dùng theo ID.

**Tham số:**
| Tên | Kiểu | Bắt buộc | Mô tả |
|-----|------|----------|-------|
| id | string | Có | User ID |

**Phản hồi:**
- 200: Object người dùng
- 404: Người dùng không tồn tại

**Ví dụ:**
[Ví dụ Request và Response]
```

---

## 3. Hướng Dẫn Comment Code

### Template JSDoc/TSDoc

```typescript
/**
 * Mô tả ngắn gọn về những gì hàm thực hiện.
 * 
 * @param paramName - Mô tả tham số
 * @returns Mô tả giá trị trả về
 * @throws ErrorType - Khi lỗi này xảy ra
 * 
 * @example
 * const result = functionName(input);
 */
```

### Khi Nào Comment

| ✅ Comment | ❌ Đừng Comment |
|------------|-----------------|
| Tại sao (logic nghiệp vụ) | Cái gì (quá hiển nhiên) |
| Thuật toán phức tạp | Mỗi dòng code |
| Hành vi không rõ ràng | Code tự giải thích |
| Các hợp đồng API | Chi tiết triển khai |

---

## 4. Template Nhật Ký Thay Đổi (Keep a Changelog)

```markdown
# Changelog

## [Unreleased]
### Added
- Tính năng mới

## [1.0.0] - 2025-01-01
### Added
- Phát hành ban đầu
### Changed
- Cập nhật dependency
### Fixed
- Sửa lỗi
```

---

## 5. Bản Ghi Quyết Định Kiến Trúc (ADR)

```markdown
# ADR-001: [Tiêu Đề]

## Trạng Thái
Accepted (Chấp nhận) / Deprecated (Lỗi thời) / Superseded (Bị thay thế)

## Ngữ Cảnh
Tại sao chúng ta đưa ra quyết định này?

## Quyết Định
Chúng ta đã quyết định gì?

## Hậu Quả
Các sự đánh đổi (trade-offs) là gì?
```

---

## 6. Tài Liệu Thân Thiện Với AI (2025)

### Template llms.txt

Dành cho AI crawlers và agents:

```markdown
# Tên Dự Án
> Mục tiêu một dòng.

## Các File Cốt Lõi
- [src/index.ts]: Entry chính
- [src/api/]: Các route API
- [docs/]: Tài liệu

## Các Khái Niệm Chính
- Concept 1: Giải thích ngắn gọn
- Concept 2: Giải thích ngắn gọn
```

### Tài Liệu Sẵn Sàng Cho MCP

Để index cho RAG:
- Phân cấp H1-H3 rõ ràng
- Ví dụ JSON/YAML cho các cấu trúc dữ liệu
- Sơ đồ Mermaid cho các luồng (flows)
- Các section tự chứa (self-contained)

---

## 7. Các Nguyên Tắc Cấu Trúc

| Nguyên Tắc | Tại Sao |
|------------|---------|
| **Dễ quét (Scannable)** | Headers, danh sách, bảng biểu |
| **Ví dụ trước** | Show, don't just tell |
| **Chi tiết lũy tiến** | Đơn giản → Phức tạp |
| **Cập nhật** | Lỗi thời = gây hiểu lầm |

---

> **Ghi nhớ:** Template là điểm khởi đầu. Hãy thích nghi theo nhu cầu dự án của bạn.
