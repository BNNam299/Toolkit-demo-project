---
name: execution-quality-gates
description: Quality gates for execution workflow. Validates build, test, traceability, AC coverage, and integration checkpoints.
---

# Execution Quality Gates

## Purpose
Define validation criteria for each phase gate in the execution workflow. Gates ensure quality is maintained throughout implementation.

## Gate Definitions

### Gate 1: Build
**Trigger:** After completing a build-affecting task or phase
**Status:** Pass/Fail

| Check | Criteria |
|-------|----------|
| Compilation | Xcode build succeeds with zero errors |
| Warnings | No new warnings introduced |
| Dependencies | All imports resolve correctly |

**On Failure:**
- Stop execution
- Report build errors with file:line references
- Offer fix options (auto-fix, manual fix, refine spec)

**Commands:**
```bash
# Use Xcode MCP tools
1. discover_projs → resolve project/workspace
2. list_schemes → confirm build target
3. build_sim → build for simulator (Debug)
```

---

### Gate 2: Test
**Trigger:** After completing a testable unit or phase
**Status:** Pass/Fail/Partial

| Check | Criteria |
|-------|----------|
| Unit Tests | All unit tests pass |
| Code Coverage | Test coverage maintained or improved |
| Integration Tests | Feature-specific integration tests pass |

**On Failure:**
- Stop execution
- Report failing tests with assertion details
- Require fix before continuing

---

### Gate 3: Traceability
**Trigger:** After completing a feature subset or phase
**Status:** Pass/Fail

| Check | Criteria |
|-------|----------|
| AC → Implementation | Every AC has corresponding code |
| Task → Code | Every task has implementation files |
| Design → Code | Architecture decisions reflected |
| No Orphans | No orphaned requirements |

**Validation:**
```bash
python .claude/scripts/validate_traceability.py [feature-name]
```

**On Failure:**
- Identify missing coverage with specific AC/Task IDs
- Offer to create missing implementation
- Or mark as intentional omission with justification

---

### Gate 4: AC Coverage
**Trigger:** After completing a design-related phase
**Status:** Pass/Fail

| Check | Criteria |
|-------|----------|
| Requirements ACs | All ACs from requirements.md appear in |
| | - Section 1: AC Coverage Summary |
| | - Section 7: ACs Implemented fields |
| | - Section 9: Validates AC column |
| Design ACs | Each task in tasks.md maps to a design section |

**On Failure:**
- List missing ACs with their requirement source
- Block phase with: `Missing AC coverage: [AC-ID]`
- Offer to refine design.md before continuing

---

### Gate 5: Integration
**Trigger:** Before final completion
**Status:** Pass/Fail

| Check | Criteria |
|-------|----------|
| App Launch | App launches successfully |
| Feature Integration | Feature integrates with existing codebase |
| No Regressions | Related areas still function correctly |
| Data Flow | Navigation and data handoff work |

**On Failure:**
- Identify integration issues
- Offer refinement of design
- Require resolution before completion

### Gate 6: Structure (file/folder placement)
**Trigger:** For any task that creates or moves a file
**Status:** Pass/Fail
**Owner:** `ios-architecture` → run its **Structure Compliance Gate** (checklist + BLOCK conditions live there).

**On Failure:** mark task `blocked`, list the off-structure/misnamed/wrong-layer path.

---

### Gate 7: Reuse-First (component reuse-vs-create)
**Trigger:** For any task that touches a UI component
**Status:** Pass/Fail
**Owner:** `ios-components` → run its **Reuse-First Gate** (search evidence, reuse decision, new-component rules).

**On Failure:** mark task `blocked` (new component without search evidence, duplicate, wrong folder, hardcoded styles).

---

### Gate 8: UI/UX Compliance
**Trigger:** Before setting any UI task `done`
**Status:** Pass/Fail
**Owner:** `ios-ui-ux` → run its **UX Compliance Gate** (4 states + recovery, touch targets, haptics, a11y, dark mode).

**On Failure:** keep task `in_progress`/`blocked`; list the missing state / a11y / dark-mode item.

These three gates reference the owning skill as the single source of truth — do not restate criteria here.

## Gate Sequencing

```
Every file-creating task   → Structure Gate (ios-architecture)
Every component task        → Reuse-First Gate (ios-components) BEFORE writing
Every UI task (before done) → UI/UX Gate (ios-ui-ux) + DSS Gate

Phase 1 (Shared)
  → Build Gate → Test Gate → Traceability Gate

Phase 2 (Feature)
  → Build Gate → Test Gate → AC Coverage Gate → Traceability Gate

Phase 3 (Integration)
  → Build Gate → Test Gate → Integration Gate → Traceability Gate
```

## DSS Gate (UI Tasks Only)

For every UI task, before marking `done`:
1. Confirm task notes include DSS evidence line
2. Confirm changed UI files reference DSS tokens for color/font/spacing
3. If violations remain, mark task `blocked` with reason

**DSS Source of Truth:**
- `.claude/shared/Styles/AppColors.swift`
- `.claude/shared/Styles/AppFonts.swift`
- `.claude/shared/Styles/AppSpacing.swift`

**DSS Evidence Format:**
```
DSS: reused tokens [Color.primary, Font.heading, Spacing.md]
```
or
```
DSS: added tokens [Color.notificationBadge] in shared/Styles
```

## Completion Criteria

All gates must pass for feature completion:
- [ ] All tasks in tasks.md marked `done`
- [ ] All phase gates passed
- [ ] Verification confirms: Completeness, Correctness, Coherence
- [ ] No TODO/FIXME in production code
- [ ] spec-state.json updated to `stage: done`