---
description: Brainstorming có cấu trúc cho dự án và tính năng. Khám phá nhiều phương án trước khi triển khai.
---

# /brainstorm - Khám Phá Ý Tưởng Có Cấu Trúc

$ARGUMENTS

> 🔴 **BẮT BUỘC (Khởi tạo Serena):**
> Trước khi thực hiện bất kỳ công việc nào trong lệnh này, Agent PHẢI:
> 1. Gọi \`mcp_serena_check_onboarding_performed\`
> 2. Gọi \`mcp_serena_activate_project\` với đường dẫn thư mục hiện tại.
> (Bỏ qua nếu Serena đã được kích hoạt trong phiên làm việc này).


## Mục Đích

Lệnh này kích hoạt chế độ BRAINSTORM để khám phá ý tưởng có cấu trúc. Sử dụng khi bạn cần khám phá các lựa chọn trước khi cam kết triển khai.

---

## Hành Vi

Khi `/brainstorm` được kích hoạt:

1. **Hiểu mục tiêu**
   - Vấn đề chúng ta đang giải quyết là gì?
   - Người dùng là ai?
   - Những ràng buộc nào tồn tại?

2. **Tạo các phương án**
   - Cung cấp ít nhất 3 cách tiếp cận khác nhau
   - Mỗi phương án có ưu và nhược điểm
   - Cân nhắc các giải pháp độc đáo/phi truyền thống

3. **So sánh và đề xuất**
   - Tóm tắt các sự đánh đổi (tradeoffs)
   - Đưa ra đề xuất kèm lý do

---

## Định Dạng Đầu Ra

```markdown
## 🧠 Brainstorm: [Chủ đề]

### Bối cảnh
[Mô tả vấn đề ngắn gọn]

---

### Phương án A: [Tên]
[Mô tả]

✅ **Ưu điểm:**
- [lợi ích 1]
- [lợi ích 2]

❌ **Nhược điểm:**
- [hạn chế 1]

📊 **Nỗ lực:** Thấp | Trung bình | Cao

---

### Phương án B: [Tên]
[Mô tả]

✅ **Ưu điểm:**
- [lợi ích 1]

❌ **Nhược điểm:**
- [hạn chế 1]
- [hạn chế 2]

📊 **Nỗ lực:** Thấp | Trung bình | Cao

---

### Phương án C: [Tên]
[Mô tả]

✅ **Ưu điểm:**
- [lợi ích 1]

❌ **Nhược điểm:**
- [hạn chế 1]

📊 **Nỗ lực:** Thấp | Trung bình | Cao

---

## 💡 Đề Xuất

**Phương án [X]** vì [lý do].

Bạn muốn khám phá theo hướng nào?
```

---

## Ví dụ

```
/brainstorm hệ thống xác thực
/brainstorm quản lý trạng thái cho form phức tạp
/brainstorm thiết kế schema database cho ứng dụng xã hội
/brainstorm chiến lược caching
```

---

## Nguyên Tắc Chính

- **Không code** - đây là về ý tưởng, không phải triển khai
- **Trực quan khi hữu ích** - sử dụng sơ đồ cho kiến trúc
- **Trung thực về đánh đổi** - không giấu giếm sự phức tạp
- **Tôn trọng người dùng** - trình bày các lựa chọn, để họ quyết định

