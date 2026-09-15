---
name: uiux-analysis-workflow
description: Deep UI/UX enrichment workflow. Extracts product DNA from Project_Overview, detects gaps across 5 gap types, enriches screens with brand-aligned creativity. Use after Wireframes.md is approved.
allowed-tools: Read, Write, Edit, Grep, Glob, Bash
skills:
  - ios-ui-ux
  - ios-components
  - uiux-analysis-contract
  - project-docs-quality-gates
---

# UI/UX Analysis Workflow — PRODUCT DNA EDITION

**Core Objective:** NOT to produce comprehensive documentation. It is to make the final app MORE USABLE, MORE DISTINCTIVE, and LESS GENERIC.

**Input Sources (mandatory):**
- `Wireframes.md` → structure, flows, layout
- `Project_Overview.md` → vision, user, value proposition, tone, brand personality, domain constraints

**Output Destination:** `.claude/specs/<project-name>/design-ui/`

---

## Core Rules

1. **All creativity MUST anchor to `Project_Overview.md`** — no generic enrichment
2. **Creativity Contract:** Only propose if it increases:
   - `clarity` — makes UX easier to understand
   - `confidence` — makes user trust the app more
   - `speed` — reduces task completion time
   - `recovery` — helps user recover from errors gracefully
   - `distinctiveness` — makes this app feel like THIS app, not a template

3. **Forbidden:** Enrichments that are purely decorative, trend-following, or "for fun"

4. **Content Classification:**
   - `EXPLICIT` — from wireframe directly
   - `INFERRED` — derived from patterns, marked "based on: ..."
   - `PROPOSED ENRICHMENT` — creative addition, must include:
     - Why UX is better
     - Why it fits this product
     - Which `Project_Overview.md` point it anchors to
     - Value label: `high-value` / `medium-value` / `low-value`

---

## File Naming Convention

Format: `screen-wf###-[slug-name].md`
- Lowercase, spaces → `-`, strip special chars `[^a-z0-9-]`
- Collapse multiple `-`, trim ends, max 50 chars
- Collision: suffix `-1`, `-2`, etc.

---

## Data Sources

| Document | Role |
|----------|------|
| `Wireframes.md` | Screen structure, flows, layouts, explicit components |
| `Project_Overview.md` | Vision, target user, value proposition, tone, brand personality, domain constraints |

---

## Phase 0: Extract Product DNA

**Read:**
1. `.claude/specs/<project-name>/Project_Overview.md`
2. `.claude/skills/ios-ui-ux/SKILL.md`

**Identify Domain Type:**

| Domain | Creative Direction |
|--------|-------------------|
| Beauty | Confidence, preview-first, gentle, self-expression |
| Finance | Trust, safety, auditability, transparency |
| Productivity | Speed, repeatability, shortcuts, efficiency |
| Social | Expression, identity, engagement, connection |
| Learning | Encouragement, low-anxiety progress, celebration |
| Health | Calm, supportive, data-driven, privacy-first |
| E-commerce | Clarity, conversion, trust signals |
| Entertainment | Delight, immersion, personalization |

**Write `design-ui/product-experience-profile.md`:**

```markdown
# Product Experience Profile

## Core Purpose
What does this app help the user accomplish?
[Answer — anchor from Project_Overview.md]

## Target User
Who is the primary user?
[Answer from Project_Overview.md]

## Desired Emotional Outcome
What emotion should the user feel when using this app?
[Answer — derived from Project_Overview.md tone/brand]

## Product Personality (3 traits)
1. [Trait 1] — [brief explanation]
2. [Trait 2] — [brief explanation]
3. [Trait 3] — [brief explanation]

## User Success Moments
- [Moment]: What success looks like, how it feels
- [Moment]: ...

## User Failure Moments
- [Moment]: What failure looks like, how it feels
- [Moment]: ...

## Domain Constraints
[Any technical, regulatory, or UX constraints specific to this domain]
```

---

## Phase 1: Define Creative Direction

**Read:**
1. `design-ui/product-experience-profile.md` (from Phase 0)
2. `.claude/specs/<project-name>/Project_Overview.md`

**Write `design-ui/creative-direction.md`:**

```markdown
# Creative Direction

## How Should This App Feel?
[Answer — emotional description, anchor to product-experience-profile]

## Preferred UX Personality
Primary: [calm / premium / playful / efficient / supportive / confident / trustworthy / empowering]
Secondary: [if applicable]

## UX Personality to AVOID
- [Type to avoid]
- [Type to avoid]

## Motion Philosophy
- [Light & subtle] OR [Bold & expressive]
- Reasoning: [why this fits the product]

## Feedback Tone
- [Warm & friendly] OR [Professional & minimal] OR [Playful & energetic]
- Reasoning: [why this fits the product]

## Brand Expression Guidelines
- What visual elements express this brand: [list]
- What interactions should feel like "this app": [list]
- What should NEVER appear in this app: [list]

## Copy Tone
Derived from Project_Overview.md:
- Voice: [formal / casual / professional / playful]
- Tone: [confident / humble / encouraging / direct]
- Style: [short / descriptive / technical]
- Example phrases: [2-3 examples of this app's voice]

## Domain-Specific Creativity
[Based on domain type identified in Phase 0]
```

---

## Phase 2: Create Directory Structure

```bash
mkdir -p .claude/specs/<project-name>/design-ui/screens
mkdir -p .claude/specs/<project-name>/design-ui/interactions
mkdir -p .claude/specs/<project-name>/design-ui/accessibility
mkdir -p .claude/specs/<project-name>/design-ui/consistency
mkdir -p .claude/specs/<project-name>/design-ui/enrichments
mkdir -p .claude/specs/<project-name>/design-ui/moments
```

---

## Phase 3: 5-Gap Detection

**Read:**
1. `.claude/specs/<project-name>/Wireframes.md`
2. `design-ui/product-experience-profile.md`
3. `design-ui/creative-direction.md`

**Write `design-ui/enrichments/gap-analysis.md`:**

Analyze each screen for ALL 5 gap types:

| Gap Type | What to Look For |
|----------|------------------|
| **State Coverage Gap** | Missing: loading, empty, error, disabled, success, skeleton states |
| **Identity Gap** | Screen looks generic, no product personality visible |
| **Emotional Gap** | No reassurance moments, no delight, no human touch |
| **Guidance Gap** | User has no direction, unclear what to do next, no feedback |
| **Recovery Gap** | No clear recovery path when things go wrong |
| **Brand Expression Gap** | Missing opportunities to show product's unique character |

**Output format per screen:**

```markdown
## Screen: [wf###-name]

### Gap Analysis
| Gap Type | Severity | Evidence from Wireframe | Proposed Enrichment |
|----------|----------|------------------------|---------------------|
| State Coverage | High | List has no loading state | Add skeleton shimmer |
| Identity Gap | Medium | Looks like any app | Add [product-specific] element |
| Emotional Gap | High | No encouragement | Add [moment] |
| Guidance Gap | Low | Next action unclear | Add [hint] |
| Recovery Gap | Medium | Error has no recovery | Add [retry flow] |
| Brand Expression | Low | Generic styling | Add [brand element] |

### Summary
- State gaps: N (High/Medium/Low)
- Identity gaps: N
- Emotional gaps: N
- Guidance gaps: N
- Recovery gaps: N
- Brand expression gaps: N
```

---

## Phase 4: Design System (Enriched)

**Read:**
1. `.claude/specs/<project-name>/Wireframes.md`
2. `.claude/skills/ios-ui-ux/SKILL.md`
3. `.claude/skills/ios-components/SKILL.md`
4. `design-ui/creative-direction.md`

**Write `design-ui/design-system.md`:**

### Token Classification (3-tier)

| Token Type | Mark | Definition |
|------------|------|------------|
| EXPLICIT | `EXPLICIT` | From wireframe directly |
| INFERRED | `INFERRED — based on: [pattern]` | Derived from patterns |
| PROPOSED ENRICHMENT | `PROPOSED ENRICHMENT` | Must include value label + anchor |

**Token sections:**
1. Color System (EXPLICIT from wireframe, PROPOSED for dark mode, etc.)
2. Typography Scale
3. Spacing System (8pt grid baseline)
4. Component Tokens
5. State Tokens (loading, empty, error — most wireframes miss these)
6. iOS Reference Heights (NOT hard constants — mark as INFERRED reference)
7. Animation Tokens (from wireframe → EXPLICIT, else INFERRED/PROPOSED)

**Quality Gate:** `gate-design-system` — 2 retries, then log and proceed.

---

## Phase 5: Moment Design

**Read:**
1. `.claude/specs/<project-name>/Wireframes.md` (main flows)
2. `design-ui/product-experience-profile.md`
3. `design-ui/creative-direction.md`

**Write `design-ui/moments/journey-moments.md`:**

Define moments for the PRIMARY user flow:

| Moment | Definition | User Should Feel | UX Support Pattern | Signature Enrichment |
|--------|------------|-------------------|--------------------|---------------------|
| **Entry Moment** | First impression | [feeling] | [pattern] | [ENRICHMENT — how this app is different] |
| **Decision Moment** | User must choose | [feeling] | [pattern] | [ENRICHMENT] |
| **Waiting Moment** | Loading, processing | [feeling] | [pattern] | [ENRICHMENT] |
| **Success Moment** | Task completed | [feeling] | [pattern] | [ENRICHMENT] |
| **Failure Moment** | Error occurred | [feeling] | [pattern] | [ENRICHMENT — recovery focused, no blame] |
| **Revisit Moment** | Return to app | [feeling] | [pattern] | [ENRICHMENT] |

**Rules for moments:**
- Success moment: Celebrate genuinely, not with marketing fluff
- Failure moment: NEVER blame user, focus on recovery
- Waiting moment: Provide progress indication, not just spinner
- Delight moments: Only if brand allows, and only at `medium-value` or `high-value`

---

## Phase 6: Per-Screen Analysis (Enriched)

For each screen in Wireframes.md:

**Read:**
1. Screen section from `Wireframes.md`
2. `design-ui/enrichments/gap-analysis.md` (this screen's gaps)
3. `design-ui/product-experience-profile.md`
4. `design-ui/creative-direction.md`
5. `.claude/skills/ios-ui-ux/SKILL.md`
6. `.claude/skills/uiux-analysis-contract/SKILL.md`

**Write `design-ui/screens/screen-wf###-[slug-name].md`:**

### Sections:

**1. Metadata**
- screen_id, screen_name, priority, related UC/FR

**2. Purpose** (EXPLICIT from wireframe)

**3. States Defined** (mark EXPLICIT/INFERRED/PROPOSED ENRICHMENT)

| State | Trigger | Visual | Behavior | Mark |
|-------|---------|--------|----------|------|
| Default | — | From wireframe | — | EXPLICIT |
| Loading | API call | Skeleton shimmer | Disabled | INFERRED |
| Empty | No data | Empty state | CTA | PROPOSED ENRICHMENT |
| Error | API fail | Error card | Retry | PROPOSED ENRICHMENT |
| Success | Complete | Checkmark | Auto-dismiss | INFERRED |

**4. Micro-Interactions Table**

| Element | Interaction | Animation | Haptic | Mark |
|---------|-------------|-----------|--------|------|
| Button tap | Scale 95% | 150ms ease-out | Impact light | EXPLICIT |
| Swipe delete | Slide + red | 250ms | Impact medium | PROPOSED ENRICHMENT |

**5. Brand Fit Review** ← NEW
```
Generic Assessment: [YES — this screen looks like any app / NO — has distinctive elements]

Elements showing product DNA:
- [element]: connects to [product personality trait]

Elements still generic:
- [element]: no product personality visible

Brand Alignment: [High/Medium/Low]%
```

**6. Emotional Journey** ← NEW
```
User emotional arc on this screen:
[Start] → [Middle] → [End]

Emotional supports needed:
- At [point]: [reassurance / encouragement / feedback]
- At [point]: [progress indicator / clarity]

Current emotional gaps:
- [gap]: [how to fix]
```

**7. Signature Opportunities** ← NEW (limit to 1-3 per screen)
```
# Signature Opportunity 1: [Name]
What: [description]
Why better UX: [reason]
Why fits this product: [reason]
Anchor to Project_Overview: [specific point]
Value: [high-value / medium-value / low-value]
```

**8. Proposed Enrichments** (with full justification)

| Enrichment | Type | Why Better UX | Why Fits Product | Project_Overview Anchor | Value |
|------------|------|---------------|------------------|------------------------|-------|
| Add skeleton | UX Completeness | Reduces perceived wait | Calm feel | "users should feel confident" | high-value |
| Add swipe archive | UX Completeness | Speed + gesture | Productive feel | "speed is core value" | high-value |

**Enrichment Type Groups:**
- `UX Completeness` — states, transitions, feedback
- `Guidance & Clarity` — hints, labels, navigation support
- `Emotional UX` — reassurance, delight, encouragement
- `Brand Expression` — visual/interaction elements showing product personality
- `Interaction Personality` — micro-interactions that feel like this app
- `Product-Specific Creativity` — domain-aware features

**9. Microcopy Proposals** ← NEW

| Context | Copy | Tone Rationale |
|---------|------|---------------|
| Empty state | [short, specific, actionable] | Clarity first, slight personality |
| Success | [brief confirmation] | Confident, not flashy |
| Validation | [clear instruction] | Helpful, not judgmental |
| Destructive confirm | [warning + action] | Serious but not scary |
| Offline message | [what happened + what to do] | Reassurance, no blame |
| Onboarding hint | [contextual, brief] | Friendly, not patronizing |

**Rule:** Copy must be CLEAR first, personality second. No marketing fluff.

**10. Accessibility (iOS-Specific)** — 12-item checklist

**Quality Gate:** `gate-screen-analysis` — 2 retries, then log and proceed.

---

## Phase 7: Micro-interactions

**Read:**
1. All screen analysis files (Section 4 micro-interactions)
2. `.claude/skills/ios-ui-ux/SKILL.md`

**Write `design-ui/interactions/micro-interactions.md`:**

| Interaction | From | Animation | Haptic | Code Reference |
|-------------|------|----------|--------|---------------|
| All marked: EXPLICIT / INFERRED / PROPOSED ENRICHMENT |

Code snippets marked: `OPTIONAL APPENDIX — implementation reference only`

---

## Phase 8: Accessibility Report

Same structure as before.

**Quality Gate:** `gate-accessibility` — 2 retries.

---

## Phase 9: Consistency Report (conditional)

If score < 80% → full report. If >= 80% → brief note.

**Quality Gate:** `gate-consistency` — 1 attempt.

---

## Phase 10: Analysis Summary with Scores

**Read:** All files from previous phases

**Write `design-ui/analysis-summary.md`:**

### Scoring Metrics

| Score | Definition | How Calculated |
|-------|------------|----------------|
| **UX Completeness** | % of screens with all states defined | (screens with 5+ states / total screens) × 100 |
| **Brand Alignment** | % of screens showing product personality | (screens with brand elements / total screens) × 100 |
| **Distinctiveness** | % of screens with Signature Opportunities | (screens with 1+ signature / total screens) × 100 |
| **Emotional Clarity** | % of screens with emotional journey addressed | (screens with emotional supports / total screens) × 100 |
| **High-Value Enrichments** | ratio of high-value vs total proposed | (high-value count / total proposed) |

### Final Metrics Table

| Metric | Score | Notes |
|--------|-------|-------|
| Screens analyzed | N | — |
| UX Completeness | X% | — |
| Brand Alignment | X% | — |
| Distinctiveness | X% | — |
| Emotional Clarity | X% | — |
| EXPLICIT tokens | X% | — |
| INFERRED tokens | X% | — |
| PROPOSED ENRICHMENT tokens | X% | — |
| High-value enrichments | N | adopted/rejected in review |
| Medium-value enrichments | N | — |
| Low-value enrichments | N | — |

### Product DNA Summary

```
Product: [name]
Domain: [type]
Personality: [3 traits]
Primary UX Personality: [type]
Signature Moments: N defined
Brand Expression Gaps: N found, M filled
```

**Quality Gate:** `gate-analysis-summary` — 2 retries.

---

## Phase 11: Enrichments Review

**Write `design-ui/enrichments/enrichments-review.md`:**

```markdown
# Enrichments Review — Required Before Implementation

All PROPOSED ENRICHMENTS are listed here. Each requires approval.

## Enrichments by Value

### HIGH-VALUE (N) — strongly recommended
| # | Screen | Enrichment | Type | Why Fit Product | Approve |
|---|--------|------------|------|-----------------|---------|
| 1 | wf### | Add skeleton | UX Completeness | Fits calm product feel | [ ] |

### MEDIUM-VALUE (N) — consider carefully
...

### LOW-VALUE (N) — optional, review necessity
...

## Enrichments by Screen
...

## Enrichments by Type
...
```

---

## Phase 12: Final Review (ONLY PAUSE POINT)

Display:
```
✅ UI/UX Analysis Complete

Product DNA Extracted:
- Domain: [type]
- Personality: [3 traits]
- Primary UX: [type]

Scores:
- UX Completeness: X%
- Brand Alignment: X%
- Distinctiveness: X%
- Emotional Clarity: X%

Enrichments Proposed:
- High-value: N (review required)
- Medium-value: N
- Low-value: N

Files created:
- design-ui/product-experience-profile.md    ← NEW
- design-ui/creative-direction.md             ← NEW
- design-ui/enrichments/gap-analysis.md
- design-ui/enrichments/enrichments-review.md
- design-ui/moments/journey-moments.md       ← NEW
- design-ui/screens/ (N screen files with Brand Fit, Emotional Journey, Signature Ops)
- design-ui/interactions/micro-interactions.md
- design-ui/accessibility/accessibility-report.md
- design-ui/consistency/consistency-report.md (conditional)
- design-ui/analysis-summary.md (with scoring)

⏸️ Review required:
1. Approve/reject enrichments in enrichments-review.md
2. Verify product DNA aligns with your vision
```

---

## Quality Gate Contract

| Gate | Pass Criteria | Fail Action | Max Retry |
|------|--------------|-------------|-----------|
| `gate-design-system` | All tokens classified, PROPOSED marked | Fix | 2 |
| `gate-screen-analysis` | All sections + Brand Fit + Emotional + Signature | Add missing | 2 |
| `gate-micro-interactions` | All types + haptic table | Add missing | 2 |
| `gate-accessibility` | WCAG + iOS 12-item checklist | Add missing | 2 |
| `gate-consistency` | Skip if >= 80% | Log score | 1 |
| `gate-analysis-summary` | All 5 scores present | Fix metrics | 2 |

**Escalation:** If gate fails after 2 retries, log to `design-ui/gate-failures.md` and proceed.

---

## Core Philosophy

**The goal is NOT documentation. It is to make the final app:**

- **More usable** — all states covered, clear guidance, good recovery
- **More distinctive** — has product personality, not generic
- **Less generic** — each screen feels like THIS app, not a template

**Creativity is only valid when it anchors to Product DNA from `Project_Overview.md`.**

---

## Trigger

Invoked automatically after Wireframes.md is approved in `/project-docs` workflow.