---
doc_id: 07-05
title: UX Flows
phase: 07-structure
skill: ux-structure-architect
profile: Bắt buộc
owner: Designer
reviewers: []
version: 0.1.0
status: draft
last_updated:
approved_by: ""
approved_at: ""
depends_on: [07-02, 06-02]
feeds: [08-01, 08-04]
id_prefix: [FLOW]
gate: G6
in_handover: true
confidence: low
---

# [Tên dự án] — UX Flows

> **Flow KHÔNG được sinh màn hình mới.** Thiếu màn thì ghi vào `08-04_MISSING_SCREEN_REPORT.md`,
> `SCR` được cấp ở `08-01`, rồi flow mới trích lại. Đây là quy tắc thứ tự bắt buộc.

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


## 1. Ký hiệu
Chữ nhật = màn hình · Thoi = điểm quyết định · Mũi tên = chuyển · Mũi tên đứt = đường tuỳ chọn ·
Mũi tên đậm = đường chính

## 2. Mười loại flow bắt buộc
| # | Loại | `FLOW` | Đã có |
| --- | --- | --- | --- |
| 1 | Đường thuận lợi | | |
| 2 | Đường thay thế | | |
| 3 | Đường lỗi | | |
| 4 | Huỷ giữa chừng | | |
| 5 | Từ chối quyền | | |
| 6 | Không có dữ liệu | | |
| 7 | Đang tải | | |
| 8 | Trạng thái rỗng | | |
| 9 | Bị gián đoạn rồi quay lại | | |
| 10 | Người dùng cũ quay lại | | |

## 3. Flow
### FLOW-001 · [tên]
| Trường | Nội dung |
| --- | --- |
| Mục tiêu người dùng | |
| `UC` nguồn | |
| Điểm vào | |
| **Mọi kết cục** | _liệt kê đủ, không nhánh nào cụt_ |
| Số bước tới giá trị | |

```mermaid
graph TD
```

| Bước | Màn hình `SCR` | Người dùng làm gì | Điều kiện rẽ | Đi tới |
| --- | --- | --- | --- | --- |

## 4. Kiểm phụ thuộc phạm vi

Chạy sau khi vẽ xong mọi nhánh. Đây là chỗ bắt lỗi cắt MVP hụt đường phục hồi.

| Luồng | Tier của luồng | Nhánh phục hồi / tới hạn nó cần | `UC` tương ứng | Tier của `UC` đó | Khớp? |
| --- | --- | --- | --- | --- | --- |
| | Tier 1 / 2 / 3 | ví dụ: chụp thất bại → nhập tay | `UC-xxx` | | ✅ / ❌ |

Ô nào ❌ — nghĩa là luồng Tier 1 đang phụ thuộc vào một `UC` bị đẩy ra khỏi MVP — thì **phải xử lý**,
không được để nguyên. Hai cách hợp lệ:

- **Nâng `UC` đó lên Tier 1**, ghi vào bảng *Nâng hạ phạm vi* ở `05-01` mục 11 kèm `DEC`.
- **Hạ cả luồng xuống Post-MVP**, cũng ghi `DEC`.

Cách **không** hợp lệ: để nguyên và tính sẽ xử lý sau. Người dùng gặp nhánh lỗi ngay tuần đầu, không
phải ở bản sau.

## 5. Kiểm
| Kiểm | Kết quả |
| --- | --- |
| Đủ 10 loại flow bắt buộc | |
| **Mọi nhánh có kết cục** | |
| **Không `SCR` ID lạ** | |
| Màn hình phát sinh đã ghi vào `08-04` | |

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
# Nguồn chân lý DUY NHẤT cho G6 phần tài liệu này. KHÔNG chép khối này vào file đầu ra ở docs/.
doc: 07-05_UX_FLOWS
gate: G6
required_major:
  - "0. Đọc nhanh"
  - "1. Ký hiệu"
  - "2. Mười loại flow bắt buộc"
  - "3. Flow"
  - "4. Kiểm phụ thuộc phạm vi"
  - "5. Kiểm"
  - "6. Nguồn phương pháp"
  - "Thuật ngữ dùng trong tài liệu này"
required_minor:
  {}
quality_checks:
  - "Bước flow nào học từ đối thủ đều trích PAT ở 07-00 kèm quyết định Áp dụng hay Điều chỉnh"
  - "Đủ 10 loại flow bắt buộc — điều kiện G6"
  - "Mọi nhánh có kết cục, không nhánh nào cụt — điều kiện G6"
  - "Không tham chiếu SCR ID chưa được cấp ở 08-01 — điều kiện G6"
  - "Màn hình phát sinh trong lúc làm flow đã ghi vào 08-04"
  - "Bảng ở mục 4 không còn ô ❌: mọi UC đường phục hồi của luồng Tier 1 cũng phải Tier 1 — điều kiện G6"
  - "Mỗi lần nâng hoặc hạ tier đã ghi DEC và cập nhật 05-01 mục 11"
QUALITY-GATE-MANIFEST:END -->
