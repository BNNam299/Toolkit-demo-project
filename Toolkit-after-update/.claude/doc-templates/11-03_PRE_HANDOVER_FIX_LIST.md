---
doc_id: 11-03
title: Pre-Handover Fix List
phase: 11-evaluation
skill: design-quality-auditor
profile: Bắt buộc
owner: PO
reviewers: []
version: 0.1.0
status: draft
last_updated:
approved_by: ""
approved_at: ""
depends_on: [11-01, 11-02]
feeds: [12-01]
id_prefix: []
gate: G9
in_handover: false
confidence: low
---

# [Tên dự án] — Pre-Handover Fix List

> **Cổng G9 không đóng khi còn mục Critical hoặc usability 0–1 đang mở** mà không có `DEC` quyết định không sửa.

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


## 1. Phải sửa — Critical và Blocker
| # | Finding | Nguồn | Mức | Sửa gì | Tài liệu bị chạm | Trạng thái | `CHG` |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `DF-001` | 11-01 | Critical | | | Mở / Đang sửa / Xong | |

## 2. Quyết định không sửa
> Được phép không sửa, nhưng phải **có `DEC` kèm lý do và rủi ro**, không bỏ qua trong im lặng.

| Finding | Vì sao không sửa | Rủi ro chấp nhận | `DEC` | Xem lại khi nào |
| --- | --- | --- | --- | --- |

## 3. Hoãn sang sau
| Finding | Hoãn tới khi nào | Vì sao hoãn được | Ghi ở đâu |
| --- | --- | --- | --- |

## 4. Sửa xong thì chạm tài liệu nào
> Sửa thiết kế thường kéo theo sửa tài liệu. Bỏ bước này là nguồn gốc của việc tài liệu lệch thực tế.

| Finding | Tài liệu phải cập nhật | Đã cập nhật |
| --- | --- | --- |

## 5. Kiểm đóng cổng G9
| Kiểm | Kết quả |
| --- | --- |
| Không còn Critical đang mở | |
| Không còn usability 0–1 đang mở | |
| Mọi quyết định không sửa có `DEC` | |
| Báo cáo mồ côi ở `_INDEX` mục 5 rỗng | |

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
# Nguồn chân lý DUY NHẤT cho G9 phần tài liệu này. KHÔNG chép khối này vào file đầu ra ở docs/.
doc: 11-03_PRE_HANDOVER_FIX_LIST
gate: G9
required_major:
  - "0. Đọc nhanh"
  - "1. Phải sửa — Critical và Blocker"
  - "2. Quyết định không sửa"
  - "3. Hoãn sang sau"
  - "4. Sửa xong thì chạm tài liệu nào"
  - "5. Kiểm đóng cổng G9"
  - "6. Nguồn phương pháp"
  - "Thuật ngữ dùng trong tài liệu này"
required_minor:
  {}
quality_checks:
  - "Không còn Critical hoặc usability 0-1 đang mở — điều kiện G9"
  - "Mọi quyết định không sửa có DEC kèm rủi ro"
  - "Báo cáo mồ côi rỗng — điều kiện G9"
  - "Mục 4 ghi rõ tài liệu nào phải cập nhật sau khi sửa"
QUALITY-GATE-MANIFEST:END -->
