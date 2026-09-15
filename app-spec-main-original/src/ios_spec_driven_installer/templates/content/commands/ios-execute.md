---
description: Execute feature implementation (implement, verify, refine)
---

# COMMAND: Execute Feature Implementation

Implement the `$ARGUMENTS` feature using structured execution workflow.

## Prerequisites Check

Before executing, verify ALL:
- `{{IDE_CONFIG_DIR}}specs/<feature-name>/spec-state.json` exists
- `stage = approved_tasks` in spec-state.json
- `requirements.md`, `design.md`, `tasks.md` all exist

If prerequisites fail → tell user to run `/ios-spec <feature-name>` first.

## Workflow: 4 Phases

Each phase invokes a specific skill that handles reading context, executing, and self-validating.

| Phase | Purpose | Skill to Invoke |
|-------|---------|----------------|
| 1 | Load Context | `execution-workflow` (main orchestrator) |
| 2 | Execute Tasks | `execution-implement` |
| 3 | Verify | `execution-verify` |
| 4 | Refinement (if needed) | `spec-refine` |

## Phase-by-Phase

### Phase 1: Load Context
1. Read `{{IDE_CONFIG_DIR}}skills/execution-workflow/SKILL.md`
2. Read all spec artifacts:
   - `{{IDE_CONFIG_DIR}}specs/<feature-name>/requirements.md`
   - `{{IDE_CONFIG_DIR}}specs/<feature-name>/design.md`
   - `{{IDE_CONFIG_DIR}}specs/<feature-name>/tasks.md`
3. Confirm user execution mode: **autopilot** or **step-by-step**

### Phase 2: Execute Tasks
1. Invoke skill `execution-implement` — skill will:
   - Read task registry from `tasks.md`
   - Execute tasks in dependency order
   - Run phase gates (build, test, traceability, AC coverage)
   - Report status after each gate
2. If any gate fails → go to Phase 4 (Refinement)
3. After all tasks complete → proceed to Phase 3

### Phase 3: Verify
1. Invoke skill `execution-verify` — skill will:
   - Verify implementation against requirements.md
   - Check completeness and correctness
   - Generate verification report
2. If verification passes → deliver completion summary
3. If issues found → go to Phase 4 (Refinement)

### Phase 4: Refinement (if needed)
1. Invoke skill `spec-refine` — skill will:
   - Analyze failing gate or verification issue
   - Apply fix based on impact level (minor/medium/major)
   - Re-run affected gate/verification
2. Loop back to Phase 3 until clean

## Phase Gates

After each phase, run gate checks:
- **Build gate**: code compiles without errors
- **Test gate**: unit tests pass
- **Traceability gate**: all AC IDs traceable to implemented code
- **AC coverage gate**: every AC has a corresponding test
- **Integration gate**: components work together end-to-end

## Execution Modes

- **autopilot** (default): continuous execution, pause only on gate failures
- **step-by-step**: pause after each task for user confirmation

## Completion
After this feature reaches `stage: done`, deliver the completion summary and offer the next step:
- If more features remain in the roadmap → `/ios-spec <next-feature>` then `/ios-execute <next-feature>`.
- **If every `{{IDE_CONFIG_DIR}}specs/*/spec-state.json` is `done` and the app builds/launches** → suggest the
  optional app-wide UI enhancement pass: **`/ios-ui-redesign --pen <style> | --image <path> | --desc "<style>"`**
  (redesign the finished UI to a distinctive style; independent flow, does not change business logic).

## Rules
- Write files only under `{{IDE_CONFIG_DIR}}specs/<feature-name>/`
- Never skip phase gates
- Never proceed past a failing gate without user approval
- Track all changes in spec-state.json

## Usage
```
/ios-execute login
/ios-execute "login feature"
/ios-execute login --mode autopilot
```
