---
description: Lệnh tạo ứng dụng mới. Kích hoạt skill App Builder và bắt đầu đối thoại tương tác với người dùng.
---

# /create - Tạo Ứng Dụng

$ARGUMENTS

> 🔴 **BẮT BUỘC (Khởi tạo Serena):**
> Trước khi thực hiện bất kỳ công việc nào trong lệnh này, Agent PHẢI:
>
> 1. Gọi \`mcp_serena_check_onboarding_performed\`
> 2. Gọi \`mcp_serena_activate_project\` với đường dẫn thư mục hiện tại.
> (Bỏ qua nếu Serena đã được kích hoạt trong phiên làm việc này).

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

## Tác Vụ

Lệnh này bắt đầu quy trình tạo ứng dụng mới.

### Các Bước

1. **Phân Tích Yêu Cầu**
   - Hiểu những gì người dùng muốn
   - Nếu thiếu thông tin, sử dụng skill `conversation-manager` để hỏi

2. **Lập Kế Hoạch Dự Án**
   - Sử dụng agent `project-planner` để phân rã công việc
   - Xác định tech stack (bộ công nghệ)
   - Lên kế hoạch cấu trúc file
   - Tạo file kế hoạch và tiến hành xây dựng

3. **Xây Dựng Ứng Dụng (Sau Khi Phê Duyệt)**
   - Điều phối với skill `app-builder`
   - Phối hợp các agent chuyên gia:
     - `database-architect` → Schema
     - `backend-specialist` → API
     - `frontend-specialist` → UI

4. **Xem Trước (Preview)**
   - Bắt đầu với `auto_preview.py` khi hoàn thành
   - Trình bày URL cho người dùng

---

## Ví Dụ Sử Dụng

```
/create blog site
/create e-commerce app with product listing and cart
/create todo app
/create Instagram clone
/create crm system with customer management
```

---

## Trước Khi Bắt Đầu

Nếu yêu cầu không rõ ràng, hãy đặt những câu hỏi sau:

- Loại ứng dụng là gì?
- Các tính năng cơ bản là gì?
- Ai sẽ sử dụng nó?

Sử dụng các giá trị mặc định, thêm chi tiết sau.
