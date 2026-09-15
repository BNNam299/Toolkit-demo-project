---
name: spec-workflow
description:
  Orchestrate the creation of complete feature specifications (requirements → design → tasks) with approval gates and state tracking. Primary entry point for feature-level spec workflow.
allowed-tools: Read, Write, Edit, Grep, Glob, Task
---

# PREREADIS (read in order before starting)

Before executing this workflow, you MUST read these files:

1. `{{IDE_CONFIG_DIR}}doc-templates/spec-requirements.md` — Requirements template
2. `{{IDE_CONFIG_DIR}}doc-templates/spec-design.md` — Design template
3. `{{IDE_CONFIG_DIR}}doc-templates/spec-tasks.md` — Tasks template
4. `{{IDE_CONFIG_DIR}}skills/spec-requirements/SKILL.md` — Requirements creation skill
5. `{{IDE_CONFIG_DIR}}skills/spec-design/SKILL.md` — Design creation skill
6. `{{IDE_CONFIG_DIR}}skills/spec-tasks/SKILL.md` — Tasks creation skill
7. `{{IDE_CONFIG_DIR}}skills/spec-quality-gates/SKILL.md` — Quality gate skill

Only after reading all 7 files, proceed with the workflow below.

# Spec Workflow

Orchestrate the creation of complete feature specifications (requirements → design → tasks) with approval gates and state tracking. Delegate spec creation to per-spec skills.

---

## Spec Chain

Each step produces one file. Steps must run in order because downstream specs depend on upstream ones.

| Step | Document | Per-spec skill | Quality gate | Depends on | Template |
|------|----------|---------------|--------------|-----------|----------|
| 1 | requirements.md | spec-requirements | gate-requirements | project docs (FR, UC) | spec-requirements.md |
| 2 | design.md | spec-design | gate-design | requirements.md | spec-design.md |
| 3 | tasks.md | spec-tasks | gate-tasks | requirements.md, design.md | spec-tasks.md |

Templates live in `{{IDE_CONFIG_DIR}}doc-templates/`.

All output files go to `{{IDE_CONFIG_DIR}}specs/[feature-name]/`.

---

## State Machine

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
- Track state in `spec-state.json`

---

## Execution Protocol

For each step in the chain:

1. **Check prerequisites**: verify upstream spec files exist and are approved
2. **Read project context**: extract FR-XXX and UC-XXX IDs relevant to this feature from project docs
3. **Invoke per-spec skill**: use the skill listed in the table above
4. **Run quality gate**: use `spec-quality-gates` with the gate for this step
5. **Gate decision**:
   - Pass: ask user to confirm before proceeding
   - Fail: report blockers, require fixes, loop back
6. **User confirmation**: pause after each spec and ask:
   - **Approve**: proceed to next step
   - **Modify**: revise current spec, re-run quality gate
   - **Pause**: stop workflow, record progress

### Step 1: Requirements

Read project documentation:
- `{{IDE_CONFIG_DIR}}specs/[project-name]/PRD.md` (for evidence)
- `{{IDE_CONFIG_DIR}}specs/[project-name]/Functional_Requirements.md` (for FR-XXX IDs)
- `{{IDE_CONFIG_DIR}}specs/[project-name]/Use_Cases.md` (for UC-XXX IDs)

Extract FR-XXX and UC-XXX IDs relevant to [feature-name].

Invoke `spec-requirements` skill to create `requirements.md`.

### Step 2: Design (after requirements approved)

Verify `spec-state.json` has `stage = approved_requirements`.

Invoke `spec-design` skill to create `design.md` from approved requirements.

### Step 3: Tasks (after design approved)

Verify `spec-state.json` has `stage = approved_design`.

Invoke `spec-tasks` skill to create `tasks.md` from approved design.

---

## Resume Protocol

When resuming an interrupted spec workflow:

1. Read `spec-state.json` to determine current stage
2. Check which spec files already exist
3. Re-enter at the first incomplete stage
4. Verify existing files pass quality gates before skipping
5. If a file fails quality gate: offer to fix or recreate

---

## Completion and Handoff

After all three specs are approved:

Present completion summary:

```text
✅ Feature spec complete for [feature-name]:

1. ✅ requirements.md
   - User stories: N
   - Acceptance criteria: M

2. ✅ design.md
   - Architecture decisions: X
   - Components: Y

3. ✅ tasks.md
   - Total tasks: Z
   - Dependencies mapped

Ready for implementation!

Options:
1. Start implementation → /ios-execute [feature-name]
2. Make changes → /ios-spec [feature-name] --refine
3. Switch to autopilot mode for execution
```

Update `spec-state.json`: `stage = approved_tasks`.

---

## Spec Refinement

When the user requests changes to an existing spec:

- **Minor changes** (wording, AC clarifications): invoke `spec-refine` skill with `impact = minor`
- **Medium changes** (flow adjustments, component updates): invoke `spec-refine` skill with `impact = medium`
- **Major changes** (requirement scope changes, MVP reshuffle): invoke `spec-refine` skill with `impact = major`

---

## Non-Negotiable Rules

- Write files only under `{{IDE_CONFIG_DIR}}specs/[feature-name]/`
- Never skip a stage without user approval
- Never proceed past a failing quality gate
- Never overwrite an existing file without user confirmation
- Never fabricate FR/UC source references — extract them from actual project docs
- Always invoke per-spec skills for spec creation, never inline the content here
- Always invoke spec-quality-gates for validation, never inline the checks here
- Always pause for user confirmation between stages
- Maintain spec-state.json accuracy at all times
- Every AC must be traceable back to source FR/UC
