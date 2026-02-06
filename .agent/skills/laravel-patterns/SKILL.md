---
name: Laravel Patterns
description: 14 Laravel backend patterns chi tiết - Controller, Service, Repository, DTO, Enum, Query, Event, và Best Practices. Index điều hướng đến các reference files.
---

# Laravel Patterns - Pattern Library

> **Vai trò**: Thư viện patterns chi tiết cho Laravel backend
> **Parent Skill**: `laravel-architecture`
> **Khi dùng**: Được load bởi `laravel-architecture` dựa trên ngữ cảnh

---

## 📚 Pattern Library (14 Patterns)

Skill này chứa **14 patterns** chi tiết cho Laravel backend development. Mỗi pattern là một reference file trong `references/`.

---

## 🗺️ Bản Đồ Nội Dung

### 1️⃣ **Core Architecture** (4 patterns)
| Pattern | File | Mục Đích | Khi Nào Đọc |
|---------|------|----------|-------------|
| Controller | `controller.md` | Quy tắc Controller layer | Viết/sửa Controller |
| Service | `service.md` | Business logic rules | Viết/sửa Service |
| Repository | `repository.md` | Query layer pattern | Viết/sửa Repository |
| Query | `query.md` | Filter/Query patterns | Viết filter, query phức tạp |

### 2️⃣ **Data Structures** (3 patterns)
| Pattern | File | Mục Đích | Khi Nào Đọc |
|---------|------|----------|-------------|
| Validation | `validation.md` | FormRequest rules | Viết validation |
| DTO | `dto.md` | Data Transfer Objects | Tạo DTO classes |
| Enum | `enum.md` | Constants management | Tạo/sử dụng Enum |

### 3️⃣ **Laravel Features** (3 patterns)
| Pattern | File | Mục Đích | Khi Nào Đọc |
|---------|------|----------|-------------|
| Event-Listener | `event-listener.md` | Domain events | Tạo Event/Listener |
| ZNS Template | `zns-template.md` | Zalo notification | Tạo ZNS template |
| Laravel 10 | `laravel10.md` | Laravel 10 features | Dùng tính năng mới |

### 4️⃣ **Best Practices** (4 patterns)
| Pattern | File | Mục Đích | Khi Nào Đọc |
|---------|------|----------|-------------|
| Best Practice | `best-practice.md` | Control flow, giảm if/else | Refactor code |
| Common | `common.md` | Common rules (import, naming) | Mọi yêu cầu |
| Test | `test.md` | Manual debug scripts | Debug/Test |
| Practice Docs | `practice-docs.md` | Documentation rules | Viết docs |

---

## 🔄 Giao Thức Đọc Pattern

### **KHÔNG đọc tất cả 14 files!** 
Agent chỉ đọc file liên quan đến yêu cầu hiện tại.

### Mapping Yêu Cầu → Pattern

| Yêu Cầu | Đọc Files |
|---------|-----------|
| "Tạo API mới" | `controller.md`, `validation.md`, `service.md`, `repository.md`, `dto.md` |
| "Fix bug Service" | `service.md`, `repository.md`, `query.md`, `best-practice.md` |
| "Refactor code" | `best-practice.md`, `common.md`, `service.md` |
| "Tạo Event" | `event-listener.md`, `enum.md`, `dto.md` |
| "Debug query" | `query.md`, `repository.md`, `test.md` |
| "Tạo ZNS" | `zns-template.md`, `dto.md` |
| "Viết docs" | `practice-docs.md` |

### Luôn Đọc (mọi yêu cầu backend):
- `common.md` - Quy tắc chung
- `best-practice.md` - Control flow rules

---

## 📖 Cách Sử Dụng

### Agent Workflow:

1. **Nhận yêu cầu** từ user (ví dụ: "Fix bug trong TutorService")
2. **Mapping** yêu cầu → Patterns cần thiết
3. **Đọc files** từ `references/`:
   ```
   - references/service.md
   - references/repository.md
   - references/best-practice.md
   - references/common.md
   ```
4. **Áp dụng** quy tắc từ các files đã đọc
5. **Kiểm tra** tuân thủ trước khi hoàn thành

---

## 🎯 Pattern Priority

### P0 (Critical - Luôn Tuân Thủ):
- `common.md` - Phân tầng nghiêm ngặt
- `service.md` - Business logic rules
- `repository.md` - Query rules
- Database Safety (KHÔNG xóa data)

### P1 (Important - Nên Tuân Thủ):
- `best-practice.md` - Clean code, ≤2 if
- `dto.md` - Dùng DTO thay array
- `enum.md` - Không hardcode constants
- `query.md` - Filter pattern

### P2 (Nice to Have - Khuyến nghị):
- `laravel10.md` - Dùng tính năng mới
- `practice-docs.md` - Documentation
- `test.md` - Manual testing

---

## 🛡️ Quy Tắc Không Thương Lượng

Các quy tắc này **KHÔNG BAO GIỜ VI PHẠM**, bất kể yêu cầu:

### 1. **Phân Tầng** (từ `common.md`)
- Controller KHÔNG có business logic
- Service KHÔNG có query trực tiếp
- Repository KHÔNG có business logic

### 2. **Database Safety** (từ `common.md`)
- KHÔNG xóa bảng/database
- KHÔNG dùng `RefreshDatabase`

### 3. **Refactor Before Fix** (từ `best-practice.md`)
- Code sai cấu trúc → Refactor TRƯỚC khi fix bug

### 4. **Documentation First** (từ `practice-docs.md`)
- Dò `/docs` trước khi viết logic mới
- Cập nhật docs khi thêm Enum/DTO

---

## 📊 Quick Reference Table

| Tình Huống | Read Files | Skip Files |
|------------|------------|------------|
| API CRUD mới | controller, validation, service, repository, dto, common | event-listener, zns-template, test |
| Fix Service bug | service, repository, query, best-practice, common | controller, validation, event-listener |
| Refactor | best-practice, common, service | event-listener, zns-template |
| Event system | event-listener, enum, dto, common | controller, validation, query |
| Query optimization | query, repository, test, common | controller, validation, event-listener |

---

## 🔗 File Paths

Tất cả reference files nằm trong:
```
.agent/skills/laravel-patterns/references/
├── controller.md
├── service.md
├── repository.md
├── dto.md
├── enum.md
├── validation.md
├── query.md
├── test.md
├── event-listener.md
├── zns-template.md
├── laravel10.md
├── best-practice.md
├── common.md
└── practice-docs.md
```

---

## 💡 Tips cho Agent

- **Lazy Load**: Chỉ đọc file khi cần, không đọc hết 14 files
- **Context Aware**: Phân tích yêu cầu user trước khi quyết định đọc file nào
- **Priority First**: Luôn đọc P0 patterns trước (common, service, repository)
- **Incremental**: Đọc thêm file nếu phát hiện cần trong quá trình làm việc

---

**Parent Skill**: `laravel-architecture` → Điều hướng đến skill này
**Related Skills**: `api-patterns`, `database-design`, `clean-code`
