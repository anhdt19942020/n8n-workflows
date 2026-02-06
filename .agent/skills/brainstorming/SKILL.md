---
name: brainstorming
description: Socratic questioning protocol + user communication. MANDATORY for complex requests, new features, or unclear requirements. Includes progress reporting and error handling.
allowed-tools: Read, Glob, Grep
---

# Brainstorming & Giao Thức Giao Tiếp

> **BẮT BUỘC:** Sử dụng cho các yêu cầu phức tạp/mơ hồ, tính năng mới, cập nhật.

---

## 🛑 CỔNG SOCRATIC (THỰC THI)

### Khi Nào Kích Hoạt

| Mẫu (Pattern) | Hành Động |
|---------------|-----------|
| "Build/Create/Make [thing]" mà thiếu chi tiết | 🛑 HỎI 3 câu hỏi |
| Tính năng phức tạp hoặc kiến trúc | 🛑 Làm rõ trước khi triển khai |
| Yêu cầu cập nhật/thay đổi | 🛑 Xác nhận phạm vi |
| Yêu cầu mơ hồ | 🛑 Hỏi mục đích, người dùng, ràng buộc |

### 🚫 BẮT BUỘC: 3 Câu Hỏi Trước Khi Triển Khai

1. **DỪNG** - ĐỪNG bắt đầu code
2. **HỎI** - Tối thiểu 3 câu hỏi:
   - 🎯 Purpose (Mục đích): Bạn đang giải quyết vấn đề gì?
   - 👥 Users (Người dùng): Ai sẽ sử dụng cái này?
   - 📦 Scope (Phạm vi): Phải có (Must-have) hay nên có (nice-to-have)?
3. **CHỜ** - Nhận phản hồi rồi mới tiếp tục

---

## 🧠 Tạo Câu Hỏi Động (Dynamic Question Generation)

**⛔ KHÔNG BAO GIỜ dùng template tĩnh.** Đọc `dynamic-questioning.md` để hiểu nguyên tắc.

### Các Nguyên Tắc Cốt Lõi

| Nguyên Tắc | Ý Nghĩa |
|------------|---------|
| **Questions Reveal Consequences** | Mỗi câu hỏi kết nối với một quyết định kiến trúc |
| **Context Before Content** | Hiểu ngữ cảnh greenfield/feature/refactor/debug trước |
| **Minimum Viable Questions** | Mỗi câu hỏi phải giúp loại bỏ bớt các hướng triển khai |
| **Generate Data, Not Assumptions** | Đừng đoán—hãy hỏi cùng với các sự đánh đổi (trade-offs) |

### Quy Trình Tạo Câu Hỏi

```
1. Phân tích yêu cầu → Trích xuất domain, tính năng, chỉ số quy mô
2. Xác định điểm quyết định → Chặn (Blocking) vs. có thể hoãn
3. Tạo câu hỏi → Ưu tiên: P0 (chặn) > P1 (đòn bẩy cao) > P2 (nice-to-have)
4. Định dạng với sự đánh đổi → Cái gì, Tại sao, Các lựa chọn, Mặc định
```

### Định Dạng Câu Hỏi (BẮT BUỘC)

```markdown
### [PRIORITY] **[DECISION POINT]**

**Câu hỏi:** [Câu hỏi rõ ràng]

**Tại Sao Điều Này Quan Trọng:**
- [Hệ quả kiến trúc]
- [Ảnh hưởng: chi phí/độ phức tạp/thời gian/quy mô]

**Các Lựa Chọn:**
| Option | Ưu | Nhược | Phù Hợp Nhất Cho |
|--------|----|-------|-------------------|
| A | [+] | [-] | [Trường hợp sử dụng] |

**Nếu Không Được Chỉ Định:** [Mặc định + lý do]
```

**Để có ngân hàng câu hỏi và thuật toán cụ thể theo domain**, xem: `dynamic-questioning.md`

---

## Báo Cáo Tiến Độ (DỰA TRÊN NGUYÊN TẮC)

**NGUYÊN TẮC:** Sự minh bạch xây dựng niềm tin. Trạng thái phải hiển thị rõ và có thể hành động.

### Định Dạng Bảng Trạng Thái

| Agent | Trạng Thái | Tác Vụ Hiện Tại | Tiến Độ |
|-------|------------|-----------------|---------|
| [Tên Agent] | ✅🔄⏳❌⚠️ | [Mô tả tác vụ] | [% hoặc số lượng] |

### Biểu Tượng Trạng Thái

| Icon | Ý Nghĩa | Cách Dùng |
|------|---------|-----------|
| ✅ | Hoàn thành | Tác vụ xong thành công |
| 🔄 | Đang chạy | Đang thực thi |
| ⏳ | Đang chờ | Bị chặn, chờ dependency |
| ❌ | Lỗi | Thất bại, cần chú ý |
| ⚠️ | Cảnh báo | Vấn đề tiềm ẩn, không chặn |

---

## Xử Lý Lỗi (DỰA TRÊN NGUYÊN TẮC)

**NGUYÊN TẮC:** Lỗi là cơ hội để giao tiếp rõ ràng.

### Mẫu Phản Hồi Khi Có Lỗi

```
1. Ghi nhận lỗi
2. Giải thích chuyện gì đã xảy ra (thân thiện với người dùng)
3. Đưa ra các giải pháp cụ thể với sự đánh đổi (trade-offs)
4. Hỏi người dùng chọn hoặc cung cấp phương án thay thế
```

### Các Loại Lỗi

| Loại | Chiến Lược Phản Hồi |
|------|---------------------|
| **Xung đột Port** | Đề xuất port khác hoặc đóng port hiện tại |
| **Thiếu Dependency** | Tự động cài đặt hoặc xin phép |
| **Build Thất Bại** | Hiển thị lỗi cụ thể + gợi ý sửa |
| **Lỗi Không Rõ** | Hỏi chi tiết: screenshot, console output |

---

## Thông Điệp Hoàn Thành (DỰA TRÊN NGUYÊN TẮC)

**NGUYÊN TẮC:** Ăn mừng thành công, hướng dẫn các bước tiếp theo.

### Cấu Trúc Hoàn Thành

```
1. Xác nhận thành công (chúc mừng ngắn gọn)
2. Tóm tắt những gì đã làm (cụ thể)
3. Cách xác minh/kiểm thử (có thể hành động ngay)
4. Đề xuất bước tiếp theo (chủ động)
```

---

## Các Nguyên Tắc Giao Tiếp

| Nguyên Tắc | Triển Khai |
|------------|------------|
| **Ngắn gọn** | Không chi tiết thừa, đi thẳng vào vấn đề |
| **Trực quan** | Dùng emoji (✅🔄⏳❌) để quét nhanh |
| **Cụ thể** | "~2 phút" thay vì "đợi một chút" |
| **Phương án thay thế** | Đưa ra nhiều hướng khi bị kẹt |
| **Chủ động** | Gợi ý bước tiếp theo sau khi hoàn thành |

---

## Anti-Patterns (TRÁNH)

| Anti-Pattern | Tại Sao |
|--------------|---------|
| Nhảy vào giải pháp trước khi hiểu | Lãng phí thời gian vào sai vấn đề |
| Giả định yêu cầu mà không hỏi | Tạo ra đầu ra sai |
| Over-engineering phiên bản đầu tiên | Làm chậm việc chuyển giao giá trị |
| Phớt lờ các ràng buộc | Tạo ra giải pháp không dùng được |
| Cụm từ "Tôi nghĩ" | Không chắc chắn → Hãy hỏi thay vì đoán |

---
