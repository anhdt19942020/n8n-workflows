# Query Filter Pattern

> **Pattern**: Query Filtering & Dynamic Conditions
> **Scope**: `app/Repositories/**/*.php`, `app/Services/**/*.php`
> **Priority**: P1 (Important)

---

## 🎯 Mục Đích

Chuẩn hóa cách viết **query filter** để:
- ✅ Tránh duplicate code (`if (!empty(...))` lặp đi lặp lại)
- ✅ Dễ maintain và mở rộng
- ✅ Tái sử dụng logic filter

---

## ❌ Anti-Pattern (KHÔNG Làm)

```php
public function filter(array $filters)
{
    $query = $this->model->newQuery();
    
    if (!empty($filters['status'])) {
        $query->where('status', $filters['status']);
    }
    
    if (!empty($filters['name'])) {
        $query->where('name', 'like', '%' . $filters['name'] . '%');
    }
    
    if (!empty($filters['tutor_id'])) {
        $query->whereHas('academicTaskDetail', function($q) use ($filters) {
            $q->where('object_handle', $filters['tutor_id']);
        });
    }
    
    if (!empty($filters['date_from']) && !empty($filters['date_to'])) {
        $query->whereBetween('created_at', [$filters['date_from'], $filters['date_to']]);
    }
    
    // ... NHIỀU if (!empty()) ...
    
    return $query->paginate(20);
}
```

**Vấn đề**:
- Quá nhiều if/else
- Khó maintain
- Duplicate logic giữa các repository

---

## ✅ Chuẩn Pattern (QueryFilterService)

### Bước 1: Định Nghĩa FilterConditions

#### Cách 1: Trong Config Class
```php
namespace App\Configs\Filters;

use App\DTOs\FilterConditionDTO;
use App\Enums\FilterConditionType;

class AcademicTaskFilterConfig
{
    public static function conditions(): array
    {
        return [
            new FilterConditionDTO(
                key: 'status',
                keyDatabase: 'status',
                type: FilterConditionType::Equal,
            ),
            new FilterConditionDTO(
                key: 'name',
                keyDatabase: 'name',
                type: FilterConditionType::Like,
            ),
            new FilterConditionDTO(
                key: 'tutor_id',
                keyDatabase: 'object_handle',
                type: FilterConditionType::Equal,
                relationShip: 'academicTaskDetail',
            ),
            new FilterConditionDTO(
                key: 'created_at',
                keyDatabase: 'created_at',
                type: FilterConditionType::DateBetween,
            ),
        ];
    }
}
```

#### Cách 2: Private Method trong Repository
```php
private function getFilterConditions(): array
{
    return [
        new FilterConditionDTO(
            key: 'status',
            keyDatabase: 'status',
            type: FilterConditionType::Equal,
        ),
        // ...
    ];
}
```

---

### Bước 2: Áp Dụng Filter trong Repository

```php
use App\Services\QueryFilterService;
use App\Configs\Filters\AcademicTaskFilterConfig;

public function filter(array $filters)
{
    // 1. Define conditions
    $conditions = AcademicTaskFilterConfig::conditions();
    
    // 2. Start fresh query
    $query = $this->model->newQuery();
    
    // 3. Apply filters
    $query = app(QueryFilterService::class)->apply($query, $filters, $conditions);
    
    // 4. Additional logic (if needed)
    // $query->where('deleted_at', null);
    
    return $query->paginate(20);
}
```

---

## 📋 FilterConditionType (Enum)

| Type | Mô Tả | DB Query |
|------|-------|----------|
| `Equal` | So sánh bằng | `where('key', $value)` |
| `Like` | Tìm kiếm gần đúng | `where('key', 'like', "%$value%")` |
| `In` | Trong danh sách | `whereIn('key', $value)` |
| `Between` | Khoảng giá trị | `whereBetween('key', [$from, $to])` |
| `DateBetween` | Khoảng ngày | `whereBetween('key', [$dateFrom, $dateTo])` |
| `GreaterThan` | Lớn hơn | `where('key', '>', $value)` |
| `LessThan` | Nhỏ hơn | `where('key', '<', $value)` |
| `Custom` | Logic đặc biệt | Tự định nghĩa |

---

## 🔧 FilterConditionDTO

```php
new FilterConditionDTO(
    key: 'status',              // Key trong $filters array
    keyDatabase: 'status',      // Column trong DB
    type: FilterConditionType::Equal,
    relationShip: null,         // Null nếu query trực tiếp, 'relation' nếu whereHas
    customCallback: null,       // Closure cho Custom type
)
```

### Ví Dụ Với Relationship

```php
new FilterConditionDTO(
    key: 'tutor_id',
    keyDatabase: 'object_handle',
    type: FilterConditionType::Equal,
    relationShip: 'academicTaskDetail', // whereHas('academicTaskDetail', ...)
)
```

### Ví Dụ Với Custom Logic

```php
new FilterConditionDTO(
    key: 'complex_filter',
    keyDatabase: 'id',
    type: FilterConditionType::Custom,
    customCallback: function($query, $value) {
        return $query->where(function($q) use ($value) {
            $q->where('status', $value)
              ->orWhere('priority', '>', 5);
        });
    }
)
```

---

## 📐 Best Practices

### 1. Không Hardcode Type String
```php
// ❌ SAI
type: 'equal'

// ✅ ĐÚNG
type: FilterConditionType::Equal
```

### 2. Date Range Filter
```php
// Input format: ['date_from' => '2025-01-01', 'date_to' => '2025-12-31']
new FilterConditionDTO(
    key: 'created_at',
    keyDatabase: 'created_at',
    type: FilterConditionType::DateBetween,
)
```

### 3. Logic Phức Tạp (Không Tái Sử Dụng)
Nếu logic **chỉ dùng cho repo đó**:

```php
public function filter(array $filters)
{
    $conditions = $this->getFilterConditions();
    $query = $this->model->newQuery();
    
    // Apply common filters
    $query = app(QueryFilterService::class)->apply($query, $filters, $conditions);
    
    // Additional complex logic
    if (!empty($filters['special_case'])) {
        $query->where(function($q) use ($filters) {
            // Special logic here
        });
    }
    
    return $query->paginate(20);
}
```

---

## 📋 Checklist

Khi viết query/filter:

- [ ] KHÔNG viết nhiều `if (!empty(...))` trong Repository
- [ ] Dùng `FilterConditionDTO` + `FilterConditionType`
- [ ] Gọi `QueryFilterService::apply()` để build query
- [ ] Logic đặc biệt → Dùng `FilterConditionType::Custom` hoặc viết sau `apply()`
- [ ] KHÔNG hardcode type string

---

## 🔗 Related Patterns

- `repository.md` - Repository chứa filter logic
- `service.md` - Service gọi Repository filter
- `enum.md` - FilterConditionType là Enum
- `dto.md` - FilterConditionDTO
