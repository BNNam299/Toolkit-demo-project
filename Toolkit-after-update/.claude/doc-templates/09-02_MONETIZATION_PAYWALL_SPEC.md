---
doc_id: 09-02
title: Monetization & Paywall Spec
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
depends_on: [05-01, 06-04]
feeds: [09-06, 10-03, 12-01]
id_prefix: [PLN]
gate: G8
in_handover: true
confidence: low
---

# [Tên dự án] — Monetization & Paywall Spec

> **Nguồn chân lý duy nhất về giá.** PRD, copy deck và trang store đều trích `PLN-xxx`, không viết lại số.

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


## 1. Mô hình
| Trường | Nội dung |
| --- | --- |
| Mô hình | Freemium / Trial / Trả một lần / Thuê bao thuần |
| Vì sao chọn | |
| Đối thủ làm gì | _trích `02-01` mục 4_ |

## 2. Cấu trúc tier

> **Điền bảng này TRƯỚC khi thiết kế paywall.** Paywall chỉ là cách trình bày bảng tier cho người dùng.
> Xem `_depth/09-growth/paywall-ads-strategy` — framework F3.

| | Free / Basic | Premium | Pro / cao hơn |
| --- | --- | --- | --- |
| **Purpose** | | | |
| **Tính năng** | | | |
| **Cơ chế thu chính** | | | |
| **Giá** | `PLN-` | `PLN-` | `PLN-` |

| Kiểm | Kết quả |
| --- | --- |
| Mỗi ô Purpose khác nhau rõ rệt — trùng thì gộp tier | |
| Mỗi tier chỉ có **một** cơ chế thu chính | |
| Tier nào có ads, tier nào không ads — ghi rõ | |

## 3. Gói
| `PLN` | Tên gói | Chu kỳ | **Giá** | Trial | Nội dung gồm | Giới hạn |
| --- | --- | --- | --- | --- | --- | --- |
| `PLN-001` | | | | | | |

### 3.1 Duration khớp tần suất nhu cầu

> Trước khi chọn chu kỳ gói, trả lời: **người dùng cần tính năng này bao nhiêu lần trong một chu kỳ gói?**
> Gói năm chỉ hợp lý khi hệ tính năng đủ dày để tạo giá trị lặp lại.

| `PLN` | Chu kỳ | Số lần dùng dự kiến trong chu kỳ | Chu kỳ này hợp lý không |
| --- | --- | --- | --- |

## 4. Giới hạn bản free
| Giới hạn | Ngưỡng | `BR` định nghĩa công thức | Người dùng thấy còn bao nhiêu ở đâu |
| --- | --- | --- | --- |

> Công thức và quy tắc reset do `06-04` sở hữu. Ở đây chỉ trích `BR-xxx`.

## 5. Quảng cáo trong app (IAA)

> Bỏ trống toàn mục nếu sản phẩm **không có** quảng cáo, và ghi rõ **Không áp dụng**.
> Có quảng cáo thì đi hết mục này. Xem framework F2 ở `_depth/09-growth/paywall-ads-strategy`.

### 5.1 Vị trí và loại

| # | Vị trí | `SCR` | Loại | Người dùng nhận được gì | Tần suất tối đa |
| --- | --- | --- | --- | --- | --- |
| 1 | | | Rewarded / Interstitial / Banner / Native | | |

> **Ưu tiên rewarded thay cho popup.** Rewarded làm người dùng chủ động hiểu vì sao phải xem và xem thì
> được gì. Quen "xem ad đổi giá trị" thì dễ chuyển thành người trả tiền hơn.

### 5.2 Quyết định theo 4 quadrant

Với mỗi vị trí ads, xác định trạng thái người dùng tại thời điểm đó:

| Vị trí | Đã khám phá đích đến | Đã nhận ra giá trị | Quadrant | Quyết định |
| --- | --- | --- | --- | --- |
| | Có / Không | Có / Không | Q1 / Q2 / Q3 / Q4 | |

| Quadrant | Quyết định bắt buộc |
| --- | --- |
| Q1 — đã khám phá + đã nhận giá trị | được show, eCPM cao nhất |
| Q2 — đã khám phá, chưa nhận giá trị | phải soi số liệu trước khi bật |
| Q3 — chưa khám phá + chưa nhận giá trị | **không show ở lần chạm đầu** |
| Q4 — đã nhận giá trị, chưa khám phá đích này | tránh show, bảo vệ lần chạm đầu vào tính năng mới |

> Ads rơi vào Q3 vừa làm người dùng rời app vừa kéo eCPM trung bình toàn app xuống.
> Đặt đúng chỗ thì bảo vệ retention **và** tối ưu eCPM — không phải đánh đổi.

### 5.3 Ranh giới giữa IAA và IAP

| Tier | Có ads | Loại ads | Vì sao |
| --- | --- | --- | --- |

## 6. Paywall
| Trường | Nội dung |
| --- | --- |
| `SCR` | |
| Điểm kích hoạt | |
| Giá trị nhấn mạnh | |
| Bằng chứng xã hội nếu có | |
| Downsell khi đóng | |
| Cách huỷ — nói rõ ở đâu | |

## 7. Tám trạng thái giao dịch
> Bắt buộc đủ tám. Điều kiện đóng G8.

| # | Trạng thái | Người dùng thấy gì | `SCR` / `ST` | `EVT` |
| --- | --- | --- | --- | --- |
| 1 | Thành công | | | |
| 2 | Thất bại | | | |
| 3 | Đang chờ | | | |
| 4 | Huỷ giữa chừng | | | |
| 5 | Hoàn tiền | | | |
| 6 | Hết hạn | | | |
| 7 | Gia hạn thất bại | | | |
| 8 | Khôi phục mua hàng | | | |

## 8. Kiểm dark pattern
> Không dùng. Mỗi dòng phải PASS.

| Kiểm | Kết quả |
| --- | --- |
| Giá và chu kỳ hiển thị rõ trước khi bấm mua | |
| Thời điểm hết trial nói rõ | |
| Cách huỷ nói rõ, không giấu | |
| Nút đóng paywall thấy được, không nguỵ trang | |
| Không đếm ngược giả | |
| Không claim sai về tính năng | |
| Nút Continue trong onboarding **không phải** nút mở ads | |
| "Trusted by N users" chỉ dùng khi kiểm chứng được con số | |
| Giới thiệu tính năng khớp trải nghiệm thật, không thêm bước ẩn | |

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
# Nguồn chân lý DUY NHẤT cho G8 phần tài liệu này. KHÔNG chép khối này vào file đầu ra ở docs/.
doc: 09-02_MONETIZATION_PAYWALL_SPEC
gate: G8
required_major:
  - "0. Đọc nhanh"
  - "1. Mô hình"
  - "2. Cấu trúc tier"
  - "3. Gói"
  - "4. Giới hạn bản free"
  - "5. Quảng cáo trong app (IAA)"
  - "6. Paywall"
  - "7. Tám trạng thái giao dịch"
  - "8. Kiểm dark pattern"
  - "9. Nguồn phương pháp"
  - "Thuật ngữ dùng trong tài liệu này"
required_minor:
  "3. Gói": ["3.1 Duration khớp tần suất nhu cầu"]
  "5. Quảng cáo trong app (IAA)": ["5.1 Vị trí và loại", "5.2 Quyết định theo 4 quadrant", "5.3 Ranh giới giữa IAA và IAP"]
quality_checks:
  - "Đủ 8 trạng thái giao dịch — điều kiện G8"
  - "Mục 6 mọi dòng PASS — không dark pattern — điều kiện G8"
  - "Giá viết bằng số CHỈ ở file này, các file khác trích PLN-xxx"
  - "Công thức giới hạn free trích BR-xxx từ 06-04, không viết lại"
  - "Bảng tier điền TRƯỚC khi thiết kế paywall; mỗi tier chỉ một cơ chế thu chính"
  - "Mỗi PLN trả lời được câu chu kỳ có khớp tần suất nhu cầu"
  - "Có ads thì mọi vị trí ads được xếp quadrant; KHÔNG có vị trí nào ở Q3"
  - "Không có ads thì mục 5 ghi rõ Không áp dụng, không bỏ trống"
QUALITY-GATE-MANIFEST:END -->
