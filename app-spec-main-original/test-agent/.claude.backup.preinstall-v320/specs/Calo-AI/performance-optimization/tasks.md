# performance-optimization - Implementation Plan

## Execution Mode
- Mode: manual
- Policy: run sequentially by default (instrumentation first → measure → optimize → re-measure → gate)
- Gate: stop on phase boundary or blocking error

## Task Registry (Machine Readable)

| ID | Title | Type | Status | Refs AC | Refs Design | Files | Checkpoint |
|---|---|---|---|---|---|---|---|
| 2.1.1 | PerfSignpost typed wrappers + LaunchTimeProbe | normal | pending | AC-001.1, AC-002.1, AC-003.1, AC-005.2 | 7.1, 7.2, 7.3, 7.5 | Shared/Perf/PerfSignpost.swift, App/LaunchTimeProbe.swift | os_signpost intervals compile |
| 2.1.2 | URLSessionFactory.shared + AppEnvironment wiring | normal | pending | AC-001.3, AC-003.2, AC-005.3 | 7.1, 7.3, 7.5 | Shared/Perf/URLSessionFactory.swift, App/AppEnvironment.swift | One shared URLSession |
| 2.1.3 | MemoryProfiler + MetricKitSubscriber | normal | pending | AC-004.1, AC-004.2 | 7.4 | Shared/Perf/MemoryProfiler.swift, Shared/Perf/MetricKitSubscriber.swift, App/AppDelegate.swift | Snapshot + MX delegate wired |
| 3.1.1 | Defer Firebase/RC/Analytics init off launch path + lazy VMs | normal | pending | AC-001.3, AC-001.4, AC-002.3 | 7.1, 7.2 | App/AppDelegate.swift, App/RootView.swift | Eager work removed |
| 3.2.1 | Screen-render signposts across feature views (Diary/Dashboard/Settings/Paywall/Camera) | normal | pending | AC-002.1, AC-002.2, AC-002.3 | 7.2 | Features/Diary/Views/DiaryView.swift, Features/Dashboard/Views/DashboardView.swift, Features/Account/Views/AccountView.swift, Features/Paywall/Views/PaywallView.swift, Features/Camera/Views/CameraView.swift | Per-screen intervals |
| 3.3.1 | ImageReencoder + VisionAPIService instrumentation | normal | pending | AC-003.1, AC-003.2, AC-003.3 | 7.3 | Shared/Perf/ImageReencoder.swift, Features/AI/Services/VisionAPIService.swift | ≤500 KB, ≤1600px; signpost emit |
| 4.1.1 | ImageCache (NSCache, 64 MB cost limit) + RequestCounter | normal | pending | AC-005.1, AC-005.2, AC-005.3, AC-005.4 | 7.5 | Shared/Perf/ImageCache.swift, Shared/Perf/RequestCounter.swift | Cost-limit + per-op counter |
| 4.1.2 | Diary batch PostgREST + Dashboard thumbnail cache wiring | normal | pending | AC-005.3, AC-005.4 | 7.5 | Features/Diary/ViewModels/DiaryViewModel.swift, Features/Dashboard/ViewModels/DashboardViewModel.swift | One query per Diary load |
| 4.2.1 | LaunchTimeMeasurer + AIVisionPerfReportParser + MemoryGate + PerfSignoffCheck + PerfRegressionReport | normal | pending | AC-001.2, AC-002.4, AC-003.1, AC-003.4, AC-004.5 | 7.1, 7.2, 7.3, 7.4 | scripts/launch_time_measurer.sh, Tools/Perf/AIVisionPerfReportParser.swift, scripts/memory_gate.sh, scripts/perf_signoff_check.sh, Tools/Perf/PerfRegressionReport.md | All scripts exit 0 on success |
| 4.2.2 | CrashInvestigation.md + MemoryReport.md + ImageCacheReport.md + NetworkReport.md + LaunchTimeReport.md + AIVisionPerfReport.md + PerfSignOff.md templates | normal | pending | AC-001.1, AC-003.1, AC-004.3, AC-004.4, AC-005.2, AC-005.4 | 7.1, 7.3, 7.4, 7.5 | StoreMetadata/*, Tools/Perf/* | Report artifacts present |
| 4.2.3 | Performance unit tests (ImageCache/ImageReencoder/MemoryProfiler/RequestCounter) | pbt | pending | AC-005.1, AC-005.2 | 6 | calo-ai-testTests/Performance/ImageCacheTests.swift, ImageReencoderTests.swift, MemoryProfilerTests.swift, RequestCounterTests.swift | All unit tests green |
| 4.2.4 | DiaryLoadPerformanceTests + ColdLaunchUITests | pbt | pending | AC-001.2, AC-002.1 | 6 | Calo-AIUITests/Performance/DiaryLoadPerformanceTests.swift, Calo-AIUITests/Performance/ColdLaunchUITests.swift | Median ≤2000/1000 ms |
| 4.3.1 | Build + perf-signoff gate | normal | pending | AC-001.2, AC-003.4, AC-004.5 | 6 | (build gate) | All scripts green; TestFlight ≥1 cycle |

## Dependency Matrix
| Task | Depends On | Can Parallel With |
|---|---|---|
| 2.1.1 | — | 2.1.2, 2.1.3 |
| 2.1.2 | — | 2.1.1, 2.1.3 |
| 2.1.3 | — | 2.1.1, 2.1.2 |
| 3.1.1 | 2.1.1, 2.1.2 | 3.2.1, 3.3.1 |
| 3.2.1 | 2.1.1 | 3.1.1, 3.3.1 |
| 3.3.1 | 2.1.1, 2.1.2 | 3.1.1, 3.2.1 |
| 4.1.1 | 2.1.2 | 4.1.2, 4.2.1, 4.2.3 |
| 4.1.2 | 4.1.1 | 4.2.1, 4.2.3 |
| 4.2.1 | 2.1.1, 2.1.3, 3.1.1, 3.3.1, 4.1.1 | 4.2.2, 4.2.3 |
| 4.2.2 | 4.2.1 | 4.2.3, 4.2.4 |
| 4.2.3 | 4.1.1, 4.1.2 | 4.2.2, 4.2.4 |
| 4.2.4 | 2.1.1, 3.1.1, 3.2.1, 4.1.2 | 4.2.2, 4.2.3 |
| 4.3.1 | 3.*, 4.* | — |

## 1. Shared Tasks
> Instrumentation primitives shared by every feature/perf task.

- [ ] **2.1.1** `PerfSignpost` (typed wrappers around `os_signpost`: `appLaunchInterval()`, `screenRender(_ name:)`, `aiVisionLatency()`, `imageCacheHit/Miss`, `networkRequestPer(_ op:)`) + `LaunchTimeProbe` that emits `app.launch` and logs the value on first foreground
  - Refs: AC-001.1, AC-002.1, AC-003.1, AC-005.2
  - Design: 7.1, 7.2, 7.3, 7.5
  - File: `Shared/Perf/PerfSignpost.swift`, `App/LaunchTimeProbe.swift`
- [ ] **2.1.2** `URLSessionFactory.shared` (one `URLSession`, default config + `httpMaximumConnectionsPerHost = 4` + `requestTimeoutInterval = 10` + `waitsForConnectivity = false`) + extend `AppEnvironment` to vend it; replace any per-call `.session` constructions
  - Refs: AC-001.3, AC-003.2, AC-005.3
  - Design: 7.1, 7.3, 7.5
  - File: `Shared/Perf/URLSessionFactory.swift`, `App/AppEnvironment.swift`
- [ ] **2.1.3** `MemoryProfiler.snapshot()` (Mach `task_info` typed API) + `MetricKitSubscriber : MXMetricManagerDelegate` (forwards payloads to `MemoryReport.md` / `CrashInvestigation.md`); wire from `AppDelegate.applicationDidReceiveMemoryWarning` and `applicationDidBecomeActive`
  - Refs: AC-004.1, AC-004.2
  - Design: 7.4
  - File: `Shared/Perf/MemoryProfiler.swift`, `Shared/Perf/MetricKitSubscriber.swift`, `App/AppDelegate.swift`

**Phase Gate 2 (end of Shared phase):** Run XcodeBuildMCP `discover_projs -> list_schemes -> build_sim`, then traceability check (AC-001.1, AC-002.1, AC-003.1, AC-004.1, AC-004.2, AC-005.2, AC-005.3 covered; instrumentation compiles; Refs Design resolve).

## 2. Feature Tasks
> Apply instrumentation + first-pass optimizations to the app launch path, screen-render path, and AI Vision path.

- [ ] **3.1.1** Defer `FirebaseApp.configure()` + RevenueCat SDK + Firebase Analytics init off launch path (background queue after first frame); replace eager view-model `@StateObject var vm = FooViewModel()` in `RootView` and feature tabs with lazy `@StateObject` constructed on `.task(id:)`; lazy `URLSession` warm-up via `URLSessionFactory.shared`; assert no `os_signpost`-tagged launch-path step exceeds 100 ms (AC-001.4 regression guard)
  - Refs: AC-001.3, AC-001.4, AC-002.3
  - Design: 7.1, 7.2
  - File: `App/AppDelegate.swift`, `App/RootView.swift`
- [ ] **3.2.1** Wrap tab-tap → first interactive frame in `PerfSignpost.screenRender(name:)` for Diary (`diary`), Dashboard (`dashboard`), Settings (`settings`), Paywall (`paywall`), Camera preview (`camera.preview`); emit `screen.render.diary` with cache-only duration when `OfflineSyncService.lastSyncedAt < 60s`
  - Refs: AC-002.1, AC-002.2, AC-002.3
  - Design: 7.2
  - File: `Features/Diary/Views/DiaryView.swift`, `Features/Dashboard/Views/DashboardView.swift`, `Features/Account/Views/AccountView.swift`, `Features/Paywall/Views/PaywallView.swift`, `Features/Camera/Views/CameraView.swift`
- [ ] **3.3.1** `ImageReencoder` re-encodes captured `UIImage` to ≤1600px long edge + quality 0.7 JPEG (≤500 KB) before upload; `VisionAPIService.analyze` wraps the URLSession call in `PerfSignpost.aiVisionLatency()` and uses `URLSessionFactory.shared`; the existing `RetryPolicy` (shared-foundations) continues to cap retries (NFR-016)
  - Refs: AC-003.1, AC-003.2, AC-003.3
  - Design: 7.3
  - File: `Shared/Perf/ImageReencoder.swift`, `Features/AI/Services/VisionAPIService.swift`

**Phase Gate 3 (end of Feature phase):** Run XcodeBuildMCP `discover_projs -> list_schemes -> build_sim -> test_sim`, then run `launch_time_measurer.sh` x10 + a manual `screen.render` spot check; traceability check (AC-001.1/.3, AC-002.1/.2/.3, AC-003.1/.2/.3 covered; app still builds + tests pass; Refs Design resolve).

## 3. Integration Tasks
> Cache + batching + perf gates + reports + perf unit/UI tests.

- [ ] **4.1.1** `ImageCache` (NSCache, `totalCostLimit = 64 MB`, per-entry cost = `w * h * 4`; lazy `UIImage` construction; emits `image.cache.hit/.miss`) + `RequestCounter` (thread-safe per-op counter, exposed via `AppEnvironment`)
  - Refs: AC-005.1, AC-005.2, AC-005.3, AC-005.4
  - Design: 7.5
  - File: `Shared/Perf/ImageCache.swift`, `Shared/Perf/RequestCounter.swift`
- [ ] **4.1.2** `DiaryViewModel.loadToday` issues ONE PostgREST query `GET /meal_logs?select=*,ingredients(*)&date=eq.<today>&order=created_at.desc` (instead of N parallel reads) + uses `RequestCounter` to assert `network.requests.per.diary.load = 1`; `DashboardViewModel` reuses `ImageCache.shared` for thumbnail URLs
  - Refs: AC-005.3, AC-005.4
  - Design: 7.5
  - File: `Features/Diary/ViewModels/DiaryViewModel.swift`, `Features/Dashboard/ViewModels/DashboardViewModel.swift`
- [ ] **4.2.1** `launch_time_measurer.sh` (x10 `xcrun simctl app_launch_measurement` → `LaunchTimeReport.md`) + `AIVisionPerfReportParser` (consumes signpost CSV → p50/p95/p99 → `AIVisionPerfReport.md`) + `memory_gate.sh` (reads `MemoryReport.md`; exits 0 iff peak ≤250 MB, leak ≤5 MB) + `perf_signoff_check.sh` (aggregates launch + AI Vision + memory gates; exits 0 on success) + `PerfRegressionReport.md` generation for any screen with median `screen.render` >1s (AC-002.4 release-blocker)
  - Refs: AC-001.2, AC-002.4, AC-003.1, AC-003.4, AC-004.5
  - Design: 7.1, 7.2, 7.3, 7.4
  - File: `scripts/launch_time_measurer.sh`, `Tools/Perf/AIVisionPerfReportParser.swift`, `scripts/memory_gate.sh`, `scripts/perf_signoff_check.sh`, `Tools/Perf/PerfRegressionReport.md`
- [ ] **4.2.2** `CrashInvestigation.md` (every Crashlytics signature + MetricKit hang + leak with owning spec + P0 fix-before-promote marker per AC-004.4) + `MemoryReport.md` + `ImageCacheReport.md` + `NetworkReport.md` + `LaunchTimeReport.md` + `AIVisionPerfReport.md` + `PerfSignOff.md` templates under `StoreMetadata/` (generated by parsers or seeded with headers); `PerfRegressionReport.md` template for `perf_signoff_check.sh` output
  - Refs: AC-001.1, AC-003.1, AC-004.3, AC-004.4, AC-005.2, AC-005.4
  - Design: 7.1, 7.3, 7.4, 7.5
  - File: `StoreMetadata/*`, `Tools/Perf/*`
- [ ] **4.2.3** `ImageCacheCostLimitTests` (synthetic 200 mixed-size images; asserts peak ≤64 MB, cost-based eviction) + `ImageReencoderTests` (asserts output ≤500 KB, quality ≥0.6 SSIM, ≤1600px long edge) + `MemoryProfilerTests` (mocks `task_info`) + `RequestCounterTests` (concurrency)
  - Refs: AC-005.1, AC-005.2
  - Design: 6
  - File: `calo-ai-testTests/Performance/ImageCacheTests.swift`, `ImageReencoderTests.swift`, `MemoryProfilerTests.swift`, `RequestCounterTests.swift`
- [ ] **4.2.4** `DiaryLoadPerformanceTests` (10 tab taps; assert median ≤1000 ms; Diary ≤500 ms cached) + `ColdLaunchUITests` (10 cold launches via `xcrun simctl app_launch_measurement`; assert median ≤2000 ms, p95 ≤2500 ms)
  - Refs: AC-001.2, AC-002.1
  - Design: 6
  - File: `Calo-AIUITests/Performance/DiaryLoadPerformanceTests.swift`, `Calo-AIUITests/Performance/ColdLaunchUITests.swift`
- [ ] **4.3.1** Build + perf-signoff gate: `build_sim` + `test_sim` (unit + UI) green; `launch_time_measurer.sh` passes (median ≤2000 ms, p95 ≤2500 ms); `perf_signoff_check.sh` passes (AI Vision p95 ≤3000 ms, memory peak ≤250 MB); ≥1 TestFlight cycle exports the perf reports
  - Refs: AC-001.2, AC-003.4, AC-004.5
  - Design: 6
  - File: (build gate)

**Phase Gate 4 (end of Integration phase):** Run XcodeBuildMCP `discover_projs -> list_schemes -> build_sim -> test_sim`, then `launch_time_measurer.sh` + `memory_gate.sh` + `perf_signoff_check.sh`; traceability check (all 21 ACs traced to ≥1 done task; every Refs Design resolves).

## Traceability Matrix
| Task ID | AC | Design | Property | Status |
|---|---|---|---|---|
| 2.1.1 | AC-001.1, AC-002.1, AC-003.1, AC-005.2 | 7.1, 7.2, 7.3, 7.5 | P1, P3, P6, P12 | pending |
| 2.1.2 | AC-001.3, AC-003.2, AC-005.3 | 7.1, 7.3, 7.5 | P1, P6, P13 | pending |
| 2.1.3 | AC-004.1, AC-004.2 | 7.4 | P9 | pending |
| 3.1.1 | AC-001.3, AC-001.4, AC-002.3 | 7.1, 7.2 | P1, P2, P4 | pending |
| 3.2.1 | AC-002.1, AC-002.2, AC-002.3 | 7.2 | P3, P4, P5 | pending |
| 3.3.1 | AC-003.1, AC-003.2, AC-003.3 | 7.3 | P6, P7 | pending |
| 4.1.1 | AC-005.1, AC-005.2, AC-005.3, AC-005.4 | 7.5 | P12, P13, P14 | pending |
| 4.1.2 | AC-005.3, AC-005.4 | 7.5 | P13, P14 | pending |
| 4.2.1 | AC-001.2, AC-002.4, AC-003.1, AC-003.4, AC-004.5 | 7.1, 7.2, 7.3, 7.4 | P1, P5, P8, P11 | pending |
| 4.2.2 | AC-001.1, AC-003.1, AC-004.3, AC-004.4, AC-005.2, AC-005.4 | 7.1, 7.3, 7.4, 7.5 | P3, P6, P10, P12, P14 | pending |
| 4.2.3 | AC-005.1, AC-005.2 | 6 | P12 | pending |
| 4.2.4 | AC-001.2, AC-002.1 | 6 | P1, P3 | pending |
| 4.3.1 | AC-001.2, AC-003.4, AC-004.5 | 6 | P1, P8, P11 | pending |

## Progress
| Section | Total | Done | Status |
|---|---:|---:|---|
| Shared | 3 | 0 | ⬜ |
| Feature | 3 | 0 | ⬜ |
| Integration | 7 | 0 | ⬜ |