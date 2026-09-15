---
doc_id: 06-05
title: Permission & Data Needs
phase: 06-breakdown
skill: product-breakdown
profile: Bắt buộc
owner: PO
reviewers: []
version: 0.1.0
status: draft
last_updated:
approved_by: ""
approved_at: ""
depends_on: [06-02]
feeds: [08-02, 10-02]
id_prefix: [PRM, ENT]
gate: G5
in_handover: true
confidence: low
---

# [Tên dự án] — Permission & Data Needs

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


## 1. Quyền hệ thống
### PRM-001 · [tên quyền]
| Trường | Nội dung |
| --- | --- |
| Vì sao cần | |
| **Xin vào lúc nào trong luồng** | |
| Màn hình giải thích trước khi xin | `SCR-` |
| `FR` phụ thuộc | |

**Ba nhánh bắt buộc**
| Nhánh | Hành vi app | Màn hình | Người dùng làm gì tiếp |
| --- | --- | --- | --- |
| Đồng ý | | | |
| Từ chối | | | |
| **Từ chối vĩnh viễn** | | | |

> Nhánh từ chối vĩnh viễn hay bị bỏ nhất. Trên di động, khi người dùng đã từ chối vĩnh viễn thì app
> **không thể hỏi lại**, chỉ có thể hướng dẫn mở cài đặt hệ thống. **Mọi quyền phải có nhánh này.**

## 2. Bảng quyền
| `PRM` | Quyền | Xin lúc nào | Đủ 3 nhánh | `FR` phụ thuộc |
| --- | --- | --- | --- | --- |

## 3. Dữ liệu
### ENT-001 · [tên thực thể]
| Trường | Kiểu | Bắt buộc | Nguồn | Ghi chú |
| --- | --- | --- | --- | --- |

| Trường | Nội dung |
| --- | --- |
| Vì sao thu thập | |
| Lưu ở đâu | Trên máy / Server — _theo `TECH-03`_ |
| Giữ bao lâu | |
| Người dùng xoá được không | |
| **Đổi thiết bị thì sao** | |
| Là dữ liệu cá nhân không | |

## 4. Dữ liệu KHÔNG thu thập
> Trích `00-02_SCOPE_LOCK.md` mục Bị cấm.

| Dữ liệu | Vì sao không |
| --- | --- |

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
# Nguồn chân lý DUY NHẤT cho G5 phần tài liệu này. KHÔNG chép khối này vào file đầu ra ở docs/.
doc: 06-05_PERMISSION_AND_DATA_NEEDS
gate: G5
required_major:
  - "0. Đọc nhanh"
  - "1. Quyền hệ thống"
  - "2. Bảng quyền"
  - "3. Dữ liệu"
  - "4. Dữ liệu KHÔNG thu thập"
  - "5. Nguồn phương pháp"
  - "Thuật ngữ dùng trong tài liệu này"
required_minor:
  {}
quality_checks:
  - "Mọi PRM có đủ 3 nhánh gồm từ chối vĩnh viễn — điều kiện G5"
  - "Mọi ENT có mục đổi thiết bị thì sao"
  - "Mục 4 khớp danh sách bị cấm ở 00-02"
  - "Nơi lưu dữ liệu lấy từ TECH-03 hoặc gắn [ASM] + DQ"
QUALITY-GATE-MANIFEST:END -->
