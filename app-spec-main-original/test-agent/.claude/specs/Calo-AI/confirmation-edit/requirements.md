# confirmation-edit - Requirements

## Overview
`confirmation-edit` là spec thứ ba của core loop (Phase 4), nhận `MealDraft` (kết quả AI gồm tên món, calo, macros, danh sách nguyên liệu, confidence) từ `ai-recognition` và dựng màn hình Confirmation (WF-003) cùng modal Add Ingredient (WF-012). User xác nhận từng nguyên liệu (toggle add/remove), điều chỉnh khẩu phần (small/medium/large hoặc grams), chỉnh macro thủ công, thêm nguyên liệu mới qua autocomplete, và lưu meal log — tổng calo/macros phải recalc real-time (<200ms) và save phải kích hoạt `ScanQuotaService.increment()` (handoff AC-003.5 từ `camera-capture`). Spec dùng lại `shared-foundations` (MealLog, Ingredient, AppError, ErrorHandler, DataClient, AppEnvironment) và `camera-capture` (ScanQuotaService). KHÔNG bao gồm loading AI (ai-recognition) hay diary (diary-logging).

## Evidence References
- **Market data from PRD:** Sai số AI (dầu/nước sốt/nguyên liệu ẩn) là phàn nàn phổ nào ở mọi app AI-photo (PRD §4); chính vì vậy bước confirmation bắt buộc — KPI `scan_manual_override` (PRD §12) sẽ đo tỷ lệ user sửa. PRD §9 yêu cầu core loop <10s nên recalc <200ms và modal autocomplete <500ms là critical-path.
- **Source documents:**
  - `.claude/specs/Calo-AI/Functional_Requirements.md` — FR-003 (AI return draft + AC-003.1/.2/.3, BR-003.2/.3/.4), FR-004 (Confirm & save + BR-004.1/.2/.3/.4, VR-004.1/.2, ERR-004.1/.2/.3, AC-004.1..4), FR-005 (Add ingredient + BR-005.1/.2/.3, VR-005.1/.2, ERR-005.1/.2/.3, AC-005.1..5), FR-006 (Adjust portion + BR-006.1/.2/.3, VR-006.1/.2, ERR-006.1/.2, AC-006.1..5), FR-007 (Edit macros + BR-007.1/.2, VR-007.1/.2, ERR-007.1/.2, AC-007.1..3), FR-008 (Remove ingredient + BR-008.1/.2, VR-008.1, ERR-008.1, AC-008.1..3)
  - `.claude/specs/Calo-AI/Wireframes.md` — WF-003 (Confirmation), WF-012 (Add Ingredient Modal)
  - `.claude/specs/Calo-AI/Use_Cases.md` — UC-003 (Xem kết quả AI), UC-004 (Xác nhận nguyên liệu), UC-005 (Thêm nguyên liệu), UC-006 (Điều chỉnh khẩu phần), UC-007 (Điều chỉnh macro), UC-008 (Xoá nguyên liệu)
  - `.claude/specs/Calo-AI/PRD.md` §9 (core loop <10s), §12 (`scan_manual_override` KPI)
  - `.claude/specs/Calo-AI/camera-capture/requirements.md` — AC-003.5 (ScanQuotaService.increment() called by save flow, not capture)
- **Key KPIs / measurable targets:** Macro recalculation <200ms (FR-006 AC-006.2 / NFR-002 implication); autocomplete suggestions <500ms (FR-005 AC-005.2); save-to-Diary end-to-end <2s (BR-004 implication); `scan_manual_override` measured per save (PRD §12).

## Requirements

### Requirement 1 (REQ-001): Display AI Result as Editable Meal Draft
**User Story:** As a user coming from AI recognition, I want to see the AI's proposed dish, calories, macros and ingredients in an editable list, so that I can verify and adjust before saving.
**Source:** FR-003, UC-003, WF-003, NFR-002

#### Acceptance Criteria
1. AC-001.1: WHEN a `MealDraft` is received from `ai-recognition` (success callback) THEN THE SYSTEM SHALL present the Confirmation screen (WF-003) with meal name, total calories (large), macro breakdown (P/C/F), and the ingredient list rendered with checkboxes all checked by default.
2. AC-001.2: WHEN confidence < 70% THEN THE SYSTEM SHALL display a yellow warning banner "Not confident — please verify" with a "Retry photo" secondary action, AND still allow the user to proceed.
3. AC-001.3: WHEN the ingredient list is rendered THEN THE SYSTEM SHALL show each ingredient with name, portion label (default medium), and per-ingredient calories.
4. AC-001.4: IF the `MealDraft` payload is missing a required field (name, calories, ingredients) THEN THE SYSTEM SHALL reject the hand-off and surface a recoverable error via the shared `ErrorHandler`, NOT render a partial screen.

### Requirement 2 (REQ-002): Toggle Ingredient Selection
**User Story:** As a user, I want to uncheck ingredients the AI got wrong (e.g. a sauce I didn't actually have), so that my log reflects what I actually ate.
**Source:** FR-004, UC-004, FR-008, UC-008, WF-003

#### Acceptance Criteria
1. AC-002.1: WHEN the user taps an ingredient checkbox THEN THE SYSTEM SHALL toggle the ingredient's `isSelected` flag and recalculate the displayed total calories and macros in <200ms.
2. AC-002.2: WHILE at least one ingredient remains selected THE SYSTEM SHALL keep the "Confirm & Save" button enabled.
3. AC-002.3: WHEN the user swipes-left on an ingredient row and taps "Delete" THEN THE SYSTEM SHALL remove the ingredient from the list and recalculate totals in <200ms.
4. AC-002.4: IF the user attempts to remove the last remaining ingredient THEN THE SYSTEM SHALL prevent removal and display a non-blocking warning "At least one ingredient required".
5. AC-002.5: WHEN the user changes selection THEN THE SYSTEM SHALL persist the change in the in-memory draft only (not yet written to disk/Supabase) until "Confirm & Save" is tapped.

### Requirement 3 (REQ-003): Add Ingredient Manually via Modal
**User Story:** As a user, I want to add an ingredient the AI missed (e.g. olive oil, a sauce) by typing its name and selecting from autocomplete, so that my log is complete.
**Source:** FR-005, UC-005, WF-012

#### Acceptance Criteria
1. AC-003.1: WHEN the user taps "+ Add ingredient" THEN THE SYSTEM SHALL open the Add Ingredient modal (WF-012) with a text input focused and a placeholder "e.g., olive oil, rice".
2. AC-003.2: WHEN the user types into the input THEN THE SYSTEM SHALL show up to 5 autocomplete suggestions from the local ingredient database within 500ms.
3. AC-003.3: WHEN the user taps a suggestion THEN THE SYSTEM SHALL add the ingredient to the list at default portion `medium` (1.0×), default checkbox unchecked, and recalculate totals in <200ms.
4. AC-003.4: IF the user types a name with no database match THEN THE SYSTEM SHALL show an "Add as custom" option that, when tapped, adds an ingredient with 0 kcal (per BR-005.2) and unchecked checkbox.
5. AC-003.5: IF the input is empty (length < 2) THEN THE SYSTEM SHALL disable the Add button and show the validation message "Enter at least 2 characters".

### Requirement 4 (REQ-004): Adjust Portion Size
**User Story:** As a user, I want to change the portion of an ingredient (small / medium / large, or grams) so the calories match what I actually ate.
**Source:** FR-006, UC-006, WF-003

#### Acceptance Criteria
1. AC-004.1: WHEN the user taps the portion selector for an ingredient THEN THE SYSTEM SHALL present options small (0.75×) / medium (1.0×) / large (1.25×) AND an "Enter grams" secondary option.
2. AC-004.2: WHEN the user selects small/medium/large THEN THE SYSTEM SHALL apply the multiplier, recompute the ingredient's calo/macros via `MacroCalculationService`, and update the total within 200ms.
3. AC-004.3: WHEN the user selects "Enter grams" and submits a number in [10, 500] THEN THE SYSTEM SHALL look up the food's calorie density from the local ingredient database, compute the calories, and update the total.
4. AC-004.4: IF the user submits grams outside [10, 500] THEN THE SYSTEM SHALL reject the input and show the message "Enter weight between 10 and 500 grams".
5. AC-004.5: WHILE portion changes are made THEN THE SYSTEM SHALL persist the latest portion per ingredient in the in-memory draft, regardless of how many times the user adjusts.

### Requirement 5 (REQ-005): Edit Macros Manually
**User Story:** As a user, I want to override the AI's macro estimates (P/C/F in grams), so that my log is accurate when I know the real numbers (e.g. from a nutrition label).
**Source:** FR-007, UC-007, WF-003

#### Acceptance Criteria
1. AC-005.1: WHEN the user taps the macro edit (pencil) icon THEN THE SYSTEM SHALL reveal three numeric input fields for Protein, Carbs and Fat (grams) pre-filled with the AI estimate.
2. AC-005.2: WHEN any of P/C/F is edited THEN THE SYSTEM SHALL recalculate total calories as `(P×4) + (C×4) + (F×9)` and update the total display in <200ms.
3. AC-005.3: IF the user submits values where all three macros are 0 THEN THE SYSTEM SHALL block the change, show the message "At least one macro must be > 0", and revert to the prior values.
4. AC-005.4: WHEN the user taps "Reset to AI estimate" THEN THE SYSTEM SHALL restore P/C/F to the AI-provided values and recalculate total calories.

### Requirement 6 (REQ-006): Real-Time Total Recalculation
**User Story:** As a user adjusting portions, toggling, or adding ingredients, I want the total calories and macros at the top of the screen to update immediately, so that I see the impact of each change without tapping a confirm button.
**Source:** FR-006 (AC-006.2/.3), FR-004 (AC-004.2), UC-004, UC-006, UC-007, UC-008

#### Acceptance Criteria
1. AC-006.1: WHILE the user mutates the draft (toggle, add, remove, portion, manual macros) THEN THE SYSTEM SHALL recompute total calories and P/C/F via `MacroCalculationService` in <200ms per mutation.
2. AC-006.2: WHEN totals are recomputed THEN THE SYSTEM SHALL update the "total calories" header and the macro breakdown bar without rebuilding the ingredient list.
3. AC-006.3: IF the recomputation produces a total of 0 kcal (e.g. only unchecked custom ingredients) THEN THE SYSTEM SHALL disable the "Confirm & Save" button and display the hint "Total must be > 0".

### Requirement 7 (REQ-007): Save Meal Log & Trigger Scan Increment
**User Story:** As a user, I want to tap "Confirm & Save" to log my meal and see it in my Diary immediately, so that my daily progress reflects what I just ate.
**Source:** FR-004 (AC-004.4, BR-004.1/.2/.3, ERR-004.1/.2/.3), UC-004, camera-capture AC-003.5

#### Acceptance Criteria
1. AC-007.1: WHEN the user taps "Confirm & Save" with ≥1 selected ingredient AND total > 0 THEN THE SYSTEM SHALL build a `MealLog` (timestamp = current system time, userId, ingredients, totalCalories, macros), persist it via `DataClient.insert`, AND call `ScanQuotaService.increment()` exactly once.
2. AC-007.2: WHEN the save succeeds THEN THE SYSTEM SHALL navigate to the Diary screen (WF-004, `diary-logging`) within 2s and the new log SHALL be visible at the top of today's list.
3. AC-007.3: IF the user taps "Confirm & Save" with 0 selected ingredients OR total = 0 THEN THE SYSTEM SHALL block the save and show a specific message ("Select at least one ingredient" or "Total must be > 0"), without incrementing the scan counter.
4. AC-007.4: IF the persistence call fails (network/DB error) THEN THE SYSTEM SHALL keep the draft, surface a recoverable error via `ErrorHandler` with a "Retry" action, and SHALL NOT call `ScanQuotaService.increment()`.
5. AC-007.5: WHEN a save is retried after a previous failure THEN THE SYSTEM SHALL call `ScanQuotaService.increment()` exactly once on the first successful persistence, and never on subsequent failures.

## Non-Functional Requirements
- NFR-CE-001: Recalculation latency — Macro/total recalc SHALL complete <200ms per mutation (FR-006 AC-006.2 / NFR-002). Measured: tap toggle/portion → total update.
- NFR-CE-002: Autocomplete latency — Add-ingredient suggestions SHALL appear <500ms after keystroke (FR-005 AC-005.2). Measured: keystroke → suggestions rendered.
- NFR-CE-003: Save latency — Save-to-Diary end-to-end SHALL be <2s on a warm cache (FR-004 AC-004.4 / PRD §9 core loop). Measured: "Confirm & Save" tap → Diary updated.
- NFR-CE-004: Validation strictness — Save SHALL be rejected if total ≤ 0 or selected-ingredients count = 0 (BR-004.1, BR-004.2). Measured: button state + message.
- NFR-CE-005: Increment idempotency — `ScanQuotaService.increment()` SHALL be invoked at most once per successful save (camera-capture AC-003.5). Measured: pbt/property test on retry flow.
- NFR-CE-006: Portion multiplier — small=0.75×, medium=1.0×, large=1.25× — fixed; manual grams convert via local DB density (BR-006.2, BR-006.3). Measured: pbt `MacroCalculationService`.
- NFR-CE-007: Macro calorie formula — Calories = (P×4) + (C×4) + (F×9), integer grams (BR-007.1). Measured: pbt rounding tolerance.
- NFR-CE-008: Offline behavior — Save shall attempt local-first; if offline, queue via `OfflineSyncService` (NFR-007) and surface "Saved locally — will sync when online"; scan increment MUST happen locally regardless of network.
