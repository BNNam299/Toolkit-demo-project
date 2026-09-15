---
doc_id: 05-02
title: PRD Audit
phase: 05-prd
skill: prd-architect
profile: Bắt buộc
owner: PO
reviewers: []
version: 0.1.0
status: draft
last_updated:
approved_by: ""
approved_at: ""
depends_on: [05-01]
feeds: [06-01]
id_prefix: []
gate: G4
in_handover: false
confidence: low
---

# [Tên dự án] — PRD Audit

> Audit **chỉ liệt kê finding**, không tự sửa `05-01`.

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


## 1. Năm cổng chất lượng
| # | Cổng | Kiểm gì | Kết quả | Finding |
| --- | --- | --- | --- | --- |
| 1 | **Truy nguyên** | Mọi `FEAT` về được `INS` hoặc `JTBD` | PASS / FAIL | |
| 2 | **Phạm vi** | Mục 11 khớp `00-02`, MVP không phình | | |
| 3 | **Ranh giới** | Không khai báo công nghệ, không viết giá bằng số | | |
| 4 | **Bằng chứng** | Mọi mệnh đề có nhãn đúng, không giả định trình bày như sự thật | | |
| 5 | **Khả thi** | Đã đối chiếu `tech-input/TECH-05` nếu có | | |

## 2. Tính năng đáng nghi
| `FEAT` | Vấn đề | Loại | Đề xuất |
| --- | --- | --- | --- |
| | | Không gắn pain point / Trùng lặp / Quá lớn cho MVP / Không đo được | |

## 3. Câu hỏi phản biện
> Với mỗi `FEAT`: nó giải quyết vấn đề gì · cho ai · trong bối cảnh nào · người dùng nhận giá trị gì ·
> đo hiệu quả bằng cách nào · điều gì khiến nó thất bại.

| `FEAT` | Câu không trả lời được | Hành động |
| --- | --- | --- |

## 4. Kết luận
| Trường | Nội dung |
| --- | --- |
| **PASS đủ 5 cổng** | Có / Không |
| Phải sửa gì trước khi đóng G4 | |
| Finding đã được duyệt áp dụng | |

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
# Nguồn chân lý DUY NHẤT cho G4 phần tài liệu này. KHÔNG chép khối này vào file đầu ra ở docs/.
doc: 05-02_PRD_AUDIT
gate: G4
required_major:
  - "0. Đọc nhanh"
  - "1. Năm cổng chất lượng"
  - "2. Tính năng đáng nghi"
  - "3. Câu hỏi phản biện"
  - "4. Kết luận"
  - "5. Nguồn phương pháp"
  - "Thuật ngữ dùng trong tài liệu này"
required_minor:
  {}
quality_checks:
  - "Mục 4 kết luận PASS đủ 5 cổng — điều kiện G4"
  - "Audit không sửa 05-01, chỉ liệt kê finding"
  - "Mỗi FEAT đi qua 6 câu phản biện ở mục 3"
QUALITY-GATE-MANIFEST:END -->
