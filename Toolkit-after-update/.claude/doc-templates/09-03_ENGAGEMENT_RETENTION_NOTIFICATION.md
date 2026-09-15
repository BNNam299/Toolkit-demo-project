---
doc_id: 09-03
title: Engagement, Retention & Notification
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
depends_on: [04-06, 09-01]
feeds: [09-06, 10-03]
id_prefix: [TRG, NTF]
gate: G8
in_handover: true
confidence: low
---

# [Tên dự án] — Engagement, Retention & Notification

> Usability tốt không tự tạo retention. Mọi cơ chế ở đây phải **củng cố giá trị cốt lõi**,
> không phải gamification gắn thêm.

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


## 1. Phân tích hành vi
| Trường | Nội dung |
| --- | --- |
| Hành vi cốt lõi cần lặp lại | |
| Tần suất tự nhiên của hành vi đó | |
| Điều gì cản trở lặp lại | |

## 2. Trigger
| `TRG` | Loại | Mô tả | Kích hoạt khi nào | Củng cố hành vi cốt lõi nào |
| --- | --- | --- | --- | --- |
| `TRG-001` | Nội tại / Bên ngoài | | | |

## 3. Vòng lặp
| Khâu | Nội dung | `SCR` |
| --- | --- | --- |
| Trigger | | |
| Hành động | | |
| Phần thưởng | | |
| Đầu tư của người dùng | | |

> "Đầu tư" là thứ khiến lần sau quay lại có giá trị hơn — dữ liệu đã nhập, tiến độ đã có, tuỳ chỉnh đã làm.

## 4. Thông báo
| `NTF` | Nội dung | Kích hoạt | Tần suất tối đa | Người dùng tắt được không | `CPY` |
| --- | --- | --- | --- | --- | --- |

| Kiểm | Kết quả |
| --- | --- |
| Mỗi thông báo có lý do người dùng thấy hữu ích | |
| Có giới hạn tần suất | |
| Tắt được từng loại, không phải tắt tất cả hoặc không | |

## 5. Kiểm chống gamification vô nghĩa
| Cơ chế | Củng cố hành vi cốt lõi nào | Nếu bỏ đi thì mất gì | Giữ hay bỏ |
| --- | --- | --- | --- |

> Cơ chế không trả lời được cột 2 thì **bỏ**.

## 6. Đo lường
| Cơ chế | `EVT` | `KPI` | Target | **Kill rule** |
| --- | --- | --- | --- | --- |

## 7. Nguồn phương pháp

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
doc: 09-03_ENGAGEMENT_RETENTION_NOTIFICATION
gate: G8
required_major:
  - "0. Đọc nhanh"
  - "1. Phân tích hành vi"
  - "2. Trigger"
  - "3. Vòng lặp"
  - "4. Thông báo"
  - "5. Kiểm chống gamification vô nghĩa"
  - "6. Đo lường"
  - "7. Nguồn phương pháp"
  - "Thuật ngữ dùng trong tài liệu này"
required_minor:
  {}
quality_checks:
  - "Mọi TRG củng cố một hành vi cốt lõi cụ thể"
  - "Mọi cơ chế ở mục 5 trả lời được cột củng cố hành vi nào, nếu không thì bỏ"
  - "Mỗi cơ chế có target và kill rule — điều kiện G8"
  - "Thông báo tắt được từng loại"
QUALITY-GATE-MANIFEST:END -->
