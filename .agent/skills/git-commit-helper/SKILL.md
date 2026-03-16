---
name: Git Commit Helper
description: Skill chuyên biệt để phân tích thay đổi code và tạo Git Commit Message chuẩn Conventional Commits (feat, fix, refactor, chore...).
---

# Git Commit Helper

> **Vai trò**: Trợ lý tạo Git Commit Message chuẩn xác
> **Kích hoạt**: Sau khi hoàn thành một tác vụ (workflow, fix bug, feature) và cần lưu thay đổi.

---

## 🎯 Mục Đích

Đảm bảo lịch sử Git sạch, rõ ràng và tuân thủ chuẩn **Conventional Commits** để dễ dàng theo dõi và generate changelog.

---

## 📝 Quy Tắc Tạo Message (Conventional Commits)

Format chuẩn:
```
<type>(<scope>): <short summary>
  │       │             │
  │       │             └─ Mô tả ngắn gọn BẰNG TIẾNG VIỆT, bắt đầu bằng động từ, viết thường
  │       └─ Phạm vi thay đổi (Service, Controller, Module, hoặc tên file chính)
  └─ Loại thay đổi (feat, fix, docs, style, refactor, test, chore)
```
Ngỗn ngữ: Tiếng Việt

### Các Loại (Types) Phổ Biến

| Type | Ý nghĩa | Ví dụ |
|------|---------|-------|
| **feat** | Tính năng mới | `feat(auth): thêm đăng nhập bằng google` |
| **fix** | Sửa lỗi | `fix(payment): sửa lỗi chuyển đổi tiền tệ` |
| **docs** | Tài liệu | `docs(readme): cập nhật hướng dẫn cài đặt` |
| **style** | Formatting, chấm phẩy (không đổi logic) | `style(user): format code theo chuẩn PSR-12` |
| **refactor** | Tái cấu trúc (không thêm tính năng/sửa lỗi) | `refactor(order): đơn giản hóa logic tính tổng` |
| **perf** | Tối ưu hiệu năng | `perf(search): dùng elasticsearch thay vì like query` |
| **test** | Thêm/sửa test | `test(cart): thêm unit test cho thêm sản phẩm` |
| **chore** | Cập nhật build, tool, config | `chore(deps): cập nhật laravel/framework lên 10.x` |

---

## 🔍 Quy Trình Thực Hiện

### Bước 1: Phân Tích Thay Đổi
1. Sử dụng `git status` để xem file nào thay đổi.
2. Sử dụng `git diff` để xem nội dung thay đổi chi tiết.

### Bước 2: Xác Định Type & Scope
- **Type**: Dựa vào bản chất thay đổi (Logic mới? Sửa lỗi? Format?).
- **Scope**:
  - Backend: Tên Service, Module, Controller (vd: `TutorService`, `Order`, `Auth`).
  - Frontend: Tên Component, Page (vd: `Button`, `Dashboard`).
  - General: `core`, `config`, `deps`.

### Bước 3: Soạn Thảo Message
- **Tiêu đề**: Ngắn gọn (< 72 ký tự), không viết hoa toàn bộ, không dấu chấm cuối.
- **Body** (Tùy chọn): Giải thích *tại sao* thay đổi, *như thế nào*.
- **Footer** (Tùy chọn): Reference issue (vd: `Closes #123`).

### Bước 4: Đề Xuất & Thực Thi
1. Đề xuất lệnh commit cho người dùng.
2. Chờ xác nhận hoặc chỉnh sửa.
3. Thực thi commit (nếu được phép).

---

## ✅ Ví Dụ Thực Tế

### Ví Dụ 1: Backend Fix
**Thay đổi**: Sửa logic tính điểm trong `TestInputService.php`.
**Message**:
```bash
git commit -m "fix(grading): sửa công thức tính điểm cho đề thi thử ielts"
```

### Ví Dụ 2: Thêm API Mới
**Thay đổi**: Thêm `TutorController`, `TutorService`, `Route`.
**Message**:
```bash
git commit -m "feat(tutor): thêm api lấy danh sách gia sư với filtering"
```

### Ví Dụ 3: Refactor
**Thay đổi**: Chuyển logic từ Controller sang Service.
**Message**:
```bash
git commit -m "refactor(auth): chuyển logic đăng nhập từ controller sang AuthService"
```

---

## 🛠️ Lệnh Hỗ Trợ

Nếu người dùng chưa add file:
```bash
git add .
git commit -m "..."
```

Nếu chỉ muốn add file cụ thể:
```bash
git add path/to/file
git commit -m "..."
```
