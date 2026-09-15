---
name: ui-redesign
description: Post-build app-wide UI redesign engine. Use to redesign a finished iOS app to a distinctive style from an image, a text description, or a .pen design file (via Pencil MCP) — audit the built UI, propose new tokens/components/screens, then apply to code with existing gates. Independent of project-docs.
allowed-tools: Read, Write, Edit, Grep, Glob, Bash, mcp__pencil__get_editor_state, mcp__pencil__get_variables, mcp__pencil__get_guidelines, mcp__pencil__get_screenshot, mcp__pencil__snapshot_layout, mcp__pencil__export_nodes, mcp__pencil__export_html, mcp__pencil__batch_get
skills:
  - ui-redesign-craft
  - ui-redesign-contract
---

# UI Redesign — Engine (pipeline + Creative Method)

Redesign a **built** iOS app to a **distinctive style**. This skill is the **creative engine** — it *produces*
the redesign. `ui-redesign-contract` only *validates* the output; `ui-redesign-craft` supplies the design
craft (signature moments). This flow is **independent of project-docs**.

## Required reading before running
- `.claude/skills/ui-redesign-contract/SKILL.md` — output paths, file schemas, `gate-redesign`
- `.claude/skills/ui-redesign-craft/SKILL.md` — distinctiveness principles + signature-moments catalog
- `.claude/skills/ios-architecture/SKILL.md` — file placement + `shared/Styles` (Structure Gate)
- `.claude/skills/ios-components/SKILL.md` — Reuse-First Gate
- `.claude/skills/ios-ui-ux/SKILL.md` — UX Compliance Gate (the FLOOR that must be kept)

## Non-Negotiable Rules
- **Only UI/visual/motion/navigation** — never change business logic. Anything touching logic → stop, report `/ios-spec`.
- **Keep the UX floor** on every screen: 4 states, error recovery, a11y labels + Dynamic Type + contrast ≥4.5:1, ≥44pt targets, dark mode.
- **Distinctiveness is required** — output must visibly leave iOS-stock (no leftover `#007AFF`/system-default) and carry ≥1 signature moment per screen, all traceable to the Style DNA.
- **Reuse-first** for components; new components are parameterized and use DSS tokens.
- `.pen` files are encrypted → access ONLY via Pencil MCP; never Read/Grep them.
- Write proposal files ONLY under `.claude/specs/[project-name]/redesign/`; write code ONLY under `shared/Styles|Components/` and `Features/*/Views/*`.
- Advance a phase only after its gate passes; persist `redesign-state.json` after each phase.

---

## State machine (`redesign/redesign-state.json`)

```
intake → audit → proposed → approved → applying → done
```
Schema and fields: see `ui-redesign-contract` §State Schema.

---

## Pipeline

### P0 — Prerequisite & init
1. Verify every `.claude/specs/*/spec-state.json` has `stage: done` and the app builds. If not → STOP (E-1).
2. Create `.claude/specs/[project-name]/redesign/` and `redesign-state.json` with `state: intake`.

### P1 — Intake style → Style DNA
Resolve the source from `$ARGUMENTS`:
- `--pen <name>`: use **Pencil MCP** (order below) to learn the design and extract variables/tokens.
- `--image <path...>`: read the image(s) as the visual reference.
- `--desc "<text>"`: parse the description.

**Pencil MCP order (contract):**
```
1. get_editor_state(include_schema: true)   # MUST be first — loads schema for other tools
2. get_variables()                           # → design tokens: color/type/spacing/radius/shadow (main source for design-tokens.md)
3. get_guidelines()                          # → style rules → feed into Style DNA
4. get_screenshot() / snapshot_layout()      # → reference image/layout (store path in style-reference.md)
5. export_nodes() / export_html() (optional) # → sample component/layout spec → hints for components.md
```
Valid `--pen` name = a file in `.claude/design-token/` (strip `template-` prefix and `.pen` suffix).
No match / MCP unavailable → E-2 (ask / list options / offer `--image|--desc`).

Synthesize **Style DNA** `{mood, palette, type-vibe, shape-language, motion, density, refs}` → write `style-reference.md`.
Record `style_ref` (source, images/pen_file/pen_variables, dna_summary). `state: audit`.

### P2 — Audit the built UI (combined)
1. **Screen inventory from the built app**: list every SwiftUI screen under `Features/*/Views/*.swift` (this — not `Wireframes.md` — is the source of screens).
2. Read current DSS: `shared/Styles/AppColors.swift`, `AppFonts.swift`, `AppSpacing.swift`; and `shared/Components/*`.
3. **Screenshot before** (unless `--mode static`): via XcodeBuild MCP `discover_projs → list_schemes → build_sim`, then boot simulator and capture each screen. If the sim can't boot → E-3 (static-only, record "screenshot skipped").
4. (Optional) cross-reference `design-ui/*` and `Wireframes.md` if present.
5. Write `current-ui-audit.md`: inventory + screenshot refs + **gap vs Style DNA** (where current UI is generic/iOS-stock).

### P3 — New design system (tokens + components)
- `design-tokens.md`: the new token set (color/type/spacing/radius/shadow/motion/elevation) **plus a table mapping each token → `shared/Styles/*.swift`** (symbol name + target file). If source = `.pen`, map Pencil variables → tokens directly (fills the JSON→Swift bridge).
- `components.md`: the new-style component library. For each: **old→new** mapping + reuse tier (`as-is > parameterize > compose > extend > new`) + reason. Maximize reuse; new components are parameterized + use tokens.

### P4 — Redesign each screen (CREATIVE — see §Creative Method)
For every screen in the inventory, apply the **Creative Method** below + the **craft catalog** (`ui-redesign-craft`) and write `screens/screen-[view-name].md` (per `ui-redesign-contract` §Screen Schema). Then write `flows.md` with **mermaid** navigation flows (may change — full UI refactor allowed). `state: proposed`.

### P5 — Index + manifest + gate
- Write `README.md` (human+AI index: style summary, read-order, single-source-of-truth table), `redesign-summary.md` (change list, migration order shared→core→secondary, risk), and `manifest.json` (machine-readable tokens + old→new components + screen list).
- Run **`gate-redesign`** (defined in `ui-redesign-contract`). Fix failures. Then **PAUSE for user approval**.

### P6 — Apply to code (after approval)
Following `manifest.json`, in migration order:
1. Tokens → `shared/Styles/*.swift` (+ `AppMotion.swift`/`AppElevation.swift` if the style needs them).
2. Build the new-style components in `shared/Components/[Type]/` (Reuse-First Gate).
3. Refactor each `Features/*/Views/*.swift` to its proposal.
Each step passes the **Structure**, **Reuse-First**, **UX Compliance**, and **DSS** gates; run XcodeBuild MCP `build_sim` after each phase. `state: applying`.

### P7 — Verify + screenshot-critique loop
Iterate (≤ N rounds, default 3):
1. Build + boot sim + **screenshot after** each screen.
2. **Self-critique as a UI/UX expert**: does it match the Style DNA? Is it distinctive (left iOS-stock)? Hierarchy/rhythm/motion coherent? Floor intact?
3. If below bar → refine tokens/components/views and repeat.
When the bar is met: produce before/after per screen, run Build/Integration gate (app launches, no regression, no behavior change), update `redesign-summary.md`, set `state: done`.

---

## Creative Method (the generation engine — this is what makes it *design*, not just conform)

Contract can't create; this can. For each screen, transform **Style DNA → concrete visual decisions**:

```
INPUT : Style DNA {mood, palette, type-vibe, shape-language, motion, density} + screen role + current screenshot
STEPS :
  1. Pick a "signature system": ONE recurring form idea across the whole app
     (e.g. bento layout, bold neo borders, typographic hero, layered depth) — chosen from the craft catalog.
  2. Per-screen decisions: composition/zones · visual hierarchy (#1..#4) · color roles (bg/surface/accent/semantic)
     · type scale · spacing rhythm · elevation · motion/transition.
  3. Choose 1–3 signature moments per screen from the craft catalog; place them at focal points
     (hero, empty state, primary CTA, key transition).
  4. For every major decision, record WHY it traces to the Style DNA (trace) AND how it leaves iOS-stock (distinctiveness).
OUTPUT: content for screens/screen-[view].md + the tokens/components it requires.
GUARD : keep the UX floor; never change business logic; prefer reusing components.
```

---

## Edge Cases
- **E-1** App not built / spec not `done` → STOP, require `/ios-execute` first.
- **E-2** No style input / `--pen` not found / Pencil MCP unavailable → ask, list `.pen` options, offer `--image|--desc`; still empty → STOP.
- **E-3** Simulator won't boot → static audit only, record "screenshot skipped" (never silent).
- **E-4** Style breaks the UX floor (contrast <4.5:1, missing state) → gate BLOCKS; adjust, don't trade away.
- **E-5** A change would touch business logic → split it out; report `/ios-spec`.
- **E-6** New component duplicates an existing one → Reuse-First forces reuse/parameterize.
- **E-7** Refactor causes a regression → roll back that step, keep the app green; do not mark `done`.
- **E-8** No `design-ui/`/`Wireframes.md` → still runs (screens from Views; DNA from input); note missing optional references.

## Output Contract
All output paths, file schemas, and `gate-redesign` are defined in `ui-redesign-contract`. This skill produces the
content; the contract validates it.
