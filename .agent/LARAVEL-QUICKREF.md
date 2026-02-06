# Laravel Backend Quick Reference

> **Dành cho**: Backend Developer sử dụng Agent
> **Project**: EduTalk API (Laravel 10)

---

## 🚀 Cách Sử Dụng

Khi bạn làm việc với Laravel backend, agent sẽ **TỰ ĐỘNG**:

1. ✅ Detect Laravel project
2. ✅ Load `laravel-architecture` skill
3. ✅ Load các patterns cần thiết từ `laravel-patterns`
4. ✅ Áp dụng quy tắc khi viết/sửa code

**Bạn KHÔNG CẦN làm gì thêm!** Agent tự hiểu.

---

## 📋 Pattern Cheatsheet

### Khi Tạo API Mới

Agent sẽ tự động áp dụng:
- ✅ Controller pattern (thin layer)
- ✅ FormRequest validation
- ✅ Service business logic
- ✅ Repository query
- ✅ DTO input/output
- ✅ Enum cho constants

### Khi Fix Bug

Agent sẽ:
1. ✅ Check code hiện tại đúng cấu trúc chưa
2. ✅ Nếu SAI → Refactor trước khi fix
3. ✅ Apply best practices

### Khi Refactor

Agent sẽ áp dụng:
- ✅ Guard clause (early return)
- ✅ Giảm if/else (≤2 if per method)
- ✅ Tách method phức tạp
- ✅ Strategy pattern cho enum logic

---

## 🎯 Quy Tắc Vàng (KHÔNG BAO GIỜ VI PHẠM)

### 1️⃣ Phân Tầng
```
Controller → Service → Repository → Model
```

### 2️⃣ Database Safety 🔴
- ❌ **CẤM** xóa bảng/database
- ❌ **CẤM** `RefreshDatabase`

### 3️⃣ Documentation First
- ✅ Dò `/docs` trước khi code
- ✅ Update docs khi thêm Enum/DTO

### 4️⃣ Refactor Before Fix
- ✅ Code sai → Refactor trước → Fix sau

---

## 🧠 Agent Hiểu Gì

### Tự Động Nhận Diện

| Yêu cầu | Agent Load |
|---------|------------|
| "Tạo API user" | controller, validation, service, repository, dto |
| "Fix bug TutorService" | service, repository, query, best-practice |
| "Refactor code" | best-practice, common, service |
| "Tạo Event" | event-listener, enum, dto |
| "Debug query" | query, repository, test |

### KHÔNG Cần Nói Rõ

- ❌ "Hãy dùng Repository pattern"
- ❌ "Remember to use DTO"
- ❌ "Don't forget Enum"

Agent **TỰ BIẾT** và áp dụng!

---

## 📚 Patterns Có Sẵn (14)

| # | Pattern | Mục Đích |
|---|---------|----------|
| 1 | Controller | HTTP layer, routing |
| 2 | Service | Business logic |
| 3 | Repository | Query, data access |
| 4 | Validation | FormRequest rules |
| 5 | DTO | Data structure |
| 6 | Enum | Constants |
| 7 | Query | Filter pattern |
| 8 | Event-Listener | Domain events |
| 9 | ZNS Template | Zalo notification |
| 10 | Laravel 10 | Modern features |
| 11 | Best Practice | Clean code, control flow |
| 12 | Common | Global rules |
| 13 | Test | Manual debug scripts |
| 14 | Practice Docs | Documentation |

---

## 💡 Tips

### 1. Để Agent Làm
```
✅ "Tạo API create user"
✅ "Fix bug trong TutorService"
✅ "Refactor CompleteExamService"
```

Agent sẽ tự:
- Phân tích structure
- Load patterns phù hợp
- Apply best practices
- Check database safety

### 2. Chỉ Cần Nói Rõ Business Logic
```
✅ "User phải có email unique"
✅ "Status chuyển từ pending → completed"
✅ "Gửi ZNS khi assign tutor"
```

Agent lo phần kỹ thuật (Controller/Service/Repository/DTO/Enum).

### 3. Agent Sẽ Hỏi Khi Chưa Rõ
```
Agent: "Enum này đã có trong /docs chưa?"
Agent: "Bạn muốn tạo Event cho action này không?"
Agent: "Logic phức tạp này có nên tách Strategy không?"
```

---

## 🔍 Debugging

Nếu agent không áp dụng Laravel patterns:

### Check 1: Laravel Project Detection
```bash
# Có file này không?
ls artisan
cat composer.json | grep "laravel/framework"
```

### Check 2: Backend-Specialist Active
```
# Agent hiện tại
@backend-specialist
```

### Check 3: Skills Loaded
```
# Check skill description
cat .agent/skills/laravel-architecture/SKILL.md
```

---

## 📖 Đọc Thêm

- **Full Migration**: `.agent/skills/MIGRATION-SUMMARY.md`
- **Architecture**: `.agent/ARCHITECTURE.md`
- **Pattern Details**: `.agent/skills/laravel-patterns/references/*.md`
- **Backend Agent**: `.agent/agents/backend-specialist.md`

---

**Tóm tắt**: Agent tự hiểu Laravel, tự load patterns, tự apply best practices. Bạn chỉ cần nói rõ business logic! 🚀
