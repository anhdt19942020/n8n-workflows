# ZNS Template Pattern (Zalo Notification Service)

> **Pattern**: Zalo ZNS Template Management
> **Scope**: `app/Libraries/Templates/**/*.php`, `app/Abstracts/Zalo/**/*.php`
> **Priority**: P2 (Nice to Have)

---

## 🎯 Mục Đích

Chuẩn hóa cách tạo và gửi **Zalo ZNS notification template** trong dự án.

---

## 🏗️ Cấu Trúc

### 1. Template Class
Kế thừa `ZaloTemplate` hoặc abstract con (`ZaloIeltsMentorTemplate`).

**Phải có**:
```php
public int $template_id;          // ID template từ ZNS OA
public IDataTemplate $template_data;  // Data object
```

---

## ✅ Tạo Template Mới

### Template Class

```php
namespace App\Libraries\Templates\Tutors;

use App\Abstracts\Zalo\ZaloIeltsMentorTemplate;
use App\Libraries\TemplateData\Tutors\TutorAssignedDataTemplate;
use App\Contracts\IDataTemplate;

class TutorAssignedTemplate extends ZaloIeltsMentorTemplate
{
    public int $template_id = 123456; // ID từ ZNS OA
    public IDataTemplate $template_data;

    public function __construct(
        string $customerName,
        int $userId,
        string $phone,
        string $tutorName
    ) {
        $this->setData($customerName, $userId, $phone, $tutorName);
    }

    public function setData(
        string $customerName,
        int $userId,
        string $phone,
        string $tutorName
    ): void {
        $this->template_data = new TutorAssignedDataTemplate(
            $customerName,
            $userId,
            $phone,
            $tutorName
        );
    }
}
```

---

## 📦 Data Template

Đặt trong `App\Libraries\TemplateData\<Domain>\*DataTemplate.php`.

### Implement `IDataTemplate`

```php
namespace App\Libraries\TemplateData\Tutors;

use App\Contracts\IDataTemplate;

class TutorAssignedDataTemplate implements IDataTemplate
{
    public function __construct(
        public string $customerName,
        public int $userId,
        public string $phone,
        public string $tutorName
    ) {}

    public function toArray(): array
    {
        return [
            'customer_name' => $this->customerName,
            'user_id' => (string) $this->userId, // ZNS yêu cầu string
            'phone' => $this->phone,
            'tutor_name' => $this->tutorName,
        ];
    }
}
```

**⚠️ Chú ý**:
- Field trong `toArray()` **PHẢI khớp** placeholder của ZNS template
- ZNS thường yêu cầu **string**, cast int → string

---

## 🚀 Gửi Tin Nhắn

### Gửi Ngay (Sync)

```php
use App\Libraries\Templates\Tutors\TutorAssignedTemplate;

$template = new TutorAssignedTemplate(
    customerName: 'Nguyễn Văn A',
    userId: 12345,
    phone: '0912345678',
    tutorName: 'Trần Thị B'
);

$template->send('0912345678');
```

### Gửi Sau (Schedule)

```php
use Carbon\Carbon;

$sendAt = Carbon::parse('2025-02-01 09:00:00');

$template->sendLater('0912345678', $sendAt);
```

---

## 📐 Best Practices

### 1. Naming Convention

```php
// Template class
XxxTemplate.php

// Data class
XxxDataTemplate.php

// Ví dụ:
TutorAssignedTemplate.php
TutorAssignedDataTemplate.php
```

### 2. Template ID Chính Xác

```php
// ✅ Đúng - ID từ ZNS OA
public int $template_id = 123456;

// ❌ Sai - ID giả
public int $template_id = 0;
```

### 3. Field Khớp Placeholder

ZNS Template có placeholder: `{{customer_name}}`, `{{user_id}}`

→ `toArray()` phải return:
```php
[
    'customer_name' => '...',
    'user_id' => '...',
]
```

### 4. Không Override send/sendLater

```php
// ❌ SAI - Đừng override
public function send($phone) {
    // Custom logic
}

// ✅ ĐÚNG - Dùng method có sẵn từ parent
$template->send($phone);
```

---

## 🔄 Integration với Service

```php
namespace App\Services;

use App\Libraries\Templates\Tutors\TutorAssignedTemplate;

class TutorService
{
    public function assignTutor(int $tutorId, int $studentId): void
    {
        // Business logic
        $student = $this->userRepository->find($studentId);
        $tutor = $this->userRepository->find($tutorId);
        
        $this->tutorRepository->update($studentId, ['tutor_id' => $tutorId]);
        
        // Send ZNS
        $template = new TutorAssignedTemplate(
            customerName: $student->name,
            userId: $student->id,
            phone: $student->phone,
            tutorName: $tutor->name
        );
        
        $template->send($student->phone);
    }
}
```

---

## 📋 Checklist

Khi tạo ZNS template:

- [ ] Template class kế thừa `ZaloTemplate` hoặc abstract con
- [ ] Có `public int $template_id` (ID từ ZNS OA)
- [ ] Có `public IDataTemplate $template_data`
- [ ] Data class implement `IDataTemplate`
- [ ] `toArray()` fields khớp placeholder ZNS
- [ ] Tên class theo convention (`XxxTemplate`, `XxxDataTemplate`)
- [ ] Không override `send()` hoặc `sendLater()`

---

## 🔗 Related Patterns

- `dto.md` - Data structure pattern
- `service.md` - Service gọi template
- `event-listener.md` - Có thể gửi ZNS trong Listener
