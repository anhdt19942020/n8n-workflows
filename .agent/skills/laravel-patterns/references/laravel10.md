# Laravel 10 Best Practices

> **Pattern**: Laravel 10 Specific Features
> **Scope**: `app/**/*.php`, `tests/**/*.php`
> **Priority**: P1 (Important)

---

## 🎯 Mục Đích

Tận dụng tối đa **tính năng mới của Laravel 10** trong codebase.

---

## 1️⃣ Type Declarations

**Luôn** khai báo type cho property, argument, return.

```php
// ✅ Đúng
public function createUser(string $name, int $age): User
{
    return User::create(['name' => $name, 'age' => $age]);
}

// ❌ Sai
public function createUser($name, $age) // Không type
{
    return User::create(['name' => $name, 'age' => $age]);
}
```

**Tránh `mixed`** nếu có thể:
```php
// ✅ Đúng
public function getData(): array|Collection { ... }

// ❌ Sai (nếu có thể tránh)
public function getData(): mixed { ... }
```

---

## 2️⃣ Enum & Casts

### Tất cả status/type/role → Enum

```php
// Model
use App\Enums\User\UserRoleEnum;

class User extends Model
{
    protected $casts = [
        'role' => UserRoleEnum::class,
        'status' => UserStatusEnum::class,
    ];
}

// Usage
$user->role; // Instance of UserRoleEnum
$user->role->value; // 'admin'
$user->role->label(); // 'Quản trị viên'
```

---

## 3️⃣ Validation (FormRequest)

### Rule Objects

```php
use Illuminate\Validation\Rule;
use App\Enums\User\UserRoleEnum;

public function rules(): array
{
    return [
        'role' => ['required', Rule::enum(UserRoleEnum::class)],
        'email' => ['required', Rule::unique('users')->ignore($this->user)],
        'status' => ['required', Rule::when(
            $this->isAdmin(),
            ['required', 'in:active,inactive'],
            ['nullable']
        )],
    ];
}
```

---

## 4️⃣ Repository Query

### Modern Query Builder Methods

```php
// whenExists (Laravel 10)
$query->when($request->has('search'), function($q) use ($request) {
    $q->where('name', 'like', "%{$request->search}%");
});

// whereExists
$users = User::query()
    ->whereExists(function($query) {
        $query->select('id')
              ->from('posts')
              ->whereColumn('posts.user_id', 'users.id');
    })
    ->get();

// fullText (nếu có full-text index)
$posts = Post::query()
    ->whereFullText('title', $searchTerm)
    ->get();
```

---

## 5️⃣ Service & Jobs

### Job Queue

Tác vụ nặng → Job:

```php
use App\Jobs\SendWelcomeEmailJob;

public function createUser(CreateUserDTO $dto): User
{
    $user = $this->userRepository->create([...]);
    
    // ✅ Dispatch job (async)
    SendWelcomeEmailJob::dispatch($user);
    
    return $user;
}
```

### Job Batching

```php
use Illuminate\Support\Facades\Bus;
use App\Jobs\ProcessUserJob;

$users = User::all();

$batch = Bus::batch(
    $users->map(fn($user) => new ProcessUserJob($user))
)->dispatch();
```

---

## 6️⃣ Events & Listeners

### Auto-Discovery

Laravel 10 tự động discover Events/Listeners nếu đặt đúng namespace:

```php
// ✅ Không cần đăng ký thủ công nếu:
App\Events\UserRegisteredEvent
App\Listeners\SendWelcomeEmailListener // Tên khớp event
```

**Tuy nhiên**, vẫn khuyến nghị đăng ký trong `EventServiceProvider` để rõ ràng.

---

## 7️⃣ Testing

### Dùng Pest

```php
// tests/Feature/UserServiceTest.php
use App\Services\UserService;

it('creates user successfully', function() {
    $service = app(UserService::class);
    $dto = new CreateUserDTO('John', 'john@example.com');
    
    $user = $service->createUser($dto);
    
    expect($user)->toBeInstanceOf(User::class);
    expect($user->name)->toBe('John');
});

it('throws exception when email exists', function() {
    $service = app(UserService::class);
    $dto = new CreateUserDTO('John', 'existing@example.com');
    
    $service->createUser($dto);
})->throws(DomainException::class);
```

---

## 8️⃣ Process API

Chạy shell command qua `Process::run()`:

```php
use Illuminate\Support\Facades\Process;

// ✅ Đúng
$result = Process::run('ls -la');
echo $result->output();

if ($result->failed()) {
    throw new RuntimeException($result->errorOutput());
}

// ❌ Sai
exec('ls -la'); // Không dùng exec/shell_exec
```

---

## 9️⃣ Factory & Seeder

### Factory

```php
// database/factories/UserFactory.php
use App\Enums\User\UserRoleEnum;

public function definition(): array
{
    return [
        'name' => fake()->name(),
        'email' => fake()->unique()->safeEmail(),
        'role' => UserRoleEnum::STUDENT->value,
    ];
}

// State
public function admin(): static
{
    return $this->state(fn() => ['role' => UserRoleEnum::ADMIN->value]);
}
```

### Trong Test

```php
// ✅ Đúng
$user = User::factory()->create();
$admin = User::factory()->admin()->create();

// ❌ Sai - Không insert thủ công
User::create(['name' => 'Test', 'email' => 'test@example.com']);
```

---

## 🔟 Eager Load

Mọi relation **PHẢI** eager load, tránh N+1:

```php
// ✅ Đúng
$users = User::with('profile', 'orders')->get();

foreach ($users as $user) {
    echo $user->profile->bio; // Không query thêm
}

// ❌ Sai - Lazy loading
$users = User::all();

foreach ($users as $user) {
    echo $user->profile->bio; // N+1 query!
}
```

### Prevent Lazy Loading (Development)

```php
// app/Providers/AppServiceProvider.php
use Illuminate\Database\Eloquent\Model;

public function boot(): void
{
    Model::preventLazyLoading(!app()->isProduction());
}
```

---

## 1️⃣1️⃣ Documentation

Khi thêm tính năng Laravel 10 mới → **Update `/docs/laravel10.md`**.

---

## 📋 Checklist

Laravel 10 features checklist:

- [ ] Type declarations cho properties/methods
- [ ] Enum cho status/type/role + Model cast
- [ ] FormRequest với Rule objects
- [ ] Query builder dùng methods mới (whenExists, whereExists)
- [ ] Job cho tác vụ nặng
- [ ] Pest cho testing
- [ ] Process API cho shell commands
- [ ] Factory cho test data
- [ ] Eager load relations
- [ ] Prevent lazy loading trong dev

---

## 🔗 Related Patterns

- `enum.md` - Enum usage
- `validation.md` - FormRequest
- `service.md` - Job dispatch
- `test.md` - Testing patterns
