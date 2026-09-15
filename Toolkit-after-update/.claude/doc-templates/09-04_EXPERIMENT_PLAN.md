---
doc_id: 09-04
title: Experiment Plan
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
depends_on: [09-01, 09-02]
feeds: [10-02]
id_prefix: [EXP]
gate: G8
in_handover: false
confidence: low
---

# [Tên dự án] — Experiment Plan

> **Không A/B test nếu không có giả thuyết.** Thử nghiệm không giả thuyết chỉ tạo ra số liệu, không tạo ra hiểu biết.

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


## 1. Thí nghiệm
### EXP-001 · [tên]
| Trường | Nội dung |
| --- | --- |
| **Giả thuyết** | _Chúng tôi tin rằng [thay đổi] sẽ khiến [chỉ số] [tăng/giảm] vì [lý do]_ |
| Bản gốc | |
| Biến thể | |
| Đối tượng áp dụng | |
| Quy tắc phân bổ | |
| **Chỉ số chính** | `KPI-` |
| **Chỉ số bảo vệ** | `KPI-` |
| Thời gian chạy tối thiểu | |
| Cỡ mẫu tối thiểu | |
| **Kill rule** | _dừng ngay nếu…_ |
| `EVT` cần có | |

## 2. Bảng thí nghiệm
| `EXP` | Giả thuyết tóm tắt | Chỉ số chính | Chỉ số bảo vệ | Kill rule | Trạng thái |
| --- | --- | --- | --- | --- | --- |

## 3. Thứ tự chạy
| Thứ tự | `EXP` | Vì sao chạy trước | Phụ thuộc |
| --- | --- | --- | --- |

> Không chạy hai thí nghiệm chồng lên nhau trên cùng một luồng.

## 4. Kết quả
| `EXP` | Ngày | Kết quả chính | Chỉ số bảo vệ có xấu đi không | Kết luận | `DEC` |
| --- | --- | --- | --- | --- | --- |

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
doc: 09-04_EXPERIMENT_PLAN
gate: G8
required_major:
  - "0. Đọc nhanh"
  - "1. Thí nghiệm"
  - "2. Bảng thí nghiệm"
  - "3. Thứ tự chạy"
  - "4. Kết quả"
  - "5. Nguồn phương pháp"
  - "Thuật ngữ dùng trong tài liệu này"
required_minor:
  {}
quality_checks:
  - "Mọi EXP có giả thuyết dạng tin rằng/sẽ khiến/vì — điều kiện G8"
  - "Mọi EXP có chỉ số bảo vệ, không chỉ chỉ số chính"
  - "Mọi EXP có kill rule đặt trước"
  - "Không hai thí nghiệm chồng nhau trên cùng luồng"
QUALITY-GATE-MANIFEST:END -->
