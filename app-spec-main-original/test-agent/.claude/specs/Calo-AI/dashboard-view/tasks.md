# dashboard-view - Implementation Plan

## Execution Mode
- Mode: manual
- Policy: run sequentially by default (hybrid order from design.md)
- Gate: stop on phase boundary or blocking error

## Task Registry (Machine Readable)

| ID | Title | Type | Status | Refs AC | Refs Design | Files | Checkpoint |
|---|---|---|---|---|---|---|---|
| 2.1.1 | WeeklyStats + DayBucket + MacroBreakdown + GoalStatus + Weekday + WeeklyInsight models | normal | pending | AC-001.1, AC-001.2, AC-001.4, AC-001.5, AC-002.2, AC-002.3, AC-002.4, AC-003.1, AC-003.2, AC-003.5 | 4 | Features/Dashboard/Models/WeeklyStats.swift | 7 days, Mon-Sun, goal status thresholds, percentages sum 100%±1% |
| 2.1.2 | DashboardRepository (week read over DataClient) | normal | pending | AC-001.1, AC-001.2, AC-001.3, AC-001.4, AC-001.5 | 7.1 | Features/Dashboard/Services/DashboardRepository.swift | fetchWeek(containing:) returns 7 buckets; default goal=2000 |
| 2.1.3 | InsightsGenerator (pure rule engine) | normal | pending | AC-003.1, AC-003.2, AC-003.3, AC-003.4, AC-003.5 | 7.3 | Features/Dashboard/Services/InsightsGenerator.swift | tone buckets + coaching tips + empty placeholder |
| 2.1.4 | ExportService (CSV write + UIActivityViewController) | normal | pending | AC-004.1, AC-004.2, AC-004.4, AC-004.5 | 7.4 | Features/Dashboard/Services/ExportService.swift | CSV header + 7 rows + summary; temp file cleanup |
| 3.1.1 | DashboardViewModel (state, cache 5min, lifecycle, callbacks) | normal | pending | AC-001.3, AC-005.1, AC-005.2, AC-005.3, AC-005.4 | 7.5 | Features/Dashboard/ViewModels/DashboardViewModel.swift | State machine + 5min cache + Retry + onToggleToDaily |
| 3.2.1 | WeeklySummaryCard | normal | pending | AC-001.1, AC-001.3, AC-001.5 | 7.1 | Features/Dashboard/Views/WeeklySummaryCard.swift | Renders total + avg; empty/goal-unset banners |
| 3.2.2 | WeeklyBarChart (Swift Charts, iOS 16+) | normal | pending | AC-002.1, AC-002.2, AC-002.5 | 7.2 | Features/Dashboard/Views/WeeklyBarChart.swift | 7 bars color-coded; iOS<16 fallback text |
| 3.2.3 | MacroPieChart (Swift Charts) | normal | pending | AC-002.3, AC-002.4 | 7.2 | Features/Dashboard/Views/MacroPieChart.swift | 3 slices; placeholder when isEmpty |
| 3.2.4 | InsightTextView | normal | pending | AC-003.1, AC-003.3, AC-003.5 | 7.3 | Features/Dashboard/Views/InsightTextView.swift | Renders headline + optional tip |
| 3.2.5 | ShareModal (WF-015) | normal | pending | AC-004.2, AC-004.3 | 7.4 | Features/Dashboard/Views/ShareModal.swift | Preview + Share/Cancel; UIActivityViewController |
| 3.3.1 | DashboardView assembly (composes card + charts + insight + buttons + modal) | normal | pending | AC-001.1, AC-001.3, AC-002.1, AC-002.3, AC-003.1, AC-004.1, AC-004.2, AC-005.1 | 7.5 | Features/Dashboard/Views/DashboardView.swift | Renders all subviews; wires callbacks |
| 3.4.1 | RootView wiring (replace PlaceholderView for Dashboard + onToggleToDaily) | normal | pending | AC-005.1 | 8 | App/RootView.swift | Dashboard tab shows DashboardView; toggle callback switches to .diary |
| 4.1.1 | WeeklyStatsComputationTests | pbt | pending | AC-001.1, AC-001.2, AC-001.3, AC-001.4, AC-001.5, AC-002.2, AC-002.3, AC-002.4 | 6 | calo-ai-testTests/WeeklyStatsComputationTests.swift | 7-day invariants; goal status thresholds; macro sum |
| 4.1.2 | InsightsGeneratorTests | pbt | pending | AC-003.1, AC-003.2, AC-003.3, AC-003.4, AC-003.5 | 6 | calo-ai-testTests/InsightsGeneratorTests.swift | Tone buckets; coaching tips; empty placeholder |
| 4.1.3 | DashboardViewModelTests (fakes) | pbt | pending | AC-001.3, AC-004.4, AC-005.1, AC-005.2, AC-005.3, AC-005.4 | 6 | calo-ai-testTests/DashboardViewModelTests.swift | Cache fresh/stale; error + retry; lifecycle; toggle |
| 4.1.4 | ExportServiceTests | pbt | pending | AC-004.1, AC-004.4 | 6 | calo-ai-testTests/ExportServiceTests.swift | CSV header + rows; partial-file cleanup on throw |
| 4.1.5 | ChartFallbackTests | pbt | pending | AC-002.5 | 6 | calo-ai-testTests/ChartFallbackTests.swift | iOS<16 path returns text-only summary |
| 4.2.1 | Build + integration gate | normal | pending | AC-001.1, AC-002.1, AC-003.1, AC-004.1, AC-005.1 | 6 | (build gate) | build_sim green; Dashboard tab renders |

## Dependency Matrix
| Task | Depends On | Can Parallel With |
|---|---|---|
| 2.1.1 | — | 2.1.2, 2.1.3, 2.1.4 |
| 2.1.2 | 2.1.1 | 2.1.3, 2.1.4 |
| 2.1.3 | 2.1.1 | 2.1.2, 2.1.4 |
| 2.1.4 | 2.1.1 | 2.1.2, 2.1.3 |
| 3.1.1 | 2.1.1, 2.1.2 | 3.2.1, 3.2.2, 3.2.3, 3.2.4, 3.2.5 |
| 3.2.1 | 2.1.1, 2.1.2 | 3.1.1, 3.2.2, 3.2.3, 3.2.4, 3.2.5 |
| 3.2.2 | 2.1.1, 2.1.2 | 3.1.1, 3.2.1, 3.2.3, 3.2.4, 3.2.5 |
| 3.2.3 | 2.1.1, 2.1.2 | 3.1.1, 3.2.1, 3.2.2, 3.2.4, 3.2.5 |
| 3.2.4 | 2.1.3 | 3.1.1, 3.2.1, 3.2.2, 3.2.3, 3.2.5 |
| 3.2.5 | 2.1.4 | 3.1.1, 3.2.1, 3.2.2, 3.2.3, 3.2.4 |
| 3.3.1 | 3.1.1, 3.2.1, 3.2.2, 3.2.3, 3.2.4, 3.2.5 | — |
| 3.4.1 | 3.3.1 | — |
| 4.1.1 | 2.1.1, 2.1.2 | 4.1.2, 4.1.3, 4.1.4, 4.1.5 |
| 4.1.2 | 2.1.3 | 4.1.1, 4.1.3, 4.1.4, 4.1.5 |
| 4.1.3 | 3.1.1 | 4.1.1, 4.1.2, 4.1.4, 4.1.5 |
| 4.1.4 | 2.1.4 | 4.1.1, 4.1.2, 4.1.3, 4.1.5 |
| 4.1.5 | 2.1.1, 3.2.2, 3.2.3 | 4.1.1, 4.1.2, 4.1.3, 4.1.4 |
| 4.2.1 | 3.4.1, 4.1.1, 4.1.2, 4.1.3, 4.1.4, 4.1.5 | — |

## 1. Shared Tasks
> Models + services the Dashboard ViewModel and views depend on.

- [ ] **2.1.1** `WeeklyStats` (`weekStart` Mon 00:00 local, `days: [DayBucket; 7]`, `totalCalories`, `averageCalories`, `macroBreakdown`, `goal`, `isEmpty`) + `DayBucket` (`date`, `weekday`, `totalCalories`, `macro: Macros`, `goalStatus`) + `MacroBreakdown` (`proteinG/carbsG/fatG`, `isEmpty`, `proteinPct/carbsPct/fatPct` sum 100%±1%, calorie-equivalent ±10%) + `GoalStatus` (`.onTrack/.nearLimit/.over/.under` thresholds 100/110/80%) + `Weekday` enum with localized `shortLabel` + `WeeklyInsight` (`headline`, optional `coachingTip`)
  - Refs: AC-001.1, AC-001.2, AC-001.4, AC-001.5, AC-002.2, AC-002.3, AC-002.4, AC-003.1, AC-003.2, AC-003.5
  - Design: 4
  - File: `Features/Dashboard/Models/WeeklyStats.swift`
- [ ] **2.1.2** `DashboardRepository` (protocol) + `DashboardRepositoryImpl` (concrete) — `fetchWeek(containing date: Date) async throws -> WeeklyStats` over injected `DataClient`; groups `MealLog`s by `date` in Mon-Sun local window; substitutes `goal = 2000` if `User.calorieTarget <= 0` or nil; sets `isEmpty` when total=0 and macros empty
  - Refs: AC-001.1, AC-001.2, AC-001.3, AC-001.4, AC-001.5
  - Design: 7.1
  - File: `Features/Dashboard/Services/DashboardRepository.swift`
- [ ] **2.1.3** `InsightsGenerator` (pure) — `static func generate(stats: WeeklyStats, goal: Int, locale: Locale = .current) -> WeeklyInsight`; tone buckets by `avgPct` (≤1.0 / 1.0-1.10 / >1.10); coaching tip when ≥4/7 days `over` or `under`; placeholder "Hãy ghi log để xem insight tuần" when `stats.isEmpty`
  - Refs: AC-003.1, AC-003.2, AC-003.3, AC-003.4, AC-003.5
  - Design: 7.3
  - File: `Features/Dashboard/Services/InsightsGenerator.swift`
- [ ] **2.1.4** `ExportService` (protocol) + `ExportServiceImpl` — `writeCSV(stats:) throws -> URL` writes header `weekday,date,total_cal,daily_goal` + 7 daily rows + 1 summary row to NSTemporaryDirectory; `presentShareSheet(items:from:) async throws -> Bool` invokes `UIActivityViewController`; `cleanupTempFile(at:)` called in catch path of writeCSV
  - Refs: AC-004.1, AC-004.2, AC-004.4, AC-004.5
  - Design: 7.4
  - File: `Features/Dashboard/Services/ExportService.swift`

**Phase Gate 2 (end of Shared phase):** Run XcodeBuildMCP `discover_projs -> list_schemes -> build_sim`, then traceability check (AC-001.1/.2/.3/.4/.5, AC-002.2/.3/.4, AC-003.1/.2/.5, AC-004.1/.2/.4/.5 covered; Refs Design resolve).

## 2. Feature Tasks
> ViewModel + dashboard UI + subviews + RootView wiring.

- [ ] **3.1.1** `DashboardViewModel` — `@MainActor ObservableObject` with `state: DashboardState`; in-memory 5-min cache; `onAppear()` decides cache-fresh vs cache-stale path; `onDisappear()` cancels in-flight task; `refresh()` / `retry()`; `exportCSV() async -> URL?`; `openShareModal() / dismissShareModal()`; callback `onToggleToDaily: () -> Void`
  - Refs: AC-001.3, AC-005.1, AC-005.2, AC-005.3, AC-005.4
  - Design: 7.5
  - File: `Features/Dashboard/ViewModels/DashboardViewModel.swift`
- [ ] **3.2.1** `WeeklySummaryCard` — "Tổng tuần: N cal / Trung bình: M cal/ngày" + empty-state copy + CTA Camera when `isEmpty` + goal-unset banner
  - Refs: AC-001.1, AC-001.3, AC-001.5
  - Design: 7.1
  - File: `Features/Dashboard/Views/WeeklySummaryCard.swift`
- [ ] **3.2.2** `WeeklyBarChart` — Swift Charts `Chart { BarMark }` for 7 days; `foregroundStyle` by `GoalStatus` (green/yellow/red); iOS 16+ `if #available` guard with text-only fallback; `accessibilityLabel` summarizing all 7 days
  - Refs: AC-002.1, AC-002.2, AC-002.5
  - Design: 7.2
  - File: `Features/Dashboard/Views/WeeklyBarChart.swift`
- [ ] **3.2.3** `MacroPieChart` — Swift Charts `Chart { SectorMark }` for P/C/F with percentages; placeholder "Chưa có dữ liệu macro" when `isEmpty`; `accessibilityLabel` listing 3 percentages
  - Refs: AC-002.3, AC-002.4
  - Design: 7.2
  - File: `Features/Dashboard/Views/MacroPieChart.swift`
- [ ] **3.2.4** `InsightTextView` — renders `headline` + optional `coachingTip`; placeholder when insight is nil; VoiceOver reads both fields
  - Refs: AC-003.1, AC-003.3, AC-003.5
  - Design: 7.3
  - File: `Features/Dashboard/Views/InsightTextView.swift`
- [ ] **3.2.5** `ShareModal` (WF-015) — title "Chia Sẻ Tiến Độ" + preview text "Tôi đã ăn <N> calo hôm nay! 📊" + Share/Cancel buttons; uses `UIViewControllerRepresentable` to host `UIActivityViewController` on Share
  - Refs: AC-004.2, AC-004.3
  - Design: 7.4
  - File: `Features/Dashboard/Views/ShareModal.swift`
- [ ] **3.3.1** `DashboardView` — composes `WeeklySummaryCard` + `WeeklyBarChart` + `MacroPieChart` + `InsightTextView` + Export/Share buttons + "Xem hàng ngày" toggle; wires `onToggleToDaily` callback; shows `ShareModal` when toggled
  - Refs: AC-001.1, AC-001.3, AC-002.1, AC-002.3, AC-003.1, AC-004.1, AC-004.2, AC-005.1
  - Design: 7.5
  - File: `Features/Dashboard/Views/DashboardView.swift`
- [ ] **3.4.1** Replace `PlaceholderView("Dashboard")` in `RootView` with `DashboardView`; wire `onToggleToDaily` to `AppTab.diary` selection; ensure other tabs (Camera, Diary, Settings) untouched
  - Refs: AC-005.1
  - Design: 8
  - File: `App/RootView.swift`

**Phase Gate 3 (end of Feature phase):** Run XcodeBuildMCP `discover_projs -> list_schemes -> build_sim`, then traceability check (AC-001.1/.3/.5, AC-002.1/.2/.3/.4/.5, AC-003.1/.2/.3/.5, AC-004.1/.2/.3/.4/.5, AC-005.1 covered; Dashboard tab renders DashboardView; Refs Design resolve).

## 3. Integration Tasks
> Unit tests + build/integration gate.

- [ ] **4.1.1** `WeeklyStatsComputationTests` — 7-day invariants (Mon-Sun, count==7), `average == total/7`, missing days = 0, `goalStatus` thresholds, macro sum 100%±1%, calorie-equivalent ±10%, `isEmpty` detection
  - Refs: AC-001.1, AC-001.2, AC-001.3, AC-001.4, AC-001.5, AC-002.2, AC-002.3, AC-002.4
  - Design: 6
  - File: `calo-ai-testTests/WeeklyStatsComputationTests.swift`
- [ ] **4.1.2** `InsightsGeneratorTests` — tone buckets (≤100, 100-110, >110), coaching tips for ≥4/7 days over/under, empty placeholder
  - Refs: AC-003.1, AC-003.2, AC-003.3, AC-003.4, AC-003.5
  - Design: 6
  - File: `calo-ai-testTests/InsightsGeneratorTests.swift`
- [ ] **4.1.3** `DashboardViewModelTests` (fake `DashboardRepository`, fake `ExportService`) — cache-fresh (no re-query), cache-stale (re-query, `loading(prevStats?)` state), empty state, error + Retry, lifecycle (onAppear/onDisappear), `onToggleToDaily` fires once
  - Refs: AC-001.3, AC-004.4, AC-005.1, AC-005.2, AC-005.3, AC-005.4
  - Design: 6
  - File: `calo-ai-testTests/DashboardViewModelTests.swift`
- [ ] **4.1.4** `ExportServiceTests` — CSV header correctness, 7 daily rows + 1 summary row, partial-file cleanup on write throw, `UIActivityViewController` invocation (using a UIViewController fake)
  - Refs: AC-004.1, AC-004.4
  - Design: 6
  - File: `calo-ai-testTests/ExportServiceTests.swift`
- [ ] **4.1.5** `ChartFallbackTests` — iOS<16 simulation returns text-only summary; no Swift Charts API call attempted
  - Refs: AC-002.5
  - Design: 6
  - File: `calo-ai-testTests/ChartFallbackTests.swift`
- [ ] **4.2.1** Build + integration gate — `build_sim` green; Dashboard tab shows `DashboardView`; simulator smoke (Charts works on sim, UIActivityViewController verified on device)
  - Refs: AC-001.1, AC-002.1, AC-003.1, AC-004.1, AC-005.1
  - Design: 6
  - File: (build gate)

**Phase Gate 4 (end of Integration phase):** Run XcodeBuildMCP `discover_projs -> list_schemes -> build_sim` (+ `test_sim`), then traceability check (all 24 ACs traced to ≥1 done task; every Refs Design resolves).

## Traceability Matrix
| Task ID | AC | Design | Property | Status |
|---|---|---|---|---|
| 2.1.1 | AC-001.1, AC-001.2, AC-001.4, AC-001.5, AC-002.2, AC-002.3, AC-002.4, AC-003.1, AC-003.2, AC-003.5 | 4 | P1, P3, P4, P5, P7, P8, P11 | pending |
| 2.1.2 | AC-001.1, AC-001.2, AC-001.3, AC-001.4, AC-001.5 | 7.1 | P1, P2, P3, P4 | pending |
| 2.1.3 | AC-003.1, AC-003.2, AC-003.3, AC-003.4, AC-003.5 | 7.3 | P8, P9, P10, P11 | pending |
| 2.1.4 | AC-004.1, AC-004.2, AC-004.4, AC-004.5 | 7.4 | P12, P13, P14, P15 | pending |
| 3.1.1 | AC-001.3, AC-005.1, AC-005.2, AC-005.3, AC-005.4 | 7.5 | P2, P15, P16, P17 | pending |
| 3.2.1 | AC-001.1, AC-001.3, AC-001.5 | 7.1 | P1, P2, P4 | pending |
| 3.2.2 | AC-002.1, AC-002.2, AC-002.5 | 7.2 | P5, P6, P18 | pending |
| 3.2.3 | AC-002.3, AC-002.4 | 7.2 | P7 | pending |
| 3.2.4 | AC-003.1, AC-003.3, AC-003.5 | 7.3 | P8, P9, P10, P11 | pending |
| 3.2.5 | AC-004.2, AC-004.3 | 7.4 | P14, P15 | pending |
| 3.3.1 | AC-001.1, AC-001.3, AC-002.1, AC-002.3, AC-003.1, AC-004.1, AC-004.2, AC-005.1 | 7.5 | P5, P7, P8, P12, P14, P16 | pending |
| 3.4.1 | AC-005.1 | 8 | P16 | pending |
| 4.1.1 | AC-001.1, AC-001.2, AC-001.3, AC-001.4, AC-001.5, AC-002.2, AC-002.3, AC-002.4 | 6 | P1, P2, P3, P4, P5, P7 | pending |
| 4.1.2 | AC-003.1, AC-003.2, AC-003.3, AC-003.4, AC-003.5 | 6 | P8, P9, P10, P11 | pending |
| 4.1.3 | AC-001.3, AC-004.4, AC-005.1, AC-005.2, AC-005.3, AC-005.4 | 6 | P2, P13, P16, P17 | pending |
| 4.1.4 | AC-004.1, AC-004.4 | 6 | P12, P13 | pending |
| 4.1.5 | AC-002.5 | 6 | P18 | pending |
| 4.2.1 | AC-001.1, AC-002.1, AC-003.1, AC-004.1, AC-005.1 | 6 | P1, P5, P8, P12, P16 | pending |

## Progress
| Section | Total | Done | Status |
|---|---:|---:|---|
| Shared | 4 | 0 | ⬜ |
| Feature | 8 | 0 | ⬜ |
| Integration | 6 | 0 | ⬜ |
