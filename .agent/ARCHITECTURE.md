# Kiến trúc Antigravity Kit

> **Phiên bản 5.0** - Bộ công cụ mở rộng khả năng Agent AI toàn diện

---

## 📋 Tổng quan

Antigravity Kit là một hệ thống mô-đun bao gồm:
- **16 Agent Chuyên gia** - Các persona AI dựa trên vai trò
- **40 Skill** - Các mô-đun kiến thức chuyên biệt theo miền
- **11 Workflow** - Các quy trình lệnh slash

---

## 🏗️ Cấu trúc thư mục

```
.agent/
├── ARCHITECTURE.md          # File này
├── agents/                  # 16 Agent Chuyên gia
├── skills/                  # 40 Skill
├── workflows/               # 11 Quy trình lệnh Slash
├── rules/                   # Các quy tắc toàn cục (Global Rules)
└── .shared/                 # Tài nguyên chia sẻ
```

---

## 🤖 Agents (16)

Các persona AI chuyên gia cho các lĩnh vực khác nhau.

| Agent | Trọng tâm | Skill được sử dụng |
|-------|-----------|--------------------|
| `orchestrator` | Điều phối đa agent | parallel-agents, behavioral-modes |
| `project-planner` | Khám phá, lập kế hoạch tác vụ | brainstorming, plan-writing, architecture |
| `frontend-specialist` | Web UI/UX | frontend-design, react-patterns, tailwind-patterns |
| `backend-specialist` | API, logic nghiệp vụ | api-patterns, nodejs-best-practices, database-design |
| `database-architect` | Schema, SQL | database-design, prisma-expert |
| `mobile-developer` | iOS, Android, RN | mobile-design |
| `game-developer` | Logic game, cơ chế | game-development |
| `devops-engineer` | CI/CD, Docker | deployment-procedures, docker-expert |
| `security-auditor` | Tuân thủ bảo mật | vulnerability-scanner, red-team-tactics |
| `penetration-tester` | Bảo mật tấn công (Offensive security) | red-team-tactics |
| `test-engineer` | Chiến lược kiểm thử | testing-patterns, tdd-workflow, webapp-testing |
| `debugger` | Phân tích nguyên nhân gốc rễ | systematic-debugging |
| `performance-optimizer` | Tốc độ, Web Vitals | performance-profiling |
| `seo-specialist` | Xếp hạng, hiển thị | seo-fundamentals, geo-fundamentals |
| `documentation-writer` | Hướng dẫn, tài liệu | documentation-templates |
| `explorer-agent` | Phân tích codebase | - |

---

## 🧠 Skills (40)

Các mô-đun kiến thức chuyên biệt theo miền. Skill được tải theo yêu cầu dựa trên ngữ cảnh tác vụ.

### Frontend & UI
| Skill | Mô tả |
|-------|-------|
| `react-patterns` | React hooks, state, hiệu năng |
| `nextjs-best-practices` | App Router, Server Components |
| `tailwind-patterns` | Tiện ích Tailwind CSS v4 |
| `frontend-design` | UI/UX patterns, hệ thống thiết kế |
| `ui-ux-pro-max` | 50 styles, 21 bảng màu, 50 fonts |

### Backend & API
| Skill | Mô tả |
|-------|-------|
| `laravel-architecture` | Master router cho Laravel Backend patterns |
| `laravel-patterns` | Controller, Service, Repository, DTO, Enum, Query (14 patterns) |
| `api-patterns` | REST, GraphQL, tRPC |
| `nestjs-expert` | NestJS modules, DI, decorators |
| `nodejs-best-practices` | Node.js async, modules |
| `python-patterns` | Tiêu chuẩn Python, FastAPI |

### Database
| Skill | Mô tả |
|-------|-------|
| `database-design` | Thiết kế schema, tối ưu hóa |
| `prisma-expert` | Prisma ORM, migrations |

### TypeScript/JavaScript
| Skill | Mô tả |
|-------|-------|
| `typescript-expert` | Lập trình cấp type, hiệu năng |

### Cloud & Infrastructure
| Skill | Mô tả |
|-------|-------|
| `docker-expert` | Container hóa, Compose |
| `deployment-procedures` | CI/CD, quy trình deploy |
| `server-management` | Quản lý hạ tầng |

### Testing & Quality
| Skill | Mô tả |
|-------|-------|
| `testing-patterns` | Jest, Vitest, các chiến lược |
| `webapp-testing` | E2E, Playwright |
| `tdd-workflow` | Phát triển hướng kiểm thử (TDD) |
| `code-review-checklist` | Tiêu chuẩn review code |
| `lint-and-validate` | Linting, validation |

### Security
| Skill | Mô tả |
|-------|-------|
| `vulnerability-scanner` | Kiểm toán bảo mật, OWASP |
| `red-team-tactics` | Bảo mật tấn công (Offensive security) |

### Architecture & Planning
| Skill | Mô tả |
|-------|-------|
| `app-builder` | Dựng khung ứng dụng Full-stack |
| `architecture` | Các mẫu thiết kế hệ thống |
| `plan-writing` | Lập kế hoạch tác vụ, phân rã |
| `brainstorming` | Hỏi đáp Socrates |

### Mobile
| Skill | Mô tả |
|-------|-------|
| `mobile-design` | Mobile UI/UX patterns |

### Game Development
| Skill | Mô tả |
|-------|-------|
| `game-development` | Logic game, cơ chế |

### SEO & Growth
| Skill | Mô tả |
|-------|-------|
| `seo-fundamentals` | SEO, E-E-A-T, Core Web Vitals |
| `geo-fundamentals` | Tối ưu hóa GenAI |

### Shell/CLI
| Skill | Mô tả |
|-------|-------|
| `bash-linux` | Lệnh Linux, scripting |
| `powershell-windows` | Windows PowerShell |

### Khác
| Skill | Mô tả |
|-------|-------|
| `git-commit-helper` | Tạo commit message chuẩn |
| `clean-code` | Tiêu chuẩn mã nguồn (Toàn cục) |
| `behavioral-modes` | Các persona Agent |
| `parallel-agents` | Các mẫu đa agent |
| `mcp-builder` | Model Context Protocol |
| `documentation-templates` | Định dạng tài liệu |
| `i18n-localization` | Quốc tế hóa |
| `performance-profiling` | Web Vitals, tối ưu hóa |
| `systematic-debugging` | Khắc phục sự cố (Troubleshooting) |

---

## 🔄 Workflows (11)

Các quy trình lệnh slash. Gọi bằng `/command`.

| Lệnh | Mô tả |
|------|-------|
| `/brainstorm` | Khám phá kiểu Socrates |
| `/create` | Tạo tính năng mới |
| `/debug` | Debug vấn đề |
| `/deploy` | Deploy ứng dụng |
| `/enhance` | Cải thiện mã hiện có |
| `/orchestrate` | Điều phối đa agent |
| `/plan` | Phân rã tác vụ |
| `/preview` | Xem trước thay đổi |
| `/status` | Kiểm tra trạng thái dự án |
| `/test` | Chạy test |
| `/ui-ux-pro-max` | Thiết kế với 50 phong cách |

---

## 🎯 Giao thức Tải Skill

```
Yêu cầu người dùng → Khớp mô tả Skill → Tải SKILL.md
                                             ↓
                                     Đọc references/
                                             ↓
                                     Đọc scripts/
```

### Cấu trúc Skill

```
skill-name/
├── SKILL.md           # (Bắt buộc) Metadata & hướng dẫn
├── scripts/           # (Tùy chọn) Script Python/Bash
├── references/        # (Tùy chọn) Template, tài liệu
└── assets/            # (Tùy chọn) Hình ảnh, logo
```

### Các Skill Nâng cao (có scripts/references)

| Skill | Files | Phạm vi |
|-------|-------|---------|
| `laravel-patterns` | 14 | Controller, Service, Repository, DTO, Enum, Query, Best Practices |
| `typescript-expert` | 5 | Utility types, tsconfig, cheatsheet |
| `ui-ux-pro-max` | 27 | 50 styles, 21 bảng màu, 50 fonts |
| `app-builder` | 20 | Dựng khung Full-stack |

---

## 📊 Thống kê

| Chỉ số | Giá trị |
|--------|---------|
| **Tổng số Agent** | 16 |
| **Tổng số Skill** | 42 |
| **Tổng số Workflow** | 11 |
| **Độ phủ** | ~90% phát triển web/mobile/backend |

---

## 🔗 Tham khảo nhanh

| Nhu cầu | Agent | Skill |
|---------|-------|-------|
| Web App | `frontend-specialist` | react-patterns, nextjs-best-practices |
| API | `backend-specialist` | api-patterns, nodejs-best-practices |
| Mobile | `mobile-developer` | mobile-design |
| Database | `database-architect` | database-design, prisma-expert |
| Security | `security-auditor` | vulnerability-scanner |
| Testing | `test-engineer` | testing-patterns, webapp-testing |
| Debug | `debugger` | systematic-debugging |
| Plan | `project-planner` | brainstorming, plan-writing |
