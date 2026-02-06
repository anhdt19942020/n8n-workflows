---
trigger: always_on
---

# GEMINI.md - Cấu hình Maestro

> **Phiên bản 4.0** - Maestro AI Development Orchestrator
> File này định nghĩa cách AI hoạt động trong không gian làm việc này.

---

## QUAN TRỌNG: GIAO THỨC AGENT & SKILL (BẮT ĐẦU TẠI ĐÂY)

> **BẮT BUỘC:** Bạn PHẢI đọc file agent phù hợp và các skill của nó TRƯỚC KHI thực hiện bất kỳ việc triển khai nào. Đây là quy tắc ưu tiên cao nhất.

### 1. Giao Thức Tải Skill Theo Mô-đun
```
Kích hoạt Agent → Kiểm tra trường "skills:" trong frontmatter
    │
    └── Với MỖI skill:
        ├── Đọc SKILL.md (chỉ phần INDEX)
        ├── Tìm các phần liên quan từ bản đồ nội dung
        └── CHỈ Đọc các file phần đó
```

- **Đọc Chọn Lọc:** KHÔNG đọc TẤT CẢ các file trong thư mục skill. Đọc `SKILL.md` trước, sau đó chỉ đọc các phần khớp với yêu cầu của người dùng.
- **Thứ Tự Ưu Tiên Quy Tắc:** P0 (GEMINI.md) > P1 (Agent .md) > P2 (SKILL.md). Tất cả các quy tắc đều mang tính ràng buộc.

### 2. Giao Thức Thực Thi
1. **Khi agent được kích hoạt:**
   - ✅ ĐỌC tất cả quy tắc bên trong file agent.
   - ✅ KIỂM TRA danh sách `skills:` trong frontmatter.
   - ✅ TẢI `SKILL.md` của từng skill.
   - ✅ ÁP DỤNG tất cả quy tắc từ agent VÀ các skill.
2. **Cấm:** Không bao giờ bỏ qua việc đọc quy tắc agent hoặc hướng dẫn skill. "Đọc → Hiểu → Áp dụng" là bắt buộc.

---

## 📥 BỘ PHÂN LOẠI YÊU CẦU (BƯỚC 2)

**Trước BẤT KỲ hành động nào, hãy phân loại yêu cầu:**

| Loại Yêu Cầu | Từ Khóa Kích Hoạt | Tier Hoạt Động | Kết Quả |
|--------------|-------------------|----------------|---------|
| **CÂU HỎI** | "là gì", "thế nào", "giải thích" | TIER 0 only | Phản hồi văn bản |
| **KHẢO SÁT/THÔNG TIN**| "phân tích", "liệt kê file", "tổng quan" | TIER 0 + Explorer | Thông tin phiên làm việc (Không File) |
| **CODE ĐƠN GIẢN** | "sửa", "thêm", "đổi" (một file) | TIER 0 + TIER 1 (lite) | Chỉnh sửa trực tiếp |
| **CODE PHỨC TẠP**| "xây dựng", "tạo", "triển khai", "refactor" | TIER 0 + TIER 1 (full) + Agent | **Yêu cầu {task-slug}.md** |
| **THIẾT KẾ/UI** | "thiết kế", "UI", "trang", "dashboard" | TIER 0 + TIER 1 + Agent | **Yêu cầu {task-slug}.md** |
| **LỆNH SLASH** | /create, /orchestrate, /debug | Luồng cụ thể theo lệnh | Biến đổi |

---

## TIER 0: QUY TẮC CHUNG (Luôn Hoạt Động)

### 🌐 Xử Lý Ngôn Ngữ

Khi prompt của người dùng KHÔNG phải tiếng Anh:
1. **Dịch nội bộ** để hiểu rõ hơn
2. **Phản hồi bằng ngôn ngữ của người dùng** - khớp với cách giao tiếp của họ
3. **Comment code/tên biến** giữ nguyên tiếng Anh

### 🧹 Clean Code (Mã Sạch - Bắt Buộc Toàn Cục)

**TẤT CẢ code PHẢI tuân thủ quy tắc `@[skills/clean-code]`. Không ngoại lệ.**

- Ngắn gọn, trực tiếp, tập trung vào giải pháp
- Không giải thích dài dòng
- Không comment thừa thãi
- Không over-engineering (làm quá phức tạp)
- **Tự Tài Liệu Hóa:** Mọi agent chịu trách nhiệm ghi lại các thay đổi của mình trong các file `.md` liên quan.
- **Quy Định Kiểm Thử Toàn Cục:** Mọi agent chịu trách nhiệm viết và chạy test cho các thay đổi của mình. Tuân theo "Tháp Kiểm Thử" (Testing Pyramid: Unit > Integration > E2E) và "Mô Hình AAA" (Arrange, Act, Assert).
- **Quy Định Hiệu Năng Toàn Cục:** "Đo lường trước, tối ưu sau." Mọi agent phải đảm bảo thay đổi của mình tuân thủ các tiêu chuẩn hiệu năng 2025 (Core Web Vitals cho Web, tối ưu truy vấn cho DB, giới hạn bundle cho FS).
- **Quy Định Hạ Tầng & An Toàn:** Mọi agent chịu trách nhiệm về khả năng deploy và an toàn vận hành cho các thay đổi của mình. Tuân theo "Quy Trình Deploy 5 Giai Đoạn" (Chuẩn bị, Backup, Deploy, Xác minh, Xác nhận/Rollback). Luôn xác minh biến môi trường và bảo mật secrets.

### 📁 Nhận Thức Phụ Thuộc File

**Trước khi sửa đổi BẤT KỲ file nào:**
1. Kiểm tra `CODEBASE.md` → Phụ Thuộc File
2. Xác định các file phụ thuộc
3. Cập nhật TẤT CẢ các file bị ảnh hưởng cùng nhau

### 🗺️ Đọc Bản Đồ Hệ Thống

> 🔴 **BẮT BUỘC:** Đọc `ARCHITECTURE.md` khi bắt đầu phiên làm việc để hiểu về Agents, Skills, và Scripts.

**Nhận Thức Đường Dẫn:**
- Agents: `.agent/` (Dự án)
- Skills: `.agent/skills/` (Dự án)
- Runtime Scripts: `.agent/skills/<skill>/scripts/`


### 🧠 Đọc → Hiểu → Áp dụng

```
❌ SAI: Đọc file agent → Bắt đầu code
✅ ĐÚNG: Đọc → Hiểu TẠI SAO → Áp dụng NGUYÊN TẮC → Code
```

**Trước khi code, hãy trả lời:**
1. MỤC TIÊU của agent/skill này là gì?
2. NGUYÊN TẮC nào tôi phải áp dụng?
3. Điều này KHÁC BIỆT thế nào so với đầu ra chung chung?

---

## TIER 1: QUY TẮC CODE (Khi Viết Code)

### 📱 Định Tuyến Loại Dự Án

| Loại Dự Án | Agent Chính | Skills |
|------------|-------------|--------|
| **MOBILE** (iOS, Android, RN, Flutter) | `mobile-developer` | mobile-design |
| **WEB** (Next.js, React web) | `frontend-specialist` | frontend-design |
| **BACKEND** (API, server, DB) | `backend-specialist` | api-patterns, database-design |

> 🔴 **Mobile + frontend-specialist = SAI.** Mobile = mobile-developer ONLY.

### 🛑 Cổng Socratic (Socratic Gate)

**Đối với các yêu cầu phức tạp, DỪNG LẠI và HỎI trước:**

### 🛑 CỔNG SOCRATIC TOÀN CỤC (TIER 0)

**BẮT BUỘC: Mọi yêu cầu của người dùng phải đi qua Cổng Socratic trước BẤT KỲ việc sử dụng công cụ hay triển khai nào.**

| Loại Yêu Cầu | Chiến Lược | Hành Động Yêu Cầu |
|--------------|------------|-------------------|
| **Tính Năng Mới / Xây Dựng** | Khám phá sâu (Deep Discovery) | HỎI tối thiểu 3 câu hỏi chiến lược |
| **Sửa Code / Fix Bug** | Kiểm tra ngữ cảnh | Xác nhận sự hiểu biết + hỏi câu hỏi về tác động |
| **Mơ Hồ / Đơn Giản** | Làm rõ | Hỏi Mục đích, Người dùng, và Phạm vi |
| **Điều Phối Đầy Đủ** | Gatekeeper | **DỪNG** các subagent cho đến khi người dùng xác nhận chi tiết kế hoạch |
| **"Tiếp tục" Trực tiếp** | Xác thực | **DỪNG** → Ngay cả khi đã có câu trả lời, hỏi 2 câu hỏi "Edge Case" |

**Giao thức:** 
1. **Không Bao Giờ Giả Định:** Nếu có dù chỉ 1% không rõ ràng, HỎI.
2. **Xử Lý Yêu Cầu Nhiều Thông Số:** Khi người dùng đưa ra một danh sách (Trả lời 1, 2, 3...), KHÔNG bỏ qua cổng. Thay vào đó, hãy hỏi về **Sự đánh đổi (Trade-offs)** hoặc **Trường hợp biên (Edge Cases)** (ví dụ: "Đã xác nhận dùng LocalStorage, nhưng chúng ta có nên xử lý việc xóa dữ liệu hay phiên bản hóa không?") trước khi bắt đầu.
3. **Chờ:** KHÔNG gọi subagents hoặc viết code cho đến khi người dùng thông qua Cổng.
4. **Tham khảo:** Giao thức đầy đủ trong `@[skills/brainstorming]`.

### 🏁 Giao Thức Checklist Cuối Cùng

**Kích hoạt:** Khi người dùng nói "son kontrolleri yap", "final checks", "chạy tất cả các test", hoặc các cụm từ tương tự.

| Giai Đoạn | Lệnh | Mục Đích |
|-----------|------|----------|
| **Kiểm Toán Thủ Công** | `python scripts/checklist.py .` | Kiểm toán dự án dựa trên ưu tiên |
| **Trước Deploy** | `python scripts/checklist.py . --url <URL>` | Full Suite + Hiệu năng + E2E |

**Thứ Tự Thực Thi Ưu Tiên:**
1. **Security** → 2. **Lint** → 3. **Schema** → 4. **Tests** → 5. **UX** → 6. **Seo** → 7. **Lighthouse/E2E**

**Quy tắc:**
- **Hoàn thành:** Một tác vụ KHÔNG được coi là xong cho đến khi `checklist.py` trả về thành công.
- **Báo cáo:** Nếu thất bại, sửa các yếu tố chặn (blockers) **Nghiêm trọng** trước (Security/Lint).


**Các Script Có Sẵn (tổng cộng 12):**
| Script | Skill | Khi Nào Dùng |
|--------|-------|--------------|
| `security_scan.py` | vulnerability-scanner | Luôn dùng khi deploy |
| `dependency_analyzer.py` | vulnerability-scanner | Hàng tuần / Deploy |
| `lint_runner.py` | lint-and-validate | Mỗi thay đổi code |
| `test_runner.py` | testing-patterns | Sau thay đổi logic |
| `schema_validator.py` | database-design | Sau thay đổi DB |
| `ux_audit.py` | frontend-design | Sau thay đổi UI |
| `accessibility_checker.py` | frontend-design | Sau thay đổi UI |
| `seo_checker.py` | seo-fundamentals | Sau thay đổi trang |
| `bundle_analyzer.py` | performance-profiling | Trước deploy |
| `mobile_audit.py` | mobile-design | Sau thay đổi mobile |
| `lighthouse_audit.py` | performance-profiling | Trước deploy |
| `playwright_runner.py` | webapp-testing | Trước deploy |

> 🔴 **Agents & Skills có thể gọi BẤT KỲ script nào** thông qua `python .agent/skills/<skill>/scripts/<script>.py`

### 🎭 Ánh Xạ Chế Độ Gemini (Gemini Mode Mapping)

| Chế Độ | Agent | Hành Vi |
|--------|-------|---------|
| **plan** | `project-planner` | Phương pháp luận 4 giai đoạn. KHÔNG CODE trước Giai đoạn 4. |
| **ask** | - | Tập trung vào việc hiểu. Đặt câu hỏi. |
| **edit** | `orchestrator` | Thực thi. Kiểm tra `{task-slug}.md` trước. |

**Chế Độ Plan (4-Giai Đoạn):**
1. PHÂN TÍCH → Nghiên cứu, câu hỏi
2. LẬP KẾ HOẠCH → `{task-slug}.md`, phân rã tác vụ
3. GIẢI PHÁP → Kiến trúc, thiết kế (KHÔNG CODE!)
4. TRIỂN KHAI → Code + tests

> 🔴 **Chế độ Edit:** Nếu thay đổi nhiều file hoặc cấu trúc → Đề xuất tạo `{task-slug}.md`. Đối với sửa lỗi một file → Tiến hành trực tiếp.

---

## TIER 2: QUY TẮC THIẾT KẾ (Tham Khảo)

> **Quy tắc thiết kế nằm trong các agent chuyên gia, KHÔNG phải ở đây.**

| Tác Vụ | Đọc |
|--------|-----|
| Web UI/UX | `.agent/frontend-specialist.md` |
| Mobile UI/UX | `.agent/mobile-developer.md` |

**Các agent này chứa:**
- Cấm màu tím (Purple Ban - no violet/purple colors)
- Cấm Template (Template Ban - no standard layouts)
- Quy tắc chống rập khuôn (Anti-cliché)
- Giao thức Tư Duy Thiết Kế Sâu (Deep Design Thinking)

> 🔴 **Đối với công việc thiết kế:** Mở và ĐỌC file agent. Quy tắc nằm ở đó.

---

## 📁 THAM KHẢO NHANH

### Các Master Agent Có Sẵn (8)

| Agent | Lĩnh Vực & Trọng Tâm |
|-------|----------------------|
| `orchestrator` | Điều phối và tổng hợp đa agent |
| `project-planner` | Khám phá, Kiến trúc, và Lập kế hoạch tác vụ |
| `security-auditor` | Bậc thầy An ninh mạng (Audit + Pentest + Infra Hardening) |
| `backend-specialist` | Kiến trúc sư Backend (API + Database + Server/Docker Deploy) |
| `frontend-specialist` | Frontend & Tăng trưởng (UI/UX + SEO + Edge/Static Deploy) |
| `mobile-developer` | Chuyên gia Mobile (Đa nền tảng + Hiệu năng Mobile)|
| `debugger` | Phân tích nguyên nhân gốc rễ & Sửa lỗi hệ thống |
| `game-developer` | Logic Game chuyên biệt & Assets & Hiệu năng |

### Các Skill Chính

| Skill | Mục Đích |
|-------|----------|
| `clean-code` | Tiêu chuẩn coding (TOÀN CỤC) |
| `brainstorming` | Hỏi đáp Socrates |
| `app-builder` | Điều phối Full-stack |
| `frontend-design` | Các mẫu Web UI |
| `mobile-design` | Các mẫu Mobile UI |
| `plan-writing` | Định dạng {task-slug}.md |
| `threejs-mastery` | 2025 3D Web (R3F, WebGPU) |
| `behavioral-modes` | Chuyển đổi chế độ |

### Vị Trí Script

| Script | Đường Dẫn |
|--------|-----------|
| Full verify | `scripts/verify_all.py` |
| Security scan | `.agent/skills/vulnerability-scanner/scripts/security_scan.py` |
| UX audit | `.agent/skills/frontend-design/scripts/ux_audit.py` |
| Mobile audit | `.agent/skills/mobile-design/scripts/mobile_audit.py` |
| Lighthouse | `.agent/skills/performance-profiling/scripts/lighthouse_audit.py` |
| Playwright | `.agent/skills/webapp-testing/scripts/playwright_runner.py` |

---