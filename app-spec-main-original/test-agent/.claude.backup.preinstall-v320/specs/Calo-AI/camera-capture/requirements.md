# camera-capture - Requirements

## Overview
`camera-capture` là spec đầu tiên của core loop (Phase 3). Nó dựng màn hình Camera (WF-002) và luồng quyền camera (WF-009): xin quyền camera, hiển thị live preview, chụp ảnh hoặc chọn từ thư viện, xác nhận ảnh (Use/Retake), và quản lý **giới hạn scan free tier** (3 lượt/ngày) — hiển thị badge số lượt còn lại và chặn lượt thứ 4 để trigger paywall. Ảnh hợp lệ được bàn giao cho `ai-recognition` (FR-003). Spec dùng lại `shared-foundations` (AppEnvironment, ErrorHandler, User/session) và `project-structure` (RootView Camera tab). KHÔNG bao gồm phân tích AI (ai-recognition) hay UI paywall (paywall-display).

## Evidence References
- **Market data from PRD:** Tốc độ core loop là lợi thế cạnh tranh chính — mục tiêu <10s từ mở camera đến log xong (PRD §2 nguyên tắc 1, Overview §1.2). Free tier "hào phóng 3 lượt/ngày" cố ý rộng hơn giới hạn 5-lượt-nhập/ngày gây bất mãn của MyFitnessPal (PRD §11) để tạo thói quen dùng hàng ngày.
- **Source documents:**
  - `.claude/specs/Calo-AI/Functional_Requirements.md` — FR-001 (camera permission + BR/VR/ERR/AC), FR-002 (live preview & capture + BR-002.1..3, VR-002.1..2), FR-009 (remaining scans + BR-009.1..4), FR-010 (paywall trigger — chỉ phần trigger)
  - `.claude/specs/Calo-AI/Wireframes.md` — WF-002 (Camera), WF-009 (Permission)
  - `.claude/specs/Calo-AI/Use_Cases.md` — UC-001, UC-002, UC-009
  - `.claude/specs/Calo-AI/PRD.md` §9 (AVFoundation camera; portrait one-hand; permission một lần)
- **Key KPIs / measurable targets:** Live preview xuất hiện <1s sau khi cấp quyền (FR-001 AC-001.3); ảnh preview hiển thị <2s (BR-002.3); scan completion rate (PRD §12) — badge phải chính xác để không chặn nhầm.

## Requirements

### Requirement 1 (REQ-001): Camera Permission
**User Story:** As a user, I want the app to request camera access when I first open the Camera tab and guide me if I denied it, so that I can start photographing meals or recover from a denial.
**Source:** FR-001, UC-001, WF-009

#### Acceptance Criteria
1. AC-001.1: WHEN the user opens the Camera tab for the first time THEN THE SYSTEM SHALL present the iOS native camera permission dialog.
2. AC-001.2: WHEN permission is granted THEN THE SYSTEM SHALL show the live preview within 1 second.
3. AC-001.3: IF permission is denied THEN THE SYSTEM SHALL show a "Camera access required" state with a button that deep-links to Settings, and SHALL NOT crash or show a black screen.
4. AC-001.4: IF the device has no usable camera THEN THE SYSTEM SHALL show "Camera not available on this device" and still allow choosing a photo from the library.

### Requirement 2 (REQ-002): Live Preview, Capture & Photo Selection
**User Story:** As a user, I want to see a live camera preview and either shoot a photo or pick one from my library, then confirm it, so that I can supply a clear meal image to the AI.
**Source:** FR-002, UC-002, WF-002

#### Acceptance Criteria
1. AC-002.1: WHEN permission is granted THEN THE SYSTEM SHALL display a full-screen live preview (rear camera) with a shutter button and a photo-library button.
2. AC-002.2: WHEN the user taps the shutter THEN THE SYSTEM SHALL capture a frame and show a preview with "Use This" and "Retake" within 2 seconds.
3. AC-002.3: WHEN the user taps the photo-library button THEN THE SYSTEM SHALL present the native photo picker and, after selection, show the same Use/Retake preview.
4. AC-002.4: WHEN the user taps "Use This" THEN THE SYSTEM SHALL hand the image off to AI recognition (FR-003 entry).
5. AC-002.5: IF the chosen image is below 640×480 or an unsupported format (not JPG/PNG) THEN THE SYSTEM SHALL reject it with a specific message and return to capture (no hand-off).

### Requirement 3 (REQ-003): Scan Quota Display & Enforcement
**User Story:** As a free-tier user, I want to see how many AI scans I have left today and be told when I've run out, so that I understand the free limit and know when to upgrade.
**Source:** FR-009, UC-009; FR-010 (trigger only — paywall UI owned by `paywall-display`)

#### Acceptance Criteria
1. AC-003.1: WHILE the user is on the free tier THE SYSTEM SHALL display a "X/3 scans" badge on the Camera tab reflecting scans remaining today.
2. AC-003.2: WHILE the user is Premium THE SYSTEM SHALL display "Unlimited" instead of a count.
3. AC-003.3: WHEN the local day rolls over (midnight) THEN THE SYSTEM SHALL reset the free-tier count to 3.
4. AC-003.4: WHEN a free-tier user with 3 scans used attempts a 4th scan THEN THE SYSTEM SHALL block the scan and emit a paywall-trigger signal (handoff to FR-010) instead of proceeding to AI.
5. AC-003.5: WHERE a scan is only counted after a meal log is successfully saved (BR-009.4) THE SYSTEM SHALL expose an `increment()` the save flow (`confirmation-edit`) calls, NOT increment on photo capture.

### Requirement 4 (REQ-004): Camera Screen Lifecycle & Handoff
**User Story:** As a user, I want the camera to behave correctly as I enter/leave the tab and hand a clean image to analysis, so that the core loop feels fast and reliable.
**Source:** FR-002 (output→FR-003), UC-002, PRD §9 (performance, portrait)

#### Acceptance Criteria
1. AC-004.1: WHEN the Camera tab appears THEN THE SYSTEM SHALL start the capture session, and WHEN it disappears THEN THE SYSTEM SHALL stop the session to release the camera and save battery.
2. AC-004.2: WHEN "Use This" is confirmed THEN THE SYSTEM SHALL pass a normalized image (correct orientation, JPEG-encoded) to the AI entry point.
3. AC-004.3: IF a hardware capture error occurs THEN THE SYSTEM SHALL surface a recoverable error via the shared `ErrorHandler` and return to the preview.

## Non-Functional Requirements
- NFR-CC-001: Preview latency — Live preview SHALL appear <1s after permission granted (FR-001 AC-001.3). Measured: grant→first frame.
- NFR-CC-002: Capture latency — Captured/selected photo preview SHALL render <2s (BR-002.3). Measured: shutter tap→preview.
- NFR-CC-003: Permission timeout — A permission response SHALL be treated as denied if not received within 30s (VR-001.1).
- NFR-CC-004: Image constraints — Only JPG/PNG ≥640×480 and ≤10MB SHALL be accepted (BR-002.2, VR-002.1/2).
- NFR-CC-005: Resource release — The capture session SHALL be stopped when the tab is not visible (no camera held in background).
