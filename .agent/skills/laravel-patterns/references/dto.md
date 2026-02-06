# DTO Pattern

> **Pattern**: Data Transfer Objects
> **Scope**: `app/DTOs/**/*.php`
> **Priority**: P1 (Important)

---

## 🎯 Nguyên Tắc

- ✅ Service **PHẢI** dùng DTO cho input/output
- ❌ **KHÔNG** truyền array hoặc Request object vào Service
- ✅ DTO có thể dùng `readonly` properties (PHP 8.1+)

---

## 📁 Cấu Trúc & Naming

DTO đặt trong `App/DTOs`, tên theo chức năng:

### Input DTO
```
App/DTOs/User/CreateUserDTO.php
App/DTOs/Order/UpdateOrderDTO.php
App/DTOs/Academic/TutorAssignDTO.php
```

### Output DTO
```
App/DTOs/User/UserResponseDTO.php
App/DTOs/Order/OrderListDTO.php
App/DTOs/Academic/ScheduleOverviewDTO.php
```

---

## ✅ Ví Dụ Chuẩn

### Input DTO
```php
namespace App\DTOs\User;

readonly class CreateUserDTO
{
    public function __construct(
        public string $name,
        public string $email,
        public string $password,
        public ?int $roleId = null,
    ) {}
    
    // Tạo từ validated request
    public static function fromRequest(array $validated): self
    {
        return new self(
            name: $validated['name'],
            email: $validated['email'],
            password: $validated['password'],
            roleId: $validated['role_id'] ?? null,
        );
    }
}
```

### Output DTO
```php
namespace App\DTOs\User;

use App\Models\User;

readonly class UserResponseDTO
{
    public function __construct(
        public int $id,
        public string $name,
        public string $email,
        public string $role,
        public string $createdAt,
    ) {}
    
    // Tạo từ Model
    public static function fromModel(User $user): self
    {
        return new self(
            id: $user->id,
            name: $user->name,
            email: $user->email,
            role: $user->role->name,
            createdAt: $user->created_at->toIso8601String(),
        );
    }
    
    // Convert to array for response
    public function toArray(): array
    {
        return [
            'id' => $this->id,
            'name' => $this->name,
            'email' => $this->email,
            'role' => $this->role,
            'created_at' => $this->createdAt,
        ];
    }
}
```

---

## 🔄 Workflow

### Controller → Service
```php
// Controller
public function store(CreateUserRequest $request)
{
    $dto = CreateUserDTO::fromRequest($request->validated());
    $response = $this->userService->createUser($dto);
    
    return $this->successResponse($response->toArray());
}

// Service
public function createUser(CreateUserDTO $dto): UserResponseDTO
{
    $user = $this->userRepository->create([
        'name' => $dto->name,
        'email' => $dto->email,
        'password' => Hash::make($dto->password),
    ]);
    
    return UserResponseDTO::fromModel($user);
}
```

---

## 📚 Tái Sử Dụng DTO

**TRƯỚC KHI** tạo DTO mới:

1. **Dò `/docs`** → Check DTO đã có chưa
2. **Nếu đã có** → Tái sử dụng
3. **Nếu chưa có** → Tạo mới VÀ cập nhật `/docs`

---

## 📋 Checklist

Khi tạo DTO mới:

- [ ] Tên DTO rõ ràng (Input: `CreateXxxDTO`, Output: `XxxResponseDTO`)
- [ ] Đặt đúng namespace domain (`App/DTOs/<Domain>/`)
- [ ] Dùng `readonly` properties
- [ ] Có static factory method (`fromRequest`, `fromModel`)
- [ ] Output DTO có `toArray()` method
- [ ] Cập nhật `/docs` nếu DTO mới

---

## 💡 Tips

### 1. Collection DTO
Cho list items:

```php
readonly class UserListDTO
{
    /** @param UserResponseDTO[] $users */
    public function __construct(
        public array $users,
        public int $total,
        public int $page,
    ) {}
    
    public function toArray(): array
    {
        return [
            'users' => array_map(fn($u) => $u->toArray(), $this->users),
            'total' => $this->total,
            'page' => $this->page,
        ];
    }
}
```

### 2. Nested DTO
```php
readonly class OrderResponseDTO
{
    public function __construct(
        public int $id,
        public UserResponseDTO $user, // Nested DTO
        public float $total,
    ) {}
}
```

---

## 🔗 Related Patterns

- `service.md` - Service dùng DTO
- `validation.md` - Validate before DTO
- `practice-docs.md` - Document DTO trong /docs
