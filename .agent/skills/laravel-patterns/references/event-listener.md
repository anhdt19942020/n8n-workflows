# Event & Listener Pattern

> **Pattern**: Domain Events (Event-Driven Architecture)
> **Scope**: `app/Events/**/*.php`, `app/Listeners/**/*.php`
> **Priority**: P2 (Nice to Have)

---

## 🎯 Nguyên Tắc

Event-Listener giúp **decoupling** logic:
- Event = **Điều gì đã xảy ra** (past tense)
- Listener = **Xử lý phản ứng** khi event xảy ra

---

## 📁 Cấu Trúc Theo Domain

```
App/Events/
├── Tutors/
│   ├── TutorAssignedEvent.php
│   └── TutorRemovedEvent.php
├── Academic/
│   ├── ExamCompletedEvent.php
│   └── GradeUpdatedEvent.php

App/Listeners/
├── Tutors/
│   ├── SendTutorAssignedNotificationListener.php
│   └── UpdateTutorStatisticsListener.php
├── Academic/
│   ├── SendExamResultEmailListener.php
│   └── RecalculateOverallScoreListener.php
```

---

## ✅ Tạo Event

### Naming
- Tên class = **hành động (past tense) + Event**
- Ví dụ: `TutorAssignedEvent`, `ExamCompletedEvent`, `UserRegisteredEvent`

### Code Example
```php
namespace App\Events\Tutors;

use Illuminate\Foundation\Events\Dispatchable;
use Illuminate\Queue\SerializesModels;

class TutorAssignedEvent
{
    use Dispatchable, SerializesModels;

    public function __construct(
        public int $tutorId,
        public int $studentId,
        public string $assignedAt
    ) {}
}
```

**Quy tắc**:
- Chỉ chứa **data cần thiết**
- Public properties (PHP 8.1+)
- Không chứa logic

---

## ✅ Tạo Listener

### Naming
- Tên class = **Hành động xử lý + Listener**
- Ví dụ: `SendTutorAssignedNotificationListener`, `UpdateStatisticsListener`

### Code Example
```php
namespace App\Listeners\Tutors;

use App\Events\Tutors\TutorAssignedEvent;
use App\Services\NotificationService;

class SendTutorAssignedNotificationListener
{
    public function __construct(
        private NotificationService $notificationService
    ) {}

    public function handle(TutorAssignedEvent $event): void
    {
        $this->notificationService->sendTutorAssignedEmail(
            tutorId: $event->tutorId,
            studentId: $event->studentId,
            assignedAt: $event->assignedAt
        );
    }
}
```

**Quy tắc**:
- Method `handle()` nhận Event
- Có thể inject Service/Repository
- **Logic nằm trong Service**, Listener chỉ orchestrate

---

## 🔄 Đăng Ký Event-Listener

### app/Providers/EventServiceProvider.php

```php
protected $listen = [
    \App\Events\Tutors\TutorAssignedEvent::class => [
        \App\Listeners\Tutors\SendTutorAssignedNotificationListener::class,
        \App\Listeners\Tutors\UpdateTutorStatisticsListener::class,
    ],
    
    \App\Events\Academic\ExamCompletedEvent::class => [
        \App\Listeners\Academic\SendExamResultEmailListener::class,
        \App\Listeners\Academic\RecalculateOverallScoreListener::class,
    ],
];
```

**Laravel 10 Auto-Discovery**:
Nếu đặt đúng namespace, có thể không cần đăng ký thủ công.

---

## 🚀 Dispatch Event

### Trong Service

```php
use App\Events\Tutors\TutorAssignedEvent;

class TutorService
{
    public function assignTutor(int $tutorId, int $studentId): void
    {
        // Business logic
        $this->tutorRepository->update($studentId, ['tutor_id' => $tutorId]);
        
        // Dispatch event
        event(new TutorAssignedEvent(
            tutorId: $tutorId,
            studentId: $studentId,
            assignedAt: now()->toIso8601String()
        ));
    }
}
```

---

## ⚡ Queue Listener (Async)

Nếu Listener xử lý **nặng** (send email, call API) → Queue:

```php
use Illuminate\Contracts\Queue\ShouldQueue;

class SendTutorAssignedNotificationListener implements ShouldQueue
{
    public function handle(TutorAssignedEvent $event): void
    {
        // Heavy logic - chạy async trong queue
        $this->notificationService->sendEmail(...);
    }
}
```

---

## 📐 Best Practices

### 1. Event = Data Contract
```php
// ✅ Đúng - Chỉ data
class TutorAssignedEvent {
    public function __construct(
        public int $tutorId,
        public int $studentId,
    ) {}
}

// ❌ Sai - Chứa logic
class TutorAssignedEvent {
    public function sendNotification() { ... }
}
```

### 2. Listener = Logic Handler
```php
// ✅ Đúng - Gọi Service
public function handle(TutorAssignedEvent $event): void
{
    $this->service->doSomething($event->tutorId);
}

// ❌ Sai - Logic phức tạp trong Listener
public function handle(TutorAssignedEvent $event): void
{
    // 100 dòng logic...
}
```

### 3. Nhóm Theo Domain
```php
// ✅ Đúng
App\Events\Tutors\TutorAssignedEvent
App\Listeners\Tutors\SendTutorAssignedNotificationListener

// ❌ Sai - Không phân loại
App\Events\TutorAssignedEvent
App\Listeners\SendEmailListener
```

### 4. Listener Nặng → Queue
```php
// ✅ Đúng - Email/SMS/API call → Queue
class SendEmailListener implements ShouldQueue { ... }

// ❌ Sai - Đồng bộ làm chậm request
class SendEmailListener { ... }
```

---

## 📋 Checklist

Khi tạo Event/Listener:

- [ ] Event tên past tense + hậu tố `Event`
- [ ] Listener tên hành động + hậu tố `Listener`
- [ ] Event chỉ chứa data, không logic
- [ ] Listener gọi Service, không viết logic phức tạp
- [ ] Nhóm theo domain (Tutors, Academic, ...)
- [ ] Listener nặng → implement `ShouldQueue`
- [ ] Đăng ký trong `EventServiceProvider`

---

## 🔗 Related Patterns

- `service.md` - Service dispatch Event
- `enum.md` - Event data dùng Enum
- `dto.md` - Event data có thể là DTO
