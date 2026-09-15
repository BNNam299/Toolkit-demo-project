---
name: execution-contract
description: Execution workflow contract for implementing approved specs. Defines phase gates, mode behaviors, refinement procedures, and skill references.
---

# Execution Contract

## Purpose
Define standards and procedures for implementing feature specifications with quality assurance.

## Skill References
This contract works with these execution skills:
- **execution-workflow** — Orchestrates the full execution flow (validation → context → mode → tasks → verify → finalize)
- **execution-implement** — Executes individual tasks with transaction protocol, DSS gates, collision checks
- **execution-verify** — Verifies implementation completeness, correctness, coherence
- **execution-quick** — Quick implementation for small features (<4hrs) without full specs
- **execution-quality-gates** — Validates build, test, traceability, AC coverage, integration checkpoints

## Execution Modes

### Autopilot Mode
- Execute tasks continuously in dependency order
- Stop only at:
  - Phase gates (build/test/traceability failures)
  - Spec-design mismatches requiring refinement
  - User interruption
- Best for: Clear specs, experienced team, urgent delivery

### Manual Mode
- Pause after each task completion
- Wait for explicit user confirmation to continue
- Stop at:
  - Every task boundary
  - Phase gates
  - User request
- Best for: Complex features, learning, high-risk changes

## Phase Gates

### Gate 1: Build
**Trigger:** After completing a build-affecting task
**Validation:**
- Xcode build succeeds with no errors
- No new warnings introduced
**On Failure:**
- Stop execution
- Report build errors
- Offer fix options

### Gate 2: Test
**Trigger:** After completing a testable unit
**Validation:**
- Unit tests pass
- Code coverage maintained
**On Failure:**
- Stop execution
- Report failing tests
- Require fix before continue

### Gate 3: Traceability
**Trigger:** After completing feature subset
**Validation:**
- All ACs have corresponding implementation
- No orphaned requirements
**On Failure:**
- Identify missing coverage
- Offer to create missing implementations
- Or mark as intentional omission

### Gate 4: AC Coverage
**Trigger:** After completing a design-related phase
**Validation:**
- All ACs from requirements.md appear in design.md (AC Coverage Summary, Section 7, Section 9)
- Each task in tasks.md maps to a design section
**On Failure:**
- List missing ACs with source
- Block phase
- Offer to refine design before continuing

### Gate 5: Integration
**Trigger:** Before final completion
**Validation:**
- Feature integrates with existing codebase
- No regressions in related areas
- App launches successfully
**On Failure:**
- Identify integration issues
- Offer refinement of design
- Require resolution

## Gate Sequencing

```
Phase 1 (Shared):
  → Build Gate → Test Gate → Traceability Gate

Phase 2 (Feature):
  → Build Gate → Test Gate → AC Coverage Gate → Traceability Gate

Phase 3 (Integration):
  → Build Gate → Test Gate → Integration Gate → Traceability Gate
```

## Refinement Procedures

### When to Refine
- Implementation reveals spec is incomplete
- Technical constraints make design infeasible
- Better approach discovered during implementation

### Refinement Workflow
1. Pause current execution
2. Document discovery/issue
3. Use **spec-refine** skill to update specs
4. Wait for spec update
5. Reload updated artifacts
6. Resume execution from first impacted checkpoint

### Refinement Routing
- **Minor** (wording, AC clarifications) → spec-refine skill with patch mode
- **Medium** (flow adjustments, new scenarios) → spec-design + spec-tasks skills
- **Major** (requirement changes, new features) → full regenerate via /ios-spec command

### Refinement Tracking
- Log refinement cycle in spec-state.json
- Track what changed and why
- Maintain audit trail

## Task Execution Standards

### Before Starting Task
- Verify prerequisites complete
- Check dependencies satisfied
- Review acceptance criteria

### During Task Execution
- Follow design.md guidance
- Reference requirements for ACs
- Write tests alongside implementation

### After Task Completion
- Mark task done in tasks.md
- Verify AC satisfaction
- Update traceability matrix
- Run relevant tests

## State Management

- Maintain accurate spec-state.json throughout execution
- Track which tasks are `done`/`in_progress`/`blocked`
- Record refinement cycles for audit trail
- Allowed task statuses: `pending | in_progress | blocked | done`
- Final state: `stage: done`

## Completion Criteria

Feature implementation is complete when:
1. All tasks in tasks.md marked `done`
2. All phase gates passed
3. Verification confirms:
   - Completeness: All ACs implemented
   - Correctness: Code behaves as specified
   - Coherence: Implementation matches design intent
4. No TODO/FIXME in production code
5. spec-state.json updated to `stage: done`

## Error Recovery

### Build Errors
1. Stop execution
2. Capture build output
3. Analyze error
4. Options:
   - Auto-fix if obvious
   - Ask user for guidance
   - Refine spec if design issue

### Test Failures
1. Stop execution
2. Capture test output
3. Identify failing assertions
4. Options:
   - Fix implementation
   - Update test if spec changed
   - Refine spec if requirement unclear

### Spec Mismatches
1. Document mismatch
2. Pause execution
3. Offer refinement workflow
4. After refinement, reload and continue
