---
name: spec-design
description: Write technical design for features. Use when designing architecture, wireframes, file/folder structure, data flow, state management.
allowed-tools: Read, Write, Edit, Grep, Glob
skills:
  - spec-creation-contract
  - ios-architecture
  - ios-components
  - ios-ui-ux
  - spec-quality-gates
---

# Create Design

Create `design.md` from approved requirements with explicit implementation boundaries and traceable design decisions.

## Output

- `{{IDE_CONFIG_DIR}}specs/[feature-name]/design.md`
- Update `{{IDE_CONFIG_DIR}}specs/[feature-name]/spec-state.json`

## Prerequisites

- `requirements.md` exists and is valid
- `spec-state.json` has `stage = approved_requirements`

If prerequisites fail, stop and ask user to complete requirements approval first.

---

## Phase 1: Read Context

1. Read `requirements.md` to extract all AC-XXX.Y IDs
2. Read project docs for architecture context (Project_Overview.md, Functional_Requirements.md)
3. Determine implementation intent:
   - Ask user: "Do you prefer logic-first, UI-first, or hybrid approach?"
   - Logic-first: start with domain models, services, then wire to UI
   - UI-first: start with screens and flows, then implement supporting logic
   - Hybrid: interleave based on feature complexity

---

## Phase 2: Write Design

Create `design.md` at `{{IDE_CONFIG_DIR}}specs/[feature-name]/design.md`.

Reference the template structure from `doc-templates/spec-design.md` for section layout.

**Write incrementally** — follow the "Write Incrementally (avoid oversized output)" rule in
`spec-creation-contract`: create the file with §1, append later sections with `Edit`, and append
the Feature Breakdown **one `7.X` block at a time**. Run the quality gate only after all sections
are written.

Set `stage = draft_design` in spec-state.json.

### Key Rules

- **AC Coverage (MANDATORY)**:
  - Section 1: List ALL AC-XXX.Y IDs that this design implements
  - Section 7: Each feature MUST have **ACs Implemented** field listing specific AC IDs
  - Section 9: Each property MUST have **Validates AC** column referencing specific AC
  - No feature may be marked complete without AC coverage
- **Section Numbering Convention**: Use `X.Y` format (7.1, 7.2, etc.) — these become Design Ref in tasks.md
- **Traceability**: Every AC from requirements.md must appear in at least one design feature section
- No production code snippets in design
- Every key decision references one or more ACs
- Testing strategy must mention concrete test files/targets

### iOS Implementation Depth Rules

- Prefer SwiftUI + MVVM unless requirement says otherwise
- **Bake the execution gates into the design so tasks inherit the decisions:**
  - **Reuse Plan** — for each screen/component, state reuse-vs-create up front (which `shared/Components/`
    to reuse/parameterize/compose, or a justified new component). Feeds the `ios-components` Reuse-First Gate.
  - **Structure-compliant file plan** — every file path in §3/§7 must map to the `ios-architecture`
    canonical tree (`Features/[Feature]/{Views,ViewModels,Models,Services}/`, `shared/Components/[Type]/`).
  - **UX expectations** — note the 4 states + a11y/dark-mode expectations per screen so the
    `ios-ui-ux` UX Compliance Gate is satisfiable at execution time.
- Include component reuse plan before proposing new UI components
- Include accessibility expectations for core views (labels, dynamic type, contrast targets)
- If Figma is available, note token/component mapping expectations for execution phase
- Reference `ios-architecture` skill for file/folder structure conventions
- Reference `ios-components` skill for reusable component patterns

---

## Phase 3: AC Coverage Validation

**BEFORE showing approval prompt, validate AC coverage:**

1. Read `requirements.md` and extract ALL AC-XXX.Y IDs
2. Read `design.md` and extract ALL AC-XXX.Y IDs from:
   - Section 1: AC Coverage Summary
   - Section 7: **ACs Implemented** fields
   - Section 9: **Validates AC** column
3. Compare: Every AC from requirements MUST appear in design
4. If any AC is missing → **BLOCK approval** with error

```text
AC Coverage Check:
- Requirements ACs: [list from requirements.md]
- Design ACs: [list from design.md]
- Missing ACs: [list any missing]
```

If coverage is incomplete:
```text
❌ Cannot approve design - missing AC coverage:
- [AC-XXX.Y from requirements] is NOT referenced in design
Fix required: Add [AC-XXX.Y] to Feature [7.X] section
```

---

## Phase 4: Quality Gate and Confirmation

1. Run the design quality gate: invoke `spec-quality-gates` with gate `gate-design`
2. Fix any issues the gate raises
3. Present delivery summary to user:

```text
✅ Created: {{IDE_CONFIG_DIR}}specs/[feature-name]/design.md

Design summary:
- Architecture decisions: X
- Components: Y
- AC Coverage: [complete/incomplete]
- Feature sections: Z

AC Coverage Check:
- Requirements ACs: [list]
- Design ACs: [list]
- Missing ACs: [none or list]

Does the design look good?

1. ✅ Approve and continue to tasks (only if AC coverage complete)
2. ✏️ Request changes
3. ⏸️ Stop here
```

- **Approve**: set `stage = approved_design` in spec-state.json
- **Approve but AC incomplete**: BLOCK — require fixes first
- **Modify**: revise design, keep `stage = draft_design`, re-run gate