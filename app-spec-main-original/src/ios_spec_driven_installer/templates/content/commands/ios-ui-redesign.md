---
description: Standalone post-build UI redesign to a distinctive style (style ref → proposal → apply)
allowed-tools: Read, Write, Edit, Grep, Glob, Task, Bash, mcp__pencil__get_editor_state, mcp__pencil__get_variables, mcp__pencil__get_guidelines, mcp__pencil__get_screenshot, mcp__pencil__snapshot_layout, mcp__pencil__export_nodes, mcp__pencil__export_html, mcp__pencil__batch_get
---

# COMMAND: Redesign App UI to a Distinctive Style (independent flow)

Cải tiến UI của **app đã build xong** theo một **phong cách riêng**. Đây là **luồng thứ 4, độc lập** —
song song `/ios-project-docs`, `/ios-spec`, `/ios-execute`. **Không** thuộc pipeline project-docs, **không**
dùng `project-docs-quality-gates`.

`ui-redesign-contract` chỉ *kiểm tra* đầu ra; phần **sáng tạo** nằm ở `ui-redesign` (Creative Method) +
`ui-redesign-craft` (signature-moments) + vòng screenshot-critique. Xem 3 skill đó.

## Input ($ARGUMENTS) — 1 trong 3 nguồn phong cách

| Cờ | Ý nghĩa |
|----|---------|
| `--pen <name>` | Tên file `.pen` trong `{{IDE_CONFIG_DIR}}design-token/` (vd: `neo`, `bento`, `Swiss-Clean`, `Monochrome-Type`) → học thiết kế + rút design token qua **Pencil MCP** |
| `--image <path...>` | Một hoặc nhiều ảnh mẫu phong cách |
| `--desc "<text>"` | Mô tả phong cách bằng chữ |

Không có nguồn → hỏi tương tác và liệt kê các `.pen` có sẵn. Vẫn trống → DỪNG (không tự chế identity).

## Prerequisite

- App đã build/launch được: mọi `{{IDE_CONFIG_DIR}}specs/*/spec-state.json` có `stage: done`.
  Nếu chưa → DỪNG, yêu cầu hoàn tất `/ios-execute` trước.

## Workflow (đều gọi skill `ui-redesign`, KHÔNG gọi skill project-docs)

| Step | Giai đoạn | Skill (phase) | Kết quả |
|------|-----------|---------------|---------|
| 1 | Intake + Audit | `ui-redesign` (P0–P2) | `style-reference.md`, `current-ui-audit.md` (+ screenshot before) |
| 2 | Proposal + Gate | `ui-redesign` (P3–P5) | `design-tokens.md`, `components.md`, `screens/*`, `flows.md`, `manifest.json` + `gate-redesign` PASS |
| 3 | Apply + Verify/Critique | `ui-redesign` (P6–P7) | code đã redesign + screenshot after + before/after |

Sau **mỗi step**: trình bày tóm tắt và hỏi **Approve / Modify / Pause**. Cập nhật `redesign-state.json`.

## Rules

- Giai đoạn đề xuất (Step 1–2): chỉ ghi dưới `{{IDE_CONFIG_DIR}}specs/[project-name]/redesign/`.
- Giai đoạn áp dụng (Step 3): chỉ ghi `{{IDE_CONFIG_DIR}}shared/Styles|Components/` và `Features/*/Views/*`.
- **KHÔNG đổi business logic** (chỉ UI/visual/motion/navigation). Việc chạm logic → tách ra, báo dùng `/ios-spec`.
- **Không vượt gate fail**: `gate-redesign` (đề xuất) + Structure/Reuse-First/UX Compliance/DSS + Build/Integration (khi áp code).
- **Giữ SÀN UX** khi áp phong cách mới: 4 state, a11y, contrast ≥4.5:1, ≥44pt, dark mode.
- File `.pen` mã hoá → chỉ đọc qua Pencil MCP, cấm Read/Grep trực tiếp.

## Options
- `--mode static` — chỉ audit tĩnh (bỏ screenshot; dùng khi simulator không khả dụng)
- `--screens <ViewName,...>` — chỉ redesign một số màn (mặc định: toàn bộ màn của app)

## Usage
```
/ios-ui-redesign --pen neo
/ios-ui-redesign --image ./ref/home.png ./ref/detail.png
/ios-ui-redesign --desc "neo-brutalist, high-contrast, bold borders"
```
