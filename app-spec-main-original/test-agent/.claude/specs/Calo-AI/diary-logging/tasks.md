# diary-logging - Implementation Plan

## Execution Mode
- Mode: manual
- Policy: run sequentially by default (logic-first from design.md)
- Gate: stop on phase boundary or blocking error

## Task Registry (Machine Readable)

| ID | Title | Type | Status | Refs AC | Refs Design | Files | Checkpoint |
|---|---|---|---|---|---|---|---|
| 2.1.1 | ColorTier enum + threshold mapping (green/amber/red/unknown) | normal | pending | AC-003.2, AC-003.3, AC-003.4 | 4 | Features/Diary/Models/ColorTier.swift | ≤1.0 green, 1.0..1.1 amber, >1.1 red |
| 2.1.2 | DiaryEntry + WeeklySummary + DailyTotal value types | normal | pending | AC-001.1, AC-002.1, AC-002.2, AC-003.1 | 4 | Features/Diary/Models/DiaryEntry.swift, Features/Diary/Models/WeeklySummary.swift | consumed/remaining/ratio/tier; 7 days Mon..Sun |
| 2.2.1 | DiaryCalculationService (pure: dailyTotal + tier) | normal | pending | AC-003.1, AC-003.2, AC-003.3, AC-003.4, AC-003.5 | 7.3 | Features/Diary/Services/DiaryCalculationService.swift | Threshold grid exact |
| 2.2.2 | WeeklySummaryCalculator (pure: Mon..Sun, empty=0, average, total) | normal | pending | AC-002.1, AC-002.2, AC-002.3 | 7.2 | Features/Diary/Services/WeeklySummaryCalculator.swift | 7 rows always |
| 3.1.1 | DiaryViewModel (loadToday/loadWeek/refresh/edit/delete/applyExternalSave) | normal | pending | AC-001.1, AC-001.3, AC-001.4, AC-002.1, AC-002.3, AC-004.4, AC-005.3, AC-005.4, AC-006.2, AC-006.3, AC-006.4, AC-007.1, AC-007.2, AC-007.3, AC-007.4 | 7.1, 7.2, 7.6, 7.7 | Features/Diary/ViewModels/DiaryViewModel.swift | State machine; offline branch |
| 3.1.2 | EditMealViewModel (load meal + reuse MacroCalculationService + save) | normal | pending | AC-005.1, AC-005.2, AC-005.3, AC-005.4, AC-005.5 | 7.4, 7.5 | Features/Diary/ViewModels/EditMealViewModel.swift | Validation gates |
| 3.2.1 | ProgressBar consumer integration (hero zone) | normal | pending | AC-003.1, AC-003.2, AC-003.3, AC-003.4, AC-003.5 | 7.3 | Features/Diary/Views/DiaryView.swift | Reuses shared-foundations ProgressBar |
| 3.2.2 | MealListItem (row + swipe Edit/Delete) | normal | pending | AC-004.1, AC-004.2, AC-004.3, AC-004.4 | 7.4 | Features/Diary/Views/MealListItem.swift | Swipe reveal <200ms |
| 3.2.3 | EditMealModal (WF-013: form + Save/Cancel/Delete) | normal | pending | AC-005.1, AC-005.2, AC-005.3, AC-005.4, AC-005.5 | 7.5 | Features/Diary/Views/EditMealModal.swift | Reuses confirmation-edit subview pattern |
| 3.2.4 | DeleteConfirmationModal (WF-014: warning + Delete + Cancel) | normal | pending | AC-006.1, AC-006.2, AC-006.3, AC-006.4 | 7.6 | Features/Diary/Views/DeleteConfirmationModal.swift | Destructive button styling |
| 3.2.5 | DiaryEmptyState + OfflineBadge | normal | pending | AC-001.3, AC-002.3, AC-007.3, AC-007.4 | 7.1, 7.7 | Features/Diary/Views/DiaryEmptyState.swift, Features/Diary/Views/OfflineBadge.swift | Camera CTA; "Last updated X min ago" |
| 3.2.6 | DiaryView assembly (ProgressBar + list + Week toggle + pull-to-refresh + states) | normal | pending | AC-001.1, AC-001.2, AC-002.1, AC-002.4, AC-003.1, AC-007.2, AC-007.3 | 7.1, 7.2, 7.3, 7.7 | Features/Diary/Views/DiaryView.swift, App/RootView.swift | Replaces PlaceholderView("Diary") |
| 4.1.1 | DiaryCalculationService tests (color tier grid) | pbt | pending | AC-003.1, AC-003.2, AC-003.3, AC-003.4, AC-003.5 | 6 | calo-ai-testTests/DiaryCalculationServiceTests.swift | Boundary 1.0/1.1 |
| 4.1.2 | WeeklySummaryCalculator tests | pbt | pending | AC-002.1, AC-002.2, AC-002.3 | 6 | calo-ai-testTests/WeeklySummaryCalculatorTests.swift | 7 days always; Mon start |
| 4.1.3 | DiaryViewModel tests (fakes for DataClient, OfflineSyncing, AuthService) | pbt | pending | AC-001.1, AC-001.3, AC-001.4, AC-002.1, AC-002.3, AC-004.4, AC-005.3, AC-005.4, AC-006.2, AC-006.3, AC-006.4, AC-007.1, AC-007.2, AC-007.3, AC-007.4 | 6 | calo-ai-testTests/DiaryViewModelTests.swift | Empty/error/offline + refresh handoff |
| 4.1.4 | EditMealViewModel tests | pbt | pending | AC-005.1, AC-005.2, AC-005.3, AC-005.4, AC-005.5 | 6 | calo-ai-testTests/EditMealViewModelTests.swift | Save success/failure; cancel discards |
| 4.1.5 | ProgressBarColor pbt | pbt | pending | AC-003.2, AC-003.3, AC-003.4 | 6 | calo-ai-testTests/ProgressBarColorTests.swift | Ratio grid |
| 4.2.1 | Build + integration gate | normal | pending | AC-001.1, AC-007.1 | 6 | (build gate) | build_sim green; Diary tab wired; save from confirmation-edit refreshes |

## Dependency Matrix
| Task | Depends On | Can Parallel With |
|---|---|---|
| 2.1.1 | — | 2.1.2, 2.2.1, 2.2.2 |
| 2.1.2 | 2.1.1 | 2.2.1, 2.2.2 |
| 2.2.1 | 2.1.1, 2.1.2 | 2.2.2 |
| 2.2.2 | 2.1.1, 2.1.2 | 2.2.1 |
| 3.1.1 | 2.1.2, 2.2.1, 2.2.2 | 3.1.2, 3.2.1, 3.2.2, 3.2.3, 3.2.4, 3.2.5 |
| 3.1.2 | 2.1.2, 2.2.1 | 3.1.1, 3.2.1, 3.2.2, 3.2.3, 3.2.4, 3.2.5 |
| 3.2.1 | 3.1.1 | 3.2.2, 3.2.3, 3.2.4, 3.2.5 |
| 3.2.2 | 3.1.1 | 3.2.1, 3.2.3, 3.2.4, 3.2.5 |
| 3.2.3 | 3.1.2 | 3.2.1, 3.2.2, 3.2.4, 3.2.5 |
| 3.2.4 | 3.1.1 | 3.2.1, 3.2.2, 3.2.3, 3.2.5 |
| 3.2.5 | 3.1.1 | 3.2.1, 3.2.2, 3.2.3, 3.2.4 |
| 3.2.6 | 3.1.1, 3.1.2, 3.2.1, 3.2.2, 3.2.3, 3.2.4, 3.2.5 | — |
| 4.1.1 | 2.2.1 | 4.1.2, 4.1.3, 4.1.4, 4.1.5 |
| 4.1.2 | 2.2.2 | 4.1.1, 4.1.3, 4.1.4, 4.1.5 |
| 4.1.3 | 3.1.1 | 4.1.1, 4.1.2, 4.1.4, 4.1.5 |
| 4.1.4 | 3.1.2 | 4.1.1, 4.1.2, 4.1.3, 4.1.5 |
| 4.1.5 | 2.2.1 | 4.1.1, 4.1.2, 4.1.3, 4.1.4 |
| 4.2.1 | 3.2.6, 4.1.1, 4.1.2, 4.1.3, 4.1.4, 4.1.5 | — |

## 1. Shared Tasks
> Models + pure services the ViewModels depend on.

- [ ] **2.1.1** `ColorTier` enum (`.green / .amber / .red / .unknown`) + threshold mapping helper
  - Refs: AC-003.2, AC-003.3, AC-003.4
  - Design: 4
  - File: `Features/Diary/Models/ColorTier.swift`
- [ ] **2.1.2** `DiaryEntry` (date, meals, consumed, goal, remaining, ratio, tier) + `WeeklySummary` (weekStart, days[7], weeklyAverage, weeklyTotal) + `DailyTotal` (date, consumed, ratio, tier)
  - Refs: AC-001.1, AC-002.1, AC-002.2, AC-003.1
  - Design: 4
  - File: `Features/Diary/Models/DiaryEntry.swift`, `Features/Diary/Models/WeeklySummary.swift`
- [ ] **2.2.1** `DiaryCalculationService` — pure `dailyTotal(meals, goal)` and `tier(forRatio:)`; goal=0 ⇒ caller substitutes 2000 default
  - Refs: AC-003.1, AC-003.2, AC-003.3, AC-003.4, AC-003.5
  - Design: 7.3
  - File: `Features/Diary/Services/DiaryCalculationService.swift`
- [ ] **2.2.2** `WeeklySummaryCalculator` — pure `summarize(logs, weekStart, goal)`; Mon..Sun; empty days = 0; weekly average = total / 7
  - Refs: AC-002.1, AC-002.2, AC-002.3
  - Design: 7.2
  - File: `Features/Diary/Services/WeeklySummaryCalculator.swift`

**Phase Gate 2 (end of Shared phase):** Run XcodeBuildMCP `discover_projs -> list_schemes -> build_sim`, then traceability check (AC-001.1, AC-002.1, AC-002.2, AC-002.3, AC-003.1, AC-003.2, AC-003.3, AC-003.4, AC-003.5 covered; Refs Design resolve).

## 2. Feature Tasks
> ViewModels, sub-views, and Diary screen assembly.

- [ ] **3.1.1** `DiaryViewModel` — `@MainActor ObservableObject`; `viewMode: .daily / .week`; `state: DiaryState`; `loadToday()`, `loadWeek()`, `refresh()`, `applyExternalSave(meal)`, `commitEdit(updatedMeal)`, `commitDelete(id)`; published state; `OfflineBadge` integration
  - Refs: AC-001.1, AC-001.3, AC-001.4, AC-002.1, AC-002.3, AC-004.4, AC-005.3, AC-005.4, AC-006.2, AC-006.3, AC-006.4, AC-007.1, AC-007.2, AC-007.3, AC-007.4
  - Design: 7.1, 7.2, 7.6, 7.7
  - File: `Features/Diary/ViewModels/DiaryViewModel.swift`
- [ ] **3.1.2** `EditMealViewModel` — wraps meal; uses `MacroCalculationService` from `confirmation-edit`; `save()` → `DataClient.update`; cancel discards; error → recoverable
  - Refs: AC-005.1, AC-005.2, AC-005.3, AC-005.4, AC-005.5
  - Design: 7.4, 7.5
  - File: `Features/Diary/ViewModels/EditMealViewModel.swift`
- [ ] **3.2.1** `ProgressBar` hero zone wiring (consumer of `ColorTier` + `DiaryEntry.ratio`) in `DiaryView`
  - Refs: AC-003.1, AC-003.2, AC-003.3, AC-003.4, AC-003.5
  - Design: 7.3
  - File: `Features/Diary/Views/DiaryView.swift`
- [ ] **3.2.2** `MealListItem` — row with name, calories, time + `.swipeActions(edge: .trailing)` (Edit, Delete); reveal <200ms
  - Refs: AC-004.1, AC-004.2, AC-004.3, AC-004.4
  - Design: 7.4
  - File: `Features/Diary/Views/MealListItem.swift`
- [ ] **3.2.3** `EditMealModal` (WF-013) — form (ingredient list, portion, macro editor) + Save/Cancel/Delete
  - Refs: AC-005.1, AC-005.2, AC-005.3, AC-005.4, AC-005.5
  - Design: 7.5
  - File: `Features/Diary/Views/EditMealModal.swift`
- [ ] **3.2.4** `DeleteConfirmationModal` (WF-014) — warning text + Cancel + Delete (destructive red)
  - Refs: AC-006.1, AC-006.2, AC-006.3, AC-006.4
  - Design: 7.6
  - File: `Features/Diary/Views/DeleteConfirmationModal.swift`
- [ ] **3.2.5** `DiaryEmptyState` ("No meals logged yet" + Camera CTA) + `OfflineBadge` ("Last updated X min ago")
  - Refs: AC-001.3, AC-002.3, AC-007.3, AC-007.4
  - Design: 7.1, 7.7
  - File: `Features/Diary/Views/DiaryEmptyState.swift`, `Features/Diary/Views/OfflineBadge.swift`
- [ ] **3.2.6** Assemble `DiaryView` (ProgressBar + list + Week toggle + pull-to-refresh + states); wire `EditMealModal` + `DeleteConfirmationModal`; wire `confirmation-edit.onSaveSuccess(meal)` → `DiaryViewModel.applyExternalSave(_:)`; replace `PlaceholderView("Diary")` in `RootView`
  - Refs: AC-001.1, AC-001.2, AC-002.1, AC-002.4, AC-003.1, AC-007.2, AC-007.3
  - Design: 7.1, 7.2, 7.3, 7.7
  - File: `Features/Diary/Views/DiaryView.swift`, `App/RootView.swift`

**Phase Gate 3 (end of Feature phase):** Run XcodeBuildMCP `discover_projs -> list_schemes -> build_sim`, then traceability check (AC-001.*, AC-002.*, AC-003.*, AC-004.*, AC-005.*, AC-006.*, AC-007.* covered; Refs Design resolve; Diary tab wired).

## 3. Integration Tasks
> Unit/property tests + build/integration gate.

- [ ] **4.1.1** `DiaryCalculationServiceTests` — daily total; remaining; tier grid at ratio ∈ {0, 0.5, 0.99, 1.0, 1.01, 1.1, 1.11, 2.0}; goal=0 fallback
  - Refs: AC-003.1, AC-003.2, AC-003.3, AC-003.4, AC-003.5
  - Design: 6
  - File: `calo-ai-testTests/DiaryCalculationServiceTests.swift`
- [ ] **4.1.2** `WeeklySummaryCalculatorTests` — 7 rows always; Mon start; empty days = 0; weekly average
  - Refs: AC-002.1, AC-002.2, AC-002.3
  - Design: 6
  - File: `calo-ai-testTests/WeeklySummaryCalculatorTests.swift`
- [ ] **4.1.3** `DiaryViewModelTests` (fakes for `DataClient`, `OfflineSyncing`, `AuthService`) — daily success/empty/failure; week toggle; refresh; `applyExternalSave`; commitEdit/Delete; offline badge
  - Refs: AC-001.1, AC-001.3, AC-001.4, AC-002.1, AC-002.3, AC-004.4, AC-005.3, AC-005.4, AC-006.2, AC-006.3, AC-006.4, AC-007.1, AC-007.2, AC-007.3, AC-007.4
  - Design: 6
  - File: `calo-ai-testTests/DiaryViewModelTests.swift`
- [ ] **4.1.4** `EditMealViewModelTests` — load pre-populates; mutate recalcs; validation gates; save success/failure; cancel discards
  - Refs: AC-005.1, AC-005.2, AC-005.3, AC-005.4, AC-005.5
  - Design: 6
  - File: `calo-ai-testTests/EditMealViewModelTests.swift`
- [ ] **4.1.5** `ProgressBarColorTests` — pbt over ratio grid
  - Refs: AC-003.2, AC-003.3, AC-003.4
  - Design: 6
  - File: `calo-ai-testTests/ProgressBarColorTests.swift`
- [ ] **4.2.1** Build + integration gate: `build_sim` green; Diary tab renders; save from `confirmation-edit` refreshes Diary; swipe Edit/Delete work end-to-end
  - Refs: AC-001.1, AC-007.1
  - Design: 6
  - File: (build gate)

**Phase Gate 4 (end of Integration phase):** Run XcodeBuildMCP `discover_projs -> list_schemes -> build_sim` (+ `test_sim`), then traceability check (all 30 ACs traced to ≥1 done task; every Refs Design resolves; P1–P15 covered by tests).

## Traceability Matrix
| Task ID | AC | Design | Property | Status |
|---|---|---|---|---|
| 2.1.1 | AC-003.2, AC-003.3, AC-003.4 | 4 | P2 | pending |
| 2.1.2 | AC-001.1, AC-002.1, AC-002.2, AC-003.1 | 4 | P1, P3, P4 | pending |
| 2.2.1 | AC-003.1, AC-003.2, AC-003.3, AC-003.4, AC-003.5 | 7.3 | P1, P2 | pending |
| 2.2.2 | AC-002.1, AC-002.2, AC-002.3 | 7.2 | P3, P4 | pending |
| 3.1.1 | AC-001.1, AC-001.3, AC-001.4, AC-002.1, AC-002.3, AC-004.4, AC-005.3, AC-005.4, AC-006.2, AC-006.3, AC-006.4, AC-007.1, AC-007.2, AC-007.3, AC-007.4 | 7.1, 7.2, 7.6, 7.7 | P5, P6, P7, P9, P10, P12, P13, P14, P15 | pending |
| 3.1.2 | AC-005.1, AC-005.2, AC-005.3, AC-005.4, AC-005.5 | 7.4, 7.5 | P10, P11 | pending |
| 3.2.1 | AC-003.1, AC-003.2, AC-003.3, AC-003.4, AC-003.5 | 7.3 | P1, P2 | pending |
| 3.2.2 | AC-004.1, AC-004.2, AC-004.3, AC-004.4 | 7.4 | P8, P9 | pending |
| 3.2.3 | AC-005.1, AC-005.2, AC-005.3, AC-005.4, AC-005.5 | 7.5 | P10, P11 | pending |
| 3.2.4 | AC-006.1, AC-006.2, AC-006.3, AC-006.4 | 7.6 | P12 | pending |
| 3.2.5 | AC-001.3, AC-002.3, AC-007.3, AC-007.4 | 7.1, 7.7 | P5, P14 | pending |
| 3.2.6 | AC-001.1, AC-001.2, AC-002.1, AC-002.4, AC-003.1, AC-007.2, AC-007.3 | 7.1, 7.2, 7.3, 7.7 | P5, P6, P7, P13, P14, P15 | pending |
| 4.1.1 | AC-003.1, AC-003.2, AC-003.3, AC-003.4, AC-003.5 | 6 | P1, P2 | pending |
| 4.1.2 | AC-002.1, AC-002.2, AC-002.3 | 6 | P3, P4 | pending |
| 4.1.3 | AC-001.1, AC-001.3, AC-001.4, AC-002.1, AC-002.3, AC-004.4, AC-005.3, AC-005.4, AC-006.2, AC-006.3, AC-006.4, AC-007.1, AC-007.2, AC-007.3, AC-007.4 | 6 | P5, P6, P7, P9, P10, P12, P13, P14, P15 | pending |
| 4.1.4 | AC-005.1, AC-005.2, AC-005.3, AC-005.4, AC-005.5 | 6 | P10, P11 | pending |
| 4.1.5 | AC-003.2, AC-003.3, AC-003.4 | 6 | P2 | pending |
| 4.2.1 | AC-001.1, AC-007.1 | 6 | P5, P13 | pending |

## Progress
| Section | Total | Done | Status |
|---|---:|---:|---|
| Shared | 4 | 0 | ⬜ |
| Feature | 8 | 0 | ⬜ |
| Integration | 6 | 0 | ⬜ |
