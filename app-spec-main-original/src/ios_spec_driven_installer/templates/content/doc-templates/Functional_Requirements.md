# [Project Name] - Functional Requirements

## 1. Introduction

### 1.1 Purpose
This document specifies WHAT the system must do, bridging user needs
(Use_Cases.md) to technical implementation (Design specs).

### 1.2 Scope
Transforms Use Cases into system requirements. Each FR traces back to
one or more UCs. MVP scope is determined by High-priority UCs.

### 1.3 Document Conventions
- **FR-XXX**: Functional Requirement
- **NFR-XXX**: Non-Functional Requirement
- **Priority**: High (MVP) / Medium (Post-MVP) / Low (Future)
- **Status**: Planned / In Progress / Completed / Deferred

---

## 2. Functional Requirements

**DYNAMIC SECTIONS:** Read `Use_Cases.md` → Create FR sections based on:
- Feature groups from UC sections (e.g., Authentication, Core Features, etc.)
- Number of UCs per feature
- MVP scope for current phase

### 2.1 [Feature Group Name - from Use_Cases.md]

**Examples (User Experience focused):**
- Onboarding & First Experience - Welcome, tutorial, first actions
- Discovery & Exploration - Browse, search, filter, navigate content
- Content Creation & Interaction - Create, edit, share, comment, react
- Progress & Achievement - Tracking, goals, milestones, rewards
- Social & Communication - Messaging, notifications, sharing, following
- Settings & Personalization - Profile, preferences, privacy, account
- Transactions & Payments - Checkout, payment methods, order history

**Examples by App Type:**
- E-commerce: Onboarding → Browse → Cart → Checkout → Order Tracking
- Fitness: Onboarding → Workout Tracking → Progress → Social → Settings
- Social: Onboarding → Profile → Feed → Posts → Messaging
- SaaS: Onboarding → Dashboard → Projects → Reports → Settings

#### [FR-XXX]: [Feature Name]
**Source UC**: [UC-XXX from Use_Cases.md]

**Priority**: High / Medium / Low
**Status**: Planned

**Description**:
[Detailed description of what the feature does]

**Input**:
- [Parameter 1]: [Type, constraints]
- [Parameter 2]: [Type, constraints]

**Processing**:
1. [Step 1]
2. [Step 2]
3. [Step 3]

**Output**:
- [Expected output]

**Business Rules**:
- [BR-XXX.1]: [Rule 1]
- [BR-XXX.2]: [Rule 2]

**Validation Rules**:
- [VR-XXX.1]: [Validation 1]
- [VR-XXX.2]: [Validation 2]

**Error Handling**:
- [ERR-XXX.1]: [Error scenario] → [Error message]
- [ERR-XXX.2]: [Error scenario] → [Error message]

**Acceptance Criteria**:
- [AC-XXX.1]: WHEN [trigger] THEN [behavior]
- [AC-XXX.2]: IF [condition] THEN [behavior]

---

### 2.N [Additional Feature Groups - as needed]

**For complex projects, add sections as needed:**
```
### 2.2 [Feature Group 2]
### 2.3 [Feature Group 3]
...
```

**Scaling guidance:**
- Small project (< 5 FRs): 1-2 sections, 3-5 FRs
- Medium project (5-10 FRs): 3-4 sections, 10-20 FRs
- Large project (10+ FRs): 5+ sections, 20+ FRs, consider grouping by module

---

### 2 bis. Component Behavior Matrix

**PURPOSE:** Same FR, different behavior per screen. This matrix documents how a requirement's behavior changes depending on which screen it appears on. Derived from Use_Cases.md §2 bis Feature Expression Matrix.

| FR ID | Component | Screen (WF) | Context | Behavior Difference |
|-------|-----------|------------|---------|--------------------|
| FR-012 | BtnPrimary "Add to Cart" | WF-005 Product Detail | Full product view | Full-width button, shows price, quantity selector visible |
| FR-012 | SwipeAction "Quick Add" | WF-004 Home Feed | Feed browsing | Swipe reveals cart icon, adds directly — no quantity, no detail |
| FR-012 | StepperControl "+/-" | WF-006 Search Grid | Search results | Inline +/- without modal, updates badge on cart icon |
| FR-012 | SwipeAction "Save Later" | WF-008 Cart | Cart management | Opposite intent — remove from cart, save to wishlist |

**Rules:**
- Every FR that maps to >1 screen MUST appear in this matrix
- Each screen expression documents WHAT changes: UI component, interaction pattern, data required, validation rules
- If behavior is identical across screens, they are not separate expressions — merge them

---

### 2 ter. Context-Dependent Behaviors

**PURPOSE:** Requirements don't behave identically in all contexts. This table documents how behavior changes based on user state, data state, and device context. Derived from Use_Cases.md UC Context Variations.

| FR ID | Context | Trigger | Behavior Change |
|-------|---------|---------|----------------|
| FR-008 Show Feed | First Visit (no data) | User is new, feed empty | Show onboarding cards + "Discover your taste" CTA instead of empty feed |
| FR-008 Show Feed | Offline | No network | Show cached feed + "Last updated 2h ago" banner + queue actions for sync |
| FR-008 Show Feed | Premium User | User has active subscription | Show advanced filters, personalized sections, no ads |
| FR-015 Process Payment | Success | Payment approved | Show confirmation animation, update order status, clear cart |
| FR-015 Process Payment | Network Error | API timeout during payment | Retain entered data, show "Payment in progress — do not close app", auto-retry 3x |
| FR-015 Process Payment | Insufficient Funds | Payment declined | Show specific decline reason, suggest alternative payment method |

**Rules:**
- Every High-priority FR must have ≥2 context-dependent behavior rows
- Contexts come from Use_Cases.md UC Context Variations (§2 per UC)
- Behavior changes must be concrete: what the user sees, what the system does, what the component renders
- "Show error message" is not a behavior change — specify WHICH error, with WHAT recovery action

---

## 3. Non-Functional Requirements

**DYNAMIC:** Generate NFRs based on:
- App type (fitness, e-commerce, SaaS, social, etc.)
- Platform requirements (iOS 15+, iPad support, etc.)
- Security needs (health data, financial data, personal data, etc.)

### 3.1 Core NFRs (Required for all projects)

#### [NFR-XXX]: Performance - App Launch Time
**Priority**: High
**Requirement**: App shall launch in less than [X] seconds on target devices.

**Measurement**:
- Time from tap icon to first interactive screen
- Measured on [target device], [iOS version]
- Cold start (app not in memory)

**Acceptance Criteria**:
- [AC-NFR-XXX.1]: WHEN user taps app icon THEN app becomes interactive within [X] seconds
- [AC-NFR-XXX.2]: WHEN measured on target devices THEN [X]% of launches meet target

---

#### [NFR-XXX]: Performance - API Response Time
**Priority**: High
**Requirement**: API calls shall complete in less than [X]ms under normal conditions.

**Acceptance Criteria**:
- [AC-NFR-XXX.1]: WHEN API is called THEN response received within [X]ms
- [AC-NFR-XXX.2]: WHEN network is slow THEN system shows loading indicator

---

#### [NFR-XXX]: Security - Data Protection
**Priority**: High
**Requirement**: All sensitive data shall be encrypted at rest and in transit.

**Implementation**:
- At rest: iOS Data Protection API
- In transit: TLS [version] minimum
- Passwords: bcrypt with cost factor [X]
- Tokens: Stored in Keychain

**Acceptance Criteria**:
- [AC-NFR-XXX.1]: WHEN data is stored THEN it is encrypted
- [AC-NFR-XXX.2]: WHEN data is transmitted THEN TLS is used
- [AC-NFR-XXX.3]: WHEN password is stored THEN it is hashed

---

### 3.2 Additional NFRs (Based on App Type)

**For [app type], consider these additional NFRs:**

#### Usability
- [NFR-XXX]: Accessibility - VoiceOver, Dynamic Type
- [NFR-XXX]: Localization (if multi-language)
- [NFR-XXX]: Offline Support (if core feature)

#### Reliability
- [NFR-XXX]: Crash-Free Rate - [X]%
- [NFR-XXX]: Data Sync Reliability

#### Scalability
- [NFR-XXX]: Concurrent Users - [X] users
- [NFR-XXX]: API Rate Limits

**Scaling guidance:**
- Small project: Core NFRs only (Performance, Security, Accessibility)
- Medium project: Add Reliability, Usability enhancements
- Large project: Add Scalability, Localization, Compliance (GDPR, HIPAA, etc.)

---

## 4. Requirements Summary

### 4.1 Functional Requirements by Priority

| ID | Requirement | Priority | Module | Status |
|----|-------------|----------|--------|--------|
| [FR-XXX] | [Requirement name] | High/Medium/Low | [Module] | Planned |

**Total**: X High, Y Medium, Z Low

### 4.2 Non-Functional Requirements by Category

| Category | Count | Priority Breakdown |
|----------|-------|-------------------|
| Performance | X | X High, Y Medium |
| Security | X | X High, Y Medium |
| Usability | X | X High, Y Medium |
| Reliability | X | X High, Y Medium |
| Scalability | X | X High, Y Medium |

---

**Document Version**: 1.0
**Last Updated**: 2026
**Status**: Draft / In Review / Approved
**Dependencies**: PRD.md, Use_Cases.md

<!-- QUALITY-GATE-MANIFEST:START
# Nguồn chân lý DUY NHẤT cho gate-fr. KHÔNG chép khối này vào file đầu ra ở specs/.
# Bỏ qua heading placeholder/ví dụ (2.N, 2.2/2.3, [FR-XXX], [NFR-XXX]).
doc: Functional_Requirements
gate: gate-fr
required_major:
  - "1. Introduction"
  - "2. Functional Requirements"
  - "2 bis. Component Behavior Matrix"
  - "2 ter. Context-Dependent Behaviors"
  - "3. Non-Functional Requirements"
  - "4. Requirements Summary"
required_minor:
  "1. Introduction": ["1.1 Purpose", "1.2 Scope", "1.3 Document Conventions"]
  "3. Non-Functional Requirements": ["3.1 Core NFRs (Required for all projects)", "3.2 Additional NFRs (Based on App Type)"]
  "4. Requirements Summary": ["4.1 Functional Requirements by Priority", "4.2 Non-Functional Requirements by Category"]
quality_checks:
  - "Functional Coverage: mọi UC được map sang ít nhất 1 FR"
  - "Component Behavior Matrix (§2 bis): FR đa màn hình có ghi khác biệt hành vi"
  - "Context-Dependent Behaviors (§2 ter): FR high-priority có >=2 dòng hành vi theo ngữ cảnh"
  - "NFR đo được (mục tiêu định lượng); phủ Performance + Security, và Usability/Reliability/Scalability khi áp dụng"
  - "Error handling: trạng thái lỗi tường minh"
  - "Secondary-action coverage: mọi hành động phụ / secondary action trong Use_Cases §4 Screen-Context (settings, share, skip, help, export, edit sub-field, manage/restore...) phải có FR hoặc bước Processing kèm AC — không chỉ bắt happy-path của flow chính. Đây là nhóm dễ bị rơi khi lên wireframe"
  - "Mỗi hành vi/màn hình người-dùng-thấy có FR RIÊNG có AC — nguyên tắc 'no behavior without acceptance criteria'. Cấm để một chức năng (vd share/export/sign-in) chỉ tồn tại như NFR hoặc gán gượng vào FR khác"
  - "Mỗi FR: ID FR-xxx, trigger/condition/result testable, AC references, priority + lý do"
  - "Không FR trùng lặp: cấm FR có thân 'Same as FR-XXX'; nếu hai UC dẫn tới cùng hành vi thì gộp hoặc phân biệt rõ, mỗi FR-ID là duy nhất về nội dung"
  - "Không hard-depend vào tham số chưa chốt: nếu FR/BR/AC/NFR phụ thuộc giá trị PRD §14, giá trị đó phải có Default (ASSUMPTION) trong PRD (không để agent tự chọn tùy tiện)"
QUALITY-GATE-MANIFEST:END -->
