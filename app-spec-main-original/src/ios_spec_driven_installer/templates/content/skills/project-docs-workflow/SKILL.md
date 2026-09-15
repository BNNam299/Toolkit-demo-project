---
name: project-docs-workflow
description:
  Orchestrate the full project documentation chain from PRD through Roadmap. Runs each step in order, invokes per-doc skills and quality gates, handles resume and mode switching. Use when generating or continuing a complete project documentation set.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# PREREQUISITES (read in order before starting)

Before executing this workflow, you MUST read these files:

1. `{{IDE_CONFIG_DIR}}doc-templates/PRD.md`
2. `{{IDE_CONFIG_DIR}}doc-templates/Project_Overview.md`
3. `{{IDE_CONFIG_DIR}}doc-templates/Use_Cases.md`
4. `{{IDE_CONFIG_DIR}}doc-templates/Functional_Requirements.md`
5. `{{IDE_CONFIG_DIR}}doc-templates/Wireframes.md`
6. `{{IDE_CONFIG_DIR}}doc-templates/UX_Flows.md`
7. `{{IDE_CONFIG_DIR}}doc-templates/Project_Implementation_Roadmap.md`
8. `{{IDE_CONFIG_DIR}}skills/project-docs-prd/SKILL.md`
9. `{{IDE_CONFIG_DIR}}skills/project-docs-overview/SKILL.md`
10. `{{IDE_CONFIG_DIR}}skills/project-docs-uc/SKILL.md`
11. `{{IDE_CONFIG_DIR}}skills/project-docs-fr/SKILL.md`
12. `{{IDE_CONFIG_DIR}}skills/project-docs-wireframes/SKILL.md`
13. `{{IDE_CONFIG_DIR}}skills/project-docs-flows/SKILL.md`
14. `{{IDE_CONFIG_DIR}}skills/project-docs-roadmap/SKILL.md`
15. `{{IDE_CONFIG_DIR}}skills/project-docs-contract/SKILL.md`

Only after reading all 15 files, proceed with the workflow below.

## Non-Negotiable Rules

- MUST write files only under `{{IDE_CONFIG_DIR}}specs/[project-name]/`
- MUST NOT skip a step in the chain without explicit user confirmation
- MUST NOT proceed past a failing quality gate
- MUST NOT overwrite an existing file without user confirmation
- MUST NOT fabricate prerequisite content for missing upstream documents
- MUST invoke per-doc skills for document creation, never inline the content here
- MUST invoke quality gate skills for validation, never inline the checks here
- MUST pause for user confirmation between steps
- MUST keep section IDs and naming stable across all documents for traceability
- MUST verify existing documents with quality gates before skipping on resume

# Project Docs Workflow

## When to Use

- User invokes `/ios-project-docs [project-name]` to start a new project doc set
- User invokes `/ios-project-docs [project-name] --continue` to resume an interrupted set
- All seven project documents need to be created or updated end-to-end

## Objective

Orchestrate the full documentation chain. Delegate document creation to per-doc skills, quality gates to `project-docs-quality-gates`, and lifecycle steps to `project-docs-lifecycle`.

## Prerequisites

- `{{IDE_CONFIG_DIR}}specs/[project-name]/` does not exist OR only contains files for completed stages
- All seven templates exist in `{{IDE_CONFIG_DIR}}doc-templates/`
- User has confirmed project scope and naming

---

## Document Chain

Each step produces one file. Steps must run in order because downstream docs depend on upstream ones.

| Step | Document | Per-doc skill | Quality gate | Depends on | Template |
|------|----------|--------------|-------------|-----------|----------|
| 1 | PRD.md | project-docs-prd | gate-prd | none | PRD.md |
| 2 | Project_Overview.md | project-docs-overview | gate-overview | PRD | Project_Overview.md |
| 3 | Use_Cases.md | project-docs-uc | gate-uc | PRD, Overview | Use_Cases.md |
| 4 | Functional_Requirements.md | project-docs-fr | gate-fr | PRD, Overview, Use_Cases | Functional_Requirements.md |
| 5 | Wireframes.md | project-docs-wireframes | gate-wireframes | PRD, Use_Cases, FR | Wireframes.md |
| 6 | UX_Flows.md | project-docs-flows | gate-flows | PRD, Use_Cases, Wireframes | UX_Flows.md |
| 7 | Project_Implementation_Roadmap.md | project-docs-roadmap | gate-roadmap | all above | Project_Implementation_Roadmap.md |

Templates live in `{{IDE_CONFIG_DIR}}doc-templates/`.

All output files go to `{{IDE_CONFIG_DIR}}specs/[project-name]/`.

---

## Workflow

### Step-by-step execution protocol

For each step in the chain:

1. **Check prerequisites**: verify all upstream documents exist in `{{IDE_CONFIG_DIR}}specs/[project-name]/`
2. **Invoke per-doc skill**: use the skill listed in the chain table
3. **Run quality gate**: use the quality gate skill listed in the table
4. **Gate decision**:
   - Pass: ask user to confirm before proceeding to next step
   - Fail: report blockers, require fixes, loop back to step 2
5. **User confirmation**: pause after each document and ask:
   - **Approve**: proceed to next step
   - **Modify**: revise current document, re-run quality gate
   - **Pause**: stop workflow, record progress for resume

### Step 8: Completion

After Roadmap is approved, perform **Completion & Handoff per `project-docs-contract` rule #8**
(generate `_INDEX.md`, completion summary listing all files, offer `/ios-spec <feature-name>`),
then record final status in the project directory.

> **Note:** `project-docs-review` is available as a standalone tool (invoke directly when needed) but is not part of the standard pipeline. Each per-doc skill's quality gate already covers traceability, orphan IDs, and placeholders.

---

## Quality Gates

Each step runs its gate via the `project-docs-quality-gates` skill. **Required sections
(mục lớn + mục con) and doc-specific pass criteria are read from each template's
`QUALITY-GATE-MANIFEST` block — they are NOT restated here** (single source of truth).

| Step | Gate | Skill | Criteria source |
|------|------|-------|-----------------|
| PRD | `gate-prd` | `project-docs-quality-gates` | `doc-templates/PRD.md` → QUALITY-GATE-MANIFEST |
| Overview | `gate-overview` | `project-docs-quality-gates` | `doc-templates/Project_Overview.md` → QUALITY-GATE-MANIFEST |
| Use Cases | `gate-uc` | `project-docs-quality-gates` | `doc-templates/Use_Cases.md` → QUALITY-GATE-MANIFEST |
| Functional Reqs | `gate-fr` | `project-docs-quality-gates` | `doc-templates/Functional_Requirements.md` → QUALITY-GATE-MANIFEST |
| Wireframes | `gate-wireframes` | `project-docs-quality-gates` | `doc-templates/Wireframes.md` → QUALITY-GATE-MANIFEST |
| UX Flows | `gate-flows` | `project-docs-quality-gates` | `doc-templates/UX_Flows.md` → QUALITY-GATE-MANIFEST |
| Roadmap | `gate-roadmap` | `project-docs-quality-gates` | `doc-templates/Project_Implementation_Roadmap.md` → QUALITY-GATE-MANIFEST |

---

## Error Handling / Resume

### Resume protocol

When resuming an interrupted workflow:
1. Scan `{{IDE_CONFIG_DIR}}specs/[project-name]/` for existing documents
2. For each existing document, run its quality gate to verify integrity
3. Skip steps whose documents exist and pass quality gate
4. Re-enter the chain at the first incomplete step
5. If a document exists but fails its quality gate, offer the user:
   - **Fix**: revise and re-validate the failing document
   - **Recreate**: delete and regenerate from scratch

Never assume a document is complete without quality gate verification.

### Mode handling

**fast mode (default):**
- Skip external research unless user requests it
- Concise output with essential sections only
- Quality gates check Core requirements only
- Reduced section depth in documents

**strict mode:**
- Full research with `WebSearch` and `WebFetch` for every evidence claim
- All sections present, detailed content
- Quality gates check every criterion
- Complete cross-references and traceability

Switch modes when user explicitly requests. Document the active mode at the start of each step.

### Gate verification between steps

Before advancing from step N to step N+1:
1. Confirm the output file exists at `{{IDE_CONFIG_DIR}}specs/[project-name]/[DocumentName].md`
2. Confirm the quality gate for step N passed
3. Confirm user approved the document
4. Log progress: which step completed, mode used, issues found

If any check fails, hold at the current step and report the issue.

---

## Output Contract

After Roadmap is approved, present:
- Completion summary listing all files created
- Next-step recommendation: `/ios-spec` for the first feature
- Final status recorded in the project directory
