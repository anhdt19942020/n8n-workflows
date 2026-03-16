---
description: Preview server start, stop, and status check. Local development server management.
---

# /preview - Quản Lý Preview

$ARGUMENTS

> 🔴 **BẮT BUỘC (Khởi tạo Serena):**
> Trước khi thực hiện bất kỳ công việc nào trong lệnh này, Agent PHẢI:
> 1. Gọi \`mcp_serena_check_onboarding_performed\`
> 2. Gọi \`mcp_serena_activate_project\` với đường dẫn thư mục hiện tại.
> (Bỏ qua nếu Serena đã được kích hoạt trong phiên làm việc này).


## Tác Vụ

Quản lý server preview: khởi động, dừng, kiểm tra trạng thái.

### Các Lệnh

```
/preview           - Hiển thị trạng thái hiện tại
/preview start     - Khởi động server
/preview stop      - Dừng server
/preview restart   - Khởi động lại
/preview check     - Kiểm tra sức khỏe (health check)
```

---

## Ví Dụ Sử Dụng

### Khởi Động Server
```
/preview start

Phản hồi:
🚀 Starting preview...
   Port: 3000
   Type: Next.js

✅ Preview ready!
   URL: http://localhost:3000
```

### Kiểm Tra Trạng Thái
```
/preview

Phản hồi:
=== Preview Status ===

🌐 URL: http://localhost:3000
📁 Project: C:/projects/my-app
🏷️ Type: nextjs
💚 Health: OK
```

### Xung Đột Cổng (Port Conflict)
```
/preview start

Phản hồi:
⚠️ Port 3000 is in use.

Options:
1. Start on port 3001
2. Close app on 3000
3. Specify different port

Which one? (default: 1)
```

---

## Kỹ Thuật

Auto preview sử dụng script `auto_preview.py`:

```bash
python ~/.claude/scripts/auto_preview.py start [path] [port]
python ~/.claude/scripts/auto_preview.py stop
python ~/.claude/scripts/auto_preview.py status
```
