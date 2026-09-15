---
doc_id: 13-04
title: Acceptance Criteria Pack
phase: 13-handover
skill: dev-handover
profile: Bắt buộc
owner: PO
reviewers: []
version: 0.1.0
status: draft
last_updated:
approved_by: ""
approved_at: ""
depends_on: [06-02, 06-03, 06-04, 08-02]
feeds: [13-01]
id_prefix: [AC]
gate: G11
in_handover: true
confidence: low
---

# [Tên dự án] — Acceptance Criteria Pack

> Gom toàn bộ `AC` từ `06-02` thành bộ nghiệm thu dùng được. **Mọi `FR` phải có ít nhất một mục nghiệm thu.**

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


## 1. Nghiệm thu theo tính năng
### FEAT-001 · [tên]
| `AC` | `FR` | Điều kiện | Các bước kiểm | Kết quả mong đợi | `SCR`/`ST` | Dữ liệu cần chuẩn bị |
| --- | --- | --- | --- | --- | --- | --- |
| `AC-001` | `FR-001` | | | | | |

## 2. Nhóm dễ sót — phải có đủ
> Đây là những nhóm luôn bị quên và luôn là nơi lỗi xuất hiện sau khi phát hành.

| # | Nhóm | Đã có | `AC` |
| --- | --- | --- | --- |
| 1 | Trạng thái lỗi và đường phục hồi | | |
| 2 | Từ chối quyền | | |
| 3 | **Từ chối quyền vĩnh viễn** | | |
| 4 | Mất mạng giữa chừng | | |
| 5 | Chạm ngưỡng giới hạn free | | |
| 6 | Thành công giao dịch | | |
| 7 | Thất bại giao dịch | | |
| 8 | Giao dịch đang chờ | | |
| 9 | Huỷ giữa chừng | | |
| 10 | Hoàn tiền | | |
| 11 | Hết hạn subscription | | |
| 12 | Gia hạn thất bại | | |
| 13 | **Khôi phục mua hàng** | | |
| 14 | Cỡ chữ hệ thống lớn nhất | | |
| 15 | Chế độ tối | | |
| 16 | App bị dừng rồi mở lại | | |

## 3. Nghiệm thu phi chức năng
| `AC` | `NFR` | Ngưỡng | Cách đo | Thiết bị | Đạt |
| --- | --- | --- | --- | --- | --- |

## 4. Nghiệm thu business rule
| `AC` | `BR` | Đầu vào | Kết quả mong đợi | Trường hợp biên đã phủ |
| --- | --- | --- | --- | --- |

## 5. Kiểm phủ
| Kiểm | Kết quả | Vi phạm |
| --- | --- | --- |
| **Mọi `FR` có ≥1 `AC`** | | |
| Mọi `NFR` có cách đo | | |
| Mọi `BR` có nghiệm thu kèm trường hợp biên | | |
| Mục 2 đủ 16 nhóm | | |

> `FR` không nghiệm thu được thì hoặc AC viết chưa đủ, hoặc **FR đó không nên tồn tại**.

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
# Nguồn chân lý DUY NHẤT cho G11 phần tài liệu này. KHÔNG chép khối này vào file đầu ra ở docs/.
doc: 13-04_ACCEPTANCE_CRITERIA_PACK
gate: G11
required_major:
  - "0. Đọc nhanh"
  - "1. Nghiệm thu theo tính năng"
  - "2. Nhóm dễ sót — phải có đủ"
  - "3. Nghiệm thu phi chức năng"
  - "4. Nghiệm thu business rule"
  - "5. Kiểm phủ"
  - "6. Nguồn phương pháp"
  - "Thuật ngữ dùng trong tài liệu này"
required_minor:
  {}
quality_checks:
  - "Mọi FR có ít nhất một AC — điều kiện G11"
  - "Mục 2 đi hết 16 nhóm dễ sót"
  - "Mọi BR có nghiệm thu kèm trường hợp biên"
  - "Mọi NFR có cách đo và thiết bị đo"
QUALITY-GATE-MANIFEST:END -->
