---
name: uiux-analysis-contract
description:
  Strict output contract for spec-uiux-analyzer. Enforces exact directory structure, file naming conventions, and output format for UI/UX analysis deliverables.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# UI/UX Analysis Output Contract

## Purpose
This skill ensures spec-uiux-analyzer produces output in EXACT format with EXACT paths.

---

## 1) EXACT Output Directory

```
{{IDE_CONFIG_DIR}}specs/[project-name]/design-ui/
```

CRITICAL: Always use this exact path structure. Never use variations like:
- `design/` 
- `ui-analysis/`
- `ux-docs/`
- Any other variation

---

## 2) EXACT File Structure

```
design-ui/
├── analysis-summary.md           # MUST exist - executive summary
├── design-system.md              # MUST exist - visual specs
├── screens/
│   ├── screen-wf001-[name].md   # One file per screen from Wireframes.md
│   ├── screen-wf002-[name].md
│   └── ...
├── interactions/
│   └── micro-interactions.md    # MUST exist
└── accessibility/
    └── accessibility-report.md  # MUST exist
```

OPTIONAL (create if analysis warrants):
```
├── consistency/
│   └── consistency-report.md
```

---

## 3) EXACT File Naming Rules

### Screen Analysis Files
- Format: `screen-wf[XXX]-[name].md`
- Where XXX = screen number from Wireframes.md (001, 002, etc.)
- Where [name] = lowercase with hyphens, e.g.:
  - `screen-wf001-splash.md`
  - `screen-wf002-onboarding.md`
  - `screen-wf003-login.md`

### NEVER use:
- `WF001.md`
- `Splash-Screen.md`
- `login-screen.md`
- Any variation not matching `screen-wf###-[name].md`

---

## 4) Required Content Per File

### analysis-summary.md (MANDATORY)
```markdown
---
screen_id: analysis-summary
version: 1.0
analyst: spec-uiux-analyzer
date: YYYY-MM-DD
---

# UI/UX Deep Analysis Summary

## Project: [project-name]
## Analysis Date: YYYY-MM-DD
## Version: 1.0

---

## Executive Summary

| Metric | Value |
|--------|-------|
| Total Screens | N |
| Heuristic Compliance | X% |
| Accessibility Score | X% |
| Critical Issues | N |
| Recommendations | N |

---

## Heuristic Evaluation (Nielsen's 10)

| # | Heuristic | Compliance | Issues |
|---|-----------|------------|--------|
| 1 | Visibility of system status | X% | ... |

---

## Critical Issues

### 1. [Issue Title]
- **Severity**: High/Medium/Low
- **Affected Screens**: ...
- **Recommendation**: ...

---

## Top Recommendations

### Must Fix
1. ...

### Should Fix
1. ...

### Nice to Have
1. ...

---

## Files Produced

| File | Description |
|------|-------------|
| `design-ui/analysis-summary.md` | This file |
| `design-ui/design-system.md` | Visual design specifications |
| `design-ui/screens/*.md` | Individual screen analyses |
| `design-ui/interactions/micro-interactions.md` | All micro-interactions |
| `design-ui/accessibility/accessibility-report.md` | WCAG compliance |

---

**Analysis performed by**: spec-uiux-analyzer
**Methodology**: Nielsen's Heuristics + WCAG 2.1 + Modern UX Best Practices
```

### design-system.md (MANDATORY)
Must include:
- Color System (Primary, Semantic, Neutral - with hex codes)
- Typography (type scale table)
- Spacing System (8pt grid tokens)
- Corner Radius tokens
- Shadows tokens
- iOS-Specific (safe areas, nav bar, tab bar)
- Animation Specifications
- Interaction Patterns (gestures, haptics)

### screen-wf###-[name].md (ONE PER SCREEN)
Must include ALL sections:
```markdown
---
screen_id: WF-XXX
screen_name: [Name]
version: 1.0
analyst: spec-uiux-analyzer
date: YYYY-MM-DD
---

# Screen Analysis: [Name]

## Metadata
## Purpose
## User Stories
## Information Architecture
## User Actions
## Component Specifications
## Interaction Details
## Error States
## Validation Rules
## Accessibility (WCAG 2.1)
## Usability Checklist
## Recommendations
## Cross-Screen Consistency
## Related Files
```

### micro-interactions.md (MANDATORY)
Must include:
- Interaction categories table
- Animation specifications table
- Implementation guidelines (SwiftUI + UIKit)

### accessibility-report.md (MANDATORY)
Must include:
- WCAG summary table
- Failed items list
- Screen-by-screen accessibility
- Recommendations by priority

---

## 5) Strict Execution Rules

### Step 1: DETERMINE PROJECT NAME
- Read `{{IDE_CONFIG_DIR}}specs/[project-name]/Wireframes.md`
- Extract [project-name] from path

### Step 2: CREATE DIRECTORY STRUCTURE
```bash
# MUST run these commands FIRST
mkdir -p {{IDE_CONFIG_DIR}}specs/[project-name]/design-ui/screens
mkdir -p {{IDE_CONFIG_DIR}}specs/[project-name]/design-ui/interactions
mkdir -p {{IDE_CONFIG_DIR}}specs/[project-name]/design-ui/accessibility
```

### Step 3: COUNT SCREENS
- Count ALL screens in Wireframes.md
- Create ONE file per screen

### Step 4: WRITE FILES IN ORDER
1. design-system.md (first, establishes standards)
2. screen-wf001-xxx.md through screen-wfNNN-xxx.md
3. micro-interactions.md
4. accessibility-report.md
5. analysis-summary.md (last, summarizes all)

---

## 6) Non-Negotiable Rules

### NEVER DO:
- ❌ Skip creating any mandatory file
- ❌ Use different file names than specified
- ❌ Put files in wrong directory
- ❌ Skip any required section in a file
- ❌ Use placeholder text like "[TODO]" or "[Add content]"
- ❌ Leave analysis incomplete

### ALWAYS DO:
- ✅ Use exact paths as specified
- ✅ Use exact file names as specified
- ✅ Include all required sections
- ✅ Fill in every table completely
- ✅ Provide specific recommendations
- ✅ Include real content, not placeholders

---

## 7) Quality Gate

Before completing, verify:

- [ ] `analysis-summary.md` exists and has all sections
- [ ] `design-system.md` exists and has color/typography/spacing
- [ ] All screens from Wireframes.md have corresponding `screen-wf###-*.md` files
- [ ] `micro-interactions.md` exists
- [ ] `accessibility-report.md` exists
- [ ] No placeholder text remains
- [ ] All paths use `{{IDE_CONFIG_DIR}}specs/[project-name]/design-ui/`

If ANY check fails → Fix before completing.

---

## 8) Exit Criteria

Task is complete ONLY when:
1. All 5 mandatory files exist
2. All screens analyzed (1 file per screen)
3. All tables fully populated
4. No placeholders or TODOs remain
5. All paths are exact as specified
