---
doc_id: 02-04
title: Opportunity Gap
phase: 02-competitor
skill: competitor-intel
profile: Bắt buộc
owner: PO
reviewers: []
version: 0.1.0
status: draft
last_updated:
approved_by: ""
approved_at: ""
depends_on: [01-01, 02-01, 02-02, 02-03]
feeds: [03-01, 03-02]
id_prefix: [GAP]
gate: G1
in_handover: true
confidence: low
---

# [Tên dự án] — Opportunity Gap

> Khoảng trống phải có **bằng chứng**, không phải suy diễn. Đây là điều kiện đóng G1.

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


## 1. Khoảng trống đã xác định

### GAP-001 · [tên ngắn]

| Trường | Nội dung |
| --- | --- |
| Mô tả khoảng trống | |
| Nhu cầu liên quan | `NC-001` |
| Bằng chứng | `PN-003`, `PN-011`, review mining mục 2 dòng 4 |
| Vì sao đối thủ chưa lấp | |
| Đây có phải lý do chính đáng không | _Đối thủ không làm vì khó, vì không đáng, hay vì chưa nghĩ tới?_ |
| Mức độ tin cậy | `[INSIGHT]` / `[HYP]` |

## 2. Bảng tổng hợp

| ID | Khoảng trống | Nhu cầu | Số bằng chứng | Đối thủ nào chưa lấp | Độ tin cậy |
| --- | --- | --- | --- | --- | --- |

## 3. Khoảng trống đã loại

> Ghi lại để không nghĩ lại. Nhiều khoảng trống trông hấp dẫn nhưng đối thủ không lấp **vì lý do chính đáng**.

| Khoảng trống | Vì sao loại |
| --- | --- |

## 4. Nguồn phương pháp

## Thuật ngữ dùng trong tài liệu này

Chép nghĩa một câu từ `docs/_GLOSSARY.md` mục *Thuật ngữ chuyên môn*, và nghĩa của tiền tố mã từ
`docs/_ID_REGISTRY.md`. Chỉ liệt kê thứ **thật sự xuất hiện** trong tài liệu này.

| Thuật ngữ / tiền tố mã | Nghĩa một câu |
| --- | --- |
| | |

> Bảng này không phải để người trong nghề đọc — nó dành cho người ở vai trò khác đang phải duyệt tài liệu
> này. `validate_docs.py` đối chiếu: dùng mà không liệt kê là **LỖI**; liệt kê mà không dùng là cảnh báo.

<!-- QUALITY-GATE-MANIFEST:START
# Nguồn chân lý DUY NHẤT cho G1 phần tài liệu này. KHÔNG chép khối này vào file đầu ra ở docs/.
doc: 02-04_OPPORTUNITY_GAP
gate: G1
required_major:
  - "0. Đọc nhanh"
  - "1. Khoảng trống đã xác định"
  - "2. Bảng tổng hợp"
  - "3. Khoảng trống đã loại"
  - "4. Nguồn phương pháp"
  - "Thuật ngữ dùng trong tài liệu này"
required_minor:
  {}
quality_checks:
  - "Mỗi GAP có ít nhất một bằng chứng truy được về PN hoặc review mining — điều kiện G1"
  - "Mỗi GAP trả lời được câu vì sao đối thủ chưa lấp"
  - "Mục 3 không rỗng — phải có khoảng trống đã cân nhắc và loại"
QUALITY-GATE-MANIFEST:END -->
