---
description: Display agent and project status. Progress tracking and status board.
---

# /status - Hiển Thị Trạng Thái

$ARGUMENTS

> 🔴 **BẮT BUỘC (Khởi tạo Serena):**
> Trước khi thực hiện bất kỳ công việc nào trong lệnh này, Agent PHẢI:
> 1. Gọi \`mcp_serena_check_onboarding_performed\`
> 2. Gọi \`mcp_serena_activate_project\` với đường dẫn thư mục hiện tại.
> (Bỏ qua nếu Serena đã được kích hoạt trong phiên làm việc này).


## Tác Vụ

Hiển thị trạng thái dự án và agent hiện tại.

### Những Gì Nó Hiển Thị

1. **Thông Tin Dự Án**
   - Tên dự án và đường dẫn
   - Tech stack
   - Các tính năng hiện tại

2. **Bảng Trạng Thái Agent**
   - Agent nào đang chạy
   - Tác vụ nào đã hoàn thành
   - Công việc đang chờ xử lý

3. **Thống Kê File**
   - Số lượng file đã tạo
   - Số lượng file đã sửa đổi

4. **Trạng Thái Preview**
   - Server có đang chạy không
   - URL
   - Kiểm tra sức khỏe (Health check)

---

## Ví Dụ Đầu Ra

```
=== Project Status ===

📁 Project: my-ecommerce
📂 Path: C:/projects/my-ecommerce
🏷️ Type: nextjs-ecommerce
📊 Status: active

🔧 Tech Stack:
   Framework: next.js
   Database: postgresql
   Auth: clerk
   Payment: stripe

✅ Features (5):
   • product-listing
   • cart
   • checkout
   • user-auth
   • order-history

⏳ Pending (2):
   • admin-panel
   • email-notifications

📄 Files: 73 created, 12 modified

=== Agent Status ===

✅ database-architect → Completed
✅ backend-specialist → Completed
🔄 frontend-specialist → Dashboard components (60%)
⏳ test-engineer → Waiting

=== Preview ===

🌐 URL: http://localhost:3000
💚 Health: OK
```

---

## Kỹ Thuật

Status sử dụng các script sau:
- `session_manager.py status`
- `auto_preview.py status`
