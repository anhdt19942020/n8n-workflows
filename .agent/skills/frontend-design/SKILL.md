---
name: frontend-design
description: Design thinking and decision-making for web UI. Use when designing components, layouts, color schemes, typography, or creating aesthetic interfaces. Teaches principles, not fixed values.
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
---

# Hệ Thống Thiết Kế Frontend

> **Triết Lý:** Mọi điểm ảnh đều có mục đích. Sự tiết chế là sự sang trọng. Tâm lý người dùng định hướng quyết định.
> **Nguyên Tắc Cốt Lõi:** TƯ DUY, đừng học thuộc lòng. HỎI, đừng giả định.

---

## 🎯 Quy Tắc Đọc Chọn Lọc (BẮT BUỘC)

**Đọc các file BẮT BUỘC luôn luôn, TÙY CHỌN chỉ khi cần:**

| File | Trạng Thái | Khi Nào Đọc |
|------|------------|-------------|
| [ux-psychology.md](ux-psychology.md) | 🔴 **BẮT BUỘC** | Luôn đọc đầu tiên! |
| [color-system.md](color-system.md) | ⚪ Tùy chọn | Quyết định màu sắc/bảng màu |
| [typography-system.md](typography-system.md) | ⚪ Tùy chọn | Chọn font/phối hợp font |
| [visual-effects.md](visual-effects.md) | ⚪ Tùy chọn | Glassmorphism, bóng đổ, gradient |
| [animation-guide.md](animation-guide.md) | ⚪ Tùy chọn | Khi cần Animation |
| [motion-graphics.md](motion-graphics.md) | ⚪ Tùy chọn | Lottie, GSAP, 3D |
| [decision-trees.md](decision-trees.md) | ⚪ Tùy chọn | Các template ngữ cảnh |

> 🔴 **ux-psychology.md = LUÔN ĐỌC. Các file khác = chỉ khi liên quan.**

---

## 🔧 Runtime Scripts

**Thực thi các script này để audit (đừng đọc, chỉ chạy):**

| Script | Mục Đích | Cách Dùng |
|--------|----------|-----------|
| `scripts/ux_audit.py` | UX Psychology & Accessibility Audit | `python scripts/ux_audit.py <project_path>` |

---

## ⚠️ QUAN TRỌNG: HỎI TRƯỚC KHI GIẢ ĐỊNH (BẮT BUỘC)

> **DỪNG LẠI! Nếu yêu cầu của người dùng là mở, ĐỪNG mặc định dùng sở thích của bạn.**

### Khi Prompt Của Người Dùng Mơ Hồ, HÃY HỎI:

**Màu sắc không được chỉ định?** Hỏi:
> "Bạn thích bảng màu nào? (xanh dương/xanh lá/cam/trung tính/khác?)"

**Phong cách không được chỉ định?** Hỏi:
> "Bạn đang hướng tới phong cách nào? (tối giản/đậm nét/hoài cổ/tương lai/hữu cơ?)"

**Bố cục không được chỉ định?** Hỏi:
> "Bạn có ưu tiên bố cục nào không? (cột đơn/lưới/bất đối xứng/toàn màn hình?)"

### ⛔ CÁC XU HƯỚNG MẶC ĐỊNH CẦN TRÁNH (ANTI-SAFE HARBOR):

| Xu Hướng Mặc Định Của AI | Tại Sao Nó Tệ | Hãy Nghĩ Thay Thế |
|--------------------------|---------------|-------------------|
| **Bento Grids (Cliché Hiện Đại)** | Dùng trong mọi thiết kế AI | Tại sao nội dung này CẦN lưới? |
| **Hero Split (Trái/Phải)** | Dễ đoán & Nhàm chán | Thử Typography Khổng Lồ hoặc Kể Chuyện Dọc xem? |
| **Mesh/Aurora Gradients** | Background lười biếng "kểu mới" | Một cặp màu táo bạo thì sao? |
| **Glassmorphism** | Định nghĩa "sang trọng" của AI | Phẳng, tương phản cao (solid, high-contrast) thì sao? |
| **Deep Cyan / Fintech Blue** | Nơi trú ẩn an toàn khỏi lệnh cấm màu tím | Tại sao không phải Đỏ, Đen, hoặc Xanh Neon? |
| **"Orchestrate / Empower"** | Copywriting do AI tạo | Con người sẽ nói câu này như thế nào? |
| Dark background + neon glow | Bị lạm dụng, "giao diện AI" | THƯƠNG HIỆU thực sự cần gì? |
| **Bo tròn mọi thứ** | Chung chung/An toàn | Chỗ nào có thể dùng cạnh sắc, brutalist? |

> 🔴 **"Mỗi cấu trúc 'an toàn' bạn chọn đưa bạn một bước gần hơn đến một template chung chung. HÃY CHẤP NHẬN RỦI RO."**

---

## 1. Phân Tích Ràng Buộc (LUÔN LÀ ĐẦU TIÊN)

Trước bất kỳ công việc thiết kế nào, TRẢ LỜI CÁC CÂU HỎI SAU hoặc HỎI NGƯỜI DÙNG:

| Ràng Buộc | Câu Hỏi | Tại Sao Quan Trọng |
|-----------|---------|--------------------|
| **Thời gian** | Bao nhiêu thời gian? | Quyết định độ phức tạp |
| **Nội dung** | Có sẵn hay placeholder? | Ảnh hưởng độ linh hoạt bố cục |
| **Thương hiệu** | Guideline hiện có? | Có thể quy định màu/font |
| **Công nghệ** | Stack là gì? | Ảnh hưởng khả năng thực hiện |
| **Khán giả** | Chính xác là ai? | Định hướng mọi quyết định hình ảnh |

### Khán Giả → Cách Tiếp Cận Thiết Kế

| Khán Giả | Cần Nghĩ Về |
|----------|-------------|
| **Gen Z** | Đậm nét, nhanh, mobile-first, chân thực |
| **Millennials** | Sạch sẽ, tối giản, hướng giá trị |
| **Gen X** | Quen thuộc, đáng tin cậy, rõ ràng |
| **Boomers** | Dễ đọc, tương phản cao, đơn giản |
| **B2B** | Chuyên nghiệp, tập trung dữ liệu, tin cậy |
| **Luxury** | Sự sang trọng tiết chế, khoảng trắng |

---

## 2. Các Nguyên Tắc Tâm Lý Học UX

### Các Định Luật Cốt Lõi (Hãy Thấm Nhuần)

| Định Luật | Nguyên Tắc | Áp Dụng |
|-----------|------------|---------|
| **Định luật Hick** | Nhiều lựa chọn = quyết định chậm hơn | Giới hạn tùy chọn, tiết lộ dần dần |
| **Định luật Fitts** | To hơn + gần hơn = dễ click hơn | Kích thước CTA phù hợp |
| **Định luật Miller** | ~7 mục trong trí nhớ làm việc | Gom nhóm nội dung (Chunking) |
| **Von Restorff** | Khác biệt = dễ nhớ | Làm CTA nổi bật về thị giác |
| **Vị trí chuỗi** | Mục đầu/cuối được nhớ nhiều nhất | Thông tin chính ở đầu/cuối |

### Các Cấp Độ Thiết Kế Cảm Xúc

```
VISCERAL (tức thì)  → Ấn tượng đầu: màu sắc, hình ảnh, cảm giác chung
BEHAVIORAL (hành vi) → Sử dụng: tốc độ, phản hồi, hiệu quả
REFLECTIVE (phản chiếu) → Sau đó: "Tôi thích những gì điều này nói về tôi"
```

### Xây Dựng Niềm Tin

- Chỉ báo bảo mật trên các hành động nhạy cảm
- Bằng chứng xã hội (social proof) ở nơi phù hợp
- Liên hệ/hỗ trợ rõ ràng
- Thiết kế nhất quán, chuyên nghiệp
- Chính sách minh bạch

---

## 3. Các Nguyên Tắc Bố Cục

### Tỷ Lệ Vàng (φ = 1.618)

```
Sử dụng cho sự hài hòa về tỷ lệ:
├── Nội dung : Sidebar = xấp xỉ 62% : 38%
├── Mỗi kích thước tiêu đề = cái trước × 1.618 (để tạo tỷ lệ ấn tượng)
├── Khoảng cách có thể theo: sm → md → lg (mỗi cái × 1.618)
```

### Khái Niệm Lưới 8-Point

```
Tất cả khoảng cách và kích thước là bội số của 8:
├── Chặt: 4px (nửa bước cho micro)
├── Nhỏ: 8px
├── Trung bình: 16px
├── Lớn: 24px, 32px
├── XL: 48px, 64px, 80px
└── Điều chỉnh dựa trên mật độ nội dung
```

### Các Nguyên Tắc Kích Thước Chính

| Thành Phần | Cân Nhắc |
|------------|----------|
| **Vùng chạm** | Kích thước tap thoải mái tối thiểu |
| **Nút** | Chiều cao dựa trên phân cấp quan trọng |
| **Inputs** | Khớp chiều cao nút để căn chỉnh |
| **Cards** | Padding nhất quán, thoáng đãng |
| **Độ rộng đọc** | 45-75 ký tự là tối ưu |

---

## 4. Các Nguyên Tắc Màu Sắc

### Quy Tắc 60-30-10

```
60% → Chính/Nền (yên bình, nền trung tính)
30% → Phụ (các khu vực hỗ trợ)
10% → Điểm nhấn (CTAs, highlights, sự chú ý)
```

### Tâm Lý Học Màu Sắc (Cho Việc Ra Quyết Định)

| Nếu Bạn Cần... | Cân Nhắc Các Tone | Tránh |
|----------------|-------------------|-------|
| Tin cậy, bình tĩnh | Họ Xanh dương | Đỏ hung hăng |
| Tăng trưởng, thiên nhiên | Họ Xanh lá | Xám công nghiệp |
| Năng lượng, khẩn cấp | Cam, đỏ | Xanh dương thụ động |
| Sang trọng, sáng tạo | Deep Teal, Vàng kim, Ngọc lục bảo | Màu sáng tạo cảm giác rẻ tiền |
| Sạch, tối giản | Trung tính | Màu sắc quá áp đảo |

### Quy Trình Lựa Chọn

1. **Ngành công nghiệp là gì?** (thu hẹp lựa chọn)
2. **Cảm xúc là gì?** (chọn màu chính)
3. **Chế độ sáng hay tối?** (đặt nền móng)
4. **HỎI NGƯỜI DÙNG** nếu không được chỉ định

Chi tiết lý thuyết màu sắc: [color-system.md](color-system.md)

---

## 5. Các Nguyên Tắc Typography

### Lựa Chọn Tỷ Lệ (Scale)

| Loại Nội Dung | Tỷ Lệ Scale | Cảm Giác |
|---------------|-------------|----------|
| UI dày đặc | 1.125-1.2 | Gọn gàng, hiệu quả |
| Web chung | 1.25 | Cân bằng (phổ biến nhất) |
| Tạp chí/Editorial | 1.333 | Dễ đọc, rộng rãi |
| Hero/trình diễn | 1.5-1.618 | Tác động mạnh mẽ |

### Khái Niệm Ghép Cặp (Pairing)

```
Tương phản + Hài hòa:
├── Đủ KHÁC BIỆT để phân cấp
├── Đủ TƯƠNG ĐỒNG để gắn kết
└── Thường là: display + trung tính, hoặc serif + sans
```

### Quy Tắc Dễ Đọc

- **Độ dài dòng**: 45-75 ký tự tối ưu
- **Chiều cao dòng**: 1.4-1.6 cho body text
- **Tương phản**: Kiểm tra yêu cầu WCAG
- **Kích thước**: 16px+ cho body trên web

Chi tiết typography: [typography-system.md](typography-system.md)

---

## 6. Các Nguyên Tắc Hiệu Ứng Hình Ảnh

### Glassmorphism (Khi Phù Hợp)

```
Các thuộc tính chính:
├── Nền bán trong suốt
├── Làm mờ hậu cảnh (Backdrop blur)
├── Viền tinh tế để định hình
└── ⚠️ **CẢNH BÁO:** Glassmorphism xanh/trắng tiêu chuẩn là cliché hiện đại. Dùng nó một cách táo bạo hoặc đừng dùng.
```

### Phân Cấp Bóng Đổ

```
Khái niệm độ cao (Elevation):
├── Phần tử cao hơn = bóng lớn hơn
├── Y-offset > X-offset (ánh sáng từ trên)
├── Nhiều lớp = thực tế hơn
└── Chế độ tối: có thể cần phát sáng (glow) thay thế
```

### Sử Dụng Gradient

```
Gradient hài hòa:
├── Các màu liền kề trên bánh xe màu (analogous)
├── HOẶC cùng tone, khác độ sáng
├── Tránh các cặp bổ sung (complementary) gay gắt
├── 🚫 **KHÔNG Mesh/Aurora Gradients** (các đốm trôi nổi)
└── THAY ĐỔI triệt để tùy theo dự án
```

Hướng dẫn hiệu ứng đầy đủ: [visual-effects.md](visual-effects.md)

---

## 7. Các Nguyên Tắc Animation

### Khái Niệm Thời Gian (Timing)

```
Thời lượng dựa trên:
├── Khoảng cách (xa hơn = lâu hơn)
├── Kích thước (lớn hơn = chậm hơn)
├── Mức quan trọng (then chốt = rõ ràng)
└── Ngữ cảnh (khẩn cấp = nhanh, sang trọng = chậm)
```

### Chọn Easing

| Hành Động | Easing | Tại Sao |
|-----------|--------|---------|
| Vào (Entering) | Ease-out | Giảm tốc, ổn định vào |
| Ra (Leaving) | Ease-in | Tăng tốc, thoát ra |
| Nhấn mạnh | Ease-in-out | Mượt mà, có chủ đích |
| Vui tươi | Bounce | Vui, năng lượng |

### Hiệu Năng

- Chỉ animate transform và opacity
- Tôn trọng tùy chọn giảm chuyển động (reduced-motion preference)
- Test trên thiết bị cấu hình thấp

Các pattern animation: [animation-guide.md](animation-guide.md), nâng cao: [motion-graphics.md](motion-graphics.md)

---

## 8. Checklist "Yếu Tố Wow"

### Các Chỉ Báo Cao Cấp (Premium)

- [ ] Khoảng trắng hào phóng (sang trọng = không gian thở)
- [ ] Chiều sâu và kích thước tinh tế
- [ ] Animation mượt mà, có mục đích
- [ ] Chú ý đến chi tiết (căn chỉnh, nhất quán)
- [ ] Nhịp điệu hình ảnh gắn kết
- [ ] Các thành phần tùy chỉnh (không phải tất cả là mặc định)

### Xây Dựng Niềm Tin

- [ ] Các dấu hiệu bảo mật ở nơi phù hợp
- [ ] Bằng chứng xã hội / lời chứng thực
- [ ] Tuyên bố giá trị rõ ràng
- [ ] Hình ảnh chuyên nghiệp
- [ ] Ngôn ngữ thiết kế nhất quán

### Các Kích Hoạt Cảm Xúc

- [ ] Hero gợi lên cảm xúc mong muốn
- [ ] Yếu tố con người (khuôn mặt, câu chuyện)
- [ ] Các chỉ báo tiến bộ/thành tựu
- [ ] Những khoảnh khắc thú vị (delight)

---

## 9. Anti-Patterns (Những Gì KHÔNG Nên Làm)

### ❌ Các Chỉ Báo Thiết Kế Lười Biếng

- Font hệ thống mặc định mà không xem xét
- Hình ảnh Stock không phù hợp
- Khoảng cách không nhất quán
- Quá nhiều màu cạnh tranh
- Các bức tường văn bản không phân cấp
- Độ tương phản không đạt chuẩn (Inaccessible)

### ❌ Các Mẫu Xu Hướng AI (TRÁNH XA!)

- **Màu giống nhau mọi dự án**
- **Tối + Neon làm mặc định**
- **Tím/Violet mọi thứ (CẤM MÀU TÍM ✅)**
- **Bento grids cho landing page đơn giản**
- **Mesh Gradients & Glow Effects**
- **Cấu trúc layout y hệt nhau / Vercel clone**
- **Không hỏi sở thích người dùng**

### ❌ Dark Patterns (Phi Đạo Đức)

- Chi phí ẩn
- Sự khẩn cấp giả tạo
- Hành động cưỡng ép
- UI lừa dối
- Confirmshaming (Làm người dùng thấy tội lỗi khi từ chối)

---

## 10. Tóm Tắt Quy Trình Quyết Định

```
Cho MỖI tác vụ thiết kế:

1. RÀNG BUỘC (CONSTRAINTS)
   └── Thời gian, thương hiệu, công nghệ, khán giả là gì?
   └── Nếu không rõ → HỎI

2. NỘI DUNG (CONTENT)
   └── Nội dung gì đang tồn tại?
   └── Phân cấp ra sao?

3. ĐỊNH HƯỚNG PHONG CÁCH (STYLE DIRECTION)
   └── Cái gì phù hợp ngữ cảnh?
   └── Nếu không rõ → HỎI (đừng mặc định!)

4. THỰC THI (EXECUTION)
   └── Áp dụng các nguyên tắc trên
   └── Kiểm tra đối chiếu với anti-patterns

5. REVIEW
   └── "Cái này có phục vụ người dùng không?"
   └── "Cái này có khác với mặc định của mình không?"
   └── "Mình có tự hào về nó không?"
```

---

## Các File Tham Khảo

Để hướng dẫn sâu hơn về các lĩnh vực cụ thể:

- [color-system.md](color-system.md) - Lý thuyết màu sắc và quy trình chọn
- [typography-system.md](typography-system.md) - Ghép cặp font và quyết định tỷ lệ
- [visual-effects.md](visual-effects.md) - Nguyên tắc và kỹ thuật hiệu ứng
- [animation-guide.md](animation-guide.md) - Nguyên tắc thiết kế chuyển động
- [motion-graphics.md](motion-graphics.md) - Nâng cao: Lottie, GSAP, SVG, 3D, Particles
- [decision-trees.md](decision-trees.md) - Các template theo ngữ cảnh cụ thể
- [ux-psychology.md](ux-psychology.md) - Đào sâu tâm lý người dùng

---

> **Ghi nhớ:** Thiết kế là TƯ DUY, không phải sao chép. Mỗi dự án xứng đáng được xem xét mới mẻ dựa trên ngữ cảnh và người dùng độc nhất của nó. **Tránh xa Nơi Trú Ẩn Hiện Đại Của SaaS!**
