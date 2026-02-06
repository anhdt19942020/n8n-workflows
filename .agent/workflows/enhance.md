---
description: Thêm hoặc cập nhật tính năng trong ứng dụng hiện có. Sử dụng cho phát triển lặp lại.
---

# /enhance - Cập Nhật Ứng Dụng

$ARGUMENTS

---

## Tác Vụ

Lệnh này thêm các tính năng hoặc thực hiện cập nhật cho ứng dụng hiện có.

### Các Bước:

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
   - Nếu là backend code (Laravel/Node.js/Python), tự động tạo commit message
   - Đọc `@[skills/git-commit-helper]` để tạo message chuẩn Conventional Commits
   - Phân tích thay đổi với `git diff --stat`
   - Đề xuất commit message dạng: `<type>(<scope>): <summary>`
   - Chờ người dùng xác nhận trước khi commit

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
