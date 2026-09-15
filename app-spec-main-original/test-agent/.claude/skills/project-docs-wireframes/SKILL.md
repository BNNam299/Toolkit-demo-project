---
name: project-docs-wireframes
description: Create Wireframes.md with UI mockups and screen layouts. Use when designing screens, creating wireframes, defining UI components.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Required Skills & Files

Before executing this skill, you MUST read these files:

1. `.claude/doc-templates/Wireframes.md` — Wireframes template (archetype-specific)
2. `.claude/skills/project-docs-lifecycle/SKILL.md` — Lifecycle (dir setup, file safety, user confirmation)
3. `.claude/skills/project-docs-contract/SKILL.md` — Workflow contract
4. `.claude/skills/project-docs-quality-gates/SKILL.md` — Quality gate skill
5. `.claude/skills/ios-components/SKILL.md` — SwiftUI component implementation patterns
6. `.claude/skills/ios-ui-ux/SKILL.md` — UI/UX design principles
7. `.claude/shared/DESIGN_TOKEN_*.json` — Design token files (10 systems)

## Non-Negotiable Rules

1. **Step 0: Select Design System first.** No wireframe is drawn without a confirmed design token file.
2. **Every screen must have a Design System declaration.** `**Design System**: [token-name]` at the top.
3. **All components are custom-specified by the design system.** No iOS default UI patterns. Navigation bars, tab bars, buttons, cards, inputs — all sizes and colors from the token file.
4. **Every screen must have an Archetype from Use_Cases.md §9.**
5. **Use the archetype-specific template** (Discovery→A, Action→B, Consumption→C, Management→D, Social→E).
6. **Every screen must have Visual Hierarchy** — #1/#2/#3/#4 before the layout.
7. **Every screen must have a Content Zones Map** — Zone A/B/C/D with token-based sizes.
8. **Key screens must have Layout Variants** — ≥1 variant for ≥Medium density screens.
9. **Post-completion: Run Cross-Screen Component Consistency Audit.** Verify token consistency.
10. **Components reference `ios-components` skill for SwiftUI implementation patterns only. Visual properties come from the design system token file.**
11. Write files only under `.claude/specs/[project-name]/`.
12. **WF IDs MUST match those assigned in Use_Cases.md §0.4 Screen Architecture Canvas.** Provisional IDs in UC are binding contracts for WF. No renumbering, no skipping, no reuse.
13. **Affordance → FR back-trace (no silent affordances).** Every Component and every Interaction you draw must trace back to an FR (with AC). Secondary/utility affordances (settings icon, share, skip, date picker, tooltip, help/FAQ, export, edit-a-field) are the ones that get dropped — they are NOT exempt. If a screen needs an affordance that no FR covers, you have found an upstream gap: STOP, add the FR (and its ACs) to `Functional_Requirements.md` first (per `project-docs-contract` cascade), then draw it. Never introduce a UI affordance that no FR backs.
14. **Every WF (including modals/overlays) has a dedicated, on-topic FR.** Do not launder a screen (e.g. a Share modal) onto an unrelated FR (e.g. "progress vs goal"). If it has its own screen, it needs its own FR.

# Project Docs: Wireframes

## When to Use

- Use_Cases.md and Functional_Requirements.md are approved
- Need to define UI screen layouts and component specs
- Need to assign a design system (one of 10 token files) before any drawing

## Objective

Create `Wireframes.md` that maps every functional requirement to a screen with layouts, component references, and state definitions. This document is the visual blueprint connecting FRs to UI.

**ALL components are custom-designed based on a chosen Design System.** No iOS default UI patterns (NavigationStack, TabView, List) are used. Every component — including navigation bars and tab bars — is custom-specified through the design token file.

## Prerequisites

- `.claude/specs/[project-name]/PRD.md` exists and is approved
- `.claude/specs/[project-name]/Use_Cases.md` exists (with §0.4 Screen Architecture Canvas, §3 UC→Screen Mapping, §4 Screen-Context, §2 bis Feature Expression Matrix, §9 Screen-Intent Summary)
- `.claude/specs/[project-name]/Functional_Requirements.md` exists
- At least one design token file loaded from `.claude/shared/DESIGN_TOKEN_*.json`

---

## Archetype Zone Override Table

`Use_Cases.md` §4 defines Zone A/B/C/D with **default** Discovery-archetype semantics (Hero / Engagement / Discovery / Utility). For other archetypes, the zones are reassigned per the table below. When a screen's archetype requires override, the Wireframes §Content Zones Map MUST use the override labels — UC's default labels apply only to Discovery screens.

| Archetype | Zone A | Zone B | Zone C | Zone D |
|---|---|---|---|---|
| **Discovery** (default — uses UC labels) | Hero | Engagement | Discovery | Utility |
| **Discovery** (feed variant) | Hero / Featured | Main Feed / Grid | Discovery Sections | Navigation + Tab Bar |
| **Action** | Context / Summary | Input Area + Primary CTA | — | Navigation |
| **Consumption** | Hero Media (full-bleed) | Key Info + CTA (sticky) | Detailed Content | — |
| **Management** | — | Actionable List | — | Navigation + Filter Bar + Edit Bar |
| **Social** | — | Content / Activity + Compose | — | Profile Header |

**Rules:**
- If a screen's archetype requires zone reassignment, the override MUST match the table above.
- Custom overrides (e.g., a hybrid Discovery/Consumption screen) require explicit justification in Wireframes §Notes for that screen.
- "—" in a zone cell means that archetype does not require that zone (the slot is unused or merged with another).

---

## Action Layers to Visual Hierarchy Mapping

`Use_Cases.md` §4 declares 4 **Action Layers** (Primary / Contextual / Discovery / Personal). Wireframes §Visual Hierarchy declares 4 hierarchy slots (#1 / #2 / #3 / #4). The two systems are NOT 1:1 — Visual Hierarchy describes eye-priority order, while Action Layers describe purpose. The mapping below is the bridge.

| UC Action Layer | Visual Hierarchy Slot | Rationale |
|---|---|---|
| **Layer 1 — Primary** | #3 (high contrast, after hero) | The ONE main action the user takes on this screen — becomes the CTA in the wireframe |
| **Layer 2 — Contextual** | #3-#4 (inline with content) | Related to current content (like, comment, share, save) — inline buttons, not separate |
| **Layer 3 — Discovery** | #4 (below fold or zone C/D) | Leads user to new content (related items, trending, explore more) — secondary zone |
| **Layer 4 — Personal** | #4 (chrome/utility) | User identity/preferences (customize, filter, settings) — chrome-level visibility |

**Rules:**
- Every screen MUST map each declared UC Action Layer to a Visual Hierarchy slot. Any unmapped layer fails the gate.
- Layer 1 (Primary) MUST be the highest-contrast interactive element after the hero. A Primary action assigned to slot #4 is a failure.
- Layers 2-4 may compete for slot #3 or #4 depending on screen density. Layer 1 always wins slot #3.
- The mapping for each screen is declared in Wireframes §3 (Screen Sections) before the Visual Hierarchy list.

**Example** (Discovery screen, e-commerce Home):
| UC Action Layer | Visual Hierarchy Slot |
|---|---|
| Layer 1 — Primary: "Tap product card" | #3 — entire card is tappable, highest contrast after hero |
| Layer 2 — Contextual: "Save to wishlist" | #4 — inline icon button on each card |
| Layer 3 — Discovery: "See trending category" | #4 — section header link "See all >" |
| Layer 4 — Personal: "Switch language" | #4 — chrome-level, settings icon in nav bar |

---

### Step 0: Select Design System (MANDATORY — before reading any context)

Before writing a single screen, select the design system that will govern ALL visual decisions. The design system determines colors, typography, spacing, borders, shadows, animations, and every component spec — including custom navigation bars and tab bars.

#### 0.1 Read Project Context

Read `Project_Overview.md` and `PRD.md`. Extract:
- **App type** (e-commerce, social, fitness, etc.) → maps to `bestFor` in token meta
- **Brand mood** (if described in Overview) → maps to `mood` in token meta
- **Target audience** (age, context) → influences visual weight preference
- **User goal** (productivity vs entertainment vs social) → maps to functional need

#### 0.2 Choose from 10 Design Systems

Read the `meta` section of each design token file at `.claude/shared/DESIGN_TOKEN_*.json`. Match app context to design system using this guide:

| Design System | Visual Character | Best For |
|--------------|-----------------|----------|
| `bento-grid` | Structured Apple-like cards with soft shadows | Dashboard, content discovery, productivity |
| `functional-minimalism` | Invisible UI, typography-driven, no shadows | Writing, reading, task management |
| `cards-layering` | Depth-rich stacked cards, 5 elevation levels | Finance, banking, file management |
| `soft-skeuomorphism` | Warm 3D highlights, paper texture, rounded | Wellness, journaling, meditation |
| `dark-mode-first` | True-black OLED, neon accents, no shadows | Media player, crypto, night-mode apps |
| `glassmorphism` | Frosted glass, blur, pastel gradients | Music, weather, creative showcase |
| `aurora-gradients` | Mesh gradients, colored shadows, glow | Meditation, mood tracking, creative tools |
| `neobrutalism` | Bold black borders, hard shadows, pop colors | Gen-Z social, gaming, edtech |
| `typographic-driven` | Serif + sans-serif, no cards, editorial | Reader, news, journal, documentation |
| `motion-first` | Spring animations, haptics, stagger effects | Social, fitness, onboarding, camera |

#### 0.3 Confirm Selection

Present your recommendation to the user with reasoning:
```
Recommended: [Design System Name]
Because: [2-3 reasons matching app type, mood, audience]
Alternative: [One other option if this doesn't feel right]

Use this system? (or specify another)
```

Once confirmed, load the full design token file into context. ALL subsequent layout decisions reference this file.

### Step 1: Read Context

Gather all source documents before writing. Also load the chosen design token file at `.claude/shared/DESIGN_TOKEN_[name].json`:

- **PRD** for product goals and scope
- **Use Cases (UC)** for user interactions and actors
- **Use_Cases.md §0.4 Screen Architecture Canvas** for the FULL screen hierarchy (tabs, subsections, modals) — use this to know which screens exist, not just PRD's flat inventory
- **Use_Cases.md §4 Screen-Context** for archetype + density + layers + zones per screen — archetype choice directly determines which template to use
- **Use_Cases.md §2 bis Feature Expression Matrix** for which UCs are expressed on which screens — informs component reuse and layout variants
- **Functional_Requirements.md §2 bis Component Behavior Matrix** for multi-screen FR expression details (component used, input required, validation rules applied, output behavior per screen)
- **Functional Requirements (FR)** for specific features each screen must satisfy
- **UC → Screen Mapping (Use_Cases.md §3)** for which UCs belong on which screens — REQUIRED input
- **Screen-Context Use Cases (Use_Cases.md §4)** for user intent and primary/secondary actions per screen — REQUIRED input
- **Task Flows (Use_Cases.md §5)** for cross-screen user journeys — REQUIRED input
- **Screen-Intent Summary (Use_Cases.md §9)** for quick-reference of what each screen must support — REQUIRED input
- Note every FR ID, every screen mentioned, every requirement

List all FRs and map each one to at least one screen. Validate against the UC → Screen Mapping from Use_Cases.md — every FR's parent UC must appear in the Screen → UC Coverage table.

### Step 2: Create Directory

Follow `project-docs-lifecycle` to create the project docs directory structure if it doesn't exist. Ensure the directory is ready before writing.

### Step 3: Write Wireframes.md

Use the template at `.claude/doc-templates/Wireframes.md` as the structural foundation. Fill it with project-specific content. Its `QUALITY-GATE-MANIFEST` (end of template) is the authoritative list of required sections — reproduce them, do NOT copy the manifest block into the output. `gate-wireframes` validates against that manifest.

#### Mandatory Screens

Regardless of app type, always include these screens:

- **Splash** (WF-001): App launch, branding, initialization check
- **Onboarding** (WF-002): First-run experience, permissions, feature introduction
- **IAP / Paywall** (WF-003): In-app purchase flow, subscription options, restore purchases

These three screens exist in every app. Add them even if the PRD doesn't explicitly mention them.

#### Screen ID Format

Every screen gets an ID: `WF-XXX` (e.g., WF-001, WF-002, WF-010). Sequential numbering. **MUST match IDs assigned in Use_Cases.md §0.4 Screen Architecture Canvas — do not reassign, renumber, skip, or reuse.**

#### Each Screen Section Must Have

Reference the template at `doc-templates/Wireframes.md` for the archetype-specific templates. **CRITICAL: Choose the template that matches the screen's archetype from Use_Cases.md §4 and §9.**

**Design System Reference**: Every screen starts with `**Design System**: [name]`. All visual decisions (color, spacing, typography, component specs) come from the loaded design token file.

1. **Screen Archetype & Density** (from Use_Cases.md §4/§9)
2. **Visual Hierarchy** — #1/#2/#3/#4 ordered by eye path.
3. **Required Features** (from FR)
4. **UX Enhancements** — start with the chosen design system's `composition.[archetype]` defaults.
5. **Content Zones Map** — Zone A/B/C/D with sizes from design system's `component.navBar.height`, `spacing` scale.
6. **Layout** — ASCII wireframe using design system's component specs (nav bar style from `component.navBar`, tab bar from `component.tabBar`, cards from `component.card`, etc.). Reference token values by path: `${component.navBar.height}`, `${color.palette.background}`.
7. **Layout Variants** — ≥1 variant for key screens.
8. **Components** — reference `ios-components` skill for SwiftUI implementation patterns, but apply design system tokens for all visual properties.
9. **States** — every screen MUST declare BOTH:
   - **User-Context States** (inherited from Use_Cases.md §4): First Visit + Returning + Error minimum
   - **Data States**: Default + Loading + Empty + Error
   - 7 states total minimum (3 user-context + 4 data).
10. **User Flow** — entry/exit with WF-XXX references.

#### Component Specification Protocol

Every component in the layout must reference the design system. Format:

```
Component: [Name from token] — [Brief description]
  Uses tokens:
    height: ${component.[name].height}
    background: ${color.palette.[key]}
    radius: ${border.radius.[level]}
    font: ${typography.scale.[key]}
    shadow: ${shadow.elevation.[level]}
    animation: ${animation.spring.[preset]} + ${animation.duration.[key]}
```

**Custom navigation bar example (using bento-grid tokens):**
```
navBar:
  height: 44 (${component.navBar.height})
  background: rgba(244,245,247,0.85) (${component.navBar.background})
  hasDivider: true, color: #E2E8F0
  title in ${typography.scale.headline}
  back icon: chevron.left, 20pt, medium weight
```

**All navigation, tab bars, buttons, cards, inputs, chips, avatars, dividers, toasts, and sheets are custom-defined by the design system.** No default iOS component appearance is used.

#### Archetype Assignment Check (before writing any screen)

Before writing a single screen wireframe, verify:
- Every screen has a Primary Archetype assigned in Use_Cases.md §9 Screen-Intent Summary
- Every screen's archetype matches its user intent (a "consumption" screen shouldn't have action-heavy UX)
- The chosen template matches the archetype (no using Discovery template for an Action screen)
- Density from Use_Cases.md matches the archetype expectations:
  - Discovery: Dense (6+ zones)
  - Action: Medium (3-5 zones)
  - Consumption: Light/Medium (1-4 zones)
  - Management: Dense/Medium (4-6 zones)
  - Social: Medium/Dense (3-6 zones)

#### Visual Hierarchy Protocol (MANDATORY — before drawing layout)

For each screen, BEFORE drawing the ASCII layout, declare the visual hierarchy. AI must think about what the user's eyes see FIRST, SECOND, THIRD. Without this step, layouts become flat — every element competes for attention equally.

**Declare the hierarchy in this format:**

```
**Visual Hierarchy** (order the user's eye follows):
1. [Element] — [Why first: largest size, highest position, brightest color, or strongest contrast]
2. [Element] — [Why second: below/near #1, supports the primary message]
3. [Element] — [Why third: primary action, high contrast against background]
4. [Element] — [Why lower: smaller, secondary, supporting role]
```

**Hierarchy rules by archetype:**

| Archetype | #1 (Most Important) | #2 | #3 | #4+ |
|-----------|-------------------|-----|-----|-----|
| Discovery | Hero/featured content (full-width, image-driven) | Section headers (scannable labels) | Card actions (inline, non-intrusive) | Chrome (search, nav, tabs — utility) |
| Action | Form/input context (what is being acted on) | Input fields (largest tappable area) | CTA button (high contrast, fixed position) | Navigation (back/cancel — escape route) |
| Consumption | Media (full-bleed, edge-to-edge) | Key info (title, price, rating — sticky) | Primary action (FAB or sticky bar) | Secondary content (reviews, specs — below fold) |
| Management | List header (sort/filter, context) | List rows (scanning pattern top-down) | Swipe actions (revealed on demand) | Action bar (edit/select — appears on demand) |
| Social | Identity (avatar, name — who is this?) | Content (post, message — what did they say?) | Reactions (inline, lightweight) | Compose/input (only when user wants to respond) |

**Self-check questions for each screen (answer before finalizing):**

1. Is the #1 element genuinely the largest/most prominent thing on this screen? If not, adjust.
2. Can the user complete the #1 task on this screen within 3 seconds of opening it?
3. Is the CTA the highest-contrast element (after the hero)? If not, the user won't find it.
4. Are secondary elements at least 30% smaller/less prominent than the primary? If everything is the same size, nothing is important.
5. Does the layout match the archetype's hierarchy pattern above? A Discovery screen with CTA as #1 is an Action screen mislabeled.

#### iOS Pattern Reference for Layout

When drawing the ASCII layout, map each zone to a real iOS UI pattern:

| iOS Pattern | Use When | Implementation Hint | Typical Size |
|-------------|----------|--------------------|--------------|
| **NavigationStack** | Push/pop navigation between screens | `NavigationLink` wraps tappable rows | 44pt nav bar |
| **TabView** | 3-5 top-level sections | `.tabItem` with SF Symbol + title | 49pt bar (83pt with safe area) |
| **.sheet** | Modal for focused tasks (create, filter, select) | `.sheet(isPresented:)` — partial or full | Default detent or custom |
| **.fullScreenCover** | Immersive full-screen task | `.fullScreenCover(isPresented:)` | Full screen |
| **.toolbar** | Top/bottom bar actions | `.toolbar { ToolbarItem(placement:) }` | 44pt |
| **.contextMenu** | Long-press secondary actions | `.contextMenu { Button(...) }` | Native size |
| **.refreshable** | Pull-to-refresh on scrollable content | `.refreshable { await load() }` | Native spinner |
| **.searchable** | Search bar integrated with navigation | `.searchable(text: $query)` | 44pt |
| **.confirmationDialog** | Destructive or choice confirmation | `.confirmationDialog(...)` | Native action sheet |
| **List + .swipeActions** | Leading/trailing swipe on rows | `.swipeActions(edge: .trailing) { ... }` | Row height |
| **ScrollView + LazyVStack** | Custom scrollable content (not List) | Manual layout with `ForEach` | Fill |
| **ZStack overlay** | Floating button, badge, toast | Content + overlay aligned to edge | Custom |
| **SafeArea** | Respect notch/home indicator | `.ignoresSafeArea()` for hero images only | ~44pt top / ~34pt bottom |
| **Dynamic Island** | Live activity on iPhone 14 Pro+ | `ActivityKit` if real-time info | Native |

**Rule for each screen's layout:** All sizing, colors, and component specs come from the chosen design token file. Reference token paths explicitly. Example using `bento-grid` tokens:

```
┌─────────────────────────────────────┐
│  custom navBar                      │ ← ${component.navBar.height}pt
│  background: ${component.navBar.background}
│  divider: ${component.navBar.dividerColor}
├─────────────────────────────────────┤
│  [Hero Image]                       │ ← ${spacing.xxl}pt height
├─────────────────────────────────────┤
│  ScrollView                         │ ← Zone B (fills remaining)
│  ┌─────────────────────────────┐   │
│  │ card: ${component.card.radius}px││ ← ${component.card.padding}px padding
│  │      ${component.card.shadow} │  │
│  │      ${component.card.border} │  │
│  └─────────────────────────────┘   │
├─────────────────────────────────────┤
│  custom tabBar                      │ ← ${component.tabBar.height}pt
│  background: ${component.tabBar.background}
└─────────────────────────────────────┘
```

#### Design System Token Reference

All dimensional and visual values come from the selected design token file, never hardcoded. Key token paths:

| Visual Property | Token Path |
|----------------|-----------|
| Screen background | `${color.palette.background}` |
| Card surface | `${color.palette.surface}` |
| Primary text | `${color.palette.textPrimary}` |
| Accent color | `${color.palette.accent}` |
| Nav bar height | `${component.navBar.height}` |
| Nav bar background | `${component.navBar.background}` |
| Nav bar blur | `${component.navBar.blur}` |
| Tab bar height | `${component.tabBar.height}` |
| Tab bar background | `${component.tabBar.background}` |
| Button height/radius | `${component.button.primary.height}` / `${component.button.primary.radius}` |
| Card radius/padding | `${component.card.radius}` / `${component.card.padding}` |
| Border radius scale | `${border.radius.lg}` |
| Shadow levels | `${shadow.elevation.1}` through `${shadow.elevation.5}` |
| Spacing scale | `${spacing.xs}` through `${spacing.xxl}` |
| Typography | `${typography.scale.headline}` (font, size, weight, lineHeight) |
| Animation | `${animation.spring.bouncy}` + `${animation.duration.normal}` |

#### Cross-Screen Component Consistency Audit (AFTER writing all screens)

After completing all screen wireframes, audit component consistency. Same component → same visual treatment across all screens. Inconsistency makes apps feel broken and unprofessional.

**Audit Steps:**

**Step 1 — Identify shared components.** Scan all screens for components that appear on ≥2 screens. List them:

```
Component → Screen: Expression
  CartBadge → WF-004 (nav bar right) / WF-005 (nav bar right) / WF-006 (nav bar right) / WF-008 (inside page)
  ShareButton → WF-005 (nav bar) / WF-004 (context menu) / WF-020 (post-success sheet)
  SearchBar → WF-004 (top of scroll) / WF-010 (nav bar integrated) / WF-013 (filter bar)
```

**Step 2 — Verify consistency.** For each shared component, check:

| Check | Question | Fail = |
|-------|----------|--------|
| Size | Same height/width across all screens? | Adjust to match |
| Position | Same screen zone across all screens? (e.g., always nav bar, always bottom-right) | Justify difference or align |
| Icon | Same SF Symbol or image asset? | Use identical asset name |
| Label | Same text label? (if navigation element) | Keep label identical |
| Color | Same semantic color? (not same hex if context differs) | Use shared color token |
| Behavior | Same interaction pattern? (tap→same action, swipe→same result) | Document why different |
| State | Same loading/error/disabled appearance? | Match the state design |

**Step 3 — Document exceptions.** If a component deliberately looks different on different screens, document WHY:

```
CartBadge on WF-008 Cart page: SHOWS COUNT + "Items" label (larger, in-page)
  → Differs from nav bar CartBadge because user is managing cart, not navigating.
  → This is a DIFFERENT component: "CartSummaryBadge" not "CartNavBadge".
```

**Step 4 — Name distinction.** If two expressions are different enough, give them distinct component names. This prevents AI from treating them as the same component and getting confused later during implementation.

#### Common Components Section

Reference the `ios-components` skill. Do NOT reproduce the full component catalog.

#### Design System Section

Reference the `ios-ui-ux` skill. Do NOT hardcode iOS colors or font sizes.

#### Scaling Guidelines

- **Small apps (<12 screens)**: 12-20 screens, cover all MVP FRs
- **Medium apps (12-25 screens)**: 20-35 screens, include secondary flows
- **Large apps (25+ screens)**: 35+ screens, exhaustive coverage

Screen count is driven by Use_Cases.md §0.4 Screen Architecture Canvas, not by PRD alone.

#### Affordance → FR Back-Trace Audit (AFTER writing all screens — BLOCKING)

Before the gate, list EVERY Component and Interaction of EVERY screen and back-trace each to an FR:

```
WF-XXX <screen>
  Component/Interaction → FR-XXX (AC-XXX.Y)   ✓ backed
  Component/Interaction → (no FR)             ✗ GAP
  Component/Interaction → out-of-scope: owned by <spec/FR>   ✓ deferred
```

For every `✗ GAP`:
1. Decide: is this affordance real? If yes → add the FR + ACs to `Functional_Requirements.md` (upstream fix, then regenerate the affected part), and re-run `gate-fr`.
2. If it should not exist → remove it from the wireframe.
3. Never leave a `✗ GAP`. A screen affordance with no FR is exactly the silent-drop failure this audit exists to catch (e.g. a Share button, a Skip button, a settings gear, a Help/FAQ cell).

Also confirm every WF-XXX (including modals like a Share/Delete/Edit modal) has its OWN on-topic FR, not a borrowed one.

### Step 4: Quality Gate

Run the `project-docs-quality-gates` skill with gate `gate-wireframes`. Fix any failures.

Then follow `project-docs-lifecycle` for user confirmation before marking complete.

---

## Quality Gates

| Gate | Skill | Pass Criteria |
|------|-------|---------------|
| `gate-wireframes` | `project-docs-quality-gates` | Every screen has Design System + Archetype + Visual Hierarchy + Content Zones + token-based sizes; cross-screen component consistency audit run; mandatory screens (Splash, Onboarding, IAP) included |

---

## Error Handling

- **No design system selected**: stop. Direct user to Step 0 first.
- **Screen missing archetype**: assign from Use_Cases.md §9 before writing wireframe.
- **Token reference not path-style** (e.g., hardcoded hex): replace with `${token.path}`.
- **iOS default component appearance used**: replace with custom design system spec.
- **Quality gate failure**: revise, re-run gate.

---

## Output Contract

- File: `.claude/specs/[project-name]/Wireframes.md`
- Every screen: WF-XXX, Design System declaration, Archetype, Visual Hierarchy, Content Zones, Layout (ASCII), ≥1 Layout Variant (Medium+ density), States (Default/Loading/Empty/Error), User Flow
- Cross-Screen Component Consistency Audit section at the end
- Token-based sizing/colors throughout (no hardcoded values)
