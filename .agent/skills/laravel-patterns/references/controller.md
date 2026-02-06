# Controller Pattern

> **Pattern**: Controller Layer Rules
> **Scope**: `app/Http/Controllers/**/*.php`
> **Priority**: P0 (Critical)

---

## 🎯 Nguyên Tắc

Controller **CHỈ ĐƯỢC**:
- ✅ Validate request (qua FormRequest)
- ✅ Gọi Service
- ✅ Trả về Response (theo chuẩn `ApiResponser`)

Controller **KHÔNG ĐƯỢC**:
- ❌ Viết business logic trực tiếp
- ❌ Gọi trực tiếp Model/Eloquent
- ❌ Viết query
- ❌ Chứa validation rules inline

---

## ✅ Đúng

```php
namespace App\Http\Controllers\Api;

use App\Http\Requests\User\CreateUserRequest;
use App\Services\UserService;
use App\Traits\ApiResponser;

class UserController extends Controller
{
    use ApiResponser;

    public function __construct(private UserService $userService) {}

    public function store(CreateUserRequest $request)
    {
        // ✅ Validate qua FormRequest
        // ✅ Gọi Service
        $user = $this->userService->createUser($request->validated());
        
        // ✅ Response chuẩn
        return $this->successResponse($user, 'User created successfully');
    }
}
```

---

## ❌ Sai

```php
public function store(Request $request)
{
    // ❌ Validate inline trong Controller
    $request->validate([
        'name' => 'required|string',
    ]);
    
    // ❌ Business logic trong Controller
    if ($request->role === 'admin') {
        // logic...
    }
    
    // ❌ Gọi trực tiếp Model
    $user = User::create($request->all());
    
    return response()->json($user);
}
```

---

## 📐 Chuẩn Response

Controller PHẢI dùng trait `App\Traits\ApiResponser`:

```php
use App\Traits\ApiResponser;

class SomeController extends Controller
{
    use ApiResponser;
    
    // Success
    return $this->successResponse($data, 'Message');
    
    // Error
    return $this->errorResponse('Error message', 400);
    
    // Paginated
    return $this->successResponse($paginator);
}
```

---

## 🔁 Workflow Chuẩn

```
Request → FormRequest (Validation)
            ↓
        Controller (Routing)
            ↓
        Service (Business Logic)
            ↓
        Repository (Query)
            ↓
        Model (Data)
```

Controller chỉ là **thin layer** kết nối HTTP layer với business logic.

---

## 📋 Checklist

Trước khi commit Controller, đảm bảo:

- [ ] Không có business logic trong Controller
- [ ] Validation qua FormRequest riêng
- [ ] Chỉ gọi Service, không gọi Model/Repository trực tiếp
- [ ] Response dùng ApiResponser trait
- [ ] Dependency injection Service qua constructor
- [ ] Method ngắn gọn (≤10 dòng)

---

## 🔗 Related Patterns

- `validation.md` - FormRequest rules
- `service.md` - Service layer
- `common.md` - Import, naming conventions
