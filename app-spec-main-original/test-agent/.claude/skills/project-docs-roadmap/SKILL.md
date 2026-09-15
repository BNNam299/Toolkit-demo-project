---
name: project-docs-roadmap
description: Create Project_Implementation_Roadmap.md with spec breakdown, dependency analysis, and phase planning. Use when planning implementation phases, breaking features into specs, ordering dependencies.
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
---

# Required Skills & Files

Before executing this skill, you MUST read these files:

1. `.claude/doc-templates/Project_Implementation_Roadmap.md` — Roadmap template
2. `.claude/skills/project-docs-lifecycle/SKILL.md` — Lifecycle (dir setup, file safety, user confirmation)
3. `.claude/skills/project-docs-contract/SKILL.md` — Workflow contract (scaling, sub-spec rules)
4. `.claude/skills/project-docs-quality-gates/SKILL.md` — Quality gate skill

## Non-Negotiable Rules

- `project-structure` section: directories and filenames ONLY. Zero code.
- **Feature spec = vertical slice of MULTIPLE screens.** Mỗi feature spec phải list tất cả WF-XXX screens nó cover. No feature spec without screen mapping.
- **Every WF-XXX screen must map to exactly one feature spec.** Orphan screen = quality gate failure.
- Sub-spec splitting: MANDATORY at >5 FRs per section. Split by sub-feature, not by layer.
- Phase count: follow `project-docs-contract` scaling guidance (1-2 small, 2-4 medium, 4+ large).
- Traceability matrix MUST be complete: every FR, UC, and WF mapped to a spec and file.
- Every FR/UC/WF MUST be covered by at least one file in the File Breakdown. Zero orphans.
- File Breakdown MUST use real project paths and real function/component names. No placeholders like "function1()".
- Functions/components in each file MUST be meaningful — not "function1()" but "validateEmail(), loginUser()".
- MUST NOT include Python pseudocode — use declarative dependency rules only.
- Write files only under `.claude/specs/[project-name]/`.

# Project Implementation Roadmap Creator

## When to Use

- All seven upstream project docs are approved (PRD → UX Flows)
- Need to break features into implementation specs and assign to phases
- Need topological ordering of specs based on dependencies

## Objective

Create `Project_Implementation_Roadmap.md` that breaks features into specs, analyzes dependencies, and assigns specs to implementation phases with topological ordering.

## Prerequisites

All previous project docs must exist in `.claude/specs/[project-name]/`:
- `PRD.md`
- `Project_Overview.md`
- `Use_Cases.md`
- `Functional_Requirements.md`
- `Wireframes.md`
- `UX_Flows.md`

---

## Workflow

### Step 0: Read Screen Inventory from Use_Cases.md

Before planning, extract the full screen inventory from upstream docs. This ensures every screen (WF-XXX) is assigned to exactly one feature spec — no orphans.

#### 0.1 Extract Screen Architecture Canvas

Read `Use_Cases.md` §0.3 Screen Architecture Canvas. Extract:

- All WF-XXX IDs and their screen names
- Screen hierarchy (parent screens, child screens, modals, system screens)
- Archetype per screen (Discovery / Action / Consumption / Management / Social)

#### 0.2 Extract Screen-Context Details

Read `Use_Cases.md` §4 Screen-Context Use Cases. For each screen:

- Interaction Density (Dense / Medium / Light)
- Primary Action
- Source UCs (which UC-XXX IDs are served by this screen)
- Entry / Exit points

#### 0.3 Extract FR Section Grouping

Read `Functional_Requirements.md` §2 and §2 ter. Map FR sections to feature groups:

| FR Section | FR IDs | Feature Group | Feature Spec Candidate |
|------------|--------|---------------|----------------------|
| §2.1 [Name] | FR-XXX–FR-XXX | [Auth / Home / etc.] | feature-[name] |
| §2.2 [Name] | FR-XXX–FR-XXX | [Next group] | feature-[next] |

#### 0.4 Build Feature→Screen Candidate Map

Cross-reference FR sections with Use_Cases.md §3 UC → Screen Mapping. For each FR section, determine which WF-XXX screens its UCs touch:

```
[FR Section Name] → [UC-XXX, UC-XXX] → [WF-XXX, WF-XXX]
[Next section]    → [UC-XXX]         → [WF-XXX, WF-XXX, WF-XXX]
```

**Output:** A preliminary Feature→Screen mapping table that will be finalized in Step 3.

#### 0.5 Screen Ownership Verification

Verify every WF-XXX from the Screen Architecture Canvas appears in at least one feature's screen list. Any screen not yet assigned:

- Does it belong to an existing feature? Assign it.
- Is it a shared/system screen (Splash, Onboarding)? Keep it unassigned — infra handles it.

**Rule:** Leave Step 0 with zero orphan screens. Every WF-XXX must map to a feature or explicitly to infra.

### Step 1: Read Context

Read all previous project docs in order:

- `PRD.md` — product vision, goals, target market
- `Project_Overview.md` — architecture, tech stack, design system
- `Use_Cases.md` — user scenarios and flows (with screen inventory from §0.3)
- `Functional_Requirements.md` — FR sections and acceptance criteria
- `Wireframes.md` — screen layouts and component inventory
- `UX_Flows.md` — navigation and interaction patterns

### Step 2: Create Directory

Ensure the project docs directory exists: `.claude/specs/[project-name]/`. Create it with `mkdir -p` if missing.

### Step 3: Build Spec List with Sub-Spec Splitting

Map FR sections to specs. Apply these rules:

- **Each FR section = one feature spec.** The spec includes data layer + service + viewmodel + view for all its screens.
- **FR sections with >5 requirements MUST be split into sub-specs** — split by sub-feature, NOT by layer. Example: `Auth` (>5 FRs) → `Auth-Login`, `Auth-SignUp`, `Auth-PasswordReset` (each still a vertical slice with model/service/viewmodel/view).
- Sub-spec naming: `[FeatureGroup]-[SubFeature]` (e.g., `Auth-Login`, `Auth-SignUp`).
- Always include shared infrastructure specs: `project-structure`, `shared-foundations`.
- Infrastructure specs (project-structure, shared-foundations) do NOT own screens.
- **Max 3 specs per phase.**
- Phase count follows `project-docs-contract` scaling guidance: 1-2 (small), 2-4 (medium), 4+ (large). Scale by domain complexity, not just feature count.
- Each feature spec MUST list all WF-XXX screens it covers. Source from Step 0.4 candidate map.
- Every WF-XXX must belong to exactly one feature spec. Orphan screens = quality gate failure.

### Step 3b: File-Level Breakdown per Spec

For every spec in the list, enumerate every file that will be created. Each file entry MUST include:

- **File path** — relative to project root (e.g., `Features/Auth/Models/User.swift`)
- **Key functions/classes** — what public symbols will exist in that file
- **Covers** — which FR-XXX, UC-XXX, WF-XXX this file satisfies
- **Screens** — which WF-XXX screen(s) this file implements

Rules:
- Every FR must appear in at least one file's "Covers".
- Every UC must appear in at least one file's "Covers".
- Every WF must appear in at least one file's "Covers".
- A file can cover multiple FRs/UCs/WFs if they are related.
- If a FR/UC/WF has zero files assigned → flag as **GAP** in the roadmap.
- File paths MUST use the actual project directory structure from `Project_Overview.md`.
- A feature spec with multiple screens MUST have at least one View file per screen (WF-XXX).

Format for each spec:
```
Spec: [spec-id]
Screens: [WF-XXX: Name, WF-XXX: Name]
Files:
  [path-to-model.swift]
    Functions: [function1(), function2(), ...]
    Covers: FR-XXX, UC-XXX
  [path-to-service.swift]
    Functions: [function1(), function2(), ...]
    Covers: FR-XXX
  [path-to-viewmodel.swift]
    Functions: [function1(), function2(), ...]
    Covers: FR-XXX
  [path-to-view.swift]
    Components: [ComponentName1, ComponentName2]
    Covers: FR-XXX, UC-XXX, WF-XXX
  [path-to-view2.swift]
    Components: [ComponentName1, ComponentName2]
    Covers: FR-XXX, UC-XXX, WF-XXX
```

### Step 3c: Screen-to-File Cross-Reference

After the file breakdown, build a screen-to-file cross-reference to ensure every screen has implementing files:

```
Spec: [spec-id]
Screens: [WF-XXX: Name, WF-XXX: Name]
Screen→File:
  WF-XXX → [path-to-view.swift], [path-to-viewmodel.swift]
  WF-XXX → [path-to-view2.swift]
```

**Rule:** Every WF-XXX in the spec's screen list must have ≥1 View file. If a screen has zero View files, it is unimplemented — flag as GAP.

### Step 4: Dependency Analysis

Apply these seven dependency rules in order:

1. **Infrastructure before features** — `shared/` directory and core modules must exist before feature code.
2. **Module before screen** — data layer before UI layer for any given feature.
3. **API contract before consumer** — backend models/interfaces before frontend consumers.
4. **Shared components before feature screens** — reusable UI components before feature-specific screens.
5. **Parent flow before child** — main navigation and list screens before detail screens.
6. **Cross-feature dependencies** — auth must precede any protected screen; session tokens before API calls.
7. **Feature ordering by user-facing priority** — core features (auth, onboarding) before secondary features (settings, profile). Product Owner decides, not engineering.

### Step 5: Phase Assignment

- Assign specs to phases using topological order derived from the dependency graph.
- Phase 1: `project-structure` (always first).
- Phase 2: `shared-foundations` (always second — blocks all feature specs).
- Phase 3+: feature specs ordered by priority and dependency.
- Each phase = **1 to 3 days** of work.
- No phase may contain more than 3 specs.

### Step 6: Write the Roadmap

Use the template at `.claude/doc-templates/Project_Implementation_Roadmap.md`. The
authoritative list of required sections (mục lớn + mục con) is its `QUALITY-GATE-MANIFEST`
block — reproduce those sections and do NOT copy the manifest block into the output.
`gate-roadmap` validates against that manifest. The notes below explain what to put in each section:

- **Scope Decision Record** — the single source of truth for scope. Fill the priority legend, the explicit MVP definition (list UC/FR IDs or "all N"), and any Scope Promotions. Every UC/FR priority label (Use_Cases §7, Functional_Requirements §1.3, Project_Overview §4) MUST agree with this record; a phase is MVP only if all UC/FR it covers are Tier 1 (or promoted here with a reason). A recovery/critical-path UC of an MVP flow must be Tier 1.
- **Project Structure** — dedicated block listing directories and files for the scaffold. Zero code, zero logic. File paths and names only.
- **Phase Timeline** — phases with specs, duration estimates, entry criteria, deliverables, exit criteria.
- **Feature→Screen Mapping** — table mapping each feature spec to its WF-XXX screens (from Step 0.4).
- **Spec Registry** — every spec with source FR section, assigned phase, screen list, and traceability.
- **File Breakdown** — table listing all files with their FR/UC/WF references.
- **Screen→File Breakdown** — per-phase, per-screen file listing (from Step 3c).
- **JSON Dependencies block** — machine-readable for `/ios-spec` workflow consumption. Every spec must appear.
- **Dependency Graph** — Mermaid diagram showing spec ordering.
- **Traceability Matrix** — three mappings:
  - FR → Spec → File — each FR mapped to a spec and the specific file implementing it
  - UC → Spec → Screen (WF) — each UC mapped to a spec and its corresponding WF screen
  - WF → Spec → Component — each WF mapped to a spec and its specific component/view
  - GAP Report — list of FR/UC/WF with no file covering them
- **GAP Analysis** — FR/UC/WF with no file assigned
- **Next Spec Recommendation** — which spec to start first.

**CRITICAL: The project-structure section must be a standalone block listing directories and files ONLY. Not embedded in tables — its own `##` section.**

**CRITICAL: File paths in the File Breakdown MUST use the actual project directory structure from Project_Overview.md (e.g., `Features/Auth/ViewModels/LoginViewModel.swift`), not generic names.**

**CRITICAL: Every feature spec must list its screens. Every screen must appear in exactly one feature spec. Orphan screens fail the quality gate.**

### Step 7: Quality Gate and Confirmation

1. Run the `project-docs-quality-gates` skill with gate name `gate-roadmap`.
2. Per `project-docs-lifecycle`, get user confirmation before marking the roadmap as complete.

---

## Quality Gates

| Gate | Skill | Pass Criteria |
|------|-------|---------------|
| `gate-roadmap` | `project-docs-quality-gates` | Every FR/UC/WF → spec → file; no orphans; project-structure has no code; sub-spec split applied at >5 FRs; every WF-XXX maps to exactly one feature spec; every spec lists its screens |

---

## Error Handling

- **Missing upstream doc**: stop. Direct user to complete the missing step before roadmap.
- **Orphan FR/UC/WF in traceability matrix**: add to file breakdown or flag as GAP.
- **Orphan screen (WF-XXX not assigned to any spec)**: investigate. Assign to the correct feature spec or flag as unplanned screen.
- **Phase with >3 specs**: split into multiple phases.
- **Code in project-structure section**: strip code, keep paths only.
- **Feature spec missing screen list**: cross-reference from Step 0.4. Every spec must list ≥1 screen.
- **Quality gate failure**: revise, re-run gate.

---

## Output Contract

- File: `.claude/specs/[project-name]/Project_Implementation_Roadmap.md`
- Sections: Project Structure, Phase Timeline, Feature→Screen Mapping, Spec Registry, File Breakdown, Screen→File Breakdown, JSON Dependencies, Dependency Graph, Traceability Matrix (3 mappings), GAP Analysis, Next Spec Recommendation
- All FR/UC/WF covered by at least one file
- Every WF-XXX maps to exactly one feature spec
- File Breakdown uses real project paths from Project_Overview.md
