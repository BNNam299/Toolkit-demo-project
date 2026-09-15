# confirmation-edit - Implementation Plan

## Execution Mode
- Mode: manual
- Policy: run sequentially by default (logic-first from design.md)
- Gate: stop on phase boundary or blocking error

## Task Registry (Machine Readable)

| ID | Title | Type | Status | Refs AC | Refs Design | Files | Checkpoint |
|---|---|---|---|---|---|---|---|
| 2.1.1 | Portion enum + extend Ingredient with portion/isSelected/isCustom/manualOverrideMacros | normal | pending | AC-002.1, AC-002.2, AC-004.2, AC-004.5, AC-005.2 | 4 | Features/Confirmation/Models/Portion.swift, Features/Confirmation/Models/Ingredient+Confirmation.swift | Multipliers 0.75/1.0/1.25 + grams branch |
| 2.1.2 | ConfirmationDraft + MealDraft (matches ai-recognition hand-off) | normal | pending | AC-001.1, AC-001.3, AC-001.4 | 4 | Features/Confirmation/Models/ConfirmationDraft.swift, Features/Confirmation/Models/MealDraft.swift | Required-field validation |
| 2.2.1 | MacroCalculationService (pure recalc + portion multipliers + manual override formula) | normal | pending | AC-004.2, AC-005.2, AC-005.3, AC-006.1 | 7.6 | Features/Confirmation/Services/MacroCalculationService.swift | <200ms; zero-macro rejected |
| 2.2.2 | IngredientSearchService (local JSON DB, ≤5 results, ≤500ms) | normal | pending | AC-003.2, AC-003.4, AC-003.5 | 7.3 | Features/Confirmation/Services/IngredientSearchService.swift | Debounce + bound |
| 3.1.1 | ConfirmationViewModel (load/toggle/remove/portion/macro/add/save) | normal | pending | AC-001.1, AC-001.4, AC-002.1, AC-002.2, AC-002.3, AC-002.4, AC-002.5, AC-003.3, AC-003.4, AC-004.1, AC-004.2, AC-004.3, AC-004.4, AC-004.5, AC-005.1, AC-005.2, AC-005.3, AC-005.4, AC-006.1, AC-006.2, AC-006.3, AC-007.1, AC-007.3, AC-007.4, AC-007.5 | 7.1, 7.2, 7.5, 7.6, 7.7 | Features/Confirmation/ViewModels/ConfirmationViewModel.swift | State machine + callbacks |
| 3.2.1 | AddIngredientModalViewModel (search + suggestions + custom path) | normal | pending | AC-003.1, AC-003.2, AC-003.3, AC-003.4, AC-003.5 | 7.3 | Features/Confirmation/ViewModels/AddIngredientModalViewModel.swift | Debounced search; ≥2-char guard |
| 3.3.1 | IngredientRow (checkbox + PortionSelector + swipe-delete) | normal | pending | AC-002.1, AC-002.3, AC-002.4, AC-004.1 | 7.2 | Features/Confirmation/Views/IngredientRow.swift | Swipe delete; last-item guard |
| 3.3.2 | PortionSelector (segmented + "Enter grams" sheet) | normal | pending | AC-004.1, AC-004.2, AC-004.3, AC-004.4, AC-004.5 | 7.4 | Features/Confirmation/Views/PortionSelector.swift | Grams 10..500 validation |
| 3.3.3 | MacroBar (inline P/C/F + total label) | normal | pending | AC-001.1, AC-006.1, AC-006.2 | 7.6 | Features/Confirmation/Views/MacroBar.swift | Spring fill animation |
| 3.3.4 | MacroEditor (3 numeric fields + Reset) | normal | pending | AC-005.1, AC-005.2, AC-005.3, AC-005.4 | 7.5 | Features/Confirmation/Views/MacroEditor.swift | All-zero rejection |
| 3.3.5 | AddIngredientModal (search + suggestions + "Add as custom") | normal | pending | AC-003.1, AC-003.2, AC-003.3, AC-003.4, AC-003.5 | 7.3 | Features/Confirmation/Views/AddIngredientModal.swift | Modal sheet; keyboard focus |
| 3.3.6 | ConfirmationView assembly + warning banner + save/retry toolbar | normal | pending | AC-001.1, AC-001.2, AC-001.3, AC-007.1, AC-007.2 | 7.1, 7.7 | Features/Confirmation/Views/ConfirmationView.swift, App/RootView.swift | Replaces PlaceholderView("Confirmation") |
| 4.1.1 | MacroCalculationService tests | pbt | pending | AC-004.2, AC-005.2, AC-005.3, AC-005.4 | 6 | calo-ai-testTests/MacroCalculationServiceTests.swift | Portion multipliers + override formula |
| 4.1.2 | ConfirmationViewModel tests (fakes for DataClient, ScanQuotaServicing, IngredientSearchService) | pbt | pending | AC-001.4, AC-002.1, AC-002.2, AC-002.3, AC-002.4, AC-002.5, AC-003.3, AC-003.4, AC-004.1, AC-004.2, AC-004.4, AC-005.1, AC-005.2, AC-005.3, AC-006.1, AC-006.3, AC-007.1, AC-007.3, AC-007.4, AC-007.5 | 6 | calo-ai-testTests/ConfirmationViewModelTests.swift | Save+increment idempotency; validation guards |
| 4.1.3 | IngredientSearchService tests | pbt | pending | AC-003.2, AC-003.4, AC-003.5 | 6 | calo-ai-testTests/IngredientSearchServiceTests.swift | ≤5 results; ≥2-char guard; <500ms |
| 4.1.4 | PortionValidation tests | pbt | pending | AC-004.3, AC-004.4 | 6 | calo-ai-testTests/PortionValidationTests.swift | Grams 10..500; custom kcal 0..2000 |
| 4.2.1 | Build + integration gate | normal | pending | AC-001.1, AC-007.1, AC-007.2 | 6 | (build gate) | build_sim green; Save→Diary handoff works |

## Dependency Matrix
| Task | Depends On | Can Parallel With |
|---|---|---|
| 2.1.1 | — | 2.1.2, 2.2.1, 2.2.2 |
| 2.1.2 | — | 2.1.1, 2.2.1, 2.2.2 |
| 2.2.1 | 2.1.1, 2.1.2 | 2.2.2 |
| 2.2.2 | 2.1.2 | 2.2.1 |
| 3.1.1 | 2.1.1, 2.1.2, 2.2.1, 2.2.2 | 3.2.1 |
| 3.2.1 | 2.2.2 | 3.1.1, 3.3.5 |
| 3.3.1 | 2.1.1, 2.1.2, 3.1.1 | 3.3.2, 3.3.3, 3.3.4 |
| 3.3.2 | 2.1.1, 3.1.1 | 3.3.1, 3.3.3, 3.3.4 |
| 3.3.3 | 3.1.1 | 3.3.1, 3.3.2, 3.3.4 |
| 3.3.4 | 3.1.1 | 3.3.1, 3.3.2, 3.3.3 |
| 3.3.5 | 3.2.1 | 3.3.1, 3.3.2, 3.3.3, 3.3.4 |
| 3.3.6 | 3.1.1, 3.3.1, 3.3.2, 3.3.3, 3.3.4, 3.3.5 | — |
| 4.1.1 | 2.2.1 | 4.1.2, 4.1.3, 4.1.4 |
| 4.1.2 | 3.1.1 | 4.1.1, 4.1.3, 4.1.4 |
| 4.1.3 | 2.2.2 | 4.1.1, 4.1.2, 4.1.4 |
| 4.1.4 | 2.1.1 | 4.1.1, 4.1.2, 4.1.3 |
| 4.2.1 | 3.3.6, 4.1.1, 4.1.2, 4.1.3, 4.1.4 | — |

## 1. Shared Tasks
> Models + pure services the ViewModel depends on.

- [ ] **2.1.1** `Portion` enum (small=0.75, medium=1.0, large=1.25, grams(Double)) + extend `Ingredient` with `portion`, `isSelected` (default `true`), `isCustom`, `manualOverrideMacros`
  - Refs: AC-002.1, AC-002.2, AC-004.2, AC-004.5, AC-005.2
  - Design: 4
  - File: `Features/Confirmation/Models/Portion.swift`, `Features/Confirmation/Models/Ingredient+Confirmation.swift`
- [ ] **2.1.2** `MealDraft` (matches `ai-recognition` hand-off: mealName, totalCalories, macros, ingredients[], confidence, imageRef?) + `ConfirmationDraft` wrapper with `manualMacros: Macros?` + missing-field validator
  - Refs: AC-001.1, AC-001.3, AC-001.4
  - Design: 4
  - File: `Features/Confirmation/Models/MealDraft.swift`, `Features/Confirmation/Models/ConfirmationDraft.swift`
- [ ] **2.2.1** `MacroCalculationService` — pure `recalculate(ingredients:) -> (cal, P, C, F)`; portion multipliers; grams conversion; manual-override formula `(P×4)+(C×4)+(F×9)`; reject all-zero
  - Refs: AC-004.2, AC-005.2, AC-005.3, AC-006.1
  - Design: 7.6
  - File: `Features/Confirmation/Services/MacroCalculationService.swift`
- [ ] **2.2.2** `IngredientSearchService` (protocol) + impl over bundled JSON; `search(query)` returns ≤5 results, debounce 250ms, ≤500ms
  - Refs: AC-003.2, AC-003.4, AC-003.5
  - Design: 7.3
  - File: `Features/Confirmation/Services/IngredientSearchService.swift`

**Phase Gate 2 (end of Shared phase):** Run XcodeBuildMCP `discover_projs -> list_schemes -> build_sim`, then traceability check (AC-001.4, AC-002.1, AC-002.2, AC-003.2, AC-003.4, AC-003.5, AC-004.2, AC-004.5, AC-005.2, AC-006.1 covered; Refs Design resolve).

## 2. Feature Tasks
> ViewModels, sub-views, and Confirmation screen assembly.

- [ ] **3.1.1** `ConfirmationViewModel` — `@MainActor ObservableObject`; `load(draft:)`; `toggle(id:)`; `remove(id:)`; `setPortion(id:, portion:)`; `setManualMacros(P:C:F:)`; `addSuggestion`; `addCustom(name:)`; `save()`; published `state`; callbacks `onSaveSuccess(MealLog)`, `onRetryPhoto`; validation gates; `DataClient.insert` + `ScanQuotaService.increment()` on success
  - Refs: AC-001.1, AC-001.4, AC-002.1, AC-002.2, AC-002.3, AC-002.4, AC-002.5, AC-003.3, AC-003.4, AC-004.1, AC-004.2, AC-004.3, AC-004.4, AC-004.5, AC-005.1, AC-005.2, AC-005.3, AC-005.4, AC-006.1, AC-006.2, AC-006.3, AC-007.1, AC-007.3, AC-007.4, AC-007.5
  - Design: 7.1, 7.2, 7.5, 7.6, 7.7
  - File: `Features/Confirmation/ViewModels/ConfirmationViewModel.swift`
- [ ] **3.2.1** `AddIngredientModalViewModel` — debounced search call to `IngredientSearchService`; ≥2-char guard; expose `suggestions`, `showCustomOption`; on select → `ConfirmationViewModel.addSuggestion`
  - Refs: AC-003.1, AC-003.2, AC-003.3, AC-003.4, AC-003.5
  - Design: 7.3
  - File: `Features/Confirmation/ViewModels/AddIngredientModalViewModel.swift`
- [ ] **3.3.1** `IngredientRow` — checkbox + name + `PortionSelector` + per-row calo; SwiftUI `.swipeActions` for delete; last-ingredient guard surfaces inline
  - Refs: AC-002.1, AC-002.3, AC-002.4, AC-004.1
  - Design: 7.2
  - File: `Features/Confirmation/Views/IngredientRow.swift`
- [ ] **3.3.2** `PortionSelector` — segmented small/medium/large + "Enter grams" sheet; grams input 10..500; invalid inline
  - Refs: AC-004.1, AC-004.2, AC-004.3, AC-004.4, AC-004.5
  - Design: 7.4
  - File: `Features/Confirmation/Views/PortionSelector.swift`
- [ ] **3.3.3** `MacroBar` — inline P/C/F with total label; spring animation on fill
  - Refs: AC-001.1, AC-006.1, AC-006.2
  - Design: 7.6
  - File: `Features/Confirmation/Views/MacroBar.swift`
- [ ] **3.3.4** `MacroEditor` — 3 numeric fields pre-filled with AI estimate + "Reset to AI estimate" link; all-zero rejected
  - Refs: AC-005.1, AC-005.2, AC-005.3, AC-005.4
  - Design: 7.5
  - File: `Features/Confirmation/Views/MacroEditor.swift`
- [ ] **3.3.5** `AddIngredientModal` — sheet hosting search field + suggestion list + "Add as custom" affordance; a11y labels
  - Refs: AC-003.1, AC-003.2, AC-003.3, AC-003.4, AC-003.5
  - Design: 7.3
  - File: `Features/Confirmation/Views/AddIngredientModal.swift`
- [ ] **3.3.6** Assemble `ConfirmationView` (hero + warning banner + `MacroBar` + list + Save/Retry toolbar); wire `AddIngredientModal`; replace `PlaceholderView("Confirmation")` in `RootView`; inject `onSaveSuccess(MealLog)` → `DiaryView` (from `diary-logging`); inject `onRetryPhoto` → `CameraView`
  - Refs: AC-001.1, AC-001.2, AC-001.3, AC-007.1, AC-007.2
  - Design: 7.1, 7.7
  - File: `Features/Confirmation/Views/ConfirmationView.swift`, `App/RootView.swift`

**Phase Gate 3 (end of Feature phase):** Run XcodeBuildMCP `discover_projs -> list_schemes -> build_sim`, then traceability check (AC-001.*, AC-002.*, AC-003.*, AC-004.*, AC-005.*, AC-006.*, AC-007.* covered; Refs Design resolve; Confirmation tab wired).

## 3. Integration Tasks
> Unit/property tests + build/integration gate.

- [ ] **4.1.1** `MacroCalculationServiceTests` — portion multipliers (small/medium/large), grams conversion in [10,500], manual override formula, all-zero rejection
  - Refs: AC-004.2, AC-005.2, AC-005.3, AC-005.4
  - Design: 6
  - File: `calo-ai-testTests/MacroCalculationServiceTests.swift`
- [ ] **4.1.2** `ConfirmationViewModelTests` (fakes for `DataClient`, `ScanQuotaServicing`, `IngredientSearchService`) — load+validate; toggle/remove/portion/macro mutate draft; 0-selected + total=0 blocks save; save success → `increment()` exactly once; save failure → no increment; retry after failure → exactly one increment on first success
  - Refs: AC-001.4, AC-002.1, AC-002.2, AC-002.3, AC-002.4, AC-002.5, AC-003.3, AC-003.4, AC-004.1, AC-004.2, AC-004.4, AC-005.1, AC-005.2, AC-005.3, AC-006.1, AC-006.3, AC-007.1, AC-007.3, AC-007.4, AC-007.5
  - Design: 6
  - File: `calo-ai-testTests/ConfirmationViewModelTests.swift`
- [ ] **4.1.3** `IngredientSearchServiceTests` — empty query → no results; ≥2 chars → ≤5 results; missing match → empty + custom path; latency ≤500ms
  - Refs: AC-003.2, AC-003.4, AC-003.5
  - Design: 6
  - File: `calo-ai-testTests/IngredientSearchServiceTests.swift`
- [ ] **4.1.4** `PortionValidationTests` — grams in [10,500]; custom kcal in [0,2000]
  - Refs: AC-004.3, AC-004.4
  - Design: 6
  - File: `calo-ai-testTests/PortionValidationTests.swift`
- [ ] **4.2.1** Build + integration gate: `build_sim` green; Save→Diary handoff wired; `ScanQuotaService.increment()` invoked exactly once on success
  - Refs: AC-001.1, AC-007.1, AC-007.2
  - Design: 6
  - File: (build gate)

**Phase Gate 4 (end of Integration phase):** Run XcodeBuildMCP `discover_projs -> list_schemes -> build_sim` (+ `test_sim`), then traceability check (all 31 ACs traced to ≥1 done task; every Refs Design resolves; P1–P13 covered by tests).

## Traceability Matrix
| Task ID | AC | Design | Property | Status |
|---|---|---|---|---|
| 2.1.1 | AC-002.1, AC-002.2, AC-004.2, AC-004.5, AC-005.2 | 4 | P3, P7 | pending |
| 2.1.2 | AC-001.1, AC-001.3, AC-001.4 | 4 | P1, P2 | pending |
| 2.2.1 | AC-004.2, AC-005.2, AC-005.3, AC-006.1 | 7.6 | P3, P7, P8 | pending |
| 2.2.2 | AC-003.2, AC-003.4, AC-003.5 | 7.3 | P13 | pending |
| 3.1.1 | AC-001.1, AC-001.4, AC-002.1, AC-002.2, AC-002.3, AC-002.4, AC-002.5, AC-003.3, AC-003.4, AC-004.1, AC-004.2, AC-004.3, AC-004.4, AC-004.5, AC-005.1, AC-005.2, AC-005.3, AC-005.4, AC-006.1, AC-006.2, AC-006.3, AC-007.1, AC-007.3, AC-007.4, AC-007.5 | 7.1, 7.2, 7.5, 7.6, 7.7 | P1, P2, P3, P4, P5, P7, P8, P9, P10, P11, P12 | pending |
| 3.2.1 | AC-003.1, AC-003.2, AC-003.3, AC-003.4, AC-003.5 | 7.3 | P5, P6, P13 | pending |
| 3.3.1 | AC-002.1, AC-002.3, AC-002.4, AC-004.1 | 7.2 | P3, P4 | pending |
| 3.3.2 | AC-004.1, AC-004.2, AC-004.3, AC-004.4, AC-004.5 | 7.4 | P6, P7 | pending |
| 3.3.3 | AC-001.1, AC-006.1, AC-006.2 | 7.6 | P1 | pending |
| 3.3.4 | AC-005.1, AC-005.2, AC-005.3, AC-005.4 | 7.5 | P8 | pending |
| 3.3.5 | AC-003.1, AC-003.2, AC-003.3, AC-003.4, AC-003.5 | 7.3 | P5, P6, P13 | pending |
| 3.3.6 | AC-001.1, AC-001.2, AC-001.3, AC-007.1, AC-007.2 | 7.1, 7.7 | P10, P12 | pending |
| 4.1.1 | AC-004.2, AC-005.2, AC-005.3, AC-005.4 | 6 | P3, P7, P8 | pending |
| 4.1.2 | AC-001.4, AC-002.1, AC-002.2, AC-002.3, AC-002.4, AC-002.5, AC-003.3, AC-003.4, AC-004.1, AC-004.2, AC-004.4, AC-005.1, AC-005.2, AC-005.3, AC-006.1, AC-006.3, AC-007.1, AC-007.3, AC-007.4, AC-007.5 | 6 | P1, P2, P3, P4, P5, P7, P8, P9, P10, P11, P12 | pending |
| 4.1.3 | AC-003.2, AC-003.4, AC-003.5 | 6 | P13 | pending |
| 4.1.4 | AC-004.3, AC-004.4 | 6 | P6, P7 | pending |
| 4.2.1 | AC-001.1, AC-007.1, AC-007.2 | 6 | P1, P9, P10 | pending |

## Progress
| Section | Total | Done | Status |
|---|---:|---:|---|
| Shared | 4 | 0 | ⬜ |
| Feature | 8 | 0 | ⬜ |
| Integration | 5 | 0 | ⬜ |
