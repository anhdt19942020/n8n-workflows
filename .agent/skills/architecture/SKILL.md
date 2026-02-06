---
name: architecture
description: Architectural decision-making framework. Requirements analysis, trade-off evaluation, ADR documentation. Use when making architecture decisions or analyzing system design.
allowed-tools: Read, Glob, Grep
---

# Khung Quyết Định Kiến Trúc (Architecture Decision Framework)

> "Yêu cầu định hướng kiến trúc. Sự đánh đổi thông báo quyết định. ADRs ghi lại lý do."

## 🎯 Quy Tắc Đọc Chọn Lọc

**CHỈ đọc các file liên quan đến yêu cầu!** Kiểm tra bản đồ nội dung, tìm cái bạn cần.

| File | Mô Tả | Khi Nào Đọc |
|------|-------|-------------|
| `context-discovery.md` | Các câu hỏi cần hỏi, phân loại dự án | Bắt đầu thiết kế kiến trúc |
| `trade-off-analysis.md` | Mẫu ADR, khung đánh đổi (trade-off) | Ghi lại quyết định |
| `pattern-selection.md` | Cây quyết định, anti-patterns | Chọn patterns |
| `examples.md` | Ví dụ MVP, SaaS, Enterprise | Triển khai tham khảo |
| `patterns-reference.md` | Tra cứu nhanh patterns | So sánh pattern |

---

## 🔗 Các Skill Liên Quan

| Skill | Dùng Cho |
|-------|----------|
| `@[skills/database-design]` | Thiết kế schema cơ sở dữ liệu |
| `@[skills/api-patterns]` | Các mẫu thiết kế API |
| `@[skills/deployment-procedures]` | Kiến trúc deployment |

---

## Nguyên Tắc Cốt Lõi

**"Đơn giản là đỉnh cao của sự tinh tế."**

- Bắt đầu đơn giản
- Thêm sự phức tạp CHỈ KHI đã chứng minh được là cần thiết
- Bạn luôn có thể thêm patterns sau
- Loại bỏ sự phức tạp KHÓ HƠN NHIỀU so với thêm vào

---

## Checklist Xác Thực

Trước khi chốt kiến trúc:

- [ ] Yêu cầu đã được hiểu rõ ràng
- [ ] Các ràng buộc đã được xác định
- [ ] Mỗi quyết định đều có phân tích đánh đổi (trade-off)
- [ ] Các phương án đơn giản hơn đã được xem xét
- [ ] ADRs đã được viết cho các quyết định quan trọng
- [ ] Chuyên môn của team phù hợp với patterns đã chọn
