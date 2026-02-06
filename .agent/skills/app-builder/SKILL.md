---
name: app-builder
description: Main application building orchestrator. Creates full-stack applications from natural language requests. Determines project type, selects tech stack, coordinates agents.
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, Agent
---

# App Builder - Trình Điều Phối Xây Dựng Ứng Dụng

> Phân tích yêu cầu người dùng, xác định tech stack, lên kế hoạch cấu trúc, và điều phối các agent.

## 🎯 Quy Tắc Đọc Chọn Lọc

**CHỈ đọc các file liên quan đến yêu cầu!** Kiểm tra bản đồ nội dung, tìm cái bạn cần.

| File | Mô Tả | Khi Nào Đọc |
|------|-------|-------------|
| `project-detection.md` | Ma trận từ khóa, phát hiện loại dự án | Bắt đầu dự án mới |
| `tech-stack.md` | Stack mặc định 2025, các lựa chọn thay thế | Chọn công nghệ |
| `agent-coordination.md` | Pipeline agent, thứ tự thực thi | Điều phối đa agent |
| `scaffolding.md` | Cấu trúc thư mục, các file cốt lõi | Tạo cấu trúc dự án |
| `feature-building.md` | Phân tích tính năng, xử lý lỗi | Thêm tính năng vào dự án hiện có |
| `templates/SKILL.md` | **Template dự án** | Scaffolding dự án mới |

---

## 📦 Templates (13)

Scaffolding khởi động nhanh cho dự án mới. **Chỉ đọc template phù hợp!**

| Template | Tech Stack | Khi Nào Dùng |
|----------|------------|--------------|
| [nextjs-fullstack](templates/nextjs-fullstack/TEMPLATE.md) | Next.js + Prisma | Full-stack web app |
| [nextjs-saas](templates/nextjs-saas/TEMPLATE.md) | Next.js + Stripe | Sản phẩm SaaS |
| [nextjs-static](templates/nextjs-static/TEMPLATE.md) | Next.js + Framer | Landing page |
| [nuxt-app](templates/nuxt-app/TEMPLATE.md) | Nuxt 3 + Pinia | Vue full-stack app |
| [express-api](templates/express-api/TEMPLATE.md) | Express + JWT | REST API |
| [python-fastapi](templates/python-fastapi/TEMPLATE.md) | FastAPI | Python API |
| [react-native-app](templates/react-native-app/TEMPLATE.md) | Expo + Zustand | Mobile app |
| [flutter-app](templates/flutter-app/TEMPLATE.md) | Flutter + Riverpod | Cross-platform mobile |
| [electron-desktop](templates/electron-desktop/TEMPLATE.md) | Electron + React | Desktop app |
| [chrome-extension](templates/chrome-extension/TEMPLATE.md) | Chrome MV3 | Browser extension |
| [cli-tool](templates/cli-tool/TEMPLATE.md) | Node.js + Commander | CLI app |
| [monorepo-turborepo](templates/monorepo-turborepo/TEMPLATE.md) | Turborepo + pnpm | Monorepo |

---

## 🔗 Các Agent Liên Quan

| Agent | Vai Trò |
|-------|---------|
| `project-planner` | Chia nhỏ tác vụ, biểu đồ phụ thuộc |
| `frontend-specialist` | UI components, pages |
| `backend-specialist` | API, logic nghiệp vụ |
| `database-architect` | Schema, migrations |
| `devops-engineer` | Deployment, preview |

---

## Ví Dụ Sử Dụng

```
User: "Make an Instagram clone with photo sharing and likes"

Quy trình App Builder:
1. Loại dự án: Social Media App
2. Tech stack: Next.js + Prisma + Cloudinary + Clerk
3. Tạo kế hoạch:
   ├─ Database schema (users, posts, likes, follows)
   ├─ API routes (12 endpoints)
   ├─ Pages (feed, profile, upload)
   └─ Components (PostCard, Feed, LikeButton)
4. Điều phối các agent
5. Báo cáo tiến độ
6. Chạy preview
```
