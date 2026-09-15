# Carbina: Car Dashboard & Widgets — Use Cases

**Document Version**: 2.4
**Snapshot Date**: 2026-08-07 (đồng bộ với PRD v2.4 và Project_Overview v2.4)
**Ngày tạo file**: 2026-08-17
**Status**: Draft — chờ PO review
**Dependencies**: [`PRD.md`](./PRD.md) v2.4 · [`Project_Overview.md`](./Project_Overview.md) v2.4

**Phân loại scale**: **Medium** (5–10 feature hướng người dùng). PRD §7 có 13 feature, nhưng F11 (crash reporting) và F12 (giám sát sentiment review) là công cụ nội bộ không có bề mặt người dùng cuối, và F13 (Contacts) đã dời MVP 2 ⇒ 10 feature hướng người dùng trong MVP 1. Mục tiêu theo `project-docs-contract`: 20–35 UC · ≥ 25 màn hình (gồm modal/overlay) · 8–15 task flow · 10–20 sub-flow · 15–25 scenario.

---

## 0. Creative Decomposition Summary

Mục này ghi lại quá trình suy nghĩ đã tạo ra các UC bên dưới. Nó tồn tại để chứng minh các UC **không phải bản chép lại của bảng feature trong PRD §7**, mà là kết quả của việc bung feature thành hành động nhỏ, soi từng hành động qua ba ngữ cảnh người dùng, kiểm tra hành động nào cần xuất hiện ở nhiều chỗ, rồi mới dựng cây màn hình.

### 0.1 Feature Explosion

| PRD Feature | Sub-Features Discovered | UC Candidates | Daily? | Relates To |
|---|---|---|---|---|
| **F1 — Âm thanh Connect/Disconnect/Arrive** | Nghe thử preset trước khi chọn · Gán sound cho sự kiện Connect · Gán sound cho Disconnect · Gán sound cho Arrive · Điều chỉnh âm lượng sound độc lập với nhạc · Nghe sound lúc lên xe không bị nhạc lấn · Nghe sound disconnect đúng thời điểm tắt máy qua loa xe · Phân biệt preset Free và preset khoá | UC-006 → UC-011 | **Yes** (2 lần/ngày: lên và xuống xe) | F4 (3 preset ở Free), F7 (khoá preset), F9 (sound theo ngôn ngữ) |
| **F2 — Widget CarPlay tự adapt** | Tạo widget đầu tiên · Chọn loại widget · Chọn ảnh xe hoặc ảnh cá nhân · Xem preview theo đúng tỉ lệ màn hình xe · Xem widget thật trên màn hình xe · Xử lý khi widget không render được · Chẩn đoán kích thước màn hình xe nhận được · Gửi báo cáo lỗi tương thích · Đổi widget đang dùng | UC-012 → UC-017 | **Yes** (xem mỗi chuyến) | F5 (ảnh xe), F4 (1 widget ở Free), F10 (telemetry render) |
| **F3 — Giọng chào AI cá nhân hóa** | Bật/tắt toàn bộ · Chọn nguồn ngữ cảnh (giờ/thời tiết/lịch/điểm đến) · Nghe thử câu chào trước khi lái · Nghe câu chào thật khi lên xe · Nhận câu chào khác nhau theo hoàn cảnh · Tắt riêng một nguồn ngữ cảnh khi bị từ chối quyền | UC-018 → UC-021 | **Yes** | F6 (quyền Location/Calendar), F9 (nội dung chào theo ngôn ngữ), F8 (dùng chung ContextEngine) |
| **F4 — Gói Free vô thời hạn** | Dùng app không trả tiền, không hết hạn · Tự xác nhận widget chạy trên xe của mình · Thấy rõ cái gì mở và cái gì khoá · Không bị paywall ở lần mở app đầu · Nâng cấp khi tự thấy cần, không bị ép | UC-024 (+ AF trong UC-007, UC-012) | **Yes** | F7 (paywall), F2 (widget Free đầy đủ chức năng), F1 (3 preset) |
| **F5 — Thư viện xe (make/model/year)** | Tìm hãng theo tên · Chọn model · Chọn năm · Báo xe không có trong danh sách · Đổi xe sau khi đã chọn · Xem ảnh xe sắc nét trên màn hình xe | UC-002, UC-003 | No (một lần, đổi rất ít) | F2 (ảnh xe cho widget), F6 (bước 2 onboarding) |
| **F6 — Onboarding ≤ 5 bước** | Hiểu app làm gì trong 1 câu · Đi hết 5 bước dưới 2 phút · Bỏ qua từng bước xin quyền · Hiểu vì sao app cần từng quyền · Hoàn tất mà chưa cấp quyền nào · Quay lại bước trước | UC-001, UC-004, UC-005 | No (một lần) | F5, F1, F3, và **không** liên quan F7 (cấm paywall trong onboarding) |
| **F7 — Paywall & Trial 7 ngày** | Xem 3 bậc giá cùng gói Free hiện tại · Xác nhận giá cuối bằng tiền tệ địa phương · Bắt đầu trial 7 ngày · Biết chính xác ngày hết trial và ngày trừ tiền · Nhận nhắc ngày 6 và ngày 7 · Huỷ trial trước khi bị trừ · Mua Lifetime một lần · Quản lý đăng ký đang có · Phục hồi giao dịch đã mua | UC-025 → UC-030 | No (một lần, cộng 1 lần nhắc) | F4 (Free là bậc thứ tư trên paywall), F10 (event funnel) |
| **F8 — AI sắp xếp dashboard** | Xem dashboard tự đổi theo ngữ cảnh · Chạm thẻ gợi ý để thực hiện · Bỏ qua gợi ý sai · Không phải tự cấu hình bất cứ gì · Nhận gợi ý tốt hơn sau vài ngày dùng | UC-022, UC-023 | **Yes** | F3 (dùng chung ContextEngine), F2 (thẻ nằm trên dashboard CarPlay) |
| **F9 — Localize EN/ES/PT-BR** | Đổi ngôn ngữ app · Nhận nội dung giọng chào theo ngôn ngữ đã chọn · Thấy giá theo tiền tệ địa phương · Dùng ngôn ngữ hệ thống làm mặc định | UC-031 (+ AC trong UC-026, UC-021) | No (một lần) | F3, F7, F1 |
| **F10 — Analytics & Telemetry** | Ghi nhận render thành công/thất bại kèm kích thước màn hình · Ghi nhận hoàn tiền · Người dùng gửi báo cáo tương thích chủ động · Không gửi PII · Người dùng xoá được toàn bộ dữ liệu on-device | UC-017, UC-032 | Ngầm (không có UI hằng ngày) | F2 (R-11), F7 (R-12), quyền riêng tư PRD §9 |
| **F11 — Crash Reporting** (P1) | Tự động thu crash · Không có bề mặt người dùng | Không tạo UC — công cụ nội bộ | — | Được phủ bằng NFR ở `Functional_Requirements.md` |
| **F12 — Giám sát sentiment review** (P1) | Job hằng tuần đọc 50 review · Không có bề mặt người dùng. Sub-feature **có** bề mặt: mời người dùng đánh giá trong app sau khoảnh khắc tích cực | UC-033 | No | F10 |
| **F13 — Contacts Shortcuts** (MVP 2) | Đọc Contacts · Lưu 5 favorite · Gọi 1 chạm từ CarPlay | UC-034 | Yes (ở MVP 2) | F2 (shortcut nằm trên dashboard) |
| **Cloud sync (MVP 3)** | Đăng nhập email · Đồng bộ cấu hình giữa thiết bị · Đăng xuất và xoá dữ liệu cloud | UC-035 | No | UC-032 |

**Explosion Rule Check:**
- Tổng feature PRD được bung: **13** (F1–F13) + 1 nhóm post-MVP (Cloud sync)
- Tổng sub-feature phát hiện: **62** → ngưỡng ≥ 3 × 13 = 39 ⇒ **Pass**
- Tổng UC candidate: **41** (trước khi gộp/tỉa)
- UC thực tế sau khi gộp và tỉa: **36** (UC-001 → UC-036; UC-036 được bổ sung sau khi rà soát hành động phụ ở §4.12 — xem ghi chú ở cuối UC-036)
- Feature nào chỉ ra 1 UC? F5 ra 2, F9 ra 1 UC riêng + 2 AC gắn vào UC khác, F12 ra 1. **F11 cố tình không có UC** — nó không có bề mặt người dùng, được phủ bằng NFR ở Step 4. Đây là quyết định có chủ ý, không phải thiếu sót.
- **Passes? Yes**

### 0.2 Repetition Audit

Bảy nhóm hành động dưới đây là những hành động mà nếu chỉ tồn tại ở một chỗ thì trải nghiệm sẽ nghèo và người dùng sẽ không tìm thấy đúng lúc họ cần.

| Action | Position 1 (Primary) | Position 2 (Contextual) | Position 3 (Discoverable) | Expression Difference |
|---|---|---|---|---|
| **Nâng cấp / Đăng ký** (UC-025) | WF-010 Paywall — trang giá đầy đủ, 4 bậc | WF-007 Thư Viện Âm Thanh — nhãn khoá trên preset, chạm vào mở paywall theo ngữ cảnh sound | WF-018 CarPlay Trạng thái Free — **một dòng chữ tĩnh, không popup, không chắn nội dung** | Position 1 là quyết định chủ động (Full CTA, mật độ thông tin cao). Position 2 là khoảnh khắc nhận ra giá trị (Inline Action, chỉ nói về đúng preset vừa chạm). Position 3 xảy ra **khi đang lái** ⇒ bắt buộc là thông báo thụ động, không tương tác, vì mọi thứ chắn nội dung lúc lái xe đều là lỗi an toàn |
| **Nghe thử âm thanh** (UC-006) | WF-020 Sheet Nghe Thử — nghe và áp dụng ngay | WF-004 Onboarding Chọn Âm Thanh — nghe thử ngay trong onboarding, **không cần trả tiền** | WF-007 Thư Viện Âm Thanh — chạm dòng để nghe inline, không mở sheet | Position 1 là sheet tập trung có nút áp dụng. Position 2 là bước bắt buộc trong luồng tuyến tính, chỉ nghe rồi tiếp. Position 3 là nghe nhanh khi đang duyệt danh sách (Compact Row), không rời khỏi danh sách |
| **Đổi widget đang dùng** (UC-012) | WF-008 Trình Tạo Widget — chọn loại, chọn ảnh, lưu | WF-006 Home — thẻ widget hiện tại, chạm để đổi nhanh | WF-023 Modal Preview — đổi ngay trong lúc đang xem preview theo tỉ lệ xe | Position 1 là luồng tạo đầy đủ. Position 2 là lối tắt cho người đã biết mình muốn gì (Inline Action trên thẻ). Position 3 là sửa ngay khi vừa thấy preview bị lệch — sửa tại nơi phát hiện vấn đề |
| **Chẩn đoán / Báo lỗi tương thích** (UC-017) | WF-014 Chẩn Đoán Tương Thích — màn hình đầy đủ, hiện kích thước scene nhận được | WF-019 CarPlay Fallback Lỗi — hướng dẫn mở màn Chẩn Đoán trên iPhone | WF-028 Sheet Gửi Báo Cáo — gửi báo cáo kèm dữ liệu kỹ thuật | Position 1 là nơi tra cứu chủ động. Position 2 là nơi lỗi **thật sự xảy ra** nhưng người dùng đang lái nên chỉ được đọc, không được thao tác. Position 3 là hành động gửi, tách riêng để người dùng thấy rõ dữ liệu gì sẽ được gửi đi |
| **Điều chỉnh âm lượng sound** (UC-009) | WF-012 Cài Đặt Chung — slider âm lượng sound độc lập | WF-020 Sheet Nghe Thử — điều chỉnh ngay trong lúc nghe thử | WF-007 Thư Viện Âm Thanh — nút âm lượng ở thanh trên | Position 1 là cấu hình bền vững. Position 2 là điều chỉnh trong lúc đang nghe, phản hồi tức thì (Stepper/Slider inline). Position 3 là lối vào nhanh khi đang duyệt |
| **Xem / quản lý đăng ký** (UC-029) | WF-025 Sheet Quản Lý Đăng Ký | WF-012 Cài Đặt Chung — dòng "Đăng ký của tôi" kèm trạng thái | WF-013 Nhắc Hết Trial — nút "Huỷ trial" đặt ngang hàng với "Đăng ký" | Position 1 là nơi thao tác. Position 2 là nơi tra trạng thái (Compact Row có chevron). Position 3 là khoảnh khắc quyết định — **nút huỷ phải ngang hàng với nút mua**, không ẩn, vì đây là biện pháp chống R-12 |
| **Đánh giá / Phản hồi** (UC-033) | WF-030 Overlay — biến thể "mời đánh giá" sau khoảnh khắc tích cực | WF-012 Cài Đặt Chung — dòng "Đánh giá Carbina" | WF-028 Sheet Gửi Báo Cáo — kênh phản hồi khi có vấn đề, tách khỏi kênh đánh giá | Position 1 là chủ động mời, có thời điểm (sau khi sound phát thành công ≥ 5 lần). Position 2 là luôn có sẵn cho người muốn tự tìm. Position 3 phân luồng người đang **không** hài lòng sang kênh sửa lỗi thay vì đẩy họ ra App Store — đây là biện pháp trực tiếp cho KPI Recent 1★ Ratio |
| **Xoá dữ liệu on-device** (UC-032) | WF-029 Alert Xác Nhận Xoá | WF-012 Cài Đặt Chung — dòng "Quyền riêng tư & dữ liệu" | — (chỉ 2 vị trí) | Hành động phá hủy, **cố ý chỉ có 2 vị trí** — xem justification bên dưới |

**Audit Rule Check:**
- Hành động chỉ có 1 vị trí: **không có**.
- Hành động chỉ có 2 vị trí, đã cân nhắc và giữ nguyên:
  - **Xoá dữ liệu on-device (UC-032)** — hành động không hoàn tác được. Đặt ở nhiều nơi làm tăng nguy cơ chạm nhầm. Hai vị trí là mức tối thiểu đúng: một nơi tra cứu, một nơi xác nhận.
  - **Xác nhận giá (UC-026)** — cố ý **chỉ tồn tại ở WF-011**, đúng một vị trí duy nhất trên đường đến giao dịch. Nhân bản màn xác nhận giá sẽ tạo ra khả năng có một đường mua **bỏ qua** nó, và đó chính là lỗ hổng đã khiến đối thủ bị tố bait-and-switch (R-12). Đây là trường hợp mà lặp lại là có hại.
- Hành động **cấm lặp lại**: paywall trong onboarding (WF-002 → WF-005) và paywall ở lần mở app đầu tiên. Đây là ràng buộc cứng từ F4/F6, không phải lựa chọn thiết kế.

### 0.3 Screen Architecture Canvas

```
App Root (Carbina)
│
├── System Screens
│   ├── WF-001: Splash / Launch (Consumption)
│   └── WF-030: Toast Xác Nhận — overlay dùng chung (Consumption)
│
├── Onboarding Flow (tuyến tính, ≤ 5 bước — F6)
│   ├── WF-002: Onboarding — Welcome (Discovery)
│   ├── WF-003: Onboarding — Chọn Xe (Action)
│   ├── WF-004: Onboarding — Chọn Âm Thanh (Discovery)
│   └── WF-005: Onboarding — Cấp Quyền (Action)
│
├── Tab 1: Home — hub trạng thái (Management)
│   ├── WF-006: Home (iPhone)
│   └── WF-014: Chẩn Đoán Tương Thích (Management)
│
├── Tab 2: Sounds (Discovery)
│   └── WF-007: Thư Viện Âm Thanh
│
├── Tab 3: Widgets (Management)
│   ├── WF-008: Trình Tạo Widget
│   └── WF-009: Cài Đặt Giọng Chào (Action)
│
├── Tab 4: Settings (Management)
│   ├── WF-012: Cài Đặt Chung
│   └── WF-015: Account (Phase 3 — MVP 3)
│
├── Monetization Flow
│   ├── WF-010: Paywall (Action)
│   ├── WF-011: Xác Nhận Giá (Action)
│   └── WF-013: Nhắc Hết Trial (Action)
│
├── CarPlay Surface (root độc lập, không phải con của app iPhone)
│   ├── WF-016: CarPlay Dashboard (Discovery)
│   ├── WF-017: CarPlay Widget (Consumption)
│   ├── WF-018: CarPlay — Trạng Thái Free (Consumption)
│   └── WF-019: CarPlay — Fallback Lỗi (Consumption)
│
└── Modals & Overlays (màn hình hạng nhất, có WF-ID riêng)
    ├── WF-020: Sheet — Nghe Thử Âm Thanh
    ├── WF-021: Sheet — "Không tìm thấy xe của tôi"
    ├── WF-022: Sheet — Lý Do Xin Quyền (biến thể Location / Calendar)
    ├── WF-023: Modal — Preview Widget Theo Màn Hình Xe
    ├── WF-024: Sheet — Chọn Ảnh Cho Widget
    ├── WF-025: Sheet — Quản Lý Đăng Ký
    ├── WF-026: Sheet — Chọn Ngôn Ngữ
    ├── WF-027: Alert — Xác Nhận Huỷ Trial
    ├── WF-028: Sheet — Gửi Báo Cáo Tương Thích
    └── WF-029: Alert — Xoá Dữ Liệu On-Device
```

**Screen Count**: **30 màn hình** (19 màn hình chính + 11 modal/overlay) — ngưỡng Medium là ≥ 25 ⇒ **Pass**.

**Quan hệ với PRD §10**: PRD liệt kê 18 màn hình. Tài liệu này giữ đủ 18 màn đó và bổ sung 12 màn: 1 splash, 1 overlay xác nhận dùng chung, 10 modal/sheet/alert. Toàn bộ phần bổ sung là **modal và sheet vốn đã ẩn trong mô tả của PRD** (ví dụ "có ô không tìm thấy xe của tôi", "nêu rõ lý do từng quyền", "preview theo đúng tỉ lệ màn hình xe của user") — chúng được nâng thành màn hình hạng nhất vì có state, entry/exit và UC riêng.

**Ánh xạ PRD §10 → WF-ID**: PRD 1→WF-002 · 2→WF-003 · 3→WF-004 · 4→WF-005 · 5→WF-006 · 6→WF-007 · 7→WF-008 · 8→WF-009 · 9→WF-010 · 10→WF-011 · 11→WF-012 · 12→WF-013 · 13→WF-014 · 14→WF-015 · 15→WF-016 · 16→WF-017 · 17→WF-018 · 18→WF-019.

**Ba nguyên tắc kiến trúc màn hình riêng của app này:**
1. **CarPlay là root độc lập, không phải một tab.** Scene CarPlay có thể active khi app iPhone đang background. Không có màn hình CarPlay nào là "con" của màn hình iPhone.
2. **Màn hình CarPlay không có modal, không có popup.** Mọi thông tin phụ phải nằm inline. Đây là ràng buộc an toàn, và cũng là lý do WF-018 chỉ là một dòng chữ chứ không phải một sheet nâng cấp.
3. **Độ sâu tối đa 3 tầng** (Tab → Section → Detail/Modal). Không có màn hình nào cần cuộn qua 3 lần chạm để tới.

### 0.4 Context Storming Highlights

| UC | First-Time User | Returning User | Power User / Edge Case |
|---|---|---|---|
| UC-001 Hoàn tất onboarding | Chính là ngữ cảnh gốc: 5 bước có tiến trình rõ, mỗi bước 1 việc | Không gặp lại; nếu cài lại thì cấu hình cũ được phục hồi từ Keychain nếu có giao dịch | Bỏ qua toàn bộ quyền, hoàn tất trong 40 giây và vẫn có widget chạy được |
| UC-002 Chọn xe | Danh sách hãng theo mức phổ biến ở storefront hiện tại, không theo thứ tự chữ cái | Xe đã chọn hiện sẵn ở đầu; đổi xe là 2 chạm từ WF-006 | Xe không có trong thư viện → WF-021, và **vẫn đi tiếp được** với ảnh xe chung |
| UC-006 Nghe thử âm thanh | Nghe được ngay 3 preset Free, preset khoá có nhãn rõ chứ không ẩn | Nghe nhanh inline ngay trong danh sách, không mở sheet | Nghe thử khi đang cắm tai nghe hoặc đang phát nhạc → phải nghe được ducking thật, không phải nghe khô |
| UC-010 Nghe sound khi lên xe | Lần đầu lên xe sau khi cài: sound phát và app ghi `sound_played` — đây là khoảnh khắc chứng minh giá trị | Phát trong ≤ 1,5s, người dùng không cần mở app | Đang có cuộc gọi → **bỏ hẳn lượt phát**, không chèn vào cuộc gọi; đang phát podcast → duck rồi phục hồi đúng vị trí |
| UC-012 Tạo widget | Có preset gợi ý theo xe vừa chọn để không phải bắt đầu từ màn trắng — **tuyệt đối không bắt người dùng tự dựng widget từ đầu** (khác đối thủ) | Đổi widget từ thẻ trên WF-006, 2 chạm | Ảnh cá nhân tỉ lệ lạ → tự crop theo tỉ lệ màn hình xe và báo trước vùng sẽ bị cắt |
| UC-015 Xem widget trên xe | Lần đầu cắm xe: widget render, app ghi `widget_render_ok` kèm kích thước | Không thao tác gì; widget đã đúng | **Render thất bại → WF-019**, không bao giờ là màn trắng; app ghi `widget_render_failed` kèm `failure_reason` |
| UC-021 Nghe giọng chào | Câu chào lần đầu chỉ dùng ngữ cảnh giờ (chưa có quyền, chưa có dữ liệu) | Sau vài ngày có thêm ngữ cảnh tuyến đường và lịch; ≥ 4 biến thể, không lặp 2 lần liên tiếp | Từ chối hết quyền → vẫn có câu chào theo giờ, không im lặng và không báo lỗi |
| UC-022 Xem dashboard | Thẻ theo thứ tự mặc định, kèm một dòng giải thích "dashboard sẽ tự đổi sau vài chuyến" | Thứ tự thẻ đã học được từ hành vi; thẻ hay dùng lên đầu | Ngữ cảnh đoán sai (gợi ý về nhà lúc đang đi công tác) → bỏ qua gợi ý là hành động rẻ nhất, không cần vào Settings để sửa |
| UC-024 Dùng gói Free | **Không thấy paywall ở lần mở app đầu tiên** — bắt buộc | Vẫn dùng Free vô thời hạn, không bị nhắc lặp lại | Đã dùng Free 30 ngày và widget chạy tốt → đây mới là thời điểm hợp lý để đề nghị nâng cấp |
| UC-026 Xác nhận giá | Lần đầu thấy giá: hiện **giá cuối bằng tiền tệ địa phương**, ngày hết trial, ngày trừ tiền | Không gặp lại nếu đã mua | Đổi vùng App Store giữa lúc mua → giá được đọc lại từ StoreKit, không dùng giá đã cache |
| UC-028 Nhắc hết trial | Ngày 6 và ngày 7, nêu số tiền chính xác và ngày trừ | — | Huỷ trial ngay từ màn nhắc, **nút huỷ ngang hàng nút đăng ký** |
| UC-031 Đổi ngôn ngữ | Mặc định theo ngôn ngữ hệ thống; nếu hệ thống không phải EN/ES/PT-BR thì về EN | Đổi trong Settings, áp dụng ngay không cần khởi động lại | Đổi ngôn ngữ khi đang cắm CarPlay → nội dung giọng chào đổi từ lượt phát kế tiếp, không cắt lượt đang phát |

**Rule Check**: mọi UC ở §2 đều có đủ 3 biến thể ngữ cảnh trong phần **Context Variations** của chính UC đó. Bảng trên là bản trích những UC có biến thể đáng chú ý nhất; không có UC nào chỉ có 1 biến thể.

---

## 1. Introduction

### 1.1 Purpose

Tài liệu này mô tả người dùng tương tác với **Carbina** như thế nào trong hoàn cảnh thật, ở hai bề mặt có ràng buộc hoàn toàn khác nhau: **app iPhone** (nơi cấu hình, người dùng đang đứng yên, có thể đọc và gõ) và **màn hình CarPlay** (nơi sử dụng, người dùng đang lái, chỉ được nhìn thoáng và chạm một lần). Mỗi UC được gắn với màn hình cụ thể và với task flow, để `Wireframes.md` và `UX_Flows.md` ở bước sau có đủ đầu vào mà không phải suy diễn.

Tài liệu này **không** định nghĩa lại đặc tả tính năng (thuộc `Functional_Requirements.md`) và **không** mô tả layout (thuộc `Wireframes.md`).

### 1.2 Scope

- Phủ toàn bộ 10 feature hướng người dùng của MVP 1 (F1–F10 trong PRD §7) — mỗi feature có ít nhất một UC.
- Phủ 2 UC post-MVP để cây màn hình không phải đập đi làm lại ở MVP 2/MVP 3: UC-034 (Contacts, MVP 2) và UC-035 (Cloud sync, MVP 3). Hai UC này được đánh dấu rõ và **không** nằm trong phạm vi thi công MVP 1.
- F11 (Crash Reporting) không có UC vì không có bề mặt người dùng — nó sẽ xuất hiện dưới dạng NFR ở Step 4.
- 36 UC · 30 màn hình · 13 task flow · 21 sub-flow · 18 scenario.

### 1.3 Document Conventions

- **UC-XXX**: Use Case (tuần tự: UC-001 → UC-036)
- **AF-XXX.Y**: Alternative Flow — luồng thay thế hoặc luồng lỗi của UC-XXX
- **AC-XXX.Y**: Acceptance Criterion, viết theo **EARS notation** (WHEN … THEN … / IF … THEN …). AC gắn với UC (không gắn với FR); `Functional_Requirements.md` sẽ mang nguyên các AC này sang, không đánh số lại
- **WF-XXX**: màn hình Wireframe (tạm thời trong tài liệu này; sẽ được `Wireframes.md` chốt lại — ánh xạ với PRD §10 đã ghi ở §0.3)
- **TF-XXX**: Task Flow — hành trình xuyên nhiều màn hình
- **SF-XXX**: Sub-Flow — tương tác **bên trong** một màn hình
- **Ký hiệu bề mặt**: 📱 = màn hình iPhone · 🚗 = màn hình CarPlay. Mọi UC có ký hiệu 🚗 đều chịu ràng buộc "người dùng đang lái": không modal, không nhập liệu, không quá 1 chạm.

---

## 2. User Stories by Feature Group

Bảy nhóm dưới đây gom UC theo **feature group của PRD §7**, không theo màn hình — vì một feature thường trải trên nhiều màn hình và một màn hình thường phục vụ nhiều feature.

| Nhóm | Tên | PRD Feature | UC |
|---|---|---|---|
| 2.1 | Onboarding & Thiết Lập Xe | F5, F6 | UC-001 → UC-005 |
| 2.2 | Âm Thanh Lên/Xuống Xe | F1 | UC-006 → UC-011 |
| 2.3 | Widget CarPlay & Tương Thích | F2, F10 | UC-012 → UC-017 |
| 2.4 | Giọng Chào AI & Dashboard Ngữ Cảnh | F3, F8 | UC-018 → UC-023 |
| 2.5 | Gói Free, Paywall & Thanh Toán | F4, F7 | UC-024 → UC-030 |
| 2.6 | Ngôn Ngữ, Quyền Riêng Tư & Phản Hồi | F9, F10, F12 | UC-031 → UC-033, UC-036 |
| 2.7 | Post-MVP | F13, Cloud sync | UC-034 → UC-035 |

---

### 2.1 Onboarding & Thiết Lập Xe

#### UC-001: Hoàn tất onboarding trong 5 bước 📱

**As a** người dùng mới (Alex — Tech-Savvy Commuter)
**I want** setup xong dưới 2 phút và hiểu ngay app làm được gì
**So that** tôi thấy giá trị trước khi phải cân nhắc bất cứ chuyện tiền bạc nào

**Priority**: High · **Complexity**: Medium

**Preconditions**:
- App vừa được cài, chưa có cấu hình nào
- Không có yêu cầu đăng nhập hay tạo tài khoản

**Main Flow**:
1. Người dùng mở app → WF-001 Splash hiện ≤ 1,5s rồi chuyển WF-002.
2. WF-002 giới thiệu app trong 1 câu + nút "Bắt đầu"; thanh tiến trình hiện 1/4.
3. Người dùng chạm "Bắt đầu" → WF-003 Chọn Xe (xem UC-002).
4. Sau khi chọn xe → WF-004 Chọn Âm Thanh (xem UC-006).
5. Sau khi chọn sound → WF-005 Cấp Quyền (xem UC-004).
6. Hoàn tất → WF-006 Home, hiện trạng thái "Chưa kết nối CarPlay" kèm hướng dẫn cắm xe.

**Alternative Flows**:
- **AF-001.1** — Người dùng thoát app giữa onboarding: tiến trình được lưu; lần mở lại vào đúng bước đang dở, không bắt đầu lại từ WF-002.
- **AF-001.2** — Người dùng chạm nút quay lại: về bước trước, giữ nguyên lựa chọn đã làm.
- **AF-001.3** — Cài lại app sau khi đã từng mua: sau WF-002 hiện dòng "Phục hồi giao dịch"; nếu phục hồi thành công thì bỏ qua WF-004 phần khoá preset.

**Postconditions**:
- Có xe đã chọn, có sound connect đã gán, trạng thái quyền đã xác định (dù là bị từ chối)
- Người dùng ở WF-006 và có ít nhất 1 widget sẵn dùng ở gói Free

**Acceptance Criteria**:
- **AC-001.1**: WHEN người dùng mở app lần đầu THEN hệ thống hiển thị WF-002 và **không** hiển thị WF-010 Paywall tại bất kỳ bước nào của onboarding.
- **AC-001.2**: WHEN người dùng đi hết 4 bước không bỏ qua gì THEN tổng thời gian tối thiểu cần thiết ≤ 120 giây.
- **AC-001.3**: IF người dùng thoát app ở bước N THEN lần mở kế tiếp hệ thống hiển thị đúng bước N.
- **AC-001.4**: WHEN onboarding hoàn tất THEN hệ thống ghi `onboarding_completed`; tỉ lệ hoàn tất mục tiêu ≥ 70%.
- **AC-001.5**: WHEN người dùng ở bất kỳ bước nào của onboarding THEN thanh tiến trình hiển thị đúng số bước còn lại.

**Screens Involved**: WF-001, WF-002, WF-003, WF-004, WF-005, WF-006
**Primary Screen**: WF-002
**Entry Point**: Mở app lần đầu (từ WF-001)
**Exit Point**: WF-006 Home

**Context Variations**:
- **First-time user**: đây chính là ngữ cảnh gốc — mỗi bước làm đúng một việc, có tiến trình rõ.
- **Returning user**: không gặp lại onboarding; nếu cài lại thì AF-001.3 phục hồi giao dịch.
- **Power user / Edge case**: bỏ qua toàn bộ quyền ở WF-005, hoàn tất trong ~40 giây và vẫn có widget chạy được.

---

#### UC-002: Chọn xe của mình (hãng → model → năm) 📱

**As a** chủ xe
**I want** chọn đúng xe của tôi
**So that** widget hiển thị hình xe giống xe thật của tôi

**Priority**: High · **Complexity**: Low

**Preconditions**: người dùng đang ở WF-003 (trong onboarding) hoặc mở lại từ WF-006

**Main Flow**:
1. WF-003 hiện danh sách hãng, sắp theo mức phổ biến ở storefront hiện tại + ô tìm kiếm.
2. Người dùng chọn hãng → danh sách model của hãng đó (sub-flow SF-002).
3. Người dùng chọn model → chọn năm.
4. Hệ thống hiện ảnh xe tương ứng để người dùng đối chiếu, kèm nút "Đúng xe của tôi".
5. Người dùng xác nhận → chuyển bước kế tiếp.

**Alternative Flows**:
- **AF-002.1** — Không tìm thấy hãng/model: người dùng chạm "Không tìm thấy xe của tôi" → WF-021 (xem UC-003).
- **AF-002.2** — Người dùng muốn đổi xe sau này: từ WF-006 chạm thẻ xe → quay lại WF-003, giữ nguyên mọi cấu hình widget và sound đã có.
- **AF-002.3** — Ảnh xe của model đó chưa có trong bộ asset: dùng ảnh silhouette theo phân khúc (sedan/SUV/pickup) và ghi nhận thiếu asset.

**Postconditions**: xe (hãng + model + năm) được lưu on-device; ảnh xe được gán cho widget mặc định

**Acceptance Criteria**:
- **AC-002.1**: WHEN người dùng mở WF-003 THEN thư viện chứa ≥ 40 hãng và ≥ 400 model.
- **AC-002.2**: WHEN người dùng chọn hãng, model và năm THEN hệ thống lưu cả ba giá trị và hiển thị ảnh xe tương ứng.
- **AC-002.3**: WHEN ảnh xe được hiển thị trên màn hình CarPlay THEN ảnh phải ở độ phân giải đủ để không bị mờ ở kích thước màn hình lớn nhất trong test matrix.
- **AC-002.4**: IF model của người dùng không có trong thư viện THEN hệ thống vẫn cho phép đi tiếp và dùng ảnh silhouette theo phân khúc.
- **AC-002.5**: WHEN người dùng gõ vào ô tìm kiếm THEN kết quả được lọc trong ≤ 200ms và **không** yêu cầu kết nối mạng.
- **AC-002.6**: IF trim và color được người dùng tìm THEN hệ thống nêu rõ hai thuộc tính này thuộc MVP 3, không hiển thị lựa chọn rỗng.

**Screens Involved**: WF-003, WF-021, WF-006
**Primary Screen**: WF-003
**Entry Point**: WF-002 (onboarding bước 2) hoặc thẻ xe trên WF-006
**Exit Point**: WF-004 (nếu trong onboarding) hoặc WF-006 (nếu đổi xe sau)

**Context Variations**:
- **First-time user**: danh sách hãng theo mức phổ biến, không theo thứ tự chữ cái — giảm số lần cuộn.
- **Returning user**: xe đã chọn hiện ở đầu danh sách; đổi xe là 2 chạm từ WF-006.
- **Power user / Edge case**: xe rất mới hoặc xe nội địa không có trong thư viện → AF-002.1 + AF-002.3, và luồng **không** bị chặn.

---

#### UC-003: Báo xe không có trong thư viện 📱

**As a** chủ xe có xe không phổ biến
**I want** báo cho nhà phát triển biết xe của tôi bị thiếu
**So that** xe của tôi được thêm vào và tôi biết yêu cầu của mình đã tới

**Priority**: Medium · **Complexity**: Low

**Preconditions**: người dùng đang ở WF-003 và đã thử tìm nhưng không thấy xe

**Main Flow**:
1. Người dùng chạm "Không tìm thấy xe của tôi" → WF-021 mở dạng sheet.
2. Sheet hiện 3 ô: hãng, model, năm (điền sẵn phần đã gõ ở WF-003).
3. Người dùng chạm "Gửi" → hệ thống gửi request vào backlog và hiện WF-030 (toast "Đã nhận, cảm ơn bạn").
4. Sheet đóng, người dùng quay về WF-003 và có thể chọn phân khúc xe để đi tiếp.

**Alternative Flows**:
- **AF-003.1** — Không có mạng: request được xếp hàng on-device và gửi khi có mạng; toast vẫn hiện xác nhận đã ghi nhận.
- **AF-003.2** — Người dùng đóng sheet mà không gửi: quay về WF-003, không mất phần đã gõ.

**Postconditions**: request được ghi nhận (cục bộ hoặc đã gửi); người dùng vẫn hoàn tất được việc chọn xe bằng phân khúc

**Acceptance Criteria**:
- **AC-003.1**: WHEN người dùng gửi request THEN hệ thống xác nhận bằng WF-030 trong ≤ 500ms, không chờ phản hồi mạng.
- **AC-003.2**: IF không có kết nối mạng THEN request được lưu on-device và gửi lại khi có mạng, không mất dữ liệu.
- **AC-003.3**: WHEN request được gửi THEN nội dung **không** chứa PII nào ngoài ba giá trị hãng/model/năm do người dùng tự gõ.

**Screens Involved**: WF-021, WF-003, WF-030
**Primary Screen**: WF-021
**Entry Point**: nút "Không tìm thấy xe của tôi" trên WF-003
**Exit Point**: WF-003 (tiếp tục onboarding)

**Context Variations**:
- **First-time user**: gặp trong onboarding — sheet phải ngắn, 3 ô, không bắt buộc mô tả thêm.
- **Returning user**: gặp khi đổi sang xe mới mua; sheet nhớ hãng đã gửi trước đó để tránh gửi trùng.
- **Power user / Edge case**: gửi nhiều request liên tiếp → hệ thống gộp và không gửi trùng cùng một hãng/model/năm.

---

#### UC-004: Cấp quyền sau khi hiểu rõ lý do 📱

**As a** người dùng quan tâm quyền riêng tư
**I want** biết chính xác app dùng từng quyền để làm gì trước khi tôi đồng ý
**So that** tôi cấp quyền một cách có ý thức thay vì bấm bừa

**Priority**: High · **Complexity**: Medium

**Preconditions**: người dùng đang ở WF-005; chưa có quyền nào được cấp

**Main Flow**:
1. WF-005 liệt kê 2 quyền: Vị trí và Lịch, mỗi quyền có một dòng nêu **app dùng nó để làm gì** và một dòng nêu **dữ liệu không rời thiết bị**.
2. Người dùng chạm "Tìm hiểu thêm" ở một quyền → WF-022 mở dạng sheet với biến thể tương ứng (Location hoặc Calendar).
3. Người dùng chạm "Cho phép" → hệ thống gọi dialog quyền của iOS.
4. Người dùng trả lời dialog iOS → WF-005 cập nhật trạng thái từng quyền (Đã cấp / Đã từ chối / Chưa hỏi).
5. Người dùng chạm "Tiếp tục" → WF-006.

**Alternative Flows**:
- **AF-004.1** — Người dùng từ chối một quyền: hệ thống nêu rõ tính năng nào sẽ hoạt động ở mức giảm, **không** hiện lại dialog và không chặn bước tiếp.
- **AF-004.2** — Người dùng từ chối cả hai quyền: giọng chào rơi về biến thể chỉ theo giờ; dashboard dùng thứ tự mặc định (xem UC-005).
- **AF-004.3** — Người dùng đổi ý sau này: WF-012 có lối vào Cài đặt hệ thống để cấp lại quyền.

**Postconditions**: trạng thái của cả 2 quyền được xác định và lưu; app dùng được ở mọi tổ hợp trạng thái quyền

**Acceptance Criteria**:
- **AC-004.1**: WHEN WF-005 hiển thị THEN mỗi quyền có nêu lý do cụ thể bằng ngôn ngữ người dùng, không dùng câu chung như "để cải thiện trải nghiệm".
- **AC-004.2**: IF người dùng từ chối một quyền THEN hệ thống **không** hiển thị lại dialog quyền đó trong cùng phiên và vẫn cho phép chạm "Tiếp tục".
- **AC-004.3**: WHEN người dùng cấp quyền Vị trí THEN hệ thống ghi `location_permission_granted`.
- **AC-004.4**: WHEN bất kỳ quyền nào bị từ chối THEN WF-005 hiển thị rõ tính năng nào bị ảnh hưởng và ở mức nào.
- **AC-004.5**: IF người dùng chạm "Tiếp tục" khi chưa trả lời quyền nào THEN hệ thống vẫn chuyển sang WF-006.

**Screens Involved**: WF-005, WF-022, WF-006, WF-012
**Primary Screen**: WF-005
**Entry Point**: WF-004 (onboarding bước 4)
**Exit Point**: WF-006 Home

**Context Variations**:
- **First-time user**: đây là ngữ cảnh gốc, xuất hiện trong onboarding sau khi người dùng đã nghe thử sound — nghĩa là **sau khi đã thấy giá trị**, không phải trước.
- **Returning user**: vào lại từ WF-012 để cấp thêm quyền khi muốn giọng chào thông minh hơn.
- **Power user / Edge case**: người dùng cấp quyền Vị trí ở mức "Khi dùng app" thay vì "Luôn luôn" → hệ thống nêu rõ tuyến đường sẽ chỉ học được khi app đang mở.

---

#### UC-005: Dùng app đầy đủ mức cơ bản dù đã từ chối mọi quyền 📱🚗

**As a** người dùng không muốn cấp quyền nào
**I want** app vẫn chạy được và vẫn có widget lẫn âm thanh
**So that** tôi không bị buộc phải đánh đổi quyền riêng tư để dùng thứ mình đã tải về

**Priority**: High · **Complexity**: Medium

**Preconditions**: cả quyền Vị trí và Lịch đều ở trạng thái bị từ chối

**Main Flow**:
1. Người dùng hoàn tất onboarding mà không cấp quyền nào (AF-004.2).
2. WF-006 hiện trạng thái đầy đủ: widget đang bật, sound đang chọn, xe đã chọn.
3. Người dùng cắm CarPlay → WF-017 widget render bình thường; sound connect phát bình thường.
4. Giọng chào phát ở biến thể chỉ dùng ngữ cảnh giờ trong ngày.
5. WF-016 Dashboard hiện thẻ theo thứ tự mặc định, không có gợi ý điểm đến.

**Alternative Flows**:
- **AF-005.1** — Người dùng thắc mắc vì sao dashboard không đổi: WF-006 và WF-009 có một dòng giải thích cùng lối vào cấp quyền, **không** dùng popup nhắc lặp lại.
- **AF-005.2** — Người dùng cấp quyền sau: ngữ cảnh mới được dùng từ lượt lên xe kế tiếp, không cần khởi động lại app.

**Postconditions**: app hoạt động ở mức cơ bản trên cả hai bề mặt; không có tính năng nào bị chặn hoàn toàn ngoài phần phụ thuộc trực tiếp vào quyền

**Acceptance Criteria**:
- **AC-005.1**: IF mọi quyền đều bị từ chối THEN widget, sound và dashboard cơ bản vẫn hoạt động đầy đủ.
- **AC-005.2**: IF quyền Lịch bị từ chối THEN giọng chào vẫn phát, dùng ngữ cảnh giờ trong ngày, và **không** phát câu báo lỗi.
- **AC-005.3**: WHEN người dùng ở trạng thái không có quyền nào THEN hệ thống hiển thị tối đa **một** lời mời cấp quyền dạng tĩnh trên WF-006, không dùng popup và không nhắc lại theo phiên.
- **AC-005.4**: WHEN người dùng cấp quyền muộn THEN ngữ cảnh mới có hiệu lực từ lần kết nối CarPlay kế tiếp.

**Screens Involved**: WF-006, WF-009, WF-016, WF-017
**Primary Screen**: WF-006
**Entry Point**: hoàn tất onboarding với mọi quyền bị từ chối
**Exit Point**: WF-016 CarPlay Dashboard (khi lên xe)

**Context Variations**:
- **First-time user**: thấy ngay rằng từ chối quyền không làm app vô dụng — đây là tín hiệu tin cậy quan trọng ở một niche đầy app bị coi là scam.
- **Returning user**: dùng mãi ở trạng thái này mà không bị quấy rầy.
- **Power user / Edge case**: người dùng cấp quyền Lịch nhưng từ chối Vị trí → giọng chào dùng lịch, dashboard không có gợi ý điểm đến; hệ thống phải xử lý được mọi tổ hợp một phần.

---

### 2.2 Âm Thanh Lên/Xuống Xe

> Nhóm này phục vụ **F1 — tính năng có PMF cao nhất** theo PRD §6 (được khen ngay trong chính review 1★ của đối thủ). Ba complaint cụ thể của đối thủ được chuyển thành AC ở đây: sound bị nhạc lấn, sound phát qua loa iPhone thay vì loa xe, sound disconnect lệch thời điểm tắt máy.

#### UC-006: Nghe thử âm thanh trước khi chọn 📱

**As a** chủ xe
**I want** nghe thử từng âm thanh trước khi gán nó cho xe của mình
**So that** tôi chọn được âm thanh mình thật sự thích, và biết app có tiếng thật chứ không phải quảng cáo

**Priority**: High · **Complexity**: Low

**Preconditions**: app đã cài; không yêu cầu trả tiền, không yêu cầu quyền nào

**Main Flow**:
1. Người dùng mở WF-007 Thư Viện Âm Thanh (hoặc đang ở WF-004 trong onboarding).
2. Danh sách sound chia theo nhóm; mỗi dòng có tên, thời lượng và nhãn trạng thái (mở / khoá).
3. Người dùng chạm một dòng → sound phát inline, icon chuyển sang trạng thái đang phát (sub-flow SF-003).
4. Người dùng chạm "Chọn" hoặc mở WF-020 để nghe kỹ hơn và điều chỉnh âm lượng.
5. Sound được gán; WF-030 hiện toast xác nhận.

**Alternative Flows**:
- **AF-006.1** — Sound bị khoá (gói Free): vẫn **nghe thử được đầy đủ**, nhưng nút "Chọn" chuyển thành "Mở khoá" dẫn tới WF-010 với ngữ cảnh đúng preset vừa nghe.
- **AF-006.2** — Đang phát nhạc từ app khác: sound thử được phát kèm ducking thật, để người dùng nghe đúng trải nghiệm sẽ có trên xe.
- **AF-006.3** — Người dùng đang cắm tai nghe: hệ thống nêu rõ trên xe âm thanh sẽ phát qua loa xe.
- **AF-006.4** — Chạm dòng khác khi sound đang phát: dừng sound cũ ngay, phát sound mới, không chồng tiếng.

**Postconditions**: người dùng đã nghe ít nhất 1 sound; nếu chạm "Chọn" thì sound được gán cho sự kiện Connect

**Acceptance Criteria**:
- **AC-006.1**: WHEN người dùng chạm một dòng sound THEN sound bắt đầu phát trong ≤ 300ms.
- **AC-006.2**: IF sound thuộc nhóm khoá THEN người dùng vẫn nghe thử được **toàn bộ** sound, không bị cắt ngắn và không bị chèn watermark.
- **AC-006.3**: WHEN thư viện được mở THEN có ≥ 12 preset, trong đó đúng 3 preset thuộc gói Free.
- **AC-006.4**: IF đang có nhạc phát từ app khác THEN lượt nghe thử áp dụng ducking giống hệt lúc chạy thật.
- **AC-006.5**: WHEN người dùng chạm dòng thứ hai trong lúc dòng thứ nhất đang phát THEN sound thứ nhất dừng ngay, không phát chồng.

**Screens Involved**: WF-007, WF-020, WF-004, WF-010, WF-030
**Primary Screen**: WF-007
**Entry Point**: Tab Sounds trên WF-006, hoặc bước 3 của onboarding (WF-004)
**Exit Point**: WF-007 (đã gán) hoặc WF-010 (nếu chọn preset khoá)

**Context Variations**:
- **First-time user**: gặp ở WF-004 trong onboarding, **nghe thử được ngay mà không trả tiền** — đây là điểm khác biệt trực tiếp so với đối thủ.
- **Returning user**: nghe nhanh inline trong danh sách, không mở sheet.
- **Power user / Edge case**: nghe thử khi đang cắm tai nghe hoặc đang phát podcast → AF-006.2, AF-006.3.

---

#### UC-007: Gán âm thanh cho sự kiện Connect 📱

**As a** chủ xe
**I want** chọn âm thanh phát lúc tôi vào xe
**So that** khoảnh khắc lên xe có cảm giác là của riêng tôi

**Priority**: High · **Complexity**: Low

**Preconditions**: người dùng đã nghe thử ≥ 1 sound (UC-006)

**Main Flow**:
1. Ở WF-007 hoặc WF-020, người dùng chạm "Chọn cho lúc lên xe".
2. Hệ thống lưu lựa chọn, ghi vào App Group để widget và CarPlay scene đọc được.
3. WF-030 hiện toast; dòng sound trên WF-006 cập nhật ngay.

**Alternative Flows**:
- **AF-007.1** — Preset khoá: chuyển sang WF-010 (paywall theo ngữ cảnh sound), không gán.
- **AF-007.2** — Người dùng muốn không có sound lúc lên xe: chọn "Không dùng" — đây là lựa chọn hợp lệ, không phải trạng thái lỗi.

**Postconditions**: sound connect được lưu và có hiệu lực từ lần cắm CarPlay kế tiếp

**Acceptance Criteria**:
- **AC-007.1**: WHEN người dùng gán một sound THEN lựa chọn có hiệu lực ở lần `carplay_connected` kế tiếp mà không cần khởi động lại app.
- **AC-007.2**: IF người dùng chọn "Không dùng" THEN hệ thống không phát sound nào lúc connect và **không** hiển thị nhắc nhở về việc này.
- **AC-007.3**: WHEN sound được gán THEN cấu hình được ghi vào App Group container để CarPlay scene đọc được khi app iPhone ở background.

**Screens Involved**: WF-007, WF-020, WF-006, WF-010, WF-030
**Primary Screen**: WF-007
**Entry Point**: WF-007 hoặc WF-020
**Exit Point**: WF-007 (ở lại danh sách) hoặc WF-006

**Context Variations**:
- **First-time user**: gán ngay trong onboarding, mặc định là preset Free đầu tiên nếu người dùng bỏ qua bước này.
- **Returning user**: đổi sound là 2 chạm; sound đang dùng luôn ở đầu danh sách.
- **Power user / Edge case**: chọn "Không dùng" cho Connect nhưng vẫn giữ sound cho Arrive.

---

#### UC-008: Gán âm thanh cho Disconnect và Arrive 📱

**As a** chủ xe
**I want** có âm thanh riêng cho lúc xuống xe và lúc tới nơi
**So that** cả chuyến đi có điểm mở và điểm kết rõ ràng

**Priority**: Medium · **Complexity**: Medium

**Preconditions**: người dùng đang ở WF-007

**Main Flow**:
1. WF-007 có bộ chọn ba sự kiện: Connect · Disconnect · Arrive.
2. Người dùng chuyển sang tab "Disconnect", nghe thử và gán (như UC-006, UC-007).
3. Lặp lại cho "Arrive".
4. WF-006 hiện tóm tắt cả ba sự kiện đã gán.

**Alternative Flows**:
- **AF-008.1** — Người dùng chỉ muốn sound cho Connect: hai sự kiện còn lại để trống, đây là mặc định hợp lệ.
- **AF-008.2** — Không có quyền Vị trí: sự kiện Arrive không xác định được, hệ thống nêu rõ điều này ngay tại chỗ chọn thay vì để người dùng chờ một âm thanh không bao giờ phát.

**Postconditions**: từng sự kiện có sound riêng hoặc rõ ràng là không có

**Acceptance Criteria**:
- **AC-008.1**: WHEN người dùng gán sound cho ba sự kiện THEN mỗi sự kiện lưu độc lập, đổi một cái không ảnh hưởng hai cái còn lại.
- **AC-008.2**: IF quyền Vị trí bị từ chối THEN mục Arrive hiển thị rõ là không khả dụng kèm lý do, và **không** cho gán để tránh kỳ vọng sai.
- **AC-008.3**: WHEN mỗi sound phát THEN hệ thống ghi `sound_played` kèm `sound_type` phân biệt connect/disconnect/arrive.

**Screens Involved**: WF-007, WF-020, WF-006
**Primary Screen**: WF-007
**Entry Point**: WF-007 (bộ chọn sự kiện)
**Exit Point**: WF-006

**Context Variations**:
- **First-time user**: onboarding chỉ hỏi sound Connect; hai sự kiện kia được giới thiệu ở WF-007 sau đó, để không làm onboarding dài quá 5 bước.
- **Returning user**: gán cả ba, mỗi cái một preset khác nhau.
- **Power user / Edge case**: quyền Vị trí bị từ chối → AF-008.2.

---

#### UC-009: Điều chỉnh âm lượng sound độc lập với nhạc 📱

**As a** chủ xe
**I want** đặt âm lượng của sound riêng, không dính vào âm lượng nhạc
**So that** sound không quá to gây giật mình cũng không quá nhỏ đến mức vô nghĩa

**Priority**: High · **Complexity**: Medium

**Preconditions**: đã có ít nhất một sound được gán

**Main Flow**:
1. Người dùng mở WF-012 Cài Đặt Chung (hoặc nút âm lượng trên WF-007 / WF-020).
2. Slider "Âm lượng âm thanh Carbina" hiện giá trị hiện tại kèm nút nghe thử.
3. Người dùng kéo slider → sound mẫu phát ở đúng mức vừa chọn (sub-flow SF-004).
4. Giá trị được lưu ngay, không cần nút Lưu.

**Alternative Flows**:
- **AF-009.1** — Người dùng đặt về 0: tương đương tắt sound; hệ thống nêu rõ điều đó bằng chữ, không để người dùng tưởng app lỗi.
- **AF-009.2** — Âm lượng hệ thống của xe rất thấp: hệ thống nêu rõ âm lượng cuối cùng còn phụ thuộc âm lượng xe.

**Postconditions**: mức âm lượng sound được lưu và áp dụng cho cả ba sự kiện

**Acceptance Criteria**:
- **AC-009.1**: WHEN người dùng đổi âm lượng sound THEN âm lượng nhạc đang phát **không** bị thay đổi.
- **AC-009.2**: WHEN người dùng kéo slider THEN sound mẫu phát ở đúng mức mới trong ≤ 300ms.
- **AC-009.3**: IF âm lượng sound bằng 0 THEN hệ thống hiển thị rõ trạng thái "đang tắt" thay vì để trống.
- **AC-009.4**: WHEN giá trị được đổi THEN nó được lưu ngay và áp dụng ở lần phát kế tiếp trên xe.

**Screens Involved**: WF-012, WF-020, WF-007
**Primary Screen**: WF-012
**Entry Point**: WF-012, hoặc nút âm lượng trên WF-007 / WF-020
**Exit Point**: ở lại màn hình hiện tại

**Context Variations**:
- **First-time user**: dùng giá trị mặc định; slider không xuất hiện trong onboarding để giữ 5 bước.
- **Returning user**: điều chỉnh một lần rồi không sửa nữa.
- **Power user / Edge case**: đặt âm lượng khác nhau theo thói quen mùa (cửa sổ mở/đóng) → hệ thống chỉ cần lưu 1 giá trị, việc đổi phải nhanh (≤ 2 chạm từ WF-006).

---

#### UC-010: Nghe âm thanh khi lên xe mà không bị nhạc lấn 🚗

**As a** chủ xe đang phát nhạc lúc lên xe
**I want** nghe được âm thanh chào của mình rõ ràng rồi nhạc trở lại bình thường
**So that** tính năng tôi trả tiền cho nó thật sự hoạt động, không bị nhạc át đi

**Priority**: High · **Complexity**: High

**Preconditions**: đã gán sound Connect; iPhone kết nối CarPlay; có thể đang phát nhạc hoặc không

**Main Flow**:
1. iPhone kết nối CarPlay → hệ thống nhận `carplay_connected`.
2. Nếu có audio đang phát: hệ thống giảm âm lượng nguồn đó xuống 20%.
3. Sound Connect phát **qua loa xe** trong ≤ 1,5s kể từ thời điểm connect.
4. Sound kết thúc → âm lượng nguồn cũ được phục hồi về đúng mức trước đó.
5. Hệ thống ghi `sound_played` (kèm `music_was_playing`, `output_route`) và `sound_ducking_applied`.

**Alternative Flows**:
- **AF-010.1** — Đang có cuộc gọi: **bỏ hẳn lượt phát**, không chèn tiếng vào cuộc gọi, không phát bù sau khi cuộc gọi kết thúc.
- **AF-010.2** — Đang có dẫn đường phát chỉ dẫn giọng nói: nhường chỉ dẫn, phát sound ngay sau khi chỉ dẫn kết thúc, tối đa chờ 3s rồi bỏ lượt.
- **AF-010.3** — Tuyến đầu ra không phải loa xe: hệ thống vẫn phát và ghi `output_route` để phát hiện sai định tuyến — đây là complaint trực tiếp của đối thủ.
- **AF-010.4** — Connect và disconnect liên tiếp trong 3s (cắm lại dây): chỉ phát 1 lần, không phát 2 lần.

**Postconditions**: sound đã phát (hoặc lượt phát bị bỏ có lý do rõ ràng); âm lượng nguồn cũ được phục hồi nguyên trạng

**Acceptance Criteria**:
- **AC-010.1**: WHEN `carplay_connected` xảy ra THEN sound Connect bắt đầu phát trong ≤ 1,5s.
- **AC-010.2**: IF có audio đang phát THEN hệ thống giảm nguồn đó xuống 20% trong lúc phát sound và phục hồi đúng mức cũ sau khi phát xong.
- **AC-010.3**: WHEN sound phát trên xe THEN tuyến đầu ra là **loa xe**, không phải loa iPhone.
- **AC-010.4**: IF đang có cuộc gọi THEN hệ thống bỏ lượt phát và không phát bù.
- **AC-010.5**: WHEN sound phát xong THEN hệ thống ghi `sound_played` kèm `sound_type`, `music_was_playing`, `output_route`, và ghi `sound_ducking_applied` nếu đã áp dụng ducking.
- **AC-010.6**: IF connect rồi disconnect trong vòng 3s THEN chỉ phát tối đa 1 lần.

**Screens Involved**: WF-016, WF-017 (không có UI riêng — đây là hành vi nền trên bề mặt CarPlay)
**Primary Screen**: WF-016
**Entry Point**: sự kiện hệ thống `carplay_connected`
**Exit Point**: WF-016 CarPlay Dashboard

**Context Variations**:
- **First-time user**: lần cắm xe đầu tiên là khoảnh khắc chứng minh giá trị — nếu lần này thất bại thì gần như không có lần thứ hai.
- **Returning user**: xảy ra 2 lần mỗi ngày, hoàn toàn không cần thao tác.
- **Power user / Edge case**: cuộc gọi, chỉ dẫn dẫn đường, cắm lại dây, tai nghe → AF-010.1 đến AF-010.4.

---

#### UC-011: Nghe âm thanh xuống xe đúng thời điểm tắt máy 🚗

**As a** chủ xe
**I want** nghe âm thanh tạm biệt đúng lúc tôi tắt máy, qua loa xe
**So that** nó là một phần của việc xuống xe, chứ không phải một tiếng lạc lõng phát trong túi tôi

**Priority**: High · **Complexity**: High

**Preconditions**: đã gán sound Disconnect; đang trong phiên CarPlay

**Main Flow**:
1. Người dùng tắt máy → hệ thống nhận tín hiệu ngắt kết nối CarPlay.
2. Sound Disconnect phát **qua loa xe** trước khi phiên audio bị thu hồi.
3. Hệ thống ghi `sound_played` với `sound_type = disconnect` và `output_route`.

**Alternative Flows**:
- **AF-011.1** — Phiên audio bị thu hồi trước khi kịp phát: hệ thống **bỏ lượt phát**, ghi lý do vào telemetry, và **tuyệt đối không** phát bù qua loa iPhone — phát qua loa điện thoại chính là complaint của đối thủ.
- **AF-011.2** — Người dùng chỉ rút dây mà không tắt máy: coi là disconnect bình thường.
- **AF-011.3** — Sự kiện Arrive vừa phát trong 10s trước đó: bỏ sound disconnect để không phát 2 tiếng liền nhau.

**Postconditions**: sound disconnect đã phát qua loa xe, hoặc bị bỏ có ghi nhận lý do

**Acceptance Criteria**:
- **AC-011.1**: WHEN người dùng tắt máy THEN sound Disconnect phát qua **loa xe**, không qua loa iPhone.
- **AC-011.2**: IF phiên audio bị thu hồi trước khi phát được THEN hệ thống bỏ lượt phát và ghi `sound_played` với trạng thái thất bại kèm lý do — **không** phát bù qua loa iPhone.
- **AC-011.3**: WHEN sound Arrive đã phát trong 10s trước đó THEN hệ thống bỏ sound Disconnect.
- **AC-011.4**: WHEN sound Disconnect phát THEN thời điểm phát lệch không quá 1s so với tín hiệu ngắt kết nối.

**Screens Involved**: WF-016, WF-017 (hành vi nền)
**Primary Screen**: WF-016
**Entry Point**: sự kiện hệ thống ngắt kết nối CarPlay
**Exit Point**: kết thúc phiên CarPlay

**Context Variations**:
- **First-time user**: cùng chuyến đầu tiên với UC-010 — hai đầu của cùng một khoảnh khắc.
- **Returning user**: 2 lần/ngày, không thao tác.
- **Power user / Edge case**: xe tắt máy rất nhanh sau khi tới nơi, hoặc rút dây thay vì tắt máy → AF-011.1 đến AF-011.3.

---

### 2.3 Widget CarPlay & Tương Thích

> Nhóm này phục vụ **F2** và **F10**. Đây là nhóm chứa rủi ro cao nhất của dự án (**R-11 — phân mảnh màn hình CarPlay**, complaint kỹ thuật số 1 của đối thủ). Nguyên tắc xuyên suốt: **không có đường nào dẫn tới màn hình trắng**, và mọi lỗi render đều để lại dấu vết đủ để chẩn đoán trong 24h.

#### UC-012: Tạo widget đầu tiên 📱

**As a** chủ xe
**I want** có một widget đẹp trên màn hình xe mà không phải tự dựng từ đầu
**So that** tôi thấy kết quả ngay, không phải học cách dùng một công cụ

**Priority**: High · **Complexity**: Medium

**Preconditions**: đã chọn xe (UC-002); đang ở gói Free hoặc Premium

**Main Flow**:
1. Người dùng mở WF-008 Trình Tạo Widget từ Tab Widgets hoặc từ thẻ trên WF-006.
2. WF-008 hiện **các preset gợi ý theo đúng xe vừa chọn** — không bắt đầu từ màn trắng.
3. Người dùng chọn một loại widget (ảnh xe / ảnh cá nhân / counter).
4. Người dùng chạm "Xem trước trên xe của tôi" → WF-023 Modal Preview (xem UC-013).
5. Người dùng chạm "Lưu" → widget được ghi vào App Group; WF-030 hiện toast; WF-006 cập nhật thẻ widget.

**Alternative Flows**:
- **AF-012.1** — Gói Free đã dùng hết 1 widget: hệ thống nêu rõ giới hạn và cho **đổi** widget hiện có, không chặn hoàn toàn; nút "Thêm widget thứ hai" dẫn tới WF-010.
- **AF-012.2** — Người dùng chọn loại widget thuộc Premium: nghe/xem trước được đầy đủ, nút "Lưu" chuyển thành "Mở khoá" dẫn tới WF-010 với ngữ cảnh đúng loại widget đó.
- **AF-012.3** — Người dùng thoát giữa lúc tạo: bản nháp được giữ; lần mở lại WF-008 hỏi "Tiếp tục widget đang làm?".
- **AF-012.4** — iOS < 17.4 (không hỗ trợ widget CarPlay): WF-008 hiện rõ yêu cầu phiên bản iOS và **vẫn cho cấu hình** để sẵn sàng khi người dùng nâng cấp; không giả vờ là widget đang chạy.

**Postconditions**: có ≥ 1 widget được lưu và ghi vào App Group container; widget sẵn sàng render ở lần cắm CarPlay kế tiếp

**Acceptance Criteria**:
- **AC-012.1**: WHEN người dùng mở WF-008 lần đầu THEN hệ thống hiển thị ≥ 3 preset gợi ý dựa trên xe đã chọn, và **không** hiển thị canvas rỗng.
- **AC-012.2**: WHEN widget được lưu THEN cấu hình được ghi vào App Group container ngay tại thời điểm lưu, không chờ app vào background.
- **AC-012.3**: IF người dùng ở gói Free và đã có 1 widget THEN hệ thống cho phép đổi widget đó và nêu rõ giới hạn 1 widget, không xoá widget đang có.
- **AC-012.4**: IF phiên bản iOS < 17.4 THEN WF-008 nêu rõ widget CarPlay yêu cầu iOS 17.4+, và các tính năng còn lại vẫn dùng được.
- **AC-012.5**: WHEN người dùng dùng widget ở gói Free THEN hệ thống ghi `free_tier_widget_used`.
- **AC-012.6**: WHEN widget được lưu THEN widget ở gói Free là widget **đầy đủ chức năng**, không có watermark và không bị làm mờ.

**Screens Involved**: WF-008, WF-023, WF-024, WF-010, WF-006, WF-030
**Primary Screen**: WF-008
**Entry Point**: Tab Widgets, hoặc thẻ widget trên WF-006
**Exit Point**: WF-006 (đã lưu) hoặc WF-010 (nếu chọn loại Premium)

**Context Variations**:
- **First-time user**: preset gợi ý theo xe vừa chọn — **tuyệt đối không bắt người dùng tự dựng widget**, đây là complaint trực tiếp về đối thủ ("you had to create it yourself").
- **Returning user**: đổi widget bằng 2 chạm từ thẻ trên WF-006.
- **Power user / Edge case**: ảnh cá nhân tỉ lệ lạ → tự crop theo tỉ lệ màn hình xe và báo trước vùng sẽ bị cắt (UC-014).

---

#### UC-013: Xem trước widget theo đúng tỉ lệ màn hình xe của mình 📱

**As a** chủ xe không biết màn hình xe mình bao nhiêu inch
**I want** thấy widget sẽ trông thế nào trên đúng màn hình xe của tôi trước khi lên xe
**So that** tôi không phải ra xe thử rồi mới phát hiện chữ bị cắt

**Priority**: High · **Complexity**: High

**Preconditions**: đang cấu hình widget ở WF-008

**Main Flow**:
1. Người dùng chạm "Xem trước trên xe của tôi" → WF-023 mở dạng modal.
2. Nếu app đã từng nhận được kích thước scene từ xe của người dùng: preview dùng **đúng kích thước thật đó**.
3. Nếu chưa từng cắm xe: preview dùng bộ tỉ lệ tham chiếu của test matrix và nêu rõ đây là ước lượng.
4. Người dùng vuốt ngang để xem widget ở từng tỉ lệ; mỗi tỉ lệ hiện cảnh báo nếu có nội dung vượt vùng an toàn.
5. Người dùng chạm "Dùng bản này" → quay về WF-008 với cấu hình đã chọn.

**Alternative Flows**:
- **AF-013.1** — Có nội dung vượt vùng an toàn ở một tỉ lệ: hệ thống chỉ rõ phần tử nào vượt và đề xuất giảm số phần tử, **không** tự âm thầm cắt.
- **AF-013.2** — Người dùng sửa ngay trong preview: cho đổi loại widget và ảnh tại chỗ, không phải quay về WF-008 (đây là Position 3 trong Repetition Audit §0.2).
- **AF-013.3** — Xe của người dùng có kích thước chưa từng thấy: preview vẫn tính được vì layout dựa trên bounds, không dựa trên danh sách xe.

**Postconditions**: người dùng đã thấy widget ở ≥ 1 tỉ lệ; cấu hình được xác nhận hoặc sửa

**Acceptance Criteria**:
- **AC-013.1**: IF app đã từng nhận kích thước scene từ xe của người dùng THEN WF-023 dùng đúng kích thước đó làm tỉ lệ mặc định của preview.
- **AC-013.2**: IF app chưa từng nhận kích thước scene nào THEN WF-023 nêu rõ preview là ước lượng và hiển thị ≥ 4 tỉ lệ tham chiếu.
- **AC-013.3**: WHEN có phần tử vượt vùng an toàn ở một tỉ lệ THEN hệ thống chỉ rõ phần tử đó và **không** tự cắt nội dung mà không thông báo.
- **AC-013.4**: WHEN preview được hiển thị THEN toàn bộ layout được tính từ tỉ lệ đang chọn tại runtime, không dùng bất kỳ hằng số kích thước nào.

**Screens Involved**: WF-023, WF-008, WF-024
**Primary Screen**: WF-023
**Entry Point**: nút "Xem trước trên xe của tôi" trên WF-008
**Exit Point**: WF-008

**Context Variations**:
- **First-time user**: chưa có kích thước thật ⇒ dùng bộ tỉ lệ tham chiếu và nói thật rằng đây là ước lượng.
- **Returning user**: đã cắm xe ít nhất một lần ⇒ preview dùng kích thước thật của xe họ, chính xác tuyệt đối.
- **Power user / Edge case**: người dùng có 2 xe khác kích thước ⇒ preview cho chọn giữa các kích thước đã từng gặp.

---

#### UC-014: Chọn ảnh xe hoặc ảnh cá nhân cho widget 📱

**As a** người thích tuỳ biến (Sam — Car Enthusiast)
**I want** đặt ảnh xe thật của tôi lên widget
**So that** màn hình xe trông đúng là xe của tôi, không phải một ảnh chung chung

**Priority**: Medium · **Complexity**: Medium

**Preconditions**: đang ở WF-008; nếu chọn ảnh cá nhân thì cần quyền Thư viện ảnh

**Main Flow**:
1. Người dùng chạm ô ảnh → WF-024 Sheet Chọn Ảnh mở ra với hai lựa chọn: ảnh xe theo model đã chọn, hoặc ảnh từ thư viện.
2. Người dùng chọn ảnh từ thư viện → iOS photo picker.
3. Hệ thống crop theo tỉ lệ màn hình xe đang chọn và **hiện trước vùng sẽ bị cắt**.
4. Người dùng điều chỉnh khung crop → chạm "Xong".
5. Ảnh được nén và lưu vào App Group; WF-023 cập nhật preview.

**Alternative Flows**:
- **AF-014.1** — Ảnh có độ phân giải quá thấp: hệ thống cảnh báo ảnh sẽ bị mờ trên màn hình xe và đề nghị chọn ảnh khác — complaint "Looks fairly blurry" của đối thủ.
- **AF-014.2** — Người dùng từ chối quyền thư viện ảnh: chỉ dùng được ảnh xe theo model; nêu rõ lý do, không chặn luồng.
- **AF-014.3** — Ảnh cá nhân là tính năng Premium: xem trước được đầy đủ, lưu thì dẫn tới WF-010.
- **AF-014.4** — Ảnh quá lớn: hệ thống tự giảm kích thước trước khi ghi vào App Group để không vượt ngưỡng bộ nhớ của widget extension.

**Postconditions**: ảnh được gán cho widget, đã crop đúng tỉ lệ, đã nén dưới ngưỡng an toàn cho widget extension

**Acceptance Criteria**:
- **AC-014.1**: WHEN người dùng chọn ảnh cá nhân THEN hệ thống hiển thị vùng sẽ bị cắt **trước** khi lưu.
- **AC-014.2**: IF ảnh có độ phân giải thấp hơn ngưỡng cần cho màn hình xe lớn nhất trong test matrix THEN hệ thống cảnh báo trước khi lưu.
- **AC-014.3**: WHEN ảnh được lưu THEN dung lượng sau nén nằm dưới ngưỡng an toàn của widget extension.
- **AC-014.4**: IF quyền thư viện ảnh bị từ chối THEN người dùng vẫn dùng được ảnh xe theo model và luồng không bị chặn.

**Screens Involved**: WF-024, WF-008, WF-023, WF-010
**Primary Screen**: WF-024
**Entry Point**: ô ảnh trên WF-008 hoặc trong WF-023
**Exit Point**: WF-008 hoặc WF-023

**Context Variations**:
- **First-time user**: mặc định là ảnh xe theo model — có kết quả tốt mà không cần chọn gì.
- **Returning user**: đổi ảnh theo mùa hoặc sau khi rửa xe; luồng phải nhanh, không quá 3 chạm.
- **Power user / Edge case**: ảnh panorama hoặc ảnh dọc → AF-014.1, AF-014.4.

---

#### UC-015: Xem widget hoạt động trên màn hình xe 🚗

**As a** chủ xe
**I want** widget hiển thị đúng và đầy đủ trên màn hình xe của tôi
**So that** thứ tôi cấu hình trên điện thoại thật sự xuất hiện trên xe

**Priority**: High · **Complexity**: High

**Preconditions**: đã lưu ≥ 1 widget; iPhone kết nối CarPlay; iOS ≥ 17.4

**Main Flow**:
1. iPhone kết nối CarPlay → CarPlay scene active; hệ thống đọc bounds từ `CPTemplateApplicationScene`.
2. `WidgetRenderService` tính toàn bộ layout từ bounds vừa đọc.
3. Widget render trên WF-017 với ảnh, chữ và counter theo cấu hình.
4. Hệ thống kiểm tra không có phần tử nào vượt bounds → ghi `widget_render_ok` kèm `screen_width`, `screen_height`, `widget_type`, `car_make`.

**Alternative Flows**:
- **AF-015.1** — Có phần tử vượt bounds: hệ thống **giảm cấp layout** (bỏ phần tử ưu tiên thấp nhất, co chữ theo Dynamic Type, truncate có ellipsis) rồi render lại; nếu vẫn không được thì chuyển WF-019 (UC-016).
- **AF-015.2** — Kích thước bounds chưa từng gặp: vẫn render bình thường vì layout tính tại runtime; ghi kích thước mới vào telemetry.
- **AF-015.3** — Widget extension bị hệ thống thu hồi vì bộ nhớ: chuyển WF-019 và ghi `widget_render_failed` với `failure_reason = memory`, **phân biệt rõ với lỗi vượt bounds**.
- **AF-015.4** — Người dùng ở gói Free: render widget đầy đủ chức năng, kèm WF-018 (một dòng gợi ý nâng cấp, không chắn nội dung).

**Postconditions**: widget hiển thị đúng, hoặc WF-019 hiện thông báo có hướng dẫn; trong mọi trường hợp **không bao giờ là màn hình trắng**

**Acceptance Criteria**:
- **AC-015.1**: WHEN CarPlay scene active THEN layout được tính từ `CPTemplateApplicationScene` bounds tại runtime; **không có hằng số kích thước nào** trong đường render.
- **AC-015.2**: WHEN widget render THEN không có nội dung nào bị cắt ở bất kỳ kích thước nào trong test matrix (≥ 4 kích thước + 1 xe thật mỗi nhóm).
- **AC-015.3**: WHEN chữ dài hơn không gian THEN chữ được truncate có ellipsis, **không** cắt giữa chữ.
- **AC-015.4**: WHEN widget render THEN mọi touch target ≥ 44pt và widget hiển thị đúng ở cả dark mode và light mode.
- **AC-015.5**: WHEN render thành công THEN hệ thống ghi `widget_render_ok` kèm `screen_width`, `screen_height`, `widget_type`.
- **AC-015.6**: IF render thất bại THEN hệ thống ghi `widget_render_failed` kèm `screen_width`, `screen_height`, `widget_type`, `failure_reason` phân biệt được vượt-bounds với hết-bộ-nhớ.
- **AC-015.7**: WHEN tính trên toàn bộ phiên có kết nối CarPlay THEN Widget Render Success Rate ≥ 90% ở tháng 3 và ≥ 95% ở tháng 6.

**Screens Involved**: WF-017, WF-016, WF-018, WF-019
**Primary Screen**: WF-017
**Entry Point**: sự kiện hệ thống `carplay_connected`
**Exit Point**: WF-016 CarPlay Dashboard

**Context Variations**:
- **First-time user**: lần cắm đầu tiên — đây là lần app chứng minh nó chạy được trên xe này; kích thước scene được lưu để dùng cho WF-023 về sau.
- **Returning user**: không thao tác gì, widget đã đúng; kích thước đã biết nên đường render ngắn hơn.
- **Power user / Edge case**: xe đời 2026, Jeep màn 8", Ram Rebel, Audi — những trường hợp đã ghi nhận lỗi ở đối thủ → AF-015.1 đến AF-015.3.

---

#### UC-016: Phục hồi khi widget không render được 🚗

**As a** chủ xe gặp lỗi trên xe
**I want** biết đang có vấn đề và biết phải làm gì, ngay trên màn hình xe
**So that** tôi không nhìn một màn hình trắng và kết luận app này rác

**Priority**: High · **Complexity**: Medium

**Preconditions**: một lần render đã thất bại (AF-015.1 hoặc AF-015.3)

**Main Flow**:
1. Hệ thống chuyển sang WF-019 CarPlay — Fallback Lỗi.
2. WF-019 hiện một thông báo gọn: có vấn đề tương thích với màn hình xe này.
3. WF-019 hướng dẫn mở màn **Chẩn Đoán Tương Thích** trên iPhone — **không** yêu cầu thao tác phức tạp nào trên xe.
4. Hệ thống ghi `widget_render_failed` và đánh dấu phiên này cần chẩn đoán.
5. Lần mở app iPhone kế tiếp, WF-006 hiện một dòng dẫn tới WF-014.

**Alternative Flows**:
- **AF-016.1** — Lỗi tạm thời: lần cắm kế tiếp render lại thành công; dòng nhắc trên WF-006 tự biến mất, không để lại cảnh báo giả.
- **AF-016.2** — Lỗi lặp lại ≥ 3 lần trên cùng kích thước màn hình: hệ thống ưu tiên cao trong telemetry để phát hiện xe không tương thích trong 24h.
- **AF-016.3** — Chỉ widget lỗi nhưng dashboard vẫn được: WF-016 vẫn hoạt động bình thường, chỉ vùng widget bị thay bằng thông báo — **không** hạ toàn bộ bề mặt CarPlay.

**Postconditions**: người dùng đã được thông báo bằng chữ; telemetry đã ghi đủ dữ liệu để chẩn đoán; không có màn hình trắng

**Acceptance Criteria**:
- **AC-016.1**: IF widget không render được THEN hệ thống hiển thị WF-019 với thông báo bằng chữ, và **tuyệt đối không** để lại vùng trắng.
- **AC-016.2**: WHEN WF-019 hiển thị THEN nội dung chỉ để đọc, không yêu cầu người dùng nhập gì và không có modal — vì người dùng đang trong xe.
- **AC-016.3**: WHEN render thất bại THEN lần mở app iPhone kế tiếp hiển thị lối vào WF-014 trên WF-006.
- **AC-016.4**: IF lần render kế tiếp thành công THEN mọi cảnh báo trên WF-006 được xoá tự động.
- **AC-016.5**: IF chỉ widget lỗi THEN WF-016 Dashboard vẫn hoạt động đầy đủ.

**Screens Involved**: WF-019, WF-016, WF-006, WF-014
**Primary Screen**: WF-019
**Entry Point**: render thất bại trong UC-015
**Exit Point**: WF-016 (ở lại trên xe) → WF-014 (khi về dùng iPhone)

**Context Variations**:
- **First-time user**: đây là tình huống tệ nhất có thể xảy ra ở lần cắm đầu tiên — thông báo phải nói rõ **vấn đề nằm ở tương thích màn hình**, không phải "đã xảy ra lỗi".
- **Returning user**: lỗi lẻ một lần rồi hết → AF-016.1, không để lại cảnh báo tồn.
- **Power user / Edge case**: lỗi lặp lại → AF-016.2, và người dùng có đường gửi báo cáo qua UC-017.

---

#### UC-017: Chẩn đoán tương thích và gửi báo cáo 📱

**As a** chủ xe gặp lỗi render (hoặc QA đang kiểm thử)
**I want** xem app nhận được kích thước màn hình xe là bao nhiêu và gửi thông tin đó đi
**So that** vấn đề của xe tôi được sửa, thay vì tôi chỉ còn cách để lại 1 sao

**Priority**: Medium · **Complexity**: Medium

**Preconditions**: app đã từng kết nối CarPlay ít nhất một lần (dù thành công hay thất bại)

**Main Flow**:
1. Người dùng mở WF-014 từ WF-006 (hoặc theo hướng dẫn ở WF-019).
2. WF-014 hiện: kích thước scene đã nhận được, phiên bản iOS, xe đã chọn, trạng thái render của các lần gần nhất.
3. Người dùng chạm "Gửi báo cáo" → WF-028 Sheet mở ra, **liệt kê rõ từng mục dữ liệu sẽ được gửi**.
4. Người dùng chạm "Gửi" → WF-030 toast xác nhận.

**Alternative Flows**:
- **AF-017.1** — Chưa từng kết nối CarPlay: WF-014 nêu rõ chưa có dữ liệu và hướng dẫn cắm xe một lần, thay vì hiện bảng trống.
- **AF-017.2** — Không có mạng: báo cáo xếp hàng on-device và gửi khi có mạng.
- **AF-017.3** — Người dùng muốn thêm mô tả: WF-028 có ô ghi chú tuỳ chọn, tối đa 500 ký tự.
- **AF-017.4** — Người dùng không muốn gửi gì: đóng sheet; dữ liệu chẩn đoán vẫn chỉ nằm trên máy.

**Postconditions**: báo cáo được gửi hoặc xếp hàng; người dùng đã thấy chính xác dữ liệu gì rời khỏi thiết bị

**Acceptance Criteria**:
- **AC-017.1**: WHEN WF-014 mở THEN hệ thống hiển thị kích thước scene thật đã nhận từ xe, không phải giá trị suy đoán.
- **AC-017.2**: WHEN WF-028 mở THEN hệ thống liệt kê **từng mục** dữ liệu sẽ gửi và báo cáo **không** chứa PII.
- **AC-017.3**: IF chưa có dữ liệu kết nối nào THEN WF-014 hiển thị hướng dẫn thay vì bảng trống.
- **AC-017.4**: WHEN báo cáo được gửi THEN người dùng nhận xác nhận trong ≤ 500ms mà không phải chờ mạng.

**Screens Involved**: WF-014, WF-028, WF-030, WF-006, WF-019
**Primary Screen**: WF-014
**Entry Point**: WF-006 (dòng chẩn đoán) hoặc hướng dẫn từ WF-019
**Exit Point**: WF-006

**Context Variations**:
- **First-time user**: hiếm khi tự vào — thường tới đây vì WF-019 dẫn sang.
- **Returning user**: dùng để kiểm tra sau khi đổi xe.
- **Power user / Edge case**: QA dùng màn này như công cụ chính của test matrix R-11 — đây là lý do màn này tồn tại (PRD §10 màn 13).

---

### 2.4 Giọng Chào AI & Dashboard Ngữ Cảnh

> Nhóm này phục vụ **F3** (điểm khác biệt hóa số 1) và **F8**. Cả hai dùng chung `ContextEngine` chạy on-device. Ràng buộc bao trùm: **không có lệnh gọi mạng nào trong đường xử lý ngữ cảnh**, và **R-13 nhắc rằng ý tưởng này đã có người thử và thất bại** ⇒ mọi AC ở đây phải đo được, không dừng ở mức "có tính năng".

#### UC-018: Bật hoặc tắt hoàn toàn giọng chào 📱

**As a** chủ xe
**I want** quyết định app có nói hay không nói
**So that** nó không bao giờ trở thành thứ tôi phải chịu đựng

**Priority**: High · **Complexity**: Low

**Preconditions**: app đã cài; giọng chào bật theo mặc định sau onboarding

**Main Flow**:
1. Người dùng mở WF-009 Cài Đặt Giọng Chào từ Tab Widgets hoặc WF-006.
2. Công tắc chính "Giọng chào khi lên xe" ở đầu màn hình.
3. Người dùng tắt công tắc → toàn bộ mục cấu hình bên dưới mờ đi nhưng vẫn đọc được.
4. Thay đổi có hiệu lực từ lần lên xe kế tiếp.

**Alternative Flows**:
- **AF-018.1** — Người dùng tắt rồi bật lại: cấu hình nguồn ngữ cảnh cũ được giữ nguyên, không reset.
- **AF-018.2** — Giọng chào thuộc Premium và người dùng ở gói Free: công tắc hiện trạng thái khoá, nhưng **nghe thử được** (UC-020), và nút mở khoá dẫn WF-010.

**Postconditions**: trạng thái bật/tắt được lưu và tôn trọng ở mọi lần kết nối sau đó

**Acceptance Criteria**:
- **AC-018.1**: WHEN người dùng tắt giọng chào THEN hệ thống **không** phát bất kỳ câu chào nào ở các lần kết nối sau, cho tới khi được bật lại.
- **AC-018.2**: WHEN người dùng tắt rồi bật lại THEN cấu hình nguồn ngữ cảnh trước đó được giữ nguyên.
- **AC-018.3**: WHEN trạng thái được đổi THEN nó có hiệu lực ở lần `carplay_connected` kế tiếp mà không cần khởi động lại app.

**Screens Involved**: WF-009, WF-006, WF-010
**Primary Screen**: WF-009
**Entry Point**: Tab Widgets hoặc thẻ giọng chào trên WF-006
**Exit Point**: WF-009 (ở lại) hoặc WF-006

**Context Variations**:
- **First-time user**: bật theo mặc định, kèm một dòng nói rõ có thể tắt bất cứ lúc nào — giảm cảm giác bị áp đặt.
- **Returning user**: hiếm khi vào lại; nếu vào thường là để tắt trong giai đoạn cần yên tĩnh.
- **Power user / Edge case**: tắt tạm 1 tuần rồi bật lại → AF-018.1 giữ nguyên cấu hình.

---

#### UC-019: Chọn nguồn ngữ cảnh cho giọng chào 📱

**As a** chủ xe
**I want** quyết định app được dùng thông tin nào để tạo câu chào
**So that** tôi kiểm soát được app biết gì về mình

**Priority**: Medium · **Complexity**: Medium

**Preconditions**: giọng chào đang bật

**Main Flow**:
1. WF-009 liệt kê 4 nguồn ngữ cảnh: giờ trong ngày · thời tiết · lịch · điểm đến dự đoán.
2. Mỗi nguồn có công tắc riêng, một dòng ví dụ câu chào sinh ra từ nguồn đó, và trạng thái quyền liên quan.
3. Người dùng bật/tắt từng nguồn.
4. Nguồn nào cần quyền mà chưa có: hiện lối vào cấp quyền tại chỗ (dẫn WF-022 hoặc Cài đặt hệ thống).

**Alternative Flows**:
- **AF-019.1** — Nguồn bị bật nhưng quyền bị từ chối: nguồn hiện trạng thái "cần quyền", **không** âm thầm không hoạt động.
- **AF-019.2** — Người dùng tắt hết 4 nguồn: hệ thống dùng câu chào trung tính, vẫn phát, không im lặng.
- **AF-019.3** — Nguồn thời tiết không lấy được dữ liệu: bỏ qua nguồn đó cho lượt phát này, dùng nguồn còn lại.

**Postconditions**: tập nguồn ngữ cảnh được lưu; ContextEngine chỉ dùng đúng những nguồn được bật

**Acceptance Criteria**:
- **AC-019.1**: WHEN người dùng tắt một nguồn THEN ContextEngine **không** đọc dữ liệu từ nguồn đó ở các lượt sinh câu chào sau.
- **AC-019.2**: IF một nguồn được bật nhưng quyền tương ứng bị từ chối THEN WF-009 hiển thị rõ trạng thái "cần quyền" kèm lối vào cấp quyền.
- **AC-019.3**: IF cả 4 nguồn đều tắt THEN hệ thống vẫn phát một câu chào trung tính, không im lặng và không báo lỗi.
- **AC-019.4**: WHEN mỗi nguồn được hiển thị THEN có kèm một ví dụ câu chào cụ thể sinh ra từ nguồn đó.

**Screens Involved**: WF-009, WF-022, WF-012
**Primary Screen**: WF-009
**Entry Point**: WF-009
**Exit Point**: WF-009

**Context Variations**:
- **First-time user**: chỉ nguồn "giờ trong ngày" hoạt động (chưa có quyền, chưa có dữ liệu) — và điều đó được nói rõ.
- **Returning user**: bật thêm nguồn khi thấy câu chào đơn điệu; đây là lối nâng cấp trải nghiệm không tốn tiền.
- **Power user / Edge case**: bật lịch nhưng tắt điểm đến (không muốn app học tuyến đường) — mọi tổ hợp phải hợp lệ.

---

#### UC-020: Nghe thử giọng chào trước khi lên xe 📱

**As a** chủ xe
**I want** nghe trước câu chào sẽ phát trên xe
**So that** tôi biết chính xác mình sẽ nghe gì, và biết tính năng này có thật

**Priority**: High · **Complexity**: Medium

**Preconditions**: đang ở WF-009

**Main Flow**:
1. Người dùng chạm "Nghe thử" trên WF-009.
2. ContextEngine sinh câu chào bằng **ngữ cảnh thật tại thời điểm này** (giờ hiện tại, thời tiết hiện tại, lịch sắp tới nếu có quyền).
3. Câu chào được phát qua loa iPhone; chữ của câu chào hiện đồng thời trên màn hình.
4. Người dùng chạm "Nghe thử" lần nữa → nhận **câu khác**, không lặp y hệt.

**Alternative Flows**:
- **AF-020.1** — Gói Free: nghe thử được đầy đủ (không cắt, không watermark), nhưng tính năng chỉ chạy trên xe khi đã nâng cấp; nút mở khoá dẫn WF-010.
- **AF-020.2** — Không có quyền nào: nghe thử vẫn hoạt động với ngữ cảnh giờ.
- **AF-020.3** — Đang phát nhạc: áp dụng ducking như trên xe, để bản nghe thử phản ánh đúng trải nghiệm thật.

**Postconditions**: người dùng đã nghe ≥ 1 câu chào thật do ContextEngine sinh ra

**Acceptance Criteria**:
- **AC-020.1**: WHEN người dùng chạm "Nghe thử" THEN câu chào được sinh từ ngữ cảnh thật tại thời điểm đó, **không** phải câu mẫu cố định.
- **AC-020.2**: WHEN người dùng chạm "Nghe thử" hai lần liên tiếp THEN hai câu chào **không** giống y hệt nhau.
- **AC-020.3**: WHEN câu chào phát THEN chữ tương ứng được hiển thị đồng thời trên màn hình.
- **AC-020.4**: WHEN nghe thử THEN toàn bộ quá trình sinh câu chào diễn ra on-device, **không có lệnh gọi mạng nào**.

**Screens Involved**: WF-009, WF-010
**Primary Screen**: WF-009
**Entry Point**: nút "Nghe thử" trên WF-009
**Exit Point**: WF-009

**Context Variations**:
- **First-time user**: đây là nơi người dùng lần đầu xác nhận **giọng chào là thật** — đối trọng trực tiếp với R-10 và R-13.
- **Returning user**: nghe thử sau khi bật thêm nguồn ngữ cảnh để thấy khác biệt.
- **Power user / Edge case**: chạm liên tiếp 10 lần để kiểm số biến thể → phải thấy ≥ 4 biến thể ngữ cảnh khác nhau.

---

#### UC-021: Nghe giọng chào cá nhân hóa khi lên xe 🚗

**As a** chủ xe
**I want** xe chào tôi bằng câu phù hợp hoàn cảnh lúc đó
**So that** cảm giác như xe hiểu tôi, không phải như một cái loa đọc câu có sẵn

**Priority**: High · **Complexity**: High

**Preconditions**: giọng chào đang bật; đã nâng cấp Premium (hoặc đang trong trial); iPhone kết nối CarPlay

**Main Flow**:
1. `carplay_connected` xảy ra.
2. ContextEngine đọc các nguồn đang bật và chọn biến thể câu chào phù hợp — hoàn toàn on-device.
3. `AVSpeechSynthesizer` phát câu chào qua loa xe, sau sound Connect (UC-010), trong ≤ 2s kể từ thời điểm connect.
4. Hệ thống ghi `voice_greeting_played` kèm `context_used`.

**Alternative Flows**:
- **AF-021.1** — Câu chào vừa phát giống câu lần trước: ContextEngine chọn biến thể khác trước khi phát.
- **AF-021.2** — Đang có cuộc gọi: bỏ lượt phát, không phát bù.
- **AF-021.3** — Không đủ ngữ cảnh: rơi về câu chào theo giờ; **không** im lặng và **không** phát câu báo lỗi.
- **AF-021.4** — Người dùng ở gói Free: không phát giọng chào; WF-018 nêu rõ đây là tính năng Premium bằng **một dòng chữ tĩnh**, không popup.
- **AF-021.5** — Ngôn ngữ app là ES hoặc PT-BR: câu chào phát bằng đúng ngôn ngữ đó, không chỉ UI (xem UC-031).

**Postconditions**: câu chào đã phát qua loa xe, hoặc lượt phát bị bỏ có lý do ghi nhận

**Acceptance Criteria**:
- **AC-021.1**: WHEN `carplay_connected` xảy ra THEN câu chào bắt đầu phát trong ≤ 2s.
- **AC-021.2**: WHEN câu chào được sinh THEN toàn bộ quá trình chạy on-device và **không có lệnh gọi mạng nào**.
- **AC-021.3**: WHEN hệ thống chọn câu chào THEN có ≥ 4 biến thể ngữ cảnh khả dụng và **không lặp lại câu y hệt hai lần liên tiếp**.
- **AC-021.4**: WHEN câu chào phát xong THEN hệ thống ghi `voice_greeting_played` kèm `context_used` phân biệt time/weather/calendar/destination.
- **AC-021.5**: IF không có ngữ cảnh nào khả dụng THEN hệ thống phát câu chào theo giờ trong ngày, không im lặng.
- **AC-021.6**: WHEN nội dung câu chào được sinh THEN **không** chứa tên "Jarvis" hoặc bất kỳ tham chiếu Marvel/Disney nào (R-10).
- **AC-021.7**: WHEN ngôn ngữ app là ES hoặc PT-BR THEN nội dung câu chào phát bằng đúng ngôn ngữ đó.

**Screens Involved**: WF-016, WF-018 (hành vi nền trên bề mặt CarPlay)
**Primary Screen**: WF-016
**Entry Point**: sự kiện hệ thống `carplay_connected`
**Exit Point**: WF-016 CarPlay Dashboard

**Context Variations**:
- **First-time user**: câu chào đầu tiên chỉ dùng ngữ cảnh giờ — và điều đó vẫn phải nghe tự nhiên, không nghe như bản rút gọn.
- **Returning user**: sau vài ngày có thêm ngữ cảnh tuyến đường và lịch; câu chào rõ ràng phong phú hơn.
- **Power user / Edge case**: cuộc gọi, thiếu quyền, ngôn ngữ khác, gói Free → AF-021.2 đến AF-021.5.

---

#### UC-022: Xem dashboard tự sắp xếp theo ngữ cảnh 🚗

**As a** người lái hằng ngày
**I want** dashboard tự đổi theo hoàn cảnh mà tôi không phải cấu hình gì
**So that** thứ tôi cần luôn ở chỗ dễ chạm nhất, không phải đi tìm

**Priority**: High · **Complexity**: High

**Preconditions**: iPhone kết nối CarPlay; CarPlay scene active

**Main Flow**:
1. WF-016 CarPlay Dashboard hiện các thẻ: nhạc đang phát · thời tiết · điểm đến gợi ý · shortcut.
2. ContextEngine sắp thứ tự thẻ theo ngữ cảnh hiện tại (giờ, tuyến quen, thói quen nghe nhạc) — học on-device.
3. Layout của toàn bộ dashboard được tính theo scene bounds tại runtime.
4. Người dùng nhìn thoáng và thấy thẻ liên quan nhất ở vị trí ưu tiên.

**Alternative Flows**:
- **AF-022.1** — Chưa đủ dữ liệu để học: dùng thứ tự mặc định kèm một dòng nói rõ dashboard sẽ tự đổi sau vài chuyến — **không** giả vờ là đã cá nhân hóa.
- **AF-022.2** — Ngữ cảnh đoán sai: người dùng bỏ qua thẻ đó; hệ thống hạ trọng số thẻ này, không cần người dùng vào Settings.
- **AF-022.3** — Không có mạng: thẻ nhạc và thời tiết dùng dữ liệu cache và ghi rõ thời điểm cập nhật; thẻ shortcut vẫn hoạt động bình thường.
- **AF-022.4** — Gói Free: hiện dashboard cơ bản (nhạc đang phát, thời tiết, 1 shortcut) — đây là cấu hình Free đã chốt ở PRD §11, không phải bản bị cắt tuỳ ý.

**Postconditions**: dashboard hiển thị đúng trong bounds; thứ tự thẻ phản ánh ngữ cảnh hoặc là thứ tự mặc định được nói rõ

**Acceptance Criteria**:
- **AC-022.1**: WHEN CarPlay scene active THEN layout dashboard được tính theo scene bounds tại runtime, không dùng hằng số kích thước.
- **AC-022.2**: WHEN ContextEngine sắp thẻ THEN toàn bộ dữ liệu học **không rời thiết bị**.
- **AC-022.3**: IF chưa đủ dữ liệu để cá nhân hóa THEN hệ thống dùng thứ tự mặc định và nói rõ điều đó, không tuyên bố đã cá nhân hóa.
- **AC-022.4**: WHEN người dùng dùng app THEN hệ thống **không bao giờ** yêu cầu người dùng tự tạo hoặc tự cấu hình widget/thẻ để dashboard hoạt động.
- **AC-022.5**: IF người dùng ở gói Free THEN dashboard hiển thị đúng cấu hình Free đã chốt: nhạc đang phát, thời tiết, 1 shortcut.
- **AC-022.6**: WHEN mất mạng THEN thẻ dùng dữ liệu cache và hiển thị rõ thời điểm cập nhật cuối.

**Screens Involved**: WF-016, WF-017, WF-018
**Primary Screen**: WF-016
**Entry Point**: `carplay_connected` → CarPlay scene active
**Exit Point**: người dùng chạm một thẻ (UC-023), hoặc kết thúc phiên

**Context Variations**:
- **First-time user**: thứ tự mặc định + dòng giải thích; kỳ vọng được đặt đúng ngay từ đầu.
- **Returning user**: thứ tự đã học; thẻ hay dùng lên đầu.
- **Power user / Edge case**: đi công tác nên ngữ cảnh sai hoàn toàn → AF-022.2, và cách sửa rẻ nhất là **bỏ qua**, không phải vào Settings.

---

#### UC-023: Chạm thẻ gợi ý trên dashboard 🚗

**As a** người lái
**I want** thực hiện việc mình cần bằng đúng một lần chạm
**So that** tôi rời mắt khỏi đường trong thời gian ngắn nhất

**Priority**: High · **Complexity**: Medium

**Preconditions**: WF-016 đang hiển thị ít nhất 1 thẻ có hành động

**Main Flow**:
1. Người dùng chạm một thẻ (ví dụ: thẻ nhạc gợi ý).
2. Hệ thống thực hiện hành động tương ứng ngay: phát nhạc, mở dẫn đường trong Apple Maps, hoặc gọi shortcut.
3. Hệ thống ghi `ai_recommendation_tapped` và hạ/nâng trọng số thẻ theo phản hồi ngầm này.
4. Người dùng quay lại WF-016 hoặc ở lại app hệ thống vừa mở.

**Alternative Flows**:
- **AF-023.1** — Hành động thất bại (nguồn nhạc không sẵn sàng): hiện thông báo gọn ngay trên thẻ, kèm một hành động thay thế; **không** hiện modal.
- **AF-023.2** — Không có mạng: thẻ nhạc chuyển sang phát từ nguồn cục bộ; thẻ dẫn đường dùng địa điểm đã cache.
- **AF-023.3** — Thẻ thuộc tính năng Premium: hiện trạng thái khoá bằng chữ trên thẻ, **không** mở paywall trên màn hình xe.
- **AF-023.4** — Chạm nhiều thẻ liên tiếp: mỗi lần chạm huỷ hành động trước, không xếp hàng.

**Postconditions**: hành động đã thực hiện hoặc đã báo thất bại kèm đường thay thế; phản hồi ngầm đã được ghi

**Acceptance Criteria**:
- **AC-023.1**: WHEN người dùng chạm một thẻ THEN hành động tương ứng bắt đầu trong ≤ 1s.
- **AC-023.2**: WHEN thẻ được hiển thị THEN mọi touch target ≥ 44pt.
- **AC-023.3**: IF hành động thất bại THEN hệ thống hiển thị thông báo gọn kèm hành động thay thế, và **không** dùng modal trên bề mặt CarPlay.
- **AC-023.4**: IF thẻ thuộc tính năng Premium THEN hệ thống hiển thị trạng thái khoá bằng chữ và **không** mở paywall trên màn hình xe.
- **AC-023.5**: WHEN người dùng chạm thẻ THEN hệ thống ghi `ai_recommendation_tapped`; mục tiêu tap-through rate ≥ 30%.

**Screens Involved**: WF-016, WF-018
**Primary Screen**: WF-016
**Entry Point**: WF-016 CarPlay Dashboard
**Exit Point**: app hệ thống tương ứng (nhạc / Maps / điện thoại) hoặc quay về WF-016

**Context Variations**:
- **First-time user**: thẻ mặc định; lần chạm đầu tiên là dữ liệu học đầu tiên.
- **Returning user**: chạm đúng thẻ đầu tiên trong phần lớn trường hợp — đó chính là ý nghĩa của tap-through rate ≥ 30%.
- **Power user / Edge case**: mất mạng, hành động thất bại, thẻ khoá → AF-023.1 đến AF-023.4.

---

### 2.5 Gói Free, Paywall & Thanh Toán

> Nhóm này phục vụ **F4** và **F7** — theo PRD §11 đây là **điểm khác biệt hóa lớn nhất** của sản phẩm, không phải một chi tiết triển khai. Toàn bộ AC ở đây là phản ứng trực tiếp với dữ liệu: ~60/96 review 1★ của đối thủ là về paywall. Hai ràng buộc cứng xuyên suốt: **không bán gói weekly** và **paywall không xuất hiện ở lần mở app đầu tiên**.

#### UC-024: Dùng gói Free vô thời hạn để tự xác nhận app chạy trên xe 📱🚗

**As a** người dùng đang cân nhắc
**I want** xác nhận app thật sự chạy trên xe của tôi trước khi trả bất kỳ đồng nào
**So that** tôi không mất tiền cho một thứ có thể không tương thích với xe mình

**Priority**: High · **Complexity**: Medium

**Preconditions**: app đã cài; chưa có giao dịch nào

**Main Flow**:
1. Người dùng hoàn tất onboarding (UC-001) — **không gặp paywall lần nào**.
2. WF-006 hiện đầy đủ: 1 widget đang bật, 3 sound preset mở, dashboard cơ bản.
3. Người dùng cắm CarPlay → widget render đầy đủ chức năng (UC-015), sound phát (UC-010).
4. Người dùng dùng như vậy bao lâu cũng được — không hết hạn, không quảng cáo.
5. Khi muốn thêm widget hoặc thêm sound, người dùng **tự** mở WF-010.

**Alternative Flows**:
- **AF-024.1** — Người dùng dùng Free mãi: hợp lệ, đây là thiết kế có chủ ý. Hệ thống **không** nhắc nâng cấp lặp lại theo phiên.
- **AF-024.2** — Widget không chạy trên xe của người dùng: người dùng phát hiện **trước khi trả tiền** — đây chính là mục đích của free tier như một cơ chế lọc rủi ro (R-11, R-04).
- **AF-024.3** — Người dùng chạm một tính năng khoá: WF-010 mở với ngữ cảnh đúng tính năng vừa chạm, không phải paywall chung.

**Postconditions**: người dùng có trải nghiệm đầy đủ ở mức Free; nếu nâng cấp thì đó là quyết định sau khi đã xác nhận app chạy

**Acceptance Criteria**:
- **AC-024.1**: WHEN người dùng mở app lần đầu THEN hệ thống **không** hiển thị WF-010; kiểm chứng bằng `paywall_shown.days_since_install > 0` hoặc `trigger_source` là hành động chủ động của người dùng.
- **AC-024.2**: WHEN người dùng ở gói Free THEN có đúng 1 widget CarPlay **đầy đủ chức năng** (không watermark, không làm mờ), 3 sound preset chất lượng đầy đủ, và dashboard cơ bản.
- **AC-024.3**: WHEN người dùng ở gói Free THEN **không có quảng cáo** và **không có giới hạn thời gian**.
- **AC-024.4**: WHEN người dùng ở gói Free THEN hệ thống hiển thị tối đa **một** lời mời nâng cấp dạng tĩnh mỗi màn hình, không dùng popup và không nhắc lại theo phiên.
- **AC-024.5**: WHEN người dùng dùng widget ở gói Free THEN hệ thống ghi `free_tier_widget_used`.

**Screens Involved**: WF-006, WF-007, WF-008, WF-016, WF-017, WF-018, WF-010
**Primary Screen**: WF-006
**Entry Point**: hoàn tất onboarding
**Exit Point**: WF-010 (khi người dùng chủ động muốn nâng cấp) hoặc tiếp tục dùng Free

**Context Variations**:
- **First-time user**: **không thấy paywall** — đây là ràng buộc cứng, không phải lựa chọn thiết kế.
- **Returning user**: dùng Free lâu dài mà không bị quấy rầy.
- **Power user / Edge case**: dùng Free 30 ngày, widget chạy tốt, muốn thêm widget thứ hai → đây mới là thời điểm nâng cấp hợp lý (AF-024.3).

---

#### UC-025: Xem bảng giá minh bạch 📱

**As a** người dùng đã thấy giá trị
**I want** thấy rõ các lựa chọn và giá của từng lựa chọn
**So that** tôi quyết định được mà không cảm thấy bị gài

**Priority**: High · **Complexity**: Medium

**Preconditions**: người dùng chủ động mở paywall (từ tính năng khoá hoặc từ WF-012); `days_since_install > 0` hoặc do người dùng chủ động

**Main Flow**:
1. WF-010 hiện **4 lựa chọn**: gói Free hiện tại · $4,99/tháng · $29,99/năm · $49,99 lifetime.
2. Mỗi bậc nêu rõ mở khóa những gì; gói Free hiện là "gói bạn đang dùng", không bị làm mờ.
3. Giá hiển thị bằng **tiền tệ địa phương**, là giá cuối cùng.
4. Người dùng chọn một bậc → WF-011 Xác Nhận Giá (UC-026).

**Alternative Flows**:
- **AF-025.1** — Người dùng đóng paywall: về đúng màn hình trước đó, không bị hỏi lại trong cùng phiên.
- **AF-025.2** — Người dùng đã mua trên thiết bị khác: nút "Phục hồi giao dịch" luôn hiện, ngang hàng với các bậc giá.
- **AF-025.3** — Không lấy được giá từ StoreKit: hiện trạng thái đang tải rồi báo lỗi rõ ràng; **tuyệt đối không** hiện giá cache hoặc giá hardcode.
- **AF-025.4** — Paywall mở từ ngữ cảnh một tính năng: bậc chứa tính năng đó được nhấn mạnh, nhưng ba bậc kia vẫn hiển thị đầy đủ.

**Postconditions**: người dùng đã thấy đủ 4 lựa chọn và giá cuối; hệ thống ghi `paywall_shown`

**Acceptance Criteria**:
- **AC-025.1**: WHEN WF-010 hiển thị THEN có đúng 4 lựa chọn: Free · Monthly $4,99 · Yearly $29,99 · Lifetime $49,99, và **không có bậc weekly nào**.
- **AC-025.2**: WHEN giá hiển thị THEN đó là **giá cuối cùng bằng tiền tệ địa phương**, và hệ thống **không** quy đổi kiểu "$0,48/tuần" (R-12).
- **AC-025.3**: WHEN WF-010 hiển thị THEN hệ thống **không** dùng discount phần trăm không đúng thực tế (R-12).
- **AC-025.4**: WHEN WF-010 hiển thị THEN gói Free được trình bày như một lựa chọn hợp lệ đang dùng, không bị làm mờ hay ẩn.
- **AC-025.5**: IF không lấy được giá từ StoreKit THEN hệ thống báo lỗi rõ ràng và **không** hiển thị giá cache hay giá hardcode.
- **AC-025.6**: WHEN WF-010 hiển thị THEN hệ thống ghi `paywall_shown` kèm `trigger_source` và `days_since_install`.

**Screens Involved**: WF-010, WF-011, WF-025, WF-007, WF-008
**Primary Screen**: WF-010
**Entry Point**: tính năng khoá trên WF-007 / WF-008 / WF-009, hoặc dòng "Nâng cấp" trên WF-012
**Exit Point**: WF-011 (chọn mua) hoặc màn hình trước đó (đóng)

**Context Variations**:
- **First-time user**: chỉ tới đây nếu **tự** chạm vào một tính năng khoá — không bao giờ bị đẩy vào.
- **Returning user**: quay lại paywall sau khi đã dùng Free một thời gian; bậc yearly được nhấn mạnh.
- **Power user / Edge case**: đã mua trên iPad → AF-025.2; StoreKit lỗi → AF-025.3.

---

#### UC-026: Xác nhận giá cuối cùng trước khi trả tiền 📱

**As a** người dùng sắp trả tiền
**I want** biết chính xác tôi trả bao nhiêu, khi nào bị trừ, và trừ bao nhiêu lần
**So that** tôi không bị bất ngờ trên hoá đơn và không phải đi khiếu nại

**Priority**: High · **Complexity**: Medium

**Preconditions**: người dùng đã chọn một bậc giá ở WF-010

**Main Flow**:
1. WF-011 hiện: bậc đã chọn · **giá cuối bằng tiền tệ địa phương** · ngày hết trial · **ngày bị trừ tiền** · chu kỳ gia hạn.
2. Người dùng đọc và chạm "Xác nhận" → hệ thống ghi `price_confirmed`.
3. StoreKit hiện dialog thanh toán của Apple.
4. Thanh toán thành công → `EntitlementService` cập nhật; WF-030 toast; các tính năng mở khóa ngay.

**Alternative Flows**:
- **AF-026.1** — Người dùng huỷ ở dialog Apple: về WF-011, không mất lựa chọn, không hiện lại paywall.
- **AF-026.2** — Thanh toán thất bại: thông báo rõ nguyên nhân từ StoreKit, có nút thử lại.
- **AF-026.3** — Mua gói Lifetime: không có phần "ngày trừ tiền tiếp theo"; hiện rõ đây là giao dịch **một lần**.
- **AF-026.4** — Người dùng đổi vùng App Store giữa lúc mua: giá được đọc lại từ StoreKit, **không** dùng giá đã cache.

**Postconditions**: entitlement được cập nhật; người dùng đã thấy và xác nhận giá cuối trước khi có bất kỳ khoản trừ nào

**Acceptance Criteria**:
- **AC-026.1**: WHEN WF-011 hiển thị THEN nó hiện đồng thời: giá cuối bằng tiền tệ địa phương, ngày hết trial, và ngày bị trừ tiền.
- **AC-026.2**: WHEN người dùng chạm "Xác nhận" THEN hệ thống ghi `price_confirmed` **trước khi** gọi dialog thanh toán.
- **AC-026.3**: IF bậc đã chọn là Lifetime THEN WF-011 nêu rõ đây là giao dịch một lần và **không** hiển thị ngày gia hạn.
- **AC-026.4**: WHEN thanh toán thành công THEN tính năng được mở khóa trong ≤ 2s mà không cần khởi động lại app.
- **AC-026.5**: WHEN người dùng đi tới giao dịch THEN **không có đường nào** dẫn tới thanh toán mà bỏ qua WF-011.
- **AC-026.6**: WHEN thanh toán thành công THEN hệ thống gửi xác nhận giao dịch (email hoặc thông báo trong app) — biện pháp chống chargeback (R-12).

**Screens Involved**: WF-011, WF-010, WF-030
**Primary Screen**: WF-011
**Entry Point**: chọn một bậc giá trên WF-010
**Exit Point**: màn hình trước paywall (đã mở khóa) hoặc WF-010 (nếu huỷ)

**Context Variations**:
- **First-time user**: lần đầu thấy giá cuối — đây là màn hình chống bait-and-switch, **tồn tại đúng một chỗ duy nhất** trên đường tới giao dịch (xem §0.2).
- **Returning user**: không gặp lại sau khi đã mua; nếu nâng bậc thì gặp lại với thông tin của bậc mới.
- **Power user / Edge case**: đổi vùng App Store, huỷ giữa dialog, thanh toán lỗi → AF-026.1 đến AF-026.4.

---

#### UC-027: Bắt đầu trial 7 ngày 📱

**As a** người dùng muốn thử toàn bộ tính năng
**I want** dùng đủ 7 ngày và biết rõ khi nào hết
**So that** tôi thử trên xe mình đủ nhiều lần trước khi quyết định

**Priority**: High · **Complexity**: Medium

**Preconditions**: chưa từng dùng trial; đã xác nhận giá ở WF-011

**Main Flow**:
1. Người dùng xác nhận bậc Monthly hoặc Yearly có trial → trial 7 ngày bắt đầu.
2. Hệ thống ghi `trial_started`; entitlement chuyển sang Premium.
3. WF-006 và WF-012 hiện rõ: "Trial còn N ngày · sẽ trừ <số tiền bằng tiền tệ địa phương> vào <ngày trừ tiền>".
4. Ngày 6 và ngày 7 → WF-013 Nhắc Hết Trial (UC-028).
5. Hết ngày 7 mà không huỷ → chuyển sang trả phí; hệ thống ghi `trial_converted`.

**Alternative Flows**:
- **AF-027.1** — Người dùng huỷ trong trial: giữ Premium tới hết ngày 7 rồi về gói Free; **không mất cấu hình widget hay sound đã tạo**.
- **AF-027.2** — Đã dùng trial trước đó: bậc giá không hiện trial; nêu rõ đây là mua trực tiếp.
- **AF-027.3** — Mua Lifetime: không có trial, hiện rõ điều đó ở WF-011.

**Postconditions**: trial đang chạy với ngày hết hạn rõ ràng, hiển thị được ở cả WF-006 và WF-012

**Acceptance Criteria**:
- **AC-027.1**: WHEN trial bắt đầu THEN hệ thống ghi `trial_started` và độ dài trial là đúng **7 ngày**.
- **AC-027.2**: WHEN trial đang chạy THEN ngày hết hạn và ngày bị trừ tiền hiển thị **trong app**, ở cả WF-006 và WF-012.
- **AC-027.3**: IF người dùng huỷ trial THEN quyền Premium được giữ tới hết ngày 7, sau đó về gói Free, và **mọi cấu hình widget/sound đã tạo được giữ nguyên**.
- **AC-027.4**: IF người dùng đã từng dùng trial THEN hệ thống **không** hiển thị lại ưu đãi trial.
- **AC-027.5**: WHEN trial chuyển thành trả phí THEN hệ thống ghi `trial_converted`.

**Screens Involved**: WF-011, WF-006, WF-012, WF-013, WF-025
**Primary Screen**: WF-011
**Entry Point**: xác nhận bậc có trial ở WF-011
**Exit Point**: WF-006 (đã mở khóa, trial đang chạy)

**Context Variations**:
- **First-time user**: trial là lần đầu dùng Premium; đếm ngày phải hiện ở nơi dễ thấy, không chỉ trong Settings.
- **Returning user**: đã dùng trial → AF-027.2, mua trực tiếp.
- **Power user / Edge case**: huỷ ngày thứ 2 nhưng vẫn dùng tới ngày 7 → AF-027.1, và không được mất dữ liệu cấu hình.

---

#### UC-028: Nhận nhắc trước khi hết trial và quyết định 📱

**As a** người dùng đang trong trial
**I want** được nhắc trước khi bị trừ tiền, kèm số tiền chính xác
**So that** tôi chủ động quyết định thay vì phát hiện khoản trừ sau khi đã xảy ra

**Priority**: Medium · **Complexity**: Low

**Preconditions**: trial đang chạy, đang ở ngày 6 hoặc ngày 7

**Main Flow**:
1. Ngày 6 → WF-013 hiện: số ngày còn lại, **số tiền chính xác**, ngày bị trừ.
2. Ba nút ngang hàng: "Nhắc sau" · "Đăng ký" · **"Huỷ trial"**.
3. Người dùng chọn một trong ba.
4. Nếu chọn "Huỷ trial" → WF-027 Alert xác nhận → dẫn tới WF-025 Quản Lý Đăng Ký.

**Alternative Flows**:
- **AF-028.1** — Người dùng chọn "Nhắc sau": hiện lại ngày 7, **tối đa 2 lần trong cả kỳ trial**.
- **AF-028.2** — Người dùng bỏ qua hoàn toàn: trial chuyển thành trả phí đúng ngày 7 như đã thông báo.
- **AF-028.3** — Người dùng huỷ: về gói Free sau ngày 7; cấu hình được giữ (AF-027.1).

**Postconditions**: người dùng đã được thông báo ít nhất 1 lần với số tiền chính xác trước khi bị trừ

**Acceptance Criteria**:
- **AC-028.1**: WHEN trial còn 1 ngày THEN hệ thống hiển thị WF-013 kèm **số tiền chính xác** và **ngày bị trừ**.
- **AC-028.2**: WHEN WF-013 hiển thị THEN nút "Huỷ trial" **ngang hàng về mặt thị giác** với nút "Đăng ký", không bị ẩn hay làm mờ (biện pháp chống R-12).
- **AC-028.3**: IF người dùng chọn "Nhắc sau" THEN hệ thống nhắc lại tối đa 2 lần trong cả kỳ trial.
- **AC-028.4**: WHEN WF-013 hiển thị THEN nó **không** dùng đếm ngược gây áp lực hay ngôn từ khan hàng giả tạo.

**Screens Involved**: WF-013, WF-027, WF-025, WF-012
**Primary Screen**: WF-013
**Entry Point**: hệ thống kích hoạt vào ngày 6 và ngày 7 của trial
**Exit Point**: WF-006 (nhắc sau / đăng ký) hoặc WF-025 (huỷ)

**Context Variations**:
- **First-time user**: đây là lần đầu người dùng thấy con số sẽ bị trừ — phải là con số thật, bằng tiền tệ địa phương.
- **Returning user**: không gặp lại nếu đã trả phí.
- **Power user / Edge case**: chọn "Nhắc sau" nhiều lần → AF-028.1 chặn ở 2 lần để không thành vòng lặp quấy rầy.

---

#### UC-029: Quản lý hoặc huỷ đăng ký 📱

**As a** người dùng đang trả phí
**I want** thấy tôi đang dùng gói gì và huỷ được dễ dàng
**So that** tôi không cảm thấy bị mắc kẹt — điều làm người dùng gọi app khác là scam

**Priority**: Medium · **Complexity**: Low

**Preconditions**: có subscription đang hoạt động hoặc trial đang chạy

**Main Flow**:
1. Người dùng mở WF-012 → chạm dòng "Đăng ký của tôi" (có hiện trạng thái ngay trên dòng).
2. WF-025 Sheet hiện: gói hiện tại · giá · ngày gia hạn kế tiếp · nút "Huỷ đăng ký" · nút "Phục hồi giao dịch".
3. Người dùng chạm "Huỷ đăng ký" → WF-027 Alert xác nhận, nêu rõ **quyền Premium còn dùng tới ngày nào**.
4. Xác nhận → chuyển sang trang quản lý subscription của hệ thống iOS.

**Alternative Flows**:
- **AF-029.1** — Gói Lifetime: không có gì để huỷ; WF-025 hiện rõ "đã mua vĩnh viễn", không hiện nút huỷ gây bối rối.
- **AF-029.2** — Phục hồi giao dịch: đọc lại từ StoreKit và cập nhật entitlement; nếu không có giao dịch thì nói rõ chứ không báo lỗi chung.
- **AF-029.3** — Đã huỷ trước đó: WF-025 hiện rõ ngày quyền Premium kết thúc.

**Postconditions**: người dùng biết chính xác trạng thái đăng ký và ngày kết thúc quyền

**Acceptance Criteria**:
- **AC-029.1**: WHEN WF-025 hiển thị THEN nó hiện gói hiện tại, giá, và ngày gia hạn kế tiếp.
- **AC-029.2**: WHEN người dùng muốn huỷ THEN đường huỷ dài **tối đa 3 chạm** kể từ WF-012.
- **AC-029.3**: IF người dùng mua Lifetime THEN WF-025 **không** hiển thị nút huỷ đăng ký.
- **AC-029.4**: WHEN người dùng huỷ THEN hệ thống nêu rõ ngày quyền Premium kết thúc, và hệ thống ghi `subscription_cancelled`.
- **AC-029.5**: WHEN người dùng chạm "Phục hồi giao dịch" mà không có giao dịch nào THEN hệ thống nói rõ điều đó thay vì báo lỗi chung.

**Screens Involved**: WF-025, WF-012, WF-027
**Primary Screen**: WF-025
**Entry Point**: dòng "Đăng ký của tôi" trên WF-012, hoặc nút huỷ trên WF-013
**Exit Point**: WF-012, hoặc trang quản lý subscription của iOS

**Context Variations**:
- **First-time user**: chưa có gì để quản lý; dòng trên WF-012 hiện "Gói Free" và dẫn tới WF-010.
- **Returning user**: vào để kiểm ngày gia hạn.
- **Power user / Edge case**: có cả subscription cũ và Lifetime mới → WF-025 nêu rõ Lifetime đã bao trùm, và nhắc huỷ subscription để không trả trùng.

---

#### UC-030: Mua gói Lifetime một lần 📱

**As a** người dùng không muốn trả tiền định kỳ (Sam — Car Enthusiast)
**I want** trả một lần rồi dùng mãi
**So that** tôi sở hữu thứ mình đã mua, thay vì thuê nó cả đời

**Priority**: Medium · **Complexity**: Medium

**Preconditions**: chưa mua Lifetime

**Main Flow**:
1. Ở WF-010, người dùng chọn bậc "$49,99 — một lần".
2. WF-011 hiện rõ: giao dịch **một lần**, không gia hạn, không ngày trừ tiền tiếp theo.
3. Người dùng xác nhận → StoreKit xử lý non-consumable.
4. Entitlement chuyển sang Lifetime; toàn bộ tính năng Premium mở vĩnh viễn.

**Alternative Flows**:
- **AF-030.1** — Đang có subscription: hệ thống nêu rõ nên huỷ subscription sau khi mua Lifetime để không trả trùng, kèm lối vào WF-025.
- **AF-030.2** — Cài lại app: "Phục hồi giao dịch" trả lại Lifetime mà không phải trả lại tiền.
- **AF-030.3** — Thanh toán thất bại: như AF-026.2.

**Postconditions**: entitlement Lifetime được lưu và phục hồi được trên thiết bị khác cùng Apple ID

**Acceptance Criteria**:
- **AC-030.1**: WHEN người dùng mua Lifetime THEN hệ thống nêu rõ đây là giao dịch một lần và **không** hiển thị bất kỳ ngày gia hạn nào.
- **AC-030.2**: WHEN Lifetime được mua THEN toàn bộ tính năng Premium mở khóa vĩnh viễn, không phụ thuộc kết nối mạng sau đó.
- **AC-030.3**: IF người dùng đang có subscription khi mua Lifetime THEN hệ thống nhắc huỷ subscription kèm lối vào WF-025.
- **AC-030.4**: WHEN người dùng cài lại app và phục hồi giao dịch THEN Lifetime được trả lại mà **không** phải trả tiền lần nữa.

**Screens Involved**: WF-010, WF-011, WF-025, WF-030
**Primary Screen**: WF-011
**Entry Point**: bậc Lifetime trên WF-010
**Exit Point**: màn hình trước paywall (đã mở khóa vĩnh viễn)

**Context Variations**:
- **First-time user**: ít khi mua Lifetime ngay; bậc này chủ yếu dành cho người đã dùng Free và tin app.
- **Returning user**: chuyển từ subscription lên Lifetime → AF-030.1.
- **Power user / Edge case**: dùng nhiều thiết bị cùng Apple ID → AF-030.2.

---

### 2.6 Ngôn Ngữ, Quyền Riêng Tư & Phản Hồi

> Nhóm này phục vụ **F9**, **F10** và phần có bề mặt người dùng của **F12**. UC-033 có vai trò đặc biệt: nó là cơ chế trực tiếp phục vụ KPI **Recent 1★ Ratio < 15%** bằng cách phân luồng người đang gặp vấn đề sang kênh sửa lỗi thay vì đẩy họ ra App Store.

#### UC-031: Đổi ngôn ngữ app 📱

**As a** người dùng ở Mexico hoặc Brazil
**I want** dùng app bằng tiếng của tôi, kể cả phần giọng nói
**So that** app này thật sự dành cho tôi, không phải bản dịch nửa vời

**Priority**: Medium · **Complexity**: Medium

**Preconditions**: app đã cài

**Main Flow**:
1. Người dùng mở WF-012 → chạm "Ngôn ngữ" → WF-026 Sheet.
2. WF-026 hiện 3 lựa chọn: English · Español · Português (Brasil), kèm lựa chọn "Theo hệ thống".
3. Người dùng chọn một ngôn ngữ → áp dụng ngay, **không** cần khởi động lại app.
4. Nội dung giọng chào chuyển sang ngôn ngữ đó từ lượt phát kế tiếp.

**Alternative Flows**:
- **AF-031.1** — Ngôn ngữ hệ thống không phải EN/ES/PT-BR: mặc định về English, và WF-026 nêu rõ điều đó.
- **AF-031.2** — Đổi ngôn ngữ khi đang cắm CarPlay: UI CarPlay cập nhật ở lần vẽ kế tiếp; **giọng chào đang phát không bị cắt giữa câu**.
- **AF-031.3** — Người dùng tìm ngôn ngữ chưa hỗ trợ (DE/FR/IT): WF-026 nêu rõ các ngôn ngữ này thuộc MVP 2, không hiện lựa chọn không hoạt động.

**Postconditions**: ngôn ngữ được lưu; UI, nội dung giọng chào và định dạng giá đều theo ngôn ngữ/vùng đã chọn

**Acceptance Criteria**:
- **AC-031.1**: WHEN người dùng chọn một ngôn ngữ THEN toàn bộ UI chuyển sang ngôn ngữ đó ngay, không cần khởi động lại app.
- **AC-031.2**: WHEN ngôn ngữ là ES hoặc PT-BR THEN **nội dung giọng chào AI** cũng bằng ngôn ngữ đó, không chỉ UI.
- **AC-031.3**: WHEN giá được hiển thị THEN dùng đúng tiền tệ địa phương của storefront, độc lập với ngôn ngữ UI.
- **AC-031.4**: IF ngôn ngữ hệ thống không thuộc 3 ngôn ngữ hỗ trợ THEN app dùng English và nêu rõ lý do.
- **AC-031.5**: IF người dùng đổi ngôn ngữ khi đang cắm CarPlay THEN câu chào đang phát **không** bị cắt giữa câu.

**Screens Involved**: WF-026, WF-012, WF-016
**Primary Screen**: WF-026
**Entry Point**: dòng "Ngôn ngữ" trên WF-012
**Exit Point**: WF-012

**Context Variations**:
- **First-time user**: mặc định theo ngôn ngữ hệ thống — người dùng ở MX/BR không phải làm gì.
- **Returning user**: đổi một lần rồi không sửa nữa.
- **Power user / Edge case**: người dùng để iPhone ở English nhưng muốn giọng chào tiếng Tây Ban Nha → hai thứ này chọn độc lập được.

---

#### UC-032: Xoá toàn bộ dữ liệu on-device 📱

**As a** người dùng quan tâm quyền riêng tư
**I want** xoá sạch mọi thứ app đã học về tôi
**So that** tôi kiểm soát được dữ liệu của mình, không chỉ được nghe cam kết

**Priority**: Medium · **Complexity**: Low

**Preconditions**: app đã dùng một thời gian và đã có dữ liệu ngữ cảnh

**Main Flow**:
1. Người dùng mở WF-012 → chạm "Quyền riêng tư & dữ liệu".
2. Màn hình liệt kê **những loại dữ liệu app đang giữ** và ghi rõ chúng nằm trên thiết bị.
3. Người dùng chạm "Xoá toàn bộ dữ liệu học" → WF-029 Alert xác nhận, nêu rõ điều gì sẽ mất.
4. Xác nhận → dữ liệu ngữ cảnh bị xoá; cấu hình widget/sound **được giữ** (đây là hai loại khác nhau).
5. WF-030 toast xác nhận.

**Alternative Flows**:
- **AF-032.1** — Người dùng muốn xoá tất cả kể cả cấu hình: alert có lựa chọn thứ hai "Xoá cả cấu hình", tách rõ khỏi lựa chọn thứ nhất.
- **AF-032.2** — Người dùng huỷ ở alert: không xoá gì.
- **AF-032.3** — Người dùng xoá app: mọi dữ liệu on-device mất theo, đúng như đã cam kết ở PRD §9.

**Postconditions**: dữ liệu học bị xoá; dashboard trở lại thứ tự mặc định; entitlement **không** bị ảnh hưởng

**Acceptance Criteria**:
- **AC-032.1**: WHEN người dùng mở mục quyền riêng tư THEN hệ thống liệt kê các loại dữ liệu đang giữ và nêu rõ chúng nằm trên thiết bị.
- **AC-032.2**: WHEN người dùng xoá dữ liệu học THEN dữ liệu ngữ cảnh bị xoá nhưng cấu hình widget/sound và entitlement **được giữ nguyên**.
- **AC-032.3**: WHEN hành động xoá được yêu cầu THEN hệ thống bắt xác nhận qua WF-029 và nêu rõ điều gì sẽ mất.
- **AC-032.4**: WHEN dữ liệu bị xoá THEN dashboard trở về thứ tự mặc định và bắt đầu học lại từ đầu.

**Screens Involved**: WF-012, WF-029, WF-030
**Primary Screen**: WF-012
**Entry Point**: dòng "Quyền riêng tư & dữ liệu" trên WF-012
**Exit Point**: WF-012

**Context Variations**:
- **First-time user**: chưa có dữ liệu để xoá; mục này vẫn hiện và nói rõ "chưa có dữ liệu học nào".
- **Returning user**: xoá khi cảm thấy gợi ý sai nhiều — đây là cách reset nhẹ hơn xoá app.
- **Power user / Edge case**: bán xe, đổi xe → muốn xoá sạch cả cấu hình → AF-032.1.

---

#### UC-033: Gửi đánh giá hoặc phản hồi 📱

**As a** người dùng có ý kiến (tốt hoặc xấu)
**I want** nói ra đúng chỗ
**So that** nếu tôi vui thì lời khen tới nơi cần tới, còn nếu tôi gặp lỗi thì lỗi được sửa

**Priority**: Medium · **Complexity**: Low

**Preconditions**: người dùng đã dùng app đủ để có ý kiến

**Main Flow**:
1. Sau một khoảnh khắc tích cực (ví dụ: sound đã phát thành công ≥ 5 lần và không có lỗi render nào), WF-030 hiện biến thể "mời đánh giá" — dạng overlay nhẹ, đóng được bằng một chạm.
2. Người dùng chọn mức hài lòng.
3. **Nếu hài lòng** → hệ thống mở dialog đánh giá App Store của iOS.
4. **Nếu không hài lòng** → hệ thống mở WF-028 Sheet Gửi Báo Cáo, **không** đẩy ra App Store.
5. Hệ thống ghi `in_app_rating_submitted`.

**Alternative Flows**:
- **AF-033.1** — Người dùng đóng overlay: không hiện lại trong ≥ 30 ngày.
- **AF-033.2** — Người dùng tự tìm: dòng "Đánh giá Carbina" luôn có trên WF-012.
- **AF-033.3** — Có lỗi render trong 7 ngày gần nhất: hệ thống **không** hiện lời mời đánh giá — mời đánh giá khi app vừa lỗi là cách nhanh nhất để có 1★.

**Postconditions**: ý kiến được gửi đúng kênh: khen ra App Store, phàn nàn về kênh sửa lỗi

**Acceptance Criteria**:
- **AC-033.1**: WHEN người dùng chọn mức không hài lòng THEN hệ thống mở WF-028 và **không** mở dialog đánh giá App Store.
- **AC-033.2**: IF có `widget_render_failed` trong 7 ngày gần nhất THEN hệ thống **không** hiển thị lời mời đánh giá.
- **AC-033.3**: WHEN người dùng đóng lời mời THEN hệ thống không hiển thị lại trong ≥ 30 ngày.
- **AC-033.4**: WHEN lời mời hiển thị THEN nó đóng được bằng một chạm và **không** chặn tác vụ đang làm.

**Screens Involved**: WF-030, WF-028, WF-012
**Primary Screen**: WF-030
**Entry Point**: hệ thống kích hoạt sau khoảnh khắc tích cực, hoặc dòng trên WF-012
**Exit Point**: WF-012 hoặc màn hình trước đó

**Context Variations**:
- **First-time user**: chưa đủ điều kiện kích hoạt — không mời đánh giá người mới dùng 1 ngày.
- **Returning user**: gặp lời mời đúng sau chuỗi trải nghiệm tốt.
- **Power user / Edge case**: gặp lỗi render → AF-033.3 chặn lời mời, và người dùng được đưa sang kênh chẩn đoán (UC-017).

---

#### UC-036: Đổi theme của app 📱

**As a** chủ xe hay lái đêm
**I want** chọn giao diện sáng hoặc tối cho app và cho widget
**So that** màn hình không chói mắt lúc trời tối, và widget trên xe trông đúng ý tôi

**Priority**: Medium · **Complexity**: Low

**Preconditions**: app đã cài; mặc định theo cài đặt sáng/tối của iOS

**Main Flow**:
1. Người dùng mở WF-012 Cài Đặt Chung.
2. Bộ chọn theme ở Zone C hiện giá trị hiện tại: Sáng · Tối · Theo hệ thống.
3. Người dùng chọn một theme → toàn app đổi màu ngay, không cần khởi động lại (sub-flow SF-021).
4. Preview widget nhỏ trong Zone C cập nhật theo, để người dùng thấy hiệu ứng sẽ có trên màn hình xe.
5. Widget trên CarPlay dùng cùng theme ở lần vẽ kế tiếp.

**Alternative Flows**:
- **AF-036.1** — Chọn "Theo hệ thống": app đổi theo cài đặt sáng/tối của iOS, kể cả khi hệ thống tự đổi theo giờ.
- **AF-036.2** — Ghi cấu hình theme vào App Group thất bại: widget tạm dùng theme hệ thống; app vẫn đổi theme bình thường và thử lại ở lần lưu kế tiếp.
- **AF-036.3** — Một thành phần không áp được theme: thành phần đó dùng theme hệ thống thay vì hiện màu sai.

**Postconditions**: theme được lưu và áp dụng cho **cả** app iPhone và widget CarPlay

**Acceptance Criteria**:
- **AC-036.1**: WHEN người dùng chọn một theme THEN toàn bộ UI chuyển sang theme đó ngay, không cần khởi động lại app.
- **AC-036.2**: WHEN theme được đổi THEN preview widget trong Cài Đặt Chung cập nhật theo để người dùng thấy hiệu ứng trên màn hình xe.
- **AC-036.3**: IF người dùng chọn "Theo hệ thống" THEN app đổi theo cài đặt sáng/tối của iOS mà không cần thao tác thêm.

**Screens Involved**: WF-012, WF-017
**Primary Screen**: WF-012
**Entry Point**: bộ chọn theme trên WF-012
**Exit Point**: WF-012 (ở lại)

**Context Variations**:
- **First-time user**: mặc định "Theo hệ thống" — người dùng không phải chọn gì và vẫn đúng ý trong phần lớn trường hợp.
- **Returning user**: chọn thủ công một lần rồi không sửa nữa; giá trị hiện tại luôn thấy được ngay trên dòng ở WF-012.
- **Power user / Edge case**: hay lái đêm nên đổi sang Tối cố định để không bị hệ thống tự đổi lại; và cần thấy trước hiệu ứng trên widget vì đó là bề mặt họ nhìn khi lái.

> **Ghi chú về nguồn gốc UC này**: UC-036 được bổ sung **sau khi `Functional_Requirements.md` được viết**. Rà soát hành động phụ ở §4.12 (WF-012 Layer 2) phát hiện "đổi theme" là một hành vi người dùng thấy được nhưng chưa có UC và chưa có AC — nghĩa là FR-061 sẽ không có tiêu chí chấp nhận nào để truy vết. Theo `project-docs-contract` ("nếu tài liệu downstream phát hiện lỗ hổng upstream thì sửa upstream trước, rồi tái sinh downstream"), UC-036 được thêm ở đây thay vì để tầng FR tự nghĩ ra AC. ID mới được cấp tiếp dãy hiện tại, **không** đánh số lại bất kỳ UC nào.

---

### 2.7 Post-MVP

> Hai UC dưới đây **không thuộc phạm vi thi công MVP 1**. Chúng được đặc tả ở đây để cây màn hình và lớp dữ liệu không phải đập đi làm lại ở MVP 2/MVP 3 (xem `Project_Overview.md` §4.2 và §3.3 Quyết định 7).

#### UC-034: Gọi nhanh liên hệ từ màn hình xe 🚗 — *MVP 2*

**As a** người bận (Jordan — Busy Professional)
**I want** gọi 5 người tôi hay gọi bằng một lần chạm
**So that** tôi không phải rời mắt khỏi đường để tìm số

**Priority**: Medium · **Complexity**: Medium · **Phạm vi**: MVP 2 (tháng 12/2026)

**Preconditions**: quyền Contacts đã được cấp; đã chọn ≥ 1 favorite

**Main Flow**:
1. Người dùng chọn tối đa 5 favorite trên iPhone (màn hình mới của MVP 2).
2. Thẻ shortcut liên hệ xuất hiện trên WF-016.
3. Người dùng chạm một liên hệ → cuộc gọi bắt đầu qua hệ thống.

**Alternative Flows**:
- **AF-034.1** — Quyền Contacts bị từ chối: thẻ không xuất hiện; **không** hiện thẻ rỗng.
- **AF-034.2** — Liên hệ có nhiều số: dùng số mặc định đã chọn sẵn trên iPhone, không hỏi lại trên xe.

**Postconditions**: cuộc gọi được thực hiện qua hệ thống; app không xử lý cuộc gọi

**Acceptance Criteria**:
- **AC-034.1**: WHEN người dùng chạm một thẻ liên hệ THEN cuộc gọi bắt đầu qua hệ thống trong ≤ 1s.
- **AC-034.2**: WHEN thẻ liên hệ hiển thị THEN có tối đa 5 favorite và mọi touch target ≥ 44pt.
- **AC-034.3**: IF quyền Contacts bị từ chối THEN thẻ liên hệ **không** xuất hiện trên WF-016.
- **AC-034.4**: IF liên hệ có nhiều số THEN hệ thống dùng số mặc định và **không** hỏi lại trên màn hình xe.

**Screens Involved**: WF-016 (+ màn hình chọn favorite sẽ được thêm ở MVP 2)
**Primary Screen**: WF-016
**Entry Point**: thẻ shortcut trên WF-016
**Exit Point**: app điện thoại của hệ thống

**Context Variations**:
- **First-time user**: chưa chọn favorite → thẻ hiện lời mời cấu hình trên iPhone, không hiện danh sách rỗng.
- **Returning user**: 5 favorite cố định, chạm 1 lần.
- **Power user / Edge case**: quyền bị từ chối, liên hệ nhiều số → AF-034.1, AF-034.2.

---

#### UC-035: Đồng bộ cấu hình qua cloud 📱 — *MVP 3*

**As a** người dùng có nhiều thiết bị
**I want** cấu hình widget và sound của tôi có mặt trên thiết bị khác
**So that** tôi không phải làm lại từ đầu khi đổi điện thoại

**Priority**: Low · **Complexity**: High · **Phạm vi**: MVP 3 (tháng 3/2027) · **Bắt buộc là optional, opt-in**

**Preconditions**: người dùng chủ động bật đồng bộ và đăng nhập email

**Main Flow**:
1. Người dùng mở WF-015 Account → đăng nhập bằng email.
2. Bật "Đồng bộ cấu hình" → cấu hình widget/sound/ngôn ngữ được đẩy lên cloud.
3. Trên thiết bị thứ hai, đăng nhập cùng email → cấu hình được tải về.

**Alternative Flows**:
- **AF-035.1** — Người dùng không muốn tài khoản: app hoạt động đầy đủ như MVP 1, **không** bắt tạo tài khoản.
- **AF-035.2** — Xung đột cấu hình giữa hai thiết bị: hệ thống hỏi giữ bản nào, không tự ghi đè.
- **AF-035.3** — Người dùng xoá tài khoản: dữ liệu cloud bị xoá; dữ liệu on-device vẫn còn.

**Postconditions**: cấu hình có mặt trên các thiết bị đã đăng nhập; dữ liệu học ngữ cảnh **vẫn ở lại trên từng thiết bị**

**Acceptance Criteria**:
- **AC-035.1**: WHEN người dùng không bật đồng bộ THEN app hoạt động đầy đủ và **không** yêu cầu tài khoản.
- **AC-035.2**: WHEN đồng bộ được bật THEN chỉ cấu hình được đẩy lên cloud; **dữ liệu học ngữ cảnh không rời thiết bị**.
- **AC-035.3**: IF có xung đột cấu hình THEN hệ thống hỏi người dùng chọn bản nào, không tự ghi đè.
- **AC-035.4**: WHEN người dùng xoá tài khoản THEN toàn bộ dữ liệu cloud bị xoá.

**Screens Involved**: WF-015, WF-012
**Primary Screen**: WF-015
**Entry Point**: dòng "Tài khoản" trên WF-012
**Exit Point**: WF-012

**Context Variations**:
- **First-time user**: không gặp mục này ở MVP 1; ở MVP 3 nó là tuỳ chọn, không phải bước bắt buộc.
- **Returning user**: đăng nhập một lần rồi quên nó đi.
- **Power user / Edge case**: hai thiết bị cấu hình khác nhau → AF-035.2; muốn rút khỏi cloud → AF-035.3.

---

## 2 bis. Feature Expression Matrix

Cùng một UC được **biểu đạt khác nhau** ở từng màn hình. Với Carbina, chiều khác biệt mạnh nhất không phải "nút to hay nút nhỏ" mà là **bề mặt**: cái gì diễn ra trên iPhone (người dùng đứng yên, đọc được, gõ được) so với cái gì diễn ra trên màn hình xe (người dùng đang lái, chỉ nhìn thoáng, tối đa một chạm, **không modal**). Mọi dòng có màn hình 🚗 đều chịu ràng buộc đó.

| UC ID | Primary Screen | Primary Expression | Secondary Screen | Secondary Expression | Context Trigger | Expression Difference |
|---|---|---|---|---|---|---|
| UC-001 | WF-002 | Full CTA "Bắt đầu" + thanh tiến trình | WF-006 | Empty State CTA — thẻ "Hoàn tất thiết lập" nếu bỏ dở | Người dùng thoát giữa onboarding | Primary là luồng tuyến tính bắt buộc; secondary là lời nhắc thụ động trong hub, bỏ qua được, mật độ thông tin thấp hơn nhiều |
| UC-002 | WF-003 | Compact Row 3 tầng (hãng → model → năm) + ô tìm kiếm | WF-006 | Inline Action — thẻ xe hiện tại, chạm để đổi | Người dùng mua xe mới | Primary là luồng chọn từ đầu, mật độ cao; secondary là lối tắt 2 chạm cho người đã biết mình muốn gì |
| UC-003 | WF-021 | Modal / Sheet — 3 ô điền, nút Gửi | WF-003 | Inline Action — dòng "Không tìm thấy xe của tôi" ở cuối danh sách | Tìm không ra kết quả | Primary là tác vụ tập trung; secondary là điểm phát hiện vấn đề, chỉ là một dòng chữ không chiếm chỗ |
| UC-004 | WF-005 | Compact Row mỗi quyền + trạng thái | WF-022 | Modal / Sheet — giải thích sâu một quyền | Chạm "Tìm hiểu thêm" | Primary là bảng tổng quan để quyết nhanh; secondary là nội dung dài để người cẩn thận đọc kỹ — hai mật độ thông tin đối lập |
| UC-004 | WF-005 | Compact Row + trạng thái | WF-012 | Compact Row "Quyền" có chevron dẫn Cài đặt hệ thống | Người dùng đổi ý sau onboarding | Primary xảy ra một lần trong luồng; secondary là điểm tra cứu thường trực, không có tính thúc đẩy |
| UC-005 | WF-006 | Inline Action — một dòng mời cấp quyền, tĩnh | WF-009 | Inline Expand — dòng giải thích vì sao câu chào đơn điệu | Mọi quyền bị từ chối | Primary nói ở cấp app; secondary nói ở đúng tính năng bị ảnh hưởng — đúng ngữ cảnh nên thuyết phục hơn mà không cần lặp lại |
| UC-006 | WF-020 | Modal / Sheet — nghe kỹ + slider âm lượng + nút áp dụng | WF-007 | Compact Row — chạm dòng để nghe inline | Đang duyệt danh sách | Primary là nghe tập trung có thao tác kèm theo; secondary là nghe nhanh không rời danh sách, 1 chạm |
| UC-006 | WF-020 | Modal / Sheet | WF-004 | Full CTA trong luồng onboarding — nghe rồi "Tiếp tục" | Bước 3 của onboarding | Primary là khám phá tự do; secondary là bước bắt buộc tuyến tính, chỉ có một đường ra |
| UC-007 | WF-007 | Full CTA "Chọn cho lúc lên xe" | WF-020 | Inline Action — nút áp dụng ngay trong sheet nghe thử | Đang nghe kỹ một preset | Primary là quyết định sau khi đã so sánh; secondary là quyết định ngay tại khoảnh khắc nghe thấy — timing khác nhau |
| UC-008 | WF-007 | Segmented control 3 sự kiện (Connect/Disconnect/Arrive) | WF-006 | Compact Row — tóm tắt cả 3 sound đã gán | Kiểm tra lại cấu hình | Primary là nơi thao tác cho từng sự kiện; secondary là ảnh chụp trạng thái, chỉ đọc |
| UC-009 | WF-012 | Stepper Control — slider âm lượng bền vững | WF-020 | Stepper Control inline — điều chỉnh trong lúc đang nghe | Đang nghe thử | Cùng dạng điều khiển nhưng khác **thời điểm**: primary là cấu hình nguội, secondary là điều chỉnh có phản hồi âm thanh tức thì |
| UC-009 | WF-012 | Stepper Control | WF-007 | Notification / Badge — icon âm lượng ở thanh trên | Đang duyệt thư viện | Secondary chỉ là lối vào, không phải nơi điều chỉnh — mật độ tối thiểu |
| UC-010 | WF-016 🚗 | Không có UI — hành vi âm thanh nền khi lên xe | WF-020 | Modal / Sheet — bản nghe thử **có ducking thật** trên iPhone | Nghe thử trước khi ra xe | Đây là cặp biểu đạt quan trọng nhất của app: cùng một tính năng, một lần **nghe trước** (có UI, có kiểm soát), một lần **diễn ra thật** (không UI, không kiểm soát) |
| UC-011 | WF-016 🚗 | Không có UI — phát lúc tắt máy | WF-007 | Compact Row tab "Disconnect" — nơi cấu hình | Cấu hình trước | Primary là khoảnh khắc thật, không có bề mặt; secondary là nơi duy nhất người dùng có thể tác động tới nó |
| UC-012 | WF-008 | Full CTA — luồng tạo widget đầy đủ | WF-006 | Inline Action — thẻ widget hiện tại, chạm để đổi | Muốn đổi nhanh | Primary là tạo mới, nhiều bước; secondary là đổi, 2 chạm — khác cả ý định lẫn số bước |
| UC-012 | WF-008 | Full CTA | WF-023 | Inline Action trong modal preview — sửa tại nơi phát hiện lệch | Thấy preview không ổn | Secondary là sửa lỗi ngay tại điểm phát hiện, không phải quay lại đầu luồng |
| UC-013 | WF-023 | Modal — vuốt ngang qua các tỉ lệ màn hình xe | WF-008 | Inline Expand — preview nhỏ nhúng trong trang cấu hình | Đang cấu hình | Primary là kiểm tra kỹ nhiều tỉ lệ, chiếm toàn màn hình; secondary là xác nhận thoáng qua ở một tỉ lệ |
| UC-013 | WF-023 | Modal nhiều tỉ lệ | WF-014 | Compact Row — hiển thị kích thước scene thật đã nhận | Sau khi đã cắm xe | Secondary là dữ liệu kỹ thuật thật thay cho ước lượng — cùng thông tin, khác độ chắc chắn |
| UC-014 | WF-024 | Modal / Sheet — chọn nguồn ảnh + khung crop | WF-008 | Inline Action — ô ảnh trên trang cấu hình | Đang tạo widget | Primary là tác vụ chọn và crop; secondary chỉ là điểm khởi phát, một ô |
| UC-015 | WF-017 🚗 | Consumption — widget render, không tương tác | WF-023 | Modal preview trên iPhone | Trước khi ra xe | Cùng nội dung, khác bề mặt và khác quyền tương tác: trên xe chỉ được nhìn, trên iPhone được sửa |
| UC-015 | WF-017 🚗 | Consumption | WF-018 🚗 | Inline Action — một dòng gợi ý nâng cấp cạnh widget | Người dùng gói Free | Secondary là lớp thông tin thêm **không chắn nội dung, không popup** — ràng buộc an toàn khi đang lái |
| UC-016 | WF-019 🚗 | Consumption — thông báo lỗi chỉ để đọc | WF-006 | Notification / Badge — dòng cảnh báo dẫn tới chẩn đoán | Mở app sau chuyến bị lỗi | Primary xảy ra khi đang lái nên **không được có hành động**; secondary xảy ra khi đã đỗ xe nên mới có hành động |
| UC-017 | WF-014 | Management — bảng dữ liệu kỹ thuật | WF-028 | Modal / Sheet — danh sách dữ liệu sẽ gửi + nút Gửi | Chạm "Gửi báo cáo" | Primary là tra cứu; secondary là hành động gửi, tách riêng để người dùng thấy rõ dữ liệu gì rời khỏi máy |
| UC-017 | WF-014 | Management | WF-019 🚗 | Compact text — hướng dẫn mở màn chẩn đoán trên iPhone | Lỗi xảy ra trên xe | Secondary chỉ là con trỏ, không phải nơi làm việc — vì đang lái |
| UC-018 | WF-009 | Toggle chính ở đầu màn hình | WF-006 | Compact Row — trạng thái giọng chào trên thẻ | Xem tổng quan | Primary là công tắc; secondary là chỉ báo trạng thái, không bấm được để tắt (tránh tắt nhầm) |
| UC-019 | WF-009 | Compact Row 4 nguồn, mỗi nguồn 1 toggle + ví dụ câu chào | WF-022 | Modal / Sheet — giải thích một nguồn cần quyền gì | Nguồn cần quyền chưa có | Primary là bảng cấu hình; secondary là nội dung thuyết phục cho đúng một nguồn |
| UC-020 | WF-009 | Full CTA "Nghe thử" — sinh câu chào thật | WF-010 | Full-Screen Upsell — nghe thử được, nhưng nút chuyển thành "Mở khoá" | Người dùng gói Free | Cùng hành động nghe, khác **kết quả sau khi nghe**: một bên áp dụng được, một bên dẫn tới quyết định mua |
| UC-021 | WF-016 🚗 | Không có UI — câu chào phát khi lên xe | WF-009 | Full CTA "Nghe thử" trên iPhone | Trước khi ra xe | Cặp "nghe trước / diễn ra thật" — đây là cơ chế trực tiếp chống R-10 và R-13: người dùng xác minh được tính năng có thật trước khi tin quảng cáo |
| UC-022 | WF-016 🚗 | Discovery — các thẻ tự sắp xếp theo ngữ cảnh | WF-018 🚗 | Consumption — bản cơ bản của cùng dashboard cho gói Free | Người dùng gói Free | Cùng màn hình, khác số thẻ và khác mức cá nhân hóa — không phải bản bị làm mờ mà là cấu hình Free đã chốt |
| UC-023 | WF-016 🚗 | Inline Action — chạm thẻ, 1 chạm là xong | WF-018 🚗 | Compact text — thẻ khoá hiện trạng thái bằng chữ | Thẻ thuộc Premium | Secondary **không mở paywall trên xe** — trạng thái khoá chỉ được nói bằng chữ, đây là ràng buộc cứng |
| UC-024 | WF-006 | Management — hub hiện đủ trạng thái gói Free | WF-007 | Compact Row — nhãn khoá rõ ràng trên preset Premium | Duyệt thư viện âm thanh | Primary nói "bạn đang có gì"; secondary nói "bạn chưa có gì" — hai nửa của cùng một thông điệp, đặt ở hai nơi khác nhau |
| UC-024 | WF-006 | Management | WF-018 🚗 | Inline Action — một dòng tĩnh trên màn hình xe | Đang lái, gói Free | Secondary là biểu đạt yếu nhất có thể: một dòng, không popup, không chắn — vì an toàn khi lái quan trọng hơn conversion |
| UC-025 | WF-010 | Full-Screen Upsell — 4 bậc giá đầy đủ | WF-007 | Inline Action — chạm preset khoá mở paywall theo ngữ cảnh sound | Chạm tính năng khoá | Primary là quyết định chủ động, mật độ thông tin cao; secondary là khoảnh khắc nhận ra giá trị, chỉ nói về đúng thứ vừa chạm |
| UC-025 | WF-010 | Full-Screen Upsell | WF-012 | Compact Row "Nâng cấp" có chevron | Tự tìm trong Settings | Secondary không có tính thúc đẩy, chỉ là lối vào thường trực cho người chủ động |
| UC-026 | WF-011 | Full CTA — màn xác nhận giá cuối | — | **Cố ý chỉ có một vị trí** | — | Nhân bản màn này sẽ tạo khả năng có một đường mua bỏ qua nó — đúng lỗ hổng đã khiến đối thủ bị tố bait-and-switch (R-12). Đây là trường hợp lặp lại có hại; xem justification ở §0.2 |
| UC-027 | WF-011 | Full CTA — bắt đầu trial | WF-006 | Notification / Badge — "Trial còn N ngày" | Trial đang chạy | Primary là hành động một lần; secondary là chỉ báo liên tục, mật độ tối thiểu nhưng luôn hiện |
| UC-027 | WF-011 | Full CTA | WF-012 | Compact Row — trạng thái trial + ngày trừ tiền | Tra cứu chi tiết | Secondary có đủ số liệu chính xác, dành cho người muốn kiểm tra kỹ |
| UC-028 | WF-013 | Full-Screen Upsell — 3 nút ngang hàng gồm cả "Huỷ trial" | WF-025 | Compact Row — nút huỷ trong sheet quản lý | Chủ động muốn huỷ | Primary do hệ thống chủ động mở đúng thời điểm; secondary do người dùng tự tìm — nhưng cả hai đều **không ẩn nút huỷ** |
| UC-029 | WF-025 | Modal / Sheet — trạng thái + huỷ + phục hồi | WF-012 | Compact Row "Đăng ký của tôi" + trạng thái hiện ngay trên dòng | Xem Settings | Primary là nơi thao tác; secondary là nơi thấy trạng thái mà không cần mở gì |
| UC-029 | WF-025 | Modal / Sheet | WF-027 | Alert — xác nhận huỷ, nêu rõ ngày hết quyền | Chạm "Huỷ đăng ký" | Secondary là bước chặn cuối, chỉ một câu hỏi, không có gì khác gây phân tán |
| UC-030 | WF-010 | Full-Screen Upsell — bậc Lifetime trong bảng 4 bậc | WF-011 | Full CTA — xác nhận giao dịch một lần, không có ngày gia hạn | Chọn bậc Lifetime | Secondary khác primary ở chỗ nó **loại bỏ** thông tin gia hạn — sự thiếu vắng đó chính là thông điệp |
| UC-031 | WF-026 | Modal / Sheet — 3 ngôn ngữ + "Theo hệ thống" | WF-012 | Compact Row "Ngôn ngữ" + ngôn ngữ hiện tại | Xem Settings | Primary là nơi chọn; secondary hiện giá trị hiện tại mà không cần mở sheet |
| UC-032 | WF-029 | Alert — xác nhận phá hủy, nêu rõ mất gì | WF-012 | Compact Row "Quyền riêng tư & dữ liệu" | Xem Settings | Primary là điểm chặn không thể bỏ qua; secondary là nơi đọc hiểu trước khi quyết định |
| UC-033 | WF-030 | Success Confirmation + biến thể mời đánh giá | WF-012 | Compact Row "Đánh giá Carbina" | Tự tìm | Primary do hệ thống chọn thời điểm (sau chuỗi trải nghiệm tốt); secondary luôn có sẵn, không có timing |
| UC-033 | WF-030 | Overlay mời đánh giá | WF-028 | Modal / Sheet — kênh báo lỗi cho người **không** hài lòng | Chọn mức không hài lòng | Đây là dòng quan trọng nhất về mặt kinh doanh: cùng một lời mời, nhưng hai nhánh dẫn tới hai nơi hoàn toàn khác nhau — App Store hoặc kênh sửa lỗi |
| UC-036 | WF-012 | Segmented control theme + preview widget nhỏ cập nhật ngay | WF-017 🚗 | Consumption — widget dùng cùng theme ở lần vẽ kế tiếp | Đổi theme trên iPhone | Primary là nơi chọn và **thấy trước** hiệu ứng; secondary là nơi hiệu ứng **thật sự xảy ra**, không có điều khiển nào — cùng cặp "xem trước / diễn ra thật" như UC-010 và UC-021 |
| UC-034 | WF-016 🚗 | Inline Action — thẻ liên hệ, 1 chạm để gọi | (màn hình cấu hình MVP 2) | Compact Row — chọn tối đa 5 favorite | Cấu hình trên iPhone | *MVP 2.* Primary là dùng khi đang lái; secondary là cấu hình khi đã đỗ |
| UC-035 | WF-015 | Management — đăng nhập + toggle đồng bộ | WF-012 | Compact Row "Tài khoản" | Xem Settings | *MVP 3.* Primary là nơi thao tác; secondary là lối vào |

**Kiểm tra quy tắc:**
- Tổng số dòng biểu đạt: **48** (ngưỡng Medium: ≥ 40 ⇒ **Pass**)
- Số UC có ≥ 2 dòng biểu đạt: **34/36**
- UC chỉ có 1 vị trí, đã justify inline: **UC-026** (nhân bản là lỗ hổng bảo mật thương mại — xem dòng tương ứng và §0.2)
- UC có biểu đạt đơn nhưng thuộc phạm vi post-MVP nên chưa mở rộng: **UC-035** (MVP 3, sẽ mở rộng khi lên kế hoạch MVP 3)
- **Không có dòng nào trùng lặp**: mọi dòng secondary khác dòng primary ở ít nhất 2 chiều trong 4 chiều (interaction pattern · information density · user intent · timing). Với các cặp 📱↔🚗, chiều **bề mặt** luôn kèm theo chiều **quyền tương tác**, vì trên màn hình xe người dùng bị giới hạn ở "chỉ nhìn hoặc một chạm".

---

## 3. Use Case to Screen Mapping

### 3.1 UC → Screen Matrix

| UC ID | UC Name | Screens Involved | Primary Screen | Entry | Exit |
|---|---|---|---|---|---|
| UC-001 | Hoàn tất onboarding trong 5 bước | WF-001, WF-002, WF-003, WF-004, WF-005, WF-006 | WF-002 | Mở app lần đầu (từ WF-001) | WF-006 |
| UC-002 | Chọn xe của mình | WF-003, WF-021, WF-006 | WF-003 | WF-002, hoặc thẻ xe trên WF-006 | WF-004 (onboarding) hoặc WF-006 |
| UC-003 | Báo xe không có trong thư viện | WF-021, WF-003, WF-030 | WF-021 | Nút "Không tìm thấy xe của tôi" trên WF-003 | WF-003 |
| UC-004 | Cấp quyền sau khi hiểu rõ lý do | WF-005, WF-022, WF-006, WF-012 | WF-005 | WF-004 (onboarding bước 4) | WF-006 |
| UC-005 | Dùng app dù đã từ chối mọi quyền | WF-006, WF-009, WF-016, WF-017 | WF-006 | Hoàn tất onboarding không cấp quyền | WF-016 (khi lên xe) |
| UC-006 | Nghe thử âm thanh trước khi chọn | WF-007, WF-020, WF-004, WF-010, WF-030 | WF-007 | Tab Sounds trên WF-006, hoặc WF-004 | WF-007 hoặc WF-010 |
| UC-007 | Gán âm thanh cho sự kiện Connect | WF-007, WF-020, WF-006, WF-010, WF-030 | WF-007 | WF-007 hoặc WF-020 | WF-007 hoặc WF-006 |
| UC-008 | Gán âm thanh cho Disconnect và Arrive | WF-007, WF-020, WF-006 | WF-007 | Bộ chọn sự kiện trên WF-007 | WF-006 |
| UC-009 | Điều chỉnh âm lượng sound độc lập | WF-012, WF-020, WF-007 | WF-012 | WF-012, hoặc nút âm lượng trên WF-007 / WF-020 | Ở lại màn hình hiện tại |
| UC-010 | Nghe sound khi lên xe không bị nhạc lấn | WF-016, WF-017 | WF-016 | Sự kiện `carplay_connected` | WF-016 |
| UC-011 | Nghe sound xuống xe đúng lúc tắt máy | WF-016, WF-017 | WF-016 | Sự kiện ngắt kết nối CarPlay | Kết thúc phiên CarPlay |
| UC-012 | Tạo widget đầu tiên | WF-008, WF-023, WF-024, WF-010, WF-006, WF-030 | WF-008 | Tab Widgets, hoặc thẻ widget trên WF-006 | WF-006 hoặc WF-010 |
| UC-013 | Xem trước widget theo tỉ lệ màn hình xe | WF-023, WF-008, WF-024 | WF-023 | Nút "Xem trước trên xe của tôi" trên WF-008 | WF-008 |
| UC-014 | Chọn ảnh xe hoặc ảnh cá nhân | WF-024, WF-008, WF-023, WF-010 | WF-024 | Ô ảnh trên WF-008 hoặc trong WF-023 | WF-008 hoặc WF-023 |
| UC-015 | Xem widget hoạt động trên màn hình xe | WF-017, WF-016, WF-018, WF-019 | WF-017 | Sự kiện `carplay_connected` | WF-016 |
| UC-016 | Phục hồi khi widget không render được | WF-019, WF-016, WF-006, WF-014 | WF-019 | Render thất bại trong UC-015 | WF-016 → WF-014 |
| UC-017 | Chẩn đoán tương thích và gửi báo cáo | WF-014, WF-028, WF-030, WF-006, WF-019 | WF-014 | WF-006 (dòng chẩn đoán) hoặc WF-019 | WF-006 |
| UC-018 | Bật hoặc tắt hoàn toàn giọng chào | WF-009, WF-006, WF-010 | WF-009 | Tab Widgets, hoặc thẻ giọng chào trên WF-006 | WF-009 hoặc WF-006 |
| UC-019 | Chọn nguồn ngữ cảnh cho giọng chào | WF-009, WF-022, WF-012 | WF-009 | WF-009 | WF-009 |
| UC-020 | Nghe thử giọng chào trước khi lên xe | WF-009, WF-010 | WF-009 | Nút "Nghe thử" trên WF-009 | WF-009 |
| UC-021 | Nghe giọng chào cá nhân hóa khi lên xe | WF-016, WF-018 | WF-016 | Sự kiện `carplay_connected` | WF-016 |
| UC-022 | Xem dashboard tự sắp xếp theo ngữ cảnh | WF-016, WF-017, WF-018 | WF-016 | `carplay_connected` → scene active | UC-023 hoặc kết thúc phiên |
| UC-023 | Chạm thẻ gợi ý trên dashboard | WF-016, WF-018 | WF-016 | WF-016 | App hệ thống (nhạc/Maps/điện thoại) hoặc WF-016 |
| UC-024 | Dùng gói Free để tự xác nhận app chạy | WF-006, WF-007, WF-008, WF-016, WF-017, WF-018, WF-010 | WF-006 | Hoàn tất onboarding | WF-010 hoặc tiếp tục dùng Free |
| UC-025 | Xem bảng giá minh bạch | WF-010, WF-011, WF-025, WF-007, WF-008 | WF-010 | Tính năng khoá trên WF-007/WF-008/WF-009, hoặc WF-012 | WF-011 hoặc màn hình trước đó |
| UC-026 | Xác nhận giá cuối trước khi trả tiền | WF-011, WF-010, WF-030 | WF-011 | Chọn một bậc giá trên WF-010 | Màn hình trước paywall hoặc WF-010 |
| UC-027 | Bắt đầu trial 7 ngày | WF-011, WF-006, WF-012, WF-013, WF-025 | WF-011 | Xác nhận bậc có trial ở WF-011 | WF-006 |
| UC-028 | Nhận nhắc trước khi hết trial | WF-013, WF-027, WF-025, WF-012 | WF-013 | Hệ thống kích hoạt ngày 6 và ngày 7 | WF-006 hoặc WF-025 |
| UC-029 | Quản lý hoặc huỷ đăng ký | WF-025, WF-012, WF-027 | WF-025 | Dòng "Đăng ký của tôi" trên WF-012, hoặc WF-013 | WF-012 hoặc trang subscription của iOS |
| UC-030 | Mua gói Lifetime một lần | WF-010, WF-011, WF-025, WF-030 | WF-011 | Bậc Lifetime trên WF-010 | Màn hình trước paywall |
| UC-031 | Đổi ngôn ngữ app | WF-026, WF-012, WF-016 | WF-026 | Dòng "Ngôn ngữ" trên WF-012 | WF-012 |
| UC-032 | Xoá toàn bộ dữ liệu on-device | WF-012, WF-029, WF-030 | WF-012 | Dòng "Quyền riêng tư & dữ liệu" trên WF-012 | WF-012 |
| UC-033 | Gửi đánh giá hoặc phản hồi | WF-030, WF-028, WF-012 | WF-030 | Hệ thống kích hoạt sau khoảnh khắc tích cực, hoặc WF-012 | WF-012 hoặc màn hình trước đó |
| UC-036 | Đổi theme của app | WF-012, WF-017 | WF-012 | Bộ chọn theme trên WF-012 | WF-012 (ở lại) |
| UC-034 | Gọi nhanh liên hệ từ màn hình xe *(MVP 2)* | WF-016 | WF-016 | Thẻ shortcut trên WF-016 | App điện thoại của hệ thống |
| UC-035 | Đồng bộ cấu hình qua cloud *(MVP 3)* | WF-015, WF-012 | WF-015 | Dòng "Tài khoản" trên WF-012 | WF-012 |

**Kiểm tra**: 36/36 UC có Primary Screen ⇒ **không có orphan UC**.

### 3.2 Screen → UC Coverage

| Screen | UCs Covered | Primary UC | Secondary UCs | Screen Purpose |
|---|---|---|---|---|
| **WF-001** Splash / Launch | UC-001 | UC-001 | — | Khởi động app và quyết định vào onboarding hay vào Home |
| **WF-002** Onboarding — Welcome | UC-001 | UC-001 | — | Nói app làm gì trong một câu và mở luồng thiết lập |
| **WF-003** Onboarding — Chọn Xe | UC-002, UC-003 | UC-002 | UC-003 | Xác định xe của người dùng để widget hiển thị đúng hình xe |
| **WF-004** Onboarding — Chọn Âm Thanh | UC-001, UC-006 | UC-006 | UC-001 | Cho người dùng nghe thấy giá trị của app **trước** khi bị hỏi bất cứ điều gì về tiền |
| **WF-005** Onboarding — Cấp Quyền | UC-004, UC-001, UC-005 | UC-004 | UC-001, UC-005 | Xin quyền có lý do rõ ràng, và cho phép từ chối mà không chặn luồng |
| **WF-006** Home (iPhone) | UC-001, UC-002, UC-005, UC-007, UC-008, UC-012, UC-016, UC-017, UC-018, UC-024, UC-027 | UC-024 | UC-005, UC-012, UC-016, UC-017, UC-027 | Hub trạng thái: kết nối CarPlay, widget đang bật, sound đang chọn, cảnh báo tương thích |
| **WF-007** Thư Viện Âm Thanh | UC-006, UC-007, UC-008, UC-009, UC-024, UC-025 | UC-006 | UC-007, UC-008, UC-009, UC-025 | Duyệt và nghe thử toàn bộ preset, thấy rõ cái nào mở cái nào khoá |
| **WF-008** Trình Tạo Widget | UC-012, UC-013, UC-014 | UC-012 | UC-013, UC-014 | Tạo widget từ preset gợi ý — không bao giờ bắt đầu từ canvas rỗng |
| **WF-009** Cài Đặt Giọng Chào | UC-005, UC-018, UC-019, UC-020 | UC-019 | UC-005, UC-018, UC-020 | Kiểm soát app được biết gì và nghe thử để xác minh tính năng có thật |
| **WF-010** Paywall | UC-006, UC-012, UC-018, UC-020, UC-024, UC-025, UC-030 | UC-025 | UC-024, UC-030, UC-020 | Trình bày 4 lựa chọn minh bạch, gồm cả gói Free đang dùng |
| **WF-011** Xác Nhận Giá | UC-026, UC-027, UC-030 | UC-026 | UC-027, UC-030 | Điểm chặn duy nhất trước giao dịch: giá cuối, ngày hết trial, ngày trừ tiền |
| **WF-012** Cài Đặt Chung | UC-004, UC-009, UC-029, UC-031, UC-032, UC-033, UC-035, UC-036 | UC-009 | UC-029, UC-031, UC-032, UC-033, UC-036 | Nơi tra cứu và điều chỉnh mọi thứ không thuộc luồng chính |
| **WF-013** Nhắc Hết Trial | UC-027, UC-028 | UC-028 | UC-027 | Nói trước số tiền và ngày trừ, với nút huỷ ngang hàng nút đăng ký |
| **WF-014** Chẩn Đoán Tương Thích | UC-013, UC-016, UC-017 | UC-017 | UC-013, UC-016 | Biến lỗi tương thích từ "app rác" thành một vấn đề chẩn đoán được (R-11) |
| **WF-015** Account *(MVP 3)* | UC-035 | UC-035 | — | Đăng nhập và bật đồng bộ — luôn là tuỳ chọn, không bắt buộc |
| **WF-016** CarPlay Dashboard 🚗 | UC-005, UC-010, UC-011, UC-021, UC-022, UC-023, UC-034 | UC-022 | UC-023, UC-021, UC-010, UC-011 | Bề mặt sử dụng chính: thẻ tự sắp xếp theo ngữ cảnh, một chạm là xong |
| **WF-017** CarPlay Widget 🚗 | UC-005, UC-010, UC-015, UC-036 | UC-015 | UC-005, UC-010, UC-036 | Thứ người dùng thật sự trả tiền để thấy — phải render đúng ở mọi kích thước |
| **WF-018** CarPlay — Trạng Thái Free 🚗 | UC-021, UC-022, UC-023, UC-024 | UC-024 | UC-022, UC-023, UC-021 | Cho người dùng Free thấy giá trị đang có, bằng một dòng không chắn nội dung |
| **WF-019** CarPlay — Fallback Lỗi 🚗 | UC-015, UC-016 | UC-016 | UC-015 | Bảo đảm **không bao giờ có màn hình trắng** khi render thất bại |
| **WF-020** Sheet — Nghe Thử Âm Thanh | UC-006, UC-007, UC-009, UC-010 | UC-006 | UC-007, UC-009 | Nghe kỹ một preset kèm ducking thật và áp dụng ngay |
| **WF-021** Sheet — Không tìm thấy xe của tôi | UC-002, UC-003 | UC-003 | UC-002 | Không để người dùng bị chặn chỉ vì thư viện xe thiếu model của họ |
| **WF-022** Sheet — Lý Do Xin Quyền | UC-004, UC-019 | UC-004 | UC-019 | Giải thích một quyền đủ sâu cho người cẩn thận, không nhồi vào màn chính |
| **WF-023** Modal — Preview Widget Theo Màn Hình Xe | UC-012, UC-013, UC-014 | UC-013 | UC-012, UC-014 | Cho người dùng phát hiện lỗi cắt nội dung **trước** khi ra xe (R-11) |
| **WF-024** Sheet — Chọn Ảnh Cho Widget | UC-014 | UC-014 | — | Chọn và crop ảnh theo đúng tỉ lệ màn hình xe, cảnh báo ảnh mờ |
| **WF-025** Sheet — Quản Lý Đăng Ký | UC-027, UC-028, UC-029, UC-030 | UC-029 | UC-027, UC-028, UC-030 | Cho thấy trạng thái đăng ký và cho huỷ trong tối đa 3 chạm |
| **WF-026** Sheet — Chọn Ngôn Ngữ | UC-031 | UC-031 | — | Chọn EN/ES/PT-BR cho cả UI và nội dung giọng chào |
| **WF-027** Alert — Xác Nhận Huỷ Trial | UC-028, UC-029 | UC-029 | UC-028 | Điểm chặn cuối khi huỷ, nêu rõ ngày quyền Premium kết thúc |
| **WF-028** Sheet — Gửi Báo Cáo Tương Thích | UC-017, UC-033 | UC-017 | UC-033 | Kênh nhận phản hồi tiêu cực — thay cho việc để người dùng ra App Store |
| **WF-029** Alert — Xoá Dữ Liệu On-Device | UC-032 | UC-032 | — | Điểm chặn cho hành động phá hủy, nêu rõ mất gì và giữ gì |
| **WF-030** Overlay — Toast Xác Nhận | UC-003, UC-007, UC-012, UC-017, UC-026, UC-032, UC-033 | UC-033 | UC-007, UC-012, UC-017 | Xác nhận tác vụ đã xong mà không chặn; kèm biến thể mời đánh giá |

**Kiểm tra**: 30/30 màn hình phủ ≥ 1 UC ⇒ **không có orphan screen**. Tổng 30 màn hình ≥ ngưỡng Medium (25) ⇒ **Pass**.

---

## 4. Screen-Context Use Cases

Mỗi màn hình dưới đây có: **Archetype** (quyết định ngôn ngữ thiết kế) · **Interaction Density** · **đúng một Primary Action** · **Secondary Actions theo 4 tầng** · **4 vùng nội dung** · entry/exit · **≥ 3 biến thể trạng thái** (bắt buộc có First Visit, Returning, Error).

> **Ràng buộc riêng cho 4 màn hình CarPlay (WF-016 → WF-019)**: Interaction Density **không bao giờ vượt Medium**, không có modal, không có nhập liệu, mọi touch target ≥ 44pt. Đây là ràng buộc an toàn, không phải lựa chọn thẩm mỹ. Vì vậy các tầng Layer 3 (Discovery) và Layer 4 (Personal) ở những màn này thường **cố tình để trống** — và việc để trống đó là kết quả của suy nghĩ, không phải bỏ sót.

### 4.1 WF-001 — Splash / Launch 📱

**Screen Archetype**: Consumption · **Interaction Density**: Light (1 vùng, không tương tác)
**Source UCs**: UC-001

**User Intent**: "Tôi muốn app mở ra thật nhanh."

**Primary Action**: Không có hành động người dùng — hệ thống quyết định điểm đến (WF-002 nếu chưa onboard, WF-006 nếu đã onboard)

**Secondary Actions by Layer**:
- **Layer 2 — Contextual**: (trống có chủ ý — mọi tương tác ở đây chỉ làm chậm việc mở app)
- **Layer 3 — Discovery**: (trống có chủ ý)
- **Layer 4 — Personal**: (trống có chủ ý)

**Content Zones**:
- **Zone A (Hero)**: Logo Carbina, canh giữa
- **Zone B (Engagement)**: (trống — không có CTA)
- **Zone C (Discovery)**: (trống)
- **Zone D (Utility)**: Chỉ báo tải, chỉ hiện nếu quá 1s

**Entry Points**: mở app từ home screen iOS · mở từ deep link · quay lại app sau khi bị hệ thống thu hồi
**Exit Points**: WF-002 (chưa onboard) · WF-006 (đã onboard) · WF-014 (nếu có lỗi render chờ chẩn đoán)

**State Variations with Context**:

| State | Context | Layout/Behavior Difference |
|---|---|---|
| First Visit | Chưa onboard | Hiện ≤ 1,5s rồi chuyển WF-002 |
| Returning / Has Data | Đã onboard | Hiện ≤ 1,0s rồi chuyển WF-006; cấu hình được đọc từ cache nên không có trạng thái tải |
| Error | Không đọc được cấu hình on-device | Vào WF-006 ở trạng thái mặc định an toàn kèm một dòng thông báo — **không** hiển thị màn hình lỗi và **không** bắt onboard lại |

---

### 4.2 WF-002 — Onboarding: Welcome 📱

**Screen Archetype**: Discovery · **Interaction Density**: Light (2 vùng)
**Source UCs**: UC-001

**User Intent**: "Tôi muốn biết app này làm gì trước khi bỏ thời gian thiết lập."

**Primary Action**: Chạm "Bắt đầu" để vào luồng thiết lập

**Secondary Actions by Layer**:
- **Layer 2 — Contextual**: Xem thanh tiến trình (1/4) để biết luồng này ngắn
- **Layer 3 — Discovery**: (trống có chủ ý — không có gì để khám phá trước khi thiết lập; thêm vào đây sẽ làm loãng một câu tuyên bố duy nhất)
- **Layer 4 — Personal**: "Phục hồi giao dịch" (chỉ hiện nếu phát hiện đã từng mua)

**Content Zones**:
- **Zone A (Hero)**: Hình minh họa widget trên màn hình xe + một câu nói app làm gì
- **Zone B (Engagement)**: Nút "Bắt đầu"
- **Zone C (Discovery)**: (trống)
- **Zone D (Utility)**: Thanh tiến trình 1/4

**Entry Points**: WF-001 (lần đầu cài)
**Exit Points**: WF-003 (bắt đầu) · WF-006 (nếu phục hồi giao dịch thành công và đã có cấu hình cũ)

**State Variations with Context**:

| State | Context | Layout/Behavior Difference |
|---|---|---|
| First Visit | Cài mới | Một câu tuyên bố + một nút; **không có paywall, không có gì khác** |
| Returning / Has Data | Cài lại sau khi từng mua | Thêm dòng "Phục hồi giao dịch" ở dưới nút chính |
| Error | Không lấy được trạng thái giao dịch từ StoreKit | Ẩn dòng phục hồi thay vì hiện nút bấm không hoạt động; người dùng vẫn vào được luồng thiết lập |

---

### 4.3 WF-003 — Onboarding: Chọn Xe 📱

**Screen Archetype**: Action · **Interaction Density**: Medium (4 vùng)
**Source UCs**: UC-002 (chính), UC-003

**User Intent**: "Tôi muốn app biết xe của tôi để widget trông giống xe thật."

**Primary Action**: Chọn hãng → model → năm và xác nhận

**Secondary Actions by Layer**:
- **Layer 2 — Contextual**: Tìm kiếm hãng/model · quay lại một tầng · xem ảnh xe để đối chiếu
- **Layer 3 — Discovery**: Danh sách hãng sắp theo mức phổ biến ở storefront hiện tại (không theo thứ tự chữ cái) · gợi ý hãng vừa xem
- **Layer 4 — Personal**: "Không tìm thấy xe của tôi" → WF-021 · "Bỏ qua bước này" (dùng ảnh silhouette theo phân khúc)

**Content Zones**:
- **Zone A (Hero)**: Ảnh xe được chọn hiện dần khi người dùng đi sâu vào 3 tầng
- **Zone B (Engagement)**: Nút "Đúng xe của tôi"
- **Zone C (Discovery)**: Danh sách hãng/model cuộn được
- **Zone D (Utility)**: Ô tìm kiếm, thanh tiến trình 2/4, nút quay lại

**Entry Points**: WF-002 (onboarding) · thẻ xe trên WF-006 (đổi xe sau)
**Exit Points**: WF-004 (onboarding) · WF-006 (nếu vào từ Home) · WF-021 (báo thiếu xe)

**State Variations with Context**:

| State | Context | Layout/Behavior Difference |
|---|---|---|
| First Visit | Chưa chọn xe | Danh sách hãng theo mức phổ biến; chưa có ảnh ở Zone A |
| Returning / Has Data | Đổi xe | Xe hiện tại được ghim đầu danh sách và đánh dấu; ảnh xe hiện ngay ở Zone A |
| Power User | Xe không phổ biến | Tìm kiếm khớp cả tên viết tắt và tên nội địa; lối vào WF-021 rõ ràng ở cuối danh sách |
| Error | Không có ảnh cho model đó | Dùng ảnh silhouette theo phân khúc và **nói rõ đang dùng ảnh chung**, không để trống Zone A |

---

### 4.4 WF-004 — Onboarding: Chọn Âm Thanh 📱

**Screen Archetype**: Discovery · **Interaction Density**: Medium (4 vùng)
**Source UCs**: UC-006 (chính), UC-001

**User Intent**: "Tôi muốn nghe xem app này nghe như thế nào."

**Primary Action**: Nghe thử và chọn một sound cho lúc lên xe

**Secondary Actions by Layer**:
- **Layer 2 — Contextual**: Chạm để nghe inline · dừng · chọn
- **Layer 3 — Discovery**: Duyệt các nhóm sound · xem preset nào thuộc Free và preset nào khoá (**nghe thử được cả hai**)
- **Layer 4 — Personal**: "Chọn sau" (bỏ qua, hệ thống gán preset Free đầu tiên)

**Content Zones**:
- **Zone A (Hero)**: Sound đang phát, có chỉ báo dạng sóng để thấy nó thật sự đang phát
- **Zone B (Engagement)**: Nút "Dùng sound này"
- **Zone C (Discovery)**: Danh sách preset theo nhóm
- **Zone D (Utility)**: Thanh tiến trình 3/4, nút quay lại, nút "Chọn sau"

**Entry Points**: WF-003 (onboarding bước 3)
**Exit Points**: WF-005 (tiếp tục)

**State Variations with Context**:

| State | Context | Layout/Behavior Difference |
|---|---|---|
| First Visit | Chưa nghe gì | Preset đầu tiên tự phát một lần để người dùng biết ngay nút này làm gì |
| Returning / Has Data | Đã có sound (vào lại từ WF-007) | Sound hiện tại được ghim đầu và đánh dấu đang dùng |
| Power User | Đang cắm tai nghe hoặc đang phát nhạc | Áp dụng ducking thật; hiện một dòng nói rõ trên xe âm thanh sẽ phát qua loa xe |
| Error | Không phát được (phiên audio bị chiếm) | Hiện lý do cụ thể kèm nút thử lại; **không** chặn nút "Tiếp tục" |

---

### 4.5 WF-005 — Onboarding: Cấp Quyền 📱

**Screen Archetype**: Action · **Interaction Density**: Medium (4 vùng)
**Source UCs**: UC-004 (chính), UC-001, UC-005

**User Intent**: "Tôi muốn biết app cần gì của tôi và để làm gì, trước khi tôi đồng ý."

**Primary Action**: Quyết định cấp hoặc từ chối từng quyền rồi chạm "Tiếp tục"

**Secondary Actions by Layer**:
- **Layer 2 — Contextual**: Chạm "Tìm hiểu thêm" ở từng quyền → WF-022 · xem trạng thái hiện tại của từng quyền
- **Layer 3 — Discovery**: Xem ví dụ cụ thể app sẽ làm được gì khi có quyền đó
- **Layer 4 — Personal**: "Bỏ qua tất cả" — **luôn khả dụng, không bị làm mờ**

**Content Zones**:
- **Zone A (Hero)**: Một câu cam kết: dữ liệu không rời thiết bị
- **Zone B (Engagement)**: Nút "Tiếp tục" (luôn bấm được, kể cả khi chưa cấp quyền nào)
- **Zone C (Discovery)**: Hai thẻ quyền (Vị trí, Lịch), mỗi thẻ có lý do + ví dụ + trạng thái
- **Zone D (Utility)**: Thanh tiến trình 4/4, nút quay lại, "Bỏ qua tất cả"

**Entry Points**: WF-004 (onboarding bước 4)
**Exit Points**: WF-006 (hoàn tất) · WF-022 (tìm hiểu thêm về một quyền)

**State Variations with Context**:

| State | Context | Layout/Behavior Difference |
|---|---|---|
| First Visit | Chưa hỏi quyền nào | Cả hai thẻ ở trạng thái "Chưa hỏi"; nút "Tiếp tục" đã bấm được |
| Returning / Has Data | Vào lại từ WF-012 | Thẻ hiện trạng thái thật; quyền đã bị từ chối thì dẫn sang Cài đặt hệ thống thay vì gọi lại dialog |
| Power User | Cấp Vị trí ở mức "Khi dùng app" | Nêu rõ tuyến đường chỉ học được khi app đang mở — không im lặng để người dùng tưởng đã đủ |
| Error | Dialog quyền của iOS không mở được | Nêu rõ và dẫn sang Cài đặt hệ thống; **không** chặn nút "Tiếp tục" |

---

### 4.6 WF-006 — Home (iPhone) 📱

**Screen Archetype**: Management · **Interaction Density**: Dense (7 vùng tương tác)
**Source UCs**: UC-024 (chính), UC-001, UC-002, UC-005, UC-007, UC-008, UC-012, UC-016, UC-017, UC-018, UC-027

**User Intent**: "Tôi muốn biết mọi thứ đang ở trạng thái nào và sửa nhanh thứ tôi cần."

**Primary Action**: Xem trạng thái kết nối CarPlay và trạng thái từng thành phần (widget · sound · giọng chào · xe)

**Secondary Actions by Layer**:
- **Layer 2 — Contextual**: Chạm thẻ widget → WF-008 · chạm thẻ sound → WF-007 · chạm thẻ giọng chào → WF-009 · chạm thẻ xe → WF-003
- **Layer 3 — Discovery**: Thẻ "Chưa thử trên xe? Cắm CarPlay để xem widget" · gợi ý tính năng chưa dùng
- **Layer 4 — Personal**: Trạng thái gói hiện tại (Free / Trial còn N ngày / Premium / Lifetime) · lối vào WF-012 · lối vào WF-014 khi có cảnh báo

**Content Zones**:
- **Zone A (Hero)**: Trạng thái kết nối CarPlay + ảnh xe đã chọn
- **Zone B (Engagement)**: Thẻ widget đang dùng — thẻ lớn nhất, vì đó là thứ người dùng quan tâm nhất
- **Zone C (Discovery)**: Thẻ sound, thẻ giọng chào, thẻ gợi ý tính năng chưa dùng
- **Zone D (Utility)**: Tab bar 4 tab, badge trạng thái gói, dòng cảnh báo tương thích (chỉ khi có)

**Entry Points**: WF-001 (đã onboard) · hoàn tất onboarding từ WF-005 · tab Home từ bất kỳ tab nào · quay lại từ mọi màn hình con
**Exit Points**: WF-003 · WF-007 · WF-008 · WF-009 · WF-012 · WF-014 · WF-010

**State Variations with Context**:

| State | Context | Layout/Behavior Difference |
|---|---|---|
| First Visit | Vừa onboard xong, chưa cắm xe | Zone A hiện "Chưa kết nối CarPlay" + hướng dẫn cắm xe; Zone C hiện thẻ mời thử trên xe |
| Returning / Has Data | Đã cắm xe ≥ 1 lần | Zone A hiện lần kết nối gần nhất và kết quả render; thẻ gợi ý biến mất khi đã dùng hết |
| Power User | Premium, đã cấu hình đầy đủ | Mọi thẻ ở trạng thái đầy đủ; không có thẻ mời hay thẻ gợi ý nào — mật độ giảm khi người dùng đã thành thạo |
| Trial đang chạy | Trial ngày 1–7 | Badge "Trial còn N ngày" ở Zone D, kèm ngày trừ tiền — không dùng đếm ngược gây áp lực |
| Error | Có `widget_render_failed` ở phiên gần nhất | Zone D hiện một dòng cảnh báo dẫn tới WF-014; dòng này **tự biến mất** khi lần render kế tiếp thành công |

---

### 4.7 WF-007 — Thư Viện Âm Thanh 📱

**Screen Archetype**: Discovery · **Interaction Density**: Dense (6 vùng)
**Source UCs**: UC-006 (chính), UC-007, UC-008, UC-009, UC-024, UC-025

**User Intent**: "Tôi muốn nghe hết các lựa chọn rồi chọn cái nghe hay nhất trên xe của tôi."

**Primary Action**: Nghe thử một preset và gán nó cho một sự kiện

**Secondary Actions by Layer**:
- **Layer 2 — Contextual**: Chạm dòng để nghe inline · mở WF-020 để nghe kỹ · gán cho sự kiện đang chọn · dừng phát
- **Layer 3 — Discovery**: Chuyển giữa 3 sự kiện (Connect / Disconnect / Arrive) · duyệt theo nhóm sound · xem preset khoá (nghe thử được đầy đủ)
- **Layer 4 — Personal**: Nút âm lượng ở thanh trên → điều chỉnh âm lượng sound · "Sound đang dùng" ghim đầu danh sách

**Content Zones**:
- **Zone A (Hero)**: Sound đang phát + dạng sóng + sự kiện đang cấu hình
- **Zone B (Engagement)**: Nút gán "Dùng cho lúc lên xe" (đổi nhãn theo sự kiện đang chọn)
- **Zone C (Discovery)**: Danh sách preset theo nhóm, mỗi dòng có nhãn Free/khoá rõ ràng
- **Zone D (Utility)**: Segmented control 3 sự kiện, nút âm lượng, nút đóng

**Entry Points**: Tab Sounds · thẻ sound trên WF-006 · quay lại từ WF-020
**Exit Points**: WF-020 (nghe kỹ) · WF-010 (chạm preset khoá) · WF-006 · WF-012 (âm lượng)

**State Variations with Context**:

| State | Context | Layout/Behavior Difference |
|---|---|---|
| First Visit | Mới có 1 sound từ onboarding | Sound đã gán được ghim đầu; các nhóm khác đều mở để khuyến khích nghe thử |
| Returning / Has Data | Đã gán cả 3 sự kiện | Segmented control hiện dấu đã cấu hình ở từng sự kiện; danh sách mở ở sự kiện gần nhất |
| Power User | Premium, nghe thử nhiều | Nghe liền mạch: chạm dòng khác là dừng dòng cũ ngay, không phát chồng, không cần chạm dừng |
| Free tier | Gói Free | 3 preset mở có nhãn "Đang dùng được"; preset khoá vẫn nghe thử **đầy đủ**, chỉ nút gán chuyển thành "Mở khoá" |
| Error | Phiên audio bị chiếm (đang có cuộc gọi) | Nêu rõ lý do không phát được kèm nút thử lại; danh sách vẫn duyệt được bình thường |

---

### 4.8 WF-008 — Trình Tạo Widget 📱

**Screen Archetype**: Management · **Interaction Density**: Dense (6 vùng)
**Source UCs**: UC-012 (chính), UC-013, UC-014

**User Intent**: "Tôi muốn có một widget đẹp trên màn hình xe mà không phải học cách dùng công cụ."

**Primary Action**: Chọn một preset widget và lưu nó

**Secondary Actions by Layer**:
- **Layer 2 — Contextual**: Chọn loại widget · chạm ô ảnh → WF-024 · đổi tên widget · lưu
- **Layer 3 — Discovery**: Duyệt preset gợi ý theo xe đã chọn · xem preset thuộc Premium (xem trước được đầy đủ)
- **Layer 4 — Personal**: "Xem trước trên xe của tôi" → WF-023 · bản nháp đang làm (nếu có)

**Content Zones**:
- **Zone A (Hero)**: Preview widget nhúng, tỉ lệ theo kích thước xe đã biết (hoặc tỉ lệ tham chiếu)
- **Zone B (Engagement)**: Nút "Lưu widget" (hoặc "Mở khoá" nếu preset thuộc Premium)
- **Zone C (Discovery)**: Hàng preset gợi ý cuộn ngang + các loại widget (ảnh xe / ảnh cá nhân / counter)
- **Zone D (Utility)**: Nút "Xem trước trên xe của tôi", nút đóng, chỉ báo giới hạn widget của gói hiện tại

**Entry Points**: Tab Widgets · thẻ widget trên WF-006 · quay lại từ WF-023 hoặc WF-024
**Exit Points**: WF-023 · WF-024 · WF-010 · WF-006

**State Variations with Context**:

| State | Context | Layout/Behavior Difference |
|---|---|---|
| First Visit | Chưa có widget | Zone C hiện **≥ 3 preset gợi ý theo xe vừa chọn**; Zone A đã có preview ngay — **tuyệt đối không có canvas rỗng** |
| Returning / Has Data | Đã có widget | Widget hiện tại được nạp sẵn vào Zone A; nút chính đổi thành "Lưu thay đổi" |
| Power User | Premium, dùng ảnh cá nhân | Mở thêm loại widget ảnh cá nhân và counter; lối vào WF-024 nổi bật hơn |
| Free tier | Đã dùng hết 1 widget | Nêu rõ giới hạn 1 widget và cho **đổi** widget hiện có; nút "Thêm widget thứ hai" dẫn WF-010 |
| iOS < 17.4 | Không hỗ trợ widget CarPlay | Nêu rõ yêu cầu iOS 17.4+ ở Zone D, **vẫn cho cấu hình** để sẵn sàng khi nâng cấp; không giả vờ widget đang chạy |
| Error | Không lưu được vào App Group | Nêu lỗi cụ thể kèm nút thử lại; giữ bản nháp, không mất cấu hình đang làm |

---

### 4.9 WF-009 — Cài Đặt Giọng Chào 📱

**Screen Archetype**: Action · **Interaction Density**: Medium (5 vùng)
**Source UCs**: UC-019 (chính), UC-005, UC-018, UC-020

**User Intent**: "Tôi muốn nghe thử câu chào và quyết định app được biết gì về tôi."

**Primary Action**: Chạm "Nghe thử" để xác minh tính năng, rồi bật/tắt từng nguồn ngữ cảnh

**Secondary Actions by Layer**:
- **Layer 2 — Contextual**: Công tắc chính bật/tắt giọng chào · bật/tắt từng nguồn ngữ cảnh · nghe thử lại
- **Layer 3 — Discovery**: Xem ví dụ câu chào cụ thể của từng nguồn · xem chữ của câu chào đang phát
- **Layer 4 — Personal**: Lối vào cấp quyền cho nguồn còn thiếu (→ WF-022 hoặc Cài đặt hệ thống)

**Content Zones**:
- **Zone A (Hero)**: Câu chào vừa sinh, hiển thị bằng chữ — bằng chứng tính năng có thật
- **Zone B (Engagement)**: Nút "Nghe thử"
- **Zone C (Discovery)**: 4 dòng nguồn ngữ cảnh (giờ / thời tiết / lịch / điểm đến), mỗi dòng có toggle + ví dụ + trạng thái quyền
- **Zone D (Utility)**: Công tắc chính ở đầu màn hình, nút đóng

**Entry Points**: Tab Widgets · thẻ giọng chào trên WF-006
**Exit Points**: WF-022 (cấp quyền) · WF-010 (nếu Free) · WF-006

**State Variations with Context**:

| State | Context | Layout/Behavior Difference |
|---|---|---|
| First Visit | Chưa có quyền nào | Chỉ nguồn "giờ trong ngày" hoạt động; 3 nguồn kia hiện "cần quyền" kèm lối vào — **không** im lặng để người dùng tưởng app lỗi |
| Returning / Has Data | Đã có quyền, đã dùng vài ngày | Cả 4 nguồn hoạt động; câu chào ở Zone A phong phú hơn rõ rệt |
| Power User | Chạm "Nghe thử" nhiều lần | Mỗi lần một câu khác; sau ≥ 4 lần người dùng thấy đủ dải biến thể |
| Free tier | Gói Free | **Nghe thử được đầy đủ**; công tắc chính hiện trạng thái khoá kèm nút mở khoá dẫn WF-010 |
| Error | TTS không phát được | Vẫn hiển thị chữ câu chào ở Zone A kèm lý do không phát được — nội dung vẫn kiểm chứng được dù âm thanh lỗi |

---

### 4.10 WF-010 — Paywall 📱

**Screen Archetype**: Action · **Interaction Density**: Medium (5 vùng)
**Source UCs**: UC-025 (chính), UC-006, UC-012, UC-018, UC-020, UC-024, UC-030

**User Intent**: "Tôi muốn biết mình phải trả bao nhiêu để có thứ tôi vừa chạm vào, và có lựa chọn nào khác."

**Primary Action**: Chọn một trong 4 lựa chọn (Free đang dùng · Monthly · Yearly · Lifetime)

**Secondary Actions by Layer**:
- **Layer 2 — Contextual**: Xem danh sách tính năng mở khóa của từng bậc · đóng paywall
- **Layer 3 — Discovery**: So sánh bậc · xem bậc được nhấn mạnh theo tính năng vừa chạm
- **Layer 4 — Personal**: "Phục hồi giao dịch" (ngang hàng với các bậc, không ẩn) · "Tiếp tục dùng gói Free"

**Content Zones**:
- **Zone A (Hero)**: Nói rõ tính năng nào đang khoá và nó làm được gì (theo ngữ cảnh nơi người dùng vừa chạm)
- **Zone B (Engagement)**: 4 thẻ lựa chọn, **giá cuối bằng tiền tệ địa phương**
- **Zone C (Discovery)**: Bảng so sánh Free ↔ Premium
- **Zone D (Utility)**: Nút đóng, "Phục hồi giao dịch", link điều khoản và quyền riêng tư

**Entry Points**: preset khoá trên WF-007 · loại widget khoá trên WF-008 · công tắc khoá trên WF-009 · dòng "Nâng cấp" trên WF-012 · WF-018 (khi người dùng mở app iPhone sau khi thấy dòng gợi ý trên xe)
**Exit Points**: WF-011 (chọn bậc) · màn hình trước đó (đóng)

**State Variations with Context**:

| State | Context | Layout/Behavior Difference |
|---|---|---|
| First Visit | Lần đầu chạm tính năng khoá (`days_since_install > 0`) | Zone A nói về **đúng tính năng vừa chạm**, không phải quảng cáo chung |
| Returning / Has Data | Đã xem paywall trước đó | Bậc Yearly được nhấn mạnh; không hiển thị lại cùng một nội dung Zone A |
| Power User | Đã dùng Free lâu, nhiều thiết bị | "Phục hồi giao dịch" và bậc Lifetime nổi bật hơn |
| Trial đã dùng | Từng dùng trial | Bậc giá **không** hiện ưu đãi trial; nêu rõ đây là mua trực tiếp |
| Error | StoreKit không trả về giá | Hiện trạng thái tải rồi báo lỗi rõ ràng kèm nút thử lại; **tuyệt đối không** hiện giá cache hay giá hardcode |

---

### 4.11 WF-011 — Xác Nhận Giá 📱

**Screen Archetype**: Action · **Interaction Density**: Light (2 vùng — cố ý tối giản)
**Source UCs**: UC-026 (chính), UC-027, UC-030

**User Intent**: "Tôi muốn thấy chính xác con số sẽ bị trừ và ngày bị trừ, trước khi tôi đồng ý."

**Primary Action**: Chạm "Xác nhận" để mở dialog thanh toán của Apple

**Secondary Actions by Layer**:
- **Layer 2 — Contextual**: Quay lại WF-010 để đổi bậc
- **Layer 3 — Discovery**: (trống có chủ ý — **màn hình này không được có gì để khám phá**; mọi thứ gây phân tán ở đây đều làm tăng nguy cơ người dùng bấm mà không đọc)
- **Layer 4 — Personal**: Xem điều khoản và chính sách hoàn tiền

**Content Zones**:
- **Zone A (Hero)**: Bậc đã chọn · **giá cuối bằng tiền tệ địa phương** · ngày hết trial · **ngày bị trừ tiền** · chu kỳ gia hạn
- **Zone B (Engagement)**: Nút "Xác nhận"
- **Zone C (Discovery)**: (trống có chủ ý)
- **Zone D (Utility)**: Nút quay lại, link điều khoản

**Entry Points**: chọn một bậc giá trên WF-010
**Exit Points**: dialog thanh toán iOS → màn hình trước paywall (thành công) · WF-010 (quay lại) · WF-030 (toast xác nhận sau khi mua)

**State Variations with Context**:

| State | Context | Layout/Behavior Difference |
|---|---|---|
| First Visit | Bậc có trial (Monthly/Yearly) | Hiện đủ 4 mốc: ngày bắt đầu trial · ngày hết trial · ngày trừ tiền · số tiền |
| Returning / Has Data | Bậc Lifetime | **Không** hiện ngày gia hạn; nêu rõ "một lần, không tự động gia hạn" — sự thiếu vắng thông tin gia hạn chính là thông điệp |
| Power User | Đổi vùng App Store giữa lúc mua | Giá được đọc lại từ StoreKit trước khi hiển thị; **không** dùng giá đã cache |
| Error | Thanh toán thất bại | Nêu nguyên nhân từ StoreKit kèm nút thử lại; **không** trả người dùng về WF-010 và không làm mất lựa chọn |

---

### 4.12 WF-012 — Cài Đặt Chung 📱

**Screen Archetype**: Management · **Interaction Density**: Dense (7 vùng)
**Source UCs**: UC-009 (chính), UC-004, UC-029, UC-031, UC-032, UC-033, UC-035

**User Intent**: "Tôi muốn tìm và điều chỉnh một thứ cụ thể mà tôi biết là có ở đâu đây."

**Primary Action**: Điều chỉnh âm lượng sound (mục được dùng nhiều nhất trong màn này)

**Secondary Actions by Layer**:
- **Layer 2 — Contextual**: Slider âm lượng sound · chọn theme · dòng "Ngôn ngữ" → WF-026
- **Layer 3 — Discovery**: Dòng "Quyền" → trạng thái từng quyền · dòng "Về Carbina" · dòng "Đánh giá Carbina"
- **Layer 4 — Personal**: Dòng "Đăng ký của tôi" (hiện trạng thái ngay trên dòng) → WF-025 · dòng "Quyền riêng tư & dữ liệu" → WF-029 · dòng "Tài khoản" → WF-015 *(MVP 3)*

**Content Zones**:
- **Zone A (Hero)**: Trạng thái gói hiện tại (Free / Trial còn N ngày / Premium / Lifetime)
- **Zone B (Engagement)**: Slider âm lượng sound kèm nút nghe thử
- **Zone C (Discovery)**: Nhóm dòng cài đặt: theme, ngôn ngữ, quyền, đánh giá, về app
- **Zone D (Utility)**: Nhóm dòng quản trị: đăng ký, quyền riêng tư & dữ liệu, tài khoản

**Entry Points**: Tab Settings · badge trạng thái gói trên WF-006
**Exit Points**: WF-025 · WF-026 · WF-029 · WF-010 · WF-015 · WF-028 · Cài đặt hệ thống iOS

**State Variations with Context**:

| State | Context | Layout/Behavior Difference |
|---|---|---|
| First Visit | Gói Free, vừa onboard | Zone A hiện "Gói Free" + dòng "Xem các gói" → WF-010; dòng Tài khoản **không** hiện (thuộc MVP 3) |
| Returning / Has Data | Premium hoặc trial đang chạy | Zone A hiện gói + ngày gia hạn; dòng "Đăng ký của tôi" hiện trạng thái ngay trên dòng |
| Power User | Lifetime | Zone A hiện "Đã mua vĩnh viễn"; dòng đăng ký **không** có nút huỷ gây bối rối |
| Chưa có dữ liệu học | Mới dùng | Mục "Quyền riêng tư & dữ liệu" nêu rõ "chưa có dữ liệu học nào" thay vì hiện nút xoá không có tác dụng |
| Error | Không đọc được trạng thái subscription | Zone A hiện trạng thái không xác định kèm nút "Phục hồi giao dịch"; các mục khác vẫn dùng được bình thường |

---

### 4.13 WF-013 — Nhắc Hết Trial 📱

**Screen Archetype**: Action · **Interaction Density**: Light (3 vùng)
**Source UCs**: UC-028 (chính), UC-027

**User Intent**: "Tôi muốn biết mình sắp bị trừ bao nhiêu và khi nào, để tôi kịp quyết định."

**Primary Action**: Chọn một trong ba: "Nhắc sau" · "Đăng ký" · "Huỷ trial"

**Secondary Actions by Layer**:
- **Layer 2 — Contextual**: Xem lại tính năng đang dùng nhờ trial
- **Layer 3 — Discovery**: (trống có chủ ý — đây là màn hình quyết định, không phải màn hình bán thêm)
- **Layer 4 — Personal**: Lối vào WF-025 để xem chi tiết đăng ký

**Content Zones**:
- **Zone A (Hero)**: Số ngày còn lại · **số tiền chính xác** · **ngày bị trừ tiền**
- **Zone B (Engagement)**: Ba nút **ngang hàng về mặt thị giác**: Nhắc sau · Đăng ký · Huỷ trial
- **Zone C (Discovery)**: (trống có chủ ý)
- **Zone D (Utility)**: Nút đóng

**Entry Points**: hệ thống kích hoạt vào ngày 6 và ngày 7 của trial
**Exit Points**: WF-006 (nhắc sau / đăng ký) · WF-027 → WF-025 (huỷ)

**State Variations with Context**:

| State | Context | Layout/Behavior Difference |
|---|---|---|
| First Visit | Ngày 6 của trial | Nêu "còn 1 ngày" + số tiền + ngày trừ; tông trung tính, **không** đếm ngược gây áp lực |
| Returning / Has Data | Ngày 7, đã chọn "Nhắc sau" một lần | Nêu rõ đây là lần nhắc cuối; nút "Nhắc sau" biến mất sau lần thứ hai |
| Power User | Muốn huỷ ngay | Nút "Huỷ trial" dẫn thẳng WF-027 rồi WF-025 — tối đa 3 chạm là huỷ được |
| Error | Không đọc được ngày hết trial từ StoreKit | Nêu rõ không xác định được ngày và dẫn sang trang subscription của iOS; **tuyệt đối không** đoán một con số |

---

### 4.14 WF-014 — Chẩn Đoán Tương Thích 📱

**Screen Archetype**: Management · **Interaction Density**: Medium (4 vùng)
**Source UCs**: UC-017 (chính), UC-013, UC-016

**User Intent**: "Tôi muốn biết chuyện gì đã xảy ra trên xe tôi, và làm gì để nó được sửa."

**Primary Action**: Xem dữ liệu kỹ thuật của các lần kết nối gần nhất và gửi báo cáo nếu có lỗi

**Secondary Actions by Layer**:
- **Layer 2 — Contextual**: Xem kích thước scene đã nhận · xem trạng thái render từng lần · chạm "Gửi báo cáo" → WF-028
- **Layer 3 — Discovery**: Xem widget của mình ở đúng kích thước xe đã ghi nhận (→ WF-023) · đọc giải thích vì sao lỗi có thể xảy ra
- **Layer 4 — Personal**: Sao chép dữ liệu chẩn đoán · xoá lịch sử chẩn đoán

**Content Zones**:
- **Zone A (Hero)**: Kích thước màn hình xe đã nhận được (giá trị thật, không suy đoán) + phiên bản iOS + xe đã chọn
- **Zone B (Engagement)**: Nút "Gửi báo cáo"
- **Zone C (Discovery)**: Danh sách các lần kết nối gần nhất kèm kết quả render và `failure_reason`
- **Zone D (Utility)**: Nút đóng, nút sao chép dữ liệu

**Entry Points**: dòng cảnh báo trên WF-006 · hướng dẫn từ WF-019 · lối vào chủ động từ WF-006
**Exit Points**: WF-028 · WF-023 · WF-006

**State Variations with Context**:

| State | Context | Layout/Behavior Difference |
|---|---|---|
| First Visit | Chưa từng kết nối CarPlay | Zone A hiện hướng dẫn cắm xe một lần; **không** hiện bảng trống |
| Returning / Has Data | Đã kết nối, mọi lần đều thành công | Zone C hiện danh sách toàn màu xanh; nút "Gửi báo cáo" vẫn có nhưng không nổi bật |
| Power User | QA hoặc người dùng gặp lỗi lặp lại | Zone C hiện đủ `failure_reason` phân biệt vượt-bounds với hết-bộ-nhớ; nút sao chép dữ liệu nổi bật |
| Error | Có lỗi render trong lần gần nhất | Zone A đánh dấu đỏ; nút "Gửi báo cáo" là CTA chính; kèm một câu nói rõ đây là vấn đề tương thích màn hình, **không phải lỗi của người dùng** |

---

### 4.15 WF-015 — Account 📱 *(MVP 3)*

**Screen Archetype**: Management · **Interaction Density**: Light (3 vùng)
**Source UCs**: UC-035

**User Intent**: "Tôi muốn cấu hình của mình có mặt trên thiết bị mới, nếu tôi chọn như vậy."

**Primary Action**: Đăng nhập bằng email và bật đồng bộ cấu hình

**Secondary Actions by Layer**:
- **Layer 2 — Contextual**: Đăng xuất · xem thời điểm đồng bộ gần nhất
- **Layer 3 — Discovery**: Đọc rõ **cái gì được đồng bộ và cái gì không** (dữ liệu học ngữ cảnh không rời thiết bị)
- **Layer 4 — Personal**: Xoá tài khoản và dữ liệu cloud

**Content Zones**:
- **Zone A (Hero)**: Trạng thái tài khoản và trạng thái đồng bộ
- **Zone B (Engagement)**: Nút đăng nhập, hoặc công tắc "Đồng bộ cấu hình"
- **Zone C (Discovery)**: Bảng hai cột: đồng bộ ↔ không đồng bộ
- **Zone D (Utility)**: Nút đóng, dòng xoá tài khoản

**Entry Points**: dòng "Tài khoản" trên WF-012 *(chỉ hiện ở MVP 3)*
**Exit Points**: WF-012

**State Variations with Context**:

| State | Context | Layout/Behavior Difference |
|---|---|---|
| First Visit | Chưa có tài khoản | Nêu rõ đây là **tuỳ chọn**; app hoạt động đầy đủ không cần tài khoản |
| Returning / Has Data | Đã đăng nhập, đồng bộ bật | Hiện thời điểm đồng bộ gần nhất và thiết bị đã liên kết |
| Power User | Hai thiết bị cấu hình khác nhau | Hiện lựa chọn giữ bản nào; **không** tự ghi đè |
| Error | Không kết nối được cloud | Nêu rõ đang dùng cấu hình cục bộ; mọi tính năng vẫn hoạt động vì cloud chỉ là lớp tiện ích |

---

### 4.16 WF-016 — CarPlay Dashboard 🚗

**Screen Archetype**: Discovery · **Interaction Density**: Medium (3–5 vùng — **giới hạn cứng, không được là Dense**)
**Source UCs**: UC-022 (chính), UC-005, UC-010, UC-011, UC-021, UC-023, UC-034

**User Intent**: "Tôi muốn nhìn một lượt là thấy thứ tôi cần, và chạm một lần là xong."

**Primary Action**: Chạm thẻ liên quan nhất để thực hiện việc đó ngay

**Secondary Actions by Layer**:
- **Layer 2 — Contextual**: Chạm một thẻ (nhạc / thời tiết / điểm đến gợi ý / shortcut)
- **Layer 3 — Discovery**: (trống có chủ ý — **không có "xem thêm" trên màn hình xe**; mọi thứ đòi người lái đi sâu hơn một tầng đều là rủi ro an toàn)
- **Layer 4 — Personal**: (trống có chủ ý — **không có cấu hình trên màn hình xe**; mọi cấu hình đều nằm trên iPhone)

**Content Zones**:
- **Zone A (Hero)**: Thẻ ưu tiên cao nhất theo ngữ cảnh, chiếm diện tích lớn nhất
- **Zone B (Engagement)**: Thẻ còn lại, mỗi thẻ chạm một lần là ra hành động
- **Zone C (Discovery)**: (trống có chủ ý)
- **Zone D (Utility)**: Một dòng trạng thái ở mép (gói hiện tại hoặc cảnh báo), **không chắn nội dung**

**Entry Points**: `carplay_connected` → scene active · quay lại từ app hệ thống (nhạc/Maps/điện thoại)
**Exit Points**: app hệ thống tương ứng · WF-019 (nếu widget lỗi) · kết thúc phiên khi tắt máy

**State Variations with Context**:

| State | Context | Layout/Behavior Difference |
|---|---|---|
| First Visit | Chưa đủ dữ liệu để cá nhân hóa | Thứ tự thẻ mặc định + **một dòng nói rõ dashboard sẽ tự đổi sau vài chuyến** — không giả vờ đã cá nhân hóa |
| Returning / Has Data | Đã học được thói quen | Thẻ hay dùng lên Zone A; thứ tự đổi theo giờ và tuyến đường |
| Power User | Premium, dùng hằng ngày | Đủ thẻ, đủ shortcut; ngữ cảnh chính xác nhất — đây là trạng thái mà tap-through ≥ 30% được đo |
| Free tier | Gói Free | Dashboard cơ bản: nhạc đang phát, thời tiết, 1 shortcut (đúng cấu hình Free đã chốt) + WF-018 |
| Offline | Mất mạng | Thẻ nhạc và thời tiết dùng cache và **ghi rõ thời điểm cập nhật**; thẻ shortcut vẫn hoạt động |
| Error | Một thẻ không lấy được dữ liệu | Thẻ đó hiện thông báo gọn ngay trên thẻ kèm hành động thay thế; **không modal**, các thẻ khác không bị ảnh hưởng |

---

### 4.17 WF-017 — CarPlay Widget 🚗

**Screen Archetype**: Consumption · **Interaction Density**: Light (1–2 vùng)
**Source UCs**: UC-015 (chính), UC-005, UC-010

**User Intent**: "Tôi muốn thấy widget của tôi, đúng như tôi đã cấu hình, không bị cắt."

**Primary Action**: Không có hành động — đây là bề mặt để **nhìn**, và đó là chủ ý

**Secondary Actions by Layer**:
- **Layer 2 — Contextual**: (trống có chủ ý ở MVP 1 — widget tương tác hai chiều thuộc MVP 2)
- **Layer 3 — Discovery**: (trống có chủ ý)
- **Layer 4 — Personal**: (trống có chủ ý — cấu hình nằm ở WF-008 trên iPhone)

**Content Zones**:
- **Zone A (Hero)**: Ảnh xe hoặc ảnh cá nhân, chiếm gần toàn bộ diện tích
- **Zone B (Engagement)**: Lớp thông tin (counter, chữ) — co giãn theo Dynamic Type, truncate có ellipsis
- **Zone C (Discovery)**: (trống có chủ ý)
- **Zone D (Utility)**: (trống — widget không có chrome)

**Entry Points**: `carplay_connected` → scene active, widget được hệ thống yêu cầu vẽ
**Exit Points**: WF-016 (dashboard) · WF-019 (nếu render thất bại)

**State Variations with Context**:

| State | Context | Layout/Behavior Difference |
|---|---|---|
| First Visit | Lần cắm xe đầu tiên | Render bằng bounds vừa đọc được; kích thước được lưu lại để WF-023 dùng về sau |
| Returning / Has Data | Kích thước xe đã biết | Đường render ngắn hơn vì layout đã có tham số; kết quả giống hệt lần trước |
| Power User | Widget dùng ảnh cá nhân, nhiều lớp thông tin | Khi hết chỗ, hệ thống **giảm cấp layout** theo thứ tự ưu tiên đã định thay vì cắt bừa |
| Dark / Light mode | Theo hệ thống xe | Cả hai mode đều được hỗ trợ; độ tương phản chữ trên ảnh phải đạt ngưỡng đọc được ở cả hai |
| Error | Vượt bounds hoặc hết bộ nhớ | Chuyển WF-019 và ghi `widget_render_failed` với `failure_reason` **phân biệt được hai nguyên nhân này** |

---

### 4.18 WF-018 — CarPlay: Trạng Thái Free 🚗

**Screen Archetype**: Consumption · **Interaction Density**: Light (2 vùng)
**Source UCs**: UC-024 (chính), UC-021, UC-022, UC-023

**User Intent**: "Tôi muốn dùng cái tôi đang có mà không bị quấy rầy trong lúc lái."

**Primary Action**: Không có hành động bắt buộc — người dùng tiếp tục dùng widget và dashboard Free

**Secondary Actions by Layer**:
- **Layer 2 — Contextual**: Đọc dòng gợi ý nâng cấp — **chỉ đọc, không chạm được để mở paywall**
- **Layer 3 — Discovery**: (trống có chủ ý)
- **Layer 4 — Personal**: (trống có chủ ý)

**Content Zones**:
- **Zone A (Hero)**: Widget và dashboard Free đang hoạt động bình thường
- **Zone B (Engagement)**: **Một dòng chữ tĩnh** nói tính năng nào có ở Premium
- **Zone C (Discovery)**: (trống có chủ ý)
- **Zone D (Utility)**: (trống)

**Entry Points**: scene active khi entitlement là Free
**Exit Points**: WF-016 · kết thúc phiên. **Không có exit nào dẫn tới paywall từ màn hình xe**

**State Variations with Context**:

| State | Context | Layout/Behavior Difference |
|---|---|---|
| First Visit | Lần đầu lên xe với gói Free | Dòng gợi ý xuất hiện một lần, ngắn, nằm ở mép — mục đích là **thông tin**, không phải chuyển đổi |
| Returning / Has Data | Đã dùng Free nhiều chuyến | Dòng gợi ý **không** hiện lại mỗi chuyến; tối đa theo tần suất đã định, không theo phiên |
| Power User | Dùng Free lâu dài có ý thức | Trải nghiệm gần như không có dấu hiệu của trạng thái Free — đây là chủ ý, không phải thiếu sót |
| Error | Không đọc được entitlement | Mặc định về mức Free và **vẫn cho dùng**; không chặn, không hiện lỗi trên màn hình xe |

---

### 4.19 WF-019 — CarPlay: Fallback Lỗi 🚗

**Screen Archetype**: Consumption · **Interaction Density**: Light (1 vùng)
**Source UCs**: UC-016 (chính), UC-015

**User Intent**: "Có gì đó không ổn — tôi muốn biết đó là gì và nó có phải lỗi của tôi không."

**Primary Action**: Không có hành động trên xe — người dùng chỉ đọc; hành động diễn ra sau, trên iPhone

**Secondary Actions by Layer**:
- **Layer 2 — Contextual**: (trống có chủ ý — **người dùng đang lái**)
- **Layer 3 — Discovery**: (trống có chủ ý)
- **Layer 4 — Personal**: (trống có chủ ý)

**Content Zones**:
- **Zone A (Hero)**: Một thông báo gọn: đây là vấn đề tương thích với màn hình xe này, kèm hướng dẫn mở màn Chẩn Đoán trên iPhone
- **Zone B (Engagement)**: (trống — không có CTA nào trên bề mặt đang lái)
- **Zone C (Discovery)**: (trống)
- **Zone D (Utility)**: (trống)

**Entry Points**: render thất bại trong UC-015 (vượt bounds hoặc hết bộ nhớ)
**Exit Points**: WF-016 (dashboard vẫn hoạt động nếu chỉ widget lỗi) · WF-014 (khi người dùng mở app iPhone sau đó)

**State Variations with Context**:

| State | Context | Layout/Behavior Difference |
|---|---|---|
| First Visit | Lỗi ở lần cắm xe đầu tiên | Thông báo phải nói rõ **vấn đề nằm ở tương thích màn hình**, không dùng câu chung như "đã xảy ra lỗi" — đây là khoảnh khắc quyết định người dùng ở lại hay để 1★ |
| Returning / Has Data | Lỗi lẻ một lần rồi hết | Lần cắm kế tiếp render bình thường; mọi cảnh báo trên WF-006 tự xoá |
| Power User | Lỗi lặp lại ≥ 3 lần cùng một kích thước | Telemetry đánh dấu ưu tiên cao để phát hiện xe không tương thích trong 24h |
| Error (lỗi bộ phận) | Chỉ widget lỗi, dashboard vẫn được | **Chỉ vùng widget** bị thay bằng thông báo; WF-016 vẫn hoạt động đầy đủ — không hạ toàn bộ bề mặt CarPlay |

---

### 4.20 WF-020 — Sheet: Nghe Thử Âm Thanh 📱

**Screen Archetype**: Consumption · **Interaction Density**: Medium (4 vùng)
**Source UCs**: UC-006 (chính), UC-007, UC-009, UC-010

**User Intent**: "Tôi muốn nghe kỹ preset này đúng như nó sẽ nghe trên xe, rồi quyết định."

**Primary Action**: Nghe preset ở mức âm lượng thật và chạm "Dùng sound này"

**Secondary Actions by Layer**:
- **Layer 2 — Contextual**: Phát lại · slider âm lượng có phản hồi tức thì · chọn sự kiện áp dụng (Connect/Disconnect/Arrive)
- **Layer 3 — Discovery**: Chuyển sang preset kế tiếp/trước trong cùng nhóm mà không đóng sheet
- **Layer 4 — Personal**: (trống có chủ ý — sheet này chỉ có một việc; thêm mục cá nhân hoá ở đây sẽ biến nó thành một màn hình cấu hình thứ hai)

**Content Zones**:
- **Zone A (Hero)**: Tên preset + dạng sóng + trạng thái đang phát
- **Zone B (Engagement)**: Nút "Dùng sound này" (hoặc "Mở khoá" nếu preset khoá)
- **Zone C (Discovery)**: Điều hướng preset trước/sau
- **Zone D (Utility)**: Slider âm lượng, bộ chọn sự kiện, nút đóng

**Entry Points**: chạm một preset trên WF-007 · chạm "nghe kỹ" từ WF-004
**Exit Points**: WF-007 (đã gán hoặc đóng) · WF-010 (preset khoá) · WF-030 (toast xác nhận)

**State Variations with Context**:

| State | Context | Layout/Behavior Difference |
|---|---|---|
| First Visit | Lần đầu mở sheet | Sound tự phát một lần ngay khi sheet mở, để người dùng không phải tìm nút play |
| Returning / Has Data | Preset đang dùng | Nút chính hiện "Đang dùng" ở trạng thái đã chọn thay vì "Dùng sound này" |
| Power User | Đang phát nhạc từ app khác | Áp dụng ducking thật, để bản nghe thử phản ánh đúng trải nghiệm trên xe |
| Free tier | Preset khoá | Nghe **đầy đủ**, không cắt, không watermark; chỉ nút chính đổi thành "Mở khoá" |
| Error | Không phát được | Nêu lý do cụ thể kèm nút thử lại; sheet không tự đóng để người dùng không mất ngữ cảnh |

---

### 4.21 WF-021 — Sheet: Không tìm thấy xe của tôi 📱

**Screen Archetype**: Action · **Interaction Density**: Light (3 vùng)
**Source UCs**: UC-003 (chính), UC-002

**User Intent**: "Xe tôi không có trong danh sách — tôi muốn nói ra và vẫn đi tiếp được."

**Primary Action**: Điền hãng/model/năm và chạm "Gửi"

**Secondary Actions by Layer**:
- **Layer 2 — Contextual**: Sửa ba ô (điền sẵn phần đã gõ ở WF-003) · đóng sheet
- **Layer 3 — Discovery**: Chọn phân khúc xe (sedan/SUV/pickup) để vẫn có ảnh dùng được
- **Layer 4 — Personal**: (trống có chủ ý — không thu thập gì thêm về người dùng ở đây, đúng cam kết không PII)

**Content Zones**:
- **Zone A (Hero)**: Một câu trung thực: thư viện chưa có xe này, và điều đó không chặn bạn
- **Zone B (Engagement)**: Nút "Gửi"
- **Zone C (Discovery)**: Bộ chọn phân khúc xe
- **Zone D (Utility)**: Ba ô nhập, nút đóng

**Entry Points**: nút "Không tìm thấy xe của tôi" ở cuối danh sách trên WF-003
**Exit Points**: WF-003 (tiếp tục luồng chọn xe) · WF-030 (toast xác nhận)

**State Variations with Context**:

| State | Context | Layout/Behavior Difference |
|---|---|---|
| First Visit | Trong onboarding | Sheet ngắn, ba ô, không bắt buộc mô tả thêm — không làm onboarding dài ra |
| Returning / Has Data | Đã gửi request trước đó cho cùng hãng | Nêu rõ đã gửi rồi và không gửi trùng |
| Power User | Xe nội địa hoặc xe rất mới | Chấp nhận tên tự do; không validate cứng theo danh sách có sẵn |
| Error / Offline | Không có mạng | Request xếp hàng on-device; toast vẫn xác nhận đã ghi nhận — người dùng không cần biết chuyện mạng |

---

### 4.22 WF-022 — Sheet: Lý Do Xin Quyền 📱

**Screen Archetype**: Consumption · **Interaction Density**: Light (3 vùng)
**Source UCs**: UC-004 (chính), UC-019

**User Intent**: "Tôi muốn hiểu app dùng quyền này để làm chính xác điều gì trước khi tôi đồng ý."

**Primary Action**: Đọc lý do rồi chạm "Cho phép" (mở dialog quyền của iOS) hoặc "Không, cảm ơn"

**Secondary Actions by Layer**:
- **Layer 2 — Contextual**: Đóng sheet mà không quyết định (quay về WF-005 giữ nguyên trạng thái)
- **Layer 3 — Discovery**: Xem ví dụ cụ thể app làm được gì khi có quyền này, và mất gì khi không có
- **Layer 4 — Personal**: Xem chính sách quyền riêng tư

**Content Zones**:
- **Zone A (Hero)**: Một câu nói app dùng quyền này để làm gì + cam kết dữ liệu không rời thiết bị
- **Zone B (Engagement)**: Hai nút: "Cho phép" · "Không, cảm ơn" — **ngang hàng, không làm mờ nút từ chối**
- **Zone C (Discovery)**: Hai ví dụ: có quyền thì được gì, không có quyền thì mất gì
- **Zone D (Utility)**: Nút đóng, link chính sách quyền riêng tư

**Entry Points**: "Tìm hiểu thêm" trên WF-005 · dòng "cần quyền" trên WF-009
**Exit Points**: WF-005 hoặc WF-009 (trở về nơi vào), có kèm dialog quyền iOS nếu chọn "Cho phép"

**State Variations with Context**:

| State | Context | Layout/Behavior Difference |
|---|---|---|
| First Visit (biến thể Location) | Chưa hỏi quyền Vị trí | Ví dụ nói về học tuyến đường quen và gợi ý điểm đến |
| First Visit (biến thể Calendar) | Chưa hỏi quyền Lịch | Ví dụ nói về câu chào theo cuộc họp sắp tới |
| Returning / Has Data | Quyền đã bị từ chối trước đó | Nút "Cho phép" chuyển thành "Mở Cài đặt" — vì iOS không cho hỏi lại lần hai |
| Error | Dialog quyền không mở được | Nêu rõ và dẫn sang Cài đặt hệ thống; không để nút bấm không phản hồi |

---

### 4.23 WF-023 — Modal: Preview Widget Theo Màn Hình Xe 📱

**Screen Archetype**: Consumption · **Interaction Density**: Medium (4 vùng)
**Source UCs**: UC-013 (chính), UC-012, UC-014

**User Intent**: "Tôi muốn thấy widget của tôi trên đúng màn hình xe của tôi trước khi ra xe."

**Primary Action**: Xem widget ở từng tỉ lệ và chạm "Dùng bản này"

**Secondary Actions by Layer**:
- **Layer 2 — Contextual**: Vuốt ngang qua các tỉ lệ · bật/tắt lớp thông tin để xem widget gọn hơn
- **Layer 3 — Discovery**: Xem cảnh báo phần tử vượt vùng an toàn ở từng tỉ lệ · chuyển giữa dark/light mode
- **Layer 4 — Personal**: Đổi loại widget hoặc đổi ảnh **ngay tại đây** (→ WF-024) — sửa tại nơi phát hiện vấn đề

**Content Zones**:
- **Zone A (Hero)**: Widget render trong khung đúng tỉ lệ màn hình xe
- **Zone B (Engagement)**: Nút "Dùng bản này"
- **Zone C (Discovery)**: Dải chọn tỉ lệ + cảnh báo vượt vùng an toàn (nếu có)
- **Zone D (Utility)**: Công tắc dark/light, nút đóng, nhãn nói rõ tỉ lệ này là thật hay ước lượng

**Entry Points**: nút "Xem trước trên xe của tôi" trên WF-008 · lối vào từ WF-014 (xem widget ở kích thước đã ghi nhận)
**Exit Points**: WF-008 · WF-024

**State Variations with Context**:

| State | Context | Layout/Behavior Difference |
|---|---|---|
| First Visit | Chưa từng cắm xe | Dùng ≥ 4 tỉ lệ tham chiếu và **nói rõ đây là ước lượng** — không tuyên bố chính xác khi chưa có dữ liệu |
| Returning / Has Data | Đã cắm xe ít nhất một lần | Tỉ lệ mặc định là **kích thước thật của xe người dùng**; nhãn ở Zone D nói rõ đây là số thật |
| Power User | Có hai xe khác kích thước | Cho chọn giữa các kích thước đã từng gặp; kiểm được cả hai trước khi lưu |
| Error | Có phần tử vượt vùng an toàn | Chỉ rõ **phần tử nào** vượt và đề xuất giảm bớt; **không** tự âm thầm cắt nội dung |

---

### 4.24 WF-024 — Sheet: Chọn Ảnh Cho Widget 📱

**Screen Archetype**: Action · **Interaction Density**: Medium (4 vùng)
**Source UCs**: UC-014

**User Intent**: "Tôi muốn đặt ảnh xe của tôi lên widget và biết trước phần nào sẽ bị cắt."

**Primary Action**: Chọn ảnh, điều chỉnh khung crop, chạm "Xong"

**Secondary Actions by Layer**:
- **Layer 2 — Contextual**: Kéo/zoom khung crop · đổi nguồn ảnh · xoay ảnh
- **Layer 3 — Discovery**: Duyệt bộ ảnh xe theo model đã chọn (không cần quyền thư viện ảnh)
- **Layer 4 — Personal**: Mở thư viện ảnh cá nhân (cần quyền) · gỡ ảnh hiện tại

**Content Zones**:
- **Zone A (Hero)**: Ảnh với khung crop theo đúng tỉ lệ màn hình xe, vùng sẽ bị cắt được làm tối rõ ràng
- **Zone B (Engagement)**: Nút "Xong"
- **Zone C (Discovery)**: Hàng ảnh xe theo model, cuộn ngang
- **Zone D (Utility)**: Bộ chọn nguồn ảnh, nút đóng, cảnh báo độ phân giải (nếu có)

**Entry Points**: ô ảnh trên WF-008 · nút đổi ảnh trong WF-023
**Exit Points**: WF-008 · WF-023 · WF-010 (nếu ảnh cá nhân thuộc Premium)

**State Variations with Context**:

| State | Context | Layout/Behavior Difference |
|---|---|---|
| First Visit | Chưa chọn ảnh | Mặc định là ảnh xe theo model — có kết quả tốt mà không phải chọn gì |
| Returning / Has Data | Đã có ảnh | Ảnh hiện tại nạp sẵn kèm khung crop cũ; chỉnh tiếp được, không phải làm lại |
| Power User | Ảnh cá nhân tỉ lệ lạ | Tự đề xuất khung crop tốt nhất; vùng cắt hiện rõ trước khi lưu |
| Free tier | Ảnh cá nhân thuộc Premium | Chọn và crop được để xem trước; nút "Xong" chuyển thành "Mở khoá" |
| Error | Ảnh độ phân giải thấp | Cảnh báo ảnh sẽ mờ trên màn hình xe và đề nghị chọn ảnh khác — **vẫn cho phép** nếu người dùng khăng khăng, nhưng đã được báo trước |

---

### 4.25 WF-025 — Sheet: Quản Lý Đăng Ký 📱

**Screen Archetype**: Management · **Interaction Density**: Medium (4 vùng)
**Source UCs**: UC-029 (chính), UC-027, UC-028, UC-030

**User Intent**: "Tôi muốn biết tôi đang trả cho cái gì và huỷ được nếu tôi muốn."

**Primary Action**: Xem trạng thái đăng ký hiện tại và huỷ nếu muốn

**Secondary Actions by Layer**:
- **Layer 2 — Contextual**: "Huỷ đăng ký" → WF-027 · xem ngày gia hạn kế tiếp
- **Layer 3 — Discovery**: Xem tính năng đang có nhờ gói hiện tại · xem các bậc khác (→ WF-010)
- **Layer 4 — Personal**: "Phục hồi giao dịch" · xem lịch sử giao dịch qua hệ thống iOS

**Content Zones**:
- **Zone A (Hero)**: Gói hiện tại · giá · ngày gia hạn kế tiếp (hoặc "đã mua vĩnh viễn")
- **Zone B (Engagement)**: Nút "Huỷ đăng ký" — **không ẩn, không làm mờ**
- **Zone C (Discovery)**: Danh sách tính năng đang có
- **Zone D (Utility)**: "Phục hồi giao dịch", nút đóng, link tới trang subscription của iOS

**Entry Points**: dòng "Đăng ký của tôi" trên WF-012 · nút "Huỷ trial" trên WF-013
**Exit Points**: WF-027 (xác nhận huỷ) · WF-012 · WF-010 · trang subscription của iOS

**State Variations with Context**:

| State | Context | Layout/Behavior Difference |
|---|---|---|
| First Visit | Gói Free | Zone A hiện "Gói Free"; không có gì để huỷ; Zone C hiện tính năng đang có ở Free và lối vào WF-010 |
| Returning / Has Data | Subscription đang chạy | Đủ giá + ngày gia hạn; nút huỷ ở Zone B, đường huỷ **tối đa 3 chạm** kể từ WF-012 |
| Trial đang chạy | Ngày 1–7 | Nêu rõ ngày hết trial và ngày trừ tiền; nút huỷ nhấn mạnh hơn nút xem gói khác |
| Power User | Lifetime | Zone A hiện "đã mua vĩnh viễn"; **không** hiện nút huỷ; nếu còn subscription cũ thì nhắc huỷ để không trả trùng |
| Error | Không đọc được trạng thái từ StoreKit | Nêu rõ chưa xác định được kèm nút "Phục hồi giao dịch"; nếu không có giao dịch nào thì **nói rõ điều đó** thay vì báo lỗi chung |

---

### 4.26 WF-026 — Sheet: Chọn Ngôn Ngữ 📱

**Screen Archetype**: Action · **Interaction Density**: Light (2 vùng)
**Source UCs**: UC-031

**User Intent**: "Tôi muốn dùng app bằng tiếng của tôi, kể cả phần giọng nói."

**Primary Action**: Chọn một ngôn ngữ trong danh sách

**Secondary Actions by Layer**:
- **Layer 2 — Contextual**: Chọn "Theo hệ thống" · đóng sheet
- **Layer 3 — Discovery**: Xem ngôn ngữ nào sẽ có ở MVP 2 (DE/FR/IT) — nêu rõ là chưa có, **không** hiện lựa chọn không hoạt động
- **Layer 4 — Personal**: (trống có chủ ý — ngôn ngữ giọng chào theo ngôn ngữ app, không tách thành lựa chọn thứ hai ở MVP 1)

**Content Zones**:
- **Zone A (Hero)**: Danh sách 3 ngôn ngữ + "Theo hệ thống", ngôn ngữ hiện tại được đánh dấu
- **Zone B (Engagement)**: Chọn là áp dụng ngay — không có nút "Lưu"
- **Zone C (Discovery)**: Ghi chú về các ngôn ngữ sẽ có ở MVP 2
- **Zone D (Utility)**: Nút đóng

**Entry Points**: dòng "Ngôn ngữ" trên WF-012
**Exit Points**: WF-012

**State Variations with Context**:

| State | Context | Layout/Behavior Difference |
|---|---|---|
| First Visit | Chưa từng đổi | "Theo hệ thống" được chọn; nếu ngôn ngữ hệ thống không thuộc 3 ngôn ngữ hỗ trợ thì nêu rõ đang dùng English |
| Returning / Has Data | Đã chọn thủ công | Ngôn ngữ đã chọn được đánh dấu; đổi lại áp dụng ngay không cần khởi động lại app |
| Power User | Đang cắm CarPlay khi đổi | UI CarPlay cập nhật ở lần vẽ kế tiếp; **câu chào đang phát không bị cắt giữa câu** |
| Error | Thiếu bản dịch cho một chuỗi | Rơi về English cho đúng chuỗi đó thay vì hiện khoá dịch thô hay ô trống |

---

### 4.27 WF-027 — Alert: Xác Nhận Huỷ Trial 📱

**Screen Archetype**: Action · **Interaction Density**: Light (1 vùng)
**Source UCs**: UC-029 (chính), UC-028

**User Intent**: "Tôi muốn chắc chắn mình hiểu hậu quả trước khi huỷ."

**Primary Action**: Xác nhận huỷ (hoặc quay lại)

**Secondary Actions by Layer**:
- **Layer 2 — Contextual**: "Giữ đăng ký" — quay lại không làm gì
- **Layer 3 — Discovery**: (trống có chủ ý — alert phải chỉ có một câu hỏi; mọi thứ thêm vào đều là dark pattern níu giữ)
- **Layer 4 — Personal**: (trống có chủ ý)

**Content Zones**:
- **Zone A (Hero)**: Một câu nêu rõ **quyền Premium còn dùng tới ngày nào** và cấu hình đã tạo **sẽ được giữ**
- **Zone B (Engagement)**: Hai nút: "Huỷ đăng ký" · "Giữ đăng ký"
- **Zone C (Discovery)**: (trống có chủ ý)
- **Zone D (Utility)**: (trống)

**Entry Points**: nút "Huỷ đăng ký" trên WF-025 · nút "Huỷ trial" trên WF-013
**Exit Points**: trang quản lý subscription của iOS (nếu xác nhận) · WF-025 (nếu giữ)

**State Variations with Context**:

| State | Context | Layout/Behavior Difference |
|---|---|---|
| First Visit | Huỷ trong trial | Nêu rõ vẫn dùng Premium tới hết ngày 7, sau đó về gói Free |
| Returning / Has Data | Huỷ subscription đang trả phí | Nêu rõ ngày kết thúc chu kỳ đã trả tiền |
| Power User | Có cả Lifetime và subscription | Nêu rõ Lifetime đã bao trùm nên huỷ subscription **không** làm mất quyền gì |
| Error | Không mở được trang subscription của iOS | Nêu rõ và hướng dẫn đường đi thủ công trong Cài đặt hệ thống |

---

### 4.28 WF-028 — Sheet: Gửi Báo Cáo Tương Thích 📱

**Screen Archetype**: Action · **Interaction Density**: Medium (4 vùng)
**Source UCs**: UC-017 (chính), UC-033

**User Intent**: "Tôi muốn gửi vấn đề của mình đi, và muốn biết chính xác dữ liệu gì rời khỏi máy tôi."

**Primary Action**: Xem danh sách dữ liệu sẽ gửi và chạm "Gửi"

**Secondary Actions by Layer**:
- **Layer 2 — Contextual**: Thêm ghi chú (tuỳ chọn, tối đa 500 ký tự) · bỏ tick một mục dữ liệu không muốn gửi
- **Layer 3 — Discovery**: Mở rộng để xem giá trị thật của từng mục dữ liệu
- **Layer 4 — Personal**: Sao chép toàn bộ nội dung báo cáo để tự gửi qua kênh khác

**Content Zones**:
- **Zone A (Hero)**: Danh sách **từng mục** dữ liệu sẽ gửi (kích thước màn hình, phiên bản iOS, xe đã chọn, `failure_reason`) — kèm cam kết không có PII
- **Zone B (Engagement)**: Nút "Gửi"
- **Zone C (Discovery)**: Ô ghi chú tuỳ chọn
- **Zone D (Utility)**: Nút đóng, nút sao chép

**Entry Points**: nút "Gửi báo cáo" trên WF-014 · nhánh "không hài lòng" từ WF-030
**Exit Points**: WF-014 hoặc WF-012 (tuỳ nơi vào) · WF-030 (toast xác nhận)

**State Variations with Context**:

| State | Context | Layout/Behavior Difference |
|---|---|---|
| First Visit | Vào từ WF-014 sau khi có lỗi render | Zone A đã điền sẵn đủ dữ liệu chẩn đoán; người dùng chỉ cần chạm "Gửi" |
| Returning / Has Data | Vào từ nhánh "không hài lòng" của WF-030 | Zone C được nhấn mạnh hơn — ở ngữ cảnh này điều quan trọng là **lời của người dùng**, không phải số liệu |
| Power User | QA gửi báo cáo có chủ đích | Có nút sao chép toàn bộ payload; mở rộng được để xem giá trị thật từng trường |
| Error / Offline | Không có mạng | Báo cáo xếp hàng on-device và gửi khi có mạng; xác nhận hiện trong ≤ 500ms, không chờ mạng |

---

### 4.29 WF-029 — Alert: Xoá Dữ Liệu On-Device 📱

**Screen Archetype**: Action · **Interaction Density**: Light (1 vùng)
**Source UCs**: UC-032

**User Intent**: "Tôi muốn xoá thứ app đã học về tôi, và muốn chắc mình không xoá luôn cấu hình đã dựng."

**Primary Action**: Xác nhận xoá dữ liệu học

**Secondary Actions by Layer**:
- **Layer 2 — Contextual**: "Huỷ" — không xoá gì
- **Layer 3 — Discovery**: (trống có chủ ý — alert cho hành động phá hủy chỉ được có một câu hỏi)
- **Layer 4 — Personal**: Lựa chọn thứ hai "Xoá cả cấu hình" — **tách rõ** khỏi lựa chọn thứ nhất để không xoá nhầm

**Content Zones**:
- **Zone A (Hero)**: Nêu rõ **cái gì sẽ mất** (dữ liệu học ngữ cảnh) và **cái gì được giữ** (widget, sound, entitlement)
- **Zone B (Engagement)**: Nút "Xoá dữ liệu học" · nút "Huỷ"
- **Zone C (Discovery)**: (trống có chủ ý)
- **Zone D (Utility)**: Dòng "Xoá cả cấu hình" — tách riêng, cần một xác nhận nữa

**Entry Points**: nút xoá trong mục "Quyền riêng tư & dữ liệu" trên WF-012
**Exit Points**: WF-012 · WF-030 (toast xác nhận)

**State Variations with Context**:

| State | Context | Layout/Behavior Difference |
|---|---|---|
| First Visit | Chưa có dữ liệu học | Nêu rõ "chưa có dữ liệu học nào"; nút xoá bị vô hiệu thay vì xoá một thứ không tồn tại |
| Returning / Has Data | Đã dùng vài tuần | Nêu số ngày dữ liệu sẽ mất, để người dùng biết cái giá của thao tác này |
| Power User | Bán xe / đổi xe, muốn xoá sạch | Dùng lựa chọn "Xoá cả cấu hình" ở Zone D, có xác nhận thứ hai |
| Error | Xoá thất bại một phần | Nêu rõ phần nào chưa xoá được kèm nút thử lại; **không** báo "đã xoá xong" khi chưa xong |

---

### 4.30 WF-030 — Overlay: Toast Xác Nhận 📱

**Screen Archetype**: Consumption · **Interaction Density**: Light (1–2 vùng)
**Source UCs**: UC-033 (chính), UC-003, UC-007, UC-012, UC-017, UC-026, UC-032

**User Intent**: "Tôi muốn biết việc tôi vừa làm đã xong, mà không bị chặn lại."

**Primary Action**: Không có hành động bắt buộc — overlay tự biến mất

**Secondary Actions by Layer**:
- **Layer 2 — Contextual**: Chạm để đóng ngay · "Hoàn tác" (chỉ ở biến thể có thể hoàn tác)
- **Layer 3 — Discovery**: (trống có chủ ý ở biến thể xác nhận)
- **Layer 4 — Personal**: Ở **biến thể mời đánh giá**: chọn mức hài lòng, dẫn tới App Store (hài lòng) hoặc WF-028 (không hài lòng)

**Content Zones**:
- **Zone A (Hero)**: Một dòng nói việc gì đã xong
- **Zone B (Engagement)**: (trống ở biến thể xác nhận) · bộ chọn mức hài lòng ở biến thể mời đánh giá
- **Zone C (Discovery)**: (trống có chủ ý)
- **Zone D (Utility)**: Nút đóng (một chạm)

**Entry Points**: hoàn tất một tác vụ ở WF-003 / WF-007 / WF-008 / WF-011 / WF-021 / WF-028 / WF-029 · hệ thống kích hoạt biến thể mời đánh giá sau khoảnh khắc tích cực
**Exit Points**: tự đóng sau 2s (biến thể xác nhận) · App Store (hài lòng) · WF-028 (không hài lòng)

**State Variations with Context**:

| State | Context | Layout/Behavior Difference |
|---|---|---|
| First Visit (biến thể xác nhận) | Vừa lưu một thay đổi | Một dòng, tự đóng sau 2s, **không chặn** tác vụ đang làm |
| Returning (biến thể mời đánh giá) | Sound đã phát thành công ≥ 5 lần, không có lỗi render | Hiện bộ chọn mức hài lòng; đóng được bằng một chạm; không hiện lại trong ≥ 30 ngày nếu bị đóng |
| Power User | Thực hiện nhiều tác vụ liên tiếp | Toast mới thay toast cũ, không xếp chồng nhiều toast |
| Bị chặn có chủ ý | Có `widget_render_failed` trong 7 ngày gần nhất | **Không** hiện biến thể mời đánh giá — mời đánh giá ngay sau khi app vừa lỗi là cách nhanh nhất để có 1★ |
| Error | Tác vụ thất bại | Toast hiện trạng thái thất bại kèm lý do và tồn lâu hơn (4s) để người dùng đọc kịp; có nút thử lại nếu áp dụng được |

---

## 5. Task Flows

13 task flow dưới đây phủ toàn bộ 22 UC ưu tiên High. Mỗi bước tham chiếu một **WF-XXX** và một **UC-XXX**; mỗi điểm quyết định có đường phục hồi.

> **Lưu ý về hai bề mặt**: các flow có bước 🚗 mô tả những gì xảy ra khi người dùng **đang lái**. Ở những bước đó, "User Action" thường là *không làm gì* — và đó là thiết kế đúng, không phải mô tả thiếu.

### 5.1 TF-001: Thiết lập lần đầu từ lúc cài app 📱

**Trigger**: người dùng cài app và mở lần đầu
**Referenced UCs**: UC-001, UC-002, UC-003, UC-004, UC-006, UC-007
**Referenced Screens**: WF-001, WF-002, WF-003, WF-021, WF-004, WF-005, WF-022, WF-006

| Step | Screen | User Action | System Response | Decision Point |
|---|---|---|---|---|
| 1 | WF-001 | Mở app | Kiểm tra cấu hình on-device; hiện logo ≤ 1,5s | Đã onboard? → WF-006 / Chưa → WF-002 |
| 2 | WF-002 | Đọc một câu giới thiệu, chạm "Bắt đầu" | Chuyển WF-003, tiến trình 2/4 (UC-001) | Phát hiện giao dịch cũ? → hiện "Phục hồi giao dịch" |
| 3 | WF-003 | Chọn hãng → model → năm | Hiện ảnh xe để đối chiếu (UC-002) | Không tìm thấy xe? → Bước 3a |
| 3a | WF-021 | Điền hãng/model/năm, chạm "Gửi" | Ghi nhận request, WF-030 toast, quay lại WF-003 (UC-003) | Không có mạng? → xếp hàng on-device |
| 4 | WF-003 | Chạm "Đúng xe của tôi" | Lưu xe, chuyển WF-004, tiến trình 3/4 | — |
| 5 | WF-004 | Nghe thử preset, chạm "Dùng sound này" | Gán sound Connect, chuyển WF-005 (UC-006, UC-007) | Chọn preset khoá? → nghe được đầy đủ, nút chuyển thành "Mở khoá" nhưng **không** mở paywall trong onboarding |
| 6 | WF-005 | Đọc lý do từng quyền | Hiện 2 thẻ quyền kèm lý do và ví dụ (UC-004) | Muốn hiểu sâu? → Bước 6a · Bỏ qua hết? → Bước 7 |
| 6a | WF-022 | Chạm "Cho phép" | Gọi dialog quyền iOS, cập nhật trạng thái thẻ | Bị từ chối? → nêu tính năng bị ảnh hưởng, **không** hỏi lại |
| 7 | WF-005 | Chạm "Tiếp tục" | Ghi `onboarding_completed`, chuyển WF-006 | — |
| 8 | WF-006 | Xem trạng thái | Hiện "Chưa kết nối CarPlay" + hướng dẫn cắm xe (UC-024) | → chuyển sang TF-002 khi người dùng ra xe |

**Recovery Paths**:
- Thoát app giữa luồng → lần mở lại vào **đúng bước đang dở** (AF-001.1), không bắt đầu lại từ WF-002
- Không có ảnh cho model đã chọn → dùng ảnh silhouette theo phân khúc và nói rõ (AF-002.3) → tiếp tục Bước 4
- Dialog quyền iOS không mở được → dẫn sang Cài đặt hệ thống, nút "Tiếp tục" vẫn bấm được → Bước 7
- Không phát được sound thử (phiên audio bị chiếm) → nêu lý do + nút thử lại; **không** chặn Bước 5

**Alternative Paths**:
- Cài lại sau khi đã mua → Bước 2 hiện "Phục hồi giao dịch" → entitlement được trả lại → phần khoá preset ở Bước 5 biến mất
- Bỏ qua toàn bộ quyền → Bước 6 → Bước 7 trực tiếp (~40 giây tổng) → chuyển sang TF-011
- Bỏ qua bước chọn sound ("Chọn sau") → hệ thống gán preset Free đầu tiên → Bước 6

---

### 5.2 TF-002: Chuyến đi đầu tiên — khoảnh khắc chứng minh giá trị 📱🚗

**Trigger**: người dùng cắm iPhone vào CarPlay lần đầu sau khi thiết lập
**Referenced UCs**: UC-010, UC-015, UC-021, UC-022
**Referenced Screens**: WF-017, WF-016, WF-018, WF-019, WF-006

| Step | Screen | User Action | System Response | Decision Point |
|---|---|---|---|---|
| 1 | — | Cắm iPhone / kết nối không dây | Nhận `carplay_connected`; CarPlay scene active; đọc bounds từ `CPTemplateApplicationScene` | iOS ≥ 17.4? → Bước 2 / < 17.4 → chỉ dashboard + sound, bỏ qua widget |
| 2 | WF-017 🚗 | *Không làm gì — đang lái* | Tính layout từ bounds; render widget; ghi `widget_render_ok` kèm kích thước (UC-015) | Có phần tử vượt bounds? → giảm cấp layout → nếu vẫn thất bại → **TF-003** |
| 3 | WF-016 🚗 | *Không làm gì* | Duck nhạc xuống 20% (nếu có); phát sound Connect qua **loa xe** trong ≤ 1,5s; ghi `sound_played` + `sound_ducking_applied` (UC-010) | Đang có cuộc gọi? → bỏ lượt phát, không phát bù |
| 4 | WF-016 🚗 | *Không làm gì* | ContextEngine sinh câu chào on-device; phát qua `AVSpeechSynthesizer` trong ≤ 2s; ghi `voice_greeting_played` (UC-021) | Gói Free? → không phát; WF-018 hiện một dòng tĩnh |
| 5 | WF-016 🚗 | Nhìn một lượt dashboard | Hiện thẻ theo thứ tự mặc định + **một dòng nói rõ dashboard sẽ tự đổi sau vài chuyến** (UC-022) | Chưa đủ dữ liệu học? → dùng thứ tự mặc định, **không** giả vờ đã cá nhân hóa |
| 6 | WF-016 🚗 | Chạm một thẻ (tuỳ chọn) | Thực hiện hành động trong ≤ 1s; ghi `ai_recommendation_tapped` | → chuyển sang TF-010 ở các chuyến sau |
| 7 | WF-006 | Mở app iPhone sau chuyến | Hiện lần kết nối gần nhất và kết quả render | Render thất bại? → dòng cảnh báo dẫn WF-014 (**TF-003**) |

**Recovery Paths**:
- Widget không render được → WF-019 hiện thông báo bằng chữ, **không bao giờ màn trắng** → TF-003
- Sound không phát được (phiên audio bị chiếm) → bỏ lượt phát và ghi lý do; **không** phát bù qua loa iPhone
- Mất mạng → thẻ nhạc/thời tiết dùng cache và ghi rõ thời điểm cập nhật; thẻ shortcut vẫn hoạt động
- Chỉ widget lỗi nhưng dashboard vẫn được → WF-016 hoạt động đầy đủ, chỉ vùng widget bị thay bằng thông báo

**Alternative Paths**:
- Gói Free → widget đầy đủ chức năng + dashboard cơ bản + WF-018; **không** có giọng chào
- iOS 16.4–17.3 → bỏ qua Bước 2; sound và dashboard vẫn hoạt động; WF-008 nêu rõ yêu cầu iOS 17.4+ cho widget
- Mọi quyền bị từ chối → Bước 4 phát câu chào theo giờ; Bước 5 dùng thứ tự mặc định (TF-011)

---

### 5.3 TF-003: Xử lý widget không render được trên xe 🚗📱

**Trigger**: một lần render widget thất bại (vượt bounds hoặc hết bộ nhớ)
**Referenced UCs**: UC-015, UC-016, UC-017
**Referenced Screens**: WF-017, WF-019, WF-016, WF-006, WF-014, WF-028, WF-030, WF-023

| Step | Screen | User Action | System Response | Decision Point |
|---|---|---|---|---|
| 1 | WF-017 🚗 | *Đang lái* | Phát hiện render thất bại; ghi `widget_render_failed` kèm `screen_width`, `screen_height`, `failure_reason` (UC-015) | `failure_reason` là vượt-bounds hay hết-bộ-nhớ? → phân biệt rõ trong telemetry |
| 2 | WF-019 🚗 | Đọc thông báo | Hiện: đây là vấn đề tương thích màn hình xe này + hướng dẫn mở màn Chẩn Đoán trên iPhone (UC-016) | Dashboard còn hoạt động? → WF-016 vẫn đầy đủ |
| 3 | WF-006 | Mở app iPhone sau chuyến | Hiện dòng cảnh báo dẫn WF-014 | Lần render kế tiếp thành công? → cảnh báo **tự xoá** |
| 4 | WF-014 | Xem dữ liệu chẩn đoán | Hiện kích thước scene thật đã nhận, phiên bản iOS, xe, `failure_reason` các lần gần nhất (UC-017) | Muốn thử sửa trước? → Bước 4a |
| 4a | WF-023 | Xem widget ở kích thước thật vừa ghi nhận | Chỉ rõ phần tử nào vượt vùng an toàn (UC-013) | Sửa được? → giảm bớt phần tử → quay lại TF-004 Bước 5 |
| 5 | WF-014 | Chạm "Gửi báo cáo" | Mở WF-028 | — |
| 6 | WF-028 | Xem **từng mục** dữ liệu sẽ gửi, chạm "Gửi" | Xác nhận trong ≤ 500ms không chờ mạng; WF-030 toast (UC-017) | Không có mạng? → xếp hàng on-device |
| 7 | — | — | Nếu lỗi lặp ≥ 3 lần cùng một kích thước → telemetry đánh dấu ưu tiên cao, phát hiện xe không tương thích trong 24h | — |

**Recovery Paths**:
- Người dùng không muốn gửi gì → đóng WF-028; dữ liệu chẩn đoán **chỉ nằm trên máy**
- Chưa từng kết nối CarPlay nhưng vào WF-014 → hiện hướng dẫn cắm xe, **không** hiện bảng trống
- Lỗi do hết bộ nhớ widget extension → hạ dung lượng ảnh (WF-024 AF-014.4) rồi thử lại → TF-004
- Người dùng đang không hài lòng và định để 1★ → WF-030 biến thể mời đánh giá **bị chặn** trong 7 ngày sau lỗi render (AC-033.2), thay vào đó người dùng đã có kênh WF-028

**Alternative Paths**:
- Lỗi tạm thời, lần cắm kế tiếp thành công → mọi cảnh báo tự xoá, không để lại cảnh báo giả
- QA chủ động dùng luồng này làm công cụ kiểm thử test matrix R-11 → Bước 4 → nút sao chép payload ở WF-028

---

### 5.4 TF-004: Tạo và kiểm tra widget trước khi ra xe 📱

**Trigger**: người dùng muốn có widget, hoặc muốn đổi widget hiện tại
**Referenced UCs**: UC-012, UC-013, UC-014
**Referenced Screens**: WF-006, WF-008, WF-024, WF-023, WF-010, WF-030

| Step | Screen | User Action | System Response | Decision Point |
|---|---|---|---|---|
| 1 | WF-006 | Chạm thẻ widget (hoặc Tab Widgets) | Mở WF-008 với widget hiện tại nạp sẵn (nếu có) | Chưa có widget? → hiện ≥ 3 preset gợi ý theo xe đã chọn |
| 2 | WF-008 | Chọn một preset hoặc loại widget | Cập nhật preview nhúng ở Zone A (UC-012) | Loại widget thuộc Premium? → xem trước đầy đủ, nút chuyển "Mở khoá" → WF-010 |
| 3 | WF-008 | Chạm ô ảnh | Mở WF-024 | Muốn dùng ảnh xe theo model? → chọn ngay, không cần quyền ảnh |
| 4 | WF-024 | Chọn ảnh, điều chỉnh khung crop, chạm "Xong" | Hiện vùng sẽ bị cắt **trước khi lưu**; nén ảnh dưới ngưỡng widget extension (UC-014) | Ảnh độ phân giải thấp? → cảnh báo sẽ mờ trên màn hình xe |
| 5 | WF-008 | Chạm "Xem trước trên xe của tôi" | Mở WF-023 | Đã từng cắm xe? → dùng **kích thước thật**; chưa → ≥ 4 tỉ lệ tham chiếu, nói rõ là ước lượng |
| 6 | WF-023 | Vuốt qua các tỉ lệ, kiểm dark/light | Chỉ rõ phần tử nào vượt vùng an toàn ở từng tỉ lệ (UC-013) | Có phần tử vượt? → Bước 6a |
| 6a | WF-023 | Bỏ bớt phần tử, hoặc đổi ảnh tại chỗ | Cập nhật preview ngay, không cần về WF-008 (AF-013.2) | — |
| 7 | WF-023 | Chạm "Dùng bản này" | Quay về WF-008 với cấu hình đã xác nhận | — |
| 8 | WF-008 | Chạm "Lưu widget" | Ghi cấu hình vào App Group **ngay tại thời điểm lưu**; WF-030 toast; cập nhật thẻ trên WF-006 (UC-012) | Ghi thất bại? → nêu lỗi + nút thử lại, **giữ bản nháp** |

**Recovery Paths**:
- Thoát giữa lúc tạo → bản nháp được giữ; lần mở lại WF-008 hỏi "Tiếp tục widget đang làm?" (AF-012.3)
- Không lưu được vào App Group → nêu lỗi cụ thể + nút thử lại; không mất cấu hình đang làm
- Quyền thư viện ảnh bị từ chối → chỉ dùng ảnh xe theo model; luồng **không** bị chặn (AF-014.2)
- iOS < 17.4 → vẫn cấu hình được và lưu được, nêu rõ cần iOS 17.4+ để widget chạy trên xe (AF-012.4)

**Alternative Paths**:
- Gói Free đã dùng hết 1 widget → cho **đổi** widget hiện có; "Thêm widget thứ hai" dẫn WF-010 (AF-012.1)
- Vào từ WF-014 sau khi có lỗi render → bắt đầu ở Bước 5 với kích thước thật đã ghi nhận (TF-003 Bước 4a)
- Đổi nhanh không cần preview → Bước 1 → Bước 2 → Bước 8 (2 chạm)

---

### 5.5 TF-005: Cấu hình bộ ba âm thanh 📱

**Trigger**: người dùng muốn đặt sound cho cả ba sự kiện, hoặc đổi sound đang dùng
**Referenced UCs**: UC-006, UC-007, UC-008, UC-009
**Referenced Screens**: WF-006, WF-007, WF-020, WF-012, WF-010, WF-030

| Step | Screen | User Action | System Response | Decision Point |
|---|---|---|---|---|
| 1 | WF-006 | Chạm thẻ sound (hoặc Tab Sounds) | Mở WF-007 ở sự kiện gần nhất, sound đang dùng ghim đầu | — |
| 2 | WF-007 | Chạm một dòng preset | Phát inline trong ≤ 300ms; dừng dòng đang phát nếu có (UC-006) | Muốn nghe kỹ? → Bước 2a |
| 2a | WF-020 | Nghe kỹ, kéo slider âm lượng | Sound mẫu phát ở đúng mức mới trong ≤ 300ms (UC-009) | Preset khoá? → nghe đầy đủ, nút chuyển "Mở khoá" → WF-010 |
| 3 | WF-007 | Chạm "Dùng cho lúc lên xe" | Lưu; ghi vào App Group; WF-030 toast (UC-007) | — |
| 4 | WF-007 | Chuyển segmented control sang "Disconnect" | Danh sách giữ nguyên, nhãn nút gán đổi theo sự kiện (UC-008) | — |
| 5 | WF-007 | Nghe thử và gán sound Disconnect | Lưu độc lập với sound Connect | — |
| 6 | WF-007 | Chuyển sang "Arrive" | — | Quyền Vị trí bị từ chối? → mục Arrive hiện **không khả dụng kèm lý do**, không cho gán |
| 7 | WF-012 | Mở Cài Đặt Chung, kéo slider âm lượng sound | Lưu ngay, không cần nút Lưu; âm lượng nhạc **không** bị đổi (UC-009) | Đặt về 0? → nêu rõ trạng thái "đang tắt" |

**Recovery Paths**:
- Không phát được sound thử (đang có cuộc gọi) → nêu lý do + nút thử lại; danh sách vẫn duyệt bình thường
- Chạm dòng khác khi đang phát → dừng dòng cũ ngay, không phát chồng (AF-006.4)
- Quyền Vị trí bị từ chối → Arrive bị vô hiệu có lý do, thay vì để người dùng chờ một âm thanh không bao giờ phát

**Alternative Paths**:
- Chỉ muốn sound cho Connect → dừng ở Bước 3; hai sự kiện kia để trống là mặc định hợp lệ (AF-008.1)
- Chọn "Không dùng" cho Connect nhưng giữ Arrive → hợp lệ, không phải trạng thái lỗi (AF-007.2)
- Gói Free → 3 preset mở dùng được đầy đủ; preset khoá nghe thử được nhưng gán thì dẫn WF-010

---

### 5.6 TF-006: Cấu hình giọng chào và xác minh nó có thật 📱

**Trigger**: người dùng muốn bật giọng chào, hoặc muốn kiểm xem tính năng này có thật
**Referenced UCs**: UC-018, UC-019, UC-020
**Referenced Screens**: WF-006, WF-009, WF-022, WF-010

| Step | Screen | User Action | System Response | Decision Point |
|---|---|---|---|---|
| 1 | WF-006 | Chạm thẻ giọng chào (hoặc Tab Widgets) | Mở WF-009 với công tắc chính ở đầu màn hình | — |
| 2 | WF-009 | Chạm "Nghe thử" | ContextEngine sinh câu chào từ **ngữ cảnh thật lúc này**, phát và hiện chữ đồng thời (UC-020) | Gói Free? → nghe thử **đầy đủ**, công tắc chính hiện khoá → WF-010 |
| 3 | WF-009 | Chạm "Nghe thử" lần nữa | Trả về **câu khác**, không lặp y hệt (AC-020.2) | Sau ≥ 4 lần → người dùng thấy đủ dải biến thể |
| 4 | WF-009 | Xem 4 dòng nguồn ngữ cảnh | Mỗi dòng có toggle + ví dụ câu chào + trạng thái quyền (UC-019) | Nguồn cần quyền chưa có? → Bước 4a |
| 4a | WF-022 | Đọc lý do, chạm "Cho phép" | Gọi dialog quyền iOS; cập nhật trạng thái dòng nguồn | Đã từ chối trước đó? → nút chuyển thành "Mở Cài đặt" |
| 5 | WF-009 | Bật/tắt từng nguồn | ContextEngine chỉ đọc nguồn được bật (AC-019.1) | Tắt hết 4 nguồn? → vẫn phát câu chào trung tính, **không im lặng** |
| 6 | WF-009 | Chạm "Nghe thử" lần cuối | Câu chào phong phú hơn nhờ nguồn mới bật — người dùng thấy khác biệt cụ thể | → chuyển sang TF-002 hoặc TF-010 khi lên xe |

**Recovery Paths**:
- TTS không phát được → vẫn hiển thị **chữ** câu chào kèm lý do; nội dung vẫn kiểm chứng được dù âm thanh lỗi
- Nguồn thời tiết không lấy được dữ liệu → bỏ qua nguồn đó cho lượt này, dùng nguồn còn lại (AF-019.3)
- Dialog quyền không mở được → dẫn sang Cài đặt hệ thống

**Alternative Paths**:
- Người dùng chỉ muốn tắt hẳn → Bước 1 → tắt công tắc chính → cấu hình nguồn được giữ nguyên (AF-018.1)
- Gói Free → nghe thử đầy đủ ở Bước 2–3 (đây là cơ chế chống R-10/R-13) nhưng tính năng chỉ chạy trên xe sau khi nâng cấp
- Từ chối hết quyền → chỉ nguồn "giờ trong ngày" hoạt động, được nói rõ, không im lặng (TF-011)

---

### 5.7 TF-007: Từ gói Free đến quyết định nâng cấp 📱

**Trigger**: người dùng ở gói Free chạm vào một tính năng khoá, sau khi đã xác nhận app chạy trên xe mình
**Referenced UCs**: UC-024, UC-025, UC-026, UC-027
**Referenced Screens**: WF-006, WF-007, WF-008, WF-010, WF-011, WF-030, WF-012

| Step | Screen | User Action | System Response | Decision Point |
|---|---|---|---|---|
| 1 | WF-006 | Dùng gói Free nhiều chuyến | Widget + 3 sound + dashboard cơ bản hoạt động đầy đủ, không quảng cáo, không giới hạn thời gian (UC-024) | Widget **không** chạy trên xe? → người dùng phát hiện **trước khi trả tiền** (AF-024.2) → TF-003 |
| 2 | WF-007 hoặc WF-008 | Chạm một tính năng khoá | Mở WF-010 với ngữ cảnh **đúng tính năng vừa chạm** (AF-024.3) | `days_since_install > 0`? → bắt buộc đúng, ghi `paywall_shown` |
| 3 | WF-010 | Xem 4 lựa chọn | Hiện Free (đang dùng) · $4,99/tháng · $29,99/năm · $49,99 lifetime — **không có bậc weekly**; giá cuối bằng tiền tệ địa phương (UC-025) | Không lấy được giá từ StoreKit? → báo lỗi rõ, **không** hiện giá cache |
| 4 | WF-010 | Chọn một bậc | Chuyển WF-011 | Chọn "Tiếp tục dùng gói Free"? → về màn hình trước, không hỏi lại trong phiên |
| 5 | WF-011 | Đọc giá cuối, ngày hết trial, ngày trừ tiền | Hiện đủ 4 mốc; **đây là điểm chặn duy nhất trước giao dịch** (UC-026) | Bậc Lifetime? → không hiện ngày gia hạn (TF-009) |
| 6 | WF-011 | Chạm "Xác nhận" | Ghi `price_confirmed` **trước khi** gọi dialog thanh toán; mở dialog StoreKit | Huỷ ở dialog? → về WF-011, giữ lựa chọn |
| 7 | — | Hoàn tất thanh toán | `EntitlementService` cập nhật; tính năng mở khóa trong ≤ 2s; ghi `trial_started`; gửi xác nhận giao dịch (UC-027) | Thanh toán thất bại? → nêu nguyên nhân StoreKit + nút thử lại |
| 8 | WF-006 | Xem trạng thái | Badge "Trial còn 7 ngày" + ngày trừ tiền ở Zone D | → chuyển sang TF-008 vào ngày 6 |

**Recovery Paths**:
- Thanh toán thất bại → giữ nguyên ở WF-011 với nút thử lại; **không** trả về WF-010 và không mất lựa chọn
- Đổi vùng App Store giữa lúc mua → giá đọc lại từ StoreKit trước khi hiển thị (AF-026.4)
- Đã dùng trial trước đó → bậc giá không hiện trial, nêu rõ là mua trực tiếp (AF-027.2)
- Đã mua trên thiết bị khác → "Phục hồi giao dịch" ở WF-010 Zone D

**Alternative Paths**:
- Người dùng không nâng cấp → tiếp tục dùng Free vô thời hạn; **không** bị nhắc lặp lại theo phiên (AF-024.1)
- Vào paywall chủ động từ WF-012 → bỏ qua Bước 2, vào Bước 3 với Zone A ở dạng tổng quát
- Chọn Lifetime → TF-009

---

### 5.8 TF-008: Kết thúc trial — đăng ký hoặc huỷ 📱

**Trigger**: trial bước sang ngày 6
**Referenced UCs**: UC-028, UC-029, UC-027
**Referenced Screens**: WF-013, WF-027, WF-025, WF-012, WF-006

| Step | Screen | User Action | System Response | Decision Point |
|---|---|---|---|---|
| 1 | WF-013 | Đọc thông báo | Hiện số ngày còn lại + **số tiền chính xác** + **ngày bị trừ**; tông trung tính, không đếm ngược gây áp lực (UC-028) | Đã chọn "Nhắc sau" 2 lần? → nút "Nhắc sau" biến mất |
| 2 | WF-013 | Chọn một trong ba nút ngang hàng | — | "Đăng ký" → Bước 3 · "Nhắc sau" → Bước 1 ở ngày 7 · "Huỷ trial" → Bước 4 |
| 3 | WF-006 | — | Trial tiếp tục tới ngày 7 rồi chuyển sang trả phí; ghi `trial_converted` (UC-027) | — |
| 4 | WF-027 | Đọc alert xác nhận | Nêu rõ **quyền Premium còn tới ngày nào** và **cấu hình đã tạo sẽ được giữ** (UC-029) | Chọn "Giữ đăng ký"? → về WF-025, không làm gì |
| 5 | WF-027 | Chạm "Huỷ đăng ký" | Chuyển sang trang quản lý subscription của iOS; ghi `subscription_cancelled` | Không mở được trang iOS? → hướng dẫn đường đi thủ công |
| 6 | WF-025 | Xem lại trạng thái | Hiện ngày quyền Premium kết thúc (AF-029.3) | — |
| 7 | WF-006 | Sau ngày 7 | Về gói Free; **widget và sound đã cấu hình vẫn còn** (AC-027.3) | Có > 1 widget? → giữ 1 widget, các widget còn lại được lưu chờ nếu nâng cấp lại |

**Recovery Paths**:
- Không đọc được ngày hết trial từ StoreKit → nêu rõ không xác định được và dẫn sang trang subscription của iOS; **tuyệt đối không đoán một con số**
- Người dùng bỏ qua hoàn toàn cả hai lần nhắc → trial chuyển thành trả phí đúng ngày 7 **như đã thông báo**, không có bất ngờ
- Huỷ rồi đổi ý → WF-025 → WF-010 để đăng ký lại; cấu hình cũ được dùng lại nguyên trạng

**Alternative Paths**:
- Người dùng huỷ ngay từ ngày 1 → vào WF-025 chủ động từ WF-012; vẫn giữ Premium tới hết ngày 7 (AF-027.1)
- Có cả Lifetime và subscription → WF-025 nêu rõ Lifetime đã bao trùm, nhắc huỷ subscription để không trả trùng

---

### 5.9 TF-009: Mua gói Lifetime 📱

**Trigger**: người dùng chọn bậc "$49,99 — một lần" trên paywall
**Referenced UCs**: UC-030, UC-026, UC-029
**Referenced Screens**: WF-010, WF-011, WF-025, WF-030

| Step | Screen | User Action | System Response | Decision Point |
|---|---|---|---|---|
| 1 | WF-010 | Chọn bậc Lifetime | Chuyển WF-011 (UC-030) | Đang có subscription? → Bước 4 sẽ nhắc huỷ |
| 2 | WF-011 | Đọc xác nhận | Nêu rõ **một lần, không tự động gia hạn**; **không** hiện ngày gia hạn (AC-030.1) | — |
| 3 | WF-011 | Chạm "Xác nhận" | Ghi `price_confirmed`; StoreKit xử lý non-consumable (UC-026) | Thanh toán thất bại? → nêu nguyên nhân + nút thử lại |
| 4 | WF-030 | Xem toast | Toàn bộ tính năng Premium mở vĩnh viễn, **không phụ thuộc kết nối mạng sau đó** | Đang có subscription? → hiện nhắc huỷ kèm lối vào WF-025 (AF-030.1) |
| 5 | WF-025 | (nếu có subscription) chạm "Huỷ đăng ký" | Chuyển trang subscription iOS; quyền Premium không bị ảnh hưởng vì Lifetime đã bao trùm | — |

**Recovery Paths**:
- Thanh toán thất bại → giữ ở WF-011 với nút thử lại (như AF-026.2)
- Cài lại app → "Phục hồi giao dịch" trả lại Lifetime **không phải trả tiền lần nữa** (AF-030.2)
- Không đọc được entitlement khi offline → mặc định dùng bản cache đã xác thực; Lifetime không bị hạ xuống Free vì mất mạng

**Alternative Paths**:
- Nhiều thiết bị cùng Apple ID → phục hồi giao dịch trên từng thiết bị
- Người dùng đổi ý và muốn subscription thay vì Lifetime → quay lại WF-010 từ Bước 1

---

### 5.10 TF-010: Chuyến đi hằng ngày (người dùng quen) 📱🚗

**Trigger**: người dùng đã dùng app ≥ 1 tuần, lên xe như thường lệ
**Referenced UCs**: UC-010, UC-011, UC-021, UC-022, UC-023
**Referenced Screens**: WF-017, WF-016, WF-018

| Step | Screen | User Action | System Response | Decision Point |
|---|---|---|---|---|
| 1 | WF-017 🚗 | Lên xe, không mở app | Kích thước xe đã biết ⇒ đường render ngắn hơn; widget hiện đúng như lần trước (UC-015) | — |
| 2 | WF-016 🚗 | *Không làm gì* | Duck nhạc, phát sound Connect qua loa xe ≤ 1,5s; phục hồi âm lượng nguyên trạng (UC-010) | Cắm lại dây trong 3s? → chỉ phát **1 lần** (AF-010.4) |
| 3 | WF-016 🚗 | *Không làm gì* | Câu chào dùng ngữ cảnh đầy đủ (giờ + thời tiết + lịch + tuyến quen); **không lặp câu của lần trước** (UC-021) | Đang có cuộc gọi? → bỏ lượt phát |
| 4 | WF-016 🚗 | Nhìn một lượt | Thẻ đã học được thói quen: thẻ hay dùng ở Zone A (UC-022) | Ngữ cảnh đoán sai? → Bước 4a |
| 4a | WF-016 🚗 | Bỏ qua thẻ đó | Hạ trọng số thẻ; **không** cần vào Settings để sửa (AF-022.2) | — |
| 5 | WF-016 🚗 | Chạm thẻ đúng | Hành động bắt đầu ≤ 1s; ghi `ai_recommendation_tapped` (UC-023) | Hành động thất bại? → thông báo gọn trên thẻ + hành động thay thế, **không modal** |
| 6 | WF-016 🚗 | Tới nơi | Sound Arrive phát (nếu có quyền Vị trí và đã gán) | Arrive vừa phát trong 10s? → bỏ sound Disconnect (AF-011.3) |
| 7 | — 🚗 | Tắt máy | Sound Disconnect phát **qua loa xe** trước khi phiên audio bị thu hồi; lệch ≤ 1s (UC-011) | Phiên audio bị thu hồi trước? → **bỏ lượt**, tuyệt đối không phát qua loa iPhone |

**Recovery Paths**:
- Mất mạng → thẻ nhạc/thời tiết dùng cache và ghi rõ thời điểm cập nhật; shortcut vẫn hoạt động (AF-022.3)
- Một thẻ không lấy được dữ liệu → chỉ thẻ đó hiện thông báo, các thẻ khác không bị ảnh hưởng
- Đang có chỉ dẫn dẫn đường → nhường chỉ dẫn, phát sound sau, chờ tối đa 3s rồi bỏ lượt (AF-010.2)

**Alternative Paths**:
- Gói Free → dashboard cơ bản + WF-018 một dòng tĩnh; không có giọng chào
- Đi tuyến lạ (công tác) → ngữ cảnh kém chính xác; Bước 4a là cách sửa rẻ nhất
- Rút dây thay vì tắt máy → coi là disconnect bình thường (AF-011.2)

---

### 5.11 TF-011: Dùng app khi đã từ chối toàn bộ quyền 📱🚗

**Trigger**: người dùng hoàn tất onboarding mà không cấp quyền nào
**Referenced UCs**: UC-004, UC-005, UC-019, UC-021
**Referenced Screens**: WF-005, WF-006, WF-009, WF-016, WF-017, WF-022

| Step | Screen | User Action | System Response | Decision Point |
|---|---|---|---|---|
| 1 | WF-005 | Chạm "Bỏ qua tất cả" | Ghi trạng thái quyền là đã từ chối; chuyển WF-006 (AF-004.2) | — |
| 2 | WF-006 | Xem trạng thái | Hiện đầy đủ: widget đang bật, sound đang chọn, xe đã chọn; **một** dòng mời cấp quyền dạng tĩnh (AC-005.3) | Đã hiện dòng mời? → **không** nhắc lại theo phiên, không popup |
| 3 | WF-017 🚗 | Cắm xe | Widget render bình thường — widget **không** phụ thuộc quyền nào (UC-005) | — |
| 4 | WF-016 🚗 | *Không làm gì* | Sound Connect phát bình thường; câu chào phát ở biến thể **chỉ theo giờ**, không im lặng và không báo lỗi (AC-005.2) | — |
| 5 | WF-016 🚗 | Nhìn dashboard | Thẻ theo thứ tự mặc định; **không có** thẻ gợi ý điểm đến | — |
| 6 | WF-009 | (tuỳ chọn) mở cài đặt giọng chào | 3 nguồn hiện "cần quyền" kèm lối vào; nguồn "giờ" hoạt động (UC-019) | Muốn cấp quyền? → Bước 6a |
| 6a | WF-022 | Đọc lý do, chạm "Mở Cài đặt" | Dẫn sang Cài đặt hệ thống (vì iOS không cho hỏi lại lần hai) | Cấp xong? → ngữ cảnh mới có hiệu lực từ **lần kết nối kế tiếp** (AC-005.4) |
| 7 | WF-016 🚗 | Chuyến kế tiếp | Câu chào và dashboard dùng ngữ cảnh mới, không cần khởi động lại app | — |

**Recovery Paths**:
- Cấp quyền Vị trí ở mức "Khi dùng app" → nêu rõ tuyến đường chỉ học được khi app đang mở, **không im lặng** để người dùng tưởng đã đủ
- Cấp Lịch nhưng từ chối Vị trí → giọng chào dùng lịch, dashboard không có gợi ý điểm đến; mọi tổ hợp một phần đều phải xử lý được
- Người dùng thắc mắc vì sao dashboard không đổi → giải thích ngay tại WF-009, không dùng popup (AF-005.1)

**Alternative Paths**:
- Không bao giờ cấp quyền → app dùng được mãi ở mức này; đây là trạng thái hợp lệ, không phải trạng thái lỗi
- Cấp toàn bộ quyền sau vài tuần → chuyển sang TF-010

---

### 5.12 TF-012: Đổi ngôn ngữ và kiểm tra giọng chào theo ngôn ngữ 📱

**Trigger**: người dùng ở LATAM muốn dùng app bằng tiếng Tây Ban Nha hoặc tiếng Bồ Đào Nha
**Referenced UCs**: UC-031, UC-020
**Referenced Screens**: WF-012, WF-026, WF-009, WF-016

| Step | Screen | User Action | System Response | Decision Point |
|---|---|---|---|---|
| 1 | WF-012 | Chạm dòng "Ngôn ngữ" | Mở WF-026; hiện ngôn ngữ hiện tại | Ngôn ngữ hệ thống không thuộc 3 ngôn ngữ? → nêu rõ đang dùng English (AF-031.1) |
| 2 | WF-026 | Chọn Español hoặc Português (Brasil) | Toàn bộ UI đổi **ngay**, không cần khởi động lại (AC-031.1) | Thiếu bản dịch một chuỗi? → rơi về English cho đúng chuỗi đó, không hiện khoá dịch thô |
| 3 | WF-012 | Kiểm giá | Giá hiển thị theo **tiền tệ địa phương của storefront**, độc lập với ngôn ngữ UI (AC-031.3) | — |
| 4 | WF-009 | Chạm "Nghe thử" | Câu chào phát **bằng ngôn ngữ đã chọn**, không chỉ UI (AC-031.2, UC-020) | Câu chào vẫn bằng English? → lỗi chức năng của F9, không phải khác biệt nhỏ |
| 5 | WF-016 🚗 | Lên xe | Câu chào trên xe bằng ngôn ngữ đã chọn (AC-021.7) | Đổi ngôn ngữ khi đang cắm xe? → câu đang phát **không bị cắt giữa câu** (AF-031.2) |

**Recovery Paths**:
- Thiếu bản dịch → rơi về English cho đúng chuỗi thiếu, phần còn lại giữ nguyên ngôn ngữ đã chọn
- Đổi ngôn ngữ khi đang cắm CarPlay → UI CarPlay cập nhật ở lần vẽ kế tiếp; nội dung giọng chào đổi từ lượt phát kế tiếp
- Người dùng tìm DE/FR/IT → nêu rõ thuộc MVP 2, **không** hiện lựa chọn không hoạt động (AF-031.3)

**Alternative Paths**:
- Giữ "Theo hệ thống" → không cần thao tác gì; người dùng ở MX/BR tự động có đúng ngôn ngữ
- Muốn UI English nhưng giọng chào tiếng Tây Ban Nha → hai thứ chọn độc lập được

---

### 5.13 TF-013: Phản hồi được phân luồng theo mức hài lòng 📱

**Trigger**: hệ thống phát hiện chuỗi trải nghiệm tích cực (sound phát thành công ≥ 5 lần, không có lỗi render)
**Referenced UCs**: UC-033, UC-017
**Referenced Screens**: WF-030, WF-028, WF-012

| Step | Screen | User Action | System Response | Decision Point |
|---|---|---|---|---|
| 1 | — | — | Kiểm điều kiện kích hoạt | Có `widget_render_failed` trong 7 ngày? → **không** hiện lời mời (AC-033.2) → dừng flow |
| 2 | WF-030 | Thấy overlay mời đánh giá | Hiện bộ chọn mức hài lòng, đóng được bằng một chạm, không chặn tác vụ (UC-033) | Đóng? → không hiện lại trong ≥ 30 ngày (AF-033.1) |
| 3 | WF-030 | Chọn mức hài lòng | — | **Hài lòng** → Bước 4 · **Không hài lòng** → Bước 5 |
| 4 | — | Đánh giá trên App Store | Mở dialog đánh giá của iOS; ghi `in_app_rating_submitted` | — |
| 5 | WF-028 | Điền ghi chú, chạm "Gửi" | Mở kênh báo lỗi; Zone C (ô ghi chú) được nhấn mạnh vì ở đây **lời của người dùng** quan trọng hơn số liệu (UC-017) | Không có mạng? → xếp hàng on-device |
| 6 | WF-030 | Thấy toast xác nhận | Xác nhận đã nhận trong ≤ 500ms | — |

**Recovery Paths**:
- Người dùng không hài lòng nhưng không muốn gõ gì → đóng WF-028; hệ thống **không** đẩy họ ra App Store như một đường lui
- Không gửi được báo cáo → xếp hàng on-device và gửi khi có mạng
- Người dùng tự tìm để đánh giá → dòng "Đánh giá Carbina" luôn có trên WF-012 (AF-033.2)

**Alternative Paths**:
- Người dùng gặp lỗi và tự vào WF-014 → TF-003 Bước 5, cùng đích đến WF-028 nhưng khác điểm khởi phát
- Đủ điều kiện kích hoạt nhiều lần → chỉ hiện theo tần suất đã định, không hiện lại trong 30 ngày sau khi bị đóng

---

### Kiểm tra phủ Task Flow

| Yêu cầu | Kết quả |
|---|---|
| Số task flow | **13** (ngưỡng Medium: 8–15 ⇒ Pass) |
| Mọi UC ưu tiên High được phủ ≥ 1 flow | **22/22** — UC-001, 002, 004, 005 (TF-001, TF-011) · UC-006, 007, 009 (TF-005) · UC-010, 011 (TF-002, TF-010) · UC-012, 013 (TF-004) · UC-015, 016 (TF-002, TF-003) · UC-018, 020 (TF-006) · UC-021, 022, 023 (TF-002, TF-010) · UC-024, 025, 026, 027 (TF-007) |
| Mọi bước tham chiếu WF-XXX + UC-XXX | Đạt — mỗi bảng có cột Screen là WF-XXX và UC-XXX trong cột System Response |
| Mọi điểm quyết định có đường phục hồi | Đạt — mỗi flow có mục **Recovery Paths** riêng |
| UC ưu tiên Medium/Low cũng được phủ | UC-003 (TF-001) · UC-008 (TF-005) · UC-014 (TF-004) · UC-017 (TF-003, TF-013) · UC-019 (TF-006, TF-011) · UC-028, 029 (TF-008) · UC-030 (TF-009) · UC-031 (TF-012) · UC-033 (TF-013) |
| UC chưa có task flow | **UC-032** (xoá dữ liệu on-device), **UC-036** (đổi theme) và **UC-034, UC-035** (post-MVP). UC-036 là một thao tác một bước trong WF-012, được phủ bằng sub-flow SF-021 chứ không tạo thành hành trình xuyên màn hình. UC-032 là hành động một bước trong WF-012 → WF-029, không tạo thành hành trình xuyên màn hình; UC-034/UC-035 thuộc MVP 2/MVP 3 nên task flow sẽ được viết khi lên kế hoạch giai đoạn đó |

---

## 5 bis. Sub-Flows & Micro-Interactions

Task flow ở §5 mô tả hành trình **xuyên màn hình**. Sub-flow dưới đây mô tả những gì xảy ra **bên trong một màn hình**.

> **Nguyên tắc riêng cho bề mặt CarPlay**: sub-flow trên WF-016 → WF-019 phải **kiềm chế tối đa về chuyển động**. Animation trên màn hình xe không phải để làm đẹp — mọi chuyển động thu hút mắt người lái là một chi phí an toàn. Vì vậy chỉ có **một** sub-flow cho bề mặt CarPlay (SF-017), và nó cố tình dùng crossfade chậm thay vì chuyển động vị trí.

### SF-001: Kéo xuống để làm mới trạng thái kết nối

**Parent Screen**: WF-006 · **Source UC**: UC-024, UC-016
**Trigger**: người dùng kéo xuống ở đầu Home
**Purpose**: cho người dùng cách tự kiểm tra trạng thái ngay sau khi vừa từ xe vào nhà, thay vì phải đoán app có ghi nhận chuyến vừa rồi hay không

| Step | Component | User Action | System Response | Micro-State | Haptic |
|---|---|---|---|---|---|
| 1 | Zone A — thẻ trạng thái | Kéo xuống > 60pt | Chỉ báo tải xuất hiện; đọc lại trạng thái kết nối và kết quả render gần nhất | Refreshing | Light (khi vượt ngưỡng) |
| 2 | Zone A | Nhả tay | Cập nhật trạng thái; nếu có lỗi render mới thì Zone D hiện dòng cảnh báo | Updated | None |
| 3 | Zone D — dòng cảnh báo | {Không có lỗi nào} | Dòng cảnh báo cũ **tự biến mất** | Cleared | None |

**Visual Transition**: chỉ báo tải mờ dần vào trong 0,2s; thẻ trạng thái crossfade sang giá trị mới trong 0,25s — không nhảy layout.
**Recovery**: nếu không đọc được dữ liệu, giữ giá trị cũ kèm dòng "chưa cập nhật được" thay vì hiện trạng thái rỗng.

---

### SF-002: Bộ chọn xe ba tầng

**Parent Screen**: WF-003 · **Source UC**: UC-002, UC-003
**Trigger**: người dùng chọn một hãng xe
**Purpose**: đi từ 40+ hãng và 400+ model xuống một xe cụ thể mà không rời màn hình và không mất ngữ cảnh

| Step | Component | User Action | System Response | Micro-State | Haptic |
|---|---|---|---|---|---|
| 1 | Danh sách hãng | Chạm một hãng | Hàng hãng thu lên đầu và ghim lại; danh sách model của hãng đó xuất hiện bên dưới | Level 2 | Light |
| 2 | Danh sách model | Chạm một model | Model được ghim tầng hai; bộ chọn năm xuất hiện | Level 3 | Light |
| 3 | Bộ chọn năm | Chọn năm | Ảnh xe hiện dần ở Zone A; nút "Đúng xe của tôi" bật sáng | Complete | Medium |
| 4 | Hàng đã ghim | Chạm hàng hãng đã ghim | Quay lại tầng 1, **giữ nguyên** model đã chọn để chọn lại nhanh | Level 1 | Light |
| 5 | Cuối danh sách | {Không tìm thấy} | Dòng "Không tìm thấy xe của tôi" luôn ở cuối mọi tầng → mở WF-021 | — | None |

**Visual Transition**: tầng cũ thu lên thành hàng ghim cao 44pt trong 0,25s; tầng mới trượt vào từ dưới; ảnh xe ở Zone A crossfade 0,3s.
**Recovery**: chạm hàng ghim để lùi tầng bất kỳ lúc nào; không có model nào bị mất khi lùi.

---

### SF-003: Nghe thử inline trong danh sách âm thanh

**Parent Screen**: WF-007 · **Source UC**: UC-006
**Trigger**: người dùng chạm một dòng preset
**Purpose**: nghe nhanh nhiều preset liên tiếp mà không mở/đóng sheet cho từng cái

| Step | Component | User Action | System Response | Micro-State | Haptic |
|---|---|---|---|---|---|
| 1 | Dòng preset | Chạm dòng | Sound phát trong ≤ 300ms; icon dòng chuyển thành dạng sóng đang chạy | Playing | Light |
| 2 | Dòng preset khác | Chạm dòng thứ hai | Dòng thứ nhất **dừng ngay**, trở về icon tĩnh; dòng thứ hai bắt đầu phát | Switched | Light |
| 3 | Dòng đang phát | {Sound kết thúc} | Icon trở về trạng thái tĩnh; dòng vẫn được đánh dấu "vừa nghe" | Idle | None |
| 4 | Dòng đang phát | Chạm lại dòng đang phát | Dừng phát | Stopped | Light |

**Visual Transition**: icon play → dạng sóng bằng crossfade 0,15s; dạng sóng chạy theo thời gian thực của audio, không phải animation giả.
**Recovery**: nếu phiên audio bị chiếm (đang có cuộc gọi), dòng hiện lý do cụ thể tại chỗ và giữ nguyên trạng thái tĩnh — không hiện dạng sóng khi không có tiếng.

---

### SF-004: Slider âm lượng có nghe thử tức thì

**Parent Screen**: WF-012 · **Source UC**: UC-009
**Trigger**: người dùng kéo slider âm lượng sound
**Purpose**: đặt được mức âm lượng đúng ngay lần đầu, thay vì đoán rồi ra xe thử

| Step | Component | User Action | System Response | Micro-State | Haptic |
|---|---|---|---|---|---|
| 1 | Slider | Bắt đầu kéo | Sound mẫu bắt đầu phát ở mức hiện tại | Previewing | Light |
| 2 | Slider | Tiếp tục kéo | Âm lượng sound mẫu đổi theo tay trong ≤ 300ms; **âm lượng nhạc không đổi** | Adjusting | None |
| 3 | Slider | Nhả tay | Giá trị được lưu ngay, không cần nút Lưu | Saved | Light |
| 4 | Slider | Kéo về 0 | Hiện chữ "đang tắt" thay vì để trống | Muted | Medium |

**Visual Transition**: nhãn giá trị hiện cạnh núm slider trong lúc kéo rồi mờ dần sau 1s. Không có animation nào trên chính thanh slider.
**Recovery**: nếu không phát được sound mẫu, slider vẫn điều chỉnh và lưu được; hiện một dòng nói rõ không nghe thử được lúc này.

---

### SF-005: Thẻ cảnh báo tương thích xuất hiện và tự thu hồi

**Parent Screen**: WF-006 · **Source UC**: UC-016, UC-017
**Trigger**: phiên CarPlay gần nhất có `widget_render_failed`
**Purpose**: đưa lỗi lên chỗ dễ thấy đúng lúc người dùng có thể xử lý (đã đỗ xe), và **không** để lại cảnh báo giả sau khi lỗi đã hết

| Step | Component | User Action | System Response | Micro-State | Haptic |
|---|---|---|---|---|---|
| 1 | Zone D | Mở app sau chuyến bị lỗi | Dòng cảnh báo trượt vào, nêu rõ đây là vấn đề tương thích màn hình | Warning | None |
| 2 | Dòng cảnh báo | Chạm dòng | Mở WF-014 với dữ liệu chẩn đoán đã điền sẵn | Navigating | Light |
| 3 | Dòng cảnh báo | {Lần render kế tiếp thành công} | Dòng cảnh báo **tự biến mất**, không cần người dùng đóng | Cleared | None |
| 4 | Dòng cảnh báo | Vuốt để đóng | Ẩn cho phiên này; hiện lại nếu lỗi lặp ở chuyến sau | Dismissed | Light |

**Visual Transition**: trượt vào từ mép dưới Zone D trong 0,3s; khi tự thu hồi thì mờ dần trong 0,4s — chậm hơn lúc vào, để người dùng kịp nhận ra nó đã hết.
**Recovery**: nếu người dùng đóng nhưng lỗi vẫn tiếp diễn, cảnh báo trở lại ở chuyến kế tiếp — không im lặng vĩnh viễn vì một lần vuốt.

---

### SF-006: Chuyển sự kiện âm thanh mà giữ ngữ cảnh danh sách

**Parent Screen**: WF-007 · **Source UC**: UC-008
**Trigger**: người dùng chuyển segmented control giữa Connect / Disconnect / Arrive
**Purpose**: gán ba sound cho ba sự kiện mà không phải cuộn lại danh sách từ đầu ba lần

| Step | Component | User Action | System Response | Micro-State | Haptic |
|---|---|---|---|---|---|
| 1 | Segmented control | Chạm "Disconnect" | Nhãn nút gán ở Zone B đổi thành "Dùng cho lúc xuống xe"; **vị trí cuộn của danh sách giữ nguyên** | Switched | Light |
| 2 | Danh sách | — | Dấu "đang dùng" chuyển sang preset đã gán cho sự kiện mới (nếu có) | Updated | None |
| 3 | Segmented control | Chạm "Arrive" khi thiếu quyền Vị trí | Mục hiện trạng thái không khả dụng kèm lý do; nút gán bị vô hiệu | Unavailable | None |

**Visual Transition**: chỉ nhãn nút và dấu "đang dùng" crossfade trong 0,2s — danh sách **không** trượt ngang, vì trượt ngang sẽ mất vị trí cuộn.
**Recovery**: nếu quyền được cấp sau, mục Arrive tự mở khoá ở lần vào màn kế tiếp.

---

### SF-007: Chọn preset widget và preview cập nhật tại chỗ

**Parent Screen**: WF-008 · **Source UC**: UC-012
**Trigger**: người dùng chạm một preset trong hàng gợi ý
**Purpose**: thấy kết quả ngay khi chọn, để việc "tạo widget" giống việc chọn hơn là việc dựng

| Step | Component | User Action | System Response | Micro-State | Haptic |
|---|---|---|---|---|---|
| 1 | Hàng preset (Zone C) | Chạm một preset | Preview ở Zone A cập nhật sang preset đó; preset được đánh dấu đang chọn | Selected | Light |
| 2 | Preview (Zone A) | — | Nếu preset thuộc Premium: preview hiển thị **đầy đủ**, nút ở Zone B đổi thành "Mở khoá" | Locked preview | None |
| 3 | Hàng preset | Vuốt ngang | Cuộn qua các preset khác; preset đang chọn vẫn được đánh dấu | Browsing | None |
| 4 | Nút Zone B | Chạm "Lưu widget" | Ghi vào App Group ngay; WF-030 toast | Saved | Medium |

**Visual Transition**: preview crossfade 0,25s giữa hai preset — **không** dùng chuyển động trượt, vì trượt gợi ý "đây là một trang khác" trong khi thực chất chỉ là đổi nội dung.
**Recovery**: ghi App Group thất bại → nêu lỗi + nút thử lại, giữ bản nháp; preview không bị reset.

---

### SF-008: Giảm cấp layout khi phần tử vượt vùng an toàn

**Parent Screen**: WF-008 (và cùng logic ở WF-023) · **Source UC**: UC-013, UC-015
**Trigger**: cấu hình widget hiện tại có phần tử vượt vùng an toàn ở tỉ lệ đang xem
**Purpose**: biến một lỗi tương thích tiềm ẩn (R-11) thành một quyết định hiển thị mà người dùng thấy được **trước khi** ra xe

| Step | Component | User Action | System Response | Micro-State | Haptic |
|---|---|---|---|---|---|
| 1 | Preview | Chọn một tỉ lệ nhỏ hơn | Tính lại layout từ tỉ lệ đó; phát hiện phần tử vượt vùng an toàn | Overflow detected | Light |
| 2 | Phần tử vượt | — | Phần tử đó được viền cảnh báo; hiện tên phần tử và lý do | Highlighted | None |
| 3 | Gợi ý sửa | Chạm "Giảm bớt phần tử này" | Bỏ phần tử ưu tiên thấp nhất; layout tính lại và hết cảnh báo | Resolved | Light |
| 4 | Chữ dài | — | Nếu là chữ: co theo Dynamic Type rồi truncate **có ellipsis**, không cắt giữa chữ | Truncated | None |

**Visual Transition**: viền cảnh báo xuất hiện bằng fade 0,2s (không nhấp nháy — nhấp nháy tạo cảm giác lỗi nghiêm trọng không đúng mức). Phần tử bị bỏ mờ dần rồi layout co lại trong 0,3s.
**Recovery**: hoàn tác được ngay bằng "Thêm lại phần tử"; nếu mọi cách đều không đủ chỗ thì nêu rõ cấu hình này sẽ dùng bản giảm cấp trên xe đó — và **nói trước** thay vì để người dùng phát hiện trên đường.

---

### SF-009: Vuốt qua các tỉ lệ màn hình xe

**Parent Screen**: WF-023 · **Source UC**: UC-013
**Trigger**: người dùng vuốt ngang trong modal preview
**Purpose**: kiểm widget ở nhiều kích thước trong một lần, vì người dùng không biết màn hình xe mình thuộc nhóm nào

| Step | Component | User Action | System Response | Micro-State | Haptic |
|---|---|---|---|---|---|
| 1 | Khung preview | Vuốt ngang | Chuyển sang tỉ lệ kế tiếp; khung đổi kích thước theo đúng tỉ lệ thật | Ratio 2/N | Light (mỗi lần chuyển) |
| 2 | Nhãn Zone D | — | Nhãn nói rõ tỉ lệ này là **kích thước thật của xe bạn** hay **ước lượng tham chiếu** | Labeled | None |
| 3 | Khung preview | {Có phần tử vượt} | Kích hoạt SF-008 tại chỗ | Overflow | Light |
| 4 | Công tắc dark/light | Chạm | Đổi mode; giữ nguyên tỉ lệ đang xem | Mode switched | Light |

**Visual Transition**: khung preview đổi kích thước bằng spring 0,3s (damping cao, không nảy) — người dùng cần thấy **sự khác biệt kích thước**, nên chuyển động phải làm nổi bật đúng chiều đó.
**Recovery**: vuốt về tỉ lệ trước bất kỳ lúc nào; đóng modal không làm mất cấu hình đang thử.

---

### SF-010: Điều chỉnh khung crop với vùng cắt hiện rõ

**Parent Screen**: WF-024 · **Source UC**: UC-014
**Trigger**: người dùng chọn một ảnh từ thư viện
**Purpose**: người dùng biết trước phần nào của ảnh sẽ mất, thay vì phát hiện trên xe

| Step | Component | User Action | System Response | Micro-State | Haptic |
|---|---|---|---|---|---|
| 1 | Ảnh | Ảnh vừa được chọn | Khung crop tự đặt theo tỉ lệ màn hình xe; **vùng sẽ bị cắt được làm tối rõ ràng** | Cropping | Light |
| 2 | Ảnh | Kéo / zoom | Khung giữ nguyên tỉ lệ; vùng tối cập nhật theo tay | Adjusting | None |
| 3 | Ảnh | {Độ phân giải thấp} | Hiện cảnh báo ảnh sẽ mờ trên màn hình xe, kèm mức tối thiểu cần thiết | Low-res warning | None |
| 4 | Nút Xong | Chạm | Nén ảnh dưới ngưỡng widget extension; trả về WF-008/WF-023 | Done | Medium |

**Visual Transition**: vùng cắt tối dần trong 0,2s khi khung xuất hiện; không có animation trong lúc kéo (mọi độ trễ ở đây làm mất cảm giác trực tiếp).
**Recovery**: nút "Đặt lại khung" trả về khung mặc định; cảnh báo mờ **không** chặn việc lưu — người dùng vẫn được quyết định, chỉ là đã được báo trước.

---

### SF-011: Nghe thử giọng chào kèm chữ hiện đồng thời

**Parent Screen**: WF-009 · **Source UC**: UC-020
**Trigger**: người dùng chạm "Nghe thử"
**Purpose**: cho người dùng **bằng chứng kiểm chứng được** rằng giọng chào là thật và sinh theo ngữ cảnh — đối trọng trực tiếp với R-10 và R-13

| Step | Component | User Action | System Response | Micro-State | Haptic |
|---|---|---|---|---|---|
| 1 | Nút "Nghe thử" | Chạm | ContextEngine sinh câu chào từ ngữ cảnh thật lúc này (on-device, không gọi mạng) | Generating | Light |
| 2 | Zone A | — | Chữ câu chào hiện ra **đồng thời** với âm thanh, không hiện trước cũng không hiện sau | Speaking | None |
| 3 | Zone A | — | Nguồn ngữ cảnh đã dùng được ghi nhỏ bên dưới câu chào (giờ / thời tiết / lịch / điểm đến) | Attributed | None |
| 4 | Nút "Nghe thử" | Chạm lần nữa | Sinh câu **khác**; câu cũ mờ đi, câu mới hiện ra | Varied | Light |

**Visual Transition**: chữ hiện theo tiến độ đọc của TTS (không phải typewriter giả); câu cũ mờ 0,2s trước khi câu mới vào.
**Recovery**: nếu TTS không phát được, **vẫn hiện chữ** kèm lý do — nội dung vẫn kiểm chứng được dù âm thanh lỗi.

---

### SF-012: Bật một nguồn ngữ cảnh đang thiếu quyền

**Parent Screen**: WF-009 · **Source UC**: UC-019, UC-004
**Trigger**: người dùng bật toggle của một nguồn mà quyền tương ứng chưa được cấp
**Purpose**: không để tồn tại trạng thái "đã bật nhưng âm thầm không hoạt động" — trạng thái đó làm người dùng tưởng app lỗi

| Step | Component | User Action | System Response | Micro-State | Haptic |
|---|---|---|---|---|---|
| 1 | Toggle nguồn | Bật toggle | Toggle **không** chuyển sang bật; hiện nhãn "cần quyền" kèm nút hành động | Needs permission | Medium |
| 2 | Nút hành động | Chạm "Cho phép" | Mở WF-022 (lần đầu) hoặc dẫn Cài đặt hệ thống (đã từng từ chối) | Requesting | Light |
| 3 | Toggle nguồn | {Quyền được cấp} | Toggle chuyển sang bật; ví dụ câu chào của nguồn đó xuất hiện | Enabled | Light |
| 4 | Toggle nguồn | {Quyền bị từ chối} | Toggle giữ nguyên trạng thái tắt; nhãn nêu rõ cần cấp trong Cài đặt | Blocked | None |

**Visual Transition**: toggle nảy nhẹ về vị trí tắt trong 0,2s — chuyển động này nói "không phải bạn bấm sai, mà điều kiện chưa đủ" rõ hơn bất kỳ dòng chữ nào.
**Recovery**: mọi trạng thái đều có đường đi tiếp; không có tổ hợp nào dẫn tới toggle bật mà không hoạt động.

---

### SF-013: Mở rộng thẻ quyền để đọc lý do

**Parent Screen**: WF-005 · **Source UC**: UC-004
**Trigger**: người dùng chạm "Tìm hiểu thêm" trên một thẻ quyền
**Purpose**: cho người cẩn thận đọc kỹ mà không nhồi toàn bộ nội dung vào màn hình chính của onboarding

| Step | Component | User Action | System Response | Micro-State | Haptic |
|---|---|---|---|---|---|
| 1 | Thẻ quyền | Chạm "Tìm hiểu thêm" | Mở WF-022 dạng sheet với biến thể đúng quyền đó | Expanded | Light |
| 2 | Sheet | Đọc hai ví dụ (có quyền / không có quyền) | — | Reading | None |
| 3 | Sheet | Chạm "Cho phép" hoặc "Không, cảm ơn" | Trả về WF-005; trạng thái thẻ cập nhật | Decided | Light |
| 4 | Sheet | Vuốt xuống để đóng | Trả về WF-005 **không** thay đổi trạng thái quyền | Unchanged | None |

**Visual Transition**: sheet trượt lên 0,35s; thẻ nguồn ở phía sau mờ nhẹ nhưng vẫn thấy được để giữ ngữ cảnh.
**Recovery**: đóng sheet không bao giờ ngầm cấp hay ngầm từ chối quyền — trạng thái chỉ đổi khi người dùng chọn rõ ràng.

---

### SF-014: Tự phát preset đầu tiên khi vào màn chọn âm thanh

**Parent Screen**: WF-004 · **Source UC**: UC-006
**Trigger**: người dùng vào bước 3 của onboarding
**Purpose**: cho người dùng nghe thấy giá trị của app **trong 2 giây đầu**, không cần biết phải bấm vào đâu

| Step | Component | User Action | System Response | Micro-State | Haptic |
|---|---|---|---|---|---|
| 1 | Zone A | Vào màn hình | Preset đầu tiên tự phát **một lần**; dạng sóng chạy ở Zone A | Auto-playing | Light |
| 2 | Danh sách | — | Dòng đang phát được đánh dấu, để người dùng biết tiếng vừa rồi đến từ đâu | Attributed | None |
| 3 | Danh sách | Chạm dòng khác | Chuyển sang SF-003 (nghe thử inline) | Manual | Light |
| 4 | Zone A | {Đang có nhạc phát} | Áp dụng ducking thật rồi phục hồi — bản nghe thử phản ánh đúng trải nghiệm trên xe | Ducked | None |

**Visual Transition**: dạng sóng hiện ra bằng fade 0,2s ngay khi âm thanh bắt đầu, không sớm hơn.
**Recovery**: nếu không phát được (phiên audio bị chiếm), **không** tự phát lại và không báo lỗi ồn ào — chỉ hiện một dòng gợi ý chạm để nghe, và nút "Tiếp tục" vẫn hoạt động.

---

### SF-015: So sánh bậc giá bằng bảng mở rộng

**Parent Screen**: WF-010 · **Source UC**: UC-025
**Trigger**: người dùng chạm "So sánh các gói"
**Purpose**: cho người dùng tự so sánh thay vì phải tin vào một bậc được nhấn mạnh

| Step | Component | User Action | System Response | Micro-State | Haptic |
|---|---|---|---|---|---|
| 1 | Zone C | Chạm "So sánh các gói" | Bảng Free ↔ Premium mở rộng inline | Expanded | Light |
| 2 | Bảng | Cuộn ngang/dọc | Hàng tính năng của bậc đang chọn được nhấn nhẹ | Comparing | None |
| 3 | Bảng | Chạm một bậc trong bảng | Chọn bậc đó; đồng bộ với thẻ giá ở Zone B | Selected | Light |
| 4 | Zone C | Chạm "Thu gọn" | Bảng thu lại; lựa chọn được giữ | Collapsed | Light |

**Visual Transition**: mở rộng bằng spring 0,3s damping cao; chiều cao thay đổi mượt, không nhảy nội dung phía dưới.
**Recovery**: mọi trạng thái mở/thu đều giữ nguyên bậc đang chọn; đóng paywall không mất lựa chọn nếu người dùng mở lại trong cùng phiên.

---

### SF-016: Mở rộng một dòng lịch sử kết nối

**Parent Screen**: WF-014 · **Source UC**: UC-017
**Trigger**: người dùng chạm một dòng trong danh sách các lần kết nối gần nhất
**Purpose**: cho người dùng (và QA) xem chi tiết kỹ thuật của đúng một lần kết nối, mà không biến màn hình thành một bảng log dày đặc

| Step | Component | User Action | System Response | Micro-State | Haptic |
|---|---|---|---|---|---|
| 1 | Dòng lịch sử | Chạm dòng | Mở rộng inline: kích thước scene, phiên bản iOS, widget type, `failure_reason` | Expanded | Light |
| 2 | Dòng mở rộng | — | `failure_reason` nêu rõ **vượt-bounds** hay **hết-bộ-nhớ** — hai nguyên nhân khác nhau, không gộp | Detailed | None |
| 3 | Dòng mở rộng | Chạm "Xem widget ở kích thước này" | Mở WF-023 với đúng kích thước của lần kết nối đó | Navigating | Light |
| 4 | Dòng mở rộng | Chạm dòng khác | Dòng cũ thu lại; chỉ một dòng mở tại một thời điểm | Switched | Light |

**Visual Transition**: mở rộng 0,25s; dòng khác thu lại đồng thời để chiều cao tổng không nhảy.
**Recovery**: sao chép được nội dung dòng mở rộng để gửi qua kênh khác nếu WF-028 không gửi được.

---

### SF-017: Thẻ dashboard sắp xếp lại khi ngữ cảnh đổi 🚗

**Parent Screen**: WF-016 · **Source UC**: UC-022
**Trigger**: ContextEngine xác định thứ tự thẻ mới trong lúc phiên đang chạy
**Purpose**: cập nhật thứ tự ưu tiên mà **không** tạo ra chuyển động thu hút mắt người lái

| Step | Component | User Action | System Response | Micro-State | Haptic |
|---|---|---|---|---|---|
| 1 | Các thẻ | *Không làm gì — đang lái* | ContextEngine tính thứ tự mới | Recomputing | None |
| 2 | Các thẻ | — | Thứ tự cập nhật bằng **crossfade tại chỗ**, không dùng chuyển động vị trí | Reordered | None |
| 3 | Các thẻ | — | Nếu thẻ đang được chạm: **hoãn** việc sắp xếp lại tới khi hành động kết thúc | Deferred | None |
| 4 | Các thẻ | — | Không sắp xếp lại quá 1 lần mỗi 30 giây trong cùng một phiên | Throttled | None |

**Visual Transition**: crossfade 0,4s — **cố ý chậm** và không có chuyển động vị trí. Đây là quyết định an toàn: thẻ trượt qua nhau trên màn hình xe sẽ kéo mắt người lái khỏi đường.
**Recovery**: nếu ContextEngine không có kết luận chắc chắn, **giữ nguyên thứ tự hiện tại** — thà thứ tự cũ còn hơn một thay đổi gây phân tán không có lý do rõ.

---

### SF-018: Chuyển preset trước/sau không đóng sheet

**Parent Screen**: WF-020 · **Source UC**: UC-006
**Trigger**: người dùng chạm mũi tên trước/sau trong sheet nghe thử
**Purpose**: so sánh hai preset cạnh nhau mà không phải đóng sheet, cuộn danh sách, mở lại

| Step | Component | User Action | System Response | Micro-State | Haptic |
|---|---|---|---|---|---|
| 1 | Mũi tên "sau" | Chạm | Preset kế tiếp trong cùng nhóm được nạp và tự phát | Next | Light |
| 2 | Zone A | — | Tên preset và dạng sóng cập nhật; mức âm lượng đang đặt **được giữ nguyên** | Playing | None |
| 3 | Nút Zone B | Chạm "Dùng sound này" | Gán preset đang nghe; sheet đóng; WF-030 toast | Applied | Medium |
| 4 | Mũi tên | {Hết nhóm} | Mũi tên bị vô hiệu thay vì cuộn vòng — cuộn vòng làm người dùng mất phương hướng | Boundary | None |

**Visual Transition**: tên preset crossfade 0,2s; dạng sóng reset về đầu ngay khi audio mới bắt đầu.
**Recovery**: nếu preset kế tiếp không phát được, giữ preset cũ và nêu lý do — không để sheet ở trạng thái trống.

---

### SF-019: Mở rộng danh sách tính năng của gói hiện tại

**Parent Screen**: WF-025 · **Source UC**: UC-029
**Trigger**: người dùng chạm "Xem tính năng đang có"
**Purpose**: trước khi huỷ, cho người dùng thấy chính xác họ sẽ mất gì — trình bày trung thực, không phải chiêu níu giữ

| Step | Component | User Action | System Response | Micro-State | Haptic |
|---|---|---|---|---|---|
| 1 | Zone C | Chạm "Xem tính năng đang có" | Danh sách tính năng của gói hiện tại mở rộng inline | Expanded | Light |
| 2 | Danh sách | — | Tính năng nào **vẫn còn** ở gói Free được đánh dấu rõ, để người dùng biết không mất hết | Annotated | None |
| 3 | Zone B | Chạm "Huỷ đăng ký" | Mở WF-027; nội dung alert nêu ngày quyền kết thúc | Confirming | Medium |
| 4 | Zone C | Chạm "Thu gọn" | Danh sách thu lại | Collapsed | Light |

**Visual Transition**: mở rộng 0,25s. **Không** có animation nào làm chậm đường đi tới nút huỷ — làm chậm đường huỷ là dark pattern.
**Recovery**: mở rộng hay thu gọn không ảnh hưởng gì tới trạng thái đăng ký.

---

### SF-020: Mở rộng để xem giá trị thật từng trường dữ liệu

**Parent Screen**: WF-028 · **Source UC**: UC-017
**Trigger**: người dùng chạm một mục trong danh sách dữ liệu sẽ gửi
**Purpose**: biến câu "chúng tôi không thu PII" từ một lời hứa thành một thứ người dùng tự kiểm tra được

| Step | Component | User Action | System Response | Micro-State | Haptic |
|---|---|---|---|---|---|
| 1 | Mục dữ liệu | Chạm mục | Mở rộng hiện **giá trị thật** sẽ được gửi (ví dụ: `screen_width: 1280`) | Expanded | Light |
| 2 | Mục dữ liệu | Bỏ tick một mục | Mục đó bị loại khỏi payload; danh sách cập nhật | Excluded | Light |
| 3 | Nút Gửi | Chạm | Gửi đúng những mục còn được tick; xác nhận ≤ 500ms | Sent | Medium |
| 4 | Nút sao chép | Chạm | Copy toàn bộ payload dạng chữ vào clipboard | Copied | Light |

**Visual Transition**: mở rộng 0,2s; giá trị hiện dạng chữ đơn sắc để đọc rõ là dữ liệu kỹ thuật, không phải nội dung marketing.
**Recovery**: bỏ tick hết mọi mục → nút Gửi bị vô hiệu kèm lời nhắc cần ít nhất kích thước màn hình để chẩn đoán được.

---

### SF-021: Đổi theme và xem kết quả tức thì

**Parent Screen**: WF-012 · **Source UC**: UC-036, UC-009, UC-031
**Trigger**: người dùng chọn theme khác trong Cài Đặt Chung
**Purpose**: đổi theme phải thấy ngay trên toàn app, vì widget CarPlay cũng đổi theo và người dùng cần biết trước khi ra xe

| Step | Component | User Action | System Response | Micro-State | Haptic |
|---|---|---|---|---|---|
| 1 | Bộ chọn theme | Chạm một theme | Toàn app đổi màu ngay; không cần khởi động lại | Applied | Light |
| 2 | Preview widget nhỏ | — | Preview widget trong Zone C cập nhật theo theme để thấy hiệu ứng trên màn hình xe | Previewed | None |
| 3 | Bộ chọn theme | Chọn "Theo hệ thống" | Theo cài đặt sáng/tối của iOS; đổi theo hệ thống về sau | System-driven | Light |

**Visual Transition**: crossfade toàn màn hình 0,25s — không dùng chuyển động, vì chuyển động khi đổi màu gây cảm giác giật.
**Recovery**: theme không áp được cho một thành phần → thành phần đó dùng theme hệ thống thay vì hiện màu sai.

---

### Kiểm tra phủ Sub-Flow

| Yêu cầu | Kết quả |
|---|---|
| Số sub-flow | **21** (ngưỡng Medium: 10–20; vượt 1 vì WF-012 là màn Dense cần ≥ 2 sub-flow) |
| Màn Dense có ≥ 2 sub-flow | WF-006 → SF-001, SF-005 · WF-007 → SF-003, SF-006 · WF-008 → SF-007, SF-008 · WF-012 → SF-004, SF-021 ⇒ **4/4 Pass** |
| Màn Medium có ≥ 1 sub-flow | WF-003 → SF-002 · WF-004 → SF-014 · WF-005 → SF-013 · WF-009 → SF-011, SF-012 · WF-010 → SF-015 · WF-014 → SF-016 · WF-016 → SF-017 · WF-020 → SF-018 · WF-023 → SF-009 · WF-024 → SF-010 · WF-025 → SF-019 · WF-028 → SF-020 ⇒ **12/12 Pass** |
| Màn Light | Không yêu cầu sub-flow; WF-001, WF-002, WF-011, WF-013, WF-015, WF-017, WF-018, WF-019, WF-021, WF-022, WF-026, WF-027, WF-029, WF-030 — cố ý không có, vì mỗi màn chỉ có một việc |
| Sub-flow trên bề mặt CarPlay | Chỉ **1** (SF-017), và dùng crossfade chậm không có chuyển động vị trí — quyết định an toàn, không phải thiếu sót |

---

## 6. Scenarios

18 scenario: 7 happy path · 8 edge case · 3 theo persona (ngưỡng Medium: 15–25 ⇒ Pass).

### 6.1 Happy Path Scenarios

#### Scenario 1: [UC-001] Thiết lập lần đầu thành công

**Actor**: người dùng mới (Alex) · **Goal**: setup xong dưới 2 phút và hiểu app làm được gì

**Steps**:
1. Mở app; WF-001 hiện 1,2s rồi vào WF-002.
2. Đọc một câu giới thiệu, chạm "Bắt đầu".
3. WF-003: chọn Toyota → Camry → 2022; ảnh xe hiện ra; chạm "Đúng xe của tôi".
4. WF-004: preset đầu tiên tự phát; nghe thêm 2 preset; chạm "Dùng sound này".
5. WF-005: đọc lý do quyền Vị trí và Lịch; cấp cả hai.
6. Chạm "Tiếp tục"; hệ thống ghi `onboarding_completed`.

**Expected Outcome**: xe đã chọn, sound Connect đã gán, hai quyền đã cấp, người dùng ở WF-006 với 1 widget sẵn dùng ở gói Free. Tổng thời gian ~90 giây. **Không gặp paywall lần nào.**

---

#### Scenario 2: [UC-010] Âm thanh lên xe phát đúng, không bị nhạc lấn

**Actor**: chủ xe đang phát Spotify khi lên xe · **Goal**: nghe được âm thanh chào của mình rõ ràng

**Steps**:
1. Cắm iPhone vào CarPlay; hệ thống nhận `carplay_connected`.
2. Phát hiện có audio đang phát; giảm nguồn đó xuống 20%.
3. Sound Connect phát qua **loa xe** ở giây thứ 1,1.
4. Sound kết thúc; âm lượng Spotify phục hồi về đúng mức trước đó.
5. Ghi `sound_played` (`music_was_playing: true`, `output_route: car_speaker`) và `sound_ducking_applied`.

**Expected Outcome**: nghe rõ sound chào, nhạc trở lại bình thường không lệch âm lượng. Đây là complaint "gets cancelled out if you have any music playing" của đối thủ đã được giải quyết và đo được.

---

#### Scenario 3: [UC-015] Widget render đúng trên một màn hình xe chưa từng gặp

**Actor**: chủ xe có màn hình CarPlay tỉ lệ không chuẩn · **Goal**: widget hiện đúng và đầy đủ

**Steps**:
1. Kết nối CarPlay; scene active; đọc bounds được 1180×420.
2. `WidgetRenderService` tính toàn bộ layout từ hai giá trị đó.
3. Widget render: ảnh xe, chữ co theo Dynamic Type, counter đặt trong vùng an toàn.
4. Kiểm tra không có phần tử nào vượt bounds.
5. Ghi `widget_render_ok` kèm `screen_width: 1180`, `screen_height: 420`.
6. Kích thước này được lưu để WF-023 dùng làm tỉ lệ preview mặc định về sau.

**Expected Outcome**: widget đúng dù kích thước này không có trong bất kỳ danh sách nào — vì layout tính tại runtime, không tra bảng.

---

#### Scenario 4: [UC-021] Giọng chào cá nhân hóa phát đúng ngữ cảnh

**Actor**: người dùng Premium đã dùng 2 tuần · **Goal**: nghe câu chào phù hợp hoàn cảnh

**Steps**:
1. 7:40 sáng thứ Ba, lên xe; `carplay_connected`.
2. ContextEngine đọc: giờ (sáng), thời tiết (mưa), lịch (họp 8:30 tại văn phòng), tuyến quen (đi làm).
3. Chọn biến thể ghép ngữ cảnh mưa + cuộc họp; kiểm tra khác câu lần trước.
4. Phát qua loa xe ở giây thứ 1,8 sau sound Connect.
5. Ghi `voice_greeting_played` kèm `context_used: [time, weather, calendar]`.

**Expected Outcome**: câu chào cụ thể theo hoàn cảnh thật, sinh hoàn toàn on-device, **không có lệnh gọi mạng nào**, và không lặp lại câu của lần trước.

---

#### Scenario 5: [UC-012] Tạo widget đầu tiên trong 4 chạm

**Actor**: người dùng vừa onboard xong · **Goal**: có widget đẹp mà không phải học công cụ

**Steps**:
1. WF-006: chạm thẻ widget → WF-008.
2. WF-008 hiện 4 preset gợi ý theo Toyota Camry 2022 đã chọn.
3. Chạm preset thứ hai; preview ở Zone A cập nhật (SF-007).
4. Chạm "Xem trước trên xe của tôi" → WF-023; vuốt qua 4 tỉ lệ tham chiếu, không có cảnh báo vượt vùng an toàn.
5. Chạm "Dùng bản này" → "Lưu widget"; cấu hình ghi vào App Group; WF-030 toast.

**Expected Outcome**: có widget sẵn dùng sau 4 chạm, chưa hề gặp canvas rỗng, và ghi `free_tier_widget_used`.

---

#### Scenario 6: [UC-024 → UC-027] Từ Free đến trial sau khi đã tin app

**Actor**: người dùng đã dùng gói Free 12 ngày · **Goal**: mở khoá thêm widget và giọng chào

**Steps**:
1. 12 ngày dùng Free: widget chạy tốt mọi chuyến, không quảng cáo, không bị nhắc nâng cấp.
2. Muốn thêm widget thứ hai; chạm "Thêm widget" trên WF-008 → WF-010 (`days_since_install: 12`).
3. WF-010 hiện 4 lựa chọn; giá bằng tiền tệ địa phương; **không có bậc weekly**.
4. Chọn $29,99/năm → WF-011: giá cuối, ngày hết trial, ngày trừ tiền.
5. Chạm "Xác nhận"; ghi `price_confirmed`; hoàn tất thanh toán; ghi `trial_started`.
6. WF-006 hiện badge "Trial còn 7 ngày" kèm ngày trừ tiền.

**Expected Outcome**: nâng cấp là quyết định của người dùng sau khi **đã tự xác nhận app chạy trên xe mình** — đây là cơ chế giảm refund (R-04) và giảm 1★ (R-11) hoạt động đúng thiết kế.

---

#### Scenario 7: [UC-022, UC-023] Dashboard đoán đúng và một chạm là xong

**Actor**: người dùng đã dùng 3 tuần · **Goal**: làm việc mình cần với ít thao tác nhất

**Steps**:
1. 18:10 thứ Sáu, lên xe; dashboard đã học được thói quen.
2. Thẻ "Về nhà" ở Zone A (vị trí lớn nhất); thẻ playlist buổi chiều ở Zone B.
3. Nhìn một lượt ~1 giây; chạm thẻ "Về nhà".
4. Apple Maps mở với tuyến về nhà trong 0,8s; ghi `ai_recommendation_tapped`.

**Expected Outcome**: một lần nhìn, một lần chạm. Đây là trạng thái mà KPI tap-through ≥ 30% được đo.

---

### 6.2 Edge Case Scenarios

#### Scenario 8: [AF-015.1 → AF-016] Widget vượt bounds trên xe của người dùng

**Actor**: chủ xe Jeep Wrangler 2022 (màn 8") · **Context**: widget có 4 lớp thông tin, màn hình xe nhỏ hơn mọi tỉ lệ đã thử

**Steps**:
1. Kết nối CarPlay; bounds đọc được nhỏ hơn dự kiến.
2. Layout phát hiện counter vượt vùng an toàn → **giảm cấp**: bỏ counter, co chữ theo Dynamic Type, truncate có ellipsis.
3. Render lại: lần này vừa khít → ghi `widget_render_ok` kèm cờ đã giảm cấp.
4. *(Nhánh xấu hơn)* nếu vẫn không vừa → WF-019 hiện thông báo: **vấn đề tương thích màn hình xe này**, kèm hướng dẫn mở màn Chẩn Đoán trên iPhone.
5. Ghi `widget_render_failed` với `failure_reason: overflow`; WF-016 Dashboard **vẫn hoạt động đầy đủ**.
6. Mở app iPhone sau chuyến: WF-006 hiện dòng cảnh báo → WF-014 → gửi báo cáo qua WF-028.

**Expected Outcome**: **không có màn hình trắng ở bất kỳ nhánh nào**; lỗi để lại đủ dữ liệu để phát hiện xe không tương thích trong 24h; và người dùng có kênh sửa thay vì chỉ còn cách để 1★.

---

#### Scenario 9: [AF-010.1] Đang có cuộc gọi lúc lên xe

**Actor**: Jordan đang trong conference call khi lên xe · **Context**: sound Connect sẽ chèn vào cuộc gọi nếu không xử lý

**Steps**:
1. `carplay_connected` xảy ra trong lúc cuộc gọi đang diễn ra.
2. Hệ thống phát hiện phiên audio thuộc cuộc gọi.
3. **Bỏ hẳn lượt phát** sound Connect; không ducking, không chèn tiếng.
4. Không phát bù sau khi cuộc gọi kết thúc.
5. Giọng chào cũng bị bỏ theo (AF-021.2).

**Expected Outcome**: cuộc gọi không bị làm gián đoạn; app im lặng đúng lúc cần im lặng — và **không** cố bù lại sau, vì phát một câu chào giữa chuyến đi còn tệ hơn không phát.

---

#### Scenario 10: [AF-011.1] Phiên audio bị thu hồi trước khi kịp phát sound xuống xe

**Actor**: chủ xe tắt máy rất nhanh sau khi đỗ · **Context**: hệ thống thu hồi phiên audio trước khi sound disconnect phát được

**Steps**:
1. Người dùng tắt máy; tín hiệu ngắt kết nối CarPlay tới.
2. Hệ thống bắt đầu phát sound Disconnect nhưng phiên audio đã bị thu hồi.
3. **Bỏ lượt phát**; ghi `sound_played` với trạng thái thất bại kèm lý do.
4. **Tuyệt đối không** phát bù qua loa iPhone.

**Expected Outcome**: người dùng không nghe một tiếng lạ phát ra từ túi mình — đây chính là complaint "you only hear the sound through your phone" của đối thủ, và cách xử lý đúng là **im lặng**, không phải chuyển tuyến đầu ra.

---

#### Scenario 11: [AF-002.1, AF-003.1] Xe không có trong thư viện và đang không có mạng

**Actor**: chủ xe VinFast VF8 ở vùng không có sóng · **Context**: model không có trong thư viện, và không gửi được request

**Steps**:
1. WF-003: tìm "VinFast" không có kết quả.
2. Chạm "Không tìm thấy xe của tôi" → WF-021 với phần đã gõ được điền sẵn.
3. Điền model và năm, chạm "Gửi".
4. Không có mạng → request **xếp hàng on-device**; WF-030 toast xác nhận đã ghi nhận trong 300ms.
5. Quay về WF-003, chọn phân khúc "SUV" → dùng ảnh silhouette.
6. Tiếp tục onboarding bình thường; request được gửi tự động khi có mạng.

**Expected Outcome**: luồng **không bị chặn** ở bất kỳ điểm nào; người dùng vẫn hoàn tất setup và có widget dùng được, dù thư viện thiếu xe của họ và dù không có mạng.

---

#### Scenario 12: [AF-025.3] StoreKit không trả về giá

**Actor**: người dùng muốn nâng cấp · **Context**: StoreKit lỗi hoặc mạng chập chờn

**Steps**:
1. Chạm tính năng khoá → WF-010 mở.
2. Zone B hiện trạng thái đang tải giá.
3. Sau timeout, StoreKit không trả về dữ liệu.
4. Hiện thông báo lỗi rõ ràng kèm nút thử lại.
5. **Không** hiện giá cache, **không** hiện giá hardcode, **không** cho đi tiếp tới WF-011.

**Expected Outcome**: người dùng không bao giờ thấy một con số có thể sai. Hiện giá cache ở đây chính là cách sinh ra cáo buộc bait-and-switch (R-12) — nên trạng thái đúng là báo lỗi, không phải đoán.

---

#### Scenario 13: [AF-004.2, UC-005] Từ chối toàn bộ quyền và vẫn dùng app bình thường

**Actor**: người dùng rất quan tâm quyền riêng tư · **Context**: không cấp Vị trí, không cấp Lịch

**Steps**:
1. WF-005: chạm "Bỏ qua tất cả"; hoàn tất onboarding trong ~40 giây.
2. WF-006 hiện đầy đủ trạng thái + **một** dòng mời cấp quyền dạng tĩnh (không popup).
3. Cắm xe: widget render bình thường; sound Connect phát bình thường.
4. Giọng chào phát ở biến thể **chỉ theo giờ**, không im lặng và không báo lỗi.
5. Dashboard dùng thứ tự mặc định, không có thẻ gợi ý điểm đến.
6. Sound Arrive hiện trạng thái không khả dụng kèm lý do — không để người dùng chờ một âm thanh không bao giờ phát.

**Expected Outcome**: app dùng được thật, không phải "dùng được trên giấy". Với một niche mà rating trung bình 2,2/5, đây là tín hiệu tin cậy có giá trị hơn bất kỳ câu quảng cáo nào.

---

#### Scenario 14: [AF-012.4] Người dùng ở iOS 17.3 — chưa có widget CarPlay

**Actor**: chủ xe chưa nâng cấp iOS · **Context**: app chạy được (min 16.4) nhưng widget CarPlay cần 17.4+

**Steps**:
1. Hoàn tất onboarding bình thường.
2. WF-008: nêu rõ **widget CarPlay yêu cầu iOS 17.4+**, và **vẫn cho cấu hình** để sẵn sàng khi nâng cấp.
3. Cắm xe: sound Connect phát, giọng chào phát, WF-016 Dashboard hoạt động.
4. Vùng widget hiện thông báo yêu cầu phiên bản iOS — **không** crash, **không** màn trắng.
5. Sau khi người dùng nâng cấp iOS, widget đã cấu hình sẵn render ngay ở lần cắm kế tiếp.

**Expected Outcome**: hai ngưỡng iOS (16.4 app / 17.4 widget) được xử lý bằng giảm cấp có thông báo, không phải bằng crash và không phải bằng cách nói dối rằng widget đang chạy.

---

#### Scenario 15: [AF-033.3] Không mời đánh giá sau khi vừa gặp lỗi

**Actor**: người dùng vừa gặp lỗi render 3 ngày trước · **Context**: đủ điều kiện "chuỗi tích cực" nhưng vẫn còn lỗi trong 7 ngày gần nhất

**Steps**:
1. Sound đã phát thành công 6 lần liên tiếp; điều kiện chuỗi tích cực được thoả.
2. Hệ thống kiểm thêm: có `widget_render_failed` cách đây 3 ngày.
3. **Chặn** lời mời đánh giá (AC-033.2).
4. Thay vào đó, WF-006 vẫn giữ lối vào WF-014 để người dùng xử lý vấn đề nếu muốn.
5. Sau 7 ngày không có lỗi mới, lời mời được phép hiện.

**Expected Outcome**: app không tự đưa mình vào tình huống bị đánh 1★. Đây là cơ chế trực tiếp bảo vệ KPI **Recent 1★ Ratio < 15%** — và nó hoạt động bằng cách **không** làm gì ở đúng thời điểm.

---

### 6.3 Persona-Based Scenarios

#### Scenario 16: Alex — Tech-Savvy Commuter: chuyến đi làm buổi sáng

**Actor**: Alex, 32, iPhone 14 Pro, BMW, 40 phút đi làm mỗi ngày
**Goal**: lên xe là mọi thứ đã sẵn sàng, không phải chạm quá một lần

**Steps**:
1. 7:35, mở cửa xe, cắm iPhone (UC-010).
2. Sound Connect phát ở giây 1,1 qua loa xe; nhạc đang phát được duck rồi phục hồi.
3. Giọng chào ghép ngữ cảnh mưa + cuộc họp 8:30 phát ở giây 1,8 (UC-021).
4. Dashboard đã học: thẻ playlist buổi sáng ở Zone A, thẻ "Tới văn phòng" ở Zone B (UC-022).
5. Chạm thẻ playlist; nhạc phát trong 0,7s (UC-023).
6. Lái đi; không mở app iPhone lần nào trong cả chuyến.

**Expected Outcome**: Alex đạt được mục tiêu gốc ở PRD §3 — 30 giây tìm nhạc mỗi sáng trở thành một lần chạm. Toàn bộ hành trình này **không có bước nào diễn ra trên iPhone**, và đó là điểm chính.

---

#### Scenario 17: Jordan — Busy Professional: lái xe trong lúc họp

**Actor**: Jordan, 38, iPhone 13, Audi 2022, lái 10+ giờ/tuần trên tuyến lạ
**Goal**: dùng được app mà không cần nói ra tiếng và không bị làm gián đoạn cuộc họp

**Steps**:
1. Đang trong conference call khi lên xe; `carplay_connected`.
2. Hệ thống phát hiện cuộc gọi → **bỏ cả sound và giọng chào** (Scenario 9).
3. Widget render bình thường trên màn hình Audi — kích thước này nằm trong test matrix R-11.
4. Dashboard hiện thẻ dẫn đường tới địa chỉ trong lịch; Jordan chạm **một lần**, không nói gì.
5. Apple Maps mở; cuộc họp không bị ảnh hưởng.
6. *(Ở MVP 2)* thẻ liên hệ cho phép gọi client bằng một chạm (UC-034).

**Expected Outcome**: mọi tính năng cốt lõi dùng được **hoàn toàn bằng chạm**, không phụ thuộc voice input. Đây là lý do UC-034 được dời sang MVP 2 chứ không bị loại — Jordan có nhu cầu thật, chỉ là nó nằm ngoài ba trụ PMF đã kiểm chứng.

---

#### Scenario 18: Sam — Car Enthusiast: dựng widget theo ý mình cuối tuần

**Actor**: Sam, 28, iPhone 15 Pro Max, Porsche, chuyến dài cuối tuần
**Goal**: dashboard trông đúng là xe của mình, và trả tiền một lần thay vì thuê cả đời

**Steps**:
1. Chủ Nhật ở nhà: mở WF-008, chọn loại widget "ảnh cá nhân".
2. WF-024: chọn ảnh Porsche vừa chụp; khung crop tự đặt theo tỉ lệ màn hình xe; vùng sẽ bị cắt hiện rõ (SF-010).
3. Cảnh báo độ phân giải không xuất hiện — ảnh từ iPhone 15 Pro Max đủ nét.
4. WF-023: vuốt qua các tỉ lệ, kiểm cả dark và light mode (SF-009).
5. Ảnh cá nhân thuộc Premium → nút chuyển thành "Mở khoá" → WF-010.
6. Chọn bậc **Lifetime $49,99**; WF-011 nêu rõ giao dịch một lần, **không có ngày gia hạn** (UC-030).
7. Xác nhận; widget lưu; chuyến đi cuối tuần có widget ảnh xe thật của Sam.

**Expected Outcome**: Sam có được thứ mình muốn và trả theo cách mình muốn. Bậc Lifetime tồn tại chính vì yêu cầu trực tiếp từ dữ liệu review: *"I would be willing to buy this app outright, but I'm not going to pay for the rest of my life"*. Nhu cầu trip history & stats của Sam nằm ở MVP 3 — và lược đồ SQLite đã chừa sẵn từ MVP 1 để không phải đập đi làm lại.

---

## 7. Use Case Priorities

### 7.1 Must-Have (MVP)

34 UC thuộc phạm vi thi công **MVP 1**. Cột Priority phân biệt hai mức trong cùng phạm vi: **High** là điều kiện chặn phát hành; **Medium** vẫn trong phạm vi MVP 1 nhưng là nhóm được xem xét trước nhất nếu phải cắt — và mọi lần cắt phải được ghi vào **Scope Decision Record** của `Project_Implementation_Roadmap.md`, không được cắt im lặng.

| ID | Use Case | Priority | Complexity | Primary Screen |
|---|---|---|---|---|
| UC-001 | Hoàn tất onboarding trong 5 bước | High | Medium | WF-002 |
| UC-002 | Chọn xe của mình | High | Low | WF-003 |
| UC-003 | Báo xe không có trong thư viện | Medium | Low | WF-021 |
| UC-004 | Cấp quyền sau khi hiểu rõ lý do | High | Medium | WF-005 |
| UC-005 | Dùng app dù đã từ chối mọi quyền | High | Medium | WF-006 |
| UC-006 | Nghe thử âm thanh trước khi chọn | High | Low | WF-007 |
| UC-007 | Gán âm thanh cho sự kiện Connect | High | Low | WF-007 |
| UC-008 | Gán âm thanh cho Disconnect và Arrive | Medium | Medium | WF-007 |
| UC-009 | Điều chỉnh âm lượng sound độc lập | High | Medium | WF-012 |
| UC-010 | Nghe sound khi lên xe không bị nhạc lấn | High | **High** | WF-016 |
| UC-011 | Nghe sound xuống xe đúng lúc tắt máy | High | **High** | WF-016 |
| UC-012 | Tạo widget đầu tiên | High | Medium | WF-008 |
| UC-013 | Xem trước widget theo tỉ lệ màn hình xe | High | **High** | WF-023 |
| UC-014 | Chọn ảnh xe hoặc ảnh cá nhân | Medium | Medium | WF-024 |
| UC-015 | Xem widget hoạt động trên màn hình xe | High | **High** | WF-017 |
| UC-016 | Phục hồi khi widget không render được | High | Medium | WF-019 |
| UC-017 | Chẩn đoán tương thích và gửi báo cáo | Medium | Medium | WF-014 |
| UC-018 | Bật hoặc tắt hoàn toàn giọng chào | High | Low | WF-009 |
| UC-019 | Chọn nguồn ngữ cảnh cho giọng chào | Medium | Medium | WF-009 |
| UC-020 | Nghe thử giọng chào trước khi lên xe | High | Medium | WF-009 |
| UC-021 | Nghe giọng chào cá nhân hóa khi lên xe | High | **High** | WF-016 |
| UC-022 | Xem dashboard tự sắp xếp theo ngữ cảnh | High | **High** | WF-016 |
| UC-023 | Chạm thẻ gợi ý trên dashboard | High | Medium | WF-016 |
| UC-024 | Dùng gói Free để tự xác nhận app chạy | High | Medium | WF-006 |
| UC-025 | Xem bảng giá minh bạch | High | Medium | WF-010 |
| UC-026 | Xác nhận giá cuối trước khi trả tiền | High | Medium | WF-011 |
| UC-027 | Bắt đầu trial 7 ngày | High | Medium | WF-011 |
| UC-028 | Nhận nhắc trước khi hết trial | Medium | Low | WF-013 |
| UC-029 | Quản lý hoặc huỷ đăng ký | Medium | Low | WF-025 |
| UC-030 | Mua gói Lifetime một lần | Medium | Medium | WF-011 |
| UC-031 | Đổi ngôn ngữ app | Medium | Medium | WF-026 |
| UC-032 | Xoá toàn bộ dữ liệu on-device | Medium | Low | WF-012 |
| UC-033 | Gửi đánh giá hoặc phản hồi | Medium | Low | WF-030 |
| UC-036 | Đổi theme của app | Medium | Low | WF-012 |

> **Bốn UC không được cắt trong mọi trường hợp**, dù chúng không phải là tính năng "bán được": **UC-005** (dùng được khi từ chối quyền), **UC-016** (fallback khi render lỗi), **UC-017** (chẩn đoán), **UC-024** (gói Free). Cả bốn là cơ chế giảm thiểu rủi ro R-11, R-04 và R-12 — cắt chúng đi là bỏ luôn lớp phòng vệ, không phải tiết kiệm phạm vi.

### 7.2 Should-Have (Post-MVP)

| ID | Use Case | Priority | Complexity | Primary Screen |
|---|---|---|---|---|
| UC-034 | Gọi nhanh liên hệ từ màn hình xe *(MVP 2 — tháng 12/2026)* | Medium | Medium | WF-016 |

**Các tính năng MVP 2 khác chưa được phân rã thành UC**: widget tương tác hai chiều · Coin IAP · remote config · Settings mở rộng (dark mode, cỡ chữ) · localize DE/FR/IT · Android Auto. Chúng đã được liệt kê ở `Project_Overview.md` §4.2 và sẽ được cấp UC-ID mới tiếp theo dãy hiện tại **khi lên kế hoạch MVP 2**. Không cấp ID trước, vì ID đã cấp thì không được đổi và một UC chưa có luồng cụ thể sẽ thành ID mồ côi.

### 7.3 Nice-to-Have (Future)

| ID | Use Case | Priority | Complexity | Primary Screen |
|---|---|---|---|---|
| UC-035 | Đồng bộ cấu hình qua cloud *(MVP 3 — tháng 3/2027, optional + opt-in)* | Low | **High** | WF-015 |

**Các hướng xa hơn chưa phân rã thành UC** (`Project_Overview.md` §4.3): trip history & stats (MVP 3) · thư viện xe mở rộng trim/color (MVP 3) · AI nhận biết lịch nâng cao (MVP 4) · voice input (MVP 4) · music source detection (MVP 4). **AI Driving Coach** vẫn là **giả thuyết chưa validate** (PRD §14) — số liệu category cho thấy phiên trung bình ~23 giây, trái với giả định người dùng xem lại điểm lái xe sau mỗi chuyến; phải prototype hành vi trước khi cấp UC.

---

## 8. User Journey Map

Năm hành trình dưới đây: ba theo persona của PRD §3, một theo vòng đời chuyển đổi (ngày 0 → ngày 12), một theo đường phục hồi khi gặp lỗi. Mỗi ô ghi UC-ID và WF-ID để `UX_Flows.md` ở Step 6 dùng trực tiếp.

```
HÀNH TRÌNH 1 — Alex (Tech-Savvy Commuter): chuyến đi làm buổi sáng, không chạm iPhone
┌──────────────┐   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│  Lên xe      │──▶│ Sound Connect│──▶│ Giọng chào   │──▶│ Dashboard đã │──▶│ 1 chạm →     │
│  cắm CarPlay │   │ duck nhạc    │   │ theo ngữ cảnh│   │ học thói quen│   │ nhạc phát    │
│  (UC-015)    │   │  (UC-010)    │   │  (UC-021)    │   │  (UC-022)    │   │  (UC-023)    │
│  WF-017 🚗   │   │  WF-016 🚗   │   │  WF-016 🚗   │   │  WF-016 🚗   │   │  WF-016 🚗   │
└──────────────┘   └──────────────┘   └──────────────┘   └──────────────┘   └──────┬───────┘
        ▲                                                                           │
        └────────────── lặp lại 2 lần/ngày, không mở app iPhone ────────────────────┘
                                                                    ┌──────────────┐
                                                  tắt máy ─────────▶│ Sound        │
                                                                    │ Disconnect   │
                                                                    │  (UC-011)    │
                                                                    │  WF-016 🚗   │
                                                                    └──────────────┘

HÀNH TRÌNH 2 — Jordan (Busy Professional): lái xe trong lúc họp, chỉ dùng chạm
┌──────────────┐   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│ Lên xe khi   │──▶│ App im lặng  │──▶│ Widget render│──▶│ 1 chạm →     │
│ đang gọi     │   │ bỏ lượt phát │   │ trên màn Audi│   │ dẫn đường    │
│ (UC-015)     │   │ (AF-010.1)   │   │  (UC-015)    │   │  (UC-023)    │
│ WF-017 🚗    │   │  WF-016 🚗   │   │  WF-017 🚗   │   │  WF-016 🚗   │
└──────────────┘   └──────────────┘   └──────────────┘   └──────┬───────┘
                                                                │
                                          MVP 2 ────────────────▼──────────────┐
                                                     │ Gọi client 1 chạm       │
                                                     │  (UC-034) WF-016 🚗     │
                                                     └─────────────────────────┘

HÀNH TRÌNH 3 — Sam (Car Enthusiast): dựng widget cuối tuần rồi mua Lifetime
┌──────────────┐   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│ Mở trình tạo │──▶│ Chọn ảnh xe  │──▶│ Preview theo │──▶│ Paywall →    │──▶│ Widget ảnh   │
│ widget       │   │ thật, crop   │   │ tỉ lệ xe     │   │ Lifetime     │   │ thật trên xe │
│ (UC-012)     │   │  (UC-014)    │   │  (UC-013)    │   │ (UC-030)     │   │  (UC-015)    │
│ WF-008 📱    │   │  WF-024 📱   │   │  WF-023 📱   │   │ WF-010→011📱 │   │  WF-017 🚗   │
└──────────────┘   └──────────────┘   └──────────────┘   └──────────────┘   └──────────────┘

HÀNH TRÌNH 4 — Vòng đời chuyển đổi: ngày 0 → ngày 12 (cơ chế lọc rủi ro của gói Free)
┌──────────────┐   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│ Ngày 0       │──▶│ Ngày 0       │──▶│ Ngày 1-11    │──▶│ Ngày 12      │──▶│ Trial 7 ngày │
│ onboarding   │   │ chuyến đầu:  │   │ dùng Free,   │   │ tự chạm tính │   │ + xác nhận   │
│ KHÔNG paywall│   │ app chạy trên│   │ KHÔNG bị     │   │ năng khoá    │   │ giá cuối     │
│ (UC-001)     │   │ xe tôi?      │   │ nhắc lặp lại │   │  (UC-025)    │   │ (UC-026,027) │
│ WF-002 📱    │   │ (UC-015,024) │   │ (UC-024)     │   │  WF-010 📱   │   │  WF-011 📱   │
└──────────────┘   └──────┬───────┘   └──────────────┘   └──────────────┘   └──────────────┘
                          │
             widget KHÔNG chạy trên xe
                          ▼
                   ┌──────────────────────────────────────────────┐
                   │ Phát hiện TRƯỚC khi trả tiền → không refund, │
                   │ không 1★ (R-04, R-11) → HÀNH TRÌNH 5         │
                   └──────────────────────────────────────────────┘

HÀNH TRÌNH 5 — Đường phục hồi khi gặp lỗi tương thích (không có nhánh nào dẫn tới màn trắng)
┌──────────────┐   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│ Render thất  │──▶│ Thông báo    │──▶│ Cảnh báo trên│──▶│ Xem kích     │──▶│ Gửi báo cáo  │
│ bại trên xe  │   │ bằng chữ,    │   │ Home sau     │   │ thước thật + │   │ có xem trước │
│ (UC-015)     │   │ chỉ đọc      │   │ chuyến       │   │ sửa widget   │   │ dữ liệu      │
│ WF-017 🚗    │   │ (UC-016)     │   │ (UC-016)     │   │ (UC-017,013) │   │  (UC-017)    │
│              │   │ WF-019 🚗    │   │ WF-006 📱    │   │ WF-014→023📱 │   │  WF-028 📱   │
└──────────────┘   └──────────────┘   └──────┬───────┘   └──────────────┘   └──────┬───────┘
                                             │                                     │
                          render kế tiếp OK ─┴─▶ cảnh báo TỰ XOÁ (SF-005)          │
                                                                                   ▼
                                                            ┌──────────────────────────────┐
                                                            │ Lời mời đánh giá bị CHẶN     │
                                                            │ 7 ngày (AC-033.2) → không tự │
                                                            │ đưa mình vào tình huống 1★   │
                                                            └──────────────────────────────┘
```

**Ba điều cần đọc ra từ năm hành trình này:**

1. **Hành trình 1 và 2 hoàn toàn không có bước nào trên iPhone.** Giá trị hằng ngày của app nằm trên màn hình xe; app iPhone chỉ là nơi cấu hình. Điều này định hình thứ tự ưu tiên thi công: bề mặt CarPlay phải xong trước.
2. **Hành trình 4 có một nhánh rẽ mà đối thủ không có**: người dùng phát hiện app không tương thích **trước khi** có giao dịch. Nhánh đó dẫn sang Hành trình 5 thay vì dẫn tới refund và 1★.
3. **Hành trình 5 kết thúc bằng một hành động "không làm gì"** — chặn lời mời đánh giá. Ở một niche mà rating trung bình 2,2/5, biết khi nào **không** hỏi là một cơ chế sản phẩm, không phải một chi tiết.

---

## 9. Screen-Intent Summary

Bảng tra nhanh cho `Wireframes.md` (Step 5): mỗi màn hình phải hỗ trợ **đúng một** Primary Action, với archetype và mật độ đã định.

| Screen (WF-ID) | Screen Name | Archetype | Density | User Intent | Primary Action | Secondary Actions | Key UCs |
|---|---|---|---|---|---|---|---|
| WF-001 | Splash / Launch | Consumption | Light | "Tôi muốn app mở ra thật nhanh" | Không có — hệ thống quyết định điểm đến | — | UC-001 |
| WF-002 | Onboarding — Welcome | Discovery | Light | "Tôi muốn biết app này làm gì" | Chạm "Bắt đầu" | Phục hồi giao dịch | UC-001 |
| WF-003 | Onboarding — Chọn Xe | Action | Medium | "Tôi muốn app biết xe của tôi" | Chọn hãng → model → năm | Tìm kiếm, quay lại tầng, báo thiếu xe, bỏ qua | UC-002, UC-003 |
| WF-004 | Onboarding — Chọn Âm Thanh | Discovery | Medium | "Tôi muốn nghe app này nghe thế nào" | Nghe thử và chọn sound Connect | Duyệt nhóm, dừng, chọn sau | UC-006, UC-001 |
| WF-005 | Onboarding — Cấp Quyền | Action | Medium | "Tôi muốn biết app cần gì và để làm gì" | Quyết định từng quyền rồi "Tiếp tục" | Tìm hiểu thêm, bỏ qua tất cả | UC-004, UC-005 |
| WF-006 | Home (iPhone) | Management | **Dense** | "Tôi muốn biết mọi thứ đang ở trạng thái nào" | Xem trạng thái kết nối và từng thành phần | Vào widget/sound/giọng chào/xe, chẩn đoán, gói hiện tại | UC-024, UC-005, UC-012, UC-016, UC-027 |
| WF-007 | Thư Viện Âm Thanh | Discovery | **Dense** | "Tôi muốn nghe hết rồi chọn cái hay nhất" | Nghe thử và gán preset cho một sự kiện | Chuyển 3 sự kiện, nghe kỹ, âm lượng, xem preset khoá | UC-006, UC-007, UC-008, UC-009 |
| WF-008 | Trình Tạo Widget | Management | **Dense** | "Tôi muốn widget đẹp mà không phải học công cụ" | Chọn preset widget và lưu | Chọn ảnh, xem trước theo tỉ lệ xe, đổi loại | UC-012, UC-013, UC-014 |
| WF-009 | Cài Đặt Giọng Chào | Action | Medium | "Tôi muốn nghe thử và quyết định app biết gì" | Nghe thử rồi bật/tắt từng nguồn ngữ cảnh | Công tắc chính, cấp quyền còn thiếu, xem ví dụ | UC-019, UC-018, UC-020, UC-005 |
| WF-010 | Paywall | Action | Medium | "Tôi muốn biết phải trả bao nhiêu và có lựa chọn nào" | Chọn một trong 4 lựa chọn | So sánh gói, phục hồi giao dịch, tiếp tục dùng Free | UC-025, UC-024, UC-030 |
| WF-011 | Xác Nhận Giá | Action | Light | "Tôi muốn thấy con số chính xác trước khi đồng ý" | Chạm "Xác nhận" | Quay lại đổi bậc, xem điều khoản | UC-026, UC-027, UC-030 |
| WF-012 | Cài Đặt Chung | Management | **Dense** | "Tôi muốn tìm và điều chỉnh một thứ cụ thể" | Điều chỉnh âm lượng sound | Ngôn ngữ, theme, quyền, đăng ký, quyền riêng tư, đánh giá | UC-009, UC-029, UC-031, UC-032, UC-033, UC-036 |
| WF-013 | Nhắc Hết Trial | Action | Light | "Tôi muốn biết sắp bị trừ bao nhiêu và khi nào" | Chọn: Nhắc sau · Đăng ký · Huỷ trial | Xem chi tiết đăng ký | UC-028, UC-027 |
| WF-014 | Chẩn Đoán Tương Thích | Management | Medium | "Tôi muốn biết chuyện gì đã xảy ra trên xe tôi" | Xem dữ liệu kết nối và gửi báo cáo | Xem widget ở kích thước thật, sao chép dữ liệu, xoá lịch sử | UC-017, UC-016, UC-013 |
| WF-015 | Account *(MVP 3)* | Management | Light | "Tôi muốn cấu hình có mặt trên thiết bị mới" | Đăng nhập và bật đồng bộ | Đăng xuất, xem cái gì được đồng bộ, xoá tài khoản | UC-035 |
| WF-016 | CarPlay Dashboard 🚗 | Discovery | Medium | "Tôi muốn nhìn một lượt là thấy thứ tôi cần" | Chạm thẻ liên quan nhất | Chỉ chạm thẻ — **không có Layer 3/4 trên bề mặt đang lái** | UC-022, UC-023, UC-021, UC-010, UC-011 |
| WF-017 | CarPlay Widget 🚗 | Consumption | Light | "Tôi muốn thấy widget của tôi, không bị cắt" | Không có — bề mặt để nhìn | — (widget tương tác thuộc MVP 2) | UC-015, UC-005, UC-010, UC-036 |
| WF-018 | CarPlay — Trạng Thái Free 🚗 | Consumption | Light | "Tôi muốn dùng cái đang có, không bị quấy rầy" | Không có hành động bắt buộc | Đọc một dòng gợi ý — **không mở paywall trên xe** | UC-024, UC-022, UC-023 |
| WF-019 | CarPlay — Fallback Lỗi 🚗 | Consumption | Light | "Có gì không ổn — đó là gì, có phải lỗi của tôi?" | Không có — chỉ đọc | — (mọi hành động diễn ra sau, trên iPhone) | UC-016, UC-015 |
| WF-020 | Sheet — Nghe Thử Âm Thanh | Consumption | Medium | "Tôi muốn nghe kỹ đúng như trên xe rồi quyết định" | Nghe ở mức thật và "Dùng sound này" | Phát lại, âm lượng, chọn sự kiện, preset trước/sau | UC-006, UC-007, UC-009 |
| WF-021 | Sheet — Không tìm thấy xe của tôi | Action | Light | "Xe tôi không có — tôi muốn nói ra và đi tiếp" | Điền hãng/model/năm và "Gửi" | Chọn phân khúc xe, đóng | UC-003, UC-002 |
| WF-022 | Sheet — Lý Do Xin Quyền | Consumption | Light | "Tôi muốn hiểu quyền này dùng để làm gì" | Đọc lý do rồi "Cho phép" / "Không, cảm ơn" | Xem ví dụ có/không có quyền, chính sách | UC-004, UC-019 |
| WF-023 | Modal — Preview Widget Theo Màn Hình Xe | Consumption | Medium | "Tôi muốn thấy widget trên đúng màn hình xe của tôi" | Xem từng tỉ lệ và "Dùng bản này" | Vuốt tỉ lệ, dark/light, cảnh báo vượt vùng, đổi ảnh | UC-013, UC-012, UC-014 |
| WF-024 | Sheet — Chọn Ảnh Cho Widget | Action | Medium | "Tôi muốn đặt ảnh xe tôi và biết phần nào bị cắt" | Chọn ảnh, crop, "Xong" | Đổi nguồn ảnh, xoay, duyệt ảnh xe theo model | UC-014 |
| WF-025 | Sheet — Quản Lý Đăng Ký | Management | Medium | "Tôi muốn biết đang trả cho gì và huỷ được" | Xem trạng thái và huỷ nếu muốn | Phục hồi giao dịch, xem tính năng đang có, xem gói khác | UC-029, UC-027, UC-028, UC-030 |
| WF-026 | Sheet — Chọn Ngôn Ngữ | Action | Light | "Tôi muốn dùng app bằng tiếng của tôi" | Chọn một ngôn ngữ | Theo hệ thống, xem ngôn ngữ sẽ có ở MVP 2 | UC-031 |
| WF-027 | Alert — Xác Nhận Huỷ Trial | Action | Light | "Tôi muốn chắc mình hiểu hậu quả trước khi huỷ" | Xác nhận huỷ hoặc giữ đăng ký | — (alert chỉ có một câu hỏi) | UC-029, UC-028 |
| WF-028 | Sheet — Gửi Báo Cáo Tương Thích | Action | Medium | "Tôi muốn gửi vấn đề và biết dữ liệu gì rời khỏi máy" | Xem danh sách dữ liệu và "Gửi" | Thêm ghi chú, bỏ tick từng mục, xem giá trị thật, sao chép | UC-017, UC-033 |
| WF-029 | Alert — Xoá Dữ Liệu On-Device | Action | Light | "Tôi muốn xoá thứ app đã học, không mất cấu hình" | Xác nhận xoá dữ liệu học | Huỷ, xoá cả cấu hình (tách riêng) | UC-032 |
| WF-030 | Overlay — Toast Xác Nhận | Consumption | Light | "Tôi muốn biết việc vừa làm đã xong" | Không có — tự biến mất | Đóng ngay, hoàn tác, chọn mức hài lòng (biến thể mời đánh giá) | UC-033, UC-007, UC-012, UC-017, UC-026 |

**Kiểm tra bảng:**
- 30/30 màn hình có mặt · mỗi màn có **đúng một** Primary Action · mỗi màn có Archetype thuộc {Discovery, Action, Consumption, Management} · Density thuộc {Light, Medium, Dense}
- Phân bố archetype: Management 6 · Action 10 · Discovery 4 · Consumption 10 · Social **0** — không có màn hình Social, vì MVP 1 không có nội dung chia sẻ và không có tương tác giữa người dùng. Đây là kết luận, không phải bỏ sót.
- Phân bố density: Dense 4 · Medium 12 · Light 14. Không có màn hình CarPlay nào ở mức Dense — **giới hạn cứng vì an toàn khi lái**.
- Sáu màn hình có Primary Action là "không có hành động": WF-001, WF-017, WF-018, WF-019, WF-030, và WF-016 ở trạng thái nhìn-không-chạm. Cả sáu đều có chủ ý: bốn trong số đó nằm trên bề mặt người dùng đang lái.

---

**Document Version**: 2.4
**Last Updated**: 2026-08-07 (snapshot bộ tài liệu; file tạo ngày 2026-08-17)
**Status**: Draft — chờ PO review
**Dependencies**: `PRD.md` v2.4 · `Project_Overview.md` v2.4
**Bước kế tiếp**: `gate-uc` → phê duyệt → **Step 4: `Functional_Requirements.md`** (mang nguyên **166 AC-xxx.y** ở §2 sang, không đánh số lại)

**Thống kê ID**: 36 UC · 166 AC · 113 AF · 30 WF · 13 TF · 21 SF
