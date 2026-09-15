---
name: project-docs-contract
description:
  Full workflow contract for project documentation. Enforces document sequence (PRD through UX Flows plus Roadmap), ID schemes, cross-reference rules, boundary ownership, scaling guidance, quality gate cascading, and resume protocol. Use this skill when orchestrating or validating the project docs pipeline.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Project Docs Flow Contract

## Purpose

Govern the full project documentation pipeline. Every doc has a defined place, ownership boundary, and traceability chain. No duplication, no gaps, no orphan requirements.

---

## Document Sequence

Documents must be produced in this order. Each step depends on its predecessor.

```
Step 1:  PRD.md                    (market, problem, competitors, goals)
Step 2:  Project_Overview.md       (architecture, tech stack, roadmap summary)
Step 3:  Use_Cases.md              (actor goals, primary/alternate flows)
Step 4:  Functional_Requirements.md (feature specs, acceptance criteria)
Step 5:  Wireframes.md             (screen layouts, component placement)
Step 6:  UX_Flows.md               (navigation paths, state transitions)
Step 7:  Roadmap.md                (phased delivery plan, milestone mapping)
```

Rules:

- PRD-first always. Skip PRD only with explicit user confirmation.
- Never skip a downstream step when the full workflow is requested.
- Roadmap depends on all prior docs being complete and reviewed.

---

## ID Schemes

Every artifact gets a stable, typed ID. Format: `TYPE-NNN` with optional sub-IDs using `.Y` notation.

| Prefix | Artifact | Example |
|--------|----------|---------|
| UC- | Use Case | UC-003 |
| FR- | Functional Requirement | FR-012 |
| WF- | Wireframe Screen | WF-007 |
| NFR- | Non-Functional Requirement | NFR-002 |
| AC- | Acceptance Criterion | AC-003.1 |
| AF- | Alternative Flow | AF-001.1 |
| TF- | Task Flow | TF-003 |
| SF- | Sub-Flow | SF-002.1 |
| BR- | Business Rule | BR-004.1 |
| ERR- | Error Scenario | ERR-005.2 |
| VR- | Validation Rule | VR-003.1 |

Rules:

- IDs are sequential within each prefix (UC-001, UC-002, not UC-100).
- Once assigned, IDs never change. New items get new IDs, they do not renumber existing ones.
- Sub-IDs (`.Y`) extend a parent. `AC-003.1` is the first criterion of `UC-003`. (AC extends UC, not FR — UC skill assigns AC IDs at UC creation time; FR carries them forward verbatim.)
- Cross-references always use the full ID, never plain text descriptions.

---

## Cross-Reference Rules

Documents must link forward and backward to maintain traceability.

| Source | Must Reference | Example |
|--------|---------------|---------|
| UC- entries | WF- screens | `UC-003` involves `WF-005, WF-008` |
| UC- entries | Primary WF- screen | `UC-003` primary screen `WF-005` |
| Screen-Context | UC- references, user intent, primary action | Home screen serves `UC-001, UC-002` |
| Task Flows | UC- + WF- per step | Step 1: `WF-005`, `UC-003` |
| FR- entries | UC- parent | `FR-012` → `UC-003` |
| WF- screens | UC- requirements | `WF-007` covers `UC-001, UC-002` |
| WF- screens | FR- requirements | `WF-007` covers `FR-012, FR-013` |
| UX_Flows | WF- screens | Flow: `WF-003 → WF-007` |
| AC- criteria | UC- parent | `AC-003.1` validates `UC-003` |
| Roadmap phases | FR- batch groups | Phase 1: `FR-001`-`FR-008` |
| NFR- entries | Affected FR- list | `NFR-002` constrains `FR-012, FR-015` |
| BR- entries | Applicable UC- list | `BR-004.1` governs `UC-003` |
| ERR- entries | Triggering FR-/UC- | `ERR-005.2` from `UC-003` alt |

Rules:

- Every UC must trace to at least one WF screen (§3 UC → Screen Mapping).
- Every WF screen must trace to at least one UC (§3 Screen → UC Coverage).
- Every FR must trace to at least one UC.
- Every WF must trace to at least one FR or UC.
- Every UX Flow must reference the WF screens it traverses.
- Every Task Flow step must reference both a WF-XXX and a UC-XXX.
- Every Screen-Context entry must have a user intent and primary action.
- Orphan IDs (no incoming or outgoing references) fail the quality gate.

---

## Boundary Contract

Each document owns a domain. Downstream docs refine, never duplicate.

| Document | Owns | Does Not Own |
|----------|------|-------------|
| PRD | Market analysis, competitor depth, business goals, success metrics | Architecture decisions, implementation details |
| Overview | Architecture, tech stack, roadmap summary, team structure | Market analysis (reference PRD), detailed UC flows |
| Use Cases | Actor interactions, primary/alt flows, pre/post conditions, **UC → Screen mapping, screen-context use cases (user intent, primary/secondary actions), task flows across screens** | Feature specifications (that is FR territory), screen layouts, component details |
| FR | Feature specs, acceptance criteria, business rules, constraints | Screen layouts, navigation flows |
| Wireframes | Screen layouts, component placement, visual hierarchy | Use case flows (reference UC), requirement text |
| UX Flows | Navigation paths, state transitions, error handling paths | Screen content details (reference WF) |
| Roadmap | Phase grouping, milestone deadlines, priority ordering | New requirements, new analysis |

When a document needs content from another domain, reference the owning document's ID rather than restating the content.

---

## Scaling Guidance

Scale document depth to project size. Over-documenting small projects wastes time. Under-documenting large ones creates risk.

### Small (fewer than 5 features)

- Use Cases: 10-18 | FRs: 12-25 | Screens: ≥12 (incl. modals/overlays) | Per-Screen Nav Flows: 3-5 | Phases: 1-2

### Medium (5-10 features)

- Use Cases: 20-35 | FRs: 50-100 | Screens: ≥25 (incl. modals/overlays) | Per-Screen Nav Flows: 6-10 | Phases: 2-4

### Large (10+ features)

- Use Cases: 35+ | FRs: 100+ | Screens: ≥40 (incl. modals/overlays) | Per-Screen Nav Flows: 10+ | Phases: 4+

Adjust by domain complexity, not just feature count. A 3-feature fintech app needs more rigor than a 10-feature TODO list.

> **Flows metric scope:** The "Per-Screen Nav Flows" count above is the **target** for detailed screen-to-screen navigation flows (per-template §3). The `project-docs-flows` skill additionally defines a "High-Level Journeys" count (2-3 / 3-5 / 5+ for Small/Medium/Large) — these are separate metrics, not duplicates.

> **Scope note:** These counts are **targets** for production-quality specs and are the default to build to. Each value is typically 2-3× the minimum viable floor defined in the corresponding per-doc skill (e.g., FR count floors in `project-docs-fr`). A tight schedule is NOT a license to silently drop to the floor: any reduction below these targets must be recorded in the roadmap **Scope Decision Record** with an explicit tier + reason per cut item, so nothing (edge cases, secondary affordances, error handling) disappears without a visible, reviewable decision.

---

## Quality Gate Cascading

Each document must pass its quality gate before the next document starts. Gates cascade: a failure at step N blocks all steps after N.

Gate format for each document:

```
GATE: [DocumentName]
STATUS: Pass | Fail
CHECKS:
  - [x] IDs present and sequential
  - [x] Cross-references valid
  - [x] No orphan IDs
  - [x] Boundary rules respected
  - [x] No unresolved placeholders
  - [ ] [document-specific checks]

REQUIRED_FIXES (if Fail):
  - Fix 1: description
```

Rules:

- A failed gate means revisions, not progression.
- User must explicitly approve each gate before proceeding.
- If a downstream doc reveals an upstream gap, fix the upstream doc first, then regenerate downstream.
- Gate checks are defined in `project-docs-quality-gates` skill. Do not duplicate them here.

---

## Resume Protocol

When resuming a partially completed pipeline:

1. Scan `{{IDE_CONFIG_DIR}}specs/[project-name]/` for existing files.
2. For each existing file, re-validate against its quality gate checks.
3. If a file passes validation, skip its creation step.
4. If a file fails validation, flag it for revision and re-enter that step.
5. Never overwrite a passing file without user confirmation.
6. Continue from the first incomplete step.

---

## Template References

Each document uses a template from the `doc-templates/` directory.

```
{{IDE_CONFIG_DIR}}doc-templates/
  PRD.md
  Project_Overview.md
  Use_Cases.md
  Functional_Requirements.md
  Wireframes.md
  UX_Flows.md
  Project_Implementation_Roadmap.md
```

Templates define section structure and ID placeholders. Per-doc creation instructions live in their respective skills, not here.

---

## Sub-Spec Splitting

When an FR section grows beyond 5 requirements, split it.

Guidelines:

- Group related FRs into sub-specs by functional area (auth, payments, onboarding).
- Each sub-spec gets its own file: `FR_[area].md` (e.g., `FR_auth.md`).
- Main `Functional_Requirements.md` becomes an index linking to sub-specs.
- Sub-spec IDs remain globally unique: `FR-012` stays `FR-012` regardless of file.
- Roadmap phases reference sub-spec files, not individual FRs.

---

## Non-Negotiable Rules

1. **File safety**: Write only under `{{IDE_CONFIG_DIR}}specs/[project-name]/`. Never outside.
2. **ID stability**: Once assigned, IDs stay. No renumbering, no recycling.
3. **No placeholders**: `TBD`, `TODO`, and blank sections fail the quality gate.
4. **Traceability**: Every FR→UC, every WF→FR, every UX Flow→WF. No orphans.
5. **Boundary respect**: Own your domain. Reference across docs, do not duplicate.
6. **Approval gates**: User must approve each gate. No auto-advancing.
7. **Resume awareness**: Check existing files first. Never overwrite without confirmation.
8. **Completion & Handoff** (the single definition of Handoff — command and workflow reference this, never restate it): after the last document is approved, the pipeline MUST finish by:
   a. **Generate `{{IDE_CONFIG_DIR}}specs/[project-name]/_INDEX.md`** from `{{IDE_CONFIG_DIR}}doc-templates/_INDEX.md` — files + read order, ID conventions, and the single-source-of-truth table; set its snapshot Version/Date to match all docs.
   b. **Completion summary**: list every file, ID count, and quality-gate result.
   c. **Offer next step**: `/ios-spec <feature-name>`.
