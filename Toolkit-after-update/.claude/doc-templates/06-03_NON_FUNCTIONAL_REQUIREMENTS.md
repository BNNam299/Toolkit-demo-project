---
doc_id: 06-03
title: Non-Functional Requirements
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
feeds: [08-02, 12-02, 13-04]
id_prefix: [NFR]
gate: G5
in_handover: true
confidence: low
---

# [Tên dự án] — Non-Functional Requirements

> **Mỗi NFR phải có số và điều kiện đo.** Không có số thì đó là lời chúc, không phải yêu cầu.
> Ngưỡng chưa xác nhận với Dev thì gắn `[ASM]` và tạo `DQ` — **không bịa con số nghe hợp lý**.

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


## 1. Thiết bị tham chiếu
| Mức | Thiết bị | OS | Nguồn |
| --- | --- | --- | --- |
| Thấp nhất hỗ trợ | | | `TECH-04` |
| Phổ biến | | | |
| Cao cấp | | | |

## 2. Hiệu năng
| `NFR` | Yêu cầu | **Ngưỡng** | **Đo trên thiết bị nào, mạng nào** | Nguồn | Nhãn |
| --- | --- | --- | --- | --- | --- |
| `NFR-001` | Thời gian khởi động lạnh | | | `TECH-04` | `[FACT]` / `[ASM]` |

## 3. Độ tin cậy
| `NFR` | Tình huống | Hành vi yêu cầu | Ngưỡng |
| --- | --- | --- | --- |
| | Mất mạng giữa chừng | | |
| | App bị hệ điều hành dừng | | |
| | Hết dung lượng lưu trữ | | |

## 4. Tiếp cận
| `NFR` | Yêu cầu | Ngưỡng | Cách kiểm |
| --- | --- | --- | --- |
| | Tương phản chữ thường | ≥ 4.5:1 | |
| | Vùng chạm | ≥ 44pt mỗi chiều | |
| | Cỡ chữ hệ thống lớn nhất | layout không vỡ, không cắt chữ | |
| | Màu không phải kênh truyền tin duy nhất | | |
| | Nhãn cho trình đọc màn hình | mọi thành phần tương tác | |

## 5. Tương thích
| `NFR` | Yêu cầu | Ngưỡng | Nguồn |
| --- | --- | --- | --- |

## 6. Bảo mật và riêng tư
| `NFR` | Dữ liệu | Lưu ở đâu | Mã hoá | Giữ bao lâu | Người dùng xoá được không |
| --- | --- | --- | --- | --- | --- |

## 7. Vận hành
| `NFR` | Yêu cầu | Ngưỡng |
| --- | --- | --- |
| | Crash-free session | | |

## 8. Ngưỡng chưa xác nhận
| `NFR` | Ngưỡng tạm | `DQ` | Ảnh hưởng nếu sai |
| --- | --- | --- | --- |

## 9. Nguồn phương pháp

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
doc: 06-03_NON_FUNCTIONAL_REQUIREMENTS
gate: G5
required_major:
  - "0. Đọc nhanh"
  - "1. Thiết bị tham chiếu"
  - "2. Hiệu năng"
  - "3. Độ tin cậy"
  - "4. Tiếp cận"
  - "5. Tương thích"
  - "6. Bảo mật và riêng tư"
  - "7. Vận hành"
  - "8. Ngưỡng chưa xác nhận"
  - "9. Nguồn phương pháp"
  - "Thuật ngữ dùng trong tài liệu này"
required_minor:
  {}
quality_checks:
  - "Mọi NFR có số VÀ điều kiện đo (thiết bị nào, mạng nào) — điều kiện G5"
  - "Ngưỡng chưa xác nhận với Dev có [ASM] và DQ, không bịa số"
  - "Mục 4 có đủ 5 dòng tiếp cận tối thiểu"
  - "Mục 3 phủ mất mạng, bị dừng, hết dung lượng"
QUALITY-GATE-MANIFEST:END -->
