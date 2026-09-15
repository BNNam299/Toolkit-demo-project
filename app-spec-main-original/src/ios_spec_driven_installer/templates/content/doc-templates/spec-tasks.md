# [Feature Name] - Implementation Plan

## Execution Mode
- Mode: [autopilot|manual]
- Policy: run sequentially by default
- Gate: stop on phase boundary or blocking error

## Task Registry (Machine Readable)

**IMPORTANT:** All IDs below are EXAMPLES - extract actual IDs from design.md and requirements.md

| ID | Title | Type | Status | Refs AC | Refs Design | Files | Checkpoint |
|---|---|---|---|---|---|---|---|
| [2.1.1] | [Create model] | normal | pending | [AC-XXX.Y from design] | [section # from design] | [file path] | [checkpoint] |
| [2.1.2] | [Model property test] | pbt | pending | [AC-XXX.Y from design] | [section # from design] | [file path] | [checkpoint] |
| [3.1.1] | [Build list ViewModel] | normal | pending | [AC-XXX.Y from design] | [7.1 from design] | [file path] | [checkpoint] |

## Dependency Matrix
| Task | Depends On | Can Parallel With |
|---|---|---|
| [3.1.1] | [2.1.1] | [3.2.1] |
| [3.2.1] | [2.1.1] | [3.1.1] |

## 1. Shared Tasks
- [ ] **[Task ID]** [Task title]
  - Refs: [AC-XXX.Y from requirements/design]
  - Design: [section # from design.md]
  - File: [file path]

<!-- DYNAMIC: Add more shared tasks as needed. -->

**Phase Gate 2 (end of Shared phase):** Run XcodeBuildMCP `discover_projs -> list_schemes -> build_sim`, then traceability check passes

## 2. Feature Tasks
- [ ] **[Task ID]** [Task title]
  - Refs: [AC-XXX.Y from requirements/design]
  - Design: [7.1 from design.md]
  - File: [file path]

<!-- DYNAMIC: Add more feature tasks as needed. -->

**Phase Gate 3 (end of Feature phase):** Run XcodeBuildMCP `discover_projs -> list_schemes -> build_sim`, then traceability check passes

## 3. Integration Tasks
- [ ] **[Task ID]** [Task title]
  - Refs: [AC-XXX.Y from requirements/design]
  - Design: [section # from design.md]
  - File: [file path]

<!-- DYNAMIC: Add more integration tasks as needed. -->

**Phase Gate 4 (end of Integration phase):** Run XcodeBuildMCP `discover_projs -> list_schemes -> build_sim`, then traceability check passes

## Traceability Matrix
| Task ID | AC | Design | Property | Status |
|---|---|---|---|---|
| [2.1.1] | [AC-XXX.Y from requirements] | [section #] | - | pending |
| [2.3.1] | [AC-XXX.Y from requirements] | [section #] | P[#] | pending |

## Progress
| Section | Total | Done | Status |
|---|---:|---:|---|
| Shared | 0 | 0 | ⬜ |
| Feature | 0 | 0 | ⬜ |
| Integration | 0 | 0 | ⬜ |

<!-- QUALITY-GATE-MANIFEST:START
# SINGLE source of truth for gate-tasks. Do NOT copy this block into the produced tasks.md
# under specs/. The gate matches sections by NAME, ignoring leading numbering and any trailing
# placeholder in the produced heading.
doc: Tasks
gate: gate-tasks
required_major:
  - "Execution Mode"
  - "Task Registry (Machine Readable)"
  - "Dependency Matrix"
  - "1. Shared Tasks"
  - "2. Feature Tasks"
  - "3. Integration Tasks"
  - "Traceability Matrix"
  - "Progress"
required_minor: {}
quality_checks:
  - "Task Registry has all columns: ID, Title, Type, Status, Refs AC, Refs Design, Files, Checkpoint"
  - "Every task references at least one AC-XXX.Y and exactly one design section number"
  - "Each task's 'Refs Design' matches an EXACT section number present in design.md (e.g. 7.1, 4, 9)"
  - "Every Correctness Property (P#) in design.md §9 has at least one task of Type 'pbt' referencing it (Invariant/Round-trip properties are NOT left untested); property-based tests are required, not optional, for these"
  - "Every AC-XXX.Y in requirements.md is referenced by at least one task (no acceptance criterion ships without an implementing task)"
  - "Every UI/feature task traces to a §7 feature subsection and its work covers that feature's enumerated states (loading/empty/error/success), not only the happy path"
  - "All three Phase Gates (Phase Gate 2, 3, 4) present, each using XcodeBuildMCP discover_projs -> list_schemes -> build_sim then a traceability check"
  - "Traceability Matrix has rows linking Task ID -> AC -> Design -> Property -> Status"
  - "Progress table covers Shared / Feature / Integration"
  - "Status values are one of: pending | in_progress | blocked | done"
QUALITY-GATE-MANIFEST:END -->