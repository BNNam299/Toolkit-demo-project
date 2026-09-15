---
doc_id: 10-01
title: KPI Framework
phase: 10-measurement
skill: measurement-designer
profile: Bắt buộc
owner: PO
reviewers: []
version: 0.1.0
status: draft
last_updated:
approved_by: ""
approved_at: ""
depends_on: [05-01, 04-06]
feeds: [10-02, 10-03]
id_prefix: [KPI]
gate: G8
in_handover: true
confidence: low
---

# [Tên dự án] — KPI Framework

> **KPI trước event.** Không định nghĩa event nếu chưa biết nó phục vụ chỉ số nào.

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


## 1. North Star
| Trường | Nội dung |
| --- | --- |
| Chỉ số | |
| Vì sao chỉ số này | |
| **Nếu tăng gấp đôi, người dùng có được lợi hơn không** | |
| Công thức | |
| Baseline | `[ASM]` nếu chưa có số thật |
| Target 3 tháng | |

## 2. Input metrics
| `KPI` | Tên | **Định nghĩa bằng lời** | **Công thức** | Nguồn | Tần suất | Baseline | Target |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `KPI-001` | | | tử/mẫu/cửa sổ thời gian | | | | |

## 3. Guardrail metrics
> Chỉ số **không được xấu đi** khi tối ưu các chỉ số trên. Thiếu guardrail thì tối ưu ngắn hạn phá dài hạn.

| `KPI` | Tên | Ngưỡng không được vượt | Vì sao |
| --- | --- | --- | --- |

## 4. Kiểm vanity metric
| `KPI` | Nếu tăng gấp đôi mà không gì khác đổi, doanh nghiệp tốt hơn không | Kết luận |
| --- | --- | --- |

> Trả lời không thì đó là vanity metric — bỏ. Tổng lượt tải, tổng lượt xem màn hình, tổng tài khoản là ví dụ kinh điển.

## 5. Nối KPI với sản phẩm
| `KPI` | `FEAT` ảnh hưởng | `FR` liên quan | Ai theo dõi |
| --- | --- | --- | --- |

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
doc: 10-01_KPI_FRAMEWORK
gate: G8
required_major:
  - "0. Đọc nhanh"
  - "1. North Star"
  - "2. Input metrics"
  - "3. Guardrail metrics"
  - "4. Kiểm vanity metric"
  - "5. Nối KPI với sản phẩm"
  - "6. Nguồn phương pháp"
  - "Thuật ngữ dùng trong tài liệu này"
required_minor:
  {}
quality_checks:
  - "Đúng một North Star, không nhiều hơn"
  - "Mọi KPI có công thức gồm tử số, mẫu số, cửa sổ thời gian"
  - "Có ít nhất một guardrail metric — điều kiện G8"
  - "Mục 4 loại hết vanity metric"
  - "Baseline chưa có số thật thì gắn [ASM], không bịa"
QUALITY-GATE-MANIFEST:END -->
