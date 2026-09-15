# Hướng dẫn Project Docs

> Mô tả ngắn từng file template — mục đích, giá trị, sections chính, ID conventions — để người đọc (PO, dev, AI agent) hiểu nhanh và đọc đúng thứ tự.

Hệ thống docs được sinh bởi 3 lệnh:

- `/ios-project-docs` → **7 file project-level** (PRD → Roadmap) + `_INDEX.md`
- `/ios-spec <feature>` → **3 file feature-level** (requirements → design → tasks)
- `/ios-execute <feature>` → **1 file verification-report.md**

---

## Thứ tự đọc

Đọc theo sơ đồ từ trên xuống — mỗi file chỉ tham chiếu file ở phía trên nó:

```
📱 PROJECT LEVEL
  1. PRD.md                      ← chiến lược, thị trường, monetization, KPI
  2. Project_Overview.md         ← kiến trúc + planning summary
  3. Use_Cases.md                ← UC stories + UC↔screen mapping + priority
  4. Functional_Requirements.md  ← FR/NFR + EARS AC + validation rules
  5. Wireframes.md               ← screen inventory + ASCII layouts theo archetype
  6. UX_Flows.md                 ← luồng điều hướng, error/loading flows
  7. Project_Implementation_Roadmap.md ← phases + dependency graph
  8. _INDEX.md                   ← manifest chỉ đường + snapshot

📋 FEATURE LEVEL (cho từng tính năng)
  9. spec-requirements.md  ← user stories + AC
  10. spec-design.md       ← architecture + components
  11. spec-tasks.md        ← task registry + checkpoint

💻 EXECUTION
  12. verification-report.md ← PASS/WARN/FAIL matrix
```

---

## ID Conventions

Cùng một prefix được dùng xuyên suốt — **không bao giờ renumber**, thêm mục mới thì cấp ID mới.

| Prefix | Ý nghĩa | Ví dụ |
|--------|---------|-------|
| `UC-XXX` | Use Case | UC-001 |
| `AC-XXX.Y` | Acceptance criterion (EARS) | AC-001.1 |
| `AF-XXX.Y` | Alternative / error flow | AF-001.1 |
| `FR-XXX` | Functional Requirement | FR-004 |
| `NFR-XXX` | Non-Functional Requirement | NFR-007 |
| `BR/VR/ERR-XXX.Y` | Business / Validation / Error rule | BR-001.2 |
| `WF-XXX` | Wireframe screen | WF-017 |
| `TF-XXX` / `SF-XXX` | Task flow / Sub-flow | TF-002 |
| `Spec-XXX` | Feature spec directory | Spec-auth |

---

## Nhóm A — Project-Level Docs

> Sinh bởi `/ios-project-docs <AppName>`. Mỗi file qua một quality gate (`gate-prd`, `gate-overview`, `gate-uc`, `gate-fr`, `gate-wireframes`, `gate-flows`, `gate-roadmap`) trước khi chuyển sang file kế tiếp.

### 1. PRD.md — Product Requirements Document

**Mục đích**: Tầm nhìn sản phẩm, nghiên cứu thị trường, đối thủ, phạm vi MVP, monetization, KPI.

**Giá trị**:
- Câu trả lời **TẠI SAO** xây dựng sản phẩm và **đo lường thành công bằng gì**
- Là nguồn chân lý duy nhất cho pricing/monetization (§11) và open-question defaults (§14)
- Cung cấp Evidence Table (≥28 nguồn thật) làm đầu vào cho mọi quyết định sản phẩm

**Sections chính**: Tóm tắt điều hành · Mục tiêu & bối cảnh · Vấn đề người dùng · Phân tích cạnh tranh · Tầm nhìn · Phạm vi MVP/Out-of-scope · Yêu cầu & tính năng · Luồng người dùng · Ràng buộc kỹ thuật · Danh sách màn hình · Kiếm tiền · KPI/Analytics · Rủi ro · Câu hỏi mở · Điều phối triển khai · Bảng bằng chứng.

**IDs chính**: không dùng ID, tham chiếu ngược bằng tên section.

**Ai đọc**: PO, stakeholder, người ra quyết định "build or not".

**Ví dụ (Calo-AI)**: §11 đặt pricing cho Premium tier; §14 chốt Default (ASSUMPTION) cho free scan/ngày, độ dài trial → downstream FR/AC/NFR tham chiếu giá trị này.

---

### 2. Project_Overview.md — Project Overview

**Mục đích**: Kiến trúc high-level + planning summary, **tham chiếu PRD** (không lặp lại chiến lược).

**Giá trị**:
- Cầu nối giữa PRD (chiến lược) và Use_Cases/FR (chi tiết) — đọc 1 file nắm được toàn cảnh kỹ thuật
- Định nghĩa tech stack, kiến trúc, persona chính, rủi ro
- Reference policy: tránh duplicate giữa PRD và Overview

**Sections chính**: PRD Reference · Introduction (Problem/Solution/Goals) · Target Users (Personas) · Functional Overview · Technical Architecture · Data Architecture · Integration Points · Constraints · Risks.

**IDs chính**: không tự dùng ID; tham chiếu PRD sections + danh sách persona.

**Ai đọc**: tech lead, dev mới onboard, AI agent cần context.

**Ví dụ (Calo-AI)**: §5 chốt tech stack iOS 16+ SwiftUI/MVVM + Supabase + OpenAI/Anthropic + RevenueCat — mọi spec sau này dùng stack này.

---

### 3. Use_Cases.md — Use Cases

**Mục đích**: UC stories chi tiết + UC↔screen mapping + priority + task flows.

**Giá trị**:
- Câu trả lời **NGƯỜI DÙNG LÀM GÌ** trên app — đọc 1 file biết hết mọi flow
- Creative decomposition: feature explosion (≥3×N sub-features), repetition audit, context storming — chứng minh UC không copy từ PRD
- Screen-Context Use Cases (§4) — mỗi màn hình có UC + secondary actions riêng (settings, share, help...) — chống rơi affordance

**Sections chính**: Creative Decomposition · User Stories by Feature Group · Feature Expression Matrix · UC → Screen Mapping · Screen-Context Use Cases · Task Flows · Sub-Flows & Micro-Interactions · Scenarios (Happy/Edge/Persona) · Priorities (MVP/Post-MVP/Future) · User Journey Map · Screen-Intent Summary.

**IDs chính**: `UC-XXX`, `TF-XXX`, `SF-XXX`, `AF-XXX.Y`.

**Ai đọc**: PO, dev, AI agent sinh FR/Wireframes.

**Ví dụ (Calo-AI)**: §3 map `UC-001 (Đăng ký)` → `WF-Auth-01`; §4 cho biết màn Onboarding có 5 secondary actions (skip, help, share, edit-field, manage) — mỗi cái 1 UC riêng.

---

### 4. Functional_Requirements.md — Functional Requirements

**Mục đích**: WHAT hệ thống phải làm — FR/NFR với EARS acceptance criteria, validation rules, error handling.

**Giá trị**:
- Câu trả lời **HỆ THỐNG PHẢI LÀM GÌ** — bridge giữa UC và Design/Code
- Mỗi FR có AC testable + priority + traceability ngược về UC → "no behavior without acceptance criteria"
- Component Behavior Matrix (§2 bis) + Context-Dependent Behaviors (§2 ter) — chống FR đa màn bị xử lý tệ
- NFR đo được (Performance, Security, Usability, Reliability, Scalability) — không có "nhanh/bảo mật" mơ hồ

**Sections chính**: Introduction · Functional Requirements (per feature group) · Component Behavior Matrix · Context-Dependent Behaviors · Non-Functional Requirements · Requirements Summary.

**IDs chính**: `FR-XXX`, `NFR-XXX`, `BR-XXX.Y` (Business Rule), `VR-XXX.Y` (Validation Rule), `ERR-XXX.Y` (Error Rule), `AC-XXX.Y`.

**Ai đọc**: dev, QA, AI agent viết design/tasks/tests.

**Ví dụ (Calo-AI)**: `FR-004` (Nhận diện món ăn từ ảnh) → AC-004.1 (happy path) + AC-004.2 (low confidence → fallback) + ERR-004.1 (network timeout); mỗi FR có 1 NFR-PERF-001 tương ứng (≤3s).

---

### 5. Wireframes.md — Wireframes

**Mục đích**: Screen inventory + ASCII layouts theo archetype (Discovery/Action/Consumption/Management/Social).

**Giá trị**:
- Câu trả lời **MÀN HÌNH TRÔNG NHƯ THẾ NÀO** — đọc 1 file thấy hết UI
- Screen Taxonomy (Archetype A–E) — mỗi màn phải match archetype template → nhất quán
- Per-screen parts: Visual Hierarchy, Content Zones Map, Layout, Components, States (7 states tối thiểu) — đủ chi tiết để dev vẽ code
- Affordance→FR back-trace (BLOCKING) — Component/Interaction phải map tới FR hoặc khai out-of-scope tường minh

**Sections chính**: Introduction · Screen Inventory · Screen Taxonomy · Screen Sections (theo archetype) · Common Components · Responsive Design · Accessibility · Dark Mode · Design Assets · Figma Integration.

**IDs chính**: `WF-XXX`.

**Ai đọc**: UI/UX designer, dev SwiftUI, AI agent viết View code.

**Ví dụ (Calo-AI)**: `WF-005` (Camera Capture) là Action archetype → dùng template B: Content Zones A (camera preview), B (capture button), C (gallery shortcut), D (utility: flash, settings).

---

### 6. UX_Flows.md — UX Flows

**Mục đích**: User journeys, navigation giữa các màn, error/loading flows — mọi WF-XXX phải xuất hiện ≥1 flow.

**Giá trị**:
- Câu trả lời **NGƯỜI DÙNG ĐI TỪ A ĐẾN B NHƯ THẾ NÀO**
- Coverage gate: mọi WF phải resolve đúng màn đúng loại trong Screen Inventory → ref sai = Fail
- Happy path + Error path + Loading path + Edge case — đủ flow để QA viết test case

**Sections chính**: Introduction · Flow Notation · User Journeys · Navigation Flows · Error/Recovery Flows · Loading States Flows · Cross-Feature Flows.

**IDs chính**: tham chiếu `WF-XXX`, `TF-XXX`, `SF-XXX` từ Use_Cases.

**Ai đọc**: dev, QA, AI agent verify navigation logic.

**Ví dụ (Calo-AI)**: Flow `Capture→AI-Recognition→Confirmation-Edit→Save-Diary`: WF-005 → WF-006 (loading) → WF-007 → WF-008 → WF-009; nếu AI confidence <0.7 → WF-006b (retry).

---

### 7. Project_Implementation_Roadmap.md — Roadmap

**Mục đích**: Phases + Specs + Dependency graph (machine-readable JSON) + Scope Decision Record.

**Giá trị**:
- Câu trả lủ **XÂY THEO THỨ TỰ NÀO** — phases, ước lượng, dependencies
- Scope Decision Record — ghi lại mọi cắt giảm scope (chống mặc nhiên bỏ edge case)
- Dependency graph JSON — AI agent đọc để biết spec nào build trước, phụ thuộc spec nào
- Source of truth cho effort/durations/timeline + Scope/MVP definition

**Sections chính**: Overview · Scope Decision Record · Phases · Specs per Phase · Dependency Graph (JSON) · Effort Estimates · Risks & Mitigations · Timeline.

**IDs chính**: `Spec-XXX`, `Phase-XXX`; tham chiếu `FR-XXX`, `WF-XXX` từ file khác.

**Ai đọc**: PM, dev, AI agent chọn spec để execute.

**Ví dụ (Calo-AI)**: 18 specs × 9 phases × ~13 ngày; Spec-auth phụ thuộc Spec-shared-foundations; Spec-paywall-display phụ thuộc Spec-subscription-management.

---

### 8. _INDEX.md — Docs Index (Manifest)

**Mục đích**: Manifest cho cả bộ docs — agent đọc file này ĐẦU TIÊN để biết file nào tồn tại, thứ tự nào, ID convention, mỗi loại fact sống ở đâu.

**Giá trị**:
- Single entry point cho AI agent — không phải dò từng file
- "Single source of truth" table — biết scope sống ở Roadmap, screens sống ở Wireframes, AC sống ở FR, etc. — tránh duplicate
- Snapshot version cho cả bộ — đảm bảo consistency khi regenerate

**Sections chính**: Files & Read Order · ID Conventions · Single Source of Truth · For Coding Agents (read path).

**IDs chính**: tham chiếu mọi prefix khác.

**Ai đọc**: AI agent (đọc đầu tiên), người mới onboard.

**Ví dụ (Calo-AI)**: bảng "Single source of truth" → biết pricing chỉ ở PRD §11, screen chỉ ở Wireframes.md, AC chỉ ở FR.md → agent không cố tìm ở Use_Cases.

---

## Nhóm B — Feature-Level Docs

> Sinh bởi `/ios-spec <feature>`. Mỗi feature 1 thư mục `specs/[app]/[feature]/` chứa 3 file. Quality gate: `gate-requirements` → `gate-design` → `gate-tasks`.

### 9. spec-requirements.md — Requirements

**Mục đích**: User stories + EARS acceptance criteria cho 1 tính năng — bridge giữa FR project-level và Design feature-level.

**Giá trị**:
- Mỗi AC có traceability ngược về FR-XXX + UC-XXX → biết requirement này phục vụ yêu cầu nào
- Evidence References — chỉ ra market data, KPI liên quan từ PRD → đảm bảo requirement không "trên trời"
- EARS format (Easy Approach to Requirements Syntax) — WHEN/IF/THEN/WHERE — testable rõ ràng

**Sections chính**: Overview · Evidence References · Requirements (per requirement: User Story + ACs + Source + Priority).

**IDs chính**: `AC-XXX.Y`, `AF-XXX.Y`; tham chiếu `FR-XXX`, `UC-XXX`.

**Ai đọc**: dev, QA, AI agent viết design/tasks.

**Ví dụ (Calo-AI Spec-auth)**: Requirement "Đăng nhập bằng Apple" → AC-001.1 (happy) + AC-001.2 (user cancel) + AF-001.1 (network error); source FR-001, UC-001.

---

### 10. spec-design.md — Technical Design

**Mục đích**: Kiến trúc chi tiết cho 1 tính năng — components, interfaces, data flow, AC coverage.

**Giá trị**:
- "Xương" file SwiftUI — dev đọc xong biết cần tạo file nào, ViewModel nào, Service nào
- AC Coverage Summary — liệt kê AC nào được address, AC nào chưa → chống sót
- 4 states per feature (Loading/Empty/Error/Success) + Accessibility & appearance — UX sàn
- Module boundaries + data flow → biết module nào touch vào đâu

**Sections chính**: Overview · Architecture · Components and Interfaces · Data Models · Data Flow · Error Handling · State Behaviors (4 states + a11y) · Testing Strategy.

**IDs chính**: tham chiếu `AC-XXX.Y` từ requirements.md; định nghĩa internal types (ViewModel, Service).

**Ai đọc**: dev chính implement, tech lead review.

**Ví dụ (Calo-AI Spec-auth)**: Components: `LoginView`, `LoginViewModel`, `AuthService`, `AppleAuthProvider`; AC-001.1 được cover bởi `LoginViewModel.loginWithApple()`.

---

### 11. spec-tasks.md — Implementation Plan

**Mục đích**: Task registry machine-readable + Phase gates — danh sách task cần làm, checkpoint để verify.

**Giá trị**:
- Mỗi task có `Refs AC` + `Refs Design` + `Files` + `Checkpoint` → AI agent viết code theo đúng task nào, verify bằng checkpoint nào
- Phase Gates (Gate 2/3/4) — chạy `XcodeBuildMCP build_sim` + traceability check trước khi sang phase tiếp theo
- PBT (Property-Based Testing) required cho mỗi Correctness Property — không phải optional

**Sections chính**: Execution Mode · Task Registry (table) · Phase Gates · Checkpoints · Open Questions.

**IDs chính**: `Task-X.Y.Z`, `PBT-X`; tham chiếu `AC-XXX.Y` và design sections.

**Ai đọc**: AI agent execute (`/ios-execute`), dev review tiến độ.

**Ví dụ (Calo-AI Spec-auth)**: Task 2.1.1 (Create `AuthService`) · Task 2.1.2 (PBT for AuthService) · Task 2.2.1 (Create `LoginView`) · ...; Phase Gate 2 (end of Shared phase) chạy `build_sim`.

---

## Nhóm C — Verification

### 12. verification-report.md — Verification Report

**Mục đích**: PASS/WARN/FAIL matrix sau khi `/ios-execute <feature>` chạy xong — chứng minh feature đã meet requirements.

**Giá trị**:
- Status tổng: PASS / PASS_WITH_WARNINGS / FAIL — quyết định ship hay không
- Completeness matrix: Requirements Coverage / Tasks Completion / Code Files — biết cái gì còn thiếu
- Traceability: FR → Code → Test — chứng minh không sót requirement
- Critical Issues + Warnings + Notes — next action rõ ràng

**Sections chính**: Executive Summary · Completeness · Traceability · Build & Test Results · Quality Metrics · Issues · Recommendations.

**IDs chính**: tham chiếu `Task-X.Y.Z`, `AC-XXX.Y`, `FR-XXX`.

**Ai đọc**: PO, dev, QA, stakeholder quyết định release.

**Ví dụ (Calo-AI Spec-auth)**: Status PASS_WITH_WARNINGS (1 warning: dark mode color chưa verify trên iPad); Completeness 8/8 tasks done, 5/5 FR covered, 12/12 AC tests pass.

---

## Cross-Reference — Đọc gì khi nào

| Mục đích | Đọc file |
|----------|----------|
| Hiểu sản phẩm là gì | PRD + Project_Overview |
| Hiểu 1 màn hình | Wireframes §3 (archetype) + UX_Flows |
| Hiểu 1 use case | Use_Cases §3 + §5 (Task Flows) |
| Hiểu 1 requirement | Functional_Requirements §2 + spec-requirements (nếu có spec) |
| Bắt đầu code 1 tính năng | spec-design §3 (Components) + spec-tasks |
| Verify 1 tính năng xong | verification-report |
| Chọn tính năng làm tiếp | Project_Implementation_Roadmap + _INDEX |

## Single Source of Truth — Mỗi loại fact sống ở đâu

| Loại fact | File duy nhất |
|-----------|---------------|
| Scope / MVP / priority legend | `Project_Implementation_Roadmap.md` → Scope Decision Record |
| Effort / durations / timeline | `Project_Implementation_Roadmap.md` |
| Pricing / monetization | `PRD.md` §11 |
| Open-question defaults (ASSUMPTION) | `PRD.md` §14 |
| Screens & layouts | `Wireframes.md` |
| Requirement behavior / AC | `Functional_Requirements.md` |
| Dependency graph (machine-readable) | `Project_Implementation_Roadmap.md` |
| Persona & user journey | `Use_Cases.md` §8 |
| Tech stack & architecture | `Project_Overview.md` §5–6 |

> **Nguyên tắc**: thông tin đã có ở file A thì KHÔNG lặp ở file B; tham chiếu ngược về A bằng section number.