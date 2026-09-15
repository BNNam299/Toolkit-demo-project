---
doc_id: 06-04
title: Business Rules
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
depends_on: [06-02]
feeds: [08-02, 09-02, 13-04]
id_prefix: [BR]
gate: G5
in_handover: true
confidence: low
---

# [Tên dự án] — Business Rules

> **Nguồn chân lý duy nhất về công thức.** Tài liệu khác trích `BR-xxx`, không viết lại công thức.
> Mỗi BR phải có **công thức + ít nhất một ví dụ tính tay + các trường hợp biên**.

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


## 1. Business rule
### BR-001 · [tên]
| Trường | Nội dung |
| --- | --- |
| Phát biểu | |
| **Công thức** | |
| `FR` áp dụng | |
| Điều gì xảy ra khi vi phạm | |

**Ví dụ tính tay**
| Đầu vào | Từng bước | Kết quả |
| --- | --- | --- |

**Trường hợp biên**
> Hay bị quên: giá trị 0, giá trị âm, đúng ngưỡng, vượt ngưỡng một đơn vị, reset lúc mấy giờ theo múi giờ nào,
> phần dư có cộng dồn không, người dùng đổi múi giờ giữa chừng, đổi thiết bị.

| # | Trường hợp | Kết quả mong đợi |
| --- | --- | --- |
| 1 | Giá trị bằng 0 | |
| 2 | Đúng ngưỡng | |
| 3 | Vượt ngưỡng một đơn vị | |
| 4 | Reset theo thời gian — mấy giờ, múi giờ nào | |
| 5 | Phần dư có cộng dồn không | |

## 2. Bảng tổng hợp
| `BR` | Tên | Công thức tóm tắt | `FR` áp dụng | Có ví dụ | Số trường hợp biên |
| --- | --- | --- | --- | --- | --- |

## 3. Nguồn phương pháp

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
doc: 06-04_BUSINESS_RULES
gate: G5
required_major:
  - "0. Đọc nhanh"
  - "1. Business rule"
  - "2. Bảng tổng hợp"
  - "3. Nguồn phương pháp"
  - "Thuật ngữ dùng trong tài liệu này"
required_minor:
  {}
quality_checks:
  - "Mọi BR có công thức kèm ít nhất một ví dụ tính tay — điều kiện G5"
  - "Mọi BR có mục trường hợp biên, tối thiểu 5 dòng"
  - "Quy tắc reset theo thời gian ghi rõ giờ và múi giờ"
  - "Không tài liệu nào khác viết lại công thức, chỉ trích BR-xxx"
QUALITY-GATE-MANIFEST:END -->
