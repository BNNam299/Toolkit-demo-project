---
name: project-docs-fr
description: Create Functional_Requirements.md with detailed system behavior specs. Use when defining features, specifying requirements, documenting system behavior.
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
---

# Required Skills & Files

Before executing this skill, you MUST read these files:

1. `.claude/doc-templates/Functional_Requirements.md` — Functional Requirements template
2. `.claude/skills/project-docs-lifecycle/SKILL.md` — Lifecycle (dir setup, file safety, user confirmation)
3. `.claude/skills/project-docs-contract/SKILL.md` — Workflow contract (sub-spec splitting rule)
4. `.claude/skills/project-docs-quality-gates/SKILL.md` — Quality gate skill
5. `.claude/skills/ios-architecture/SKILL.md` — iOS platform constraints (when iOS)
6. `.claude/specs/[project-name]/PRD.md` — PRD (REQUIRED; stop if missing)
7. `.claude/specs/[project-name]/Use_Cases.md` — Use Cases (REQUIRED; stop if missing)
8. `.claude/specs/[project-name]/Project_Overview.md` — Project Overview (REQUIRED; stop if missing — provides architecture context: tech stack, design system, platform constraints)

## Non-Negotiable Rules

- **Read PRD + Overview + UC first.** No FR creation without all three prerequisites. Overview provides architecture context (tech stack, design system, platform constraints) needed for NFR design.
- **Every FR traces to a UC.** Orphan FRs fail the quality gate. Period.
- **Derive, don't invent.** Every FR field must come from a specific UC field (see Step 2 protocol). No FR content without UC source.
- **Carry forward ACs verbatim.** Do not rewrite UC acceptance criteria. If untestable, flag — don't fix silently.
- **Measurable NFRs.** Numbers, percentages, milliseconds. No vague targets.
- **No placeholders.** TBD, TODO, blank sections fail the quality gate.
- **Stable IDs.** FR-XXX, NFR-XXX, BR-XXX.Y, VR-XXX.Y, ERR-XXX.Y, AC-XXX.Y.
- **File safety.** Write only under `.claude/specs/[project-name]/`.
- **iOS awareness.** Reference `ios-architecture` for platform constraints (SwiftUI limits, iOS version support, device capabilities).
- **FR count ≥ UC count.** Each UC produces at least one FR. Complex UCs produce multiple FRs.
- **Context-dependent behaviors derived from UC Context Variations.** Every High-priority UC's context variations must become rows in FR §2 ter.
- **Component behaviors derived from UC Feature Expression Matrix.** Every multi-screen UC expression must become rows in FR §2 bis.

# Create Functional_Requirements.md

## When to Use

- PRD and Use_Cases.md are approved
- Need to specify WHAT the system must do (system behavior, not implementation)
- This document bridges user needs (Use_Cases.md) to technical implementation (Design specs)

## Objective

Create `Functional_Requirements.md` at `.claude/specs/[project-name]/Functional_Requirements.md`, specifying WHAT the system must do. This document bridges user needs (Use_Cases.md) to technical implementation (Design specs).

Every FR must trace to a UC. Every UC must be covered by at least one FR. This is the central traceability contract — broken traces fail the quality gate.

## Prerequisites

- `.claude/specs/[project-name]/PRD.md` exists and is approved
- `.claude/specs/[project-name]/Use_Cases.md` exists and is approved
- (For iOS apps) `ios-architecture` skill loaded for platform constraints

---

## Workflow

### Step 1: Read Context

1. Read `Project_Overview.md` for architecture context (tech stack, design system, platform constraints). Required for NFR design.
2. Read `PRD.md` and `Use_Cases.md`. Then map UC sections to FR sections explicitly:

#### 1.1 UC → FR Source Mapping

| From Use_Cases.md | Extract | Becomes in FR |
|---|---|---|
| **§2 User Stories** — each UC entry | UC ID, actor, goal, main flow, alternative flows, acceptance criteria (AC-IDs) | FR-XXX Description, Input, Processing, Output, Error Handling. One FR per UC minimum. |
| **§2 per-UC: Preconditions** | Conditions that must be true before UC executes | FR Business Rules (BR-XXX.Y) — conditions enforced by system |
| **§2 per-UC: Main Flow steps** | Step-by-step user+system interaction | FR Processing steps (1:1 mapping from UC flow steps) |
| **§2 per-UC: Alternative Flows (AF-XXX.Y)** | Error scenarios, alternative paths | FR Error Handling (ERR-XXX.Y) — each AF becomes one error scenario |
| **§2 per-UC: Acceptance Criteria (AC-XXX.Y)** | Testable conditions | FR Acceptance Criteria — carry forward verbatim, do not rewrite |
| **§2 per-UC: Context Variations** (first-time/returning/power user) | How behavior changes per user state | FR §2 ter Context-Dependent Behaviors — one row per context variation |
| **§2 bis Feature Expression Matrix** | UC expressed differently per screen | FR §2 bis Component Behavior Matrix — one row per expression |
| **§4 Screen-Context Use Cases** | Per-screen: entry/exit, primary action, state variations | FR Input/Output: entry screen = input context, exit screen = output destination. State variations → Error Handling |
| **§5 Task Flows** | Cross-screen journeys with decision points and recovery paths | FR Error Handling + Validation Rules — each decision point with recovery becomes ERR or VR |
| **§5 bis Sub-Flows** | Within-screen micro-interactions | FR Processing detail — sub-flow steps refine main flow steps |
| **PRD §5 MVP scope** | Priority (P0/P1/P2) | FR Priority field |
| **PRD §7 Technical Specs** | Platform, architecture, third-party services | NFR §3 — performance targets, security requirements, platform constraints |

#### 1.2 Coverage Verification (BEFORE writing a single FR)

Before writing, verify coverage by creating a checklist:

```
UC-XXX → FR-XXX (will write)
UC-XXX → FR-XXX (will write)
...
Total UCs in Use_Cases.md §2: [N]
Total FRs planned: [M] — must be ≥ N (each UC → ≥1 FR)
```

If any UC has no planned FR, go back to the UC and extract what the system must do. Complex UCs (many steps, many alternative flows) should produce 2-3 FRs each.

### Step 2: Derive FR Content from UC (Field-by-Field Protocol)

For each UC, derive the FR using this exact protocol. Do not invent content — extract from UC.

#### FR Description
**Source**: UC goal + UC name
**Format**: "System shall [UC goal from 'I want to...' statement]"

#### FR Priority
**Source**: UC Priority field (High = P0, Medium = P1, Low = P2)
**Do not override**: If UC says High, FR says High. Priority changes require upstream UC change.

#### FR Input
**Source**: UC Preconditions + UC Entry Point
**Format**: List each precondition as a required input. Include data type and constraints if specified in UC.

#### FR Processing
**Source**: UC Main Flow steps (all steps, 1:1)
**Rule**: Each UC main flow step becomes one Processing step. Do not merge steps. Do not add steps not in the UC.
**Refinement**: If UC §5 bis Sub-Flows exist for this UC's primary screen, incorporate sub-flow detail into the relevant processing step.

#### FR Output
**Source**: UC Postconditions + UC Exit Point
**Format**: List expected system state after completion. Reference the exit screen (WF-XXX).

#### FR Business Rules (BR-XXX.Y)
**Source**: UC Preconditions + UC Acceptance Criteria that reference system constraints
**Derivation**: Each precondition that the SYSTEM must enforce (not user action) becomes a BR. Example: "User must be logged in" → BR-XXX.1: Authentication required.

#### FR Validation Rules (VR-XXX.Y)
**Source**: UC Acceptance Criteria that reference data validation
**Derivation**: Each AC about input format, range, or required fields. Example: "WHEN email is entered THEN format is validated" → VR-XXX.1: Email format validation.

#### FR Error Handling (ERR-XXX.Y)
**Source**: UC Alternative Flows (AF-XXX.Y)
**Derivation**: Each AF becomes one ERR entry. Include: error condition (from AF trigger), error message (from AF description), recovery action (from AF system behavior).
**Also source from**: §5 Task Flow Recovery Paths — every recovery path adds context to error handling.

#### FR Acceptance Criteria (AC-XXX.Y)
**Source**: UC Acceptance Criteria
**Rule**: Carry forward verbatim. Do not rewrite. Do not add. If the UC AC is testable, use it. If it is not testable, flag it and ask user to refine the UC first.

### Step 3: Build FR §2 bis — Component Behavior Matrix

**Source**: Use_Cases.md §2 bis Feature Expression Matrix

For each row in the UC Feature Expression Matrix where a UC is expressed on multiple screens:

1. Create one row in the FR Component Behavior Matrix
2. Map UC Expression Type → FR Component (e.g., "Full CTA" → BtnPrimary, "Swipe Action" → SwipeAction)
3. Document what changes per screen: component used, input required, validation rules applied, output behavior

**Rule**: Only create FR Component Behavior rows for UCs that appear on ≥2 screens. Single-screen UCs skip this section.

### Step 4: Build FR §2 ter — Context-Dependent Behaviors

**Source**: Use_Cases.md §2 per-UC Context Variations

For each UC's context variations (first-time user, returning user, power user/edge case):

1. Create one row per context variation
2. **Context**: First Visit / Returning / Power User / Offline / Error
3. **Trigger**: What condition activates this context (from UC Context Variation description)
4. **Behavior Change**: WHAT the system does differently — must be concrete (component change, flow change, data change). Not "better UX" — specify which component, which flow step.

**Rule**: Every High-priority UC must have ≥2 context-dependent behavior rows derived from its UC Context Variations.

### Step 5: Write Functional_Requirements.md

Reference the template structure from `.claude/doc-templates/Functional_Requirements.md` for section layout. Its `QUALITY-GATE-MANIFEST` (end of template) is the authoritative list of required sections — reproduce them, do NOT copy the manifest block into the output. `gate-fr` validates against that manifest.

#### ID Format

- `FR-XXX` for functional requirements
- `NFR-XXX` for non-functional requirements
- `BR-XXX.Y` for business rules
- `VR-XXX.Y` for validation rules
- `ERR-XXX.Y` for error scenarios
- `AC-XXX.Y` for acceptance criteria (carried forward from UC, not renumbered)

Once assigned, IDs never change. New items get new IDs, no renumbering.

#### Non-Functional Requirements

**Core (all projects)**: Performance (app launch, API response), Security (data protection, encryption).

**Additional by app type**:
- Fitness/Health: HIPAA compliance, HealthKit integration, offline sync
- Fintech: PCI compliance, biometric auth, audit logging
- Social: Content moderation, rate limiting, media processing
- SaaS: Multi-tenancy, RBAC, API rate limits

Every NFR must be measurable. Reject "fast", "secure", "reliable". Require numbers.

#### Scaling

| Project Size | Features | Sections | FR Count |
|---|---|---|---|
| Small | < 5 | 1-2 | 5-15 |
| Medium | 5-10 | 3-4 | 15-35 |
| Large | 10+ | 5+ | 35+ |

> **Scope note:** These counts are **floors** for minimum viable FR. Production-quality targets are defined in `project-docs-contract` (typically 2-3× higher). When using these floor counts, document the trade-off (e.g., deferred edge-case FRs) so downstream docs know which FRs are intentionally out of scope.

FR count scales with UC count, not feature count. A project with 20 UCs produces ≥20 FRs.

#### Sub-Spec Rule

Per `project-docs-contract` Sub-Spec Splitting: any FR section with >5 requirements must be split into a dedicated sub-spec file (e.g., `FR_auth.md`). The main file becomes an index linking to sub-specs. IDs stay globally unique across all files.

### Step 6: Traceability Verification (AFTER writing)

After writing all FRs, verify the bidirectional trace:

1. **Forward check**: Every UC in Use_Cases.md §2 has Source UC: field in at least one FR → list any missing
2. **Backward check**: Every FR has a valid UC-XXX in its Source UC field → list any orphans
3. **Context check**: Every FR's ERR-XXX.Y entries correspond to an AF-XXX.Y in the UC → list mismatches
4. **AC carry-forward check**: Every AC-XXX.Y in the FR matches the AC-XXX.Y in the UC verbatim → list rewrites

Output the verification summary as a checklist at the top of Functional_Requirements.md (or in a traceability appendix).

### Step 7: Quality Gate and Confirmation

1. Invoke `project-docs-quality-gates` with gate `gate-fr`
2. Fix any issues the gate raises
3. Follow `project-docs-lifecycle` Phase 4: present delivery summary, ask user to approve, modify, or pause

---

## Quality Gates

| Gate | Skill | Pass Criteria |
|------|-------|---------------|
| `gate-fr` | `project-docs-quality-gates` | Every FR → UC; FR count ≥ UC count; ACs carried forward verbatim; measurable NFRs; no placeholders; bidirectional trace verified |

---

## Error Handling

- **Missing PRD or Use_Cases.md**: stop. Direct user to complete prerequisites first.
- **FR with no UC source**: re-trace or remove. Orphan FRs fail gate.
- **AC rewritten (not verbatim)**: revert. Flag untestable ACs back to UC author instead.
- **NFR without measurable target**: ask user. Reject "fast", "secure", "reliable".
- **FR section >5 requirements not split**: apply sub-spec rule, create separate file.
- **Quality gate failure**: revise, re-run gate.

---

## Output Contract

- File: `.claude/specs/[project-name]/Functional_Requirements.md`
- Plus sub-spec files (`FR_[topic].md`) when FR section >5 requirements
- IDs: FR-XXX, NFR-XXX, BR-XXX.Y, VR-XXX.Y, ERR-XXX.Y, AC-XXX.Y (stable, never renumbered)
- Every FR has a Source UC field
- ACs carried forward verbatim from UC
- NFRs with measurable targets (numbers, percentages, milliseconds)
- Traceability summary at top or appendix
