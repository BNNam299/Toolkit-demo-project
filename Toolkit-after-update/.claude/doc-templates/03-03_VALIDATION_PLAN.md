---
doc_id: 03-03
title: Validation Plan
phase: 03-opportunity
skill: opportunity-validator
profile: Khuyến nghị mạnh
owner: PO
reviewers: []
version: 0.1.0
status: draft
last_updated:
approved_by: ""
approved_at: ""
depends_on: [03-02]
feeds: [03-04]
id_prefix: [VAL]
gate: G2
in_handover: false
confidence: low
---

# [Tên dự án] — Validation Plan

> **PASS/KILL đặt trước khi chạy.** Đặt sau khi thấy số liệu là tự lừa mình.

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


## 1. Giả thuyết cần kiểm

### VAL-001

| Trường | Nội dung |
| --- | --- |
| Giả thuyết | _Chúng tôi tin rằng…_ |
| Concept liên quan | `CPT-001` |
| Vì sao đây là giả thuyết rủi ro nhất | |
| **Điều kiện bác bỏ** | _Nếu … xảy ra thì giả thuyết này sai_ |

## 2. Phương pháp kiểm chứng

| VAL | Phương pháp | Vì sao chọn | Chi phí | Thời gian |
| --- | --- | --- | --- | --- |
| `VAL-001` | Fake door / Landing page / Ad test / Interview / Waitlist / Concierge | | | |

## 3. Ngưỡng PASS / KILL — đặt trước

| VAL | Chỉ số đo | **PASS nếu** | **KILL nếu** | Vùng xám thì làm gì | Ngày đặt |
| --- | --- | --- | --- | --- | --- |
| `VAL-001` | | | | | |

## 4. Thiết kế kiểm chứng

| VAL | Đối tượng | Cỡ mẫu | Kênh tiếp cận | Thời gian chạy | Rủi ro thiên lệch |
| --- | --- | --- | --- | --- | --- |

_Rủi ro thiên lệch hay gặp: hỏi bạn bè, câu hỏi dẫn dắt, mẫu chỉ gồm người đã quan tâm sẵn._

## 5. Điều kiện dừng sớm

| Tình huống | Hành động |
| --- | --- |

## 6. Nguồn phương pháp

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
doc: 03-03_VALIDATION_PLAN
gate: G2
required_major:
  - "0. Đọc nhanh"
  - "1. Giả thuyết cần kiểm"
  - "2. Phương pháp kiểm chứng"
  - "3. Ngưỡng PASS / KILL — đặt trước"
  - "4. Thiết kế kiểm chứng"
  - "5. Điều kiện dừng sớm"
  - "6. Nguồn phương pháp"
  - "Thuật ngữ dùng trong tài liệu này"
required_minor:
  {}
quality_checks:
  - "Ngưỡng PASS/KILL có ngày đặt trước ngày chạy — điều kiện G2"
  - "Mỗi VAL có điều kiện bác bỏ rõ ràng"
  - "Mục 4 nêu rủi ro thiên lệch, không bỏ trống"
  - "Cỡ mẫu và kênh tiếp cận cụ thể, không ghi chung chung"
QUALITY-GATE-MANIFEST:END -->
