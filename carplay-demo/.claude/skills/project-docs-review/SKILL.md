---
name: project-docs-review
description: Cross-review project documentation for consistency, traceability, contradictions, and PRD/Overview duplication. Use when validating project docs, checking document quality, verifying traceability.
allowed-tools:
  - Read
  - Grep
  - Glob
skills:
  - project-docs-contract
---

# Project Documentation Cross-Review

## Objective

Cross-review the full project doc set for consistency, traceability, contradictions, and PRD/Overview duplication.

## Required Files

Read all seven docs:

1. `PRD.md`
2. `Project_Overview.md`
3. `Use_Cases.md`
4. `Functional_Requirements.md`
5. `Wireframes.md`
6. `UX_Flows.md`
7. `Project_Implementation_Roadmap.md`

If any file is missing, report the gap but **continue reviewing what exists**.

## Review Output Sections

### 1. Scorecard

Four categories, each rated **Pass** or **Needs Work**:

| Category | Rating |
|---|---|
| Consistency | Pass / Needs Work |
| Traceability | Pass / Needs Work |
| Coverage | Pass / Needs Work |
| Clarity | Pass / Needs Work |

### 2. Critical Issues

Must-fix items. Each entry: file, severity, what is wrong, why it matters.

### 3. Top 5 Quick Fixes

Prioritized. One-line each. Actionable edits only.

### 4. Change Requests

Grouped by file. Include rationale and proposed edit for each.

### 5. Traceability Gaps

Items present in one doc but missing from downstream docs that should reference them.

### 6. PRD vs Overview Duplication Check

Identify duplicated market or competitor analysis between PRD and Overview. Flag text in Overview that should reference PRD instead of restating it.

### 7. Optional Improvements

Nice-to-haves that don't affect delivery.

## Severity Levels

- **Critical** — blocks delivery.
- **Major** — significant gap in quality or completeness.
- **Minor** — polish and cleanup.

## Non-Negotiable Rules

- **Do NOT edit any files.** This is a READ ONLY review.
- **Do NOT create any new files.**
- **Max 15 total issues** across all severities combined.
- **PRD/Overview duplication** must be flagged as at least Major severity.
- **Prefer specific, minimal edits** that preserve the authors' intent over broad rewrites.