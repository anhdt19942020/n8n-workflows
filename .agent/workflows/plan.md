---
description: Create project plan using project-planner agent. No code writing - only plan file generation.
---

# /plan - Chế Độ Lập Kế Hoạch Dự Án

$ARGUMENTS

> 🔴 **BẮT BUỘC (Khởi tạo Serena):**
> Trước khi thực hiện bất kỳ công việc nào trong lệnh này, Agent PHẢI:
>
> 1. Gọi \`mcp_serena_check_onboarding_performed\`
> 2. Gọi \`mcp_serena_activate_project\` với đường dẫn thư mục hiện tại.
> (Bỏ qua nếu Serena đã được kích hoạt trong phiên làm việc này).

## 🔴 QUY TẮC QUAN TRỌNG

1. **KHÔNG VIẾT CODE** - Lệnh này chỉ tạo file kế hoạch
2. **Sử dụng agent project-planner** - KHÔNG phải Plan subagent mặc định của Claude Code
3. **Cổng Socrates** - Hỏi các câu hỏi làm rõ trước khi lập kế hoạch
4. **Tên Động** - File kế hoạch được đặt tên dựa trên tác vụ

---

---

## Phối Hợp Với Sequential Thinking

Workflow này **có thể** sử dụng Sequential Thinking để làm rõ bài toán trước khi sinh phương án.

### Khi nên dùng Sequential Thinking

Agent nên dùng Sequential Thinking nếu có một trong các dấu hiệu sau:

- bài toán còn mơ hồ hoặc thiếu phạm vi rõ ràng
- có nhiều ràng buộc kỹ thuật, thời gian, vận hành hoặc bảo trì
- có nhiều hơn một hướng tiếp cận hợp lý
- chủ đề liên quan đến kiến trúc, refactor lớn, chiến lược hệ thống, hoặc quyết định dài hạn
- cần bóc tách tiêu chí đánh giá trước khi đề xuất phương án

### Khi không cần dùng Sequential Thinking

Agent có thể bỏ qua nếu:

- câu hỏi nhỏ và phạm vi rất rõ
- chỉ cần liệt kê nhanh vài ý tưởng đơn giản
- không có tradeoff quan trọng cần phân tích

### Vai trò của Sequential Thinking trong workflow này

Nếu được dùng, Sequential Thinking chỉ có nhiệm vụ:

- làm rõ vấn đề thật sự cần giải
- tách mục tiêu, ràng buộc và giả định
- xác định tiêu chí đánh giá phương án
- đảm bảo các phương án khác nhau thực sự

Sequential Thinking **không** thay thế workflow này.  
Output cuối cùng vẫn phải theo đúng định dạng của `/brainstorm`.

---

## Tác Vụ

Sử dụng agent `project-planner` với ngữ cảnh này:

```
CONTEXT:
- User Request: $ARGUMENTS
- Mode: PLANNING ONLY (no code)
- Output: docs/PLAN-{task-slug}.md (dynamic naming)

NAMING RULES:
1. Extract 2-3 key words from request
2. Lowercase, hyphen-separated
3. Max 30 characters
4. Example: "e-commerce cart" → PLAN-ecommerce-cart.md

RULES:
1. Follow project-planner.md Phase -1 (Context Check)
2. Follow project-planner.md Phase 0 (Socratic Gate)
3. Create PLAN-{slug}.md with task breakdown
4. DO NOT write any code files
5. REPORT the exact file name created
```

---

## Đầu Ra Mong Đợi

| Bàn Giao | Vị Trí |
|----------|--------|
| Kế Hoạch Dự Án | `docs/PLAN-{task-slug}.md` |
| Phân Rã Tác Vụ | Bên trong file plan |
| Giao Việc Cho Agent | Bên trong file plan |
| Checklist Xác Minh | Giai đoạn X trong file plan |

---

## Sau Khi Lập Kế Hoạch

Nói với người dùng:

```
[OK] Plan created: docs/PLAN-{slug}.md

Các bước tiếp theo:
- Xem lại kế hoạch
- Chạy `/create` để bắt đầu triển khai
- Hoặc sửa đổi kế hoạch thủ công
```

---

## Ví Dụ Đặt Tên

| Yêu Cầu | File Plan |
|---------|-----------|
| `/plan e-commerce site with cart` | `docs/PLAN-ecommerce-cart.md` |
| `/plan mobile app for fitness` | `docs/PLAN-fitness-app.md` |
| `/plan add dark mode feature` | `docs/PLAN-dark-mode.md` |
| `/plan fix authentication bug` | `docs/PLAN-auth-fix.md` |
| `/plan SaaS dashboard` | `docs/PLAN-saas-dashboard.md` |

---

## Sử Dụng

```
/plan e-commerce site with cart
/plan mobile app for fitness tracking
/plan SaaS dashboard with analytics
```
