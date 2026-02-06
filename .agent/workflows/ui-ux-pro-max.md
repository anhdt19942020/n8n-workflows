---
description: Lên kế hoạch và triển khai UI
---

# UI/UX Pro Max - Trí Tuệ Thiết Kế

Cơ sở dữ liệu có thể tìm kiếm về các phong cách UI, bảng màu, ghép font, loại biểu đồ, đề xuất sản phẩm, hướng dẫn UX và các best practice cụ thể cho từng stack.

## Yêu Cầu Tiên Quyết

Kiểm tra xem Python đã được cài đặt chưa:

```bash
python3 --version || python --version
```

Nếu Python chưa được cài đặt, hãy cài đặt dựa trên OS của người dùng:

**macOS:**
```bash
brew install python3
```

**Ubuntu/Debian:**
```bash
sudo apt update && sudo apt install python3
```

**Windows:**
```powershell
winget install Python.Python.3.12
```

---

## Cách Sử Dụng Workflow Này

Khi người dùng yêu cầu công việc UI/UX (thiết kế, xây dựng, tạo, triển khai, review, sửa, cải thiện), hãy làm theo quy trình này:

### Bước 1: Phân Tích Yêu Cầu Người Dùng

Trích xuất thông tin chính từ yêu cầu người dùng:
- **Loại sản phẩm**: SaaS, e-commerce, portfolio, dashboard, landing page, v.v.
- **Từ khóa phong cách**: tối giản, vui tươi, chuyên nghiệp, thanh lịch, chế độ tối, v.v.
- **Ngành**: y tế, fintech, gaming, giáo dục, v.v.
- **Stack**: React, Vue, Next.js, hoặc mặc định là `html-tailwind`

### Bước 2: Tìm Kiếm Các Miền Liên Quan

Sử dụng `search.py` nhiều lần để thu thập thông tin toàn diện. Tìm kiếm cho đến khi bạn có đủ ngữ cảnh.

```bash
python3 .shared/ui-ux-pro-max/scripts/search.py "<từ khóa>" --domain <miền> [-n <max_results>]
```

**Thứ tự tìm kiếm đề xuất:**

1. **Product** - Nhận đề xuất phong cách cho loại sản phẩm
2. **Style** - Nhận hướng dẫn phong cách chi tiết (màu sắc, hiệu ứng, frameworks)
3. **Typography** - Nhận ghép font với import Google Fonts
4. **Color** - Nhận bảng màu (Primary, Secondary, CTA, Background, Text, Border)
5. **Landing** - Nhận cấu trúc trang (nếu là landing page)
6. **Chart** - Nhận đề xuất biểu đồ (nếu là dashboard/analytics)
7. **UX** - Nhận best practices và anti-patterns
8. **Stack** - Nhận hướng dẫn cụ thể cho stack (mặc định: html-tailwind)

### Bước 3: Hướng Dẫn Stack (Mặc định: html-tailwind)

Nếu người dùng không chỉ định stack, **mặc định là `html-tailwind`**.

```bash
python3 .shared/ui-ux-pro-max/scripts/search.py "<từ khóa>" --stack html-tailwind
```

Các stack có sẵn: `html-tailwind`, `react`, `nextjs`, `vue`, `svelte`, `swiftui`, `react-native`, `flutter`, `shadcn`

---

## Tham Khảo Tìm Kiếm

### Các Miền (Domains) Có Sẵn

| Miền | Dùng Cho | Từ Khóa Ví Dụ |
|------|----------|---------------|
| `product` | Đề xuất loại sản phẩm | SaaS, e-commerce, portfolio, healthcare, beauty, service |
| `style` | Phong cách UI, màu sắc, hiệu ứng | glassmorphism, minimalism, dark mode, brutalism |
| `typography` | Ghép font, Google Fonts | elegant, playful, professional, modern |
| `color` | Bảng màu theo loại sản phẩm | saas, ecommerce, healthcare, beauty, fintech, service |
| `landing` | Cấu trúc trang, chiến lược CTA | hero, hero-centric, testimonial, pricing, social-proof |
| `chart` | Loại biểu đồ, đề xuất thư viện | trend, comparison, timeline, funnel, pie |
| `ux` | Best practices, anti-patterns | animation, accessibility, z-index, loading |
| `prompt` | AI prompts, từ khóa CSS | (tên phong cách) |

### Các Stack Có Sẵn

| Stack | Trọng Tâm |
|-------|-----------|
| `html-tailwind` | Tiện ích Tailwind, responsive, a11y (MẶC ĐỊNH) |
| `react` | State, hooks, hiệu năng, patterns |
| `nextjs` | SSR, routing, images, API routes |
| `vue` | Composition API, Pinia, Vue Router |
| `svelte` | Runes, stores, SvelteKit |
| `swiftui` | Views, State, Navigation, Animation |
| `react-native` | Components, Navigation, Lists |
| `flutter` | Widgets, State, Layout, Theming |
| `shadcn` | shadcn/ui components, theming, forms, patterns |

---

## Ví Dụ Workflow

**Yêu cầu người dùng:** "Làm landing page cho dịch vụ chăm sóc da chuyên nghiệp"

**AI nên:**

```bash
# 1. Search product type
python3 .shared/ui-ux-pro-max/scripts/search.py "beauty spa wellness service" --domain product

# 2. Search style (based on industry: beauty, elegant)
python3 .shared/ui-ux-pro-max/scripts/search.py "elegant minimal soft" --domain style

# 3. Search typography
python3 .shared/ui-ux-pro-max/scripts/search.py "elegant luxury" --domain typography

# 4. Search color palette
python3 .shared/ui-ux-pro-max/scripts/search.py "beauty spa wellness" --domain color

# 5. Search landing page structure
python3 .shared/ui-ux-pro-max/scripts/search.py "hero-centric social-proof" --domain landing

# 6. Search UX guidelines
python3 .shared/ui-ux-pro-max/scripts/search.py "animation" --domain ux
python3 .shared/ui-ux-pro-max/scripts/search.py "accessibility" --domain ux

# 7. Search stack guidelines (default: html-tailwind)
python3 .shared/ui-ux-pro-max/scripts/search.py "layout responsive" --stack html-tailwind
```

**Sau đó:** Tổng hợp tất cả kết quả tìm kiếm và triển khai thiết kế.

---

## Mẹo Để Có Kết Quả Tốt Hơn

1. **Cụ thể với từ khóa** - "healthcare SaaS dashboard" > "app"
2. **Tìm kiếm nhiều lần** - Các từ khóa khác nhau tiết lộ thông tin khác nhau
3. **Kết hợp các miền** - Style + Typography + Color = Hệ thống thiết kế hoàn chỉnh
4. **Luôn kiểm tra UX** - Tìm kiếm "animation", "z-index", "accessibility" cho các vấn đề chung
5. **Sử dụng cờ stack** - Nhận các best practice cụ thể cho việc triển khai
6. **Lặp lại** - Nếu tìm kiếm đầu tiên không khớp, thử từ khóa khác
7. **Chia nhỏ thành nhiều file** - Để bảo trì tốt hơn:
   - Tách các component thành file riêng (ví dụ: `Header.tsx`, `Footer.tsx`)
   - Trích xuất các style tái sử dụng vào file chuyên dụng
   - Giữ mỗi file tập trung và dưới 200-300 dòng

---

## Các Quy Tắc Chung Cho UI Chuyên Nghiệp

Đây là những vấn đề thường bị bỏ qua khiến UI trông thiếu chuyên nghiệp:

### Icons & Các Yếu Tố Trực Quan

| Quy Tắc | Nên | Không Nên |
|---------|-----|-----------|
| **Không dùng emoji làm icon** | Dùng SVG icons (Heroicons, Lucide, Simple Icons) | Dùng emojis như 🎨 🚀 ⚙️ làm UI icons |
| **Trạng thái hover ổn định** | Dùng chuyển đổi màu/độ mờ khi hover | Dùng biến đổi scale làm lệch bố cục |
| **Logo thương hiệu chính xác** | Tìm SVG chính thức từ Simple Icons | Đoán hoặc dùng đường dẫn logo sai |
| **Kích thước icon nhất quán** | Dùng viewBox cố định (24x24) với w-6 h-6 | Trộn lẫn các kích thước icon khác nhau ngẫu nhiên |

### Tương Tác & Con Trỏ (Cursor)

| Quy Tắc | Nên | Không Nên |
|---------|-----|-----------|
| **Cursor pointer** | Thêm `cursor-pointer` vào tất cả thẻ/nút click được | Để con trỏ mặc định trên các phần tử tương tác |
| **Phản hồi hover** | Cung cấp phản hồi trực quan (màu, bóng, viền) | Không có dấu hiệu phần tử có thể tương tác |
| **Chuyển đổi mượt mà** | Dùng `transition-colors duration-200` | Thay đổi trạng thái tức thì hoặc quá chậm (>500ms) |

### Tương Phản Light/Dark Mode

| Quy Tắc | Nên | Không Nên |
|---------|-----|-----------|
| **Glass card light mode** | Dùng `bg-white/80` hoặc độ mờ cao hơn | Dùng `bg-white/10` (quá trong suốt) |
| **Tương phản văn bản light** | Dùng `#0F172A` (slate-900) cho văn bản | Dùng `#94A3B8` (slate-400) cho văn bản thân |
| **Văn bản mờ light** | Dùng `#475569` (slate-600) tối thiểu | Dùng gray-400 hoặc sáng hơn |
| **Hiển thị viền** | Dùng `border-gray-200` ở chế độ sáng | Dùng `border-white/10` (vô hình) |

### Bố Cục & Khoảng Cách

| Quy Tắc | Nên | Không Nên |
|---------|-----|-----------|
| **Navbar nổi** | Thêm khoảng cách `top-4 left-4 right-4` | Dính navbar vào `top-0 left-0 right-0` |
| **Padding nội dung** | Tính toán chiều cao navbar cố định | Để nội dung ẩn sau các phần tử cố định |
| **Max-width nhất quán** | Dùng cùng `max-w-6xl` hoặc `max-w-7xl` | Trộn lẫn các độ rộng container khác nhau |

---

## Checklist Trước Khi Bàn Giao

Trước khi bàn giao mã UI, hãy xác minh các mục này:

### Chất Lượng Trực Quan
- [ ] Không dùng emoji làm icon (dùng SVG thay thế)
- [ ] Tất cả icon từ bộ icon nhất quán (Heroicons/Lucide)
- [ ] Logo thương hiệu chính xác (đã xác minh từ Simple Icons)
- [ ] Trạng thái hover không gây lệch bố cục

### Tương Tác
- [ ] Tất cả phần tử click được có `cursor-pointer`
- [ ] Trạng thái hover cung cấp phản hồi trực quan rõ ràng
- [ ] Chuyển đổi mượt mà (150-300ms)
- [ ] Trạng thái focus hiển thị rõ cho điều hướng bằng bàn phím

### Light/Dark Mode
- [ ] Văn bản chế độ sáng có độ tương phản đủ (tối thiểu 4.5:1)
- [ ] Các phần tử glass/trong suốt hiển thị rõ ở chế độ sáng
- [ ] Viền hiển thị rõ ở cả hai chế độ
- [ ] Test cả hai chế độ trước khi bàn giao

### Bố Cục
- [ ] Các phần tử nổi có khoảng cách hợp lý từ các cạnh
- [ ] Không có nội dung bị ẩn sau navbar cố định
- [ ] Responsive tại 320px, 768px, 1024px, 1440px
- [ ] Không cuộn ngang trên mobile

### Khả Năng Truy Cập (Accessibility)
- [ ] Tất cả hình ảnh có alt text
- [ ] Các input form có nhãn (label)
- [ ] Màu sắc không phải là chỉ báo duy nhất
- [ ] Tôn trọng `prefers-reduced-motion`