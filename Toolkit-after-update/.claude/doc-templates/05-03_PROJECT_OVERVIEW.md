---
doc_id: 05-03
title: Project Overview
phase: 05-prd
skill: prd-architect
profile: Bắt buộc
owner: PO
reviewers: []
version: 0.1.0
status: draft
last_updated:
approved_by: ""
approved_at: ""
depends_on: [05-01]
feeds: [13-01]
id_prefix: []
gate: G4
in_handover: true
confidence: low
---

# [Tên dự án] — Project Overview

> Bản rút gọn cho **người mới vào dự án đọc trong 10 phút**. Trích PRD, **không lặp lại** nội dung PRD.
> Đây là file đầu tiên đưa cho freelancer.

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


## 1. Sản phẩm này là gì
_Ba câu._

## 2. Cho ai và giải quyết vấn đề gì
| Persona | Vấn đề chính |
| --- | --- |

## 3. Phạm vi bản này
**Có:** _liệt kê ngắn_
**Không có:** _trích `00-02`_

## 4. Ràng buộc phải biết ngay
| Ràng buộc | Chi tiết | Nguồn |
| --- | --- | --- |

## 5. Kiến trúc và công nghệ
> **Phần này do Dev điền** từ `tech-input/TECH-01_ARCHITECTURE.md`.
> Chưa nhận được thì để `[ASM]` và ghi `DQ`, **không tự đoán**.

| Trạng thái | Nguồn | Ngày nhận |
| --- | --- | --- |
| Chưa nhận | `tech-input/TECH-01` | |

## 6. Thứ tự đọc tài liệu
| # | File | Vì sao đọc |
| --- | --- | --- |
| 1 | `00-02_SCOPE_LOCK.md` | biết ranh giới và danh sách bị cấm |
| 2 | `_GLOSSARY.md` | dùng đúng từ ngay từ đầu |
| 3 | `06-02_FUNCTIONAL_REQUIREMENTS.md` | biết phải xây gì |

## 7. Ai quyết định gì
| Vai trò | Sở hữu | Quyền quyết định |
| --- | --- | --- |
| Product Owner | | phạm vi, ưu tiên, giá, duyệt cuối |
| Designer | | giải pháp UX trong phạm vi đã duyệt |
| Developer | `tech-input/` | khả thi kỹ thuật, kiến trúc |

## 8. Nguồn phương pháp

## Thuật ngữ dùng trong tài liệu này

Chép nghĩa một câu từ `docs/_GLOSSARY.md` mục *Thuật ngữ chuyên môn*, và nghĩa của tiền tố mã từ
`docs/_ID_REGISTRY.md`. Chỉ liệt kê thứ **thật sự xuất hiện** trong tài liệu này.

| Thuật ngữ / tiền tố mã | Nghĩa một câu |
| --- | --- |
| | |

> Bảng này không phải để người trong nghề đọc — nó dành cho người ở vai trò khác đang phải duyệt tài liệu
> này. `validate_docs.py` đối chiếu: dùng mà không liệt kê là **LỖI**; liệt kê mà không dùng là cảnh báo.

<!-- QUALITY-GATE-MANIFEST:START
# Nguồn chân lý DUY NHẤT cho G4 phần tài liệu này. KHÔNG chép khối này vào file đầu ra ở docs/.
doc: 05-03_PROJECT_OVERVIEW
gate: G4
required_major:
  - "0. Đọc nhanh"
  - "1. Sản phẩm này là gì"
  - "2. Cho ai và giải quyết vấn đề gì"
  - "3. Phạm vi bản này"
  - "4. Ràng buộc phải biết ngay"
  - "5. Kiến trúc và công nghệ"
  - "6. Thứ tự đọc tài liệu"
  - "7. Ai quyết định gì"
  - "8. Nguồn phương pháp"
  - "Thuật ngữ dùng trong tài liệu này"
required_minor:
  {}
quality_checks:
  - "Không lặp lại nội dung PRD, chỉ trích dẫn"
  - "Mục 5 để trống hoặc [ASM] nếu Dev chưa nộp TECH-01 — không tự đoán kiến trúc"
  - "Mục 3 khớp 00-02_SCOPE_LOCK"
  - "Đọc hết trong 10 phút"
QUALITY-GATE-MANIFEST:END -->
