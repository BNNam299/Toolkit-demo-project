# ai-recognition - Requirements

## Overview
`ai-recognition` là spec thứ hai của core loop (Phase 3). Nó nhận ảnh bữa ăn hợp lệ từ `camera-capture`, gửi tới AI Vision API (OpenAI/Anthropic multimodal), hiển thị màn hình loading (WF-010 "Analyzing your meal..."), parse kết quả JSON `{meal name, calories, macros, ingredients[], confidence}`, kiểm tra hợp lệ + ngưỡng độ tin cậy, và chuyển sang màn Confirmation (`confirmation-edit`, WF-003) — hoặc hiển thị màn lỗi/retry (WF-011) khi timeout/lỗi/không nhận diện được. Spec dùng lại `shared-foundations` (RetryPolicy, AppError, ErrorHandler, MealLog/Ingredient/Macros models, AppEnvironment). KHÔNG bao gồm UI xác nhận nguyên liệu (confirmation-edit) hay chụp ảnh (camera-capture).

## Evidence References
- **Market data from PRD:** Sai số AI (dầu/nước sốt/nguyên liệu ẩn) là phàn nàn phổ biến ở mọi app AI-photo kể cả Cal AI (PRD §4). Vì vậy Calo AI bắt buộc bước xác nhận + đo `scan_manual_override` (PRD §12) — spec này phải trả về `confidence` và danh sách nguyên liệu để bước confirmation sửa. Tốc độ là lợi thế: AI trả kết quả <5s là ngưỡng UX quan trọng nhất (PRD §9, Overview §6.1).
- **Source documents:**
  - `.claude/specs/Calo-AI/Functional_Requirements.md` — FR-003 (AI Vision call + BR-003.1..4, VR-003.1..3, ERR-003.1..4, AC-003.1..5), NFR-002 (AI detection <5s, 10s timeout), NFR-016 (retry/backoff)
  - `.claude/specs/Calo-AI/Wireframes.md` — WF-010 (Loading), WF-011 (Error)
  - `.claude/specs/Calo-AI/Use_Cases.md` — UC-003 (Xem Kết quả AI, AF-003.1/.2)
  - `.claude/specs/Calo-AI/PRD.md` §9 (AI Vision API p95 <3s; không scan offline)
- **Key KPIs / measurable targets:** AI detection avg 3–5s, hard timeout 10s (NFR-002 / BR-003.1); confidence threshold 70% (BR-003.2); calories 0–5000, confidence 0–100, macros↔calories ±10% (VR-003.1/.2/.3).

## Requirements

### Requirement 1 (REQ-001): AI Vision Analysis Request
**User Story:** As a user, I want the app to send my meal photo to the AI and get back the dish, calories, macros and ingredients, so that I don't have to search or type anything.
**Source:** FR-003, UC-003, NFR-002

#### Acceptance Criteria
1. AC-001.1: WHEN an image is handed off from `camera-capture` ("Use This") THEN THE SYSTEM SHALL send it to the AI Vision API with a structured prompt requesting name, serving size, calories, protein/carbs/fat, and confidence (0–100) as JSON.
2. AC-001.2: WHEN the API responds successfully THEN THE SYSTEM SHALL parse it into a `MealLog` draft (`meal name`, `calories`, `macros`, `ingredients[]`, `confidence`).
3. AC-001.3: WHEN parsing succeeds and confidence ≥ 70% THEN THE SYSTEM SHALL navigate to the Confirmation screen (WF-003) with the draft.
4. AC-001.4: IF the API returns null/empty or zero ingredients THEN THE SYSTEM SHALL show "No food detected. Please take a clearer photo." (WF-011) with Retry/Back.

### Requirement 2 (REQ-002): Loading State
**User Story:** As a user, I want a clear "analyzing" state while the AI works, so that I know the app is processing and roughly how long to wait.
**Source:** FR-003 (AC-003.1), WF-010, NFR-002

#### Acceptance Criteria
1. AC-002.1: WHEN analysis starts THEN THE SYSTEM SHALL show the loading screen (WF-010) with a spinner and "Analyzing your meal…" text.
2. AC-002.2: WHILE analysis is in progress THE SYSTEM SHALL keep the loading state visible and block duplicate submissions of the same image.
3. AC-002.3: WHEN a result or error arrives THEN THE SYSTEM SHALL dismiss the loading state and route to Confirmation or Error accordingly.
4. AC-002.4: IF the user cancels from the loading screen THEN THE SYSTEM SHALL abort the request and return to the camera without creating a draft.

### Requirement 3 (REQ-003): Result Validation & Confidence Handling
**User Story:** As a user, I want the app to sanity-check the AI result and warn me when it's unsure, so that I don't unknowingly log a wildly wrong estimate.
**Source:** FR-003 (BR-003.2/.3/.4, VR-003.1/.2/.3, AC-003.4), UC-003 (AF-003.1)

#### Acceptance Criteria
1. AC-003.1: WHEN a result is parsed THEN THE SYSTEM SHALL validate calories ∈ [0,5000], confidence ∈ [0,100], each macro ≥ 0, and ≥ 1 ingredient.
2. AC-003.2: IF the macro-to-calorie equivalence is off by more than ±10% THEN THE SYSTEM SHALL flag the result as low-quality (proceed but mark for user review).
3. AC-003.3: IF confidence < 70% THEN THE SYSTEM SHALL still route to Confirmation but display a warning badge ("Not confident — please verify") with an easy Retry option.
4. AC-003.4: IF validation fails hard (non-numeric, calories out of range, empty ingredients) THEN THE SYSTEM SHALL treat it as "no usable result" and route to the Error screen (WF-011), not Confirmation.

### Requirement 4 (REQ-004): Timeout, Error & Retry
**User Story:** As a user on a flaky connection, I want a clear error and a one-tap retry when analysis fails, so that a transient problem doesn't cost me my photo.
**Source:** FR-003 (BR-003.1, ERR-003.1/.2/.3), WF-011, NFR-002, NFR-016

#### Acceptance Criteria
1. AC-004.1: IF the API call exceeds 10 seconds THEN THE SYSTEM SHALL abort and show "Connection error. Please try again." (WF-011) with a Retry button.
2. AC-004.2: WHEN a transient failure (network/5xx/timeout) occurs THEN THE SYSTEM SHALL retry with the shared `RetryPolicy` (≤3 attempts, ≤10s total) before showing the error.
3. AC-004.3: WHEN the user taps Retry THEN THE SYSTEM SHALL re-submit the same image and return to the loading state.
4. AC-004.4: WHEN the user taps Back from the error screen THEN THE SYSTEM SHALL return to the camera preview without consuming a scan.
5. AC-004.5: IF the device is offline at submission THEN THE SYSTEM SHALL fail fast with "You're offline — AI scan needs a connection." (no scan needs internet per PRD §9), without exhausting retries.

## Non-Functional Requirements
- NFR-AR-001: Detection latency — Typical end-to-end AI result SHALL be <5s (avg 3–5s); hard timeout 10s (NFR-002 / BR-003.1). Measured: submit→result/error.
- NFR-AR-002: Retry bound — Automatic retries SHALL be capped at 3 attempts and ≤10s cumulative (NFR-016 / shared `RetryPolicy`).
- NFR-AR-003: Transport security — The AI Vision request SHALL use HTTPS/TLS only; the API key SHALL come from configuration (xcconfig), never hardcoded (PRD §9, NFR-005).
- NFR-AR-004: No partial data — A malformed/partial API response SHALL never produce a Confirmation draft (routes to Error instead).
- NFR-AR-005: Privacy — The meal photo SHALL be sent only to the configured AI endpoint over HTTPS and SHALL NOT be persisted beyond the request unless the user later saves the log (PRD §9 storage policy).
