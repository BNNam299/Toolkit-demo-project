---
doc_id: 03-02
title: Concept Candidates
phase: 03-opportunity
skill: opportunity-validator
profile: Bắt buộc
owner: PO
reviewers: []
version: 0.1.0
status: draft
last_updated:
approved_by: ""
approved_at: ""
depends_on: [03-01, 02-04]
feeds: [03-03, 05-01]
id_prefix: [CPT]
gate: G2
in_handover: true
confidence: low
---

# [Tên dự án] — Concept Candidates

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


## 1. Khuôn concept bắt buộc

> Mọi concept **phải** viết đúng khuôn dưới đây. Đây là điều kiện đóng G2.

```
For [đối tượng người dùng]
who [có vấn đề gì]
sản phẩm cung cấp [giải pháp cốt lõi]
khác với [giải pháp thay thế hiện tại]
vì [lợi thế riêng]
```

## 2. Concept

### CPT-001 · [tên]

**Phát biểu**
> For … who … sản phẩm cung cấp … khác với … vì …

| Trường | Nội dung |
| --- | --- |
| Khoảng trống nhắm vào | `GAP-001` |
| Nhu cầu phục vụ | `NC-001` |
| Need Score của nhu cầu | / 35 |
| Giá trị cốt lõi trong một câu | |
| Điều gì khiến concept này thất bại | |
| Giả định rủi ro nhất | `ASM-` |

**Phạm vi tối thiểu để kiểm chứng được**
_Ít nhất cái gì để biết concept đúng hay sai._

## 3. So sánh concept

| ID | Concept | Nhu cầu | Need Score | Độ khó xây | Khác biệt | Xếp hạng |
| --- | --- | --- | --- | --- | --- | --- |

## 4. Concept đã loại

| Concept | Vì sao loại |
| --- | --- |

## 5. Concept được chọn

| Trường | Nội dung |
| --- | --- |
| Concept chọn | `CPT-00X` |
| Vì sao chọn | |
| DEC ID | `DEC-` |
| Điều kiện xem lại quyết định này | |

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
# Nguồn chân lý DUY NHẤT cho G2 phần tài liệu này. KHÔNG chép khối này vào file đầu ra ở docs/.
doc: 03-02_CONCEPT_CANDIDATES
gate: G2
required_major:
  - "0. Đọc nhanh"
  - "1. Khuôn concept bắt buộc"
  - "2. Concept"
  - "3. So sánh concept"
  - "4. Concept đã loại"
  - "5. Concept được chọn"
  - "6. Nguồn phương pháp"
  - "Thuật ngữ dùng trong tài liệu này"
required_minor:
  {}
quality_checks:
  - "Mọi concept viết đúng khuôn For/who/cung cấp/khác với/vì — điều kiện G2"
  - "Mỗi CPT nối tới ít nhất một GAP và một NC"
  - "Mỗi CPT có mục điều gì khiến nó thất bại, không bỏ trống"
  - "Mục 5 có DEC ID"
QUALITY-GATE-MANIFEST:END -->
