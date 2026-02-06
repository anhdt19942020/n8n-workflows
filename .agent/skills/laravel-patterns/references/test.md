# Test Pattern (Manual Debug Scripts)

> **Pattern**: Manual Testing & Debugging
> **Scope**: `scripts/**/*.php`, `tests/manual/**/*.php`
> **Priority**: P2 (Nice to Have)

---

## 🎯 Mục Đích

Khi cần **test/debug** logic nhanh của Repository, Service, Model → Tạo **manual debug script** thay vì unit test phức tạp.

---

## 📐 Cấu Trúc Script

### Template Chuẩn

```php
<?php

require_once 'vendor/autoload.php';

$app = require_once 'bootstrap/app.php';
$app->make('Illuminate\\Contracts\\Console\\Kernel')->bootstrap();

echo "=== Debugging [Component Name] ===\n\n";

try {
    // ========================
    // 1. SETUP
    // ========================
    $service = app(\App\Services\SomeService::class);
    
    // ========================
    // 2. TEST CASE 1
    // ========================
    echo "Test 1: [Description]\n";
    $result = $service->someMethod($param1, $param2);
    var_dump($result);
    echo "\n";
    
    // ========================
    // 3. TEST CASE 2
    // ========================
    echo "Test 2: [Description]\n";
    $result2 = $service->anotherMethod();
    print_r($result2);
    echo "\n";
    
} catch (\Throwable $e) {
    echo "❌ ERROR: " . $e->getMessage() . "\n";
    echo "File: " . $e->getFile() . ":" . $e->getLine() . "\n";
    echo "\nStack Trace:\n";
    echo $e->getTraceAsString() . "\n";
}

echo "\n=== Done ===\n";
```

---

## ✅ Ví Dụ Thực Tế

### Debug Repository

```php
<?php

require_once 'vendor/autoload.php';
$app = require_once 'bootstrap/app.php';
$app->make('Illuminate\\Contracts\\Console\\Kernel')->bootstrap();

echo "=== Debugging AcademicSlotPoolRepository ===\n\n";

try {
    $repo = app(\App\Repositories\AcademicSlotPoolRepository::class);
    
    // Test 1: Get pools by date and level
    echo "1. Test getPoolsWithCapacityByDateDurationAndLevel:\n";
    echo "   Params: date=2025-10-02, duration=90, level=null\n";
    $result = $repo->getPoolsWithCapacityByDateDurationAndLevel('2025-10-02', 90, null);
    echo "   Count: " . $result->count() . "\n";
    var_dump($result->toArray());
    echo "\n";
    
    // Test 2: Filter by level
    echo "2. Test getPoolsByDateDurationAndLevel:\n";
    echo "   Params: date=2025-10-02, duration=90, level=5\n";
    $result2 = $repo->getPoolsByDateDurationAndLevel('2025-10-02', 90, 5);
    echo "   Count: " . $result2->count() . "\n";
    var_dump($result2->toArray());
    
} catch (\Throwable $e) {
    echo "❌ Error: " . $e->getMessage() . "\n";
    echo "File: " . $e->getFile() . ":" . $e->getLine() . "\n";
}

echo "\n=== Done ===\n";
```

### Debug Service

```php
<?php

require_once 'vendor/autoload.php';
$app = require_once 'bootstrap/app.php';
$app->make('Illuminate\\Contracts\\Console\\Kernel')->bootstrap();

echo "=== Debugging TutorService ===\n\n";

try {
    $service = app(\App\Services\TutorService::class);
    
    // Test assign tutor
    echo "1. Test assignTutor:\n";
    $dto = new \App\DTOs\Tutor\AssignTutorDTO(
        userId: 12345,
        tutorId: 67890,
        startDate: '2025-02-01',
    );
    
    $result = $service->assignTutor($dto);
    echo "   Success: " . ($result ? 'YES' : 'NO') . "\n";
    
} catch (\Throwable $e) {
    echo "❌ Error: " . $e->getMessage() . "\n";
    echo "Trace: " . $e->getTraceAsString() . "\n";
}
```

---

## 📁 Naming Convention

```
scripts/debug_<component>.php
```

Ví dụ:
- `scripts/debug_slot_pool.php`
- `scripts/debug_tutor_service.php`
- `scripts/debug_exam_grading.php`

---

## 🔄 Chạy Script

```bash
# Windows
php scripts\debug_slot_pool.php

# Linux/Mac
php scripts/debug_slot_pool.php
```

---

## 📐 Best Practices

### 1. Nhóm Test Cases Rõ Ràng
```php
echo "=== TEST 1: Happy Path ===\n";
// ...

echo "\n=== TEST 2: Edge Case ===\n";
// ...

echo "\n=== TEST 3: Error Handling ===\n";
// ...
```

### 2. In Kết Quả Dễ Đọc
```php
// ✅ Đúng - Có context
echo "Test getActiveUsers:\n";
echo "  Input: status=active, limit=10\n";
echo "  Result count: " . $users->count() . "\n";

// ❌ Sai - Không context
var_dump($users);
```

### 3. Bao Bọc Try-Catch
```php
try {
    // Test logic
} catch (\Throwable $e) {
    echo "❌ Error: " . $e->getMessage() . "\n";
    echo "File: " . $e->getFile() . ":" . $e->getLine() . "\n";
    echo "\nFull Trace:\n" . $e->getTraceAsString() . "\n";
}
```

### 4. KHÔNG Dùng PHPUnit/Pest
Script này là **manual testing**, không phải automated test:

```php
// ❌ Sai - Đừng dùng PHPUnit
$this->assertEquals(...);

// ✅ Đúng - Just echo/var_dump
echo "Expected: 5, Got: " . $result . "\n";
```

---

## 📋 Checklist

Khi tạo debug script:

- [ ] Bootstrap Laravel đúng cách
- [ ] Có header/footer rõ ràng
- [ ] Nhóm test cases có tiêu đề
- [ ] Try-catch để bắt lỗi
- [ ] In kết quả có context
- [ ] Đặt tên file rõ ràng (`debug_<component>.php`)

---

## 🔗 Related Patterns

- `repository.md` - Test Repository methods
- `service.md` - Test Service logic
- `query.md` - Debug query filters
