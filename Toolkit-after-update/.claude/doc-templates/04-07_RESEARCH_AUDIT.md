---
doc_id: 04-07
title: Research Audit
phase: 04-user
skill: user-research-synthesizer
profile: Bắt buộc
owner: PO
reviewers: []
version: 0.1.0
status: draft
last_updated:
approved_by: ""
approved_at: ""
depends_on: [04-03, 04-04, 04-05, 04-06]
feeds: [05-01]
id_prefix: []
gate: G3
in_handover: false
confidence: low
---

# [Tên dự án] — Research Audit

> Audit **chỉ liệt kê finding, không tự sửa file nguồn**. Người đọc duyệt rồi mới áp dụng.

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


## 1. Kiểm đủ bằng chứng
| Kiểm | Kết quả | Chi tiết |
| --- | --- | --- |
| Mọi `INS` có ≥2 nguồn hoặc ≥3 quan sát | PASS / FAIL | |
| Mọi `JTBD` truy được về `INS` | | |
| Mọi `PER` truy được về `INS` và `JTBD` | | |
| Đã xác định aha moment | | |
| Persona dựa trên hành vi, không chỉ nhân khẩu học | | |

## 2. Kiểm thiên lệch
| Rủi ro | Có xảy ra không | Bằng chứng | Ảnh hưởng tới kết luận nào |
| --- | --- | --- | --- |
| Mẫu chỉ gồm người đã quan tâm sẵn | | | |
| Câu hỏi dẫn dắt | | | |
| Cỡ mẫu quá nhỏ để kết luận | | | |
| Ý định bị đọc như hành vi | | | |
| Vài review được coi là đại diện thị trường | | | |

## 3. Điều CHƯA biết
| # | Chưa biết gì | Ảnh hưởng tới quyết định nào | Cần nghiên cứu thêm không |
| --- | --- | --- | --- |

## 4. Kết luận
| Trường | Nội dung |
| --- | --- |
| **Đủ điều kiện đi tiếp phase 05** | Có / Không |
| Nếu không, cần bổ sung gì | |
| Giả định còn sống khi đi tiếp | `ASM-` |
| DEC ID | |

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
# Nguồn chân lý DUY NHẤT cho G3 phần tài liệu này. KHÔNG chép khối này vào file đầu ra ở docs/.
doc: 04-07_RESEARCH_AUDIT
gate: G3
required_major:
  - "0. Đọc nhanh"
  - "1. Kiểm đủ bằng chứng"
  - "2. Kiểm thiên lệch"
  - "3. Điều CHƯA biết"
  - "4. Kết luận"
  - "5. Nguồn phương pháp"
  - "Thuật ngữ dùng trong tài liệu này"
required_minor:
  {}
quality_checks:
  - "Mục 4 có kết luận đủ hay không đủ điều kiện đi tiếp — điều kiện G3"
  - "Audit không sửa file nguồn, chỉ liệt kê finding"
  - "Mục 3 không bỏ trống"
  - "Mọi FAIL ở mục 1 có hành động tương ứng"
QUALITY-GATE-MANIFEST:END -->
