<!-- PROVENANCE — do build script sinh, KHÔNG sửa tay
nguồn      : app-opportunity-scout.skill  →  references/scoring-validation.md
nhập ngày  : 2026-08-09
trạng thái : chép nguyên văn, không tóm tắt, không diễn giải
cập nhật   : xuất lại file .skill từ Claude rồi chạy lại build script
-->

# Scoring & Validation — Chấm điểm, cạnh tranh, fake-door

## Tầng 1 — Need Score (lọc cluster)

Chấm mỗi cluster 1-5 theo 10 câu hỏi; 7 tiêu chí vào công thức:

| Tiêu chí | Câu hỏi |
|---|---|
| Frequency | Vấn đề xảy ra thường xuyên không? |
| Severity | Đủ khó chịu để muốn giải quyết ngay không? |
| Existing behavior | User đã chủ động tìm giải pháp chưa? |
| Workaround cost | Đang mất bao nhiêu thời gian/tiền cho workaround? |
| Search demand | Có người chủ động search không? |
| Market growth | Nhu cầu có xu hướng tăng không? |
| Monetization | User có khả năng trả tiền không? |
| Retention | App có lý do được dùng lại không? |
| Distribution | Quảng cáo được bằng một benefit dễ hiểu không? |
| Team fit | Team build tốt hơn đối thủ được không? |

**Need Score = Frequency + Severity + Search Demand + Existing Workaround + Monetization + Retention + Team Fit** → ưu tiên cluster **≥ 25/35**. (Market growth & Distribution dùng ở tầng 2.)

### Tín hiệu mạnh nhất (nhân đôi sự chú ý khi thấy)
User đang: dùng spreadsheet để quản lý · copy dữ liệu thủ công giữa nhiều app · đặt nhiều reminder bù cho việc quên · trả tiền cho nhiều công cụ để làm một việc · dùng workaround phức tạp · liên tục tìm tutorial · chấp nhận một app tệ vì chưa có lựa chọn · **phàn nàn nhưng vẫn tiếp tục dùng** ("ghét nhưng phải dùng" = tín hiệu cơ hội rất mạnh).

## Tầng 2 — Opportunity Score (xếp hạng concept)

Điểm 1-5 mỗi yếu tố × trọng số:

| Yếu tố | Trọng số |
|---|---|
| Tăng trưởng nhu cầu | 25% |
| Khả năng kiếm tiền | 20% |
| Khoảng trống cạnh tranh | 20% |
| Tần suất sử dụng & retention | 15% |
| Lợi thế phân phối | 10% |
| Lợi thế build của team | 10% |

**Opportunity Score = Demand×0.25 + Monetization×0.20 + Gap×0.20 + Repeat×0.15 + Distribution×0.10 + Build×0.10**

Ví dụ minh họa (số chỉ để minh họa — điểm thật phải từ dữ liệu nghiên cứu, ghi chú rõ khi chưa có):
| Ý tưởng | D | M | Gap | R | Dist | B | Điểm |
|---|---|---|---|---|---|---|---|
| Duplicate Photo Cleaner | 4 | 4 | 2 | 3 | 3 | 5 | 3.45 |
| Email Cleanup by Sender | 4 | 4 | 4 | 4 | 3 | 4 | 3.95 |
| Charging Animation | 2 | 3 | 2 | 2 | 3 | 4 | 2.55 |

## Bộ lọc: Demand thật vs Trend bề mặt

| Demand thật | Trend bề mặt |
|---|---|
| Nhiều keyword liên quan cùng tăng | Chỉ một keyword tăng |
| Nhiều thảo luận độc lập | Tăng do một video viral |
| User đã dùng workaround | Tò mò nhưng không có nhu cầu dùng lại |
| Nhiều app trong cluster cùng tăng | Download cao nhưng review "dùng thử một lần" |
| Hành vi lặp lại + khả năng chi trả | Khó giải thích lý do trả subscription |
| Vấn đề tồn tại cả khi trend biến mất | Sập theo trend |

### Dấu hiệu một dòng app sắp tăng nhu cầu (cần nhiều tín hiệu CÙNG lúc)
Nhiều từ khóa liên quan cùng tăng · nhiều app MỚI bắt đầu tăng download · doanh thu tăng cùng download · user liên tục phản ánh một vấn đề chưa giải tốt · có công nghệ/API/thiết bị/hành vi mới xuất hiện · vấn đề xảy ra thường xuyên (cơ hội retention) · giá trị dễ thể hiện trong ad/screenshot.

Cơ hội tốt nhất = nhu cầu tăng + vấn đề lặp lại + kết quả dễ nhìn thấy + sẵn sàng trả tiền + giải pháp hiện tại còn yếu.

## Concept structure

```
For [user]
who struggles with [problem]
in [context],
the app helps [outcome]
by [unique mechanism].
```

Ví dụ chuẩn:
- **Email Cleaner**: For people with overloaded Gmail inboxes who cannot safely clean thousands of promotional emails, the app groups clutter by category and sender so unwanted emails can be reviewed and removed in bulk.
- **Drawing Story App**: For beginners who want to draw but lack ideas, the app turns short stories into guided, traceable drawing scenes.
- **Focus Coach**: For users who repeatedly bypass app blockers, the app creates short commitment sessions with accountability and visible consequences.

Một cluster → 5-10 concept; tạo tối thiểu 3, KHÔNG chọn concept đầu tiên. Bẫy hot-category: "Tạo một app AI" là chiến lược yếu; "dùng AI giải một vấn đề cụ thể đang tăng, đủ giá trị để trả tiền" mới đúng (AI Cleaner → dọn hàng nghìn email quảng cáo theo sender; AI Drawing → biến truyện ngắn thành bài vẽ trace được; AI Productivity → focus coach cho người hay tắt blocker).

## Kiểm tra cạnh tranh 3 lớp

1. **Có app giải trực tiếp không?** Không có đối thủ = cơ hội mới HOẶC không có nhu cầu thật — không tự động tốt.
2. **Giải pháp thay thế phi-app**: Email Cleaner cạnh tranh với Gmail Search, filter, unsubscribe link, xóa thủ công, và *không làm gì cả*.
3. **Đối thủ bỏ sót segment nào**: quá chuyên nghiệp cho user phổ thông · thiếu một quốc gia · không có bản iOS · quá đắt · thiếu privacy · kết quả khó hiểu · chỉ giải một phần workflow. **Cơ hội nằm ở segment bị bỏ quên, không nhất thiết ở category mới.**

### Checklist phân tích cụm đối thủ (10-20 app mỗi nhóm từ khóa)
Xu hướng download 3/6/12 tháng · xu hướng doanh thu · tần suất update gần đây · giá subscription + trial · **tốc độ tăng review** (không phải tổng review) · thay đổi ranking · thay đổi screenshot/onboarding/paywall · complaint lặp lại trong review tiêu cực (8 nhóm phân loại trong mining-playbook). Thị trường tốt: NHIỀU app cùng tăng trưởng, không phải một app độc chiếm.

## Fake-door validation (trước khi viết PRD)

Cho mỗi concept trong top 3: tên app tạm · value proposition · icon · 3 screenshot mô phỏng (landing kiểu App Store) · landing page · video demo 10-15s · 2-3 ad creative · CTA (Join waitlist / Get early access / Start free).

Chạy ad nhỏ **cùng audience, cùng ngân sách** cho các concept, so:

| Chỉ số | Ý nghĩa |
|---|---|
| CTR | Ý tưởng có thu hút ngay không |
| Landing conversion | User có muốn thử thật không |
| Cost per lead | Nhu cầu có dễ tiếp cận không |
| Comment quality | User có kể thêm vấn đề không |
| Feature clicks | Benefit nào quan trọng nhất |
| Hiểu không cần giải thích? | Định vị đã rõ chưa |

So concept VỚI NHAU, không so benchmark cố định. Marketing ở đây là công cụ research. Sau khi app live: App Store Connect Analytics cho biết user đến từ Search/Browse/app referrer/web referrer/campaign; so impression → product page view → download → conversion theo nguồn và territory.

## Sprint plans

### 14 ngày (đầy đủ)
Ngày 1-2 chọn 5 vùng · 3-5 problem mining (đủ chỉ tiêu tối thiểu) · 6-7 gom ~10 clusters · 8 chấm điểm chọn 3 · 9-10 competitor mapping (10 app/cluster) · 11 tạo 3 concept/cluster (9 concept) · 12 chọn 3 concept khác biệt nhất · 13-14 fake-door test.

### 7 ngày (rút gọn, thiên keyword)
Ngày 1 thu 50 từ khóa vấn đề · 2 nhóm thành 8-10 user jobs · 3 phân tích trend + quốc gia · 4 nghiên cứu 10-20 đối thủ/nhóm · 5 đọc + phân loại ~200 review gần đây · 6 chấm Opportunity Score · 7 landing + ad test cho 3 ý tưởng tốt nhất.

## Output cuối — bảng cơ hội xếp hạng

| Need cluster | User | Vấn đề | Evidence | Demand | Gap | Monetization | Concept |
|---|---|---|---|---|---|---|---|
| Digital clutter | Heavy Gmail users | Inbox quá tải | 38 | Cao | Trung bình | Cao | Clean by sender |
| Focus control | Social media users | Bỏ qua blocker | 29 | Cao | Cao | Cao | Accountability blocker |
| Guided creativity | Drawing beginners | Không biết vẽ gì | 44 | Trung bình | Cao | Trung bình | Story-to-drawing |

Phân loại hành động: (1) nhu cầu cao + còn khoảng trống → **test ngay** · (2) nhu cầu cao + cạnh tranh cao → cần khác biệt mạnh · (3) nhu cầu thấp + kiếm tiền tốt → cơ hội niche · (4) chỉ tăng do trend ngắn → theo dõi thêm · (5) download cao + retention thấp → **tránh**.
