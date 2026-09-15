# Calo AI - Tổng Quan Dự Án

## 0. Tham chiếu PRD

- **Nguồn PRD**: `.claude/specs/Calo-AI/PRD.md`
- **Chính sách tham chiếu**: Chiến lược sản phẩm, bối cảnh thị trường, và phân tích đối thủ được xác định trong PRD và không được lặp lại ở đây. Tài liệu này tập trung vào kiến trúc kỹ thuật, kế hoạch triển khai, và lịch trình thực thi.
- **Bản snapshot sử dụng**: PRD v1.0, 2026-07-21

---

## 1. Giới thiệu

### 1.1 Phát biểu Vấn đề
Các app ghi log calo hiện tại buộc người dùng phải thực hiện ghi log thủ công tốn thời gian (tìm kiếm, quét mã vạch, nhập tay) hoặc sử dụng AI-photo nhưng thiếu cơ chế xác nhận độ chính xác, gây ra tỷ lệ bỏ cuộc cao trong vài ngày. Người dùng mass-market bỏ ghi log trong 2-3 ngày do ma sát; trong khi đó, phân khúc người dùng thuốc GLP-1 mới nổi (~41 triệu người trưởng thành tại Mỹ) có nhu cầu theo dõi dinh dưỡng đặc thù (nhận biết khẩu phần, theo dõi triệu chứng, lịch trình thuốc) mà các app calo chính thống chưa phục vụ tốt trong cùng một trải nghiệm thống nhất. Thêm vào đó, những vấn đề mất niềm tin gần đây (Cal AI bị Apple gỡ vì paywall lừa dối + rò rỉ 3.2 triệu bản ghi người dùng tháng 3-4/2026) đã tạo ra cơ hội cho minh bạch billing và bảo mật dữ liệu trở thành lợi thế cạnh tranh thực sự thay vì chỉ là yêu cầu cơ bản.

### 1.2 Giải pháp Tổng quan
Calo AI kết hợp ba trụ cột chiến lược: (1) **core loop nhanh** — chụp ảnh → AI xác nhận nguyên liệu/khẩu phần → log (dưới 10 giây, thu hút mass-market); (2) **monetization minh bạch** — gói miễn phí với 3 lượt scan AI/ngày, trial 7 ngày, hiển thị giá rõ ràng trước khi tính phí, huỷ dễ dàng trong app (xây dựng niềm tin sau những vụ billing scandal); (3) **upsell phân lớp** — subscription core mở khóa scan không giới hạn + gói add-on theo dõi GLP-1 (AI Coach, nhắc lịch thuốc, ghi nhận triệu chứng) cho phân khúc sẵn sàng chi trả cao, mà không thu hẹp TAM của gói free tier.

Xem **PRD §1-§4** để hiểu đầy đủ quy mô thị trường, phân tích đối thủ, và luận điểm khác biệt hóa.

### 1.3 Mục tiêu Kinh doanh
- **Phát hành MVP (beta iOS)** trong 3 tháng kể từ khi bắt đầu design; phát hành công khai trên App Store trong 4-5 tháng
- **Đạt 20K lượt tải và D7 retention ≥20%** trong 3 tháng để kiểm chứng product-market fit (hiệu quả core loop)
- **Đạt 3-5% free-to-paid conversion** ở tháng thứ 6, chứng minh rằng billing minh bạch không làm giảm willingness-to-pay so với chuẩn ngành (2-5% tiêu chuẩn freemium mobile subscription)
- **Thiết lập định vị niềm tin** như một lựa chọn thay thế cho Cal AI cho những người dùng bị tổn thương bởi scandal billing/bảo mật, đo lường thông qua cảm nhận review App Store và word-of-mouth qua Reddit/cộng đồng

---

## 2. Người dùng Mục tiêu

### 2.1 Personas Người dùng Chính

#### Persona 1: Người Mới Diet Mass-Market (Trình driver TAM chính)
- **Nhân khẩu học**: 25-40 tuổi, cả nam và nữ, thành phố/ngoại ô, khả năng công nghệ trung bình, thu nhập $40K-$100K
- **Mục tiêu**: Giảm hoặc duy trì cân nặng mà không cảm thấy bị tước đoạt; hình thành thói quen ghi log bền vững; thấy tiến bộ hàng tuần
- **Điểm gây khó chịu**:
  - Ghi log thủ công (tìm kiếm/quét mã vạch) tẻ nhạt và gây kiệt sức sau 2-3 ngày
  - Không tin tưởng vào ước lượng khẩu phần riêng, nên nhập tay cảm thấy có rủi ro
  - App trước đã tính phí bất ngờ hoặc đòi liên hệ support để huỷ; giờ cảnh báo với subscription
- **Bối cảnh sử dụng**: Ghi log bữa ăn tại nhà hoặc khi đang đi vào giờ trưa; kiểm tra tiến bộ ~hàng ngày vào buổi tối; có thể bỏ nếu friction vượt 30 giây mỗi lần log

#### Persona 2: Người dùng Thuốc GLP-1 (Phân khúc cao ARPU thứ cấp)
- **Nhân khẩu học**: 30-55 tuổi, cả nam và nữ, thu nhập cao hơn ($80K+, sẵn sàng trả phí), quan tâm đến sức khỏe
- **Mục tiêu**: Theo dõi giảm cân nhanh trong khi dùng GLP-1; đảm bảo dinh dưỡng đầy đủ khi ăn khẩu phần nhỏ; điều phối ghi log với lịch trình thuốc
- **Điểm gây khó chịu**:
  - App calo hiện tại không tính đến khẩu phần nhỏ hoặc triệu chứng GI liên quan thuốc
  - Phải chuyển đổi giữa app calo + app nhắc thuốc riêng, phân mảnh trải nghiệm
  - Lo lắng về quyền riêng tư dữ liệu sức khỏe sau khi biết về vụ Cal AI data breach
- **Bối cảnh sử dụng**: Ghi log 1-2 bữa/ngày (khẩu phần nhỏ); kiểm tra log triệu chứng/tác dụng phụ; muốn reassurance dữ liệu lưu an toàn; sẵn sàng trả premium ($10-20/tháng) cho trải nghiệm tích hợp

### 2.2 Người dùng Thứ cấp
- **Nhà đánh giá App Store**: Sẽ đánh giá tính minh bạch billing và tư thế bảo mật dữ liệu so với các app established
- **Đội Growth/UA**: Sẽ A/B test các luồng onboarding và timing paywall; cần analytics event robust để đo funnel
- **Support/CS** (tương lai): Sẽ xử lý edge case xung quanh trial conversion và yêu cầu tính năng GLP-1

---

## 3. Kiến trúc Cấp cao

### 3.1 Technology Stack

#### Frontend
- **Nền tảng**: iOS (iPhone only, giai đoạn MVP; iPad/Android là post-MVP theo PRD §6)
- **Phiên bản tối thiểu**: iOS 16.0 (lý do: hỗ trợ SwiftUI 4, AVFoundation camera API, StoreKit 2 mà không cần phức tạp legacy; vẫn cover ~90% active iOS devices)
- **UI Framework**: SwiftUI (chính)
- **Architecture Pattern**: MVVM + Repository pattern (theo ios-architecture skill)
  - Views: `[Feature]View.swift` (UI chỉ, không logic business)
  - ViewModels: `[Feature]ViewModel.swift` (state via `@Published`, methods handle user actions)
  - Models: `[EntityName].swift` (data structs, Codable, Identifiable nếu cần)
  - Services: `[Name]Service.swift` (API calls, xử lý ảnh, persistence cục bộ)
- **State Management**: SwiftUI `@State`, `@StateObject`, `@ObservedObject` (Combine-based)
- **Navigation**: NavigationStack (iOS 16+ native, không third-party)
- **Xử lý ảnh**: AVFoundation camera + Vision framework để tiền xử lý ảnh on-device trước khi gửi AI Vision API

#### Backend
- **API Architecture**: REST (đơn giản hơn GraphQL cho MVP; dễ test offline)
- **Xác thực**: Sign in with Apple (bắt buộc theo App Store; không social login ở MVP)
- **Cơ sở dữ liệu**: PostgreSQL (qua Supabase với Row-Level Security bật mặc định)
- **Backend Runtime**: Supabase (managed Postgres + auth + real-time via PostgREST API)
  - Thay thế: Custom Node/Python backend nếu Supabase RLS không đủ cho monetization/subscriber data isolation
- **Storage**: AWS S3 (qua presigned URLs) cho ảnh món ăn tạm thời; auto-delete sau 7 ngày trừ khi người dùng explicitly archive

#### Dịch vụ Bên thứ ba
| Dịch vụ | Mục đích | Lý do |
|---------|---------|-------|
| OpenAI / Anthropic Multimodal API | Nhận diện thực phẩm bằng AI | Độ chính xác đã chứng minh (87-97% theo benchmark học thuật); thanh toán theo lượng sử dụng; nhanh hơn ML on-device cho MVP |
| RevenueCat | Quản lý subscription + billing | Giảm rủi ro StoreKit misconfiguration; xử lý restore purchases, grace periods, analytics; được Apple phê duyệt |
| Firebase Crashlytics | Crash reporting | Free tier đủ cho MVP; theo dõi crash-free ≥99.5% KPI |
| Firebase Analytics | Tracking sự kiện + analytics người dùng | Thay thế Amplitude; free tier theo dõi DAU, funnel, conversion free-to-paid |
| Superwall (hoặc tương đương) | Paywall UI + A/B testing | Config paywall remote cho phép iteration nhanh mà không cần app update; thực thi transparent billing UX by design |

### 3.2 Sơ đồ Kiến trúc Hệ thống

```
┌──────────────────────────────────────────────────────────┐
│                    iOS App (SwiftUI)                     │
├──────────────────────────────────────────────────────────┤
│  Presentation Layer (Views)                              │
│  ├─ CameraView (chụp + upload)                           │
│  ├─ ConfirmationView (chỉnh sửa nguyên liệu/khẩu phần)   │
│  ├─ DiaryView (lịch sử log)                              │
│  ├─ PaywallView (billing UI, quản lý bởi Superwall)     │
│  └─ SettingsView (tài khoản, quản lý subscription)       │
├──────────────────────────────────────────────────────────┤
│  Business Logic Layer (ViewModels + Services)            │
│  ├─ CameraViewModel → AIService                          │
│  ├─ DiaryViewModel → LogRepository                       │
│  ├─ SubscriptionViewModel → BillingService (RevenueCat)  │
│  └─ AuthService (Sign in with Apple)                     │
├──────────────────────────────────────────────────────────┤
│  Data Layer (Repositories + Local Cache)                 │
│  ├─ LogRepository (food logs)                            │
│  ├─ UserRepository (profile, goals)                      │
│  ├─ SubscriptionRepository (trial state, purchases)      │
│  └─ CoreData local store (offline read cache)            │
└─────────────────┬──────────────────────────────────────┘
                  ↓
┌──────────────────────────────────────────────────────────┐
│           Supabase Backend (REST API)                    │
├──────────────────────────────────────────────────────────┤
│  Xác thực: Apple ID → JWT via PostgREST                  │
│  PostgreSQL: users, food_logs, subscriptions tables      │
│  Row-Level Security: Mỗi người dùng chỉ thấy dữ liệu riêng│
│  Real-time: Cập nhật bảng Subscriptions trigger paywall  │
└─────────────────┬──────────────────────────────────────┘
                  ↓
┌──────────────────────────────────────────────────────────┐
│              Third-Party APIs                            │
├──────────────────────────────────────────────────────────┤
│  ├─ OpenAI/Anthropic Vision: ảnh → {dish, cals, macro}  │
│  ├─ RevenueCat: subscription receipts, restore, analytics│
│  ├─ Firebase: crashes, analytics events                  │
│  ├─ Superwall: paywall config (remote)                   │
│  └─ Apple StoreKit 2: IAP receipt validation             │
└──────────────────────────────────────────────────────────┘
```

### 3.3 Các Quyết định Kiến trúc Chính

| Quyết định | Lý do | Trade-off |
|-----------|-------|-----------|
| **Supabase (managed Postgres)** vs Firebase | Row-Level Security (RLS) cung cấp multi-tenant data isolation native; dễ implement transparent data deletion policy; Postgres quen thuộc hơn với backend teams truyền thống | Cold starts ~2-5s vs Firebase <1s; real-time kém hơn (polling cho một số feature) |
| **MVVM + Repository pattern** vs TCA/Redux | Learning curve thấp hơn; Combine integration native; đủ cho MVP scope mà không heavy DI frameworks | Tiềm năng ViewModel bloat nếu không kỷ luật; state ít predictable hơn Redux |
| **RevenueCat** vs direct StoreKit | Loại bỏ rủi ro StoreKit v2 misconfiguration (nguồn lớn Apple rejections cho billing); xử lý grace periods, renewal management, cross-device sync | ~2% revenue fee tier; vendor lock-in nếu logic subscription đặc biệt cần sau |
| **AI Vision API** (OpenAI/Anthropic) vs on-device ML | Nhanh đến MVP; độ chính xác đã chứng minh; scale theo usage cost | Privacy: ảnh gửi service bên ngoài (giảm bằng auto-delete policy); latency cao hơn ~500ms-3s vs <100ms |
| **iOS-first (không Android MVP)** | Giảm độ phức tạp; iOS users có ARPU cao hơn (chìa khóa cho freemium subscription strategy); App Store responsive hơn transparent IAP UX | Delay Android TAM; cần effort parity sau |

---

## 4. Tổng quan Tính năng Cốt lõi

Để định nghĩa tính năng đầy đủ, xem **PRD §7 Yêu cầu và Tính năng**.

### 4.1 Tính năng Bắt buộc (MVP)
1. **Ghi log Thực phẩm dựa trên Ảnh AI** — camera chụp bữa ăn, AI trả về {tên món, calo, macros}; người dùng xác nhận hoặc chỉnh sửa; log lưu vào diary
2. **Xác nhận Nguyên liệu/Khẩu phần** — differentiator quan trọng vs Cal AI; người dùng điều chỉnh nguyên liệu inferred và khẩu phần (nhỏ/vừa/lớn hoặc gram) trước khi lưu cuối cùng
3. **Diary Thực phẩm & Lịch sử** — xem log theo ngày/tuần, theo dõi calo/macro tích luỹ vs mục tiêu hàng ngày
4. **Onboarding & Cá nhân hoá Mục tiêu** — thu thập chiều cao/cân nặng/mục tiêu/mức hoạt động; tính TDEE dùng công thức Mifflin-St Jeor
5. **Subscription Minh bạch** — 3 lượt scan AI/ngày miễn phí (ASSUMPTION); $9.99/tháng hoặc $39.99-49.99/năm Premium (ASSUMPTION, PRD §14); trial 7 ngày (ASSUMPTION); huỷ trong app
6. **Sign in with Apple** — xác thực + đồng bộ dữ liệu giữa các phiên

### 4.2 Tính năng Nên có (Post-MVP)
1. **AI Coach hội thoại** — trợ lý hội thoại với bối cảnh từ food diary và mục tiêu của người dùng
2. **Theo dõi GLP-1** — subscription add-on riêng; ghi nhận triệu chứng, khẩu phần nhỏ cho GLP-1 users, nhắc lịch thuốc
3. **Gamification** — streaks, milestones, weekly badges (Cal AI chứng minh cơ chế này drive engagement)
4. **Apple Health Integration** — hai chiều sync food logs và workouts
5. **Hỗ trợ Wearable** — Apple Watch app cho quick meal logging hoặc stats view

### 4.3 Cải tiến Tương lai
- Phiên bản Android
- Meal planning và smart shopping list
- Leaderboard xã hội và challenges
- Tích hợp nutritionist chuyên nghiệp
- Telehealth partnership cho GLP-1 prescriptions (care integration, không prescribing)

---

## 5. Lộ trình Phát triển

**Tổng lịch trình: ~4-5 tháng từ design approval đến public App Store launch.**

### Phase 1: Design & Setup (Tuần 1-2)
- **Mục tiêu**: Finalize Figma mockups; setup Xcode project, Supabase backend, RevenueCat account, iOS keychain cho auth tokens
- **Deliverables**:
  - Approved wireframes (tất cả screens per PRD §10)
  - Xcode project structure (`App/` → `Core/` → `Features/` layout per ios-architecture)
  - Supabase project với auth policy, user/log tables, RLS enabled
  - RevenueCat product setup (weekly/monthly/annual tiers)
- **Parallel tracks**: Design team → Figma; Engineering → env setup; Backend → DB schema

### Phase 2: Core Loop MVP (Tuần 3-7)
- **Mục tiêu**: Implement Photo → Confirm → Log end-to-end; đạt <10 sec flow; kết nối Supabase; basic analytics
- **Deliverables**:
  - CameraView + AIService (gọi OpenAI/Anthropic; xử lý timeouts)
  - ConfirmationView (chỉnh sửa nguyên liệu, điều chỉnh khẩu phần)
  - DiaryView (lịch sử log, tổng vs goal)
  - AuthService (Sign in with Apple)
  - LogRepository (Supabase CRUD)
  - Firebase Crashlytics + Analytics integration
  - Unit tests (target 60% coverage core logic)
- **Milestones**:
  - Cuối Tuần 5: alpha build (internal dog-food)
  - Cuối Tuần 7: core loop performance < 10s validated

### Phase 3: Monetization & Polish (Tuần 8-11)
- **Mục tiêu**: Integrate RevenueCat paywall; implement billing UX per PRD §11 (minh bạch, đáng tin cậy); run QA passes
- **Deliverables**:
  - PaywallView (quản lý bởi Superwall)
  - SubscriptionViewModel + BillingService (RevenueCat SDK)
  - Logic trial (7-day, auto-renew sau clear prompt)
  - In-app cancellation (Settings → Manage Subscription)
  - Onboarding flow (TDEE calculation)
  - Privacy Policy + App Store metadata
  - Accessibility audit (VoiceOver, Dynamic Type, 44pt tap targets)
  - Full QA test plan (tất cả 9 screens per PRD §10)
- **Milestones**:
  - Cuối Tuần 9: beta build (monetization enabled, 50 external testers)
  - Cuối Tuần 10: Apple review submission
  - Cuối Tuần 11: App Store approval hoặc iterate feedback

### Phase 4: Launch & Early Monitoring (Tuần 12+)
- **Mục tiêu**: Public release; track D1/D7/D30 retention; monitor crash-free rate, conversion funnel
- **Deliverables**:
  - App Store live
  - UA campaign kick-off (organic + paid)
  - Daily monitoring dashboard (Firebase + RevenueCat)
  - Post-launch bug response SLA (P0 trong 24h, P1 trong 48h)
- **Ongoing**:
  - User feedback loop (Reddit, reviews, support)
  - Weekly metrics review (installs, D7 retention, conversion)
  - GLP-1 add-on design bắt đầu cho Post-MVP phase

---

## 6. Chỉ số Thành công

### 6.1 Chỉ số Kỹ thuật (Mục tiêu MVP)
- **Cold launch app**: < 2.0s trên iPhone 13/14
- **Core loop latency** (chụp → confirm → save): < 10s end-to-end (key differentiator vs Manual-heavy apps)
- **AI Vision API response**: < 3s p95
- **Crash-free sessions**: ≥ 99% (quan trọng cho niềm tin sau Cal AI breach)
- **API response time**: < 1s p95 (Supabase read-heavy queries)
- **Test coverage**: ≥ 60% trên core ViewModels & Services

### 6.2 Chỉ số Kinh doanh (Mục tiêu 6 tháng per PRD §5)
| Chỉ số | Tháng 3 | Tháng 6 | Nguồn dữ liệu |
|--------|---------|---------|-------------|
| **Lượt tải** | 20,000 | 150,000 | App Store Connect |
| **DAU** | 2,000-3,000 | 15,000+ | Firebase Analytics |
| **D7 Retention** | ≥20% | ≥30% | Cohort analysis |
| **D30 Retention** | 8-10% | ≥15% | Cohort analysis |
| **Free-to-Paid Conversion** | 3% | 5% | RevenueCat + Analytics |
| **MRR** | $15K | $120K | RevenueCat Reporting |
| **App Store Rating** | ≥4.5★ | ≥4.6★ | App Store Connect |

---

## 7. Ràng buộc & Giả định

### 7.1 Ràng buộc
- **Lịch trình**: 4-5 tháng đến public launch (cam kết cố định per business goals §1.3)
- **Ngân sách**: Không có ràng buộc; giả định đủ resources eng + design
- **Đội**: Minimum viable eng team: 1 iOS engineer (full-time) + 1 backend engineer (part-time cho Supabase setup) + 1 designer (full-time qua alpha) + 1 QA (tuần 8-11, intensive)
- **Kỹ thuật**: iOS 16+ only (không iOS 15 legacy support); iPhone only (không iPad hay macOS); không offline-first logging (cần internet cho AI Vision API)
- **Regulatory**: Compliant với App Store billing guidelines (non-negotiable; Cal AI violations là cautionary tale)

### 7.2 Giả định
- **Mạng người dùng**: Kết nối internet ổn định cho AI Vision API calls (không offline logging ở MVP)
- **Độ tin cậy AI Vendor**: OpenAI/Anthropic API maintain <3s p95 latency; backoff/retry logic handle transient failures gracefully
- **Phê duyệt Apple**: Transparent billing UX sẽ không trigger rejections (design validated vs Apple Guideline 3.1.2c, 5.6 trước submit)
- **Market Timing**: GLP-1 medication momentum (41M US adults) và Cal AI's trust crisis window vẫn actionable cho 3-6 tháng; contingency: pivot mass-market only nếu GLP-1 underperforms post-MVP
- **Monetization**: 3% free-to-paid conversion (PRD assumption §13) đạt được với transparent trial + no dark patterns

---

## 8. Rủi ro & Giảm thiểu

| Rủi ro | Xác suất | Tác động | Chiến lược Giảm thiểu |
|--------|----------|----------|---------------------|
| **Chi phí AI Vision API vượt budget** khi scaled to high usage | Medium | High | Đàm phán volume discount với OpenAI/Anthropic trước MVP; cache common dish results; A/B test free-tier scan limits để cap burn |
| **Apple từ chối app** vì billing UX (Guideline 3.1.2c/5.6 violation) | Low | High | Legal + product review paywall design vs guideline checklist trước submit; dùng RevenueCat + Superwall (both pre-approved by Apple) |
| **AI food recognition accuracy < 80%** làm hạ retention | Medium | High | Mandatory user-confirmation step (differentiator); collect "scan_manual_override" event làm feedback signal; iterate model với user corrections thực tế |
| **Supabase outage hoặc data loss** | Low | High | Daily automated backups to S3; test recovery procedure tuần 2; maintain 48h incident response SLA với Supabase support |
| **MyFitnessPal (incumbent + giờ owns Cal AI tech) undercut pricing** | High | Medium | Differentiate trên transparent billing + GLP-1 integration; nếu price war escalate, emphasize trust positioning (no subscription dark patterns) |
| **GLP-1 user segment underperform** (ARPU thấp hơn expected) | Medium | Medium | Monitor attach-rate KPI closely 6-month gate; be prepared pivot mass-market retention focus (cheaper trials, gamification) nếu GLP-1 không yield predicted LTV |
| **Data privacy incident hay breach** (sensitivity given Cal AI precedent) | Low | Very High | Audit backend security pre-beta (penetration test); enforce auto-delete ảnh sau 7 ngày trừ archived; comply GDPR/CCPA deletion requests trong 30 ngày; publish privacy policy transparently |

---

## 9. Stakeholders

- **Product Owner**: Chưa chỉ định (responsible cho vision, prioritization, release gates)
- **iOS Lead Engineer**: Chưa chỉ định (owns architecture, code quality, performance)
- **Backend Engineer** (part-time MVP): Chưa chỉ định (Supabase schema, RLS, API contracts)
- **UI/UX Designer**: Chưa chỉ định (9 screen mockups per PRD §10, accessibility)
- **QA/Test**: Chưa chỉ định (test plan, beta management, App Store readiness)
- **Growth/UA**: Chưa chỉ định (organic + paid UA strategy, analytics instrumentation)
- **Data Analytics**: Chưa chỉ định (dashboard setup, KPI tracking, weekly reporting)

---

## 10. Tham chiếu

- [PRD.md](./PRD.md) — Đầy đủ product requirements, market analysis, competitor deep-dive, feature specifications
- [ios-architecture](../.../ios-architecture/SKILL.md) — MVVM folder structure, naming conventions
- [Supabase documentation](https://supabase.com/docs) — Auth, RLS, PostgREST API
- [RevenueCat documentation](https://www.revenuecat.com/docs) — Subscription, receipts, analytics
- [StoreKit 2 documentation](https://developer.apple.com/storekit/) — iOS 16+ in-app purchase APIs

---

**Phiên bản Tài liệu**: 1.0  
**Cập nhật Lần cuối**: 2026-07-21  
**Trạng thái**: Bản nháp  
**Căn chỉnh với Phiên bản PRD**: 1.0 (2026-07-21)
