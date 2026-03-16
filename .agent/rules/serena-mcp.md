
# 🔧 GIAO THỨC BẮT BUỘC: SERENA MCP (Code Intelligence)

> **Quy tắc:** Khi làm việc với code (edit, debug, enhance, review, brainstorm liên quan đến code), bạn **NÊN** ưu tiên sử dụng Serena MCP tools thay vì chỉ dùng grep/view_file thuần.

---

## 🔴 QUY TẮC KÍCH HOẠT

1. **Kích hoạt tự động** khi bắt đầu phiên làm việc có liên quan đến code:
   - Gọi `mcp_serena_activate_project` với đường dẫn dự án
   - Gọi `mcp_serena_check_onboarding_performed`
   - Đọc memories liên quan nếu có

2. **Bỏ qua kích hoạt** nếu:
   - Serena đã được kích hoạt trong phiên hiện tại
   - Yêu cầu chỉ là câu hỏi đơn giản / xã giao
   - Yêu cầu không liên quan đến code (ví dụ: query DB thuần, deploy)

---

## 📋 KHI NÀO DÙNG SERENA TOOLS

| Tình Huống | Serena Tool Ưu Tiên | Thay Vì |
|------------|---------------------|---------|
| Tìm class/method/function | `find_symbol` | `grep_search` |
| Hiểu cấu trúc file | `get_symbols_overview` | `view_file` toàn bộ |
| Tìm nơi gọi method | `find_referencing_symbols` | `grep_search` tên method |
| Tìm pattern trong code | `search_for_pattern` | `grep_search` |
| Sửa body method/class | `replace_symbol_body` | `replace_file_content` |
| Thêm code sau symbol | `insert_after_symbol` | Tính toán line number |
| Đổi tên symbol | `rename_symbol` | Find & Replace thủ công |

---

## 🔄 LUỒNG LÀM VIỆC VỚI SERENA

```
Nhận yêu cầu liên quan code
    │
    ├── 1️⃣ Kích hoạt Serena (nếu chưa)
    │   └── mcp_serena_activate_project
    │
    ├── 2️⃣ Hiểu codebase
    │   ├── get_symbols_overview → hiểu cấu trúc file
    │   ├── find_symbol → tìm symbol cụ thể
    │   └── find_referencing_symbols → tìm nơi sử dụng
    │
    ├── 3️⃣ Phân tích (kết hợp Sequential Thinking)
    │   └── Dùng context từ Serena để phân tích
    │
    └── 4️⃣ Thực thi
        ├── replace_symbol_body → sửa code
        ├── insert_after_symbol → thêm code
        └── rename_symbol → đổi tên
```

---

## ⚡ KẾT HỢP VỚI CÁC TOOLS KHÁC

| Tool Hiện Tại | Khi Nào Vẫn Dùng |
|---------------|-------------------|
| `grep_search` | Tìm text thuần (không phải code symbol), tìm trong file config/env |
| `view_file` | Xem file config, .env, markdown, hoặc cần xem line numbers cụ thể |
| `find_by_name` | Tìm file theo tên/extension |
| `replace_file_content` | Sửa file không phải code (config, markdown, env) |

---

## 📝 LƯU Ý QUAN TRỌNG

- Serena hoạt động tốt nhất với **PHP, TypeScript, JavaScript, Python**
- Luôn `activate_project` trước khi dùng bất kỳ Serena tool nào
- Dùng `list_memories` và `read_memory` để tận dụng context đã lưu từ phiên trước
- Khi task phức tạp, kết hợp: **Sequential Thinking** (phân tích) + **Serena** (code intelligence) + **MCP DB** (data)
