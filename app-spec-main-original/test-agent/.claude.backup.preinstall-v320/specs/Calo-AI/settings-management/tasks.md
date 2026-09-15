# settings-management - Implementation Plan

## Execution Mode
- Mode: manual
- Policy: run sequentially by default (hybrid order from design.md)
- Gate: stop on phase boundary or blocking error

## Task Registry (Machine Readable)

| ID | Title | Type | Status | Refs AC | Refs Design | Files | Checkpoint |
|---|---|---|---|---|---|---|---|
| 2.1.1 | UnitSystem + AppTheme + PreferencesSnapshot models | normal | pending | AC-001.1 | 4 | Features/Settings/Models/UnitSystem.swift, Features/Settings/Models/AppTheme.swift, Features/Settings/Models/PreferencesSnapshot.swift | Codable enums + snapshot struct |
| 2.1.2 | PreferencesStore (UserDefaults wrapper, @Published) | normal | pending | AC-001.1, AC-001.2, AC-001.3, AC-001.4 | 7.1 | Features/Settings/Services/PreferencesStore.swift | Reactive reads/writes; persists across launches; clear() method |
| 2.1.3 | NotificationsServicing + NotificationsService (UNUserNotificationCenter wrapper) | normal | pending | AC-002.1, AC-002.2, AC-002.3, AC-002.4 | 7.2 | Features/Settings/Services/NotificationsService.swift | currentStatus / requestAuthorization / setEnabled |
| 3.1.1 | SettingsViewModel (prefs binding, notifications toggle, export, delete) | normal | pending | AC-001.2, AC-002.2, AC-002.3, AC-003.1, AC-003.2, AC-003.3, AC-003.4, AC-003.5 | 7.1, 7.2, 7.3, 7.4 | Features/Settings/ViewModels/SettingsViewModel.swift | All flows; callbacks onSignedOut, onNavigateToAccount, onNavigateToSubscription |
| 3.2.1 | PreferencesSection (Units + Theme segmented rows) | normal | pending | AC-001.1, AC-001.2, AC-001.3 | 7.1 | Features/Settings/Views/PreferencesSection.swift | Two rows bound to PreferencesStore |
| 3.2.2 | NotificationsSection (toggle + hint + Settings deep-link) | normal | pending | AC-002.1, AC-002.2, AC-002.3, AC-002.4 | 7.2 | Features/Settings/Views/NotificationsSection.swift | Toggle + denial hint |
| 3.2.3 | PrivacySection (Export + Delete buttons) | normal | pending | AC-003.1, AC-003.4 | 7.3 | Features/Settings/Views/PrivacySection.swift | Two buttons, present share sheet / confirm modal |
| 3.2.4 | AboutSection (version + privacy + terms) | normal | pending | AC-004.1, AC-004.2, AC-004.3 | 7.4 | Features/Settings/Views/AboutSection.swift | Read-only version + URL rows |
| 3.2.5 | DeleteDataConfirmModal (typed "DELETE" guardrail) | normal | pending | AC-003.2, AC-003.3 | 7.3 | Features/Settings/Views/DeleteDataConfirmModal.swift | Destructive button enabled only when input=="DELETE" |
| 3.3.1 | SettingsView assembly + replace RootView placeholder + NavigationStack links | normal | pending | AC-001.1, AC-004.4 | 8 | Features/Settings/Views/SettingsView.swift, App/RootView.swift | Settings tab shows SettingsView; pushes to Account/Subscription |
| 4.1.1 | PreferencesStore tests | pbt | pending | AC-001.1, AC-001.2, AC-001.3 | 6 | calo-ai-testTests/PreferencesStoreTests.swift | Round-trip + reactive + clear() |
| 4.1.2 | NotificationsService tests | pbt | pending | AC-002.2, AC-002.3, AC-002.4 | 6 | calo-ai-testTests/NotificationsServiceTests.swift | Granted/denied; schedule/cancel; no auto-retry |
| 4.1.3 | DeleteDataConfirmModal tests (typed-keyword guardrail) | pbt | pending | AC-003.2, AC-003.3 | 6 | calo-ai-testTests/DeleteDataConfirmModalTests.swift | Destructive enabled iff input=="DELETE" |
| 4.1.4 | SettingsViewModel tests (fakes) | pbt | pending | AC-001.2, AC-002.2, AC-002.3, AC-003.1, AC-003.2, AC-003.3, AC-003.4, AC-003.5 | 6 | calo-ai-testTests/SettingsViewModelTests.swift | All flows; error paths |
| 4.2.1 | Build + integration gate | normal | pending | AC-001.1 | 6 | (build gate) | build_sim green; Settings tab renders SettingsView |

## Dependency Matrix
| Task | Depends On | Can Parallel With |
|---|---|---|
| 2.1.1 | — | 2.1.2, 2.1.3 |
| 2.1.2 | 2.1.1 | 2.1.3 |
| 2.1.3 | — | 2.1.1, 2.1.2 |
| 3.1.1 | 2.1.1, 2.1.2, 2.1.3 | 3.2.1, 3.2.2, 3.2.3, 3.2.4, 3.2.5 |
| 3.2.1 | 2.1.1, 2.1.2, 3.1.1 | 3.2.2, 3.2.3, 3.2.4, 3.2.5 |
| 3.2.2 | 2.1.3, 3.1.1 | 3.2.1, 3.2.3, 3.2.4, 3.2.5 |
| 3.2.3 | 3.1.1 | 3.2.1, 3.2.2, 3.2.4, 3.2.5 |
| 3.2.4 | 3.1.1 | 3.2.1, 3.2.2, 3.2.3, 3.2.5 |
| 3.2.5 | 3.1.1 | 3.2.1, 3.2.2, 3.2.3, 3.2.4 |
| 3.3.1 | 3.1.1, 3.2.1, 3.2.2, 3.2.3, 3.2.4, 3.2.5 | — |
| 4.1.1 | 2.1.2 | 4.1.2, 4.1.3, 4.1.4 |
| 4.1.2 | 2.1.3 | 4.1.1, 4.1.3, 4.1.4 |
| 4.1.3 | 3.2.5 | 4.1.1, 4.1.2, 4.1.4 |
| 4.1.4 | 3.1.1 | 4.1.1, 4.1.2, 4.1.3 |
| 4.2.1 | 3.3.1, 4.1.1, 4.1.2, 4.1.3, 4.1.4 | — |

## 1. Shared Tasks
> Models + services the Settings ViewModel depends on.

- [ ] **2.1.1** `UnitSystem` (metric/imperial), `AppTheme` (system/light/dark), `PreferencesSnapshot` (units/theme/notificationsEnabled)
  - Refs: AC-001.1
  - Design: 4
  - File: `Features/Settings/Models/UnitSystem.swift`, `Features/Settings/Models/AppTheme.swift`, `Features/Settings/Models/PreferencesSnapshot.swift`
- [ ] **2.1.2** `PreferencesStore` — UserDefaults-backed key/value store; `@Published var units`, `theme`, `notificationsEnabled`; `set(_:forKey:)`; `clear()` (used by Delete flow); instance owned by `AppEnvironment`
  - Refs: AC-001.1, AC-001.2, AC-001.3, AC-001.4
  - Design: 7.1
  - File: `Features/Settings/Services/PreferencesStore.swift`
- [ ] **2.1.3** `NotificationsServicing` + `NotificationsService` (UNUserNotificationCenter wrapper) — `currentStatus()`, `requestAuthorization()`, `setEnabled(_:)` schedules daily 8pm reminder / cancels all pending
  - Refs: AC-002.1, AC-002.2, AC-002.3, AC-002.4
  - Design: 7.2
  - File: `Features/Settings/Services/NotificationsService.swift`

**Phase Gate 2 (end of Shared phase):** Run XcodeBuildMCP `discover_projs -> list_schemes -> build_sim`, then traceability check (AC-001.1/.2/.3/.4, AC-002.1/.2/.3/.4 covered; Refs Design resolve).

## 2. Feature Tasks
> ViewModel + Settings UI sections + delete modal + assembly.

- [ ] **3.1.1** `SettingsViewModel` — `@MainActor ObservableObject`; binds `PreferencesStore.@Published` to `prefs`; `setUnits(_:)`, `setTheme(_:)`, `toggleNotifications(_:)`, `exportData()` (returns URL or throws), `requestDelete()`, `confirmDelete()` (typed-keyword + flow); callbacks `onSignedOut`, `onNavigateToAccount`, `onNavigateToSubscription`; routes errors to `AppEnvironment.errors`
  - Refs: AC-001.2, AC-002.2, AC-002.3, AC-003.1, AC-003.2, AC-003.3, AC-003.4, AC-003.5
  - Design: 7.1, 7.2, 7.3, 7.4
  - File: `Features/Settings/ViewModels/SettingsViewModel.swift`
- [ ] **3.2.1** `PreferencesSection` — two rows: Units (segmented metric/imperial) + Theme (segmented system/light/dark); both bound to `viewModel.prefs`; a11y labels
  - Refs: AC-001.1, AC-001.2, AC-001.3
  - Design: 7.1
  - File: `Features/Settings/Views/PreferencesSection.swift`
- [ ] **3.2.2** `NotificationsSection` — toggle (default OFF) bound to `viewModel.prefs.notificationsEnabled`; caption "Daily meal-log reminder"; on denial, shows hint + Settings deep-link
  - Refs: AC-002.1, AC-002.2, AC-002.3, AC-002.4
  - Design: 7.2
  - File: `Features/Settings/Views/NotificationsSection.swift`
- [ ] **3.2.3** `PrivacySection` — two `CaloButton`s: "Export my data" (primary) and "Delete my data" (destructive); presents share sheet / delete confirm modal
  - Refs: AC-003.1, AC-003.4
  - Design: 7.3
  - File: `Features/Settings/Views/PrivacySection.swift`
- [ ] **3.2.4** `AboutSection` — read-only version (`CFBundleShortVersionString` + `CFBundleVersion`); tap "Privacy policy" → SFSafariViewController; tap "Terms of service" → SFSafariViewController
  - Refs: AC-004.1, AC-004.2, AC-004.3
  - Design: 7.4
  - File: `Features/Settings/Views/AboutSection.swift`
- [ ] **3.2.5** `DeleteDataConfirmModal` — sheet with copy + text field; destructive `CaloButton` enabled iff input == "DELETE" (case-sensitive); calls `viewModel.confirmDelete()` on tap
  - Refs: AC-003.2, AC-003.3
  - Design: 7.3
  - File: `Features/Settings/Views/DeleteDataConfirmModal.swift`
- [ ] **3.3.1** Assemble `SettingsView` (Preferences + Notifications + Privacy + About + NavigationStack links to Account profile and Subscription); replace Settings placeholder in `RootView`; wire `onSignedOut`, `onNavigateToAccount`, `onNavigateToSubscription`
  - Refs: AC-001.1, AC-004.4
  - Design: 8
  - File: `Features/Settings/Views/SettingsView.swift`, `App/RootView.swift`

**Phase Gate 3 (end of Feature phase):** Run XcodeBuildMCP `discover_projs -> list_schemes -> build_sim`, then traceability check (all 17 ACs covered by ViewModel + section views; Settings tab renders SettingsView; Refs Design resolve).

## 3. Integration Tasks
> Unit tests + build/integration gate.

- [ ] **4.1.1** `PreferencesStoreTests` — read/write round-trip per key; `@Published` fires on set; persists across instances; `clear()` wipes all keys
  - Refs: AC-001.1, AC-001.2, AC-001.3
  - Design: 6
  - File: `calo-ai-testTests/PreferencesStoreTests.swift`
- [ ] **4.1.2** `NotificationsServiceTests` (fake `UNUserNotificationCenter`) — `setEnabled(true)` schedules daily reminder when authorized; `setEnabled(false)` cancels; denied status does not retry request
  - Refs: AC-002.2, AC-002.3, AC-002.4
  - Design: 6
  - File: `calo-ai-testTests/NotificationsServiceTests.swift`
- [ ] **4.1.3** `DeleteDataConfirmModalTests` — destructive button enabled iff input == "DELETE" (case-sensitive); other inputs (empty, "delete", "DELETE ") keep disabled
  - Refs: AC-003.2, AC-003.3
  - Design: 6
  - File: `calo-ai-testTests/DeleteDataConfirmModalTests.swift`
- [ ] **4.1.4** `SettingsViewModelTests` (fakes for `PreferencesStore`, `NotificationsService`, `DataClient`, `AuthService`, `OfflineSyncService`) — units/theme writes flip `@Published`; toggle ON grants → persists true; toggle ON denied → keeps false; delete confirm requires typed keyword before enabling; delete confirm calls DataClient + clear prefs + clear sync + logout + onSignedOut; export success returns URL; export/delete failure surfaces ErrorHandler and does not mark complete
  - Refs: AC-001.2, AC-002.2, AC-002.3, AC-003.1, AC-003.2, AC-003.3, AC-003.4, AC-003.5
  - Design: 6
  - File: `calo-ai-testTests/SettingsViewModelTests.swift`
- [ ] **4.2.1** Build + integration gate — `build_sim` green; Settings tab shows `SettingsView`; smoke: change units/theme → persisted across relaunch; export → share sheet; delete (with "DELETE" typed) → sign out; notification toggle ON → authorization prompt
  - Refs: AC-001.1
  - Design: 6
  - File: (build gate)

**Phase Gate 4 (end of Integration phase):** Run XcodeBuildMCP `discover_projs -> list_schemes -> build_sim` (+ `test_sim`), then traceability check (all 17 ACs traced to ≥1 done task; every Refs Design resolves).

## Traceability Matrix
| Task ID | AC | Design | Property | Status |
|---|---|---|---|---|
| 2.1.1 | AC-001.1 | 4 | P1 | pending |
| 2.1.2 | AC-001.1, AC-001.2, AC-001.3, AC-001.4 | 7.1 | P1, P2 | pending |
| 2.1.3 | AC-002.1, AC-002.2, AC-002.3, AC-002.4 | 7.2 | P3, P4 | pending |
| 3.1.1 | AC-001.2, AC-002.2, AC-002.3, AC-003.1, AC-003.2, AC-003.3, AC-003.4, AC-003.5 | 7.1, 7.2, 7.3, 7.4 | P2, P3, P4, P5, P6, P7, P8 | pending |
| 3.2.1 | AC-001.1, AC-001.2, AC-001.3 | 7.1 | P1, P2 | pending |
| 3.2.2 | AC-002.1, AC-002.2, AC-002.3, AC-002.4 | 7.2 | P3, P4 | pending |
| 3.2.3 | AC-003.1, AC-003.4 | 7.3 | P7, P8 | pending |
| 3.2.4 | AC-004.1, AC-004.2, AC-004.3 | 7.4 | P9 | pending |
| 3.2.5 | AC-003.2, AC-003.3 | 7.3 | P5, P6 | pending |
| 3.3.1 | AC-001.1, AC-004.4 | 8 | P1, P10 | pending |
| 4.1.1 | AC-001.1, AC-001.2, AC-001.3 | 6 | P1, P2 | pending |
| 4.1.2 | AC-002.2, AC-002.3, AC-002.4 | 6 | P3, P4 | pending |
| 4.1.3 | AC-003.2, AC-003.3 | 6 | P5 | pending |
| 4.1.4 | AC-001.2, AC-002.2, AC-002.3, AC-003.1, AC-003.2, AC-003.3, AC-003.4, AC-003.5 | 6 | P2, P3, P4, P5, P6, P7, P8 | pending |
| 4.2.1 | AC-001.1 | 6 | P1 | pending |

## Progress
| Section | Total | Done | Status |
|---|---:|---:|---|
| Shared | 3 | 0 | ⬜ |
| Feature | 7 | 0 | ⬜ |
| Integration | 5 | 0 | ⬜ |
