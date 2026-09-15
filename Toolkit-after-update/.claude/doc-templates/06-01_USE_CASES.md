---
doc_id: 06-01
title: Use Cases
phase: 06-breakdown
skill: product-breakdown
profile: Bắt buộc
owner: PO
reviewers: []
version: 0.1.0
status: draft
last_updated:
approved_by: ""
approved_at: ""
depends_on: [05-01]
feeds: [06-02, 07-01]
id_prefix: [UC]
gate: G5
in_handover: true
confidence: low
---

# [Tên dự án] — Use Cases

> UC mô tả **người dùng làm gì**, không mô tả hệ thống làm gì. Dùng ngôn ngữ người dùng.
> **Mỗi `FEAT` phải có ≥1 `UC`** — điều kiện đóng G5.

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


## 1. Bảng phủ tính năng
| `FEAT` | Tính năng | UC tương ứng | Đủ chưa |
| --- | --- | --- | --- |
| `FEAT-001` | | `UC-001`, `UC-002` | |

## 2. Use case
### UC-001 · [tên bắt đầu bằng động từ]
| Trường | Nội dung |
| --- | --- |
| Actor | |
| Tiền điều kiện | |
| Kích hoạt | |
| Hậu điều kiện | |
| `FEAT` liên quan | |
| Persona | `PER-001` |

**Luồng chính**
| # | Người dùng làm gì | Hệ thống phản hồi gì |
| --- | --- | --- |
| 1 | | |

**Luồng thay thế**
| ID | Rẽ ở bước nào | Điều kiện | Diễn biến | Kết cục |
| --- | --- | --- | --- | --- |
| `UC-001-A1` | | | | |

**Luồng ngoại lệ**
> Với **mỗi** bước ở luồng chính, hỏi: bước này hỏng được không, và hỏng thì người dùng đi đâu?

| ID | Hỏng ở bước nào | Nguyên nhân | Người dùng thấy gì | Đường thoát |
| --- | --- | --- | --- | --- |
| `UC-001-E1` | | | | |

## 3. Kiểm
| UC | Có luồng thay thế | Có luồng ngoại lệ | Mọi nhánh có kết cục |
| --- | --- | --- | --- |

> UC chỉ có luồng chính, không nhánh nào, thì gần như chắc chắn viết chưa xong.

## 4. Nguồn phương pháp

## Thuật ngữ dùng trong tài liệu này

Chép nghĩa một câu từ `docs/_GLOSSARY.md` mục *Thuật ngữ chuyên môn*, và nghĩa của tiền tố mã từ
`docs/_ID_REGISTRY.md`. Chỉ liệt kê thứ **thật sự xuất hiện** trong tài liệu này.

| Thuật ngữ / tiền tố mã | Nghĩa một câu |
| --- | --- |
| | |

> Bảng này không phải để người trong nghề đọc — nó dành cho người ở vai trò khác đang phải duyệt tài liệu
> này. `validate_docs.py` đối chiếu: dùng mà không liệt kê là **LỖI**; liệt kê mà không dùng là cảnh báo.

<!-- QUALITY-GATE-MANIFEST:START
# Nguồn chân lý DUY NHẤT cho G5 phần tài liệu này. KHÔNG chép khối này vào file đầu ra ở docs/.
doc: 06-01_USE_CASES
gate: G5
required_major:
  - "0. Đọc nhanh"
  - "1. Bảng phủ tính năng"
  - "2. Use case"
  - "3. Kiểm"
  - "4. Nguồn phương pháp"
  - "Thuật ngữ dùng trong tài liệu này"
required_minor:
  {}
quality_checks:
  - "Mọi FEAT có ≥1 UC — điều kiện G5"
  - "Mọi UC có luồng thay thế VÀ luồng ngoại lệ"
  - "Mọi nhánh có kết cục, không nhánh nào cụt"
  - "UC viết bằng ngôn ngữ người dùng, không dùng từ kỹ thuật"
QUALITY-GATE-MANIFEST:END -->
