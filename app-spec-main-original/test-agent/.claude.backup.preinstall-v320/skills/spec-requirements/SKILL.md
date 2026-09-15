---
name: spec-requirements
description: Create requirements.md for a feature using EARS acceptance criteria. Use when creating specs, writing user stories, defining acceptance criteria.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
skills:
  - spec-creation-contract
  - spec-quality-gates
---

# Create Requirements

Create `requirements.md` for one feature using strict EARS acceptance criteria with full traceability to source FR/UC IDs.

## Output

- `.claude/specs/[feature-name]/requirements.md`
- Update `.claude/specs/[feature-name]/spec-state.json`

## Prerequisites

Project docs must exist:
- `Functional_Requirements.md` (for FR-XXX IDs)
- `Use_Cases.md` (for UC-XXX IDs)
- `PRD.md` (for evidence)

If prerequisites are missing, stop and ask user to create project docs first using `/project-docs`.

---

## Phase 1: Read Context

1. Read project documentation to extract relevant IDs:
   - `Functional_Requirements.md` → extract FR-XXX IDs relevant to [feature-name]
   - `Use_Cases.md` → extract UC-XXX IDs relevant to [feature-name]
   - `PRD.md` → extract key Evidence (market data, KPIs) from Evidence Table
2. Record all extracted FR/UC IDs for traceability

---

## Phase 2: Create Directory

Ensure `.claude/specs/[feature-name]/` exists. Create `spec-state.json` if missing:

```json
{
  "feature": "[feature-name]",
  "project": "[project-name]",
  "mode": "manual",
  "stage": "draft_requirements",
  "created": "[timestamp]",
  "artifacts": {
    "requirements": "pending",
    "design": "pending",
    "tasks": "pending"
  }
}
```

---

## Phase 3: Write Requirements

Create `requirements.md` at `.claude/specs/[feature-name]/requirements.md`.

Reference the template structure from `doc-templates/spec-requirements.md` for section layout.

**Write incrementally** — follow the "Write Incrementally (avoid oversized output)" rule in
`spec-creation-contract`: create the file with the first section, append the rest with `Edit`,
one major section per call. Run the quality gate only after all sections are written.

### Key Rules

- Every requirement has a user story (**As a [role], I want [capability], so that [benefit]**)
- Acceptance criteria are EARS style and testable (WHEN/THEN/IF/SHALL format)
- Include negative/error handling behavior
- IDs stay stable through revisions
- Every requirement MUST have a **Source** field referencing FR-XXX and UC-XXX IDs
- Evidence References section MUST exist with PRD data citations

### Traceability Contract

```
FR/UC → Requirement → Acceptance Criteria → Design section → Task IDs
```

- Every requirement MUST have a **Source** field listing FR-XXX and UC-XXX IDs from project docs
- Every AC MUST be traceable back to its source FR via the requirement's Source field

---

## Phase 4: Quality Gate and Confirmation

1. Run the requirements quality gate: invoke `spec-quality-gates` with gate `gate-requirements`
2. Fix any issues the gate raises
3. Present delivery summary to user:

```text
✅ Created: .claude/specs/[feature-name]/requirements.md

Requirements summary:
- User stories: N
- Acceptance criteria: M
- Source FR/UC IDs: [list]
- Evidence references: [count]

Do the requirements look good?

1. ✅ Approve and continue to design
2. ✏️ Request changes
3. ⏸️ Stop here
```

- **Approve**: set `stage = approved_requirements` in spec-state.json
- **Modify**: revise requirements, re-run quality gate
- **Pause**: keep `stage = draft_requirements`, end session