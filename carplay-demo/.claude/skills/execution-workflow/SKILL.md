---
name: execution-workflow
description: Orchestrate implementation of approved feature specs. Primary entry point for execution workflow including implementation, verification, and refinement.
---

# PREREADIS (read in order before starting)

Before executing this workflow, you MUST read these files:

1. `.claude/skills/execution-implement/SKILL.md` — Task implementation skill
2. `.claude/skills/execution-quality-gates/SKILL.md` — Phase gate checks
3. `.claude/skills/execution-verify/SKILL.md` — Final verification
4. `.claude/skills/spec-refine/SKILL.md` — Error recovery / refinement
5. `.claude/skills/ios-architecture/SKILL.md` — Structure Compliance Gate (file/folder placement)
6. `.claude/skills/ios-components/SKILL.md` — Reuse-First Gate (reuse-vs-create)
7. `.claude/skills/ios-ui-ux/SKILL.md` — UX Compliance Gate (states, a11y, haptics, dark mode)
8. `.claude/specs/[feature-name]/requirements.md` — Feature requirements
9. `.claude/specs/[feature-name]/design.md` — Technical design
10. `.claude/specs/[feature-name]/tasks.md` — Task registry

Only after reading all 10 files, proceed with the workflow below. The three iOS gates
(Structure / Reuse-First / UX) are **mandatory** during Step 4 and at every phase gate.

# Execution Workflow

## Purpose
Orchestrate the implementation of approved feature specifications with support for autopilot/manual modes, phase gates, and refinement loops.

## When to Use
- Spec is complete (requirements + design + tasks approved)
- Ready to implement feature
- Need structured execution with checkpoints

## Prerequisites
- `spec-state.json` shows `stage = approved_tasks`
- `tasks.md` exists with complete task registry
- `design.md` exists with technical approach
- Project structure exists per roadmap

## Workflow

### Step 1: Validation
Load and validate spec readiness:
1. Read `.claude/specs/[feature-name]/spec-state.json`
2. Verify `stage = approved_tasks`
3. Confirm `requirements.md`, `design.md`, `tasks.md` all exist
4. If any check fails, stop and direct user to `/ios-spec` command

### Step 2: Load Context
Read all spec artifacts:
- `requirements.md` — source of truth for ACs
- `design.md` — technical approach and architecture
- `tasks.md` — task registry, dependency matrix, phase gates

### Step 3: Determine Execution Mode
Ask user (if not already set in spec-state):
```
Execution mode:
1. **Autopilot** — Execute continuously until completion or blocker
2. **Manual** — Stop after each task for review
```
Update spec-state with selected mode.

### Step 4: Execute Tasks
For each task in dependency order:

1. Invoke execution-implement skill for the task
2. Update task status to `done` or `blocked`
3. Check for phase gate after each completed phase
4. In manual mode: pause after each task for user confirmation
5. In autopilot mode: continue until phase gate or blocker

**Phase Gate Protocol:**
After completing all tasks in a phase:
1. Build gate: Xcode build passes with no errors
2. Test gate: Unit tests pass
3. Traceability gate: All ACs have implementation
4. AC Coverage gate: All ACs from requirements appear in design
5. Integration gate: Feature integrates with existing code

If any gate fails: stop autopilot, report issues, offer fix options.

### Step 5: Handle Refinement (if needed)
If implementation reveals spec issues:
1. Pause execution
2. Offer options:
   - Refine spec now (use spec-refine skill)
   - Continue with workaround
   - Pause and review
3. If refining: invoke spec-refine skill, reload updated artifacts
4. Resume from first impacted checkpoint

### Step 6: Verification
After all tasks complete, invoke execution-verify skill:
- Completeness: All requirements/tasks implemented
- Correctness: Build passes, tests pass, ACs satisfied
- Coherence: Architecture matches design, naming consistent

### Step 7: Finalize
Update `spec-state.json`: `stage = done`

Present completion summary:
```
✅ Feature implementation complete: [feature-name]

### Implementation Summary
- Tasks completed: N/M
- Phase gates passed: X
- Refinement cycles: Y
- Verification: ✅ PASSED

### Artifacts
- Code changes: [list key files]
- Tests added: [list test files]
- Spec updates: [if any refinement occurred]

### Options:
1. Start next feature → /ios-spec
2. Review changes → /ios-execute verify [feature-name]
```

## Integration with Other Workflows

### From /ios-spec workflow
```
/ios-spec command completes spec creation →
  Handoff to execution-workflow →
    User confirms mode → execution begins
```

### From /project-docs workflow
```
/project-docs creates roadmap →
  /ios-spec creates spec for a feature →
    /ios-execute implements the feature
```

## Rules

### Execution
- ALWAYS validate spec-state before starting
- ALWAYS run phase gates at checkpoints
- NEVER skip verification step
- ALWAYS update task status in tasks.md
- ALWAYS handle spec refinement gracefully

### Mode Behavior
- **Autopilot**: Execute continuously, stop only on blockers/checkpoints
- **Manual**: Pause after each task, wait for explicit continue

### Error Handling
- Build failures: Stop, report, offer fix options
- Spec mismatches: Offer refinement workflow
- Blocked tasks: Escalate to user with context

### State Management
- Maintain accurate spec-state.json throughout
- Track which tasks are done/in-progress/blocked
- Record refinement cycles for audit trail
