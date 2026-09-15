---
name: spec-quality-gates
description: Unified quality gates for feature spec types (requirements, design, tasks). Use when creating or reviewing specs to enforce completeness, traceability, and AC coverage before approval. Section requirements are read from each template's QUALITY-GATE-MANIFEST, never hard-coded here.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Required Skills & Files

Before executing this skill, you MUST read these files:

- `.claude/skills/spec-creation-contract/SKILL.md` — Spec workflow contract (stage model, traceability, file contracts)
- The `QUALITY-GATE-MANIFEST` block of the template being checked (see mapping table below) — this is the SOURCE OF TRUTH for required sections.

## Non-Negotiable Rules

- Every gate MUST be a pass/fail check, not a style preference.
- Every gate failure MUST list concrete fix requests. Do NOT mark a spec ready until all categories pass.
- **Do NOT hard-code the list of required sections in this skill.** The required sections and
  doc-specific quality checks are READ AT CHECK TIME from the template's `QUALITY-GATE-MANIFEST`
  block. This skill only defines the *procedure*, not the section lists.
- Gate IDs are stable identifiers. They map 1:1 to per-spec skills and to a template:
  - Requirements → `gate-requirements` → `doc-templates/spec-requirements.md`
  - Design → `gate-design` → `doc-templates/spec-design.md`
  - Tasks → `gate-tasks` → `doc-templates/spec-tasks.md`
- Per-spec skills MUST invoke the corresponding gate ID after writing the spec.
- File safety: every output path is under `.claude/specs/[feature-name]/`.

# Spec Quality Gates

## When to Use

- After a per-spec skill writes a spec file (Phase 4 of `spec-requirements`/`spec-design`/`spec-tasks`)
- Before declaring any spec ready for approval
- During spec refinement to re-validate a patched spec
- When the user explicitly requests a spec quality check

## Objective

Enforce minimum quality for each feature spec. Each gate is a pass/fail check. A failing gate
lists concrete fix requests and blocks progression. "Required sections" is **recalled from the
template's manifest**, so the template is the single source of truth and never drifts from the gate.

---

## Template-Driven Gate Procedure (all 3 spec gates)

`gate-requirements`, `gate-design`, and `gate-tasks` ALL run the same procedure below. The only
thing that differs per gate is which template it reads and which universal rules apply.

### Step 1 — Resolve the template
From the gate ID, pick the template file from the mapping table in Non-Negotiable Rules
(e.g. `gate-design` → `.claude/doc-templates/spec-design.md`).

### Step 2 — Recall required sections from the manifest
Read the template file and extract the YAML between the markers:

```
<!-- QUALITY-GATE-MANIFEST:START
... yaml ...
QUALITY-GATE-MANIFEST:END -->
```

From it, load:
- `required_major` — top-level sections. ALL must be present.
- `required_minor` — for each major, the sub-sections. ALL must be present.
- `quality_checks` — spec-specific content rules (traceability fields, AC coverage, measurability, …).

Every section listed in the manifest is **mandatory** — the manifest has no optional tier. The
only headings NOT listed are placeholder/example patterns (`[...]`, `XXX`, `.N`, per-requirement
blocks, per-feature `7.X` subsections, per-task rows), which are fill-in patterns, not fixed sections.

If the template has no manifest block, STOP and report a Blocker
("template missing QUALITY-GATE-MANIFEST") — do NOT fall back to guessing sections.

### Step 3 — Read the produced spec
Read `.claude/specs/[feature-name]/<spec>.md` and collect all its headings.

### Step 4 — Structure check (major + minor)
- **Major:** every `required_major` name must appear as a heading. Match by name, **ignoring
  leading numbering** (`1.`, `7.`) and any trailing placeholder/param in the produced heading.
  Each missing major → Fail, list it by name.
- **Minor:** for every major, every name in its `required_minor` list must appear as a
  sub-heading under that major. Each missing minor → Fail, list as `major → minor`.
- There are no optional sections: every section in the manifest is mandatory.

### Step 5 — Content check (each required section substantively filled)
Every required section must be **substantively filled**, not just present as a heading. Fail if a
required section is empty, is only a heading, or still contains unresolved placeholders: `[...]`
bracket tokens, `XXX`, `.N`, or `TBD`. (Ignore GitHub-style checkbox `- [ ]` — that is legitimate
in tasks.md.)

### Step 6 — Quality checks (per-file hints from manifest)
`quality_checks` in the manifest are **hints that tell you what to verify inside each file** —
including per-requirement, per-feature, and per-task content the manifest does NOT enumerate as
fixed sections. Do NOT treat them as a rigid section list; for each hint, inspect the produced
spec and decide Pass/Fail, then list any that fail.

### Step 7 — Universal rules (cross-spec, defined here)
Always apply, regardless of manifest:
1. **Traceability chain** — `FR/UC → Requirement → AC → Design section → Task` must link forward
   and backward. No requirement without a Source; no task without an AC + design ref.
2. **Stable IDs** — consistent identifiers (`REQ-XXX`, `AC-XXX.Y`, task IDs, design section `7.X`)
   chained across requirements → design → tasks.
3. **Testable language** — reject "fast", "user-friendly", "secure" on critical items; require
   quantified alternatives.
4. **File safety** — the file is under `.claude/specs/[feature-name]/`.
5. **AC Coverage Validation (BLOCKING — gate-design only).** Before a design can pass:
   - Extract ALL `AC-XXX.Y` IDs from `requirements.md`.
   - Extract ALL `AC-XXX.Y` IDs from `design.md` (§1 AC Coverage Summary, §7 ACs Implemented, §9 Validates AC).
   - Every requirement AC MUST appear in the design. **If any AC is missing → BLOCK approval**,
     list each missing AC and the feature section it should be added to.
6. **Design Ref match (gate-tasks only).** Every task's `Refs Design` value must match an exact
   section number present in `design.md`. A dangling or mismatched design ref = Fail.
7. **WF reference resolution (cross-doc).** Every `WF-XXX` cited in requirements.md/design.md must
   resolve to a screen of the MATCHING purpose in `Wireframes.md`. A spec citing `WF-014` for a
   Settings screen when WF-014 is a Delete modal, or `WF-003` for a Profile screen when WF-003 is
   the Confirmation screen, is a Fail (broken/mis-cited trace). Cross-check the WF IDs the roadmap
   Feature→Screen mapping assigned to this feature.
8. **Cross-spec consistency (project-wide, when other specs exist).** Run
   `python .claude/scripts/validate_cross_spec.py <project-name>` and treat any reported
   ERROR as a gate Fail: orphan spec (a spec dir absent from the roadmap registry), dangling WF ref,
   duplicate FR (`Same as FR-XXX`), or NFR-ID collision across specs. Warnings (possible mis-cited WF,
   FR-label mismatch) must be reviewed and either fixed or justified. Also run
   `python .claude/scripts/validate_traceability.py <feature-name>` for the single-feature
   internal trace.

### Step 8 — Emit the gate decision block

```markdown
## <SpecType> Quality Gate (<gate-id>)
- Structure — Major sections: Pass/Fail (missing: [list or None])
- Structure — Minor sections: Pass/Fail (missing: [major → minor list or None])
- No Placeholders / Non-empty: Pass/Fail
- Quality Checks: Pass/Fail (failing: [list or None])
- Traceability & IDs: Pass/Fail
- AC Coverage (gate-design only): Pass/BLOCKED (missing ACs: [list or None])
- Design Ref match (gate-tasks only): Pass/Fail (mismatches: [list or None])
## Blockers: [list or None]
## Required Fixes: 1. ...
```

**Pass**: all categories Pass, Blockers None, no Required Fixes. Spec is ready for approval.
**Fail**: any category Fail, any Blocker (including a blocked AC coverage), or any Required Fix.
Spec is NOT ready — loop back to fix.

### Output paths (per gate)
- `gate-requirements` → `.claude/specs/[feature-name]/requirements.md`
- `gate-design` → `.claude/specs/[feature-name]/design.md`
- `gate-tasks` → `.claude/specs/[feature-name]/tasks.md`

---

## Universal Fail Conditions

Any gate fails if:
- Unresolved placeholders remain in required sections
- A `required_major` or `required_minor` section is missing
- A `quality_checks` item fails
- Traceability links are broken or missing (requirement without Source, task without AC/design ref)
- Vague wording replaces measurable criteria on critical items
- (gate-design) ANY AC from requirements.md is missing coverage in design.md → BLOCKED
- (gate-tasks) a task's `Refs Design` does not match an existing design section number
- File is written outside `.claude/specs/[feature-name]/`

On failure: document concrete fix requests. Do not mark any spec ready until all categories pass.

---

## Quality Gates (self-referential)

This skill has no upstream gate. It is invoked by per-spec skills and by `spec-refine`. Its own
correctness is verified by:

- Stable gate IDs (no renaming without coordinated update across per-spec skills, `spec-workflow`,
  `spec-creation-contract`, and `commands/ios-spec.md`)
- The gate NEVER re-lists required sections; it reads each template's `QUALITY-GATE-MANIFEST`
- Output paths under `.claude/specs/[feature-name]/`
- Each gate's Required Fixes section is concrete (specific section + change), not vague

---

## Error Handling

- **Wrong gate ID for spec type**: stop. Cross-check the ID-to-template mapping in Non-Negotiable Rules.
- **Template missing QUALITY-GATE-MANIFEST**: stop, report a Blocker. Do NOT guess sections.
- **Spec missing required sections**: list each missing major/minor in Required Fixes. Do NOT mark ready.
- **Design missing AC coverage**: BLOCK approval, list each uncovered AC and the target feature section.
- **Task design ref mismatch**: list each task whose `Refs Design` has no matching design section.

---

## Output Contract

Per gate invocation, the output is a **gate decision block** (see Step 8).

**Pass**: all categories Pass, Blockers None or empty, no Required Fixes. Spec is ready.
**Fail**: at least one category Fail, or any Blockers, or any Required Fixes. Spec is NOT ready.
