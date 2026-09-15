---
doc_id: 07-02
title: Information Architecture
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
depends_on: [07-01]
feeds: [07-03, 07-05, 08-01]
id_prefix: [IA]
gate: G6
in_handover: false
confidence: low
---

# [Tên dự án] — Information Architecture

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


## 1. Mô hình đối tượng
| Đối tượng | Thuộc tính người dùng thấy | Quan hệ | `ENT` liên quan |
| --- | --- | --- | --- |

## 2. Cây điều hướng
```
Gốc
├── IA-001 · [nhãn]
│   ├── IA-002 · [nhãn]
```

| `IA` | Nhãn hiển thị | Cấp | Cha | Chứa gì | `TSK` phục vụ |
| --- | --- | --- | --- | --- | --- |

> Nhãn dùng **từ của người dùng**, khớp `_GLOSSARY.md`.

## 3. Điều hướng chính
| Vị trí | Nhãn | `IA` | Vì sao ở cấp cao nhất |
| --- | --- | --- | --- |

_Tab bar tối đa 5 mục. Quá 5 thì phải gom, ghi rõ gom thế nào._

## 4. Độ sâu
| Nhiệm vụ | Số cấp phải đi qua | Chấp nhận được không |
| --- | --- | --- |

> Độ sâu quá 3 cấp thì người dùng bắt đầu lạc.

## 5. Kiểm
| Kiểm | Kết quả |
| --- | --- |
| Mọi `TSK` có đường trong IA | |
| Mọi node `IA` phục vụ ít nhất một `TSK` | |
| Nhãn khớp `_GLOSSARY` | |

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
doc: 07-02_INFORMATION_ARCHITECTURE
gate: G6
required_major:
  - "0. Đọc nhanh"
  - "1. Mô hình đối tượng"
  - "2. Cây điều hướng"
  - "3. Điều hướng chính"
  - "4. Độ sâu"
  - "5. Kiểm"
  - "6. Nguồn phương pháp"
  - "Thuật ngữ dùng trong tài liệu này"
required_minor:
  {}
quality_checks:
  - "Quyết định cấu trúc nào học từ đối thủ đều trích PAT ở 07-00, không chép lại nội dung"
  - "Mọi node IA phục vụ ít nhất một TSK"
  - "Nhãn khớp _GLOSSARY"
  - "Điều hướng chính không quá 5 mục hoặc có phương án gom"
  - "Có ghi độ sâu bằng số cấp"
QUALITY-GATE-MANIFEST:END -->
