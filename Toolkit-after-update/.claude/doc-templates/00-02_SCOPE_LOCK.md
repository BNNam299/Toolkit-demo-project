---
doc_id: 00-02
title: Scope Lock — Khoá phạm vi
phase: 00-khoi-tao
skill: doc-orchestrator
profile: Bắt buộc
owner: PO
reviewers: []
version: 0.1.0
status: draft
last_updated:
approved_by: ""
approved_at: ""
depends_on: [00-01]
feeds: [05-01, 06-02]
id_prefix: []
gate: G0
in_handover: true
confidence: low
---

# [Tên dự án] — Scope Lock

> Tài liệu ngắn nhất và mạnh nhất trong bộ. Nó tồn tại để khi AI hoặc freelancer đề xuất thêm backend,
> tài khoản hay cloud sync, bạn có một file cụ thể để chỉ vào.

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


## 1. Trong phạm vi

| # | Hạng mục | Vì sao cần ở bản này |
| --- | --- | --- |
| | | |

## 2. Ngoài phạm vi, đã cân nhắc

> Phần quan trọng nhất. Đã nghĩ tới và **cố ý** không làm khác hoàn toàn với quên.

| # | Hạng mục | Vì sao không làm ở bản này | Cân nhắc lại khi nào |
| --- | --- | --- | --- |
| | | | |

## 3. Bị cấm

> **Không được rỗng.** Cổng G0 không đóng nếu mục này trống.
> Đây là những thứ không được đề xuất, không được thêm, kể cả khi nghe hợp lý.

| # | Bị cấm | Vì sao | Ai được mở khoá |
| --- | --- | --- | --- |
| 1 | | | PO, qua `CHG` |

_Gợi ý những thứ thường nên cấm ở MVP di động: backend riêng, hệ thống tài khoản, đồng bộ đám mây,
thu thập dữ liệu cá nhân ngoài danh sách đã duyệt, tính năng xã hội, đa ngôn ngữ._

## 4. Ràng buộc kỹ thuật đã biết

| # | Ràng buộc | Nguồn | Ảnh hưởng tới |
| --- | --- | --- | --- |
| | | `tech-input/` hoặc `[ASM]` | |

## 5. Quy trình mở khoá

Chỉ Product Owner được mở khoá. Mở khoá đi qua `CHG` ở `_CHANGE_LOG.md`, **không thoả thuận miệng**.

| CHG ID | Ngày | Mục được mở | Lý do | Ảnh hưởng |
| --- | --- | --- | --- | --- |
| | | | | |

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
# Nguồn chân lý DUY NHẤT cho G0 phần tài liệu này. KHÔNG chép khối này vào file đầu ra ở docs/.
doc: 00-02_SCOPE_LOCK
gate: G0
required_major:
  - "0. Đọc nhanh"
  - "1. Trong phạm vi"
  - "2. Ngoài phạm vi, đã cân nhắc"
  - "3. Bị cấm"
  - "4. Ràng buộc kỹ thuật đã biết"
  - "5. Quy trình mở khoá"
  - "6. Nguồn phương pháp"
  - "Thuật ngữ dùng trong tài liệu này"
required_minor:
  {}
quality_checks:
  - "Mục 3 Bị cấm KHÔNG RỖNG — điều kiện đóng G0"
  - "Mục 2 có ít nhất một hạng mục kèm lý do"
  - "Mỗi mục ở 1 và 2 truy được về 00-01"
  - "Ràng buộc kỹ thuật chưa xác nhận đã gắn [ASM] và có DQ"
QUALITY-GATE-MANIFEST:END -->
