---
doc_id: 02-03
title: Review Mining
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
depends_on: [02-01]
feeds: [02-04, 04-03]
id_prefix: []
gate: G1
in_handover: false
confidence: low
---

# [Tên dự án] — Review Mining

> Đào review của đối thủ để tìm điều người dùng **thật sự** phàn nàn.
> Review một sao nói nhiều hơn review năm sao.

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


## 1. Phạm vi đào

| Đối thủ | Cửa hàng | Số review đã đọc | Khoảng thời gian | Lọc theo |
| --- | --- | --- | --- | --- |

## 2. Phàn nàn lặp lại

| # | Phàn nàn | Số lần gặp | Đối thủ | Trích dẫn đại diện | Cluster |
| --- | --- | --- | --- | --- | --- |
| 1 | | | `COM-001` | | `NC-001` |

## 3. Yêu cầu tính năng lặp lại

| # | Người dùng xin gì | Số lần | Đối thủ đã làm chưa | Cơ hội |
| --- | --- | --- | --- | --- |

## 4. Điều người dùng khen

> Đọc cả review tốt. Điều được khen nhiều là thứ bạn **phải làm được ít nhất ngang bằng**,
> nếu không thì dù giải quyết đúng pain point vẫn thua.

| # | Được khen gì | Đối thủ | Mức bắt buộc phải có |
| --- | --- | --- | --- |

## 5. Cảnh báo về mẫu

> Vài chục review **không** đại diện cho toàn thị trường. Người viết review lệch về hai cực rất hài lòng
> và rất bực. Ghi rõ giới hạn này.

| Giới hạn của dữ liệu | Ảnh hưởng tới kết luận nào |
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
# Nguồn chân lý DUY NHẤT cho G1 phần tài liệu này. KHÔNG chép khối này vào file đầu ra ở docs/.
doc: 02-03_REVIEW_MINING
gate: G1
required_major:
  - "0. Đọc nhanh"
  - "1. Phạm vi đào"
  - "2. Phàn nàn lặp lại"
  - "3. Yêu cầu tính năng lặp lại"
  - "4. Điều người dùng khen"
  - "5. Cảnh báo về mẫu"
  - "6. Nguồn phương pháp"
  - "Thuật ngữ dùng trong tài liệu này"
required_minor:
  {}
quality_checks:
  - "Mỗi phàn nàn có số lần gặp, không chỉ có một lần"
  - "Có trích dẫn đại diện nguyên văn"
  - "Mục 5 không bỏ trống — phải nêu giới hạn của mẫu"
  - "Mục 4 có ít nhất một mục — không chỉ đào điều xấu"
QUALITY-GATE-MANIFEST:END -->
