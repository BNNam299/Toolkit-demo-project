---
doc_id: 13-02
title: Dev Question Log
phase: 13-handover
skill: dev-handover
profile: Bắt buộc — mở từ phase 03
owner: PO
reviewers: []
version: 0.1.0
status: draft
last_updated:
approved_by: ""
approved_at: ""
depends_on: [03-02]
feeds: [13-01]
id_prefix: [DQ]
gate: G11
in_handover: false
confidence: low
---

# [Tên dự án] — Dev Question Log

> **Mở từ phase 03**, không phải tới phase 13 mới lập.
> Mỗi khi bất kỳ phase nào cần thông tin kỹ thuật chưa có, ghi một dòng vào đây thay vì đoán.

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


## 1. Câu hỏi
| `DQ` | Ngày hỏi | **Câu hỏi** | **Ảnh hưởng tới tài liệu / quyết định nào** | **Mức chặn** | Ai hỏi | Trạng thái | Câu trả lời | Ngày trả lời | **Tài liệu đã cập nhật** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `DQ-001` | | | | Chặn / Ảnh hưởng / Tham khảo | | mở | | | |

> Cột "ảnh hưởng tới cái gì" quyết định mức ưu tiên. `DQ` chặn một `FR` quan trọng khác hẳn `DQ` chỉ ảnh
> hưởng một chi tiết phụ.

## 2. Câu hỏi đang chặn
| `DQ` | Chặn gì | Từ ngày | Số ngày đã chờ | Đã nhắc lần nào |
| --- | --- | --- | --- | --- |

## 3. Giả định tạm khi chờ trả lời
| `DQ` | `ASM` tương ứng | Đang giả định gì | Hệ quả nếu sai |
| --- | --- | --- | --- |

## 4. Câu hỏi không còn liên quan
| `DQ` | Vì sao không còn liên quan | Ngày |
| --- | --- | --- |

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
# Nguồn chân lý DUY NHẤT cho G11 phần tài liệu này. KHÔNG chép khối này vào file đầu ra ở docs/.
doc: 13-02_DEV_QUESTION_LOG
gate: G11
required_major:
  - "0. Đọc nhanh"
  - "1. Câu hỏi"
  - "2. Câu hỏi đang chặn"
  - "3. Giả định tạm khi chờ trả lời"
  - "4. Câu hỏi không còn liên quan"
  - "5. Nguồn phương pháp"
  - "Thuật ngữ dùng trong tài liệu này"
required_minor:
  {}
quality_checks:
  - "Mỗi DQ ghi rõ ảnh hưởng tới tài liệu hoặc quyết định nào"
  - "Mỗi DQ có mức chặn"
  - "Mỗi DQ đang mở có ASM tương ứng ở mục 3"
  - "Không còn DQ mở mức Chặn — điều kiện G11"
QUALITY-GATE-MANIFEST:END -->
