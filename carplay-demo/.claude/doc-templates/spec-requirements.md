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

#### States & Edge Cases
<!-- For EACH state that applies to this requirement, provide an AC (above) that defines it.
     If a state does not apply, write "N/A — <reason>". Do NOT leave blank. -->
- **Loading:** [AC ref or N/A — reason]
- **Empty:** [AC ref or N/A — reason]
- **Error / failure:** [AC ref or N/A — reason]
- **Offline / stale:** [AC ref or N/A — reason]
- **Permission-denied:** [AC ref or N/A — reason]

#### Validation Rules
<!-- Required if this requirement takes user input. Enumerate concrete rules; else "N/A — no user input". -->
| VR ID | Field / Input | Rule (format · range · required) | On violation |
|-------|---------------|----------------------------------|--------------|
| VR-XXX.1 | [field] | [e.g. 1–5000, integer, required] | [message / AC ref] |

#### Wireframe Affordance Coverage
<!-- List EVERY Component and Interaction of the WF-XXX screen(s) this requirement owns, and the AC
     that covers each. Any affordance not covered here must be moved to another spec or declared out-of-scope. -->
- [WF-XXX affordance] → [AC-XXX.Y] | [or "out-of-scope → owned by <spec/FR>"]

### Requirement 2: [Short Title]
**User Story:** As a [role], I want [capability], so that [benefit]
**Source:** [FR-XXX], [UC-XXX]

#### Acceptance Criteria
1. WHEN [event] THEN THE SYSTEM SHALL [response]
2. WHILE [state] THE SYSTEM SHALL [response]

<!-- DYNAMIC: Add more requirements as needed. Each follows the same pattern. -->

## Non-Functional Requirements
<!-- Expand beyond the 3 defaults with the categories that apply to THIS feature's app type.
     Every NFR needs a measurable target (numbers), not "fast/secure/user-friendly". -->
- NFR-001: Performance - [measurable target, e.g. list renders <500ms with 100+ items]
- NFR-002: Reliability - [measurable target, e.g. retry ≤3 / ≤10s; no data loss on failure]
- NFR-003: Security - [measurable target, e.g. tokens in Keychain only, never logged]
<!-- Add the applicable ones (delete those truly N/A, don't leave placeholder): -->
- NFR-00X: Offline / Sync - [cached read behavior, staleness marker, queued-write flush]
- NFR-00X: Permissions - [camera/photo/notification handling + denied path]
- NFR-00X: Privacy / PII - [what personal data is handled, storage, deletion/export]
- NFR-00X: Accessibility - [VoiceOver labels, Dynamic Type, contrast ≥4.5:1, ≥44pt targets]

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
  - "Every requirement has a Source field referencing FR-XXX and UC-XXX IDs from project docs.
     INFRA CARVE-OUT: when the roadmap registry declares this spec with an empty covers
     ({fr: [], uc: [], wf: []}) — i.e. an infra spec with no user surface — a Source of NFR-XXX
     IDs from Functional_Requirements.md §3 is accepted instead, provided those NFRs' acceptance
     criteria are ones THIS spec actually satisfies. The requirement SHOULD then add an
     'Enables (does not implement)' line naming the FRs it unblocks and their owning specs.
     Citing an unrelated FR to satisfy this check is trace laundering = Fail. A requirement with
     NO Source at all is a Fail regardless of covers."
  - "Every requirement has EARS acceptance criteria (WHEN/THEN/IF/WHILE/SHALL), each testable"
  - "Every requirement's 'States & Edge Cases' lists Loading/Empty/Error/Offline/Permission-denied, each either mapped to an AC or explicitly marked 'N/A — <reason>' (a blank or missing state = Fail; this replaces the weaker 'at least one error AC' floor)"
  - "Every requirement that takes user input has a 'Validation Rules' table enumerating concrete VR-XXX rules (format/range/required + on-violation); requirements with no input say 'N/A — no user input'"
  - "Every requirement has a 'Wireframe Affordance Coverage' list where EVERY Component and Interaction of its owned WF-XXX screen(s) maps to an AC or is declared out-of-scope with an owning spec/FR — no silently dropped affordance"
  - "Carry-forward: context variations, alternate flows, and sub-flows present in the source UC/FR are reflected as ACs here (not just the UC ID cited) — a requirement that flattens a multi-context UC into a single happy-path AC = Fail"
  - "IDs follow REQ-XXX and AC-XXX.Y format consistently (stable across revisions)"
  - "Every NFR has a measurable target — reject vague 'fast/secure/user-friendly' without numbers; NFR set is expanded to the categories that apply to the feature's app type (offline/permissions/privacy/accessibility as relevant), not just the 3 defaults"
  - "Evidence References section cites concrete data from the PRD Evidence Table (market data, KPIs, source paths)"
QUALITY-GATE-MANIFEST:END -->