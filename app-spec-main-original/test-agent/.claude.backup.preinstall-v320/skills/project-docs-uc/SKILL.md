---
name: project-docs-uc
description: Create Use_Cases.md with user stories and scenarios. Use when defining user interactions, writing user stories, documenting scenarios.
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
skills:
  - project-docs-lifecycle
  - project-docs-contract
  - project-docs-quality-gates
---

# Create Use_Cases.md

## Objective

Create `Use_Cases.md` at `.claude/specs/[project-name]/Use_Cases.md`, documenting:
1. **Creative Decomposition (§0)**: Feature explosion, repetition audit, screen architecture canvas
2. **User Stories (§2)**: What users want to accomplish (UC-XXX)
3. **Feature Expression Matrix (§2 bis)**: Same UC expressed differently across screens
4. **UC → Screen Mapping (§3)**: Which UCs touch which screens — the bridge to wireframe design
5. **Screen-Context Use Cases (§4)**: What users want ON each screen with layers, zones, archetypes
6. **Task Flows (§5)**: Step-by-step user journeys across screens — drives UX flows
7. **Sub-Flows (§5 bis)**: Within-screen micro-interactions and step-by-step reveals

Source of truth is PRD.md. Screen inventory comes from PRD §8 Screen Inventory.

---

## Step 0: Creative Decomposition (MANDATORY — do not skip)

Before writing any UC, perform creative thinking. This step transforms PRD features into rich, engaging use cases. NEVER skip this step — it is the foundation of an engaging app.

### 0.1 Feature Explosion

For each feature in PRD §5, read the feature name and description, then ask:

1. **Sub-feature breakdown**: What smaller, standalone actions does this feature contain?
   - Can each sub-action be its own screen?
   - Can each sub-action be its own UC?
2. **Frequency analysis**: Which actions does the user do daily? Weekly? Once ever?
3. **Relationship discovery**: Which sub-actions naturally lead to other sub-actions?
4. **Hidden value**: What secondary value does this feature provide beyond its stated purpose?

**Output format — create a Feature Explosion Table.** Every row is a sub-feature YOU discovered by thinking deeply about the PRD feature. Use the PRD's own feature names and derive sub-features from their descriptions:

```
| PRD Feature | Sub-Features Discovered | UC Candidates | Daily? | Relates To |
|-------------|------------------------|---------------|--------|------------|
| [Feature from PRD §5] | [Sub-feature 1 you derived] | UC-001 | [Yes/No] | [Related UC] |
| [Same feature] | [Sub-feature 2 you derived] | UC-002 | [Yes/No] | [Related UC] |
| [Same feature] | [Sub-feature 3 you derived] | UC-003 | [Yes/No] | [Related UC] |
| [Same feature] | [Sub-feature 4 you derived] | UC-004 | [Yes/No] | [Related UC] |
| [Next feature from PRD §5] | [Sub-feature 1 you derived] | UC-005 | [Yes/No] | — |
| ... | ... | ... | ... | ... |
```

**Rule**: A single PRD feature must explode into ≥3 UC candidates. If a PRD feature yields only 1 UC, you have not thought deeply enough. Push yourself.

**Thinking prompts by app domain** (use the domain that matches the PRD):

| Domain | A feature in this domain typically explodes into... |
|--------|-----------------------------------------------------|
| E-commerce | Browse by category → Browse by brand → Browse curated → Browse trending → Browse new → Browse sale → Browse recommendations → Browse by price → Browse by rating |
| Social | Text post → Photo post → Video post → Poll → Story → Repost → Scheduled post → Drafts → Post with location → Post with tags |
| Fitness | Start workout → Log sets → Log cardio → Log bodyweight → Custom exercise → View history → Compare → Share workout → Export → Set goal |
| SaaS | View dashboard → Create item → Edit item → Share item → Export item → Archive item → Duplicate item → Batch operation → Search item → Filter item |
| Finance | View balance → View transactions → Filter by category → Search transaction → Export statement → Set budget → Set alert → Add account → Reconcile → Share report |
| Education | View lesson → Take quiz → Track progress → Set goal → Review mistakes → Bookmark → Share result → Download content → Set reminder → Join live |
| Health | Log entry → View trends → Set target → View insights → Export data → Share with provider → Set medication reminder → Log symptom → View history → Generate report |

**These are thinking prompts, not templates.** Derive sub-features from what the PRD actually says, not from this table. The table exists to show you what "deep decomposition" looks like.

### 0.2 Context Storming

For each UC candidate from 0.1, imagine how it changes across 3 user contexts:

| Context | User State | What Changes | Creates |
|---------|-----------|-------------|---------|
| **First-time user** | No data, unfamiliar | Needs onboarding, guidance, empty state design | Alternative flow or screen variant |
| **Returning user** | Has data, knows basics | Wants speed, shortcuts, personalization | Optimized layout, gesture support |
| **Power user / Edge case** | Heavy usage, errors | Needs advanced features, recovery, undo | Error recovery flow, advanced mode |

For EACH UC candidate, write context variations using the PRD's personas and features. Format:

```
[UC-XXX]: [Use Case Name from your Feature Explosion]
  First-time user: [What changes? Empty state? Different CTA? Guidance?]
  Returning user: [What gets faster? What gets personalized?]
  Power user / Edge case: [What shortcuts? What errors and recovery?]
```

**Example of what good context thinking looks like:**
- A "Browse Products" UC for first-time users shouldn't just say "No products yet" — it should offer curated starter collections, "Popular now", or a "Take the style quiz" CTA
- A "Send Message" UC for power users shouldn't just work — it should support quick-reply from notification, message templates, scheduled send
- A "Track Workout" UC for edge cases shouldn't show a generic error — it should auto-save draft on interruption, offer "Resume last workout" on return

**Rule**: Each UC must have ≥2 context variations. UCs with only 1 variation are under-designed.

### 0.3 Repetition Audit

Identify actions from your Feature Explosion that SHOULD appear in multiple places for a richer experience. Start with this audit checklist:

| Action Category | Should appear at least | Why |
|-----------------|----------------------|-----|
| Share / Export | 3+ locations | Different entry points = different user intent |
| Save / Bookmark | 2+ locations | Quick save + manage later |
| Delete / Remove | 2+ locations | Inline + batch management |
| Upgrade / Subscribe | 3+ locations | Different moments of value realization |
| Invite / Refer | 2+ locations | Social + settings + after success moment |
| Search / Filter | 3+ locations | Global + context-specific + advanced |
| Feedback / Rating | 2+ locations | After positive experience + settings |

**Check your UC candidate list against this table.** For every action in your app that maps to one of these categories, if it appears only once, find at least one more natural placement. Derive the positions from the PRD's features — don't copy positions from examples.

**Output — Repetition Audit Table (use YOUR app's actions, not example data):**

```
| Action (from your UC list) | Position 1 (Primary Screen) | Position 2 (Contextual Screen) | Position 3 (Discoverable) | Expression Difference |
|---------------------------|----------------------------|------------------------------|--------------------------|----------------------|
| [Action from your app] | [WF-XXX Screen — primary location] | [WF-XXX Screen — secondary location] | [WF-XXX — tertiary location] | [How expression changes across positions] |
| [Next action...] | ... | ... | ... | ... |
```

**The "Expression Difference" column is the most important.** Simply listing the same action at 3 screens is not enough — each repetition must differ meaningfully: different interaction pattern, different information density, different user intent, or different timing.

### 0.4 Screen Architecture Canvas

Before assigning WF-XXX IDs, sketch the full screen hierarchy for YOUR app. This prevents "flat" thinking where every feature gets exactly one screen. Build the hierarchy from the PRD's features and personas — do not copy screen names from examples.

**Rules:**
- App has 3-5 tab-level sections (derive from PRD's main feature groups)
- Each tab can have sub-sections with their own navigation
- Modals, sheets, alerts are FIRST-CLASS screens with their own WF-XXX IDs
- Every screen must have a parent (except root tabs)
- Max depth: 3 levels (Tab → Section → Detail)

**Output — Screen Architecture Canvas (build for YOUR app):**

```
App Root ([App Name from PRD])
├── Tab 1: [Name from PRD feature group] ([Archetype])
│   ├── WF-XXX: [Screen name — derived from feature]
│   ├── WF-XXX: [Screen name — derived from feature]
│   └── [More screens as needed...]
├── Tab 2: [Name from PRD feature group] ([Archetype])
│   ├── WF-XXX: [Screen name — derived from feature]
│   └── ...
├── Tab 3: [Name from PRD feature group] ([Archetype])
│   └── ...
├── Tab 4: [Name from PRD feature group] ([Archetype])
│   └── ...
├── Modals & Overlays (first-class screens)
│   ├── WF-XXX: [Share / Create / Confirm / Pick — as needed by features]
│   ├── WF-XXX: [Name]
│   └── WF-XXX: [Name]
└── System Screens (mandatory for all apps)
    ├── WF-001: Splash
    ├── WF-002: Onboarding
    └── WF-003: IAP / Paywall
```

**Minimum screen count by project size:**
- Small (<5 features): ≥12 screens (including modals/overlays)
- Medium (5-10 features): ≥25 screens
- Large (10+ features): ≥40 screens

If your canvas has fewer screens than the minimum, go back to Step 0.1 — you have not decomposed enough. The screen names in your canvas must come from YOUR Feature Explosion, not from any example.

---

## Step 1: Read Context

Read `PRD.md` and extract:

- **Persona count** determines persona-based scenario sections
- **Feature count** determines user story sections (one section per feature group)
- **MVP scope** determines which UCs appear in Must-Have vs. Should-Have vs. Nice-to-Have
- **Business goals** drive prioritization
- **Screen Inventory (§8)** determines which screens exist and their purposes — REQUIRED for §3, §4, §5

If PRD.md does not exist, stop and report the gap. Never fabricate context.

---

## Step 1.5: Extract Screen Inventory

From PRD §8 Screen Inventory, list all screens with their IDs and descriptions.

If PRD does not have a Screen Inventory section, derive screens from:
- Features listed in PRD §5 (each feature typically needs 1-2 screens)
- Standard mandatory screens (Splash, Onboarding, IAP/Paywall)
- User personas and their goals

Assign WF-XXX IDs to screens. This list feeds into:
- §3 (UC → Screen Mapping)
- §4 (Screen-Context Use Cases)
- §5 (Task Flows)

These WF-XXX IDs will be finalized when Wireframes.md is created. For now, use provisional IDs based on the screen inventory order.

---

## Step 2: Create Directory

Follow `project-docs-lifecycle` Phase 2. Ensure `.claude/specs/[project-name]/` exists before writing.

---

## Step 3: Write Use_Cases.md

**You MUST read `.claude/doc-templates/Use_Cases.md` first** and follow its section layout. Its `QUALITY-GATE-MANIFEST` block (end of the template) is the authoritative list of required sections — do NOT copy that manifest block into the output.

### ID Format

- `UC-XXX` for use case stories (sequential: UC-001, UC-002)
- `AF-XXX.Y` for alternative flows (AF-001.1, AF-001.2)
- `AC-XXX.Y` for acceptance criteria (AC-001.1, AC-001.2)
- `WF-XXX` for wireframe screen references (provisional until Wireframes.md is created)
- `TF-XXX` for task flows (sequential: TF-001, TF-002)

Once assigned, IDs never change. New items get new IDs, no renumbering.

### Document Structure

The required sections (mục lớn + mục con) are defined **only** in the `QUALITY-GATE-MANIFEST`
of `.claude/doc-templates/Use_Cases.md` (single source of truth). Reproduce every
`required_major` and its `required_minor` from the template; do NOT hard-code or re-list them
here. `gate-uc` validates the produced document against that manifest.

### Each UC Entry Must Have

Actor (from PRD personas), goal, preconditions, main flow steps, alternative flows with AF-IDs, postconditions, acceptance criteria with AC-IDs.

**Required fields that bridge to wireframes:**
- **Screens Involved**: List of WF-XXX screens this UC touches
- **Primary Screen**: The WF-XXX screen where the main action happens
- **Entry Point**: How user reaches this UC (screen name or trigger)
- **Exit Point**: Where user goes after completing this UC

**Context Variations** (new — required per UC):
- **First-time user variant**: How does this UC behave when user has no data/is new? Creates alternative flow or state variation.
- **Returning user variant**: How does efficient/familiar usage look different?
- **Power user / Edge case variant**: Advanced shortcuts, recovery from errors, unusual situations.

### §2 bis: Feature Expression Matrix Rules

Every UC that appears on more than one screen MUST be documented in the Feature Expression Matrix. This prevents AI from treating UCs as isolated single-screen actions.

- **Expression Type** column: Describe HOW the UC is expressed differently on each screen (e.g., "Full CTA button" vs "Swipe action" vs "Inline stepper")
- **Context Trigger** column: What causes this expression to appear (e.g., "User swipes item", "User taps search", "User is premium")
- Each UC's primary screen expression is the baseline; secondary expressions must differ meaningfully (different interaction pattern, different information density, different user intent)

### §3: UC → Screen Mapping Rules

- Every UC must map to at least 1 screen in the **Primary Screen** column
- Primary Screen = the screen where the user performs the UC's main action
- Screens Involved = all screens the user passes through in this UC's flow
- The **Screen → UC Coverage** table (§3.2) must show every screen covering at least 1 UC
- Orphan screens (no UC) = quality gate failure
- Orphan UCs (no screen) = quality gate failure

### §4: Screen-Context Use Case Rules

For each screen, define ALL of the following. Missing any field = quality gate failure.

**Screen Identity:**
- **Screen Archetype**: One of: Discovery / Action / Consumption / Management / Social. Choose the PRIMARY archetype — screens can blend 2 but must have 1 dominant.
- **Interaction Density**: Dense (6+ interactive zones) / Medium (3-5) / Light (1-2). Not all screens should be equally dense. Discovery screens are denser than Action screens.

**User Intent & Actions:**
- **User Intent**: First-person statement of why the user is on this screen (e.g., "I want to see what's relevant to me")
- **Primary Action**: The ONE main thing the user wants to do on this screen (becomes the CTA in wireframes)
- **Secondary Actions by Layer** (not just a flat list — organize by purpose):
  - **Layer 2 — Contextual**: Actions directly related to current content (e.g., like, comment, share, save)
  - **Layer 3 — Discovery**: Actions that lead user to new content (e.g., related items, trending, explore more)
  - **Layer 4 — Personal**: Actions related to user's identity/preferences (e.g., customize, filter, settings)

**Content Zones:**
- **Zone A (Hero)**: Primary content — visual-first, above the fold, what user sees first
- **Zone B (Engagement)**: Primary CTA + key interaction — where user takes action
- **Zone C (Discovery)**: Secondary content — recommendations, related, "you might also like"
- **Zone D (Utility)**: Navigation, search, filter, settings — chrome & controls

**Navigation:**
- **Entry Points**: How users arrive at this screen (from which screens, notifications, deep links)
- **Exit Points**: Where users go from this screen

**State Variations with Context** (minimum 3, must include the context):

| State | Context | Layout/Behavior Difference |
|-------|---------|---------------------------|
| **First Visit** | No data, new user | Onboarding hints, empty state with guidance CTA |
| **Returning / Has Data** | Data exists, user familiar | Full content, optimized for efficiency |
| **Power User / Advanced** | Heavy usage, shortcuts | Gestures, quick actions, advanced filter |
| **Offline / Error** | Network issue or failure | Cached content, recovery path, clear next action |

Not all 4 states are required for every screen — but at minimum: First Visit + Returning + Error.

### §5: Task Flow Rules

For each important user task:
- Reference specific screens (WF-XXX) and use cases (UC-XXX) in each step
- Every decision point must have an explicit recovery/alternative path
- Include **Recovery Paths** and **Alternative Paths** as separate subsections
- Every High-priority UC must be covered by at least one task flow

### §5 bis: Sub-Flows & Micro-Interactions

For complex screens (Dense/Medium density), document within-screen interactions. These are NOT screen-to-screen flows — they're interactions that happen WITHIN a single screen.

**When to create a sub-flow:**
- Multi-step process inside one screen (e.g., expand variant → select → update price → confirm)
- Animated transitions between visual states (e.g., collapsed card → expanded detail)
- Inline editing flows (e.g., tap to edit → type → save → show confirmation)
- Progressive disclosure (e.g., "Show more" → expand → "Show less")

**Sub-Flow format:**

```
### SF-XXX: [Sub-Flow Name]
**Parent Screen**: WF-XXX
**Trigger**: [What starts this sub-flow]
**Referenced UCs**: [UC-XXX]

| Step | Component | User Action | System Response | Micro-State |
|------|-----------|-------------|-----------------|-------------|
| 1 | [Name] | [Action] | [Response] | [Loading/Expanded/etc] |

**Visual Transition**: [Describe animation: slide down, fade in, spring expand]
**Haptic**: [None / Light / Medium / Heavy — when appropriate]
```

**Minimum sub-flows:** Every screen with Interaction Density ≥ Medium must have at least 1 sub-flow. Dense screens should have 2-3.

### Scaling

| Project Size | Features | UC Candidates (from Explosion) | Actual UCs | Feature Expressions | Screen-Context | Task Flows | Sub-Flows | Scenarios |
|-------------|----------|-------------------------------|------------|---------------------|-----------------|------------|-----------|-----------|
| Small | < 5 | 15-25 | 10-18 | 20+ (avg 2 per UC) | 12-20 screens | 5-8 | 5-10 (dense/medium screens) | 8-12 |
| Medium | 5-10 | 30-50 | 20-35 | 40+ (avg 2 per UC) | 20-35 screens | 8-15 | 10-20 (dense/medium screens) | 15-25 |
| Large | 10+ | 50+ | 35+ | 70+ (avg 2 per UC) | 35+ screens | 15+ | 20+ (dense/medium screens) | 25+ |

**Key principle:** UC Candidates (from Feature Explosion) > Actual UCs (merged/pruned) > Screens. The explosion should produce MORE ideas than you ultimately use. Pruning is fine. Under-generating is not.

---

## Step 4: Quality Gate and Confirmation

1. Invoke `project-docs-quality-gates` with gate `gate-uc`
2. Fix any issues the gate raises
3. Follow `project-docs-lifecycle` Phase 4: present delivery summary, ask user to approve, modify, or pause

---

## Non-Negotiable Rules

- **Execute Step 0 first.** Creative Decomposition is mandatory. Skip it and the output will be flat and generic.
- **Feature explosion minimum.** Each PRD feature must explode into ≥3 UC candidates. No exceptions.
- **Read PRD first.** No UC creation without PRD context.
- **Extract Screen Inventory early.** §3, §4, §5 all depend on knowing which screens exist.
- **No placeholders.** `[Feature]`, `[Description]`, TBD fail the quality gate.
- **Stable IDs.** UC-XXX, AF-XXX.Y, AC-XXX.Y, TF-XXX, SF-XXX, sequential, never renumbered.
- **Every MVP feature gets at least one UC.** Check against PRD scope.
- **EARS notation for ACs.** WHEN/IF/THEN wording, concrete and testable.
- **Every UC maps to at least one screen.** Orphan UCs fail quality gate.
- **Every screen covers at least one UC.** Orphan screens fail quality gate.
- **Every screen must have an Archetype.** Discovery / Action / Consumption / Management / Social.
- **Every screen must have 4 Action Layers.** Primary + Contextual + Discovery + Personal — even if some layers are empty, the thinking must be done.
- **Every screen must have ≥3 State Variations with Context.** First Visit + Returning + Error minimum.
- **Task flows reference specific WF-XXX and UC-XXX IDs.** No vague "user goes somewhere" language.
- **Dense/Medium screens must have sub-flows.** At least 1 sub-flow per screen with Interaction Density ≥ Medium.
- **Repetition Audit must pass.** Key actions (share, save, delete, upgrade, invite, search, feedback) must appear in ≥2 locations unless explicitly justified as single-location.
- **Minimum screen count by project size.** Small: ≥12, Medium: ≥25, Large: ≥40 screens (including modals/overlays). If below minimum, re-do Step 0.1 Feature Explosion.
- **File safety.** Write only under `.claude/specs/[project-name]/`.
