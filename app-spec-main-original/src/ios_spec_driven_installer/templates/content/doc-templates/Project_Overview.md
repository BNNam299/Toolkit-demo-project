# [Project Name] - Project Overview

## 0. PRD Reference

- **PRD Source**: `.opencode/specs/[project-name]/PRD.md`
- **Reference Policy**: Product strategy, market context, and competitor insights are defined in PRD and are not duplicated here.
- **Snapshot Used**: [PRD version/date]

## 1. Introduction

### 1.1 Problem Statement
[Describe the problem this application solves - 2-3 paragraphs]

### 1.2 Solution Overview
[High-level description of how the app solves the problem - 2-3 paragraphs]

### 1.3 Business Goals
- Goal 1: [Specific, measurable goal]
- Goal 2: [Specific, measurable goal]
- Goal 3: [Specific, measurable goal]

## 2. Target Users

### 2.1 Primary User Personas

#### Persona 1: [Name/Role]
- **Demographics**: [Age, occupation, tech-savviness]
- **Goals**: [What they want to achieve]
- **Pain Points**: [Current problems they face]
- **Usage Context**: [When/where they use the app]

#### Persona 2: [Name/Role]
- **Demographics**: [Age, occupation, tech-savviness]
- **Goals**: [What they want to achieve]
- **Pain Points**: [Current problems they face]
- **Usage Context**: [When/where they use the app]

### 2.2 Secondary Users
- [Admin, moderators, etc.]

## 3. High-Level Architecture

### 3.1 Technology Stack

#### Frontend
- **Platform**: iOS (SwiftUI)
- **Minimum Version**: iOS 15+
- **Architecture Pattern**: MVVM + Clean Architecture
- **State Management**: Combine / SwiftUI @State
- **UI Framework**: SwiftUI

#### Backend (if applicable)
- **API**: REST / GraphQL
- **Authentication**: [OAuth, JWT, etc.]
- **Database**: [Firebase, Core Data, etc.]

#### Third-Party Services
- [Analytics, Push Notifications, etc.]

### 3.2 System Architecture Diagram

```
┌─────────────────────────────────────────┐
│           iOS App (SwiftUI)             │
│  ┌─────────────────────────────────┐   │
│  │  Presentation Layer (Views)     │   │
│  └─────────────────────────────────┘   │
│  ┌─────────────────────────────────┐   │
│  │  Business Logic (ViewModels)    │   │
│  └─────────────────────────────────┘   │
│  ┌─────────────────────────────────┐   │
│  │  Data Layer (Repositories)      │   │
│  └─────────────────────────────────┘   │
└─────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│         Backend API / Services          │
└─────────────────────────────────────────┘
```

### 3.3 Key Architectural Decisions
- **Decision 1**: [Why MVVM? Why SwiftUI?]
- **Decision 2**: [Offline-first? Cloud-first?]
- **Decision 3**: [Modular architecture? Monolithic?]

## 4. Core Features Overview

### 4.1 Must-Have Features (MVP)
1. **[Feature 1]**: [Brief description]
2. **[Feature 2]**: [Brief description]
3. **[Feature 3]**: [Brief description]

### 4.2 Should-Have Features (Post-MVP)
1. **[Feature 4]**: [Brief description]
2. **[Feature 5]**: [Brief description]

### 4.3 Future Enhancements
- [Advanced features for later phases]

## 5. Development Roadmap

### Phase 1: Foundation (Weeks 1-4)
- Setup project structure
- Implement authentication
- Create core data models
- Basic UI framework

### Phase 2: Core Features (Weeks 5-8)
- Implement must-have features
- Integration with backend
- Basic testing

### Phase 3: Polish & Launch (Weeks 9-12)
- UI/UX refinement
- Performance optimization
- Beta testing
- App Store submission

### Phase 4: Post-Launch (Ongoing)
- User feedback integration
- Nice-to-have features
- Continuous improvements

## 6. Success Metrics

### 6.1 Technical Metrics
- App launch time: < 2 seconds
- Crash-free rate: > 99.5%
- API response time: < 500ms
- Test coverage: > 80%

### 6.2 Business Metrics
- User acquisition: [Target number]
- User retention: [Target percentage]
- User engagement: [Target metrics]
- App Store rating: > 4.5 stars

## 7. Constraints & Assumptions

### 7.1 Constraints
- Budget: [If applicable]
- Timeline: [Fixed deadlines]
- Resources: [Team size, skills]
- Technical: [Device support, iOS versions]

### 7.2 Assumptions
- Users have iOS 15+ devices
- Stable internet connection available
- [Other assumptions]

## 8. Risks & Mitigation

| Risk | Impact | Probability | Mitigation Strategy |
|------|--------|-------------|---------------------|
| [Risk 1] | High/Medium/Low | High/Medium/Low | [How to mitigate] |
| [Risk 2] | High/Medium/Low | High/Medium/Low | [How to mitigate] |

## 9. Stakeholders

- **Product Owner**: [Name/Role]
- **Development Team**: [Team composition]
- **Designers**: [If applicable]
- **QA**: [If applicable]

## 10. References

- [Link to PRD.md]
- [Link to PRD sections used]
- [Link to design mockups]
- [Link to technical documentation]

---

**Document Version**: 1.0
**Last Updated**: 2026
**Status**: Draft / In Review / Approved

<!-- QUALITY-GATE-MANIFEST:START
# Nguồn chân lý DUY NHẤT cho gate-overview. KHÔNG chép khối này vào file đầu ra ở specs/.
doc: Project_Overview
gate: gate-overview
required_major:
  - "0. PRD Reference"
  - "1. Introduction"
  - "2. Target Users"
  - "3. High-Level Architecture"
  - "4. Core Features Overview"
  - "5. Development Roadmap"
  - "6. Success Metrics"
  - "7. Constraints & Assumptions"
  - "8. Risks & Mitigation"
  - "9. Stakeholders"
  - "10. References"
required_minor:
  "1. Introduction": ["1.1 Problem Statement", "1.2 Solution Overview", "1.3 Business Goals"]
  "2. Target Users": ["2.1 Primary User Personas", "2.2 Secondary Users"]
  "3. High-Level Architecture": ["3.1 Technology Stack", "3.2 System Architecture Diagram", "3.3 Key Architectural Decisions"]
  "4. Core Features Overview": ["4.1 Must-Have Features (MVP)", "4.2 Should-Have Features (Post-MVP)", "4.3 Future Enhancements"]
  "6. Success Metrics": ["6.1 Technical Metrics", "6.2 Business Metrics"]
  "7. Constraints & Assumptions": ["7.1 Constraints", "7.2 Assumptions"]
quality_checks:
  - "PRD Boundary: KHÔNG chép competitor deep-dive/market sizing từ PRD; chỉ tóm tắt phục vụ kiến trúc & kế hoạch"
  - "Target Users: ít nhất 1 persona chi tiết (vai trò, nhu cầu, pain point)"
  - "Architecture: định rõ platform, stack, ranh giới component, quyết định/trade-off"
  - "Roadmap & metrics: cụ thể và đo được"
  - "Traceability: liên kết tới UC / FR / Wireframes / UX Flows"
QUALITY-GATE-MANIFEST:END -->