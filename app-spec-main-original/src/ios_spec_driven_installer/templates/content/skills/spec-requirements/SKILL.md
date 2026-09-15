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

- `{{IDE_CONFIG_DIR}}specs/[feature-name]/requirements.md`
- Update `{{IDE_CONFIG_DIR}}specs/[feature-name]/spec-state.json`

## Prerequisites

Project docs must exist:
- `Functional_Requirements.md` (for FR-XXX IDs)
- `Use_Cases.md` (for UC-XXX IDs)
- `PRD.md` (for evidence)

If prerequisites are missing, stop and ask user to create project docs first using `/project-docs`.

---

## Phase 1: Read Context

1. Read project documentation to extract IDs **and carry forward their depth** (not just IDs):
   - `Functional_Requirements.md` → FR-XXX for [feature-name], **plus each FR's Error Handling (ERR), Validation Rules (VR), Business Rules (BR), §2 bis component behaviors, and §2 ter context variations**
   - `Use_Cases.md` → UC-XXX for [feature-name], **plus each UC's Alternate Flows (AF), Context Variations (first-time/returning/power/offline/error), Sub-Flows, and §4 Screen-Context secondary actions**
   - `Wireframes.md` → the WF-XXX screen(s) this feature owns (from the roadmap Feature→Screen mapping), **and EVERY Component + Interaction + State of those screens** — this is the affordance list the requirements must cover
   - `PRD.md` → key Evidence (market data, KPIs) from Evidence Table
2. Record extracted FR/UC/WF IDs AND build the affordance/context checklist the requirements must satisfy (context variations, alternate flows, sub-flows, and every screen affordance). Flattening a multi-context UC into a single happy-path requirement, or omitting a screen affordance, is a defect.

---

## Phase 2: Create Directory

Ensure `{{IDE_CONFIG_DIR}}specs/[feature-name]/` exists. Create `spec-state.json` if missing:

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

Create `requirements.md` at `{{IDE_CONFIG_DIR}}specs/[feature-name]/requirements.md`.

Reference the template structure from `doc-templates/spec-requirements.md` for section layout.

**Write incrementally** — follow the "Write Incrementally (avoid oversized output)" rule in
`spec-creation-contract`: create the file with the first section, append the rest with `Edit`,
one major section per call. Run the quality gate only after all sections are written.

### Key Rules

- Every requirement has a user story (**As a [role], I want [capability], so that [benefit]**)
- Acceptance criteria are EARS style and testable (WHEN/THEN/IF/SHALL format)
- **States & Edge Cases per requirement:** provide an AC for each applicable state — loading, empty, error, offline/stale, permission-denied — or mark it `N/A — <reason>`. A single error AC is NOT sufficient.
- **Validation Rules:** requirements taking user input enumerate concrete VR-XXX rules (format/range/required); else `N/A — no user input`.
- **Wireframe Affordance Coverage:** every Component and Interaction of the owned WF-XXX screen(s) maps to an AC, or is declared out-of-scope with its owning spec/FR. No silently dropped affordance (settings/share/skip/help/export/edit-field...).
- **Carry-forward:** context variations, alternate flows, and sub-flows from the source UC/FR appear as ACs here — do not flatten to happy-path.
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
✅ Created: {{IDE_CONFIG_DIR}}specs/[feature-name]/requirements.md

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