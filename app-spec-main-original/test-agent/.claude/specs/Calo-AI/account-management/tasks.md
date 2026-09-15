# account-management - Implementation Plan

## Execution Mode
- Mode: manual
- Policy: run sequentially by default (hybrid order from design.md)
- Gate: stop on phase boundary or blocking error

## Task Registry (Machine Readable)

| ID | Title | Type | Status | Refs AC | Refs Design | Files | Checkpoint |
|---|---|---|---|---|---|---|---|
| 2.1.1 | UserPatch model + validation helpers | normal | pending | AC-002.2, AC-002.4, AC-003.2, AC-003.4 | 4 | Features/Account/Models/UserPatch.swift | Only non-nil fields encode; ranges delegate to User.validate() |
| 2.1.2 | UserRepository + UserRepositoryImpl (DataClient wrapper) | normal | pending | AC-001.1, AC-002.3, AC-003.3 | 7.1, 7.2, 7.3 | Features/Account/Services/UserRepository.swift | fetchCurrent/update succeed; 401 → unauth |
| 2.1.3 | AccountState enum | normal | pending | AC-001.2, AC-001.3 | 4 | Features/Account/ViewModels/AccountViewModel.swift | idle/loading(User?)/loaded/error |
| 3.1.1 | AccountViewModel (load, edit-profile flow, change-goal flow, sign-out flow) | normal | pending | AC-001.1, AC-001.2, AC-001.3, AC-001.4, AC-002.1, AC-002.2, AC-002.3, AC-002.4, AC-002.5, AC-003.1, AC-003.2, AC-003.3, AC-003.4, AC-003.5, AC-004.1, AC-004.2, AC-004.3, AC-004.4, AC-004.5 | 7.1, 7.2, 7.3, 7.4 | Features/Account/ViewModels/AccountViewModel.swift | All 4 flows; callbacks onLogout/onAuthRequired |
| 3.2.1 | ProfileCard component | normal | pending | AC-001.1 | 7.1 | Features/Account/Views/ProfileCard.swift | Renders name/height/weight/activity/goal |
| 3.2.2 | EditProfileModal | normal | pending | AC-002.1, AC-002.2, AC-002.4, AC-002.5 | 7.2 | Features/Account/Views/EditProfileModal.swift | Pre-fills + inline validation + save |
| 3.2.3 | ChangeGoalModal | normal | pending | AC-003.1, AC-003.2, AC-003.4, AC-003.5 | 7.3 | Features/Account/Views/ChangeGoalModal.swift | Goal input + formula + range validation |
| 3.2.4 | SignOutConfirmDialog (alert) | normal | pending | AC-004.1, AC-004.3 | 7.4 | Features/Account/Views/AccountView.swift | Cancel/Sign out destructive |
| 3.3.1 | AccountView assembly + replace RootView placeholder + wire onLogout/onAuthRequired | normal | pending | AC-001.1, AC-002.1, AC-003.1, AC-004.1 | 8 | Features/Account/Views/AccountView.swift, App/RootView.swift | Account tab shows AccountView; stub onLogout/onAuthRequired until settings/subscription wire in |
| 4.1.1 | UserRepository tests (DataClient fake) | pbt | pending | AC-002.3, AC-003.3 | 6 | calo-ai-testTests/UserRepositoryTests.swift | PATCH only non-nil fields; 401/500 mapped |
| 4.1.2 | UserPatch tests | pbt | pending | AC-002.2, AC-002.4, AC-003.2, AC-003.4 | 6 | calo-ai-testTests/UserPatchTests.swift | Encoding excludes nil fields |
| 4.1.3 | AccountViewModel tests (fakes) | pbt | pending | AC-001.1, AC-001.2, AC-001.3, AC-001.4, AC-002.2, AC-002.4, AC-002.5, AC-003.2, AC-003.4, AC-003.5, AC-004.2, AC-004.3, AC-004.4, AC-004.5 | 6 | calo-ai-testTests/AccountViewModelTests.swift | All 4 flows + error paths |
| 4.2.1 | Build + integration gate | normal | pending | AC-001.1 | 6 | (build gate) | build_sim green; Account tab renders |

## Dependency Matrix
| Task | Depends On | Can Parallel With |
|---|---|---|
| 2.1.1 | — | 2.1.2, 2.1.3 |
| 2.1.2 | 2.1.1 | 2.1.3 |
| 2.1.3 | — | 2.1.1, 2.1.2 |
| 3.1.1 | 2.1.1, 2.1.2, 2.1.3 | 3.2.1, 3.2.2, 3.2.3 |
| 3.2.1 | 3.1.1 | 3.2.2, 3.2.3 |
| 3.2.2 | 2.1.1, 3.1.1 | 3.2.1, 3.2.3 |
| 3.2.3 | 2.1.1, 3.1.1 | 3.2.1, 3.2.2 |
| 3.2.4 | 3.1.1 | 3.3.1 |
| 3.3.1 | 3.1.1, 3.2.1, 3.2.2, 3.2.3, 3.2.4 | — |
| 4.1.1 | 2.1.2 | 4.1.2, 4.1.3 |
| 4.1.2 | 2.1.1 | 4.1.1, 4.1.3 |
| 4.1.3 | 3.1.1 | 4.1.1, 4.1.2 |
| 4.2.1 | 3.3.1, 4.1.1, 4.1.2, 4.1.3 | — |

## 1. Shared Tasks
> Models + repository the Account ViewModel depends on.

- [ ] **2.1.1** `UserPatch` — partial-update model (`height?`, `weight?`, `activityLevel?`, `calorieTarget?`); encoding includes only non-nil fields; `validate()` mirrors `User.validate()` ranges (height 120–220, weight 30–300, calorieTarget 1000–3500, activityLevel required)
  - Refs: AC-002.2, AC-002.4, AC-003.2, AC-003.4
  - Design: 4
  - File: `Features/Account/Models/UserPatch.swift`
- [ ] **2.1.2** `UserRepository` (protocol) + `SupabaseUserRepository` (impl over `DataClient`) — `fetchCurrent()` (GET `users` filtered by `id == currentUserId`); `update(_:)` (PATCH `users` with patch fields + RLS via JWT)
  - Refs: AC-001.1, AC-002.3, AC-003.3
  - Design: 7.1, 7.2, 7.3
  - File: `Features/Account/Services/UserRepository.swift`
- [ ] **2.1.3** `AccountState` enum — `idle / loading(User?) / loaded(User) / error(AppError)`; carries last-known User on `loading`/`error` so the screen does not flash empty
  - Refs: AC-001.2, AC-001.3
  - Design: 4
  - File: `Features/Account/ViewModels/AccountViewModel.swift`

**Phase Gate 2 (end of Shared phase):** Run XcodeBuildMCP `discover_projs -> list_schemes -> build_sim`, then traceability check (AC-001.1, AC-002.2/.3, AC-003.2/.3, AC-002.4, AC-003.4 covered; Refs Design resolve).

## 2. Feature Tasks
> ViewModel + Account UI + Edit/Change modals + sign-out alert + assembly.

- [ ] **3.1.1** `AccountViewModel` — `@MainActor ObservableObject`; `loadUser()`; `saveProfile(patch:)` with validation; `saveGoal(_:)` with validation; `requestSignOut()` / `confirmSignOut()`; callbacks `onLogout`, `onAuthRequired`; routes errors to `AppEnvironment.errors`
  - Refs: AC-001.1, AC-001.2, AC-001.3, AC-001.4, AC-002.1, AC-002.2, AC-002.3, AC-002.4, AC-002.5, AC-003.1, AC-003.2, AC-003.3, AC-003.4, AC-003.5, AC-004.1, AC-004.2, AC-004.3, AC-004.4, AC-004.5
  - Design: 7.1, 7.2, 7.3, 7.4
  - File: `Features/Account/ViewModels/AccountViewModel.swift`
- [ ] **3.2.1** `ProfileCard` — renders name, height (cm), weight (kg), activity level, calorie goal from `User`; uses `CaloButton` for actions (Edit profile / Change goal / Sign out); a11y labels
  - Refs: AC-001.1
  - Design: 7.1
  - File: `Features/Account/Views/ProfileCard.swift`
- [ ] **3.2.2** `EditProfileModal` — pre-fills height/weight/activity; numeric fields with unit suffix; segmented activity picker; Save/Cancel (`CaloButton`); inline validation messages on Save; calls `viewModel.saveProfile(patch:)`
  - Refs: AC-002.1, AC-002.2, AC-002.4, AC-002.5
  - Design: 7.2
  - File: `Features/Account/Views/EditProfileModal.swift`
- [ ] **3.2.3** `ChangeGoalModal` — current goal display + Mifflin-St Jeor formula note; numeric input (`numberPad`); Update/Cancel (`CaloButton`); inline validation; calls `viewModel.saveGoal(_:)`
  - Refs: AC-003.1, AC-003.2, AC-003.4, AC-003.5
  - Design: 7.3
  - File: `Features/Account/Views/ChangeGoalModal.swift`
- [ ] **3.2.4** `SignOutConfirmDialog` — `.alert` modifier with Cancel + Sign out destructive; copy "Sign out? You'll need to sign in again with Apple."
  - Refs: AC-004.1, AC-004.3
  - Design: 7.4
  - File: `Features/Account/Views/AccountView.swift`
- [ ] **3.3.1** Assemble `AccountView` (Profile card + 3 buttons + sheet for Edit Profile + sheet for Change Goal + alert for Sign Out); replace the Profile portion placeholder in `RootView` Account tab; wire `onLogout`/`onAuthRequired` to integrator callbacks (stub during this spec; full router wiring lands when settings-management / subscription-settings integrate)
  - Refs: AC-001.1, AC-002.1, AC-003.1, AC-004.1
  - Design: 8
  - File: `Features/Account/Views/AccountView.swift`, `App/RootView.swift`

**Phase Gate 3 (end of Feature phase):** Run XcodeBuildMCP `discover_projs -> list_schemes -> build_sim`, then traceability check (all 19 ACs covered by ViewModel + Views; Refs Design resolve; Account tab renders AccountView).

## 3. Integration Tasks
> Unit tests + build/integration gate.

- [ ] **4.1.1** `UserRepositoryTests` — `fetchCurrent()` returns mapped `User`; `update()` PATCH only contains non-nil patch fields; 401 → throws `AppError.unauthenticated`; 5xx → throws `AppError.server`
  - Refs: AC-002.3, AC-003.3
  - Design: 6
  - File: `calo-ai-testTests/UserRepositoryTests.swift`
- [ ] **4.1.2** `UserPatchTests` — `UserPatch.encode(to:)` includes only non-nil fields; `validate()` accepts/rejects each range and required-activity
  - Refs: AC-002.2, AC-002.4, AC-003.2, AC-003.4
  - Design: 6
  - File: `calo-ai-testTests/UserPatchTests.swift`
- [ ] **4.1.3** `AccountViewModelTests` (fakes for `UserRepository`, `AuthService`, `OfflineSyncService`) — load success/error; sign-out confirm clears keychain+cache+onLogout; sign-out cancel; sign-out failure keeps user; edit-profile range validation blocks save; change-goal range validation blocks save; sessionValid==false fires onAuthRequired
  - Refs: AC-001.1, AC-001.2, AC-001.3, AC-001.4, AC-002.2, AC-002.4, AC-002.5, AC-003.2, AC-003.4, AC-003.5, AC-004.2, AC-004.3, AC-004.4, AC-004.5
  - Design: 6
  - File: `calo-ai-testTests/AccountViewModelTests.swift`
- [ ] **4.2.1** Build + integration gate — `build_sim` green; Account tab shows `AccountView`; smoke: view profile → edit profile → save; change goal → update; sign out → confirm → navigate
  - Refs: AC-001.1
  - Design: 6
  - File: (build gate)

**Phase Gate 4 (end of Integration phase):** Run XcodeBuildMCP `discover_projs -> list_schemes -> build_sim` (+ `test_sim`), then traceability check (all 19 ACs traced to ≥1 done task; every Refs Design resolves).

## Traceability Matrix
| Task ID | AC | Design | Property | Status |
|---|---|---|---|---|
| 2.1.1 | AC-002.2, AC-002.4, AC-003.2, AC-003.4 | 4 | P4, P5, P8 | pending |
| 2.1.2 | AC-001.1, AC-002.3, AC-003.3 | 7.1, 7.2, 7.3 | P1, P4, P7 | pending |
| 2.1.3 | AC-001.2, AC-001.3 | 4 | P1, P2 | pending |
| 3.1.1 | AC-001.1, AC-001.2, AC-001.3, AC-001.4, AC-002.1, AC-002.2, AC-002.3, AC-002.4, AC-002.5, AC-003.1, AC-003.2, AC-003.3, AC-003.4, AC-003.5, AC-004.1, AC-004.2, AC-004.3, AC-004.4, AC-004.5 | 7.1, 7.2, 7.3, 7.4 | P1, P2, P3, P4, P5, P6, P7, P8, P9, P10, P11, P12, P13 | pending |
| 3.2.1 | AC-001.1 | 7.1 | P1 | pending |
| 3.2.2 | AC-002.1, AC-002.2, AC-002.4, AC-002.5 | 7.2 | P4, P5, P6 | pending |
| 3.2.3 | AC-003.1, AC-003.2, AC-003.4, AC-003.5 | 7.3 | P7, P8, P9 | pending |
| 3.2.4 | AC-004.1, AC-004.3 | 7.4 | P10, P11 | pending |
| 3.3.1 | AC-001.1, AC-002.1, AC-003.1, AC-004.1 | 8 | P1, P10 | pending |
| 4.1.1 | AC-002.3, AC-003.3 | 6 | P4, P7 | pending |
| 4.1.2 | AC-002.2, AC-002.4, AC-003.2, AC-003.4 | 6 | P4, P5, P8 | pending |
| 4.1.3 | AC-001.1, AC-001.2, AC-001.3, AC-001.4, AC-002.2, AC-002.4, AC-002.5, AC-003.2, AC-003.4, AC-003.5, AC-004.2, AC-004.3, AC-004.4, AC-004.5 | 6 | P1, P2, P3, P5, P6, P8, P9, P10, P11, P12, P13 | pending |
| 4.2.1 | AC-001.1 | 6 | P1 | pending |

## Progress
| Section | Total | Done | Status |
|---|---:|---:|---|
| Shared | 3 | 0 | ⬜ |
| Feature | 6 | 0 | ⬜ |
| Integration | 4 | 0 | ⬜ |
