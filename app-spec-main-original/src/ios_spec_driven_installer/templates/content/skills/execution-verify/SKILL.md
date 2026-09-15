---
name: execution-verify
description: Verify implementation completeness, correctness, and coherence against specifications. Use after implementation to validate feature before completion.
---

# Execution Verify

## Purpose
Comprehensively verify that implementation satisfies specifications across three dimensions: completeness, correctness, and coherence.

## When to Use
- After completing all implementation tasks
- Before archiving feature
- When user requests verification

## Input
- `{{IDE_CONFIG_DIR}}specs/[feature-name]/requirements.md`
- `{{IDE_CONFIG_DIR}}specs/[feature-name]/design.md`
- `{{IDE_CONFIG_DIR}}specs/[feature-name]/tasks.md`
- Implementation code (Swift files)

## Verification Dimensions

### 1. Completeness

**Requirements Coverage:**
- For each requirement in requirements.md, is there corresponding implementation?
- Are all acceptance criteria addressed?
- Are edge cases handled?

**Tasks Completion:**
- For each task in tasks.md, is status marked as `done`?
- Do implementation files exist?
- Are tests written (if specified)?

**Code Presence:**
- Verify key files from design.md exist (Views/ViewModels, Services, Models, Tests)

### 2. Correctness

**Behavioral Correctness:**
- Does implementation match spec intent?
- Happy paths work as described
- Error paths handled appropriately
- Edge cases covered

**Technical Correctness:**
- Code compiles without errors
- No force unwraps or unsafe operations
- Proper error handling
- Memory management correct (no leaks)

**Test Coverage:**
- Unit tests exist for core logic
- Tests verify ACs
- Edge cases tested

### 3. Coherence

**Design Alignment:**
- Does implementation follow design.md?
- Architecture pattern used correctly
- Component boundaries respected
- Data flow matches design
- Naming conventions consistent

**Code Quality:**
- Follows Swift style guidelines
- Consistent with existing codebase
- Proper access control
- Clear separation of concerns

## Verification Process

### Step 1: Parse Specs
Read and extract:
- Requirements with ACs
- Design decisions
- Task list
- Expected file structure

### Step 2: Inspect Implementation
Find all Swift files for this feature:
```
glob "**/FeatureName*.swift"
glob "**/*FeatureName*.swift"
glob "**/*FeatureName*Test*.swift"
glob "**/*FeatureName*Spec*.swift"
```

### Step 3: Cross-Reference
Create traceability matrix mapping: Req → AC → Design → Task → Implementation → Test

### Step 4: Identify Gaps

**Critical Issues** (block completion):
- Missing requirement implementation
- Failing acceptance criteria
- Build errors
- Crashes

**Warnings** (should fix):
- Missing tests
- Partial implementation
- Code style issues
- Documentation gaps

**Notes** (informational):
- Additional edge cases handled
- Implementation improvements beyond spec
- Refactoring opportunities

## Output Format

Reference the verification report template at `{{IDE_CONFIG_DIR}}doc-templates/verification-report.md` for the exact output structure.

Key sections:
1. Executive Summary (status, counts)
2. Completeness (requirements, tasks, code)
3. Correctness (behavioral, technical, tests)
4. Coherence (architecture, naming, quality)
5. Traceability Matrix
6. Critical Issues (blocking)
7. Warnings (recommended fixes)
8. Recommendations (optional improvements)
9. Next Steps

## Rules
- Be thorough but pragmatic
- Distinguish critical vs nice-to-have
- Provide specific, actionable fixes
- Don't block on minor style issues
- Verify both positive and negative cases
- Check error handling carefully