---
name: clean-code
description: Pragmatic coding standards - concise, direct, no over-engineering, no unnecessary comments
allowed-tools: Read, Write, Edit
version: 2.0
priority: CRITICAL
---

# Clean Code - Tiêu Chuẩn Coding AI Thực Dụng

> **KỸ NĂNG QUAN TRỌNG** - Hãy **ngắn gọn, trực tiếp, và tập trung vào giải pháp**.

---

## Các Nguyên Tắc Cốt Lõi (Core Principles)

| Nguyên Tắc | Quy Tắc |
|------------|---------|
| **SRP** | Single Responsibility - mỗi hàm/lớp chỉ làm MỘT việc |
| **DRY** | Don't Repeat Yourself - tách code trùng lặp, tái sử dụng |
| **KISS** | Keep It Simple - giải pháp đơn giản nhất có thể hoạt động |
| **YAGNI** | You Aren't Gonna Need It - đừng xây dựng tính năng chưa cần dùng |
| **Boy Scout** | Để lại code sạch hơn lúc bạn tìm thấy nó |

---

## Quy Tắc Đặt Tên (Naming Rules)

| Thành Phần | Quy Ước |
|------------|---------|
| **Variables** | Thể hiện ý định: `userCount` thay vì `n` |
| **Functions** | Verb + noun: `getUserById()` thay vì `user()` |
| **Booleans** | Dạng câu hỏi: `isActive`, `hasPermission`, `canEdit` |
| **Constants** | SCREAMING_SNAKE: `MAX_RETRY_COUNT` |

> **Quy Tắc:** Nếu bạn cần comment để giải thích một cái tên, hãy đổi tên nó.

---

## Quy Tắc Hàm (Function Rules)

| Quy Tắc | Mô Tả |
|---------|-------|
| **Small** | Tối đa 20 dòng, lý tưởng là 5-10 |
| **One Thing** | Làm một việc, làm thật tốt việc đó |
| **One Level** | Một cấp độ trừu tượng cho mỗi hàm |
| **Few Args** | Tối đa 3 tham số, ưu tiên 0-2 |
| **No Side Effects** | Không làm biến đổi đầu vào một cách bất ngờ |

---

## Cấu Trúc Code (Code Structure)

| Mẫu (Pattern) | Áp Dụng |
|---------------|---------|
| **Guard Clauses** | Return sớm cho các trường hợp biên (edge cases) |
| **Flat > Nested** | Tránh lồng nhau sâu (tối đa 2 cấp) |
| **Composition** | Các hàm nhỏ kết hợp lại với nhau |
| **Colocation** | Giữ code liên quan ở gần nhau |

---

## Phong Cách Coding AI

| Tình Huống | Hành Động |
|------------|-----------|
| Người dùng yêu cầu tính năng | Viết nó trực tiếp |
| Người dùng báo lỗi (bug) | Sửa nó, không giải thích |
| Không rõ yêu cầu | Hỏi, đừng giả định |

---

## Anti-Patterns (ĐỪNG LÀM)

| ❌ Pattern | ✅ Cách Sửa |
|------------|-------------|
| Comment mỗi dòng | Xóa các comment hiển nhiên |
| Helper cho code 1 dòng | Inline code đó luôn |
| Factory cho 2 objects | Khởi tạo trực tiếp (Direct instantiation) |
| utils.ts với 1 hàm | Đặt code ở nơi sử dụng |
| "Đầu tiên chúng ta import..." | Chỉ cần viết code thôi |
| Deep nesting | Dùng Guard clauses |
| Magic numbers | Dùng Named constants |
| God functions | Tách theo trách nhiệm (Split by responsibility) |

---

## 🔴 Trước Khi Sửa BẤT KỲ File Nào (NGHĨ TRƯỚC!)

**Trước khi thay đổi một file, hãy tự hỏi:**

| Câu Hỏi | Tại Sao |
|---------|---------|
| **Cái gì import file này?** | Chúng có thể bị lỗi |
| **File này import cái gì?** | Thay đổi interface |
| **Test nào cover file này?** | Test có thể fail |
| **Đây có phải component dùng chung?** | Nhiều nơi bị ảnh hưởng |

**Kiểm Tra Nhanh:**
```
File cần sửa: UserService.ts
└── Ai import nó? → UserController.ts, AuthController.ts
└── Họ có cần thay đổi không? → Kiểm tra function signatures
```

> 🔴 **Quy Tắc:** Sửa file + tất cả các file phụ thuộc trong CÙNG một task.
> 🔴 **Không bao giờ để lại broken imports hoặc thiếu cập nhật.**

---

## Tóm Tắt

| Nên Làm (Do) | Đừng Làm (Don't) |
|--------------|------------------|
| Viết code trực tiếp | Viết hướng dẫn (tutorials) |
| Để code tự tài liệu hóa | Thêm comment hiển nhiên |
| Sửa lỗi ngay lập tức | Giải thích cách sửa trước |
| Inline những thứ nhỏ | Tạo file không cần thiết |
| Đặt tên rõ ràng | Dùng từ viết tắt |
| Giữ hàm nhỏ gọn | Viết hàm dài hơn 100 dòng |

> **Ghi nhớ: Người dùng muốn code chạy được, không phải một bài học lập trình.**

---

## 🔴 Tự Kiểm Tra Trước Khi Hoàn Thành (BẮT BUỘC)

**Trước khi nói "tác vụ hoàn tất", hãy xác minh:**

| Kiểm Tra | Câu Hỏi |
|----------|---------|
| ✅ **Đạt mục tiêu?** | Tôi đã làm chính xác những gì người dùng yêu cầu chưa? |
| ✅ **Đã sửa file?** | Tôi đã sửa đổi tất cả các file cần thiết chưa? |
| ✅ **Code hoạt động?** | Tôi đã test/xác minh thay đổi chưa? |
| ✅ **Không có lỗi?** | Lint và TypeScript có pass không? |
| ✅ **Không bỏ sót?** | Có trường hợp biên (edge cases) nào bị sót không? |

> 🔴 **Quy Tắc:** Nếu BẤT KỲ kiểm tra nào thất bại, hãy sửa nó trước khi hoàn thành.

---

## Verification Scripts (BẮT BUỘC)

> 🔴 **QUAN TRỌNG:** Mỗi agent CHỈ chạy script của skill của chính họ sau khi hoàn thành công việc.

### Ánh Xạ Agent → Script

| Agent | Script | Lệnh |
|-------|--------|------|
| **frontend-specialist** | UX Audit | `python ~/.claude/skills/frontend-design/scripts/ux_audit.py .` |
| **frontend-specialist** | A11y Check | `python ~/.claude/skills/frontend-design/scripts/accessibility_checker.py .` |
| **backend-specialist** | API Validator | `python ~/.claude/skills/api-patterns/scripts/api_validator.py .` |
| **mobile-developer** | Mobile Audit | `python ~/.claude/skills/mobile-design/scripts/mobile_audit.py .` |
| **database-architect** | Schema Validate | `python ~/.claude/skills/database-design/scripts/schema_validator.py .` |
| **security-auditor** | Security Scan | `python ~/.claude/skills/vulnerability-scanner/scripts/security_scan.py .` |
| **seo-specialist** | SEO Check | `python ~/.claude/skills/seo-fundamentals/scripts/seo_checker.py .` |
| **seo-specialist** | GEO Check | `python ~/.claude/skills/geo-fundamentals/scripts/geo_checker.py .` |
| **performance-optimizer** | Lighthouse | `python ~/.claude/skills/performance-profiling/scripts/lighthouse_audit.py <url>` |
| **test-engineer** | Test Runner | `python ~/.claude/skills/testing-patterns/scripts/test_runner.py .` |
| **test-engineer** | Playwright | `python ~/.claude/skills/webapp-testing/scripts/playwright_runner.py <url>` |
| **Any agent** | Lint Check | `python ~/.claude/skills/lint-and-validate/scripts/lint_runner.py .` |
| **Any agent** | Type Coverage | `python ~/.claude/skills/lint-and-validate/scripts/type_coverage.py .` |
| **Any agent** | i18n Check | `python ~/.claude/skills/i18n-localization/scripts/i18n_checker.py .` |

> ❌ **SAI:** `test-engineer` chạy `ux_audit.py`
> ✅ **ĐÚNG:** `frontend-specialist` chạy `ux_audit.py`

---

### 🔴 Xử Lý Output Của Script (ĐỌC → TÓM TẮT → HỎI)

**Khi chạy script validation, bạn PHẢI:**

1. **Chạy script** và bắt tất cả output
2. **Parse output** - xác định errors, warnings, và passes
3. **Tóm tắt cho người dùng** theo định dạng này:

```markdown
## Script Results: [script_name.py]

### ❌ Errors Found (X items)
- [File:Line] Mô tả lỗi 1
- [File:Line] Mô tả lỗi 2

### ⚠️ Warnings (Y items)
- [File:Line] Mô tả cảnh báo

### ✅ Passed (Z items)
- Kiểm tra 1 đã qua
- Kiểm tra 2 đã qua

**Tôi có nên sửa X lỗi này không?**
```

4. **Chờ người dùng xác nhận** trước khi sửa
5. **Sau khi sửa** → Chạy lại script để xác nhận

> 🔴 **VI PHẠM:** Chạy script và phớt lờ output = THẤT BẠI tác vụ.
> 🔴 **VI PHẠM:** Tự động sửa mà không hỏi = Không được phép.
> 🔴 **Quy Tắc:** Luôn ĐỌC output → TÓM TẮT → HỎI → sau đó mới sửa.
