# shared-foundations - Implementation Plan

## Execution Mode
- Mode: manual
- Policy: run sequentially by default (logic-first order from design.md)
- Gate: stop on phase boundary or blocking error

## Task Registry (Machine Readable)

| ID | Title | Type | Status | Refs AC | Refs Design | Files | Checkpoint |
|---|---|---|---|---|---|---|---|
| 2.1.1 | AppError taxonomy | normal | done | AC-005.1 | 5 | Shared/Utils/AppError.swift | Enum + userMessage + isRetryable |
| 2.1.2 | RetryPolicy (backoff ≤3/≤10s) | normal | done | AC-005.2, AC-005.4 | 5 | Shared/Utils/RetryPolicy.swift | Retryable retries; non-retryable doesn't |
| 2.2.1 | Domain models (User/MealLog/Ingredient/Macros) | normal | done | AC-001.1, AC-001.2, AC-001.3, AC-001.4 | 7.1 | Shared/Models/User.swift, Shared/Models/MealLog.swift, Shared/Models/Ingredient.swift | Codable round-trip + validate() |
| 2.3.1 | KeychainStore util | normal | done | AC-002.2 | 7.2 | Shared/Utils/KeychainStore.swift | Read/write/delete token in Keychain |
| 2.4.1 | Reachability util | normal | done | AC-004.4 | 7.4 | Shared/Utils/Reachability.swift, Shared/Utils/ReachabilityForwarder.swift | Emits online/offline changes |
| 3.1.1 | AuthServicing + AppleAuthService | normal | done | AC-002.1, AC-002.2, AC-002.3, AC-002.4, AC-002.5 | 7.2 | Shared/Services/AuthService.swift | Sign in/out/sessionValid/getUser |
| 3.2.1 | DataClienting + SupabaseRESTClient | normal | done | AC-003.1, AC-003.2, AC-003.3, AC-003.4, AC-003.5 | 7.3 | Shared/Services/DataClient.swift | JWT+HTTPS CRUD, decode-or-throw |
| 3.3.1 | OfflineSyncing + OfflineSyncService | normal | done | AC-004.1, AC-004.2, AC-004.3, AC-004.5 | 7.4 | Shared/Services/OfflineSyncService.swift | Cache + queue + ordered flush |
| 3.4.1 | ErrorHandler (ErrorPresenting + banner) | normal | done | AC-005.1, AC-005.3 | 7.5 | Shared/Services/ErrorHandler.swift | map()+present() publishes banner |
| 3.5.1 | CaloButton component | normal | done | AC-006.1, AC-006.3 | 7.6 | Shared/Components/Button/CaloButton.swift | 3 variants, a11y, ≥44pt |
| 3.5.2 | ProgressBar component (color + clamp) | normal | done | AC-006.2, AC-006.4 | 7.6 | Shared/Components/ProgressBar/ProgressBar.swift | Thresholds; clamp goal≤0 |
| 3.6.1 | Extend AppEnvironment (service container) | normal | done | AC-007.1, AC-007.2, AC-007.3 | 7.7 | App/AppEnvironment.swift, Shared/Services/InMemoryServices.swift | Vends services as protocols |
| 3.6.2 | AppEnvironment.fake() + wire real services in AppBootstrap | normal | done | AC-007.4 | 7.7 | App/AppEnvironment.swift, App/AppBootstrap.swift, App/RootView.swift, Shared/Components/Feedback/ErrorBannerOverlay.swift | Fake builds offline; real wired |
| 4.1.1 | Unit-test target + model tests | normal | deferred | AC-001.1, AC-001.3, AC-001.4 | 6 | calo-ai-testTests/UserModelTests.swift, calo-ai-testTests/MealLogModelTests.swift | Target added; model tests pass |
| 4.1.2 | AuthService tests (fake keychain) | pbt | deferred | AC-002.3, AC-002.4, AC-002.5 | 6 | calo-ai-testTests/AuthServiceTests.swift | Session/logout/failed-signin |
| 4.1.3 | DataClient tests (URLProtocol stub) | pbt | deferred | AC-003.2, AC-003.3, AC-003.4, AC-003.5 | 6 | calo-ai-testTests/DataClientTests.swift | JWT/HTTPS/unauth/decode |
| 4.1.4 | RetryPolicy + OfflineSync tests | pbt | deferred | AC-004.1, AC-004.3, AC-004.5, AC-005.2, AC-005.4 | 6 | calo-ai-testTests/RetryPolicyTests.swift, calo-ai-testTests/OfflineSyncServiceTests.swift | Backoff bound; ordered flush; retained fail |
| 4.2.1 | ProgressBar tests | pbt | deferred | AC-006.2, AC-006.4 | 6 | calo-ai-testTests/ProgressBarTests.swift | Color thresholds + clamp |
| 4.3.1 | Build + DI-fake + coverage gate | normal | deferred | AC-001.1, AC-007.4 | 6 | (build/CI gate) | build_sim green; fake preview builds; ≥60% |

## Dependency Matrix
| Task | Depends On | Can Parallel With |
|---|---|---|
| 2.1.1 | — | 2.2.1, 2.3.1, 2.4.1 |
| 2.1.2 | 2.1.1 | 2.2.1, 2.3.1 |
| 2.2.1 | — | 2.1.1, 2.3.1, 2.4.1 |
| 2.3.1 | — | 2.1.1, 2.2.1, 2.4.1 |
| 2.4.1 | — | 2.1.1, 2.2.1, 2.3.1 |
| 3.1.1 | 2.2.1, 2.3.1, 2.1.1 | 3.5.1, 3.5.2 |
| 3.2.1 | 2.2.1, 2.1.2, 3.1.1 | 3.3.1 |
| 3.3.1 | 2.2.1, 2.4.1, 2.1.1 | 3.2.1 |
| 3.4.1 | 2.1.1, 2.1.2 | 3.5.1, 3.5.2 |
| 3.5.1 | — | 3.1.1, 3.2.1, 3.3.1 |
| 3.5.2 | 2.2.1 | 3.5.1 |
| 3.6.1 | 3.1.1, 3.2.1, 3.3.1, 3.4.1 | — |
| 3.6.2 | 3.6.1 | — |
| 4.1.1 | 2.2.1 | 4.2.1 |
| 4.1.2 | 3.1.1, 4.1.1 | 4.1.3, 4.1.4 |
| 4.1.3 | 3.2.1, 4.1.1 | 4.1.2, 4.1.4 |
| 4.1.4 | 3.3.1, 2.1.2, 4.1.1 | 4.1.2, 4.1.3 |
| 4.2.1 | 3.5.2, 4.1.1 | 4.1.2 |
| 4.3.1 | 3.6.2, 4.1.1 | — |

## 1. Shared Tasks
> Utilities + models + error primitives that all services depend on.

- [x] **2.1.1** Define `AppError` enum (network/unauthenticated/validation/timeout/server/unknown) with `userMessage` + `isRetryable`
  - Refs: AC-005.1
  - Design: 5
  - File: `Shared/Utils/AppError.swift`
- [x] **2.1.2** Implement `RetryPolicy` — exponential backoff, ≤3 attempts, ≤10s cap; skips non-retryable errors
  - Refs: AC-005.2, AC-005.4
  - Design: 5
  - File: `Shared/Utils/RetryPolicy.swift`
- [x] **2.2.1** Implement `User`, `MealLog`, `Ingredient`, `Macros` (Codable/Identifiable, explicit CodingKeys, `validate()`)
  - Refs: AC-001.1, AC-001.2, AC-001.3, AC-001.4
  - Design: 7.1
  - File: `Shared/Models/User.swift`, `Shared/Models/MealLog.swift`, `Shared/Models/Ingredient.swift`
- [x] **2.3.1** Implement `KeychainStore` (read/write/delete token via Security.framework)
  - Refs: AC-002.2
  - Design: 7.2
  - File: `Shared/Utils/KeychainStore.swift`
- [x] **2.4.1** Implement `Reachability` (NWPathMonitor online/offline signal)
  - Refs: AC-004.4
  - Design: 7.4
  - File: `Shared/Utils/Reachability.swift`

**Phase Gate 2 (end of Shared phase):** Run XcodeBuildMCP `discover_projs -> list_schemes -> build_sim`, then traceability check (AC-005.1/.2/.4, AC-001.*, AC-002.2, AC-004.4 covered; all Refs Design resolve).

## 2. Feature Tasks
> Services (behind protocols), shared components, and DI wiring.

- [x] **3.1.1** `AuthServicing` protocol + `AppleAuthService` (Sign in with Apple, session via `KeychainStore`, logout clears, failed sign-in preserves state)
  - Refs: AC-002.1, AC-002.2, AC-002.3, AC-002.4, AC-002.5
  - Design: 7.2
  - File: `Shared/Services/AuthService.swift`
- [x] **3.2.1** `DataClienting` protocol + `SupabaseRESTClient` (URLSession→PostgREST, JWT header, HTTPS-only, decode-or-throw, unauth fail-fast, retry via `RetryPolicy`)
  - Refs: AC-003.1, AC-003.2, AC-003.3, AC-003.4, AC-003.5
  - Design: 7.3
  - File: `Shared/Services/DataClient.swift`
- [x] **3.3.1** `OfflineSyncing` protocol + `OfflineSyncService` (encrypted local cache, persisted write queue, ordered `flush()` on reconnect, last-write-wins, retained failures, `lastSyncedAt`)
  - Refs: AC-004.1, AC-004.2, AC-004.3, AC-004.5
  - Design: 7.4
  - File: `Shared/Services/OfflineSyncService.swift`
- [x] **3.4.1** `ErrorPresenting` + `ErrorHandler` (`map()` any error→`AppError`, `present()` publishes `ErrorBanner` with retry affordance)
  - Refs: AC-005.1, AC-005.3
  - Design: 7.5
  - File: `Shared/Services/ErrorHandler.swift`
- [x] **3.5.1** `CaloButton` (primary/secondary/destructive, a11y label, ≥44pt, Dynamic Type/Dark Mode)
  - Refs: AC-006.1, AC-006.3
  - Design: 7.6
  - File: `Shared/Components/Button/CaloButton.swift`
- [x] **3.5.2** `ProgressBar` (green ≤100% / yellow 100–110% / red >110%; clamp goal≤0 & negative current; accessibilityValue)
  - Refs: AC-006.2, AC-006.4
  - Design: 7.6
  - File: `Shared/Components/ProgressBar/ProgressBar.swift`
- [x] **3.6.1** Extend `AppEnvironment` to vend `auth/data/sync/errors` as protocols (constructor-injection source)
  - Refs: AC-007.1, AC-007.2, AC-007.3
  - Design: 7.7
  - File: `App/AppEnvironment.swift`
- [x] **3.6.2** `AppEnvironment.fake()` (in-memory services) + wire real services in `AppBootstrap`; add error-banner overlay hook to `RootView`
  - Refs: AC-007.4
  - Design: 7.7
  - File: `App/AppEnvironment.swift`, `App/AppBootstrap.swift`

**Phase Gate 3 (end of Feature phase):** Run XcodeBuildMCP `discover_projs -> list_schemes -> build_sim`, then traceability check (AC-002.*, AC-003.*, AC-004.1/.2/.3/.5, AC-005.1/.3, AC-006.*, AC-007.* covered; app builds with fakes; all Refs Design resolve).

## 3. Integration Tasks
> Unit tests + build/coverage gates. **Deferred** — the project-structure spec
> has not yet added a unit-test target. Tasks 4.1.1–4.3.1 are blocked on that
> prerequisite; they will be unblocked when a separate test-target spec lands.

- [ ] **4.1.1** Add unit-test target `calo-ai-testTests`; write `User`/`MealLog` model tests (validation + Codable round-trip)
  - Refs: AC-001.1, AC-001.3, AC-001.4
  - Design: 6
  - File: `calo-ai-testTests/UserModelTests.swift`, `calo-ai-testTests/MealLogModelTests.swift`
- [ ] **4.1.2** `AuthServiceTests` with a fake `KeychainStore` (sessionValid/logout/failed-signin invariants)
  - Refs: AC-002.3, AC-002.4, AC-002.5
  - Design: 6
  - File: `calo-ai-testTests/AuthServiceTests.swift`
- [ ] **4.1.3** `DataClientTests` with `URLProtocol` stub (JWT attached, HTTPS-only, unauth fail-fast, decode-or-throw)
  - Refs: AC-003.2, AC-003.3, AC-003.4, AC-003.5
  - Design: 6
  - File: `calo-ai-testTests/DataClientTests.swift`
- [ ] **4.1.4** `RetryPolicyTests` + `OfflineSyncServiceTests` (bound backoff; ordered flush + last-write-wins; retained failed item)
  - Refs: AC-004.1, AC-004.3, AC-004.5, AC-005.2, AC-005.4
  - Design: 6
  - File: `calo-ai-testTests/RetryPolicyTests.swift`, `calo-ai-testTests/OfflineSyncServiceTests.swift`
- [ ] **4.2.1** `ProgressBarTests` (color thresholds + clamp on goal 0/negative)
  - Refs: AC-006.2, AC-006.4
  - Design: 6
  - File: `calo-ai-testTests/ProgressBarTests.swift`
- [ ] **4.3.1** Build + DI-fake + coverage gate: `build_sim` green, `AppEnvironment.fake()` preview builds offline, Services/Models coverage ≥60%
  - Refs: AC-001.1, AC-007.4
  - Design: 6
  - File: (build/CI gate)

**Phase Gate 4 (end of Integration phase):** Run XcodeBuildMCP `discover_projs -> list_schemes -> build_sim` (+ `test_sim`), then traceability check (all 32 ACs traced to ≥1 done task; every Refs Design resolves).

## Traceability Matrix
| Task ID | AC | Design | Property | Status |
|---|---|---|---|---|
| 2.1.1 | AC-005.1 | 5 | P21 | done |
| 2.1.2 | AC-005.2, AC-005.4 | 5 | P13, P15 | done |
| 2.2.1 | AC-001.1, AC-001.2, AC-001.3, AC-001.4 | 7.1 | P1, P2, P3, P4 | done |
| 2.3.1 | AC-002.2 | 7.2 | P5 | done |
| 2.4.1 | AC-004.4 | 7.4 | P20 | done |
| 3.1.1 | AC-002.1, AC-002.2, AC-002.3, AC-002.4, AC-002.5 | 7.2 | P5, P6, P7 | done |
| 3.2.1 | AC-003.1, AC-003.2, AC-003.3, AC-003.4, AC-003.5 | 7.3 | P8, P9, P10, P11, P22 | done |
| 3.3.1 | AC-004.1, AC-004.2, AC-004.3, AC-004.5 | 7.4 | P12, P16, P20 | done |
| 3.4.1 | AC-005.1, AC-005.3 | 7.5 | P21 | done |
| 3.5.1 | AC-006.1, AC-006.3 | 7.6 | P23 | done |
| 3.5.2 | AC-006.2, AC-006.4 | 7.6 | P14, P17 | done |
| 3.6.1 | AC-007.1, AC-007.2, AC-007.3 | 7.7 | P18, P22 | done |
| 3.6.2 | AC-007.4 | 7.7 | P19 | done |
| 4.1.1 | AC-001.1, AC-001.3, AC-001.4 | 6 | P1, P2, P3 | deferred |
| 4.1.2 | AC-002.3, AC-002.4, AC-002.5 | 6 | P6, P7 | deferred |
| 4.1.3 | AC-003.2, AC-003.3, AC-003.4, AC-003.5 | 6 | P8, P9, P10, P11 | deferred |
| 4.1.4 | AC-004.1, AC-004.3, AC-004.5, AC-005.2, AC-005.4 | 6 | P12, P13, P15, P16 | deferred |
| 4.2.1 | AC-006.2, AC-006.4 | 6 | P14, P17 | deferred |
| 4.3.1 | AC-001.1, AC-007.4 | 6 | P19 | deferred |

## Progress
| Section | Total | Done | Status |
|---|---:|---:|---|
| Shared | 5 | 5 | ✅ |
| Feature | 8 | 8 | ✅ |
| Integration | 6 | 0 | ⬜ (deferred — no unit-test target yet) |
