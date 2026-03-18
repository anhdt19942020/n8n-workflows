---
description: Thêm hoặc cập nhật tính năng trong ứng dụng hiện có. Sử dụng cho phát triển lặp lại.
---

# /enhance - Cập Nhật Ứng Dụng

$ARGUMENTS

> 🔴 **BẮT BUỘC (Khởi tạo Serena):**
> Trước khi thực hiện bất kỳ công việc nào trong lệnh này, Agent PHẢI:
>
> 1. Gọi \`mcp_serena_check_onboarding_performed\`
> 2. Gọi \`mcp_serena_activate_project\` với đường dẫn thư mục hiện tại.
> (Bỏ qua nếu Serena đã được kích hoạt trong phiên làm việc này).

## Tác Vụ

Lệnh này thêm các tính năng hoặc thực hiện cập nhật cho ứng dụng hiện có.

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

### Các Bước

1. **Hiểu Trạng Thái Hiện Tại**
   - Tải trạng thái dự án với `session_manager.py`
   - Hiểu các tính năng hiện có, tech stack

2. **Lập Kế Hoạch Thay Đổi**
   - Xác định những gì sẽ được thêm/thay đổi
   - Phát hiện các file bị ảnh hưởng
   - Kiểm tra dependencies

3. **Trình Bày Kế Hoạch Cho Người Dùng** (cho các thay đổi lớn)

   ```
   "Để thêm admin panel:
   - Tôi sẽ tạo 15 file mới
   - Cập nhật 8 file
   - Mất khoảng 10 phút
   
   Tôi có nên bắt đầu không?"
   ```

4. **Áp Dụng**
   - Gọi các agent liên quan
   - Thực hiện thay đổi
   - Test

5. **Cập Nhật Preview**
   - Hot reload hoặc khởi động lại

6. **Generate Git Commit Message** (Chỉ Backend)
   - Nếu là backend code (Laravel/Node.js/Python), **TỰ ĐỘNG** tạo commit message — KHÔNG HỎI người dùng có muốn tạo hay không
   - Đọc `@[skills/git-commit-helper]` để tạo message chuẩn Conventional Commits
   - Phân tích thay đổi với `git diff --stat`
   - Đề xuất lệnh commit dạng: `git commit -m "<type>(<scope>): <summary>"`
   - Người dùng sẽ tự xác nhận khi chạy lệnh

---

## Ví Dụ Sử Dụng

```
/enhance add dark mode
/enhance build admin panel
/enhance integrate payment system
/enhance add search feature
/enhance edit profile page
/enhance make responsive
```

---

## Cảnh Báo

- Cần sự chấp thuận cho các thay đổi lớn
- Cảnh báo về các yêu cầu xung đột (ví dụ: "dùng Firebase" khi dự án dùng PostgreSQL)
- Commit mỗi thay đổi với git
- Backend: Tự động tạo commit message sau khi code xong
