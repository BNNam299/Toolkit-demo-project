---
name: mobile-metrics-catalog
description: Danh mục chỉ số mobile app kèm định nghĩa, công thức và cảnh báo dùng sai — DAU, MAU, stickiness, activation, retention theo cohort, trial conversion, churn, LTV, CAC, ARPU, ARPPU. Dùng khi làm phase 10 và cần chọn đúng chỉ số cho North Star, input metric hay guardrail. Đọc mục "Chọn chỉ số theo loại sản phẩm" trước khi chọn North Star.
---

# Danh mục chỉ số mobile app

Skill chiều sâu cho phase 10. Nó **không** thay `10-01_KPI_FRAMEWORK.md` — nó cung cấp từ vựng và
công thức để điền vào đó cho đúng.

## Quy tắc trước khi chọn bất kỳ chỉ số nào

Với mỗi chỉ số, trả lời: *"Nếu chỉ số này tăng gấp đôi mà không có gì khác thay đổi, doanh nghiệp có tốt
hơn không?"* Trả lời **không** thì đó là vanity metric.

Và: mọi chỉ số phải **tính được từ event** đã định nghĩa ở `10-02`. Chỉ số không có event thì không tồn tại.

---

## Nhóm 1 — Chỉ số hoạt động

| Chỉ số | Công thức | Dùng làm gì | Cảnh báo |
| --- | --- | --- | --- |
| **DAU** | số người dùng duy nhất có ≥1 phiên trong ngày | mẫu số, guardrail | **Không nói gì về giá trị.** Tăng vì thông báo spam cũng là tăng |
| **WAU / MAU** | tương tự theo tuần / 28 ngày | mẫu số cho cohort | MAU 28 ngày ổn định hơn "tháng dương lịch" |
| **Stickiness** | DAU ÷ MAU | tần suất dùng thật | <10% nghĩa là app bị mở rồi bỏ |
| **Phiên / người / tuần** | tổng phiên ÷ người hoạt động | cường độ dùng | Nhiều phiên ngắn có thể là dấu hiệu **khó dùng**, không phải yêu thích |
| **Tần suất hành vi cốt lõi** | % người hoàn thành hành vi cốt lõi ≥N lần/tuần | **thường tốt hơn DAU** | Phải định nghĩa rõ hành vi cốt lõi là gì |

> **Với app subscription, đừng chọn DAU làm North Star.** DAU không phân biệt người trả tiền với người
> dùng free, và có thể tăng trong khi doanh thu giảm. Dùng nó làm guardrail thì hợp lý.

## Nhóm 2 — Activation

| Chỉ số | Công thức | Cảnh báo |
| --- | --- | --- |
| **Tỷ lệ activation** | % người mới đạt định nghĩa activation trong N ngày đầu | Định nghĩa bằng **hành vi**, không bằng thời gian |
| **Thời gian tới giá trị** | trung vị thời gian từ mở lần đầu tới aha moment | Dùng trung vị, không dùng trung bình — trung bình bị kéo bởi ngoại lệ |
| **Tỷ lệ hoàn thành onboarding** | % qua hết onboarding | Cao mà activation thấp = onboarding dài nhưng vô ích |

Aha moment lấy từ `04-06_CUSTOMER_JOURNEY.md`, không định nghĩa lại ở phase 10.

## Nhóm 3 — Giữ chân

| Chỉ số | Công thức | Cảnh báo |
| --- | --- | --- |
| **Retention ngày mốc** D1/D7/D30 | % cohort hoạt động **đúng** ngày thứ N | Số nhỏ hơn kiểu khoảng, đừng so lẫn hai kiểu |
| **Retention theo khoảng** | % cohort hoạt động trong khoảng ngày N–M | Số lớn hơn, dễ tự lừa mình |
| **Retention theo cohort tháng** | bảng tam giác theo tháng cài đặt | **Cách duy nhất** thấy sản phẩm đang tốt lên hay xấu đi |
| **Đường cong phẳng chưa** | retention có ổn định ở mức >0 không | Không phẳng = chưa product-market fit, mọi tối ưu khác là vô nghĩa |

> Ghi rõ đang dùng loại nào. Hai kiểu cho ra số khác nhau và bị so sánh nhầm liên tục.

## Nhóm 4 — Kiếm tiền

| Chỉ số | Công thức | Cảnh báo |
| --- | --- | --- |
| **Tỷ lệ xem paywall** | % người hoạt động thấy paywall | Thấp thì paywall bị chôn quá sâu |
| **Trial start rate** | % người xem paywall bắt đầu trial | |
| **Trial → paid** | % trial chuyển thành trả tiền | Đo **sau khi** trial hết hạn, không đo sớm |
| **Churn tháng** | % hết hạn không gia hạn ÷ tổng đang hoạt động | Tách churn tự nguyện và churn do thanh toán lỗi |
| **ARPU** | doanh thu ÷ tổng người hoạt động | |
| **ARPPU** | doanh thu ÷ người **trả tiền** | ARPU thấp mà ARPPU cao = ít người mua chứ không phải giá thấp |
| **LTV** | ARPPU ÷ churn tháng (xấp xỉ) | Là **ước lượng**, gắn `[ASM]` cho tới khi có 6 tháng dữ liệu |
| **Refund rate** | % giao dịch hoàn tiền | **Guardrail bắt buộc.** Tăng conversion mà tăng refund là thất bại |

Giá và gói trích `PLN-xxx` từ `09-02`, không viết số ở phase 10.

## Chọn chỉ số theo loại sản phẩm

| Loại sản phẩm | North Star nên là | DAU dùng làm gì |
| --- | --- | --- |
| Subscription công cụ (ghi chép, theo dõi) | % người dùng hoàn thành hành vi cốt lõi ≥N lần/tuần | guardrail |
| Subscription nội dung | thời lượng tiêu thụ / người trả tiền / tuần | input metric |
| App dùng hằng ngày theo bản chất (habit, sức khoẻ) | streak trung vị hoặc ngày hoạt động / tháng | có thể là input metric |
| Mạng xã hội, tin tức | DAU hoặc thời lượng | **có thể** là North Star |
| Giao dịch một lần | số giao dịch hoàn thành / người | không dùng |

## Bộ tối thiểu cho một MVP subscription

Nếu chỉ chọn được sáu chỉ số: **tỷ lệ activation** · **retention D7 theo cohort** ·
**tần suất hành vi cốt lõi** · **trial → paid** · **churn tháng** · **refund rate** (guardrail).

DAU và MAU giữ lại làm mẫu số, không làm mục tiêu.
