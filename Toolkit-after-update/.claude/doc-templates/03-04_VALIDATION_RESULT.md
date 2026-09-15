---
doc_id: 03-04
title: Validation Result
phase: 03-opportunity
skill: opportunity-validator
profile: Có điều kiện
owner: PO
reviewers: []
version: 0.1.0
status: draft
last_updated:
approved_by: ""
approved_at: ""
depends_on: [03-03]
feeds: [05-01]
id_prefix: []
gate: G2
in_handover: false
confidence: low
---

# [Tên dự án] — Validation Result

> Chỉ viết file này **sau khi** đã chạy `03-03`. So kết quả với ngưỡng đã đặt trước, **không sửa ngưỡng**.

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


## 1. Đã chạy gì

| VAL | Phương pháp | Ngày bắt đầu | Ngày kết thúc | Cỡ mẫu thực tế | Kênh |
| --- | --- | --- | --- | --- | --- |

## 2. Kết quả thô

| VAL | Chỉ số | Ngưỡng PASS đã đặt | Ngưỡng KILL đã đặt | **Kết quả thực tế** | Kết luận |
| --- | --- | --- | --- | --- | --- |
| `VAL-001` | | | | | PASS / KILL / Vùng xám |

> Nếu bạn thấy mình muốn sửa ngưỡng sau khi nhìn kết quả — dừng lại. Đó là dấu hiệu kết quả không như mong đợi,
> không phải dấu hiệu ngưỡng sai.

## 3. Điều học được ngoài dự kiến

| # | Điều học được | Nguồn | Ảnh hưởng tới concept |
| --- | --- | --- | --- |

## 4. Giới hạn của kết quả

> **Ý định không phải hành vi.** Người nói sẽ dùng khác người thật sự dùng. Người bấm vào quảng cáo khác
> người trả tiền. Ghi rõ kết quả này chứng minh được gì và **không** chứng minh được gì.

| Kết quả | Chứng minh được | KHÔNG chứng minh được |
| --- | --- | --- |

## 5. Quyết định

| Trường | Nội dung |
| --- | --- |
| Quyết định | Đi tiếp / Xoay hướng / Dừng |
| Căn cứ | |
| DEC ID | `DEC-` |
| Giả định nào vẫn còn sống | `ASM-` |

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
# Nguồn chân lý DUY NHẤT cho G2 phần tài liệu này. KHÔNG chép khối này vào file đầu ra ở docs/.
doc: 03-04_VALIDATION_RESULT
gate: G2
required_major:
  - "0. Đọc nhanh"
  - "1. Đã chạy gì"
  - "2. Kết quả thô"
  - "3. Điều học được ngoài dự kiến"
  - "4. Giới hạn của kết quả"
  - "5. Quyết định"
  - "6. Nguồn phương pháp"
  - "Thuật ngữ dùng trong tài liệu này"
required_minor:
  {}
quality_checks:
  - "Ngưỡng ở mục 2 khớp nguyên văn ngưỡng đã đặt ở 03-03, không bị sửa"
  - "Mục 4 không bỏ trống — phải nêu điều KHÔNG chứng minh được"
  - "Mục 5 có DEC ID"
  - "Giả định còn sống đã liệt kê và có ở _ASSUMPTION_REGISTER"
QUALITY-GATE-MANIFEST:END -->
