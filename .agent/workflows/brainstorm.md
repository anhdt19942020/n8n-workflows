---
description: Brainstorming có cấu trúc cho dự án và tính năng. Khám phá nhiều phương án trước khi triển khai.
---

# /brainstorm - Khám Phá Ý Tưởng Có Cấu Trúc

$ARGUMENTS

> 🔴 **BẮT BUỘC (Khởi tạo Serena):**
> Trước khi thực hiện bất kỳ công việc nào trong lệnh này, Agent PHẢI:
>
> 1. Gọi `mcp_serena_check_onboarding_performed`
> 2. Gọi `mcp_serena_activate_project` với đường dẫn thư mục hiện tại
> (Bỏ qua nếu Serena đã được kích hoạt trong phiên làm việc này)

---

## Mục Đích

Lệnh này kích hoạt chế độ BRAINSTORM để khám phá ý tưởng có cấu trúc trước khi cam kết triển khai.

Sử dụng khi cần:

- khám phá nhiều phương án cho một dự án, tính năng, kiến trúc hoặc chiến lược
- hiểu rõ các tradeoff trước khi quyết định
- làm rõ bài toán còn mơ hồ
- tìm hướng đi phù hợp với bối cảnh dự án hiện tại

---

## Phối Hợp Với Sequential Thinking

Workflow này **có thể** sử dụng Sequential Thinking để làm rõ bài toán trước khi sinh phương án.

### Khi nên dùng Sequential Thinking

Agent nên dùng Sequential Thinking nếu có một trong các dấu hiệu sau:

- bài toán còn mơ hồ hoặc thiếu phạm vi rõ ràng
- có nhiều ràng buộc kỹ thuật, thời gian, vận hành hoặc bảo trì
- có nhiều hơn một hướng tiếp cận hợp lý
- chủ đề liên quan đến kiến trúc, refactor lớn, chiến lược hệ thống, hoặc quyết định dài hạn
- cần bóc tách tiêu chí đánh giá trước khi đề xuất phương án

### Khi không cần dùng Sequential Thinking

Agent có thể bỏ qua nếu:

- câu hỏi nhỏ và phạm vi rất rõ
- chỉ cần liệt kê nhanh vài ý tưởng đơn giản
- không có tradeoff quan trọng cần phân tích

### Vai trò của Sequential Thinking trong workflow này

Nếu được dùng, Sequential Thinking chỉ có nhiệm vụ:

- làm rõ vấn đề thật sự cần giải
- tách mục tiêu, ràng buộc và giả định
- xác định tiêu chí đánh giá phương án
- đảm bảo các phương án khác nhau thực sự

Sequential Thinking **không** thay thế workflow này.  
Output cuối cùng vẫn phải theo đúng định dạng của `/brainstorm`.

---

## Hành Vi

Khi `/brainstorm` được kích hoạt, Agent phải làm theo thứ tự sau:

### 1. Hiểu mục tiêu

- Vấn đề chúng ta đang giải quyết là gì?
- Người dùng hoặc đối tượng bị tác động là ai?
- Những ràng buộc nào đang tồn tại?
- Thành công sẽ được đo bằng điều gì?

### 2. Tạo các phương án

- Cung cấp ít nhất 3 cách tiếp cận khác nhau
- Mỗi phương án phải khác nhau về chiến lược, không chỉ khác chi tiết nhỏ
- Mỗi phương án cần có ưu và nhược điểm rõ ràng
- Cân nhắc ít nhất 1 phương án phi truyền thống nếu phù hợp với bối cảnh

### 3. So sánh và đề xuất

- Tóm tắt các tradeoff chính giữa các phương án
- Đưa ra đề xuất kèm lý do
- Nếu chưa đủ dữ liệu để chốt, phải nói rõ điều gì còn thiếu

---

## Guardrails

- **Không code** — đây là giai đoạn khám phá ý tưởng, không phải triển khai
- **Không đi quá sâu vào implementation detail**
- **Không giả vờ chắc chắn khi còn thiếu thông tin**
- **Không tạo các phương án quá giống nhau**
- **Không đề xuất chỉ vì giải pháp nghe “xịn” hoặc “hiện đại”**
- **Ưu tiên phương án phù hợp với bối cảnh dự án**
- **Giới hạn mặc định 3–4 phương án để tránh lan man**
- **Nếu dùng sơ đồ, chỉ dùng khi thực sự giúp hiểu rõ hơn**

---

## Định Dạng Đầu Ra

```markdown
## 🧠 Brainstorm: [Chủ đề]

### Bối cảnh
[Mô tả vấn đề ngắn gọn]

### Mục tiêu
- [mục tiêu 1]
- [mục tiêu 2]

### Ràng buộc chính
- [ràng buộc 1]
- [ràng buộc 2]

---

### Phương án A: [Tên]
[Mô tả]

✅ **Ưu điểm:**
- [lợi ích 1]
- [lợi ích 2]

❌ **Nhược điểm:**
- [hạn chế 1]

📊 **Nỗ lực:** Thấp | Trung bình | Cao  
🧩 **Phù hợp khi:** [bối cảnh phù hợp]

---

### Phương án B: [Tên]
[Mô tả]

✅ **Ưu điểm:**
- [lợi ích 1]

❌ **Nhược điểm:**
- [hạn chế 1]
- [hạn chế 2]

📊 **Nỗ lực:** Thấp | Trung bình | Cao  
🧩 **Phù hợp khi:** [bối cảnh phù hợp]

---

### Phương án C: [Tên]
[Mô tả]

✅ **Ưu điểm:**
- [lợi ích 1]

❌ **Nhược điểm:**
- [hạn chế 1]

📊 **Nỗ lực:** Thấp | Trung bình | Cao  
🧩 **Phù hợp khi:** [bối cảnh phù hợp]

---

## ⚖️ So sánh nhanh
- **Nhanh nhất để triển khai:** [A/B/C]
- **Dễ bảo trì nhất:** [A/B/C]
- **Linh hoạt nhất về sau:** [A/B/C]
- **Ít rủi ro nhất:** [A/B/C]

## 💡 Đề Xuất

**Phương án [X]** vì [lý do].

### Điều cần xác nhận tiếp
- [nếu có]

Bạn muốn khám phá theo hướng nào?
