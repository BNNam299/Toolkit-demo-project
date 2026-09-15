# [Project Name] - Use Cases

## 0. Creative Decomposition Summary

**PURPOSE:** Record the creative thinking that shaped this document. This section proves that features were not simply copied from PRD — they were exploded, stormed, audited, and architected.

### 0.1 Feature Explosion

| PRD Feature | Sub-Features Discovered | UC Candidates | Daily? | Relates To |
|-------------|------------------------|---------------|--------|------------|
| [Feature 1] | [Sub 1, Sub 2, Sub 3...] | UC-XXX → UC-XXX | [Yes/No] | [Related features] |
| [Feature 2] | [Sub 1, Sub 2, Sub 3...] | UC-XXX → UC-XXX | [Yes/No] | [Related features] |

**Explosion Rule Check:**
- Total PRD features: [N]
- Total sub-features discovered: [M] → Must be ≥ 3×N
- Total UC candidates: [K]
- Passes? [Yes / No — if No, re-do explosion]

### 0.2 Repetition Audit

| Action | Position 1 (Primary) | Position 2 (Contextual) | Position 3 (Discoverable) | Expression Difference |
|--------|---------------------|------------------------|--------------------------|----------------------|
| [Action from your UC list] | [WF-XXX — primary screen] | [WF-XXX — secondary screen] | [WF-XXX — tertiary screen] | [How expression changes across positions] |
| [Action from your UC list] | [WF-XXX — primary screen] | [WF-XXX — secondary screen] | — | [How expression changes] |
| [Action from your UC list] | [WF-XXX — primary screen] | [WF-XXX — secondary screen] | [WF-XXX — tertiary screen] | [How expression changes] |

**Audit Rule Check:**
- Actions with only 1 position: [List] → Must be justified below, or add more positions
- Justification for single-position actions: [Explain why each cannot appear elsewhere]

### 0.3 Screen Architecture Canvas

```
App Root
├── Tab 1: [Name] ([Archetype])
│   ├── WF-XXX: [Screen Name]
│   ├── WF-XXX: [Screen Name]
│   └── WF-XXX: [Screen Name]
├── Tab 2: [Name] ([Archetype])
│   ├── WF-XXX: [Screen Name]
│   └── ...
├── Tab 3: [Name] ([Archetype])
│   └── ...
├── Tab 4: [Name] ([Archetype])
│   └── ...
├── Modals & Overlays
│   ├── WF-XXX: [Name] (modal)
│   ├── WF-XXX: [Name] (action sheet)
│   └── WF-XXX: [Name] (alert)
└── System Screens
    ├── WF-001: Splash
    ├── WF-002: Onboarding
    └── WF-003: IAP / Paywall
```

**Screen Count:** [N] total screens (min required: Small ≥12, Medium ≥25, Large ≥40)

### 0.4 Context Storming Highlights

For each major UC, summarize how it changes across user contexts:

| UC | First-Time User | Returning User | Power User / Edge Case |
|----|----------------|----------------|----------------------|
| UC-XXX | [Onboarding, guidance, empty state] | [Efficiency, personalization] | [Shortcuts, advanced, recovery] |
| UC-XXX | [Description] | [Description] | [Description] |

**Rule Check:** Every UC with only 1 context variation is listed here: [List] → Must expand or justify.

---

## 1. Introduction

### 1.1 Purpose
This document describes how users interact with [Project Name] in real-world scenarios, including screen-level intent and cross-screen task flows that directly drive wireframe design.

### 1.2 Scope
Covers all primary and secondary use cases for MVP and post-MVP features. Each UC is mapped to screens and task flows to ensure wireframe completeness.

### 1.3 Document Conventions
- **UC-XXX**: Use Case (sequential: UC-001, UC-002)
- **AF-XXX.Y**: Alternative Flow (AF-001.1, AF-001.2)
- **AC-XXX.Y**: Acceptance Criterion (EARS notation: WHEN/IF/THEN)
- **WF-XXX**: Wireframe Screen (cross-references to Wireframes.md)
- **TF-XXX**: Task Flow (sequential: TF-001, TF-002)

---

## 2. User Stories by Feature Group

**DYNAMIC SECTIONS:** Read `PRD.md` → Create sections based on:
- Feature groups defined in overview
- User personas defined in overview
- MVP scope for current phase
- Screen inventory from PRD §8

### 2.1 [Feature Group Name - from PRD.md]

**Examples for different project types:**
- E-commerce: Authentication, Product Browsing, Search, Cart, Checkout, Payment, Profile, Admin
- SaaS: Dashboard, User Management, Projects, Reports, Settings, Billing
- Social: Authentication, Profile, Feed, Posts, Messaging, Notifications
- Fitness: Authentication, Workout Tracking, Progress, Social, Settings

#### [UC-XXX]: [Use Case Name]
**As a** [user type from PRD.md personas]  
**I want** [action]  
**So that** [benefit]

**Priority**: High / Medium / Low  
**Complexity**: High / Medium / Low

**Preconditions**:
- [List conditions that must be true before this UC]

**Main Flow**:
1. [Step 1 - User action]
2. [Step 2 - System response]
3. [Step 3 - User action]

**Alternative Flows**:
- **[AF-XXX.1]**: [Error scenario]
  - [How system handles it]
- **[AF-XXX.2]**: [Alternative scenario]
  - [System behavior]

**Postconditions**:
- [Expected state after completion]

**Acceptance Criteria**:
- **[AC-XXX.1]**: WHEN [trigger] THEN [behavior]
- **[AC-XXX.2]**: IF [condition] THEN [behavior]

**Screens Involved**: [WF-XXX, WF-XXX — list all screens this UC touches]  
**Primary Screen**: [WF-XXX — the screen where the main action happens]  
**Entry Point**: [How user reaches this UC — screen name or trigger]  
**Exit Point**: [Where user goes after completing this UC]

**Context Variations**:
- **First-time user**: [How does this UC behave for new users? Empty state? Guidance? Different CTA?]
- **Returning user**: [How does efficiency change the flow? Shortcuts? Personalization?]
- **Power user / Edge case**: [Advanced paths, shortcuts, error recovery, undo, bulk actions]

---

### 2.N [Additional Feature Groups - as needed]

**For complex projects, add sections as needed:**
```
### 2.2 [Feature Group 2]
### 2.3 [Feature Group 3]
...
```

**Scaling guidance** (must match `project-docs-uc` SKILL.md):

| Project Size | Features | Sections | UC Candidates (from Step 0.1 Explosion) | Actual UCs |
|---|---|---|---|---|
| Small | < 5 | 1-2 | 15-25 | 10-18 |
| Medium | 5-10 | 3-4 | 30-50 | 20-35 |
| Large | 10+ | 5+ | 50+ | 35+ |

**NOTE:** "UC Candidates" is the output of Step 0.1 Feature Explosion. "Actual UCs" is after pruning/merging. Under-generating candidates is a quality failure — push for ≥3 UC candidates per PRD feature before pruning.

---

## 2 bis. Feature Expression Matrix

**PURPOSE:** Same UC, expressed differently on different screens. This prevents the "1 UC = 1 screen" poverty trap. Every UC that appears on more than one screen must be documented here.

| UC ID | Primary Screen | Primary Expression | Secondary Screen | Secondary Expression | Context Trigger | Expression Difference |
|-------|---------------|-------------------|------------------|---------------------|-----------------|----------------------|
| [UC-XXX from §2] | [WF-XXX — primary screen] | [Expression type: Full CTA / Inline / Swipe / etc.] | [WF-XXX — secondary screen] | [Differently expressed] | [What triggers this version] | [How the two expressions differ] |
| [Same UC — more rows if needed] | — | — | [WF-XXX — tertiary screen] | [Differently expressed] | [What triggers this version] | [How it differs] |
| [Next UC from §2...] | [WF-XXX] | [Expression type] | [WF-XXX] | [Expression type] | [Trigger] | [Difference] |

**Rules:**
- Every High-priority UC MUST appear in this matrix with ≥2 expression rows (unless it truly is a single-screen UC — justify inline)
- Each secondary expression must differ from the primary in at least 2 dimensions: interaction pattern (tap vs swipe vs long-press vs stepper), information density (full vs compact vs minimal), user intent (exploring vs executing vs managing), or timing (proactive vs reactive)
- Derive all screen names and expressions from YOUR app's PRD features. Do not copy screen names from examples.
- If an expression row is identical to another row, merge them — they are not different expressions

**Expression Type Catalog** (reference when filling the "Expression" column — choose the type that matches your feature's interaction):

| Expression Type | Interaction Pattern | Best For | When to Use |
|----------------|--------------------|----------|-------------|
| Full CTA | Prominent button, bottom-aligned | Primary action, high-intent user | User is ready to commit (buy, subscribe, save) |
| Inline Action | Button/toggle within content flow | Secondary action during browsing | User is exploring, action should not interrupt |
| Swipe Action | Hidden until swipe gesture | Quick actions for power users | Frequent actions that need speed |
| Long-Press Menu | Context menu on long hold | Power features, reduced visual clutter | Actions that are useful but not primary |
| Stepper Control | Inline +/- or counter | Quantity changes, item counts | Numeric adjustments in context |
| Compact Row | Single-line with chevron | Settings, discovery of options | List of options, each leading to detail |
| Full-Screen Upsell | Interruptive overlay | Urgent value proposition | Critical moment before value loss |
| Modal / Sheet | Presented on top | Focused single task | Creation, selection, confirmation |
| Inline Expand | Tappable section that reveals more | Progressive disclosure | Details that not everyone needs |
| Empty State CTA | Prominent action when no data | First visit, cleared data | Guide user to first value |
| Success Confirmation | Brief overlay/toast | Task completion feedback | Non-blocking acknowledgment |
| Notification / Badge | Small indicator on icon | Passive discovery | Alert user without interrupting |

---

## 3. Use Case to Screen Mapping

### 3.1 UC → Screen Matrix

**PURPOSE:** Every UC must trace to at least one screen. Every Wireframe screen must cover at least one UC. This matrix bridges user needs (UC) to UI design (WF).

| UC ID | UC Name | Screens Involved | Primary Screen | Entry | Exit |
|-------|---------|-------------------|---------------|-------|------|
| [UC-XXX from §2] | [UC name from §2] | [WF-XXX, WF-XXX — all screens in this UC's flow] | [WF-XXX — main screen] | [How user arrives] | [Where user goes next] |
| [UC-XXX from §2] | [UC name from §2] | [WF-XXX, WF-XXX] | [WF-XXX] | [Entry] | [Exit] |
| [Continue for all UCs in §2...] | ... | ... | ... | ... | ... |

**Rules:**
- Every UC must map to at least 1 screen in the **Primary Screen** column
- Primary Screen = the screen where the user performs the main action of this UC
- Screens Involved = all screens the user passes through in this UC's flow
- Entry = where the user comes from (screen name or trigger like "push notification", "deep link")
- Exit = where the user goes after completing the UC

### 3.2 Screen → UC Coverage

**PURPOSE:** Verify no orphan screens exist. Every screen in Wireframes must serve at least one UC.

| Screen | UCs Covered | Primary UC | Secondary UCs | Screen Purpose |
|--------|------------|------------|---------------|----------------|
| [WF-XXX Screen Name] | [List UC-XXX IDs] | [The UC this screen primarily serves] | [Other UCs served] | [One-line description] |
| [WF-XXX Screen Name] | [List UC-XXX IDs] | [Primary UC] | [Secondary UCs] | [Purpose] |
| [Every screen from §0.3 Canvas must appear here...] | ... | ... | ... | ... |

**Rules:**
- Every screen must cover at least 1 UC (orphans fail quality gate)
- Primary UC = the main UC this screen exists to serve
- Screen Purpose = one-line description of why this screen exists for users

---

## 4. Screen-Context Use Cases

**PURPOSE:** Define what users want WHEN they are ON a specific screen. This drives wireframe layout — the action layers become the screen's UI hierarchy, content zones become layout sections, and archetype determines the design language.

**DYNAMIC SECTIONS:** Generate one subsection per screen from PRD Screen Inventory (§8) and UC→Screen Mapping (§3).

### 4.1 Home Screen (WF-004) — Example

**Screen Archetype**: Discovery  
**Interaction Density**: Dense (6+ interactive zones)

**Source UCs**: UC-001 (Browse products), UC-002 (Search), UC-005 (View recommendations)

**User Intent**: "I want to see what's relevant to me and quickly find what I need"

**Primary Action**:
- Browse content feed (CTA implicit — feed is the default view)

**Secondary Actions by Layer**:
- **Layer 2 — Contextual**: Search bar, notification bell, pull-to-refresh
- **Layer 3 — Discovery**: Story ring at top, "Trending now" section, "Because you viewed X" row
- **Layer 4 — Personal**: Profile avatar (top-right), customize feed preferences (hidden behind avatar)

**Content Zones**:
- **Zone A (Hero)**: Personalized feed or category carousel — visual-first, above the fold
- **Zone B (Engagement)**: Scrollable feed of content cards with inline actions (like, save, quick view)
- **Zone C (Discovery)**: Horizontal scroll sections: "Trending", "New arrivals", "Recommended for you"
- **Zone D (Utility)**: Top bar with search, notification badge, cart icon; Bottom: Tab bar

**Entry Points**:
- Splash screen (after login)
- Tab bar tap (from any tab)
- Push notification tap (deep link to specific content)

**Exit Points**:
- Product detail (tap item in feed)
- Search results (tap search bar)
- Cart (tap cart icon)
- Profile (tap profile)

**State Variations with Context**:

| State | Context | Layout/Behavior Difference |
|-------|---------|---------------------------|
| First Visit | No data, new user | Onboarding cards instead of feed, "Discover your taste" CTA, empty cart badge |
| Returning / Has Data | Data exists, familiar | Full personalized feed, cached content instantly visible, story ring populated |
| Power User | High engagement | Swipe-to-save gestures active, long-press for quick share, advanced sort/filter shortcuts |
| Offline | Network unavailable | Cached feed visible, "Last updated 2h ago" banner, queue actions for sync |
| Error | API failure | Error state with illustration, "Tap to retry" CTA, pull-to-refresh alternative |

---

### 4.N [Additional Screen-Context Use Cases]

**Generate one subsection per screen. Examples by app type:**

**E-commerce screens:**
- 4.1 Home (discovery, browsing)
- 4.2 Product Detail (evaluation, add to cart)
- 4.3 Search / Filter (finding specific items)
- 4.4 Cart (review, modify, proceed)
- 4.5 Checkout (shipping, payment)
- 4.6 Profile (orders, settings)

**SaaS screens:**
- 4.1 Dashboard (overview, quick actions)
- 4.2 Project List (browse, manage)
- 4.3 Project Detail (editing, collaboration)
- 4.4 Reports (viewing, exporting)
- 4.5 Settings (configuration, billing)

**Social screens:**
- 4.1 Feed (consume content, interact)
- 4.2 Profile (manage identity, view stats)
- 4.3 Create Post (compose, publish)
- 4.4 Messaging (conversations, notifications)
- 4.5 Explore (discover, search)

**Scaling guidance:**
- Small project (< 5 screens): Cover every screen
- Medium project (5-10 screens): Cover every screen, group similar secondary screens
- Large project (10+ screens): Cover every screen, prioritize complex screens with multiple UCs

---

## 5. Task Flows

**PURPOSE:** Map how users accomplish specific goals across screens. Each task flow traces a complete user journey from trigger to outcome, referencing specific screens (WF-XXX) and use cases (UC-XXX).

**DYNAMIC SECTIONS:** Generate one subsection per important user task. Prioritize MVP High-priority UCs.

### 5.1 [TF-XXX]: [Task Name — derived from your app's High-priority UCs]

**Trigger**: [What starts this flow — user action, notification, system event]  
**Referenced UCs**: [UC-XXX, UC-XXX — which UCs from §2 does this flow cover]  
**Referenced Screens**: [WF-XXX, WF-XXX — which screens does this flow pass through]

| Step | Screen | User Action | System Response | Decision Point |
|------|--------|-------------|-----------------|----------------|
| 1 | [WF-XXX Screen] | [What user does] | [How system responds] | [Condition? → Next step / Alternative step] |
| 2 | [WF-XXX Screen] | [What user does] | [How system responds] | [Condition? → Next step / Alternative step] |
| 3 | [WF-XXX Screen] | [What user does] | [How system responds] | [Condition? → Next step / Alternative step] |
| ... | ... | ... | ... | ... |

**Recovery Paths**:
- [Error/scenario 1] → [Recovery action] → [Result screen WF-XXX]
- [Error/scenario 2] → [Recovery action] → [Result screen WF-XXX]

**Alternative Paths**:
- [Alternative 1] → [Sequence] → [Outcome]
- [Alternative 2] → [Sequence] → [Outcome]

---

### 5.N [Additional Task Flows — continue for all High-priority UCs]
- Auth failed → Show error → Retry / Forgot password / Try different method
- Network error → Show offline message → Cache credentials → Retry when online

---

### 5.N [Additional Task Flows]

**Generate task flows for major user tasks. Examples by app type:**

**E-commerce:** Purchase product, Search & filter, Manage cart, Track order, Return item
**SaaS:** Create project, Generate report, Invite collaborator, Export data, Manage billing
**Social:** Create post, Follow user, Send message, Manage notifications, Edit profile

**Scaling guidance:**
- Small project: 3-5 task flows (core MVP flows only)
- Medium project: 5-8 task flows (core + secondary flows)
- Large project: 8+ task flows (all major flows, group by user type)

**Task Flow Rules:**
- Every High-priority UC must be covered by at least one task flow
- Each step must reference a specific screen (WF-XXX)
- Every decision point must have a recovery path
- Task flows reference UC IDs — do not redefine behaviors already in §2

---

## 5 bis. Sub-Flows & Micro-Interactions

**PURPOSE:** Document within-screen interactions. Task flows (§5) describe screen-to-screen journeys. Sub-flows describe what happens INSIDE a single screen — state transitions, progressive disclosure, inline editing, animated reveals.

**When to create a sub-flow:** The screen has Interaction Density ≥ Medium (from §4), OR the screen has a multi-step process that stays on the same WF-XXX.

### SF-XXX: [Sub-Flow Name]

**Parent Screen**: WF-XXX  
**Source UC**: UC-XXX, UC-XXX  
**Trigger**: [What starts this sub-flow — user action, system event, timer]  
**Purpose**: [Why this micro-interaction exists — what user problem it solves]

| Step | Component | User Action | System Response | Micro-State | Haptic |
|------|-----------|-------------|-----------------|-------------|--------|
| 1 | [Component name] | [User action] | [System response] | [Default/Loading/Expanded/etc] | [None/Light/Medium/Heavy] |
| 2 | [Component name] | {Decision point} | [Conditional response] | [State after] | — |
| 3 | [Component name] | [User action] | [System response] | [State after] | [Haptic if appropriate] |

**Visual Transition**: [Describe: collapse/expand, slide in/out, fade, spring — with duration]  
**Recovery**: [What happens if user cancels/interrupts/errors]

---

### Example Sub-Flows (for format reference only — replace with your app's sub-flows)

#### SF-001: [Example — e.g., "Expand Product Variants"]
**Parent Screen**: [WF-XXX from your app]  
**Source UC**: [UC-XXX from your app]  
**Trigger**: [User taps selector]  
**Purpose**: [Let user choose variant without leaving the current screen]

| Step | Component | User Action | System Response | Micro-State | Haptic |
|------|-----------|-------------|-----------------|-------------|--------|
| 1 | [Selector] | Tap to expand | Reveal options inline with animation | Expanded | Light |
| 2 | [Option item] | Tap selection | Highlight chosen, update related info | Selected | Light |
| 3 | [CTA Button] | Confirm action | Execute, show confirmation toast | Success | Medium |

**Visual Transition**: [Spring expand, 0.3s, damping 0.7. Related info crossfades.]  
**Recovery**: [Tap outside to collapse without selecting. Tap different option to change.]

#### SF-002: [Example — e.g., "Inline Field Edit"]
**Parent Screen**: [WF-XXX from your app]  
**Source UC**: [UC-XXX from your app]  
**Trigger**: [User taps a read-only field]  
**Purpose**: [Edit content inline with real-time feedback]

| Step | Component | User Action | System Response | Micro-State | Haptic |
|------|-----------|-------------|-----------------|-------------|--------|
| 1 | [Field (read mode)] | Tap field | Enter edit mode, show keyboard, show character counter | Editing | Light |
| 2 | [Field (edit mode)] | Type content | Real-time counter updates, Save button enables | Typing | None |
| 3 | [Save button] | Tap Save | Validate, persist, show "Saved" for 2s, dismiss keyboard | Saved | Light |

**Visual Transition**: [Field highlights on focus. Counter slides in. Confirmation fades after 2s.]  
**Recovery**: [Cancel reverts. Tap outside auto-saves on dismiss.]

---

**Minimum sub-flows:** Every screen with Interaction Density ≥ Medium must have at least 1 sub-flow. Dense screens should have 2-3.

---

## 6. Scenarios

**DYNAMIC:** Generate scenarios based on actual UCs created in Section 2.

### 6.1 Happy Path Scenarios

**Generate one scenario per major UC:**

#### Scenario [N]: [UC-XXX] Happy Path
**Actor**: [From UC definition]  
**Goal**: [From UC definition]

**Steps**:
1. [Step 1 from UC main flow]
2. [Step 2 from UC main flow]
3. [Continue through all steps]

**Expected Outcome**: [UC postconditions achieved]

---

### 6.2 Edge Case Scenarios

**Generate based on alternative flows defined in UCs:**

#### Scenario [N]: [AF-XXX.1] - [Error Name]
**Actor**: [From UC]  
**Context**: [Error condition from alternative flow]

**Steps**:
1. [Steps leading to error]
2. [System error response]
3. [User recovery action]
4. [Resolution]

**Expected Outcome**: [Graceful handling as defined in AF]

---

### 6.3 Persona-Based Scenarios

**Generate based on personas from PRD.md:**

#### Scenario [N]: [Persona Name] - [Goal]
**Actor**: [Persona type]  
**Goal**: [What this persona wants to achieve]

**Steps**:
1. [Persona-specific steps]
2. [Using persona's context]

**Expected Outcome**: [Persona achieves goal]

---

**Scaling guidance:**
- Small project: 3-5 total scenarios
- Medium project: 8-12 scenarios covering major paths
- Large project: 15+ scenarios, group by persona or feature area

---

## 7. Use Case Priorities

### 7.1 Must-Have (MVP)
| ID | Use Case | Priority | Complexity | Primary Screen |
|----|----------|----------|------------|----------------|
| UC-001 | [Use case name from PRD.md] | High | Medium | WF-XXX |
| UC-002 | [Use case name] | High | Medium | WF-XXX |

### 7.2 Should-Have (Post-MVP)
| ID | Use Case | Priority | Complexity | Primary Screen |
|----|----------|----------|------------|----------------|
| UC-006 | [Feature name] | Medium | Medium | WF-XXX |

### 7.3 Nice-to-Have (Future)
| ID | Use Case | Priority | Complexity | Primary Screen |
|----|----------|----------|------------|----------------|
| UC-010 | [Feature name] | Low | Low | WF-XXX |

---

## 8. User Journey Map

**DYNAMIC:** Generate journeys based on personas and UCs from PRD.md.

```
Persona 1 Journey:
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Entry     │ -> │   Action    │ -> │   Action    │ -> │   Exit      │
│  ([UC-XXX]) │    │  ([UC-XXX]) │    │  ([UC-XXX]) │    │   State     │
│   WF-XXX    │    │   WF-XXX    │    │   WF-XXX    │    │   WF-XXX    │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘

Persona 2 Journey:
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Entry     │ -> │   Action    │ -> │   Action    │ -> │   Exit      │
│  ([UC-XXX]) │    │  ([UC-XXX]) │    │  ([UC-XXX]) │    │   State     │
│   WF-XXX    │    │   WF-XXX    │    │   WF-XXX    │    │   WF-XXX    │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
```

**Scaling guidance:**
- Small project (< 3 personas): 2-3 journey diagrams
- Medium project (3-5 personas): 4-6 journey diagrams
- Large project (5+ personas): Group personas by role, create journey per group

**Journey mapping rules:**
1. Start from persona's entry point (app open, notification tap, etc.)
2. Map key actions through major UCs
3. End at meaningful exit state (goal achieved, transaction complete, etc.)
4. Include loop backs for recurring actions (daily usage patterns)
5. Reference WF-XXX screen IDs alongside UC-XXX use case IDs

---

## 9. Screen-Intent Summary

**PURPOSE:** Quick-reference table showing what every screen must support. Wireframe designers use this as the primary input.

| Screen (WF-ID) | Screen Name | Archetype | Density | User Intent | Primary Action | Secondary Actions | Key UCs |
|----------------|-------------|-----------|---------|-------------|----------------|-------------------|---------|
| WF-001 | Splash | Consumption | Light | "Launch app quickly" | Wait for initialization | — | System |
| WF-002 | Onboarding | Discovery | Light | "Learn what this app does" | Complete onboarding | Skip, sign up | UC-010 |
| WF-004 | Home | Discovery | Dense | "See what's relevant" | Browse feed | Search, notifications, cart, profile | UC-001, UC-002 |
| WF-005 | Product Detail | Consumption | Medium | "Decide if I want this" | Add to cart | Save, share, review | UC-001, UC-003 |
| WF-008 | Cart | Management | Medium | "Review and proceed" | Proceed to checkout | Edit quantity, remove item | UC-007, UC-003 |
| WF-009 | Checkout | Action | Medium | "Complete my purchase" | Confirm order | Edit address, apply promo | UC-008 |

**Rules:**
- Every screen from Wireframes must appear in this table
- Archetype = one of: Discovery / Action / Consumption / Management / Social
- Density = Dense (6+ zones) / Medium (3-5) / Light (1-2)
- Primary Action = the one thing users must be able to do on this screen (1 per screen)
- Secondary Actions = additional actions available (1-5 per screen)
- User Intent = first-person statement of why the user is on this screen
- Key UCs = which UCs from §2 are served by this screen

---

**Document Version**: 1.0
**Last Updated**: 2026
**Status**: Draft / In Review / Approved
**Dependencies**: PRD.md

<!-- QUALITY-GATE-MANIFEST:START
# Nguồn chân lý DUY NHẤT cho gate-uc. KHÔNG chép khối này vào file đầu ra ở specs/.
# Bỏ qua các heading placeholder/ví dụ (2.N, 2.2/2.3, 4.N, 5.N, [UC-XXX], SF-XXX, Scenario [N], Example ...).
doc: Use_Cases
gate: gate-uc
required_major:
  - "0. Creative Decomposition Summary"
  - "1. Introduction"
  - "2. User Stories by Feature Group"
  - "2 bis. Feature Expression Matrix"
  - "3. Use Case to Screen Mapping"
  - "4. Screen-Context Use Cases"
  - "5. Task Flows"
  - "5 bis. Sub-Flows & Micro-Interactions"
  - "6. Scenarios"
  - "7. Use Case Priorities"
  - "8. User Journey Map"
  - "9. Screen-Intent Summary"
required_minor:
  "0. Creative Decomposition Summary": ["0.1 Feature Explosion", "0.2 Repetition Audit", "0.3 Screen Architecture Canvas", "0.4 Context Storming Highlights"]
  "1. Introduction": ["1.1 Purpose", "1.2 Scope", "1.3 Document Conventions"]
  "3. Use Case to Screen Mapping": ["3.1 UC → Screen Matrix", "3.2 Screen → UC Coverage"]
  "6. Scenarios": ["6.1 Happy Path Scenarios", "6.2 Edge Case Scenarios", "6.3 Persona-Based Scenarios"]
  "7. Use Case Priorities": ["7.1 Must-Have (MVP)", "7.2 Should-Have (Post-MVP)", "7.3 Nice-to-Have (Future)"]
quality_checks:
  - "§0: Feature Explosion (mỗi feature PRD → >=3 UC), Repetition Audit, Screen Canvas, Context Storming"
  - "UC→Screen: mọi UC map >=1 màn hình; mọi màn hình có >=1 UC (không orphan)"
  - "Screen-Context §4: mỗi màn hình có user intent, đúng 1 primary action, entry/exit, >=2 state"
  - "Task Flows §5: mỗi bước tham chiếu WF-XXX + UC-XXX; có recovery path; mọi High-priority UC được phủ"
  - "Số màn hình tối thiểu theo scale (Small >=12, Medium >=25, Large >=40, gồm modal/overlay)"
  - "ID rõ ràng UC-xxx / AC-xxx.y; mỗi UC có Screens Involved, Primary Screen, Entry Point, Exit Point"
QUALITY-GATE-MANIFEST:END -->
