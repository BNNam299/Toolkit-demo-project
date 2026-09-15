---
name: spec-creation-contract
description:
  Spec workflow contract for feature-level delivery. Use when creating requirements, design, tasks, refinement, and execution with stage gates and traceability.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Spec Flow Contract

## Purpose
Use this skill as the workflow contract for spec skills:
- `spec-workflow` (orchestration)
- `spec-requirements` (requirements creation)
- `spec-design` (design creation)
- `spec-tasks` (tasks creation)
- `spec-refine` (change routing and patching)
- `spec-quality-gates` (validation)

This skill defines stage transitions, approval gates, traceability expectations, file contracts, and template references.

---

## Stage Model

```text
draft_requirements
  → approved_requirements
  → draft_design
  → approved_design
  → draft_tasks
  → approved_tasks
  → executing
  → blocked | done
```

Rules:
- Never skip stages
- Never execute before `approved_tasks`
- Major change during execution returns stage to `draft`
- Stage transitions require explicit user approval

---

## Source of Truth Files

```text
{{IDE_CONFIG_DIR}}specs/[feature-name]/
  requirements.md  (MUST contain FR/UC source references + Evidence summary)
  design.md
  tasks.md
  spec-state.json
```

Required contracts:
- `requirements.md`: user stories + EARS ACs + **Source: FR-XXX, UC-XXX** for each requirement + **Evidence References** section
- `design.md`: architecture + interfaces + test strategy + properties + **AC Coverage** (every AC must be covered)
- `tasks.md`: registry + checklist + dependency matrix + traceability matrix
- `spec-state.json`: current stage and mode

---

## Template References

Templates live in `{{IDE_CONFIG_DIR}}doc-templates/`:

| Spec Type | Template | Per-Spec Skill | Quality Gate |
|-----------|----------|---------------|--------------|
| Requirements | `doc-templates/spec-requirements.md` | `spec-requirements` | `spec-quality-gates` gate-requirements |
| Design | `doc-templates/spec-design.md` | `spec-design` | `spec-quality-gates` gate-design |
| Tasks | `doc-templates/spec-tasks.md` | `spec-tasks` | `spec-quality-gates` gate-tasks |

Each per-spec skill reads the template for section layout, then generates content from context.

---

## Spec Chain Order

Specs must be created in order because downstream specs depend on upstream ones:

1. **Requirements** → reads project docs (FR, UC, PRD), creates requirements.md
2. **Design** → reads requirements.md, creates design.md with AC coverage
3. **Tasks** → reads requirements.md + design.md, creates tasks.md with traceability

Never create a downstream spec before its upstream dependency is approved.

---

## Write Incrementally (avoid oversized output)

Spec files can be large — `design.md` (feature breakdown, interfaces, properties) and `tasks.md`
(full registry + matrices) often run several hundred lines. **Never emit the whole spec in one
giant `Write`** — a single oversized output risks hitting the model's **max output tokens** (the
file gets truncated/corrupted) and causes long response times / timeouts. Write in bounded chunks:

1. Create the file with `Write`: front matter + the **first major section** only.
2. Append **each remaining major section** with a separate `Edit` — one section per call.
3. Keep every write/edit to roughly **one major section (≈ ≤ 200–300 lines)**.
4. For large dynamic parts, append incrementally:
   - `design.md`: **one feature `7.X` block at a time**.
   - `tasks.md`: **one phase at a time** (Shared → Feature → Integration), registry/matrix after.
5. Run the quality gate **only after all sections are written**.

Trade-off: more tool calls, but each is size-bounded, so no content is lost to truncation.

---

## Approval and Execution Policy

- Require explicit user approval after each spec file
- Default stop after tasks approval
- Execute only on explicit user intent
- For autopilot execution, stop on first blocker or phase gate failure
- Never auto-start execution from ambiguous user replies

---

## Refinement Routing

When changes are requested to existing specs:

| Impact Level | Route | What Changes |
|-------------|-------|-------------|
| Minor | `spec-refine` patch path | Wordings, AC clarifications, no structure changes |
| Medium | Regenerate design + tasks | Flow adjustments, component updates |
| Major | Regenerate all three | Requirement scope changes, MVP reshuffle |

---

## Traceability Contract

Maintain full chain:

```text
FR/UC → Requirement → Acceptance Criteria → Design → Task → Code/Test
```

**Upstream traceability (REQUIRED):**
- Each requirement MUST have **Source** field linking to FR-XXX and UC-XXX IDs
- Each AC traces back to source FR via requirement's Source field
- Evidence References section MUST cite PRD Evidence Table data

**Design traceability (REQUIRED):**
- Every AC from requirements.md MUST be referenced in design.md (Section 1, 7, or 9)
- Each design feature section MUST have **ACs Implemented** field listing specific ACs
- Each correctness property MUST have **Validates AC** column referencing specific AC
- **Design Approval Gate MUST validate AC coverage before approval**

**Task traceability:**
- Every task MUST reference AC(s) and Design section number(s)
- Task `Refs AC` column references AC-XXX.Y IDs
- Task `Refs Design` column references section numbers (e.g., `7.1`, `7.2`)

---

## Real-World Readiness Checklist (shared depth contract)

This is the single definition of "detailed enough for real use" that the three feature-spec gates
(`gate-requirements`, `gate-design`, `gate-tasks`) reference. A feature is real-world-ready only when,
for each dimension, the spec either covers it or marks it `N/A — <reason>` (never silently blank):

1. **Affordance completeness** — every Component/Interaction of the owned WF-XXX screen(s) has an AC (or is declared out-of-scope with owner). No dropped settings/share/skip/help/export/edit affordance.
2. **States** — Loading, Empty, Error, Success each defined (design §7) with concrete behavior, not just named.
3. **Validation** — each user input has enumerated VR rules (format/range/required) + on-violation behavior.
4. **Error handling** — every failure mode has detection → user-visible behavior → recovery (design §5 table); covers each ERR/alternate-flow.
5. **Offline / staleness** — cached read behavior + staleness marker + queued-write flush, where the app has network state.
6. **Permissions** — camera/photo/notification request + denied path, where used.
7. **Accessibility** — VoiceOver labels, Dynamic Type, contrast ≥4.5:1, ≥44pt targets, dark mode (design §7 line).
8. **Security / privacy** — PII handling, secure storage (Keychain), no secrets in logs, deletion/export, where personal data is handled.
9. **Performance** — measurable NFR budgets (latency/memory) relevant to the feature.
10. **Tests** — every Correctness Property (design §9) has a property-based test task.

"Passes the spec" must mean this checklist is satisfied — not just that the happy path is described.

---

## Non-Negotiable Rules

- Do not proceed to next stage without required approvals
- Do not leave tasks without AC and design references
- Do not bypass build/traceability gates at checkpoints
- Keep outputs deterministic and machine-checkable
- **Do not approve requirements.md without FR/UC source references**
- **Do not approve requirements.md without Evidence References section**
- **Every AC must be traceable back to source FR via requirement's Source field**
- **Do not approve design.md if ANY AC from requirements is missing coverage**
- **Every design feature section must have ACs Implemented field**
- **Task design_ref must match exact design section number**
- Write files only under `{{IDE_CONFIG_DIR}}specs/[feature-name]/`
- Never overwrite an existing file without user confirmation
- Always invoke per-spec skills for document creation, never inline content in workflow
- Always invoke quality gates for validation, never inline checks