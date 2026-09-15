# [Feature Name] - Requirements

## Overview
[2-4 sentence summary of feature goal and scope]

## Evidence References
- **Market data from PRD:** [summary of key evidence - e.g., market size, competitor data, user insights]
- **Source documents:** [list relevant doc paths with section refs]
- **Key KPIs:** [from PRD success metrics section]

## Requirements

### Requirement 1: [Short Title]
**User Story:** As a [role], I want [capability], so that [benefit]
**Source:** [FR-XXX], [UC-XXX]

#### Acceptance Criteria
1. WHEN [event] THEN THE SYSTEM SHALL [response]
2. IF [condition] THEN THE SYSTEM SHALL [response]
3. WHEN [event] AND [condition] THEN THE SYSTEM SHALL [response]

### Requirement 2: [Short Title]
**User Story:** As a [role], I want [capability], so that [benefit]
**Source:** [FR-XXX], [UC-XXX]

#### Acceptance Criteria
1. WHEN [event] THEN THE SYSTEM SHALL [response]
2. WHILE [state] THE SYSTEM SHALL [response]

<!-- DYNAMIC: Add more requirements as needed. Each follows the same pattern. -->

## Non-Functional Requirements
- NFR-001: Performance - [target]
- NFR-002: Reliability - [target]
- NFR-003: Security - [target]

<!-- QUALITY-GATE-MANIFEST:START
# SINGLE source of truth for gate-requirements. Do NOT copy this block into the produced
# requirements.md under specs/. The gate matches sections by NAME, ignoring leading numbering
# and any trailing placeholder in the produced heading.
doc: Requirements
gate: gate-requirements
required_major:
  - "Overview"
  - "Evidence References"
  - "Requirements"
  - "Non-Functional Requirements"
# Per-requirement parts (User Story / Source / Acceptance Criteria) are DYNAMIC — one block per
# requirement — so they are verified via quality_checks below, not as fixed required_minor.
required_minor: {}
quality_checks:
  - "Every requirement has a User Story (As a [role], I want [capability], so that [benefit])"
  - "Every requirement has a Source field referencing FR-XXX and UC-XXX IDs from project docs"
  - "Every requirement has EARS acceptance criteria (WHEN/THEN/IF/WHILE/SHALL), each testable"
  - "At least one AC per requirement covers a negative / error / edge-case behavior"
  - "IDs follow REQ-XXX and AC-XXX.Y format consistently (stable across revisions)"
  - "Every NFR has a measurable target — reject vague 'fast/secure/user-friendly' without numbers"
  - "Evidence References section cites concrete data from the PRD Evidence Table (market data, KPIs, source paths)"
QUALITY-GATE-MANIFEST:END -->