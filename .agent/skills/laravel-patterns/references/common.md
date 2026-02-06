# Common Rules

> **Pattern**: Global Coding Standards
> **Scope**: `app/**/*.php`, `docs/**/*.md`
> **Priority**: P0 (Critical)
> **Always Apply**: true

---

## 🎯 Nguyên Tắc Chung

Các quy tắc này áp dụng cho **TẤT CẢ** code trong dự án.

---

## 1️⃣ Import Class (Use Statements)

### ❌ KHÔNG Dùng FQN (Fully Qualified Name)

```php
// ❌ Sai - FQN trong code
$dto = new \App\DTOs\Academic\TutorTask\TutorTaskScheduleOverviewInputDTO();
$enum = \App\Enums\User\UserRoleEnum::ADMIN;
```

### ✅ Dùng `use` Statement

```php
// ✅ Đúng
use App\DTOs\Academic\TutorTask\TutorTaskScheduleOverviewInputDTO;
use App\Enums\User\UserRoleEnum;

$dto = new TutorTaskScheduleOverviewInputDTO();
$enum = UserRoleEnum::ADMIN;
```

---

## 2️⃣ Đặt Tên Biến Rõ Ràng

### ❌ KHÔNG Viết Tắt Vô Nghĩa

```php
// ❌ Sai - Không hiểu
$slotStartC = Carbon::createFromFormat('H:i', $slotStart);
$slotEndC = Carbon::createFromFormat('H:i', $slotEnd);
$usrNm = $user->name;
```

### ✅ Tên Biến Có Nghĩa

```php
// ✅ Đúng
$slotStartTime = Carbon::createFromFormat('H:i', $slotStart);
$slotEndTime = Carbon::createFromFormat('H:i', $slotEnd);
$userName = $user->name;
```

---

## 3️⃣ Response Structure (Hạn Chế Nested Keys)

### ❌ KHÔNG Dùng Nested Object Keys

```php
// ❌ Sai - Key-based structure
"action_buttons": {
    "visible": true,
    "cancel": {
        "enabled": false,
        "enable_at": "2025-09-14T15:31:00+07:00",
        "tooltip": "Chưa tới thời gian hủy ca"
    },
    "complete": {
        "enabled": false,
        "enable_at": "2025-09-14T16:40:00+07:00",
        "tooltip": "Chưa tới thời gian hoàn thành"
    },
    "join_class": {
        "enabled": true
    }
}
```

**Vấn đề**: Khó iterate, frontend phải hardcode keys.

### ✅ Dùng Array of Objects

```php
// ✅ Đúng - Array structure
"action_buttons": [
    {
        "name": "cancel",
        "enabled": false,
        "enable_at": "2025-09-14T15:31:00+07:00",
        "tooltip": "Chưa tới thời gian hủy ca"
    },
    {
        "name": "complete",
        "enabled": false,
        "enable_at": "2025-09-14T16:40:00+07:00",
        "tooltip": "Chưa tới thời gian hoàn thành"
    },
    {
        "name": "join_class",
        "enabled": true
    }
]
```

**Benefit**: 
- Frontend có thể `map()`, `filter()`
- Không cần hardcode keys
- Dễ thêm/bớt buttons

---

## 4️⃣ Phân Tầng Nghiêm Ngặt (CORE RULE)

### Architecture Layers

```
Controller → Service → Repository → Model
```

### ❌ VI PHẠM

```php
// ❌ Controller gọi trực tiếp Model
class UserController
{
    public function index()
    {
        $users = User::where('active', true)->get(); // ❌
    }
}

// ❌ Service viết query trực tiếp
class UserService
{
    public function getActiveUsers()
    {
        return User::where('active', true)->get(); // ❌ Phải qua Repository
    }
}

// ❌ Repository chứa business logic
class UserRepository
{
    public function createPremiumUser($data)
    {
        // Calculate discount... ❌ Logic này nằm trong Service
        // Send email... ❌ Logic này nằm trong Service/Listener
        return User::create($data);
    }
}
```

### ✅ ĐÚNG

```php
// ✅ Controller
class UserController
{
    public function index()
    {
        $users = $this->userService->getActiveUsers();
        return $this->successResponse($users);
    }
}

// ✅ Service
class UserService
{
    public function getActiveUsers()
    {
        return $this->userRepository->getActive(); // Qua Repository
    }
}

// ✅ Repository
class UserRepository
{
    public function getActive()
    {
        return $this->model->newQuery()
            ->where('active', true)
            ->get();
    }
}
```

---

## 5️⃣ Database Safety 🔴 CRITICAL

### TUYỆT ĐỐI CẤM

```php
// 🔴 CẤM - Xóa bảng
Schema::drop('users');
DB::statement('DROP TABLE users');

// 🔴 CẤM - Xóa database
DB::statement('DROP DATABASE edutalk');

// 🔴 CẤM - RefreshDatabase trong test
use Illuminate\Foundation\Testing\RefreshDatabase;

class UserTest extends TestCase
{
    use RefreshDatabase; // 🔴 CẤM TUYỆT ĐỐI
}

// 🔴 CẤM - Truncate trong production
DB::table('users')->truncate();
```

### ✅ ĐƯỢC PHÉP

```php
// ✅ Soft delete
User::where('id', $id)->delete(); // Soft delete (nếu có SoftDeletes)

// ✅ Selective delete
User::where('created_at', '<', now()->subYears(5))->delete();

// ✅ Seeder (không destructive)
User::factory(10)->create();
```

---

## 6️⃣ Refactor Before Fix

Khi fix bug, tối ưu, hoặc thêm code:

### 🔍 Checklist

1. ✅ **Kiểm tra** code hiện tại có đúng cấu trúc không?
2. ✅ **Nếu SAI** → Refactor lại TRƯỚC khi fix bug
3. ❌ **KHÔNG** build logic mới lên code sai cấu trúc

### Ví Dụ

```php
// Code hiện tại (SAI - Logic trong Controller)
class TaskController
{
    public function complete($id)
    {
        $task = Task::find($id);
        if ($task->status === 'pending') {
            $task->status = 'completed';
            $task->save();
        }
        return response()->json($task);
    }
}

// ❌ SAI - Fix bug mà không refactor
class TaskController
{
    public function complete($id)
    {
        $task = Task::find($id);
        if ($task->status === 'pending') {
            $task->status = 'completed';
            $task->completed_at = now(); // Thêm logic mới
            $task->save();
        }
        return response()->json($task);
    }
}

// ✅ ĐÚNG - Refactor trước, sau đó fix bug
// 1. Refactor
class TaskController
{
    public function complete($id)
    {
        $task = $this->taskService->complete($id);
        return $this->successResponse($task);
    }
}

class TaskService
{
    public function complete(int $id): Task
    {
        $task = $this->taskRepository->find($id);
        
        if ($task->status !== 'pending') {
            throw new DomainException("Cannot complete task");
        }
        
        return $this->taskRepository->update($id, [
            'status' => 'completed',
            'completed_at' => now(), // Bây giờ mới thêm logic mới
        ]);
    }
}
```

---

## 📋 Checklist Toàn Cục

Trước khi commit bất kỳ code nào:

- [ ] KHÔNG dùng FQN, dùng `use` statement
- [ ] Tên biến rõ ràng, không viết tắt vô nghĩa
- [ ] Response structure dùng array of objects, không nested keys
- [ ] Phân tầng đúng (Controller → Service → Repository)
- [ ] KHÔNG xóa bảng/database, KHÔNG `RefreshDatabase`
- [ ] Code sai cấu trúc → Refactor trước khi fix bug

---

## 🔗 Related Patterns

- `controller.md` - Controller rules
- `service.md` - Service rules
- `repository.md` - Repository rules
- `best-practice.md` - Clean code practices
