# ai-recognition - Implementation Plan

## Execution Mode
- Mode: manual
- Policy: run sequentially by default (logic-first order from design.md)
- Gate: stop on phase boundary or blocking error

## Task Registry (Machine Readable)

| ID | Title | Type | Status | Refs AC | Refs Design | Files | Checkpoint |
|---|---|---|---|---|---|---|---|
| 2.1.1 | MealDraft + VisionResult/VisionIngredient DTOs | normal | pending | AC-001.2 | 4 | Features/AI/Models/MealDraft.swift | Decodable DTO → MealDraft mapping |
| 2.1.2 | VisionPromptBuilder | normal | pending | AC-001.1 | 7.1 | Features/AI/Services/VisionPromptBuilder.swift | Structured JSON-request prompt |
| 2.1.3 | VisionResponseParser (validate + confidence) | normal | pending | AC-001.2, AC-003.1, AC-003.2, AC-003.4 | 7.3 | Features/AI/Services/VisionResponseParser.swift | Ranges, ±10%, ≥1 ingredient |
| 2.1.4 | VisionAPIServicing + VisionAPIService | normal | pending | AC-001.1, AC-004.1, AC-004.2 | 7.1 | Features/AI/Services/VisionAPIService.swift | HTTPS, 10s timeout, key from config, retry |
| 3.1.1 | AIRecognitionViewModel (phase machine, routing) | normal | pending | AC-001.3, AC-001.4, AC-002.2, AC-002.3, AC-002.4, AC-003.3, AC-004.3, AC-004.4, AC-004.5 | 7.4 | Features/AI/ViewModels/AIRecognitionViewModel.swift | Offline fail-fast, retry/cancel/back |
| 3.2.1 | LoadingView (WF-010) | normal | pending | AC-002.1 | 7.2 | Features/AI/Views/LoadingView.swift | Spinner + Analyzing + Cancel |
| 3.2.2 | ErrorView (WF-011) | normal | pending | AC-004.1 | 7.4 | Features/AI/Views/ErrorView.swift | Message + Retry/Back |
| 3.3.1 | Wire camera onUseImage → VM.start; stub onConfirm exit | normal | pending | AC-001.3 | 8 | App/RootView.swift, Features/Camera/Views/CameraView.swift | Camera → Loading flow live |
| 4.1.1 | VisionResponseParser tests | pbt | pending | AC-001.2, AC-003.1, AC-003.2, AC-003.4 | 6 | calo-ai-testTests/VisionResponseParserTests.swift | Valid parse; range/tolerance/empty |
| 4.1.2 | VisionAPIService tests (URLProtocol stub) | pbt | pending | AC-001.1, AC-004.1, AC-004.2 | 6 | calo-ai-testTests/VisionAPIServiceTests.swift | HTTPS/timeout/retry/decode |
| 4.1.3 | AIRecognitionViewModel tests (fakes) | pbt | pending | AC-001.3, AC-001.4, AC-002.2, AC-002.4, AC-003.3, AC-004.3, AC-004.4, AC-004.5 | 6 | calo-ai-testTests/AIRecognitionViewModelTests.swift | Routing/offline/retry/cancel/back |
| 4.2.1 | Build + integration gate | normal | pending | AC-002.1 | 6 | (build gate) | build_sim green; camera→loading→(confirm stub) |

## Dependency Matrix
| Task | Depends On | Can Parallel With |
|---|---|---|
| 2.1.1 | — | 2.1.2 |
| 2.1.2 | — | 2.1.1 |
| 2.1.3 | 2.1.1 | 2.1.4 |
| 2.1.4 | 2.1.1, 2.1.2 | 2.1.3 |
| 3.1.1 | 2.1.3, 2.1.4 | 3.2.1, 3.2.2 |
| 3.2.1 | — | 3.2.2 |
| 3.2.2 | — | 3.2.1 |
| 3.3.1 | 3.1.1, 3.2.1, 3.2.2 | — |
| 4.1.1 | 2.1.3 | 4.1.2, 4.1.3 |
| 4.1.2 | 2.1.4 | 4.1.1, 4.1.3 |
| 4.1.3 | 3.1.1 | 4.1.1, 4.1.2 |
| 4.2.1 | 3.3.1, 4.1.1, 4.1.2, 4.1.3 | — |

## 1. Shared Tasks
> DTOs, prompt, parser, and API service.

- [ ] **2.1.1** `MealDraft` + `VisionResult`/`VisionIngredient` DTOs; mapping DTO→`MealLog`/`Ingredient` (ingredients default `isSelected=true`)
  - Refs: AC-001.2
  - Design: 4
  - File: `Features/AI/Models/MealDraft.swift`
- [ ] **2.1.2** `VisionPromptBuilder` — structured prompt requesting name/serving/calories/macros/confidence as JSON
  - Refs: AC-001.1
  - Design: 7.1
  - File: `Features/AI/Services/VisionPromptBuilder.swift`
- [ ] **2.1.3** `VisionResponseParser` — decode → `MealDraft`; validate ranges + ≥1 ingredient; macro±10%→lowQuality; confidence<70→lowConfidence; hard-fail throws
  - Refs: AC-001.2, AC-003.1, AC-003.2, AC-003.4
  - Design: 7.3
  - File: `Features/AI/Services/VisionResponseParser.swift`
- [ ] **2.1.4** `VisionAPIServicing` + `VisionAPIService` — URLSession HTTPS call, 10s timeout, key from `AppConfiguration`, `RetryPolicy`-wrapped, throws `AppError`
  - Refs: AC-001.1, AC-004.1, AC-004.2
  - Design: 7.1
  - File: `Features/AI/Services/VisionAPIService.swift`

**Phase Gate 2 (end of Shared phase):** Run XcodeBuildMCP `discover_projs -> list_schemes -> build_sim`, then traceability check (AC-001.1/.2, AC-003.1/.2/.4, AC-004.1/.2 covered; Refs Design resolve).

## 2. Feature Tasks
> ViewModel + loading/error screens + wiring.

- [ ] **3.1.1** `AIRecognitionViewModel` — `@Published phase` (loading/success/error); `start/retry/cancel/back`; offline fail-fast (`Reachability`); route ≥70→onConfirm, <70→onConfirm+warning, invalid/empty→error; block duplicate submit
  - Refs: AC-001.3, AC-001.4, AC-002.2, AC-002.3, AC-002.4, AC-003.3, AC-004.3, AC-004.4, AC-004.5
  - Design: 7.4
  - File: `Features/AI/ViewModels/AIRecognitionViewModel.swift`
- [ ] **3.2.1** `LoadingView` (WF-010) — spinner + "Analyzing your meal…" + Cancel (`CaloButton`), VoiceOver
  - Refs: AC-002.1
  - Design: 7.2
  - File: `Features/AI/Views/LoadingView.swift`
- [ ] **3.2.2** `ErrorView` (WF-011) — icon + mapped message + Retry/Back (`CaloButton`)
  - Refs: AC-004.1
  - Design: 7.4
  - File: `Features/AI/Views/ErrorView.swift`
- [ ] **3.3.1** Replace camera-capture stub: wire `onUseImage` → `AIRecognitionViewModel.start`; present Loading→Error/Confirmation; stub `onConfirm` until `confirmation-edit`
  - Refs: AC-001.3
  - Design: 8
  - File: `App/RootView.swift`, `Features/Camera/Views/CameraView.swift`

**Phase Gate 3 (end of Feature phase):** Run XcodeBuildMCP `discover_projs -> list_schemes -> build_sim`, then traceability check (AC-001.3/.4, AC-002.*, AC-003.3, AC-004.3/.4/.5 covered; camera→loading flow builds; Refs Design resolve).

## 3. Integration Tasks
> Unit tests + build/integration gate.

- [ ] **4.1.1** `VisionResponseParserTests` — valid→draft; ranges; macro±10%→lowQuality; empty/out-of-range→throw
  - Refs: AC-001.2, AC-003.1, AC-003.2, AC-003.4
  - Design: 6
  - File: `calo-ai-testTests/VisionResponseParserTests.swift`
- [ ] **4.1.2** `VisionAPIServiceTests` (`URLProtocol` stub) — HTTPS-only, key from config, 10s timeout, transient retry≤3, decode-or-throw
  - Refs: AC-001.1, AC-004.1, AC-004.2
  - Design: 6
  - File: `calo-ai-testTests/VisionAPIServiceTests.swift`
- [ ] **4.1.3** `AIRecognitionViewModelTests` (fake service/reachability) — offline fail-fast; ≥70→onConfirm; <70→warning; invalid→error; cancel/retry/back
  - Refs: AC-001.3, AC-001.4, AC-002.2, AC-002.4, AC-003.3, AC-004.3, AC-004.4, AC-004.5
  - Design: 6
  - File: `calo-ai-testTests/AIRecognitionViewModelTests.swift`
- [ ] **4.2.1** Build + integration gate: `build_sim` green; camera→loading→(confirm stub / error) flow exercised
  - Refs: AC-002.1
  - Design: 6
  - File: (build gate)

**Phase Gate 4 (end of Integration phase):** Run XcodeBuildMCP `discover_projs -> list_schemes -> build_sim` (+ `test_sim`), then traceability check (all 17 ACs traced to ≥1 done task; every Refs Design resolves).

## Traceability Matrix
| Task ID | AC | Design | Property | Status |
|---|---|---|---|---|
| 2.1.1 | AC-001.2 | 4 | P2 | pending |
| 2.1.2 | AC-001.1 | 7.1 | P1 | pending |
| 2.1.3 | AC-001.2, AC-003.1, AC-003.2, AC-003.4 | 7.3 | P2, P8, P9, P11 | pending |
| 2.1.4 | AC-001.1, AC-004.1, AC-004.2 | 7.1 | P1, P12, P13, P14 | pending |
| 3.1.1 | AC-001.3, AC-001.4, AC-002.2, AC-002.3, AC-002.4, AC-003.3, AC-004.3, AC-004.4, AC-004.5 | 7.4 | P3, P4, P5, P6, P7, P10, P15, P16, P17 | pending |
| 3.2.1 | AC-002.1 | 7.2 | P5 | pending |
| 3.2.2 | AC-004.1 | 7.4 | P12 | pending |
| 3.3.1 | AC-001.3 | 8 | P3 | pending |
| 4.1.1 | AC-001.2, AC-003.1, AC-003.2, AC-003.4 | 6 | P2, P8, P9, P11 | pending |
| 4.1.2 | AC-001.1, AC-004.1, AC-004.2 | 6 | P1, P12, P13, P14 | pending |
| 4.1.3 | AC-001.3, AC-001.4, AC-002.2, AC-002.4, AC-003.3, AC-004.3, AC-004.4, AC-004.5 | 6 | P3, P4, P6, P7, P10, P15, P16, P17 | pending |
| 4.2.1 | AC-002.1 | 6 | P5 | pending |

## Progress
| Section | Total | Done | Status |
|---|---:|---:|---|
| Shared | 4 | 0 | ⬜ |
| Feature | 4 | 0 | ⬜ |
| Integration | 4 | 0 | ⬜ |