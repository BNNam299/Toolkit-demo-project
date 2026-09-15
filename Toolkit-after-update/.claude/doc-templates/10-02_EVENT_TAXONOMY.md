---
doc_id: 10-02
title: Event Taxonomy
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
depends_on: [10-01, 08-01, 09-01, 09-02]
feeds: [10-03, 13-04]
id_prefix: [EVT]
gate: G8
in_handover: true
confidence: low
---

# [Tên dự án] — Event Taxonomy

> **Mọi event phải phục vụ ít nhất một `KPI` hoặc bước phễu.** Không phục vụ gì thì **xoá**, đừng cài.

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


## 1. Quy ước
`<đối_tượng>_<hành_động>` · snake_case · động từ **thì quá khứ**

Đúng: `paywall_viewed`, `trial_started`, `scan_completed`, `free_limit_reached`
Sai: `viewPaywall`, `user_clicks_button`, `Paywall View`, `startTrial`

> Tên event đã phát hành thì **không đổi** — đổi làm gãy dữ liệu lịch sử. Cần đổi thì tạo event mới,
> event cũ chuyển `deprecated`.

## 2. Bảng event
| `EVT` | Tên event | **Khi nào bắn** | Thuộc tính | Kiểu | Giá trị hợp lệ | **`KPI`/`FNL` phục vụ** | `SCR` |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `EVT-001` | | | | | | | |

## 3. Nhóm bắt buộc không được quên
| # | Nhóm | Đã có | `EVT` |
| --- | --- | --- | --- |
| 1 | Vòng đời app — mở, vào nền, quay lại | | |
| 2 | Hoàn thành hành vi cốt lõi | | |
| 3 | Từng bước onboarding | | |
| 4 | Xem paywall, bắt đầu trial, mua | | |
| 5 | **Tám trạng thái giao dịch** | | |
| 6 | **Trạng thái lỗi và hành vi phục hồi** | | |
| 7 | **Từ chối quyền, gồm từ chối vĩnh viễn** | | |
| 8 | **Mất mạng** | | |
| 9 | **Chạm ngưỡng giới hạn free** | | |
| 10 | Bật/tắt thông báo | | |

## 4. Kiểm chéo hai chiều
| Kiểm | Kết quả | Vi phạm |
| --- | --- | --- |
| Mọi `KPI` tính được từ ≥1 `EVT` | | |
| Mọi `EVT` phục vụ ≥1 `KPI` hoặc `FNL` | | |

## 5. Thuộc tính và quyền riêng tư
| Thuộc tính | Có phải dữ liệu cá nhân | Đã duyệt ở `06-05` | Vì sao cần |
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
doc: 10-02_EVENT_TAXONOMY
gate: G8
required_major:
  - "0. Đọc nhanh"
  - "1. Quy ước"
  - "2. Bảng event"
  - "3. Nhóm bắt buộc không được quên"
  - "4. Kiểm chéo hai chiều"
  - "5. Thuộc tính và quyền riêng tư"
  - "6. Nguồn phương pháp"
  - "Thuật ngữ dùng trong tài liệu này"
required_minor:
  {}
quality_checks:
  - "Mọi EVT phục vụ ≥1 KPI hoặc bước phễu — điều kiện G8"
  - "Mọi KPI tính được từ ≥1 EVT — điều kiện G8"
  - "Tên event đúng quy ước snake_case thì quá khứ"
  - "Mục 3 đi hết 10 nhóm"
  - "Thuộc tính cá nhân đã duyệt ở 06-05"
QUALITY-GATE-MANIFEST:END -->
