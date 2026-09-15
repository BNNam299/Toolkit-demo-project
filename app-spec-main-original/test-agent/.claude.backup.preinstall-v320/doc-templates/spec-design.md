# [Feature Name] - Technical Design

## 1. Overview
- Goals
- In-scope / out-of-scope
- **AC Coverage Summary:** List ALL AC-XXX.Y IDs from requirements.md that this design addresses

## 2. Architecture
- Runtime boundaries
- Module responsibilities
- Data flow (Mermaid optional)

## 3. Components and Interfaces
- Views / ViewModels / Services / Repositories
- Public interfaces and contracts
- File plan by component

## 4. Data Models and Contracts
- Entities, DTOs, mapping rules
- Validation constraints

## 5. Error Handling
- Failure modes
- User-visible behavior
- Recovery and retry rules

## 6. Testing Strategy
- Unit tests by component
- Integration test boundaries
- Property-based tests mapped to requirements (see Correctness Properties)
- Build/test checkpoints for each phase

## 7. Feature Breakdown (iOS-first)

**Section Numbering Convention:** Use `7.1`, `7.2`, `7.3` for features. These numbers become **Design Ref** in tasks.

### 7.1 Feature: [Feature Name]
- **ACs Implemented:** [list ACs from requirements - e.g., AC-001.1, AC-001.2]
- **Source:** [FR-XXX, UC-XXX from requirements Source field]
- Wireframe or visual structure
- States: Loading, Empty, Error, Success
- Actions: load, refresh, select, navigate
- Files:
  - `Features/[Name]/Views/[Name]View.swift`
  - `Features/[Name]/ViewModels/[Name]ViewModel.swift`

### 7.2 Feature: [Feature Name]
- **ACs Implemented:** [list ACs from requirements - e.g., AC-002.1, AC-002.2]
- **Source:** [FR-XXX, UC-XXX from requirements Source field]
- States and actions
- Files

<!-- DYNAMIC: Add more feature sections as needed. -->

## 8. Navigation and Integration
- Flow diagram
- Navigation table (from -> to -> trigger -> data)
- Cross-feature data synchronization rules

## 9. Correctness Properties
**IMPORTANT:** Each property MUST reference an AC from requirements.

| Property | Type | Validates AC | Statement |
|---|---|---|---|
| P1 | Invariant | [AC-XXX.Y from requirements] | [testable statement] |
| P2 | Round-trip | [AC-XXX.Y from requirements] | [testable statement] |

<!-- DYNAMIC: Add more properties as needed. -->

<!-- QUALITY-GATE-MANIFEST:START
# SINGLE source of truth for gate-design. Do NOT copy this block into the produced design.md
# under specs/. The gate matches sections by NAME, ignoring leading numbering and any trailing
# placeholder in the produced heading.
doc: Design
gate: gate-design
required_major:
  - "1. Overview"
  - "2. Architecture"
  - "3. Components and Interfaces"
  - "4. Data Models and Contracts"
  - "5. Error Handling"
  - "6. Testing Strategy"
  - "7. Feature Breakdown"
  - "8. Navigation and Integration"
  - "9. Correctness Properties"
required_minor:
  "1. Overview": ["Goals", "In-scope / out-of-scope", "AC Coverage Summary"]
# Feature subsections (7.1, 7.2, …) are DYNAMIC — one per feature — verified via quality_checks.
quality_checks:
  - "AC coverage is COMPLETE (BLOCKING): every AC-XXX.Y in requirements.md appears in design (§1 AC Coverage Summary, §7 ACs Implemented, or §9 Validates AC)"
  - "Every feature subsection (7.X) has an 'ACs Implemented' field and a 'Source' field (FR-XXX, UC-XXX)"
  - "Every correctness property in §9 has a 'Validates AC' value referencing a specific AC-XXX.Y"
  - "Feature section numbering uses stable X.Y format (7.1, 7.2, …) — these become Design Ref in tasks.md"
  - "No production code snippets in the design; Testing Strategy names concrete test files/targets"
  - "Architecture defines runtime boundaries and module responsibilities; Error Handling lists failure modes + user-visible behavior + recovery"
QUALITY-GATE-MANIFEST:END -->