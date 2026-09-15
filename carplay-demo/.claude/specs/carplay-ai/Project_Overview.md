# Carbina: Car Dashboard & Widgets — Project Overview

**Document Version**: 2.4
**Snapshot Date**: 2026-08-07 (đồng bộ với PRD v2.4 — xem §0)
**Ngày tạo file**: 2026-08-15
**Status**: Draft — chờ PO review
**Mode**: strict (đầy đủ section, mọi số liệu truy vết được về PRD)

---

## 0. PRD Reference

- **PRD Source**: `.claude/specs/carplay-ai/PRD.md`
- **Snapshot Used**: **PRD v2.4** (07/08/2026) — bản đã qua `gate-prd` với toàn bộ 16 section Pass
- **Reference Policy**: Chiến lược sản phẩm, phân tích thị trường, deep-dive đối thủ, cấu trúc giá và phân tích hòa vốn **thuộc sở hữu của PRD** và **không được chép lại** ở đây. Tài liệu này chỉ tóm tắt ở mức đủ để ra quyết định kiến trúc và kế hoạch thực thi, kèm con trỏ về section gốc của PRD.
- **Snapshot Date nghĩa là gì**: theo `project-docs-contract`, cả 7 tài liệu của bộ spec dùng **chung một Version/Date snapshot**. Snapshot hiện tại là **v2.4 / 2026-08-07** do PRD định nghĩa. File này được tạo ngày 15/08/2026 nhưng **không thêm bất kỳ dữ kiện sản phẩm mới nào** ngoài PRD v2.4, nên nó nằm trong cùng snapshot đó.

### Ranh giới sở hữu nội dung

| Nội dung | Sở hữu bởi | Tài liệu này làm gì |
|---|---|---|
| Phân tích cạnh tranh, doanh thu/DAU đối thủ, review sentiment | PRD §4 | Chỉ dẫn chiếu khi giải thích một quyết định kiến trúc |
| Cấu trúc giá, phân tích hòa vốn, blended ARPU | PRD §11 | Chỉ nêu ràng buộc kỹ thuật phát sinh (StoreKit, entitlement) |
| Danh sách tính năng F1–F13 + acceptance criteria | PRD §7 | Nhóm thành module kiến trúc, không viết lại AC |
| Danh sách 18 màn hình | PRD §10 | Ánh xạ sang module/feature folder, chi tiết layout dời `Wireframes.md` |
| Kiến trúc, tech stack, module boundary, thứ tự thi công | **Tài liệu này** | Sở hữu đầy đủ |
| Use case, luồng thay thế | `Use_Cases.md` (Step 3) | Không viết ở đây |
| Đặc tả FR + AC chi tiết | `Functional_Requirements.md` (Step 4) | Không viết ở đây |

---

## 1. Introduction

### 1.1 Problem Statement

Màn hình CarPlay nguyên bản là tĩnh: nó hiển thị cùng một bộ icon cho mọi người lái, ở mọi thời điểm, trong mọi hoàn cảnh. Nó không học được nhạc người dùng hay nghe, tuyến đường quen, hay giờ nào thì họ đi đâu. Hệ quả là mỗi lần lên xe người lái phải tự thao tác lại từ đầu — mở app nhạc, tìm playlist, gõ điểm đến — và mỗi thao tác đó là vài chục giây mất tập trung trong lúc đang cầm vô-lăng (PRD §3, hành trình hiện tại).

Thị trường đã có người cố lấp khoảng trống này, nhưng lấp bằng cách sai. Nhóm app đang dẫn đầu niche vận hành theo mô hình **churn-and-refill**: mua traffic bằng quảng cáo, chặn paywall ngay màn hình đầu, thu tiền trước khi người dùng kịp biết app có chạy trên xe của họ hay không. Kết quả đo được ở đối thủ số 1 (PRD §4): rating tích lũy 4,58★ nhưng **78% review gần nhất là 1★**, và **D30 chỉ ~4%**. Hai nguyên nhân complaint lớn nhất là (1) paywall cứng, (2) **widget không render đúng trên màn hình xe thật** — cắt chữ trên màn 8", không hiện trên một số xe đời 2026.

Vấn đề kỹ thuật nằm dưới complaint (2) mới là phần khó thật sự và là phần định hình toàn bộ kiến trúc của Carbina: **màn hình CarPlay bị phân mảnh nặng về kích thước và tỉ lệ**, và không có cách nào biết trước người dùng đang lắp xe gì. Bất kỳ layout nào hardcode kích thước đều sẽ hỏng trên một tập xe không đoán trước được — và người dùng gặp lỗi đó sẽ không báo bug, họ sẽ để lại 1★ rồi xin hoàn tiền.

### 1.2 Solution Overview

Carbina là app iOS + CarPlay biến màn hình xe thành một dashboard **tự thích ứng theo ngữ cảnh**, với ba trụ tính năng đã được dữ liệu thị trường xác nhận là nơi người dùng thật sự chi tiền (PRD §6, §7): **âm thanh connect/disconnect/arrive (F1)**, **widget CarPlay tự adapt màn hình (F2)**, và **giọng chào AI cá nhân hóa chạy hoàn toàn on-device (F3)**. Việc học thói quen và sắp xếp lại dashboard (F8) diễn ra ngầm bằng Core ML trên thiết bị — người dùng không phải cấu hình widget bằng tay.

Về mặt kỹ thuật, giải pháp được xây quanh ba cam kết kiến trúc không thương lượng:

1. **Responsive-by-construction trên CarPlay** — mọi layout đọc bounds từ `CPTemplateApplicationScene` tại runtime; không tồn tại hằng số kích thước màn hình xe nào trong code layout. Kèm theo là telemetry `widget_render_ok` / `widget_render_failed` gắn `screen_width`/`screen_height` để phát hiện xe không tương thích trong vòng 24 giờ.
2. **On-device-first** — toàn bộ suy luận ngữ cảnh (giọng chào, sắp xếp dashboard) chạy bằng Core ML + `AVSpeechSynthesizer` trên Apple Neural Engine. Dữ liệu hành vi không rời thiết bị. Điều này vừa là cam kết quyền riêng tư, vừa loại bỏ chi phí biến đổi theo user và loại bỏ backend khỏi đường găng của MVP 1.
3. **Free tier là một cơ chế kỹ thuật, không chỉ là chiêu marketing** — gói Free vô thời hạn (1 widget đầy đủ chức năng + 3 sound + dashboard cơ bản) tồn tại để người dùng **tự xác minh app chạy trên xe của họ trước khi có bất kỳ giao dịch nào**. Về mặt hệ thống, nó buộc lớp entitlement phải được thiết kế ngay từ đầu như một service độc lập, chứ không phải một cờ boolean gắn vào paywall.

Chi tiết định vị sản phẩm và lý do thương mại của các lựa chọn trên: PRD §5 (tầm nhìn), §11 (kiếm tiền).

### 1.3 Business Goals

Ba mục tiêu kinh doanh dưới đây là bản rút gọn của PRD §5 và §12, giữ nguyên con số để tài liệu downstream không phải suy diễn lại.

- **Goal 1 — Chứng minh PMF trong 6 tháng bằng retention, không bằng doanh thu thô**: D1 ≥ 55%, D7 ≥ 40%, D30 ≥ 22% ở tháng 6 (T3: 45% / 30% / 15%). Benchmark category là D1 28,8% · D7 11,5% · D30 4,0% — mục tiêu D30 của Carbina là ~5,5× benchmark, và đây chính là giả thuyết chiến lược đang được đặt cược (rủi ro R-14).
- **Goal 2 — Đạt $6,1K–$9,1K MRR ở tháng 6** với 50.000 installs, 4.000 trial starts, conversion trial→paid 12–18%, blended ARPU $3,38. Ràng buộc đi kèm: **CPI phải < $1,00**, vì cả category vận hành theo arbitrage `RPD − CPI` (PRD §11, R-07).
- **Goal 3 — Giữ rating ≥ 4,6 và Recent 1★ Ratio < 15% ở tháng 6** (T3: 4,5 và < 20%). Đây là mục tiêu chưa app nào trong niche đạt được và bền được; nó phụ thuộc trực tiếp vào hai chỉ số kỹ thuật do tài liệu này sở hữu: **Widget Render Success Rate ≥ 95%** và **crash-free ≥ 99,5%**.

---

## 2. Target Users

Persona đầy đủ (profile, context, pain point, need) thuộc PRD §3. Phần dưới đây giữ đúng ba persona đó và **bổ sung phần PRD không có: hệ quả kỹ thuật của từng persona** — vì đó là thứ ảnh hưởng đến kiến trúc và thứ tự thi công.

### 2.1 Primary User Personas

#### Persona 1: Alex — Tech-Savvy Commuter (persona chính)

- **Demographics**: 32 tuổi, lập trình viên / startup founder, iPhone 14 Pro, lái Tesla hoặc BMW hằng ngày. Mức độ am hiểu công nghệ: cao.
- **Goals**: Lên xe là mọi thứ đã sẵn sàng — nhạc đúng gu, điểm đến đoán đúng, không phải chạm quá 1 lần.
- **Pain Points**: mỗi sáng mất ~30 giây tìm nhạc trong lúc đang lái; CarPlay gốc không học gì; `Hey Siri, play Spotify` thường phải thử 2–3 lần mới ăn.
- **Usage Context**: 40 phút đi làm mỗi ngày + chuyến dài cuối tuần. Xe đời mới, màn hình lớn, tỉ lệ ngang chuẩn.
- **Hệ quả kỹ thuật**: đây là persona xác nhận giá trị của **F3 (giọng chào theo ngữ cảnh)** và **F8 (AI sắp xếp dashboard)**. Yêu cầu độ trễ khắt khe nhất đến từ đây: từ `carplay_connected` đến khi phát giọng chào ≤ 2s, và dashboard load < 500ms — nghĩa là mô hình Core ML phải được nạp sẵn (warm) chứ không nạp lười lúc scene active.

#### Persona 2: Jordan — Busy Professional (persona thứ cấp)

- **Demographics**: 38 tuổi, sales executive, iPhone 13, xe Audi đời 2022+. Mức độ am hiểu công nghệ: trung bình.
- **Goals**: Truy cập nhanh liên hệ công việc và navigation mà không cần nói ra tiếng, vì thường đang trong conference call khi lái.
- **Pain Points**: không dùng được voice control do đang họp; cần shortcut liên hệ nhanh; muốn ở lại hệ sinh thái iPhone.
- **Usage Context**: lái 10+ giờ/tuần, phần lớn là tuyến đường lạ.
- **Hệ quả kỹ thuật**: persona này là lý do **mọi tính năng cốt lõi phải dùng được hoàn toàn bằng chạm, không phụ thuộc voice input**, và là lý do **F13 (Contacts Shortcuts) được dời sang MVP 2** chứ không bị loại — nó có nhu cầu thật nhưng không nằm trong ba trụ PMF đã kiểm chứng. Xe Audi cũng nằm trong nhóm đã ghi nhận lỗi render ở đối thủ ⇒ bắt buộc có trong test matrix R-11.

#### Persona 3: Sam — Car Enthusiast (persona thứ ba)

- **Demographics**: 28 tuổi, lái xe như sở thích, iPhone 15 Pro Max, xe Porsche / sports car.
- **Goals**: Dashboard tùy biến được theo ý mình, có metric chuyến đi, nhớ playlist theo từng cung đường.
- **Pain Points**: CarPlay gốc không cho custom widget layout; muốn trip stats mà không có.
- **Usage Context**: chuyến dài cuối tuần, nghe podcast và nhạc, sẵn sàng bỏ thời gian cấu hình.
- **Hệ quả kỹ thuật**: persona này là **đối tượng chính của gói Lifetime $49,99** và của **Trình Tạo Widget (màn 7)** với ảnh xe / ảnh cá nhân. Nhu cầu trip history & stats của Sam nằm ở MVP 3 vì cần lớp lưu trữ lịch sử — đó là lý do lược đồ dữ liệu local phải chừa sẵn bảng chuyến đi ngay từ MVP 1 dù chưa dùng đến.

> **Thứ tự ưu tiên khi ba persona xung đột**: Alex > Jordan > Sam. Alex đại diện cho ba trụ PMF; Jordan mở rộng thị trường ở MVP 2; Sam là nguồn doanh thu Lifetime nhưng số lượng nhỏ và nhu cầu nằm ở MVP 3.

### 2.2 Secondary Users

Nhóm này không phải người lái, nhưng có tương tác trực tiếp với hệ thống và **cần được cấp giao diện hoặc kênh dữ liệu riêng** — nếu bỏ sót, các cơ chế giảm thiểu rủi ro của PRD sẽ không có nơi để chạy.

| Người dùng phụ | Tương tác với hệ thống | Bề mặt cần có |
|---|---|---|
| **PM / Product Owner** | Theo dõi 5 dashboard analytics (PRD §12), phát hiện sự cố tương thích xe trong 24h | Firebase dashboard + cảnh báo tự động khi Widget Render Success Rate < 90% (F10) |
| **QA** | Sở hữu test matrix ≥ 4 kích thước màn hình CarPlay + 1 xe thật mỗi nhóm (R-11) | Màn **Chẩn Đoán Tương Thích** (màn 13) hiển thị kích thước scene nhận được và trạng thái render |
| **Growth / UA** | Theo dõi CPI, RPD, phân bổ kênh | Event funnel `paywall_shown` → `price_confirmed` → `trial_started` → `trial_converted` |
| **Creative Reviewer** | Phê duyệt mọi ad creative; bắt buộc đã tự chạy feature trên xe thật (R-10) | Build production truy cập được + checklist phê duyệt (quy trình, không phải phần mềm) |
| **Support** | Xử lý báo cáo lỗi render và yêu cầu hoàn tiền | Báo cáo do người dùng gửi từ màn 13, kèm `screen_width`/`screen_height`/`failure_reason` |
| **Người dùng cuối chưa trả tiền (gói Free)** | Là một hạng người dùng riêng về mặt hệ thống, không phải trạng thái "chưa mua" | Lớp entitlement độc lập — xem §3.3, Quyết định 5 |

> **Không có vai trò admin/moderator trong MVP 1.** Không có nội dung do người dùng tạo được chia sẻ công khai, không có backend quản trị. Điều này là chủ ý và giữ backend nằm ngoài đường găng MVP 1.

---

## 3. High-Level Architecture

### 3.1 Technology Stack

#### Frontend (iPhone app)

| Yếu tố | Lựa chọn | Ghi chú ràng buộc |
|---|---|---|
| **Platform** | iOS (MVP 1). Android Auto ở MVP 2 (tháng 12/2026) | PRD §9 |
| **Minimum Version** | **iOS 16.4+** cho app iPhone | Ngưỡng Neural Engine + `NavigationStack` |
| **Ngưỡng cho tính năng CarPlay** | **iOS 17.4+** cho widget CarPlay (WidgetKit trên CarPlay); iOS 17.1+ cho CarPlay SDK | Chênh lệch giữa hai ngưỡng này được xử lý bằng graceful degradation — xem §3.3 Quyết định 1 |
| **Thiết bị** | iPhone 12 trở lên (có Apple Neural Engine); iPad Air 5 / iPad Pro là tùy chọn | On-device ML là bắt buộc, không có đường lui cloud |
| **UI Framework** | SwiftUI (app iPhone) + **WidgetKit** (widget CarPlay) + **CarPlay framework** (`CPTemplate*`, dashboard) | Ba runtime khác nhau, cùng một lớp domain — xem §3.3 Quyết định 2 |
| **Architecture Pattern** | **MVVM + Coordinator** | Coordinator cần thiết vì có hai cây điều hướng độc lập (iPhone và CarPlay) |
| **State Management** | `@State` / `@StateObject` cục bộ; `@EnvironmentObject` cho state dùng chung; `UserDefaults` + App Group cho cài đặt bền vững | App Group là bắt buộc để widget extension đọc được cấu hình |
| **Navigation** | `NavigationStack` (iOS 16+) trên iPhone; `CPInterfaceController` template stack trên CarPlay | Hai stack không chia sẻ trạng thái điều hướng |
| **Concurrency** | Swift Concurrency (`async/await`, `actor`) | `actor` dùng cho lớp truy cập ML và lớp audio để tránh tranh chấp |

#### ML / Audio (on-device, không có phần cloud)

| Yếu tố | Lựa chọn | Ghi chú |
|---|---|---|
| **ML Framework** | **Core ML + Create ML** | Chốt ở PRD §14. Không dùng scikit-learn / PyTorch / TensorFlow trực tiếp trên thiết bị |
| **Suy luận** | Apple Neural Engine, chạy hoàn toàn on-device | Không có lệnh gọi mạng nào trong đường xử lý ngữ cảnh |
| **Text-to-Speech** | `AVSpeechSynthesizer` | Chốt ở PRD §14; loại bỏ chi phí biến đổi theo user |
| **Audio session** | `AVAudioSession` với ducking (`.duckOthers`) và định tuyến ra loa xe | Trực tiếp phục vụ AC của F1 |
| **Ngữ cảnh đầu vào** | `CoreLocation` (tuyến quen), `EventKit` (lịch), giờ trong ngày, thời tiết | Mọi quyền đều bỏ qua được; app vẫn chạy ở mức cơ bản khi bị từ chối |

#### Backend và dịch vụ

| Yếu tố | Lựa chọn | Phạm vi |
|---|---|---|
| **Backend** | **Không có backend riêng ở MVP 1.** Chỉ Firebase (managed) | Backend riêng chỉ xuất hiện ở MVP 3 khi có cloud sync |
| **Analytics** | Firebase Analytics — 28 event ở PRD §12 | `widget_render_failed` và `refund_detected` **bắt buộc có từ ngày launch** |
| **Crash Reporting** | Firebase Crashlytics (MVP 1 chỉ Firebase, không thêm Sentry) | Chốt ở PRD §14 |
| **Webhook hoàn tiền** | App Store Server Notifications V2 → hàm nhận `refund_detected` | Phần backend duy nhất của MVP 1 |
| **Thanh toán** | **StoreKit 2** — subscription (monthly/yearly) + non-consumable (lifetime) | Cần Small Business Program 15% trước submission |
| **Authentication** | **Không có ở MVP 1.** Email login xuất hiện ở MVP 3 cùng cloud sync | Bắt tạo tài khoản sẽ làm giảm conversion (PRD §14) |
| **Database** | **SQLite cục bộ** (cấu hình, lịch sử ngữ cảnh, thư viện xe); Firestore chỉ ở MVP 3 | Lược đồ chừa sẵn bảng chuyến đi cho MVP 3 |
| **Storage** | Keychain cho token; file system cho model và asset âm thanh; App Group container chia sẻ với widget extension | Không có API key dạng plain-text trong bundle |

#### Third-party

| Dịch vụ | Mục đích | Giai đoạn | Rủi ro phụ thuộc |
|---|---|---|---|
| **Firebase** (Analytics, Crashlytics) | Telemetry và phát hiện sớm R-11/R-12 | MVP 1 | Thấp; free tier đủ, ~$100/tháng nếu volume cao |
| **Spotify iOS SDK** | Đọc top track / playlist cho gợi ý nhạc | MVP 1 (tùy chọn, có thể bỏ qua) | **Cần legal review terms cho commercial app** — chưa xong, xem §7.1 |
| **MapKit / Apple Maps** | Navigation, truy vấn địa điểm | MVP 1 | Thấp; native, không cần SDK ngoài. Google Maps **không** có ở MVP 1 |
| **Contacts framework** | Shortcut liên hệ | MVP 2 | Thấp |
| **Core Location** | Học tuyến đường quen | MVP 1 | Thấp; on-device |

### 3.2 System Architecture Diagram

```
┌──────────────────────── THIẾT BỊ CỦA NGƯỜI DÙNG (không có gì rời máy) ────────────────────────┐
│                                                                                               │
│  ┌─────────────── iPhone App (SwiftUI) ──────────────┐  ┌──── CarPlay Runtime ─────────────┐  │
│  │  Presentation — Views + Coordinator               │  │  CarPlay Scene (CPTemplate…)      │  │
│  │  Onboarding · Home · SoundLibrary · WidgetBuilder │  │  Dashboard · Free-state · Fallback│  │
│  │  VoiceGreeting · Paywall · Settings · Diagnostics │  │  ── đọc bounds tại RUNTIME ──     │  │
│  └───────────────────────┬───────────────────────────┘  └──────────┬───────────────────────┘  │
│                          │                                          │                          │
│  ┌───────────────────────▼──────────────────────────────────────────▼───────────────────────┐  │
│  │                       ViewModels (@Published, một VM cho mỗi màn)                          │  │
│  └───────────────────────┬──────────────────────────────────────────────────────────────────┘  │
│                          │                                                                      │
│  ┌───────────────────────▼──────────────── Core Services ─────────────────────────────────┐    │
│  │  CarPlaySceneService │ WidgetRenderService │ AudioSessionService │ VoiceGreetingService  │    │
│  │  ContextEngine (Core ML) │ EntitlementService │ AnalyticsService │ VehicleCatalogService │    │
│  └───────────────────────┬──────────────────────────────────────────────────────────────────┘   │
│                          │                                                                      │
│  ┌───────────────────────▼──────────── Data / Models ────────────────────────────────────┐      │
│  │  SQLite (cấu hình, lịch sử ngữ cảnh, thư viện xe) · App Group container · Keychain     │      │
│  │  Core ML model bundle · Thư viện asset âm thanh                                        │      │
│  └───────────────────────────────────────────────────────────────────────────────────────┘      │
│                          │                                                                      │
│  ┌───────────────────────▼──── Widget Extension (WidgetKit, tiến trình riêng) ───────────┐      │
│  │  Đọc cấu hình từ App Group · Layout tính theo container size · KHÔNG gọi mạng          │      │
│  └───────────────────────────────────────────────────────────────────────────────────────┘      │
└───────────────────────────────────┬───────────────────────────────────────────────────────────┘
                                    │  chỉ event ẩn danh + giao dịch (không có PII, không có dữ liệu hành vi)
                    ┌───────────────▼───────────────┐   ┌──────────────────────────────┐
                    │  Firebase Analytics/Crashlytics│   │  App Store Connect / StoreKit│
                    │  28 event · cảnh báo R-11      │   │  Server Notification V2      │
                    └───────────────────────────────┘   │  → refund_detected           │
                                                        └──────────────────────────────┘
        ┌── MVP 3 (chưa xây) ──────────────────────────────────────────────────────────┐
        │  Auth (email) · Firestore cloud sync · Trip history · Stats — optional, opt-in │
        └───────────────────────────────────────────────────────────────────────────────┘
```

**Ba điều cần đọc ra từ sơ đồ này:**

1. **Ranh giới dữ liệu nằm ở đáy khối thiết bị.** Mọi thứ liên quan đến hành vi người dùng (nhạc, tuyến đường, lịch, ngữ cảnh) nằm hoàn toàn phía trên đường kẻ đó. Chỉ event ẩn danh và giao dịch đi xuống dưới. Đây là điều kiện để giữ cam kết ở PRD §9 (Quyền Riêng Tư).
2. **Widget extension là một tiến trình riêng.** Nó không dùng chung bộ nhớ với app, nên **giao tiếp duy nhất là qua App Group container**. Hệ quả: mọi cấu hình widget phải được ghi xuống App Group ngay lúc người dùng thay đổi, không phải lúc app đóng.
3. **CarPlay Scene và iPhone Views là hai cây điều hướng ngang hàng**, cùng chia sẻ tầng ViewModel/Service bên dưới. Không cái nào là "con" của cái nào — CarPlay scene có thể active khi app iPhone đang background.

### 3.3 Key Architectural Decisions

#### Quyết định 1 — Hai ngưỡng iOS, xử lý bằng graceful degradation

**Bối cảnh**: PRD §9 ghi min iOS 16.4+ (Neural Engine) nhưng cũng ghi CarPlay SDK 17.1+ và WidgetKit-trên-CarPlay 17.4+. Đây là hai ngưỡng khác nhau, và PRD không nói cách hòa giải.
**Quyết định**: deployment target của app là **iOS 16.4**; tính năng widget CarPlay được bọc trong `if #available(iOS 17.4, *)`. Người dùng iOS 16.4–17.3 vẫn dùng được sound (F1), giọng chào (F3), thư viện xe (F5), dashboard cơ bản; phần widget hiển thị thông báo yêu cầu nâng cấp iOS thay vì bị crash hoặc màn trắng.
**Đánh đổi**: thêm nhánh điều kiện và thêm một trạng thái phải test. Chấp nhận, vì đặt min lên 17.4 sẽ cắt mất một phần đáng kể thị trường ngay ở giai đoạn cần install nhất, còn để `@available` sai sẽ tạo đúng loại crash mà R-11 đang muốn tránh.

#### Quyết định 2 — Ba runtime, một lớp domain duy nhất

**Bối cảnh**: app chạy trên ba môi trường tách biệt — app iPhone, CarPlay scene, widget extension.
**Quyết định**: toàn bộ logic nghiệp vụ nằm trong **Core Services** dùng chung, biên dịch vào cả app target lẫn widget target. Mỗi runtime chỉ sở hữu tầng View của riêng nó. Không có logic nào bị nhân bản giữa CarPlay và iPhone.
**Đánh đổi**: Core Services phải giữ được tính thuần khiết (không phụ thuộc UIKit/SwiftUI, không giả định vòng đời app) để widget extension nạp được mà không kéo theo cả app. Đây là ràng buộc thiết kế đáng giá vì nó cũng làm cho lớp domain test được bằng property-based test.

#### Quyết định 3 — Responsive-by-construction, cấm hằng số kích thước

**Bối cảnh**: R-11 (Fragmentation màn hình CarPlay) là rủi ro `High/High` và là complaint kỹ thuật số 1 của đối thủ.
**Quyết định**: `WidgetRenderService` nhận kích thước từ `CPTemplateApplicationScene` bounds (hoặc container size của WidgetKit) và **tính toàn bộ layout từ đó**. Không tồn tại hằng số kích thước màn hình xe trong codebase. Mọi đường render đều phát `widget_render_ok` hoặc `widget_render_failed` kèm `screen_width`/`screen_height`.
**Cách cưỡng chế**: đây là điều kiện kiểm tra tự động ở giai đoạn thực thi, không phải quy ước mềm — bất kỳ giá trị point cứng nào trong code layout CarPlay đều là lỗi build-review. Cộng với màn Chẩn Đoán (màn 13) và fallback CarPlay (màn 18), không có đường nào dẫn tới màn hình trắng.
**Đánh đổi**: layout khó viết hơn và cần test matrix ≥ 4 kích thước + 1 xe thật mỗi nhóm. Chi phí này được chấp nhận vì nó là điều kiện cần của KPI Widget Render Success Rate ≥ 95%.

#### Quyết định 4 — On-device-first, không có đường lui cloud

**Bối cảnh**: giọng chào và sắp xếp dashboard có thể làm bằng cloud LLM/TTS, dễ hơn và chất lượng cao hơn.
**Quyết định**: chạy hoàn toàn on-device bằng Core ML + `AVSpeechSynthesizer`, **không có fallback cloud**.
**Lý do**: (a) giữ đúng cam kết "dữ liệu không rời thiết bị" — đây là điểm khác biệt so với niche; (b) không có chi phí biến đổi theo user, quan trọng khi blended ARPU chỉ $3,38; (c) không có độ trễ mạng, giúp đạt ngưỡng ≤ 2s từ connect đến phát; (d) app vẫn chạy đủ chức năng khi mất sóng — tình huống phổ biến trong hầm gửi xe.
**Đánh đổi**: chất lượng câu chào bị giới hạn bởi mô hình on-device và phải chấp nhận rằng nó là chọn-mẫu-theo-ngữ-cảnh chứ không phải sinh ngôn ngữ tự do. Yêu cầu tối thiểu (PRD §7 F3): ≥ 4 biến thể ngữ cảnh, không lặp câu y hệt hai lần liên tiếp. Rủi ro "AI không đủ tốt" được theo dõi ở R-01.

#### Quyết định 5 — Entitlement là service độc lập, không phải cờ của paywall

**Bối cảnh**: gói Free vô thời hạn là điểm khác biệt hóa số 1 và có cấu hình cụ thể (1 widget đầy đủ chức năng + 3 sound + dashboard cơ bản). Đây là một **hạng người dùng thường trực**, không phải trạng thái tạm trước khi mua.
**Quyết định**: `EntitlementService` là nguồn chân lý duy nhất cho câu hỏi "người dùng này được dùng gì", tách khỏi `PaywallViewModel` và khỏi StoreKit. Mọi feature gate đều hỏi service này. Ràng buộc **paywall không được hiển thị ở lần mở app đầu tiên** được cưỡng chế trong service (kiểm `days_since_install > 0` hoặc trigger do người dùng chủ động), không phải bằng điều kiện rải rác trong View.
**Đánh đổi**: thêm một lớp gián tiếp cho một app nhỏ. Chấp nhận, vì cấu hình free tier còn đang mở ở PRD §14 (có thể đổi sau A/B test) và vì mô hình Coin ở MVP 2 sẽ thêm một loại entitlement nữa — nếu logic này nằm rải trong View thì mỗi lần đổi là một lần sửa toàn bộ màn hình.

#### Quyết định 6 — Không có backend riêng ở MVP 1

**Bối cảnh**: có thể xây API cho analytics và cấu hình từ xa ngay từ đầu.
**Quyết định**: MVP 1 chỉ dùng Firebase (managed) + một endpoint nhận App Store Server Notification cho `refund_detected`. Không có server riêng, không có tài khoản người dùng.
**Đánh đổi**: không thể đổi cấu hình từ xa (ví dụ tắt một feature lỗi mà không cần update app) — chấp nhận ở MVP 1 vì nó giữ backend khỏi đường găng 12 tuần và loại bỏ một lớp vận hành khỏi giai đoạn cần tốc độ nhất. Từ MVP 2 nên bổ sung remote config để có thể tắt nhanh feature khi phát hiện sự cố tương thích.

#### Quyết định 7 — Cấu trúc thư mục theo `ios-architecture`

Mỗi tính năng là một thư mục riêng dưới `Features/` với bốn thư mục con `Views/`, `ViewModels/`, `Models/`, `Services/`; code dùng chung ở `Core/`; component tái sử dụng ở `shared/Components/<Type>/` (Buttons, Cards, Inputs, Modals, Feedback). Chiều phụ thuộc một chiều `View → ViewModel → Service → Model`. Cấu trúc dự kiến:

```
Carbina/
├── App/                          CarbinaApp.swift, AppDelegate (CarPlay scene delegate)
├── Core/
│   ├── CarPlay/                  CarPlaySceneService, WidgetRenderService, layout engine
│   ├── ML/                       ContextEngine, model loader
│   ├── Audio/                    AudioSessionService, VoiceGreetingService
│   ├── Entitlement/              EntitlementService, StoreKit adapter
│   ├── Analytics/                AnalyticsService (28 event), event schema
│   ├── Persistence/              SQLite layer, App Group bridge
│   ├── Extensions/  Utilities/
├── Features/
│   ├── Onboarding/               (màn 1–4)
│   ├── Home/                     (màn 5)
│   ├── SoundLibrary/             (màn 6)
│   ├── WidgetBuilder/            (màn 7)
│   ├── VoiceGreeting/            (màn 8)
│   ├── Paywall/                  (màn 9, 10, 12)
│   ├── Settings/                 (màn 11)
│   ├── Diagnostics/              (màn 13)
│   └── CarPlayDashboard/         (màn 15, 17, 18)
├── CarbinaWidget/                Widget extension target (màn 16)
├── shared/Components/  shared/Styles/  shared/Modifiers/
├── Resources/                    Assets, Localizable (EN/ES/PT-BR), âm thanh
└── Tests/
```

Số màn hình trong ngoặc tham chiếu **PRD §10**. Layout chi tiết của từng màn thuộc `Wireframes.md` (Step 5), không phải tài liệu này.

---

## 4. Core Features Overview

Acceptance criteria đầy đủ của F1–F13 thuộc **PRD §7** và sẽ được chuyển thành AC có ID ở `Use_Cases.md` / `Functional_Requirements.md`. Bảng dưới đây bổ sung thứ **PRD không có**: mỗi tính năng thuộc module kiến trúc nào, phụ thuộc kỹ thuật gì, và độ khó thực thi.

### 4.1 Must-Have Features (MVP)

| # | Tính năng | Module | Phụ thuộc kỹ thuật chính | Độ khó | Ràng buộc đo được |
|---|---|---|---|---|---|
| 1 | **F1 — Âm thanh Connect / Disconnect / Arrive** | `Core/Audio` + `Features/SoundLibrary` | `AVAudioSession` ducking + định tuyến ra loa xe; bắt sự kiện tắt máy | Trung bình-Cao | Phát trong ≤ 1,5s sau `carplay_connected`; duck nhạc xuống 20% rồi phục hồi; ≥ 12 preset, 3 preset ở gói Free |
| 2 | **F2 — Widget CarPlay tự adapt màn hình** | `Core/CarPlay` + `CarbinaWidget` | `CPTemplateApplicationScene` bounds; App Group; WidgetKit iOS 17.4+ | **Cao — rủi ro cao nhất dự án** | Không nội dung nào bị cắt ở mọi kích thước trong test matrix; touch target ≥ 44pt; Render Success ≥ 90% (T3) / 95% (T6) |
| 3 | **F3 — Giọng chào AI cá nhân hóa** | `Core/ML` + `Core/Audio` + `Features/VoiceGreeting` | Core ML chọn ngữ cảnh; `AVSpeechSynthesizer`; `EventKit` + `CoreLocation` | Cao | Connect → phát ≤ 2s; ≥ 4 biến thể ngữ cảnh; không lặp câu 2 lần liên tiếp; không gọi cloud; tắt được hoàn toàn |
| 4 | **F4 — Gói Free vô thời hạn** | `Core/Entitlement` | StoreKit 2; kiểm `days_since_install` | Trung bình | 1 widget đầy đủ chức năng + 3 sound + dashboard cơ bản; **không paywall ở lần mở app đầu tiên**; không quảng cáo |
| 5 | **F5 — Thư viện xe (make/model/year)** | `Core/Persistence` + `Features/Onboarding` | Dataset đóng gói sẵn + asset ảnh xe độ phân giải cao | Thấp-Trung bình | ≥ 40 hãng, ≥ 400 model; có ô "không tìm thấy xe của tôi"; ảnh sắc nét trên màn hình xe |
| 6 | **F6 — Onboarding ≤ 5 bước** | `Features/Onboarding` | Điều phối quyền (Location, Calendar) | Thấp | ≤ 5 bước; **không paywall trong onboarding**; skip được mọi quyền; completion rate ≥ 70% |
| 7 | **F7 — Paywall & Trial 7 ngày** | `Features/Paywall` + `Core/Entitlement` | StoreKit 2 subscription + non-consumable | Trung bình | $4,99/tháng · $29,99/năm · $49,99 lifetime; **không bán weekly**; hiển thị giá cuối bằng tiền tệ địa phương |
| 8 | **F8 — AI sắp xếp dashboard** | `Core/ML` + `Features/CarPlayDashboard` | Core ML on-device; lịch sử ngữ cảnh trong SQLite | Cao | Học on-device; tự xếp lại thẻ; **không bắt người dùng tự tạo widget**; tap-through ≥ 30% |
| 9 | **F9 — Localize EN / ES / PT-BR** | `Resources` (xuyên suốt) | Localizable + nội dung giọng chào theo từng ngôn ngữ | Trung bình | 3 ngôn ngữ đầy đủ, **gồm cả nội dung giọng chào**, không chỉ UI |
| 10 | **F10 — Analytics & Telemetry** | `Core/Analytics` | Firebase Analytics; webhook App Store | Trung bình | 28 event; **`widget_render_failed` + `refund_detected` có từ ngày launch**; cảnh báo tự động khi Render Success < 90%; không gửi PII |
| 11 | **F11 — Crash Reporting** (P1) | `Core/Analytics` | Firebase Crashlytics + upload symbol | Thấp | ≥ 99,2% crash-free (T3), ≥ 99,5% (T6) |
| 12 | **F12 — Giám sát sentiment review** (P1) | Ngoài app (job định kỳ) | Customer Reviews RSS | Thấp | Job hằng tuần đọc 50 review gần nhất; cảnh báo khi Recent 1★ Ratio > 20% |

> **Thứ tự trong bảng theo mức PMF đã kiểm chứng, không theo mức dễ làm** (PRD §6). F1 và F2 là hai thứ người dùng thật sự trả tiền; F3 là điểm khác biệt hóa. Nếu phải cắt phạm vi, cắt từ dưới lên — nhưng **F4 và F10 không được cắt** vì chúng là hai cơ chế giảm thiểu rủi ro (R-11, R-12), không phải tính năng thông thường.

**Ba capability tối thiểu để tuyên bố MVP 1 thành công** (PRD §6): Widget Render Success ≥ 90% · Recent 1★ Ratio < 20% · D1 ≥ 45% và D7 ≥ 30%.

### 4.2 Should-Have Features (Post-MVP)

| # | Tính năng | Giai đoạn | Vì sao chưa vào MVP 1 |
|---|---|---|---|
| 1 | **F13 — Contacts Shortcuts** (5 favorites, gọi 1 chạm) | MVP 2 — tháng 12/2026 | Có nhu cầu thật (persona Jordan) nhưng nằm ngoài ba trụ PMF đã kiểm chứng |
| 2 | **Android Auto** | MVP 2 | Cần port toàn bộ tầng View; giữ MVP 1 ở iOS để rút ngắn từ 16+ tuần xuống 8–12 tuần |
| 3 | **Widget tương tác (hai chiều)** | MVP 2 | MVP 1 chỉ hiển thị. Giải quyết complaint "Click on orders and nothing happens" của đối thủ |
| 4 | **Settings mở rộng** (dark mode, cỡ chữ) | MVP 2 | Không chặn PMF |
| 5 | **Coin (consumable IAP)** | MVP 2 | Còn là câu hỏi mở ở PRD §14 (Coin hay Lifetime hay cả hai) |
| 6 | **Remote config** (tắt nhanh feature lỗi) | MVP 2 | Hệ quả của Quyết định 6 ở §3.3 — nợ kỹ thuật đã biết và đã lên lịch trả |
| 7 | **Localize DE / FR / IT** | MVP 2 | LATAM (ES, PT-BR) được ưu tiên trước vì chiếm 14,6% user base đối thủ |
| 8 | **Cloud sync + tài khoản** (optional, opt-in) | MVP 3 — tháng 3/2027 | Cần backend thật; bắt tạo tài khoản làm giảm conversion |
| 9 | **Trip history & Stats** | MVP 3 | Cần lớp lưu trữ lịch sử — lược đồ SQLite đã chừa sẵn từ MVP 1 |
| 10 | **Thư viện xe mở rộng (trim, color)** | MVP 3 | Chỉ là mở rộng dữ liệu, không đổi kiến trúc |

### 4.3 Future Enhancements

- **AI nhận biết lịch nâng cao** (MVP 4 — tháng 6/2027): gợi ý điều hướng đến cuộc họp kế tiếp khi vị trí hiện tại không khớp.
- **Voice control đầu vào** (MVP 4): MVP 1 hoàn toàn dựa vào chạm. Lưu ý phân biệt — **giọng chào AI là đầu ra và đã có trong MVP 1**; thứ bị hoãn là đầu vào bằng giọng nói.
- **Music source detection** (MVP 4): tự nhận nguồn nhạc đang phát thay vì chỉ tích hợp Spotify.
- **AI Driving Coach**: **đang là giả thuyết chưa validate** (PRD §14). Số liệu category cho thấy phiên trung bình ~23 giây, trái với giả định người dùng xem lại điểm lái xe sau mỗi chuyến. Phải prototype và test hành vi trước khi đầu tư.
- **Nằm ngoài phạm vi dài hạn** (PRD §6): tích hợp OBD / Tesla API, tối ưu giao thông thời gian thực.

---

## 5. Development Roadmap

Timeline gốc và các mốc thuộc **PRD §15**. Phần dưới đây giữ nguyên khung thời gian đó và bổ sung **thứ tự thi công kỹ thuật** — thứ PRD không quy định. Kế hoạch phase chi tiết theo nhóm FR sẽ do `Project_Implementation_Roadmap.md` (Step 7) sở hữu.

### Phase 1: Foundation (Tuần 1–2 · 15/08 – 29/08/2026)

- Dựng project theo cấu trúc ở §3.3 Quyết định 7; thiết lập App Group giữa app và widget extension.
- **Prototype layout engine CarPlay trước mọi thứ khác** — dựng khung đọc `CPTemplateApplicationScene` bounds và render trên ≥ 4 kích thước giả lập. Đây là rủi ro cao nhất nên phải chạm vào tuần 1.
- Prototype mô hình Core ML chọn ngữ cảnh (R-01 yêu cầu làm sớm tuần 1–2).
- Dựng `AnalyticsService` với đủ 28 event schema — telemetry phải có trước tính năng, không phải sau.
- Chốt test matrix ≥ 4 kích thước + 1 xe thật mỗi nhóm (bắt buộc trước khi code widget, R-11).
- **Song song, không phải việc kỹ thuật**: gửi email Apple Developer xin guidance về CarPlay widget (R-02/R-08, cần làm trong tuần 1); luật sư bắt đầu tra trademark "Carbina".

### Phase 2: Core Features (Tuần 3–6 · 29/08 – 26/09/2026)

- **Tuần 3–4**: F2 (widget adapt) hoàn chỉnh + F1 (âm thanh có ducking) + F5 (thư viện xe). Đây là hai tính năng có PMF cao nhất, làm trước.
- **Tuần 4–5**: F3 (giọng chào on-device) + F8 (AI sắp xếp dashboard) — cả hai dùng chung `ContextEngine`.
- **Tuần 5–6**: F4 (`EntitlementService` + gói Free) + F7 (paywall, StoreKit 2, trial) + F6 (onboarding) + màn 13 (Chẩn Đoán) + màn 18 (fallback CarPlay).
- **Tuần 6**: F9 (localize EN/ES/PT-BR, gồm nội dung giọng chào) + F10 hoàn thiện.
- Cổng ra khỏi Phase 2: chạy được end-to-end trên CarPlay simulator ở đủ 4 kích thước, và trên ít nhất 1 xe thật.

### Phase 3: Polish & Launch (Tuần 7–12 · 26/09 – 07/11/2026)

- **Tuần 7–8**: QA theo test matrix + TestFlight beta (nội bộ và một nhóm ngoài giới hạn). Ngưỡng chặn phát hành: crash-free ≥ 99,0% trên TestFlight.
- **Tuần 9–10**: đăng ký Small Business Program (15%); hoàn thiện metadata theo ràng buộc R-08 (tên/subtitle **không** chứa `Connect`, `Sync`, `Link`, `Remote`, `Auto Sync`, `Cast`, `Mirror`); privacy policy + review terms Spotify xong; chuẩn bị creative theo quy trình R-10 (chỉ quay feature thật trên build production); nộp App Store.
- **Tuần 11–12**: App review + chuẩn bị launch + theo dõi hậu launch. Tuần đầu sau launch: theo dõi `widget_render_failed` hằng ngày, không phải hằng tuần.

### Phase 4: Post-Launch và các MVP tiếp theo

- **Tháng 12/2026 — MVP 2**: Android Auto · F13 Contacts · widget tương tác · Settings mở rộng · remote config · Coin IAP · DE/FR/IT.
- **Tháng 3/2027 — MVP 3**: cloud sync opt-in · trip history · stats · thư viện xe mở rộng (trim/color).
- **Tháng 6/2027 — MVP 4**: AI nhận biết lịch nâng cao · voice input · music source detection.

> **Điểm quyết định chiến lược ở tháng 3 sau launch**: đo D30 của cohort tháng đầu so với benchmark category 4%. **Nếu D30 < 8%, giả thuyết retention của Carbina sai** và phải cân nhắc lại toàn bộ mô hình kiếm tiền (R-14). Điểm này phải nằm trong lịch, không phải là việc "để ý sau".

---

## 6. Success Metrics

### 6.1 Technical Metrics

| Chỉ số | Mục tiêu | Đo bằng | Ngưỡng chặn |
|---|---|---|---|
| **Widget Render Success Rate** | ≥ 90% (T3) · **≥ 95% (T6)** | `widget_render_ok` / `carplay_connected` | **< 90% → cảnh báo tự động trong 24h.** Đây là chỉ số kỹ thuật quan trọng nhất của dự án |
| Cold launch | < 2,0s (chuẩn iPhone 12) | Firebase Performance | > 3,0s chặn phát hành |
| Dashboard load | < 500ms sau khi app vào foreground | Firebase Performance | — |
| Thời gian suy luận gợi ý | < 1,0s (Core ML on-device) | Trace tùy chỉnh | — |
| Độ trễ giọng chào | **≤ 2,0s** từ `carplay_connected` đến khi phát | `voice_greeting_played` timestamp | > 3s coi là lỗi chức năng của F3 |
| Độ trễ phát âm thanh connect | **≤ 1,5s** sau `carplay_connected` | `sound_played` | — |
| Bộ nhớ | < 150MB toàn bộ framework | Xcode Instruments | Widget extension có ngưỡng riêng chặt hơn nhiều — phải giữ tối thiểu |
| Frame rate | 60 FPS khi cuộn trên CarPlay | Instruments | < 45 FPS chặn phát hành |
| Timeout Spotify API | < 2,0s rồi chuyển sang nguồn cục bộ | `error_occurred` | — |
| **Crash-Free Sessions** | ≥ 99,2% (T3) · ≥ 99,5% (T6) | Crashlytics | **< 99,0% trên TestFlight chặn phát hành** |
| Error rate | < 0,5% (T3) · < 0,3% (T6) | `error_occurred` / session | — |
| Test coverage | ≥ 80% cho `Core/` (logic domain) | Xcode coverage | Tầng View không tính vào con số này |
| Cảnh báo Xcode | 0 | Build log | Bắt buộc trước submission |

**Ba ràng buộc kỹ thuật riêng của dự án này, không có trong app iOS thông thường:**

1. Test matrix CarPlay **≥ 4 kích thước màn hình + 1 xe thật cho mỗi nhóm** trước khi widget được coi là xong.
2. **Không có hằng số kích thước màn hình xe** trong code layout — kiểm tra ở review, không phải ở runtime.
3. `widget_render_failed` và `refund_detected` **phải hoạt động từ build đầu tiên lên TestFlight**, không phải bổ sung trước launch.

### 6.2 Business Metrics

Định nghĩa KPI đầy đủ và cách tính thuộc **PRD §12**. Bảng dưới là mục tiêu đã chốt, đưa vào đây để `Project_Implementation_Roadmap.md` không phải suy diễn lại.

| Chỉ số | Mục tiêu T3 | Mục tiêu T6 | Vì sao chỉ số này tồn tại |
|---|---|---|---|
| Installs | 10.000 | 50.000 | Đầu phễu |
| Trial starts | 2.000 | 4.000 | — |
| DAU | 2.000 | 12.500 | — |
| Session length | 8–12 phút | 10–14 phút | Benchmark category chỉ ~1 phút |
| **D1 Retention** | ≥ 45% | ≥ 55% | Chỉ số quan trọng nhất 2 tuần đầu — người dùng của đối thủ rời trong 5 phút đến 1 ngày |
| **D7 Retention** | 30% | 40% | Tín hiệu PMF |
| **D30 Retention** | 15% | 22% | Cơ sở LTV. Benchmark category: 4% |
| Trial → Paid | 10–14% | 12–18% | — |
| MRR | $1,2K–$1,8K | **$6,1K–$9,1K** | Tính theo blended ARPU $3,38 |
| Lifetime buyers | 50–100 | 300–500 tích lũy | — |
| **Recent 1★ Ratio** | < 20% | **< 15%** | Rating tích lũy che lấp sentiment thật (đối thủ: 4,58★ nhưng 78% review gần nhất 1★) |
| **Refund Rate** | < 7% | **< 5%** | Tín hiệu kỳ vọng lệch thực tế; hệ quả trực tiếp của R-12 |
| App Store rating | 4,5/5 (≥ 200 review) | 4,6/5 | Chưa app nào trong niche giữ được mức này |
| NPS | 35+ | 40+ | — |
| AI tap-through | ≥ 30% | ≥ 30% | Tín hiệu chất lượng AI (F8) |
| **CPI** | < $1,00 | < $1,00 | Cả category là arbitrage `RPD − CPI`. CPI $2 sẽ **lỗ trên mỗi install** |

---

## 7. Constraints & Assumptions

### 7.1 Constraints

**Ràng buộc kỹ thuật**

- **Phân mảnh màn hình CarPlay là ràng buộc chi phối toàn bộ thiết kế UI.** Không có danh sách kích thước đầy đủ và không thể biết trước người dùng lắp xe gì ⇒ layout phải tính tại runtime, và phải có đường fallback cho trường hợp render thất bại.
- **Widget extension chạy trong tiến trình riêng, có ngưỡng bộ nhớ rất chặt** ⇒ không được nạp model ML hay asset lớn trong widget; widget chỉ đọc dữ liệu đã tính sẵn từ App Group.
- **Toàn bộ suy luận phải chạy on-device trên Apple Neural Engine** ⇒ giới hạn thiết bị ở iPhone 12+, và giới hạn độ phức tạp mô hình.
- **Hai ngưỡng iOS** (16.4 cho app, 17.4 cho widget CarPlay) ⇒ mọi tính năng CarPlay phải có nhánh `@available` và trạng thái thay thế.
- **Không có backend riêng ở MVP 1** ⇒ không thể tắt feature từ xa; lỗi phát hiện sau launch cần một bản cập nhật app và một vòng App Review.

**Ràng buộc thời gian và nguồn lực**

- Cửa sổ 12 tuần từ phê duyệt PRD đến launch (MVP 1 tháng 10–11/2026); TestFlight beta tháng 9/2026.
- Đội: Product, Design, **2 iOS dev**, 1 ML Engineer, QA, Growth/UA, Backend (khối lượng nhỏ).
- **Toàn bộ 10 vai trò ở PRD "Các Bên Liên Quan" hiện chưa phân công người cụ thể.** Đây là ràng buộc thực thi nghiêm trọng nhất hiện tại — xem §9.
- Ngân sách paid UA giả định: $15K cho 3 tháng đầu, CPI mục tiêu ≤ $1,00.

**Ràng buộc bên ngoài**

- **App Review là rủi ro nhị phân**: Apple đã gỡ 42–52% app trong cluster "carplay"/"car play", kể cả app rating 4,1★ ⇒ metadata và định vị bị ràng buộc cứng (không dùng `Connect`, `Sync`, `Link`, `Remote`, `Auto Sync`, `Cast`, `Mirror`).
- **Điều khoản Spotify API cho app thương mại chưa được legal xác nhận** ⇒ kiến trúc phải cho phép gỡ tích hợp Spotify mà không làm hỏng tính năng cốt lõi. Đây là lý do F1/F2/F3 không phụ thuộc Spotify.
- **Trademark "Carbina" mới qua sàng lọc sơ bộ** (USPTO wordmark + App Store + domain); chưa tra phonetic equivalents, design marks, common-law rights, Google Play, EUIPO.
- **Commission App Store 15% (Small Business Program) là giả định**; nếu là 30% thì Net Revenue T6 giảm ~$1,5K/tháng và điểm hòa vốn lùi ~2 tháng.
- Chỉ Apple Maps ở MVP 1 (không Google Maps) để giảm rủi ro review và không cần SDK ngoài.

### 7.2 Assumptions

Mọi giả định dưới đây đều có **Default đã chốt ở PRD §14** để tài liệu downstream làm việc được ngay. Nếu một giả định được trả lời khác Default, đó là một change request có phạm vi rõ ràng, không phải một khoảng trống.

| # | Giả định | Default đang dùng | Nếu sai thì sao |
|---|---|---|---|
| 1 | On-device ML đủ mạnh để tạo gợi ý dùng được | Core ML + Create ML, chạy trên ANE | Chất lượng F3/F8 giảm ⇒ mất điểm khác biệt hóa chính (R-01). Không có đường lui cloud theo Quyết định 4 |
| 2 | Người dùng chấp nhận cấp quyền Location + Calendar | Mọi quyền skip được, app vẫn chạy mức cơ bản | Giọng chào mất chiều ngữ cảnh, rơi về biến thể theo giờ |
| 3 | Apple phê duyệt app CarPlay widget với định vị mới | Tiến hành, kèm early communication từ tuần 1 | Không launch được (R-02, Critical) |
| 4 | Retention 28,8% / 11,5% / 4,0% là **benchmark category**, không phải số riêng của từng app | Coi là benchmark — cách đọc an toàn hơn | Mục tiêu retention của Carbina phải đặt lại |
| 5 | Free tier không cannibalize paid | 1 widget + 3 sound + dashboard cơ bản, không quảng cáo, không giới hạn thời gian | Conversion thấp hơn dự kiến ⇒ phải siết cấu hình free tier (đã tách thành service riêng nên sửa được ở một chỗ) |
| 6 | Giá $29,99/năm giữ được | Đã chốt 07/08/2026, không còn là giả định về mức giá | Rủi ro thật không phải "giá cao" mà là RPD có > $1,00 để bù CPI hay không (R-07) |
| 7 | Lifetime $49,99 phù hợp hơn Coin cho nhóm ghét subscription | Lifetime ở MVP 1, Coin ở MVP 2 | Mất một phần nhóm khách giá thấp; giảm thiểu bằng cách thêm Coin ở MVP 2 |
| 8 | Commission 15% | Small Business Program | Break-even lùi ~2 tháng |
| 9 | EN + ES + PT-BR là đúng ưu tiên ngôn ngữ | 3 ngôn ngữ trong MVP 1, DE/FR/IT ở MVP 2 | Chỉ ảnh hưởng phân bổ nguồn lực, không ảnh hưởng kiến trúc |
| 10 | Trial 7 ngày là độ dài đúng | 7 ngày cho cả Monthly và Yearly | Điều chỉnh được bằng cấu hình, chi phí thấp |
| 11 | AI Driving Coach là **giả thuyết chưa validate** | Không lên kế hoạch cho đến khi prototype hành vi xong | Đã được hạ khỏi nhóm khác biệt hóa chắc chắn nên rủi ro đã được kiềm chế |
| 12 | Người dùng iPhone 12+ chiếm đủ thị phần mục tiêu | Yêu cầu tối thiểu cho ANE | Nếu không, phải có nhánh không-ML — hiện **không có** trong kế hoạch |

---

## 8. Risks & Mitigation

ID rủi ro **giữ nguyên theo PRD §13** (R-01 … R-14) để hai tài liệu không bị lệch. Cột "Neo trong kiến trúc / kế hoạch" là phần bổ sung của tài liệu này: mỗi biện pháp giảm thiểu được gắn vào một quyết định kiến trúc, một module, hoặc một mốc lịch cụ thể — nếu không gắn được vào đâu, biện pháp đó chỉ là ý định.

| ID | Rủi ro | Tác động | Xác suất | Chiến lược giảm thiểu | Neo trong kiến trúc / kế hoạch |
|---|---|---|---|---|---|
| **R-11** | **Phân mảnh màn hình CarPlay** — widget cắt chữ hoặc không render trên một tập xe không đoán trước | High | High | Layout tính theo scene bounds tại runtime; test matrix ≥ 4 kích thước + 1 xe thật/nhóm; telemetry phát hiện trong 24h; free tier để người dùng tự kiểm tra trước khi trả tiền | §3.3 **Quyết định 3**; module `Core/CarPlay`; màn 13 + màn 18; Phase 1 tuần 1 |
| **R-14** | **Chiến lược retention đi ngược mô hình ngành** — cả category sống bằng churn-and-refill (D30 4%) | **Critical** | Medium-High | Đo D30 cohort tháng 1 so với benchmark 4% trong 3 tháng đầu; nếu D30 < 8% ở tháng 3 thì giả thuyết sai, cân nhắc mô hình paywall gắt hơn | §5 Phase 4 — **điểm quyết định tháng 3 đã nằm trong lịch**; `Core/Analytics` cohort tracking |
| **R-10** | **Backlash false-advertising** — quảng cáo tính năng không tồn tại là nguyên nhân trực tiếp gây làn sóng 1★ ở đối thủ | **Critical** | High | Ad creative chỉ quay feature thật trên build production; người duyệt phải đã tự chạy feature trên xe thật; cấm mọi tham chiếu Marvel/Disney | §9 — vai trò **Creative Reviewer**; quy trình phê duyệt phải viết trước Phase 3 |
| **R-07** | **CPI vượt ngưỡng RPD** — cả category là arbitrage `RPD − CPI` | **Critical** | High | Theo dõi RPD từ tuần đầu chứ không chỉ MRR; dừng scale UA nếu RPD < $1,00 sau 4 tuần; kênh đã validate là Facebook/IG/TikTok | §6.2 — CPI < $1,00 là chỉ số có ngưỡng chặn; funnel event trong `Core/Analytics` |
| **R-02** | **Apple chặn app trong review** | Critical | Medium | Liên hệ Apple xin guidance sớm; nộp TestFlight beta sớm; rà guidelines hằng tuần | §5 Phase 1 — email Apple ở **tuần 1**; Phase 3 tuần 7–8 TestFlight |
| **R-08** | **Takedown do định vị / từ khóa** — Apple đã gỡ 42–52% cluster "carplay"/"car play" | Critical | Medium-High | Tên và subtitle không chứa `Connect`/`Sync`/`Link`/`Remote`/`Auto Sync`/`Cast`/`Mirror`; không bao giờ tuyên bố app tạo hay cải thiện kết nối CarPlay; rà guideline 4.3 và 2.3 mỗi lần submit | §5 Phase 3 tuần 9–10 — ràng buộc metadata là mục kiểm bắt buộc trước submission |
| **R-01** | **On-device ML quá yếu** → gợi ý sai | High | High | Prototype mô hình ngay tuần 1–2; A/B test nhiều biến thể; vòng phản hồi từ người dùng | §5 Phase 1; module `Core/ML`; §3.3 **Quyết định 4** (đã chấp nhận trần chất lượng) |
| **R-05** | **Churn cao như category** (D1 28,8% · D7 11,5% · D30 4,0%) | High | High | Nếu D7 < 25% ở tuần 2, **điều tra lỗi render widget trước**, không phải chất lượng AI | `widget_render_failed` phải chạy từ build TestFlight đầu tiên để chẩn đoán được |
| **R-09** | **Bị xếp cùng nhóm app scam (guilt by association)** | High | Medium | ASO đặt vào cluster `widget`/`dashboard`/`personalization`/`car aesthetic`; theo dõi mục "You Might Also Like" của chính Carbina sau launch | §5 Phase 3 và Phase 4 — việc theo dõi hậu launch, không phải việc kỹ thuật |
| **R-03** | **Trial→paid thấp (< 8%)** | High | Medium | Free tier đã giảm rủi ro (người dùng xác nhận app chạy trước khi vào trial); A/B test copy paywall | `Core/Entitlement` tách riêng nên đổi cấu hình free tier ở một chỗ (§3.3 **Quyết định 5**) |
| **R-13** | **Ý tưởng "giọng AI trong xe" đã có người thử và thất bại** — 6 app gắn nhãn AI đều $0 doanh thu | Medium | Medium | Thắng nhờ thực thi + marketing, không nhờ ý tưởng; ngân sách marketing phải có thật; không dựa vào chữ "AI" trong tên | §4.1 — F3 phải đạt AC đo được (≤ 2s, ≥ 4 biến thể) chứ không dừng ở demo |
| **R-12** | **Chargeback / dispute do giá không rõ ràng** | Medium | Low-Medium | Hiển thị giá cuối bằng tiền tệ địa phương trước khi confirm; không quy đổi kiểu "$0,48/tuần"; email xác nhận sau giao dịch | Màn 10 (Xác Nhận Giá) + event `price_confirmed` là bằng chứng tuân thủ |
| **R-04** | **Refund rate cao (> 7%)** | Medium | Medium | Free tier là biện pháp chính; không dark pattern; theo dõi hằng tuần | `refund_detected` bắt buộc từ ngày launch |
| **R-06** | **Spotify API rate limiting** | Medium | Low | Cache top track cục bộ; retry backoff; pre-fetch | Kiến trúc đã tách Spotify khỏi F1/F2/F3 nên sự cố này không hạ tính năng cốt lõi |

**Ba rủi ro cấp thực thi mà PRD chưa nêu, phát sinh từ chính các quyết định kiến trúc ở §3.3:**

| # | Rủi ro | Tác động | Giảm thiểu |
|---|---|---|---|
| A | **Ngưỡng bộ nhớ của widget extension** — widget bị hệ thống kill nếu vượt ngưỡng, biểu hiện ra ngoài giống hệt lỗi render và sẽ bị đếm nhầm vào R-11 | High | `widget_render_failed` phải phân biệt được `failure_reason` giữa "vượt bounds" và "bị kill vì bộ nhớ"; widget tuyệt đối không nạp model ML hay ảnh chưa giảm kích thước |
| B | **Không có remote config ở MVP 1** — một lỗi tương thích phát hiện sau launch cần một vòng App Review mới sửa được | High | Chấp nhận có ý thức (§3.3 Quyết định 6); bù bằng fallback CarPlay (màn 18) để lỗi không bao giờ thành màn trắng; đưa remote config vào MVP 2 |
| C | **Chưa phân công người cho toàn bộ 10 vai trò** — R-10 không có người kiểm soát nếu thiếu Creative Reviewer, R-11 không có người sở hữu nếu thiếu QA | **Critical** | Phải xong **trước tuần 1**. Đây là mục số 1 trong "Điều Chỉnh Bắt Buộc" của PRD và là điều kiện tiên quyết của Phase 1 |

---

## 9. Stakeholders

Vai trò và trách nhiệm giữ nguyên theo **PRD "Các Bên Liên Quan"**. Cột bên phải là phần bổ sung của tài liệu này: mỗi vai trò gắn với artefact kỹ thuật nào.

| Vai trò | Người | Sở hữu về mặt kỹ thuật |
|---|---|---|
| **Product Owner** | *Chưa phân công* | Chốt các Default `(ASSUMPTION)` ở PRD §14; phê duyệt từng cổng chất lượng của bộ tài liệu |
| **Project Manager** | *Chưa phân công* | Lịch 12 tuần ở §5; theo dõi điều kiện ra khỏi từng Phase |
| **Lead Developer (iOS)** | *Chưa phân công* | `Core/CarPlay` và layout engine — **chịu trách nhiệm trực tiếp cho R-11**; cấu trúc thư mục §3.3 Quyết định 7 |
| **iOS Developer #2** | *Chưa phân công* | `Features/*` (onboarding, paywall, settings, sound library); tích hợp StoreKit 2 |
| **ML Engineer** | *Chưa phân công* | `Core/ML` — ContextEngine, mô hình chọn ngữ cảnh, chuyển đổi Core ML |
| **Designer (UI/UX)** | *Chưa phân công* | Thiết kế cho **nhiều kích thước màn hình CarPlay**, không phải một kích thước cố định; đầu vào cho `Wireframes.md` |
| **QA** | *Chưa phân công* | **Sở hữu test matrix ≥ 4 kích thước + 1 xe thật/nhóm (R-11)**; điều kiện chặn phát hành ở §6.1 |
| **Growth / UA** | *Chưa phân công* | Theo dõi CPI/RPD; ASO theo ràng buộc R-08/R-09 |
| **Creative Reviewer** | *Chưa phân công* | **Phê duyệt mọi ad creative; bắt buộc đã tự chạy feature trên xe thật (R-10)** |
| **Backend Engineer** | *Chưa phân công* | Endpoint nhận App Store Server Notification cho `refund_detected` — phần backend duy nhất của MVP 1 |
| **Legal** | *Chưa phân công* | Xác nhận trademark "Carbina" (phonetic, design marks, common-law, Google Play, EUIPO); review Privacy Policy + Spotify API terms |

> ⚠️ **Trạng thái**: không vai trò nào có người cụ thể tại thời điểm snapshot này. Hai vai trò không được bỏ trống khi bước vào Phase 1 là **Creative Reviewer** (không có người này thì R-10 không có ai kiểm soát) và **QA** (không có người này thì R-11 không có ai sở hữu). Xem rủi ro thực thi **C** ở §8.

---

## 10. References

### Tài liệu nguồn (upstream)

| Tài liệu | Đường dẫn | Nội dung tài liệu này dựa vào |
|---|---|---|
| **PRD v2.4** | [`PRD.md`](./PRD.md) | §3 personas · §5 tầm nhìn & KPI · §6 phạm vi · §7 F1–F13 · §9 ràng buộc kỹ thuật · §10 danh sách 18 màn hình · §11 kiếm tiền · §12 analytics · §13 rủi ro R-01…R-14 · §14 câu hỏi mở · §15 mốc triển khai |
| Deep-dive đối thủ #1 | [`research/mycar-deep-dive.md`](./research/mycar-deep-dive.md) | Nguồn của các chế độ thất bại đã định hình R-10, R-11, R-12 |
| Dữ liệu niche AppStoreSpy | [`research/appstorespy-competitor-data.md`](./research/appstorespy-competitor-data.md) | Tỉ lệ takedown cluster (cơ sở của R-08) |
| Ma trận tính năng & phân tầng | [`research/feature-tiers-and-competitor-matrix.md`](./research/feature-tiers-and-competitor-matrix.md) | Cơ sở phân tầng Free/Premium |

### Tài liệu kế tiếp (downstream — sẽ được tạo)

| Bước | Tài liệu | Sẽ lấy gì từ tài liệu này |
|---|---|---|
| Step 3 | `Use_Cases.md` | Ba persona ở §2.1 → actor; 18 màn hình PRD §10 → ánh xạ UC → Screen; F1–F13 → mục tiêu của actor. Gán ID `UC-xxx` và `AC-xxx.y` |
| Step 4 | `Functional_Requirements.md` | AC ở PRD §7 → `FR-xxx`; ngưỡng ở §6.1 → `NFR-xxx`; ràng buộc §7.1 → business rule |
| Step 5 | `Wireframes.md` | 18 màn hình → `WF-xxx`; ràng buộc responsive ở §3.3 Quyết định 3 là điều kiện thiết kế bắt buộc cho mọi màn CarPlay |
| Step 6 | `UX_Flows.md` | Hai cây điều hướng độc lập (iPhone và CarPlay) ở §3.2; đường lỗi qua màn 18 và màn 13 |
| Step 7 | `Project_Implementation_Roadmap.md` | Phase 1–4 ở §5 → nhóm phase theo `FR-xxx`; điểm quyết định tháng 3 (R-14) là mốc bắt buộc |

### Tham chiếu kỹ thuật bên ngoài

- Apple CarPlay App Programming Guide — `CPTemplateApplicationScene`, `CPInterfaceController`
- WidgetKit trên CarPlay (iOS 17.4+) — ràng buộc kích thước container và ngưỡng bộ nhớ
- StoreKit 2 — subscription và non-consumable, App Store Server Notifications V2
- Core ML / Create ML — suy luận on-device trên Apple Neural Engine
- App Store Review Guidelines — mục 2.3 (metadata chính xác) và 4.3 (spam/trùng lặp), cơ sở của R-08
- App Store Small Business Program — điều kiện hưởng commission 15%

### Chưa tồn tại tại thời điểm snapshot

- **Figma design** — sẽ có ở Step 5 (`Wireframes.md`)
- **API specification** — MVP 1 gần như không có backend; chỉ có endpoint `refund_detected`, sẽ đặc tả ở Step 4
- **Privacy policy** — bắt buộc hoàn thành trước submission (Phase 3, tuần 9–10)

---

**Document Version**: 2.4
**Last Updated**: 2026-08-07 (snapshot bộ tài liệu; file tạo ngày 2026-08-15)
**Status**: Draft — chờ PO review
**Bước kế tiếp**: `gate-overview` → phê duyệt → **Step 3: `Use_Cases.md`**
