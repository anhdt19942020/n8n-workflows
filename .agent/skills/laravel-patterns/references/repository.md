# Repository Pattern

> **Pattern**: Query Layer (Data Access)
> **Scope**: `app/Repositories/**/*.php`
> **Priority**: P0 (Critical)

---

## 🎯 Nguyên Tắc

Repository **CHỈ ĐƯỢC**:
- ✅ Chứa query logic
- ✅ Tương tác với Model/Eloquent
- ✅ Return Collection, Model, hoặc scalar

Repository **KHÔNG ĐƯỢC**:
- ❌ Chứa business logic
- ❌ Validation
- ❌ Call Service khác

---

## 🏗️ Cấu Trúc

### 1. Tạo Interface
```php
// app/Repositories/Contracts/UserRepositoryInterface.php
namespace App\Repositories\Contracts;

interface UserRepositoryInterface
{
    public function find(int $id): ?User;
    public function create(array $data): User;
    public function update(int $id, array $data): bool;
}
```

### 2. Tạo Implementation
```php
// app/Repositories/Eloquent/UserRepository.php
namespace App\Repositories\Eloquent;

use App\Repositories\Contracts\UserRepositoryInterface;
use App\Models\User;

class UserRepository implements UserRepositoryInterface
{
    public function find(int $id): ?User
    {
        return User::find($id);
    }

    public function create(array $data): User
    {
        return User::create($data);
    }

    public function update(int $id, array $data): bool
    {
        return User::where('id', $id)->update($data);
    }
}
```

### 3. Đăng Ký Binding
```php
// app/Providers/AppServiceProvider.php
public function register(): void
{
    $this->app->bind(
        \App\Repositories\Contracts\UserRepositoryInterface::class,
        \App\Repositories\Eloquent\UserRepository::class,
    );
}
```

---

## 🔑 Best Practices

### 1. Luôn Dùng `newQuery()`
Tránh dính điều kiện cũ:

```php
// ✅ Đúng
$query = $this->model->newQuery();

// ❌ Sai
$query = $this->model; // Có thể dính scope/where cũ
```

### 2. Viết Logic Query Tách Nhỏ (Scope Pattern)
```php
public function getActiveUsers(): Collection
{
    return $this->model->newQuery()
        ->where('status', 'active')
        ->get();
}

public function getUsersByRole(string $role): Collection
{
    return $this->model->newQuery()
        ->where('role', $role)
        ->get();
}
```

### 3. Hạn Chế Join - Dùng Relationship
**Trước khi viết JOIN**, kiểm tra Model có relationship chưa:

```php
// ❌ Sai - Join thủ công
$users = DB::table('users')
    ->join('profiles', 'users.id', '=', 'profiles.user_id')
    ->select('users.*', 'profiles.bio')
    ->get();

// ✅ Đúng - Dùng relationship
class User extends Model
{
    public function profile()
    {
        return $this->hasOne(Profile::class);
    }
}

$users = User::with('profile')->get();
```

Nếu **chưa có relationship** → Tạo trong Model trước khi query.

---

## 🔄 Query Filter Pattern

Xem chi tiết trong `query.md`. Tóm tắt:

### ❌ KHÔNG Làm
```php
public function filter(array $filters)
{
    $query = $this->model->newQuery();
    
    if (!empty($filters['status'])) {
        $query->where('status', $filters['status']);
    }
    if (!empty($filters['role'])) {
        $query->where('role', $filters['role']);
    }
    // ... nhiều if (!empty()) ...
    
    return $query->get();
}
```

### ✅ Phải Làm
```php
use App\Services\QueryFilterService;
use App\DTOs\FilterConditionDTO;
use App\Enums\FilterConditionType;

public function filter(array $filters)
{
    $conditions = [
        new FilterConditionDTO(
            key: 'status',
            keyDatabase: 'status',
            type: FilterConditionType::Equal,
        ),
        new FilterConditionDTO(
            key: 'role',
            keyDatabase: 'role',
            type: FilterConditionType::Equal,
        ),
    ];

    $query = $this->model->newQuery();
    $query = app(QueryFilterService::class)->apply($query, $filters, $conditions);
    
    return $query->get();
}
```

---

## 📋 Checklist

Trước khi viết Repository:

- [ ] Check đã có Interface chưa → Nếu chưa, tạo Interface
- [ ] Check đã có Implementation chưa → Nếu chưa, tạo Implementation
- [ ] Đăng ký binding trong `AppServiceProvider`
- [ ] Dùng `newQuery()` cho mọi query mới
- [ ] Check relationship trong Model trước khi JOIN
- [ ] Dùng `QueryFilterService` cho filter (xem `query.md`)
- [ ] KHÔNG chứa business logic

---

## 🔗 Related Patterns

- `query.md` - Filter pattern chi tiết
- `service.md` - Business logic layer
- `common.md` - Naming conventions
