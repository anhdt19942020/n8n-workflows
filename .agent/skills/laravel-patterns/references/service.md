# Service Pattern

> **Pattern**: Business Logic Layer
> **Scope**: `app/Services/**/*.php`
> **Priority**: P0 (Critical)

---

## 🎯 Nguyên Tắc Chung

### Service CHỈ ĐƯỢC:
- ✅ Chứa **business logic**
- ✅ Nhận dữ liệu đã validate (qua DTO)
- ✅ Gọi Repository
- ✅ Orchestrate logic giữa nhiều Repository/Service

### Service KHÔNG ĐƯỢC:
- ❌ Chứa validation rules (nằm ở FormRequest)
- ❌ Query trực tiếp DB (phải qua Repository)
- ❌ Chứa code liên quan HTTP (Request/Response)
- ❌ Hardcode constants (phải dùng Enum)

---

## 📦 Sử Dụng Enum & DTO

### Enum (Constants)
Tất cả hằng số **PHẢI** định nghĩa trong `App\Enums`:

```php
// ✅ Đúng
use App\Enums\UserRoleEnum;

$user->role = UserRoleEnum::STUDENT->value;

// ❌ Sai
$user->role = 'student'; // Hardcode
```

### DTO (Input/Output)
Service **PHẢI** nhận/trả DTO:

```php
// ✅ Đúng
public function createUser(CreateUserDTO $dto): UserResponseDTO
{
    $user = $this->userRepository->create([
        'name' => $dto->name,
        'role' => UserRoleEnum::STUDENT->value,
    ]);
    
    return new UserResponseDTO($user);
}

// ❌ Sai
public function createUser(array $data): array // Không dùng array
```

---

## 📚 Documentation First

**TRƯỚC KHI** viết logic mới:

1. **Dò `/docs`** → Check enum/DTO đã có chưa
2. **Đã có** → Tái sử dụng
3. **Chưa có** → Tạo mới VÀ cập nhật docs

---

## 🧹 Clean Code Rules

### 1. Single Responsibility
Mỗi method chỉ làm **1 việc rõ ràng**:

```php
// ✅ Đúng
public function createUser(CreateUserDTO $dto): UserResponseDTO { ... }
public function assignTutor(int $userId, int $tutorId): void { ... }

// ❌ Sai
public function createUserAndAssignTutorAndSendEmail(...) { ... } // Quá nhiều việc
```

### 2. Naming
Method tên là **động từ**, mô tả hành động:

```php
// ✅ Đúng
createUser()
assignTutor()
calculateScore()

// ❌ Sai
user()
tutor()
score()
```

### 3. Ngắn Gọn
Method ≤ **30 dòng**. Nếu dài hơn → tách private method hoặc sub-service.

### 4. Dependency Injection
Inject Repository/Service qua **constructor**:

```php
// ✅ Đúng
public function __construct(
    private UserRepository $userRepository,
    private EmailService $emailService
) {}

// ❌ Sai
$repo = new UserRepository(); // Không new trực tiếp
```

### 5. Không Hardcode
Luôn dùng **Enum** hoặc **config**:

```php
// ✅ Đúng
if ($user->role === UserRoleEnum::ADMIN->value) { ... }

// ❌ Sai
if ($user->role === 'admin') { ... }
```

### 6. Exception Handling
Throw exception **có ý nghĩa**:

```php
// ✅ Đúng
throw new DomainException("User already exists");

// ❌ Sai
throw new Exception("Error"); // Quá chung chung
```

---

## 📐 Best Practices

### 1. Service Quá Lớn (>500 dòng)
→ Tách thành **Domain Service** hoặc sub-service

### 2. Đặt Service Theo Domain
```
App\Services\Tutors\TutorService
App\Services\Academic\ExamService
```

### 3. Cập Nhật /docs
Khi thay đổi hoặc thêm logic → **Cập nhật `/docs`**

### 4. Logic Liên Quan Nhiều Domain
→ Viết thêm service riêng, **không dồn vào một class**

### 5. Collection vs Array
Chỉ dùng `array` hoặc PHP functions khi **KHÔNG THỂ** dùng Collection

---

## ✅ Ví Dụ Chuẩn

```php
namespace App\Services;

use App\Repositories\UserRepository;
use App\Enums\UserRoleEnum;
use App\DTOs\User\CreateUserDTO;
use App\DTOs\User\UserResponseDTO;

class UserService
{
    public function __construct(private UserRepository $userRepository) {}

    public function createUser(CreateUserDTO $dto): UserResponseDTO
    {
        // ✅ Logic nghiệp vụ
        $user = $this->userRepository->create([
            'name' => $dto->name,
            'email' => $dto->email,
            'role' => UserRoleEnum::STUDENT->value,
        ]);

        // ✅ Trả DTO
        return new UserResponseDTO($user);
    }

    public function assignTutor(int $userId, int $tutorId): void
    {
        // ✅ Orchestrate nhiều repository
        $user = $this->userRepository->find($userId);
        
        if (!$this->canAssignTutor($user)) {
            throw new DomainException("Cannot assign tutor");
        }
        
        $this->userRepository->update($userId, ['tutor_id' => $tutorId]);
    }

    private function canAssignTutor(User $user): bool
    {
        // ✅ Tách logic phức tạp thành private method
        return $user->role === UserRoleEnum::STUDENT->value
            && $user->tutor_id === null;
    }
}
```

---

## 📋 Checklist

Trước khi commit Service, đảm bảo:

- [ ] Chỉ chứa business logic
- [ ] Không có validation rules
- [ ] Không query trực tiếp DB
- [ ] Dùng DTO cho input/output
- [ ] Dùng Enum cho constants
- [ ] Method ≤ 30 dòng
- [ ] Dependency injection đúng
- [ ] Đã dò `/docs` và cập nhật nếu cần

---

## 🔗 Related Patterns

- `repository.md` - Query layer
- `dto.md` - Data Transfer Objects
- `enum.md` - Constants management
- `best-practice.md` - Control flow, clean code
- `practice-docs.md` - Documentation rules
