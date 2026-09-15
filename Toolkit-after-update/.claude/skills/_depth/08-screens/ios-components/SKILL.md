---
name: ios-components
description: 
  Create UI components for SwiftUI. Use when creating buttons, cards, input fields, modals, bottom sheets, loading views, empty states, creating components from design images, coding UI from Figma, making custom views, creating reusable views.
allowed-tools: Read, Grep, Glob, Bash
---

<!-- APPSPEC-PRELUDE -->

> **ĐỌC KHỐI NÀY TRƯỚC.** File này lấy nguyên văn từ bộ **app-spec** rồi đưa vào Pipeline v2.
> Nội dung chuyên môn bên dưới dùng bình thường, nhưng **ba loại tham chiếu trong đó đã lỗi** — bỏ qua chúng,
> đừng đi tìm.
>
> **1. Skill không tồn tại trong bộ này.** `project-docs-contract` · `project-docs-workflow` ·
> `project-docs-prd` · `project-docs-overview` · `project-docs-uc` · `project-docs-fr` ·
> `project-docs-wireframes` · `project-docs-flows` · `project-docs-roadmap` · mọi `spec-*` · mọi
> `execution-*` · `ui-redesign` · `quick-*` · `dev-spec-driven` · `ios-debug` · `ios-icon-gen` · `mcp-xcode`.
> Chúng bị loại **có chủ đích** vì thuộc phạm vi sau bàn giao. Danh sách đầy đủ ở `.claude/KIT_MANIFEST.md`.
> Gặp câu *"phải đọc skill X trước"* mà X nằm trong danh sách này thì **bỏ qua câu đó**, không dừng, không đi tìm.
>
> **2. Đường dẫn `.claude/specs/<tên dự án>/...`** — cấu trúc của app-spec, **không có** ở đây.
> Bộ này ghi tài liệu ra `docs/<thư-mục-phase>/<doc_id>_<TÊN>.md`. Danh sách 61 tài liệu ở `docs/_INDEX.md`.
>
> **3. Bảng ánh xạ 1:1 gate→file** kiểu `gate-prd → PRD.md`. Pipeline v2 có 61 tài liệu và 12 cổng G0–G11;
> cổng đọc từ khối `QUALITY-GATE-MANIFEST` ở **cuối template tương ứng**, không từ bảng cứng.
>
> **Đây là skill CHIỀU SÂU.** Nó không sở hữu tài liệu nào, không cấp ID, không gọi cổng. Vai của nó là làm
> skill phụ trách phase hiểu sâu hơn. Mọi thứ ghi ra file vẫn do skill phụ trách phase quyết định.


# SwiftUI Reusable Components

## Non-Negotiable Rules (MUST / MUST NOT)

These are enforced by the **Reuse-First Gate** at the bottom of this skill. Execution skills run that
gate before any component is written; a violation marks the task `blocked`.

- **MUST** search `.claude/shared/Components/` (ls / find / grep) BEFORE creating any
  component, and record the candidates examined.
- **MUST** prefer, in order: use as-is → add parameters → compose existing → extend via ViewModifier.
  Create new only when no compatible option exists.
- **MUST** place a new component in the correct `shared/Components/[Type]/` folder, expose it via
  parameters (reusable), add a `#Preview`, and style it with DSS tokens from `shared/Styles/`.
- **MUST** record the reuse decision as an evidence line (see gate).
- **MUST NOT** create a component that duplicates an existing one (exact or near-duplicate).
- **MUST NOT** hardcode color / font / spacing when a DSS token exists or should exist.
- **MUST NOT** create new when parameterizing/composing an existing component would suffice.

## Table of Contents
- [1. Reuse First Strategy](#1-reuse-first-strategy) . L20-L179
- [2. Workflow](#2-workflow) ......................... L181-L233
- [3. Component Locations](#3-component-locations) ... L235-L258
- [4. Design Integration](#4-design-integration) ..... L260-L298
- [5. Style Files](#5-style-files) ................... L300-L358
- [6. Checklist](#6-checklist) ....................... L360-L390
- [7. UI Component Catalog](#7-ui-component-catalog) . L393-L499

---

## 1. Reuse First Strategy

### Core Principle
**ALWAYS try to reuse existing components before creating new ones.**

Benefits:
- Consistency across the app
- Less code to maintain
- Faster development
- Fewer bugs

---

### Decision Tree

```
Need a UI component?
    │
    ├─→ Search existing components
    │       │
    │       ├─→ Found exact match?
    │       │       └─→ ✅ Use it!
    │       │
    │       ├─→ Found similar component?
    │       │       │
    │       │       ├─→ Can customize with parameters?
    │       │       │       └─→ ✅ Add parameters & use!
    │       │       │
    │       │       └─→ Need minor changes?
    │       │               └─→ ✅ Extend or compose!
    │       │
    │       └─→ Nothing similar?
    │               └─→ ⚠️ Create new component
    │
    └─→ Document for future reuse
```

---

### Step-by-Step: Search Before Create

#### 1. Search by Type
```bash
# List all components by category
ls .claude/shared/Components/Buttons/
ls .claude/shared/Components/Cards/
ls .claude/shared/Components/Inputs/
```

#### 2. Search by Name Pattern
```bash
# Search for button-related components
find .claude/shared/Components -name "*Button*"

# Search for card-related components
find .claude/shared/Components -name "*Card*"
```

#### 3. Grep for Similar Functionality
```bash
# Search for components with specific features
grep -r "loading" .claude/shared/Components/
grep -r "icon" .claude/shared/Components/
```

---

### Reuse Strategies

#### Strategy 1: Use As-Is
Component already does what you need.

```swift
// Existing: PrimaryButton.swift
// Just use it!
PrimaryButton(title: "Submit", action: submit)
```

#### Strategy 2: Customize with Parameters
Component is close, add parameters to make it flexible.

**Before:**
```swift
struct PrimaryButton: View {
    let title: String
    let action: () -> Void
    
    var body: some View {
        Button(action: action) {
            Text(title)
                .foregroundColor(.white)
        }
        .background(Color.primary)
    }
}
```

**After (add icon parameter):**
```swift
struct PrimaryButton: View {
    let title: String
    let icon: String? = nil  // ← Add optional parameter
    let action: () -> Void
    
    var body: some View {
        Button(action: action) {
            HStack {
                if let icon = icon {
                    Image(systemName: icon)
                }
                Text(title)
            }
            .foregroundColor(.white)
        }
        .background(Color.primary)
    }
}
```

#### Strategy 3: Compose Multiple Components
Combine existing components to create new functionality.

```swift
// Reuse existing components
struct LoginForm: View {
    var body: some View {
        VStack(spacing: Spacing.md) {
            // Reuse existing input component
            TextInputField(placeholder: "Email", text: $email)
            
            // Reuse existing input component
            SecureInputField(placeholder: "Password", text: $password)
            
            // Reuse existing button component
            PrimaryButton(title: "Login", action: login)
        }
    }
}
```

#### Strategy 4: Extend with ViewModifier
Add functionality without modifying original component.

```swift
// Create reusable modifier
struct ShakeEffect: ViewModifier {
    let shakes: Int
    
    func body(content: Content) -> some View {
        content
            .modifier(ShakeAnimation(shakes: shakes))
    }
}

// Use with any component
PrimaryButton(title: "Submit", action: submit)
    .modifier(ShakeEffect(shakes: errorCount))
```

---

## 2. Workflow

### Step 1: Read Standard Format File
ALWAYS read this file before working with components:
```
.claude/shared/COMPONENT_FORMAT.md
```
This file contains code format, style guide, and project rules.

### Step 2: Search Existing Components (REUSE FIRST!)
```bash
# Browse by category
ls .claude/shared/Components/Buttons/
ls .claude/shared/Components/Cards/
ls .claude/shared/Components/Inputs/

# Search by name
find .claude/shared/Components -name "*Button*"

# Search by functionality
grep -r "loading" .claude/shared/Components/
```

### Step 3: Evaluate Reuse Options
- Can use as-is? → Use it!
- Need customization? → Add parameters
- Need combination? → Compose components
- Nothing similar? → Create new (last resort)

### Step 4: If Creating New Component
- Use design tokens from `.claude/shared/Styles/`
- Follow format from `COMPONENT_FORMAT.md`
- Make it reusable (add parameters)
- Add Preview
- Document usage
- If a required style value does not exist yet, add/update token in `.claude/shared/Styles/` first, then reference token in component code

## 2b. Design Style System (DSS) Source of Truth (Required)

All UI style decisions must be persisted in the DSS locations below:

- Format and conventions: `.claude/shared/COMPONENT_FORMAT.md`
- Color tokens: `.claude/shared/Styles/AppColors.swift`
- Typography tokens: `.claude/shared/Styles/AppFonts.swift`
- Spacing tokens: `.claude/shared/Styles/AppSpacing.swift`

Rules:
- Do not hardcode color, font size/weight, or spacing in feature/component files when a shared token should exist.
- When creating or modifying UI, check shared style files first and reuse existing tokens.
- If no suitable token exists, add it to the correct style file and then use that token in UI code.
- If `shared/Styles` is missing, create it before adding new UI components.
- Keep `COMPONENT_FORMAT.md` aligned with current token naming and usage patterns.

---

## 3. Component Locations

| Type | Location |
|------|----------|
| Button | `.claude/shared/Components/Buttons/` |
| Input | `.claude/shared/Components/Inputs/` |
| Card | `.claude/shared/Components/Cards/` |
| Modal | `.claude/shared/Components/Modals/` |
| Layout | `.claude/shared/Components/Layouts/` |
| Feedback | `.claude/shared/Components/Feedback/` |
| Navigation | `.claude/shared/Components/Navigation/` |

### Common Feedback Components

| Component | Purpose | Reuse For |
|-----------|---------|-----------|
| `LoadingView.swift` | Loading indicator | Any loading state |
| `EmptyStateView.swift` | Empty state with message + CTA | Empty lists, no data |
| `ErrorView.swift` | Error state with retry | API errors, failures |
| `SkeletonView.swift` | Skeleton loading placeholder | Content loading |
| `ToastView.swift` | Toast notifications | Success/error messages |

---

## 4. Design Integration

### When User Sends UI Design Image

1. **First: Check if similar components exist**
   - Search existing components
   - Can you compose existing ones?
   - Can you customize existing ones?

2. **Analyze the image to understand:**
   - UI style (rounded, sharp, gradient, flat...)
   - Color scheme
   - Typography style
   - Spacing pattern
   - Shadow/elevation style

3. **Update or create `.claude/shared/COMPONENT_FORMAT.md` with:**
   - Code template for components
   - Style rules extracted from design
   - Specific examples

4. **Update `.claude/shared/Styles/` if needed:**
   - AppColors.swift
   - AppFonts.swift
   - AppSpacing.swift

### COMPONENT_FORMAT.md

This is the most important file - contains project's standard format.
If it doesn't exist, create it when user sends first design image.
If it exists, read and follow it.

File contents include:
- Code template for struct View
- Naming conventions
- Style conventions (corner radius, shadows, colors...)
- Example component

---

## 5. Style Files

### AppColors.swift

```swift
import SwiftUI

extension Color {
    // Primary Colors
    static let primary = Color(hex: "#007AFF")
    static let secondary = Color(hex: "#5856D6")
    
    // Semantic Colors
    static let success = Color(hex: "#34C759")
    static let warning = Color(hex: "#FF9500")
    static let error = Color(hex: "#FF3B30")
    
    // Neutral Colors
    static let textPrimary = Color(hex: "#000000")
    static let textSecondary = Color(hex: "#8E8E93")
    static let background = Color(hex: "#FFFFFF")
}
```

### AppFonts.swift

```swift
import SwiftUI

extension Font {
    // Headings
    static let h1 = Font.system(size: 34, weight: .bold)
    static let h2 = Font.system(size: 28, weight: .bold)
    static let h3 = Font.system(size: 22, weight: .semibold)
    
    // Body
    static let bodyRegular = Font.system(size: 17, weight: .regular)
    static let bodyBold = Font.system(size: 17, weight: .semibold)
    
    // Small
    static let caption = Font.system(size: 13, weight: .regular)
    static let footnote = Font.system(size: 11, weight: .regular)
}
```

### AppSpacing.swift

```swift
import SwiftUI

enum Spacing {
    static let xs: CGFloat = 4
    static let sm: CGFloat = 8
    static let md: CGFloat = 16
    static let lg: CGFloat = 24
    static let xl: CGFloat = 32
    static let xxl: CGFloat = 48
}
```

---

## 6. Checklist

### Before creating component:
- [ ] Read `.claude/shared/COMPONENT_FORMAT.md`
- [ ] **Search existing components** (ls, find, grep)
- [ ] **Evaluate reuse options** (use as-is, customize, compose)
- [ ] Record reuse evidence (components checked and why not reused)
- [ ] Identify design tokens needed
- [ ] Check `.claude/shared/Styles/` for existing tokens before adding new values
- [ ] Only create new if nothing can be reused

### When creating component:
- [ ] Use design tokens from `.claude/shared/Styles/`
- [ ] Avoid hardcoded color/font/spacing values in component code
- [ ] If new style value is required, add token in the correct file under `.claude/shared/Styles/`
- [ ] Create file in correct folder by type
- [ ] Follow format from COMPONENT_FORMAT.md
- [ ] **Make component reusable** (add parameters for flexibility)
- [ ] Add Preview with multiple examples
- [ ] Document parameters and usage

### After creating component:
- [ ] Test in Preview
- [ ] Test with different data/states
- [ ] Test dark mode if applicable
- [ ] **Document for future reuse**
- [ ] Consider: Can this replace similar components?

---

## 7. UI Component Catalog

Reference specs for common iOS UI components referenced in wireframes documents.

### 7.1 Navigation Bar

- **Large Title**: Scroll to collapse into inline title, prefers large titles enabled
- **Back Button**: System chevron, auto-labeled from previous screen title
- **Right Action Items**: Max 2, system icon or text button
- **Background**: Translucent with scroll edge appearance (blurs content on scroll)
- **Heights**: Regular 44pt, Large title 96pt (collapsible)
- **Title Style**: Large title `h1` (34pt bold), Inline title `bodyBold` (17pt semibold)
- **Search**: Integrated search bar collapses into nav bar on scroll

### 7.2 Buttons

| Variant | Style | Size |
|---------|-------|------|
| Primary | Full-width, rounded, brand color fill, white text | 50pt height |
| Secondary | Full-width, rounded, border only, brand color text | 50pt height |
| Text | No background, brand color text, underline optional | Min tap target 44pt |
| Icon | SF Symbol, no background | 44×44pt tap, icon 22pt |
| Floating Action | Bottom-right, circular, shadow, brand color | 56pt circle |

**States**: Default, Pressed (opacity 0.7), Disabled (opacity 0.4), Loading (spinner replaces title)

### 7.3 Text Fields

| Variant | Details |
|---------|---------|
| Standard | SF Pro 17pt, rounded border, clear button, 44pt height |
| Secure | Eye toggle, auto-fill credential support |
| Search | Magnifying glass icon, Cancel button, rounded rect style |
| Multiline | Expanding text view, min 100pt, max 200pt |

- **Validation**: Real-time inline error below field (red 13pt), checkmark for valid
- **States**: Default, Focused (blue border), Error (red border + message), Disabled (gray)

### 7.4 Cards

- **Corner radius**: 12pt
- **Shadow**: (0, 2, 8, 0.1 opacity)
- **Padding**: 16pt
- **Content layout**: Image (aspect fill, 120pt height), title (headline), subtitle (caption), action

| State | Effect |
|-------|--------|
| Default | As designed |
| Pressed | Scale 0.98 |
| Selected | Brand color border |

| Variant | Style |
|---------|-------|
| Elevated | Default shadow |
| Outlined | Border only, no shadow |
| Filled | Brand color background |

### 7.5 Lists / Table Views

- **Standard row**: 44pt height, left icon (29pt), title (body), accessory (chevron)
- **Subtitle row**: 60pt height, title + subtitle below, icon left
- **Swipe actions**: Delete (red), Edit (orange), Archive (gray), Custom
- **Pull to refresh**: 60pt pull threshold, system spinner
- **Search**: Inline search bar, scope bar for filtering
- **Section headers**: 36pt height, system background, bold caption
- **Section footers**: Plain text, secondary color, for explanatory notes
- **Dividers**: Full-width or inset (16pt from left edge)
- **Editing mode**: Reorder handles (trailing), delete controls (leading)
- **Empty state**: Show `EmptyStateView` when list has no items

### 7.6 Alerts

- **Style**: System alert only (no custom)
- **Buttons**: Max 2 (primary + secondary)
- **Title**: Bold, 17pt. Message: Regular, 13pt
- **Destructive actions**: Red text, bottom position
- **Auto-focus**: On least destructive action
- **Animation**: 200ms scale-in from center
- **Background**: Modal overlay, not dismissible by tap outside for destructive actions
- **Text input alerts**: Support for plain text and secure text fields within alert

### 7.7 Dialogs / Action Sheets

- **Dialog**: 300ms slide-up spring animation, drag handle (36×5pt gray pill)
- **Action Sheet**: Slides from bottom, drag-to-dismiss enabled
- **Input validation**: Real-time, inline errors
- **Background**: 50% black overlay, dismissible by tap outside (except destructive)
- **Sheet sizes**: Half (50%), Medium (70%), Full (95%)

### 7.8 Bottom Sheets

- **Snap points**: Partial (40%), Medium (60%), Full (90%)
- **Drag indicator**: 36×5pt gray pill at top
- **Background**: 30% black overlay
- **Animation**: 300ms slide-up, spring damping 0.8
- **Dismiss**: Drag below threshold or tap outside
- **Content**: Variable height, scroll when content overflows
- **Keyboard**: Sheet adjusts up when keyboard appears
- **Detents**: Use `UISheetPresentationController` detents for native support

### 7.9 Snackbars / Toasts

- **Position**: Bottom, 16pt above safe area
- **Max content**: 2 lines text, 1 action button
- **Duration**: 3-4 seconds (adjustable)
- **Animation**: 200ms slide-up in, 200ms slide-down out
- **Stack**: New replaces old (no stacking)

| Variant | Color |
|---------|-------|
| Info | Brand color |
| Success | Green (#34C759) |
| Warning | Yellow (#FF9500) |
| Error | Red (#FF3B30) |

---

## Reuse-First Gate (Required)

Execution skills (`execution-implement`, `execution-quick`, `execution-quality-gates`) run this gate
for any task that touches a UI component. It is the single source of truth for the reuse-vs-create
decision — the executor must not skip the search or invent its own components silently.

**Checklist (every item must pass):**
- [ ] Searched `.claude/shared/Components/` by type / name / functionality before deciding.
- [ ] Chose the highest-reuse option that works (as-is > parameterize > compose > extend > create new).
- [ ] If creating new: no existing component covers the need (near-duplicates rejected with a reason).
- [ ] New component is in the correct `shared/Components/[Type]/` folder, parameterized, has a `#Preview`.
- [ ] All color/font/spacing come from DSS tokens in `shared/Styles/` (no hardcoded style values).
- [ ] Task Registry `Files` column lists the exact component file path(s).

**BLOCK conditions** → mark task `blocked`, do not set `done`:
- A new component was created without evidence that `shared/Components/` was searched.
- The new component duplicates an existing one that could have been reused/parameterized/composed.
- The component is placed in the wrong folder, lacks a `#Preview`, or hardcodes style values.

**Evidence line** (required in task notes for any component task):
```
Reuse: <component>
```
or, when creating new:
```
New: <component> | Reason: <why no reuse> | Searched: <dirs/candidates examined>
```
Pair it with the DSS evidence line:
```
DSS: reused tokens <list>  |  or  DSS: added tokens <list> in shared/Styles
```

Do not mark a component task `done` until: preview compiles, required states render, the component is
reusable via parameters where practical, and styles reference DSS tokens.
