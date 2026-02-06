# 🔍 Debug Report: Band Mismatch Analysis

**Date:** 2026-01-20  
**Issue:** Schedule Item có tester_id là admin band cao nhưng lại được gán vào tác vụ band thấp  
**Reporter:** User  
**Item ID Reference:** 2949830 (đã không tồn tại)

---

## 📋 1. Triệu Chứng

Trong bảng `test_input_schedule_items`:
- Có các trường hợp tester có `band_type = BAND_HIGH (1)` được gán vào test có `band_type = BAND_LOW (0)`
- Hoặc ngược lại: tester `BAND_LOW (0)` được gán vào test `BAND_HIGH (1)`

**Kết quả kiểm tra:** Tìm thấy **16 trường hợp** band mismatch trong 100 schedule items gần nhất.

---

## 🎯 2. Thông Tin Thu Thập Được

### 2.1. Cấu trúc Band Type

**File:** `app/Enums/TestInput/TestInputExamBand.php`

```php
enum TestInputExamBand: int
{
    case BAND_HIGH = 1;  // Band cao - Cho khách hàng Basic - IELTS 6.5
    case BAND_LOW = 0;   // Band thấp - Cho khách hàng IELTS 6.5+
}
```

**⚠️ Lưu ý quan trọng:** Tên gọi "BAND_HIGH" và "BAND_LOW" ngược với ý nghĩa:
- `BAND_HIGH (1)` = "Đề test dành cho khách hàng học **Basic - IELTS 6.5**" (mức thấp)
- `BAND_LOW (0)` = "Đề test dành cho khách hàng học **IELTS 6.5+**" (mức cao)

### 2.2. Logic Kiểm Tra Band

**Đã có validation:** 
- `TestInputService::validateTesterBandType()` (dòng 2513-2542)
- `TestInputScheduleItemService::isTaskMatchTesterBandType()` (dòng 67-97)

**Logic lọc tester:**
- `TestInputService::takeTesterRegisterWorking()` (dòng 3110-3136)
- `TestInputService::isTesterMatchBandType()` (dòng 3145-3161)

---

## 🔎 3. Giả Thuyết 

### ✅ Giả thuyết 1: Một số nơi gán tester KHÔNG validate band (NGUYÊN NHÂN GỐC RỄ)

**Kiểm tra:**

| Vị trí | File | Dòng | Có Validate? | Status |
|--------|------|------|-------------|--------|
| `assignAuto()` | TestInputService.php | 2495-2506 | ✅ CÓ | Safe |
| `swap()` | TestInputScheduleItemService.php | 178-193 | ✅ CÓ (qua `handleErrorSwap`) | Safe |
| `transferTaskAnotherTester()` | TestInputService.php | 1250-1277 | ❌ **KHÔNG** | **🔴 Vulnerable** |
| `autoAssignTestInput()` | TestInputService.php | 3409-3439 | ⚠️ Partial (filter trước) | Risky |
| Import/Migration | TestInputImportService.php | 218, 224 | ❌ **KHÔNG** | **🔴 Vulnerable** |

**Kết quả:** ✅ **Giả thuyết đúng**

### ❓ Giả thuyết 2: Band_type được thêm sau khi đã có data

**Kiểm tra migration:**
```
2025_11_17_155435_add_column_band_type_in_test_input_schedules_table.php
2026_01_02_145815_add_column_band_type_in_academic_admin_levels_table.php
```

**Kết quả:** ✅ **Đúng** - Band type là tính năng mới, data cũ có thể chưa được migrate đúng

### ❓ Giả thuyết 3: Admin có thể update thủ công qua UI

**Cần kiểm tra:** Controller methods có validate không?

---

## 🎯 4. Nguyên Nhân Gốc Rễ

### Nguyên nhân chính:

1. **`transferTaskAnotherTester()` không validate:**
   - Dòng 1268: `$taskOnline->update(['tester_id' => $newTesterId]);`
   - Có lọc tester theo band (dòng 1259-1261) nhưng **không validate trước khi update**
   - Nếu logic lọc có bug hoặc `$newTesterId` từ `priorityTester()` trả về sai → mismatch

2. **Import Service không validate:**
   - `TestInputImportService.php` dòng 218, 224
   - Import trực tiếp mà không check band compatibility

3. **Data migration thiếu:**
   - Khi thêm `band_type` vào `academic_admin_levels`, các record cũ có thể có giá trị mặc định `0` (BAND_LOW)
   - Nhưng tester thực tế có thể phải là BAND_HIGH

### Nguyên nhân phụ:

4. **`autoAssignTestInput()` dựa vào filter:**
   - Dựa vào `getTesterFreeTime()` đã filter band
   - Nhưng không có validation rõ ràng trước `update()`
   - Nếu filter có bug → mismatch

---

## 6. Sửa Lỗi

### 6.1. Fix `transferTaskAnotherTester()`

**File:** `app/Services/TestInput/TestInputService.php`  
**Dòng:** 1268

```php
// TRƯỚC (Có bug)
$taskOnline->update(['tester_id' => $newTesterId]);

// SAU (Đã fix)
$this->validateTesterBandType($taskOnline, $newTesterId);
$taskOnline->update(['tester_id' => $newTesterId]);
```

### 6.2. Fix `autoAssignTestInput()`

**File:** `app/Services/TestInput/TestInputService.php`  
**Dòng:** 3438

```php
// TRƯỚC
return $scheduleItem->update(['tester_id' => $firstTester['id']]);

// SAU
$this->validateTesterBandType($scheduleItem, $firstTester['id']);
return $scheduleItem->update(['tester_id' => $firstTester['id']]);
```

### 6.3. Fix Import Service

**File:** `app/Services/TestInput/TestInputImportService.php`  
**Dòng:** 218, 224

Cần thêm validation trước khi import.

### 6.4. Fix data hiện tại

Tạo script để:
1. Tìm tất cả mismatch
2. Hoặc unassign tester (set `tester_id = 0`)
3. Hoặc reassign tester phù hợp

---

## 7. Phòng Ngừa

### 7.1. Nguyên tắc

🛡️ **"Validate trước mọi assignment"**
- Tất cả nơi update `tester_id` phải gọi `validateTesterBandType()`
- Không chỉ dựa vào filter

### 7.2. Test Cases cần thêm

1. Test unit: `validateTesterBandType()` throw lỗi khi mismatch
2. Test integration: Tất cả API gán tester phải reject khi band không khớp
3. Regression test: Import không được tạo mismatch

### 7.3. Database Constraint

Cân nhắc thêm database trigger để ngăn insert/update mismatch (nếu performance cho phép).

### 7.4. Monitoring

Tạo command để scan định kỳ:
```bash
php artisan test-input:check-band-mismatch
```

---

## 📊 8. Tác Động

- **Severity:** 🔴 HIGH
- **Affected Records:** 16+ items (trong 100 gần nhất)
- **Business Impact:** Tester không phù hợp có thể chấm sai chuẩn
- **User Impact:** Học viên có thể nhận kết quả không chính xác

---

## ✅ 9. Kế Hoạch Hành Động

### Immediate (Ngay lập tức)
- [ ] Fix code theo section 6.1, 6.2
- [ ] Review tất cả nơi update `tester_id`
- [ ] Tạo script fix data hiện tại

### Short-term (1-2 ngày)
- [ ] Thêm validation vào Import Service
- [ ] Viết test cases
- [ ] Deploy fix lên staging

### Long-term (1 tuần)
- [ ] Review lại migration để đảm bảo data consistency
- [ ] Thêm monitoring/alert
- [ ] Document quy trình gán tester

---

## 📝 10. Notes

- ID 2949830 không tồn tại nữa (có thể đã bị xóa)
- Tìm thấy 16 cases khác có cùng vấn đề
- Logic filter trong `getTestFreeTime()` đã đúng, nhưng không đủ
- Cần validate ở **điểm gán cuối cùng**
