# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [3.2.0] - 2026-07-22

### Added — Luồng cải tiến UI post-build (`/ios-ui-redesign`, độc lập)
- **Command mới `ios-ui-redesign`**: luồng thứ 4, tách khỏi project-docs. Chạy sau khi app build xong để thiết kế lại UI theo phong cách riêng. Nguồn phong cách: `--image` / `--desc` / **`--pen <name>`** (file `.pen` trong `design-token/`, đọc qua **Pencil MCP**)
- **Skill `ui-redesign`**: cỗ máy sinh (pipeline P0–P7) + **Creative Method** (Style DNA → quyết định thị giác từng màn) + vòng **screenshot self-critique**; audit UI từ app đã build, đề xuất token/component/màn, áp code qua gate execution
- **Skill `ui-redesign-craft`**: kiến thức craft — distinctiveness principles + **catalog signature-moments** + cách vượt iOS-stock (giữ SÀN UX)
- **Skill `ui-redesign-contract`**: output contract tự chứa (cây `redesign/`, schema file, readability) + **`gate-redesign`** gồm **distinctiveness bar** — contract chỉ validate, sáng tạo do skill+craft đảm nhiệm
- **Installer**: copy `design-token/*.pen` verbatim (binary mã hoá) sang `{{IDE_CONFIG_DIR}}design-token/`; thêm file mới vào danh sách verify (gồm cả `validate_cross_spec.py` bị sót ở 3.1.0)

### Changed
- `commands/ios-execute.md`: khi mọi spec `done` → gợi ý bước cuối `/ios-ui-redesign`
- `skills/ios-ui-ux/SKILL.md`: ghi chú pha redesign ghi đè mặc định "native/clarity"; SÀN UX vẫn bất di bất dịch

## [3.1.0] - 2026-07-22

### Added — Spec depth, completeness & consistency gates
- **Depth gates (nội dung, không chỉ cấu trúc)**: `spec-requirements`/`spec-design`/`spec-tasks` manifests giờ bắt buộc: phủ đủ states (loading/empty/error/offline/permission) thay cho sàn "1 AC lỗi"; bảng Validation Rules cho input; §4 Data Models ở mức field+validation; §5 Error Handling dạng bảng phủ mọi ERR/AF; §7 liệt kê đủ 4 state + a11y/dark-mode; mỗi Correctness Property (P#) phải có task `pbt`
- **Completeness gate (chống rơi affordance)**: back-trace hai chiều Wireframe↔FR — mọi Component/Interaction phải có FR+AC hoặc khai out-of-scope; mỗi WF (kể cả modal) có FR backing riêng; "no behavior without acceptance criteria"; secondary actions (settings/share/skip/help/export) phải thành FR
- **Consistency gate (chống orphan/đứt trace)**: script mới `scripts/validate_cross_spec.py` bắt orphan spec, dangling/mis-cited WF, FR trùng (`Same as FR-XXX`), NFR-ID collision; kèm quy tắc WF-resolve trong `spec-quality-gates` và kiểm nhất quán FR-label/owner/cơ chế chéo trong roadmap
- **Real-World Readiness checklist** dùng chung trong `spec-creation-contract` (10 chiều) làm định nghĩa chuẩn cho "đủ chi tiết"

### Changed
- Gỡ "cửa thoát" cho phép làm tới floor tối thiểu: `project-docs-fr`, `project-docs-contract` — cắt scope phải ghi Scope Decision Record, không mặc nhiên bỏ edge case
- `execution-quick` chỉ dùng cho prototype/thử nghiệm nhỏ, cấm dùng cho core/production feature
- PBT cho correctness property chuyển từ optional → required (`spec-tasks`, `execution-implement`)

## [3.0.0] - 2026-07-21

### Major Release
- **Quick track chuyển sang skills**: `quick-plan`/`quick-implement` từ commands trở thành skills (`quick-plan-skill`, `quick-implement-skill`), commands `q-plan`/`q-implement` chỉ còn delegate
- **Skill mới `ios-icon-gen`**: sinh iOS app icon imageset từ SF Symbols hoặc Iconify API (kèm `scripts/generate_icons.swift`, `iconify_gen.sh`)
- **Installer**: copy nested skill assets (scripts) nguyên vẹn khi cài đặt

### Enhanced
- Cập nhật execution skills và iOS skills (architecture, components, ui-ux, debug)
- Tinh chỉnh project-docs workflow/contract và lifecycle

### Fixed
- Agent transform dùng `permission` format thay cho `tools` đã deprecated
- Sửa MCP config validation khi migrate sang Claude Code format

## [2.0.1] - 2025-01-22

### Added
- **Enhanced PRD Market Research** (project-docs-prd skill)
  - New "Option B" AI-Assisted Discovery for users without clear direction
  - Global market opportunities research with IAP business model suggestions
  - Propose 2-3 directions with target user, problem, core action, IAP strategy

### Enhanced
- **Comprehensive Market Research Phase (Phase 2)**
  - Strict data freshness: Only 2025-2026 data (January 2025 to current)
  - Minimum 18 sources across 6 categories (was 14)
  - New "Data Range" column in Evidence Table with format `[2025-01 to 2026-XX]`
  - Data Quality Priority: Real-time app store > Platform estimates > Media > Community

### Improved
- **Academic & Industry Reports**: Queries now target 2025-2026 reports with `after:2024-12-31` filter
- **News & Tech Blogs**: All queries use date filters, publication dates verified
- **App Store Intelligence**: Enhanced Sensor Tower, AppMagic, Apptopia integration
- **Community & Social**: Reddit, HN, Product Hunt filtered for 2025-2026 content

### Data Sources
- Sensor Tower: Blog, reports, market indices, download/revenue estimates
- AppMagic: Public top charts, live rankings, market research
- Apptopia: Public charts, trending, market data/statistical models
- AppTweak: ASO insights, keyword rankings
- Direct app store analysis: iOS App Store, Google Play

## [2.0.0] - 2025-01-XX

### Major Release
- Complete architecture refactor: Agents → Skills-based workflow
- Only 1 agent remains (spec-uiux-analyzer)
- All 3 commands use skill-based workflows: /project-docs, /ios-spec, /execute
- Total 35+ skills across all layers
- 11 document templates created

### Migration
- 16 old agents removed (project-docs: 9, spec: 6, execution: 4)
- 29 new skills created
- Commands updated: project-docs.md, spec.md, execute.md
- Enhanced contracts: project-docs-contract, spec-creation-contract, execution-contract

### Stats
- 5182 insertions(+), 6409 deletions(-)
- 72 files changed

## [1.x.x] - Earlier versions
- Initial implementation
- 3-orchestrator architecture (project-docs, spec, execution)
- Agent-based workflow
