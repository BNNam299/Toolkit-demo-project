---
name: mobile-ui-master
description: Visual-design knowledge for mobile app screens — layout and spacing rhythm, information density, visual hierarchy, typography, colour, iconography — plus the measured structure of real designer screens (Top Container / Content / Bottom Container, paddings, gaps, toolbar, CTA and sheet sizes, templates per screen type), a six-question method for reading screens, and a script that compares a built screen's skeleton with a reference screen. Use whenever you lay out, critique or visually review a mobile screen — choosing regions and spacing, fixing a cluttered or empty-looking screen, replacing stacks of identical cards, picking type/colour/icon treatment, reading an existing Figma project screen by screen — even if the user only says "bố cục màn này thế nào", "màn này trông rối", "dàn trang lại giúp tôi", "khoảng cách bao nhiêu", "soát giao diện", "màn trống trải quá". For the screen build loop use figma-ui-flow; touch, states, gestures use mobile-ux-fundamentals; heuristic UX review use ux-review-handoff.
---

# mobile-ui-master — layout, density and visual review for mobile screens

This skill answers **what a good mobile screen looks like and how to judge one**: where the regions go, how much space between things, how dense
the content should be, what stands out first, and how type, colour and icons support that. It is the skill `figma-ui-flow` calls for "layout,
information density, avoiding card stacks / meaningless emptiness, visual review".

What lives elsewhere — link, do not restate:
- **How to build** a screen (8 stages, three-pass outside-in loop, Definition of Done) → `../figma-ui-flow/references/build-loop.md`.
- **Tool mechanics** (`execute_code`, `screenshot`, `get_node`) → `../figma-agent-tools/SKILL.md`.
- **Touch targets, states, feedback, gestures** → `../mobile-ux-fundamentals/SKILL.md`.
- **Platform rules** → `../apple-hig/SKILL.md`, `../material-design-3/SKILL.md`.

Let `SKILL_DIR` be the directory containing this file.

## Need → Read

| Need | Read |
|---|---|
| Regions, paddings, gaps, toolbar/CTA/sheet sizes, list rows, templates per screen type (onboarding, home, feed, settings, edit form, sheet, shield, paywall, passcode…) | `references/screen-structure.md` |
| iPhone Duo packaging (four variants, `Pane controls`, pane split, where panels move) | `references/screen-structure.md` §11 + `../iphone-duo-adaptive/SKILL.md` |
| Container-first layout, breakpoints, the five breakpoint questions, canonical layouts, padding/gap/margin, foldables | `references/layout-spacing.md` §1–7 |
| Corner-radius rules, action hierarchy, opacity vs alpha, colour dust, letter spacing | `references/layout-spacing.md` §8–12 |
| Typography, semantic colour, Liquid Glass, elevation, near-black backgrounds, icons, app icon, images | `references/visual-foundations.md` |
| Reading an existing screen / section / project (six questions, `flows.md`) | `references/reading-screens.md` |
| Compare a built screen's skeleton with a reference screen | `scripts/skeleton.js` (see "Running the script") |
| Paywalls, offers, real Amobear app samples | `references/monetization-screens.md` |
| Heuristics, severity scale, cognitive principles for a review | `../ux-review-handoff/references/heuristics-evaluation.md` |
| Team frame size and safe-area standard | `../bnnam-team-standards/references/frame-standards.md` |
| Touch, states, gestures, sheets/dialogs | `../mobile-ux-fundamentals/SKILL.md` |
| The build passes this review plugs into | `../figma-ui-flow/references/build-loop.md` |

Do not read everything at once. Laying out a new screen → `screen-structure.md` (§1–6 + the matching §7b row). Reviewing → this file's checklist,
then the reference for whichever item fails. Reading a project → `reading-screens.md` only.

## Core rules (apply them even without opening a reference)

### 1. Frame and regions
- Default iPhone frame **402 × 874**, root radius **44**, root fill = a surface token. Long scrolling screens grow taller (402 × 1444…). Older
  projects keep their size (390 × 844, 393 × 852) — size follows the project, structure follows the standard.
- Layers bottom → top: `Background/<name>` instance (only if there is a visual background) → `Content` → `Bottom Container` → `Top Container`
  (above Content so content scrolls under it) → `Scrim` → `Bottom sheet / Popup`.
- Top safe area **62** for a new 402 × 874 build (60 in older files), bottom **34**, always as a `Safe-Area` component instance, never as padding.
- Primary CTA lives in `Bottom Container`, pinned to the bottom; it is never floated mid-content to fill space.

### 2. Spacing rhythm
- `Content` padding **24** all round, or **16** horizontal on dense screens; **48** between sections; **24 / 16 / 8** inside a section (larger
  for looser relationships, smaller for tighter ones). Toolbar **76** high (pad 16), CTA **56**, list icon tile **36** with a 20 icon.
- Space expresses grouping: the gap *between* groups is clearly larger than the gap *inside* a group. If every gap is the same, the screen has no structure.
- Padding and gap on the container, not margins on each child; `leading/trailing`, not `left/right`.

### 3. Information density — no card stacks
- Rows of the same kind share **one** grouped container (`Table row Container`, dividers between rows, r21 on screen / r28 in a sheet) — not one
  card per row. A single-row group becomes a pill (r999).
- Each content block is **header + body** (title + chevron, then content). A block without a header that just sits in a card is usually noise.
- A card earns its own surface only when it is a distinct unit the user compares, browses or taps as a whole (offer card, focus card,
  horizontally scrolling group card 216 × 260). Browsable items → horizontal scroller or a 2-column grid of auto-layout rows (gap 12).
- Few hierarchy levels per screen: one headline, a subheadline, section titles, body. Emphasized styles are for a few moments, not every title.
- Surface advanced features directly (one tap starts the work) instead of hiding them behind menus.

### 4. Emptiness — meaningful vs meaningless
- Large empty space is meaningful only when it **focuses**: a full-screen screen with no navigation (shield, barrier: no Top Container, centred
  content, gap 98), a Welcome hero visual, a celebration over a scrim.
- Everywhere else empty space must separate groups (48 between sections), not float. Short content hugs from the top; the CTA stays pinned in
  `Bottom Container` — never stretch cards or spacers to "fill" the screen.
- An empty *state* is not an empty *screen*: it carries an explanation and an action (`../mobile-ux-fundamentals/SKILL.md`).

### 5. Visual hierarchy and actions
- Exactly one primary action, big; secondary actions small or tucked away.
- Two buttons: **side by side** when they are equals (Cancel / Save), **stacked** when one is primary (shield, Premium lock).
- Overlay by job: **sheet** (edit, confirm, lock) · **popover** anchored below the top bar (quick choice) · **scrim + centred content** (celebration, big announcement).
- Question to ask of every screen: *what does the user see first, and is that the thing this screen is for?*

### 6. Corner radius
- Containers in the same frame share one radius. A large element next to a small one takes **½ the small one's height** (button 44 → image r22;
  bar 50 → container r25). Designer scale: pill · 21 list card · 28 sheet/summary card · 36 large card · 44 screen root.

### 7. Typography
- System fonts and text styles by role (iOS: Dynamic Type styles; M3: Display / Headline / Title / Body / Label × L/M/S). No ALL CAPS paragraphs,
  no thin weights at small sizes, no important text inside images, no clipped or height-locked text.
- Letter spacing = size × 2.5% in this designer's files. Test Vietnamese diacritics and long translations.

### 8. Colour
- Semantic roles, never `blue500` at component level; check every `on…` colour against its container; body contrast ≥ 4.5:1, large text/UI ≥ 3:1.
- Alpha colour tokens (`Primary / Black 50%`), not layer opacity; layer opacity only to fade a whole composite for **Disabled**.
- Avoid colour dust (tints that go muddy over white/black). For a custom dark background prefer a near-black (`#121212`, `#0A0A0A`…) over `#000000`;
  iOS system colours stay Apple's.
- Liquid Glass for the navigation/control layer only; M3 depth via tonal surfaces first, shadows sparingly; iOS depth via material/blur, not copied Android shadows.

### 9. Iconography
- One icon family and style, consistent stroke/optical weight/bounding box; label any icon that is not universal; selected states change fill/weight
  without moving layout. Glyph meaning differs per platform (back, share, overflow, delete, menu, check).

## Workflow — visual review of a screen

Use this at the end of each build pass (`../figma-ui-flow/references/build-loop.md` §3) or when the user says "soát giao diện" / "màn này trông rối".

1. **Read the screen** — screenshot + outline, answer the six questions (`references/reading-screens.md` §3). Question 2 (what is seen first) drives the review.
2. **Skeleton** — if a template screen or an approved sibling exists, run `scripts/skeleton.js` against it. Fix differences or state why they are intentional.
3. **Walk the checklist** below; for each failing item open the reference named in it.
4. **Report** findings grouped by severity (scale in `../ux-review-handoff/references/heuristics-evaluation.md`): what is wrong, where (node name/id), the fix with numbers ("gap 16 → 48 between Stats and History").

Checklist:
- [ ] Regions and layer order per core rule 1; safe area is a component instance (`screen-structure.md` §1–2).
- [ ] Gap between groups > gap inside groups; values from the 48 / 24 / 16 / 8 rhythm (`screen-structure.md` §3).
- [ ] No stack of same-kind cards; lists grouped in one container (`screen-structure.md` §4).
- [ ] No meaningless emptiness; CTA pinned at the bottom (`screen-structure.md` §5, §7b shield row).
- [ ] One primary action; two-button arrangement correct (`screen-structure.md` §7b).
- [ ] Radii consistent and adjacent-radius rule respected (`layout-spacing.md` §8).
- [ ] Few type levels, roles correct, nothing clipped (`visual-foundations.md` §1).
- [ ] Semantic colours, contrast, no layer-opacity "colours", no colour dust (`visual-foundations.md` §2, `layout-spacing.md` §10–11).
- [ ] Icons from one family, labelled when not universal (`visual-foundations.md` §4).
- [ ] Platform pass: `../apple-hig/SKILL.md` or `../material-design-3/SKILL.md`; touch and states: `../mobile-ux-fundamentals/SKILL.md`.

## Running the script

`scripts/skeleton.js` is Figma Plugin API code, read-only. Read it, set `CONFIG` at the top (`PAGE`, `REFERENCE` = template or approved sibling
screen, `REFERENCE_PAGE` if different, `TARGETS` = screens just built, `DEPTH` default 3), then send the whole file as `code` to
`execute_code{code, timeoutMs}` (default 30 s is enough for a few screens). It returns, per target, `matches`, `differenceCount`, up to 40
`differences` (`missing` / `extra` blocks, or `differs` on type, layout, sizing, absolute position, instance component) and `required` notes
(background instance, safe-area component). It compares structure only — never text or colour.

## Designer standard vs tool-demo defaults

When working in a file that follows this designer's standard, these differ from `figma-ui-flow` defaults; follow the designer standard and say so in the report:

| Topic | Designer standard (this skill) | Tool demo |
|---|---|---|
| Screen root | `layoutMode NONE`, three regions layered; regions themselves are auto layout | "Auto Layout on every frame that holds content" |
| iPhone frame | 402 × 874, r44, top safe area 62 | 393 × 852 |
| Region names | `Top Container` / `Content` / `Bottom Container` | `Header` / `Content` / `Footer` in examples |
| Spacing on screen layout frames | raw numbers on purpose; tokens inside components | any unbound spacing is a defect |
| When to componentize | at the second screen with an identical block | blocks repeated ≥ 3 times |
| Letter spacing | size × 2.5% | slightly negative for large sizes |

## Common pitfalls

- **Card for everything** — each setting, stat or row in its own rounded card with shadow. Group same-kind rows; reserve cards for units.
- **Even spacing everywhere** — 16 between every element hides the grouping. Use 48 between sections, 8–16 inside.
- **Filling the screen** — stretching cards, adding spacers or decorative blocks so a short screen "looks full". Let content hug; pin the CTA.
- **Several "primary" buttons** or tinted glass on every control — nothing stands out.
- **Judging from the screenshot alone** — misses small text and hidden actions; read the outline too (`reading-screens.md`).
- **Copying a deviation** — the Duo file's Outer `Bottom Container` with pad 16 is a known error, not a pattern.
- **Layer opacity as a colour** — developers cannot tell 50% from 48%; use an alpha token.

## Self-check before reporting

- Answered the six questions for every screen reviewed, from screenshot + outline (or stated "image not viewed").
- Skeleton compared with a reference when one exists; intentional differences stated.
- Every finding names the node and gives the fix in numbers; severity from the heuristics scale.
- Spacing rhythm, density, emptiness, hierarchy, radius, type, colour and icons each checked — not just "looks fine".
- Conflicts with tool-demo defaults (table above) stated, not silently applied.
