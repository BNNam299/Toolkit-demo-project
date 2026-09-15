# diary-logging - Requirements

## Overview
`diary-logging` là spec thứ tư của core loop (Phase 4), dựng màn hình Diary (WF-004) và hai modal Edit (WF-013) / Delete confirm (WF-014). User xem danh sách meal log theo ngày (FR-012) hoặc tuần (FR-013), so sánh tổng calo với mục tiêu qua `ProgressBar` (mã màu: green ≤100%, amber 100–110%, red >110% — BR-012.2 / BR-014.2, FR-014), vuốt trái trên từng meal row để mở Edit modal (WF-013, FR-015/FR-016) hoặc Delete confirm (WF-014, FR-017), và refresh khi có log mới từ `confirmation-edit`. Spec dùng lại `shared-foundations` (MealLog, DataClient, AppError, ErrorHandler, AppEnvironment, CaloButton, ProgressBar) và `confirmation-edit` (saves land in diary). KHÔNG bao gồm dashboard tuần (dashboard-view), paywall, onboarding.

## Evidence References
- **Market data from PRD:** Tốc độ core loop <10s (PRD §9) → diary phải load <500ms với 100+ meals (NFR-003). Empty-state phải có CTA rõ ràng về Camera (PRD §10 onboarding hints). Daily progress bar là "trust anchor" để user quay lại mỗi ngày (PRD §4 retention hooks).
- **Source documents:**
  - `.claude/specs/Calo-AI/Functional_Requirements.md` — FR-012 (Display daily log + BR-012.1/.2/.3, VR-012.1, ERR-012.1, AC-012.1..3), FR-013 (Weekly summary + BR-013.1/.2/.3, VR-013.1, ERR-013.1, AC-013.1..3), FR-014 (Progress vs goal + BR-014.1/.2/.3, VR-014.1, ERR-014.1, AC-014.1..3), FR-015 (Edit open modal + BR-015.1/.2, VR-015.1, ERR-015.1/.2, AC-015.1..3), FR-016 (Save edit + tied to FR-015), FR-017 (Delete + BR-017.1/.2, ERR-017.1, AC-017.1..3), NFR-003 (Diary load <500ms), NFR-007/008 (offline)
  - `.claude/specs/Calo-AI/Wireframes.md` — WF-004 (Diary), WF-013 (Edit Meal Modal), WF-014 (Delete Confirm Modal)
  - `.claude/specs/Calo-AI/Use_Cases.md` — UC-011 (Xem diary theo ngày), UC-012 (Xem diary theo tuần), UC-013 (So sánh vs mục tiêu), UC-014 (Chỉnh sửa log), UC-015 (Xoá log)
  - `.claude/specs/Calo-AI/PRD.md` §9 (NFR-003), §10 (empty state)
- **Key KPIs / measurable targets:** Diary initial load <500ms with 100+ meals (NFR-003); progress bar color thresholds green/amber/red (FR-014 AC-014.2, BR-012.2, BR-014.2); weekly view returns 7 rows for any Mon–Sun range (FR-013 AC-013.1, BR-013.1); swipe actions reveal within 200ms (UX expectation).

## Requirements

### Requirement 1 (REQ-001): Daily Meal Log View
**User Story:** As a user, I want to see all the meals I logged today with their calories and times, so that I can review my day and know what's left to reach my goal.
**Source:** FR-012, UC-011, WF-004, NFR-003

#### Acceptance Criteria
1. AC-001.1: WHEN the user opens the Diary tab THEN THE SYSTEM SHALL render the list of all `MealLog`s for today (local date) ordered by time, each row showing meal name, total calories, and time.
2. AC-001.2: WHILE the daily list is being fetched THEN THE SYSTEM SHALL display a skeleton/loading state for ≤500ms (NFR-003); if fetch exceeds 500ms a spinner remains visible without blocking the UI.
3. AC-001.3: IF no meals are logged today THEN THE SYSTEM SHALL show the empty state "No meals logged yet. Tap Camera to add one." with a primary CTA that navigates to the Camera tab.
4. AC-001.4: IF the data fetch fails THEN THE SYSTEM SHALL surface a recoverable error via the shared `ErrorHandler` and a "Retry" CTA, and SHALL NOT silently show stale data as if it were fresh (NFR-008 staleness marker).

### Requirement 2 (REQ-002): Weekly Summary View
**User Story:** As a user, I want to toggle from daily to weekly view and see 7 day rows (Mon–Sun) with daily totals and a weekly average, so that I can spot trends across the week.
**Source:** FR-013, UC-012, WF-004, BR-013.1/.2/.3

#### Acceptance Criteria
1. AC-002.1: WHEN the user taps the "Week view" toggle THEN THE SYSTEM SHALL replace the daily list with 7 rows (Mon–Sun) showing date label, daily total calories, and progress vs goal for the current week (Mon = start).
2. AC-002.2: WHEN the weekly view is shown THEN THE SYSTEM SHALL display a footer with the weekly average = `sum(dailyTotals) / 7` and the weekly total.
3. AC-002.3: IF no logs exist in the current week THEN THE SYSTEM SHALL show the empty state "Start logging to see weekly trends" with a CTA back to daily view.
4. AC-002.4: WHEN the user taps a daily row in week view THEN THE SYSTEM SHALL expand that row to reveal the meal list for that day (read-only), without leaving week view.

### Requirement 3 (REQ-003): Progress Bar vs Goal with Color Thresholds
**User Story:** As a user, I want a prominent progress bar showing today's calories vs my daily goal, color-coded so I instantly know if I'm on track, near, or over.
**Source:** FR-014, UC-013, WF-004, BR-012.2, BR-014.1/.2

#### Acceptance Criteria
1. AC-003.1: WHEN the daily total is computed THEN THE SYSTEM SHALL render a `ProgressBar` showing `consumed / goal` (e.g. "1800 / 2000 cal") and a remaining label ("200 cal left" or "10 cal over" if negative per BR-014.3).
2. AC-003.2: WHEN `consumed / goal ≤ 1.0` (≤100%) THEN THE SYSTEM SHALL render the `ProgressBar` in green (#34C759).
3. AC-003.3: WHEN `1.0 < consumed / goal ≤ 1.1` (100–110%) THEN THE SYSTEM SHALL render the `ProgressBar` in amber (#FF9500).
4. AC-003.4: WHEN `consumed / goal > 1.1` (>110%) THEN THE SYSTEM SHALL render the `ProgressBar` in red (#FF3B30) and show the message "You're over your goal".
5. AC-003.5: IF the user goal is not set THEN THE SYSTEM SHALL fall back to a 2000 kcal default and show a non-blocking prompt to complete onboarding profile (per ERR-014.1).

### Requirement 4 (REQ-004): Swipe-to-Edit on Meal Row
**User Story:** As a user, I want to swipe left on a meal row to reveal an "Edit" button so I can fix a wrong portion or ingredient from earlier.
**Source:** FR-015, UC-014, WF-013, WF-004

#### Acceptance Criteria
1. AC-004.1: WHEN the user swipes-left on a meal row THEN THE SYSTEM SHALL reveal Edit and Delete action buttons within 200ms.
2. AC-004.2: WHEN the user taps "Edit" THEN THE SYSTEM SHALL open the Edit Meal modal (WF-013) pre-populated with the meal's current ingredients, portions, and macros.
3. AC-004.3: IF the user is not the creator of the meal (BR-015.1) THEN THE SYSTEM SHALL hide the Edit action and only show Delete (still allowed for own meals only) — for MVP all meals are own meals so the action is always shown; future-proof the branch.
4. AC-004.4: IF the meal's `id` no longer exists (e.g. deleted from another path) THEN THE SYSTEM SHALL close the modal and show "Meal deleted by another user" via `ErrorHandler` (ERR-015.2).

### Requirement 5 (REQ-005): Edit Modal State & Save
**User Story:** As a user, I want to adjust ingredients/portions/macros in the Edit modal and tap Save to persist the changes, so that my diary reflects the corrected meal.
**Source:** FR-015, FR-016, UC-014, WF-013, BR-015.1/.2, VR-015.1

#### Acceptance Criteria
1. AC-005.1: WHEN the Edit modal opens THEN THE SYSTEM SHALL display a form mirroring the Confirmation screen (WF-003) — ingredient list with checkboxes, portion selectors, macro editor — pre-populated with the meal's current values.
2. AC-005.2: WHEN the user mutates the form THEN THE SYSTEM SHALL recalculate totals in <200ms (same `MacroCalculationService` from `confirmation-edit`).
3. AC-005.3: WHEN the user taps "Save" with valid data (≥1 ingredient, total > 0) THEN THE SYSTEM SHALL update the meal via `DataClient.update`, close the modal, and refresh the daily list (totals + progress bar).
4. AC-005.4: IF validation fails (0 selected OR total = 0) THEN THE SYSTEM SHALL block save with the specific message and keep the modal open.
5. AC-005.5: IF the update fails (DB error) THEN THE SYSTEM SHALL show a recoverable error via `ErrorHandler` with Retry; the modal stays open and the user's edits are preserved.

### Requirement 6 (REQ-006): Swipe-to-Delete with Confirmation
**User Story:** As a user, I want to swipe left and tap "Delete" to remove a meal I logged by mistake, with a confirmation step so I don't lose data accidentally.
**Source:** FR-017, UC-015, WF-014, BR-017.1/.2

#### Acceptance Criteria
1. AC-006.1: WHEN the user taps "Delete" on a meal row THEN THE SYSTEM SHALL open the Delete confirmation modal (WF-014) with the warning text "Delete this meal log? This action cannot be undone." and two buttons: Delete (destructive) and Cancel.
2. AC-006.2: WHEN the user confirms "Delete" THEN THE SYSTEM SHALL call `DataClient.delete(mealId)`, close the modal, remove the row from the list, and refresh the daily total + progress bar.
3. AC-006.3: IF the user taps "Cancel" THEN THE SYSTEM SHALL close the modal and leave the meal untouched.
4. AC-006.4: IF the delete fails (DB error) THEN THE SYSTEM SHALL keep the meal visible, surface a recoverable error via `ErrorHandler` with Retry, and SHALL NOT remove the row optimistically without a successful response (or roll back if optimistic).

### Requirement 7 (REQ-007): Refresh, Offline & Cross-Feature Sync
**User Story:** As a user, I want the Diary to refresh when I add/edit/delete a meal, work offline with a "last updated" indicator, and never silently lose my changes.
**Source:** FR-012, FR-015, FR-017, NFR-007, NFR-008, confirmation-edit save handoff

#### Acceptance Criteria
1. AC-007.1: WHEN the user returns to the Diary tab after a save in `confirmation-edit` (or after edit/delete in this spec) THEN THE SYSTEM SHALL refresh the list and progress bar so the latest changes are visible without a manual reload.
2. AC-007.2: WHEN the user pulls down to refresh THEN THE SYSTEM SHALL re-fetch from `DataClient` and re-render; the action SHALL complete within 2s for typical daily volumes (≤50 meals).
3. AC-007.3: IF the device is offline THEN THE SYSTEM SHALL render the cached list with a "Last updated X min ago" badge (NFR-008); queued writes (e.g. delete, edit) are flushed via `OfflineSyncService` when connectivity returns.
4. AC-007.4: IF a queued write fails to sync after N retries THEN THE SYSTEM SHALL surface a non-blocking error banner via `ErrorHandler` identifying the affected meal(s).

## Non-Functional Requirements
- NFR-DL-001: Load latency — Initial daily view SHALL render <500ms with 100+ meals (NFR-003). Measured: tab tap → list rendered.
- NFR-DL-002: Swipe latency — Swipe-action reveal SHALL occur within 200ms (UX expectation). Measured: swipe gesture → action buttons visible.
- NFR-DL-003: Recalc latency — Edit-modal macro recalc SHALL complete <200ms per mutation (NFR-002 implication; reuse `confirmation-edit`'s `MacroCalculationService`). Measured: input change → total update.
- NFR-DL-004: Color thresholds — green ≤100%, amber 100–110%, red >110% — exact (BR-012.2, BR-014.2). Measured: pbt over ratio grid.
- NFR-DL-005: Offline behavior — Diary SHALL display cached data with a "Last updated" indicator; queued edits/deletes SHALL retry via `OfflineSyncService` (NFR-007, NFR-008). Measured: airplane-mode simulation.
- NFR-DL-006: Edit isolation — Editing a meal SHALL update only that meal's `MealLog` and recompute daily totals from the new value, not from the prior value (correctness). Measured: pbt round-trip on edit.
- NFR-DL-007: Delete isolation — Deleting a meal SHALL remove it from the day's totals and progress bar; weekly aggregates SHALL also drop the deleted day's data (correctness). Measured: pbt round-trip on delete.
- NFR-DL-008: Week boundary — Week starts Monday (BR-013.1). Measured: pbt over locale=US calendar.
