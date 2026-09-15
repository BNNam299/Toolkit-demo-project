---
doc_id: 07-04
title: User Stories & Story Map
phase: 07-structure
skill: ux-structure-architect
profile: Bắt buộc
owner: PO
reviewers: []
version: 0.1.0
status: draft
last_updated:
approved_by: ""
approved_at: ""
depends_on: [07-01, 06-01]
feeds: [12-01]
id_prefix: [US]
gate: G6
in_handover: true
confidence: low
---

# [Tên dự án] — User Stories & Story Map

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


## 1. Khuôn
```
Là [persona], tôi muốn [hành động], để [lợi ích].
```

## 2. Story map
| Xương sống (`TSK`) | → | → |
| --- | --- | --- |
| **Bản 1 — MVP** | `US-001` | `US-002` |
| Bản 2 | | |
| Sau này | | |

## 3. User story
| `US` | Story | `UC` | `FR` | Persona | Ưu tiên | Bản |
| --- | --- | --- | --- | --- | --- | --- |
| `US-001` | Là … tôi muốn … để … | | | | Must | 1 |

## 4. Lát cắt MVP
| Trường | Nội dung |
| --- | --- |
| Lát cắt này cho phép người dùng làm trọn vẹn việc gì | |
| Có đi tới aha moment không | |
| Bỏ story nào thì lát cắt gãy | |

> Lát cắt MVP phải là một **đường đi trọn vẹn**, không phải một nửa của mọi tính năng.

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
doc: 07-04_USER_STORY_MAP
gate: G6
required_major:
  - "0. Đọc nhanh"
  - "1. Khuôn"
  - "2. Story map"
  - "3. User story"
  - "4. Lát cắt MVP"
  - "5. Nguồn phương pháp"
  - "Thuật ngữ dùng trong tài liệu này"
required_minor:
  {}
quality_checks:
  - "Mọi US viết đúng khuôn Là/tôi muốn/để"
  - "Mỗi US nối tới UC và FR"
  - "Lát cắt MVP là đường đi trọn vẹn tới aha moment"
QUALITY-GATE-MANIFEST:END -->
