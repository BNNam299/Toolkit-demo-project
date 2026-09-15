# subscription-settings - Implementation Plan

## Execution Mode
- Mode: manual
- Policy: run sequentially by default (hybrid order from design.md)
- Gate: stop on phase boundary or blocking error

## Task Registry (Machine Readable)

| ID | Title | Type | Status | Refs AC | Refs Design | Files | Checkpoint |
|---|---|---|---|---|---|---|---|
| 2.1.1 | SubscriptionSnapshot + SubscriptionAction + RestoreState + CancelState | normal | pending | AC-001.1, AC-002.1, AC-002.2 | 4 | Features/Subscription/Models/SubscriptionSnapshot.swift, Features/Subscription/ViewModels/SubscriptionSettingsViewModel.swift | Snapshot derivation + state enums |
| 2.1.2 | SubscriptionSettingsViewModel (CustomerInfo subscription, cancel, restore) | normal | pending | AC-001.1, AC-001.2, AC-001.4, AC-002.3, AC-002.4, AC-002.5, AC-002.6, AC-003.1, AC-003.2, AC-003.3, AC-003.4, AC-003.5 | 7.1, 7.2, 7.3 | Features/Subscription/ViewModels/SubscriptionSettingsViewModel.swift | Combine subscription + flow orchestration |
| 3.1.1 | SubscriptionSection view (status row + tier-appropriate buttons) | normal | pending | AC-001.1, AC-001.2, AC-001.3, AC-002.1, AC-002.2, AC-003.1, AC-003.4 | 7.1, 7.2, 7.3 | Features/Subscription/Views/SubscriptionSection.swift | Snapshot-driven rendering; onUpgrade callback |
| 3.2.1 | CancelSubscriptionModal (WF-018 destructive confirm) | normal | pending | AC-002.3, AC-002.4, AC-002.5, AC-002.6 | 7.2 | Features/Subscription/Views/CancelSubscriptionModal.swift | Keep/Continue buttons; copy per tier |
| 3.3.1 | Compose SubscriptionSection into SettingsView + wire onUpgrade to paywall router | normal | pending | AC-002.1 | 8 | Features/Settings/Views/SettingsView.swift | Subscription section embedded; stub onUpgrade until paywall-display wired |
| 4.1.1 | SubscriptionSnapshot tests (tier → snapshot mapping) | pbt | pending | AC-001.1, AC-002.1, AC-002.2 | 6 | calo-ai-testTests/SubscriptionSnapshotTests.swift | Per-tier actions + display text |
| 4.1.2 | SubscriptionSettingsViewModel tests (fakes) | pbt | pending | AC-001.2, AC-002.4, AC-002.5, AC-002.6, AC-003.2, AC-003.3, AC-003.4, AC-003.5 | 6 | calo-ai-testTests/SubscriptionSettingsViewModelTests.swift | Combine subscription + cancel/restore flows |
| 4.1.3 | CancelSubscriptionModal tests | pbt | pending | AC-002.3, AC-002.5, AC-002.6 | 6 | calo-ai-testTests/CancelSubscriptionModalTests.swift | Button labels + state-dependent copy |
| 4.2.1 | Build + integration gate (StoreKit sandbox smoke) | normal | pending | AC-001.1 | 6 | (build gate) | build_sim green; Settings tab renders Subscription section |

## Dependency Matrix
| Task | Depends On | Can Parallel With |
|---|---|---|
| 2.1.1 | — | 2.1.2 |
| 2.1.2 | 2.1.1 | — |
| 3.1.1 | 2.1.1, 2.1.2 | 3.2.1 |
| 3.2.1 | 2.1.2 | 3.1.1 |
| 3.3.1 | 3.1.1, 3.2.1 | — |
| 4.1.1 | 2.1.1 | 4.1.2, 4.1.3 |
| 4.1.2 | 2.1.2 | 4.1.1, 4.1.3 |
| 4.1.3 | 3.2.1 | 4.1.1, 4.1.2 |
| 4.2.1 | 3.3.1, 4.1.1, 4.1.2, 4.1.3 | — |

## 1. Shared Tasks
> Snapshot model + ViewModel the views depend on.

- [ ] **2.1.1** `SubscriptionSnapshot` (tier, title, subtitle, availableActions) + `SubscriptionAction` enum (`upgrade`, `manage`, `restore`, `cancel`) + `RestoreState` enum (`idle/loading/noPurchases/wrongAppleID/restored/error`) + `CancelState` enum (`idle/confirming/cancelling/cancelled/error`)
  - Refs: AC-001.1, AC-002.1, AC-002.2
  - Design: 4
  - File: `Features/Subscription/Models/SubscriptionSnapshot.swift`, `Features/Subscription/ViewModels/SubscriptionSettingsViewModel.swift`
- [ ] **2.1.2** `SubscriptionSettingsViewModel` — `@MainActor ObservableObject`; subscribes to `SubscriptionService.CustomerInfo` (Combine); `@Published snapshot: SubscriptionSnapshot?`; `@Published restoreState: RestoreState`; `@Published cancelState: CancelState`; methods `cancel()`, `confirmCancel()`, `keepSubscription()`, `restore()`, `openManagement()`; callback `onUpgrade`; routes errors to `AppEnvironment.errors`
  - Refs: AC-001.1, AC-001.2, AC-001.4, AC-002.3, AC-002.4, AC-002.5, AC-002.6, AC-003.1, AC-003.2, AC-003.3, AC-003.4, AC-003.5
  - Design: 7.1, 7.2, 7.3
  - File: `Features/Subscription/ViewModels/SubscriptionSettingsViewModel.swift`

**Phase Gate 2 (end of Shared phase):** Run XcodeBuildMCP `discover_projs -> list_schemes -> build_sim`, then traceability check (AC-001.1/.2/.4, AC-002.*, AC-003.* covered; Refs Design resolve).

## 2. Feature Tasks
> Subscription section view + cancel modal + assembly into Settings.

- [ ] **3.1.1** `SubscriptionSection` — renders `snapshot` (status row + tier-appropriate buttons); Free tier shows Upgrade only; Premium/Trial shows Manage + Restore + Cancel; presents `CancelSubscriptionModal` on Cancel; opens `itms-apps://` deep-link on Manage; invokes `onUpgrade` callback on Free Upgrade
  - Refs: AC-001.1, AC-001.2, AC-001.3, AC-002.1, AC-002.2, AC-003.1, AC-003.4
  - Design: 7.1, 7.2, 7.3
  - File: `Features/Subscription/Views/SubscriptionSection.swift`
- [ ] **3.2.1** `CancelSubscriptionModal` — WF-018 destructive confirm; copy "Cancel Premium? You'll lose unlimited scans. Access continues until [renewal_date]"; "Keep subscription" (primary `CaloButton`) + "Continue cancellation" (destructive `CaloButton`); calls `viewModel.confirmCancel()` / `viewModel.keepSubscription()`
  - Refs: AC-002.3, AC-002.4, AC-002.5, AC-002.6
  - Design: 7.2
  - File: `Features/Subscription/Views/CancelSubscriptionModal.swift`
- [ ] **3.3.1** Compose `SubscriptionSection` into `SettingsView` (owned by `settings-management`); wire `onUpgrade` callback to `AppRouter.routeToPaywall()`; the Settings screen assembles Preferences + Notifications + Privacy + About + Subscription sections in order
  - Refs: AC-002.1
  - Design: 8
  - File: `Features/Settings/Views/SettingsView.swift` (extended by integration)

**Phase Gate 3 (end of Feature phase):** Run XcodeBuildMCP `discover_projs -> list_schemes -> build_sim`, then traceability check (all 14 ACs covered by ViewModel + Views; Subscription section renders; Refs Design resolve).

## 3. Integration Tasks
> Unit tests + build/integration gate.

- [ ] **4.1.1** `SubscriptionSnapshotTests` — per-tier mapping (free/trial/premium/premiumExpiresOn → title, subtitle, availableActions)
  - Refs: AC-001.1, AC-002.1, AC-002.2
  - Design: 6
  - File: `calo-ai-testTests/SubscriptionSnapshotTests.swift`
- [ ] **4.1.2** `SubscriptionSettingsViewModelTests` (fake `SubscriptionService` with `CurrentValueSubject<CustomerInfo, Never>`) — Combine subscription flips snapshot; cancel → confirmCancel → cancelSubscription called; cancel failure keeps tier + ErrorHandler; keepSubscription does not call cancel; restore success sets restored state + Premium snapshot; restore no-purchases inline; restore wrong-apple-id inline; restore network → ErrorHandler + button stays enabled; free tier actions exclude manage/cancel
  - Refs: AC-001.2, AC-002.4, AC-002.5, AC-002.6, AC-003.2, AC-003.3, AC-003.4, AC-003.5
  - Design: 6
  - File: `calo-ai-testTests/SubscriptionSettingsViewModelTests.swift`
- [ ] **4.1.3** `CancelSubscriptionModalTests` — button labels; copy includes renewal date; cancelling state disables destructive button
  - Refs: AC-002.3, AC-002.5, AC-002.6
  - Design: 6
  - File: `calo-ai-testTests/CancelSubscriptionModalTests.swift`
- [ ] **4.2.1** Build + integration gate — `build_sim` green; Settings tab shows Subscription section; smoke in StoreKit sandbox: cancel flow → modal → confirm → snapshot flips to expires-on; restore flow → Premium state activated
  - Refs: AC-001.1
  - Design: 6
  - File: (build gate)

**Phase Gate 4 (end of Integration phase):** Run XcodeBuildMCP `discover_projs -> list_schemes -> build_sim` (+ `test_sim`), then traceability check (all 14 ACs traced to ≥1 done task; every Refs Design resolves).

## Traceability Matrix
| Task ID | AC | Design | Property | Status |
|---|---|---|---|---|
| 2.1.1 | AC-001.1, AC-002.1, AC-002.2 | 4 | P1, P3 | pending |
| 2.1.2 | AC-001.1, AC-001.2, AC-001.4, AC-002.3, AC-002.4, AC-002.5, AC-002.6, AC-003.1, AC-003.2, AC-003.3, AC-003.4, AC-003.5 | 7.1, 7.2, 7.3 | P2, P4, P5, P6, P7, P8, P9, P10 | pending |
| 3.1.1 | AC-001.1, AC-001.2, AC-001.3, AC-002.1, AC-002.2, AC-003.1, AC-003.4 | 7.1, 7.2, 7.3 | P1, P2, P3, P7, P10 | pending |
| 3.2.1 | AC-002.3, AC-002.4, AC-002.5, AC-002.6 | 7.2 | P4, P5, P6 | pending |
| 3.3.1 | AC-002.1 | 8 | P3 | pending |
| 4.1.1 | AC-001.1, AC-002.1, AC-002.2 | 6 | P1, P3 | pending |
| 4.1.2 | AC-001.2, AC-002.4, AC-002.5, AC-002.6, AC-003.2, AC-003.3, AC-003.4, AC-003.5 | 6 | P2, P4, P5, P6, P7, P8, P9, P10 | pending |
| 4.1.3 | AC-002.3, AC-002.5, AC-002.6 | 6 | P4, P5 | pending |
| 4.2.1 | AC-001.1 | 6 | P1 | pending |

## Progress
| Section | Total | Done | Status |
|---|---:|---:|---|
| Shared | 2 | 0 | ⬜ |
| Feature | 3 | 0 | ⬜ |
| Integration | 4 | 0 | ⬜ |
