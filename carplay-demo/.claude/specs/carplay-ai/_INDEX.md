# Carbina: Car Dashboard & Widgets — Docs Index

**Version**: 2.4 · **Date**: 2026-08-17 · **Snapshot**: **2.4 / 2026-08-07** (khớp toàn bộ 8 tài liệu bên dưới)

> Manifest của bộ tài liệu dự án `carplay-ai`. Agent đọc file này **trước tiên** để biết có gì, đọc theo thứ tự nào, quy ước ID ra sao, và mỗi loại dữ kiện thuộc file nào.
>
> **Sản phẩm**: Carbina — app iOS + CarPlay biến màn hình xe thành dashboard tự thích ứng theo ngữ cảnh. Ba trụ tính năng: âm thanh lên/xuống xe · widget CarPlay tự adapt màn hình · giọng chào AI on-device.

## Files & read order

Thứ tự sinh/đọc — mỗi file chỉ tham chiếu các file phía trên nó:

| # | File | Dòng | Role |
|---|---|---|---|
| 1 | `PRD.md` | 1.504 | Tầm nhìn sản phẩm, nghiên cứu cạnh tranh thực địa, phạm vi, kiếm tiền, 14 rủi ro, KPI |
| 2 | `Project_Overview.md` | 565 | Kiến trúc + kế hoạch (tham chiếu PRD, không lặp lại phân tích thị trường) |
| 3 | `Use_Cases.md` | 4.198 | 36 UC, UC↔screen mapping, 13 task flow, 21 sub-flow, 18 scenario, priorities |
| 4 | `Functional_Requirements.md` | 841 | **Index** + Component Behavior Matrix + Context-Dependent Behaviors + 24 NFR + tổng hợp |
| 4a | `FR_onboarding.md` | 430 | FR-001 → FR-009 (Onboarding & Thiết lập xe) |
| 4b | `FR_sound.md` | 504 | FR-010 → FR-020 (Âm thanh lên/xuống xe) |
| 4c | `FR_widget.md` | 578 | FR-021 → FR-032 (Widget CarPlay & Tương thích) — **nhóm rủi ro R-11** |
| 4d | `FR_voice_dashboard.md` | 489 | FR-033 → FR-042 (Giọng chào AI & Dashboard ngữ cảnh) |
| 4e | `FR_monetization.md` | 574 | FR-043 → FR-054 (Gói Free, Paywall & Thanh toán) |
| 4f | `FR_settings_privacy.md` | 424 | FR-055 → FR-062, FR-066 (Ngôn ngữ, Quyền riêng tư, Phản hồi & Telemetry) |
| 4g | `FR_postmvp.md` | 158 | FR-063 → FR-065 (Post-MVP, `Deferred`) |
| 5 | `Wireframes.md` | 4.879 | 30 màn hình + ASCII layout theo archetype + 2 audit (Affordance→FR, Component Consistency) |
| 6 | `UX_Flows.md` | 1.516 | 7 journey, 12 nhóm flow điều hướng, 15 UX enhancement flow, 28 diagram Mermaid |
| 7 | `Project_Implementation_Roadmap.md` | 1.415 | 27 spec, 11 phase, dependency graph, Scope Decision Record, traceability 3 chiều |

**Tài liệu hỗ trợ** (ngoài pipeline, được các file trên tham chiếu):

| File | Role |
|---|---|
| `research/mycar-deep-dive.md` | Deep-dive đối thủ #1 (myCar) — nguồn của R-10, R-11, R-12 |
| `research/appstorespy-competitor-data.md` | Dữ liệu niche AppStoreSpy — cơ sở của R-08 (tỉ lệ takedown cluster) |
| `research/feature-tiers-and-competitor-matrix.md` | Ma trận tính năng & phân tầng Free/Premium |
| `../../shared/DESIGN_TOKEN_BENTO_GRID.json` | Design token `bento-grid` — trích từ `.claude/design-token/template-bento.pen` (77 biến, đủ cặp light/dark) |

## ID conventions

| Prefix | Meaning | Example | Số lượng |
|---|---|---|---|
| `UC-XXX` | Use case | UC-001 | **36** |
| `AC-XXX.Y` | Acceptance criterion (EARS: WHEN/IF…THEN) | AC-015.7 | **166** |
| `AF-XXX.Y` | Alternative / error flow | AF-010.1 | **113** |
| `FR-XXX` | Functional requirement | FR-029 | **66** |
| `NFR-XXX` | Non-functional requirement | NFR-019 | **24** |
| `BR-XXX.Y` | Business rule | BR-029.1 | **206** |
| `VR-XXX.Y` | Validation rule | VR-032.2 | **87** |
| `ERR-XXX.Y` | Error scenario | ERR-031.2 | **183** |
| `WF-XXX` | Wireframe screen | WF-017 | **30** |
| `TF-XXX` | Task flow (xuyên màn hình) | TF-003 | **13** |
| `SF-XXX` | Sub-flow (trong một màn hình) | SF-017 | **21** |
| `R-XX` | Risk (PRD §13) | R-11 | **14** |

**IDs là ổn định trên toàn bộ bộ tài liệu — không bao giờ đánh số lại; item mới nhận ID mới.**

> **Lưu ý về số của AC**: `AC-015.7` là criterion thứ 7 của **UC-015**, không phải của FR-015. AC gắn với UC; `Functional_Requirements.md` mang nguyên chúng sang, giữ đúng số gốc.

## Single source of truth (mỗi dữ kiện thuộc file nào)

| Kind of fact | Authoritative file |
|---|---|
| **Phạm vi / MVP definition + priority legend** | `Project_Implementation_Roadmap.md` → **Scope Decision Record** |
| **Effort / duration / timeline** | `Project_Implementation_Roadmap.md` → Phase Timeline + Estimation Assumptions *(Use_Cases chỉ mang priority + complexity, KHÔNG mang số ngày)* |
| Giá / kiếm tiền | `PRD.md` §11 · **4 bậc giá** định nghĩa duy nhất ở `paywall` spec (FR-046) |
| Default cho câu hỏi mở `(ASSUMPTION)` | `PRD.md` §14 |
| Phân tích cạnh tranh, rủi ro R-01…R-14 | `PRD.md` §4, §13 |
| Kiến trúc, tech stack, 7 quyết định kiến trúc | `Project_Overview.md` §3 |
| Hành vi người dùng, task flow, sub-flow | `Use_Cases.md` |
| **Hành vi hệ thống / AC / BR / VR / ERR** | `Functional_Requirements.md` + 7 sub-spec |
| **Màn hình & layout** | `Wireframes.md` |
| **Design token** (màu, font, spacing, shadow, animation) | `DESIGN_TOKEN_BENTO_GRID.json` — nếu Figma lệch với file này thì **file này thắng** |
| **Đường điều hướng, chrome (tab bar, back, sheet, alert)** | `UX_Flows.md` §4 |
| **Luật điều hướng CarPlay** (không stack/modal/nhập liệu, 1 chạm) | `UX_Flows.md` §4.4 |
| **Dependency graph (machine-readable)** | `Project_Implementation_Roadmap.md` → Machine-Readable Dependencies |
| Sở hữu màn hình (WF → spec) | `Project_Implementation_Roadmap.md` → Feature→Screen Mapping |
| Affordance nằm trên màn hình của spec khác | `Project_Implementation_Roadmap.md` → Affordance Ownership |

### Cơ chế dùng chung — định nghĩa MỘT nơi, nơi khác tham chiếu

| Cơ chế | Định nghĩa duy nhất ở |
|---|---|
| 4 bậc giá (không weekly) | `FR_monetization.md` FR-046 |
| Huỷ đăng ký (qua trang subscription iOS) | `FR_monetization.md` FR-053 |
| Phục hồi giao dịch (3 điểm khởi phát, 1 hàm) | `FR_onboarding.md` FR-003 |
| Cấu hình gói Free (1 widget + 3 sound + 3 thẻ) | `FR_monetization.md` FR-044 |
| Layout engine CarPlay (bounds runtime, 0 hằng số) | `FR_widget.md` FR-029 |
| Chính sách nhường phiên audio | `FR_sound.md` FR-017 |
| 28 event schema (0 PII) | `FR_settings_privacy.md` FR-066 |
| App Group container (lối duy nhất app ↔ widget) | `Project_Overview.md` §3.2 |

## For coding agents

**Đường đọc thực dụng khi thi công:**

1. Bắt đầu từ `Project_Implementation_Roadmap.md` → khối **JSON Machine-Readable Dependencies** để lấy spec + thứ tự phụ thuộc.
2. Với mỗi spec, đọc cột `Covers` (FR / UC / WF) rồi truy về:
   - **FR** → sub-spec `FR_*.md` tương ứng (Description · Input · Processing · Output · BR · VR · ERR · AC)
   - **WF** → `Wireframes.md` §3 (archetype · visual hierarchy · content zones · layout ASCII · states · user flow)
   - **UC** → `Use_Cases.md` §2 (main flow · alternative flows · context variations)
3. Đọc `UX_Flows.md` §4 trước khi viết bất kỳ điều hướng nào — chrome và luật CarPlay ở đó.
4. Mọi giá trị thị giác lấy từ `DESIGN_TOKEN_BENTO_GRID.json`, **không hardcode**.

**Bốn ràng buộc cứng, kiểm ở code review chứ không ở runtime:**

| # | Ràng buộc | Nguồn |
|---|---|---|
| 1 | **0 hằng số kích thước màn hình xe** trong code layout CarPlay — mọi kích thước tính từ `CPTemplateApplicationScene` bounds tại runtime | BR-029.1 · AC-NFR-021.1 |
| 2 | **Chỉ một điểm gọi StoreKit purchase**, và nó nằm **sau** WF-011 | BR-048.1 · VR-048.2 |
| 3 | **0 đường mở paywall** từ bề mặt CarPlay (WF-016 → WF-019) | BR-045.3 |
| 4 | Widget extension **không** nạp Core ML và **không** gọi mạng; ảnh ≤ 2MB | BR-029.3 · NFR-007 |

**Bốn FR không được cắt trong mọi trường hợp** (lớp phòng vệ rủi ro, không phải tính năng bán được): **FR-008** (dùng được khi từ chối quyền) · **FR-031** (fallback khi render lỗi) · **FR-032** (chẩn đoán) · **FR-044** (gói Free).

**Spec khởi đầu**: `project-structure` → `shared-foundations` → `telemetry-core` → `widget-render`.

Toàn bộ tài liệu dùng chung snapshot **2.4 / 2026-08-07**.
