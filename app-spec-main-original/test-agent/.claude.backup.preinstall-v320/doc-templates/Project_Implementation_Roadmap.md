# [App Name] - Project Implementation Roadmap

**Version**: 1.0  
**Date**: [Current Date]  
**Author**: AI Research Agent

---

## Overview

| Property | Value |
|----------|-------|
| Project | [project-name] |
| Total Specs | [N] |
| Total Phases | [M] |
| Target Duration | [estimate] |
| Generated | [timestamp] |

## Scope Decision Record

Single source of truth for scope. Every priority label across PRD, Project_Overview §4,
Use_Cases §7, and Functional_Requirements §1.3 MUST follow this one legend:

| Tier | UC/Overview label | FR label | Code | In MVP? |
|------|-------------------|----------|------|---------|
| Tier 1 | Must-Have | High | P0 | Yes (MVP) |
| Tier 2 | Should-Have | Medium | P1 | No (Post-MVP) |
| Tier 3 | Could-Have / Nice-to-Have | Low | P2 | No (Future) |

**MVP definition:** [list the exact UC/FR IDs in MVP, or state "MVP = all N FR/UC"]

**Scope rules (enforced by gate-roadmap):**
- A spec/phase is in MVP scope **iff** every UC/FR it covers is Tier 1 (Must-Have) —
  or is explicitly promoted here with a reason.
- **Dependency rule:** if a Tier-1 (MVP) flow depends on a UC as a recovery/critical path,
  that UC MUST also be Tier 1. A recovery-path UC cannot be Post-MVP while its flow is MVP.
- Any deviation from the priority labels in UC/FR must be recorded in "Scope Promotions" below.

**Scope Promotions (deviations from UC/FR priority, with reason):**
| UC/FR | Original tier | Promoted to | Reason |
|-------|---------------|-------------|--------|
| [none, or list] | | | |

## Project Structure

### Directories
```
[App/]
[Core/]
[Features/]
  [Feature-A/]
  [Feature-B/]
```

### Files
| Path | Type |
|------|------|
| [App/main.swift] | [entry] |

## Phase Timeline

| Phase | Specs | Duration | Entry Criteria | Deliverables | Exit Criteria |
|-------|-------|---------|----------------|--------------|--------------|
| Phase 1: Project Structure | project-structure | [days] | [criteria] | [deliverables] | [exit criteria] |
| Phase 2: Shared Foundations | shared-foundations | [days] | [criteria] | [deliverables] | [exit criteria] |
| Phase 3: [Feature A] | feature-[a] | [days] | [criteria] | [deliverables] | [exit criteria] |
| Phase 4: [Feature B] | feature-[b] | [days] | [criteria] | [deliverables] | [exit criteria] |
| ... | ... | ... | ... | ... | ... |

### Estimation Assumptions

This Roadmap is the **single source of effort**. State the assumptions behind every
Duration/`[days]` number so estimates are reconcilable (Use_Cases carries priority +
complexity only, NOT day estimates):
- Parallel developers: [N]
- AI-assisted coding: [yes/no]
- 1 day = [ideal engineering hours]
- Buffer/contingency: [%]

## Feature→Screen Mapping

| Feature Spec | Screens (WF) | Archetype | Source UC Section |
|-------------|--------------|-----------|-------------------|
| feature-[a] | WF-XXX ([Name]), WF-XXX ([Name]) | [archetype] | [UC section] |
| feature-[b] | WF-XXX ([Name]), WF-XXX ([Name]) | [archetype] | [UC section] |

## Spec Registry

### Phase 1: Project Structure

| Spec ID | Status | Priority | Depends On | Summary | Screens (WF) | Files Created | Key Functions / Components | Covers (FR, UC, WF) |
|---------|--------|----------|-----------|---------|--------------|---------------|---------------------------|---------------------|
| `project-structure` | [status] | [N] | None | [summary] | N/A | [files] | [classes] | N/A |

### Phase 2: Shared Foundations

| Spec ID | Status | Priority | Depends On | Summary | Screens (WF) | Files Created | Key Functions / Components | Covers (FR, UC, WF) |
|---------|--------|----------|-----------|---------|--------------|---------------|---------------------------|---------------------|
| `shared-foundations` | [status] | [N] | project-structure | [summary] | N/A | [files] | [classes] | N/A |

### Phase [N]: [Feature A]

| Spec ID | Status | Priority | Depends On | Summary | Screens (WF) | Files Created | Key Functions / Components | Covers (FR, UC, WF) |
|---------|--------|----------|-----------|---------|--------------|---------------|---------------------------|---------------------|
| `feature-[a]` | [status] | [N] | project-structure, shared-foundations | [summary] | WF-XXX ([Name]), WF-XXX ([Name]) | [model.swift], [service.swift], [viewmodel.swift], [views/*.swift] | [classes] | FR-XXX–FR-XXX, UC-XXX, WF-XXX |

### Phase [N+1]: [Feature B]

| Spec ID | Status | Priority | Depends On | Summary | Screens (WF) | Files Created | Key Functions / Components | Covers (FR, UC, WF) |
|---------|--------|----------|-----------|---------|--------------|---------------|---------------------------|---------------------|
| `feature-[b]` | [status] | [N] | project-structure, shared-foundations, feature-[a] | [summary] | WF-XXX ([Name]), WF-XXX ([Name]) | [model.swift], [service.swift], [viewmodel.swift], [views/*.swift] | [classes] | FR-XXX–FR-XXX, UC-XXX, WF-XXX |

## File Breakdown

### Phase 1: Project Structure

| File Path | Type | Key Functions / Components | Covers |
|-----------|------|---------------------------|--------|
| [file] | [type] | [classes] | N/A |

### Phase 2: Shared Foundations

| File Path | Type | Key Functions / Components | Covers |
|-----------|------|---------------------------|--------|
| [file] | [type] | [classes] | N/A |

### Phase [N]: [Feature A]

| File Path | Type | Key Functions / Components | Covers |
|-----------|------|---------------------------|--------|
| [model.swift] | model | [struct] | FR-XXX, UC-XXX |
| [service.swift] | service | [class], [method] | FR-XXX |
| [viewmodel.swift] | viewmodel | [class] | FR-XXX |
| [view.swift] | view | [View], [Component] | FR-XXX, UC-XXX, WF-XXX |
| [view2.swift] | view | [View], [Component] | FR-XXX, UC-XXX, WF-XXX |

## Screen→File Breakdown

### Phase [N]: [Feature A] (WF-XXX: [Name], WF-XXX: [Name])

| Screen (WF) | File Path | Key Functions / Components | Covers |
|-------------|-----------|---------------------------|--------|
| WF-XXX | [view.swift] | [View], [Component] | FR-XXX |
| WF-XXX | [viewmodel.swift] | [ViewModel] | FR-XXX |
| WF-XXX | [view2.swift] | [View2] | FR-XXX |

## Machine-Readable Dependencies

```json
{
  "project": "[project-name]",
  "generated": "[timestamp]",
  "phases": [
    {
      "phase": 1,
      "name": "project-structure",
      "duration_days": [N],
      "specs": ["project-structure"]
    },
    {
      "phase": 2,
      "name": "shared-foundations",
      "duration_days": [N],
      "specs": ["shared-foundations"]
    },
    {
      "phase": 3,
      "name": "feature-[a]",
      "duration_days": [N],
      "specs": ["feature-[a]"]
    }
  ],
  "specs": {
    "project-structure": {
      "status": "pending",
      "priority": 1,
      "phase": 1,
      "depends_on": [],
      "blocks": ["shared-foundations", "feature-[a]"],
      "covers": {"fr": [], "uc": [], "wf": []},
      "files": [
        {"path": "[file]", "functions": ["[class]"], "covers": {"fr": [], "uc": []}}
      ],
      "summary": "[summary]",
      "screens": []
    },
    "feature-[a]": {
      "status": "pending",
      "priority": [N],
      "phase": 3,
      "depends_on": ["project-structure", "shared-foundations"],
      "blocks": ["feature-[b]"],
      "covers": {"fr": ["FR-XXX"], "uc": ["UC-XXX"], "wf": ["WF-XXX"]},
      "files": [
        {"path": "[model.swift]", "functions": ["[Model]"], "covers": {"fr": ["FR-XXX"], "uc": ["UC-XXX"]}},
        {"path": "[service.swift]", "functions": ["[Service]"], "covers": {"fr": ["FR-XXX"]}},
        {"path": "[view.swift]", "functions": ["[View]", "[Component]"], "covers": {"fr": ["FR-XXX"], "uc": ["UC-XXX"], "wf": ["WF-XXX"]}}
      ],
      "summary": "[summary]",
      "screens": ["WF-XXX", "WF-XXX"]
    }
  }
}
```

## Dependency Graph

```mermaid
graph LR
    A[project-structure] --> B[shared-foundations]
    B --> C[feature-[a]]
    C --> D[feature-[b]]
    D --> E[...]
```

## Traceability Matrix

### FR → Spec → File Mapping

| FR ID | Description | Phase | Spec | File |
|-------|-------------|-------|------|------|
| FR-XXX | [description] | [N] | `feature-[a]` | [file] |
| FR-XXX | [description] | [N] | `feature-[a]` | [file] |
| FR-XXX | [description] | [N+1] | `feature-[b]` | [file] |

### UC → Spec → Screen Mapping

| UC ID | Description | Phase | Spec | Screen (WF) | File |
|-------|-------------|-------|------|-------------|------|
| UC-XXX | [description] | [N] | `feature-[a]` | WF-XXX ([Name]) | [file] |
| UC-XXX | [description] | [N+1] | `feature-[b]` | WF-XXX ([Name]) | [file] |

### WF → Spec → Component Mapping

| WF ID | Screen Name | Archetype | Phase | Spec | Components |
|-------|-------------|-----------|-------|------|------------|
| WF-XXX | [Name] | [archetype] | [N] | `feature-[a]` | [components] |
| WF-XXX | [Name] | [archetype] | [N] | `feature-[a]` | [components] |
| WF-XXX | [Name] | [archetype] | [N+1] | `feature-[b]` | [components] |

## GAP Analysis

| Type | ID | Description | Reason | Action |
|------|----|-------------|--------|--------|
| [type] | [ID] | [description] | [reason] | [action] |

## Next Spec Recommendation

| Phase | Spec | Status | Why Ready | Duration |
|-------|------|--------|-----------|----------|
| [N] | [spec] | [status] | [reason] | [days] |
| [N] | [spec] | [status] | [reason] | [days] |
| [N] | [spec] | [status] | [reason] | [days] |

**Recommended implementation order:**
1. [first spec]
2. [next spec]
3. [continue...]

---

**Document Version**: 1.0
**Last Updated**: 2026
**Status**: Draft / In Review / Approved
**Dependencies**: PRD.md, Use_Cases.md, Functional_Requirements.md, Wireframes.md

<!-- QUALITY-GATE-MANIFEST:START
# Nguồn chân lý DUY NHẤT cho gate-roadmap. KHÔNG chép khối này vào file đầu ra ở specs/.
# Các heading "Phase [N]: [Feature A]" trong Spec Registry/File Breakdown là VÍ DỤ, không bắt buộc cố định.
doc: Project_Implementation_Roadmap
gate: gate-roadmap
required_major:
  - "Overview"
  - "Scope Decision Record"
  - "Project Structure"
  - "Phase Timeline"
  - "Feature→Screen Mapping"
  - "Spec Registry"
  - "File Breakdown"
  - "Screen→File Breakdown"
  - "Machine-Readable Dependencies"
  - "Dependency Graph"
  - "Traceability Matrix"
  - "GAP Analysis"
  - "Next Spec Recommendation"
required_minor:
  "Project Structure": ["Directories", "Files"]
  "Phase Timeline": ["Estimation Assumptions"]
  "Traceability Matrix": ["FR → Spec → File Mapping", "UC → Spec → Screen Mapping", "WF → Spec → Component Mapping"]
quality_checks:
  - "project-structure = chỉ thư mục & file, KHÔNG chứa code"
  - "Sub-spec splitting: spec có >5 FR phải tách theo sub-feature (không tách theo layer)"
  - "Phase theo scaling contract, tối đa 3 spec/phase; mỗi phase có entry/deliverables/exit criteria"
  - "Dependencies là cạnh tường minh (spec A depends B), không có vòng lặp"
  - "Feature→Screen: mỗi spec liệt kê WF-XXX; mỗi WF-XXX map đúng 1 spec (không orphan)"
  - "Traceability: chuỗi FR/UC/WF → spec → file đầy đủ"
  - "Scope consistency: nhãn priority của mỗi UC/FR khớp giữa Use_Cases §7, Functional_Requirements §1.3 và tier trong Scope Decision Record; spec chỉ nằm trong phase MVP nếu mọi UC/FR nó phủ là Tier 1 (hoặc có ghi trong Scope Promotions)"
  - "Dependency rule: UC là recovery/critical path của một flow MVP thì phải là Tier 1 (không được Post-MVP)"
  - "Scope Decision Record có MVP definition rõ ràng (danh sách UC/FR hoặc 'all N')"
QUALITY-GATE-MANIFEST:END -->
