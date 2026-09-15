---
doc_id: 04-05
title: Persona
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
depends_on: [04-03, 04-04]
feeds: [04-06, 05-01, 07-01]
id_prefix: [PER]
gate: G3
in_handover: true
confidence: low
---

# [Tên dự án] — Persona

> Persona dựa trên **hành vi**, không phải nhân khẩu học. Nếu chưa có dữ liệu thì ghi rõ là **proto-persona**.

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


## 1. Loại persona đang dùng
| Trường | Nội dung |
| --- | --- |
| Loại | Persona có dữ liệu / **Proto-persona** |
| Nguồn dữ liệu | |
| Số người tham gia | |

## 2. Persona
### PER-001 · [tên] — [định vị một dòng]
| Trường | Nội dung |
| --- | --- |
| **Hành vi đặc trưng** | |
| Bối cảnh sử dụng | |
| Động cơ | |
| Rào cản | |
| Trigger khiến họ tìm giải pháp | |
| Mức độ thành thạo công nghệ | |
| JTBD chính | `JTBD-001` |
| Insight nguồn | `INS-001`, `INS-004` |
| Câu nói đại diện | _trích nguyên văn từ research log_ |
| Nhãn | `[INSIGHT]` hoặc `[ASM]` nếu là proto |

**Nhân khẩu học** _(chỉ ghi nếu thật sự ảnh hưởng tới thiết kế)_

## 3. Phân biệt persona
| Tiêu chí phân biệt | `PER-001` | `PER-002` |
| --- | --- | --- |
| Hành vi khác nhau ở đâu | | |
| Cần thiết kế khác nhau không | | |

> Nếu hai persona không dẫn tới quyết định thiết kế khác nhau thì **gộp lại**. Nhiều persona không làm sản
> phẩm tốt hơn, chỉ làm tài liệu dài hơn.

## 4. Ai KHÔNG phải người dùng
| Nhóm | Vì sao không nhắm tới |
| --- | --- |

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
doc: 04-05_PERSONA
gate: G3
required_major:
  - "0. Đọc nhanh"
  - "1. Loại persona đang dùng"
  - "2. Persona"
  - "3. Phân biệt persona"
  - "4. Ai KHÔNG phải người dùng"
  - "5. Nguồn phương pháp"
  - "Thuật ngữ dùng trong tài liệu này"
required_minor:
  {}
quality_checks:
  - "Mỗi thuộc tính hành vi của PER dẫn được về INS, JTBD hoặc bản ghi ở 04-02 — không mô tả chung chung"
  - "Không có chi tiết nào trong persona được thêm cho sinh động mà không có nguồn"
  - "Persona dựa trên hành vi, không chỉ nhân khẩu học — điều kiện G3"
  - "Proto-persona được ghi rõ là proto, không trình bày như có dữ liệu"
  - "Mỗi PER truy được về INS và JTBD"
  - "Mục 3 chứng minh hai persona cần thiết kế khác nhau, nếu không thì gộp"
  - "Mục 4 không bỏ trống"
QUALITY-GATE-MANIFEST:END -->
