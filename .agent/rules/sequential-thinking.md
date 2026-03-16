---
trigger: always_on
---

# 🧠 GIAO THỨC BẮT BUỘC: MCP SEQUENTIAL THINKING

> **Quy tắc tối cao:** TRƯỚC KHI thực hiện BẤT KỲ hành động nào (viết code, sửa file, chạy lệnh, thiết kế, debug, trả lời câu hỏi phức tạp), bạn **PHẢI** sử dụng tool `mcp_sequential-thinking_sequentialthinking` để phân tích và lập kế hoạch.

---

## 🔴 QUY TẮC CỨNG (KHÔNG NGOẠI LỆ)

1. **KHÔNG BAO GIỜ** bắt đầu viết code, sửa file, hoặc chạy lệnh mà chưa qua Sequential Thinking
2. **KHÔNG BAO GIỜ** trả lời trực tiếp cho yêu cầu phức tạp mà chưa suy nghĩ có cấu trúc
3. **MỌI** quyết định kiến trúc, thiết kế, debug PHẢI được phân tích qua Sequential Thinking
4. Sequential Thinking phải được gọi **TRƯỚC** bất kỳ tool nào khác (trừ việc đọc file để thu thập context)

---

## 📋 MA TRẬN SỬ DỤNG THEO LOẠI YÊU CẦU

| Loại Yêu Cầu                 | Số Bước Tối Thiểu | Bắt Buộc?   | Ghi Chú                                                   |
| ---------------------------- | ----------------- | ----------- | --------------------------------------------------------- |
| **Tính năng mới / Xây dựng** | 5-8 bước          | ✅ BẮT BUỘC | Phân tích → Thiết kế → Kế hoạch → Rủi ro → Triển khai     |
| **Sửa bug / Debug**          | 3-5 bước          | ✅ BẮT BUỘC | Thu thập bằng chứng → Giả thuyết → Xác minh → Sửa         |
| **Refactor**                 | 4-6 bước          | ✅ BẮT BUỘC | Hiện trạng → Mục tiêu → Ảnh hưởng → Chiến lược → Kiểm tra |
| **Câu hỏi đơn giản**         | 2-3 bước          | ✅ BẮT BUỘC | Hiểu câu hỏi → Phân tích → Trả lời                        |
| **Khảo sát / Phân tích**     | 3-5 bước          | ✅ BẮT BUỘC | Phạm vi → Phương pháp → Thu thập → Tổng hợp               |
| **Thiết kế UI/UX**           | 5-7 bước          | ✅ BẮT BUỘC | Yêu cầu → Nghiên cứu → Concept → Chi tiết → Review        |
| **Deploy**                   | 4-6 bước          | ✅ BẮT BUỘC | Kiểm tra → Chuẩn bị → Thực thi → Xác minh                 |
| **Chào hỏi / Xã giao**       | 0 bước            | ❌ MIỄN     | Phản hồi trực tiếp                                        |

---

## 🔄 LUỒNG THỰC THI BẮT BUỘC

```
Nhận yêu cầu từ người dùng
    │
    ├── Yêu cầu xã giao? → Phản hồi trực tiếp
    │
    └── Mọi yêu cầu khác:
        │
        ├── 1️⃣ GỌI Sequential Thinking (Bước 1: Phân tích yêu cầu)
        │   └── Xác định: Loại yêu cầu, Phạm vi, Rủi ro, Dependencies
        │
        ├── 2️⃣ GỌI Sequential Thinking (Bước 2-N: Lập kế hoạch)
        │   └── Chiến lược, Các bước cụ thể, Edge cases
        │
        ├── 3️⃣ [Tùy chọn] Thu thập thêm context (đọc file, grep, v.v.)
        │
        ├── 4️⃣ GỌI Sequential Thinking (Bước tiếp: Xác minh kế hoạch)
        │   └── Kiểm tra lại kế hoạch, Điều chỉnh nếu cần
        │
        └── 5️⃣ THỰC THI (viết code, sửa file, chạy lệnh...)
```

---

## 🎯 CẤU TRÚC TỪNG BƯỚC SEQUENTIAL THINKING

### Bước 1: Phân Tích Yêu Cầu (LUÔN LUÔN BẮT ĐẦU TỪ ĐÂY)

```
- Người dùng muốn gì chính xác?
- Loại yêu cầu nào? (tính năng, bug, refactor, câu hỏi...)
- Phạm vi ảnh hưởng?
- Có thông tin nào còn thiếu không?
- Cần bao nhiêu bước suy nghĩ?
```

### Bước 2: Nghiên Cứu & Context

```
- Cần đọc file/code nào?
- Dependencies và side effects?
- Pattern hiện tại trong codebase?
- Có KI (Knowledge Item) nào liên quan?
```

### Bước 3: Thiết Kế Giải Pháp

```
- Các phương án khả thi?
- Trade-offs của từng phương án?
- Phương án tối ưu nhất?
- Edge cases cần xử lý?
```

### Bước 4: Kế Hoạch Triển Khai

```
- Thứ tự các bước cụ thể?
- File nào cần tạo/sửa?
- Test nào cần viết?
- Rollback plan?
```

### Bước 5+: Xác Minh & Điều Chỉnh

```
- Kế hoạch có bỏ sót gì không?
- Giả thuyết đã được kiểm chứng chưa?
- Cần điều chỉnh approach không?
- Sẵn sàng để thực thi?
```

---

## ⚡ SỬ DỤNG TÍNH NĂNG NÂNG CAO

### Revision (Sửa đổi suy nghĩ trước)

```
Khi phát hiện sai sót trong bước trước:
- isRevision: true
- revisesThought: <số bước cần sửa>
```

### Branching (Phân nhánh suy nghĩ)

```
Khi cần khám phá nhiều phương án song song:
- branchFromThought: <số bước gốc>
- branchId: "option-a" / "option-b"
```

### Mở rộng (Thêm bước khi cần)

```
Khi nhận ra cần phân tích sâu hơn:
- needsMoreThoughts: true
- Điều chỉnh totalThoughts lên
```

---

## 🚫 VI PHẠM & HẬU QUẢ

| Vi Phạm                                    | Mức Độ          | Hậu Quả                       |
| ------------------------------------------ | --------------- | ----------------------------- |
| Code mà không dùng Sequential Thinking     | 🔴 Nghiêm trọng | DỪNG ngay, bắt đầu lại với ST |
| Dùng ST nhưng chỉ 1 bước cho task phức tạp | 🟡 Cảnh báo     | Phải thêm bước phân tích      |
| Bỏ qua bước Xác Minh                       | 🟡 Cảnh báo     | Phải quay lại xác minh        |
| Không dùng Revision khi phát hiện sai      | 🟠 Trung bình   | Thiếu tự phản hồi             |

---

## 📝 VÍ DỤ MINH HỌA

### Ví dụ: Người dùng yêu cầu "Thêm API endpoint mới"

```
✅ ĐÚNG:
1. Sequential Thinking Bước 1: "User muốn thêm API endpoint.
   Cần xác định: endpoint path, method, request/response format,
   middleware, validation..."
2. Sequential Thinking Bước 2: "Kiểm tra các pattern hiện tại
   trong routes/backend.php, Controllers, Services..."
3. Sequential Thinking Bước 3: "Thiết kế: POST /api/xxx,
   cần Controller + Service + DTO..."
4. Sequential Thinking Bước 4: "Kế hoạch:
   a) Tạo DTO, b) Tạo Service method, c) Tạo Controller,
   d) Thêm route, e) Test"
5. → BẮT ĐẦU CODE

❌ SAI:
1. Đọc file route → Viết code luôn (KHÔNG có Sequential Thinking)
```

---

## 🔗 TÍCH HỢP VỚI CÁC QUY TẮC KHÁC

| Quy Tắc Hiện Tại  | Tích Hợp Sequential Thinking                            |
| ----------------- | ------------------------------------------------------- |
| Cổng Socratic     | ST chạy TRƯỚC Socratic Gate để chuẩn bị câu hỏi tốt hơn |
| Clean Code        | ST bao gồm bước kiểm tra Clean Code trước khi code      |
| File Dependencies | ST bao gồm bước phân tích dependencies                  |
| Agent Routing     | ST xác định agent phù hợp ở Bước 1                      |

---

> 🧠 **Nhớ:** Sequential Thinking không làm chậm quá trình - nó NGĂN NGỪA sai lầm và giúp tạo ra code chất lượng cao hơn ngay từ lần đầu tiên.
