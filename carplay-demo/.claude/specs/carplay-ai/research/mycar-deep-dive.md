# Deep Dive Đối thủ #1 — `myCar: Car Widgets & Dashboard`

**Ngày thu thập**: 2026-08-06
**Đối tượng**: Đối thủ trực tiếp duy nhất trong niche đang kiếm được tiền thật
**Nguồn**: Apple iTunes Lookup API (47 storefront), Apple Customer Reviews RSS (US/CA/MX/GB/DE), AppStoreSpy/SensorTower, trang App Store công khai
**Liên quan**: [appstorespy-competitor-data.md](./appstorespy-competitor-data.md)

---

> ## ⚠️ ĐÍNH CHÍNH — đọc trước khi dùng file này
>
> File này là bản ghi nghiên cứu **ngày 2026-08-06**, dựa trên estimate của AppStoreSpy/SensorTower và dữ liệu tái dựng từ review. Ngày **2026-08-07** PO cung cấp **dữ liệu vận hành thật**, phủ định một số kết luận ở đây:
>
> | Nội dung trong file này | Số/kết luận THẬT |
> |---|---|
> | myCar doanh thu **$900K/tháng** | **~$700K/tháng** (DAU 103K, RPD $1,46) |
> | myCar giá **weekly $7,99 · yearly $34,99** | **weekly $4,44/$5,99 · yearly $19,99/$24,99/$29,99 · Coin $0,99/$4,99** — giá tái dựng từ review là **SAI** |
> | *"Doanh thu chủ yếu từ renewal cohort cũ; sẽ sụp Q1-Q2 2027"* | **SAI.** D30 chỉ **4,0%** → không có base để renewal. Mô hình thật là **churn-and-refill bằng paid UA**: ~479K install mới/tháng |
> | Không có dữ liệu retention | **D1 28,8% · D7 11,5% · D30 4,0%** |
>
> **Nguồn đã sửa và đầy đủ**: [feature-tiers-and-competitor-matrix.md §4.3–4.5](./feature-tiers-and-competitor-matrix.md) và PRD.md v2.2 §4.
>
> Các phần **không bị ảnh hưởng** và vẫn dùng được: số lượng app trong từng cluster, tỷ lệ takedown, phân tích review/complaint, top countries, metadata app.

---

## 1. Metadata Chính xác (từ iTunes Lookup API — dữ liệu chính thức của Apple)

| Thuộc tính | Giá trị |
|---|---|
| Tên app | myCar: Car Widgets & Dashboard |
| Subtitle | Driving Widgets · Startup Sounds |
| **Seller pháp lý** | **KarmaTECH OU** (Estonia — công ty OÜ) |
| Tên hiển thị developer | DOFUapps |
| Copyright | © 2026 myCar Connect |
| Bundle price | Free (0.0 USD) |
| Có IAP | Có |
| Primary genre | **Utilities** |
| Genres | Utilities, **Travel** |
| Average rating (US) | **4.5822** |
| Rating count (US) | **10,785** |
| Version | 1.10.1 |
| Ngày phát hành | **2025-11-20** |
| Cập nhật version hiện tại | 2026-08-04 |
| **Minimum iOS** | **15.1** |
| File size | 77,306,880 bytes (**73.7 MB**) |
| Content rating | 4+ |
| Ngôn ngữ (9) | EN, FR, DE, ID, IT, MS, PT, ES, TR |
| Chart position | **#33 Utilities (US, Top Free)** |
| Nền tảng | **Chỉ iPhone** (không iPad, không verified cho macOS) |

**Ghi chú**: `myCar Connect` trong dòng copyright cho thấy họ vẫn giữ chữ "Connect" ở tầng pháp lý nhưng **cố tình loại khỏi tên app** trên store. Đây là bằng chứng thêm rằng "Connect" là từ khóa độc hại về mặt ASO/compliance.

**Cross-check với AppStoreSpy (estimate)**: 500K monthly installs, $900K monthly revenue, peak ~801K installs / ~$1M revenue vào Apr 2026.

---

## 2. Cấu trúc Paywall & Giá Subscription

**Phương pháp**: Không lấy được trực tiếp (AppStoreSpy "Paywalls: No data"; trang web App Store chỉ ghi "In-App Purchases: Yes"). Giá được **tái dựng từ 96 review của người dùng** ở 5 storefront — nhiều review nêu con số cụ thể và nhất quán với nhau.

### 2.1 Bậc giá (tái dựng từ review)

| Gói | Giá | Bằng chứng trực tiếp từ review |
|---|---|---|
| **Weekly** | **$7.99/tuần** | "waste 7.99 a week or 30 ish a year"; "aggressive subscription 7.99 per week"; "$7 A WEEK ($364 a year)" |
| **Yearly (hiện tại)** | **$34.99/năm** | "I paid for the $34.99 yearly subscription"; "not worth the $35.00 payment"; "yearly fee of 35$" |
| **Yearly (giá cũ)** | **$24.99/năm** | "Was supposed to be $24.99/year"; "Bought the annual for 24.99" |
| **Yearly (giá promo)** | **$19.99/năm** | "runs a 90% discount promo on its yearly service of $24.99. When you click to purchase it comes up as $19.99" |
| Cách đóng khung giá năm | "$0.48/tuần" | "0.48 cents a week annually which is the price they use to hide that it's $24 dollars" |

**Diễn giải**: Giá năm đã **tăng từ $24.99 → $34.99** trong khoảng 8 tháng. Giá tuần $7.99 là mức neo (anchor) cực cao — $7.99/tuần = **$415/năm**, làm cho gói năm $34.99 trông như giảm 92%. Đây là chiến thuật anchor pricing kinh điển.

### 2.2 Cấu trúc Paywall — HARD PAYWALL, KHÔNG có free trial

Đây là đặc điểm quan trọng nhất và là **nguồn gốc của mọi vấn đề** của myCar:

| Đặc điểm | Bằng chứng |
|---|---|
| Paywall xuất hiện **ngay khi mở app lần đầu** | "As soon as you open the app you have to choose a subscription. Weekly or Yearly — I don't even know what it looks like or what it does" |
| **Không có free trial** | "You're required to pay to even try to start the app, no trials"; "At least allow a demo drive for x amount of days or something; not even an option" |
| **Không có bất kỳ feature miễn phí nào** | "Yes it's free to download the app, but you can't use a single feature unless you pay"; "I genuinely could not find a single feature that would allow me to use it without being prompted to pay" |
| Paywall lặp lại giữa flow | "It lets you go through all the steps to pick and customize things right to the end of every feature, then asks you for money" |
| Paywall xuất hiện **sau khi đã trả tiền** (bug) | "every time I try to add one, it just sends me back to the same paywall, so the feature I paid for doesn't work"; "it keeps cycling back to the screen where you have to subscribe" |
| Không refund | "Apple is saying this app is not refundable"; 9/96 review nhắc `refund` |
| Có báo cáo **thu tiền sai** | "Bought the annual for 24.99 but charged 44.98"; "supposed to be $24.99/year and was charged $49.00" |

**Kết luận**: myCar chọn hard paywall để tối đa hóa doanh thu ngắn hạn từ traffic ads. Nó hiệu quả về mặt cash-flow ($900K/tháng) nhưng đang **phá hủy tài sản thương hiệu** — xem mục 4.

---

## 3. Top Countries (proxy qua rating votes, 47 storefront)

**Phương pháp**: Gọi iTunes Lookup API cho từng storefront, lấy `userRatingCount`. Đây là **proxy** cho phân bổ user base, không phải số installs thật. App có mặt ở **47/47 storefront kiểm tra** (phát hành toàn cầu).

Tổng rating votes trên 47 storefront: **20,075**

| Rank | Quốc gia | Rating Votes | Share | Avg Rating |
|---|---|---|---|---|
| 1 | **US** | **10,785** | **53.7%** | 4.58 |
| 2 | **MX** | **1,447** | **7.2%** | 4.67 |
| 3 | **CA** | 898 | 4.5% | 4.40 |
| 4 | **BR** | 550 | 2.7% | 4.55 |
| 5 | DE | 455 | 2.3% | 4.20 |
| 6 | GB | 436 | 2.2% | 4.25 |
| 7 | FR | 412 | 2.1% | 4.37 |
| 8 | **CO** | 404 | 2.0% | 4.74 |
| 9 | AU | 391 | 1.9% | 4.36 |
| 10 | TR | 367 | 1.8% | 4.16 |
| 11 | **CL** | 361 | 1.8% | 4.64 |
| 12 | IT | 299 | 1.5% | 4.49 |
| 13 | ES | 262 | 1.3% | 4.31 |
| 14 | JP | 250 | 1.2% | 4.21 |
| 15 | PH | 232 | 1.2% | 4.68 |
| 16 | ZA | 219 | 1.1% | 4.60 |
| 17 | AR | 186 | 0.9% | 4.52 |
| 18 | NL | 182 | 0.9% | 4.40 |
| 19 | MY | 162 | 0.8% | 4.70 |
| 20 | BE | 161 | 0.8% | 4.30 |
| 21 | RO | 148 | 0.7% | 4.49 |
| 22 | CH | 129 | 0.6% | 4.21 |
| 23 | PL | 127 | 0.6% | 4.10 |
| 24 | EG | 114 | 0.6% | 4.55 |
| 25 | SA | 108 | 0.5% | 4.21 |
| 26 | AT | 105 | 0.5% | 4.35 |
| 27 | ID | 87 | 0.4% | 4.54 |
| 28 | GR | 83 | 0.4% | 4.35 |
| 29 | IL | 74 | 0.4% | 4.32 |
| 30 | PT | 70 | 0.3% | 4.44 |
| 31 | **VN** | **65** | **0.3%** | **4.68** |
| 32 | CZ | 63 | 0.3% | 4.30 |
| 33 | DK | 55 | 0.3% | 4.07 |
| 34 | KR | 51 | 0.3% | 4.51 |
| 35 | NZ | 51 | 0.3% | 4.18 |
| 36 | AE | 48 | 0.2% | 4.10 |
| 37 | NO | 45 | 0.2% | 4.27 |
| 38 | TH | 41 | 0.2% | 4.41 |
| 39 | IE | 39 | 0.2% | 4.03 |
| 40 | TW | 29 | 0.1% | 4.76 |
| 41 | SE | 26 | 0.1% | 3.81 |
| 42 | FI | 14 | 0.1% | 4.43 |
| 43 | HK | 14 | 0.1% | 4.29 |
| 44 | SG | 11 | 0.1% | 4.00 |
| 45 | RU | 10 | 0.0% | 4.30 |
| 46 | IN | 9 | 0.0% | 4.00 |
| 47 | NG | 0 | 0.0% | — |

### 3.1 Ba nhận xét chiến lược từ phân bổ địa lý

**A. US chiếm hơn nửa (53.7%)** — Thị trường US quyết định thành bại. Doanh thu $900K/tháng gần như chắc chắn tập trung ở US (giá $34.99/năm + purchasing power).

**B. LATAM là cluster số 2 bất ngờ (14.6%)** — MX 7.2% + BR 2.7% + CO 2.0% + CL 1.8% + AR 0.9% = **14.6%**, vượt cả Tây Âu (DE+GB+FR+IT+ES = 9.4%).
Đáng chú ý: rating ở LATAM **cao hơn US** (MX 4.67, CO 4.74, CL 4.64 vs US 4.58) → user LATAM hài lòng hơn, có thể vì mức giá địa phương thấp hơn hoặc kỳ vọng khác.
→ Hàm ý cho Carbina: **ưu tiên localize tiếng Tây Ban Nha và Bồ Đào Nha (Brazil)** ngay từ MVP. myCar đã có ES và PT trong 9 ngôn ngữ.

**C. Rating thấp nhất ở Bắc Âu + thị trường trưởng thành** — SE 3.81 (thấp nhất), IE 4.03, DK 4.07, PL 4.10, AE 4.10. Đây là các thị trường ít khoan dung với hard paywall.

**D. Việt Nam**: 65 votes, rating **4.68** (cao) nhưng volume rất nhỏ (0.3%). Không phải thị trường ưu tiên cho monetization nhưng là nơi tốt để soft-launch/test.

---

## 4. Phân tích Review — 96 review gần nhất (US, CA, MX, GB, DE)

### 4.1 PHÁT HIỆN QUAN TRỌNG NHẤT: Sentiment đã sụp đổ

| | Rating tổng thể (tích lũy) | Rating trong 96 review GẦN NHẤT |
|---|---|---|
| 5★ | — | **8 (8.3%)** |
| 4★ | — | **0 (0%)** |
| 3★ | — | 6 (6.3%) |
| 2★ | — | 7 (7.3%) |
| 1★ | — | **75 (78.1%)** |
| **Trung bình** | **4.58★** (10,785 votes) | **≈1.5★** |

**Đây là tín hiệu mạnh nhất trong toàn bộ nghiên cứu này.**

Rating tổng thể 4.58★ **không phản ánh thực tế hiện tại**. 78% review gần nhất là 1★. Khoảng cách này chỉ có thể giải thích bằng: rating cao được tích lũy sớm (qua in-app rating prompt đặt trước paywall, hoặc trước khi user phát hiện paywall), sau đó sentimen thật xuất hiện trong review viết tay.

**Đối chiếu với dữ liệu installs**: installs giảm 37% từ đỉnh (801K→500K) đúng lúc sentiment sụp. Word-of-mouth âm đang bắt đầu ăn vào top-of-funnel.

→ **Hàm ý cho Carbina**: Đừng benchmark theo 4.58★ của myCar. Rating thật của họ đang là ~1.5★. Đây là cửa sổ cơ hội: một app cùng niche với UX trung thực có thể chiếm thị phần nhanh khi myCar tiếp tục rơi.

### 4.2 Top 6 Complaint (xếp theo tần suất)

| # | Complaint | Tần suất | Trích dẫn tiêu biểu |
|---|---|---|---|
| **1** | **Hard paywall, không có trial, không feature miễn phí** | **~60/96 review** (`subscription` 24, `paid` 9, `subscribe` 3) | "There's a reason you're required to pay for a subscription before you can even get past the opening screen. The reason is, it's not worth it." |
| **2** | **Widget không hoạt động trên CarPlay** | 28 lần nhắc `widget` | "Widget don't know matter what I do"; "I cannot get the widgets option up in my CarPlay settings after I just spent 24 dollars on the app for the widgets specifically" |
| **3** | **Quảng cáo sai sự thật (false advertising) — "Jarvis"** | ≥6 review nêu rõ | "Please don't fall for the fake advertisements on Insta, Facebook, or TikTok. The app does not start everything up like Jarvis."; "I was grabbed in by the Jarvis welcome Miss and that's not in the library." |
| **4** | **Không refund được** | 9 lần nhắc `refund` | "Apple is saying this app is not refundable? Why? even if doesn't work?" |
| **5** | **Thu tiền sai / giá không khớp** | 4 lần nhắc `charge` | "Bought the annual for 24.99 but charged 44.98"; "supposed to be $24.99/year and was charged $49.00"; "runs a 90% discount promo on its yearly service of $24.99. When you click to purchase it comes up as $19.99 which is not 90% discount... bait and switch" |
| **6** | **Không có support — email bị bounce** | ≥4 review | "I emailed a review and it was sent back as a mailer demon"; "I emailed the developer and he never answered"; "no support whatsoever" |

### 4.3 Complaint Kỹ thuật Cụ thể (nguồn trực tiếp cho Functional Requirements của Carbina)

| Vấn đề kỹ thuật | Trích dẫn | Xe/thiết bị được nêu |
|---|---|---|
| **Widget không fit màn hình xe** | "I have a 2022 Jeep Wrangler with the 8 inch screen and the widget does not fit. The wording is cut off on both the right and left side." | Jeep Wrangler 2022, màn 8" |
| **Không hoạt động trên xe mới** | "Does not work on new cars! I can't get this to work on my 2026 no matter what I do" | xe 2026, Ram Rebel 2026, Audi |
| **Âm thanh quá nhỏ, bị nhạc lấn** | "If you have a half decent sound system or subwoofers this thing sucks. Super quiet and gets cancelled out almost completely if you have any music playing." | — |
| **Sound disconnect không sync đúng lúc tắt máy** | "More times than not, the disconnect sound does not sync correctly to the vehicle shutting off so you only hear the sound through your phone." | — |
| **Chỉ widget cờ (flag) hiện được** | "Only the flag widgets show.. can get the sounds to work, but the flashy car widgets don't show" | — |
| **Custom photo widget không hiện** | "the custom photo widget or couples widget does not show up on the CarPlay in the vehicle even when set up correctly following the in app tutorial several times" | — |
| **Widget đếm ngày bị đóng băng** | "The together with Babe widget does not update the amount of days. It stays the same for weeks on the end." | — |
| **Yêu cầu tải app thứ 2** | "The only thing that really is cool is the audio message you can customize on the start up with CarPlay. You do need to download a separate app for that however." | — |
| **Chất lượng hình ảnh mờ** | "Looks fairly blurry" | — |
| **Không nhận subscription đã mua** | "it kept failing to recognize my subscription" | — |
| **Cần wireless CarPlay** | "My car doesn't support wireless CarPlay" (3★) | — |
| **Thư viện xe thiếu** | "they only have the Subaru wrx no Subaru STI"; "The Gr Corolla is missing"; "would like to see the mk3 supra"; "should be able to select year, trim, and color" | Subaru STI, GR Corolla, MK3 Supra |

### 4.4 Điều người dùng THỰC SỰ THÍCH (từ 5★ và các câu tích cực trong review âm)

Đây là phần quan trọng — nó cho biết **feature nào có product-market fit thật**:

| Feature được khen | Bằng chứng |
|---|---|
| **Âm thanh khi connect / disconnect / arrive home** | "The connection, disconnection, and arrival sounds work and are great!" (5★); "The startup sound works" (ngay trong review 1★) |
| **Làm màn hình CarPlay cá nhân hóa và vui** | "It makes my CarPlay screen look more personal and fun. The widgets are easy to set up, and everything works smoothly." (5★) |
| **Dễ setup (khi chạy được)** | "Very easy to set up." (5★) |
| **Thư viện hình ảnh xe** | "The only thing it looks like they spent time on was getting pictures of all the different cars" (1★ nhưng vẫn thừa nhận); "The car selection is good" (5★) |
| **Cảm giác "must have" cho xe mới** | "Must have for newer vehicles..!" (5★, Canada) |

**Kết luận PMF**: Feature có PMF thật là **âm thanh khởi động/tắt máy** — nó hoạt động và người dùng thích. Widget là feature bị lỗi nhiều nhất nhưng lại là thứ được quảng cáo mạnh nhất. Đây là mismatch chết người.

### 4.5 Feature Request rõ ràng từ user

1. **Cho dùng thử miễn phí** — request số 1, xuất hiện trong ~60 review
2. **Bán một lần thay vì subscription** — "I would be willing to buy this app outright, but I'm not going to pay for the rest of my life to use it"; "This should maybe cost you $5 one time to purchase"
3. **Chọn được năm / phiên bản trim / màu xe** — "should be able to select year, trim, and color"
4. **Thêm nhiều mẫu xe** — Subaru STI, GR Corolla, MK3 Supra, Ford F150 icon đẹp hơn
5. **Widget tương tác thật** — "Amazon doesn't seem to do anything with its selections. Click on orders and nothing happens. Would like to be able to do more with screen"
6. **Điều chỉnh âm lượng sound / ducking nhạc** — từ complaint âm thanh bị lấn
7. **Widget tự adapt kích thước màn hình xe** — từ complaint Jeep 8"

---

## 5. Retention D1 / D7 / D30 — KHÔNG CÓ DỮ LIỆU

**Kết luận thẳng: không lấy được, và không có nguồn công khai nào cung cấp con số này.**

| Nguồn đã thử / xem xét | Kết quả |
|---|---|
| AppStoreSpy (gói hiện tại) | Không có metric retention. Chỉ có installs, revenue, rankings, changelog, SDK, ad creatives |
| Apple iTunes Lookup API | Không có retention (chỉ metadata + rating) |
| Apple Customer Reviews RSS | Không có retention |
| Trang App Store công khai | Không có retention |

**Lý do cấu trúc**: Retention (D1/D7/D30) là dữ liệu **first-party**, chỉ có trong App Store Connect của chính chủ app hoặc SDK analytics của họ. Các nền tảng như Sensor Tower / data.ai chỉ bán **estimate** retention trong gói enterprise (giá $10K+/năm), và ngay cả khi có thì độ chính xác cho một app đơn lẻ cũng thấp.

**Không nên bịa số.** Thay vào đó, dùng 2 proxy dưới đây.

### 5.1 Proxy 1 — Suy luận retention từ đường cong installs vs revenue

| Mốc | Monthly Installs | Monthly Revenue | Revenue/Install |
|---|---|---|---|
| Mar 2026 | ~300K | ~$250K | ~$0.83 |
| Apr 2026 (đỉnh) | ~801K | ~$1.0M | ~$1.25 |
| Jul 2026 | ~500K | ~$900K | ~$1.80 |

Revenue/install **tăng liên tục** (0.83 → 1.25 → 1.80) trong khi installs giảm. Hai cách đọc:
1. Conversion rate paywall tăng (do tối ưu paywall + tăng giá $24.99→$34.99), **hoặc**
2. Doanh thu hiện tại phần lớn đến từ **renewal của cohort cũ**, không phải từ user mới

Với hard paywall + 78% review 1★, cách đọc số 2 hợp lý hơn. Nghĩa là: **retention thực tế của user mới rất thấp**, và $900K/tháng chủ yếu là annual subscription từ cohort Mar-Apr 2026 chưa đến kỳ hủy.

**Cảnh báo suy ra được**: Cohort Mar-Apr 2026 sẽ đến kỳ gia hạn vào **Mar-Apr 2027**. Với 78% sentiment 1★ và nhiều người đã nói "cancelled my subscription the next day", tỷ lệ renewal sẽ rất thấp → doanh thu myCar có khả năng **sụp mạnh vào Q1-Q2 2027**.

### 5.2 Proxy 2 — Bằng chứng churn trực tiếp trong review

Các câu cho thấy user hủy gần như ngay lập tức:

| Trích dẫn | Thời gian đến lúc churn |
|---|---|
| "I canceled my subscription immediately" | ngay lập tức |
| "Deleted the app not even an hour after my first downloading it" | < 1 giờ |
| "I deleted it immediately, so I cannot tell you about how the app works" | < 1 giờ |
| "je l'ai installé pendant 5 minutes" (tôi cài 5 phút) | 5 phút |
| "Tried out for one day. ... I then requested a refund" | 1 ngày |
| "Cancelled my subscription the next day" | 1 ngày |
| "Tried it and deleted" (nhiều biến thể) | trong ngày |

→ **D1 retention của myCar gần như chắc chắn ở mức thảm họa.** Không định lượng được nhưng định tính rất rõ.

### 5.3 Đề xuất: dùng benchmark ngành thay cho số của myCar

Vì không có số thật của myCar, PRD của Carbina nên đặt mục tiêu retention theo **benchmark ngành cho app Utilities freemium** và ghi rõ đây là benchmark, không phải số đối thủ. Cần tìm nguồn benchmark riêng (chưa thực hiện trong lần nghiên cứu này) — xem mục 8.

---

## 6. Marketing & Kênh Acquisition của myCar

**Kênh chính (từ review)**: Facebook, Instagram, TikTok ads.

| Bằng chứng | Trích dẫn |
|---|---|
| Facebook ads | "On their Facebook ad, they show the scenario that was appealing and made the assumption that it was part of their app" |
| Instagram ads | "saw this on Instagram and gave it a shot" |
| TikTok | "Say on TikTok one for Jarvis so I got the app and it wasn't on their" |
| Cả 3 kênh | "don't fall for the fake advertisements on Insta, Facebook, or TikTok" |

**Creative hook chính**: Cảnh xe khởi động với giọng AI kiểu **"Jarvis"** (Iron Man) chào người lái. Đây là hook cực mạnh — nhiều user nói rõ họ tải app **chỉ vì** cảnh này.

**Vấn đề**: Feature "Jarvis" **không tồn tại trong app**. Đây là nguồn gốc của complaint "false advertising" và là lý do trực tiếp cho làn sóng 1★.

### 6.1 Đây chính là cơ hội lớn nhất cho Carbina

myCar đã **validate demand** cho một thứ họ không làm được:
- Người dùng **muốn** giọng AI chào khi vào xe
- Họ **sẵn sàng trả tiền** cho nó (đã trả $34.99 vì cái ad đó)
- myCar **không giao được** → 1★

Carbina với on-device AI có thể **giao thật thứ myCar chỉ hứa**: giọng chào cá nhân hóa theo ngữ cảnh (thời gian, thời tiết, lịch, điểm đến dự đoán). Đó không phải là feature phụ — đó là **hook marketing đã được thị trường chứng minh, đang bị bỏ trống**.

**Nhưng cảnh báo compliance**: Không được đặt tên feature là "Jarvis" (trademark Marvel/Disney). Và không được quảng cáo bất cứ thứ gì app không làm được — đó chính là cái bẫy myCar đang mắc.

### 6.2 App khác của cùng developer (DOFUapps / KarmaTECH OU)

| App | Subtitle |
|---|---|
| proRadar・Radar & Speed Cameras | Live Traffic & Police Alerts |
| Reverse Audio Singing・Happy AI | Record Viral Song Challenges |

→ Pattern rõ: **studio chuyên app viral-hook + hard paywall**, không phải công ty sản phẩm dài hạn. Họ không có động lực sửa chất lượng.

---

## 7. Cluster Đối thủ Thật — "Car Play" (có dấu cách)

**Phát hiện**: Query ban đầu dùng `name contains "carplay"` (liền) đã **bỏ sót phần lớn niche**. Các app dùng tên `Car Play`, `Car.Play`, `Car Auto Play` (có dấu cách/dấu chấm) để né ASO filter và có thể để né trademark.

### 7.1 Số liệu tổng hợp — iOS, `name contains "car play"`

| Chỉ số | Giá trị |
|---|---|
| Published | **48** |
| Total | 100 |
| Removed | **52 (52%)** |
| **Monthly Installs** | **512K** |
| **Monthly Revenue** | **$660K** |

**Điều này sửa lại kết luận trước đó.** Niche "CarPlay Connect" **không hoàn toàn chết** — nó tạo ra **$660K/tháng** trên 48 app iOS. Con số $0 ở lần query đầu là do filter `carplay` (liền) chỉ bắt được 7 app rìa.

Tuy nhiên: **52% removal rate** vẫn là bằng chứng rủi ro takedown rất cao, không thay đổi.

### 7.2 Danh sách app trong cluster (từ "You Might Also Like" của myCar)

Đây là các app Apple coi là **cùng nhóm cạnh tranh trực tiếp** với myCar:

| App Name | Subtitle |
|---|---|
| **Car.Play Connect: Auto Sync** | Smart Dash & GPS Speedometer |
| **Car Play Connect - Auto Sync** | Smart link for digital cast |
| **Car Auto Play: Sync & Connect** | Smart Link GPS Dash Navigation |
| **Car Play Connect: Remote Start** | Car Sync & Connect, Auto Link |
| **Car Play Connect, Sync & Care** | My Remote Pass & Mobile Link 3 |
| **Car Play Connect: Remote Sync** | Digital Mobile Driving |
| **KeyConnect Digital Car Key** | Remote Connect & Car Link |

⚠️ Lưu ý: **`Car Play Connect - Auto Sync`** là tên gần như y hệt tên gốc dự định của chúng ta (`CarPlay Connect - Auto Sync`). Quyết định đổi sang **Carbina** là đúng.

Pattern subtitle của cả cluster: `Sync`, `Connect`, `Link`, `Remote`, `Dash`, `GPS`, `Speedometer`. Đây là **vùng từ khóa nên tránh** để không bị Apple xếp cùng nhóm rủi ro.

### 7.3 Bảng chi tiết 30 app đầu trong cluster "car play" (iOS, sort theo Monthly Revenue)

| # | App Name | Developer | Rating | Votes | Release | Last Updated | Monthly Installs | Monthly Revenue |
|---|---|---|---|---|---|---|---|---|
| 1 | Car Auto Play: Sync & Connect | Appstract Works | 4.6 | 3K | 28 Sept 2025 | 1 Aug 2026 | 60K | **$200K** |
| 2 | **Car Play Connect - Auto Sync** | **App Ventures** | **4.6** | **6K** | 10 May 2025 | 2 Jul 2026 | **200K** | **$200K** |
| 3 | Car Play Connect: Remote Start | TV Cast Pte. Ltd. | 4.7 | **25K** | 25 Jul 2023 | 28 Jul 2026 | 40K | **$100K** |
| 4 | Car Play Connect, Sync & Care | Bloomup LTD | 4.7 | **48K** | 20 Jan 2023 | 22 May 2026 | 100K | **$100K** |
| 5 | Car Play Connect: Auto Sync | VALERY STAKARSKI | 4.6 | 2K | 25 Aug 2025 | 8 Jul 2026 | 80K | **$60K** |
| 6 | Sync: Ford Car Play Connect | Huy Nguyen | 4.6 | 3K | 25 Apr 2023 | 30 Oct 2024 | 20K | — |
| 7 | Car Play Connect: Remote Sync | Monstermob Usa, INC. | 4.4 | **19K** | 13 May 2022 | 22 Jul 2026 | — | — |
| 8 | Car Sync Play: Car Key Play | TECHISTIC LTD | 4.5 | 3K | 5 Jun 2023 | 30 Apr 2024 | — | — |
| 9 | Car Play Connect: Digital Key | TRIPLE IT LTD | 4.2 | 2K | 23 Jan 2023 | 3 Apr 2023 | — | — |
| 10 | CarLink: Car Sync Play Widgets | COOLDEV CO., LTD | 4.5 | 955 | 18 Jul 2024 | 29 Jun 2026 | — | — |
| 11 | **Car Play Connect: Car Sync AI** | AUTHENTICATOR APP 2FA AUTH LTD | **4.9** | 781 | 29 Apr 2025 | 27 Jun 2025 | — | — |
| 12 | Car Play Connect: Car Sync Key | CAR CONNECT PLAY DIGITAL CAR KEY. | 4.8 | 668 | 5 Feb 2024 | 4 Mar 2025 | — | — |
| 13 | Car Play Connect. Digital key. | Alexey Timokhin | 4.3 | 465 | 9 May 2023 | 30 Dec 2024 | — | — |
| 14 | Car Play Connect Sync | Emrullah Bas | 4.5 | 392 | 20 Sept 2025 | 15 Dec 2025 | — | — |
| 15 | Cartube Plus - Sync Car & Play | Chanh Tran | 4.3 | 300 | 2 Dec 2024 | 4 Dec 2024 | — | — |
| 16 | Zlink5 Car-Play Sync & Connect | Tu Ti Co | 2.8 | 88 | 30 Nov 2025 | 8 Dec 2025 | — | — |
| 17 | Car Play Connect Auto Sync | Veysel AKBALIK | 4.3 | 34 | 12 Jan 2026 | 21 May 2026 | — | — |
| 18 | Car Remote Connect & Sync Play | Service Prime SRL | 4.5 | 23 | 22 Sept 2025 | 31 Jan 2026 | — | — |
| 19 | Car Play Sync: AI Connect App | PDF Scanner Editor PDF Converter Expert | 5.0 | 14 | 23 Jul 2025 | 25 Jul 2025 | — | — |
| 20 | Car Sync & Play Dashboard | AHMET KEREM YUCALAN | 4.4 | 10 | 18 Jun 2025 | 16 Jul 2026 | — | — |
| 21 | Car Play Connect & Sync | Nazar Stasyk | 4.2 | 10 | 22 May 2026 | 9 Jun 2026 | — | — |
| 22 | Car Play Connect & Auto Sync | DEEPLY AI | 4.8 | 7 | 23 Nov 2025 | 14 Jul 2026 | — | — |
| 23 | Car Play Connect & Sync Mawja | Sidra Capital | 3.0 | 6 | 31 May 2026 | 25 Jun 2026 | — | — |
| 24 | Car Play Connect & Smart Sync | Zhansaya Tolepbergenova | 3.8 | 4 | 23 Nov 2024 | 24 Nov 2024 | — | — |
| 25 | Carlink–It Syncs AI Car & Play | Hong Thuan Truong Thi | 3.0 | 3 | 17 Dec 2025 | 6 Jan 2026 | — | — |
| 26 | Car Play Connect Music Sync | Nguyen Nam Giang | 2.0 | 2 | 5 Oct 2014 | 29 Nov 2025 | — | — (giá $1.99) |
| 27 | **Car Play AI Voice - DriveSpeak** | Berke Keser | 0.0 | 0 | 21 Mar 2026 | 22 May 2026 | — | — |
| 28 | Safar: Muslim Car Play & Drive | ARDA GUENGOER | 0.0 | 0 | 19 Jul 2026 | 2 Aug 2026 | — | — |
| 29 | Car Connect Play - Car Synced | BVK Technologies pvt ltd | 0.0 | 0 | 22 Jun 2026 | 23 Jun 2026 | — | — |
| 30 | CarTube App - Car Play & Task | Tram Nguyen Ngoc | 0.0 | 0 | 12 Mar 2026 | 19 Mar 2026 | — | — |

*(18 app còn lại trong 48 published có installs/revenue dưới ngưỡng đo, không hiển thị.)*

### 7.4 Sáu phát hiện từ bảng cluster

**A. Chỉ 5 app kiếm được tiền — quy luật power-law rất gắt**
5 app đầu chiếm $660K trong tổng $660K của cả cluster. 43 app còn lại: **$0**.
Tỷ lệ thành công tài chính trong niche này: **5/100 app từng tồn tại = 5%**.

**B. Đối thủ trực tiếp nhất mang đúng tên gốc chúng ta định dùng**
`Car Play Connect - Auto Sync` (App Ventures) — 4.6★, 6K votes, **200K installs/tháng**, **$200K/tháng**, release 10 May 2025, cập nhật 2 Jul 2026.
→ Đây là app đang sống tốt với chính cái tên đó. Nếu ta dùng tên `CarPlay Connect - Auto Sync` thì (1) vi phạm không gian tên của họ, (2) cạnh tranh ASO trực diện với một app đã có 6K review và 14 tháng tuổi. **Quyết định đổi sang Carbina là bắt buộc, không chỉ nên.**

**C. Các app "già" tích lũy review khổng lồ nhưng revenue thấp hơn app mới**

| App | Tuổi | Votes | Monthly Revenue | Revenue/1K votes |
|---|---|---|---|---|
| Car Play Connect, Sync & Care | 3.5 năm | 48K | $100K | $2.1K |
| Car Play Connect: Remote Sync | 4.2 năm | 19K | — | — |
| Car Play Connect: Remote Start | 3 năm | 25K | $100K | $4.0K |
| **Car Play Connect - Auto Sync** | **1.2 năm** | **6K** | **$200K** | **$33.3K** |
| **Car Auto Play: Sync & Connect** | **0.9 năm** | **3K** | **$200K** | **$66.7K** |
| **myCar (ngoài cluster)** | **0.7 năm** | **10K** | **$900K** | **$90K** |

→ Xu hướng rất rõ: **app càng mới, revenue/review càng cao**. App cũ có nhiều review nhưng monetize kém (paywall lỏng, giá thấp thời 2022-2023). App mới (2025-2026) dùng paywall gắt + giá cao. myCar là cực điểm của xu hướng này.
→ Hàm ý: đây là niche **không có lợi thế người đi trước (no first-mover advantage)**. Vào muộn với monetization tốt hơn thắng vào sớm. **Tốt cho Carbina.**

**D. Đã có 4 app dùng từ khóa "AI" — nhưng chưa ai làm được**

| App | Rating | Votes | Revenue |
|---|---|---|---|
| Car Play Connect: Car Sync AI | 4.9 | 781 | — |
| Car Play Sync: AI Connect App | 5.0 | 14 | — |
| Carlink–It Syncs AI Car & Play | 3.0 | 3 | — |
| **Car Play AI Voice - DriveSpeak** | **0.0** | **0** | — |
| Car Play Connect & Auto Sync (dev: **DEEPLY AI**) | 4.8 | 7 | — |

Cả 5 đều **$0 revenue**. Đáng chú ý nhất: **`Car Play AI Voice - DriveSpeak`** (release 21 Mar 2026) — đây chính là ý tưởng "giọng AI trong xe", đã có người thử, và có **0 rating / 0 traction**.

→ Hai cách đọc, cả hai đều quan trọng:
1. **Tích cực**: "AI" chưa được ai thực thi tốt trong niche này. Khoảng trống còn nguyên.
2. **Cảnh báo**: gắn chữ "AI" vào tên **không** tự tạo ra traction. DriveSpeak chứng minh điều đó. Thứ tạo traction trong niche này là **creative marketing + paywall**, không phải tên.

→ Hàm ý cho Carbina: AI phải là **chất lượng sản phẩm thật** (giải quyết complaint kỹ thuật của myCar), không phải nhãn dán trên tên. Và cần ngân sách marketing thật — myCar đạt $900K/tháng nhờ Facebook/Instagram/TikTok ads, không nhờ organic.

**E. Nhiều developer là cá nhân, không phải công ty**
Trong 30 app: 14 developer là **tên cá nhân** (Alexey Timokhin, Emrullah Bas, Veysel AKBALIK, Nazar Stasyk, Huy Nguyen, Chanh Tran, Nguyen Nam Giang, Tram Nguyen Ngoc, Hong Thuan Truong Thi, Berke Keser, VALERY STAKARSKI, AHMET KEREM YUCALAN, Zhansaya Tolepbergenova, ARDA GUENGOER).
Đáng chú ý: **6 developer là người Việt Nam** (Huy Nguyen, Chanh Tran, Nguyen Nam Giang, Tram Nguyen Ngoc, Hong Thuan Truong Thi, Tu Ti Co). Một trong số đó — `Sync: Ford Car Play Connect` (Huy Nguyen) — đạt **20K installs/tháng**, 4.6★, 3K votes.
→ Rào cản gia nhập thấp. Vừa là cơ hội (ta làm được) vừa là rủi ro (ai cũng làm được, khác biệt hóa phải nằm ở chất lượng thực thi).

**F. Tên developer bất thường — dấu hiệu app farm**
- `PDF Scanner Editor PDF Converter Expert` phát hành app CarPlay
- `AUTHENTICATOR APP 2FA AUTH LTD` phát hành app CarPlay
- `CAR CONNECT PLAY DIGITAL CAR KEY.` (tên developer nhồi từ khóa, có dấu chấm cuối)

→ Đây là các studio làm app hàng loạt, đặt tên account theo từ khóa ASO. Xác nhận thêm: niche này đầy app farm, Apple đang phải dọn liên tục (52% removal).

### 7.5 Dữ liệu KHÔNG lấy được cho cluster này

- **SDK stack của myCar**: AppStoreSpy trả "No data at this time" → không biết họ dùng RevenueCat / Adapty / Superwall
- **Paywall structure chính thức**: "No data at this time"
- **Similar Apps / Reverse Similar Apps**: "No data at this time"
- **Ad creatives**: Section tồn tại và có **3 creative Facebook**, kèm link "Search in Meta Ad Library" — nhưng chưa mở từng creative để xem nội dung. Đây là việc còn lại đáng làm nhất, vì nó sẽ cho biết chính xác hook "Jarvis" được trình bày thế nào.
- **Top Countries trên AppStoreSpy**: hiển thị "-" (cần gói cao hơn) → đã thay bằng proxy rating-votes ở mục 3

---

## 8. Bảng Bằng chứng (bổ sung cho lần nghiên cứu này)

| Claim | Nguồn | Ngày | Độ tin cậy |
|---|---|---|---|
| Seller pháp lý = KarmaTECH OU; genres Utilities+Travel; minOS 15.1; 73.7MB; 9 ngôn ngữ; rating 4.5822/10,785 votes; release 2025-11-20; v1.10.1 (2026-08-04) | Apple iTunes Lookup API, `country=us` | 2026-08-06 | **Rất cao** (API chính thức của Apple) |
| Chart #33 Utilities US Top Free | Trang App Store công khai (apps.apple.com/us/app/id6755033589) | 2026-08-06 | Cao |
| Copyright "© 2026 myCar Connect" | Trang App Store công khai | 2026-08-06 | Cao |
| Phân bổ 47 storefront; US 53.7%, MX 7.2%, LATAM cluster 14.6% | iTunes Lookup API × 47 country codes, tổng hợp `userRatingCount` | 2026-08-06 | **Cao cho rating votes** / **Trung bình khi dùng làm proxy cho user base** |
| Giá: weekly $7.99, yearly $34.99 (trước là $24.99, promo $19.99) | Tổng hợp 96 review người dùng ở 5 storefront (US, CA, MX, GB, DE) qua Apple Customer Reviews RSS | 2026-08-06 | **Trung bình** — user-reported, không phải từ App Store Connect. Nhiều review độc lập khớp nhau nên độ tin cậy khá, nhưng cần xác nhận lại bằng cách mở paywall thật |
| Hard paywall ngay khi mở app, không free trial, không feature miễn phí | ~60/96 review nêu rõ | 2026-08-06 | **Cao** (khối lượng bằng chứng lớn, nhất quán) |
| Phân bổ rating của 96 review gần nhất: 78.1% là 1★, 0% là 4★ | Apple Customer Reviews RSS, `sortby=mostrecent`, 5 storefront | 2026-08-06 | **Cao** cho mẫu này. **Lưu ý sai lệch mẫu**: RSS chỉ trả review có viết nội dung (không tính rating-only), và người viết review thường có động lực âm mạnh hơn. Không được đọc con số 78% như tỷ lệ của toàn bộ 10,785 votes |
| Kênh acquisition = Facebook/Instagram/TikTok ads; hook "Jarvis" AI voice không tồn tại trong app | ≥6 review nêu tên kênh cụ thể và tên hook | 2026-08-06 | Cao |
| Complaint kỹ thuật: widget cắt chữ trên Jeep Wrangler 2022 màn 8"; không chạy trên xe 2026; sound bị nhạc lấn; disconnect sound lệch thời điểm | Review cụ thể có nêu model xe | 2026-08-06 | Cao (báo cáo trực tiếp từ người dùng, có ngữ cảnh cụ thể) |
| iOS cluster "car play": 48 published / 100 total / 52 removed / 512K monthly installs / $660K monthly revenue | AppStoreSpy Market Explorer, filter `name="car play"`, App Store | 2026-08-06 | Cao (count) / **Trung bình** (installs & revenue là estimate SensorTower) |
| 7 app cùng cluster do Apple gợi ý là đối thủ trực tiếp của myCar | Section "You Might Also Like" trên trang App Store của myCar | 2026-08-06 | Cao (Apple tự xác định nhóm liên quan) |
| Retention D1/D7/D30 của myCar | **KHÔNG CÓ NGUỒN** | — | — |
| Revenue/install tăng 0.83→1.25→1.80 (Mar→Apr→Jul 2026) | Tính từ chart AppStoreSpy Revenue & Downloads | 2026-08-06 | **Thấp-Trung bình** (giá trị nội suy từ chart, cả tử số và mẫu số đều là estimate) |

### 8.1 Giới hạn cần nêu rõ khi dùng dữ liệu này trong PRD

1. **Giá subscription là user-reported**, không phải từ nguồn chính thức. Con số $7.99/tuần và $34.99/năm được nhiều review độc lập xác nhận, nhưng nên verify bằng cách mở app thật trước khi đưa vào bảng so sánh giá của PRD.
2. **78% review 1★ là của mẫu 96 review có viết nội dung**, không phải của toàn bộ 10,785 rating. Đừng viết "rating thật của myCar là 1.5★" như một fact — hãy viết "sentiment trong review viết tay gần nhất đã đảo chiều mạnh".
3. **Top countries là proxy qua rating votes**, không phải installs. Tỷ lệ rating/install có thể khác nhau giữa các nước (văn hóa review, prompt localization).
4. **Installs và revenue là estimate SensorTower**, sai số có thể ±30-50%.
5. **Retention: không có dữ liệu.** Mọi con số retention trong PRD phải là mục tiêu của chúng ta hoặc benchmark ngành có nguồn, tuyệt đối không gán cho myCar.

---

## 9. Hàm ý Trực tiếp cho `Carbina: Car Dashboard & Widgets`

### 9.1 Chiến lược Monetization — điểm khác biệt lớn nhất

| | myCar (đối thủ) | **Carbina (đề xuất)** | Lý do |
|---|---|---|---|
| Paywall | Hard, ngay khi mở app | **Free tier có giá trị thật + 7-day trial** | 60/96 review complaint chính là đây. Đây là khe hở lớn nhất |
| Free tier | Không có gì | 1 widget + 3 sound preset + dashboard cơ bản | Cho user thấy app chạy được **trên xe của họ** trước khi trả tiền — giải quyết luôn complaint "không chạy trên xe tôi" |
| Weekly | $7.99 | **Không bán weekly** | Weekly $7.99 là thứ khiến user gọi họ là "scam". Bán weekly = tự đặt mình vào cùng nhóm |
| Monthly | — | **$4.99/tháng** | Thấp hơn ngưỡng đau, không có ở myCar → không so sánh trực tiếp được |
| Yearly | $34.99 | **$29.99/năm** | Dưới myCar, và **không dùng chiêu "90% off"** (myCar bị tố bait-and-switch vì việc này) |
| Lifetime | Không có | **$49.99 one-time** | Request rõ ràng: "I would be willing to buy this app outright, but I'm not going to pay for the rest of my life" |

### 9.2 Ưu tiên Feature — dựa trên PMF đã được validate

**Tier 1 — có PMF chứng minh, phải có trong MVP:**
1. **Âm thanh connect / disconnect / arrive-home** — feature duy nhất được khen cả trong review 1★. Phải làm tốt hơn: điều chỉnh âm lượng, duck nhạc đang phát, sync đúng thời điểm tắt máy (3 complaint riêng về việc này)
2. **Widget CarPlay tự adapt kích thước màn hình** — complaint Jeep 8" cho thấy myCar hardcode layout. Đây là lỗi kỹ thuật cụ thể có thể thắng
3. **Thư viện xe có year + trim + color** — request trực tiếp

**Tier 2 — hook marketing đã validate nhưng đang bỏ trống:**
4. **Giọng AI chào cá nhân hóa theo ngữ cảnh** (không đặt tên "Jarvis") — myCar quảng cáo cái này và thu được $900K/tháng mà **không giao được**. Đây là chỗ on-device AI của Carbina thắng thật

**Tier 3 — khác biệt hóa dài hạn:**
5. AI học thói quen → tự sắp xếp dashboard
6. Widget tương tác thật (complaint: "Click on orders and nothing happens")

### 9.3 Rủi ro phải thêm vào Risk Matrix của PRD

| ID | Rủi ro | Bằng chứng | Mitigation |
|---|---|---|---|
| R-new-1 | **App Store takedown** | 52% removal rate trong cluster "car play"; 42% trong cluster "carplay" | Không dùng từ `Connect`/`Sync`/`Link`/`Remote` trong tên & subtitle. Không hứa hẹn khả năng kết nối CarPlay trong metadata/screenshot |
| R-new-2 | **Bị xếp cùng nhóm với app scam** | Apple's "You Might Also Like" nhóm myCar với 6 app "Car Play Connect" | Định vị ASO sang cluster "widget/dashboard/personalization", không phải "connect/sync" |
| R-new-3 | **Backlash false-advertising** | myCar mất sentiment vì quảng cáo "Jarvis" không có thật | Mọi creative chỉ được quay **feature thật đang chạy**. Không mockup, không concept video |
| R-new-4 | **Fragmentation màn hình xe** | Widget cắt chữ trên Jeep 8"; không chạy trên xe 2026 | Test matrix bắt buộc trên nhiều kích thước CarPlay screen. Layout responsive, không hardcode |
| R-new-5 | **Chargeback / dispute** | Nhiều báo cáo thu sai tiền ($24.99 → $44.98/$49.00) | Không dùng dark pattern giá. Hiển thị giá cuối cùng rõ ràng trước khi confirm |

### 9.4 Thị trường ưu tiên

| Ưu tiên | Thị trường | Lý do |
|---|---|---|
| P0 | **US** (EN) | 53.7% user base của đối thủ; purchasing power cao nhất |
| P1 | **MX + CO + CL + AR** (ES) | Cluster 11.9%, rating cao hơn US (4.64-4.74), ít cạnh tranh chất lượng |
| P1 | **BR** (PT) | 2.7%, rating 4.55 |
| P2 | CA (EN/FR), GB, DE, FR, AU | Tổng ~13% |
| Soft-launch | **VN** (rating 4.68, volume nhỏ) | Test an toàn trước khi mở US |

---

## 10. Việc còn thiếu

**Đã thử và xác nhận KHÔNG có nguồn:**
- ~~SDK stack của myCar~~ → AppStoreSpy trả "No data at this time"
- ~~Paywall structure chính thức~~ → AppStoreSpy trả "No data at this time"; đã thay bằng tái dựng từ 96 review (mục 2)
- ~~Top Countries trên AppStoreSpy~~ → cần gói cao hơn; đã thay bằng proxy rating-votes 47 storefront (mục 3)
- ~~Retention D1/D7/D30~~ → không tồn tại nguồn công khai (mục 5); đã thay bằng 2 proxy

**Còn làm được, xếp theo giá trị:**
- [ ] **Mở 3 ad creative Facebook của myCar** trên AppStoreSpy (section "Ad сreatives", anchor `#app-ad-сreatives`) + tra Meta Ad Library. Đây là việc giá trị nhất còn lại: sẽ cho biết chính xác hook "Jarvis" được dựng thế nào, để (a) học cấu trúc creative đang thắng, (b) biết rõ đường ranh giới false-advertising cần tránh
- [ ] **Xác nhận giá subscription từ paywall thật** — cài myCar và mở paywall. Hiện $7.99/tuần + $34.99/năm là user-reported từ 96 review (nhất quán nhưng không phải nguồn chính thức)
- [ ] **Deep-dive 2 app revenue cao nhất trong cluster**: `Car Play Connect - Auto Sync` (App Ventures, $200K/tháng) và `Car Auto Play: Sync & Connect` (Appstract Works, $200K/tháng) — đọc review để tìm complaint pattern, so với myCar
- [ ] **Benchmark retention ngành cho iOS Utilities freemium** — cần nguồn thật (không dùng số của myCar). Dùng để đặt mục tiêu D1/D7/D30 trong PRD
- [ ] **Đọc review của `Car Play AI Voice - DriveSpeak`** — app "AI voice" duy nhất, 0 rating. Tìm hiểu tại sao thất bại (0 review nên có thể chỉ là chưa marketing)
- [ ] **Kiểm tra `CarPlay: Mirror & Car Control`** (Trail Byte, Android, 4.4★/725 votes) — đối thủ chất lượng duy nhất trong cluster Android
