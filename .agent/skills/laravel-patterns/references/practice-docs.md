# Practice Docs - Documentation Rules

> **Pattern**: Documentation Standards
> **Scope**: `docs/**/*.md`
> **Priority**: P1 (Important)

---

## 🎯 Mục Đích

**`/docs` là source of truth** cho business logic, Enum, DTO trong dự án.

---

## 1️⃣ Documentation First Workflow

### Trước Khi Viết Logic Mới

```
1. 🔍 Dò /docs → Đã có Enum/DTO/Logic chưa?
   ├─ Đã có → ✅ Tái sử dụng
   └─ Chưa có → 📝 Tạo mới VÀ cập nhật /docs
```

### ❌ KHÔNG Làm

```php
// Tạo Enum mới mà không check docs
enum TaskStatusEnum { ... }

// Viết logic mới mà không ghi docs
public function complexBusinessLogic() { ... }
```

### ✅ Phải Làm

```
1. Mở /docs/enums.md → Check TaskStatusEnum đã có chưa
2. Nếu chưa:
   - Tạo enum
   - Cập nhật /docs/enums.md
3. Nếu đã có:
   - Tái sử dụng
```

---

## 2️⃣ Nội Dung Cần Ghi Trong /docs

### Với Mỗi Business Logic

- ✅ **Ý nghĩa và phạm vi** của logic
- ✅ **Cách sử dụng** (Controller nào gọi, Service nào implement)
- ✅ **Ví dụ minh họa**

### Với Mỗi Enum

- ✅ Liệt kê **toàn bộ giá trị**
- ✅ Giải thích **ý nghĩa** từng giá trị
- ✅ **Use case** khi nào dùng

Ví dụ: `/docs/enums/task-status.md`
```markdown
# TaskStatusEnum

## Values

| Value | Label | Ý nghĩa | Khi nào dùng |
|-------|-------|---------|--------------|
| `pending` | Chờ xử lý | Task mới tạo | Khi tạo task |
| `in_progress` | Đang xử lý | Task đang làm | Khi assign user |
| `completed` | Hoàn thành | Task xong | Khi complete |
| `cancelled` | Đã hủy | Task bị hủy | Khi cancel |

## Usage

```php
use App\Enums\TaskStatusEnum;

$task->status = TaskStatusEnum::PENDING->value;
```
```

### Với Mỗi DTO

- ✅ Mô tả **fields** (input/output)
- ✅ Data type và **validation rules**
- ✅ **Ví dụ sử dụng**

Ví dụ: `/docs/dtos/user-create.md`
```markdown
# CreateUserDTO

## Input Fields

| Field | Type | Required | Validation | Description |
|-------|------|----------|------------|-------------|
| name | string | Yes | max:255 | Tên người dùng |
| email | string | Yes | email, unique | Email đăng nhập |
| password | string | Yes | min:8 | Mật khẩu |
| role_id | int | No | exists:roles | ID vai trò |

## Example

```php
$dto = new CreateUserDTO(
    name: 'John Doe',
    email: 'john@example.com',
    password: 'secret123',
    roleId: 1
);
```
```

---

## 3️⃣ API Documentation

Mỗi API nên có **1 doc riêng**:

### Đặt File

```
docs/api/<module>/<api-name>.md
```

Ví dụ:
- `docs/api/teacher-quality/get-history.md`
- `docs/api/tutors/assign-tutor.md`

### Template

```markdown
# [Tên API]

## Bối cảnh & Mục tiêu
[Mô tả ngắn gọn API làm gì, tại sao cần]

## Route & Method
`GET /api/teacher-quality/history`

## Auth & Permission
- Role: `teacher`, `admin`
- Permission: `view-history`

## Request

### Query Parameters
| Param | Type | Required | Description |
|-------|------|----------|-------------|
| page | int | No | Số trang (default: 1) |
| per_page | int | No | Số items/page (default: 15) |

### Body (nếu có)
```json
{
    "filter": "active",
    "date_from": "2025-01-01"
}
```

## Response

### Success (200)
```json
{
    "success": true,
    "data": {
        "items": [...],
        "total": 100,
        "page": 1
    }
}
```

### Error (400/422/500)
```json
{
    "success": false,
    "message": "Validation error",
    "errors": { ... }
}
```

## Business Rules
- Chỉ lấy history của user hiện tại
- Kết quả sort theo `created_at DESC`

## Example cURL
```bash
curl -X GET "http://api.example.com/api/teacher-quality/history?page=1" \
  -H "Authorization: Bearer {token}"
```
```

---

## 4️⃣ Domain/Module Documentation

### Đặt File

```
docs/domain/<module>/overview.md
```

### Nên Có

- ✅ **Bối cảnh & thuật ngữ** chính
- ✅ **Các enum, DTO, entity** quan trọng (link file riêng)
- ✅ **Luồng xử lý** chính (flow diagram)

Ví dụ: `docs/domain/tutors/overview.md`
```markdown
# Tutors Module

## Thuật ngữ
- **Tutor**: Gia sư
- **Student**: Học sinh
- **Assignment**: Gán gia sư cho học sinh

## Enums
- [TutorStatusEnum](../enums/tutor-status.md)
- [AssignmentTypeEnum](../enums/assignment-type.md)

## DTOs
- [AssignTutorDTO](../dtos/assign-tutor.md)
- [TutorResponseDTO](../dtos/tutor-response.md)

## Luồng chính

```
1. Admin tạo tutor
2. Admin assign tutor cho student
3. System gửi notification (Event)
4. Tutor xác nhận
5. System cập nhật status
```
```

---

## 5️⃣ Metadata (Frontmatter)

Khuyến nghị metadata ở đầu file:

```markdown
---
title: Assign Tutor API
module: Tutors
owner: Backend Team
task_id: JIRA-1234
lastUpdated: 2025-01-27
---

# Assign Tutor API
...
```

**Benefit**: Search, truy vết quyết định (ai làm, theo task nào).

---

## 6️⃣ Changelog & Breaking Changes

Khi **thay đổi logic** hoặc **thêm enum mới**:

### Cập Nhật Docs

```markdown
## Changelog

### 2025-01-27
- **Added**: `cancelled` status to TaskStatusEnum
- **Changed**: `complete()` method now requires `completion_note`

### 2025-01-15
- **Breaking**: `role` field changed from string to enum
```

### Breaking Changes

```markdown
## Breaking Changes

### v2.0.0 (2025-02-01)
- **API Response Structure**: Changed from nested object to array
  - Before: `{ "data": { "user": {...} } }`
  - After: `{ "data": {...} }`
- **Migration Guide**: [Link to migration doc]
```

---

## 7️⃣ Agent Rules

### `/docs` là Source of Truth

Khi Agent thấy **code khác docs**:

❌ **KHÔNG** tự sửa theo ý mình

✅ **PHẢI**:
- Hoặc đề xuất chỉnh docs
- Hoặc hỏi lại user: docs hay code là đúng?

---

## 8️⃣ Ngôn Ngữ & Style

### Ngôn Ngữ
- ✅ **Tiếng Việt kỹ thuật**
- ✅ Thống nhất thuật ngữ (Issue, Metric, Retake, Tutor, ...)

### Style
- ✅ Ưu tiên **bullet, bảng, ví dụ**
- ❌ Tránh viết lan man

---

## 📋 Checklist

Khi tạo/sửa code:

- [ ] Đã dò `/docs` để check Enum/DTO chưa?
- [ ] Nếu tạo Enum/DTO mới → Cập nhật `/docs`
- [ ] Nếu thêm API → Tạo doc API trong `/docs/api/`
- [ ] Nếu thay đổi logic → Cập nhật `/docs` + Changelog
- [ ] Breaking change → Ghi rõ trong Breaking Changes section

---

## 🔗 Related Patterns

- `enum.md` - Document Enums
- `dto.md` - Document DTOs
- `service.md` - Business logic cần docs
- `common.md` - Global rules cũng cần docs
