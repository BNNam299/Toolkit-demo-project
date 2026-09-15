---
doc_id: 10-03
title: Funnel Definition
phase: 10-measurement
skill: measurement-designer
profile: Bắt buộc
owner: PO
reviewers: []
version: 0.1.0
status: draft
last_updated:
approved_by: ""
approved_at: ""
depends_on: [10-02, 04-06, 09-01]
feeds: [13-01]
id_prefix: [FNL]
gate: G8
in_handover: true
confidence: low
---

# [Tên dự án] — Funnel Definition

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


## 1. Phễu chính
| `FNL` | Bước | **Event đánh dấu** | Điều kiện | Tỷ lệ chuyển kỳ vọng | `SCR` |
| --- | --- | --- | --- | --- | --- |
| `FNL-001` | Cài đặt | | | — | |
| `FNL-002` | Mở lần đầu | | | | |
| `FNL-003` | Xong onboarding | | | | |
| `FNL-004` | **Chạm aha moment** | | | | |
| `FNL-005` | Xem paywall | | | | |
| `FNL-006` | Bắt đầu trial | | | | |
| `FNL-007` | Chuyển thành trả tiền | | | | |
| `FNL-008` | Giữ được sau kỳ đầu | | | | |

> Mỗi bước định nghĩa bằng **event cụ thể**, không bằng mô tả.

## 2. Activation
| Trường | Nội dung |
| --- | --- |
| **Định nghĩa bằng hành vi** | _hoàn thành [hành động cốt lõi] ít nhất N lần trong M ngày đầu_ |
| Aha moment tương ứng | _trích `04-06`_ |
| Event đo | |
| Target |  |

> Không định nghĩa activation bằng thời gian. "Dùng trong 7 ngày" không phải activation.

## 3. Retention
| Trường | Nội dung |
| --- | --- |
| **Loại đang dùng** | Ngày mốc D1/D7/D30 / Theo khoảng |
| Thế nào là "còn hoạt động" | |
| Event đo | |
| Target |  |

> Ghi rõ loại vì hai cách cho ra con số khác nhau và hay bị so sánh nhầm.

## 4. Phễu phụ
| Tên phễu | Các bước | Vì sao theo dõi riêng |
| --- | --- | --- |

## 5. Chỗ rơi dự kiến
| Bước | Vì sao dự kiến rơi nhiều | Giả thuyết | `EXP` |
| --- | --- | --- | --- |

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
# Nguồn chân lý DUY NHẤT cho G8 phần tài liệu này. KHÔNG chép khối này vào file đầu ra ở docs/.
doc: 10-03_FUNNEL_DEFINITION
gate: G8
required_major:
  - "0. Đọc nhanh"
  - "1. Phễu chính"
  - "2. Activation"
  - "3. Retention"
  - "4. Phễu phụ"
  - "5. Chỗ rơi dự kiến"
  - "6. Nguồn phương pháp"
  - "Thuật ngữ dùng trong tài liệu này"
required_minor:
  {}
quality_checks:
  - "Mọi bước phễu có event đánh dấu cụ thể — điều kiện G8"
  - "Activation định nghĩa bằng hành vi, không bằng thời gian"
  - "Retention ghi rõ loại ngày mốc hay theo khoảng"
  - "Aha moment trích từ 04-06, không định nghĩa lại"
QUALITY-GATE-MANIFEST:END -->
