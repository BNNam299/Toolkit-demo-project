# FR — Gói Free, Paywall & Thanh Toán

**Sub-spec của**: [`Functional_Requirements.md`](./Functional_Requirements.md) · **Version** 2.4 · **Snapshot** 2026-08-07
**Phạm vi**: FR-043 → FR-054 · **UC nguồn**: UC-024 → UC-030 · **PRD Feature**: F4, F7
**Màn hình liên quan**: WF-006, WF-007, WF-008, WF-010, WF-011, WF-012, WF-013, WF-016, WF-018, WF-025, WF-027, WF-030

> Theo PRD §11, đây là **điểm khác biệt hóa lớn nhất** của sản phẩm, không phải một chi tiết triển khai. Toàn bộ nhóm là phản ứng trực tiếp với dữ liệu: ~60/96 review 1★ của đối thủ là về paywall. Bốn ràng buộc cứng: **không bán gói weekly** · **paywall không xuất hiện ở lần mở app đầu tiên** · **giá cuối bằng tiền tệ địa phương, không quy đổi gây nhầm** · **nút huỷ ngang hàng nút mua**.

---

## FR-043: EntitlementService là nguồn chân lý duy nhất 📱🚗

**Source UC**: UC-024
**Priority**: High · **Status**: Planned

**Description**:
Hệ thống phải có **một** service duy nhất trả lời câu hỏi "người dùng này được dùng gì", tách khỏi paywall và tách khỏi StoreKit. Mọi feature gate đều hỏi service này; **cấm** rải điều kiện entitlement trong tầng View.

**Input**:
- `Transaction.currentEntitlements` từ StoreKit 2
- Trạng thái trial (ngày bắt đầu, ngày hết hạn)
- `daysSinceInstall` (Int)

**Processing**:
1. Xác định mức entitlement hiện tại: `free` | `trial` | `premium` | `lifetime`.
2. Trả về **tập quyền** tương ứng: số widget tối đa, tập sound preset khả dụng, tập thẻ dashboard khả dụng, giọng chào bật/tắt được.
3. Cấu hình gói Free: **1 widget đầy đủ chức năng + 3 sound preset + dashboard cơ bản** (nhạc đang phát, thời tiết, 1 shortcut) — theo Default đã chốt ở PRD §14.
4. Phát thông báo khi entitlement đổi, để mọi màn hình đang mở cập nhật trong ≤ 2s (bàn giao FR-049).
5. Cache entitlement đã xác thực on-device để hoạt động khi offline.
6. Cưỡng chế ràng buộc "paywall không ở lần mở đầu" ngay trong service (bàn giao FR-045), **không** bằng điều kiện rải rác trong View.

**Output**:
- Một tập quyền nhất quán cho toàn app và cho widget extension
- Sự kiện thay đổi entitlement để UI phản ứng tức thì

**Business Rules**:
- **BR-043.1**: `EntitlementService` là **nguồn chân lý duy nhất**; **cấm** View tự suy ra quyền từ trạng thái mua hàng.
- **BR-043.2**: Gói Free là **một hạng người dùng thường trực**, không phải trạng thái tạm trước khi mua (`Project_Overview.md` §3.3 Quyết định 5).
- **BR-043.3**: Khi offline, dùng entitlement đã xác thực trong cache; **cấm** hạ Lifetime xuống Free vì mất mạng.
- **BR-043.4**: Không đọc được entitlement → mặc định về **Free và vẫn cho dùng**; chặn người dùng vì lỗi đọc là hành vi sai.

**Validation Rules**:
- **VR-043.1**: Chỉ chấp nhận entitlement do StoreKit xác thực; **cấm** suy quyền từ dữ liệu cục bộ chưa xác thực.
- **VR-043.2**: Cấu hình gói Free phải khớp đúng Default ở PRD §14; lệch cấu hình là lỗi dữ liệu, không phải lựa chọn thiết kế.

**Error Handling**:
- **ERR-043.1** (từ State Variation FR-043 "Error"): Không đọc được entitlement → mặc định Free, vẫn cho dùng, không hiện lỗi trên màn hình xe.
- **ERR-043.2** (từ State Variation FR-043 "Offline"): Mất mạng khi đã mua Lifetime → dùng cache đã xác thực, không hạ xuống Free.

**Acceptance Criteria**:
- **AC-024.2**: WHEN người dùng ở gói Free THEN có đúng 1 widget CarPlay **đầy đủ chức năng** (không watermark, không làm mờ), 3 sound preset chất lượng đầy đủ, và dashboard cơ bản.

---

## FR-044: Cấu hình gói Free vô thời hạn 📱🚗

**Source UC**: UC-024
**Priority**: High · **Status**: Planned

**Description**:
Hệ thống phải cung cấp gói Free **vô thời hạn, không quảng cáo**, đủ dùng để người dùng tự xác nhận app chạy trên xe của họ trước khi có bất kỳ giao dịch nào. Đây vừa là chiến lược tăng trưởng vừa là cơ chế lọc rủi ro cho R-11 và R-04.

**Input**:
- Tập quyền của mức `free` từ FR-043
- Trạng thái sử dụng: có widget đang bật, sound đã gán, dashboard đang hiển thị

**Processing**:
1. Kích hoạt đúng 1 widget đầy đủ chức năng — **không** watermark, **không** làm mờ, **không** giới hạn thời gian.
2. Mở 3 sound preset ở chất lượng đầy đủ; giữ preset còn lại có `LockLabel` (bàn giao FR-010).
3. Hiển thị dashboard cơ bản trên CarPlay theo cấu hình đã chốt (bàn giao FR-041).
4. **Không** hiển thị quảng cáo ở bất kỳ đâu.
5. Hiển thị `StatusBadge` "Gói Free" trên WF-006 — nói "bạn đang có gì", không phải "bạn thiếu gì".
6. Ghi `free_tier_widget_used` mỗi lần widget ở gói Free được dùng trên xe.

**Output**:
- Trải nghiệm đầy đủ ở mức Free, không hết hạn, không quảng cáo
- Nếu widget **không** chạy trên xe của người dùng, họ phát hiện **trước khi trả tiền**

**Business Rules**:
- **BR-044.1**: Gói Free **không có giới hạn thời gian** và **không có quảng cáo**. Đây là điểm khác biệt hóa được tuyên bố công khai; vi phạm nó là phá luận điểm chính của sản phẩm.
- **BR-044.2**: Widget ở gói Free là widget **đầy đủ chức năng** — không phải preview mờ hay bản có watermark.
- **BR-044.3**: Dùng Free vô thời hạn là **kết quả hợp lệ**, không phải thất bại chuyển đổi.

**Validation Rules**:
- **VR-044.1**: Số widget kích hoạt ở mức Free = 1; số sound preset mở = 3; số thẻ dashboard = 3 (nhạc, thời tiết, 1 shortcut).

**Error Handling**:
- **ERR-044.1** (từ AF-024.1): Người dùng dùng Free mãi → hợp lệ; hệ thống **không** nhắc nâng cấp lặp lại theo phiên.
- **ERR-044.2** (từ AF-024.2): Widget không chạy trên xe người dùng → đây chính là mục đích của free tier; bàn giao FR-031 và FR-032 để chẩn đoán, **không** phát sinh giao dịch nào.

**Acceptance Criteria**:
- **AC-024.3**: WHEN người dùng ở gói Free THEN **không có quảng cáo** và **không có giới hạn thời gian**.
- **AC-024.5**: WHEN người dùng dùng widget ở gói Free THEN hệ thống ghi `free_tier_widget_used`.

---

## FR-045: Chính sách hiển thị paywall 📱🚗

**Source UC**: UC-024, UC-025
**Priority**: High · **Status**: Planned

**Description**:
Hệ thống phải cưỡng chế: **paywall không xuất hiện ở lần mở app đầu tiên**, tối đa **một** lời mời nâng cấp dạng tĩnh mỗi màn hình, **không popup**, và **không có đường nào** mở paywall từ màn hình xe.

**Input**:
- `daysSinceInstall` (Int)
- `trigger_source`: hành động chủ động của người dùng · giới hạn tính năng · lối vào từ Settings
- Bề mặt hiện tại: iPhone hoặc CarPlay
- Số lời mời đã hiển thị trong phiên hiện tại

**Processing**:
1. Trước khi hiển thị WF-010, kiểm điều kiện: `daysSinceInstall > 0` **hoặc** `trigger_source` là hành động chủ động của người dùng.
2. Nếu điều kiện không thoả: **từ chối** hiển thị paywall và ghi nhận lần từ chối (để audit chính sách này).
3. Nếu bề mặt hiện tại là CarPlay: **từ chối tuyệt đối** — không có đường nào mở paywall khi người dùng đang lái.
4. Hiển thị tối đa **một** `StaticNotice`/`LockLabel` mời nâng cấp trên mỗi màn hình; **cấm** popup; **cấm** nhắc lại theo phiên.
5. Khi paywall được mở hợp lệ: Zone A nói về **đúng tính năng người dùng vừa chạm**, không phải quảng cáo chung.
6. Ghi `paywall_shown` kèm `trigger_source` và `days_since_install`.
7. Nếu người dùng chọn "Tiếp tục dùng gói Free" hoặc đóng: về màn hình trước, **không** hỏi lại trong cùng phiên.

**Output**:
- Paywall chỉ xuất hiện khi người dùng chủ động, và không bao giờ ở lần mở đầu
- Event `paywall_shown` đủ dữ liệu để **audit** rằng chính sách này được tuân thủ

**Business Rules**:
- **BR-045.1**: **Cấm** hiển thị paywall ở lần mở app đầu tiên. Kiểm chứng được bằng `paywall_shown.days_since_install > 0` (PRD §7 F4).
- **BR-045.2**: **Cấm** popup mời nâng cấp; chỉ dùng thông báo tĩnh trong luồng.
- **BR-045.3**: **Cấm** mọi đường mở paywall từ bề mặt CarPlay — an toàn khi lái quan trọng hơn conversion.
- **BR-045.4**: Đóng paywall → **không** hỏi lại trong cùng phiên.

**Validation Rules**:
- **VR-045.1**: Mọi lần hiển thị paywall phải ghi `paywall_shown` kèm cả `trigger_source` và `days_since_install`; thiếu tham số làm mất khả năng audit.

**Error Handling**:
- **ERR-045.1** (từ AF-024.3): Người dùng chạm tính năng khoá → mở WF-010 với ngữ cảnh đúng tính năng đó.
- **ERR-045.2** (từ AF-025.1): Người dùng đóng paywall → về màn hình trước, không hỏi lại trong phiên.
- **ERR-045.3** (từ AF-025.4): Paywall mở từ ngữ cảnh một tính năng → nhấn mạnh bậc chứa tính năng đó, nhưng **ba bậc kia vẫn hiển thị đầy đủ**.

**Acceptance Criteria**:
- **AC-024.1**: WHEN người dùng mở app lần đầu THEN hệ thống **không** hiển thị WF-010; kiểm chứng bằng `paywall_shown.days_since_install > 0` hoặc `trigger_source` là hành động chủ động của người dùng.
- **AC-024.4**: WHEN người dùng ở gói Free THEN hệ thống hiển thị tối đa **một** lời mời nâng cấp dạng tĩnh mỗi màn hình, không dùng popup và không nhắc lại theo phiên.
- **AC-025.6**: WHEN WF-010 hiển thị THEN hệ thống ghi `paywall_shown` kèm `trigger_source` và `days_since_install`.

---

## FR-046: Trình bày 4 bậc giá từ StoreKit 📱

**Source UC**: UC-025
**Priority**: High · **Status**: Planned

**Description**:
Hệ thống phải hiển thị đúng **4 lựa chọn** (Free đang dùng · $4,99/tháng · $29,99/năm · $49,99 lifetime), **không có bậc weekly**, với giá cuối bằng tiền tệ địa phương lấy trực tiếp từ StoreKit.

**Input**:
- Product IDs cấu hình trên App Store Connect: monthly, yearly, lifetime
- `Product.displayPrice` từ StoreKit 2 (đã theo tiền tệ storefront)
- Entitlement hiện tại (để đánh dấu bậc đang dùng)
- `trigger_source` (để nhấn mạnh bậc phù hợp)

**Processing**:
1. Truy vấn StoreKit lấy 3 product; **chờ** kết quả, hiển thị trạng thái tải trong lúc chờ.
2. Dựng 4 `PriceTierCard`: Free (đánh dấu "gói bạn đang dùng", **không làm mờ**), Monthly, Yearly, Lifetime.
3. Mỗi bậc nêu rõ mở khóa những gì.
4. Cho người dùng mở bảng so sánh Free ↔ Premium inline (sub-flow SF-015); chọn bậc trong bảng đồng bộ với thẻ giá ở Zone B.
5. Nhấn mạnh bậc phù hợp với `trigger_source`, nhưng **giữ đủ 4 bậc hiển thị**.
6. Người dùng chọn một bậc → chuyển WF-011 (bàn giao FR-048).

**Output**:
- 4 lựa chọn hiển thị đầy đủ với giá cuối bằng tiền tệ địa phương
- Bậc được chọn, sẵn sàng cho bước xác nhận giá

**Business Rules**:
- **BR-046.1**: **Cấm bán gói weekly**. Weekly $5,99 = $311/năm và là nguồn trực tiếp của cáo buộc "scam" nhắm vào đối thủ (PRD §11).
- **BR-046.2**: Gói Free phải được trình bày như **một lựa chọn hợp lệ đang dùng**, không bị làm mờ hay ẩn.
- **BR-046.3**: Giá luôn là **giá cuối bằng tiền tệ địa phương**; **cấm** quy đổi kiểu "$0,48/tuần" (R-12).
- **BR-046.4**: **Cấm** dùng discount phần trăm không đúng thực tế (R-12).

**Validation Rules**:
- **VR-046.1**: Số bậc hiển thị đúng bằng 4; xuất hiện bậc thứ 5 hoặc bậc weekly là lỗi cấu hình.
- **VR-046.2**: Giá hiển thị phải lấy từ `Product.displayPrice`, **không** ghép chuỗi thủ công từ số và ký hiệu tiền tệ.

**Error Handling**:
- **ERR-046.1** (từ AF-025.3): StoreKit không trả về giá → bàn giao FR-047 (báo lỗi rõ, chặn đường sang WF-011).
- **ERR-046.2** (từ AF-025.2): Người dùng đã mua trên thiết bị khác → nút "Phục hồi giao dịch" luôn hiện (bàn giao FR-003).
- **ERR-046.3** (từ State Variation WF-010 "Trial đã dùng"): Đã từng dùng trial → bậc giá **không** hiện ưu đãi trial; nêu rõ là mua trực tiếp.

**Acceptance Criteria**:
- **AC-025.1**: WHEN WF-010 hiển thị THEN có đúng 4 lựa chọn: Free · Monthly $4,99 · Yearly $29,99 · Lifetime $49,99, và **không có bậc weekly nào**.
- **AC-025.2**: WHEN giá hiển thị THEN đó là **giá cuối cùng bằng tiền tệ địa phương**, và hệ thống **không** quy đổi kiểu "$0,48/tuần" (R-12).
- **AC-025.4**: WHEN WF-010 hiển thị THEN gói Free được trình bày như một lựa chọn hợp lệ đang dùng, không bị làm mờ hay ẩn.

---

## FR-047: Cấm hiển thị giá cache hoặc giá hardcode 📱

**Source UC**: UC-025 (AF-025.3)
**Priority**: High · **Status**: Planned

**Description**:
Khi không lấy được giá từ StoreKit, hệ thống phải **báo lỗi rõ ràng và chặn đường tới giao dịch** — tuyệt đối không hiển thị giá cache, giá hardcode, hay giá đoán. Hiển thị một con số có thể sai chính là cách sinh ra cáo buộc bait-and-switch (R-12).

**Input**:
- Kết quả truy vấn StoreKit: thành công / lỗi / timeout
- Storefront hiện tại (có thể đổi giữa phiên)

**Processing**:
1. Hiển thị trạng thái đang tải trong lúc chờ StoreKit.
2. Nếu truy vấn thất bại hoặc timeout: hiển thị thông báo lỗi rõ ràng kèm nút thử lại.
3. **Chặn** đường chuyển sang WF-011 khi chưa có giá xác thực.
4. **Cấm** đọc giá từ bất kỳ nguồn nào khác StoreKit — không cache, không hardcode, không remote config.
5. Nếu người dùng đổi vùng App Store giữa lúc mua: **đọc lại** giá từ StoreKit trước khi hiển thị WF-011.

**Output**:
- Người dùng **không bao giờ** thấy một con số giá có thể sai
- Hoặc có giá xác thực, hoặc có thông báo lỗi — không có trạng thái thứ ba

**Business Rules**:
- **BR-047.1**: **Cấm tuyệt đối** hiển thị giá không đến từ StoreKit tại thời điểm đó.
- **BR-047.2**: Trạng thái đúng khi không lấy được giá là **báo lỗi**, không phải đoán.
- **BR-047.3**: Đổi storefront giữa phiên → giá phải được đọc lại, không dùng giá của storefront cũ.

**Validation Rules**:
- **VR-047.1**: Trước khi render WF-011, xác nhận giá đang dùng đến từ lần truy vấn StoreKit gần nhất và cùng storefront hiện tại.

**Error Handling**:
- **ERR-047.1** (từ AF-025.3): StoreKit không trả về dữ liệu → báo lỗi rõ ràng + nút thử lại; **không** hiện giá cache hay hardcode.
- **ERR-047.2** (từ AF-026.4): Người dùng đổi vùng App Store giữa lúc mua → đọc lại giá từ StoreKit.

**Acceptance Criteria**:
- **AC-025.3**: WHEN WF-010 hiển thị THEN hệ thống **không** dùng discount phần trăm không đúng thực tế (R-12).
- **AC-025.5**: IF không lấy được giá từ StoreKit THEN hệ thống báo lỗi rõ ràng và **không** hiển thị giá cache hay giá hardcode.

---

## FR-048: Màn xác nhận giá là điểm chặn duy nhất 📱

**Source UC**: UC-026
**Priority**: High · **Status**: Planned

**Description**:
Hệ thống phải có **đúng một** điểm chặn trước mọi giao dịch (WF-011), hiển thị đồng thời giá cuối, ngày hết trial và ngày bị trừ tiền, và ghi `price_confirmed` **trước khi** gọi dialog thanh toán.

**Input**:
- Bậc giá đã chọn từ FR-046
- Giá cuối xác thực từ StoreKit (qua FR-047)
- Ngày hết trial và ngày trừ tiền tính từ độ dài trial (7 ngày)

**Processing**:
1. Hiển thị Zone A với **đồng thời**: bậc đã chọn · giá cuối bằng tiền tệ địa phương · ngày hết trial · **ngày bị trừ tiền** · chu kỳ gia hạn.
2. Nếu bậc là Lifetime: **không** hiển thị ngày gia hạn; nêu rõ đây là giao dịch một lần (bàn giao FR-054).
3. Giữ Zone C (Discovery) **trống có chủ ý** — mọi thứ gây phân tán ở đây làm tăng nguy cơ người dùng bấm mà không đọc.
4. Cung cấp lối xem điều khoản và chính sách hoàn tiền ở Zone D.
5. Người dùng chạm "Xác nhận" → ghi `price_confirmed` **trước khi** gọi dialog thanh toán của Apple.
6. Gọi StoreKit purchase; bàn giao FR-049.

**Output**:
- Người dùng đã thấy và xác nhận giá cuối trước khi có bất kỳ khoản trừ nào
- Event `price_confirmed` là **bằng chứng tuân thủ** R-12

**Business Rules**:
- **BR-048.1**: **Không có đường nào** dẫn tới thanh toán mà bỏ qua WF-011. Nhân bản màn này sẽ tạo khả năng có một đường mua bỏ qua nó — đúng lỗ hổng đã khiến đối thủ bị tố bait-and-switch.
- **BR-048.2**: `price_confirmed` phải ghi **trước** dialog thanh toán; ghi sau thì mất giá trị làm bằng chứng.
- **BR-048.3**: Zone C của WF-011 **cấm** có nội dung khám phá hay bán thêm.

**Validation Rules**:
- **VR-048.1**: Bốn thông tin (giá cuối, ngày hết trial, ngày trừ tiền, chu kỳ) phải cùng hiển thị; thiếu một là lỗi.
- **VR-048.2**: Rà soát mã phải xác nhận chỉ có **một** điểm gọi StoreKit purchase, và nó nằm sau WF-011.

**Error Handling**:
- **ERR-048.1** (từ AF-026.1): Người dùng huỷ ở dialog Apple → về WF-011 **giữ lựa chọn**; không trả về WF-010, không hiện lại paywall.
- **ERR-048.2** (từ AF-026.3): Bậc Lifetime → không hiển thị ngày gia hạn (FR-054).
- **ERR-048.3** (từ AF-026.4): Đổi vùng App Store → đọc lại giá (FR-047).

**Acceptance Criteria**:
- **AC-026.1**: WHEN WF-011 hiển thị THEN nó hiện đồng thời: giá cuối bằng tiền tệ địa phương, ngày hết trial, và ngày bị trừ tiền.
- **AC-026.2**: WHEN người dùng chạm "Xác nhận" THEN hệ thống ghi `price_confirmed` **trước khi** gọi dialog thanh toán.
- **AC-026.5**: WHEN người dùng đi tới giao dịch THEN **không có đường nào** dẫn tới thanh toán mà bỏ qua WF-011.

---

## FR-049: Xử lý giao dịch StoreKit và mở khóa tính năng 📱

**Source UC**: UC-026
**Priority**: High · **Status**: Planned

**Description**:
Hệ thống phải xử lý kết quả giao dịch StoreKit, cập nhật entitlement và mở khóa tính năng trong **≤ 2 giây** mà không cần khởi động lại app, và báo nguyên nhân cụ thể khi thất bại.

**Input**:
- Kết quả `Product.purchase()`: success · userCancelled · pending · lỗi
- `Transaction` đã xác thực

**Processing**:
1. Nhận kết quả từ StoreKit.
2. Nếu thành công: xác thực `Transaction`, gọi `finish()`, cập nhật `EntitlementService` (FR-043).
3. Phát thông báo thay đổi entitlement; mọi màn hình đang mở cập nhật trong **≤ 2s**, không cần khởi động lại app.
4. Hiển thị WF-030 toast; bàn giao FR-050 để gửi xác nhận giao dịch.
5. Nếu `userCancelled`: về WF-011 giữ lựa chọn (ERR-048.1).
6. Nếu `pending`: hiển thị trạng thái chờ và nêu rõ giao dịch đang xử lý; **không** mở khóa trước khi xác thực.
7. Nếu lỗi: nêu **nguyên nhân từ StoreKit** kèm nút thử lại; giữ nguyên ở WF-011.

**Output**:
- Entitlement mới có hiệu lực trong ≤ 2s; tính năng mở khóa ngay
- Hoặc thông báo lỗi có nguyên nhân cụ thể và đường thử lại

**Business Rules**:
- **BR-049.1**: **Cấm** mở khóa tính năng trước khi `Transaction` được xác thực.
- **BR-049.2**: Thất bại thanh toán **không** đẩy người dùng về WF-010 và **không** làm mất lựa chọn bậc giá.
- **BR-049.3**: Thông báo lỗi phải nêu nguyên nhân từ StoreKit, **không** dùng câu chung "đã xảy ra lỗi".

**Validation Rules**:
- **VR-049.1**: Chỉ cập nhật entitlement từ `Transaction` đã xác thực chữ ký.

**Error Handling**:
- **ERR-049.1** (từ AF-026.2): Thanh toán thất bại → nêu nguyên nhân từ StoreKit + nút thử lại.
- **ERR-049.2** (từ AF-026.1): Người dùng huỷ ở dialog → về WF-011, giữ lựa chọn.
- **ERR-049.3** (từ State Variation FR-049 "Error"): Giao dịch ở trạng thái `pending` → hiện trạng thái chờ, không mở khóa sớm.

**Acceptance Criteria**:
- **AC-026.4**: WHEN thanh toán thành công THEN tính năng được mở khóa trong ≤ 2s mà không cần khởi động lại app.

---

## FR-050: Gửi xác nhận giao dịch sau khi mua 📱

**Source UC**: UC-026
**Priority**: High · **Status**: Planned

**Description**:
Hệ thống phải gửi xác nhận sau mỗi giao dịch thành công (email hoặc thông báo trong app), như biện pháp trực tiếp chống chargeback và dispute (R-12).

**Input**:
- `Transaction` đã xác thực: product ID, giá, ngày, ngày gia hạn (nếu có)
- Kênh xác nhận khả dụng

**Processing**:
1. Sau khi FR-049 cập nhật entitlement, dựng nội dung xác nhận: bậc đã mua, số tiền, ngày, ngày gia hạn kế tiếp (hoặc "một lần" với Lifetime).
2. Gửi xác nhận qua kênh khả dụng; nếu chưa có kênh email (MVP 1 không có tài khoản), dùng **thông báo trong app** lưu lại được ở WF-025.
3. Nếu gửi thất bại: **xếp hàng** và gửi lại; **không** chặn việc mở khóa tính năng vì lý do này.
4. Ghi nhận vào lịch sử giao dịch cục bộ để người dùng tra được ở WF-025.

**Output**:
- Người dùng có bằng chứng giao dịch tra được trong app
- Việc mở khóa tính năng **không** bị chặn bởi lỗi gửi xác nhận

**Business Rules**:
- **BR-050.1**: Lỗi gửi xác nhận **không được** ảnh hưởng tới việc mở khóa tính năng.
- **BR-050.2**: MVP 1 không có tài khoản nên xác nhận trong app là kênh chính; email chỉ khả dụng từ MVP 3 (FR-064).

**Validation Rules**:
- **VR-050.1**: Nội dung xác nhận phải chứa số tiền và ngày giao dịch chính xác từ `Transaction`, không phải giá hiển thị trước đó.

**Error Handling**:
- **ERR-050.1** (từ State Variation FR-050 "Error"): Không gửi được xác nhận → xếp hàng và gửi lại; không chặn mở khóa.
- **ERR-050.2** (từ AC-NFR-023.2): Endpoint nhận notification quá tải → xếp hàng phía server; không mất dữ liệu.

**Acceptance Criteria**:
- **AC-026.6**: WHEN thanh toán thành công THEN hệ thống gửi xác nhận giao dịch (email hoặc thông báo trong app) — biện pháp chống chargeback (R-12).

---

## FR-051: Quản lý trial 7 ngày và hiển thị đếm ngày 📱

**Source UC**: UC-027
**Priority**: High · **Status**: Planned

**Description**:
Hệ thống phải quản lý trial đúng **7 ngày**, hiển thị ngày hết hạn và ngày bị trừ tiền **trong app** ở cả WF-006 và WF-012, và khi trial kết thúc mà người dùng đã huỷ thì **giữ nguyên mọi cấu hình** widget/sound đã tạo.

**Input**:
- Trạng thái trial từ StoreKit: ngày bắt đầu, ngày hết hạn, đã dùng trial trước đó hay chưa
- Cấu hình widget/sound hiện có

**Processing**:
1. Khi người dùng xác nhận bậc có trial: bắt đầu trial 7 ngày; ghi `trial_started`; entitlement chuyển sang `trial`.
2. Hiển thị `StatusBadge` "Trial còn N ngày" **kèm ngày trừ tiền** ở WF-006 Zone D — tông trung tính, **không** đếm ngược gây áp lực.
3. Hiển thị `CompactRow` trạng thái trial kèm số liệu chính xác ở WF-012.
4. Ngày 6 và ngày 7: bàn giao FR-052 (nhắc hết trial).
5. Hết ngày 7 mà không huỷ: entitlement chuyển sang `premium`; ghi `trial_converted`.
6. Nếu người dùng huỷ trong trial: giữ quyền Premium **tới hết ngày 7**, sau đó về `free`, và **giữ nguyên toàn bộ cấu hình** widget/sound (bàn giao FR-023 ERR-023.2).
7. Nếu người dùng đã từng dùng trial: **không** hiển thị lại ưu đãi trial; nêu rõ là mua trực tiếp.

**Output**:
- Trial chạy đúng 7 ngày với ngày hết hạn và ngày trừ tiền hiển thị trong app
- Sau khi về Free: cấu hình đã tạo còn nguyên

**Business Rules**:
- **BR-051.1**: Độ dài trial là **đúng 7 ngày**, áp dụng cho cả Monthly và Yearly (Default đã chốt ở PRD §14).
- **BR-051.2**: Ngày hết hạn và ngày trừ tiền phải hiển thị **trong app**, không chỉ trong email hay trang subscription của iOS.
- **BR-051.3**: **Cấm** dùng đếm ngược gây áp lực hay ngôn từ khan hàng giả tạo.
- **BR-051.4**: Huỷ trial **không bao giờ** làm mất cấu hình người dùng đã tạo.
- **BR-051.5**: Lifetime **không có** trial; điều này phải nêu rõ ở WF-011.

**Validation Rules**:
- **VR-051.1**: Ngày trừ tiền hiển thị phải tính từ dữ liệu StoreKit, **không** tính thủ công từ ngày bắt đầu ở client.

**Error Handling**:
- **ERR-051.1** (từ AF-027.1): Người dùng huỷ trong trial → giữ Premium tới hết ngày 7, sau đó về Free, cấu hình được giữ.
- **ERR-051.2** (từ AF-027.2): Đã dùng trial trước đó → không hiện ưu đãi trial; nêu rõ là mua trực tiếp.
- **ERR-051.3** (từ AF-027.3): Mua Lifetime → không có trial, nêu rõ ở WF-011.
- **ERR-051.4** (từ State Variation WF-013 "Error"): Không đọc được ngày hết trial từ StoreKit → nêu rõ không xác định được và dẫn sang trang subscription của iOS; **tuyệt đối không đoán một con số**.

**Acceptance Criteria**:
- **AC-027.1**: WHEN trial bắt đầu THEN hệ thống ghi `trial_started` và độ dài trial là đúng **7 ngày**.
- **AC-027.2**: WHEN trial đang chạy THEN ngày hết hạn và ngày bị trừ tiền hiển thị **trong app**, ở cả WF-006 và WF-012.
- **AC-027.3**: IF người dùng huỷ trial THEN quyền Premium được giữ tới hết ngày 7, sau đó về gói Free, và **mọi cấu hình widget/sound đã tạo được giữ nguyên**.
- **AC-027.4**: IF người dùng đã từng dùng trial THEN hệ thống **không** hiển thị lại ưu đãi trial.
- **AC-027.5**: WHEN trial chuyển thành trả phí THEN hệ thống ghi `trial_converted`.

---

## FR-052: Nhắc trước khi hết trial 📱

**Source UC**: UC-028
**Priority**: Medium · **Status**: Planned

**Description**:
Hệ thống phải nhắc người dùng vào ngày 6 và ngày 7 với **số tiền chính xác** và **ngày bị trừ**, đặt nút "Huỷ trial" **ngang hàng thị giác** với nút "Đăng ký", và giới hạn "Nhắc sau" tối đa 2 lần.

**Input**:
- Số ngày còn lại của trial, số tiền chính xác, ngày trừ tiền (từ FR-051)
- Số lần người dùng đã chọn "Nhắc sau"

**Processing**:
1. Vào ngày 6 và ngày 7, hiển thị WF-013 với Zone A: số ngày còn lại · **số tiền chính xác** · **ngày bị trừ**.
2. Zone B có ba nút **ngang hàng thị giác**: "Nhắc sau" · "Đăng ký" · **"Huỷ trial"**.
3. Nếu người dùng chọn "Nhắc sau": tăng bộ đếm; hiện lại ở ngày 7. Sau **2 lần**, nút "Nhắc sau" biến mất.
4. Nếu chọn "Đăng ký": về WF-006; trial tiếp tục tới ngày 7 rồi chuyển trả phí.
5. Nếu chọn "Huỷ trial": mở WF-027 (bàn giao FR-053).
6. Giữ Zone C **trống có chủ ý** — đây là màn hình quyết định, không phải màn hình bán thêm.

**Output**:
- Người dùng được thông báo ít nhất một lần với số tiền chính xác **trước khi** bị trừ
- Đường huỷ dài tối đa 3 chạm kể từ WF-013

**Business Rules**:
- **BR-052.1**: Nút "Huỷ trial" **ngang hàng thị giác** với nút "Đăng ký"; ẩn hay làm mờ nút huỷ là dark pattern (R-12).
- **BR-052.2**: "Nhắc sau" tối đa **2 lần** trong cả kỳ trial; nhiều hơn thì trở thành quấy rầy.
- **BR-052.3**: **Cấm** đếm ngược gây áp lực và ngôn từ khan hàng giả tạo.
- **BR-052.4**: Zone C của WF-013 **cấm** có nội dung bán thêm.

**Validation Rules**:
- **VR-052.1**: Số tiền hiển thị phải là số tiền thật sẽ bị trừ, lấy từ StoreKit, bằng tiền tệ địa phương.

**Error Handling**:
- **ERR-052.1** (từ AF-028.1): Chọn "Nhắc sau" → hiện lại ngày 7, tối đa 2 lần.
- **ERR-052.2** (từ AF-028.2): Bỏ qua hoàn toàn → trial chuyển trả phí đúng ngày 7 **như đã thông báo**, không có bất ngờ.
- **ERR-052.3** (từ AF-028.3): Huỷ → về Free sau ngày 7, cấu hình được giữ (FR-051).

**Acceptance Criteria**:
- **AC-028.1**: WHEN trial còn 1 ngày THEN hệ thống hiển thị WF-013 kèm **số tiền chính xác** và **ngày bị trừ**.
- **AC-028.2**: WHEN WF-013 hiển thị THEN nút "Huỷ trial" **ngang hàng về mặt thị giác** với nút "Đăng ký", không bị ẩn hay làm mờ (biện pháp chống R-12).
- **AC-028.3**: IF người dùng chọn "Nhắc sau" THEN hệ thống nhắc lại tối đa 2 lần trong cả kỳ trial.
- **AC-028.4**: WHEN WF-013 hiển thị THEN nó **không** dùng đếm ngược gây áp lực hay ngôn từ khan hàng giả tạo.

---

## FR-053: Quản lý, huỷ đăng ký và phục hồi giao dịch 📱

**Source UC**: UC-029
**Priority**: Medium · **Status**: Planned

**Description**:
Hệ thống phải hiển thị gói hiện tại, giá và ngày gia hạn, cho huỷ trong **tối đa 3 chạm** kể từ WF-012, và nêu rõ ngày quyền Premium kết thúc trước khi người dùng xác nhận huỷ.

**Input**:
- Entitlement hiện tại và chi tiết subscription từ StoreKit
- Điểm khởi phát: dòng "Đăng ký của tôi" trên WF-012, hoặc nút "Huỷ trial" trên WF-013

**Processing**:
1. Trên WF-012, dòng "Đăng ký của tôi" hiển thị **trạng thái ngay trên dòng** — người dùng thấy được mà không cần mở sheet.
2. Chạm dòng → mở WF-025 với Zone A: gói hiện tại · giá · ngày gia hạn kế tiếp (hoặc "đã mua vĩnh viễn").
3. Cho mở rộng inline danh sách tính năng đang có, **đánh dấu rõ tính năng nào vẫn còn ở gói Free** (sub-flow SF-019) — trình bày trung thực, không phải chiêu níu giữ.
4. Nút "Huỷ đăng ký" ở Zone B, **không ẩn, không làm mờ**; **không** có animation làm chậm đường tới nút này.
5. Chạm huỷ → WF-027 alert nêu rõ **quyền Premium còn dùng tới ngày nào** và **cấu hình đã tạo sẽ được giữ**.
6. Xác nhận → chuyển trang quản lý subscription của iOS; ghi `subscription_cancelled`.
7. Nút "Phục hồi giao dịch" luôn hiện ở Zone D (bàn giao FR-003).
8. Nếu entitlement là Lifetime: **không** hiện nút huỷ; nếu còn subscription cũ thì nhắc huỷ để không trả trùng.

**Output**:
- Người dùng biết chính xác trạng thái đăng ký và ngày kết thúc quyền
- Đường huỷ ≤ 3 chạm kể từ WF-012

**Business Rules**:
- **BR-053.1**: Đường huỷ **tối đa 3 chạm** kể từ WF-012. Làm dài đường huỷ là dark pattern và là nguyên nhân người dùng gọi app khác là scam.
- **BR-053.2**: Lifetime **không** hiện nút huỷ — hiện nút huỷ cho một giao dịch một lần gây bối rối.
- **BR-053.3**: Alert huỷ phải nêu rõ ngày kết thúc quyền **và** việc cấu hình được giữ.
- **BR-053.4**: **Cấm** animation hay bước trung gian làm chậm đường tới nút huỷ.

**Validation Rules**:
- **VR-053.1**: Ngày gia hạn hiển thị lấy từ StoreKit, không tính thủ công.

**Error Handling**:
- **ERR-053.1** (từ AF-029.1): Gói Lifetime → hiện "đã mua vĩnh viễn", không hiện nút huỷ.
- **ERR-053.2** (từ AF-029.2): Phục hồi giao dịch không tìm thấy gì → nói rõ điều đó (FR-003 ERR-003.1).
- **ERR-053.3** (từ AF-029.3): Đã huỷ trước đó → hiện rõ ngày quyền Premium kết thúc.
- **ERR-053.4** (từ State Variation WF-027 "Error"): Không mở được trang subscription của iOS → nêu rõ và hướng dẫn đường đi thủ công trong Cài đặt hệ thống.

**Acceptance Criteria**:
- **AC-029.1**: WHEN WF-025 hiển thị THEN nó hiện gói hiện tại, giá, và ngày gia hạn kế tiếp.
- **AC-029.2**: WHEN người dùng muốn huỷ THEN đường huỷ dài **tối đa 3 chạm** kể từ WF-012.
- **AC-029.3**: IF người dùng mua Lifetime THEN WF-025 **không** hiển thị nút huỷ đăng ký.
- **AC-029.4**: WHEN người dùng huỷ THEN hệ thống nêu rõ ngày quyền Premium kết thúc, và hệ thống ghi `subscription_cancelled`.

> **AC-029.5** (phục hồi giao dịch khi không có giao dịch nào) được hiện thực ở **FR-003**, nơi sở hữu hành vi phục hồi giao dịch cho cả ba điểm khởi phát. Không nhân bản ở đây.

---

## FR-054: Mua và phục hồi gói Lifetime 📱

**Source UC**: UC-030, UC-026
**Priority**: Medium · **Status**: Planned

**Description**:
Hệ thống phải xử lý Lifetime như **giao dịch một lần**: không hiển thị bất kỳ ngày gia hạn nào, mở khóa vĩnh viễn không phụ thuộc mạng, và nhắc huỷ subscription nếu người dùng đang có để không trả trùng.

**Input**:
- Product ID non-consumable của Lifetime
- Trạng thái subscription hiện tại (nếu có)

**Processing**:
1. Người dùng chọn bậc Lifetime ở WF-010 → chuyển WF-011.
2. WF-011 nêu rõ **"một lần, không tự động gia hạn"**; **loại bỏ** hoàn toàn phần ngày gia hạn — sự thiếu vắng đó chính là thông điệp.
3. Ghi `price_confirmed`; StoreKit xử lý non-consumable.
4. Sau khi thành công: entitlement chuyển sang `lifetime`; toàn bộ tính năng Premium mở **vĩnh viễn**, **không phụ thuộc kết nối mạng** về sau (dùng cache đã xác thực, xem BR-043.3).
5. Nếu người dùng đang có subscription: nhắc huỷ subscription kèm lối vào WF-025, để không trả trùng.
6. Phục hồi giao dịch trên thiết bị khác cùng Apple ID: bàn giao FR-003.

**Output**:
- Entitlement `lifetime` bền vững, phục hồi được trên thiết bị khác
- Người dùng đang có subscription được nhắc huỷ

**Business Rules**:
- **BR-054.1**: Lifetime **không có trial** và **không có ngày gia hạn**; hiển thị hai thứ đó là sai bản chất giao dịch.
- **BR-054.2**: Lifetime mở khóa **vĩnh viễn**; **cấm** hạ xuống Free khi offline.
- **BR-054.3**: Nếu có cả Lifetime và subscription, Lifetime **bao trùm**; hệ thống phải nhắc huỷ subscription.

**Validation Rules**:
- **VR-054.1**: Lifetime dùng product loại **non-consumable**; dùng loại subscription cho bậc này là lỗi cấu hình App Store Connect.

**Error Handling**:
- **ERR-054.1** (từ AF-030.1): Đang có subscription → nhắc huỷ kèm lối vào WF-025.
- **ERR-054.2** (từ AF-030.2): Cài lại app → phục hồi giao dịch trả lại Lifetime (FR-003).
- **ERR-054.3** (từ AF-030.3): Thanh toán thất bại → như ERR-049.1.

**Acceptance Criteria**:
- **AC-026.3**: IF bậc đã chọn là Lifetime THEN WF-011 nêu rõ đây là giao dịch một lần và **không** hiển thị ngày gia hạn.
- **AC-030.1**: WHEN người dùng mua Lifetime THEN hệ thống nêu rõ đây là giao dịch một lần và **không** hiển thị bất kỳ ngày gia hạn nào.
- **AC-030.2**: WHEN Lifetime được mua THEN toàn bộ tính năng Premium mở khóa vĩnh viễn, không phụ thuộc kết nối mạng sau đó.
- **AC-030.3**: IF người dùng đang có subscription khi mua Lifetime THEN hệ thống nhắc huỷ subscription kèm lối vào WF-025.

> **AC-030.4** (phục hồi Lifetime sau khi cài lại) được hiện thực ở **FR-003**. Không nhân bản ở đây.

---

## Tổng hợp nhóm

| FR | Priority | UC nguồn | Số BR | Số VR | Số ERR | AC mang từ UC |
|---|---|---|---|---|---|---|
| FR-043 | High | UC-024 | 4 | 2 | 2 | AC-024.2 |
| FR-044 | High | UC-024 | 3 | 1 | 2 | AC-024.3, AC-024.5 |
| FR-045 | High | UC-024, UC-025 | 4 | 1 | 3 | AC-024.1, AC-024.4, AC-025.6 |
| FR-046 | High | UC-025 | 4 | 2 | 3 | AC-025.1, AC-025.2, AC-025.4 |
| FR-047 | High | UC-025 | 3 | 1 | 2 | AC-025.3, AC-025.5 |
| FR-048 | High | UC-026 | 3 | 2 | 3 | AC-026.1, AC-026.2, AC-026.5 |
| FR-049 | High | UC-026 | 3 | 1 | 3 | AC-026.4 |
| FR-050 | High | UC-026 | 2 | 1 | 2 | AC-026.6 |
| FR-051 | High | UC-027 | 5 | 1 | 4 | AC-027.1 → AC-027.5 |
| FR-052 | Medium | UC-028 | 4 | 1 | 3 | AC-028.1 → AC-028.4 |
| FR-053 | Medium | UC-029 | 4 | 1 | 4 | AC-029.1 → AC-029.4 |
| FR-054 | Medium | UC-030, UC-026 | 3 | 1 | 3 | AC-026.3, AC-030.1, AC-030.2, AC-030.3 |

**Tổng nhóm**: 12 FR (9 High, 3 Medium) · 42 BR · 15 VR · 34 ERR · **33 AC** trong nhóm này, cộng **AC-029.5** và **AC-030.4** được hiện thực ở FR-003 ⇒ đủ toàn bộ **35 AC** của UC-024 → UC-030.

**Bốn ràng buộc cứng của nhóm, kiểm ở code review**: (1) chỉ có **một** điểm gọi StoreKit purchase và nó nằm sau WF-011 (VR-048.2); (2) **không** product weekly trong cấu hình App Store Connect (VR-046.1); (3) **không** đường mở paywall nào từ bề mặt CarPlay (BR-045.3); (4) giá **chỉ** đến từ `Product.displayPrice` (VR-046.2, BR-047.1).
