---
name: Laravel Architecture
description: Master router cho Laravel backend patterns. Điều hướng đến các quy tắc chuyên biệt về Controller, Service, Repository, DTO, Enum và các patterns Laravel 10. Use PROACTIVELY khi làm việc với Laravel backend.
---

# Laravel Architecture - Master Router

> **Vai trò**: Master Router điều hướng đến các Laravel backend patterns
> **Khi dùng**: Tự động kích hoạt khi nhận diện Laravel project (có `app/`, `routes/`, `composer.json`)

---

## 🎯 Mục Đích

Skill này là **cổng trung tâm** cho mọi quy tắc kiến trúc Laravel trong dự án EduTalk API. Nó điều hướng agent đến các pattern cụ thể dựa trên ngữ cảnh công việc.

---

## 📁 Cấu Trúc Kiến Trúc

Dự án tuân thủ kiến trúc **Repository-Service Pattern** với các lớp:

```
Controller → Service → Repository → Model
     ↓          ↓           ↓
Validation   DTO/Enum   Query Logic
```

### Các Skill Con (trong `laravel-patterns`)

Khi làm việc với Laravel backend, **BẮT BUỘC** tải các pattern liên quan:

| Pattern | Khi Nào Dùng | File Reference |
|---------|--------------|----------------|
| **@controller** | Viết/sửa Controller | `controller.md` |
| **@validation** | Viết FormRequest, validation | `validation.md` |
| **@service** | Viết/sửa Service (business logic) | `service.md` |
| **@repository** | Viết/sửa Repository (query) | `repository.md` |
| **@enum** | Tạo/sử dụng Enum constants | `enum.md` |
| **@dto** | Tạo/sử dụng DTO classes | `dto.md` |
| **@query** | Filter/Query patterns | `query.md` |
| **@test** | Tạo manual debug script | `test.md` |
| **@event-listener** | Tạo Event & Listener | `event-listener.md` |
| **@zns-template** | Tạo Zalo ZNS template | `zns-template.md` |
| **@laravel10** | Laravel 10 features | `laravel10.md` |
| **@best-practice** | Control flow, giảm if/else | `best-practice.md` |
| **@common** | Common rules (import, naming) | `common.md` |
| **@practice-docs** | Quy định /docs documentation | `practice-docs.md` |

---

## 🔄 Giao Thức Tải Pattern

```
Yêu cầu Backend → Phân tích ngữ cảnh → Tải pattern liên quan
                         ↓
    Ví dụ: "Fix bug API X"
    → Tải: @service, @repository, @query, @practice-docs
    
    Ví dụ: "Tạo Event mới"
    → Tải: @event-listener, @enum, @dto
    
    Ví dụ: "Refactor Service"
    → Tải: @service, @best-practice, @common, @dto
```

### Quy Tắc Tải Tự Động

**Luôn tải** (cho mọi yêu cầu backend):
- `@service`
- `@repository`
- `@best-practice`
- `@common`

**Tải theo ngữ cảnh**:
- Controller code → `@controller`, `@validation`
- Query/Filter → `@query`
- Event system → `@event-listener`
- ZNS notification → `@zns-template`
- Test/Debug → `@test`
- Documentation → `@practice-docs`

---

## 🛑 Quy Tắc Chung (KHÔNG BAO GIỜ VI PHẠM)

### 1. **Phân Tầng Nghiêm Ngặt**
- ❌ Controller KHÔNG được chứa business logic
- ❌ Service KHÔNG được viết query trực tiếp (phải qua Repository)
- ❌ Repository KHÔNG được chứa business logic
- ✅ Mỗi tầng chỉ làm 1 việc

### 2. **Refactor Before Fix**
Khi fix bug, tối ưu, hoặc thêm code:
- ✅ Kiểm tra code hiện tại có đúng cấu trúc không
- ✅ Nếu SAI → **Refactor lại đúng chuẩn TRƯỚC** khi sửa bug
- ❌ KHÔNG build thêm logic lên code sai cấu trúc

### 3. **Database Safety**
- 🔴 **TUYỆT ĐỐI CẤM** xóa bảng hoặc xóa database
- 🔴 **TUYỆT ĐỐI CẤM** dùng `RefreshDatabase` trong test
- ✅ Data migration chỉ dùng seeder, không destructive

### 4. **Documentation First**
- ✅ **Dò `/docs` TRƯỚC** khi viết logic mới
- ✅ Nếu Enum/DTO đã có → Tái sử dụng
- ✅ Nếu chưa có → Tạo mới VÀ cập nhật docs

---

## 📖 Cách Sử Dụng Skill Này

### Khi Agent Nhận Yêu Cầu Backend:

1. **Nhận diện Laravel project** (tự động)
2. **Phân tích yêu cầu** → Xác định pattern liên quan
3. **Tải các reference files** từ `laravel-patterns/references/`
4. **Áp dụng quy tắc** khi viết/sửa code
5. **Kiểm tra tuân thủ** trước khi hoàn thành

---

## 🔗 Integration với Backend-Specialist Agent

Skill này được trigger tự động bởi `backend-specialist` agent khi:
- Detect Laravel project (có `artisan`, `composer.json` với `laravel/framework`)
- User request liên quan backend (API, Service, Repository, etc.)

Agent sẽ:
1. Load `laravel-architecture/SKILL.md` (file này)
2. Đọc ngữ cảnh yêu cầu
3. Load các pattern cần thiết từ `laravel-patterns/references/`
4. Thực thi theo đúng quy tắc

---

## 📊 Checklist Tuân Thủ

Trước khi hoàn thành bất kỳ tác vụ backend nào, đảm bảo:

- [ ] Logic đúng tầng (Controller/Service/Repository)
- [ ] Dùng Enum cho constants
- [ ] Dùng DTO cho input/output Service
- [ ] Query chỉ trong Repository
- [ ] Validation chỉ trong FormRequest
- [ ] Code tuân thủ best-practice (≤2 if, guard clause)
- [ ] /docs đã được cập nhật (nếu thêm logic mới)
- [ ] KHÔNG có RefreshDatabase trong test

---

## 🚀 Quick Reference

| Tác vụ | Load Pattern |
|--------|--------------|
| Fix API bug | @service, @repository, @query |
| Tạo API mới | @controller, @validation, @service, @repository, @dto |
| Refactor code | @service, @best-practice, @common |
| Tạo Event | @event-listener, @enum, @dto |
| Debug query | @query, @repository, @test |
| Tạo ZNS | @zns-template, @dto |

---

**Ghi chú**: Skill này KHÔNG chứa code implementation, chỉ routing logic. Tất cả quy tắc chi tiết nằm trong `laravel-patterns/references/`.
