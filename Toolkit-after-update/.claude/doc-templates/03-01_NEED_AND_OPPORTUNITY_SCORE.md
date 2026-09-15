---
doc_id: 03-01
title: Need Score & Opportunity Score
phase: 03-opportunity
skill: opportunity-validator
profile: Bắt buộc
owner: PO
reviewers: []
version: 0.1.0
status: draft
last_updated:
approved_by: ""
approved_at: ""
depends_on: [01-01, 02-04]
feeds: [03-02]
id_prefix: []
gate: G2
in_handover: false
confidence: low
---

# [Tên dự án] — Need Score & Opportunity Score

> **Ngưỡng đặt trước khi chấm.** Chấm xong mới đặt ngưỡng là tự lừa mình.

## 0. Đọc nhanh

| Câu hỏi | Trả lời ngắn |
| --- | --- |
| **Tài liệu này là gì** | |
| **Ai cần đọc** | |
| **Đọc xong phải biết gì** | |
| **Quyết định nào chốt ở đây** | |

> Bốn dòng này viết **không dùng một thuật ngữ nào**, kể cả thuật ngữ của chính nghề mình. Người mới vào dự
> án — hoặc người ở vai trò khác — đọc bốn dòng là biết có cần đọc tiếp hay không. Để trống hoặc chép lại
> tên tài liệu là chưa làm.


## 1. Ngưỡng đã đặt trước

| Ngưỡng | Giá trị | Ngày đặt | Ai đặt |
| --- | --- | --- | --- |
| Need Score tối thiểu để đi tiếp | **25 / 35** | | |
| Ngưỡng KILL | | | |

## 2. Need Score

Chấm mỗi tiêu chí 1–5. Tổng tối đa 35.

| Tiêu chí | `NC-001` | `NC-002` | Căn cứ chấm |
| --- | --- | --- | --- |
| Tần suất gặp phải | | | |
| Mức độ nghiêm trọng | | | |
| Mức độ cấp bách | | | |
| Ý định chi trả | | | |
| Độ yếu của giải pháp hiện tại | | | |
| Khả năng tiếp cận người dùng | | | |
| Khả năng xây MVP | | | |
| **Tổng / 35** | | | |
| **Đạt ngưỡng 25** | Có / Không | | |

_Cột "căn cứ chấm" bắt buộc. Điểm không có căn cứ là cảm tính._

## 3. Opportunity Score có trọng số

| Yếu tố | Trọng số | `NC-001` | Điểm có trọng số |
| --- | --- | --- | --- |
| Quy mô nhu cầu | | | |
| Mức cạnh tranh (đảo chiều) | | | |
| Khả năng khác biệt | | | |
| Chi phí tiếp cận | | | |
| Khả năng kiếm tiền | | | |
| **Tổng** | | | |

## 4. Kết luận

| Cluster | Need Score | Opportunity Score | Quyết định | DEC ID |
| --- | --- | --- | --- | --- |
| `NC-001` | | | Đi tiếp / Dừng / Xoay hướng | `DEC-` |

> **Nếu không cluster nào đạt 25/35: dừng lại.** Ghi quyết định dừng vào `_DECISION_LOG.md`.
> Dừng ở đây là thắng, không phải thua — bạn vừa tiết kiệm được vài tháng.

## 5. Nguồn phương pháp

## Thuật ngữ dùng trong tài liệu này

Chép nghĩa một câu từ `docs/_GLOSSARY.md` mục *Thuật ngữ chuyên môn*, và nghĩa của tiền tố mã từ
`docs/_ID_REGISTRY.md`. Chỉ liệt kê thứ **thật sự xuất hiện** trong tài liệu này.

| Thuật ngữ / tiền tố mã | Nghĩa một câu |
| --- | --- |
| | |

> Bảng này không phải để người trong nghề đọc — nó dành cho người ở vai trò khác đang phải duyệt tài liệu
> này. `validate_docs.py` đối chiếu: dùng mà không liệt kê là **LỖI**; liệt kê mà không dùng là cảnh báo.

<!-- QUALITY-GATE-MANIFEST:START
# Nguồn chân lý DUY NHẤT cho G2 phần tài liệu này. KHÔNG chép khối này vào file đầu ra ở docs/.
doc: 03-01_NEED_AND_OPPORTUNITY_SCORE
gate: G2
required_major:
  - "0. Đọc nhanh"
  - "1. Ngưỡng đã đặt trước"
  - "2. Need Score"
  - "3. Opportunity Score có trọng số"
  - "4. Kết luận"
  - "5. Nguồn phương pháp"
  - "Thuật ngữ dùng trong tài liệu này"
required_minor:
  {}
quality_checks:
  - "Ngưỡng ở mục 1 có ngày đặt TRƯỚC ngày chấm ở mục 2 — điều kiện G2"
  - "Need Score ≥ 25/35 cho ít nhất một cluster, hoặc có DEC quyết định dừng"
  - "Mọi điểm có căn cứ chấm, không bỏ trống cột căn cứ"
  - "Mục 4 có DEC ID cho mỗi quyết định"
QUALITY-GATE-MANIFEST:END -->
