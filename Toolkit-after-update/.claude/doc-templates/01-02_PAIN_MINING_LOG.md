---
doc_id: 01-02
title: Pain Mining Log
phase: 01-market
skill: market-niche-scout
profile: Bắt buộc
owner: PO
reviewers: []
version: 0.1.0
status: draft
last_updated:
approved_by: ""
approved_at: ""
depends_on: [01-01]
feeds: [01-01, 02-04]
id_prefix: [PN]
gate: G1
in_handover: false
confidence: low
---

# [Tên dự án] — Pain Mining Log

> Sổ ghi thô. Mỗi dòng là một lời phàn nàn có thật, **có nguồn truy được**.
> Không tổng hợp ở đây — tổng hợp nằm ở `01-01`.

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


## 1. Nguồn đã đào

| # | Nguồn | Cách đào | Số bản ghi thu được | Ngày |
| --- | --- | --- | --- | --- |
| 1 | App Store review | | | |
| 2 | Google Play review | | | |
| 3 | Reddit | | | |
| 4 | Google Trends / keyword | | | |
| 5 | Cộng đồng, mạng xã hội | | | |

## 2. Bản ghi pain point

| ID | Trích dẫn nguyên văn | Nguồn + link | Ngày | Cluster | Nhãn |
| --- | --- | --- | --- | --- | --- |
| `PN-001` | | | | `NC-001` | `[FACT]` |

_Trích **nguyên văn**, không diễn giải. Diễn giải làm mất chi tiết mà sau này mới thấy quan trọng._

## 3. Cụm từ mồi đã dùng

| Cụm từ | Nguồn áp dụng | Kết quả |
| --- | --- | --- |
| | | |

## 4. Nguồn đã đào nhưng không ra gì

> Ghi lại để lần sau không đào lại.

| Nguồn | Vì sao không ra | Ngày |
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
# Nguồn chân lý DUY NHẤT cho G1 phần tài liệu này. KHÔNG chép khối này vào file đầu ra ở docs/.
doc: 01-02_PAIN_MINING_LOG
gate: G1
required_major:
  - "0. Đọc nhanh"
  - "1. Nguồn đã đào"
  - "2. Bản ghi pain point"
  - "3. Cụm từ mồi đã dùng"
  - "4. Nguồn đã đào nhưng không ra gì"
  - "5. Nguồn phương pháp"
  - "Thuật ngữ dùng trong tài liệu này"
required_minor:
  {}
quality_checks:
  - "Mỗi PN có link hoặc trích dẫn kiểm chứng được — điều kiện G1"
  - "Trích dẫn là nguyên văn, không diễn giải"
  - "Mỗi PN gắn vào một NC ở 01-01"
  - "Đã đào ít nhất 2 loại nguồn khác nhau"
QUALITY-GATE-MANIFEST:END -->
