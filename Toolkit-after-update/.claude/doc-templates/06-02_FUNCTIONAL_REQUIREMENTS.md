---
doc_id: 06-02
title: Functional Requirements
phase: 06-breakdown
skill: product-breakdown
profile: Bắt buộc
owner: PO
reviewers: []
version: 0.1.0
status: draft
last_updated:
approved_by: ""
approved_at: ""
depends_on: [06-01]
feeds: [07-05, 08-01, 13-04]
id_prefix: [FR]
gate: G5
in_handover: true
confidence: low
---

# [Tên dự án] — Functional Requirements

> FR mô tả **hệ thống phải làm gì**. **Mọi `UC` phải có ≥1 `FR`. Mọi `FR` phải có AC đo được.**

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


## 1. Bảng phủ use case
| `UC` | FR tương ứng | Đủ chưa |
| --- | --- | --- |

## 2. Functional requirement
### FR-001 · [tên]
| Trường | Nội dung |
| --- | --- |
| Phát biểu | Hệ thống phải … |
| `UC` nguồn | |
| Mức ưu tiên | Must / Should / Could |
| Phụ thuộc | `FR-`, `tech-input/TECH-02` |
| Khả thi | _theo `TECH-05` nếu đã nhận, nếu chưa thì `[ASM]` + `DQ`_ |

**Acceptance criteria**
| ID | Given | When | Then |
| --- | --- | --- | --- |
| `AC-001` | | | |

> **Từ bị cấm trong AC vì không đo được:** nhanh, mượt, dễ dùng, trực quan, đẹp, hợp lý, đầy đủ, tối ưu.
> Thay bằng số hoặc mô tả hành vi cụ thể.
>
> Sai: *"Kết quả hiển thị nhanh."*
> Đúng: *"Given ảnh đã chụp xong, When bấm Phân tích, Then kết quả hiển thị trong 3 giây trên thiết bị
> tham chiếu; quá 3 giây thì hiện trạng thái đang xử lý kèm nút Huỷ."*

**Năm câu phải trả lời được**
| Câu | Trả lời |
| --- | --- |
| Giải quyết vấn đề gì | |
| Dành cho ai | |
| Trong bối cảnh nào | |
| Người dùng nhận giá trị gì | |
| Đo hiệu quả bằng cách nào | `KPI-` |

## 3. Bảng tổng hợp
| `FR` | Phát biểu | `UC` | Ưu tiên | Số AC | Khả thi |
| --- | --- | --- | --- | --- | --- |

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
# Nguồn chân lý DUY NHẤT cho G5 phần tài liệu này. KHÔNG chép khối này vào file đầu ra ở docs/.
doc: 06-02_FUNCTIONAL_REQUIREMENTS
gate: G5
required_major:
  - "0. Đọc nhanh"
  - "1. Bảng phủ use case"
  - "2. Functional requirement"
  - "3. Bảng tổng hợp"
  - "4. Nguồn phương pháp"
  - "Thuật ngữ dùng trong tài liệu này"
required_minor:
  {}
quality_checks:
  - "Mọi UC có ≥1 FR — điều kiện G5"
  - "Mọi FR có ít nhất một AC đo được — điều kiện G5"
  - "AC KHÔNG chứa các từ: nhanh, mượt, dễ dùng, trực quan, đẹp, hợp lý, đầy đủ, tối ưu"
  - "Mỗi FR trả lời được đủ 5 câu"
  - "FR phụ thuộc kỹ thuật chưa xác nhận đã gắn [ASM] và có DQ"
QUALITY-GATE-MANIFEST:END -->
