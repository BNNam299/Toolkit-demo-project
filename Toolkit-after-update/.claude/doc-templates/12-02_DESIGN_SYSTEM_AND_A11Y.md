---
doc_id: 12-02
title: Design System & Accessibility Baseline
phase: 12-prototype
skill: figma-prototype-spec
profile: Bắt buộc
owner: Designer
reviewers: []
version: 0.1.0
status: draft
last_updated:
approved_by: ""
approved_at: ""
depends_on: [12-00, 06-03, 08-03]
feeds: [12-03, 13-01]
id_prefix: [TOK, CMP]
gate: G10
in_handover: true
confidence: low
---

# [Tên dự án] — Design System & Accessibility Baseline

> **Nguồn chân lý duy nhất cho token và component.** Mọi màu, cỡ chữ, khoảng cách dùng trong Figma phải
> truy được về một token có tên ở đây.

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


## 1. Token màu
| `TOK` | Tên | Dùng cho | Sáng | Tối | Tương phản với nền |
| --- | --- | --- | --- | --- | --- |
| `TOK-001` | | | | | |

_Nhóm tối thiểu: nền, bề mặt, chữ chính, chữ phụ, nhấn, thành công, cảnh báo, lỗi, viền._

## 2. Token chữ
| `TOK` | Tên | Cỡ | Độ đậm | Chiều cao dòng | Dùng cho |
| --- | --- | --- | --- | --- | --- |

| Trường | Nội dung |
| --- | --- |
| **Hành vi khi phóng cỡ chữ hệ thống** | |
| Cỡ chữ nhỏ nhất được dùng | |

## 3. Token khoảng cách
| `TOK` | Tên | Giá trị | Dùng cho |
| --- | --- | --- | --- |

## 4. Component
### CMP-001 · [tên]
| Biến thể | Kích thước tối thiểu | Token dùng |
| --- | --- | --- |

**Trạng thái bắt buộc**
| Trạng thái | Đã có | Ghi chú |
| --- | --- | --- |
| Mặc định | | |
| Nhấn | | |
| **Vô hiệu** | | |
| **Đang tải** | | |
| Lỗi | | |
| Tập trung | | |

> Vô hiệu và đang tải là hai trạng thái hay quên nhất, và là hai trạng thái người dùng gặp nhiều nhất khi mạng chậm.

## 5. Baseline tiếp cận
| # | Ngưỡng | Giá trị | **Cách kiểm** | Kết quả |
| --- | --- | --- | --- | --- |
| 1 | Tương phản chữ thường | ≥ 4.5:1 | | |
| 2 | Tương phản chữ lớn | ≥ 3:1 | | |
| 3 | Vùng chạm | ≥ 44pt mỗi chiều | | |
| 4 | Cỡ chữ hệ thống lớn nhất | layout không vỡ, không cắt chữ | | |
| 5 | Màu không phải kênh truyền tin duy nhất | | | |
| 6 | Nhãn trình đọc màn hình | mọi thành phần tương tác | | |
| 7 | Thứ tự đọc | hợp lý theo thị giác | | |

_Ngưỡng lấy từ `06-03` mục 4. Mỗi ngưỡng phải kiểm được bằng công cụ hoặc bằng mắt theo cách lặp lại được._

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
# Nguồn chân lý DUY NHẤT cho G10 phần tài liệu này. KHÔNG chép khối này vào file đầu ra ở docs/.
doc: 12-02_DESIGN_SYSTEM_AND_A11Y
gate: G10
required_major:
  - "0. Đọc nhanh"
  - "1. Token màu"
  - "2. Token chữ"
  - "3. Token khoảng cách"
  - "4. Component"
  - "5. Baseline tiếp cận"
  - "6. Nguồn phương pháp"
  - "Thuật ngữ dùng trong tài liệu này"
required_minor:
  {}
quality_checks:
  - "Mọi component có đủ 6 trạng thái gồm vô hiệu và đang tải"
  - "Mục 5 đi hết 7 ngưỡng và có kết quả kiểm — điều kiện G10"
  - "Token màu có giá trị cho cả chế độ sáng và tối"
  - "Ngưỡng tiếp cận khớp 06-03 mục 4"
QUALITY-GATE-MANIFEST:END -->
