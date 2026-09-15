---
doc_id: 08-04
title: Missing Screen Report
phase: 08-screens
skill: screen-inventory-wireframe
profile: Bắt buộc khi làm flow
owner: Designer
reviewers: []
version: 0.1.0
status: draft
last_updated:
approved_by: ""
approved_at: ""
depends_on: [07-05]
feeds: [08-01]
id_prefix: []
gate: G7
in_handover: false
confidence: low
---

# [Tên dự án] — Missing Screen Report

> Tồn tại để thực thi quy tắc: **UX flow không được sinh màn hình mới.**
> Làm flow phát hiện thiếu màn thì ghi vào đây trước, `SCR` cấp ở `08-01`, rồi flow mới trích lại.

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


## 1. Màn hình phát hiện thiếu
| # | Phát hiện khi làm gì | Màn hình cần | Vì sao thiếu | `FLOW` liên quan | Trạng thái |
| --- | --- | --- | --- | --- | --- |
| 1 | `FLOW-003` | | | | Chờ cấp `SCR` |

## 2. Đã cấp mã
| # | Mô tả màn hình | `SCR` đã cấp | Ngày | Flow đã cập nhật |
| --- | --- | --- | --- | --- |

## 3. Đề xuất bị từ chối
| # | Màn hình đề xuất | Vì sao không cần | Ai quyết |
| --- | --- | --- | --- |

## 4. Phân tích nguyên nhân
> Nhiều màn thiếu ở cùng một chỗ là dấu hiệu tài liệu trước đó có lỗ hổng, không phải chỉ là sơ suất.

| Nhóm màn thiếu | Nguyên nhân gốc | Tài liệu cần sửa | `CHG` |
| --- | --- | --- | --- |

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
# Nguồn chân lý DUY NHẤT cho G7 phần tài liệu này. KHÔNG chép khối này vào file đầu ra ở docs/.
doc: 08-04_MISSING_SCREEN_REPORT
gate: G7
required_major:
  - "0. Đọc nhanh"
  - "1. Màn hình phát hiện thiếu"
  - "2. Đã cấp mã"
  - "3. Đề xuất bị từ chối"
  - "4. Phân tích nguyên nhân"
  - "5. Nguồn phương pháp"
  - "Thuật ngữ dùng trong tài liệu này"
required_minor:
  {}
quality_checks:
  - "Mọi màn hình phát sinh đi qua file này trước khi được cấp SCR ở 08-01"
  - "Mục 4 có phân tích nguyên nhân nếu ≥3 màn thiếu cùng nhóm"
  - "Flow đã cập nhật sau khi SCR được cấp"
QUALITY-GATE-MANIFEST:END -->
