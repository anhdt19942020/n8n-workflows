---
name: ui-ux-pro-max
description: "UI/UX design intelligence. 50 styles, 21 palettes, 50 font pairings, 20 charts, 9 stacks (React, Next.js, Vue, Svelte, SwiftUI, React Native, Flutter, Tailwind, shadcn/ui). Actions: plan, build, create, design, implement, review, fix, improve, optimize, enhance, refactor, check UI/UX code. Projects: website, landing page, dashboard, admin panel, e-commerce, SaaS, portfolio, blog, mobile app, .html, .tsx, .vue, .svelte. Elements: button, modal, navbar, sidebar, card, table, form, chart. Styles: glassmorphism, claymorphism, minimalism, brutalism, neumorphism, bento grid, dark mode, responsive, skeuomorphism, flat design. Topics: color palette, accessibility, animation, layout, typography, font pairing, spacing, hover, shadow, gradient. Integrations: shadcn/ui MCP for component search and examples."
---

# UI/UX Pro Max - Trí Tuệ Thiết Kế

Hướng dẫn thiết kế toàn diện cho ứng dụng web và mobile. Chứa 50+ phong cách, 97 bảng màu, 57 cặp font, 99 hướng dẫn UX, và 25 loại biểu đồ trên 9 nền tảng công nghệ. Cơ sở dữ liệu có thể tìm kiếm với các đề xuất dựa trên mức ưu tiên.

## Khi Nào Áp Dụng

Tham khảo các hướng dẫn này khi:
- Thiết kế UI components hoặc trang mới
- Chọn bảng màu và typography
- Review code tìm lỗi UX
- Xây dựng landing pages hoặc dashboards
- Triển khai các yêu cầu về accessibility

## Các Danh Mục Quy Tắc Theo Ưu Tiên

| Priority | Danh Mục | Tác Động | Domain |
|----------|----------|----------|--------|
| 1 | Khả năng truy cập (Accessibility) | CRITICAL | `ux` |
| 2 | Chạm & Tương tác | CRITICAL | `ux` |
| 3 | Hiệu năng | HIGH | `ux` |
| 4 | Bố cục & Responsive | HIGH | `ux` |
| 5 | Typography & Màu sắc | MEDIUM | `typography`, `color` |
| 6 | Animation | MEDIUM | `ux` |
| 7 | Chọn phong cách | MEDIUM | `style`, `product` |
| 8 | Biểu đồ & Dữ liệu | LOW | `chart` |

## Tham Khảo Nhanh

### 1. Accessibility (CRITICAL)

- `color-contrast` - Tỷ lệ tối thiểu 4.5:1 cho văn bản thường
- `focus-states` - Vòng focus rõ ràng trên các phần tử tương tác
- `alt-text` - Alt text mô tả cho các hình ảnh có ý nghĩa
- `aria-labels` - aria-label cho các nút chỉ có icon
- `keyboard-nav` - Thứ tự Tab khớp với thứ tự hiển thị
- `form-labels` - Dùng label với thuộc tính for

### 2. Chạm & Tương tác (CRITICAL)

- `touch-target-size` - Vùng chạm tối thiểu 44x44px
- `hover-vs-tap` - Dùng click/tap cho các tương tác chính
- `loading-buttons` - Disable nút trong khi xử lý bất đồng bộ
- `error-feedback` - Thông báo lỗi rõ ràng gần nơi có vấn đề
- `cursor-pointer` - Thêm cursor-pointer vào các phần tử click được

### 3. Hiệu năng (HIGH)

- `image-optimization` - Dùng WebP, srcset, lazy loading
- `reduced-motion` - Kiểm tra prefers-reduced-motion
- `content-jumping` - Dành chỗ trước cho nội dung bất đồng bộ

### 4. Bố cục & Responsive (HIGH)

- `viewport-meta` - width=device-width initial-scale=1
- `readable-font-size` - Minimum 16px body text trên mobile
- `horizontal-scroll` - Đảm bảo nội dung vừa khít chiều rộng viewport
- `z-index-management` - Định nghĩa thang z-index (10, 20, 30, 50)

### 5. Typography & Màu sắc (MEDIUM)

- `line-height` - Dùng 1.5-1.75 cho văn bản thân (body text)
- `line-length` - Giới hạn 65-75 ký tự mỗi dòng
- `font-pairing` - Cá tính của font tiêu đề/thân bài phải hợp nhau

### 6. Animation (MEDIUM)

- `duration-timing` - Dùng 150-300ms cho các tương tác vi mô
- `transform-performance` - Dùng transform/opacity, không dùng width/height
- `loading-states` - Skeleton screens hoặc spinners

### 7. Chọn Phong Cách (MEDIUM)

- `style-match` - Phong cách khớp với loại sản phẩm
- `consistency` - Dùng cùng phong cách trên tất cả các trang
- `no-emoji-icons` - Dùng SVG icons, không dùng emojis

### 8. Biểu đồ & Dữ liệu (LOW)

- `chart-type` - Loại biểu đồ phù hợp với loại dữ liệu
- `color-guidance` - Dùng bảng màu dễ truy cập (accessible)
- `data-table` - Cung cấp bảng thay thế để đảm bảo accessibility

## Cách Sử Dụng

Tìm kiếm các domain cụ thể bằng công cụ CLI bên dưới.

---

## Yêu Cầu Tiên Quyết

Kiểm tra Python đã cài đặt chưa:

```bash
python3 --version || python --version
```

Nếu Python chưa được cài đặt, cài đặt dựa trên OS của người dùng:

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

## Cách Sử Dụng Skill Này

Khi người dùng yêu cầu công việc UI/UX (thiết kế, xây dựng, tạo, triển khai, review, sửa, cải thiện), hãy theo quy trình này:

### Bước 1: Phân Tích Yêu Cầu Người Dùng

Trích xuất thông tin chính từ yêu cầu người dùng:
- **Loại sản phẩm**: SaaS, e-commerce, portfolio, dashboard, landing page, v.v.
- **Từ khóa phong cách**: tối giản, vui tươi, chuyên nghiệp, sang trọng, chế độ tối, v.v.
- **Ngành**: y tế, fintech, game, giáo dục, v.v.
- **Stack**: React, Vue, Next.js, hoặc mặc định là `html-tailwind`

### Bước 2: Tạo Design System (BẮT BUỘC)

**Luôn bắt đầu với `--design-system`** để nhận các đề xuất toàn diện cùng lý do:

```bash
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "<product_type> <industry> <keywords>" --design-system [-p "Project Name"]
```

Lệnh này:
1. Tìm kiếm 5 domain song song (product, style, color, landing, typography)
2. Áp dụng các quy tắc lý luận từ `ui-reasoning.csv` để chọn các kết quả khớp nhất
3. Trả về design system hoàn chỉnh: pattern, style, colors, typography, effects
4. Bao gồm các anti-patterns cần tránh

**Ví dụ:**
```bash
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "beauty spa wellness service" --design-system -p "Serenity Spa"
```

### Bước 3: Bổ Sung Bằng Tìm Kiếm Chi Tiết (khi cần)

Sau khi có design system, dùng tìm kiếm domain để lấy thêm chi tiết:

```bash
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "<keyword>" --domain <domain> [-n <max_results>]
```

**Khi nào dùng tìm kiếm chi tiết:**

| Nhu Cầu | Domain | Ví Dụ |
|---------|--------|-------|
| Thêm tùy chọn phong cách | `style` | `--domain style "glassmorphism dark"` |
| Đề xuất biểu đồ | `chart` | `--domain chart "real-time dashboard"` |
| Thực hành UX tốt nhất | `ux` | `--domain ux "animation accessibility"` |
| Font thay thế | `typography` | `--domain typography "elegant luxury"` |
| Cấu trúc Landing | `landing` | `--domain landing "hero social-proof"` |

### Bước 4: Hướng Dẫn Theo Stack (Mặc định: html-tailwind)

Lấy các thực hành tốt nhất cụ thể theo triển khai. Nếu người dùng không chỉ định stack, **mặc định là `html-tailwind`**.

```bash
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "<keyword>" --stack html-tailwind
```

Các stack có sẵn: `html-tailwind`, `react`, `nextjs`, `vue`, `svelte`, `swiftui`, `react-native`, `flutter`, `shadcn`

---

## Tham Khảo Tìm Kiếm

### Các Domain Có Sẵn

| Domain | Dùng Cho | Từ Khóa Ví Dụ |
|--------|----------|---------------|
| `product` | Đề xuất loại sản phẩm | SaaS, e-commerce, portfolio, healthcare, beauty, service |
| `style` | Phong cách UI, màu sắc, hiệu ứng | glassmorphism, minimalism, dark mode, brutalism |
| `typography` | Cặp font, Google Fonts | elegant, playful, professional, modern |
| `color` | Bảng màu theo loại sản phẩm | saas, ecommerce, healthcare, beauty, fintech, service |
| `landing` | Cấu trúc trang, chiến lược CTA | hero, hero-centric, testimonial, pricing, social-proof |
| `chart` | Loại biểu đồ, đề xuất thư viện | trend, comparison, timeline, funnel, pie |
| `ux` | Thực hành tốt nhất, anti-patterns | animation, accessibility, z-index, loading |
| `react` | Hiệu năng React/Next.js | waterfall, bundle, suspense, memo, rerender, cache |
| `web` | Hướng dẫn giao diện Web | aria, focus, keyboard, semantic, virtualize |
| `prompt` | AI prompts, CSS keywords | (tên phong cách) |

### Các Stack Có Sẵn

| Stack | Trọng Tâm |
|-------|-----------|
| `html-tailwind` | Các tiện ích Tailwind, responsive, a11y (MẶC ĐỊNH) |
| `react` | State, hooks, hiệu năng, patterns |
| `nextjs` | SSR, routing, images, API routes |
| `vue` | Composition API, Pinia, Vue Router |
| `svelte` | Runes, stores, SvelteKit |
| `swiftui` | Views, State, Navigation, Animation |
| `react-native` | Components, Navigation, Lists |
| `flutter` | Widgets, State, Layout, Theming |
| `shadcn` | shadcn/ui components, theming, forms, patterns |

---

## Ví Dụ Quy Trình

**User request:** "Làm landing page cho dịch vụ chăm sóc da chuyên nghiệp"

### Bước 1: Phân Tích Yêu Cầu
- Product type: Beauty/Spa service
- Style keywords: elegant, professional, soft
- Industry: Beauty/Wellness
- Stack: html-tailwind (mặc định)

### Bước 2: Tạo Design System (BẮT BUỘC)

```bash
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "beauty spa wellness service elegant" --design-system -p "Serenity Spa"
```

**Output:** Design system hoàn chỉnh với pattern, style, colors, typography, effects, và anti-patterns.

### Bước 3: Bổ Sung Bằng Tìm Kiếm Chi Tiết (khi cần)

```bash
# Lấy hướng dẫn UX cho animation và accessibility
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "animation accessibility" --domain ux

# Lấy tùy chọn typography thay thế nếu cần
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "elegant luxury serif" --domain typography
```

### Bước 4: Hướng Dẫn Theo Stack

```bash
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "layout responsive form" --stack html-tailwind
```

**Sau đó:** Tổng hợp design system + tìm kiếm chi tiết và triển khai thiết kế.

---

## Các Định Dạng Output

Cờ `--design-system` hỗ trợ hai định dạng đầu ra:

```bash
# Hộp ASCII (mặc định) - tốt nhất cho hiển thị terminal
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "fintech crypto" --design-system

# Markdown - tốt nhất cho tài liệu hóa
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "fintech crypto" --design-system -f markdown
```

---

## Mẹo Để Có Kết Quả Tốt Hơn

1. **Cụ thể với từ khóa** - "healthcare SaaS dashboard" > "app"
2. **Tìm kiếm nhiều lần** - Các từ khóa khác nhau tiết lộ những insight khác nhau
3. **Kết hợp các domain** - Style + Typography + Color = Design system hoàn chỉnh
4. **Luôn kiểm tra UX** - Tìm "animation", "z-index", "accessibility" cho các vấn đề phổ biến
5. **Dùng cờ stack** - Lấy các thực hành tốt nhất cụ thể theo triển khai
6. **Lặp lại** - Nếu tìm kiếm đầu tiên không khớp, thử từ khóa khác

---

## Các Quy Tắc Chung Cho UI Chuyên Nghiệp

Đây là các vấn đề thường bị bỏ qua làm cho UI trông thiếu chuyên nghiệp:

### Icons & Các Phần Tử Hình Ảnh

| Quy Tắc | Nên (Do) | Không Nên (Don't) |
|---------|----------|-------------------|
| **Không dùng emoji làm icon** | Dùng SVG icons (Heroicons, Lucide, Simple Icons) | Dùng emojis như 🎨 🚀 ⚙️ làm UI icons |
| **Trạng thái hover ổn định** | Dùng chuyển đổi color/opacity khi hover | Dùng biến đổi scale làm lệch bố cục |
| **Logo thương hiệu đúng** | Tìm SVG chính thức từ Simple Icons | Đoán mò hoặc dùng đường dẫn logo sai |
| **Kích thước icon nhất quán** | Dùng viewBox cố định (24x24) với w-6 h-6 | Trộn các kích thước icon ngẫu nhiên |

### Tương Tác & Con Trỏ (Cursor)

| Quy Tắc | Nên (Do) | Không Nên (Don't) |
|---------|----------|-------------------|
| **Cursor pointer** | Thêm `cursor-pointer` vào tất cả thẻ click được | Để cursor mặc định trên phần tử tương tác |
| **Phản hồi khi Hover** | Cung cấp phản hồi thị giác (màu, bóng, viền) | Không có dấu hiệu phần tử có thể tương tác |
| **Chuyển đổi mượt mà** | Dùng `transition-colors duration-200` | Thay đổi trạng thái tức thì hoặc quá chậm (>500ms) |

### Tương Phản Light/Dark Mode

| Quy Tắc | Nên (Do) | Không Nên (Don't) |
|---------|----------|-------------------|
| **Glass card light mode** | Dùng `bg-white/80` hoặc độ mờ cao hơn | Dùng `bg-white/10` (quá trong suốt) |
| **Tương phản văn bản Light** | Dùng `#0F172A` (slate-900) cho chữ | Dùng `#94A3B8` (slate-400) cho body text |
| **Văn bản mờ (Muted) Light** | Dùng tối thiểu `#475569` (slate-600) | Dùng gray-400 hoặc nhạt hơn |
| **Hiển thị viền (Border)** | Dùng `border-gray-200` ở light mode | Dùng `border-white/10` (vô hình) |

### Bố Cục & Khoảng Cách

| Quy Tắc | Nên (Do) | Không Nên (Don't) |
|---------|----------|-------------------|
| **Navbar nổi (Floating)** | Thêm khoảng cách `top-4 left-4 right-4` | Dính navbar vào `top-0 left-0 right-0` |
| **Padding nội dung** | Tính toán chiều cao navbar cố định | Để nội dung bị che sau phần tử cố định |
| **Max-width nhất quán** | Dùng cùng `max-w-6xl` hoặc `max-w-7xl` | Trộn lẫn các độ rộng container khác nhau |

---

## Checklist Trước Khi Bàn Giao (Pre-Delivery)

Trước khi bàn giao code UI, hãy xác minh các mục này:

### Chất Lượng Hình Ảnh
- [ ] Không dùng emojis làm icon (dùng SVG thay thế)
- [ ] Tất cả icon từ bộ icon nhất quán (Heroicons/Lucide)
- [ ] Logo thương hiệu chính xác (xác minh từ Simple Icons)
- [ ] Trạng thái Hover không gây lệch bố cục
- [ ] Dùng màu theme trực tiếp (bg-primary) không phải var() wrapper

### Tương Tác
- [ ] Tất cả phần tử click được đều có `cursor-pointer`
- [ ] Trạng thái Hover cung cấp phản hồi thị giác rõ ràng
- [ ] Transition mượt mà (150-300ms)
- [ ] Trạng thái Focus hiển thị rõ khi điều hướng bằng bàn phím

### Light/Dark Mode
- [ ] Văn bản chế độ Light có đủ độ tương phản (tối thiểu 4.5:1)
- [ ] Phần tử Glass/trong suốt hiển thị rõ ở light mode
- [ ] Viền hiển thị rõ ở cả hai chế độ
- [ ] Test cả hai chế độ trước khi bàn giao

### Bố Cục
- [ ] Các phần tử nổi có khoảng cách hợp lý so với cạnh
- [ ] Không có nội dung bị che sau navbar cố định
- [ ] Responsive tại 375px, 768px, 1024px, 1440px
- [ ] Không cuộn ngang trên mobile

### Accessibility
- [ ] Tất cả hình ảnh có alt text
- [ ] Form inputs có nhãn (labels)
- [ ] Màu sắc không phải là chỉ báo duy nhất
- [ ] Tôn trọng `prefers-reduced-motion`
