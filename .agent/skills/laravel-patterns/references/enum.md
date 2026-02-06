# Enum Pattern

> **Pattern**: Constants Management
> **Scope**: `app/Enums/**/*.php`
> **Priority**: P1 (Important)

---

## 🎯 Nguyên Tắc

- ✅ Mọi hằng số (status, type, role, ...) **PHẢI** định nghĩa trong Enum
- ❌ **KHÔNG** hardcode string/number trong Service hoặc Controller
- ✅ Enum đặt trong `App/Enums`, phân loại theo domain

---

## 📁 Cấu Trúc

```
App/Enums/
├── Academic/
│   ├── TaskStatusEnum.php
│   └── ExamTypeEnum.php
├── User/
│   ├── UserRoleEnum.php
│   └── UserStatusEnum.php
└── Order/
    └── PaymentStatusEnum.php
```

---

## ✅ Ví Dụ Chuẩn

```php
namespace App\Enums\User;

enum UserRoleEnum: string
{
    case ADMIN = 'admin';
    case TEACHER = 'teacher';
    case STUDENT = 'student';
    
    // Helper methods
    public function label(): string
    {
        return match($this) {
            self::ADMIN => 'Quản trị viên',
            self::TEACHER => 'Giáo viên',
            self::STUDENT => 'Học sinh',
        };
    }
    
    public static function values(): array
    {
        return array_column(self::cases(), 'value');
    }
}
```

---

## 🔄 Sử Dụng

### Trong Service
```php
// ✅ Đúng
$user->role = UserRoleEnum::STUDENT->value;

if ($user->role === UserRoleEnum::ADMIN->value) {
    // logic...
}

// ❌ Sai
$user->role = 'student'; // Hardcode
if ($user->role === 'admin') { ... }
```

### Trong Model Cast
```php
use App\Enums\User\UserRoleEnum;

class User extends Model
{
    protected $casts = [
        'role' => UserRoleEnum::class,
    ];
}

// Sử dụng
$user->role; // Instance of UserRoleEnum
$user->role->value; // 'student'
$user->role->label(); // 'Học sinh'
```

### Trong Validation
```php
use Illuminate\Validation\Rule;
use App\Enums\User\UserRoleEnum;

public function rules()
{
    return [
        'role' => ['required', Rule::enum(UserRoleEnum::class)],
    ];
}
```

---

## 📚 Tái Sử Dụng

**TRƯỚC KHI** tạo Enum mới:

1. **Dò `/docs`** → Check Enum đã có chưa
2. **Nếu đã có** → Tái sử dụng
3. **Nếu chưa có** → Tạo mới VÀ cập nhật `/docs`

---

## 📋 Checklist

- [ ] Enum tên kết thúc bằng `Enum`
- [ ] Đặt đúng namespace domain
- [ ] Backed enum (string hoặc int)
- [ ] Có helper methods nếu cần (label, color, etc.)
- [ ] Cập nhật `/docs` liệt kê tất cả values

---

## 🔗 Related Patterns

- `service.md` - Service dùng Enum
- `practice-docs.md` - Document Enum trong /docs
