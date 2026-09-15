# performance-optimization - Requirements

## Overview
`performance-optimization` là spec kết thúc của Phase 9 (Polish & QA). Nó đo và tối ưu các chỉ số hiệu năng cam kết trong PRD §9 + Overview §6.1 để app đạt "nhanh ngang Cal AI nhưng đáng tin cậy hơn": (1) **cold launch <2s** trên iPhone 12+ (NFR-001 / PRD §9), (2) **screen-to-content render <1s** với dữ liệu cache (PRD §9), (3) **AI recognition p95 <3s** — giới hạn của external AI Vision API (PRD §9; bên trong app chỉ tối ưu được request size + caching), (4) **crash investigation + memory profiling** — tìm và fix leak / allocation spike / hang, (5) **image cache (NSCache + cost limits) + network request batching (URLSession configuration)** để giảm memory peak + round-trip. Spec đo bằng `os_signpost` + `MetricKit` (Apple-native, không SPM), tận dụng `shared-foundations` `ErrorHandler` + `OfflineSyncService` cho retry/backoff bound, và đo trên iPhone 12+ sim + thực thiếtbằng TestFlight beta. KHÔNG bao gồm kiến trúc lại, thêm dependency ngoài Apple framework, hay thêm feature mới (xem `testing-integration` cho E2E + metadata + crash-free ≥99%).

## Evidence References
- **Market data from PRD:** Tốc độ là lợi thế cạnh tranh chính đã chọn (PRD §2 nguyên tắc 1) — mục tiêu core loop <10s, cold launch <2s, AI Vision p95 <3s (PRD §9). Cal AI mất niềm tin vì data breach 2026-03 (PRD §1) và crash / ANR không rõ nguyên nhân — Calo AI cần memory profiling + crash investigation chủ động để không lặp lại. App Category Health & Fitness có ARPU cao nhưng retention ngắn (Overview §6.2), nên cold launch <2s + render <1s quyết định D1 retention. Tối ưu image cache + batch network là những đòn tăng tốc truyền thống nhưng hay bị bỏ qua sau khi spec khác đã ổn định.
- **Source documents:**
  - `.claude/specs/Calo-AI/PRD.md` §9 (Cold launch <2.0s; Screen-to-content render <1.0s; AI Vision <5s end-to-end / <3s API p95; Crash-free ≥99.5%; offline + sync; portrait; iOS 16+; AVFoundation), §12 (KPI: scan completion rate, AI manual-override rate), §13 (rủi ro AI accuracy + data privacy)
  - `.claude/specs/Calo-AI/Project_Overview.md` §3.3 (Quyết định kiến trúc — AI Vision external ~500ms–3s latency vs on-device <100ms; trade-off chấp nhận vì time-to-market + accuracy), §5 Phase 3 (cold launch <2s; target core loop <10s), §6.1 (Cold launch <2s; AI Vision <3s p95; API p95 <1s; Crash-free ≥99%; Test coverage ≥60%), §3.1 (Supabase + Firebase + RevenueCat + Superwall)
  - `.claude/specs/Calo-AI/Functional_Requirements.md` NFR-001 (App launch <2s), NFR-002 (AI detection <5s, 10s timeout), NFR-003 (Diary load <500ms — feeds screen-to-content), NFR-015 (Crash-Free ≥99.9%), NFR-016 (retry/backoff)
  - `.claude/specs/Calo-AI/Use_Cases.md` UC-011 (diary load), UC-001/002 (camera preview), UC-003 (AI result)
  - `.claude/specs/Calo-AI/Project_Implementation_Roadmap.md` — Phase 9 (performance-optimization)
  - `.claude/specs/Calo-AI/shared-foundations/` — `OfflineSyncService` (cache layer), `ErrorHandler` (retry/backoff), `AppEnvironment` (DI)
  - `.claude/specs/Calo-AI/ai-recognition/` — `VisionAPIService` (URLSession target for batching)
- **Key KPIs / measurable targets (PRD §9 / Overview §6.1):** Cold launch <2s; Screen-to-content render <1s; AI Vision p95 <3s (external API bound); memory peak <150 MB steady-state + <250 MB transient; no leak (heap delta <5 MB after 10-min session); 95th-percentile image cache hit rate ≥80% for thumbnail reads; network request batches reduce connection count ≥40% on diary load.

## Requirements

### Requirement 1 (REQ-001): Cold Launch Optimization (<2s)
**User Story:** As a user opening the app for the first time or returning after a kill, I want the splash→tab bar ready in under 2 seconds on my iPhone 12+, so that the app feels instant and I don't churn before reaching the Camera tab (the first monetizable moment).
**Source:** PRD §9 (Cold launch <2.0s trên iPhone đời máy mục tiêu), NFR-001, Overview §6.1, §5 Phase 3; enables D1 retention KPI (Overview §6.2)

#### Acceptance Criteria
1. AC-001.1: THE SYSTEM SHALL measure cold launch end-to-end (process start → `RootView` interactive with all 4 tabs renderable) using `os_signpost` intervals tagged `app.launch` and SHALL record the value into a `LaunchTimeProbe` log line emitted on the first foreground event for later TestFlight telemetry.
2. AC-001.2: WHEN measured on iPhone 12+ simulator (iOS 16, ≤50% storage, clean install) over 10 cold launches with `xcrun simctl` `app_launch_measurement` THEN THE SYSTEM SHALL have a median cold launch ≤2000 ms and p95 ≤2500 ms (NFR-001 — leaves headroom for production variance).
3. AC-001.3: THE SYSTEM SHALL defer non-critical work off the launch path: `FirebaseApp.configure()`, Crashlytics, Firebase Analytics, and RevenueCat SDK init SHALL run on a background queue or after first frame; `OnboardingView`/`PaywallView`/`DashboardView` SHALL NOT eagerly instantiate view models before the first tab tap.
4. AC-001.4: IF a slow dependency (`URLSession` warm-up, large JSON parsing, CoreData stack bring-up) is detected as taking >100 ms on the launch path via `os_signpost` THEN THE SYSTEM SHALL move it off the launch path (lazy / background) and re-measure; the launch budget SHALL NOT regress vs the prior build (release-blocker).

### Requirement 2 (REQ-002): Screen-to-Content Render (<1s)
**User Story:** As a user switching between tabs (Diary, Dashboard, Settings) or returning to the Camera tab, I want content to render within 1 second, so that the app feels responsive and I don't perceive a blank screen or spinner.
**Source:** PRD §9 (Screen-to-content render <1.0s với dữ liệu đã cache), NFR-003 (Diary load <500ms với 100+ meals — tighter internal target), Overview §6.1; targets `diary-logging`, `dashboard-view`, `account-management`, `subscription-settings`, `settings-management`, `paywall-display`

#### Acceptance Criteria
1. AC-002.1: THE SYSTEM SHALL measure screen-to-content render as: tab tap → first interactive frame containing the screen's primary content (Diary list / Dashboard chart / Settings list / Paywall pricing cards / Camera preview when permission already granted) via `os_signpost` interval `screen.render.<ScreenName>`; the measured value SHALL be ≤1000 ms for cached data and ≤500 ms for Diary specifically (NFR-003).
2. AC-002.2: WHEN the user taps the Diary tab with a warm CoreData cache (`OfflineSyncService` snapshot exists, `lastSyncedAt` <60s old) THEN THE SYSTEM SHALL render the day's meal list from cache without a network round-trip and SHALL emit `screen.render.diary` with the cache-only duration.
3. AC-002.3: THE SYSTEM SHALL use SwiftUI view-identity-stable, pre-sized `LazyVStack`/`LazyHStack` cells with view-model `@StateObject` created on the main actor only when the view first appears (`onAppear`/`.task`); the screens SHALL NOT eagerly construct view models for every cell at table-load time.
4. AC-002.4: IF a screen renders >1s in the median over 10 instrumented taps THEN THE SYSTEM SHALL be reported in `PerfRegressionReport.md` with the slowest 3 frames + a remediation task; no screen shall ship in release state with median >1s (release-blocker per PRD §9).

### Requirement 3 (REQ-003): AI Recognition p95 <3s (External API Bound)
**User Story:** As a user snapping a meal photo, I want the AI recognition round-trip (request sent → result parsed) to complete under 3 seconds for 95% of calls, so that the core loop "chụp → nhận diện → xác nhận" feels fast and supports the <10s end-to-end core loop (PRD §9).
**Source:** PRD §9 (AI nhận diện ảnh core loop <5s end-to-end; API p95 <3s — đây là giới hạn của external AI Vision API, không thể đạt <800ms), NFR-002, Overview §3.3 (trade-off external vs on-device accepted for time-to-market + accuracy), PRD §12 (`photo_scan_completed` event with processing time)

#### Acceptance Criteria
1. AC-003.1: THE SYSTEM SHALL measure AI Vision API latency (request sent → response received + parsed) via `os_signpost` interval `ai.vision.latency`, recorded on every call from `VisionAPIService` (ai-recognition spec) and aggregated into `AIVisionPerfReport.md` with p50, p95, p99 over the prior TestFlight cycle (≥100 calls).
2. AC-003.2: WHEN measured across a TestFlight cycle of ≥100 AI Vision calls THEN THE SYSTEM SHALL have p95 latency ≤3000 ms and p99 ≤5000 ms (NFR-002 / PRD §9). The system SHALL request `image` JPEG payload ≤500 KB by re-encoding camera capture at quality 0.7 and ≤1600px long edge before upload (reduces transport time without losing AI accuracy).
3. AC-003.3: WHEN a transient network failure occurs during an AI Vision call THEN THE SYSTEM SHALL retry with the shared `RetryPolicy` (≤3 attempts, ≤10s cumulative per NFR-016 / shared-foundations `RetryPolicy`) and SHALL NOT block the user-facing spinner longer than the budget; the spinner is dismissed with a retry affordance once the budget is exhausted.
4. AC-003.4: IF p95 exceeds 3000 ms in a TestFlight cycle THEN THE SYSTEM SHALL fail the perf gate (`perf_signoff_check.sh`) and require either: (a) a transport mitigation (request size reduction, connection reuse, `URLSession` `waitsForConnectivity = false`), or (b) explicit sign-off in `PerfSignOff.md` from iOS Lead.

### Requirement 4 (REQ-004): Crash Investigation & Memory Profiling
**User Story:** As a release engineer, I want continuous memory profiling + crash investigation during the TestFlight beta so that we ship with no leak and no allocation spike that would push us below the NFR-015 crash-free ≥99% bar.
**Source:** PRD §9 (Crash-free ≥99.5%), NFR-015, Overview §6.1, §8 risk table (data privacy incident — leak detection); `tools/CrashMonitor/` (testing-integration) provides the verifier + report pipeline; `MetricKit` (iOS 13+) and `os_signpost` are Apple-native

#### Acceptance Criteria
1. AC-004.1: THE SYSTEM SHALL install `MetricKit` (`MXMetricManager.shared().add(self)`) and `os_signpost` intervals around all long-lived subscriptions (Camera capture session, `OfflineSyncService` reachability, `URLSession` tasks, Firebase observation, RevenueCat SDK callbacks) so that hangs, memory growth, and CPU spikes are tagged in the Instruments trace and `mxDiagnostics` payload.
2. AC-004.2: THE SYSTEM SHALL expose `MemoryProfiler.snapshot()` (heap used / peak / resident) from `AppDelegate.applicationDidReceiveMemoryWarning` and on every background→foreground transition; snapshots SHALL be exported via `mxDiagnostics` JSON during the TestFlight beta and parsed into `MemoryReport.md` showing peak, average, and per-feature allocation.
3. AC-004.3: WHEN the beta cycle ends THEN THE SYSTEM SHALL produce `CrashInvestigation.md` enumerating: (a) every Crashlytics crash signature with the owning feature spec, (b) every MetricKit hang diagnostic >250ms with stack frames, (c) any leak suspected from heap-delta over a 10-minute scripted session in `Instruments` (`leaks` template); each item SHALL have an owner (spec name) + fix ETA before the next beta.
4. AC-004.4: THE SYSTEM SHALL fix every P0 crash signature (crashes that occur on a happy-path user flow within 30s of launch) before promoting to public release; P1 signatures SHALL be triaged in `ReleaseSignOff.md` (testing-integration spec) with explicit sign-off if not fixed.
5. AC-004.5: IF memory peak exceeds 250 MB during the scripted 10-minute session OR a leak >5 MB is detected THEN THE SYSTEM SHALL fail the memory gate (`memory_gate.sh`) and require remediation (cache eviction, retain-cycle fix, or image-cache cost-limit reduction) before promotion.

### Requirement 5 (REQ-005): Image Cache & Network Request Batching
**User Story:** As a user scrolling a long Diary or Dashboard, I want images (meal photos, dashboard thumbnails) to load instantly from cache and I want the network chatter to be batched into few round-trips, so that scrolling stays smooth and the radio stays cool on cellular.
**Source:** PRD §9 (offline cache + sync), NFR-007/008 (offline read + sync queue), Overview §6.1 (Diary load <500ms), §3.3 (Supabase polling for some features), §3.1 (Supabase REST, Firebase); targets `diary-logging`, `dashboard-view`, `ai-recognition`, `account-management`

#### Acceptance Criteria
1. AC-005.1: THE SYSTEM SHALL provide an `ImageCache` (NSCache-based) with a `totalCostLimit` of 64 MB and per-entry `cost` = `width × height × 4` bytes; the cache SHALL evict by cost when the limit is hit and SHALL NOT retain UIImage instances past their underlying `Data` storage (`UIImage` constructed lazily on read).
2. AC-005.2: WHEN the same image URL is requested ≥2 times within a session THEN THE SYSTEM SHALL serve it from `ImageCache` without a network round-trip (cache hit); the per-session cache-hit rate for thumbnail reads SHALL be ≥80% measured by `image.cache.hit` / `image.cache.miss` signposts aggregated into `ImageCacheReport.md`.
3. AC-005.3: THE SYSTEM SHALL configure a single shared `URLSession` (`URLSessionConfiguration.default` with `httpMaximumConnectionsPerHost = 4`, `requestTimeoutInterval = 10`, `waitsForConnectivity = false`) for all Supabase/AI Vision/RevenueCat REST calls; `URLSession` instances SHALL be reused via `AppEnvironment` rather than constructed per-call.
4. AC-005.4: WHEN the Diary view loads ≥10 meals for the current day THEN THE SYSTEM SHALL batch all `meal_logs` reads into a single PostgREST query (`select=*,ingredients(*)`, `date=eq.<today>`) instead of N parallel reads; measured `network.requests.per.diary.load` SHALL be ≤1 (was N before optimization).

## Non-Functional Requirements
- NFR-PO-001: Measurement overhead — `os_signpost` instrumentation SHALL NOT add >2% to cold launch or screen-render time on iPhone 12+ sim (measured by A/B run with signposts disabled). Measured: paired launch timings.
- NFR-PO-002: AI Vision p95 — p95 ≤3000 ms; p99 ≤5000 ms over ≥100-call TestFlight cycle (NFR-002 / PRD §9). Measured: `AIVisionPerfReport.md`.
- NFR-PO-003: Memory ceiling — Steady-state memory SHALL be ≤150 MB; transient peak SHALL be ≤250 MB during the 10-minute scripted session (PRD §9 stability bar). Measured: `MemoryReport.md` from `mxDiagnostics` + `Instruments` `allocations` template.
- NFR-PO-004: Leak-free session — Heap delta from minute 1 to minute 10 of a scripted session SHALL be ≤5 MB (no retain cycle, no unbounded cache growth) (NFR-015 / Overview §6.1 stability). Measured: `leaks` template + `MemoryProfiler.snapshot()` series.
- NFR-PO-005: Cache correctness — `ImageCache.totalCostLimit` SHALL be respected (never exceed 64 MB); eviction policy SHALL be cost-based, NOT count-based (prevents one giant image evicting 200 small thumbnails). Measured: synthetic cache-fill test asserts peak ≤ 64 MB.
- NFR-PO-006: Network batching — A Diary load with ≥10 meals SHALL issue ≤1 network request (PostgREST `select=*,ingredients(*)`); measured `network.requests.per.diary.load`. Measured: `RequestCounter` signposts aggregated into `NetworkReport.md`.