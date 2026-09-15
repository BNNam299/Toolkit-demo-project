---
description: Create feature specification (requirements, design, tasks)
allowed-tools: Read, Write, Edit, Grep, Glob, Task
---

# COMMAND: Create Feature Specification

Create feature specification for $ARGUMENTS.

## Workflow: 3 Steps in Order

Each step invokes a self-contained skill that handles reading context, creating the file, and running its own quality gate.

| Step | Document | Template | Skill to Invoke |
|------|----------|----------|----------------|
| 1 | requirements.md | `{{IDE_CONFIG_DIR}}doc-templates/spec-requirements.md` | `spec-requirements` |
| 2 | design.md | `{{IDE_CONFIG_DIR}}doc-templates/spec-design.md` | `spec-design` |
| 3 | tasks.md | `{{IDE_CONFIG_DIR}}doc-templates/spec-tasks.md` | `spec-tasks` |

After each skill completes, ask user to **Approve / Modify / Pause**.

Also update `spec-state.json` after each approval.

## Step-by-Step

### Step 1: requirements.md
1. Read `{{IDE_CONFIG_DIR}}doc-templates/spec-requirements.md`
2. Invoke skill `spec-requirements` — skill will:
   - Read project docs to extract FR-XXX, UC-XXX IDs
   - Create `requirements.md` with EARS acceptance criteria
   - Run quality gate internally
   - Present summary and ask for approval
3. If approved → set `spec-state.json` stage to `approved_requirements`
4. Ask: **Approve / Modify / Pause**

### Step 2: design.md (after Step 1 approved)
1. Read `{{IDE_CONFIG_DIR}}doc-templates/spec-design.md`
2. Verify `spec-state.json` has `stage = approved_requirements`
3. Invoke skill `spec-design` — skill will:
   - Read `requirements.md` to get AC IDs
   - Read project docs for architecture context
   - Create `design.md` with technical architecture
   - Run quality gate internally
   - Present summary and ask for approval
4. If approved → set `spec-state.json` stage to `approved_design`
5. Ask: **Approve / Modify / Pause**

### Step 3: tasks.md (after Step 2 approved)
1. Read `{{IDE_CONFIG_DIR}}doc-templates/spec-tasks.md`
2. Verify `spec-state.json` has `stage = approved_design`
3. Invoke skill `spec-tasks` — skill will:
   - Read `requirements.md` and `design.md`
   - Create `tasks.md` with task registry and dependencies
   - Run quality gate internally
   - Present summary and ask for approval
4. If approved → set `spec-state.json` stage to `approved_tasks`
5. Ask: **Approve / Modify / Pause**

## Completion

After all 3 specs approved:
- Display completion summary
- Offer next step: `/ios-execute <feature-name>`

## Rules
- Write files only under `{{IDE_CONFIG_DIR}}specs/<feature-name>/`
- Never skip a step without user approval
- Never proceed past a failing quality gate
- Every AC must trace back to FR/UC from project docs

## Options
- `--refine` - Modify existing specs (minor/medium/major impact routing)
- `--mode strict` - Full quality gate checks on every step
- `--mode fast` - Streamlined gates, reduced section depth

## Usage
```
/ios-spec login
/ios-spec "login feature"
/ios-spec "login" --mode strict
```
