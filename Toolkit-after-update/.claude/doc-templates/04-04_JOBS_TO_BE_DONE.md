---
doc_id: 04-04
title: Jobs To Be Done
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
depends_on: [04-03]
feeds: [04-05, 05-01]
id_prefix: [JTBD]
gate: G3
in_handover: true
confidence: low
---

# [Tên dự án] — Jobs To Be Done

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


## 1. Khuôn JTBD
```
Khi [tình huống],
tôi muốn [động cơ],
để [kết quả mong đợi].
```

## 2. Job
### JTBD-001
| Trường | Nội dung |
| --- | --- |
| Phát biểu | Khi … tôi muốn … để … |
| Insight nguồn | `INS-001` |
| Tần suất | |
| Mức quan trọng | |
| Mức hài lòng với cách hiện tại | |
| **Khoảng trống** | _quan trọng cao + hài lòng thấp = cơ hội_ |

## 3. Bảng ưu tiên
| ID | Job | Tần suất | Quan trọng | Hài lòng hiện tại | Khoảng trống | Hạng |
| --- | --- | --- | --- | --- | --- | --- |

## 4. Job phụ và job cảm xúc
> Ngoài job chức năng, người dùng còn có job cảm xúc và job xã hội. Bỏ qua chúng là lý do nhiều sản phẩm
> đúng chức năng mà vẫn không ai dùng.

| ID | Loại | Phát biểu | Insight nguồn |
| --- | --- | --- | --- |
| | Cảm xúc / Xã hội | | |

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
doc: 04-04_JOBS_TO_BE_DONE
gate: G3
required_major:
  - "0. Đọc nhanh"
  - "1. Khuôn JTBD"
  - "2. Job"
  - "3. Bảng ưu tiên"
  - "4. Job phụ và job cảm xúc"
  - "5. Nguồn phương pháp"
  - "Thuật ngữ dùng trong tài liệu này"
required_minor:
  {}
quality_checks:
  - "Mỗi JTBD dẫn về ít nhất một INS hoặc một bản ghi nghiên cứu cụ thể — không tự nghĩ ra job"
  - "Mọi JTBD viết đúng khuôn Khi/tôi muốn/để"
  - "Mỗi JTBD truy được về một INS"
  - "Mục 4 có ít nhất một job cảm xúc hoặc xã hội"
QUALITY-GATE-MANIFEST:END -->
