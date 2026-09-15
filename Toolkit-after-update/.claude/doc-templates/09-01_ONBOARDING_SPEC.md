---
doc_id: 09-01
title: Onboarding Specification
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
depends_on: [04-06, 08-01]
feeds: [09-06, 10-03, 12-01]
id_prefix: [ONB]
gate: G8
in_handover: true
confidence: low
---

# [Tên dự án] — Onboarding Specification

> Mục tiêu duy nhất: đưa người dùng tới **aha moment** nhanh nhất. Aha moment lấy từ `04-06`, không định nghĩa lại.

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


## 1. Bối cảnh
| Trường | Nội dung |
| --- | --- |
| Ý định người dùng khi mở app lần đầu | |
| Aha moment | _trích `04-06` mục 4_ |
| Đường ngắn nhất tới đó | _số bước_ |
| Kịch bản đã chọn | |
| Vì sao chọn kịch bản này | |

## 2. Chuỗi màn hình
| `ONB` | Bước | `SCR` | Mục đích | **Có cần trước aha moment không** | Bỏ được không |
| --- | --- | --- | --- | --- | --- |
| `ONB-001` | | | | | |

> Với mỗi bước, hỏi: **bỏ bước này thì người dùng có tới được aha moment không?** Nếu có thì bỏ.

## 3. Thông tin hỏi trước khi cho dùng
| Hỏi gì | Vì sao cần NGAY | Hoãn được không | `PRM` / `ENT` |
| --- | --- | --- | --- |

> Mỗi câu hỏi trước giá trị là một chỗ người dùng rời đi. Chỉ hỏi thứ **không thể** hoãn.

## 4. Vị trí xin quyền
| `PRM` | Xin ở bước nào | Màn giải thích trước | Ba nhánh đã có ở `06-05` |
| --- | --- | --- | --- |

## 5. Vị trí paywall
| Trường | Nội dung |
| --- | --- |
| Paywall xuất hiện ở bước nào | |
| **Trước hay sau aha moment** | |
| Nếu trước, lý do gì đủ mạnh | |
| Có downsell khi đóng không | |

> Paywall trước khi chứng minh giá trị là lỗi phổ biến nhất và tốn kém nhất. Nếu đặt trước aha moment thì
> phải có lý do rõ ràng ghi ở đây.

## 6. Biến thể để thử nghiệm
| Biến thể | Khác gì bản gốc | Giả thuyết | `EXP` |
| --- | --- | --- | --- |

## 7. Đo lường
| Bước | `EVT` | Chỉ số | Target |
| --- | --- | --- | --- |

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
# Nguồn chân lý DUY NHẤT cho G8 phần tài liệu này. KHÔNG chép khối này vào file đầu ra ở docs/.
doc: 09-01_ONBOARDING_SPEC
gate: G8
required_major:
  - "0. Đọc nhanh"
  - "1. Bối cảnh"
  - "2. Chuỗi màn hình"
  - "3. Thông tin hỏi trước khi cho dùng"
  - "4. Vị trí xin quyền"
  - "5. Vị trí paywall"
  - "6. Biến thể để thử nghiệm"
  - "7. Đo lường"
  - "8. Nguồn phương pháp"
  - "Thuật ngữ dùng trong tài liệu này"
required_minor:
  {}
quality_checks:
  - "Aha moment trích từ 04-06, không định nghĩa lại"
  - "Mỗi bước onboarding trả lời được câu bỏ được không"
  - "Nếu paywall đặt trước aha moment thì phải có lý do ghi rõ"
  - "Mỗi bước có EVT tương ứng ở 10-02"
QUALITY-GATE-MANIFEST:END -->
