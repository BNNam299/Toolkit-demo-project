---
doc_id: _INDEX
title: Bảng điều khiển dự án
owner: PO
version: 0.1.0
status: draft
---

# _INDEX — Bảng điều khiển

> File này **sống từ phase 00**, không phải sản phẩm cuối. Cập nhật sau **mỗi** tài liệu được duyệt.
> Đây là thứ nên mở ra đọc 5 phút mỗi tuần.

## 1. Thông tin dự án

| Trường | Giá trị |
| --- | --- |
| Tên dự án | _TBD_ |
| Nền tảng | _TBD_ |
| **Profile đang dùng** | _Lean / MVP / Full — chọn và ghi lý do_ |
| Ngày bắt đầu | _TBD_ |
| Phiên bản bộ mẫu | _xem `.claude/KIT_MANIFEST.md`_ |
| **Định mức bằng chứng** | _mặc định — xem `AGENTS.md` mục Định mức tối thiểu_ |
| Phase hiện tại | 00 |
| Cổng đã đóng | — |

## 2. Trạng thái tài liệu

Ký hiệu: ⬜ chưa bắt đầu · 🟨 draft · 🟦 in-review · ✅ approved · ⬛ superseded/archived · ⏭️ bỏ theo profile

| doc_id | Tài liệu | Thư mục | Profile | Owner | Skill | Cổng | Bàn giao | Trạng thái | Version |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `00-01` | PROJECT_BRIEF | `00-khoi-tao` | Bắt buộc | PO | `doc-orchestrator` | G0 | Có | ⬜ chưa bắt đầu | — |
| `00-02` | SCOPE_LOCK | `00-khoi-tao` | Bắt buộc | PO | `doc-orchestrator` | G0 | Có | ⬜ chưa bắt đầu | — |
| `01-01` | MARKET_AND_NEED_ZONE | `01-market` | Bắt buộc | PO | `market-niche-scout` | G1 | — | ⬜ chưa bắt đầu | — |
| `01-02` | PAIN_MINING_LOG | `01-market` | Bắt buộc | PO | `market-niche-scout` | G1 | — | ⬜ chưa bắt đầu | — |
| `02-01` | COMPETITOR_LANDSCAPE | `02-competitor` | Bắt buộc | PO | `competitor-intel` | G1 | Có | ⬜ chưa bắt đầu | — |
| `02-02` | COMPETITOR_TEARDOWN | `02-competitor` | Bắt buộc | PO | `competitor-intel` | G1 | — | ⬜ chưa bắt đầu | — |
| `02-03` | REVIEW_MINING | `02-competitor` | Bắt buộc | PO | `competitor-intel` | G1 | — | ⬜ chưa bắt đầu | — |
| `02-04` | OPPORTUNITY_GAP | `02-competitor` | Bắt buộc | PO | `competitor-intel` | G1 | Có | ⬜ chưa bắt đầu | — |
| `03-01` | NEED_AND_OPPORTUNITY_SCORE | `03-opportunity` | Bắt buộc | PO | `opportunity-validator` | G2 | — | ⬜ chưa bắt đầu | — |
| `03-02` | CONCEPT_CANDIDATES | `03-opportunity` | Bắt buộc | PO | `opportunity-validator` | G2 | Có | ⬜ chưa bắt đầu | — |
| `03-03` | VALIDATION_PLAN | `03-opportunity` | Khuyến nghị mạnh | PO | `opportunity-validator` | G2 | — | ⬜ chưa bắt đầu | — |
| `03-04` | VALIDATION_RESULT | `03-opportunity` | Có điều kiện | PO | `opportunity-validator` | G2 | — | ⬜ chưa bắt đầu | — |
| `03-05` | TECH_FEASIBILITY_BRIEF | `03-opportunity` | Bắt buộc | PO | `opportunity-validator` | G2 | Có | ⬜ chưa bắt đầu | — |
| `04-01` | RESEARCH_PLAN_AND_GUIDE | `04-user` | Có điều kiện | PO | `user-research-synthesizer` | G3 | — | ⬜ chưa bắt đầu | — |
| `04-02` | RESEARCH_LOG | `04-user` | Bắt buộc | PO | `user-research-synthesizer` | G3 | — | ⬜ chưa bắt đầu | — |
| `04-03` | USER_INSIGHTS | `04-user` | Bắt buộc | PO | `user-research-synthesizer` | G3 | Có | ⬜ chưa bắt đầu | — |
| `04-04` | JOBS_TO_BE_DONE | `04-user` | Bắt buộc | PO | `user-research-synthesizer` | G3 | Có | ⬜ chưa bắt đầu | — |
| `04-05` | PERSONA | `04-user` | Bắt buộc | PO | `user-research-synthesizer` | G3 | Có | ⬜ chưa bắt đầu | — |
| `04-06` | CUSTOMER_JOURNEY | `04-user` | Bắt buộc | PO | `user-research-synthesizer` | G3 | Có | ⬜ chưa bắt đầu | — |
| `04-07` | RESEARCH_AUDIT | `04-user` | Bắt buộc | PO | `user-research-synthesizer` | G3 | — | ⬜ chưa bắt đầu | — |
| `04-08` | EMPATHY_MAP | `04-user` | Khuyến nghị mạnh | PO | `user-research-synthesizer` | G3 | Có | ⬜ chưa bắt đầu | — |
| `05-01` | PRD | `05-prd` | Bắt buộc | PO | `prd-architect` | G4 | Có | ⬜ chưa bắt đầu | — |
| `05-02` | PRD_AUDIT | `05-prd` | Bắt buộc | PO | `prd-architect` | G4 | — | ⬜ chưa bắt đầu | — |
| `05-03` | PROJECT_OVERVIEW | `05-prd` | Bắt buộc | PO | `prd-architect` | G4 | Có | ⬜ chưa bắt đầu | — |
| `06-00` | FEATURE_BRIEF_FOR_DEV | `06-breakdown` | Bắt buộc | PO | `product-breakdown` | G5 | Có | ⬜ chưa bắt đầu | — |
| `06-01` | USE_CASES | `06-breakdown` | Bắt buộc | PO | `product-breakdown` | G5 | Có | ⬜ chưa bắt đầu | — |
| `06-02` | FUNCTIONAL_REQUIREMENTS | `06-breakdown` | Bắt buộc | PO | `product-breakdown` | G5 | Có | ⬜ chưa bắt đầu | — |
| `06-03` | NON_FUNCTIONAL_REQUIREMENTS | `06-breakdown` | Bắt buộc | PO | `product-breakdown` | G5 | Có | ⬜ chưa bắt đầu | — |
| `06-04` | BUSINESS_RULES | `06-breakdown` | Bắt buộc | PO | `product-breakdown` | G5 | Có | ⬜ chưa bắt đầu | — |
| `06-05` | PERMISSION_AND_DATA_NEEDS | `06-breakdown` | Bắt buộc | PO | `product-breakdown` | G5 | Có | ⬜ chưa bắt đầu | — |
| `07-00` | UX_RESEARCH | `07-structure` | Bắt buộc | PO | `ux-structure-architect` | G6 | Có | ⬜ chưa bắt đầu | — |
| `07-01` | TASK_ANALYSIS | `07-structure` | Bắt buộc | Designer | `ux-structure-architect` | G6 | — | ⬜ chưa bắt đầu | — |
| `07-02` | INFORMATION_ARCHITECTURE | `07-structure` | Bắt buộc | Designer | `ux-structure-architect` | G6 | — | ⬜ chưa bắt đầu | — |
| `07-03` | SITEMAP | `07-structure` | Bắt buộc | Designer | `ux-structure-architect` | G6 | — | ⬜ chưa bắt đầu | — |
| `07-04` | USER_STORY_MAP | `07-structure` | Bắt buộc | PO | `ux-structure-architect` | G6 | Có | ⬜ chưa bắt đầu | — |
| `07-05` | UX_FLOWS | `07-structure` | Bắt buộc | Designer | `ux-structure-architect` | G6 | Có | ⬜ chưa bắt đầu | — |
| `08-01` | SCREEN_INVENTORY | `08-screens` | Bắt buộc | Designer | `screen-inventory-wireframe` | G7 | Có | ⬜ chưa bắt đầu | — |
| `08-02` | STATE_MATRIX | `08-screens` | Bắt buộc | Designer | `screen-inventory-wireframe` | G7 | Có | ⬜ chưa bắt đầu | — |
| `08-03` | WIREFLOWS | `08-screens` | Bắt buộc | Designer | `screen-inventory-wireframe` | G7 | Có | ⬜ chưa bắt đầu | — |
| `08-04` | MISSING_SCREEN_REPORT | `08-screens` | Bắt buộc khi làm flow | Designer | `screen-inventory-wireframe` | G7 | — | ⬜ chưa bắt đầu | — |
| `09-01` | ONBOARDING_SPEC | `09-growth` | Bắt buộc | PO | `growth-and-copy` | G8 | Có | ⬜ chưa bắt đầu | — |
| `09-02` | MONETIZATION_PAYWALL_SPEC | `09-growth` | Bắt buộc | PO | `growth-and-copy` | G8 | Có | ⬜ chưa bắt đầu | — |
| `09-03` | ENGAGEMENT_RETENTION_NOTIFICATION | `09-growth` | Có điều kiện | PO | `growth-and-copy` | G8 | Có | ⬜ chưa bắt đầu | — |
| `09-04` | EXPERIMENT_PLAN | `09-growth` | Có điều kiện | PO | `growth-and-copy` | G8 | — | ⬜ chưa bắt đầu | — |
| `09-05` | VOICE_AND_TONE | `09-growth` | Có điều kiện | PO | `growth-and-copy` | G8 | — | ⬜ chưa bắt đầu | — |
| `09-06` | COPY_DECK | `09-growth` | Bắt buộc | PO | `growth-and-copy` | G8 | Có | ⬜ chưa bắt đầu | — |
| `09-07` | UX_WRITING_REVIEW | `09-growth` | Có điều kiện | PO | `growth-and-copy` | G8 | — | ⬜ chưa bắt đầu | — |
| `10-01` | KPI_FRAMEWORK | `10-measurement` | Bắt buộc | PO | `measurement-designer` | G8 | Có | ⬜ chưa bắt đầu | — |
| `10-02` | EVENT_TAXONOMY | `10-measurement` | Bắt buộc | PO | `measurement-designer` | G8 | Có | ⬜ chưa bắt đầu | — |
| `10-03` | FUNNEL_DEFINITION | `10-measurement` | Bắt buộc | PO | `measurement-designer` | G8 | Có | ⬜ chưa bắt đầu | — |
| `11-01` | DESIGN_REVIEW | `11-evaluation` | Bắt buộc | Designer | `design-quality-auditor` | G9 | — | ⬜ chưa bắt đầu | — |
| `11-02` | USABILITY_EVALUATION | `11-evaluation` | Có điều kiện | Designer | `design-quality-auditor` | G9 | — | ⬜ chưa bắt đầu | — |
| `11-03` | PRE_HANDOVER_FIX_LIST | `11-evaluation` | Bắt buộc | PO | `design-quality-auditor` | G9 | — | ⬜ chưa bắt đầu | — |
| `12-00` | UI_RESEARCH | `12-prototype` | Bắt buộc | Designer | `figma-prototype-spec` | G10 | Có | ⬜ chưa bắt đầu | — |
| `12-01` | PROTOTYPE_BUILD_SPEC | `12-prototype` | Bắt buộc | Designer | `figma-prototype-spec` | G10 | Có | ⬜ chưa bắt đầu | — |
| `12-02` | DESIGN_SYSTEM_AND_A11Y | `12-prototype` | Bắt buộc | Designer | `figma-prototype-spec` | G10 | Có | ⬜ chưa bắt đầu | — |
| `12-03` | PROTOTYPE_REVIEW | `12-prototype` | Bắt buộc | Designer | `figma-prototype-spec` | G10 | — | ⬜ chưa bắt đầu | — |
| `13-01` | HANDOVER_PACKAGE | `13-handover` | Bắt buộc | PO | `dev-handover` | G11 | Có | ⬜ chưa bắt đầu | — |
| `13-02` | DEV_QUESTION_LOG | `13-handover` | Bắt buộc — mở từ phase 03 | PO | `dev-handover` | G11 | — | ⬜ chưa bắt đầu | — |
| `13-03` | TECH_INPUT_CONTRACT | `13-handover` | Bắt buộc | PO | `dev-handover` | G11 | — | ⬜ chưa bắt đầu | — |
| `13-04` | ACCEPTANCE_CRITERIA_PACK | `13-handover` | Bắt buộc | PO | `dev-handover` | G11 | Có | ⬜ chưa bắt đầu | — |

## 3. Tiến độ theo cổng

| Cổng | Sau phase | Trạng thái | Ngày đóng | Ghi chú |
| --- | --- | --- | --- | --- |
| G0 | 00 | ⬜ | | |
| G1 | 01–02 | ⬜ | | |
| G2 | 03 | ⬜ | | |
| G3 | 04 | ⬜ | | |
| G4 | 05 | ⬜ | | |
| G5 | 06 | ⬜ | | |
| G6 | 07 | ⬜ | | |
| G7 | 08 | ⬜ | | |
| G8 | 09–10 | ⬜ | | |
| G9 | 11 | ⬜ | | |
| G10 | 12 | ⬜ | | |
| G11 | 13 | ⬜ | | |

## 4. Ma trận truy nguyên

Chuỗi chuẩn, không được đứt ở khâu nào:

```
PN/NC → GAP → CPT → INS → JTBD → PER → FEAT → UC → FR → FLOW → SCR → ST → CPY → EVT → KPI → AC
```

| Khâu | Số hạng mục | Đã nối xuôi | Đã nối ngược | Ghi chú |
| --- | --- | --- | --- | --- |
| | | | | |

## 5. Báo cáo mồ côi

Chạy trước **mỗi** cổng. Bốn dòng in đậm là nghiêm trọng nhất.

| # | Loại mồ côi | Số lượng | Danh sách ID | Xử lý |
| --- | --- | --- | --- | --- |
| 1 | Pain point không dẫn tới concept | | | |
| 2 | Concept không dựa trên pain point | | | |
| 3 | Insight không dùng ở đâu | | | |
| 4 | Persona không xuất hiện trong flow | | | |
| 5 | **Tính năng không có use case** | | | |
| 6 | **Use case không có requirement** | | | |
| 7 | Requirement không có acceptance criteria | | | |
| 8 | Flow tham chiếu SCR không tồn tại | | | |
| 9 | **Màn hình không xuất hiện trong flow nào** | | | |
| 10 | State matrix còn ô `?` | | | |
| 11 | Màn hình có chữ mà không có CPY | | | |
| 12 | **Event không phục vụ KPI nào / KPI không tính được từ event** | | | |

## 6. Cổng bị bỏ và mâu thuẫn

Cổng có thể bỏ, nhưng phải bỏ **có ý thức**. Tài liệu bị loại khỏi profile cũng ghi vào đây.

| Loại | Cổng / tài liệu | Lý do | Rủi ro | Ghi ở đâu | Ngày |
| --- | --- | --- | --- | --- | --- |
| | | | | | |

Mâu thuẫn giữa hai tài liệu (tài liệu sở hữu thắng):

| # | Mâu thuẫn | File A | File B | Bên thắng | Trạng thái |
| --- | --- | --- | --- | --- | --- |
| | | | | | |

## 7. Nhật ký cập nhật

| Ngày | Việc | Người |
| --- | --- | --- |
| | | |

## 8. Sổ đổi công cụ

Ghi mỗi lần đổi agent — hết hạn mức, đổi máy, hoặc thử công cụ khác. Trạng thái dự án nằm trên ổ đĩa nên
đổi công cụ không mất gì, nhưng **giọng văn và độ sâu tài liệu sẽ lệch**, và sổ này là thứ duy nhất cho
bạn biết chỗ nào cần soi kỹ khi đọc lại.

| Ngày | Từ công cụ | Sang công cụ | Đang dở ở tài liệu nào | Lý do đổi |
| --- | --- | --- | --- | --- |
| | Claude Code | Codex / OpenCode / … | | hết hạn mức / đổi máy / … |

**Đổi ở ranh giới, đừng đổi giữa chừng.** Tốt nhất là đổi sau khi một tài liệu đã `approved`; tốt nhì là
sau khi một cổng đã đóng. Đổi giữa lúc đang viết dở một tài liệu là trường hợp tệ nhất — xem cách xử lý ở
`AGENTS.md` mục *Tiếp nhận dự án đang dở của agent khác*.
