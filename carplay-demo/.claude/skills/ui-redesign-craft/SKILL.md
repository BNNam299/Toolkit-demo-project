---
name: ui-redesign-craft
description: Design craft knowledge for the UI redesign flow — distinctiveness principles, a named catalog of signature moments, and how to push a screen beyond generic iOS-stock while keeping the UX floor. Used by ui-redesign at code-time.
allowed-tools: Read, Grep, Glob
---

# UI Redesign — Craft (distinctiveness knowledge)

This is the **creative knowledge** the `ui-redesign` engine draws on. `ios-ui-ux` defines the *floor*
(correctness, "iOS native, clarity over decoration") — that floor stays. This skill defines how to make a
screen **distinctive** on top of that floor. It brings the distinctiveness concepts of
`uiux-analysis-workflow` (Product DNA, Signature Opportunities) down to **code-time**, applied to a built app.

## Core stance: floor is kept, generic default is overridden

- **Keep (never trade away):** all 4 states + recovery, a11y labels, Dynamic Type, contrast ≥4.5:1, ≥44pt targets, dark mode, DSS tokens.
- **Override (this is the whole point):** the `ios-ui-ux` default of "clarity over decoration / iOS native feel". During redesign, the chosen Style DNA takes precedence — the app should look like *itself*, not like a stock template.
- **Test for "still generic?"** — if a screen would look identical under any of the 10 design systems, it has no identity yet. Push further.

## Distinctiveness principles

1. **One signature system, everywhere.** Pick a single recurring form idea (see catalog) and apply it consistently so the app reads as one identity.
2. **Commit the tokens.** Replace system defaults (`#007AFF`, system font, 8pt-only spacing, default shadow/spring) with Style-DNA tokens. Leftover defaults = not distinctive.
3. **Hierarchy first, decoration second.** Distinctiveness amplifies hierarchy (what the eye hits #1→#4); it never fights legibility.
4. **Motion as identity.** A consistent motion language (easing/spring/duration) is part of the signature, not an afterthought.
5. **Focal signature moments, not everywhere.** 1–3 per screen at focal points (hero, empty state, primary CTA, key transition) — over-decoration is noise.
6. **Every choice traces to the Style DNA** and is justified against "how does this leave iOS-stock?".

## Signature-moments catalog (named — pick from these; extend when justified)

| Moment | What it is | Best at | Needs (tokens/motion) | A11y cost / guard |
|--------|------------|---------|-----------------------|-------------------|
| `hero-typography` | Oversized expressive display type as the focal element | Headers, landing, section intros | type scale, weight, tracking | keep Dynamic Type; don't clip |
| `layered-depth` | Stacked surfaces w/ deliberate elevation & shadow | Cards, dashboards | elevation tokens, shadow | maintain contrast on layers |
| `bold-border` | Thick borders + hard offset shadow (neo) | Buttons, cards, inputs | border width, offset shadow, palette | ensure focus ring still visible |
| `gradient-wash` | Mesh/linear gradient backdrop w/ colored glow | Hero, empty, paywall | gradient tokens, glow | text contrast ≥4.5:1 over gradient |
| `expressive-empty-state` | Illustrated/animated empty state w/ personality + CTA | Empty lists/diary | illustration, motion, CTA token | keep the CTA + message legible |
| `springy-transition` | Consistent spring for present/dismiss/state change | Sheets, navigation, state swaps | spring preset, duration | pair w/ visual; respect reduce-motion |
| `glass-surface` | Frosted blur surface over content | Nav/tab bars, sheets | blur, translucency, border | contrast over blur; fallback opaque |
| `data-accent` | One vivid accent reserved for the key metric/action | Dashboards, progress | accent color role | not the only state indicator |
| `tactile-press` | Scale/haptic press feedback w/ shadow shift | All primary controls | scale, haptic, shadow | haptic + visual (never haptic-only) |
| `sectioned-bento` | Bento-grid modular layout of unequal tiles | Home, overview | grid, radius, spacing | logical VoiceOver order |

> Motion presets, blur, gradient, elevation, spring: source their values from the chosen `DESIGN_TOKEN_*.json`
> or the `.pen` variables, then map into `shared/Styles/*.swift` (see `ui-redesign` P3).

## Applying a moment (contract with the engine)
For each signature moment placed on a screen, the `screens/screen-[view].md` must record:
`moment name · placement · tokens/motion used · Style-DNA trace · how it leaves iOS-stock · a11y note`.

## How to leave iOS-stock (checklist)
- [ ] No leftover `#007AFF` / `.accentColor` default / system font where a brand token should be.
- [ ] Corner radius, shadow, spacing come from tokens (not ad-hoc values).
- [ ] At least one signature moment is visible on the screen.
- [ ] Motion uses the app's spring/easing preset, not the SwiftUI default.
- [ ] The screen would look wrong under a *different* design system (i.e., it has identity).
