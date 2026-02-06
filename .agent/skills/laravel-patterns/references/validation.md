# Validation Pattern

> **Pattern**: Request Validation
> **Scope**: `app/Http/Requests/**/*.php`
> **Priority**: P0 (Critical)

---

## 🎯 Nguyên Tắc

- ✅ Mọi validation **PHẢI** tách riêng vào FormRequest
- ❌ **KHÔNG** viết validation rules trực tiếp trong Controller
- ✅ FormRequest tự động validate trước khi vào Controller method

---

## ✅ Ví Dụ Chuẩn

```php
namespace App\Http\Requests\User;

use Illuminate\Foundation\Http\FormRequest;
use Illuminate\Validation\Rule;
use App\Enums\User\UserRoleEnum;

class CreateUserRequest extends FormRequest
{
    public function authorize(): bool
    {
        // Authorization logic
        return true;
    }

    public function rules(): array
    {
        return [
            'name' => 'required|string|max:255',
            'email' => 'required|email|unique:users,email',
            'password' => 'required|string|min:8|confirmed',
            'role' => ['required', Rule::enum(UserRoleEnum::class)],
        ];
    }

    public function messages(): array
    {
        return [
            'name.required' => 'Tên không được để trống',
            'email.unique' => 'Email đã tồn tại',
        ];
    }
}
```

---

## 🔄 Sử Dụng

```php
// Controller
public function store(CreateUserRequest $request)
{
    // Request đã được validate tự động
    $validated = $request->validated();
    
    $dto = CreateUserDTO::fromRequest($validated);
    $user = $this->userService->createUser($dto);
    
    return $this->successResponse($user);
}
```

---

## 📐 Best Practices

### 1. Dùng Rule Objects
```php
use Illuminate\Validation\Rule;

public function rules(): array
{
    return [
        'status' => ['required', Rule::in(['active', 'inactive'])],
        'role' => ['required', Rule::enum(UserRoleEnum::class)],
        'email' => ['required', Rule::unique('users')->ignore($this->user)],
    ];
}
```

### 2. Conditional Rules
```php
use Illuminate\Validation\Rule;

public function rules(): array
{
    return [
        'type' => 'required|string',
        'tutor_id' => [
            Rule::when(
                $this->input('type') === 'tutor',
                ['required', 'exists:users,id'],
                ['nullable']
            )
        ],
    ];
}
```

### 3. Custom Error Messages
```php
public function messages(): array
{
    return [
        'name.required' => 'Vui lòng nhập tên',
        'email.email' => 'Email không đúng định dạng',
        'password.min' => 'Mật khẩu phải có ít nhất :min ký tự',
    ];
}
```

---

## ❌ Anti-Patterns

```php
// ❌ SAI - Validation trong Controller
public function store(Request $request)
{
    $request->validate([
        'name' => 'required|string',
    ]);
    // ...
}

// ❌ SAI - Validation trong Service
public function createUser(array $data)
{
    $validator = Validator::make($data, [
        'name' => 'required',
    ]);
    // ...
}
```

---

## 📋 Checklist

- [ ] Tạo FormRequest riêng cho mỗi action
- [ ] Tên Request rõ ràng (`CreateUserRequest`, `UpdateOrderRequest`)
- [ ] Đặt trong namespace phù hợp (`App\Http\Requests\<Domain>\`)
- [ ] Dùng Rule objects thay vì string
- [ ] Có custom messages (tiếng Việt)
- [ ] Controller KHÔNG có validation logic

---

## 🔗 Related Patterns

- `controller.md` - Controller dùng FormRequest
- `dto.md` - Convert validated to DTO
- `enum.md` - Validate Enum với Rule::enum()
