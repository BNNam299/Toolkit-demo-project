---
doc_id: 08-02
title: State & Edge Case Matrix
phase: 08-screens
skill: screen-inventory-wireframe
profile: Bắt buộc
owner: Designer
reviewers: []
version: 0.1.0
status: draft
last_updated:
approved_by: ""
approved_at: ""
depends_on: [08-01, 06-03, 06-04, 06-05]
feeds: [08-03, 09-06, 12-01]
id_prefix: [ST]
gate: G7
in_handover: true
confidence: low
---

# [Tên dự án] — State & Edge Case Matrix

> **Không còn ô `?` là điều kiện đóng G7.** Mỗi ô là một frame phải dựng ở phase 12.

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


## 1. Ma trận trạng thái
| `SCR` | Đang tải | Rỗng | Có dữ liệu | Lỗi | Mất mạng | Không quyền | Hết lượt | Bị khoá |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `SCR-001` | `ST-001` | `ST-002` | `ST-003` | `ST-004` | | | | Không áp dụng |

_Ô không áp dụng thì ghi **Không áp dụng**, không để trống và không để `?`._

## 1b. Ma trận trạng thái theo ngữ cảnh người dùng

Trục trên là **trạng thái dữ liệu** — máy đang có gì. Trục này là **trạng thái người dùng** — họ đang ở đâu
trong quan hệ với sản phẩm. Cùng một màn, cùng dữ liệu đầy đủ, nhưng người mở lần đầu và người dùng ba tháng
cần **hai màn khác nhau**.

| `SCR` | Lần đầu vào | Quay lại | Đã thành thạo | Còn lỗi từ phiên trước |
| --- | --- | --- | --- | --- |
| `SCR-001` | `ST-005` | `ST-006` | `ST-007` | Không áp dụng |

| Ngữ cảnh | Nghĩa | Khác gì so với mặc định |
| --- | --- | --- |
| **Lần đầu vào** | vừa xong onboarding, chưa có dữ liệu của chính họ | thường có thẻ mời làm việc đầu tiên, hoặc dữ liệu mẫu |
| **Quay lại** | đã dùng ≥1 lần, có dữ liệu | mặc định của màn |
| **Đã thành thạo** | dùng thường xuyên, đã hết chỗ để hướng dẫn | **mật độ giảm** — bỏ thẻ gợi ý, bỏ nhắc nhở, nhường chỗ cho nội dung |
| **Còn lỗi từ phiên trước** | phiên trước có lỗi chưa xử | thêm một dòng cảnh báo, và **nó phải tự mất** khi lỗi hết |

**Cột "Đã thành thạo" là cột hay bị bỏ nhất và cũng đáng nhất.** Hầu hết sản phẩm dạy người dùng mãi không
thôi: thẻ gợi ý ở màn chính vẫn còn đó sau ba tháng, chiếm chỗ của thứ họ thật sự muốn xem. Điền cột này là
buộc mình quyết định *"khi nào thì thôi hướng dẫn"*.

Ô nào không áp dụng thì ghi **Không áp dụng** kèm lý do một câu. Ô trống là chưa nghĩ tới.

**Mỗi ô có mã `ST` ở bảng này cũng là một màn phải dựng** ở phase 08 và một frame phải dựng ở phase 12 —
đếm chung với bảng mục 1.

## 2. Chi tiết trạng thái
### ST-001 · SCR-001 · [tên trạng thái]
| Trường | Nội dung |
| --- | --- |
| Điều kiện vào trạng thái | |
| Người dùng thấy gì | |
| **Đường thoát** | |
| `CPY` liên quan | |
| `BR` áp dụng | |

> **Mọi trạng thái phải có đường thoát.** Trạng thái không lối ra là chỗ người dùng bỏ app.

## 3. Edge case
| # | Tình huống | `SCR` ảnh hưởng | Hành vi yêu cầu | `BR` |
| --- | --- | --- | --- | --- |
| 1 | Mất mạng giữa luồng | | | |
| 2 | App bị dừng rồi mở lại | | | |
| 3 | Đổi thiết bị | | | |
| 4 | Cỡ chữ hệ thống lớn nhất | | | |
| 5 | Chế độ tối | | | |
| 6 | Từ chối quyền vĩnh viễn | | | |
| 7 | Hết dung lượng | | | |

## 4. Trạng thái giao dịch
> Tám trạng thái bắt buộc nếu có subscription.

| # | Trạng thái | `SCR` | `ST` | Người dùng thấy gì |
| --- | --- | --- | --- | --- |
| 1 | Thành công | | | |
| 2 | Thất bại | | | |
| 3 | Đang chờ | | | |
| 4 | Huỷ giữa chừng | | | |
| 5 | Hoàn tiền | | | |
| 6 | Hết hạn | | | |
| 7 | Gia hạn thất bại | | | |
| 8 | Khôi phục mua hàng | | | |

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
# Nguồn chân lý DUY NHẤT cho G7 phần tài liệu này. KHÔNG chép khối này vào file đầu ra ở docs/.
doc: 08-02_STATE_MATRIX
gate: G7
required_major:
  - "0. Đọc nhanh"
  - "1. Ma trận trạng thái"
  - "1b. Ma trận trạng thái theo ngữ cảnh người dùng"
  - "2. Chi tiết trạng thái"
  - "3. Edge case"
  - "4. Trạng thái giao dịch"
  - "5. Nguồn phương pháp"
  - "Thuật ngữ dùng trong tài liệu này"
required_minor:
  {}
quality_checks:
  - "Ma trận KHÔNG còn ô `?` — điều kiện G7"
  - "Mọi trạng thái có đường thoát"
  - "Mục 3 đi hết 7 edge case"
  - "Mục 4 đủ 8 trạng thái giao dịch nếu có subscription"
  - "Mục 1b có mặt và không ô nào để trống — ô không áp dụng thì ghi Không áp dụng kèm lý do"
  - "Cột 'Đã thành thạo' ở mục 1b đã điền: đã quyết định khi nào thôi hướng dẫn, khi nào giảm mật độ"
  - "Mã ST ở mục 1b đếm chung với mục 1 — mỗi ô là một màn phải dựng ở phase 08"
QUALITY-GATE-MANIFEST:END -->
