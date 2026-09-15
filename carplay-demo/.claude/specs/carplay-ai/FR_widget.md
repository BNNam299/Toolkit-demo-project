# FR — Widget CarPlay & Tương Thích

**Sub-spec của**: [`Functional_Requirements.md`](./Functional_Requirements.md) · **Version** 2.4 · **Snapshot** 2026-08-07
**Phạm vi**: FR-021 → FR-032 · **UC nguồn**: UC-012 → UC-017 · **PRD Feature**: F2, F10
**Màn hình liên quan**: WF-006, WF-008, WF-010, WF-014, WF-017, WF-019, WF-023, WF-024, WF-028, WF-030

> **Nhóm rủi ro cao nhất của dự án.** R-11 (phân mảnh màn hình CarPlay) là rủi ro `High/High` và là complaint kỹ thuật số 1 của đối thủ. Hai ràng buộc bao trùm cả nhóm: **(1) không tồn tại hằng số kích thước màn hình xe trong code layout** (NFR-021); **(2) không có đường nào dẫn tới màn hình trắng** (NFR-020).

---

## FR-021: Preset widget gợi ý theo xe đã chọn 📱

**Source UC**: UC-012
**Priority**: High · **Status**: Planned

**Description**:
Hệ thống phải hiển thị ≥ 3 preset widget gợi ý dựa trên xe người dùng đã chọn ngay khi mở trình tạo widget, để việc "tạo widget" giống việc **chọn** hơn là việc **dựng**. Tuyệt đối không có canvas rỗng.

**Input**:
- `selectedVehicle` (từ FR-004) và ảnh xe đã gán (từ FR-005)
- Danh mục preset widget: `id`, `type` (carPhoto / personalPhoto / counter), `tier` (free/premium), `layoutSpec`
- Kích thước màn hình xe đã ghi nhận (nếu có, từ FR-029)
- Widget hiện tại (nếu đã có)

**Processing**:
1. Nạp danh mục preset widget; lọc ra ≥ 3 preset phù hợp với `segment` của xe đã chọn.
2. Nếu chưa có widget: hiển thị hàng preset gợi ý ở Zone C và nạp preset đầu tiên vào preview Zone A — **preview có nội dung ngay từ giây đầu**.
3. Nếu đã có widget: nạp widget hiện tại vào Zone A; nút chính đổi nhãn thành "Lưu thay đổi".
4. Người dùng chạm một preset → cập nhật preview tại chỗ bằng crossfade 0,25s (sub-flow SF-007).
5. Nếu preset thuộc Premium: preview hiển thị **đầy đủ**, nút chính đổi thành "Mở khoá" và dẫn WF-010 kèm ngữ cảnh đúng loại widget đó.
6. Nếu người dùng vào từ thẻ widget trên WF-006 (đổi nhanh), nạp sẵn widget hiện tại và cho lưu chỉ với 2 chạm.
7. Người dùng chạm "Lưu widget" → bàn giao FR-022.

**Output**:
- Cấu hình widget được chọn (type + ảnh + lớp thông tin), sẵn sàng để lưu
- Người dùng **chưa bao giờ** phải đối diện canvas rỗng

**Business Rules**:
- **BR-021.1**: Hệ thống **cấm** hiển thị canvas rỗng ở WF-008. Đây là phản ứng trực tiếp với complaint *"you had to create it yourself"* của đối thủ.
- **BR-021.2**: Số preset gợi ý ≥ 3 tại mọi thời điểm, kể cả khi xe của người dùng dùng ảnh silhouette.
- **BR-021.3**: Preset Premium phải **xem trước được đầy đủ** trước khi trả tiền.

**Validation Rules**:
- **VR-021.1**: `layoutSpec` của mỗi preset phải khai báo thứ tự ưu tiên của các phần tử, để FR-030 biết bỏ phần tử nào trước khi thiếu chỗ.

**Error Handling**:
- **ERR-021.1** (từ AF-012.2): Preset thuộc Premium → xem trước đầy đủ, nút chuyển "Mở khoá", **không** lưu.
- **ERR-021.2** (từ AF-012.3): Người dùng thoát giữa lúc tạo → giữ bản nháp; lần mở lại hỏi "Tiếp tục widget đang làm?".
- **ERR-021.3** (từ State Variation WF-008 "First Visit"): Không nạp được preset gợi ý → dùng preset mặc định của app kèm ảnh silhouette; **không** để Zone A trống.

**Acceptance Criteria**:
- **AC-012.1**: WHEN người dùng mở WF-008 lần đầu THEN hệ thống hiển thị ≥ 3 preset gợi ý dựa trên xe đã chọn, và **không** hiển thị canvas rỗng.
- **AC-012.6**: WHEN widget được lưu THEN widget ở gói Free là widget **đầy đủ chức năng**, không có watermark và không bị làm mờ.

---

## FR-022: Lưu cấu hình widget vào App Group 📱

**Source UC**: UC-012
**Priority**: High · **Status**: Planned

**Description**:
Hệ thống phải ghi cấu hình widget vào App Group container **ngay tại thời điểm người dùng lưu**, không chờ app vào background — vì widget extension chạy trong tiến trình riêng và chỉ đọc được qua container này.

**Input**:
- Cấu hình widget: `type`, `imagePath`, `infoLayers` (mảng phần tử kèm thứ tự ưu tiên), `presetId`
- Đường dẫn App Group container

**Processing**:
1. Ghi cấu hình dưới dạng file trong App Group container, kèm số phiên bản schema.
2. Ghi ảnh đã nén (từ FR-028) vào cùng container.
3. Gọi `WidgetCenter.shared.reloadAllTimelines()` để widget cập nhật.
4. Xác nhận ghi thành công bằng cách đọc lại; nếu đọc lại không khớp, coi là thất bại.
5. Hiển thị WF-030 toast; cập nhật thẻ widget trên WF-006.
6. Ghi `free_tier_widget_used` nếu entitlement hiện tại là Free.

**Output**:
- Cấu hình và ảnh nằm trong App Group, đọc được từ widget extension
- Widget sẵn sàng render ở lần cắm CarPlay kế tiếp

**Business Rules**:
- **BR-022.1**: Ghi phải hoàn tất **ngay tại thời điểm lưu**; ghi lười lúc app vào background sẽ làm widget dùng cấu hình cũ ở chuyến kế tiếp.
- **BR-022.2**: Cấu hình mang số phiên bản schema, để bản app mới đọc được cấu hình do bản cũ ghi.
- **BR-022.3**: Ghi thất bại **không được** làm mất bản nháp đang làm.

**Validation Rules**:
- **VR-022.1**: Tổng dung lượng ghi vào App Group cho một widget ≤ 2MB (xem AC-NFR-007.2).
- **VR-022.2**: Sau khi ghi, đọc lại phải khớp; không khớp thì báo thất bại thay vì báo thành công.

**Error Handling**:
- **ERR-022.1** (từ State Variation WF-008 "Error"): Ghi App Group thất bại → nêu lỗi cụ thể kèm nút thử lại; **giữ bản nháp**.
- **ERR-022.2** (từ Recovery Path TF-004): Đọc lại không khớp → coi là thất bại, không hiển thị toast thành công.

**Acceptance Criteria**:
- **AC-012.2**: WHEN widget được lưu THEN cấu hình được ghi vào App Group container ngay tại thời điểm lưu, không chờ app vào background.

---

## FR-023: Giới hạn số widget theo entitlement 📱

**Source UC**: UC-012
**Priority**: High · **Status**: Planned

**Description**:
Hệ thống phải cưỡng chế giới hạn 1 widget ở gói Free bằng cách cho **đổi** widget hiện có (không chặn hoàn toàn), và phải giữ nguyên mọi cấu hình khi người dùng hạ cấp từ Premium về Free.

**Input**:
- Entitlement hiện tại từ FR-043
- Số widget đã cấu hình (`widgetConfigs.count`)

**Processing**:
1. Hỏi `EntitlementService` giới hạn widget cho entitlement hiện tại: Free = 1, Premium/Lifetime = không giới hạn.
2. Nếu Free và đã có 1 widget: hiển thị `LimitNotice` nêu rõ giới hạn, và **cho phép đổi** widget hiện có.
3. Nút "Thêm widget thứ hai" dẫn WF-010 với `trigger_source = widget_limit`.
4. Nếu người dùng hạ cấp (trial hết, về Free) trong khi có nhiều widget: **giữ nguyên tất cả cấu hình**, chỉ kích hoạt 1 widget; không xoá dữ liệu.
5. Khi người dùng nâng cấp lại, các widget đã lưu được kích hoạt lại nguyên trạng.
6. Ghi `free_tier_widget_used` mỗi lần widget ở gói Free được dùng trên xe.

**Output**:
- Số widget được kích hoạt đúng theo entitlement; cấu hình vượt giới hạn được bảo toàn
- Event `free_tier_widget_used` được ghi khi áp dụng

**Business Rules**:
- **BR-023.1**: Widget ở gói Free là widget **đầy đủ chức năng** — không watermark, không làm mờ, không giới hạn thời gian.
- **BR-023.2**: Hạ cấp **không bao giờ xoá** cấu hình widget của người dùng.
- **BR-023.3**: Giới hạn được cưỡng chế trong `EntitlementService`, **không** rải rác trong View (xem `Project_Overview.md` §3.3 Quyết định 5).

**Validation Rules**:
- **VR-023.1**: Số widget kích hoạt ≤ giới hạn của entitlement hiện tại tại mọi thời điểm.

**Error Handling**:
- **ERR-023.1** (từ AF-012.1): Free đã dùng hết 1 widget → cho đổi, nêu rõ giới hạn, không xoá widget đang có.
- **ERR-023.2** (từ State Variation FR-023 "Returning (hạ cấp)"): Trial hết với 3 widget → giữ cả 3 cấu hình, kích hoạt 1.
- **ERR-023.3** (từ ERR-010.1): Entitlement không đọc được → mặc định về Free và vẫn cho dùng 1 widget.

**Acceptance Criteria**:
- **AC-012.3**: IF người dùng ở gói Free và đã có 1 widget THEN hệ thống cho phép đổi widget đó và nêu rõ giới hạn 1 widget, không xoá widget đang có.
- **AC-012.5**: WHEN người dùng dùng widget ở gói Free THEN hệ thống ghi `free_tier_widget_used`.

---

## FR-024: Xử lý ngưỡng iOS 17.4 cho widget CarPlay 📱🚗

**Source UC**: UC-012 (AF-012.4)
**Priority**: High · **Status**: Planned

**Description**:
Hệ thống phải xử lý khoảng cách giữa hai ngưỡng iOS (app 16.4+, widget CarPlay 17.4+) bằng **suy giảm có thông báo**: nêu rõ yêu cầu phiên bản, vẫn cho cấu hình và lưu, và **không giả vờ** widget đang chạy.

**Input**:
- Phiên bản iOS của thiết bị (`ProcessInfo.processInfo.operatingSystemVersion`)
- Cấu hình widget đã lưu (nếu có)

**Processing**:
1. Kiểm khả dụng WidgetKit-trên-CarPlay bằng `if #available(iOS 17.4, *)`.
2. Nếu < 17.4: hiển thị `VersionNotice` ở WF-008 Zone D nêu rõ yêu cầu iOS 17.4+, và **vẫn cho phép** cấu hình và lưu.
3. Trên bề mặt CarPlay, vùng widget hiển thị thông báo yêu cầu phiên bản — **không crash, không màn trắng**.
4. Sound (FR-016, FR-019), giọng chào (FR-037), thư viện xe (FR-004) và dashboard (FR-040) vẫn hoạt động đầy đủ.
5. Sau khi người dùng nâng cấp iOS, cấu hình đã lưu được render ngay ở lần cắm kế tiếp — **không** yêu cầu cấu hình lại.

**Output**:
- Người dùng iOS 16.4–17.3 dùng được mọi tính năng trừ widget CarPlay, và biết chính xác vì sao
- Cấu hình widget được bảo toàn để dùng ngay sau khi nâng cấp iOS

**Business Rules**:
- **BR-024.1**: **Cấm** đặt deployment target lên 17.4 — làm vậy sẽ cắt một phần thị trường ở giai đoạn cần install nhất (`Project_Overview.md` §3.3 Quyết định 1).
- **BR-024.2**: **Cấm** hiển thị widget như đang hoạt động khi phiên bản iOS không hỗ trợ. Nói dối ở đây tạo đúng loại review 1★ mà R-11 đang muốn tránh.
- **BR-024.3**: Mọi API chỉ có từ 17.4 phải nằm trong kiểm tra khả dụng; gọi trực tiếp là lỗi build-review.

**Validation Rules**:
- **VR-024.1**: Cấu hình widget lưu trên iOS < 17.4 phải dùng cùng schema với bản lưu trên 17.4+, để không cần chuyển đổi khi nâng cấp.

**Error Handling**:
- **ERR-024.1** (từ AF-012.4): iOS < 17.4 → `VersionNotice`, vẫn cho cấu hình; vùng widget trên xe hiện thông báo phiên bản.
- **ERR-024.2** (từ State Variation FR-024 "Returning"): Sau khi nâng cấp iOS → widget render ngay ở lần cắm kế tiếp.

**Acceptance Criteria**:
- **AC-012.4**: IF phiên bản iOS < 17.4 THEN WF-008 nêu rõ widget CarPlay yêu cầu iOS 17.4+, và các tính năng còn lại vẫn dùng được.

---

## FR-025: Preview widget theo tỉ lệ màn hình xe 📱

**Source UC**: UC-013
**Priority**: High · **Status**: Planned

**Description**:
Hệ thống phải cho người dùng thấy widget của họ ở đúng tỉ lệ màn hình xe **trước khi ra xe**, dùng kích thước thật nếu đã từng cắm xe, hoặc ≥ 4 tỉ lệ tham chiếu kèm nhãn nói rõ đây là ước lượng.

**Input**:
- Cấu hình widget hiện tại
- Danh sách kích thước scene **đã ghi nhận** từ các phiên CarPlay trước (từ FR-029), có thể rỗng
- Bộ ≥ 4 tỉ lệ tham chiếu của test matrix
- Chế độ hiển thị đang xem: dark / light

**Processing**:
1. Mở WF-023 dạng modal.
2. Nếu có ≥ 1 kích thước đã ghi nhận: chọn kích thước gần nhất làm tỉ lệ mặc định; nhãn Zone D ghi **"kích thước thật của xe bạn"**.
3. Nếu chưa có kích thước nào: dùng ≥ 4 tỉ lệ tham chiếu; nhãn ghi rõ **"ước lượng"**.
4. Người dùng vuốt ngang để chuyển tỉ lệ (sub-flow SF-009); công tắc dark/light đổi mode mà **giữ nguyên** tỉ lệ đang xem.
5. Người dùng đổi loại widget hoặc đổi ảnh **ngay trong modal** (dẫn FR-027) — sửa tại nơi phát hiện vấn đề, không quay về WF-008.
6. Với mỗi tỉ lệ, bàn giao FR-026 để kiểm phần tử vượt vùng an toàn.
7. Người dùng chạm "Dùng bản này" → trả cấu hình đã xác nhận về WF-008.

**Output**:
- Người dùng đã xem widget ở ≥ 1 tỉ lệ và biết tỉ lệ đó là thật hay ước lượng
- Cấu hình được xác nhận hoặc đã sửa

**Business Rules**:
- **BR-025.1**: Hệ thống **phải nói rõ** tỉ lệ đang xem là thật hay ước lượng. Tuyên bố chính xác khi chưa có dữ liệu là nói quá.
- **BR-025.2**: Toàn bộ layout trong preview được tính từ tỉ lệ đang chọn **tại runtime**, dùng đúng engine với FR-029 — nếu dùng engine khác, preview sẽ nói dối.
- **BR-025.3**: Nếu người dùng có nhiều kích thước đã ghi nhận (nhiều xe), cho chọn giữa các kích thước **đã từng gặp**.

**Validation Rules**:
- **VR-025.1**: Bộ tỉ lệ tham chiếu phải có ≥ 4 phần tử và **phải bao gồm** nhóm màn 8" (nhóm đã ghi nhận lỗi ở đối thủ).

**Error Handling**:
- **ERR-025.1** (từ AF-013.1): Có phần tử vượt vùng an toàn → bàn giao FR-026.
- **ERR-025.2** (từ AF-013.2): Người dùng sửa ngay trong preview → cập nhật tại chỗ, không rời modal.
- **ERR-025.3** (từ AF-013.3): Kích thước chưa từng thấy → vẫn tính được vì layout dựa trên bounds, không dựa danh sách xe.

**Acceptance Criteria**:
- **AC-013.1**: IF app đã từng nhận kích thước scene từ xe của người dùng THEN WF-023 dùng đúng kích thước đó làm tỉ lệ mặc định của preview.
- **AC-013.2**: IF app chưa từng nhận kích thước scene nào THEN WF-023 nêu rõ preview là ước lượng và hiển thị ≥ 4 tỉ lệ tham chiếu.
- **AC-013.4**: WHEN preview được hiển thị THEN toàn bộ layout được tính từ tỉ lệ đang chọn tại runtime, không dùng bất kỳ hằng số kích thước nào.

---

## FR-026: Phát hiện và báo phần tử vượt vùng an toàn 📱🚗

**Source UC**: UC-013
**Priority**: High · **Status**: Planned

**Description**:
Hệ thống phải phát hiện phần tử nào vượt vùng an toàn ở một tỉ lệ nhất định, **chỉ rõ phần tử đó cho người dùng**, và tuyệt đối không tự âm thầm cắt nội dung.

**Input**:
- `layoutSpec` của widget: danh sách phần tử kèm **thứ tự ưu tiên**
- Kích thước khả dụng (width × height) và insets vùng an toàn
- Cài đặt Dynamic Type hiện tại

**Processing**:
1. Tính khung của từng phần tử theo kích thước khả dụng.
2. So khung từng phần tử với vùng an toàn; ghi nhận phần tử vượt.
3. Nếu có phần tử vượt: viền cảnh báo phần tử đó (fade 0,2s, **không nhấp nháy**) và hiển thị **tên phần tử** kèm lý do (sub-flow SF-008).
4. Cho người dùng bật/tắt từng lớp thông tin để tự giảm bớt, hoặc chạm "Giảm bớt phần tử này" để hệ thống bỏ phần tử ưu tiên thấp nhất.
5. Với phần tử là chữ: co theo Dynamic Type rồi **truncate có ellipsis**, không cắt giữa chữ.
6. Nếu mọi cách đều không đủ chỗ: nêu rõ cấu hình này sẽ dùng bản giảm cấp trên xe đó — **nói trước**, không để người dùng phát hiện trên đường.
7. Cho phép hoàn tác bằng "Thêm lại phần tử".

**Output**:
- Danh sách phần tử vượt vùng an toàn (có thể rỗng) kèm gợi ý sửa
- Cấu hình sau khi sửa, hoặc cảnh báo rằng bản giảm cấp sẽ được dùng

**Business Rules**:
- **BR-026.1**: **Cấm** tự cắt nội dung mà không thông báo. Cắt im lặng chính là hành vi tạo ra complaint "chữ bị cắt" của đối thủ.
- **BR-026.2**: Chữ luôn truncate **có ellipsis**; cắt giữa chữ là lỗi.
- **BR-026.3**: Viền cảnh báo dùng fade, **không nhấp nháy** — nhấp nháy tạo cảm giác lỗi nghiêm trọng không đúng mức.

**Validation Rules**:
- **VR-026.1**: Mọi phần tử trong `layoutSpec` phải có thứ tự ưu tiên; phần tử không có ưu tiên khiến FR-030 không biết bỏ cái nào — đây là lỗi dữ liệu ở giai đoạn build.
- **VR-026.2**: Phép kiểm phải chạy ở **cả** mức Dynamic Type mặc định và mức lớn nhất.

**Error Handling**:
- **ERR-026.1** (từ AF-013.1): Phần tử vượt vùng → chỉ rõ phần tử + đề xuất giảm bớt.
- **ERR-026.2** (từ SF-008 Recovery): Mọi cách đều không đủ chỗ → nêu rõ sẽ dùng bản giảm cấp trên xe đó.

**Acceptance Criteria**:
- **AC-013.3**: WHEN có phần tử vượt vùng an toàn ở một tỉ lệ THEN hệ thống chỉ rõ phần tử đó và **không** tự cắt nội dung mà không thông báo.

---

## FR-027: Chọn ảnh và crop theo tỉ lệ màn hình xe 📱

**Source UC**: UC-014
**Priority**: Medium · **Status**: Planned

**Description**:
Hệ thống phải cho người dùng chọn ảnh xe theo model (không cần quyền thư viện ảnh) hoặc ảnh cá nhân, và phải **hiện trước vùng sẽ bị cắt** theo đúng tỉ lệ màn hình xe trước khi lưu.

**Input**:
- Nguồn ảnh: bộ ảnh xe theo model (từ FR-005) hoặc thư viện ảnh của người dùng
- Tỉ lệ màn hình xe đang chọn (từ FR-025)
- Trạng thái quyền thư viện ảnh

**Processing**:
1. Mở WF-024 với hai lựa chọn: ảnh xe theo model, hoặc ảnh từ thư viện.
2. Hiển thị hàng ảnh xe theo model cuộn ngang — dùng được **không cần quyền** thư viện ảnh.
3. Nếu người dùng chọn ảnh cá nhân: yêu cầu quyền thư viện; nếu bị từ chối, chỉ dùng được ảnh xe theo model và **luồng không bị chặn**.
4. Sau khi có ảnh: đặt khung crop theo đúng tỉ lệ màn hình xe, **làm tối rõ ràng vùng sẽ bị cắt** (sub-flow SF-010); cho kéo, zoom, xoay và "Đặt lại khung".
5. Bàn giao FR-028 để kiểm độ phân giải và nén.
6. Người dùng chạm "Xong" → trả ảnh đã crop về WF-008 hoặc WF-023.

**Output**:
- Ảnh đã crop theo đúng tỉ lệ màn hình xe, đã nén dưới ngưỡng an toàn
- Người dùng đã thấy trước phần nào của ảnh sẽ mất

**Business Rules**:
- **BR-027.1**: Vùng bị cắt phải hiển thị **trước khi lưu**; cắt xong mới cho biết là quá muộn.
- **BR-027.2**: Ảnh xe theo model là mặc định và dùng được **không cần quyền nào** — người dùng có kết quả tốt mà không phải đánh đổi quyền riêng tư.
- **BR-027.3**: Ảnh cá nhân thuộc Premium; **xem trước và crop được đầy đủ**, chỉ chặn ở bước lưu.

**Validation Rules**:
- **VR-027.1**: Khung crop luôn giữ đúng tỉ lệ màn hình xe đang chọn; người dùng không thể tạo khung sai tỉ lệ.
- **VR-027.2**: Chỉ nhận định dạng ảnh mà hệ thống hỗ trợ; định dạng lạ bị từ chối kèm lý do rõ.

**Error Handling**:
- **ERR-027.1** (từ AF-014.2): Quyền thư viện ảnh bị từ chối → chỉ dùng ảnh xe theo model; nêu rõ lý do, không chặn luồng.
- **ERR-027.2** (từ AF-014.3): Ảnh cá nhân thuộc Premium → xem trước đầy đủ, lưu thì dẫn WF-010.
- **ERR-027.3** (từ SF-010 Recovery): Người dùng muốn bắt đầu lại → "Đặt lại khung" trả về khung mặc định.

**Acceptance Criteria**:
- **AC-014.1**: WHEN người dùng chọn ảnh cá nhân THEN hệ thống hiển thị vùng sẽ bị cắt **trước** khi lưu.
- **AC-014.4**: IF quyền thư viện ảnh bị từ chối THEN người dùng vẫn dùng được ảnh xe theo model và luồng không bị chặn.

---

## FR-028: Kiểm độ phân giải và nén ảnh widget 📱

**Source UC**: UC-014
**Priority**: Medium · **Status**: Planned

**Description**:
Hệ thống phải cảnh báo khi ảnh có độ phân giải thấp hơn ngưỡng cần cho màn hình xe lớn nhất trong test matrix, và phải nén ảnh xuống dưới ngưỡng an toàn của widget extension trước khi ghi vào App Group.

**Input**:
- Ảnh đã crop từ FR-027 (kích thước pixel, định dạng)
- Ngưỡng độ phân giải tối thiểu = kích thước màn hình xe lớn nhất trong test matrix × scale
- Ngưỡng dung lượng sau nén: **≤ 2MB**

**Processing**:
1. So kích thước pixel của ảnh đã crop với ngưỡng tối thiểu.
2. Nếu thấp hơn: cảnh báo ảnh **sẽ bị mờ trên màn hình xe**, nêu rõ mức tối thiểu cần thiết, và đề nghị chọn ảnh khác.
3. Cảnh báo mờ **không chặn** việc lưu — người dùng vẫn được quyết định, nhưng đã được báo trước.
4. Nén ảnh (giảm kích thước và điều chỉnh chất lượng) xuống ≤ 2MB.
5. Nếu sau nén vẫn vượt ngưỡng: giảm tiếp kích thước pixel cho tới khi đạt, ưu tiên giữ dưới ngưỡng bộ nhớ của widget extension.
6. Bàn giao FR-022 để ghi vào App Group.

**Output**:
- Ảnh có dung lượng ≤ 2MB, sẵn sàng cho widget extension
- Người dùng đã được cảnh báo nếu ảnh sẽ bị mờ

**Business Rules**:
- **BR-028.1**: Ngưỡng bộ nhớ của widget extension thắng mọi ưu tiên khác về chất lượng ảnh — vượt ngưỡng thì widget bị hệ thống kill và biểu hiện ra ngoài **giống hệt lỗi render** (rủi ro thực thi A ở `Project_Overview.md` §8).
- **BR-028.2**: Cảnh báo độ phân giải là **cảnh báo**, không phải chặn; quyền quyết định thuộc người dùng.

**Validation Rules**:
- **VR-028.1**: Dung lượng ảnh sau nén ≤ 2MB — bắt buộc, không có ngoại lệ.
- **VR-028.2**: Kích thước pixel sau nén ≥ 50% ngưỡng tối thiểu; nếu không đạt, từ chối ảnh kèm lý do rõ thay vì lưu một ảnh chắc chắn mờ.

**Error Handling**:
- **ERR-028.1** (từ AF-014.1): Ảnh độ phân giải thấp → cảnh báo sẽ mờ trên màn hình xe, đề nghị chọn ảnh khác.
- **ERR-028.2** (từ AF-014.4): Ảnh quá lớn → tự giảm kích thước trước khi ghi vào App Group.

**Acceptance Criteria**:
- **AC-014.2**: IF ảnh có độ phân giải thấp hơn ngưỡng cần cho màn hình xe lớn nhất trong test matrix THEN hệ thống cảnh báo trước khi lưu.
- **AC-014.3**: WHEN ảnh được lưu THEN dung lượng sau nén nằm dưới ngưỡng an toàn của widget extension.

---

## FR-029: Render widget theo scene bounds tại runtime 🚗

**Source UC**: UC-015
**Priority**: High · **Status**: Planned

**Description**:
Hệ thống phải đọc kích thước từ `CPTemplateApplicationScene` bounds (hoặc container size của WidgetKit) **tại runtime** và tính toàn bộ layout từ đó. **Không tồn tại hằng số kích thước màn hình xe nào trong đường render.** Đây là biện pháp giảm thiểu chính cho R-11.

**Input**:
- `CPTemplateApplicationScene` bounds (width, height) — đọc tại thời điểm scene active
- Cấu hình widget từ App Group (từ FR-022)
- Cài đặt Dynamic Type và chế độ dark/light của hệ thống xe

**Processing**:
1. Khi CarPlay scene active, đọc bounds; **không** tra bảng xe, **không** dùng giá trị mặc định.
2. Tính insets vùng an toàn từ bounds.
3. Tính khung của từng phần tử theo `layoutSpec` và kích thước thật vừa đọc.
4. Bàn giao FR-026 để kiểm phần tử vượt vùng an toàn; nếu có, bàn giao FR-030 để giảm cấp.
5. Render widget: ảnh ở Zone A, lớp thông tin ở Zone B; chữ co theo Dynamic Type; truncate có ellipsis khi cần.
6. Bảo đảm mọi touch target ≥ 44pt và widget đúng ở **cả** dark và light mode.
7. Nếu render thành công: ghi `widget_render_ok` kèm `screen_width`, `screen_height`, `widget_type`, `car_make` (nếu suy được), và **lưu kích thước này** để FR-025 dùng làm tỉ lệ preview.
8. Nếu thất bại: ghi `widget_render_failed` kèm `screen_width`, `screen_height`, `widget_type`, `failure_reason` — **phân biệt** `overflow` với `memory`; bàn giao FR-031.

**Output**:
- Widget hiển thị đúng trong bounds, không nội dung nào bị cắt
- Kích thước màn hình xe được lưu để dùng cho preview về sau
- Một trong hai event render được ghi, đủ dữ liệu để chẩn đoán trong 24h

**Business Rules**:
- **BR-029.1**: **Cấm** mọi hằng số kích thước màn hình xe trong code layout CarPlay. Đây là mục kiểm ở code review (AC-NFR-021.1), không phải kiểm tại runtime.
- **BR-029.2**: **Cấm** tra bảng theo hãng/model xe để quyết định layout — kích thước phải đến từ bounds thật.
- **BR-029.3**: Widget extension **không** nạp mô hình Core ML và **không** gọi mạng (AC-NFR-007.4).
- **BR-029.4**: `failure_reason` phải phân biệt được `overflow` và `memory`; gộp hai nguyên nhân này lại sẽ làm chẩn đoán R-11 sai hướng.

**Validation Rules**:
- **VR-029.1**: Bounds đọc được phải có width > 0 và height > 0; giá trị không hợp lệ được coi là thất bại render, không phải lý do dùng giá trị mặc định.
- **VR-029.2**: Với **mọi** cặp (width, height) trong dải hợp lệ, không phần tử nào được vượt bounds — kiểm bằng property-based test (AC-NFR-024.3).

**Error Handling**:
- **ERR-029.1** (từ AF-015.1): Phần tử vượt bounds → bàn giao FR-030 (giảm cấp), rồi FR-031 nếu vẫn thất bại.
- **ERR-029.2** (từ AF-015.2): Kích thước chưa từng gặp → vẫn render bình thường; ghi kích thước mới vào telemetry.
- **ERR-029.3** (từ AF-015.3): Widget extension bị thu hồi vì bộ nhớ → ghi `failure_reason = memory`, bàn giao FR-031.
- **ERR-029.4** (từ AF-015.4): Người dùng ở gói Free → render widget đầy đủ chức năng kèm WF-018 (bàn giao FR-041).

**Acceptance Criteria**:
- **AC-015.1**: WHEN CarPlay scene active THEN layout được tính từ `CPTemplateApplicationScene` bounds tại runtime; **không có hằng số kích thước nào** trong đường render.
- **AC-015.2**: WHEN widget render THEN không có nội dung nào bị cắt ở bất kỳ kích thước nào trong test matrix (≥ 4 kích thước + 1 xe thật mỗi nhóm).
- **AC-015.4**: WHEN widget render THEN mọi touch target ≥ 44pt và widget hiển thị đúng ở cả dark mode và light mode.
- **AC-015.5**: WHEN render thành công THEN hệ thống ghi `widget_render_ok` kèm `screen_width`, `screen_height`, `widget_type`.
- **AC-015.7**: WHEN tính trên toàn bộ phiên có kết nối CarPlay THEN Widget Render Success Rate ≥ 90% ở tháng 3 và ≥ 95% ở tháng 6.

---

## FR-030: Giảm cấp layout khi thiếu không gian 🚗

**Source UC**: UC-015 (AF-015.1)
**Priority**: High · **Status**: Planned

**Description**:
Khi không đủ chỗ cho mọi phần tử, hệ thống phải giảm cấp layout theo thứ tự ưu tiên đã định (bỏ phần tử ưu tiên thấp nhất → co chữ theo Dynamic Type → truncate có ellipsis) rồi render lại — trước khi kết luận là thất bại.

**Input**:
- `layoutSpec` với thứ tự ưu tiên của từng phần tử
- Kích thước khả dụng và kết quả kiểm của FR-026
- Số vòng giảm cấp đã thực hiện

**Processing**:
1. Nhận báo cáo phần tử vượt vùng an toàn từ FR-026.
2. Vòng 1: bỏ phần tử có ưu tiên **thấp nhất**; tính lại layout.
3. Vòng 2: nếu vẫn vượt, co chữ theo Dynamic Type xuống mức tối thiểu đọc được (≥ 16pt trên màn hình xe).
4. Vòng 3: nếu vẫn vượt, truncate chữ **có ellipsis**.
5. Tối đa **3 vòng** giảm cấp; nếu sau 3 vòng vẫn vượt, kết luận thất bại và bàn giao FR-031.
6. Nếu render thành công sau giảm cấp: ghi `widget_render_ok` kèm **cờ đã giảm cấp**, để phân biệt với render đầy đủ.

**Output**:
- Widget render được ở dạng giảm cấp, hoặc kết luận thất bại và chuyển FR-031
- Telemetry phân biệt render đầy đủ với render đã giảm cấp

**Business Rules**:
- **BR-030.1**: Thứ tự bỏ phần tử tuân theo `layoutSpec`, **không** tuỳ ý theo runtime — để hành vi có thể dự đoán và test được.
- **BR-030.2**: Chữ **không bao giờ** nhỏ hơn 16pt trên màn hình xe; nhỏ hơn ngưỡng đó thì chữ không còn phục vụ mục đích gì khi đang lái.
- **BR-030.3**: Số vòng giảm cấp tối đa là 3; giảm cấp vô hạn sẽ tạo widget rỗng, tệ hơn một thông báo trung thực.
- **BR-030.4**: Render sau giảm cấp được tính là **thành công** trong Widget Render Success Rate, nhưng phải mang cờ riêng để theo dõi tỉ lệ giảm cấp.

**Validation Rules**:
- **VR-030.1**: Sau mỗi vòng giảm cấp, phải kiểm lại toàn bộ phần tử — không giả định rằng bỏ một phần tử là đủ.

**Error Handling**:
- **ERR-030.1** (từ AF-015.1): Sau 3 vòng vẫn vượt bounds → bàn giao FR-031 với `failure_reason = overflow`.
- **ERR-030.2** (từ AF-015.3): Bị thu hồi vì bộ nhớ trong lúc giảm cấp → bàn giao FR-031 với `failure_reason = memory`, **không** ghi là overflow.

**Acceptance Criteria**:
- **AC-015.3**: WHEN chữ dài hơn không gian THEN chữ được truncate có ellipsis, **không** cắt giữa chữ.
- **AC-015.6**: IF render thất bại THEN hệ thống ghi `widget_render_failed` kèm `screen_width`, `screen_height`, `widget_type`, `failure_reason` phân biệt được vượt-bounds với hết-bộ-nhớ.

---

## FR-031: Fallback CarPlay khi render thất bại 🚗📱

**Source UC**: UC-016
**Priority**: High · **Status**: Planned

**Description**:
Khi widget không render được, hệ thống phải hiển thị thông báo bằng chữ trên màn hình xe nêu rõ **đây là vấn đề tương thích màn hình**, không yêu cầu bất kỳ thao tác nào khi đang lái, và đưa người dùng tới màn chẩn đoán khi họ mở app iPhone sau đó. **Không bao giờ để lại vùng trắng.**

**Input**:
- Kết quả thất bại từ FR-029/FR-030 kèm `failure_reason`
- Số lần thất bại liên tiếp trên cùng cặp kích thước
- Trạng thái dashboard (còn hoạt động hay không)

**Processing**:
1. Chuyển vùng widget sang WF-019 với `FallbackNotice`: nêu rõ đây là vấn đề tương thích với màn hình xe này, kèm hướng dẫn mở màn Chẩn Đoán trên iPhone.
2. `FallbackNotice` **chỉ để đọc**: không CTA, không modal, không nhập liệu — vì người dùng đang lái.
3. Nếu chỉ widget lỗi mà dashboard vẫn được: **chỉ** thay vùng widget; WF-016 hoạt động đầy đủ.
4. Đánh dấu phiên này cần chẩn đoán.
5. Ở lần mở app iPhone kế tiếp, hiển thị `WarningRow` trên WF-006 dẫn WF-014 (bàn giao FR-009 Processing 6).
6. Nếu lần render kế tiếp thành công: **tự xoá** `WarningRow`, không để lại cảnh báo giả.
7. Nếu cùng một cặp kích thước thất bại ≥ 3 lần: đánh dấu ưu tiên cao trong telemetry (bàn giao FR-066).

**Output**:
- Người dùng được thông báo bằng chữ; không có vùng trắng ở bất kỳ nhánh nào
- Telemetry đủ dữ liệu để phát hiện xe không tương thích trong 24h
- Đường dẫn tới chẩn đoán được mở khi người dùng đã đỗ xe

**Business Rules**:
- **BR-031.1**: **0 trường hợp** màn hình trắng hoặc vùng trắng trên bề mặt CarPlay, ở mọi nhánh lỗi (NFR-020).
- **BR-031.2**: Thông báo phải nói rõ **vấn đề nằm ở tương thích màn hình**; câu chung như "đã xảy ra lỗi" khiến người dùng kết luận app rác.
- **BR-031.3**: WF-019 **cấm** có CTA, modal hay nhập liệu — người dùng đang lái.
- **BR-031.4**: Lỗi widget **không** được hạ toàn bộ bề mặt CarPlay.

**Validation Rules**:
- **VR-031.1**: `FallbackNotice` phải luôn có nội dung chữ khác rỗng, ở mọi kích thước màn hình.

**Error Handling**:
- **ERR-031.1** (từ AF-016.1): Lỗi tạm thời, render kế tiếp OK → cảnh báo tự xoá.
- **ERR-031.2** (từ AF-016.2): Lỗi lặp ≥ 3 lần cùng kích thước → ưu tiên cao trong telemetry.
- **ERR-031.3** (từ AF-016.3): Chỉ widget lỗi → dashboard vẫn đầy đủ.

**Acceptance Criteria**:
- **AC-016.1**: IF widget không render được THEN hệ thống hiển thị WF-019 với thông báo bằng chữ, và **tuyệt đối không** để lại vùng trắng.
- **AC-016.2**: WHEN WF-019 hiển thị THEN nội dung chỉ để đọc, không yêu cầu người dùng nhập gì và không có modal — vì người dùng đang trong xe.
- **AC-016.3**: WHEN render thất bại THEN lần mở app iPhone kế tiếp hiển thị lối vào WF-014 trên WF-006.
- **AC-016.4**: IF lần render kế tiếp thành công THEN mọi cảnh báo trên WF-006 được xoá tự động.
- **AC-016.5**: IF chỉ widget lỗi THEN WF-016 Dashboard vẫn hoạt động đầy đủ.

---

## FR-032: Chẩn đoán tương thích và gửi báo cáo 📱

**Source UC**: UC-017
**Priority**: Medium · **Status**: Planned

**Description**:
Hệ thống phải hiển thị kích thước scene **thật** đã nhận từ xe của người dùng cùng trạng thái render các lần gần nhất, và phải cho gửi báo cáo sau khi liệt kê **từng mục** dữ liệu sẽ rời khỏi thiết bị.

**Input**:
- Lịch sử kết nối CarPlay: dấu thời gian, `screen_width`, `screen_height`, `widget_type`, kết quả render, `failure_reason`
- Phiên bản iOS, xe đã chọn
- Ghi chú tuỳ chọn do người dùng gõ (0–500 ký tự)

**Processing**:
1. Mở WF-014; hiển thị kích thước scene thật đã nhận (không phải giá trị suy đoán), phiên bản iOS, xe đã chọn.
2. Hiển thị danh sách các lần kết nối gần nhất kèm kết quả render; đánh dấu đỏ nếu lần gần nhất thất bại.
3. Người dùng chạm một dòng → mở rộng inline hiện `failure_reason` phân biệt `overflow` và `memory`; có nút "Xem widget ở kích thước này" dẫn WF-023 (sub-flow SF-016).
4. Người dùng chạm "Gửi báo cáo" → mở WF-028 liệt kê **từng mục** dữ liệu sẽ gửi; chạm một mục để xem **giá trị thật** (ví dụ `screen_width: 1280`).
5. Người dùng bỏ tick mục không muốn gửi → mục đó bị loại khỏi payload.
6. Nút "Sao chép" copy toàn bộ payload dạng chữ vào clipboard, để người dùng gửi qua kênh khác nếu muốn.
7. Nút "Xoá lịch sử chẩn đoán" xoá dữ liệu chẩn đoán cục bộ, **không** ảnh hưởng cấu hình widget hay entitlement.
8. Chạm "Gửi" → xác nhận trong ≤ 500ms **không chờ mạng**; xếp hàng on-device nếu offline.

**Output**:
- Người dùng thấy chính xác dữ liệu gì rời khỏi thiết bị và gửi đúng những gì họ đồng ý
- Báo cáo được gửi hoặc xếp hàng; payload **không** chứa PII

**Business Rules**:
- **BR-032.1**: Chỉ hiển thị **kích thước thật đã nhận**; suy đoán từ hãng/model xe là vi phạm mục đích của màn này.
- **BR-032.2**: WF-028 phải liệt kê từng mục dữ liệu **kèm giá trị thật** — đây là cách biến cam kết "không thu PII" thành thứ người dùng tự kiểm tra được.
- **BR-032.3**: Payload **không** chứa PII (NFR-011).
- **BR-032.4**: Xoá lịch sử chẩn đoán **không** ảnh hưởng cấu hình widget hay entitlement.

**Validation Rules**:
- **VR-032.1**: Ghi chú của người dùng tối đa 500 ký tự; vượt thì cắt, không gây lỗi.
- **VR-032.2**: Nếu người dùng bỏ tick hết mọi mục, nút "Gửi" bị vô hiệu kèm lời nhắc cần ít nhất kích thước màn hình để chẩn đoán được.

**Error Handling**:
- **ERR-032.1** (từ AF-017.1): Chưa từng kết nối CarPlay → hiển thị hướng dẫn cắm xe một lần, **không** hiện bảng trống.
- **ERR-032.2** (từ AF-017.2): Không có mạng → xếp hàng on-device và gửi khi có mạng.
- **ERR-032.3** (từ AF-017.3): Người dùng thêm ghi chú → chấp nhận tối đa 500 ký tự.
- **ERR-032.4** (từ AF-017.4): Người dùng không muốn gửi → đóng sheet; dữ liệu chẩn đoán **chỉ nằm trên máy**.

**Acceptance Criteria**:
- **AC-017.1**: WHEN WF-014 mở THEN hệ thống hiển thị kích thước scene thật đã nhận từ xe, không phải giá trị suy đoán.
- **AC-017.2**: WHEN WF-028 mở THEN hệ thống liệt kê **từng mục** dữ liệu sẽ gửi và báo cáo **không** chứa PII.
- **AC-017.3**: IF chưa có dữ liệu kết nối nào THEN WF-014 hiển thị hướng dẫn thay vì bảng trống.
- **AC-017.4**: WHEN báo cáo được gửi THEN người dùng nhận xác nhận trong ≤ 500ms mà không phải chờ mạng.

---

## Tổng hợp nhóm

| FR | Priority | UC nguồn | Số BR | Số VR | Số ERR | AC mang từ UC |
|---|---|---|---|---|---|---|
| FR-021 | High | UC-012 | 3 | 1 | 3 | AC-012.1, AC-012.6 |
| FR-022 | High | UC-012 | 3 | 2 | 2 | AC-012.2 |
| FR-023 | High | UC-012 | 3 | 1 | 3 | AC-012.3, AC-012.5 |
| FR-024 | High | UC-012 | 3 | 1 | 2 | AC-012.4 |
| FR-025 | High | UC-013 | 3 | 1 | 3 | AC-013.1, AC-013.2, AC-013.4 |
| FR-026 | High | UC-013 | 3 | 2 | 2 | AC-013.3 |
| FR-027 | Medium | UC-014 | 3 | 2 | 3 | AC-014.1, AC-014.4 |
| FR-028 | Medium | UC-014 | 2 | 2 | 2 | AC-014.2, AC-014.3 |
| FR-029 | High | UC-015 | 4 | 2 | 4 | AC-015.1, AC-015.2, AC-015.4, AC-015.5, AC-015.7 |
| FR-030 | High | UC-015 | 4 | 1 | 2 | AC-015.3, AC-015.6 |
| FR-031 | High | UC-016 | 4 | 1 | 3 | AC-016.1 → AC-016.5 |
| FR-032 | Medium | UC-017 | 4 | 2 | 4 | AC-017.1 → AC-017.4 |

**Tổng nhóm**: 12 FR (9 High, 3 Medium) · 39 BR · 18 VR · 33 ERR · **30 AC** — phủ đủ toàn bộ 30 AC của UC-012 → UC-017.

**Ba ràng buộc của nhóm này được kiểm ở code review, không ở runtime**: (1) không hằng số kích thước màn hình xe trong code layout (BR-029.1); (2) không tra bảng theo hãng/model để quyết định layout (BR-029.2); (3) mọi API iOS 17.4+ nằm trong kiểm tra khả dụng (BR-024.3).
