---
description: Điều phối đa agent cho các nhiệm vụ phức tạp. Sử dụng để phân tích đa chiều, đánh giá toàn diện hoặc các nhiệm vụ cần chuyên môn khác nhau.
---

# Điều Phối Đa Agent (Multi-Agent Orchestration)

Bạn đang ở trong **CHẾ ĐỘ ĐIỀU PHỐI (ORCHESTRATION MODE)**. Nhiệm vụ của bạn: điều phối các agent chuyên gia để giải quyết vấn đề phức tạp này.

## Nhiệm Vụ Cần Điều Phối
$ARGUMENTS

---

## 🔴 QUAN TRỌNG: Yêu Cầu Agent Tối Thiểu

> ⚠️ **ĐIỀU PHỐI = TỐI THIỂU 3 AGENT KHÁC NHAU**
> 
> Nếu bạn sử dụng ít hơn 3 agent, bạn KHÔNG phải là đang điều phối - bạn chỉ đang ủy quyền.
> 
> **Xác thực trước khi hoàn thành:**
> - Đếm số agent đã gọi
> - Nếu `agent_count < 3` → DỪNG và gọi thêm agent
> - Một agent đơn lẻ = THẤT BẠI trong việc điều phối

### Ma Trận Chọn Agent

| Loại Tác Vụ | Các Agent BẮT BUỘC (tối thiểu) |
|-------------|--------------------------------|
| **Web App** | frontend-specialist, backend-specialist, test-engineer |
| **API** | backend-specialist, security-auditor, test-engineer |
| **UI/Design** | frontend-specialist, seo-specialist, performance-optimizer |
| **Database** | database-architect, backend-specialist, security-auditor |
| **Full Stack** | project-planner, frontend-specialist, backend-specialist, devops-engineer |
| **Debug** | debugger, explorer-agent, test-engineer |
| **Security** | security-auditor, penetration-tester, devops-engineer |

---

## Kiểm Tra Trước Khi Bay: Chế Độ (Mode Check)

| Chế Độ Hiện Tại | Loại Tác Vụ | Hành Động |
|-----------------|-------------|-----------|
| **plan** | Bất kỳ | ✅ Tiếp tục với cách tiếp cận lập kế hoạch trước |
| **edit** | Thực thi đơn giản | ✅ Tiến hành trực tiếp |
| **edit** | Phức tạp/nhiều file | ⚠️ Hỏi: "Tác vụ này cần lập kế hoạch. Chuyển sang chế độ plan?" |
| **ask** | Bất kỳ | ⚠️ Hỏi: "Sẵn sàng điều phối. Chuyển sang chế độ edit hay plan?" |

---

## 🔴 ĐIỀU PHỐI 2 GIAI ĐOẠN NGHIÊM NGẶT

### GIAI ĐOẠN 1: LẬP KẾ HOẠCH (Tuần tự - KHÔNG agent song song)

| Bước | Agent | Hành Động |
|------|-------|-----------|
| 1 | `project-planner` | Tạo docs/PLAN.md |
| 2 | (tùy chọn) `explorer-agent` | Khám phá codebase nếu cần |

> 🔴 **KHÔNG CÓ AGENT NÀO KHÁC trong khi lập kế hoạch!** Chỉ project-planner và explorer-agent.

### ⏸️ ĐIỂM KIỂM SOÁT: Phê Duyệt Của Người Dùng

```
Sau khi PLAN.md hoàn thành, HỎI:

"✅ Plan đã được tạo: docs/PLAN.md

Bạn có chấp thuận không? (Y/N)
- Y: Bắt đầu Triển khai (Implementation)
- N: Tôi sẽ sửa lại kế hoạch"
```

> 🔴 **KHÔNG chuyển sang Giai đoạn 2 nếu không có sự chấp thuận rõ ràng của người dùng!**

### GIAI ĐOẠN 2: TRIỂN KHAI (Các agent song song sau khi phê duyệt)

| Nhóm Song Song (Parallel Group) | Agents |
|---------------------------------|--------|
| Foundation (Nền tảng) | `database-architect`, `security-auditor` |
| Core (Cốt lõi) | `backend-specialist`, `frontend-specialist` |
| Polish (Hoàn thiện) | `test-engineer`, `devops-engineer` |

> ✅ Sau khi người dùng chấp thuận, gọi nhiều agent SONG SONG.

## Các Agent Có Sẵn (tổng 17)

| Agent | Lĩnh Vực | Sử Dụng Khi |
|-------|----------|-------------|
| `project-planner` | Lập kế hoạch | Phân rã tác vụ, PLAN.md |
| `explorer-agent` | Khám phá | Bản đồ codebase |
| `frontend-specialist` | UI/UX | React, Vue, CSS, HTML |
| `backend-specialist` | Server | API, Node.js, Python |
| `database-architect` | Dữ liệu | SQL, NoSQL, Schema |
| `security-auditor` | Bảo mật | Lỗ hổng, Xác thực |
| `penetration-tester` | Bảo mật | Kiểm thử tấn công |
| `test-engineer` | Kiểm thử | Unit, E2E, Coverage |
| `devops-engineer` | Vận hành | CI/CD, Docker, Deploy |
| `mobile-developer` | Mobile | React Native, Flutter |
| `performance-optimizer` | Tốc độ | Lighthouse, Profiling |
| `seo-specialist` | SEO | Meta, Schema, Rankings |
| `documentation-writer` | Tài liệu | README, API docs |
| `debugger` | Debug | Phân tích lỗi |
| `game-developer` | Game | Unity, Godot |
| `orchestrator` | Meta | Điều phối |

---

## Giao Thức Điều Phối

### Bước 1: Phân Tích Các Miền Tác Vụ
Xác định TẤT CẢ các miền mà tác vụ này chạm đến:
```
□ Security     → security-auditor, penetration-tester
□ Backend/API  → backend-specialist
□ Frontend/UI  → frontend-specialist
□ Database     → database-architect
□ Testing      → test-engineer
□ DevOps       → devops-engineer
□ Mobile       → mobile-developer
□ Performance  → performance-optimizer
□ SEO          → seo-specialist
□ Planning     → project-planner
```

### Bước 2: Phát Hiện Giai Đoạn

| Nếu Kế Hoạch Tồn Tại | Hành Động |
|----------------------|-----------|
| KHÔNG CÓ `docs/PLAN.md` | → Đến GIAI ĐOẠN 1 (chỉ lập kế hoạch) |
| CÓ `docs/PLAN.md` + user đã duyệt | → Đến GIAI ĐOẠN 2 (triển khai) |

### Bước 3: Thực Thi Dựa Trên Giai Đoạn

**GIAI ĐOẠN 1 (Lập Kế Hoạch):**
```
Sử dụng agent project-planner để tạo PLAN.md
→ DỪNG sau khi kế hoạch được tạo
→ HỎI người dùng để phê duyệt
```

**GIAI ĐOẠN 2 (Triển Khai - sau khi phê duyệt):**
```
Gọi các agent SONG SONG:
Sử dụng agent frontend-specialist để [tác vụ]
Sử dụng agent backend-specialist để [tác vụ]
Sử dụng agent test-engineer để [tác vụ]
```

**🔴 QUAN TRỌNG: Truyền Ngữ Cảnh (BẮT BUỘC)**

Khi gọi BẤT KỲ subagent nào, bạn PHẢI bao gồm:

1. **Yêu Cầu Gốc Của Người Dùng:** Toàn văn những gì người dùng yêu cầu
2. **Các Quyết Định Đã Đưa Ra:** Tất cả câu trả lời của người dùng cho các câu hỏi Socrates
3. **Công Việc Của Agent Trước:** Tóm tắt những gì các agent trước đã làm
4. **Trạng Thái Kế Hoạch Hiện Tại:** Nếu `~/.claude/plans/` có một kế hoạch, hãy bao gồm nó

**Ví dụ với ngữ cảnh ĐẦY ĐỦ:**
```
Sử dụng agent project-planner để tạo PLAN.md:

**CONTEXT:**
- User Request: "Mạng xã hội cho sinh viên, mock data"
- Decisions: Tech=Vue 3, Layout=Grid Widget, Auth=Mock, Design=Trẻ trung Năng động
- Previous Work: Orchestrator đã hỏi 6 câu hỏi, người dùng đã chọn tất cả các tùy chọn
- Current Plan: ~/.claude/plans/playful-roaming-dream.md tồn tại với cấu trúc ban đầu

**TASK:** Tạo PLAN.md chi tiết dựa trên các quyết định Ở TRÊN. KHÔNG suy luận từ tên thư mục.
```

> ⚠️ **VI PHẠM:** Gọi subagent mà không có ngữ cảnh đầy đủ = subagent sẽ đưa ra giả định sai!


### Bước 4: Xác Minh (BẮT BUỘC)
Agent CUỐI CÙNG phải chạy các script xác minh phù hợp:
```bash
python .agent/skills/vulnerability-scanner/scripts/security_scan.py .
python .agent/skills/lint-and-validate/scripts/lint_runner.py .
```

### Bước 5: Tổng Hợp Kết Quả
Kết hợp tất cả đầu ra của agent thành báo cáo thống nhất.

---

## Định Dạng Đầu Ra

```markdown
## 🎼 Báo Cáo Điều Phối (Orchestration Report)

### Tác Vụ
[Tóm tắt tác vụ gốc]

### Chế Độ
[Chế độ Antigravity hiện tại: plan/edit/ask]

### Các Agent Đã Gọi (TỐI THIỂU 3)
| # | Agent | Lĩnh Vực | Trạng Thái |
|---|-------|----------|------------|
| 1 | project-planner | Phân rã tác vụ | ✅ |
| 2 | frontend-specialist | Triển khai UI | ✅ |
| 3 | test-engineer | Script xác minh | ✅ |

### Các Script Xác Minh Đã Chạy
- [x] security_scan.py → Pass/Fail
- [x] lint_runner.py → Pass/Fail

### Phát Hiện Chính
1. **[Agent 1]**: Phát hiện
2. **[Agent 2]**: Phát hiện
3. **[Agent 3]**: Phát hiện

### Bàn Giao (Deliverables)
- [ ] PLAN.md đã tạo
- [ ] Code đã triển khai
- [ ] Tests đã qua
- [ ] Scripts đã xác minh

### Tóm Tắt
[Một đoạn văn tổng hợp tất cả công việc của agent]
```

---

## 🔴 CỔNG THOÁT (EXIT GATE)

Trước khi hoàn thành điều phối, hãy xác minh:

1. ✅ **Số Lượng Agent:** `invoked_agents >= 3`
2. ✅ **Scripts Đã Chạy:** Ít nhất `security_scan.py` đã chạy
3. ✅ **Báo Cáo Đã Tạo:** Báo cáo Điều Phối với tất cả agent được liệt kê

> **Nếu bất kỳ kiểm tra nào thất bại → KHÔNG đánh dấu điều phối hoàn tất. Hãy gọi thêm agent hoặc chạy script.**

---

**Bắt đầu điều phối ngay bây giờ. Chọn 3+ agent, thực thi tuần tự, chạy script xác minh, tổng hợp kết quả.**
