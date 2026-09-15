# camera-capture - Implementation Plan

## Execution Mode
- Mode: manual
- Policy: run sequentially by default (hybrid order from design.md)
- Gate: stop on phase boundary or blocking error

## Task Registry (Machine Readable)

| ID | Title | Type | Status | Refs AC | Refs Design | Files | Checkpoint |
|---|---|---|---|---|---|---|---|
| 2.1.1 | CapturedImage + CameraState + image validation | normal | pending | AC-002.5 | 4 | Features/Camera/Models/CapturedImage.swift | Rejects <640x480/wrong format/>10MB |
| 2.1.2 | ScanQuotaServicing + ScanQuotaService | normal | pending | AC-003.1, AC-003.2, AC-003.3, AC-003.5 | 7.3 | Features/Camera/Services/ScanQuotaService.swift | Count/reset/increment/unlimited |
| 2.1.3 | CameraServicing + CameraService (AVFoundation) | normal | pending | AC-001.1, AC-001.2, AC-001.4, AC-002.1, AC-002.2, AC-002.3, AC-004.1 | 7.2 | Features/Camera/Services/CameraService.swift | Permission/session/capture/library |
| 3.1.1 | CameraViewModel (state, validate, quota, handoff, lifecycle) | normal | pending | AC-002.4, AC-002.5, AC-003.4, AC-004.1, AC-004.2, AC-004.3 | 7.4 | Features/Camera/ViewModels/CameraViewModel.swift | State machine + callbacks |
| 3.2.1 | CameraPreviewRepresentable | normal | pending | AC-002.1 | 7.2 | Features/Camera/Views/CameraPreviewRepresentable.swift | Live preview renders |
| 3.2.2 | PhotoConfirmView (Use/Retake) | normal | pending | AC-002.2, AC-002.3 | 7.2 | Features/Camera/Views/PhotoConfirmView.swift | Use/Retake for both sources |
| 3.2.3 | Permission-denied / no-camera states | normal | pending | AC-001.3, AC-001.4 | 7.1 | Features/Camera/Views/CameraView.swift | Settings link; library fallback |
| 3.3.1 | ScanBadge component | normal | pending | AC-003.1, AC-003.2 | 7.3 | Features/Camera/Views/ScanBadge.swift | X/3 or Unlimited |
| 3.4.1 | CameraView assembly + replace RootView placeholder + wire callbacks | normal | pending | AC-001.1, AC-002.4, AC-003.4 | 8 | Features/Camera/Views/CameraView.swift, App/RootView.swift | Camera tab shows CameraView |
| 4.1.1 | ScanQuotaService tests | pbt | pending | AC-003.1, AC-003.2, AC-003.3, AC-003.4, AC-003.5 | 6 | calo-ai-testTests/ScanQuotaServiceTests.swift | Quota invariants |
| 4.1.2 | CameraViewModel tests (fakes) | pbt | pending | AC-001.3, AC-002.4, AC-002.5, AC-003.4, AC-004.1, AC-004.2 | 6 | calo-ai-testTests/CameraViewModelTests.swift | State + handoff + lifecycle |
| 4.1.3 | ImageValidation tests | pbt | pending | AC-002.5 | 6 | calo-ai-testTests/ImageValidationTests.swift | Size/format/byte thresholds |
| 4.2.1 | Build + integration gate | normal | pending | AC-001.1 | 6 | (build gate) | build_sim green; Camera tab live |

## Dependency Matrix
| Task | Depends On | Can Parallel With |
|---|---|---|
| 2.1.1 | — | 2.1.2, 2.1.3 |
| 2.1.2 | — | 2.1.1, 2.1.3 |
| 2.1.3 | 2.1.1 | 2.1.2 |
| 3.1.1 | 2.1.1, 2.1.2, 2.1.3 | 3.2.1, 3.3.1 |
| 3.2.1 | 2.1.3 | 3.3.1 |
| 3.2.2 | 2.1.1, 3.1.1 | 3.2.3 |
| 3.2.3 | 2.1.3, 3.1.1 | 3.2.2 |
| 3.3.1 | 2.1.2 | 3.2.1 |
| 3.4.1 | 3.1.1, 3.2.1, 3.2.2, 3.2.3, 3.3.1 | — |
| 4.1.1 | 2.1.2 | 4.1.2, 4.1.3 |
| 4.1.2 | 3.1.1 | 4.1.1, 4.1.3 |
| 4.1.3 | 2.1.1 | 4.1.1, 4.1.2 |
| 4.2.1 | 3.4.1, 4.1.1, 4.1.2, 4.1.3 | — |

## 1. Shared Tasks
> Models + services the Camera ViewModel depends on.

- [ ] **2.1.1** `CapturedImage` (image/data/dims/source, normalized JPEG) + `CameraState` enum + validation (≥640×480, JPG/PNG, ≤10MB)
  - Refs: AC-002.5
  - Design: 4
  - File: `Features/Camera/Models/CapturedImage.swift`
- [ ] **2.1.2** `ScanQuotaServicing` + `ScanQuotaService` (persisted `{dateKey,used}`, midnight reset, free max 3, Premium unlimited, public `increment()`)
  - Refs: AC-003.1, AC-003.2, AC-003.3, AC-003.5
  - Design: 7.3
  - File: `Features/Camera/Services/ScanQuotaService.swift`
- [ ] **2.1.3** `CameraServicing` + `CameraService` (permission query/request, AVCaptureSession start/stop, `capturePhoto()`, PhotosUI selection)
  - Refs: AC-001.1, AC-001.2, AC-001.4, AC-002.1, AC-002.2, AC-002.3, AC-004.1
  - Design: 7.2
  - File: `Features/Camera/Services/CameraService.swift`

**Phase Gate 2 (end of Shared phase):** Run XcodeBuildMCP `discover_projs -> list_schemes -> build_sim`, then traceability check (AC-001.1/.2/.4, AC-002.1/.2/.3/.5, AC-003.1/.2/.3/.5, AC-004.1 covered; Refs Design resolve).

## 2. Feature Tasks
> ViewModel + camera UI + badge + assembly.

- [ ] **3.1.1** `CameraViewModel` — `@MainActor ObservableObject` state machine; validate image; enforce quota; `onUseImage`/`onScanLimitReached`; start/stop on appear/disappear; hardware error → `ErrorHandler`
  - Refs: AC-002.4, AC-002.5, AC-003.4, AC-004.1, AC-004.2, AC-004.3
  - Design: 7.4
  - File: `Features/Camera/ViewModels/CameraViewModel.swift`
- [ ] **3.2.1** `CameraPreviewRepresentable` wrapping `AVCaptureVideoPreviewLayer`
  - Refs: AC-002.1
  - Design: 7.2
  - File: `Features/Camera/Views/CameraPreviewRepresentable.swift`
- [ ] **3.2.2** `PhotoConfirmView` — captured image + `CaloButton` Use/Retake (camera + library sources)
  - Refs: AC-002.2, AC-002.3
  - Design: 7.2
  - File: `Features/Camera/Views/PhotoConfirmView.swift`
- [ ] **3.2.3** Permission-denied + no-camera states in `CameraView` (Settings deep-link, library fallback)
  - Refs: AC-001.3, AC-001.4
  - Design: 7.1
  - File: `Features/Camera/Views/CameraView.swift`
- [ ] **3.3.1** `ScanBadge` — "X/3 scans" / "Unlimited" with accessibilityValue
  - Refs: AC-003.1, AC-003.2
  - Design: 7.3
  - File: `Features/Camera/Views/ScanBadge.swift`
- [ ] **3.4.1** Assemble `CameraView` (preview/shutter/library/badge/confirm), replace `PlaceholderView("Camera")` in `RootView`, wire `onUseImage`/`onScanLimitReached` (stub until ai-recognition/paywall)
  - Refs: AC-001.1, AC-002.4, AC-003.4
  - Design: 8
  - File: `Features/Camera/Views/CameraView.swift`, `App/RootView.swift`

**Phase Gate 3 (end of Feature phase):** Run XcodeBuildMCP `discover_projs -> list_schemes -> build_sim`, then traceability check (AC-001.3/.4, AC-002.*, AC-003.4, AC-004.* covered; Camera tab renders CameraView; Refs Design resolve).

## 3. Integration Tasks
> Unit tests + build/integration gate.

- [ ] **4.1.1** `ScanQuotaServiceTests` — free/premium remaining, midnight reset, increment-only, 4th-scan block
  - Refs: AC-003.1, AC-003.2, AC-003.3, AC-003.4, AC-003.5
  - Design: 6
  - File: `calo-ai-testTests/ScanQuotaServiceTests.swift`
- [ ] **4.1.2** `CameraViewModelTests` (fake `CameraServicing`/`ScanQuotaServicing`) — denied state, invalid-image reject, valid→handoff, limit→trigger, lifecycle start/stop
  - Refs: AC-001.3, AC-002.4, AC-002.5, AC-003.4, AC-004.1, AC-004.2
  - Design: 6
  - File: `calo-ai-testTests/CameraViewModelTests.swift`
- [ ] **4.1.3** `ImageValidationTests` — size/format/byte thresholds
  - Refs: AC-002.5
  - Design: 6
  - File: `calo-ai-testTests/ImageValidationTests.swift`
- [ ] **4.2.1** Build + integration gate: `build_sim` green; Camera tab shows `CameraView`; sim library-path smoke (AVCapture limited on sim)
  - Refs: AC-001.1
  - Design: 6
  - File: (build gate)

**Phase Gate 4 (end of Integration phase):** Run XcodeBuildMCP `discover_projs -> list_schemes -> build_sim` (+ `test_sim`), then traceability check (all 17 ACs traced to ≥1 done task; every Refs Design resolves).

## Traceability Matrix
| Task ID | AC | Design | Property | Status |
|---|---|---|---|---|
| 2.1.1 | AC-002.5 | 4 | P9 | pending |
| 2.1.2 | AC-003.1, AC-003.2, AC-003.3, AC-003.5 | 7.3 | P4, P5, P7 | pending |
| 2.1.3 | AC-001.1, AC-001.2, AC-001.4, AC-002.1, AC-002.2, AC-002.3, AC-004.1 | 7.2 | P1, P3, P8, P11 | pending |
| 3.1.1 | AC-002.4, AC-002.5, AC-003.4, AC-004.1, AC-004.2, AC-004.3 | 7.4 | P6, P10, P11, P12 | pending |
| 3.2.1 | AC-002.1 | 7.2 | P8 | pending |
| 3.2.2 | AC-002.2, AC-002.3 | 7.2 | P8 | pending |
| 3.2.3 | AC-001.3, AC-001.4 | 7.1 | P2, P3 | pending |
| 3.3.1 | AC-003.1, AC-003.2 | 7.3 | P4 | pending |
| 3.4.1 | AC-001.1, AC-002.4, AC-003.4 | 8 | P1, P6, P10 | pending |
| 4.1.1 | AC-003.1, AC-003.2, AC-003.3, AC-003.4, AC-003.5 | 6 | P4, P5, P6, P7 | pending |
| 4.1.2 | AC-001.3, AC-002.4, AC-002.5, AC-003.4, AC-004.1, AC-004.2 | 6 | P2, P6, P9, P10, P11 | pending |
| 4.1.3 | AC-002.5 | 6 | P9 | pending |
| 4.2.1 | AC-001.1 | 6 | P1 | pending |

## Progress
| Section | Total | Done | Status |
|---|---:|---:|---|
| Shared | 3 | 0 | ⬜ |
| Feature | 6 | 0 | ⬜ |
| Integration | 4 | 0 | ⬜ |