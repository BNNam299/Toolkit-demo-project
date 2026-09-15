# authentication - Implementation Plan

## Execution Mode
- Mode: manual
- Policy: run sequentially by default (UI-first order from design.md)
- Gate: stop on phase boundary or blocking error

## Task Registry (Machine Readable)

| ID | Title | Type | Status | Refs AC | Refs Design | Files | Checkpoint |
|---|---|---|---|---|---|---|---|
| 2.1.1 | AuthCoordinator (route decision matrix) | normal | pending | AC-001.1, AC-002.1, AC-002.2, AC-002.4 | 7.2 | Features/Authentication/Services/AuthCoordinator.swift | Route decision matrix |
| 2.1.2 | SplashViewModel + SplashView | normal | pending | AC-001.1, AC-002.1 | 7.2 | Features/Authentication/ViewModels/SplashViewModel.swift, Features/Authentication/Views/SplashView.swift | Splash shows + decides ≤2s |
| 3.1.1 | SignInViewModel | normal | pending | AC-001.2, AC-001.3, AC-001.4 | 7.1 | Features/Authentication/ViewModels/SignInViewModel.swift | Sign in / cancel / error paths |
| 3.2.1 | SignInView + SignInWithAppleButton | normal | pending | AC-001.1, AC-001.2, AC-001.3, AC-001.4 | 7.1 | Features/Authentication/Views/SignInView.swift, Features/Authentication/Views/SignInWithAppleButton.swift | UIKit→SwiftUI button bridge |
| 3.3.1 | SignOutConfirmModal + SignOutViewModel | normal | pending | AC-003.1, AC-003.2, AC-003.4 | 7.3 | Features/Authentication/Views/SignOutConfirmModal.swift, Features/Authentication/ViewModels/SignOutViewModel.swift | Confirm/cancel/retry |
| 3.4.1 | Wire SplashView into RootView/CaloApp + sign-out entry from Settings | normal | pending | AC-001.1, AC-002.1, AC-003.1 | 8 | App/RootView.swift, App/CaloApp.swift, Features/Authentication/Views/SplashView.swift | Splash hosts in root; sign-out hook |
| 4.1.1 | AuthCoordinator tests | pbt | pending | AC-001.1, AC-002.1, AC-002.2, AC-002.4 | 6 | calo-ai-testTests/AuthCoordinatorTests.swift | Route matrix |
| 4.1.2 | SplashViewModel tests | pbt | pending | AC-001.1, AC-002.1 | 6 | calo-ai-testTests/SplashViewModelTests.swift | decide() terminal phase |
| 4.1.3 | SignInViewModel tests (fake AuthServicing) | pbt | pending | AC-001.2, AC-001.3, AC-001.4 | 6 | calo-ai-testTests/SignInViewModelTests.swift | Sign-in / cancel / error |
| 4.1.4 | SignOutViewModel tests (fake AuthServicing) | pbt | pending | AC-003.2, AC-003.4 | 6 | calo-ai-testTests/SignOutViewModelTests.swift | Logout + clear + retry |
| 4.2.1 | Build + integration gate | normal | pending | AC-001.1, AC-002.1, AC-003.2 | 6 | (build gate) | build_sim green; Splash shows; sign-in flows |

## Dependency Matrix
| Task | Depends On | Can Parallel With |
|---|---|---|
| 2.1.1 | — | 2.1.2 |
| 2.1.2 | 2.1.1 | — |
| 3.1.1 | 2.1.1 | 3.3.1 |
| 3.2.1 | 3.1.1, 2.1.1 | 3.3.1 |
| 3.3.1 | 2.1.1 | 3.1.1, 3.2.1 |
| 3.4.1 | 2.1.2, 3.2.1, 3.3.1 | — |
| 4.1.1 | 2.1.1 | 4.1.2, 4.1.3, 4.1.4 |
| 4.1.2 | 2.1.2, 4.1.1 | 4.1.3, 4.1.4 |
| 4.1.3 | 3.1.1, 4.1.1 | 4.1.2, 4.1.4 |
| 4.1.4 | 3.3.1, 4.1.1 | 4.1.2, 4.1.3 |
| 4.2.1 | 3.4.1, 4.1.1, 4.1.2, 4.1.3, 4.1.4 | — |

## 1. Shared Tasks
> Routing logic + Splash scaffolding consumed by every auth screen.

- [ ] **2.1.1** `AuthCoordinator` — `enum Route { signIn, onboarding, main }`; `static func route(user: User?, sessionValid: Bool) -> Route` matrix (no session → signIn; signedIn + !onboardingComplete → onboarding; signedIn + onboardingComplete → main)
  - Refs: AC-001.1, AC-002.1, AC-002.2, AC-002.4
  - Design: 7.2
  - File: `Features/Authentication/Services/AuthCoordinator.swift`
- [ ] **2.1.2** `SplashViewModel` (`@MainActor ObservableObject`, `@Published phase: Phase`, `decide()` queries injected `AuthServicing.sessionValid()` / `getUser()` and emits terminal phase via `AuthCoordinator`); `SplashView` (logo + spinner, ≤2s, cross-fade)
  - Refs: AC-001.1, AC-002.1
  - Design: 7.2
  - File: `Features/Authentication/ViewModels/SplashViewModel.swift`, `Features/Authentication/Views/SplashView.swift`

**Phase Gate 2 (end of Shared phase):** Run XcodeBuildMCP `discover_projs -> list_schemes -> build_sim`, then traceability check (AC-001.1, AC-002.1, AC-002.2, AC-002.4 covered; Refs Design resolve).

## 2. Feature Tasks
> Sign in, sign-out, and Sign in with Apple button.

- [ ] **3.1.1** `SignInViewModel` — depends on injected `AuthServicing` + `ErrorPresenting`; `startSignIn()` / `cancel()` / `retry()`; state machine `idle / presenting / signedIn / cancelled / error(AppError)`; routes via `AuthCoordinator` on success
  - Refs: AC-001.2, AC-001.3, AC-001.4
  - Design: 7.1
  - File: `Features/Authentication/ViewModels/SignInViewModel.swift`
- [ ] **3.2.1** `SignInView` + `SignInWithAppleButton` (UIViewRepresentable wrapping `ASAuthorizationAppleIDProvider`); retry banner via `ErrorHandler`; cancel silent; `CaloButton` retry
  - Refs: AC-001.1, AC-001.2, AC-001.3, AC-001.4
  - Design: 7.1
  - File: `Features/Authentication/Views/SignInView.swift`, `Features/Authentication/Views/SignInWithAppleButton.swift`
- [ ] **3.3.1** `SignOutConfirmModal` (warning + Confirm/Cancel with `CaloButton`) + `SignOutViewModel` (state `idle / confirming / signingOut / signedOut / error`); calls `AuthService.logout()`; never navigates on failure (AC-003.4)
  - Refs: AC-003.1, AC-003.2, AC-003.4
  - Design: 7.3
  - File: `Features/Authentication/Views/SignOutConfirmModal.swift`, `Features/Authentication/ViewModels/SignOutViewModel.swift`
- [ ] **3.4.1** Wire `SplashView` as the root entry in `CaloApp` (host for ≤2s while decide runs) + register sign-out entry hook consumed by `account-management` (this spec exposes the modal+VM contract; the Settings list ships later)
  - Refs: AC-001.1, AC-002.1, AC-003.1
  - Design: 8
  - File: `App/RootView.swift`, `App/CaloApp.swift`, `Features/Authentication/Views/SplashView.swift`

**Phase Gate 3 (end of Feature phase):** Run XcodeBuildMCP `discover_projs -> list_schemes -> build_sim`, then traceability check (AC-001.*, AC-002.*, AC-003.* covered; Refs Design resolve).

## 3. Integration Tasks
> Unit tests + build/integration gate.

- [ ] **4.1.1** `AuthCoordinatorTests` — route matrix (no user, signedIn+!complete, signedIn+complete, expired, signedIn+nil-user)
  - Refs: AC-001.1, AC-002.1, AC-002.2, AC-002.4
  - Design: 6
  - File: `calo-ai-testTests/AuthCoordinatorTests.swift`
- [ ] **4.1.2** `SplashViewModelTests` — `decide()` invokes coordinator with the correct args and emits terminal `phase`; never hangs in `loading`
  - Refs: AC-001.1, AC-002.1
  - Design: 6
  - File: `calo-ai-testTests/SplashViewModelTests.swift`
- [ ] **4.1.3** `SignInViewModelTests` (fake `AuthServicing`) — success routes via coordinator; cancel stays idle (no token written); error surfaces
  - Refs: AC-001.2, AC-001.3, AC-001.4
  - Design: 6
  - File: `calo-ai-testTests/SignInViewModelTests.swift`
- [ ] **4.1.4** `SignOutViewModelTests` (fake `AuthServicing`) — confirmed logout clears state and emits `signedOut`; Keychain-clear failure surfaces error and does NOT emit `signedOut`
  - Refs: AC-003.2, AC-003.4
  - Design: 6
  - File: `calo-ai-testTests/SignOutViewModelTests.swift`
- [ ] **4.2.1** Build + integration gate: `build_sim` green; Splash shown ≤2s on launch; Sign in with Apple sheet presents; sign-out flow end-to-end; re-auth preserves User.id
  - Refs: AC-001.1, AC-002.1, AC-003.2
  - Design: 6
  - File: (build gate)

**Phase Gate 4 (end of Integration phase):** Run XcodeBuildMCP `discover_projs -> list_schemes -> build_sim` (+ `test_sim`), then traceability check (all 12 ACs traced to ≥1 done task; every Refs Design resolves).

## Traceability Matrix
| Task ID | AC | Design | Property | Status |
|---|---|---|---|---|
| 2.1.1 | AC-001.1, AC-002.1, AC-002.2, AC-002.4 | 7.2 | P5 | pending |
| 2.1.2 | AC-001.1, AC-002.1 | 7.2 | P1 | pending |
| 3.1.1 | AC-001.2, AC-001.3, AC-001.4 | 7.1 | P2, P3, P4 | pending |
| 3.2.1 | AC-001.1, AC-001.2, AC-001.3, AC-001.4 | 7.1 | P2, P3, P4 | pending |
| 3.3.1 | AC-003.1, AC-003.2, AC-003.4 | 7.3 | P7, P8 | pending |
| 3.4.1 | AC-001.1, AC-002.1, AC-003.1 | 8 | P1, P8 | pending |
| 4.1.1 | AC-001.1, AC-002.1, AC-002.2, AC-002.4 | 6 | P5 | pending |
| 4.1.2 | AC-001.1, AC-002.1 | 6 | P1 | pending |
| 4.1.3 | AC-001.2, AC-001.3, AC-001.4 | 6 | P2, P3, P4 | pending |
| 4.1.4 | AC-003.2, AC-003.4 | 6 | P7, P8 | pending |
| 4.2.1 | AC-001.1, AC-002.1, AC-003.2 | 6 | P1, P2, P7 | pending |

## Progress
| Section | Total | Done | Status |
|---|---:|---:|---|
| Shared | 2 | 0 | ⬜ |
| Feature | 4 | 0 | ⬜ |
| Integration | 5 | 0 | ⬜ |