---
doc_id: 07-01
title: Task Analysis
phase: 07-structure
skill: ux-structure-architect
profile: Bắt buộc
owner: Designer
reviewers: []
version: 0.1.0
status: draft
last_updated:
approved_by: ""
approved_at: ""
depends_on: [06-01, 04-05]
feeds: [07-02, 07-04]
id_prefix: [TSK]
gate: G6
in_handover: false
confidence: low
---

# [Tên dự án] — Task Analysis

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


## 1. Nhiệm vụ chính
| `TSK` | Nhiệm vụ | Persona | `UC` nguồn | Tần suất | Mức quan trọng |
| --- | --- | --- | --- | --- | --- |

## 2. Phân rã nhiệm vụ
### TSK-001 · [tên]
| Cấp | Bước | Người dùng cần biết gì | Người dùng cần quyết gì | Có thể sai ở đâu |
| --- | --- | --- | --- | --- |
| 1 | | | | |
| 1.1 | | | | |

## 3. Điểm ma sát
| # | Bước | Ma sát | Loại | Bỏ được không |
| --- | --- | --- | --- | --- |
| | | | Nhận thức / Thao tác / Chờ đợi / Quyết định | |

## 4. Số bước tới giá trị
| Nhiệm vụ | Số bước hiện tại | Số bước tối thiểu khả thi | Chênh lệch | Bỏ được bước nào |
| --- | --- | --- | --- | --- |

> Đối chiếu với aha moment ở `04-06`. Mỗi bước thừa trước aha moment là một chỗ người dùng rời đi.

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
# Nguồn chân lý DUY NHẤT cho G6 phần tài liệu này. KHÔNG chép khối này vào file đầu ra ở docs/.
doc: 07-01_TASK_ANALYSIS
gate: G6
required_major:
  - "0. Đọc nhanh"
  - "1. Nhiệm vụ chính"
  - "2. Phân rã nhiệm vụ"
  - "3. Điểm ma sát"
  - "4. Số bước tới giá trị"
  - "5. Nguồn phương pháp"
  - "Thuật ngữ dùng trong tài liệu này"
required_minor:
  {}
quality_checks:
  - "Mỗi TSK truy được về một UC"
  - "Mục 4 có số bước cụ thể, không mô tả chung chung"
  - "Đã đối chiếu số bước với aha moment ở 04-06"
QUALITY-GATE-MANIFEST:END -->
