---
name: execution-implement
description: Execute tasks from an implementation plan. Use to implement task IDs from tasks.md, keep progress/traceability updated, write property-based tests, and build-check with XcodeBuildMCP.
---

# Execution Implement

## Purpose
Execute `tasks.md` with strict autopilot controls: transactional single-task execution, automatic continuation inside current phase, mandatory phase gates.

## Required Skills (read before executing)

Read these three iOS rulebooks before running any task. Their gates are **mandatory** during
execution — this skill invokes them, it does not restate their criteria:

- `{{IDE_CONFIG_DIR}}skills/ios-architecture/SKILL.md` — **Structure Compliance Gate** (file/folder placement)
- `{{IDE_CONFIG_DIR}}skills/ios-components/SKILL.md` — **Reuse-First Gate** (reuse-vs-create decision)
- `{{IDE_CONFIG_DIR}}skills/ios-ui-ux/SKILL.md` — **UX Compliance Gate** (states, a11y, haptics, dark mode)

Each gate defines its own checklist, BLOCK conditions, and the evidence line to record in task notes.

## Input
- Task selector: specific ID, `next`, or `autopilot`
- Optional Figma link for UI tasks

## Outputs
- Implemented code and tests
- Updated task statuses in `tasks.md`
- Updated `spec-state.json`
- Traceability validation result

---

## Required Files
Before execution, verify all exist:
- `{{IDE_CONFIG_DIR}}specs/[feature-name]/requirements.md`
- `{{IDE_CONFIG_DIR}}specs/[feature-name]/design.md`
- `{{IDE_CONFIG_DIR}}specs/[feature-name]/tasks.md`
- `{{IDE_CONFIG_DIR}}specs/[feature-name]/spec-state.json`

Reject execution unless `spec-state.stage = approved_tasks`.

Xcode MCP readiness preflight (required before task execution):
1. `discover_projs` to resolve project/workspace
2. `list_schemes` to confirm build target
3. If MCP tools unavailable, stop and report config issue

---

## Execution Mode

### Default: Autopilot
- Run sequentially through tasks in current phase
- Stop only at: phase gate, blocked task, unresolved declaration collision, explicit user stop

### Optional: Manual
- Execute one task then stop

---

## Task Transaction Protocol (Required)

**Execute exactly in the order defined in `tasks.md`** — do not reorder tasks based on architectural preferences.

For each task:
1. Validate dependencies complete (per Dependency Matrix)
2. Set task status to `in_progress`
3. For any new `class`/`struct`/`enum`, run declaration collision check first
4. **Pre-implementation gates (mandatory):**
   - If the task **creates or moves a file** → run the **Structure Compliance Gate** (`ios-architecture`).
   - If the task **touches a UI component** → run the **Reuse-First Gate** (`ios-components`) BEFORE writing code.
   - Any gate BLOCK → set status `blocked`, record the failing evidence line, stop autopilot.
5. Implement only this task as specified
6. **Pre-done gate (mandatory):** if the task is a **UI task** → run the **UX Compliance Gate** (`ios-ui-ux`).
   A BLOCK keeps the task `in_progress`/`blocked` — never `done`.
7. Run scoped checks (build-first, lint optional)
8. On pass (all applicable gates + build): set status `done`
9. On fail: set status `blocked`, write cause, stop autopilot
10. Update traceability rows for task

**Declaration collision check** (required before creating types):
- Search project sources for existing declaration names
- Detect collisions by exact type name
- If matching declaration exists:
  - Prefer reuse/update/extension of existing type
  - Otherwise rename using project naming conventions
  - If conflict cannot be safely resolved, mark task `blocked` and stop autopilot
- Never introduce duplicate declarations

**Task completion synchronization** (required on done):
- Task Registry: update status to `done`
- Checklist markdown: change `- [ ] **TASK_ID**` to `- [x] **TASK_ID**`
- Traceability Matrix: update row status to `done`

**Task notes format:**
```
Result: done|blocked
Files: <comma-separated>
Build: pass|fail
Structure: <path> → <layer> OK | violations: none        (required for file-creating tasks)
Reuse: <component> | New: <component> | Reason: <why> | Searched: <dirs>  (required for component tasks)
UX: states[4/4] recovery[✓] touch≥44[✓] haptic+visual[✓] a11y[✓] dynamicType[✓] darkmode[✓]  (required for UI tasks)
DSS: reused tokens <list> | added tokens <list> in shared/Styles (required for UI tasks)
DeclarationCheck: pass|conflict
DeclarationConflict: <TypeName> | Resolution: reused|renamed|blocked (only if conflict)
Reason: <only if blocked>
```

Allowed statuses: `pending | in_progress | blocked | done`

---

## Phase Gate Protocol (Required)

When all tasks in a phase are `done`:
1. Build with Xcode tools
2. Run traceability validation script
3. **AC Coverage Validation** (for design-related phases):
   - Read `requirements.md` and extract all AC IDs
   - Read `design.md` and verify each AC appears in AC Coverage Summary or feature sections
   - If any AC missing coverage, mark phase `blocked`
4. If any fail: mark phase `blocked`, stop
5. If all pass: mark phase `done`, continue autopilot

**Recommended gate sequence:**
1. `discover_projs`
2. `list_schemes`
3. `build_sim` for selected scheme (Debug)
4. `python {{IDE_CONFIG_DIR}}scripts/validate_traceability.py [feature-name]`
5. AC coverage check (manual validation against requirements.md + design.md)

**Simulator-first policy:**
- Build gate always uses simulator compile (`build_sim`)
- `build_run_sim` allowed only when run/launch verification is explicitly needed
- `boot_sim` and other simulator launch actions are prohibited unless user explicitly asks

---

## Figma Policy (Framelink MCP)
- For UI tasks, if Figma URL provided, fetch design context via Framelink MCP
- Prefer existing shared components before creating new ones
- Record component decision: `Reuse: <name>` or `New: <name> | Reason: <why>`
- Apply accessibility checks for key UI states

UI task flow:
1. Parse file and node URL if provided
2. Fetch tokens/layout context from Framelink MCP
3. Map to local design tokens/component variants
4. Implement state-complete SwiftUI view (loading/empty/error/success)
5. Add/adjust snapshot or UI tests where available

---

## Design Style System Gate (Required)

For UI tasks, enforce DSS before marking `done`:
- Runtime tokens source of truth: `{{IDE_CONFIG_DIR}}shared/Styles/` (AppColors.swift, AppFonts.swift, AppSpacing.swift)
- `{{IDE_CONFIG_DIR}}shared/COMPONENT_FORMAT.md` is style usage guide, not runtime token storage
- Do not hardcode style values when DSS tokenization is appropriate

DSS verification on UI task completion:
1. Confirm task notes include DSS evidence line
2. Confirm changed UI files reference DSS tokens for color/font/spacing
3. If violations remain, mark task `blocked` with reason and stop autopilot

---

## Parallel Policy
- Sequential is default and recommended
- Parallel execution allowed only if dependency matrix confirms no ordering or file conflicts
- If any parallel branch fails, stop all active branches and mark failed task as `blocked`

---

## Error Handling
- Build failure: up to 3 direct fix attempts; then mark task `blocked`
- Requirements/design change request: stop execution, use spec-refine skill for minor changes or /ios-spec for major redesign
- Missing references in traceability: block task until refs corrected
- Declaration collision: resolve by reuse/rename; if unresolved, block task and stop

Retry tiers:
- Attempt 1-2: direct code fix, rerun scoped checks
- Attempt 3: verify design/task alignment, patch task notes if mismatch
- After attempt 3 fail: block task and request user decision

If requirements or design changed mid-run:
1. Pause autopilot immediately
2. Update `spec-state.json` stage to appropriate draft stage
3. Regenerate affected docs/tasks
4. Resume from first impacted checkpoint

---

## Completion Rules
- Autopilot run completes when all non-optional tasks are `done` and final phase gate passes
- Optional PBT tasks can remain pending if marked optional in task registry
- Final state update:
```json
{
  "stage": "done",
  "execution": {
    "mode": "autopilot",
    "last_checkpoint": "[id]"
  }
}
```

## Non-Negotiable iOS Quality Rules
- Do not move to next checkpoint if build fails
- Do not set a file-creating task `done` if the **Structure Compliance Gate** (`ios-architecture`) fails
- Do not set a component task `done` without a **Reuse-First Gate** (`ios-components`) evidence line (reuse or justified new)
- Do not set a UI task `done` if the **UX Compliance Gate** (`ios-ui-ux`) fails (missing state, no recovery, a11y/dark-mode gaps)
- Do not mark feature complete without verifying all declared UI states
- For ViewModel tasks, include deterministic state transition tests
- For integration tasks, verify navigation data handoff and refresh behavior
- For UI tasks, do not mark `done` when style is hardcoded and not persisted in DSS tokens
- Do not mark any task `done` if new declarations were added without collision check
- Do not introduce duplicate type declarations in the same build target
- Property-based tests for design §9 Correctness Properties (P#) are REQUIRED tasks and must be authored; other tests may be run manually after build-stable milestones. Do not mark a feature complete while any P# has no implemented pbt task. If the test target is not yet present, that is a blocker to resolve (see project-structure / testing-integration), not a reason to silently drop the tests
