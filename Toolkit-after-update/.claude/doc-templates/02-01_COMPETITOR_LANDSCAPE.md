---
doc_id: 02-01
title: Competitor Landscape
phase: 02-competitor
skill: competitor-intel
profile: Bắt buộc
owner: PO
reviewers: []
version: 0.1.0
status: draft
last_updated:
approved_by: ""
approved_at: ""
depends_on: [01-01]
feeds: [02-04, 05-01]
id_prefix: [COM]
gate: G1
in_handover: true
confidence: low
---

# [Tên dự án] — Competitor Landscape

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


## 1. Phạm vi khảo sát

### 1.1 Tiêu chí đưa vào danh sách
### 1.2 Thị trường và nền tảng đã xét

## 2. Bản đồ đối thủ

| ID | Tên | Loại | Nền tảng | Mô hình giá | Quy mô công bố | Nhãn |
| --- | --- | --- | --- | --- | --- | --- |
| `COM-001` | | Trực tiếp / Gián tiếp / Thay thế thủ công | | | Không công bố | `[FACT]` |

_Loại **thay thế thủ công** hay bị bỏ nhưng thường là đối thủ lớn nhất — Excel, giấy bút, ghi chú điện thoại._

## 3. Định vị

| Đối thủ | Nhắm vào ai | Giải quyết vấn đề gì | Điểm mạnh rõ nhất | Điểm yếu rõ nhất |
| --- | --- | --- | --- | --- |

## 4. Mô hình kiếm tiền

| Đối thủ | Mô hình | Giá công bố | Có trial | Giới hạn bản free |
| --- | --- | --- | --- | --- |

## 5. Ma trận vị trí tính năng

> Framework F1 ở `_depth/02-competitor/paywall-ads-strategy`. Cần **5–6 app cùng loại, cùng thị trường**
> bạn nhắm tới. Phải **tự vào app bấm thử** — mô tả trên store không nói cái gì bị khoá sau paywall.

| Tính năng | Số đối thủ có | Đối thủ để free hay trả phí | Vùng | App của mình có chưa |
| --- | --- | --- | --- | --- |
| | /6 | Free / Trả phí | Baseline / Core Premium / Premium Differentiator / Niche Utility | |

| Vùng | Nghĩa |
| --- | --- |
| **Baseline** — free, nhiều đối thủ có | phải có, cửa vào cho người dùng free |
| **Core Premium** — trả phí, nhiều đối thủ có | thị trường đặt trong gói trả phí |
| **Premium Differentiator** — trả phí, ít đối thủ có | chỗ tạo khác biệt |
| **Niche Utility** — free, ít đối thủ có | phục vụ nhóm hẹp |

### 5.1 Hai phát hiện phải rút ra

| Loại | Tính năng | Xử lý |
| --- | --- | --- |
| **Lỗ hổng** — Baseline mà mình chưa có | | bổ sung, thiếu thì người dùng vào rồi đi luôn |
| **Tiền bỏ quên** — mình đang free mà thị trường thu tiền | | cân nhắc dời lên gói trả phí |

> Với "tiền bỏ quên", kiểm hai điều trước khi dời: tính năng đó **có phải lý do chính người dùng tải app
> không** — nếu đúng thì đang free có chủ đích, đừng chạm; và **giữ free cho người đang dùng**, chỉ khoá
> với người mới, hoặc để bản giới hạn ở free.

### 5.2 Hạn sử dụng của ma trận

Cái hôm nay là khác biệt, vài tháng sau đối thủ copy là thành hàng phổ thông.

| Ngày khảo sát | Hẹn audit lại |
| --- | --- |

## 6. Ba lớp cạnh tranh

| Lớp | Ai | Mức đe doạ | Ghi chú |
| --- | --- | --- | --- |
| Trực tiếp | | | |
| Gián tiếp | | | |
| Thay thế thủ công | | | |

## 7. Số liệu không công bố

> Doanh thu, DAU, retention của đối thủ **không có nguồn công khai**. Ghi **Không công bố**, không ước đoán.
> Nếu dùng số của công cụ bên thứ ba, ghi rõ tên công cụ và rằng đây là ước lượng.

| Chỉ số | Đối thủ | Trạng thái | Nguồn nếu có |
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
# Nguồn chân lý DUY NHẤT cho G1 phần tài liệu này. KHÔNG chép khối này vào file đầu ra ở docs/.
doc: 02-01_COMPETITOR_LANDSCAPE
gate: G1
required_major:
  - "0. Đọc nhanh"
  - "1. Phạm vi khảo sát"
  - "2. Bản đồ đối thủ"
  - "3. Định vị"
  - "4. Mô hình kiếm tiền"
  - "5. Ma trận vị trí tính năng"
  - "6. Ba lớp cạnh tranh"
  - "7. Số liệu không công bố"
  - "8. Nguồn phương pháp"
  - "Thuật ngữ dùng trong tài liệu này"
required_minor:
  "1. Phạm vi khảo sát": ["1.1", "1.2"]
  "5. Ma trận vị trí tính năng": ["5.1 Hai phát hiện phải rút ra", "5.2 Hạn sử dụng của ma trận"]
quality_checks:
  - "Có ít nhất một đối thủ loại thay thế thủ công"
  - "Không có số liệu nội bộ đối thủ bị ước đoán — phải ghi Không công bố"
  - "Mỗi COM có nguồn kiểm chứng được"
  - "Đủ ba lớp cạnh tranh ở mục 6"
  - "Ma trận mục 5 dựa trên 5-6 app đã tự vào dùng thử, không đọc mô tả store"
  - "Mục 5.1 có kết luận cho cả Lỗ hổng và Tiền bỏ quên, không bỏ trống"
QUALITY-GATE-MANIFEST:END -->
