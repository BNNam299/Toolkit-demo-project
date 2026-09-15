---
doc_id: 12-03
title: Prototype Review
phase: 12-prototype
skill: figma-prototype-spec
profile: Bắt buộc
owner: Designer
reviewers: []
version: 0.1.0
status: draft
last_updated:
approved_by: ""
approved_at: ""
depends_on: [12-01, 12-02, 08-01, 08-02, 09-06]
feeds: [13-01]
id_prefix: []
gate: G10
in_handover: false
confidence: low
---

# [Tên dự án] — Prototype Review

> Chạy **sau khi** người dựng xong Figma. Đây là lúc đối chiếu bản đã dựng ngược lại tài liệu.

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


## 1. Màn thiếu
| `SCR` | `ST` | Có trong tài liệu | Có frame trong Figma | Hành động |
| --- | --- | --- | --- | --- |
| | | Có | **Không** | Dựng bổ sung |

## 2. Màn thừa
> Thường là dấu hiệu **tốt** — người dựng phát hiện trạng thái tài liệu bỏ sót.
> Nhưng phải **cập nhật ngược** vào `08-01` và `08-02`, không để nó chỉ tồn tại trong Figma.

| Tên frame | Không có mã trong tài liệu | Đây có phải trạng thái thật không | `SCR`/`ST` cần cấp | `CHG` |
| --- | --- | --- | --- | --- |

## 3. Trạng thái thiếu
| `SCR` | Đủ 4 trạng thái đang tải/rỗng/lỗi/có dữ liệu | Đủ nhánh quyền | Thiếu gì |
| --- | --- | --- | --- |

## 4. Chữ lệch
> `09-06_COPY_DECK.md` là nguồn chân lý. Nếu chữ trong Figma hay hơn thì **sửa copy deck trước**, rồi mới
> sửa Figma — đừng để hai bên nói khác nhau.

| `CPY` | Bản trong copy deck | Bản trong Figma | Bên nào đúng | Hành động |
| --- | --- | --- | --- | --- |

## 5. Kiểm tiếp cận trên bản đã dựng
| # | Ngưỡng | Kết quả đo thật | Đạt |
| --- | --- | --- | --- |

## 6. Cập nhật ngược
| # | Sai lệch | Tài liệu phải sửa | `CHG` | Đã sửa |
| --- | --- | --- | --- | --- |

## 7. Kiểm đóng cổng G10
| Kiểm | Kết quả |
| --- | --- |
| Mọi frame bắt buộc đã dựng | |
| Tên frame khớp mã `SCR`/`ST` | |
| Không còn Lorem Ipsum | |
| Mọi sai lệch đã cập nhật ngược | |
| Baseline tiếp cận đã kiểm trên bản thật | |

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
# Nguồn chân lý DUY NHẤT cho G10 phần tài liệu này. KHÔNG chép khối này vào file đầu ra ở docs/.
doc: 12-03_PROTOTYPE_REVIEW
gate: G10
required_major:
  - "0. Đọc nhanh"
  - "1. Màn thiếu"
  - "2. Màn thừa"
  - "3. Trạng thái thiếu"
  - "4. Chữ lệch"
  - "5. Kiểm tiếp cận trên bản đã dựng"
  - "6. Cập nhật ngược"
  - "7. Kiểm đóng cổng G10"
  - "8. Nguồn phương pháp"
  - "Thuật ngữ dùng trong tài liệu này"
required_minor:
  {}
quality_checks:
  - "Mọi frame bắt buộc đã dựng và tên khớp mã — điều kiện G10"
  - "Mọi sai lệch đã cập nhật ngược vào 08-01, 08-02, 09-06"
  - "Không còn Lorem Ipsum"
  - "Baseline tiếp cận đo trên bản đã dựng, không chỉ trên giấy"
QUALITY-GATE-MANIFEST:END -->
