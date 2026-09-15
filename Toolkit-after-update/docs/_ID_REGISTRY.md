---
doc_id: _ID_REGISTRY
title: Sổ cấp ID
owner: PO
version: 0.1.0
status: draft
---

# _ID_REGISTRY — Sổ cấp ID

Định dạng: `<PREFIX>-<ba chữ số>`, ví dụ `FR-014`.

**Ba quy tắc, vi phạm là hỏng truy nguyên:**

1. ID **không bao giờ đổi**.
2. ID đã bỏ **không bao giờ tái sử dụng** — giữ ở trạng thái `archived`.
3. **Không bao giờ đánh số lại** cả loạt.

Cấp ID mới thì ghi ngay vào đây, đừng để cuối phase mới ghi.

**Nhận ID từ hồ sơ cũ.** Dự án nạp bộ tài liệu đã có sẵn thì **nhận nguyên số cũ**, không đánh số lại — đặt
*Số cuối đã cấp* bằng số lớn nhất đã dùng, ID mới cấp tiếp từ đó. Prefix cũ không có trong bảng dưới thì phải
đổi hoặc thêm vào bảng, ghi ở `research-raw/ho-so-cu/_MAP.md` mục 3 kèm `DEC`. Quy trình:
`.claude/commands/import-legacy.md`.

## Bảng prefix

| Prefix | Hạng mục | Cấp tại | Skill | Số cuối đã cấp | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| `PN` | Pain point | `01-02` | `market-niche-scout` | 000 | |
| `NC` | Need cluster | `01-01` | `market-niche-scout` | 000 | |
| `COM` | Đối thủ | `02-01` | `competitor-intel` | 000 | |
| `GAP` | Khoảng trống cơ hội | `02-04` | `competitor-intel` | 000 | |
| `CPT` | Concept sản phẩm | `03-02` | `opportunity-validator` | 000 | |
| `VAL` | Giả thuyết kiểm chứng | `03-03` | `opportunity-validator` | 000 | |
| `RQ` | Câu hỏi nghiên cứu | `04-01` | `user-research-synthesizer` | 000 | |
| `INS` | Insight | `04-03` | `user-research-synthesizer` | 000 | |
| `JTBD` | Job to be done | `04-04` | `user-research-synthesizer` | 000 | |
| `EMP` | Bản đồ đồng cảm | `04-08` | `user-research-synthesizer` | 000 | |
| `PER` | Persona | `04-05` | `user-research-synthesizer` | 000 | |
| `JRN` | Điểm trong journey | `04-06` | `user-research-synthesizer` | 000 | |
| `CAP` | Năng lực kỹ thuật cốt lõi | `03-05` | `opportunity-validator` | 000 | |
| `PAT` | Mẫu UX/UI quan sát từ đối thủ | `07-00` | `ux-structure-architect` | 000 | |
| `FEAT` | Tính năng | `05-01` | `prd-architect` | 000 | |
| `UC` | Use case | `06-01` | `product-breakdown` | 000 | |
| `FR` | Yêu cầu chức năng | `06-02` | `product-breakdown` | 000 | |
| `NFR` | Yêu cầu phi chức năng | `06-03` | `product-breakdown` | 000 | |
| `BR` | Business rule | `06-04` | `product-breakdown` | 000 | |
| `PRM` | Quyền hệ thống | `06-05` | `product-breakdown` | 000 | |
| `ENT` | Thực thể dữ liệu | `06-05` | `product-breakdown` | 000 | |
| `TSK` | Task | `07-01` | `ux-structure-architect` | 000 | |
| `IA` | Node điều hướng | `07-02` | `ux-structure-architect` | 000 | |
| `US` | User story | `07-04` | `ux-structure-architect` | 000 | |
| `FLOW` | UX flow | `07-05` | `ux-structure-architect` | 000 | |
| `SCR` | Màn hình | `08-01` | `screen-inventory-wireframe` | 000 | |
| `ST` | Trạng thái màn hình | `08-02` | `screen-inventory-wireframe` | 000 | |
| `ONB` | Bước onboarding | `09-01` | `growth-and-copy` | 000 | |
| `PLN` | Gói subscription | `09-02` | `growth-and-copy` | 000 | |
| `TRG` | Trigger giữ chân | `09-03` | `growth-and-copy` | 000 | |
| `NTF` | Thông báo | `09-03` | `growth-and-copy` | 000 | |
| `EXP` | Thí nghiệm | `09-04` | `growth-and-copy` | 000 | |
| `CPY` | Chuỗi văn bản | `09-06` | `growth-and-copy` | 000 | |
| `CW` | Finding UX writing | `09-07` | `growth-and-copy` | 000 | |
| `KPI` | Chỉ số | `10-01` | `measurement-designer` | 000 | |
| `EVT` | Event | `10-02` | `measurement-designer` | 000 | |
| `FNL` | Bước phễu | `10-03` | `measurement-designer` | 000 | |
| `DF` | Finding design | `11-01` | `design-quality-auditor` | 000 | |
| `UF` | Finding usability | `11-02` | `design-quality-auditor` | 000 | |
| `UIP` | Mẫu thị giác từ moodboard | `12-00` | `figma-prototype-spec` | 000 | |
| `TOK` | Design token | `12-02` | `figma-prototype-spec` | 000 | |
| `CMP` | Component | `12-02` | `figma-prototype-spec` | 000 | |
| `AC` | Acceptance criteria | `13-04` | `dev-handover` | 000 | |
| `DQ` | Câu hỏi cho Dev | `13-02` | `dev-handover` | 000 | |
| `DEC` | Quyết định | `_DECISION_LOG` | `doc-orchestrator` | 000 | |
| `CHG` | Thay đổi | `_CHANGE_LOG` | `doc-orchestrator` | 000 | |
| `OQ` | Câu hỏi mở | `_OPEN_QUESTIONS` | `doc-orchestrator` | 000 | |
| `ASM` | Giả định | `_ASSUMPTION_REGISTER` | `doc-orchestrator` | 000 | |

## ID đã bỏ (giữ chỗ, không tái sử dụng)

| ID | Nội dung cũ | Lý do bỏ | Ngày | Thay bằng |
| --- | --- | --- | --- | --- |
| | | | | |

## Hai hệ khoá không dùng số

Hai hệ dưới đây cố ý không đánh số vì được tham chiếu trực tiếp trong code. Chúng vẫn có ID số song song
để tiện trích dẫn trong tài liệu.

**Copy key** — `<màn>.<thành phần>.<biến thể>`, ví dụ `scan.cta.analyze`
**Tên event** — `<đối_tượng>_<hành_động>` snake_case thì quá khứ, ví dụ `paywall_viewed`
