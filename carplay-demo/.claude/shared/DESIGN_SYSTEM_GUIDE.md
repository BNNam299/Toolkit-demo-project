# Design System Guide

Reference for creating visual identity and consistent UI components.

---

## 1. How to Think About Visual Identity

A design system is NOT a set of colors and fonts. It is a **visual language** that makes the app feel like itself. Follow this thinking process, in order:

### 1.1 Extract Product DNA

Read Project_Overview.md and PRD.md for:

- **Domain**: e-commerce, social, finance, productivity, health, education, entertainment, fitness, SaaS
- **Brand personality**: 2-3 traits (e.g., playful + trustworthy, minimal + bold, warm + premium)
- **Target audience**: age range, tech literacy, context (on-the-go, desk, couch)
- **Desired emotion**: What should user feel? (calm, excited, focused, trusted, inspired)
- **Competitor differentiation**: How is this app visually different from competitors?

### 1.2 Propose Visual Direction

From product DNA, propose 2-3 visual directions. Each direction must answer:

**Color Philosophy:**
- Primary palette: dominant hue + rationale (why this color evokes the right emotion)
- Accent: contrasting color for CTAs and interactive elements
- Background: warm vs cool, light vs dark
- Semantic colors: success, error, warning — tone that matches brand (gentle vs stark)

**Typography Character:**
- Sans-serif vs serif vs slab vs rounded: which matches the personality?
- Weight distribution: bold headings + light body vs all-medium
- Line height: spacious vs compact (matches density of content)

**Shape & Space Language:**
- Corner radius: sharp (0-4pt) = precise/technical, soft (8-12pt) = friendly/approachable, pill (16pt+) = playful
- Shadows: none (flat/2D), soft (subtle depth), bold (hard drop shadow)
- Spacing: generous (24pt gutters) = premium/calm, compact (8-12pt) = dense/efficient
- Borders: none, thin (1px), or bold (2-3px)

### 1.3 Formalize as Design Tokens

Once direction is chosen, organize into token structure:

```json
{
  "meta": {
    "name": "Direction name",
    "version": "1.0",
    "description": "3-sentence summary of visual character",
    "mood": ["trait1", "trait2", "trait3"],
    "visualWeight": "light | medium | bold",
    "bestFor": ["domain1", "domain2"]
  },
  "color": {
    "palette": { ... },
    "semantic": { ... }
  },
  "typography": { ... },
  "spacing": { ... },
  "border": { ... },
  "shadow": { ... },
  "component": { ... },
  "animation": { ... },
  "composition": { ... }
}
```

---

## 2. Reference Design Systems

The project ships 10 pre-built design token files in the `shared/` directory. Use them as:

- **Inspiration** — read `meta` section to understand visual character
- **Starting point** — load one and customize tokens
- **Comparison** — see how different systems solve the same problem

| File | Character | Best For |
|------|-----------|----------|
| `DESIGN_TOKEN_BENTO_GRID.json` | Structured cards, soft shadows, premium calm | Dashboard, content discovery, productivity |
| `DESIGN_TOKEN_FUNCTIONAL_MINIMALISM.json` | Invisible UI, typography-driven, no shadows | Writing, reading, task management |
| `DESIGN_TOKEN_CARDS_LAYERING.json` | Depth-rich stacked cards, 5 elevation levels | Finance, banking, file management |
| `DESIGN_TOKEN_SOFT_SKEUOMORPHISM.json` | Warm 3D highlights, paper texture | Wellness, journaling, meditation |
| `DESIGN_TOKEN_DARK_MODE_FIRST.json` | True-black OLED, neon accents | Media player, crypto, night-mode |
| `DESIGN_TOKEN_GLASSMORPHISM.json` | Frosted glass, blur, pastel gradients | Music, weather, creative showcase |
| `DESIGN_TOKEN_AURORA_GRADIENTS.json` | Mesh gradients, colored shadows, glow | Meditation, mood tracking, creative tools |
| `DESIGN_TOKEN_NEOBRUTALISM.json` | Bold borders, hard shadows, pop colors | Gen-Z social, gaming, edtech |
| `DESIGN_TOKEN_TYPOGRAPHIC_DRIVEN.json` | Serif + sans-serif, no cards, editorial | Reader, news, journal, documentation |
| `DESIGN_TOKEN_MOTION_FIRST.json` | Spring animations, haptics, stagger effects | Social, fitness, onboarding, camera |

**You are NOT limited to these 10.** Propose a custom direction when the app's DNA doesn't fit any existing system. You can also blend: e.g., bento-grid colors + neobrutalism shadows.

---

## 3. Token Categories Reference

### 3.1 Color Palette

| Token | Purpose |
|-------|---------|
| `color.palette.background` | Main screen background |
| `color.palette.surface` | Card/sheet surface |
| `color.palette.surfaceVariant` | Secondary surface (search bars, dividers) |
| `color.palette.surfaceElevated` | Modal/sheet elevated surface |
| `color.palette.textPrimary` | Primary text |
| `color.palette.textSecondary` | Secondary/meta text |
| `color.palette.textTertiary` | Placeholder, disabled text |
| `color.palette.textInverse` | Text on dark backgrounds |
| `color.palette.accent` | Primary interactive color |
| `color.palette.accentVariant` | Pressed/hover state |
| `color.palette.accentSubtle` | Background tint for accent |
| `color.palette.onAccent` | Text on accent background |
| `color.semantic.*.color` | Semantic: success, warning, error, info |
| `color.semantic.*.background` | Tint backgrounds for each semantic |

### 3.2 Typography

| Token | Purpose |
|-------|---------|
| `typography.family` | Font family name |
| `typography.scale.h1.*` | Largest heading (34pt+): size, weight, lineHeight |
| `typography.scale.h2.*` | Section heading (28pt) |
| `typography.scale.h3.*` | Card heading (22pt) |
| `typography.scale.headline` | Inline title (17pt semibold) |
| `typography.scale.body` | Body text (17pt) |
| `typography.scale.caption` | Caption/meta (13pt) |
| `typography.scale.footnote` | Small print (11pt) |
| `typography.scale.button` | Button label (16-17pt semibold) |
| `typography.scale.stat` | Large display numbers (40-48pt) |

### 3.3 Spacing (8pt Grid)

| Token | Pt Value |
|-------|----------|
| `spacing.xs` | 4 |
| `spacing.sm` | 8 |
| `spacing.md` | 16 |
| `spacing.lg` | 24 |
| `spacing.xl` | 32 |
| `spacing.xxl` | 48 |

### 3.4 Border Radius

| Token | Use Case | Typical |
|-------|----------|---------|
| `border.radius.sm` | Text fields, small elements | 4-6pt |
| `border.radius.md` | Buttons, medium cards | 8-12pt |
| `border.radius.lg` | Large cards, modals | 12-16pt |
| `border.radius.xl` | Sheets, containers | 16-20pt |
| `border.radius.full` | Circular: avatars, pills | 9999pt |

### 3.5 Shadows

| Token | Elevation | Use |
|-------|-----------|-----|
| `shadow.elevation.1` | Content card | Subtle: (0,1,3,0.08) |
| `shadow.elevation.2` | Floating element | Medium: (0,2,6,0.1) |
| `shadow.elevation.3` | Sheet/modal | Elevated: (0,4,12,0.12) |
| `shadow.elevation.4` | FAB, sticky bar | High: (0,6,16,0.15) |
| `shadow.elevation.5` | Alert/tooltip | Highest: (0,8,24,0.18) |

### 3.6 Components (iOS Patterns)

| Component | Token Prefix | Typical Tokens |
|-----------|-------------|----------------|
| Nav bar | `component.navBar` | height, background, blur, dividerColor, titleStyle |
| Tab bar | `component.tabBar` | height, background, blur, inactiveColor, activeColor, badgeStyle |
| Button primary | `component.button.primary` | height, radius, font, padding, shadow |
| Button secondary | `component.button.secondary` | height, radius, borderWidth, font |
| Card | `component.card` | radius, padding, shadow, border, background |
| Text field | `component.textField` | height, radius, borderColor, focusColor, errorColor |
| Avatar | `component.avatar` | size, borderWidth, borderColor |
| Chip | `component.chip` | height, radius, padding, font, selectedColor |
| Divider | `component.divider` | thickness, color, inset |
| Toast | `component.toast` | height, radius, font, shadow, duration |
| Sheet | `component.sheet` | radius, maxHeight, dragIndicatorHeight, overlayColor |

### 3.7 Animation

| Token | Purpose |
|-------|---------|
| `animation.spring.bouncy` | Fun, playful: 0.5s, damping 0.5 |
| `animation.spring.smooth` | Natural feel: 0.4s, damping 0.7 |
| `animation.spring.stiff` | Precise: 0.3s, damping 0.9 |
| `animation.duration.fast` | Micro-interactions: 0.15s |
| `animation.duration.normal` | Standard: 0.3s |
| `animation.duration.slow` | Expressive: 0.5s |

### 3.8 Composition (Per-Archetype UX Enhancements)

Each archetype gets default enhancements from the design system:

```
composition.[archetype].defaults  — list of UX enhancements
composition.[archetype].zones     — Zone A/B/C/D definitions with sizing
```

Example (Discovery):
```json
"composition": {
  "discovery": {
    "defaults": ["pull-to-refresh", "skeleton-loading", "infinite-scroll", "personalization"],
    "zones": {
      "A": { "name": "Hero", "height": "dynamic", "behavior": "carousel" },
      "B": { "name": "Feed", "height": "fill", "behavior": "scroll" },
      "C": { "name": "Sections", "height": "~140pt", "behavior": "horizontal-scroll" },
      "D": { "name": "Chrome", "height": "44+49pt", "behavior": "nav+tab" }
    }
  }
}
```

---

## 4. iOS Pattern Reference

When designing layout, map zones to real iOS patterns. Reference these for sizing and behavior:

| Pattern | Typical Height | Use |
|---------|---------------|-----|
| NavigationStack toolbar | 44pt | Title + leading/trailing actions |
| Large title nav | 96pt (collapses to 44pt) | First screen in a nav stack |
| TabView bar | 49pt (+34pt safe area on notched) | 3-5 top-level sections |
| .sheet (medium detent) | ~50% screen | Quick actions, pickers |
| .sheet (large detent) | ~90% screen | Full-page modal tasks |
| .searchable | 44pt (integrated in nav) | List/search screen |
| .toolbar | 44pt | Contextual actions |
| List row | 44pt (standard) / 60pt (subtitle) | Menu, settings |
| List row with swipe | 44-72pt | Actionable rows |
| Button (touch target) | 44pt minimum / 50pt recommended | All tappable elements |
| Safe area top | 44pt standard / 47pt dynamic island | Respect safeAreaInsets |
| Safe area bottom | 34pt standard / 83pt with tab bar | Respect safeAreaInsets |

---

## 5. Creativity Rules

- **Anchored**: Every creative choice must trace to Product DNA (domain, personality, audience). If it can't be justified, it's decoration.
- **Purposeful**: Propose unconventional layouts only when they increase clarity, confidence, speed, recovery, or distinctiveness.
- **Document trade-offs**: For every creative choice, note what you gained and what you sacrificed.
- **Mark proposals**: `INFERRED` = derived from PRD/UC context. `PROPOSED` = creative addition with value label.
