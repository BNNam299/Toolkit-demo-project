<!-- PROVENANCE — do build script sinh, KHÔNG sửa tay
nguồn      : prd-builder.skill  →  SKILL.md
nhập ngày  : 2026-08-09
trạng thái : chép nguyên văn, không tóm tắt, không diễn giải
cập nhật   : xuất lại file .skill từ Claude rồi chạy lại build script
-->

---
name: prd-builder
description: "Collaboratively build a complete Product Requirements Document (PRD) when starting a new product or project, following the team's standard PRD template, then export it to .docx. Use this skill whenever the user mentions starting a new project/product/app, writing or filling a PRD, 'tài liệu yêu cầu sản phẩm', brainstorming product requirements, defining MVP scope, personas, competitive analysis, monetization strategy, or KPIs for a new product — even if they don't say 'PRD' explicitly. Also use when the user wants to continue, review, update, or export an in-progress PRD. This skill drives a non-linear, section-by-section brainstorm (start anywhere), deep multi-angle research, and produces the final Word document."
---

# PRD Builder

Guide a Product Owner through building a complete PRD for a new product, one section at a time, in whatever order fits their thinking — then export a polished `.docx` that follows the team's standard template.

The PRD shapes the entire project's path. Treat this as high-stakes collaborative thinking, not form-filling. Your job is equal parts facilitator (draw out what the PO knows), researcher (fill gaps with evidence), and devil's advocate (stress-test weak assumptions before they become expensive).

**Language**: Mirror the user. The template is Vietnamese-first with English terms kept as-is (PRD, MVP, retention, streak, freemium...). Write PRD content the same way unless asked otherwise.

## The three modes

Every turn of a PRD session is one of three modes. Move between them freely; tell the user which mode you're in only when it helps.

1. **Brainstorm** — ask focused questions, propose drafts, challenge assumptions, converge on content for one section.
2. **Research** — gather evidence (competitors, market size, pricing, user complaints). Read `references/research-playbook.md` before any research task.
3. **Write & track** — commit agreed content into the working file, update the status board, check cross-section consistency.

## Session workflow

### 0. Setup (first message of a new PRD)

Create a working directory and seed the state file:

```bash
mkdir -p /home/claude/prd-<project-slug>
cp <skill-dir>/assets/prd_skeleton.md /home/claude/prd-<project-slug>/prd_working.md
touch /home/claude/prd-<project-slug>/research_log.md
```

`prd_working.md` is the single source of truth. It follows strict markdown conventions (see "Working file conventions" below) so the export script can convert it deterministically. `research_log.md` accumulates raw findings, sources, and dates so nothing gets lost between sessions.

Ask (or infer) the **depth mode** at setup and record it in the meta block: **Lite** (S1-S9 + Kiếm tiền + Phụ lục rút gọn — dự án nhỏ/khám phá) hoặc **Full** (đủ 16 section theo mẫu chuẩn ScreenTimeControl — sản phẩm sẽ build thật). Full mode thêm: Danh sách Màn hình, Analytics & event taxonomy, Giả định/Rủi ro, Câu hỏi Mở, Điều phối Triển khai, và Phụ lục governance (Bảng Bằng chứng + Cổng Chất lượng). Xem block "Full mode" trong `references/template-structure.md`. Với app subscription, luồng Onboarding Chi tiết trong S8 (spec từng màn + event riêng) được khuyến nghị ở CẢ hai mode — onboarding là cỗ máy conversion của mô hình freemium.

Then run a short intake — 3-4 questions max, conversational, not a form:
- One-liner của ý tưởng? (what is it, for whom)
- Bối cảnh: sản phẩm mới hoàn toàn, clone-and-improve một category có sẵn, hay mở rộng portfolio?
- Đã có gì trong tay? (Figma, nghiên cứu đối thủ, số liệu, deadline, team)
- Platform & ràng buộc lớn đã biết (iOS/Android, budget, timeline)

### 1. Pick the entry point (non-linear by design)

The template's 10 sections are NOT filled in order. After intake, read the routing table in `references/template-structure.md` (section "Entry-point routing") and recommend where to start, with a one-line reason. Typical routings:

- Idea is vague / user-driven hunch → start **Section 3 (User Problem & Personas)**
- "Category X is proven, we want in" (common for mobile studios) → start **Section 4 (Competitive Analysis)**
- Hard deadline or fixed team → start **Section 6 (Scope)** and work backward
- Monetization-first bet ("subscription app in niche Y") → start **Section 10 (Monetization)** + Section 4 together
- Leadership already wrote a vision memo → start **Section 1 (Executive Summary)** to formalize, then validate downward

Always show the status board (below) and let the PO override. Never force a sequence.

### 2. Brainstorm a section

For the chosen section, open `references/template-structure.md` and read that section's block. It contains: what the section is for, the question bank, quality bar, common failure modes, and which other sections it feeds/depends on.

Brainstorm rules:
- Ask **2-4 questions at a time**, never a wall of questions. Prefer concrete over abstract ("kể tôi nghe lần gần nhất bạn thấy ai đó gặp vấn đề này" beats "pain point là gì").
- After the PO answers, **draft the content yourself** in template voice and show it for reaction. POs edit drafts far faster than they write from blank.
- Play devil's advocate on load-bearing claims once per section: the assumption that, if wrong, kills the product. Flag it explicitly: `⚠ Giả định cần kiểm chứng: ...`
- Tag every item you write into the working file with a status: `[CONFIRMED]` (PO agreed), `[DRAFT]` (your proposal awaiting reaction), `[RESEARCH]` (needs evidence). Strip tags only at export.
- When the section needs facts you don't have, switch to Research mode rather than inventing numbers.

### 3. Research mode

Read `references/research-playbook.md` and follow the relevant play (competitor matrix, review mining, market sizing, pricing benchmark, why-now analysis). Two hard rules from the template itself:

- **Label estimates.** Apple/Google don't publish DAU, retention, or revenue. Anything inferred must be marked **ước tính** with the inference basis. The template has a dedicated methodology note for this — keep it honest.
- **Log sources.** Every external fact goes into `research_log.md` with source + date before it goes into the PRD.

If web search is available, use it aggressively — competitor data goes stale fast. If not, say so, provide knowledge-cutoff-dated analysis, and mark items `[RESEARCH: verify with live data]`.

### 4. Consistency pass (after every section)

Sections interlock. After committing a section, run its dependency checklist from `references/template-structure.md` (section "Dependency map"). The three most common breaks:
- Success criteria (S1) ↔ KPIs (S5) ↔ MVP scope (S6): can this scope plausibly move those numbers?
- Personas (S3) ↔ user flows (S8) ↔ feature table (S7): does every MVP feature serve a named persona's stated need?
- Pricing (S10) ↔ competitor anchors (S4): is the price justified by the matrix, or wishful?

Report any break to the PO immediately — cheaper to fix now.

### 5. Status board

At the start of a session, after finishing a section, and whenever the user asks "đang tới đâu rồi", print the board:

```
PRD — <Project>                          trạng thái
 1. Executive Summary                    ▓▓▓░░ 3/5 mục · 1 RESEARCH
 2. Mục tiêu & Bối cảnh                  ▓▓▓▓▓ done
 3. User Problem & Personas              ▓▓▓▓░ 4/5 · thiếu journey mong muốn
 4. Competitive Analysis                 ░░░░░ chưa bắt đầu  ← đề xuất kế tiếp
 ...
```

Compute fill state by scanning `prd_working.md` for empty placeholders (`_TBD_`) and status tags. Recommend the next section based on the dependency map, but keep it a suggestion.

### 6. Living document behavior

The PRD is not write-once (Atlassian's core principle — see `references/prd-best-practices.md`). When the PO changes something already `[CONFIRMED]`:
- Make the edit, then add a row to the **Version History** table in the working file (date, what changed, why).
- If the change ripples (e.g., dropping a persona), run the consistency pass on affected sections and list the ripple effects before applying them.

### 7. Export to .docx

When the PO asks to export (or the PRD is complete):

1. Sweep `prd_working.md`: list any remaining `_TBD_` / `[RESEARCH]` / `[DRAFT]` items. Ask whether to resolve, keep as visibly-marked open questions, or drop. Never silently export placeholders as if final.
1b. **Chạy Cổng Chất lượng PRD** (Full mode bắt buộc, Lite khuyến nghị): chấm Pass/Fail 5 cổng — Core-8 Completeness, Evidence Quality, Mobile-Specific Coverage, Scope Clarity, Metrics Readiness (định nghĩa trong template-structure.md, block Full mode) — VÀ quét danh sách "Anti-patterns từ PRD thực tế" ở cuối template-structure.md (section rỗng, bảng-dạng-ảnh, flow không có bước text, số không nguồn, persona dưới chuẩn, thiếu luồng permission/AI-thất-bại). Cổng Fail → ghi vào mục Vướng mắc + Điều chỉnh Bắt buộc thay vì im lặng; PO vẫn có quyền export với vướng mắc được ghi rõ. Kết thúc bằng Tóm tắt Bàn giao (chế độ, số đối thủ, số nguồn, số giả định mở, hành động tiếp theo).
2. Strip status tags, set Version/Date/Status in the meta block.
3. Run the export script:
   ```bash
   node <skill-dir>/scripts/export_prd.js /home/claude/prd-<slug>/prd_working.md /home/claude/prd-<slug>/PRD_<Project>.docx
   ```
4. **Verify the render** (per docx skill): convert to PDF, rasterize, and actually look at a few pages:
   ```bash
   python3 /mnt/skills/public/docx/scripts/office/soffice.py --headless --convert-to pdf PRD_<Project>.docx
   pdftoppm -jpeg -r 80 PRD_<Project>.pdf page && ls page-*.jpg
   ```
   Check: headings hierarchy, tables not overflowing, Vietnamese diacritics intact, bullets rendered (not literal `-`).
5. Copy to `/mnt/user-data/outputs/` and present with `present_files`.

## Working file conventions (required for export)

The export script understands exactly this dialect — deviating breaks the docx:

- `# Title` → document title (one only, first line)
- Meta block right after title: lines of `**Key**: value`
- `## N. Section Name` → Heading 1 (numbered template sections)
- `### Subsection` → Heading 2 (e.g., `### Phát biểu Vấn đề`)
- `#### Sub-sub` → Heading 3 (e.g., per-persona blocks)
- Bullets `- text`, nested with 2-space indent; `**bold**` inline supported everywhere
- Tables as GitHub pipe tables with a header row — used for stakeholders, version history, links, competitor matrix, feature table, KPI table
- `> text` → callout paragraph (methodology notes, warnings)
- `---` → ignored (visual separator for humans only)
- Placeholders: `_TBD_` for empty values; status tags `[CONFIRMED]`/`[DRAFT]`/`[RESEARCH]` appended to lines

The skeleton in `assets/prd_skeleton.md` is the canonical structure — 10 sections matching the team template exactly (Stakeholders, Version History, Links, Executive Summary, Mục tiêu & Bối cảnh, User Problem & Personas, Competitive Analysis, Vision & KPI, Scope, Features, User Flows, Mobile Constraints, Monetization, Meeting Notes). Do not invent, rename, or reorder top-level sections; add subsections freely when the product needs them.

## Things that make this skill worth having

- **Never let the PO fill a section with generic filler.** "Tăng retention" is not a success criterion; "D7 retention ≥ 12% trước khi mở rộng tính năng" is. The quality bars in `references/template-structure.md` define the line — hold it.
- **Estimates are labeled, always.** The template's credibility with engineers and leadership depends on it.
- **One section at a time, committed in writing.** Long brainstorms that live only in chat get lost. Write after every convergence.
- **The PRD is for alignment, not specification.** When the PO starts writing implementation details (API shapes, DB schemas), redirect: link it in Important Links, keep the PRD at the what/why level. See `references/prd-best-practices.md` for the full philosophy.
