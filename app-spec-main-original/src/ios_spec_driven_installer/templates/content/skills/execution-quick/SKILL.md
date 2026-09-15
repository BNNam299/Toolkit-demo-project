---
name: execution-quick
description: Quick implementation without full specs for small features (<4 hours). Use for simple features, prototypes, experiments, single components.
---

# Execution Quick

## Purpose
Implement small features quickly without creating full spec files (requirements.md, design.md, tasks.md).

## When to Use

Use this skill when:
- Feature is simple (<4 hours estimated)
- Single screen or component
- Prototype or experiment
- Solo developer (no team collaboration needed)
- Quick bug fix with new code

**Do NOT use when:**
- Feature is complex (>4 hours)
- Multiple screens/components
- Team collaboration needed
- Long-term maintenance expected
- Critical business logic
- **The feature is a core/production feature that ships to users** — anything that appears in the roadmap Spec Registry, owns a WF-XXX screen, or handles user data, payments, auth, or privacy MUST go through the full `/ios-spec` → `/ios-execute` flow (requirements → design → tasks with quality gates). This quick path is ONLY for throwaway prototypes, experiments, and tiny isolated helpers. Do not use it to dodge the depth/completeness/consistency gates on real features.

---

## Process

### Step 1: Gather Requirements (Inline)

Ask user for:
1. What is the feature?
2. What should it do? (brief description)
3. What are the acceptance criteria? (2-3 bullet points)
4. Any specific design requirements?

Example:
```
Feature: Settings Toggle
Description: Add a toggle to enable/disable notifications
Acceptance Criteria:
- Toggle appears in Settings screen
- State persists across app restarts
- Changing toggle updates notification permissions
```

### Step 2: Quick Design (Mental Model)

Determine:
- **Files needed**: Which files to create/modify
- **Architecture**: ViewModel? Service? Just View?
- **Dependencies**: Any external dependencies?

If user provides Figma URL:
- Parse file URL: `figma.com/file/{fileKey}/{name}`
- Parse node URL: `figma.com/file/{fileKey}/{name}?node-id={nodeId}`
- Use `figma_get_styles(fileKey)` for tokens
- Use `figma_get_node(fileKey, nodeId)` for exact screen/component specs

**Before creating any new UI component (REQUIRED):**
- Search `{{IDE_CONFIG_DIR}}shared/Components/` for reusable matches
- Prefer reuse via as-is, parameterization, or composition
- Only create new component if no compatible option exists
- Document decision: `Reuse` or `New + reason`

Document inline:
```
Files:
- Views/SettingsView.swift (modify)
- ViewModels/SettingsViewModel.swift (modify)
- Services/NotificationService.swift (new)

Architecture:
- Add @Published var notificationsEnabled in ViewModel
- Add toggle() method in ViewModel
- Call NotificationService to update permissions
```

### Step 3: Implement

Create/modify files directly. No task IDs, no traceability matrix. Just implement the feature.

**The quick path is lighter on process, NOT on quality.** These three gates still apply (run them
inline, no formal checkpoint needed — see the owning skill for criteria):
- **Structure Compliance Gate** (`ios-architecture`) — place every file in the canonical tree with correct naming.
- **Reuse-First Gate** (`ios-components`) — search `shared/Components/` before creating; reuse > parameterize > compose > new.
- **UX Compliance Gate** (`ios-ui-ux`) — any UI must render all 4 states (loading/empty/error+recovery/success), use DSS tokens, and pass basic a11y + dark mode.

If a gate can't be satisfied within the quick scope, stop and upgrade to the full spec workflow.

### Step 4: Quick Validation

1. Build with mcp-xcode
2. Fix any errors
3. Quick manual test
4. Commit

**No formal checkpoints, no user confirmations between steps.**

---

## Implementation Templates

### Single Component

```swift
// File: {{IDE_CONFIG_DIR}}shared/Components/[Name].swift
// Feature: [Brief description]
// AC: [Acceptance criteria]

import SwiftUI

struct [Name]: View {
    // Implementation
    var body: some View {
        // UI
    }
}

#Preview {
    [Name]()
}
```

### Feature with ViewModel

```swift
// File: Features/[Feature]/ViewModels/[Name]ViewModel.swift
// Feature: [Brief description]

import Foundation
import Combine

@MainActor
final class [Name]ViewModel: ObservableObject {
    @Published var state: State = .idle
    
    func action() {
        // Implementation
    }
}

// File: Features/[Feature]/Views/[Name]View.swift
import SwiftUI

struct [Name]View: View {
    @StateObject private var viewModel = [Name]ViewModel()
    
    var body: some View {
        // UI
    }
}
```

---

## Validation Checklist

Quick checklist (not formal):
- [ ] Feature works as described
- [ ] Build passes
- [ ] No obvious bugs
- [ ] Code follows project style
- [ ] Files placed in the canonical structure (Structure Gate)
- [ ] Existing components checked before creating new one (Reuse-First Gate)
- [ ] UI renders all 4 states + basic a11y/dark mode (UX Gate)
- [ ] Committed to git

---

## When to Upgrade to Full Spec

If during implementation you realize:
- Feature is more complex than expected
- Need multiple screens/components
- Need team collaboration
- Will require long-term maintenance

**Stop and switch to full spec workflow:**
1. Document what you've learned
2. Create requirements.md using spec-requirements skill
3. Create design.md using spec-design skill
4. Create tasks.md using spec-tasks skill
5. Continue with execution-implement skill

---

## Comparison

| Aspect | Quick Implement | Full Spec |
|--------|----------------|-----------|
| Time | <4 hours | >4 hours |
| Spec Files | None | 3 files |
| Traceability | Inline comments | Full chain |
| Checkpoints | None | Multiple |
| User Confirmations | None | After each file |
| Team Collaboration | Solo | Team |
| Documentation | Minimal | Comprehensive |

---

## Rules

### DO:
- Keep it simple
- Focus on working code
- Quick validation
- Commit frequently

### DON'T:
- Create spec files
- Formal checkpoints
- User confirmations between steps
- Complex traceability

### WHEN IN DOUBT:
- Use full spec workflow
- Better to over-document than under-document
- Quick implement is for truly simple features only

---

## Output Format

After completion:
```
✅ Quick Implementation Complete

Feature: [Name]
Files Created/Modified:
- [File 1]
- [File 2]

Build Status: ✅ Pass
Commit: [hash]

Note: This was a quick implementation without full specs.
If this feature grows in complexity, consider creating full specs.
```