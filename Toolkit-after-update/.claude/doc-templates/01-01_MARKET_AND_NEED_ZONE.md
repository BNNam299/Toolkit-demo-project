---
doc_id: 01-01
title: Thị trường & Need Zone
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
depends_on: [00-01]
feeds: [02-04, 03-01]
id_prefix: [NC]
gate: G1
in_handover: false
confidence: low
---

# [Tên dự án] — Thị trường & Need Zone

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


## 1. Need zone đang xét

### 1.1 Phạm vi
_Nhóm nhu cầu đang khảo sát và lý do chọn._

### 1.2 Ranh giới
_Cái gì nằm ngoài phạm vi khảo sát này._

## 2. Tín hiệu thị trường

| # | Tín hiệu | Nguồn | Ngày lấy | Nhãn | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| 1 | | | | `[FACT]` | |

_Số liệu không có nguồn công khai: ghi **Không công bố**. Số liệu từ công cụ bên thứ ba: ghi rõ tên công cụ
và rằng đây là ước lượng._

## 3. Need cluster

> Mỗi cluster phải có **≥3 bản ghi** từ **≥2 nguồn khác nhau** — điều kiện đóng G1.

### NC-001 · [tên cluster]

| Trường | Nội dung |
| --- | --- |
| Mô tả nhu cầu | |
| Số bản ghi | |
| Số nguồn khác nhau | |
| Pain point thuộc cluster | `PN-001`, `PN-002`, … |
| Tần suất xuất hiện | |
| Mức độ nghiêm trọng | |
| Nhãn | `[INSIGHT]` |

## 4. Nhu cầu thật hay trend bề mặt

| Cluster | Dấu hiệu nhu cầu thật | Dấu hiệu trend bề mặt | Kết luận |
| --- | --- | --- | --- |
| `NC-001` | | | Thật / Trend / Chưa rõ |

_Dấu hiệu nhu cầu thật: lặp lại qua nhiều năm, người dùng đang tự xoay xở thủ công, sẵn sàng trả tiền cho
giải pháp kém. Dấu hiệu trend: chỉ tăng theo một sự kiện, thảo luận nhiều nhưng không ai đang làm gì._

## 5. Xếp hạng sơ bộ

| Hạng | Cluster | Tần suất | Nghiêm trọng | Cấp bách | Ghi chú |
| --- | --- | --- | --- | --- | --- |

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
# Nguồn chân lý DUY NHẤT cho G1 phần tài liệu này. KHÔNG chép khối này vào file đầu ra ở docs/.
doc: 01-01_MARKET_AND_NEED_ZONE
gate: G1
required_major:
  - "0. Đọc nhanh"
  - "1. Need zone đang xét"
  - "2. Tín hiệu thị trường"
  - "3. Need cluster"
  - "4. Nhu cầu thật hay trend bề mặt"
  - "5. Xếp hạng sơ bộ"
  - "6. Nguồn phương pháp"
  - "Thuật ngữ dùng trong tài liệu này"
required_minor:
  "1. Need zone đang xét": ["1.1", "1.2"]
quality_checks:
  - "Mỗi NC có ≥3 bản ghi từ ≥2 nguồn khác nhau — điều kiện G1"
  - "Mọi số liệu có nguồn hoặc ghi Không công bố"
  - "Mỗi NC liên kết tới các PN cụ thể ở 01-02"
  - "Mục 4 có kết luận cho từng cluster, không bỏ trống"
QUALITY-GATE-MANIFEST:END -->
