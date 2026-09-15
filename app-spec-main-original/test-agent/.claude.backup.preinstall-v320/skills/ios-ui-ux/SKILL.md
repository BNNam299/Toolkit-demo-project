---
name: ios-ui-ux
description:
  UI/UX design principles for iOS. Use when designing screens, making UI look good, user flow design, handling loading states, empty states, error states, animations, navigation patterns, accessibility, dark mode, form design, better UX.
allowed-tools: Read, Grep, Glob
---

# UI/UX Design Principles

## Non-Negotiable Rules (MUST / MUST NOT)

These are enforced by the **UX Compliance Gate** at the bottom of this skill. Execution skills run
that gate before a UI task is set `done`; a violation marks the task `blocked`.

- **MUST** handle all 4 states on every screen: loading, empty, error, success — each rendering.
- **MUST** give the error state a recovery path (retry / dismiss / correct-and-resubmit).
- **MUST** keep touch targets ≥ 44×44pt with ≥ 8pt spacing between interactive elements.
- **MUST** pair every haptic with visual feedback (never haptic-only), and animate state transitions (~0.3s).
- **MUST** add accessibility labels/hints, support Dynamic Type, and meet contrast ≥ 4.5:1 (3:1 large text).
- **MUST** support dark mode and use DSS tokens (`shared/Styles/`) rather than hardcoded colors/fonts/spacing.
- **MUST** apply the matching §7 UX pattern spec when the screen uses it (pull-to-refresh, sheet, toast, swipe…).
- **MUST NOT** use color as the only indicator of state or meaning.
- **MUST NOT** block the main thread or ship a screen missing any of the 4 states.

## Table of Contents
- [1. Design Philosophy](#1-design-philosophy) ....... L23-L40
- [2. Navigation Patterns](#2-navigation-patterns) ... L44-L65
- [3. States & Feedback](#3-states--feedback) ........ L68-L108
- [4. Interaction Patterns](#4-interaction-patterns) . L111-L143
- [5. Visual Hierarchy](#5-visual-hierarchy) ......... L147-L196
- [6. Accessibility](#6-accessibility) ............... L200-L231
- [7. UX Enhancement Patterns](#7-ux-enhancement-patterns) . L233-L409
- [8. Performance UX](#8-performance-ux) ............. L411-L443
- [9. Checklist](#9-checklist) ....................... L446-L478

---

## 1. Design Philosophy

### Core Values
- **Simple first** - Prioritize simplicity, avoid over-complication
- **Consistency** - Consistent throughout the app
- **Feedback** - Always respond to user actions
- **Accessibility** - Design for all users

### Design Style
- Minimalist / Clean
- iOS native feel (follow Human Interface Guidelines)
- Light mode first, support dark mode

### Key Principles
1. Content over chrome
2. Clarity over decoration
3. Depth through layering
4. Direct manipulation

---

## 2. Navigation Patterns

### Main Structure
- Tab Bar for main navigation (max 5 tabs)
- Navigation Stack for drill-down
- Modal/Sheet for temporary actions

### Rules
- No more than 3 levels deep in navigation stack
- Back button always visible
- Swipe back gesture enabled
- Clear navigation hierarchy

### Navigation Types

| Type | Use Case | Presentation |
|------|----------|--------------|
| Push | Drill-down to detail | NavigationStack |
| Sheet | Temporary task | .sheet() |
| Full Screen | Immersive content | .fullScreenCover() |
| Tab | Main sections | TabView |

---

## 3. States & Feedback

### Every Screen Must Handle

| State | Display |
|-------|---------|
| Loading | Skeleton or ProgressView |
| Empty | Illustration + message + CTA |
| Error | Message + retry button |
| Success | Confirmation + next action |

### State Diagram

```
         ┌─────────┐
         │  Idle   │
         └────┬────┘
              │ load()
              ▼
         ┌─────────┐
    ┌────│ Loading │────┐
    │    └─────────┘    │
    │ error             │ success
    ▼                   ▼
┌─────────┐       ┌─────────┐
│  Error  │       │ Success │
└────┬────┘       └────┬────┘
     │ retry()         │ refresh()
     └────────┬────────┘
              ▼
         ┌─────────┐
         │ Loading │
         └─────────┘
```

### User Feedback
- Haptic feedback for important actions
- Animation for state transitions (0.3s default)
- Toast/Snackbar for light confirmations
- Progress indicators for long operations

---

## 4. Interaction Patterns

### Touch Targets
- Minimum 44x44pt for tappable elements
- Spacing between buttons: 8pt minimum
- Adequate padding around interactive elements

### Gestures

| Gesture | Use Case |
|---------|----------|
| Tap | Primary action |
| Long press | Secondary options |
| Swipe | Delete, archive, quick actions |
| Pull to refresh | Reload data |
| Pinch | Zoom |
| Pan | Scroll, drag |

### Forms
- Inline validation
- Clear error messages
- Auto-focus next field
- Appropriate keyboard type
- Show/hide password toggle
- Clear button for text fields

### Form Validation

| Timing | Use Case |
|--------|----------|
| On blur | Field-level validation |
| On change | Real-time feedback (optional) |
| On submit | Full form validation |

---

## 5. Visual Hierarchy

### Typography Scale

| Style | Usage | Weight |
|-------|-------|--------|
| Large Title | Screen titles | Bold |
| Title | Section headers | Bold |
| Headline | Important text | Semibold |
| Body | Main content | Regular |
| Callout | Secondary content | Regular |
| Caption | Labels, hints | Regular |
| Footnote | Legal, timestamps | Regular |

### Spacing System
- Base unit: 8pt
- Use: 4, 8, 16, 24, 32, 48
- Consistent spacing throughout app

### Colors

| Type | Usage |
|------|-------|
| Primary | Brand color for CTAs |
| Secondary | Supporting actions |
| Destructive | Red for delete/danger |
| Success | Green for success states |
| Warning | Yellow/Orange for warnings |
| Error | Red for error states |

### Elevation/Shadows
- Use sparingly
- Consistent shadow styles
- Higher elevation = more important

## 5b. Design Style System (DSS) Persistence (Required)

When creating or modifying UI, always reference and update the DSS source of truth:

- `.claude/shared/COMPONENT_FORMAT.md`
- `.claude/shared/Styles/AppColors.swift`
- `.claude/shared/Styles/AppFonts.swift`
- `.claude/shared/Styles/AppSpacing.swift`

Required behavior:
- Reuse existing tokens first; do not introduce ad-hoc style values in screen/component code.
- If a needed token does not exist, add it in `shared/Styles` before implementation.
- Keep naming semantic (`primary`, `textSecondary`, `bodyRegular`) instead of raw-value naming.
- Reflect new style conventions in `COMPONENT_FORMAT.md` so future tasks follow the same pattern.
- Treat these files as the only DSS style management layer for ongoing maintenance.

---

## 6. Accessibility

### Required
- VoiceOver labels for all interactive elements
- Dynamic Type support
- Minimum contrast ratio 4.5:1
- Don't use color as only indicator
- Support reduced motion

### VoiceOver

```swift
Button("Submit") {
    // action
}
.accessibilityLabel("Submit form")
.accessibilityHint("Double tap to submit your information")
```

### Dynamic Type

```swift
Text("Hello")
    .font(.body) // Automatically scales
```

### Contrast
- Text on background: 4.5:1 minimum
- Large text: 3:1 minimum
- Interactive elements: clearly distinguishable

---

## 7. UX Enhancement Patterns

Reference specs for 12 common iOS UX interaction patterns. Use these when creating UX flow documents.

### 7.1 Pull-to-Refresh

| Spec | Value |
|------|-------|
| Trigger distance | 60pt pull |
| Haptic | On threshold reach |
| Animation | 300ms ease-out rotation |
| Cancel | Release before threshold |
| Confirm | Release at/after threshold |

**States**: Pulling → Threshold (haptic) → Loading → Complete / Error

---

### 7.2 Skeleton Loading

| Spec | Value |
|------|-------|
| Shimmer duration | 1.5s, infinite loop |
| Light placeholder | #E5E5E5 |
| Dark placeholder | #F5F5F5 |
| Content transition | Fade in real content |

**Rules**:
- Match actual content layout structure
- Placeholder shapes approximate real element sizes
- Transition fades skeleton out as content fades in

---

### 7.3 Empty State

| Element | Spec |
|---------|------|
| Illustration | 120x120pt, centered |
| Title | SF Pro Display, 20pt, Bold |
| Description | SF Pro Text, 15pt, Regular |
| Primary CTA | 50pt height button |

**Message variants**:
- **First-time user**: Explain what goes here + CTA to create/add
- **Returning user**: Confirm empty + CTA to add more or refresh

---

### 7.4 Error State with Retry

| Error type | Display | Color / Style |
|------------|---------|---------------|
| Network | Top banner with offline indicator | Yellow #FFCC00 |
| Server | Alert modal with Retry / Cancel | System alert style |
| Validation | Inline red text below field | 13pt, red |

**Recovery**:
- Auto-retry on network recovery for transient network errors
- Retry button always visible for server errors
- Inline validation clears on field correction

---

### 7.5 Haptic Feedback

| Feedback type | When | Style |
|---------------|------|-------|
| UIImpactFeedback | Button tap, toggle, slider | `.light` |
| UIImpactFeedback | Major action complete | `.heavy` |
| UINotificationFeedback | Form submit success | `.success` |
| UINotificationFeedback | Delete action | `.warning` |
| UINotificationFeedback | Validation failure | `.error` |
| UISelectionFeedback | Picker scroll, segment change | (default) |

**Rule**: Always pair haptic with visual feedback. Never haptic-only responses.

---

### 7.6 Quick Actions (Swipe Gestures)

| Direction | Actions | Colors |
|-----------|---------|--------|
| Left swipe | Delete, Edit, Archive | Red, Orange, Gray |
| Right swipe | Complete, Favorite | Green, Yellow |

| Threshold | Behavior |
|-----------|----------|
| 80pt | Reveal actions |
| 120pt | Full action commit |

**Rule**: Confirm before destructive actions (delete, archive).

---

### 7.7 Onboarding Animation

| Element | Spec |
|---------|------|
| Page transition | 300ms ease-in-out |
| Dot indicator | 200ms spring animation |
| Content fade | 250ms |
| Haptic | `.light` on page change |
| Final page CTA | "Get Started" with `.success` haptic |

---

### 7.8 IAP Purchase Flow

- **Product carousel**: Swipe between options
- **Multi-tier**: Price comparison table
- **Restore button**: Always visible, standard placement
- **Success**: Celebration animation
- **Error**: Clear message + retry. Preserve user's selection across retry.

---

### 7.9 Alert Presentation

| Spec | Value |
|------|-------|
| Animation | 200ms scale-in from center |
| Background | 50% black overlay, blocking |
| Max buttons | 2 (primary + secondary) |
| Destructive text | Red, bottom position |
| Auto-focus | Least destructive action |
| Dismiss | Not by tap outside for destructive alerts |

---

### 7.10 Dialog Presentation

| Spec | Value |
|------|-------|
| Animation | 300ms slide-up, spring damping |
| Background | 50% overlay, dismissible (except destructive) |
| Action Sheet | Slides from bottom, drag-to-dismiss |
| Input dialogs | Real-time inline validation |

**Variants**: Confirmation, Input, Selection, Action Sheet

---

### 7.11 Bottom Sheet

| Spec | Value |
|------|-------|
| Snap points | Partial 40% → Medium 60% → Full 90% |
| Drag indicator | 36x5pt gray pill |
| Animation | 300ms slide-up, spring damping 0.8 |
| Background | 30% black overlay |
| Dismiss | Drag below threshold OR tap outside |
| Content overflow | Scroll enabled within sheet |

---

### 7.12 Snackbar/Toast

| Spec | Value |
|------|-------|
| Position | Bottom, 16pt above safe area |
| Max content | 2 lines text + 1 action button |
| Duration | 3-4s auto-dismiss |
| Show animation | 200ms slide-up |
| Hide animation | 200ms slide-down |
| Stacking | New replaces old |

**Variants**:

| Variant | Color |
|---------|-------|
| Info | Brand color |
| Success | Green |
| Warning | Yellow |
| Error | Red |

---

## 8. Performance UX

### Loading
- Skeleton screens instead of spinners when possible
- Optimistic UI for fast actions
- Lazy loading for long lists
- Progressive loading for images

### Skeleton Example

```
┌────────────────────────────┐
│ ████████████               │  <- Title placeholder
│ ████████████████████████   │  <- Subtitle placeholder
│                            │
│ ████████████████████████   │  <- Content placeholder
│ ████████████████           │
└────────────────────────────┘
```

### Offline
- Cache important data
- Show offline indicator
- Queue actions to sync later
- Graceful degradation

### Performance Tips
- Avoid blocking main thread
- Use lazy loading for lists
- Cache computed values
- Optimize images
- Minimize re-renders

---

## 9. Checklist

### When Designing New Screen

- [ ] Define user goal for the screen
- [ ] Handle all 4 states (loading, empty, error, success)
- [ ] Touch targets >= 44pt
- [ ] VoiceOver labels
- [ ] Dark mode compatible
- [ ] Keyboard handling (if has input)
- [ ] Animation for transitions
- [ ] Consistent with app style

### When Implementing

- [ ] Use design tokens (colors, fonts, spacing)
- [ ] Reference tokens from `.claude/shared/Styles/` (avoid hardcoded style constants)
- [ ] If new visual rule is introduced, update the matching style file in `.claude/shared/Styles/`
- [ ] Add accessibility labels
- [ ] Support Dynamic Type
- [ ] Test with VoiceOver
- [ ] Test dark mode
- [ ] Test different screen sizes
- [ ] Handle keyboard appearance

### Before Release

- [ ] All states implemented
- [ ] Accessibility audit passed
- [ ] Performance acceptable
- [ ] Animations smooth (60fps)
- [ ] No layout issues on different devices

---

## UX Compliance Gate (Required)

Execution skills (`execution-implement`, `execution-quick`, `execution-quality-gates`) run this gate
before a UI task can be set `done`. It is the single source of truth for UX quality — the executor
must not lower the bar on its own.

**Checklist (every item must pass):**
- [ ] Loading state implemented and testable.
- [ ] Empty state implemented and testable (illustration + message + CTA).
- [ ] Error state implemented **with a recovery action** (retry / dismiss / correct-and-resubmit).
- [ ] Success/default state implemented.
- [ ] Touch targets ≥ 44×44pt with adequate spacing.
- [ ] Haptics paired with visual feedback; state transitions animated (~0.3s).
- [ ] Accessibility labels/hints on key interactions; Dynamic Type supported; contrast ≥ 4.5:1.
- [ ] Dark mode verified.
- [ ] Styles reference `.claude/shared/Styles/` tokens (no hardcoded color/font/spacing).
- [ ] If the screen uses a §7 pattern (pull-to-refresh, sheet, toast, swipe, alert…), it follows that spec.

**BLOCK conditions** → mark task `blocked` (or keep `in_progress`), do not set `done`:
- Any of the 4 states is missing or non-rendering, or the error state has no recovery.
- Touch target < 44pt, color used as the only indicator, or accessibility/Dynamic Type absent.
- Dark mode broken, or styles hardcoded instead of DSS tokens.

**Evidence line** (required in task notes for any UI task):
```
UX: states[4/4] recovery[✓] touch≥44[✓] haptic+visual[✓] a11y[✓] dynamicType[✓] darkmode[✓]
```
Replace any `✓` with the failing detail and block if not all pass.
