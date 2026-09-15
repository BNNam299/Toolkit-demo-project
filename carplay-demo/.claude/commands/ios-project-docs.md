---
description: Create project documentation (PRD, Overview, Use Cases, FR, Wireframes, UX Flows, Roadmap)
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch, Bash
---
# COMMAND: Create Project Documentation

Create full project documentation for $ARGUMENTS.

## Workflow: Steps in Order

Each step must run in order. For each step:

1. Read **only the template file** for that document
2. Invoke the **per-doc skill** listed in the table below
3. Run the **quality gate skill** after creating the document
4. Ask user to **Approve / Modify / Pause** before proceeding to next step


| Step | Document                          | Template                                                            | Per-Doc Skill             | Quality Gate                                          |
| ---- | --------------------------------- | ------------------------------------------------------------------- | ------------------------- | ----------------------------------------------------- |
| 1    | PRD.md                            | `.claude/doc-templates/PRD.md`                            | `project-docs-prd`        | `project-docs-quality-gates` with gate for PRD        |
| 2    | Project_Overview.md               | `.claude/doc-templates/Project_Overview.md`               | `project-docs-overview`   | `project-docs-quality-gates` with gate for Overview   |
| 3    | Use_Cases.md                      | `.claude/doc-templates/Use_Cases.md`                      | `project-docs-uc`         | `project-docs-quality-gates` with gate for UC         |
| 4    | Functional_Requirements.md        | `.claude/doc-templates/Functional_Requirements.md`        | `project-docs-fr`         | `project-docs-quality-gates` with gate for FR         |
| 5    | Wireframes.md                     | `.claude/doc-templates/Wireframes.md`                     | `project-docs-wireframes` | `project-docs-quality-gates` with gate for Wireframes |
| 6    | UX_Flows.md                       | `.claude/doc-templates/UX_Flows.md`                       | `project-docs-flows`      | `project-docs-quality-gates` with gate for UX Flows   |
| 7    | Project_Implementation_Roadmap.md | `.claude/doc-templates/Project_Implementation_Roadmap.md` | `project-docs-roadmap`    | `project-docs-quality-gates` with gate for Roadmap    |
| 8    | _INDEX.md                         | none                                                                | none                      | none                                                  |


## Per-Step Instructions

### Step 1: PRD.md

1. Read `.claude/doc-templates/PRD.md`
2. Invoke skill `project-docs-prd` to create PRD
3. Run quality gate for PRD
4. Ask user: **Approve / Modify / Pause**

### Step 2: Project_Overview.md (after Step 1 approved)

1. Read `.claude/doc-templates/Project_Overview.md`
2. Invoke skill `project-docs-overview` to create Overview
3. Run quality gate for Overview
4. Ask user: **Approve / Modify / Pause**

### Step 3: Use_Cases.md (after Step 2 approved)

1. Read `.claude/doc-templates/Use_Cases.md`
2. Invoke skill `project-docs-uc` to create Use Cases
3. Run quality gate for UC
4. Ask user: **Approve / Modify / Pause**

### Step 4: Functional_Requirements.md (after Step 3 approved)

1. Read `.claude/doc-templates/Functional_Requirements.md`
2. Invoke skill `project-docs-fr` to create FR
3. Run quality gate for FR
4. Ask user: **Approve / Modify / Pause**

### Step 5: Wireframes.md (after Step 4 approved)

1. Read `.claude/doc-templates/Wireframes.md`
2. Invoke skill `project-docs-wireframes` to create Wireframes
3. Run quality gate for Wireframes
4. Ask user: **Approve / Modify / Pause**

### Step 6: UX_Flows.md (after Step 5 approved)

1. Read `.claude/doc-templates/UX_Flows.md`
2. Invoke skill `project-docs-flows` to create UX Flows
3. Run quality gate for UX Flows
4. Ask user: **Approve / Modify / Pause**

### Step 7: Project_Implementation_Roadmap.md (after Step 6 approved)

1. Read `.claude/doc-templates/Project_Implementation_Roadmap.md`
2. Invoke skill `project-docs-roadmap` to create Roadmap
3. Run quality gate for Roadmap
4. Ask user: **Approve / Modify / Pause**

### Step 8: Handoff

Follow the **Completion &amp; Handoff** rule (#8) in `project-docs-contract`: generate `_INDEX.md`, display the completion summary, and offer next step `/ios-spec <feature-name>`.

## Optional: UI/UX Analysis

UI/UX Analysis is **not part of this pipeline** — it is an optional tool, so the design step
(Pencil/Figma/human) stays free to be creative and is not locked to a machine-generated
analysis. If you explicitly want a detailed UI/UX analysis, invoke the `uiux-analysis-workflow`
skill by hand after Wireframes are approved (it produces the `design-ui/` deliverables and
runs its own gates). By default it does not run.

Cross-Review is likewise **not part of this pipeline** — the per-doc quality gates plus your
Approve/Modify/Pause at each step already enforce consistency and traceability. If you want a
final full-set audit, invoke the `project-docs-review` skill by hand. By default it does not run.

## Rules

- Write files only under `.claude/specs/<project-name>/`
- Never skip a step without user approval
- Never proceed past a failing quality gate
- Never overwrite without user confirmation

## Usage

```
/project-docs MyProjectName
/project-docs MyProjectName --mode strict
```

