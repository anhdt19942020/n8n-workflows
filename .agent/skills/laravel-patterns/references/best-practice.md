# Best Practice - Control Flow

> **Pattern**: Clean Code & Control Flow
> **Scope**: `app/**/*.php`
> **Priority**: P0 (Critical)
> **Always Apply**: true

---

## 🎯 Mục Đích

Giảm độ phức tạp của code bằng cách:
- ✅ Giảm `if/else`
- ✅ Giảm độ lồng nhau (nesting)
- ✅ Code dễ đọc, dễ maintain

---

## 1️⃣ Guard Clause / Early Return

Ưu tiên **return sớm** để giảm lồng nhau.

### ✅ Đúng

```php
public function processOrder(Order $order): void
{
    if (!$order->isPaid()) {
        return; // Early return
    }
    
    if ($order->isShipped()) {
        return; // Early return
    }
    
    // Happy path - không lồng sâu
    $this->shipOrder($order);
    $this->sendNotification($order);
}
```

### ❌ Sai

```php
public function processOrder(Order $order): void
{
    if ($order->isPaid()) {
        if (!$order->isShipped()) {
            // Lồng 2 cấp
            $this->shipOrder($order);
            $this->sendNotification($order);
        }
    }
}
```

---

## 2️⃣ Cấm `else` Sau `return`

Nếu nhánh `if` đã `return`, **KHÔNG dùng `else`**.

### ✅ Đúng

```php
public function getDiscount(User $user): float
{
    if ($user->isPremium()) {
        return 0.2;
    }
    
    if ($user->isRegular()) {
        return 0.1;
    }
    
    return 0.0;
}
```

### ❌ Sai

```php
public function getDiscount(User $user): float
{
    if ($user->isPremium()) {
        return 0.2;
    } else { // ❌ else không cần thiết
        if ($user->isRegular()) {
            return 0.1;
        } else {
            return 0.0;
        }
    }
}
```

---

## 3️⃣ Giới Hạn Độ Lồng

**Không lồng `if` quá 1 cấp**.

### ✅ Đúng - Tách Method

```php
public function processUser(User $user): void
{
    if (!$this->canProcess($user)) {
        return;
    }
    
    $this->doProcess($user);
}

private function canProcess(User $user): bool
{
    return $user->isActive() 
        && $user->hasPermission('process')
        && !$user->isBanned();
}
```

### ❌ Sai - Lồng Sâu

```php
public function processUser(User $user): void
{
    if ($user->isActive()) {
        if ($user->hasPermission('process')) {
            if (!$user->isBanned()) {
                // Lồng 3 cấp!
                $this->doProcess($user);
            }
        }
    }
}
```

---

## 4️⃣ Tách Điều Kiện Thành Method

Đặt tên theo **ý định**, không để điều kiện dài.

### ✅ Đúng

```php
public function completeExam(Exam $exam): void
{
    if (!$this->canComplete($exam)) {
        throw new DomainException("Cannot complete exam");
    }
    
    if ($this->shouldMoveToGrading($exam)) {
        $this->moveToGrading($exam);
    }
    
    $this->markAsCompleted($exam);
}

private function canComplete(Exam $exam): bool
{
    return $exam->status === ExamStatusEnum::IN_PROGRESS->value
        && $exam->endTime <= now();
}

private function shouldMoveToGrading(Exam $exam): bool
{
    return $exam->type === ExamTypeEnum::RETAKE->value
        && $exam->hasAllAnswers();
}
```

### ❌ Sai - Điều Kiện Dài

```php
public function completeExam(Exam $exam): void
{
    if ($exam->status === ExamStatusEnum::IN_PROGRESS->value && $exam->endTime <= now()) {
        // Điều kiện dài, khó đọc
        if ($exam->type === ExamTypeEnum::RETAKE->value && $exam->hasAllAnswers()) {
            $this->moveToGrading($exam);
        }
        $this->markAsCompleted($exam);
    }
}
```

---

## 5️⃣ Strategy Pattern (Thay Thế if/else)

Khi logic thay đổi theo **enum type/status** → Dùng Strategy.

### ❌ Sai - Nhiều if/else

```php
public function calculateScore(Exam $exam): float
{
    if ($exam->type === ExamTypeEnum::RETAKE->value) {
        // Logic retake
        return $this->calculateRetakeScore($exam);
    } elseif ($exam->type === ExamTypeEnum::REGULAR->value) {
        // Logic regular
        return $this->calculateRegularScore($exam);
    } elseif ($exam->type === ExamTypeEnum::FINAL->value) {
        // Logic final
        return $this->calculateFinalScore($exam);
    }
    
    throw new DomainException("Unknown exam type");
}
```

### ✅ Đúng - Strategy Pattern

```php
// Interface
interface ScoreCalculatorInterface
{
    public function calculate(Exam $exam): float;
}

// Implementations
class RetakeScoreCalculator implements ScoreCalculatorInterface { ... }
class RegularScoreCalculator implements ScoreCalculatorInterface { ... }
class FinalScoreCalculator implements ScoreCalculatorInterface { ... }

// Service
public function calculateScore(Exam $exam): float
{
    $calculator = $this->resolveCalculator($exam->type);
    return $calculator->calculate($exam);
}

private function resolveCalculator(string $type): ScoreCalculatorInterface
{
    return match($type) {
        ExamTypeEnum::RETAKE->value => app(RetakeScoreCalculator::class),
        ExamTypeEnum::REGULAR->value => app(RegularScoreCalculator::class),
        ExamTypeEnum::FINAL->value => app(FinalScoreCalculator::class),
        default => throw new DomainException("Unknown type"),
    };
}
```

---

## 6️⃣ `match` Chỉ Cho Mapping Đơn Giản

**KHÔNG viết logic dài** trong `match`.

### ✅ Đúng - Mapping Class

```php
$handler = match($type) {
    'create' => CreateHandler::class,
    'update' => UpdateHandler::class,
    default => DefaultHandler::class,
};

return app($handler)->handle($data);
```

### ❌ Sai - Logic Trong match

```php
$result = match($type) {
    'create' => (function() use ($data) {
        // 20 dòng logic...
        $this->validate($data);
        $this->create($data);
        return $this->format($data);
    })(),
    'update' => (function() use ($data) {
        // 30 dòng logic...
    })(),
};
```

---

## 7️⃣ Ràng Buộc Định Lượng

### Quy Tắc Cứng

Mỗi **public method** trong Service:
- ✅ Tối đa **2 câu lệnh if**
- ✅ Nếu vượt → Refactor sang private method hoặc strategy class

### Ví Dụ

```php
// ✅ Đúng - Chỉ 2 if
public function processTask(Task $task): void
{
    if (!$this->canProcess($task)) { // If 1
        return;
    }
    
    if ($this->needsValidation($task)) { // If 2
        $this->validate($task);
    }
    
    $this->doProcess($task);
}

// ❌ Sai - Quá 2 if
public function processTask(Task $task): void
{
    if (!$task->isActive()) { ... }      // If 1
    if ($task->type === 'A') { ... }     // If 2
    if ($task->userId > 0) { ... }       // If 3 ❌
    if ($task->hasData()) { ... }        // If 4 ❌
}
```

---

## 📋 Checklist

Trước khi commit code:

- [ ] Dùng guard clause/early return
- [ ] KHÔNG có `else` sau `return`
- [ ] Không lồng `if` quá 1 cấp
- [ ] Điều kiện phức tạp tách thành method boolean
- [ ] Logic theo type/status → Strategy pattern
- [ ] `match` chỉ mapping đơn giản
- [ ] Mỗi public method ≤ 2 câu lệnh `if`

---

## 🔗 Related Patterns

- `service.md` - Service clean code
- `common.md` - Common coding rules
- `repository.md` - Query complexity
