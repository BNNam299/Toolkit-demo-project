# dashboard-view - Requirements

## Overview
`dashboard-view` là spec của Phase 5 dựng màn hình Dashboard (WF-005) trong Calo AI: thẻ tóm tắt tuần (Mon-Sun), biểu đồ cột 7 ngày cho calo, biểu đồ tròn phân tích macro (P/C/F), văn bản insight tự sinh theo trạng thái trung bình tuần so với mục tiêu, nút Xuất (CSV) và nút Chia sẻ (WF-015 share modal), và nút chuyển về xem hàng ngày (WF-004). Spec dùng lại `shared-foundations` (`MealLog`/`Macros` model, `DataClient`, `ProgressBar` color thresholds, `ErrorHandler`, `AppEnvironment`) và `project-structure` (Dashboard tab trong `RootView`). Phép tính "tiến độ vs mục tiêu" (FR-014) đã được dựng trong `diary-logging` (WF-004) — dashboard dùng lại hàm đó cho mỗi ngày trong tuần và thêm aggregation weekly + insight. KHÔNG bao gồm: xuất PDF (post-MVP), thay đổi mục tiêu từ dashboard (WF-017 — `account-management`), paywall (paywall-display), và core logging loop (`confirmation-edit`/`diary-logging`).

## Evidence References
- **Market data from PRD:** Dashboard là màn hình Consumption chính để giữ chân người dùng — cơ chế "xem tiến trình tuần" được Cal AI và MyFitnessPal dùng để drive D7 retention (PRD §1, §2 nguyên tắc 1). Chia sẻ progress qua OS share sheet là kênh organic acquisition đã chứng minh hiệu quả (PRD §2, Cal AI / Noom case studies). PRD §5 KPI **Weekly active users ≥ 3K** (mục tiêu 6 tháng, `_INDEX.md` line 61) phụ thuộc trực tiếp vào engagement của màn hình này; PRD §12 success metrics — Engagement KPIs (Scan completion rate, sessions/ngày) — đo qua event `scan_confirmed_saved` (PRD §12 Sự kiện Cốt lõi) mà dashboard là bề mặt phản hồi chính.
- **Source documents:**
  - `.claude/specs/Calo-AI/Functional_Requirements.md` — FR-013 (Display Weekly Summary: BR-013.1 Mon start, BR-013.2 avg = sum/7, BR-013.3 days-without-logs = 0, ERR-013.1 empty state, AC-013.1/.2/.3); FR-014 (Calculate Progress vs Goal: BR-014.1 goal=2000 default, BR-014.2 color thresholds 100/110, BR-014.3 remaining có thể âm, ERR-014.1 goal unset, AC-014.1/.2/.3)
  - `.claude/specs/Calo-AI/Use_Cases.md` — UC-012 (Xem Diary theo Tuần), UC-013 (So sánh vs Mục tiêu)
  - `.claude/specs/Calo-AI/Wireframes.md` — WF-005 (Dashboard — 4 vùng A/B/C/D, "Tuần đầu tiên" empty state, "On Track/Above Average/Below Average" variations, a11y labels "Biểu đồ hàng tuần, Thứ Hai 1800 calo, Thứ Ba 1950…", "Xuất tuần dưới dạng CSV"), WF-015 (Share Modal — preview text "Tôi đã ăn 1850 calo hôm nay! 📊", Share/Cancel buttons, UIActivityViewController), WF-004 (Diary — toggle target cho "Xem hàng ngày")
  - `.claude/specs/Calo-AI/PRD.md` §5 (KPI: Weekly active users ≥3K), §12 (Success metrics — Engagement KPIs, `scan_confirmed_saved` event), §9 (a11y: Dynamic Type, VoiceOver, tap targets ≥44pt)
  - `.claude/specs/Calo-AI/Project_Implementation_Roadmap.md` Phase 5 (file breakdown `Features/Dashboard/{Views,ViewModels,Models}/WeeklyStats.swift`, depends_on `diary-logging`)
- **Key KPIs / measurable targets:** Weekly active users ≥3K (PRD §5 mục tiêu 6 tháng); Dashboard load <1s sau tab tap; Export CSV <500ms; insight text generation <100ms (synchronous, no network); share modal preview <100ms.

## Requirements

### Requirement 1 (REQ-001): Weekly Aggregation & Summary Card
**User Story:** As a user, I want to open the Dashboard tab and see a clear weekly summary card with total calories, daily average, and per-day status, so that I can quickly understand how my week is going versus my goal.
**Source:** FR-013, UC-012, WF-005; FR-014 (goal semantics reused for daily status, BR-014.1/2/3, ERR-014.1)

#### Acceptance Criteria
1. AC-001.1: WHEN the user opens the Dashboard tab THEN THE SYSTEM SHALL display a weekly summary card with the weekly total calories and the daily average in `<weeklyTotal> cal / <avg> cal/day` format (FR-013 AC-013.2, BR-013.2).
2. AC-001.2: WHEN the local clock crosses Monday 00:00 THEN THE SYSTEM SHALL reset the displayed week to the new Mon-Sun range (BR-013.1).
3. AC-001.3: IF no meal logs exist in the current week THEN THE SYSTEM SHALL show the empty state "Ghi log bữa ăn để xem xu hướng hàng tuần" with a CTA to the Camera tab (ERR-013.1, WF-005 "Tuần đầu tiên" state).
4. AC-001.4: WHEN any day in the week has zero logs THEN THE SYSTEM SHALL show 0 calories for that day (BR-013.3) AND the daily average SHALL still be computed as `sum_of_daily_totals / 7` (BR-013.2).
5. AC-001.5: IF the user's calorie goal is unset (`User.calorieTarget <= 0` or nil) THEN THE SYSTEM SHALL fall back to a 2000 kcal default for ratio calculations (BR-014.1) AND SHALL show a banner prompting the user to set their profile (ERR-014.1).

### Requirement 2 (REQ-002): 7-Bar Calorie Chart & Macro Pie Chart
**User Story:** As a user, I want a bar chart showing each of the 7 days of the week with each day's calories color-coded by goal status, plus a macro pie chart of my weekly Protein/Carbs/Fat split, so that I can see both my daily pacing and macro balance at a glance.
**Source:** FR-014, UC-013, WF-005

#### Acceptance Criteria
1. AC-002.1: WHEN weekly stats are available THEN THE SYSTEM SHALL render a 7-bar chart (Mon, Tue, Wed, Thu, Fri, Sat, Sun) where each bar's height equals the daily total calories.
2. AC-002.2: WHEN a bar is rendered THEN THE SYSTEM SHALL color it green (≤100% of goal), yellow (100–110%), or red (>110%) per BR-014.2 / BR-012.2.
3. AC-002.3: WHEN weekly macros are non-zero THEN THE SYSTEM SHALL render a pie chart with three slices (Protein/Carbs/Fat) whose percentages sum to 100% (±1% rounding tolerance) and the underlying gram values SHALL sum to within ±10% of the calorie equivalent (VR-003.3).
4. AC-002.4: IF the entire week has zero macro grams THEN THE SYSTEM SHALL render a placeholder "Chưa có dữ liệu macro" instead of a degenerate pie chart, AND SHALL NOT crash on divide-by-zero.
5. AC-002.5: IF the Swift Charts framework cannot render (e.g. iOS <16) THEN THE SYSTEM SHALL fall back to a text-only summary of the 7 days and macros, AND SHALL NOT crash or show a blank pane.

### Requirement 3 (REQ-003): Insights Text Generation
**User Story:** As a user, I want a 1-2 sentence insight comparing my weekly average to my goal, so that I get a quick read on whether I am on track, slightly over, or consistently over/under, and can adjust my behavior.
**Source:** FR-014, UC-013, WF-005

#### Acceptance Criteria
1. AC-003.1: WHEN the weekly average is computed THEN THE SYSTEM SHALL generate a 1-2 sentence insight comparing the average to the goal (e.g. "Tuyệt vời, 2% dưới mục tiêu tuần này" — WF-005 insight copy, FR-014 AC-014.3).
2. AC-003.2: WHEN the average is ≤100% of goal THEN THE SYSTEM SHALL use an on-track tone ("Tuyệt vời…"); WHEN 100–110% THEN a near-limit tone ("Cẩn thận…"); WHEN >110% THEN an over-goal tone ("Bạn đã vượt mục tiêu tuần…").
3. AC-003.3: IF at least 4 of 7 days are >110% of goal THEN THE SYSTEM SHALL append a gentle coaching tip per the WF-005 "Above Average" state variation.
4. AC-003.4: IF at least 4 of 7 days are <80% of goal THEN THE SYSTEM SHALL append an encouragement to eat enough per the WF-005 "Below Average" state variation.
5. AC-003.5: IF the insight cannot be generated (empty weekly stats or zero-goal) THEN THE SYSTEM SHALL show a generic placeholder "Hãy ghi log để xem insight tuần" rather than render a blank text view.

### Requirement 4 (REQ-004): Export & Share Progress
**User Story:** As a user, I want to export my weekly progress as a CSV file and share a friendly summary via the OS share sheet, so that I can keep a record or show my progress to friends.
**Source:** FR-014, UC-013, WF-005, WF-015

#### Acceptance Criteria
1. AC-004.1: WHEN the user taps the Export button on WF-005 THEN THE SYSTEM SHALL generate a CSV file with 7 daily rows (weekday, date, daily_total, daily_goal) plus a weekly summary row (total + average) AND present a system share/save sheet (WF-005 "Nhấn Xuất → Tải CSV hoặc PDF").
2. AC-004.2: WHEN the user taps the Share button on WF-005 THEN THE SYSTEM SHALL open the WF-015 Share Modal showing a preview text (e.g. "Tôi đã ăn 1850 calo hôm nay! 📊") AND a Share button that, when tapped, presents `UIActivityViewController` (WF-015 "Nhấn 'Chia Sẻ' → Open UIActivityViewController").
3. AC-004.3: WHEN the user taps Cancel in the WF-015 Share Modal THEN THE SYSTEM SHALL close the modal without invoking `UIActivityViewController` AND the underlying Dashboard state SHALL remain intact.
4. AC-004.4: IF the CSV file write fails (disk full, permission denied) THEN THE SYSTEM SHALL surface a recoverable error via the shared `ErrorHandler` AND SHALL NOT leave a partial file in the temp directory.
5. AC-004.5: IF the user dismisses `UIActivityViewController` without selecting a target THEN THE SYSTEM SHALL return the user to the WF-005 Dashboard with all previously rendered charts and insights intact.

### Requirement 5 (REQ-005): Dashboard Lifecycle, Tab Integration & Daily Toggle
**User Story:** As a user, I want the Dashboard tab to load quickly when I switch to it, survive an interrupted session, and let me toggle back to the daily Diary view, so that the dashboard fits naturally into my tab navigation and re-entry is seamless.
**Source:** FR-014, UC-013, WF-005, WF-004 (toggle target)

#### Acceptance Criteria
1. AC-005.1: WHEN the user taps the "Xem hàng ngày" toggle on WF-005 THEN THE SYSTEM SHALL switch the active tab to the Diary tab and present WF-004 (daily) with the most recent day selected (WF-005 "Nhấn 'Xem hàng ngày' → Quay lại WF-004").
2. AC-005.2: WHEN the Dashboard tab is re-entered within the same session AND the underlying weekly-stats cache is still fresh (cacheAge ≤ 5 minutes) THEN THE SYSTEM SHALL re-render the previously computed `WeeklyStats` without re-querying the backend.
3. AC-005.3: IF the user re-enters the Dashboard tab after the cache is stale (cacheAge > 5 minutes) THEN THE SYSTEM SHALL re-fetch the week's logs via the shared `DataClient` and show a subtle loading indicator on the bar chart, AND SHALL NOT clear the previous chart (smooth refresh, no flicker).
4. AC-005.4: IF the underlying `DataClient` query fails (network or server error) THEN THE SYSTEM SHALL surface a recoverable error via the shared `ErrorHandler`, retain the last successfully loaded `WeeklyStats` if any, and provide a "Retry" affordance — AND SHALL NOT crash or blank the screen.

## Non-Functional Requirements
- NFR-DV-001: Dashboard load time — Dashboard tab SHALL render the summary card and the 7-bar chart within <1 second after tab tap on an iPhone 12+ with up to 100 cached logs in scope (matches PRD §12 Engagement measurement window). Measured: tab tap → first paint of bar chart.
- NFR-DV-002: Export latency — CSV generation + share/save-sheet presentation SHALL complete within <500ms (FR-014 derived). Measured: Export button tap → `UIActivityViewController` visible.
- NFR-DV-003: Insight latency — Insight text generation SHALL complete within <100ms (synchronous, no network). Measured: `WeeklyStats` loaded → `WeeklyInsight` string returned.
- NFR-DV-004: iOS version floor — Swift Charts requires iOS 16+; Dashboard SHALL use `if #available(iOS 16, *)` guard and SHALL NOT regress the build minimum below iOS 16.
- NFR-DV-005: Accessibility — Charts SHALL expose a VoiceOver `accessibilityLabel` summarizing each day's calories (e.g. "Biểu đồ hàng tuần, Thứ Hai 1800 calo, Thứ Ba 1950…" per WF-005 Hỗ Trợ Tiếp Cận); Dynamic Type SHALL be respected; tap targets SHALL be ≥44pt (PRD §9 a11y baseline).
