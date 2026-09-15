---
doc_id: 11-02
title: Usability Evaluation
phase: 11-evaluation
skill: design-quality-auditor
profile: Có điều kiện
owner: Designer
reviewers: []
version: 0.1.0
status: draft
last_updated:
approved_by: ""
approved_at: ""
depends_on: [08-03]
feeds: [11-03]
id_prefix: [UF]
gate: G9
in_handover: false
confidence: low
---

# [Tên dự án] — Usability Evaluation

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


## 1. Chế độ và bối cảnh
| Trường | Nội dung |
| --- | --- |
| Chế độ | Đánh giá chuyên gia / Kiểm thử có điều phối |
| **Who** — ai tham gia | |
| **When** — ở giai đoạn nào | |
| **Why** — quyết định nào phụ thuộc | |
| **How** — cách chạy | |

## 2. Nhiệm vụ kiểm thử
| # | Nhiệm vụ | Dựa trên goal thật nào | **Tiêu chí thành công** | **Tiêu chí thất bại** | Dữ liệu cần ghi |
| --- | --- | --- | --- | --- | --- |

> Nhiệm vụ **không được tiết lộ cách thực hiện**. Sai: "Bấm nút Phân tích ở góc dưới". Đúng: "Bạn vừa ăn xong,
> hãy ghi lại bữa ăn này."

## 3. Thang điểm
| Điểm | Nghĩa |
| --- | --- |
| 4 | Tốt, không cần sửa |
| 3 | Chưa tối ưu, có thể sửa |
| 2 | Vấn đề khá nghiêm trọng, cần sửa |
| 1 | Rất nghiêm trọng, phải sửa sớm |
| **0** | **Blocker — không sửa thì người dùng không hoàn thành được mục tiêu** |

## 4. Chấm theo 5 thành phần
| Thành phần | Điểm | Căn cứ | `UF` liên quan |
| --- | --- | --- | --- |
| Learnability | | | |
| Efficiency | | | |
| Memorability | | | |
| Errors | | | |
| Satisfaction | | | |

## 5. Finding
| `UF` | Nhiệm vụ | Quan sát | Điểm | Thành phần | Số người gặp | Đề xuất |
| --- | --- | --- | --- | --- | --- | --- |

## 6. Chỉ số
| Chỉ số | Giá trị | Cỡ mẫu |
| --- | --- | --- |
| Tỷ lệ hoàn thành nhiệm vụ | | |
| Thời gian mỗi nhiệm vụ | | |
| Tỷ lệ lỗi | | |
| Số lần bấm nhầm | | |
| Số lần phải quay lại | | |
| Số lần cần trợ giúp | | |

## 7. Giới hạn
> Cỡ mẫu nhỏ **không** kết luận được về tỷ lệ. Nó phát hiện vấn đề, không đo được mức phổ biến của vấn đề.

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
# Nguồn chân lý DUY NHẤT cho G9 phần tài liệu này. KHÔNG chép khối này vào file đầu ra ở docs/.
doc: 11-02_USABILITY_EVALUATION
gate: G9
required_major:
  - "0. Đọc nhanh"
  - "1. Chế độ và bối cảnh"
  - "2. Nhiệm vụ kiểm thử"
  - "3. Thang điểm"
  - "4. Chấm theo 5 thành phần"
  - "5. Finding"
  - "6. Chỉ số"
  - "7. Giới hạn"
  - "8. Nguồn phương pháp"
  - "Thuật ngữ dùng trong tài liệu này"
required_minor:
  {}
quality_checks:
  - "Mục 1 xác định đủ Who/When/Why/How trước khi đánh giá"
  - "Nhiệm vụ không tiết lộ cách thực hiện"
  - "Mỗi nhiệm vụ có tiêu chí thành công VÀ thất bại"
  - "Mục 7 nêu giới hạn cỡ mẫu, không kết luận về tỷ lệ"
QUALITY-GATE-MANIFEST:END -->
