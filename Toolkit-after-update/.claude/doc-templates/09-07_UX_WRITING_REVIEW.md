---
doc_id: 09-07
title: UX Writing Review
phase: 09-growth
skill: growth-and-copy
profile: Có điều kiện
owner: PO
reviewers: []
version: 0.1.0
status: draft
last_updated:
approved_by: ""
approved_at: ""
depends_on: [09-06]
feeds: [12-03]
id_prefix: [CW]
gate: G8
in_handover: false
confidence: low
---

# [Tên dự án] — UX Writing Review

> Review **chỉ liệt kê finding**, không tự sửa `09-06`. Mỗi finding phải nêu **chỗ nào, vì sao, tác động gì**.
> Không nói chung chung kiểu "viết gọn hơn".

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


## 1. Finding
| `CW` | `CPY` | Bản hiện tại | **Vấn đề** | Nguyên tắc vi phạm | Đề xuất | **Lý do cụ thể** | Mức |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `CW-001` | | | | | | | Cao / TB / Thấp |

## 2. Vấn đề lặp lại
| # | Kiểu vấn đề | Số lần | `CPY` liên quan | Sửa hệ thống thế nào |
| --- | --- | --- | --- | --- |

## 3. Kiểm nhất quán
| Kiểm | Kết quả | Ví dụ vi phạm |
| --- | --- | --- |
| Cùng một thứ gọi cùng một tên | | |
| Nút cùng chức năng dùng cùng nhãn | | |
| Giọng khớp `09-05` | | |
| Khớp `_GLOSSARY` | | |

## 4. Điều KHÔNG khẳng định
> **Không tuyên bố copy mới chắc chắn tăng conversion.** Chỉ nói rõ hơn, đúng hơn, hoặc ngắn hơn.
> Muốn biết có tăng không thì phải chạy `EXP`.

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
# Nguồn chân lý DUY NHẤT cho G8 phần tài liệu này. KHÔNG chép khối này vào file đầu ra ở docs/.
doc: 09-07_UX_WRITING_REVIEW
gate: G8
required_major:
  - "0. Đọc nhanh"
  - "1. Finding"
  - "2. Vấn đề lặp lại"
  - "3. Kiểm nhất quán"
  - "4. Điều KHÔNG khẳng định"
  - "5. Nguồn phương pháp"
  - "Thuật ngữ dùng trong tài liệu này"
required_minor:
  {}
quality_checks:
  - "Mỗi finding nêu rõ chỗ nào, vì sao, tác động gì — không nói chung chung"
  - "Review không sửa 09-06, chỉ liệt kê finding"
  - "Không khẳng định copy mới chắc chắn tăng conversion"
QUALITY-GATE-MANIFEST:END -->
