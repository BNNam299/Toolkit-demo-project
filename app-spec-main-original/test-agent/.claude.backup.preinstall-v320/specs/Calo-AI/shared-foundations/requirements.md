# shared-foundations - Requirements

## Overview
`shared-foundations` là spec hạ tầng thứ hai (Phase 2) của Calo AI. Nó cung cấp các primitive dùng chung mà mọi feature spec (Camera, AI, Confirmation, Diary, Dashboard, Paywall, Onboarding, Account) đều dựa lên: **domain models** (User, MealLog, Ingredient), **authentication + session** (Sign in with Apple, token trong Keychain), **backend data client** (Supabase CRUD scoped bằng Row-Level Security qua JWT), **offline cache + sync queue**, **error handling + retry/backoff**, và **thư viện UI component dùng chung** (Button, ProgressBar). Spec KHÔNG dựng màn hình tính năng nào — nó là lớp Shared/Services + Shared/Models + Shared/Components mà `project-structure` đã chừa chỗ. Blocks tất cả spec Phase 3–8.

## Evidence References
- **Market data from PRD:** Khủng hoảng niềm tin Cal AI — rò rỉ 3.2 triệu bản ghi qua backend Firebase **không xác thực** (2026-03-09, Kiteworks/Hackread) — biến bảo mật dữ liệu + backend có auth thành lợi thế cạnh tranh (PRD §1, §4, §13). Định vị "app AI calo bạn không cần lo bị lộ dữ liệu" phụ thuộc trực tiếp vào lớp auth/RLS của spec này.
- **Source documents:**
  - `.claude/specs/Calo-AI/PRD.md` §9 (Backend có xác thực đầy đủ + RLS mặc định; Sign in with Apple bắt buộc; offline xem lại nhật ký; DI constructor injection; audit bảo mật trước beta)
  - `.claude/specs/Calo-AI/Project_Overview.md` §3.1–§3.3 (MVVM + Repository, Supabase + RLS, Keychain cho auth token, CoreData local read cache, quyết định Supabase vs Firebase)
  - `.claude/specs/Calo-AI/Functional_Requirements.md` — FR-012 (daily log data + BR-012.2 ngưỡng progress bar), FR-018 (User profile fields + ranges), §3 NFRs
  - `.claude/specs/Calo-AI/Project_Implementation_Roadmap.md` — Phase 2 file breakdown (User.swift, MealLog.swift, AuthService.swift, SupabaseService.swift, OfflineSyncService.swift, ErrorHandler.swift, Button.swift, ProgressBar.swift)
- **Key KPIs / measurable targets (PRD §5 / Overview §6.1):** Crash-free ≥99.5%; API p95 <1s (Supabase reads); Diary load <500ms; test coverage ≥60% core Services/ViewModels; auto-retry backoff ≤3 lần / ≤10s (NFR-016).

## Requirements

### Requirement 1 (REQ-001): Domain Data Models
**User Story:** As a feature developer, I want typed, validated `User`, `MealLog`, and `Ingredient` models with Codable/Identifiable conformance, so that every feature reads and writes the same well-formed domain data.
**Source:** FR-018 (User profile: height/weight/goal/calorieTarget), FR-012 (MealLog: date/ingredients/calories/macros), UC-016, UC-011; Roadmap Phase 2 models

#### Acceptance Criteria
1. AC-001.1: THE SYSTEM SHALL define a `User` model with at least `id`, `email`, `name`, `height`, `weight`, `goal`, `activityLevel`, `calorieTarget`, `onboardingComplete`, conforming to `Codable` and `Identifiable`.
2. AC-001.2: THE SYSTEM SHALL define a `MealLog` model with at least `id`, `userId`, `date`, `ingredients`, `totalCalories`, `macros` (protein/carbs/fat), `confidence`, and an `Ingredient` model with `id`, `name`, `portion`, `calories`, `macros`, `isSelected`.
3. AC-001.3: WHEN a model is decoded from backend JSON and re-encoded THEN THE SYSTEM SHALL round-trip without data loss (stable `CodingKeys`).
4. AC-001.4: IF a `User` field is out of its valid range (height 120–220 cm, weight 30–300 kg per BR-018.1/2) or a numeric total is negative (VR-012.1) THEN THE SYSTEM SHALL reject it via a validation function returning a typed error, not persist an invalid value.

### Requirement 2 (REQ-002): Authentication & Session (Sign in with Apple)
**User Story:** As a user, I want to sign in with my Apple ID and stay signed in across launches, so that my data syncs securely and I never see an unauthenticated data path.
**Source:** NFR-004 (Apple ID auth), NFR-006 (at-rest encryption / Keychain), PRD §9 (Sign in with Apple bắt buộc); enables `authentication`, and session for FR-024/FR-025 (getUser/sessionValid)

#### Acceptance Criteria
1. AC-002.1: THE SYSTEM SHALL expose an `AuthService` with `signInWithApple()`, `logout()`, `sessionValid()`, and `getUser()`.
2. AC-002.2: WHEN Sign in with Apple succeeds THEN THE SYSTEM SHALL persist the session/identity token in the iOS Keychain (never in `UserDefaults` or plaintext).
3. AC-002.3: WHEN the app relaunches with a valid stored session THEN THE SYSTEM SHALL report `sessionValid() == true` without prompting sign-in again.
4. AC-002.4: WHEN `logout()` is called THEN THE SYSTEM SHALL clear the Keychain token and cached user so `sessionValid() == false`.
5. AC-002.5: IF Sign in with Apple fails or is cancelled THEN THE SYSTEM SHALL surface a typed auth error and leave the prior session unchanged (no partial/authenticated state).

### Requirement 3 (REQ-003): Backend Data Client (Supabase + RLS)
**User Story:** As a feature developer, I want a Supabase-backed data client that performs CRUD scoped to the signed-in user, so that each user only ever reads/writes their own rows over an encrypted channel.
**Source:** NFR-005 (TLS 1.3), NFR-014 (data isolation / RLS), FR-012 (query today's logs), UC-011; Overview §3.1 (Supabase + RLS default-on)

#### Acceptance Criteria
1. AC-003.1: THE SYSTEM SHALL expose a `SupabaseService` (or `DataClient`) with generic `query`, `insert`, `update`, `delete` operations over Codable models.
2. AC-003.2: WHEN any request is issued THEN THE SYSTEM SHALL attach the authenticated user's JWT so Row-Level Security scopes results to that user.
3. AC-003.3: WHEN the network call completes THEN THE SYSTEM SHALL decode into the requested Codable type or throw a typed error (never return partially-decoded data).
4. AC-003.4: THE SYSTEM SHALL use only HTTPS/TLS endpoints and SHALL NOT issue any request over cleartext HTTP.
5. AC-003.5: IF a request is made while `sessionValid() == false` THEN THE SYSTEM SHALL fail fast with an unauthenticated error rather than sending an unscoped request.

### Requirement 4 (REQ-004): Offline Cache & Sync Queue
**User Story:** As a user with a flaky connection, I want to view my logged diary offline and have my changes sync when I reconnect, so that the app stays useful without a live connection.
**Source:** NFR-007 (offline logging + sync), NFR-008 (offline diary view + staleness marker), PRD §9 (offline read cache, last-write-wins)

#### Acceptance Criteria
1. AC-004.1: WHEN meal logs have been fetched once THEN THE SYSTEM SHALL cache them locally so the diary is readable offline.
2. AC-004.2: WHEN a write (create/update/delete) is made offline THEN THE SYSTEM SHALL enqueue it and report a pending/"Syncing…" state rather than failing.
3. AC-004.3: WHEN connectivity is restored THEN THE SYSTEM SHALL flush the queued writes in order and reconcile using last-write-wins.
4. AC-004.4: WHILE showing cached data offline THE SYSTEM SHALL expose a staleness indicator (e.g. "Last updated X min ago").
5. AC-004.5: IF a queued write permanently fails after retries THEN THE SYSTEM SHALL preserve the queued item and surface a recoverable error (no silent data loss).

### Requirement 5 (REQ-005): Error Handling & Retry Policy
**User Story:** As a feature developer, I want one typed error model plus a shared retry/backoff and user-facing error presenter, so that transient failures recover automatically and users see consistent, actionable messages.
**Source:** NFR-016 (auto-retry, exponential backoff, max 3 / 10s), FR-001 (permission errors), FR-003 (AI timeout/error paths)

#### Acceptance Criteria
1. AC-005.1: THE SYSTEM SHALL define a typed `AppError` taxonomy (at least: network, unauthenticated, validation, timeout, server, unknown).
2. AC-005.2: WHEN a transient (network/timeout/5xx) failure occurs THEN THE SYSTEM SHALL retry with exponential backoff, capped at 3 retries and ≤10s total (NFR-016).
3. AC-005.3: WHEN retries are exhausted THEN THE SYSTEM SHALL surface a user-facing error banner/message with a retry affordance, via a shared `ErrorHandler`.
4. AC-005.4: IF an error is non-retryable (validation, unauthenticated) THEN THE SYSTEM SHALL NOT retry and SHALL present the specific message immediately.

### Requirement 6 (REQ-006): Shared UI Components
**User Story:** As a feature developer, I want reusable Button and ProgressBar components in `Shared/Components/`, so that screens share one visual language instead of re-declaring styles.
**Source:** FR-014 (progress vs goal), FR-012 BR-012.2 (progress color thresholds), WF-004; Roadmap Phase 2 (Button, ProgressBar); all screens

#### Acceptance Criteria
1. AC-006.1: THE SYSTEM SHALL provide a reusable `Button` component (or style) exposing Primary, Secondary, and Destructive variants.
2. AC-006.2: THE SYSTEM SHALL provide a color-coded `ProgressBar` component that takes current/goal and renders green ≤100%, yellow 100–110%, red >110% (per BR-012.2).
3. AC-006.3: WHEN a component is rendered THEN THE SYSTEM SHALL support Dynamic Type and Dark Mode and expose accessibility labels (PRD §9 accessibility baseline; tap targets ≥44pt).
4. AC-006.4: IF `ProgressBar` receives a goal of zero or a negative current value THEN THE SYSTEM SHALL clamp to a safe rendering (no divide-by-zero / no NaN width).

### Requirement 7 (REQ-007): Service Composition & Dependency Injection
**User Story:** As a feature developer, I want the shared services provided through a lightweight injection point, so that ViewModels receive their dependencies via constructor injection and can be tested with fakes.
**Source:** PRD §9 (DI: constructor injection / factory nhẹ, tránh framework DI nặng), Overview §3.1; enables all feature ViewModels; extends `project-structure` `AppEnvironment`

#### Acceptance Criteria
1. AC-007.1: THE SYSTEM SHALL provide a composition point (e.g. `AppEnvironment`/service container) that vends `AuthService`, `SupabaseService`, `OfflineSyncService`, and `ErrorHandler`.
2. AC-007.2: WHEN a feature ViewModel is constructed THEN THE SYSTEM SHALL allow its dependencies to be injected via its initializer (constructor injection), not resolved from a global singleton inside the ViewModel.
3. AC-007.3: THE SYSTEM SHALL define protocols for each service so tests can substitute fakes/mocks.
4. AC-007.4: IF a required service is not provided in a test/preview context THEN THE SYSTEM SHALL allow a documented default/fake so previews and unit tests build without live backends.

## Non-Functional Requirements
- NFR-SF-001: Security in transit — All backend traffic SHALL use TLS 1.3+ (HTTPS only); 0 cleartext requests. (NFR-005)
- NFR-SF-002: Security at rest — Auth tokens SHALL be stored in the iOS Keychain; local cache SHALL be encrypted via device keychain-derived key. (NFR-006)
- NFR-SF-003: Data isolation — Every backend row access SHALL be RLS-scoped to the authenticated user; a request without a valid JWT SHALL return zero rows or an error, never another user's data. (NFR-014)
- NFR-SF-004: Retry bound — Automatic retry SHALL be capped at 3 attempts and ≤10s cumulative before surfacing to the user. (NFR-016)
- NFR-SF-005: Read latency — Cached diary reads SHALL render in <500ms; Supabase read p95 SHALL be <1s. (Overview §6.1)
- NFR-SF-006: Testability — Core Services and Models SHALL reach ≥60% unit-test coverage. (Overview §5)
