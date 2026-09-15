---
doc_id: 02-02
title: Competitor Teardown
phase: 02-competitor
skill: competitor-intel
profile: Bắt buộc
owner: PO
reviewers: []
version: 0.1.0
status: draft
last_updated:
approved_by: ""
approved_at: ""
depends_on: [02-01]
feeds: [02-04, 09-01]
id_prefix: []
gate: G1
in_handover: false
confidence: low
---

# [Tên dự án] — Competitor Teardown

> **Dựa trên dùng thật**, không phải đọc trang store. Đây là điều kiện đóng G1.

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


## 1. Đối thủ đã mổ xẻ

| Đối thủ | Đã cài | Đã dùng bao lâu | Đã mua bản trả phí | Ngày |
| --- | --- | --- | --- | --- |
| `COM-001` | Có | | Có / Không | |

## 2. Onboarding

| Đối thủ | Số bước | Hỏi gì trước khi cho dùng | Bao lâu tới giá trị đầu tiên | Xin quyền lúc nào |
| --- | --- | --- | --- | --- |

## 3. Paywall

| Đối thủ | Xuất hiện ở đâu | Trước hay sau aha moment | Có trial | Có downsell khi đóng | Cách huỷ |
| --- | --- | --- | --- | --- | --- |

## 4. Luồng cốt lõi

_Mô tả từng bước của luồng chính, kèm nhận xét chỗ nào mượt và chỗ nào vướng._

### COM-001
| Bước | Người dùng làm gì | Mượt hay vướng | Ghi chú |
| --- | --- | --- | --- |

## 5. Điều họ làm tốt

| # | Đối thủ | Làm tốt điều gì | Có nên học không |
| --- | --- | --- | --- |

## 6. Điều họ làm dở

| # | Đối thủ | Dở ở đâu | Có phải cơ hội không | GAP liên quan |
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
# Nguồn chân lý DUY NHẤT cho G1 phần tài liệu này. KHÔNG chép khối này vào file đầu ra ở docs/.
doc: 02-02_COMPETITOR_TEARDOWN
gate: G1
required_major:
  - "0. Đọc nhanh"
  - "1. Đối thủ đã mổ xẻ"
  - "2. Onboarding"
  - "3. Paywall"
  - "4. Luồng cốt lõi"
  - "5. Điều họ làm tốt"
  - "6. Điều họ làm dở"
  - "7. Nguồn phương pháp"
  - "Thuật ngữ dùng trong tài liệu này"
required_minor:
  {}
quality_checks:
  - "Teardown dựa trên dùng thật — mục 1 xác nhận đã cài và dùng — điều kiện G1"
  - "Mỗi điểm dở ở mục 6 nối tới một GAP ở 02-04 hoặc ghi rõ không phải cơ hội"
  - "Có ghi thời điểm paywall so với aha moment"
QUALITY-GATE-MANIFEST:END -->
