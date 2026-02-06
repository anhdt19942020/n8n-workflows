---
description: Create project plan using project-planner agent. No code writing - only plan file generation.
---

# /plan - Chế Độ Lập Kế Hoạch Dự Án

$ARGUMENTS

---

## 🔴 QUY TẮC QUAN TRỌNG

1. **KHÔNG VIẾT CODE** - Lệnh này chỉ tạo file kế hoạch
2. **Sử dụng agent project-planner** - KHÔNG phải Plan subagent mặc định của Claude Code
3. **Cổng Socrates** - Hỏi các câu hỏi làm rõ trước khi lập kế hoạch
4. **Tên Động** - File kế hoạch được đặt tên dựa trên tác vụ

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
