---
name: spec-tasks
description: Create implementation plan from design. Use when creating tasks.md, breaking down work by feature, planning implementation.
allowed-tools: Read, Write, Edit, Grep, Glob
skills:
  - spec-creation-contract
  - spec-quality-gates
---

# Create Tasks

Create a strict, execution-ready `tasks.md` for autopilot task implementation.

## Output

- `.claude/specs/[feature-name]/tasks.md`
- Update `.claude/specs/[feature-name]/spec-state.json`

## Prerequisites

- `requirements.md` exists
- `design.md` exists
- `spec-state.json` has `stage = approved_design`

If prerequisites fail, stop and ask user to complete prior stages first.

---

## Phase 1: Read Context

1. Read `requirements.md` to extract all AC-XXX.Y IDs
2. Read `design.md` to extract:
   - Section numbers (for Design Ref column)
   - Feature breakdown sections (7.1, 7.2, etc.)
   - Component/file plan
   - Correctness properties (for PBT tasks)
3. Map each AC to its design section

---

## Phase 2: Write Tasks

Create `tasks.md` at `.claude/specs/[feature-name]/tasks.md`.

Reference the template structure from `doc-templates/spec-tasks.md` for section layout.

**Write incrementally** — follow the "Write Incrementally (avoid oversized output)" rule in
`spec-creation-contract`: create the file with the registry, then append **one phase at a time**
(Shared → Feature → Integration) with `Edit`. Run the quality gate only after all sections are written.

Set `stage = draft_tasks` in spec-state.json.

### Task Rules

- Every task must map to at least one AC
- Every task must reference a design section number
- **Design Ref format**: Use EXACT design section number (e.g., `7.1`, `4`, `9`)
- **Matching rule**: Task `Refs Design` MUST match a design.md section number exactly
- Status starts at `pending`
- Allowed status values: `pending | in_progress | blocked | done`
- Only include coding tasks (write/modify/test code)
- Task order follows user's chosen approach from design.md (logic-first, UI-first, or hybrid)
- Each feature task set must include ViewModel, View, and Verify tasks
- Each feature/UI task must cover its design §7 states (loading/empty/error/success), not just the happy path
- PBT tasks are REQUIRED for every Correctness Property (P#) in design §9 (Invariant/Round-trip): each P# needs at least one Type `pbt` task in the registry and matrix. PBTs for non-property behaviors remain optional.

### Phase-End Debug Gates

- Run full debug/build gate at the end of each phase (Phase 2, Phase 3, Phase 4)
- Gate must use XcodeBuildMCP sequence: `discover_projs → list_schemes → build_sim`
- After simulator build passes, run traceability validation
- Do not promote to next phase if phase-end gate fails
- Do not run or boot simulator during phase-end gates unless user explicitly requests

### Autopilot Sequencing Rules

- Default execution order follows checkpoint order
- Autopilot may continue automatically inside same phase
- On first blocked task, stop and report root cause and suggested fix
- Parallel tasks allowed only when dependency matrix explicitly allows

---

## Phase 3: Quality Gate and Confirmation

1. Run the tasks quality gate: invoke `spec-quality-gates` with gate `gate-tasks`
2. Fix any issues the gate raises
3. Present delivery summary to user:

```text
✅ Created: .claude/specs/[feature-name]/tasks.md

Tasks summary:
- Total tasks: Z
- Shared tasks: N
- Feature tasks: M
- Integration tasks: K
- Dependencies mapped
- Traceability complete

Do the tasks look good?

1. ✅ Approve tasks and stop here
2. ✏️ Request changes
3. ▶️ Start execution now (explicit)
4. ⏸️ Stop here
```

- **Approve (option 1)**: set `stage = approved_tasks`, stop and wait for explicit execution command
- **Modify**: revise tasks, keep `stage = draft_tasks`, re-run gate
- **Start execution (option 3)**: set `stage = approved_tasks`, invoke `/ios-execute [feature-name]`
- **Pause**: end session

**Execution trigger safety**: Never auto-start execution from ambiguous user replies. Start execution only on explicit intent.
