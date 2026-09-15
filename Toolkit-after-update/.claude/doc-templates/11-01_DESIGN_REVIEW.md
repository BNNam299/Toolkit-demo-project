---
doc_id: 11-01
title: UI/UX Design Review
phase: 11-evaluation
skill: design-quality-auditor
profile: Bắt buộc
owner: Designer
reviewers: []
version: 0.1.0
status: draft
last_updated:
approved_by: ""
approved_at: ""
depends_on: [08-03, 09-06]
feeds: [11-03]
id_prefix: [DF]
gate: G9
in_handover: false
confidence: low
---

# [Tên dự án] — UI/UX Design Review

> Review **chỉ liệt kê finding, không tự sửa file nguồn**. Không đánh giá kiểu đẹp/xấu chủ quan.

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


## 1. Bối cảnh đánh giá
| Trường | Nội dung |
| --- | --- |
| Đánh giá cái gì | Wireframe `08-03` / Prototype |
| Ai là người dùng | `PER-001` |
| Trong bối cảnh nào | |
| Nhiệm vụ nào được xét | `TSK-` |

## 2. Finding
| `DF` | **Vị trí** | **Quan sát** | **Vấn đề** | **Heuristic vi phạm** | Bằng chứng | **Mức** | Tác động người dùng | Tác động kinh doanh | Đề xuất | Ưu tiên |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `DF-001` | `SCR-003` `ST-002` | | | | | Critical / Cao / TB / Thấp | | | | |

## 3. Phân loại finding
> Phân biệt rõ, vì mỗi loại xử lý khác nhau.

| `DF` | Loại |
| --- | --- |
| | Sở thích thị giác / Vấn đề usability / Vấn đề tiếp cận / Lỗi logic sản phẩm / Vấn đề nội dung / Giới hạn kỹ thuật |

> **Sở thích thị giác không phải finding.** Nếu chỉ là "tôi thấy không đẹp" thì không đưa vào mục 2.

## 4. Kiểm heuristic
| # | Heuristic | Kết quả | `DF` |
| --- | --- | --- | --- |
| 1 | Hiển thị trạng thái hệ thống | | |
| 2 | Khớp mô hình thế giới thực | | |
| 3 | Người dùng kiểm soát và thoát được | | |
| 4 | Nhất quán và theo chuẩn | | |
| 5 | Phòng ngừa lỗi | | |
| 6 | Nhận ra thay vì phải nhớ | | |
| 7 | Linh hoạt và hiệu quả | | |
| 8 | Thiết kế tối giản | | |
| 9 | Giúp nhận biết và khắc phục lỗi | | |
| 10 | Trợ giúp và tài liệu | | |

## 5. Kiểm tiếp cận
| Kiểm | Kết quả | `DF` |
| --- | --- | --- |
| Tương phản ≥ 4.5:1 | | |
| Vùng chạm ≥ 44pt | | |
| Cỡ chữ hệ thống lớn nhất không vỡ layout | | |
| Màu không phải kênh truyền tin duy nhất | | |
| Nhãn cho trình đọc màn hình | | |
| Thứ tự đọc hợp lý | | |

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
# Nguồn chân lý DUY NHẤT cho G9 phần tài liệu này. KHÔNG chép khối này vào file đầu ra ở docs/.
doc: 11-01_DESIGN_REVIEW
gate: G9
required_major:
  - "0. Đọc nhanh"
  - "1. Bối cảnh đánh giá"
  - "2. Finding"
  - "3. Phân loại finding"
  - "4. Kiểm heuristic"
  - "5. Kiểm tiếp cận"
  - "6. Nguồn phương pháp"
  - "Thuật ngữ dùng trong tài liệu này"
required_minor:
  {}
quality_checks:
  - "Mỗi DF có đủ vị trí, quan sát, vấn đề, heuristic vi phạm, mức, đề xuất"
  - "Sở thích thị giác không được đưa vào mục 2 như finding"
  - "Review không sửa file nguồn"
  - "Mục 4 đi hết 10 heuristic, mục 5 đi hết 6 dòng tiếp cận"
QUALITY-GATE-MANIFEST:END -->
