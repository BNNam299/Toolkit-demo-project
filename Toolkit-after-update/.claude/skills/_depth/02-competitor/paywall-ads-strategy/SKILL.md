---
name: paywall-ads-strategy
description: Chiến lược kiếm tiền kết hợp quảng cáo (IAA) và mua trong app (IAP) theo bộ nguyên tắc và 4 framework của team — Feature Prioritization Matrix (quyết định tính năng nào vào tier nào dựa trên đối thủ), Elimination Framework (quyết định show ads ở thời điểm nào theo 4 quadrant), cấu trúc tier thương mại 3 tầng, và bảng anti-pattern FTUE theo hành trình. Dùng khi làm phase 09 nếu sản phẩm có quảng cáo hoặc nhiều tier; cũng dùng ở phase 02 cho F1, và phase 05 khi quyết định tính năng nào miễn phí tính năng nào trả tiền.
---

# Chiến lược Feature – Paywall – Ads

Skill chiều sâu do team cung cấp. Toàn bộ nội dung ở `references/method.md`, chép nguyên văn.
Hai sơ đồ F1 và F2 nằm cùng thư mục dưới dạng `.png`.

## Dùng khi nào

| Phase | Dùng phần nào |
| --- | --- |
| 02 competitor | **F1** — khảo sát 5–6 đối thủ, ghi tính năng nào free tính năng nào trả phí, xếp vào ma trận |
| 05 prd | **F1** — quyết định tính năng nào vào tier nào; tìm "lỗ hổng" và "tiền bỏ quên" |
| 09 growth | **F2, F3, F4** và 10 nguyên tắc — vị trí ads, cấu trúc tier, thời điểm paywall |

## Ba điều quan trọng nhất trong tài liệu này

**Điền bảng tier TRƯỚC khi thiết kế paywall.** Paywall chỉ là cách trình bày bảng tier cho người dùng.
Thiết kế paywall trước rồi mới nghĩ tier là làm ngược, và sẽ ra một paywall không bán được gì rõ ràng.

**Đặt ads đúng chỗ không phải đánh đổi giữa retention và doanh thu.** Ads rơi vào vùng người dùng chưa
hiểu giá trị vừa làm họ rời app vừa kéo eCPM trung bình xuống. Đúng chỗ thì được cả hai.

**Duration của gói phải khớp tần suất nhu cầu.** Trước khi chọn gói tháng hay gói năm, hỏi: người dùng
cần tính năng này bao nhiêu lần trong chu kỳ gói? Bán gói năm cho app dùng vài lần một tháng là không hợp lý.

## Ranh giới khi áp dụng vào tài liệu

Quyết định rút ra từ skill này **phải ghi vào tài liệu**, không để trong hội thoại:

- Tính năng nào vào tier nào → `05-01_PRD.md` mục 10, và bảng tier ở `09-02`
- Vị trí và loại ads → `09-02_MONETIZATION_PAYWALL_SPEC.md`
- Thời điểm paywall trên hành trình → `09-01_ONBOARDING_SPEC.md`
- Anti-pattern đã tránh → ghi vào mục kiểm dark pattern của `09-02`

## Một lưu ý về số liệu

Tài liệu có nêu con số tham chiếu *">50% user abandon tại paywall trước khi kịp thấy value"*, ghi nguồn là
"case thực tế". Theo quy tắc nhãn của Pipeline v2, đây là **số liệu nội bộ của team**, không phải dữ kiện
công bố. Khi trích vào tài liệu dự án, ghi `[FACT]` kèm nguồn là tài liệu này, hoặc `[ASM]` nếu không
truy được về một case cụ thể. Không trình bày như số liệu ngành.
