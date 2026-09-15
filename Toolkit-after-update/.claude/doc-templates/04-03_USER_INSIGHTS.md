---
doc_id: 04-03
title: User Insights
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
depends_on: [04-02, 02-03]
feeds: [04-04, 04-05, 05-01]
id_prefix: [INS]
gate: G3
in_handover: true
confidence: low
---

# [Tên dự án] — User Insights

> **Mỗi insight cần ≥2 nguồn hoặc ≥3 quan sát độc lập.** Đây là điều kiện đóng G3.

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


## 1. Affinity cluster
| Cluster | Quan sát thuộc cluster | Số quan sát | Số nguồn |
| --- | --- | --- | --- |

## 2. Insight
### INS-001 · [phát biểu một câu]
| Trường | Nội dung |
| --- | --- |
| Phát biểu | |
| Bằng chứng | `OBS-003`, `OBS-011`, review mining mục 2 |
| Số quan sát độc lập | |
| Số nguồn khác nhau | |
| Nhãn | `[INSIGHT]` |
| Vì sao điều này quan trọng | |
| Hệ quả cho sản phẩm | |

## 3. Bảng tổng hợp
| ID | Insight | Số bằng chứng | Số nguồn | Dùng ở tài liệu nào |
| --- | --- | --- | --- | --- |

## 4. Điều tưởng là insight nhưng chưa đủ bằng chứng
| Phát biểu | Số bằng chứng hiện có | Cần thêm gì | Nhãn |
| --- | --- | --- | --- |
| | | | `[HYP]` |

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
doc: 04-03_USER_INSIGHTS
gate: G3
required_major:
  - "0. Đọc nhanh"
  - "1. Affinity cluster"
  - "2. Insight"
  - "3. Bảng tổng hợp"
  - "4. Điều tưởng là insight nhưng chưa đủ bằng chứng"
  - "5. Nguồn phương pháp"
  - "Thuật ngữ dùng trong tài liệu này"
required_minor:
  {}
quality_checks:
  - "Mỗi INS dẫn tới bản ghi cụ thể ở 04-02, hoặc PN/NC ở 01-02 và 02-03 — không dùng kiến thức chung"
  - "Không có INS nào chỉ dựa trên suy luận về hành vi người dùng nói chung"
  - "Mỗi INS có ≥2 nguồn hoặc ≥3 quan sát độc lập — điều kiện G3"
  - "Insight thiếu bằng chứng nằm ở mục 4 với nhãn [HYP], không nằm ở mục 2"
  - "Mỗi INS có mục hệ quả cho sản phẩm"
QUALITY-GATE-MANIFEST:END -->
