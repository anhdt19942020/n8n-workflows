# Task: Thêm cột loại thi vào AcademicProctoringResource

Thêm trường `exam_type` và `exam_type_label` vào `AcademicProctoringResource` để phân biệt các loại thi dựa trên enum `App\Enums\Academic\Marking\ExamRetake\Type`.

## Thay đổi dự kiến:

### 1. Cập nhật Model `MarkingExamRetake`
- Cast trường `type` sang Enum `App\Enums\Academic\Marking\ExamRetake\Type`.

### 2. Cập nhật Resource `AcademicProctoringResource`
- Thêm trường `exam_type` lấy từ `markingExamRetake->type`.
- Thêm trường `exam_type_label` lấy từ `markingExamRetake->type->labelCustom()`.

## Chi tiết triển khai:

### Bước 1: Model `App\Models\MarkingExamRetake`
Thêm cast:
```php
protected $casts = [
    'type' => Type::class,
];
```

### Bước 2: Resource `App\Http\Resources\Academic\AcademicProctoringResource`
Cập nhật method `toArray`:
```php
'exam_type' => $this->markingExamRetake?->type,
'exam_type_label' => $this->markingExamRetake?->type?->labelCustom(),
```

## Xác nhận:
- Bạn có muốn tôi thực hiện cả việc cast trong model không? (Việc này sẽ giúp code sạch hơn và tái sử dụng được ở nhiều nơi).
- Bạn có muốn tôi cập nhật cả `AcademicTaskResource` hoặc các resource khác liên quan không?
