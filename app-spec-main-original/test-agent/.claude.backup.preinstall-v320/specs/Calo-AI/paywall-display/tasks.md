# paywall-display - Implementation Plan

## Execution Mode
- Mode: manual
- Policy: run sequentially by default (hybrid order from design.md)
- Gate: stop on phase boundary or blocking error

## Task Registry (Machine Readable)

| ID | Title | Type | Status | Refs AC | Refs Design | Files | Checkpoint |
|---|---|---|---|---|---|---|---|
| 2.1.1 | SubscriptionPlan + PaywallPresentation models and offer validation | normal | pending | AC-001.2, AC-001.3, AC-002.2, AC-002.4, AC-004.1, AC-004.4 | 4 | Features/Paywall/Models/SubscriptionPlan.swift, Features/Paywall/Models/PaywallPresentation.swift | Only valid product, price, cycle, trial, renewal, and cancellation terms are selectable |
| 2.1.2 | SubscriptionService protocol and RevenueCat offerings/purchase adapter | normal | pending | AC-001.4, AC-003.1, AC-003.2, AC-003.3, AC-003.4 | 3 | Features/Paywall/Services/SubscriptionService.swift, Features/Paywall/Services/RevenueCatService.swift | purchases-ios maps offerings and verified purchase outcomes without SDK leakage |
| 3.1.1 | PaywallViewModel loading, source state, selection, and purchase preconditions | normal | pending | AC-001.1, AC-001.4, AC-002.1, AC-002.3, AC-002.4, AC-003.1, AC-003.3, AC-003.4, AC-004.4 | 7.1 | Features/Paywall/ViewModels/PaywallViewModel.swift | Loading/error/content/purchasing/activated states and one valid selection |
| 3.2.1 | PaywallView WF-006 layout, benefits, trial badge, and terms | normal | pending | AC-001.2, AC-001.3, AC-004.1, AC-004.2, AC-004.3, AC-004.4 | 7.1 | Features/Paywall/Views/PaywallView.swift, Features/Paywall/Views/TrialBadge.swift, Features/Paywall/Views/BenefitsList.swift, Features/Paywall/Views/PaywallTermsView.swift | Price/cycle/trial/renewal/cancel terms visible before CTA; dismissal remains available |
| 3.2.2 | PricingCard plan selection and accessibility semantics | normal | pending | AC-002.1, AC-002.2, AC-002.3, AC-002.4 | 7.2 | Features/Paywall/Views/PricingCard.swift | Exactly one valid plan selected; unavailable cards cannot purchase |
| 3.3.1 | Trial CTA, RevenueCat purchase state, and verified activation | normal | pending | AC-003.1, AC-003.2, AC-003.3, AC-003.4 | 7.3 | Features/Paywall/ViewModels/PaywallViewModel.swift, Features/Paywall/Views/PaywallView.swift | Explicit CTA opens StoreKit; only verified entitlement dismisses as Premium |
| 3.4.1 | Camera/Settings presentation wiring and transparent dismissal | normal | pending | AC-001.1, AC-004.2, AC-004.3 | 8 | Features/Paywall/Views/PaywallView.swift, App/RootView.swift, Features/Camera/Views/CameraView.swift | Both entry sources present/dismiss without quota or entitlement mutation |
| 4.1.1 | Offer and pricing validation property tests | pbt | pending | AC-001.2, AC-001.3, AC-001.4, AC-002.2, AC-002.4, AC-004.1, AC-004.4 | 6 | calo-ai-testTests/PaywallOfferTests.swift | P2, P3, P5, P10 hold for valid/malformed catalogs |
| 4.1.2 | PaywallViewModel and purchase outcome tests | pbt | pending | AC-001.1, AC-001.4, AC-002.1, AC-002.3, AC-003.1, AC-003.2, AC-003.3, AC-003.4, AC-004.3 | 6 | calo-ai-testTests/PaywallViewModelTests.swift, calo-ai-testTests/RevenueCatServiceTests.swift | P1, P4, P6, P7, P9 hold with fake service outcomes |
| 4.1.3 | Paywall accessibility and compliance tests | normal | pending | AC-001.2, AC-001.3, AC-004.1, AC-004.2, AC-004.3, AC-004.4 | 6 | calo-ai-testTests/PaywallAccessibilityTests.swift | VoiceOver, Dynamic Type, 44pt controls, visible terms, and dismissal pass |
| 4.2.1 | Build, StoreKit sandbox, and integration gate | normal | pending | AC-001.1, AC-003.2, AC-004.2 | 6 | (build gate), StoreKit Configuration | build_sim green; camera/settings entry and verified activation smoke pass |

## Dependency Matrix
| Task | Depends On | Can Parallel With |
|---|---|---|
| 2.1.1 | — | 2.1.2 |
| 2.1.2 | — | 2.1.1 |
| 3.1.1 | 2.1.1, 2.1.2 | 3.2.1, 3.2.2 |
| 3.2.1 | 2.1.1, 3.1.1 | 3.2.2 |
| 3.2.2 | 2.1.1, 3.1.1 | 3.2.1 |
| 3.3.1 | 2.1.2, 3.1.1, 3.2.2 | 3.4.1 |
| 3.4.1 | 3.1.1, 3.2.1, 3.3.1 | — |
| 4.1.1 | 2.1.1 | 4.1.2, 4.1.3 |
| 4.1.2 | 3.1.1, 3.3.1 | 4.1.1, 4.1.3 |
| 4.1.3 | 3.2.1, 3.2.2 | 4.1.1, 4.1.2 |
| 4.2.1 | 3.4.1, 4.1.1, 4.1.2, 4.1.3 | — |

## 1. Shared Tasks
> Models and service contracts required by the paywall ViewModel.

- [ ] **2.1.1** Implement `SubscriptionPlan` and `PaywallPresentation` models; validate product ID, localized price, billing cycle, 7-day trial, renewal disclosure, cancellation path, and availability.
  - Refs: AC-001.2, AC-001.3, AC-002.2, AC-002.4, AC-004.1, AC-004.4
  - Design: 4
  - File: `Features/Paywall/Models/SubscriptionPlan.swift`, `Features/Paywall/Models/PaywallPresentation.swift`
- [ ] **2.1.2** Implement `SubscriptionService` protocol and `RevenueCatService` using the configured `purchases-ios` handle; map Offerings/Package and verified/cancelled/failed purchase results.
  - Refs: AC-001.4, AC-003.1, AC-003.2, AC-003.3, AC-003.4
  - Design: 3
  - File: `Features/Paywall/Services/SubscriptionService.swift`, `Features/Paywall/Services/RevenueCatService.swift`

**Phase Gate 2 (end of Shared phase):** Run XcodeBuildMCP `discover_projs -> list_schemes -> build_sim`, then traceability check passes for AC-001.2/.3/.4, AC-002.2/.4, AC-003.1/.2/.3/.4, and AC-004.1/.4; every Refs Design value resolves to design.md.

## 2. Feature Tasks
> ViewModel, WF-006 UI, plan selection, trial CTA, and entry wiring.

- [ ] **3.1.1** Implement `PaywallViewModel` loading, source-aware presentation, valid-plan selection, CTA preconditions, retry, dismiss, and ErrorHandler mapping.
  - Refs: AC-001.1, AC-001.4, AC-002.1, AC-002.3, AC-002.4, AC-003.1, AC-003.3, AC-003.4, AC-004.4
  - Design: 7.1
  - File: `Features/Paywall/ViewModels/PaywallViewModel.swift`
- [ ] **3.2.1** Implement WF-006 `PaywallView`, `TrialBadge`, `BenefitsList`, and explicit transparent terms using `CaloButton` and shared tokens.
  - Refs: AC-001.2, AC-001.3, AC-004.1, AC-004.2, AC-004.3, AC-004.4
  - Design: 7.1
  - File: `Features/Paywall/Views/PaywallView.swift`, `Features/Paywall/Views/TrialBadge.swift`, `Features/Paywall/Views/BenefitsList.swift`, `Features/Paywall/Views/PaywallTermsView.swift`
- [ ] **3.2.2** Implement `PricingCard` with weekly/monthly/annual selection, localized price/cycle, annual savings label, unavailable state, and VoiceOver value.
  - Refs: AC-002.1, AC-002.2, AC-002.3, AC-002.4
  - Design: 7.2
  - File: `Features/Paywall/Views/PricingCard.swift`
- [ ] **3.3.1** Implement Start 7-day trial purchase state, StoreKit handoff through `SubscriptionService`, verified activation, cancellation return, retry, and no-duplicate guard.
  - Refs: AC-003.1, AC-003.2, AC-003.3, AC-003.4
  - Design: 7.3
  - File: `Features/Paywall/ViewModels/PaywallViewModel.swift`, `Features/Paywall/Views/PaywallView.swift`
- [ ] **3.4.1** Wire camera scan-limit and Settings Upgrade presentations, analytics, close/back/Remind me later dismissal, and origin callbacks without quota mutation.
  - Refs: AC-001.1, AC-004.2, AC-004.3
  - Design: 8
  - File: `Features/Paywall/Views/PaywallView.swift`, `App/RootView.swift`, `Features/Camera/Views/CameraView.swift`

**Phase Gate 3 (end of Feature phase):** Run XcodeBuildMCP `discover_projs -> list_schemes -> build_sim`, then traceability check passes for AC-001.*, AC-002.*, AC-003.*, and AC-004.*; WF-006 renders with visible terms and both entry sources dismiss safely.

## 3. Integration Tasks
> Property tests, accessibility/compliance tests, StoreKit sandbox, and build gate.

- [ ] **4.1.1** Write offer/pricing property tests for valid/malformed catalogs, disclosure gating, and failure fallback.
  - Refs: AC-001.2, AC-001.3, AC-001.4, AC-002.2, AC-002.4, AC-004.1, AC-004.4
  - Design: 6
  - File: `calo-ai-testTests/PaywallOfferTests.swift`
- [ ] **4.1.2** Write ViewModel/service tests with fakes for source entry, exclusive selection, purchase/cancel/verification outcomes, activation, retry, and dismissal.
  - Refs: AC-001.1, AC-001.4, AC-002.1, AC-002.3, AC-003.1, AC-003.2, AC-003.3, AC-003.4, AC-004.3
  - Design: 6
  - File: `calo-ai-testTests/PaywallViewModelTests.swift`, `calo-ai-testTests/RevenueCatServiceTests.swift`
- [ ] **4.1.3** Write accessibility and compliance tests for price/cycle visibility, trial/renewal/cancel copy, no dark-pattern dismissal, Dynamic Type, VoiceOver, contrast, and hit areas.
  - Refs: AC-001.2, AC-001.3, AC-004.1, AC-004.2, AC-004.3, AC-004.4
  - Design: 6
  - File: `calo-ai-testTests/PaywallAccessibilityTests.swift`
- [ ] **4.2.1** Run StoreKit sandbox flow and integration gate: camera-limit entry, Settings entry, plan selection, cancelled payment, verified activation, and close/remind-later paths.
  - Refs: AC-001.1, AC-003.2, AC-004.2
  - Design: 6
  - File: (build gate), StoreKit Configuration

**Phase Gate 4 (end of Integration phase):** Run XcodeBuildMCP `discover_projs -> list_schemes -> build_sim` (+ `test_sim`), then traceability check passes for all 16 ACs; every AC maps to a completed test/task and every Refs Design value resolves.

## Traceability Matrix
| Task ID | AC | Design | Property | Status |
|---|---|---|---|---|
| 2.1.1 | AC-001.2, AC-001.3, AC-002.2, AC-002.4, AC-004.1, AC-004.4 | 4 | P2, P5, P10 | pending |
| 2.1.2 | AC-001.4, AC-003.1, AC-003.2, AC-003.3, AC-003.4 | 3 | P3, P6, P7, P9 | pending |
| 3.1.1 | AC-001.1, AC-001.4, AC-002.1, AC-002.3, AC-002.4, AC-003.1, AC-003.3, AC-003.4, AC-004.4 | 7.1 | P1, P3, P4, P5, P6, P7, P9, P10 | pending |
| 3.2.1 | AC-001.2, AC-001.3, AC-004.1, AC-004.2, AC-004.3, AC-004.4 | 7.1 | P2, P7, P8, P10 | pending |
| 3.2.2 | AC-002.1, AC-002.2, AC-002.3, AC-002.4 | 7.2 | P4, P5 | pending |
| 3.3.1 | AC-003.1, AC-003.2, AC-003.3, AC-003.4 | 7.3 | P6, P7, P9 | pending |
| 3.4.1 | AC-001.1, AC-004.2, AC-004.3 | 8 | P1, P7, P8 | pending |
| 4.1.1 | AC-001.2, AC-001.3, AC-001.4, AC-002.2, AC-002.4, AC-004.1, AC-004.4 | 6 | P2, P3, P5, P10 | pending |
| 4.1.2 | AC-001.1, AC-001.4, AC-002.1, AC-002.3, AC-003.1, AC-003.2, AC-003.3, AC-003.4, AC-004.3 | 6 | P1, P3, P4, P6, P7, P9 | pending |
| 4.1.3 | AC-001.2, AC-001.3, AC-004.1, AC-004.2, AC-004.3, AC-004.4 | 6 | P2, P7, P8, P10 | pending |
| 4.2.1 | AC-001.1, AC-003.2, AC-004.2 | 6 | P1, P6, P8 | pending |

## Progress
| Section | Total | Done | Status |
|---|---:|---:|---|
| Shared | 2 | 0 | ⬜ |
| Feature | 5 | 0 | ⬜ |
| Integration | 4 | 0 | ⬜ |
