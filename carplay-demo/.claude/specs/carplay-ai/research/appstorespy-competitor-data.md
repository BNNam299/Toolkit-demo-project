# Dữ liệu Đối thủ từ AppStoreSpy — CarPlay Niche

**Nguồn**: https://appstorespy.com (Market Explorer, dữ liệu SensorTower)
**Ngày thu thập**: 2026-08-06
**Phương pháp**: Truy cập trực tiếp qua browser (Kimi WebBridge), lọc `name contains "carplay"` và `name contains "car"`, sắp xếp theo Monthly Installs / Monthly Revenue
**Lưu ý**: Số liệu installs/revenue là **estimate** của AppStoreSpy/SensorTower, không phải số liệu chính thức từ Apple/Google.

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

## 1. Tổng quan Niche "CarPlay" — Bảng Điều Khiển Thị Trường

| Chỉ số | iOS App Store | Google Play |
|---|---|---|
| Apps đang phát hành (Published) | **7** | **72** |
| Tổng apps từng tồn tại (Total) | 12 | 223 |
| Apps đã bị xóa (Removed) | **5** | **151** |
| **Tỷ lệ bị xóa** | **41.7%** | **67.7%** |
| Daily Installs (toàn niche) | 0 | 2K |
| Monthly Installs (toàn niche) | **0** | **98K** |
| Monthly Revenue (toàn niche) | **$0** | **$0** |

**Kết luận số 1**: Niche tên "CarPlay" trên **iOS hoàn toàn không có doanh thu và không có lượt tải đo được**. Trên Android có 98K installs/tháng nhưng **doanh thu $0** — không ai monetize được.

**Kết luận số 2**: Tỷ lệ app bị xóa 42% (iOS) và 68% (Android) là mức cực kỳ cao. Đây là tín hiệu **rủi ro tuân thủ (compliance risk)** rất mạnh — Apple/Google chủ động takedown các app hứa hẹn "kết nối CarPlay" mà không thực hiện được về mặt kỹ thuật.

---

## 2. Bảng 1 — Toàn bộ 7 App iOS có "CarPlay" trong tên (Published)

| # | App Name | Developer | Rating | Rating Votes | Release Date | Last Updated | Monthly Installs | Monthly Revenue |
|---|---|---|---|---|---|---|---|---|
| 1 | DriveGo: GPS & CarPlay | Stefano Presot | 5.0 | 4 | 19 Feb 2026 | 20 May 2026 | — | — |
| 2 | ParkFast - CarPlay Parking | Datachain Consulting Pty Ltd | 0.0 | 0 | 1 May 2026 | 12 May 2026 | — | — |
| 3 | Drive Hub: CarPlay & Tracker | Vu Van | 0.0 | 0 | 13 Jan 2026 | 26 Jul 2026 | — | — |
| 4 | Carplayer+ | Deshi Limawan | 0.0 | 0 | 22 Jul 2026 | 24 Jul 2026 | — | — |
| 5 | **CarPlay Connect - Sync My Auto** | **Oleksandr Malyhin** | **0.0** | **0** | **3 Feb 2026** | 25 Apr 2026 | **—** | **—** |
| 6 | Dynamic Lyrics for carplay&App | ZeroEra Tech | 5.0 | 1 | 16 May 2026 | 23 Jun 2026 | — | — |
| 7 | Vibe: Dynamic Lyrics & CarPlay | Petr Nezval | 0.0 | 0 | 19 Apr 2026 | 31 Jul 2026 | — | — |

⚠️ **CẢNH BÁO TRỌNG YẾU**: App số 5 — **"CarPlay Connect - Sync My Auto"** — chính là **tên sản phẩm mục tiêu của chúng ta**. App này đã tồn tại trên App Store từ 3 Feb 2026 (6 tháng), và có:
- Rating: **0.0** (không có review nào)
- Rating votes: **0**
- Installs: không đo được (dưới ngưỡng đo)
- Cập nhật cuối: 25 Apr 2026 → **đã bỏ hoang 3 tháng**

→ Tên này đã bị chiếm dụng và đã thất bại. Cần đổi tên/định vị sản phẩm.

**Nhận xét chung 7 app iOS**:
- 5/7 app có rating 0.0 (không ai review)
- 6/7 app phát hành trong năm 2026 (đều rất mới, đều không traction)
- Không app nào đạt ngưỡng đo lường installs của SensorTower (< ~5K/tháng)

---

## 3. Bảng 2 — App iOS "CarPlay" ĐÃ BỊ XÓA (Removed / Graveyard)

| App Name | Developer | Rating | Votes | Release | Last Updated |
|---|---|---|---|---|---|
| Dynamic Lyrics for CarPlay | Meta Innovation | 4.1 | 33 | 12 Oct 2025 | 10 Nov 2025 |
| **My Smart keys-CarPlay Connect** | European Apps Solutions | 5.0 | 1 | 7 Sept 2022 | 4 Aug 2024 |
| Songiz for CarPlay | (dev id 1471876720) | 1.0 | 1 | 2 Oct 2019 | 30 Aug 2020 |
| News Break for CarPlay | (dev id 1471876720) | 3.0 | 7 | 25 Jul 2019 | 6 Oct 2020 |
| 7+ for Touch ID, CarPlay & iOS 7 | 宗亮 付 | 1.2 | 1 | 12 Dec 2013 | 22 Jul 2014 |

**Insight**: "Dynamic Lyrics for CarPlay" bị xóa chỉ **1 tháng sau** lần cập nhật cuối, dù có rating 4.1 và 33 votes — cho thấy takedown không phải vì chất lượng thấp mà vì **vi phạm guideline**. Đồng thời có 2 app clone "Dynamic Lyrics" khác đang sống trên store → Apple đang chơi trò mèo vờn chuột với nhóm này.

---

## 4. Bảng 3 — Toàn bộ 30 App Google Play "CarPlay" (sắp xếp theo Monthly Installs)

| # | App Name | Developer | Rating | Votes | Release | Last Updated | Monthly Installs | Total Installs |
|---|---|---|---|---|---|---|---|---|
| 1 | Apple Carplay App For Android | Tech Daze | 2.2 | 107 | 25 Apr 2024 | 9 Aug 2025 | 20K | 100K+ |
| 2 | Carplay for Android | Syscraft Labs | 3.8 | 587 | 13 Feb 2026 | 19 Jul 2026 | 20K | 50K+ |
| 3 | Zlink carplay | Dannis24 | 2.2 | 184 | 3 Feb 2025 | 6 Feb 2025 | 20K | 100K+ |
| 4 | Carplay for Android | CarConnect | 2.5 | 210 | 26 Feb 2025 | 26 Feb 2025 | 10K | 100K+ |
| 5 | Tlink5 carplay Android | BigQuest Apps | — | — | 26 Jan 2026 | 26 Jan 2026 | 9K | 10K+ |
| 6 | Zlink5 Carplay | DevloApps | 2.6 | 52 | 29 Oct 2024 | 12 Aug 2025 | 7K | 100K+ |
| 7 | Carplay Auto Sync | Roshnee tech | 2.9 | 215 | 13 Dec 2024 | 3 Aug 2026 | 6K | 100K+ |
| 8 | Tlink5 carplay Android | OziTech Solutions | 1.6 | 39 | 26 Dec 2025 | 26 Dec 2025 | 6K | 10K+ |
| 9 | Zlink5 Carplay Android | PixelBrew | 1.4 | 195 | 4 Feb 2025 | 28 Jul 2025 | — | 100K+ |
| 10 | Zlink carplay Android | OziTech Solutions | 1.0 | 36 | 26 Dec 2025 | 31 Dec 2025 | — | 10K+ |
| 11 | Zlink Carplay Android | Sayyara apps & games | 1.6 | 76 | 15 Feb 2024 | 6 Oct 2025 | — | 50K+ |
| 12 | CarPlay android auto link | SherazSoft | 3.5 | 30 | 30 May 2025 | 30 May 2025 | — | 10K+ |
| 13 | CarSync for Android/CarPlay | FastSoft | 4.2 | 146 | 20 Sept 2024 | 9 Dec 2024 | — | 10K+ |
| 14 | CarPlay Auto Cast Sync Android | 10x Applications | — | — | 8 Aug 2024 | 4 Jan 2025 | — | 10K+ |
| 15 | CarPlay Android - CarStream | Heavenapps | 2.9 | 27 | 1 Mar 2025 | 1 Mar 2025 | — | 10K+ |
| 16 | Bluetooth Connect Carplay Auto | Unitedappx | 4.1 | 425 | 19 Dec 2020 | 9 Apr 2026 | — | 100K+ |
| 17 | Apple Carplay Ford | RizwanDev1 | — | — | 17 May 2026 | 17 May 2026 | — | 50+ |
| 18 | Carplay App for Android | Techy Tools Hub | — | — | 13 Feb 2026 | 13 Feb 2026 | — | 500+ |
| 19 | Carplay Android AutoApp | Irfankhan | — | — | 10 Mar 2026 | 10 Mar 2026 | — | 100+ |
| 20 | Apple Carplay Mercedes | Zia.Apps | — | — | 10 May 2026 | 10 May 2026 | — | 50+ |
| 21 | Carplay android: Car play auto | Funapps Solutions | — | — | 26 Feb 2024 | 27 Mar 2024 | — | 5K+ |
| 22 | Zlink CarPlay Android Auto | Muzzlestop | — | — | 12 Mar 2026 | 1 May 2026 | — | 500+ |
| 23 | Zlink carplay | Nexus Apps Solution | — | — | 16 Jul 2025 | 19 Jul 2025 | — | 10K+ |
| 24 | Android Carplay BMW | Gemstone Developer | — | — | 15 May 2026 | 15 May 2026 | — | 100+ |
| 25 | **CarPlay: Mirror & Car Control** | **Trail Byte** | **4.4** | **725** | 12 Dec 2025 | 30 Jul 2026 | — | 10K+ |
| 26 | Zlink5 Carplay Android Auto | Gumani tech | — | — | 22 Jul 2026 | 22 Jul 2026 | — | 0+ |
| 27 | CarPlay Cast | WonderAPk | — | — | 30 Oct 2023 | 2 Nov 2023 | — | 1K+ |
| 28 | CarPlay Sync: Auto Connect | Abdul Khalique khan | — | — | 27 Jul 2026 | 27 Jul 2026 | — | 0+ |
| 29 | CarPlay Auto Link & Sync | tech solver official | — | — | 20 Jul 2025 | 20 Jul 2025 | — | 500+ |
| 30 | Carplay for Android | Console apps | — | — | 18 Jul 2026 | 18 Jul 2026 | — | 100+ |

**Phân tích chất lượng**: Rating trung bình của top 10 = **2.2/5.0**. Đây là mức thảm họa. Toàn bộ niche là **clone farm** — cùng một app được đổi tên (Zlink / Zlink5 / Tlink5) và tái xuất bản bởi nhiều developer khác nhau.

**Ngoại lệ đáng chú ý** (rating > 4.0):
- `CarPlay: Mirror & Car Control` (Trail Byte) — 4.4★, 725 votes, cập nhật đều (30 Jul 2026) → đối thủ chất lượng duy nhất trong niche
- `CarSync for Android/CarPlay` (FastSoft) — 4.2★, 146 votes
- `Bluetooth Connect Carplay Auto` (Unitedappx) — 4.1★, 425 votes, sống từ 2020 → longevity 6 năm

---

## 5. Bảng 4 — App Automotive iOS THỰC SỰ CÓ DOANH THU (mở rộng: `name contains "car"`, sort theo revenue)

Đây là các app không dùng tên "CarPlay" nhưng đang kiếm tiền thật trong không gian ô-tô:

| App Name | Developer | Rating | Votes | Release | Last Updated | Monthly Installs | **Monthly Revenue** |
|---|---|---|---|---|---|---|---|
| **myCar: Car Widgets & Dashboard** | **DOFUapps** | **4.6** | **10K** | **19 Nov 2025** | **4 Aug 2026** | **500K** | **$900K** |
| CARFAX - New & Used Cars | CARFAX, Inc. | 4.9 | 368K | 15 Nov 2011 | 5 Aug 2026 | 200K | $400K |
| Carly — OBD2 car scanner | Carly Solutions GmbH Co KG | 4.6 | 9K | 7 Oct 2011 | 29 Jul 2026 | 10K | $400K |

*(Các dòng khác trong bảng gốc là game/plant-care app trùng chữ "car"/"card" — đã loại khỏi bảng này.)*

---

## 6. Phân tích Sâu — Đối thủ Trực tiếp #1: `myCar: Car Widgets & Dashboard`

**Link**: https://apps.apple.com/app/id6755033589
**AppStoreSpy**: https://appstorespy.com/ios-apple-store/6755033589-trends-revenue-statistics-downloads-ratings

| Chỉ số | Giá trị |
|---|---|
| Developer | DOFUapps |
| Subtitle | "Driving Widgets · Startup Sounds" |
| Category | **Utilities** |
| Rating | 4.6 ★ |
| Rating Votes | 10K |
| Release date | 2025-11-20 (**8 tháng tuổi**) |
| Latest update | 2026-08-04 (2 ngày trước) |
| App size | 70 MB |
| Version hiện tại | 1.10.1 |
| Monthly Installs | **500K** |
| Monthly Revenue | **$900K** |
| Có IAP | Có |
| Top Chart | iPhone / Utilities / Top Free |

### Đường cong tăng trưởng (12 tháng, từ chart Revenue & Downloads)

| Mốc thời gian | Monthly Installs | Monthly Revenue |
|---|---|---|
| Feb 2026 | ~10K | ~$0 |
| Mar 2026 | ~300K | ~$250K |
| **Apr 2026 (đỉnh)** | **~801K** | **~$1M** |
| Jun 2026 | ~620K | ~$1M |
| Jul 2026 | ~500K | ~$900K |

**Đọc đường cong**:
1. **0 → $1M/tháng trong 5 tháng** — tốc độ tăng trưởng cực nhanh, xác nhận đây là niche có nhu cầu thật và monetize được.
2. Installs đang **giảm** (801K → 500K, -37% từ đỉnh) nhưng revenue **giữ nguyên** ($1M → $900K, -10%). Đây là mô hình hậu-viral điển hình: hết đà tăng trưởng tự nhiên nhưng base subscriber đã đóng tiền vẫn giữ.
3. Cập nhật 2 ngày/lần cho thấy team đang chạy nước rút giữ chart position.

### Chiến lược Marketing (đọc từ screenshot App Store)
Các câu headline trong 6 screenshot đầu:
1. "Build Your **Car Dashboard**"
2. "Transform Your Car **With Widgets**"
3. "Enable Custom Sounds **for Every Ride**" → có nhắc `CarPlay Connection Sound`
4. "Create Widgets **In Seconds**"
5. "Access All **Viral Sound Libary**" → có nhắc `CarPlay Sounds`
6. "Endless Widgets **Fast Install**" → có country flags

**Insight định vị**: myCar **KHÔNG** bán "kết nối CarPlay". Nó bán:
- **Widget trang trí** cho home screen (thẩm mỹ)
- **Âm thanh khởi động xe** (startup sound) — yếu tố viral trên TikTok
- CarPlay chỉ là **feature phụ**, không phải value proposition chính

→ Đây chính là lý do nó sống và kiếm $900K/tháng, trong khi 7 app "CarPlay Connect" chết sạch.

### Ghi chú giới hạn dữ liệu
- Phần **Paywalls**: "No data at this time" (AppStoreSpy chưa crawl được) → không lấy được giá subscription cụ thể
- Phần **Similar Apps** / **Reverse Similar Apps**: "No data at this time"
- Phần **Top Countries**: không hiển thị trên gói hiện tại

---

## 7. Bảng Bằng chứng (Evidence Table)

| Claim | Nguồn | URL | Ngày thu thập | Độ tin cậy |
|---|---|---|---|---|
| iOS: 7 published / 12 total / 5 removed app tên "CarPlay"; 0 installs; $0 revenue | AppStoreSpy Market Explorer (iOS, filter name=CarPlay, available=True) | https://appstorespy.com/apps/ios?filters=...name=CarPlay | 2026-08-06 | Cao (dữ liệu store trực tiếp cho count; estimate cho installs) |
| Google Play: 72 published / 223 total / 151 removed; 98K monthly installs; $0 revenue | AppStoreSpy Market Explorer (Play, filter name=CarPlay) | https://appstorespy.com/apps/play?filters=...name=CarPlay | 2026-08-06 | Cao (count) / Trung bình (installs estimate) |
| "CarPlay Connect - Sync My Auto" tồn tại, dev Oleksandr Malyhin, rating 0.0, release 3 Feb 2026 | AppStoreSpy iOS list | (như trên) | 2026-08-06 | Cao |
| 5 app iOS "CarPlay" đã bị xóa, gồm "Dynamic Lyrics for CarPlay" (4.1★, 33 votes, xóa sau 1 tháng) | AppStoreSpy Market Explorer (iOS, available=False) | https://appstorespy.com/apps/ios?filters=...available=False | 2026-08-06 | Cao |
| Rating trung bình top-10 Android "CarPlay" = 2.2/5.0 | Tính từ Bảng 3 | (như trên) | 2026-08-06 | Cao |
| myCar: 500K installs/tháng, $900K revenue/tháng, 4.6★, 10K votes, release 2025-11-20, Utilities, 70MB, v1.10.1 | AppStoreSpy app detail page | https://appstorespy.com/ios-apple-store/6755033589-trends-revenue-statistics-downloads-ratings | 2026-08-06 | Trung bình-Cao (SensorTower estimate cho installs/revenue; metadata store là chính xác) |
| myCar tăng trưởng 0 → ~$1M/tháng trong 5 tháng, đỉnh Apr 2026 | AppStoreSpy chart "Revenue and Downloads", period = Last 12 months | (như trên) | 2026-08-06 | Trung bình (đọc từ chart, giá trị nội suy) |
| myCar định vị "widget + startup sound", CarPlay là feature phụ | Screenshot marketing trên trang AppStoreSpy "Images and Description" | (như trên) | 2026-08-06 | Cao (nội dung marketing công khai) |
| Carly OBD2: $400K/tháng, 10K installs/tháng, 4.6★ | AppStoreSpy Market Explorer (iOS, name=car, sort=-revenue) | https://appstorespy.com/apps/ios?filters=...name=car&sort=-revenue | 2026-08-06 | Trung bình (estimate) |
| CARFAX: $400K/tháng, 200K installs/tháng, 4.9★, 368K votes | AppStoreSpy Market Explorer (như trên) | (như trên) | 2026-08-06 | Trung bình (estimate) |

**Giới hạn dữ liệu cần nêu rõ**:
- Installs và Revenue là **estimate** của AppStoreSpy/SensorTower, sai số có thể ±30-50%
- Dấu "—" trong bảng nghĩa là **dưới ngưỡng đo lường**, không phải bằng 0 tuyệt đối
- Không lấy được: giá subscription cụ thể, retention D1/D7/D30, DAU, top countries, paywall structure (giới hạn gói tài khoản)

---

## 8. Hàm ý Chiến lược cho Sản phẩm của Chúng ta

### 8.1 Ba kết luận buộc phải hành động

**A. Tên "CarPlay Connect - Auto Sync" phải bỏ.**
- Tên gần như y hệt đã tồn tại và đã chết trên App Store (`CarPlay Connect - Sync My Auto`, 0 rating, bỏ hoang từ Apr 2026)
- Toàn bộ cluster tên này có 0 revenue trên iOS và 0 revenue trên Android
- 42-68% app trong cluster bị store takedown

**B. Định vị "giúp bạn kết nối CarPlay" là định vị chết.**
Bằng chứng: 79 app (7 iOS + 72 Android) dùng định vị này → tổng doanh thu $0.
Nguyên nhân: CarPlay là tính năng do Apple + hãng xe kiểm soát ở tầng firmware. Một app iOS **không thể** tạo ra kết nối CarPlay mà xe không hỗ trợ. Người dùng tải về, thất vọng, để lại 1-2★, Apple takedown.

**C. Định vị "Car Dashboard / Widget / Trải nghiệm lái" là định vị sống — và đang có $900K/tháng.**
myCar chứng minh: cùng một tệp người dùng (chủ xe dùng iPhone), nhưng bán **trải nghiệm** (widget, âm thanh, dashboard đẹp) thay vì bán **kết nối** → 0 → $1M/tháng trong 5 tháng.

### 8.2 Khoảng trống (Gap) chúng ta có thể chiếm

| Gap | Bằng chứng từ dữ liệu | Cơ hội cho AI Dashboard |
|---|---|---|
| myCar bán widget **tĩnh** — người dùng phải tự cấu hình | Screenshot: "Create Widgets In Seconds", "Build Your Car Dashboard" | AI **tự học** thói quen và tự sắp xếp dashboard → không cần cấu hình |
| Installs myCar giảm 37% từ đỉnh | Chart Revenue & Downloads | Đà viral của "startup sound" đang hết → cần lý do quay lại app hằng ngày (retention), đó là chỗ AI thắng |
| Không có app nào trong niche dùng on-device ML | Không app nào trong 79 app đề cập AI/ML | Khác biệt hóa rõ ràng, khó copy trong 6 tháng |
| Rating trung bình niche 2.2★ | Bảng 3 | Chỉ cần đạt 4.5★ là đã vượt toàn bộ nhóm clone |
| Carly kiếm $400K/tháng với chỉ 10K installs/tháng | Bảng 4 | ARPU cao khả thi khi giải quyết vấn đề thật → validate mức giá $7.99/tháng |

### 8.3 Đề xuất điều chỉnh PRD

| Mục PRD | Hiện tại | Cần đổi thành |
|---|---|---|
| Tên sản phẩm | CarPlay Connect - Auto Sync | Cần đổi (xem 3 phương án bên dưới) |
| Định vị chính | Kết nối/sync CarPlay | Dashboard xe thông minh học theo thói quen |
| App Store Category | (chưa xác định) | **Utilities** (theo myCar) |
| Đối thủ số 1 trong Phân tích Cạnh tranh | 5 app clone "Car Play Connect" | **myCar (DOFUapps)** — $900K/tháng |
| Benchmark doanh thu T6 | (theo estimate cũ) | Đối chiếu myCar: $250K ở tháng 4, $1M ở tháng 5 |
| Rủi ro mới cần thêm vào Risk Matrix | — | **R-xx: App Store takedown** do định vị "CarPlay connect" (bằng chứng: 42% takedown rate) — Mitigation: không hứa hẹn kết nối CarPlay trong metadata/screenshot |

### 8.4 Tên sản phẩm — ĐÃ CHỐT (cập nhật 2026-08-07)

> Mục này ban đầu đề xuất 3 phương án (`DriveMind`, `AutoPilot`, `Carbina`). **Cả ba đều đã lỗi thời.** Ngày 07/08/2026 đã chạy sàng lọc trademark thật.

**Tên chính thức: `Carbina`** — subtitle `Car Dashboard & Widgets · AI Learns Your Every Drive`

| Lớp kiểm tra | Kết quả |
|---|---|
| USPTO wordmark | ✅ **Không có kết quả nào** (cả LIVE lẫn DEAD) |
| App Store | ✅ **0 app**; biến thể `carbine` chỉ có 1 app 0-vote khác ngành |
| Domain | ✅ `carbina.app`, `carbina.io`, `carbina.co` **còn trống** (`.com` đang rao bán trên BrandBucket) |
| Còn thiếu | ⚠️ Phonetic equivalents · design marks · common-law rights · Google Play · EUIPO |

**Tên bị loại và lý do:**

| Tên | Lý do loại |
|---|---|
| `CarPlay Connect - Auto Sync` | Trùng app đang hoạt động ($170K/tháng); cluster có 42-52% takedown |
| **`RideIQ`** | **Trademark RIDEIQ đã đăng ký** — Reg. 7063151, LIVE, **HopSkipDrive, Inc.**, Class 042 (phần mềm), standard character claim. Thêm `RIDE IQ` (Ride iQ LLC) và 4 app cùng tên |
| `DriveIQ` | USPTO sạch nhưng App Store có **4 app**, 3 ra mắt 2026, đều ở Navigation/Utilities |
| `RideMind` | USPTO sạch nhưng có `RideMind AI` (Navigation, 06/2026) |
| `Vistaro` | `VISTARO` LIVE/PENDING — **Forescout Technologies**, Class 009+042 phần mềm |
| `Cabina` | `CABINA` LIVE/PENDING — Life Lift LLC, Class 035+042 |
| `Rideo` | `RIDEO` LIVE/REGISTERED — Rideo LLC, Class 009+012 |

**Tên dự phòng nếu Carbina vướng ở vòng pháp lý**: `Cabinova` → `Dashvia` → `Autolume` (cả ba đều sạch USPTO và App Store).

---

## 9. Việc còn thiếu (cần nghiên cứu tiếp)

- [ ] Giá subscription cụ thể của myCar (AppStoreSpy không có paywall data) → cần vào trực tiếp App Store page
- [ ] Đọc 20-30 review gần nhất của myCar để tìm complaint → nguồn cho feature gap
- [ ] Retention D1/D7/D30 của myCar → không có trên AppStoreSpy, cần nguồn khác
- [ ] Top countries của myCar → cần gói AppStoreSpy cao hơn
- [ ] Kiểm tra `CarPlay: Mirror & Car Control` (Trail Byte, 4.4★/725 votes) — đối thủ chất lượng duy nhất trong cluster CarPlay
