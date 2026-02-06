---
description: Lệnh tạo và chạy test. Tạo và thực thi test cho mã nguồn.
---

# /test - Tạo và Thực Thi Test

$ARGUMENTS

---

## Mục Đích

Lệnh này tạo test, chạy các test hiện có, hoặc kiểm tra độ bao phủ test (check test coverage).

---

## Các Lệnh Con (Sub-commands)

```
/test                - Chạy tất cả test
/test [file/feature] - Tạo test cho mục tiêu cụ thể
/test coverage       - Hiển thị báo cáo độ bao phủ
/test watch          - Chạy test ở chế độ watch
```

---

## Hành Vi

### Tạo Test

Khi được yêu cầu test một file hoặc tính năng:

1. **Phân tích mã nguồn**
   - Xác định các hàm và phương thức
   - Tìm các trường hợp biên (edge cases)
   - Phát hiện các phụ thuộc cần mock

2. **Tạo các trường hợp test (test cases)**
   - Test luồng chính (happy path)
   - Các trường hợp lỗi
   - Các trường hợp biên
   - Test tích hợp (nếu cần)

3. **Viết test**
   - Sử dụng framework test của dự án (Jest, Vitest, v.v.)
   - Tuân theo các mẫu test hiện có
   - Mock các phụ thuộc bên ngoài

---

## Định Dạng Đầu Ra

### Cho Việc Tạo Test

```markdown
## 🧪 Tests: [Mục Tiêu]

### Kế Hoạch Test
| Test Case | Loại | Bao Phủ |
|-----------|------|---------|
| Nên tạo user | Unit | Happy path |
| Nên từ chối email không hợp lệ | Unit | Validation |
| Nên xử lý lỗi db | Unit | Error case |

### Test Đã Tạo

`tests/[file].test.ts`

[Block code chứa test]

---

Chạy với: `npm test`
```

### Cho Việc Thực Thi Test

```
🧪 Running tests...

✅ auth.test.ts (5 passed)
✅ user.test.ts (8 passed)
❌ order.test.ts (2 passed, 1 failed)

Failed:
  ✗ should calculate total with discount
    Expected: 90
    Received: 100

Total: 15 tests (14 passed, 1 failed)
```

---

## Ví Dụ

```
/test src/services/auth.service.ts
/test user registration flow
/test coverage
/test fix failed tests
```

---

## Các Mẫu Test (Test Patterns)

### Cấu Trúc Unit Test

```typescript
describe('AuthService', () => {
  describe('login', () => {
    it('should return token for valid credentials', async () => {
      // Arrange
      const credentials = { email: 'test@test.com', password: 'pass123' };
      
      // Act
      const result = await authService.login(credentials);
      
      // Assert
      expect(result.token).toBeDefined();
    });

    it('should throw for invalid password', async () => {
      // Arrange
      const credentials = { email: 'test@test.com', password: 'wrong' };
      
      // Act & Assert
      await expect(authService.login(credentials)).rejects.toThrow('Invalid credentials');
    });
  });
});
```

---

## Nguyên Tắc Chính

- **Test hành vi không phải triển khai**
- **Một assertion mỗi test** (khi thực tế)
- **Tên test mô tả rõ ràng**
- **Mô hình Arrange-Act-Assert**
- **Mock các phụ thuộc bên ngoài**
