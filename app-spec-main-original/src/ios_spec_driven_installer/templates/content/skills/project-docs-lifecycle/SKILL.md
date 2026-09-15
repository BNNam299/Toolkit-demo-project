---
name: project-docs-lifecycle
description:
  Common lifecycle pattern for creating project documentation. Every per-doc skill references this for directory creation, file safety, user confirmation, and quality gate invocation. Use as the shared step-by-step process for PRD, Overview, Use Cases, Functional Requirements, Wireframes, and UX Flows.
allowed-tools: Read, Write, Edit, Grep, Glob
---

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

- Ensure `{{IDE_CONFIG_DIR}}specs/[project-name]/` exists
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
   - **File created**: `{{IDE_CONFIG_DIR}}specs/[project-name]/[DocType].md`
   - **Sections**: count and list of top-level sections
   - **Coverage**: key stats (user stories, requirements, screens, etc.)
   - **Traceability**: upstream document IDs referenced
3. Ask the user to choose:
   - **Approve**: document accepted, move to next step
   - **Modify**: describe changes, loop back to Phase 3
   - **Pause**: stop here, resume later

---

## Non-Negotiable Rules

- Write files only under `{{IDE_CONFIG_DIR}}specs/[project-name]/`
- Never overwrite an existing file without user confirmation
- Never skip the quality gate
- Never fabricate prerequisite content
- Keep section IDs and naming stable across documents
- Write long documents **section-by-section** (create with the first section, append the rest with Edit) — never emit one oversized output that could truncate or time out
- Always display a delivery summary before asking for approval
- If the user pauses, record progress so the next session can resume