---
name: systematic-debugging
description: 4-phase systematic debugging methodology with root cause analysis and evidence-based verification. Use when debugging complex issues.
allowed-tools: Read, Glob, Grep
---

# Gỡ Lỗi Có Hệ Thống (Systematic Debugging)

> Nguồn: obra/superpowers

## Tổng Quan
Skill này cung cấp một cách tiếp cận có cấu trúc để gỡ lỗi, ngăn chặn việc đoán mò ngẫu nhiên và đảm bảo vấn đề được hiểu đúng trước khi giải quyết.

## Quy Trình Gỡ Lỗi 4 Giai Đoạn

### Giai Đoạn 1: Tái Lập (Reproduce)
Trước khi sửa, hãy tái lập vấn đề một cách đáng tin cậy.

```markdown
## Các Bước Tái Lập
1. [Bước chính xác để tái lập]
2. [Bước tiếp theo]
3. [Kết quả mong đợi vs thực tế]

## Tỷ Lệ Tái Lập
- [ ] Luôn luôn (100%)
- [ ] Thường xuyên (50-90%)
- [ ] Đôi khi (10-50%)
- [ ] Hiếm khi (<10%)
```

### Giai Đoạn 2: Cô Lập (Isolate)
Thu hẹp nguồn gốc vấn đề.

```markdown
## Câu Hỏi Cô Lập
- Chuyện này bắt đầu xảy ra khi nào?
- Gần đây có gì thay đổi?
- Nó có xảy ra ở mọi môi trường không?
- Chúng ta có thể tái lập với code tối thiểu không?
- Thay đổi nhỏ nhất kích hoạt nó là gì?
```

### Giai Đoạn 3: Hiểu (Understand)
Tìm nguyên nhân gốc rễ, không chỉ là triệu chứng.

```markdown
## Phân Tích Nguyên Nhân Gốc Rễ
### 5 Whys (5 Tại Sao)
1. Tại sao: [Quan sát đầu tiên]
2. Tại sao: [Lý do sâu hơn]
3. Tại sao: [Sâu hơn nữa]
4. Tại sao: [Đang đến gần]
5. Tại sao: [Nguyên nhân gốc rễ]
```

### Giai Đoạn 4: Sửa & Xác Minh (Fix & Verify)
Sửa và xác minh nó thực sự đã được sửa.

```markdown
## Xác Minh Bản Sửa Lỗi
- [ ] Bug không còn tái lập
- [ ] Chức năng liên quan vẫn hoạt động
- [ ] Không có vấn đề mới nào được đưa vào
- [ ] Đã thêm test để ngăn chặn hồi quy (regression)
```

## Checklist Gỡ Lỗi

```markdown
## Trước Khi Bắt Đầu
- [ ] Có thể tái lập nhất quán
- [ ] Có trường hợp tái lập tối thiểu
- [ ] Hiểu hành vi mong đợi

## Trong Khi Điều Tra
- [ ] Kiểm tra các thay đổi gần đây (git log)
- [ ] Kiểm tra logs tìm lỗi
- [ ] Thêm logging nếu cần
- [ ] Dùng debugger/breakpoints

## Sau Khi Sửa
- [ ] Nguyên nhân gốc rễ đã được tài liệu hóa
- [ ] Bản sửa lỗi đã được xác minh
- [ ] Regression test đã được thêm
- [ ] Code tương tự đã được kiểm tra
```

## Các Lệnh Gỡ Lỗi Phổ Biến

```bash
# Các thay đổi gần đây
git log --oneline -20
git diff HEAD~5

# Tìm kiếm pattern
grep -r "errorPattern" --include="*.ts"

# Kiểm tra logs
pm2 logs app-name --err --lines 100
```

## Anti-Patterns

❌ **Thay đổi ngẫu nhiên** - "Có lẽ nếu mình đổi cái này..."
❌ **Phớt lờ bằng chứng** - "Đó không thể là nguyên nhân được"
❌ **Giả định** - "Nó chắc chắn là X" mà không có bằng chứng
❌ **Không tái lập trước** - Sửa mù quáng
❌ **Dừng lại ở triệu chứng** - Không tìm ra nguyên nhân gốc rễ
