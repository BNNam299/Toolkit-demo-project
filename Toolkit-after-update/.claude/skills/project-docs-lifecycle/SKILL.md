---
name: project-docs-lifecycle
description:
  Common lifecycle pattern for creating project documentation. Every per-doc skill references this for directory creation, file safety, user confirmation, and quality gate invocation. Use as the shared step-by-step process for PRD, Overview, Use Cases, Functional Requirements, Wireframes, and UX Flows.
allowed-tools: Read, Write, Edit, Grep, Glob
---

<!-- APPSPEC-PRELUDE -->

> **ĐỌC KHỐI NÀY TRƯỚC.** File này lấy nguyên văn từ bộ **app-spec** rồi đưa vào Pipeline v2.
> Nội dung chuyên môn bên dưới dùng bình thường, nhưng **ba loại tham chiếu trong đó đã lỗi** — bỏ qua chúng,
> đừng đi tìm.
>
> **1. Skill không tồn tại trong bộ này.** `project-docs-contract` · `project-docs-workflow` ·
> `project-docs-prd` · `project-docs-overview` · `project-docs-uc` · `project-docs-fr` ·
> `project-docs-wireframes` · `project-docs-flows` · `project-docs-roadmap` · mọi `spec-*` · mọi
> `execution-*` · `ui-redesign` · `quick-*` · `dev-spec-driven` · `ios-debug` · `ios-icon-gen` · `mcp-xcode`.
> Chúng bị loại **có chủ đích** vì thuộc phạm vi sau bàn giao. Danh sách đầy đủ ở `.claude/KIT_MANIFEST.md`.
> Gặp câu *"phải đọc skill X trước"* mà X nằm trong danh sách này thì **bỏ qua câu đó**, không dừng, không đi tìm.
>
> **2. Đường dẫn `.claude/specs/<tên dự án>/...`** — cấu trúc của app-spec, **không có** ở đây.
> Bộ này ghi tài liệu ra `docs/<thư-mục-phase>/<doc_id>_<TÊN>.md`. Danh sách 61 tài liệu ở `docs/_INDEX.md`.
>
> **3. Bảng ánh xạ 1:1 gate→file** kiểu `gate-prd → PRD.md`. Pipeline v2 có 61 tài liệu và 12 cổng G0–G11;
> cổng đọc từ khối `QUALITY-GATE-MANIFEST` ở **cuối template tương ứng**, không từ bảng cứng.
>
> **Phần mở rộng Pipeline v2 nằm ở CUỐI file này.** Khi phần trên và phần dưới xung đột, **phần dưới thắng**.


# Project Docs Lifecycle

Every project document creator follows these four phases. Per-doc skills supply doc-type-specific content; this skill supplies the process.

---

## Phase 1: Read Context

- Read prerequisite documents listed by the per-doc skill
- If a prerequisite file does not exist, report the gap and pause
- Never fabricate content to fill missing prerequisites
- Cross-reference upstream docs for traceability IDs

---

## Phase 2: Create Directory

- Ensure `.claude/specs/[project-name]/` exists
- If the directory is missing, create it
- If the target file already exists:
  - Display the existing file path and size
  - Ask the user: overwrite / merge / skip
  - Never overwrite without explicit user approval

---

## Phase 3: Write Document

- Use the template and structure defined by the per-doc skill
- Insert content generated from context gathered in Phase 1
- Preserve section IDs and heading anchors for cross-document links

### Write incrementally (avoid oversized output)

Project docs are large (Wireframes can be 500–900+ lines; PRD/Use_Cases 500+). **Never emit
the whole document in one giant `Write`** — a single oversized output risks hitting the model's
**max output tokens** (the file gets truncated/corrupted) and long response times / timeouts.
Write the document in bounded chunks:

1. Create the file with `Write`: front matter + the **first major section** only.
2. Append **each remaining major section** with a separate `Edit` — one section per call.
3. Keep every write/edit to roughly **one major section (≈ ≤ 200–300 lines)**.
4. For a very large section (e.g. per-screen wireframes, one screen ≈ one archetype block),
   append **screen-by-screen** rather than all screens at once.
5. Run the quality gate **only after all sections are written**.

Trade-off: more tool calls, but each is size-bounded, so no content is lost to truncation.

- Invoke the quality gate specified by the per-doc skill:
  ```
  Use the quality-gate-[doc-type] skill to validate this document
  ```
- If the quality gate reports failures, fix them before proceeding

---

## Phase 4: Validate and Confirm

1. Run the quality gate one final time
2. Display a delivery summary to the user:
   - **File created**: `.claude/specs/[project-name]/[DocType].md`
   - **Sections**: count and list of top-level sections
   - **Coverage**: key stats (user stories, requirements, screens, etc.)
   - **Traceability**: upstream document IDs referenced
3. Ask the user to choose:
   - **Approve**: document accepted, move to next step
   - **Modify**: describe changes, loop back to Phase 3
   - **Pause**: stop here, resume later

---

## Non-Negotiable Rules

- Write files only under `.claude/specs/[project-name]/`
- Never overwrite an existing file without user confirmation
- Never skip the quality gate
- Never fabricate prerequisite content
- Keep section IDs and naming stable across documents
- Write long documents **section-by-section** (create with the first section, append the rest with Edit) — never emit one oversized output that could truncate or time out
- Always display a delivery summary before asking for approval
- If the user pauses, record progress so the next session can resume