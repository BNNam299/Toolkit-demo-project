---
doc_id: 09-06
title: Copy Deck
phase: 09-growth
skill: growth-and-copy
profile: Bắt buộc
owner: PO
reviewers: []
version: 0.1.0
status: draft
last_updated:
approved_by: ""
approved_at: ""
depends_on: [08-01, 08-02, 09-01, 09-02]
feeds: [12-01, 12-03]
id_prefix: [CPY]
gate: G8
in_handover: true
confidence: low
---

# [Tên dự án] — Copy Deck

> **Nguồn chân lý duy nhất về mọi chuỗi văn bản.** File thiết kế và code đều trích từ đây.
> Phải **phủ hết** `SCR` và `ST` — điều kiện đóng G8.

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


## 1. Quy ước key
`<màn>.<thành phần>.<biến thể>` — ví dụ `scan.cta.analyze`, `paywall.title.default`

## 2. Bảng copy
| `CPY` | Key | `SCR` | `ST` | **Nội dung** | Loại | **Giới hạn ký tự** | Ghi chú |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `CPY-001` | | | | | Tiêu đề / Phụ đề / Nút / Nhãn / Lỗi / Rỗng / Tooltip / Thông báo | | |

## 3. Phủ theo loại bắt buộc
> Đi hết bảng. Loại nào không áp dụng thì ghi **Không áp dụng**.

| # | Loại | Đã có | `CPY` |
| --- | --- | --- | --- |
| 1 | Tiêu đề màn hình | | |
| 2 | Phụ đề | | |
| 3 | Nút và CTA | | |
| 4 | Nhãn trường nhập | | |
| 5 | Văn bản gợi ý trong ô nhập | | |
| 6 | Thông báo lỗi | | |
| 7 | Trạng thái rỗng | | |
| 8 | Trạng thái đang tải | | |
| 9 | Xin quyền | | |
| 10 | Tooltip | | |
| 11 | Hộp thoại xác nhận | | |
| 12 | Thông báo đẩy | | |
| 13 | Onboarding | | |
| 14 | Paywall | | |
| 15 | Trial — bắt đầu, sắp hết, đã hết | | |
| 16 | Huỷ subscription | | |
| 17 | Khôi phục mua hàng | | |
| 18 | Trạng thái thành công | | |

## 4. Phủ theo màn hình
| `SCR` | Số `ST` | Số `CPY` đã có | Đủ chưa |
| --- | --- | --- | --- |

## 5. Kiểm
| Kiểm | Kết quả |
| --- | --- |
| Không còn placeholder | |
| Mọi `CPY` có giới hạn ký tự | |
| Không claim sản phẩm không làm được | |
| Thông báo lỗi nói được **cách khắc phục**, không chỉ báo lỗi | |
| Nút mô tả **hành động**, không phải Đồng ý / Huỷ chung chung | |

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
# Nguồn chân lý DUY NHẤT cho G8 phần tài liệu này. KHÔNG chép khối này vào file đầu ra ở docs/.
doc: 09-06_COPY_DECK
gate: G8
required_major:
  - "0. Đọc nhanh"
  - "1. Quy ước key"
  - "2. Bảng copy"
  - "3. Phủ theo loại bắt buộc"
  - "4. Phủ theo màn hình"
  - "5. Kiểm"
  - "6. Nguồn phương pháp"
  - "Thuật ngữ dùng trong tài liệu này"
required_minor:
  {}
quality_checks:
  - "Copy phủ hết SCR và ST, không còn placeholder — điều kiện G8"
  - "Mọi CPY có giới hạn ký tự — điều kiện G8"
  - "Mục 3 đi hết 18 loại, không bỏ trống"
  - "Thông báo lỗi nói cách khắc phục"
  - "Không claim sản phẩm không làm được"
QUALITY-GATE-MANIFEST:END -->
