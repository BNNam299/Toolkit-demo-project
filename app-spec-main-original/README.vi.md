# iOS Spec-Driven Development Toolkit

> Xây dựng ứng dụng iOS với AI, có kỷ luật.

Bộ công cụ hoàn chỉnh biến đổi quy trình phát triển iOS với AI tự động hoá có cấu trúc — từ tài liệu dự án đến code production-ready, kèm hỗ trợ redesign UI sau khi build.

---

## Commands

### Nhóm 1: Spec-Driven Flow (3 lệnh chính)

Pipeline có thứ tự: **Project Docs → Spec → Execute**.

| Lệnh | Mục đích | Cách dùng |
|------|----------|-------|
| `/ios-project-docs` | Tạo đầy đủ tài liệu dự án (PRD, Overview, UC, FR, Wireframes, UX Flows, Roadmap) | `/ios-project-docs MyApp` |
| `/ios-spec` | Tạo đặc tả tính năng (requirements → design → tasks) | `/ios-spec user-login` |
| `/ios-execute` | Thực thi implementation từ tasks đã duyệt | `/ios-execute user-login` |

```
📱 PROJECT LEVEL → /ios-project-docs MyApp
   [PRD, Overview, UC, FR, Wireframes, Flows, Roadmap]
📋 FEATURE LEVEL → /ios-spec user-login
   [requirements.md, design.md, tasks.md]
💻 CODE LEVEL → /ios-execute user-login
   [SwiftUI code + tests + commit]
```

### Nhóm 2: Tiện ích bổ sung (3 lệnh độc lập)

| Lệnh | Mục đích | Cách dùng |
|------|----------|-------|
| `/ios-ui-redesign` | Redesign UI app đã build xong theo phong cách riêng (dùng Pencil `.pen` / ảnh mẫu / mô tả) | `/ios-ui-redesign --pen neo` |
| `/q-plan` | AI đóng vai Senior Architect: research codebase → reuse UI/service hiện có → sinh blueprint duy nhất ở `/q-plan/[yyyy-MM-dd]-[name]-plan.md` gồm 3 mục: **Scope of Impact** (file chạm), **Detailed Usecases** (hành vi/luồng/edge case), **Interface & Function Signatures** (chữ ký hàm + comment step-by-step). Không code — chỉ xương. | `/q-plan "add dark mode"` |
| `/q-implement` | Implement nhanh từ blueprint `/q-plan/` | `/q-implement "add dark mode"` |

> **`/ios-ui-redesign`** chạy độc lập, không thuộc pipeline — dùng sau khi app đã build xong.
> **`/q-plan` + `/q-implement`** dành cho prototype/thử nghiệm nhỏ, không thay thế spec-driven flow cho production.

---

## Cài đặt

**Yêu cầu**: [UV](https://docs.astral.sh/uv/getting-started/installation/)

```bash
uvx --from 'git+ssh://git@svn.as.local/avn_ios/app-spec.git@main' ios-spec-driven install
```

---

## Quality Gates

Kiểm tra nằm ở cuối mỗi file template — tự động validate đầu ra theo các chiều:
- **Depth gates**: coverage states (loading/empty/error/offline/permission), validation rules, data models, error handling
- **Completeness gates**: back-trace Wireframe↔FR, "no behavior without acceptance criteria"
- **Consistency gates**: no orphan spec, no dangling/mis-cited WF, no FR-ID collision
- **Redesign gate**: distinctiveness bar + UX sàn (4 state, a11y, contrast ≥4.5:1, ≥44pt, dark mode)