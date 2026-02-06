---
description: Lệnh debug. Kích hoạt chế độ DEBUG để điều tra vấn đề một cách có hệ thống.
---

# /debug - Điều Tra Vấn Đề Có Hệ Thống

$ARGUMENTS

---

## Mục Đích

Lệnh này kích hoạt chế độ DEBUG để điều tra có hệ thống các vấn đề, lỗi hoặc hành vi không mong muốn.

---

## Hành Vi

Khi `/debug` được kích hoạt:

1. **Thu thập thông tin**
   - Thông báo lỗi
   - Các bước tái hiện
   - Hành vi mong đợi vs thực tế
   - Các thay đổi gần đây

2. **Hình thành giả thuyết**
   - Liệt kê các nguyên nhân có thể
   - Sắp xếp theo khả năng xảy ra

3. **Điều tra có hệ thống**
   - Kiểm tra từng giả thuyết
   - Kiểm tra logs, luồng dữ liệu
   - Sử dụng phương pháp loại trừ

4. **Sửa lỗi và ngăn chặn**
   - Áp dụng bản sửa lỗi
   - Giải thích nguyên nhân gốc rễ
   - Thêm các biện pháp phòng ngừa

5. **Generate Git Commit Message** (Chỉ Backend)
   - Nếu là backend code, tự động tạo commit message
   - Đọc `@[skills/git-commit-helper]`
   - Format: `fix(<scope>): <summary>`
   - Đề xuất và chờ xác nhận

---

## Định Dạng Đầu Ra

```markdown
## 🔍 Debug: [Vấn đề]

### 1. Triệu chứng
[Chuyện gì đang xảy ra]

### 2. Thông Tin Thu Thập Được
- Lỗi: `[thông báo lỗi]`
- File: `[đường dẫn file]`
- Dòng: [số dòng]

### 3. Giả Thuyết
1. ❓ [Nguyên nhân khả thi nhất]
2. ❓ [Khả năng thứ hai]
3. ❓ [Nguyên nhân ít khả thi hơn]

### 4. Điều Tra

**Kiểm tra giả thuyết 1:**
[Tôi đã kiểm tra gì] → [Kết quả]

**Kiểm tra giả thuyết 2:**
[Tôi đã kiểm tra gì] → [Kết quả]

### 5. Nguyên Nhân Gốc Rễ
🎯 **[Giải thích tại sao điều này xảy ra]**

### 6. Sửa Lỗi
```[language]
// Trước
[code bị lỗi]

// Sau
[code đã sửa]
```

### 7. Phòng Ngừa
🛡️ [Cách ngăn chặn điều này trong tương lai]
```

---

## Ví Dụ

```
/debug login not working
/debug API returns 500
/debug form doesn't submit
/debug data not saving
```

---

## Nguyên Tắc Chính

- **Hỏi trước khi giả định** - lấy đầy đủ ngữ cảnh lỗi
- **Kiểm tra giả thuyết** - không đoán mò
- **Giải thích tại sao** - không chỉ là sửa cái gì
- **Ngăn chặn tái diễn** - thêm test, validation
- **Backend: Auto-generate commit** - tự động tạo message với type `fix`

