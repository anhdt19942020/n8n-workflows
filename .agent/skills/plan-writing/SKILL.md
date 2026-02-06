---
name: plan-writing
description: Structured task planning with clear breakdowns, dependencies, and verification criteria. Use when implementing features, refactoring, or any multi-step work.
allowed-tools: Read, Glob, Grep
---

# Viết Kế Hoạch (Plan Writing)

> Nguồn: obra/superpowers

## Tổng Quan
Skill này cung cấp một khung làm việc để chia nhỏ công việc thành các tác vụ rõ ràng, có thể hành động với các tiêu chí xác minh.

## Nguyên Tắc Chia Nhỏ Tác Vụ

### 1. Tác Vụ Nhỏ, Tập Trung
- Mỗi tác vụ nên mất 2-5 phút
- Một kết quả rõ ràng cho mỗi tác vụ
- Có thể xác minh độc lập

### 2. Xác Minh Rõ Ràng
- Làm sao bạn biết nó đã xong?
- Bạn có thể kiểm tra/test cái gì?
- Đầu ra mong đợi là gì?

### 3. Sắp Xếp Logic
- Xác định các phụ thuộc (dependencies)
- Làm song song nếu có thể
- Làm nổi bật đường găng (critical path)
- **Giai đoạn X: Xác minh luôn là CUỐI CÙNG**

### 4. Đặt Tên Động Tại Project Root
- Các file kế hoạch được lưu dưới dạng `{task-slug}.md` tại PROJECT ROOT
- Tên được lấy từ tác vụ (ví dụ: "add auth" → `auth-feature.md`)
- **KHÔNG BAO GIỜ** lưu trong `.claude/`, `docs/`, hoặc các thư mục tạm

## Các Nguyên Tắc Lập Kế Hoạch (KHÔNG PHẢI Template!)

> 🔴 **KHÔNG dùng template cố định. Mỗi kế hoạch là DUY NHẤT cho tác vụ đó.**

### Nguyên Tắc 1: Giữ Nó NGẮN GỌN

| ❌ Sai | ✅ Đúng |
|--------|---------|
| 50 tác vụ với các sub-sub-task | Tối đa 5-10 tác vụ rõ ràng |
| Liệt kê mọi bước vi mô | Chỉ liệt kê các mục có thể hành động |
| Mô tả dài dòng | Một dòng cho mỗi tác vụ |

> **Quy Tắc:** Nếu kế hoạch dài hơn 1 trang, nó quá dài. Hãy đơn giản hóa.

---

### Nguyên Tắc 2: CỤ THỂ, Không Chung Chung

| ❌ Sai | ✅ Đúng |
|--------|---------|
| "Set up project" | "Chạy `npx create-next-app`" |
| "Add authentication" | "Cài next-auth, tạo `/api/auth/[...nextauth].ts`" |
| "Style the UI" | "Thêm Tailwind classes vào `Header.tsx`" |

> **Quy Tắc:** Mỗi tác vụ nên có một đầu ra rõ ràng, có thể xác minh.

---

### Nguyên Tắc 3: Nội Dung Động Dựa Trên Loại Dự Án

**Cho DỰ ÁN MỚI:**
- Tech stack là gì? (quyết định trước)
- MVP là gì? (tính năng tối thiểu)
- Cấu trúc file ra sao?

**Cho THÊM TÍNH NĂNG:**
- Những file nào bị ảnh hưởng?
- Cần dependencies nào?
- Làm sao để xác minh nó hoạt động?

**Cho SỬA BUG:**
- Nguyên nhân gốc rễ là gì?
- Sửa file/dòng nào?
- Làm sao để test bản sửa lỗi?

---

### Nguyên Tắc 4: Script Phải Cụ Thể Theo Dự Án

> 🔴 **ĐỪNG copy-paste các lệnh script. Hãy chọn dựa trên loại dự án.**

| Loại Dự Án | Script Liên Quan |
|------------|------------------|
| Frontend/React | `ux_audit.py`, `accessibility_checker.py` |
| Backend/API | `api_validator.py`, `security_scan.py` |
| Mobile | `mobile_audit.py` |
| Database | `schema_validator.py` |
| Full-stack | Kết hợp các script trên dựa trên những gì bạn chạm vào |

**Sai:** Thêm tất cả script vào mọi kế hoạch
**Đúng:** Chỉ script liên quan cho tác vụ NÀY

---

### Nguyên Tắc 5: Xác Minh Đơn Giản

| ❌ Sai | ✅ Đúng |
|--------|---------|
| "Check component works correctly" | "Chạy `npm run dev`, click nút, thấy toast hiện ra" |
| "Test the API" | "curl localhost:3000/api/users trả về 200" |
| "Check styles" | "Mở trình duyệt, xác minh dark mode toggle hoạt động" |

---

## Cấu Trúc Kế Hoạch (Linh Hoạt, Không Cố Định!)

```
# [Tên Tác Vụ]

## Mục Tiêu (Goal)
Một câu: Chúng ta đang xây dựng/sửa cái gì?

## Các Tác Vụ (Tasks)
- [ ] Task 1: [Hành động cụ thể] → Verify: [Cách kiểm tra]
- [ ] Task 2: [Hành động cụ thể] → Verify: [Cách kiểm tra]
- [ ] Task 3: [Hành động cụ thể] → Verify: [Cách kiểm tra]

## Hoàn Thành Khi (Done When)
- [ ] [Tiêu chí thành công chính]
```

> **Chỉ vậy thôi.** Không phases, không sub-sections trừ khi thực sự cần thiết.
> Giữ nó tối giản. Chỉ thêm sự phức tạp khi được yêu cầu.

## Ghi Chú
[Bất kỳ lưu ý quan trọng nào]
```

---

## Các Thực Hành Tốt Nhất (Tham Khảo Nhanh)

1. **Bắt đầu với mục tiêu** - Chúng ta đang xây dựng/sửa cái gì?
2. **Tối đa 10 tác vụ** - Nếu nhiều hơn, hãy chia thành nhiều kế hoạch
3. **Mỗi tác vụ đều xác minh được** - Tiêu chí "done" rõ ràng
4. **Cụ thể theo dự án** - Không copy-paste template
5. **Cập nhật khi làm** - Đánh dấu `[x]` khi hoàn thành

---

## Khi Nào Sử Dụng

- Dự án mới từ đầu
- Thêm tính năng
- Sửa bug (nếu phức tạp)
- Refactoring nhiều file
