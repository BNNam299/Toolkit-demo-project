# subscription-management - Implementation Plan

## Execution Mode
- Mode: manual
- Policy: run sequentially by default (hybrid order from design.md)
- Gate: stop on phase boundary or blocking error

## Task Registry (Machine Readable)

| ID | Title | Type | Status | Refs AC | Refs Design | Files | Checkpoint |
|---|---|---|---|---|---|---|---|
| 2.1.1 | SubscriptionStatus + CustomerInfoSnapshot models and mapping rules | normal | pending | AC-001.1, AC-001.2, AC-001.4, AC-002.1, AC-002.2, AC-002.3, AC-002.4, AC-003.4, AC-005.1, AC-005.4 | 4 | Features/Subscription/Models/SubscriptionStatus.swift, Features/Subscription/Models/CustomerInfoSnapshot.swift | Verified entitlement maps to correct state/access; stale and invalid data cannot grant Premium |
| 2.1.2 | SubscriptionService protocol and RevenueCat subscription adapter | normal | pending | AC-001.3, AC-002.1, AC-002.4, AC-004.1, AC-004.2, AC-004.3, AC-004.4, AC-005.3 | 3 | Features/Subscription/Services/SubscriptionService.swift, Features/Subscription/Services/RevenueCatSubscriptionService.swift | purchases-ios fetch, restore, and verified CustomerInfo contract is SDK-independent |
| 2.1.3 | CustomerInfo listener and main-actor update bridge | normal | pending | AC-001.3, AC-002.1, AC-002.4 | 2 | Features/Subscription/Services/CustomerInfoListener.swift | PurchasesDelegate updates reach the ViewModel without relaunch |
| 3.1.1 | SubscriptionViewModel status, refresh, listener, and action state machine | normal | pending | AC-001.1, AC-001.2, AC-001.3, AC-001.4, AC-005.1, AC-005.3, AC-005.4 | 7.1 | Features/Subscription/ViewModels/SubscriptionViewModel.swift | Loading/free/trial/Premium/pending/expired/stale/error states and state-aware actions |
| 3.2.1 | SubscriptionStatusCard status, plan, dates, access, and action row | normal | pending | AC-001.1, AC-001.2, AC-005.1, AC-005.4 | 7.1 | Features/Subscription/Views/SubscriptionStatusCard.swift | Settings card renders state-specific copy/actions with accessibility values |
| 3.2.2 | TrialBadge and verified trial/expiry presentation | normal | pending | AC-002.1, AC-002.2, AC-002.3, AC-002.4 | 7.2 | Features/Subscription/Views/TrialBadge.swift, Features/Subscription/ViewModels/SubscriptionViewModel.swift | Seven-day badge appears only for verified trial and disappears on expiry |
| 3.3.1 | WF-018 CancelConfirmationModal and Keep subscription path | normal | pending | AC-003.1, AC-003.2 | 7.3 | Features/Subscription/Views/CancelConfirmationModal.swift, Features/Subscription/ViewModels/SubscriptionViewModel.swift | Modal shows warning/date/actions; Keep is a no-op |
| 3.3.2 | StoreKit manage-subscriptions coordinator and pending cancellation reconciliation | normal | pending | AC-003.3, AC-003.4, AC-003.5 | 7.3 | Features/Subscription/Services/StoreKitSubscriptionCoordinator.swift, Features/Subscription/ViewModels/SubscriptionViewModel.swift | `showManageSubscriptions` presents in-app; return refreshes and never fabricates cancellation |
| 3.4.1 | Restore purchases flow, progress, success, empty, and error states | normal | pending | AC-004.1, AC-004.2, AC-004.3, AC-004.4 | 7.4 | Features/Subscription/Services/RevenueCatSubscriptionService.swift, Features/Subscription/ViewModels/SubscriptionViewModel.swift | Restore is idempotent and only verified matches activate Premium |
| 3.5.1 | State-aware Manage/change, Restore, Cancel, Upgrade wiring | normal | pending | AC-005.1, AC-005.2, AC-005.3, AC-005.4 | 7.5 | Features/Subscription/Views/SubscriptionStatusCard.swift, Features/Subscription/ViewModels/SubscriptionViewModel.swift | Correct actions appear per state; manage returns to refreshed card |
| 4.1.1 | Subscription mapping, listener, restore, and idempotency property tests | pbt | pending | AC-001.3, AC-001.4, AC-002.1, AC-002.3, AC-002.4, AC-004.1, AC-004.2, AC-004.3, AC-004.4, AC-005.3 | 6 | calo-ai-testTests/SubscriptionStatusMappingTests.swift, calo-ai-testTests/CustomerInfoListenerTests.swift, calo-ai-testTests/SubscriptionServiceTests.swift | P2, P3, P4, P10, P11, P12, P13 hold for valid/stale/restore sequences |
| 4.1.2 | ViewModel, status card, badge, cancellation, and action UI tests | normal | pending | AC-001.1, AC-001.2, AC-001.3, AC-001.4, AC-002.1, AC-002.2, AC-002.3, AC-002.4, AC-003.1, AC-003.2, AC-003.4, AC-003.5, AC-005.1, AC-005.4 | 6 | calo-ai-testTests/SubscriptionViewModelTests.swift, calo-ai-testTests/SubscriptionAccessibilityTests.swift | P1, P5, P6, P7, P9, P14, P15 hold in UI/state tests |
| 4.1.3 | StoreKit cancellation/manage and restore sandbox integration tests | normal | pending | AC-003.3, AC-003.4, AC-003.5, AC-004.1, AC-004.2, AC-004.3, AC-004.4, AC-005.2 | 6 | calo-ai-testTests/SubscriptionIntegrationTests.swift, StoreKit Configuration | In-app manage UI, scheduled cancellation, restore, no-purchase, and error flows pass |
| 4.2.1 | Build and subscription integration gate | normal | pending | AC-001.1, AC-002.1, AC-003.3, AC-004.2, AC-005.2 | 6 | (build gate) | build_sim green; CustomerInfo listener, manage, restore, and status smoke pass |

## Dependency Matrix
| Task | Depends On | Can Parallel With |
|---|---|---|
| 2.1.1 | — | 2.1.2, 2.1.3 |
| 2.1.2 | — | 2.1.1, 2.1.3 |
| 2.1.3 | 2.1.2 | 2.1.1 |
| 3.1.1 | 2.1.1, 2.1.2, 2.1.3 | 3.2.1, 3.2.2 |
| 3.2.1 | 3.1.1 | 3.2.2, 3.5.1 |
| 3.2.2 | 2.1.1, 3.1.1 | 3.2.1 |
| 3.3.1 | 3.1.1 | 3.2.1, 3.4.1 |
| 3.3.2 | 2.1.2, 2.1.3, 3.3.1 | 3.4.1 |
| 3.4.1 | 2.1.2, 3.1.1 | 3.3.2, 3.5.1 |
| 3.5.1 | 3.1.1, 3.3.2, 3.4.1 | — |
| 4.1.1 | 2.1.1, 2.1.2, 2.1.3 | 4.1.2, 4.1.3 |
| 4.1.2 | 3.1.1, 3.2.1, 3.2.2, 3.3.1, 3.5.1 | 4.1.1, 4.1.3 |
| 4.1.3 | 3.3.2, 3.4.1 | 4.1.1, 4.1.2 |
| 4.2.1 | 3.5.1, 4.1.1, 4.1.2, 4.1.3 | — |

## 1. Shared Tasks
> Subscription models, RevenueCat boundary, and live CustomerInfo synchronization.

- [ ] **2.1.1** Implement `SubscriptionStatus` and `CustomerInfoSnapshot`; map verified trial/active/expired/pending/no-entitlement/stale states and scan access.
  - Refs: AC-001.1, AC-001.2, AC-001.4, AC-002.1, AC-002.2, AC-002.3, AC-002.4, AC-003.4, AC-005.1, AC-005.4
  - Design: 4
  - File: `Features/Subscription/Models/SubscriptionStatus.swift`, `Features/Subscription/Models/CustomerInfoSnapshot.swift`
- [ ] **2.1.2** Implement `SubscriptionService` protocol and `RevenueCatSubscriptionService` with configured `purchases-ios` handle, verified CustomerInfo mapping, restore, and action contracts.
  - Refs: AC-001.3, AC-002.1, AC-002.4, AC-004.1, AC-004.2, AC-004.3, AC-004.4, AC-005.3
  - Design: 3
  - File: `Features/Subscription/Services/SubscriptionService.swift`, `Features/Subscription/Services/RevenueCatSubscriptionService.swift`
- [ ] **2.1.3** Implement retained RevenueCat `PurchasesDelegate`/`CustomerInfoListener` bridge to publish app-owned snapshots on the main actor.
  - Refs: AC-001.3, AC-002.1, AC-002.4
  - Design: 2
  - File: `Features/Subscription/Services/CustomerInfoListener.swift`

**Phase Gate 2 (end of Shared phase):** Run XcodeBuildMCP `discover_projs -> list_schemes -> build_sim`, then traceability check passes for AC-001.3/.4, AC-002.1/.4, AC-004.1/.2/.3/.4, AC-005.3, and every Refs Design value resolves to design.md.

## 2. Feature Tasks
> ViewModel, status/trial UI, WF-018 cancellation, StoreKit management, restore, and action wiring.

- [ ] **3.1.1** Implement `SubscriptionViewModel` load/refresh, listener subscription, stale/error states, entitlement updates, and state-aware actions.
  - Refs: AC-001.1, AC-001.2, AC-001.3, AC-001.4, AC-005.1, AC-005.3, AC-005.4
  - Design: 7.1
  - File: `Features/Subscription/ViewModels/SubscriptionViewModel.swift`
- [ ] **3.2.1** Implement `SubscriptionStatusCard` with status, plan, localized price/cycle, renewal/trial date, scan access, state-specific actions, and VoiceOver values.
  - Refs: AC-001.1, AC-001.2, AC-005.1, AC-005.4
  - Design: 7.1
  - File: `Features/Subscription/Views/SubscriptionStatusCard.swift`
- [ ] **3.2.2** Implement verified trial/Premium mapping and `TrialBadge` with seven-day copy, end date, expiry transition, and verification error presentation.
  - Refs: AC-002.1, AC-002.2, AC-002.3, AC-002.4
  - Design: 7.2
  - File: `Features/Subscription/Views/TrialBadge.swift`, `Features/Subscription/ViewModels/SubscriptionViewModel.swift`
- [ ] **3.3.1** Implement WF-018 `CancelConfirmationModal`, warning/date copy, Keep subscription no-op, and accessibility semantics.
  - Refs: AC-003.1, AC-003.2
  - Design: 7.3
  - File: `Features/Subscription/Views/CancelConfirmationModal.swift`, `Features/Subscription/ViewModels/SubscriptionViewModel.swift`
- [ ] **3.3.2** Implement `StoreKitSubscriptionCoordinator` using `AppStore.showManageSubscriptions(in:)`, scene resolution, return refresh, pending cancellation mapping, and recoverable failure path.
  - Refs: AC-003.3, AC-003.4, AC-003.5
  - Design: 7.3
  - File: `Features/Subscription/Services/StoreKitSubscriptionCoordinator.swift`, `Features/Subscription/ViewModels/SubscriptionViewModel.swift`
- [ ] **3.4.1** Implement restore purchases progress, RevenueCat restore, verified match success, no-purchase state, Apple ID/network errors, and retry.
  - Refs: AC-004.1, AC-004.2, AC-004.3, AC-004.4
  - Design: 7.4
  - File: `Features/Subscription/Services/RevenueCatSubscriptionService.swift`, `Features/Subscription/ViewModels/SubscriptionViewModel.swift`
- [ ] **3.5.1** Wire Manage/change, Restore, Cancel, and Upgrade actions by subscription state; refresh after StoreKit return and hide cancellation without active entitlement.
  - Refs: AC-005.1, AC-005.2, AC-005.3, AC-005.4
  - Design: 7.5
  - File: `Features/Subscription/Views/SubscriptionStatusCard.swift`, `Features/Subscription/ViewModels/SubscriptionViewModel.swift`

**Phase Gate 3 (end of Feature phase):** Run XcodeBuildMCP `discover_projs -> list_schemes -> build_sim`, then traceability check passes for AC-001.*, AC-002.*, AC-003.*, AC-004.*, and AC-005.*; status card, trial badge, WF-018, manage, and restore states render without false Premium.

## 3. Integration Tasks
> Property tests, UI/accessibility tests, StoreKit sandbox flows, and final build gate.

- [ ] **4.1.1** Write model/listener/service property tests for CustomerInfo mapping, stale/invalid safety, listener delivery, restore idempotency, no-purchase, and verified activation.
  - Refs: AC-001.3, AC-001.4, AC-002.1, AC-002.3, AC-002.4, AC-004.1, AC-004.2, AC-004.3, AC-004.4, AC-005.3
  - Design: 6
  - File: `calo-ai-testTests/SubscriptionStatusMappingTests.swift`, `calo-ai-testTests/CustomerInfoListenerTests.swift`, `calo-ai-testTests/SubscriptionServiceTests.swift`
- [ ] **4.1.2** Write ViewModel/UI tests for all status states, seven-day badge, action visibility, WF-018 Keep/cancel states, pending expiration, accessibility, and no-active cancellation guard.
  - Refs: AC-001.1, AC-001.2, AC-001.3, AC-001.4, AC-002.1, AC-002.2, AC-002.3, AC-002.4, AC-003.1, AC-003.2, AC-003.4, AC-003.5, AC-005.1, AC-005.4
  - Design: 6
  - File: `calo-ai-testTests/SubscriptionViewModelTests.swift`, `calo-ai-testTests/SubscriptionAccessibilityTests.swift`
- [ ] **4.1.3** Run StoreKit sandbox integration tests for `showManageSubscriptions`, scheduled cancellation, retain-through-expiry, restore success/no-purchase/errors, and Manage refresh.
  - Refs: AC-003.3, AC-003.4, AC-003.5, AC-004.1, AC-004.2, AC-004.3, AC-004.4, AC-005.2
  - Design: 6
  - File: `calo-ai-testTests/SubscriptionIntegrationTests.swift`, StoreKit Configuration
- [ ] **4.2.1** Run build and integration gate covering paywall activation handoff, CustomerInfo listener, Settings status, StoreKit manage, restore, and state refresh.
  - Refs: AC-001.1, AC-002.1, AC-003.3, AC-004.2, AC-005.2
  - Design: 6
  - File: (build gate)

**Phase Gate 4 (end of Integration phase):** Run XcodeBuildMCP `discover_projs -> list_schemes -> build_sim` (+ `test_sim`), then traceability check passes for all 21 ACs; every AC maps to a completed task/test and every Refs Design value resolves.

## Traceability Matrix
| Task ID | AC | Design | Property | Status |
|---|---|---|---|---|
| 2.1.1 | AC-001.1, AC-001.2, AC-001.4, AC-002.1, AC-002.2, AC-002.3, AC-002.4, AC-003.4, AC-005.1, AC-005.4 | 4 | P1, P3, P4, P5, P9, P14 | pending |
| 2.1.2 | AC-001.3, AC-002.1, AC-002.4, AC-004.1, AC-004.2, AC-004.3, AC-004.4, AC-005.3 | 3 | P2, P3, P11, P12, P13 | pending |
| 2.1.3 | AC-001.3, AC-002.1, AC-002.4 | 2 | P2, P3 | pending |
| 3.1.1 | AC-001.1, AC-001.2, AC-001.3, AC-001.4, AC-005.1, AC-005.3, AC-005.4 | 7.1 | P1, P2, P3, P14 | pending |
| 3.2.1 | AC-001.1, AC-001.2, AC-005.1, AC-005.4 | 7.1 | P1, P14, P15 | pending |
| 3.2.2 | AC-002.1, AC-002.2, AC-002.3, AC-002.4 | 7.2 | P4, P5, P15 | pending |
| 3.3.1 | AC-003.1, AC-003.2 | 7.3 | P6, P7, P15 | pending |
| 3.3.2 | AC-003.3, AC-003.4, AC-003.5 | 7.3 | P8, P9, P10 | pending |
| 3.4.1 | AC-004.1, AC-004.2, AC-004.3, AC-004.4 | 7.4 | P11, P12, P13 | pending |
| 3.5.1 | AC-005.1, AC-005.2, AC-005.3, AC-005.4 | 7.5 | P8, P11, P14, P15 | pending |
| 4.1.1 | AC-001.3, AC-001.4, AC-002.1, AC-002.3, AC-002.4, AC-004.1, AC-004.2, AC-004.3, AC-004.4, AC-005.3 | 6 | P2, P3, P4, P11, P12, P13 | pending |
| 4.1.2 | AC-001.1, AC-001.2, AC-001.3, AC-001.4, AC-002.1, AC-002.2, AC-002.3, AC-002.4, AC-003.1, AC-003.2, AC-003.4, AC-003.5, AC-005.1, AC-005.4 | 6 | P1, P2, P3, P5, P6, P7, P9, P10, P14, P15 | pending |
| 4.1.3 | AC-003.3, AC-003.4, AC-003.5, AC-004.1, AC-004.2, AC-004.3, AC-004.4, AC-005.2 | 6 | P8, P9, P10, P11, P12, P13 | pending |
| 4.2.1 | AC-001.1, AC-002.1, AC-003.3, AC-004.2, AC-005.2 | 6 | P1, P2, P8, P11 | pending |

## Progress
| Section | Total | Done | Status |
|---|---:|---:|---|
| Shared | 3 | 0 | ⬜ |
| Feature | 7 | 0 | ⬜ |
| Integration | 4 | 0 | ⬜ |
