---
doc_id: 08-01
title: Screen Inventory
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
depends_on: [07-02, 07-05]
feeds: [08-02, 08-03, 09-06, 12-01]
id_prefix: [SCR]
gate: G7
in_handover: true
confidence: low
---

# [Tên dự án] — Screen Inventory

> **Kiểm kê TRƯỚC khi vẽ.** Vẽ trước khi kiểm kê thì số màn luôn thiếu 40–60%, và thiếu đúng ở chỗ đắt nhất.
> Đây là nơi **duy nhất** cấp mã `SCR`.

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


## 1. Danh sách màn hình
| `SCR` | Tên | Loại | `IA` | `FLOW` xuất hiện | `FR` liên quan | Ưu tiên |
| --- | --- | --- | --- | --- | --- | --- |
| `SCR-001` | | Chính / Phụ / Modal / Bottom sheet / Xác nhận | | `FLOW-001` | | |

## 2. Kiểm kê theo nhóm bắt buộc
> Đi hết bảng này. Nhóm nào không áp dụng thì ghi **Không áp dụng** kèm lý do, **không bỏ trống**.

| Nhóm | Có màn hình nào | `SCR` |
| --- | --- | --- |
| Màn hình chính | | |
| Màn hình phụ | | |
| Modal | | |
| Bottom sheet | | |
| Xác nhận | | |
| Đang tải | | |
| Trạng thái rỗng | | |
| Lỗi | | |
| Mất mạng | | |
| Xin quyền | | |
| Bị từ chối quyền vĩnh viễn | | |
| Lần đầu dùng | | |
| Người dùng cũ quay lại | | |
| Thành công | | |
| Thất bại | | |
| Hoàn thành một phần | | |
| Onboarding | | |
| Paywall | | |
| Đang có subscription | | |
| Nội dung bị khoá | | |
| Hết hạn subscription | | |
| Khôi phục mua hàng | | |
| Hết lượt free | | |

## 3. Kiểm mồ côi
| Kiểm | Kết quả | `SCR` vi phạm |
| --- | --- | --- |
| Mọi `SCR` xuất hiện trong ≥1 `FLOW` | | |
| Mọi `SCR` phục vụ ít nhất một `FR` hoặc `TSK` | | |

## 4. Ước lượng công thiết kế
| `SCR` | Độ phức tạp | Số trạng thái | Ước lượng |
| --- | --- | --- | --- |

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
doc: 08-01_SCREEN_INVENTORY
gate: G7
required_major:
  - "0. Đọc nhanh"
  - "1. Danh sách màn hình"
  - "2. Kiểm kê theo nhóm bắt buộc"
  - "3. Kiểm mồ côi"
  - "4. Ước lượng công thiết kế"
  - "5. Nguồn phương pháp"
  - "Thuật ngữ dùng trong tài liệu này"
required_minor:
  {}
quality_checks:
  - "Mục 2 đi hết mọi nhóm, không nhóm nào bỏ trống — điều kiện G7"
  - "Không màn hình mồ côi: mọi SCR xuất hiện trong ≥1 FLOW — điều kiện G7"
  - "Screen inventory làm trước wireframe 08-03"
  - "Đây là nơi duy nhất cấp mã SCR"
QUALITY-GATE-MANIFEST:END -->
