---
name: project-docs-overview
description: Create Project_Overview.md with high-level vision, architecture, and roadmap. Use after PRD is approved.
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - WebSearch
  - WebFetch
skills:
  - project-docs-lifecycle
  - project-docs-contract
  - project-docs-quality-gates
  - ios-architecture
---

# Create Project_Overview.md

## Objective

Create a Project_Overview.md that captures high-level vision, architecture direction, and roadmap. The PRD is the product source of truth. This document does not duplicate it.

## Step 1: Gather Information

Check whether `{{IDE_CONFIG_DIR}}specs/[project-name]/PRD.md` exists.

- **PRD exists**: read it. Use it as the product authority. Ask clarifying questions only for gaps.
- **PRD missing**: ask the user for project context directly (target users, core problem, key features, technical constraints).

Never invent product details. If the PRD covers it, reference it rather than restating it.

## Step 2: Create Directory

Follow `project-docs-lifecycle` to set up the specs directory structure for this project. Ensure `{{IDE_CONFIG_DIR}}specs/[project-name]/` exists before writing.

## Step 3: Write Project_Overview

Write to `{{IDE_CONFIG_DIR}}specs/[project-name]/Project_Overview.md`.

**You MUST read `{{IDE_CONFIG_DIR}}doc-templates/Project_Overview.md`** for section structure; its `QUALITY-GATE-MANIFEST` (end of template) is the authoritative list of required sections — reproduce them, do NOT copy the manifest block into the output. Use the `ios-architecture` skill for iOS-specific architecture guidance.

### PRD Boundary Rules

The PRD owns market analysis, competitor breakdowns, and feature prioritization. This document does not repeat that content. Instead:

- Reference the PRD for product scope and positioning
- Focus this document on architecture, tech stack, timeline, and execution plan
- If the PRD already describes a feature, link to it rather than summarizing it here

## Step 4: Quality Gate and Confirmation

1. Run the overview quality gate: invoke `project-docs-quality-gates` with gate `gate-overview`
2. Address any issues found
3. Follow `project-docs-lifecycle` to present the draft for user confirmation

## Non-negotiable Rules

- **PRD first.** If no PRD exists, flag this. The overview should not be the first spec written.
- **No duplication.** Don't copy market or competitor content from the PRD. Reference it.
- **Write only to specs directory.** Never write project docs outside `{{IDE_CONFIG_DIR}}specs/[project-name]/`.