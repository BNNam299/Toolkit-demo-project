# [Project Name] - Wireframes

## 1. Introduction

### 1.1 Purpose
This document provides visual representations of all screens and UI components for [Project Name].

### 1.2 Design Principles
- **Simplicity**: Clean, uncluttered interfaces
- **Consistency**: Unified design language across screens
- **Accessibility**: Support for VoiceOver, Dynamic Type
- **iOS Native**: Follow Apple Human Interface Guidelines

### 1.3 Design System
- **Typography**: SF Pro (system font) — override via `${typography.scale.*}` from chosen design system token file
- **Color Palette** (placeholder token paths — replace with actual values from your selected design system):
  - Primary: `${color.palette.primary}`
  - Secondary: `${color.palette.secondary}`
  - Success: `${color.palette.success}`
  - Error: `${color.palette.error}`
  - Background: `${color.palette.background}`
  - Text Primary: `${color.palette.textPrimary}`
  - Text Secondary: `${color.palette.textSecondary}`

  > **NOTE:** The above are placeholder token paths. Replace with the actual values from your selected design system token file at `{{IDE_CONFIG_DIR}}shared/DESIGN_TOKEN_[name].json`. Do NOT hardcode iOS default colors (#007AFF, #34C759, #FF3B30, #5856D6) unless your chosen design system explicitly specifies them.
- **Spacing**: 8pt grid system — use `${spacing.xs/sm/md/lg/xl/xxl}` from token file
- **Corner Radius**: `${border.radius.sm/md/lg/xl}` from token file

### 1.4 External References & Fallback

This document references external skills/artifacts that may not exist yet. For each, an
implementing agent MUST have a fallback so it never hits a dead end:

| External reference | If available | Fallback if missing |
|--------------------|--------------|---------------------|
| `ios-components` skill | Use its component definitions | Use inline component list in §4 Common Components |
| `ios-ui-ux` skill | Use its UX guidance | Use §5–§7 (Responsive/Accessibility/Dark Mode) here |
| `mcp-figma` (Framelink) | Extract tokens/specs from Figma | Use the ASCII wireframes + §1.3 Design System here |
| `DESIGN_TOKEN_[name].json` | Use token values | Use token paths in §1.3 as-is; do not hardcode iOS defaults |
| Figma file | Link the file | Mark "(not created)"; wireframes here are authoritative |

---

## 2. Screen Inventory

**REQUIRED SCREENS** (Always include):
| Screen ID | Screen Name | Priority | Related FR | Related UC | Status |
|-----------|-------------|----------|------------|------------|--------|
| [WF-XXX] | Splash Screen | High | - | - | Draft |
| [WF-XXX] | Onboarding | High | - | [UC-XXX] | Draft |
| [WF-XXX] | IAP / Store | High | [FR-XXX] | [UC-XXX] | Draft |

**ADDITIONAL SCREENS** (DYNAMIC based on Functional_Requirements.md):
| Screen ID | Screen Name | Priority | Related FR | Related UC | Status |
|-----------|-------------|----------|------------|------------|--------|
| [WF-XXX] | [Screen from FR] | High/Medium/Low | [FR-XXX] | [UC-XXX] | Draft |

**Screen coverage rule:** Every High-priority FR must have at least one screen.

**Scaling guidance** (must match `project-docs-wireframes` SKILL.md):

| Project Size | Required Screens | Additional Screens | Total |
|---|---|---|---|
| Small (<12 features) | 3 (Splash, Onboarding, IAP) | 9-17 | 12-20 |
| Medium (12-25 features) | 3 | 17-32 | 20-35 |
| Large (25+ features) | 3 | 32+ | 35+ |

**NOTE:** Screen count minimums from Use_Cases.md §0.3 Screen Architecture Canvas take precedence. If UC says ≥25 screens, Wireframes must match.

---

## 2 bis. Screen Taxonomy

**PURPOSE:** Every screen must be classified by archetype. The archetype determines the layout pattern, component priority, and engagement defaults. AI must choose ONE primary archetype per screen.

### Archetype Catalog

| Archetype | Purpose | Layout Pattern | Component Priority | Engagement Default | Example Screens |
|-----------|---------|---------------|--------------------|-------------------|-----------------|
| **Discovery** | Browse, explore, find | Feed / Grid / Carousel, scroll-driven, visual-heavy | Cards, images, CTAs as inline actions | Pull-to-refresh, infinite scroll, skeleton loading, recommendation sections | Home, Explore, Search Results, Categories |
| **Action** | Complete a task | Form / CTA / Progress indicator, single-purpose, minimal | Text fields, buttons, toggles, progress bar | Validation feedback, keyboard handling, loading state on submit | Checkout, Create Post, Settings, Sign Up |
| **Consumption** | Read, watch, listen | Full-bleed / Immersive, minimal chrome, gesture-driven | Media player, text blocks, minimal controls | Full-screen mode, swipe to dismiss, playback controls, dark background | Article, Video Player, Photo Viewer, Product Detail |
| **Management** | Organize, review, control | List / Dashboard, dense information, filterable | Table/List, toggles, search bar, filter chips | Swipe actions, batch operations, sort options, empty state management | Notifications, Orders, File Manager, Admin Dashboard |
| **Social** | Interact, connect, express | Profile / Feed / Comment, micro-action heavy | Avatar, text input, reaction buttons, share sheet | Real-time updates, presence indicators, notification badges, moderation | Profile, Messaging, Comments, Activity Feed |

### Screen Taxonomy Assignment Table

| WF-ID | Screen Name | Primary Archetype | Secondary Archetype (if blended) | Density | Key Behaviors |
|-------|-------------|-------------------|---------|----------|
| WF-001 | Splash | Consumption | — | Light | Auto-dismiss, brand logo, loading indicator |
| WF-002 | Onboarding | Discovery | Action | Light | Swipeable pages, Skip button, Get Started CTA |
| WF-003 | IAP / Paywall | Action | Discovery | Medium | Product comparison, Purchase button, Restore |
| WF-004 | Home | Discovery | — | Dense | Feed, search, notifications, multiple sections |
| WF-005 | Product Detail | Consumption | Action | Medium | Media, description, Add to Cart, price |
| WF-008 | Cart | Management | Action | Medium | List items, edit quantity, checkout CTA |

**Rules:**
- Every screen MUST be assigned a Primary Archetype. Screens without archetype = quality gate failure.
- Screens can blend 2 archetypes (e.g., Product Detail is Consumption + Action) but must declare which is PRIMARY.
- The archetype choice drives which template the screen uses in §3.
- Density must match Use_Cases.md §4 (Screen-Context) and §9 (Screen-Intent Summary).

---

## 3. Screen Sections

**MANDATORY SECTIONS** (Always include):
- 3.1 Splash Screen
- 3.2 Onboarding
- 3.3 IAP / Store

**DYNAMIC SECTIONS** (based on FR categories from Functional_Requirements.md):
- Additional screens as needed by FRs

**Examples by App Type:**
- E-commerce: Splash → Onboarding → IAP → Browse → Search → Cart → Checkout → Order → Profile
- Fitness: Splash → Onboarding → IAP → Workout → Progress → Social → Settings
- Social: Splash → Onboarding → IAP → Feed → Post → Messaging → Profile → Settings
- SaaS: Splash → Onboarding → IAP → Dashboard → Projects → Reports → Settings

**Screen Structure for each screen** (choose template based on Archetype from §2 bis):

Each screen section must include:
0. **Design System** — Token file name in use (e.g., `bento-grid`, `neobrutalism`). All visual values derive from this.
1. **Screen Archetype & Density** (from Use_Cases.md §4 / §9)
2. **Visual Hierarchy** — declares what the user's eye sees 1st, 2nd, 3rd, 4th.
3. **Required Features** (from FR)
4. **UX Enhancements** (beyond FR — archetype-specific defaults from design system's `composition` section)
5. **Content Zones Map** — Zone A/B/C/D with token-based sizes
6. **Layout** — ASCII wireframe using design system component specs
7. **Components** — reference ios-components skill for patterns; token file for visual values
8. **Layout Variants** — minimum 1 variant for key screens
9. **States** — all possible states with context-driven behavior
10. **User Flow** — entry/exit/transitions

---

### Archetype Template A: Discovery Screen

**For screens where user browses, explores, discovers content. Archetype: Discovery.**

#### Template: [WF-XXX] [Screen Name]

**Archetype**: Discovery | **Density**: [Dense/Medium/Light]  
**Design System**: [token-name]  
**Source UC**: [UC-XXX, UC-XXX from Use_Cases.md §4]  
**Source FR**: [FR-XXX from Functional_Requirements.md]

**User Intent** (from Use_Cases.md §4): "[First-person statement]"

#### Visual Hierarchy

1. **[Hero/Featured Content]** — full-width image/carousel, largest element above the fold. First thing user sees.
2. **[Section Headers + Discovery Rows]** — labeled sections like "Trending", "New for You". Scannable, horizontal-scroll cards.
3. **[Feed Cards]** — individual content items below sections. Image + label + inline save button. User scrolls through these.
4. **[Navigation + Chrome]** — search bar (top), tab bar (bottom). Utility, visible but never dominant.

**Self-check:** Is the hero at least 2x the height of any single feed card? Are section headers visually separated from cards (different font weight, divider line)?

#### Required Features (from FR)
- [List features directly from FR]

#### UX Enhancements (Discovery defaults + screen-specific)
- **Pull-to-refresh**: Refresh content with haptic feedback
- **Skeleton loading**: Shimmer placeholders matching card shapes
- **Infinite scroll**: Auto-load next page at 80% scroll depth
- **Discovery sections**: "Trending", "New", "Recommended for you" — at least 2 sections
- **Empty state**: Illustrated empty state with discovery CTA ("Start exploring")
- **Personalization**: Feed ordering based on user behavior
- **Quick actions**: Swipe gestures for common actions (save, share, quick view)
- **Haptic feedback**: Light haptic on pull-to-refresh, medium on item selection

#### Content Zones Map (with iOS Patterns)

```
┌─────────────────────────────────────┐
│ ZONE D: Navigation + Brand          │ ← NavigationStack .toolbar (44pt)
(Zone mapping per project-docs-wireframes Archetype Zone Override Table; default UC labels in parentheses for reference)
│ [Back], Title, [Search], [Cart]     │    .searchable for search bar
├─────────────────────────────────────┤
│ ZONE A: Hero / Featured             │ ← TabView(.page) or ScrollView(.horizontal)
│ (scrollable, ~200pt)                │    Full-bleed, .ignoresSafeArea() optional
│                                     │    Spring animation on page change
├─────────────────────────────────────┤
│ ZONE C: Discovery Sections          │ ← LazyHStack in ScrollView(.vertical)
│ (horizontal scroll rows)            │    Each row: SectionHeader + card collection
│ (variable height, ~140pt per row)   │    .refreshable on parent ScrollView
├─────────────────────────────────────┤
│ ZONE B: Main Feed / Grid            │ ← LazyVStack / LazyVGrid in ScrollView
│ (primary scroll, fills remaining)   │    Each card: 16pt padding, 8pt cornerRadius
│                                     │    .swipeActions for quick save/share
├─────────────────────────────────────┤
│ ZONE D: Tab Bar                     │ ← TabView with .tabItem (49pt + safe area)
│ [Home] [Explore] [Cart] [Profile]   │    SF Symbols + title, badge modifier
└─────────────────────────────────────┘
```

#### Layout

```
┌─────────────────────────────────────────────┐
│ .toolbar: [Search Bar]     [Bell] [Cart(3)]│ ← NavigationStack (44pt)
├─────────────────────────────────────────────┤
│ TabView(.page):                             │ ← ZONE A: Hero (~200pt)
│ ┌─────────────────────────────────────────┐ │
│ │          [Hero Carousel]                │ │   .ignoresSafeArea() top
│ │     SF Symbol page dots ○ ○ ○ ○        │ │
│ └─────────────────────────────────────────┘ │
├─────────────────────────────────────────────┤
│ LazyHStack: "Trending Now"    [See All >]  │ ← ZONE C (~140pt)
│ ┌──────────┐ ┌──────────┐ ┌──────────┐    │
│ │ [Image]  │ │ [Image]  │ │ [Image]  │ →→ │   Each card: 120×140pt
│ │ Label    │ │ Label    │ │ Label    │    │   8pt spacing, 8pt corner
│ └──────────┘ └──────────┘ └──────────┘    │
├─────────────────────────────────────────────┤
│ LazyHStack: "New Arrivals"   [See All >]  │ ← ZONE C (~140pt)
│ ┌──────────┐ ┌──────────┐ ┌──────────┐    │
│ │ [Image]  │ │ [Image]  │ │ [Image]  │ →→ │
│ └──────────┘ └──────────┘ └──────────┘    │
├─────────────────────────────────────────────┤
│ LazyVStack (.refreshable):                  │ ← ZONE B: Feed (fills)
│ ┌─────────────────────────────────────────┐ │
│ │ [Image 16:9]  Product Name             │ │   Row: 120pt height
│ │               $XX.XX   [♡ Save]        │ │   .swipeActions for save
│ └─────────────────────────────────────────┘ │   16pt horizontal padding
│ ┌─────────────────────────────────────────┐ │
│ │ [Image 16:9]  Product Name             │ │
│ │               $XX.XX   [♡ Save]        │ │
│ └─────────────────────────────────────────┘ │
│ ... (LazyVStack infinite scroll via .task)  │
├─────────────────────────────────────────────┤
│ TabView .tabItem:                           │ ← ZONE D: Tab Bar (49pt+34pt)
│ [🏠 Home] [🔍 Explore] [🛒 Cart] [👤 Me]   │   SF Symbols, badge on Cart
└─────────────────────────────────────────────┘
```

#### Layout Variants
**Variant A — Returning User (default above)**
- Full feed, personalized sections, cart badge active

**Variant B — First Visit**
```
┌─────────────────────────────────────┐
│  [App Logo]                         │
├─────────────────────────────────────┤
│                                     │
│      [Welcome Illustration]         │
│                                     │
│    "Discover products you'll love"  │
│                                     │
│       [Start Exploring]             │
│                                     │
│                                     │
├─────────────────────────────────────┤
│  [Home]  [Explore]  [Cart]  [Me]  │
└─────────────────────────────────────┘
```

#### Components
- Navigation → NavSearch (search bar with voice input)
- Cards → CardProductFeed (image, name, price, save icon)
- Cards → CardFeatured (full-width hero, gradient overlay, title)
- Cards → CardHorizontal (compact, for row sections)
- Lists → ListStandard (for section headers with See All)
- TabBar → TabStandard (4 tabs with badge support)
- Reference ios-components skill for detailed specs

#### States

| State | Context | Layout/Behavior |
|-------|---------|----------------|
| **Default** | Returning user, data exists | Full layout as above, personalized feed |
| **First Visit** | New user, no data | Layout Variant B — onboarding CTA, empty feed |
| **Loading (Initial)** | App first launch | Skeleton cards matching layout, shimmer animation |
| **Loading (More)** | Scrolling down | Skeleton cards appended below existing content |
| **Empty (Search)** | No results for query | Illustration + "No results for [query]" + suggested searches |
| **Offline** | Network unavailable | Cached feed + "Last updated X ago" banner |
| **Error** | API failure | Error illustration + "Something went wrong" + Retry button |

#### User Flow
- **Entry**: Splash → Home (default tab), or Tab bar tap
- **Exit**: Product Detail (tap item), Search Results (tap search), Cart (tap icon)
- **Transitions**: Push to product detail, Modal for quick view, Crossfade on feed refresh

---

### Archetype Template B: Action Screen

**For screens where user completes a focused task. Archetype: Action.**

#### Template: [WF-XXX] [Screen Name]

**Archetype**: Action | **Density**: [Medium/Light]  
**Source UC**: [UC-XXX] | **Source FR**: [FR-XXX]

**User Intent** (from Use_Cases.md §4): "[First-person statement]"

#### Visual Hierarchy

1. **[Context/Summary]** — what is being acted on. Compact, always visible. User must know WHAT they're doing.
2. **[Input Fields]** — largest tappable area. Focus ring visible. Label above, placeholder inside. User spends most time here.
3. **[CTA Button]** — highest contrast color, fixed at bottom. Enabled only when form is valid. User completes the task here.
4. **[Navigation]** — back/cancel top-left. Escape route, minimal visual weight.

**Self-check:** Is the CTA at least 50pt tall with 16pt horizontal padding? Is the CTA disabled (grayed out) when required fields are empty? Are input fields at least 44pt tall (touch target minimum)?

#### Required Features (from FR)
- [List features]

#### UX Enhancements (Action defaults)
- **Progress indicator**: Step X of Y for multi-step actions
- **Inline validation**: Real-time validation with check/cross marks
- **Keyboard handling**: Return key advances to next field, toolbar with Done
- **Confirmation dialog**: Before destructive actions
- **Success feedback**: Animation + brief confirmation ("Order placed ✓")
- **Error recovery**: Specific error message with fix guidance, not generic "Error"
- **Auto-save**: Save draft on dismiss for long forms
- **Undo**: Brief undo option after completion ("Undo?" toast)

#### Content Zones Map (with iOS Patterns)

```
┌─────────────────────────────────────┐
│ ZONE D: Navigation                  │ ← NavigationStack .toolbar (44pt)
│ (Zone mapping per project-docs-wireframes Archetype Zone Override Table; default UC labels in parentheses for reference)
│ [Cancel/Back], Title, [Done/Save]  │    .toolbar placement: .cancellationAction
├─────────────────────────────────────┤
│ ZONE A: Context / Summary           │ ← HStack / VStack, non-scrollable
│ (compact, non-scrollable, ~60pt)    │    Shows item being acted on (order, item)
├─────────────────────────────────────┤
│ ZONE B: Input / Action Area         │ ← ScrollView + VStack
│ (scrollable if >3 fields)           │    Each field: 44pt min height
│                                     │    .focused() for keyboard handling
│                                     │    @FocusState for next field on Return
├─────────────────────────────────────┤
│ ZONE B: Primary CTA                 │ ← .safeAreaInset(edge: .bottom)
│ (fixed bottom, 50pt + safe area)    │    Button 50pt, full-width minus 32pt padding
│                                     │    .disabled() when form invalid
└─────────────────────────────────────┘
```

#### Layout

```
┌────────────────────────────────────────────┐
│ NavigationStack .toolbar:                   │
│  [< Back]    Checkout                      │ ← 44pt
├────────────────────────────────────────────┤
│  Order Summary (HStack)        [Expand v]  │ ← ZONE A (~60pt)
│  3 items · $XX.XX                         │    .contextMenu for details
├────────────────────────────────────────────┤
│  ScrollView { VStack(spacing: 16) }        │ ← ZONE B: Form
│                                            │
│  Text("Shipping Address")  .font(.headline)│
│  ┌────────────────────────────────────────┐│
│  │ TextField("Full Name")                 ││   44pt height, 8pt corner
│  └────────────────────────────────────────┘│   .textFieldStyle(.roundedBorder)
│  ┌────────────────────────────────────────┐│
│  │ TextField("Street Address")            ││   44pt height
│  └────────────────────────────────────────┘│
│  HStack(spacing: 12) {                     │
│  ┌──────────────────┐ ┌──────────────────┐ │
│  │ TextField("City")│ │ TextField("ZIP") │ │   44pt each
│  └──────────────────┘ └──────────────────┘ │
│  }                                         │
│                                            │
│  Text("Payment Method") .font(.headline)   │
│  ┌────────────────────────────────────────┐│
│  │ [Visa icon] •••• 4242       [Edit >]  ││   .contextMenu for options
│  └────────────────────────────────────────┘│   48pt height
│                                            │
├────────────────────────────────────────────┤
│ .safeAreaInset(edge: .bottom):             │ ← ZONE B: CTA (50pt + safe)
│  ┌────────────────────────────────────────┐│
│  │          [    Pay $XX.XX    ]          ││   50pt height, full-width-32pt
│  └────────────────────────────────────────┘│   .disabled(when form incomplete)
└────────────────────────────────────────────┘
```

#### Components
- Navigation → NavStandard (Back + Title)
- Text Fields → TFField (standard), TFSecure (payment)
- Buttons → BtnPrimary (submit/pay), BtnText (edit/expand)
- Alerts → AlertDestructive (cancel confirmation)
- Reference ios-components skill

#### States

| State | Context | Layout/Behavior |
|-------|---------|----------------|
| **Default** | Normal data entry | All fields enabled, CTA active |
| **Validating** | User tabs out of field | Inline check/cross, field border green/red |
| **Submitting** | User taps CTA | Button shows spinner, all fields disabled |
| **Success** | Action completed | Success animation, auto-navigate after 1.5s |
| **Validation Error** | Invalid input | Highlight field in red, show message below field, CTA disabled |
| **Network Error** | Submit fails | Alert: "Could not complete. Check connection." + Retry/Cancel |

#### User Flow
- **Entry**: From previous screen (push) or modal presentation
- **Exit**: Success → Confirmation screen, Cancel → Previous screen with confirmation
- **Transitions**: Push for success, modal dismiss for cancel

---

### Archetype Template C: Consumption Screen

**For screens where user reads, watches, or views content. Archetype: Consumption.**

#### Template: [WF-XXX] [Screen Name]

**Archetype**: Consumption | **Density**: [Light/Medium]  
**Source UC**: [UC-XXX] | **Source FR**: [FR-XXX]

**User Intent**: "[First-person immersion or evaluation statement]"

#### Visual Hierarchy

1. **[Media]** — full-bleed image/video, edge-to-edge. Maximum screen real estate. User immerses here.
2. **[Key Info]** — title, price, rating. Sticky below media, always visible even on scroll. User evaluates here.
3. **[Primary Action]** — FAB or sticky bar. High contrast. User acts here.
4. **[Secondary Content]** — description, specs, reviews, related items. Below the fold, scroll-to-discover. User dives deeper here.

**Self-check:** Does the media occupy at least 50% of screen height on first load? Is key info always visible (sticky behavior)? Is the primary action reachable with one thumb (bottom half of screen)?

#### Required Features (from FR)
- [List features]

#### UX Enhancements (Consumption defaults)
- **Full-bleed media**: Edge-to-edge images/video, immersive
- **Minimal chrome**: Navigation hides on scroll, only essential controls visible
- **Gesture navigation**: Swipe to go back, pinch to zoom, double-tap to like
- **Dark background**: For media-rich content, dark chrome reduces distraction
- **Progressive info**: Title/price always visible, details scroll below fold
- **Quick actions float**: Floating action buttons for primary actions (buy, save, share)

#### Content Zones Map (with iOS Patterns)

```
┌─────────────────────────────────────┐
│ ZONE A: Hero Media                  │ ← TabView(.page) for carousel
│ (Zone mapping per project-docs-wireframes Archetype Zone Override Table; default UC labels in parentheses for reference)
│ (fills top 50-60%, fixed)           │    .ignoresSafeArea() for full-bleed
│                                     │    Pinch-to-zoom gesture
│                                     │    .overlay for back/share buttons
├─────────────────────────────────────┤
│ ZONE B: Key Info + CTA (sticky)     │ ← VStack pinned via ScrollView + .safeAreaInset
│ (compact, always visible)           │    Title + price + rating + CTA button
│                                     │    Stays visible when user scrolls below
├─────────────────────────────────────┤
│ ZONE C: Detailed Content            │ ← ScrollView(.vertical)
│ (scrollable, fills remaining)       │    Description, specs, reviews, related items
│                                     │    "Show more" with .animation
│                                     │    Related items: LazyHStack
│                                     │
└─────────────────────────────────────┘
```

#### Layout

```
┌─────────────────────────────────────────────┐
│ ZStack (ignoresSafeArea top):               │
│ ┌─────────────────────────────────────────┐ │ ← ZONE A: Hero (full-bleed)
│ │                                         │ │   TabView(.page)
│ │           [Product Image]               │ │
│ │                                         │ │
│ │ ZStack .overlay(alignment: .topLeading):│ │
│ │  [<]  ← translucent circle button      │ │   44×44pt touch target
│ │ ZStack .overlay(alignment: .topTrailing):│ │
│ │                     [Share]             │ │   44×44pt
│ │ ZStack .overlay(alignment: .bottom):    │ │
│ │  ○ ○ ○ ○  ← TabView page indicators    │ │
│ └─────────────────────────────────────────┘ │
├─────────────────────────────────────────────┤
│ .safeAreaInset(edge: .top):                 │ ← ZONE B: Key Info (sticky)
│  VStack(alignment: .leading, spacing: 4) {  │
│   Text("Product Name") .font(.title2)       │
│   HStack { Text("$XX.XX") Spacer()          │
│            Text("★ 4.8 (2.3k)") }          │
│   ┌───────────────────────────────────────┐ │
│   │        [    Add to Cart    ]          │ │   50pt, full-width
│   └───────────────────────────────────────┘ │   .disabled if out of stock
│  }                                          │
├─────────────────────────────────────────────┤
│ ScrollView(.vertical) {                     │ ← ZONE C: Details
│  VStack(alignment: .leading, spacing: 16) { │
│   Text("Description") .font(.headline)      │
│   Text("Lorem ipsum...") .lineLimit(3)      │   "Show more" → .lineLimit(nil)
│                                             │
│   Text("Size & Fit")                        │
│   Text("Model wears size M...")             │
│                                             │
│   Divider()                                 │
│   Text("Reviews (2.3k)")                    │
│   ┌───────────────────────────────────────┐ │   Each review card:
│   │ ★★★★★  "Great product!"              │ │   16pt padding, 8pt corner
│   │ User123  · 2 days ago                │ │
│   └───────────────────────────────────────┘ │
│   [See all reviews >]                       │
│                                             │
│   Text("You Might Also Like")               │
│   ScrollView(.horizontal) {                 │
│    LazyHStack(spacing: 12) {                │
│     ┌──────┐ ┌──────┐ ┌──────┐            │   120×140pt cards
│     │ Img  │ │ Img  │ │ Img  │ →→         │
│     └──────┘ └──────┘ └──────┘            │
│    }                                        │
│   }                                         │
│  }                                          │
│ }                                           │
└─────────────────────────────────────────────┘
```

#### Components
- Navigation → NavMinimal (transparent overlay, back + share)
- ImageCarousel → CarouselGallery (swipeable, page dots)
- Buttons → BtnPrimary (Add to Cart, full-width)
- Cards → CardReview (star rating, user, date, content)
- Cards → CardHorizontal (related items)
- Reference ios-components skill

#### States

| State | Context | Layout/Behavior |
|-------|---------|----------------|
| **Default** | Product loaded | Full layout as above |
| **Loading** | Fetching product | Skeleton image + shimmer text blocks |
| **Image Loading** | Media heavy | Blur-up placeholder → full resolution on load |
| **Out of Stock** | Inventory zero | CTA changes to "Notify When Available" with email field |
| **Error** | Product not found | Illustration + "Product unavailable" + Browse similar CTA |
| **Offline** | No connection | Cached product data + "Offline" banner |

#### User Flow
- **Entry**: Push from Home/Feed/Search, or deep link
- **Exit**: Back to previous screen (swipe right or tap back), Cart (tap CTA)
- **Transitions**: Hero image shared element transition from feed
- **Interaction**: Pinch to zoom images, swipe between images, double-tap to like

---

### Archetype Template D: Management Screen

**For screens where user organizes, reviews, or controls data. Archetype: Management.**

#### Template: [WF-XXX] [Screen Name]

**Archetype**: Management | **Density**: [Dense/Medium]  
**Source UC**: [UC-XXX] | **Source FR**: [FR-XXX]

**User Intent**: "[First-person organization or control statement]"

#### Visual Hierarchy

1. **[Filter/Sort Bar]** — user needs to narrow down before scanning. Top of list, compact, 44pt.
2. **[List Rows]** — primary content, scanning from top to bottom. Each row: icon/avatar (leading), title + subtitle + metadata (center), chevron or count (trailing). 
3. **[Swipe Actions]** — revealed on demand, not visible by default. Left swipe = primary action, right swipe = destructive.
4. **[Action Bar]** — appears only in edit mode. "X selected" + action buttons. Temporary, contextual.

**Self-check:** Can user scan 6-8 rows without scrolling? Are row heights consistent (60-72pt)? Is the sort/filter bar always visible or does it collapse on scroll? Are swipe actions tappable at 44pt minimum height?

#### Required Features (from FR)
- [List features]

#### UX Enhancements (Management defaults)
- **Swipe actions**: Leading swipe (primary action), trailing swipe (destructive)
- **Batch operations**: Edit mode with select all, multi-select, bulk delete
- **Sort & Filter**: Sort picker (date, name, status) + filter chips
- **Search within list**: Context search bar that filters current list
- **Empty state management**: Different empty states for "no items" vs "all filtered out" vs "all completed"
- **Undo**: After delete/archive action, brief "Undo" toast (5 seconds)
- **Pull-to-refresh**: Refresh list, preserve scroll position

#### Content Zones Map (with iOS Patterns)

```
┌─────────────────────────────────────┐
│ ZONE D: Navigation + Tools          │ ← NavigationStack .toolbar (44pt)
│ (Zone mapping per project-docs-wireframes Archetype Zone Override Table; default UC labels in parentheses for reference)
│ [Back], Title, [Edit], [Sort]      │    .toolbar: .navigationBarLeading/Trailing
│ Filter Chips: [All] [Unread] [Read]│    Picker or Menu for sort options
│ (44pt filter bar below nav)        │    ScrollView(.horizontal) for chips
├─────────────────────────────────────┤
│ ZONE B: Actionable List             │ ← List / ForEach with .swipeActions
│ (scrollable, fills remaining)       │    .listStyle(.plain)
│                                     │    Row: 60-72pt height, 16pt padding
│  ● [Icon] Title           [Meta]   │    Leading: SF Symbol circle (unread dot)
│     Subtitle · timestamp            │    .swipeActions(edge: .leading) { read }
│  ○ [Icon] Title           [Meta]   │    .swipeActions(edge: .trailing) { delete }
│     Subtitle · timestamp            │    .onDelete for edit mode
│                                     │
├─────────────────────────────────────┤
│ ZONE D: Edit Mode Bar (conditional) │ ← .toolbar replacement in editMode
│ [Cancel]  "X Selected"  [Delete]   │    Appears when Edit tapped
│ (48pt, fixed bottom)               │    Disappears on Cancel/Done
└─────────────────────────────────────┘
```

#### Layout

```
┌────────────────────────────────────────────┐
│ NavigationStack .toolbar (44pt):            │
│  [< Back]  Notifications    [Edit] [Sort] │
│  ScrollView(.horizontal): [All][Unread][Read] │ ← ChipFilter (44pt)
├────────────────────────────────────────────┤
│ List {                                      │ ← ZONE B: List (fills)
│  ForEach(items) { item in                   │
│   ● ┌────────────────────────────────────┐  │   Row: 64pt height
│   │ [Icon 40pt]  Order Confirmed  2h ago │  │   .swipeActions(edge: .leading) {
│   │              Your order #1234...     │  │     Button("Read") }
│   └────────────────────────────────────┘  │  │   .swipeActions(edge: .trailing) {
│   ○ ┌────────────────────────────────────┐  │     Button("Delete", role: .destructive) }
│   │ [Icon 40pt]  Payment Processed  Yest │  │
│   │              $XX.XX charged to Visa  │  │
│   └────────────────────────────────────┘  │  │
│   ○ ┌────────────────────────────────────┐  │
│   │ [Icon 40pt]  Welcome to [App]    Wed │  │
│   │              Tap to get started!     │  │
│   └────────────────────────────────────┘  │  │
│  }                                         │
│ } .listStyle(.plain)                        │
│ .refreshable { await sync() }               │
├────────────────────────────────────────────┤
│ Edit Mode (conditional):                    │ ← ZONE D: Edit bar (48pt)
│  HStack {                                   │
│   Button("[Cancel]")  Spacer()              │   Appears on Edit tap
│   Text("3 Selected")  Spacer()              │
│   Button("[Delete]", role: .destructive)    │
│  } .padding(.horizontal, 16)                │
└────────────────────────────────────────────┘
```

#### Components
- Navigation → NavStandard (Back + Edit)
- Lists → ListSwipe (with leading + trailing actions)
- Buttons → BtnText (Filter/Sort), BtnDestructive (Delete)
- Search → TFFilter (inline filter, not full search)
- Chips → ChipFilter (All/Unread/Read)
- Reference ios-components skill

#### States

| State | Context | Layout/Behavior |
|-------|---------|----------------|
| **Default** | Items exist | Full list, sort/filter active, swipe actions enabled |
| **Loading** | First load | Skeleton rows (icon circle + text lines) |
| **Empty (No items)** | No data ever | Illustration + "No notifications yet" + CTA |
| **Empty (Filtered)** | Active filter, zero matches | "No results for [filter]" + Clear filter button |
| **Empty (All done)** | All items completed/read | "All caught up! 🎉" + celebration state |
| **Edit Mode** | User tapped Edit | Checkboxes visible, bottom action bar appears |
| **Offline** | No connection | Cached list + "Offline" badge |
| **Error** | Sync failure | Error banner with retry, list still visible |

#### User Flow
- **Entry**: Tab bar tap, or push from related screen
- **Exit**: Detail view (tap row), Previous screen (back)
- **Transitions**: Push for detail, Edit mode slides in action bar, swipe reveals actions

---

### Archetype Template E: Social Screen

**For screens where user interacts with other users. Archetype: Social.**

#### Template: [WF-XXX] [Screen Name]

**Archetype**: Social | **Density**: [Medium/Dense]  
**Source UC**: [UC-XXX] | **Source FR**: [FR-XXX]

**User Intent**: "[First-person social interaction statement]"

#### Visual Hierarchy

1. **[Identity]** — avatar + username. User needs to know WHO before reading WHAT. Top-left, 40-48pt avatar.
2. **[Content]** — post text, image, media. Main body. Full-width, below identity. User reads/views here.
3. **[Reactions]** — like, comment, share, repost. Below content, compact row of icon buttons. Lightweight.
4. **[Compose/Input]** — only on messaging/comment screens. Fixed bottom with TextField. Appears when user chooses to engage.

**Self-check:** Is the avatar at least 40pt (recognizable)? Are reaction buttons ≥44pt touch target? Is the compose bar's text field expanding (not fixed height)? Is "Report/Block" accessible but not prominent (behind ••• menu)?

#### UX Enhancements (Social defaults)
- **Real-time indicators**: Online presence dots, typing indicators, read receipts
- **Reaction system**: Quick reaction picker (long-press or double-tap)
- **Share & Repost**: Share sheet with platform options
- **Report / Block**: Accessible but not prominent (behind ••• menu)
- **Content moderation cues**: "Sensitive content" warnings, spoiler tags
- **Notification badge sync**: Badge counts update across app in real-time

#### Content Zones Map (with iOS Patterns)

```
┌─────────────────────────────────────┐
│ ZONE D: Profile Header              │ ← VStack (scrolls away with content)
│ (Zone mapping per project-docs-wireframes Archetype Zone Override Table; default UC labels in parentheses for reference)
│ Avatar(40-48pt) + Name + Bio + Stats│    .contextMenu on avatar for options
│ [Follow] [Message] buttons          │    44pt height buttons, full-width or split
├─────────────────────────────────────┤
│ ZONE B: Content / Activity          │ ← List / LazyVStack in ScrollView
│ (scrollable, fills remaining)       │    Each item: identity + content + reactions
│                                     │    Post card: 16pt padding, 8pt corner
│                                     │    Reaction bar: 4 icons, 44pt touch each
│                                     │
│                                     │
├─────────────────────────────────────┤
│ ZONE B: Compose / Input (conditional)│ ← .safeAreaInset(edge: .bottom)
│ (fixed bottom, 56pt + safe area)    │    TextField + attachment + send button
│                                     │    Only on messaging/comments screens
└─────────────────────────────────────┘
```

#### Layout (Profile example)

```
┌──────────────────────────────────────────────┐
│ NavigationStack .toolbar (44pt):              │
│  [<]  @username                    [•••]     │ ← .contextMenu for Report/Block
├──────────────────────────────────────────────┤
│ ScrollView { VStack {                        │
│  // ZONE D: Header                           │
│  HStack(spacing: 12) {                       │
│   ┌────┐                                     │
│   │    │  ← Circle, 48pt, overlay border     │   AsyncImage
│   │Avtr│                                     │
│   └────┘                                     │
│   VStack(alignment: .leading) {              │
│    Text("Display Name") .font(.title3)       │
│    Text("@username") .foregroundStyle(.gray) │
│    Text("Bio text here...") .lineLimit(3)    │
│   }                                          │
│  }                                           │
│  HStack(spacing: 24) {                       │
│   Text("1.2K") + Text("Following")           │   Tappable stats
│   Text("500")  + Text("Followers")           │
│   Text("300")  + Text("Likes")               │
│  } .font(.caption)                           │
│  HStack(spacing: 12) {                       │
│   ┌──────────────────────┐                   │
│   │    [  Follow  ]      │   ← 44pt         │   BtnPrimary
│   └──────────────────────┘                   │
│   ┌──────────────────────┐                   │
│   │    [  Message ]      │   ← 44pt         │   BtnSecondary
│   └──────────────────────┘                   │
│  }                                           │
│                                              │
│  Divider()                                   │
│                                              │
│  // ZONE B: Posts                            │
│  ForEach(posts) { post in                    │
│   VStack(alignment: .leading, spacing: 8) {  │   Post card
│    HStack {                                   │
│     Circle() .frame(32)   ← small avatar     │
│     VStack(alignment: .leading) {            │
│      Text("Username") .font(.subheadline)    │
│      Text("2h ago") .font(.caption)          │
│     }                                        │
│     Spacer()                                 │
│     Button("•••") { }  ← .contextMenu        │
│    }                                         │
│    Text("Post content here...")              │
│    ┌──────────────────────────────────────┐  │
│    │           [Image attached]           │  │   .aspectRatio(contentMode: .fill)
│    └──────────────────────────────────────┘  │
│    HStack(spacing: 32) {                     │   Reaction bar
│     Button { } label: { Image(systemName:"heart") Text("234") } │ 44pt touch
│     Button { } label: { Image(systemName:"bubble") Text("45") } │
│     Button { } label: { Image(systemName:"arrow.2.squarepath") Text("12") }
│     Spacer()                                 │
│     Button { } label: { Image(systemName:"bookmark") }          │
│    } .buttonStyle(.borderless)               │
│   } .padding(16)                             │   Card padding
│  }                                           │
│ }                                            │
│ }                                            │
└──────────────────────────────────────────────┘
```

#### Components
- Navigation → NavStandard (back + more options)
- Avatar → AvatarLarge, AvatarSmall
- Buttons → BtnPrimary (Follow), BtnSecondary (Message)
- Cards → CardPost (avatar, username, content, media, reactions)
- Input → TFCompose (text + attachment + send)
- Reference ios-components skill

#### States (same pattern as other archetypes — Default, Loading, Empty, Error, Offline)

#### User Flow
- **Entry**: From feed, search, notification, or deep link
- **Exit**: Back, or navigate to related profiles/content
- **Transitions**: Push for detail views, modal for composer, sheet for reactions

---

**Scaling guidance:**
- Small project (< 12 screens): Use archetype templates directly, 2-4 dynamic sections
- Medium project (12-25 screens): Customize each archetype instance, 5-8 sections
- Large project (25+ screens): Add screen-specific variations within archetypes, 9+ sections

---

## 4. Common Components

<!-- NOTE: Detailed iOS component catalog (Navigation Bar, Buttons, Text Fields, Cards, Lists, Alerts, Dialogs, Bottom Sheets, Snackbars) is available in the ios-components skill. Reference it when implementing. -->

### 4.1 Navigation
- Standard iOS navigation patterns (NavigationStack, TabView, Sheet)
- Reference ios-components skill for detailed specs

### 4.2 Core UI Elements
- Buttons (Primary, Secondary, Text)
- Text Fields (Standard, Secure, Search)
- Cards (Content, Action, List Item)
- Lists (Plain, Grouped, Inset)
- Reference ios-components skill for detailed specs

### 4.3 Feedback Components
- Alerts (System, Custom)
- Dialogs (Confirmation, Input, Selection)
- Bottom Sheets (Partial, Medium, Full)
- Snackbars / Toast
- Reference ios-components skill for detailed specs

---

## 5. Responsive Design

### 5.1 Device Support
- iPhone SE (375pt width) - Minimum
- iPhone 14 (390pt width) - Primary
- iPhone 14 Pro Max (430pt width) - Large
- iPad (768pt width) - Optional

### 5.2 Orientation
- Portrait: Primary
- Landscape: Supported for main screens

### 5.3 Adaptive Layout
- Use Auto Layout with constraints
- Stack views for flexible layouts
- Safe area insets respected
- Dynamic Type support

---

## 6. Accessibility

### 6.1 VoiceOver
- All interactive elements labeled
- Meaningful labels (not "Button")
- Logical reading order

### 6.2 Dynamic Type
- All text scales with system settings
- Minimum 11pt, maximum 34pt
- Layout adapts to larger text

### 6.3 Color Contrast
- Text: 4.5:1 minimum
- Interactive elements: 3:1 minimum
- Support for high contrast mode

### 6.4 Touch Targets
- Minimum: 44x44pt
- Recommended: 48x48pt
- Adequate spacing between targets

---

## 7. Dark Mode

All screens support dark mode with:
- System background colors
- Elevated backgrounds for cards
- Adjusted shadows and borders
- Semantic colors (not hardcoded)

---

## 8. Design Assets

### 8.1 Icons
- SF Symbols for system icons (preferred)
- Custom icons: 24x24pt, 1pt stroke
- Asset catalog with light/dark variants

### 8.2 Images
- @2x and @3x resolutions
- Lazy loading for lists
- Placeholder images for empty states

### 8.3 Animations
- Spring animations: duration 0.3s, damping 0.7
- Fade transitions: duration 0.25s
- Slide transitions: duration 0.3s

### 8.4 SwiftUI Style Files
For implementation, map to shared style files:
- `{{IDE_CONFIG_DIR}}shared/Styles/AppColors.swift` - Color roles
- `{{IDE_CONFIG_DIR}}shared/Styles/AppFonts.swift` - Typography scale
- `{{IDE_CONFIG_DIR}}shared/Styles/AppSpacing.swift` - Spacing rhythm

---

## 9. Figma Integration

If using Figma, document:
- **Design Tokens**: [Link to Figma variables/tokens]
- **Component Library**: [Link to shared components]
- **Screen Specs**: [Link to screen-specific frames]

For Framelink MCP integration:
- Use `mcp-figma` skill to extract tokens and layout context
- Map tokens to SwiftUI style files before implementing

---

**Document Version**: 1.0
**Last Updated**: 2026
**Status**: Draft / In Review / Approved
**Dependencies**: PRD.md, Use_Cases.md, Functional_Requirements.md

<!-- QUALITY-GATE-MANIFEST:START
# Nguồn chân lý DUY NHẤT cho gate-wireframes. KHÔNG chép khối này vào file đầu ra ở specs/.
# "3. Screen Sections" chứa các Archetype Template A-E là VÍ DỤ (không phải section bắt buộc cố định);
# yêu cầu thực nằm ở quality_checks (mỗi màn hình thật phải theo đúng archetype template).
doc: Wireframes
gate: gate-wireframes
required_major:
  - "1. Introduction"
  - "2. Screen Inventory"
  - "2 bis. Screen Taxonomy"
  - "3. Screen Sections"
  - "4. Common Components"
  - "5. Responsive Design"
  - "6. Accessibility"
  - "7. Dark Mode"
  - "8. Design Assets"
  - "9. Figma Integration"
required_minor:
  "1. Introduction": ["1.1 Purpose", "1.2 Design Principles", "1.3 Design System", "1.4 External References & Fallback"]
  "2 bis. Screen Taxonomy": ["Archetype Catalog", "Screen Taxonomy Assignment Table"]
  "4. Common Components": ["4.1 Navigation", "4.2 Core UI Elements", "4.3 Feedback Components"]
  "5. Responsive Design": ["5.1 Device Support", "5.2 Orientation", "5.3 Adaptive Layout"]
  "6. Accessibility": ["6.1 VoiceOver", "6.2 Dynamic Type", "6.3 Color Contrast", "6.4 Touch Targets"]
  "8. Design Assets": ["8.1 Icons", "8.2 Images", "8.3 Animations", "8.4 SwiftUI Style Files"]
quality_checks:
  - "Screen Taxonomy: mỗi màn hình được gán archetype (§2 bis)"
  - "Archetype Template Match: template màn khớp archetype (Discovery→A, Action→B, Consumption→C, Management→D, Social→E)"
  - "Per-screen parts: mỗi màn hình có đủ Visual Hierarchy, Content Zones Map, Layout, Components, States, User Flow (theo archetype template)"
  - "Content Zones Map: mỗi màn hình có Zone A/B/C/D khớp Use_Cases §4"
  - "State Completeness: user-context (First Visit/Returning/Error) + data states (Default/Loading/Empty/Error) — tối thiểu 7 state"
  - "Screen Coverage: mọi requirement MVP có màn hình"
  - "Affordance→FR back-trace (BLOCKING): MỌI Component và Interaction của mỗi màn hình phải map tới ≥1 FR có AC, HOẶC được khai out-of-scope tường minh (kèm chủ sở hữu). Affordance phụ ở Zone D/utility hoặc trong khối States (settings icon, share, skip, date picker, tooltip, help/FAQ, export, edit-field) KHÔNG được rơi. Affordance chưa có FR → REQUIRED_FIX: bổ sung FR upstream trước rồi mới pass"
  - "Mỗi WF-XXX (kể cả modal/overlay) có FR backing RIÊNG và đúng chủ đề — cấm gán gượng vào FR không liên quan (vd màn Share gán vào FR 'progress vs goal')"
  - "Component Consistency: tham chiếu ios-components skill, không đặc tả inline"
  - "Flow Traceability: entry/exit tham chiếu WF-XXX + TF-XXX; mọi WF-XXX được trích dẫn phải resolve đúng màn hình đúng loại trong Screen Inventory — ref sai loại = Fail"
QUALITY-GATE-MANIFEST:END -->
