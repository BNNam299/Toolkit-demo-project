---
name: spec-refine
description: Apply changes to existing specs by impact level. Routes minor updates to patch path and medium/major updates to partial or full regeneration. Use when modifying existing requirements, design, or tasks.
allowed-tools: Read, Write, Edit, Grep, Glob, Task
skills:
  - spec-creation-contract
---

# Refine Spec

Receive change requests for existing feature specs, classify impact, and route to the correct refinement path.

## Scope

Feature folder: `{{IDE_CONFIG_DIR}}specs/[feature-name]/`

Required files:
- `requirements.md`
- `design.md`
- `tasks.md`

If any required file is missing, stop and instruct user to create missing specs first.

---

## Impact Classification

### Minor (Patch Path)
Use when ALL are true:
- Wording or acceptance-criteria clarifications
- No architecture/module boundary changes
- No major checkpoint/dependency reshaping

Action: Apply minimal edits directly, preserving format, IDs, and heading hierarchy.

### Medium (Partial Regenerate Path)
Use when design or task structure changes materially:
- Feature flow adjustments
- Component/interface updates
- Checkpoint/dependency updates

Action: Confirm plan with user, then regenerate `design.md` and `tasks.md`.

### Major (Full Regenerate Path)
Use when requirement scope changes:
- New/removed requirement families
- MVP priority reshuffle
- Broad behavior changes across docs

Action: Confirm plan with user, then regenerate all three: `requirements.md`, `design.md`, `tasks.md`.

---

## Required Flow

1. Read all three spec files
2. Classify impact: minor / medium / major
3. Present routing decision + rationale
4. Ask explicit confirmation before proceeding
5. Run selected path
6. Summarize what changed and what remains

Never apply direct file edits in the routing phase.

---

## Confirmation Prompt

```text
Refinement impact: [minor|medium|major]

Recommended path:
- minor: Apply patch directly
- medium: Regenerate design.md + tasks.md
- major: Regenerate all specs (requirements + design + tasks)

Proceed with this path?
1) Yes, proceed
2) Choose different path
3) Stop
```

---

## Minor Patch Rules

When applying minor changes:
- Keep existing heading hierarchy
- Keep existing ID conventions (US-*, AC-*, task IDs)
- Do not remove task registry, dependency matrix, or traceability matrix sections
- Do not introduce placeholders in final output
- Re-check references (AC/design/task IDs) for consistency after patching

---

## Partial/Major Regeneration Rules

When regenerating specs:
1. Preserve IDs from the current spec that remain valid
2. Update `spec-state.json` to the appropriate draft stage
3. Follow the per-spec skill quality gates for regenerated files
4. Present delivery summary after regeneration

---

## Output Contract

Always provide:
- Impact level classified
- Selected path and rationale
- Files expected to change
- Whether execution was started or stopped