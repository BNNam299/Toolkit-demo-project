---
name: project-docs-quality-gates
description: Unified quality gates for all project documentation types (PRD, Overview, Use Cases, Functional Requirements, Wireframes, UX Flows, Roadmap). Use when creating or reviewing any project spec to enforce completeness, traceability, and actionability before declaring the document ready. Section requirements are read from each template's QUALITY-GATE-MANIFEST, never hard-coded here.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Required Skills & Files

Before executing this skill, you MUST read these files:

- `{{IDE_CONFIG_DIR}}skills/project-docs-lifecycle/SKILL.md` — Lifecycle (directory, file safety, confirmation, gate invocation)
- `{{IDE_CONFIG_DIR}}skills/project-docs-contract/SKILL.md` — Workflow contract (scaling, sub-spec rules, document sequence)
- The `QUALITY-GATE-MANIFEST` block of the template being checked (see mapping table below) — this is the SOURCE OF TRUTH for required sections.

## Non-Negotiable Rules

- Every gate MUST be a pass/fail check, not a style preference.
- Every gate failure MUST list concrete fix requests. Do NOT mark a document ready until all categories pass.
- **Do NOT hard-code the list of required sections in this skill.** For the 7 project-doc gates, the required sections and doc-specific quality checks are READ AT CHECK TIME from the template's `QUALITY-GATE-MANIFEST` block. This skill only defines the *procedure*, not the section lists.
- Gate IDs are stable identifiers. They map 1:1 to per-doc skills and to a template:
  - PRD → `gate-prd` → `doc-templates/PRD.md`
  - Project Overview → `gate-overview` → `doc-templates/Project_Overview.md`
  - Use Cases → `gate-uc` → `doc-templates/Use_Cases.md`
  - Functional Requirements → `gate-fr` → `doc-templates/Functional_Requirements.md`
  - Wireframes → `gate-wireframes` → `doc-templates/Wireframes.md`
  - UX Flows → `gate-flows` → `doc-templates/UX_Flows.md`
  - Implementation Roadmap → `gate-roadmap` → `doc-templates/Project_Implementation_Roadmap.md`
  - Design System → `gate-design-system` (design-ui, no template — see Design-UI Gates)
  - Screen Analysis → `gate-screen-analysis`
  - Micro-interactions → `gate-micro-interactions`
  - Accessibility Report → `gate-accessibility`
  - Consistency Report → `gate-consistency` (optional)
  - Analysis Summary → `gate-analysis-summary`
- Per-doc skills MUST invoke the corresponding gate ID after writing the document.
- File safety: every output path is under `{{IDE_CONFIG_DIR}}specs/[project-name]/`.

# Project Documentation Quality Gates

## When to Use

- After any per-doc skill writes a document (Phase 3 of `project-docs-lifecycle`)
- Before declaring any document ready
- During `project-docs-review` to audit existing documents
- When the user explicitly requests a quality check

## Objective

Enforce minimum quality for each project document. Each gate is a pass/fail check. A failing gate lists concrete fix requests and blocks progression. For the 7 project-doc types, "required sections" is **recalled from the template's manifest**, so the template is the single source of truth and never drifts from the gate.

---

## Template-Driven Gate Procedure (7 project-doc gates)

`gate-prd`, `gate-overview`, `gate-uc`, `gate-fr`, `gate-wireframes`, `gate-flows`, and
`gate-roadmap` ALL run the same procedure below. The only thing that differs per gate is
which template it reads.

### Step 1 — Resolve the template
From the gate ID, pick the template file from the mapping table in Non-Negotiable Rules
(e.g. `gate-prd` → `{{IDE_CONFIG_DIR}}doc-templates/PRD.md`).

### Step 2 — Recall required sections from the manifest
Read the template file and extract the YAML between the markers:

```
<!-- QUALITY-GATE-MANIFEST:START
... yaml ...
QUALITY-GATE-MANIFEST:END -->
```

From it, load:
- `required_major` — mục lớn (top-level sections). ALL must be present.
- `required_minor` — for each major, the mục con (sub-sections). ALL must be present.
- `quality_checks` — doc-specific content rules (evidence, coverage, measurability, …).

Every section listed in the manifest is **mandatory** — the manifest has no optional tier
(the template is a contract; nothing in it is auxiliary). The only headings NOT listed are
placeholder/example patterns (`[...]`, `XXX`, `.N`, "Example …", archetype template samples),
which are fill-in patterns, not fixed sections.

If the template has no manifest block, STOP and report a Blocker
("template missing QUALITY-GATE-MANIFEST") — do NOT fall back to guessing sections.

### Step 3 — Read the produced document
Read `{{IDE_CONFIG_DIR}}specs/[project-name]/<Doc>.md` and collect all its headings.

### Step 4 — Structure check (major + minor, đủ mục lớn và nhỏ)
- **Major:** every `required_major` name must appear as a heading. Match by name,
  **ignoring leading numbering** (`1.`, `2 bis.`, `3.5`) and any trailing placeholder/param
  in the produced heading (e.g. manifest `"Luồng Chính"` matches `## Luồng Chính: Đặt hàng`).
  Each missing major → Fail, list it by name.
- **Minor:** for every major, every name in its `required_minor` list must appear as a
  sub-heading under that major. Each missing minor → Fail, list as `major → minor`.
- There are no optional sections: every section in the manifest is mandatory.

### Step 5 — Content check (each required section substantively filled)
Every required section must be **substantively filled**, not just present as a heading. Fail if
a required section is empty, is only a heading, or still contains unresolved placeholders:
`[...]` bracket tokens, `XXX`, `.N`, or `TBD`. (Ignore GitHub-style checkbox `- [ ]` and
`${...}` design tokens — those are legitimate.)

### Step 6 — Quality checks (per-file hints from manifest)
`quality_checks` in the manifest are **hints that tell you what to verify inside each file** —
including deeper (level-4) content that the manifest does NOT enumerate as fixed sections
(e.g. per-screen parts in Wireframes, NFR categories in FR). Do NOT treat them as a rigid
section list; instead, for each hint, inspect the produced document and decide Pass/Fail, then
list any that fail. Examples: PRD evidence ≥28 sources; UC screen-count minimums; Wireframes
each screen has its archetype parts.

### Step 7 — Universal rules (cross-doc, defined here)
Always apply, regardless of manifest:
1. **Traceability chain** — PRD → Overview → UC → FR → Wireframes → UX Flows → Roadmap link forward and backward.
2. **Stable IDs** — consistent identifiers (UC-xxx, FR-xxx, WF-xxx, AC-xxx.y) chained across docs.
3. **Measurable language** — reject "fast", "user-friendly", "secure" on critical items; require quantified alternatives.
4. **File safety** — the file is under `{{IDE_CONFIG_DIR}}specs/[project-name]/`.
5. **Valid cross-references (consistency lint)** — every ID referenced (`UC-`, `FR-`, `WF-`,
   `TF-`, `SF-`, `AC-`) must resolve to an existing item of the **correct type**. A dangling
   ref, or a wrong-type ref (e.g. an Exit Point citing `WF-017` when WF-017 is a different
   screen), is a Fail — it is a broken edge in the navigation/traceability graph for the agent.
6. **No duplicate section numbers** — each section number (e.g. `§3.5`) appears exactly once;
   duplicates (two `§3.5`) = Fail.
7. **Snapshot consistency** — all 7 project docs share the same Version and Date so the agent
   knows they are one coherent snapshot; a mismatched Version/Date = Fail.

### Step 8 — Emit the gate decision block

```markdown
## <DocType> Quality Gate (<gate-id>)
- Structure — Major sections: Pass/Fail (thiếu: [list or None])
- Structure — Minor sections: Pass/Fail (thiếu: [major → minor list or None])
- No Placeholders / Non-empty: Pass/Fail
- Quality Checks: Pass/Fail (mục fail: [list or None])
- Traceability & IDs: Pass/Fail
- Consistency lint (refs valid / no dup numbering / snapshot): Pass/Fail (issues: [list or None])
## Blockers: [list or None]
## Required Fixes: 1. ...
```

**Pass**: all categories Pass, Blockers None, no Required Fixes. Document is ready.
**Fail**: any category Fail, or any Blocker, or any Required Fix. Document is NOT ready — loop back to fix.

### Output paths (per gate)
- `gate-prd` → `{{IDE_CONFIG_DIR}}specs/[project-name]/PRD.md`
- `gate-overview` → `{{IDE_CONFIG_DIR}}specs/[project-name]/Project_Overview.md`
- `gate-uc` → `{{IDE_CONFIG_DIR}}specs/[project-name]/Use_Cases.md`
- `gate-fr` → `{{IDE_CONFIG_DIR}}specs/[project-name]/Functional_Requirements.md`
- `gate-wireframes` → `{{IDE_CONFIG_DIR}}specs/[project-name]/Wireframes.md`
- `gate-flows` → `{{IDE_CONFIG_DIR}}specs/[project-name]/UX_Flows.md`
- `gate-roadmap` → `{{IDE_CONFIG_DIR}}specs/[project-name]/Project_Implementation_Roadmap.md`

### PRD delivery footer (gate-prd only)
The PRD already has a required `## Tóm tắt Bàn giao` section (in `required_major`). On a PRD
Pass, ensure that section is filled — do NOT add a separate English "Delivery Summary" block:
- File đã tạo/cập nhật: `{{IDE_CONFIG_DIR}}specs/[project-name]/PRD.md`
- Số đối thủ đã phân tích: N | Số nguồn đã rà soát: N | Số giả định đang mở: N
- Hành động tiếp theo: project-docs-overview

---

## Design-UI Gates (no template — criteria defined here)

The design-ui documents are produced by `uiux-analysis-workflow` and have **no
doc-template**, so their required content is defined inline below (not manifest-driven).
Their structure follows `uiux-analysis-contract`.

#### gate-design-system — Design System
**Output:** `{{IDE_CONFIG_DIR}}specs/[project-name]/design-ui/design-system.md`
Core Content: Color System (Primary/Semantic/Neutral with hex), Typography (8-style scale table), Spacing (8pt grid: xs=4, sm=8, md=16, lg=24, xl=32, xxl=48), Corner Radius (sm=4, md=8, lg=12, xl=16, full=9999), Shadow (sm/md/lg/xl), iOS-Specific (safe areas, nav bar 44/96pt, tab bar 49/83pt), Animation Specs, Interaction Patterns (gestures, haptics).
```markdown
## Design System Quality Gate
- Color System: Pass/Fail (all types with hex)
- Typography Scale: Pass/Fail (8 styles)
- Spacing System: Pass/Fail (8pt grid tokens)
- iOS Specifics: Pass/Fail (safe areas, nav, tab bar)
- Interaction Patterns: Pass/Fail (gestures + haptics)
## Required Fixes: 1. ...
```

#### gate-screen-analysis — Screen Analysis
**Output:** `{{IDE_CONFIG_DIR}}specs/[project-name]/design-ui/screens/screen-wf###-[name].md`
Core Content per screen: Metadata (screen_id, name, priority, related UC/FR), Purpose, User Stories, Information Architecture, User Actions, Component Specifications, Interaction Details, Error States, Validation Rules, Accessibility (WCAG 2.1), Usability Checklist, Recommendations, Cross-Screen Consistency.
```markdown
## Screen Analysis Quality Gate
- Metadata: Pass/Fail
- Purpose: Pass/Fail
- Component Specs: Pass/Fail
- Interaction Details: Pass/Fail
- Accessibility: Pass/Fail (WCAG 2.1)
- No Placeholders: Pass/Fail
## Required Fixes: 1. ...
```

#### gate-micro-interactions — Micro-interactions
**Output:** `{{IDE_CONFIG_DIR}}specs/[project-name]/design-ui/interactions/micro-interactions.md`
Core Content: Interaction Categories table (Button, Input, List, Navigation, Feedback), Animation Specifications (timing/easing), Implementation Guidelines (SwiftUI + UIKit).
```markdown
## Micro-interactions Quality Gate
- Categories: Pass/Fail (5 categories)
- Animation Specs: Pass/Fail (timing + easing)
- Implementation: Pass/Fail (SwiftUI + UIKit)
## Required Fixes: 1. ...
```

#### gate-accessibility — Accessibility Report
**Output:** `{{IDE_CONFIG_DIR}}specs/[project-name]/design-ui/accessibility/accessibility-report.md`
Core Content: WCAG Summary table (Perceivable/Operable/Understandable/Robust counts), Failed Items list (criterion + fix), Screen-by-Screen table, Recommendations by priority.
```markdown
## Accessibility Report Quality Gate
- WCAG Summary: Pass/Fail (4 categories)
- Failed Items: Pass/Fail (item + fix)
- Screen Breakdown: Pass/Fail
- Recommendations: Pass/Fail (prioritized)
## Required Fixes: 1. ...
```

#### gate-consistency — Consistency Report (optional)
**Output:** `{{IDE_CONFIG_DIR}}specs/[project-name]/design-ui/consistency/consistency-report.md`
Core Content: Consistency Scores table (6 categories), Category Issues tables, Action Items (P0/P1/P2).
```markdown
## Consistency Report Quality Gate
- Scores Table: Pass/Fail (6 categories)
- Issues: Pass/Fail (per category)
- Action Items: Pass/Fail (P0/P1/P2)
## Required Fixes: 1. ...
```

#### gate-analysis-summary — Analysis Summary
**Output:** `{{IDE_CONFIG_DIR}}specs/[project-name]/design-ui/analysis-summary.md`
Core Content: Executive Summary (metrics table), Heuristic Evaluation table (Nielsen's 10), Critical Issues, Top Recommendations (Must/Should/Nice), Design System Recommendations, Next Steps, Files Produced table.
```markdown
## Analysis Summary Quality Gate
- Metrics Table: Pass/Fail
- Heuristic Evaluation: Pass/Fail (10 heuristics)
- Critical Issues: Pass/Fail
- Files Produced: Pass/Fail
## Required Fixes: 1. ...
```

---

## Universal Fail Conditions

Any gate fails if:
- Unresolved placeholders remain in required sections
- A `required_major` or `required_minor` section (project-doc gates) or a listed Core Content item (design-ui gates) is missing
- Traceability links are broken or missing
- Vague wording replaces measurable criteria on critical items
- A `quality_checks` item fails (project-doc gates) — e.g. PRD claims lack evidence sources
- A cross-reference ID is dangling or wrong-type, a section number is duplicated, or the doc's Version/Date is out of snapshot with the set (Step 7 consistency lint)
- File is written outside `{{IDE_CONFIG_DIR}}specs/[project-name]/`

On failure: document concrete fix requests. Do not mark any document ready until all categories pass.

---

## Quality Gates (self-referential)

This skill has no upstream gate. It is invoked by per-doc skills and by `project-docs-review`. Its own correctness is verified by:

- Stable gate IDs (no renaming without coordinated update across all per-doc skills and `commands/ios-project-docs.md`)
- The gate NEVER re-lists required sections; it reads each template's `QUALITY-GATE-MANIFEST`
- Output paths under `{{IDE_CONFIG_DIR}}specs/[project-name]/`
- Each gate's Required Fixes section is concrete (specific section + change), not vague

---

## Error Handling

- **Wrong gate ID for doc type**: stop. Cross-check the ID-to-template mapping in Non-Negotiable Rules.
- **Template missing QUALITY-GATE-MANIFEST**: stop, report a Blocker. Do NOT guess sections.
- **Document missing required sections**: list each missing major/minor in Required Fixes. Do NOT mark ready.
- **Inconclusive evidence (PRD specifically)**: mark claim as "Assumption - needs verification" rather than inventing sources.
- **Cross-doc inconsistency** (e.g. an FR that appears in no UC): surface the orphan in Required Fixes.

---

## Output Contract

Per gate invocation, the output is a **gate decision block** (see Step 8 for project-doc gates, or the per-gate block for design-ui gates).

**Pass**: all categories Pass, Blockers None or empty, no Required Fixes. Document is ready.
**Fail**: at least one category Fail, or any Blockers, or any Required Fixes. Document is NOT ready.
