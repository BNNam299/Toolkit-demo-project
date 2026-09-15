---
name: ui-redesign-contract
description: Self-contained output contract + quality gate for the UI redesign flow. Enforces the exact redesign/ directory, file naming, per-file schemas, machine+human readability, and gate-redesign (incl. distinctiveness bar). Independent of project-docs quality gates.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# UI Redesign — Output Contract & Gate (self-contained)

Governs the OUTPUT of the `ui-redesign` engine. This contract **validates** structure/completeness/readability
and enforces the **distinctiveness bar** — it does not create the design (that is `ui-redesign` + `ui-redesign-craft`).
It is **independent of project-docs** (does not use `project-docs-quality-gates`), mirroring how
`uiux-analysis-contract` carries its own gate.

## 1. Exact output directory
```
{{IDE_CONFIG_DIR}}specs/[project-name]/redesign/
```
Never use variations (`redesign-ui/`, `design/`, …).

## 2. Exact file structure
```
redesign/
├── README.md              # index (human+AI): style summary, read-order, single-source-of-truth table
├── redesign-state.json    # §5 state schema
├── style-reference.md     # source input (image/desc/pen) + extracted Style DNA
├── current-ui-audit.md    # audit of the BUILT app + screenshot-before refs + gap vs Style DNA
├── design-tokens.md       # new tokens + table mapping token → shared/Styles/*.swift
├── components.md          # new components + old→new table + reuse tier
├── flows.md               # mermaid navigation flows (redesigned)
├── screens/
│   └── screen-[view-name].md   # ONE per screen (source = Features/*/Views/*.swift)
├── redesign-summary.md    # change list, migration order, risk, before/after result
└── manifest.json          # §6 machine-readable
```

## 3. File naming
- Screen files: `screen-[view-name].md`, where `view-name` = the SwiftUI View file name, lowercase-hyphen
  (e.g. `DiaryView.swift` → `screen-diary-view.md`). Never `WF001.md` or ad-hoc names.
- Every markdown file starts with front-matter `{ doc_id, version, date, style_ref }` so AI can parse it.

## 4. Required content per file

### style-reference.md
Source used (image paths / pen file + variables / description) and the extracted **Style DNA**:
`mood, palette, type-vibe, shape-language, motion, density, references`.

### current-ui-audit.md
Screen inventory (from `Features/*/Views/*`), screenshot-before refs (or "screenshot skipped" + reason),
and a per-screen gap-vs-DNA note (where the current UI is generic/iOS-stock).

### design-tokens.md
The new token set, and a mandatory mapping table:

| Token | Value | Swift symbol | Target file |
|-------|-------|-------------|-------------|
| color.accent | `<hex/spec>` | `accent` | `shared/Styles/AppColors.swift` |

(color / typography / spacing / radius / shadow / motion / elevation). If source = `.pen`, each Pencil variable maps to a token here.

### components.md
The new-style library with an **old→new** table:

| New component | Replaces | Reuse tier | File | Reason |
|---------------|----------|-----------|------|--------|
| `<Name>` | `<Old\|null>` | as-is/parameterize/compose/extend/new | `shared/Components/<Type>/<Name>.swift` | … |

### screens/screen-[view-name].md (Screen Schema)
```
## Metadata (doc_id, view, view_file, style_ref)
## Before (current description / screenshot ref)
## After — New Layout (zones, hero, hierarchy in the new style)
## Components Used (link components.md; mark reuse/new)
## States (Loading / Empty / Error+recovery / Success — KEEP THE FLOOR)
## Signature Moments (1–3, each: name · placement · tokens/motion · Style-DNA trace · leaves-iOS-stock · a11y)
## Screen Flow (mermaid)
## Accessibility (VoiceOver / Dynamic Type / contrast / ≥44pt / dark mode)
```

### flows.md
Mermaid diagrams of the (redesigned) navigation. README, redesign-summary: see §2.

## 5. State schema (`redesign-state.json`)
```json
{
  "project": "<name>",
  "state": "intake|audit|proposed|approved|applying|done",
  "style_ref": {
    "source": "image|desc|pen",
    "images": ["<path>"],
    "description": "<text>",
    "pen_file": "design-token/template-neo.pen",
    "pen_variables": { "<var>": "<value>" },
    "dna_summary": "<text>"
  },
  "screens_source": "built-app-views",
  "screenshots": { "before": ["<path>"], "after": ["<path>"] },
  "gate_redesign": "pending|pass|fail",
  "applied_screens": ["<ViewName>"],
  "updated": "<timestamp passed in>"
}
```

## 6. Manifest schema (`manifest.json`)
```json
{
  "tokens":     [ { "name": "color.accent", "value": "<hex/spec>", "swift_target": "shared/Styles/AppColors.swift", "symbol": "accent" } ],
  "components": [ { "new": "<Name>", "replaces": "<Old|null>", "reuse_tier": "as-is|parameterize|compose|extend|new", "file": "shared/Components/<Type>/<Name>.swift" } ],
  "screens":    [ { "view": "DiaryView", "view_file": "Features/Diary/Views/DiaryView.swift", "proposal": "redesign/screens/screen-diary-view.md", "flow_changed": true } ]
}
```

## 7. Quality Gate — `gate-redesign` (self-contained; PASS/FAIL)

Run after the proposal is written (P5). Emit a decision block. FAIL blocks approval.

**Completeness**
- All mandatory files present (§2); `manifest.json` parses.
- **Every built screen** (each View in `Features/*/Views/*`) has a matching `screens/screen-*.md` — no dropped screen.
- `design-tokens.md` has the token→`shared/Styles/*.swift` mapping table (no token stranded in docs).
- `components.md` has the old→new table with a reuse tier + reason each.
- `flows.md` has mermaid, and each screen file has a Screen Flow.

**Readability (human + AI)**
- Every file has front-matter; no placeholders (`[...]`, `TBD`, `TODO`); README has read-order + single-source-of-truth table.

**UX floor (kept)**
- Every screen file enumerates all 4 states + a11y + contrast ≥4.5:1 + ≥44pt + dark mode.

**Distinctiveness bar (creativity check — the reason a validator alone isn't enough)**
- Each screen has ≥1 signature moment, each traced to the Style DNA.
- Tokens/screens **visibly leave iOS-stock**: no leftover `#007AFF` / system-default font/spacing where a brand token belongs.
- README states the app's overall "signature system".

**Decision block**
```
## UI Redesign Gate (gate-redesign)
- Completeness: Pass/Fail (missing: [...])
- Readability: Pass/Fail
- UX Floor: Pass/Fail
- Distinctiveness: Pass/Fail (screens without a signature moment: [...])
## Required Fixes: 1. ...
```
**Pass** = all categories Pass, no Required Fixes. **Fail** = loop back to fix.

## 8. Non-Negotiable Rules
- Write only under `{{IDE_CONFIG_DIR}}specs/[project-name]/redesign/` (proposal stage).
- Do NOT reference or modify `project-docs-quality-gates`; this gate is self-contained.
- Never mark a proposal ready while any category fails, especially the **Distinctiveness bar** — a well-formed but generic package is a FAIL.
