# FR — Onboarding & Thiết Lập Xe

**Sub-spec của**: [`Functional_Requirements.md`](./Functional_Requirements.md) · **Version** 2.4 · **Snapshot** 2026-08-07
**Phạm vi**: FR-001 → FR-009 · **UC nguồn**: UC-001 → UC-005 · **PRD Feature**: F5, F6
**Màn hình liên quan**: WF-001, WF-002, WF-003, WF-004, WF-005, WF-006, WF-021, WF-022, WF-030

> AC được **mang nguyên văn** từ `Use_Cases.md` §2. Số của AC theo UC gốc, **không** theo số FR.

---

## FR-001: Điều phối luồng onboarding 5 bước 📱

**Source UC**: UC-001
**Priority**: High · **Status**: Planned

**Description**:
Hệ thống phải dẫn người dùng mới qua đúng 5 bước (Welcome → Chọn Xe → Chọn Âm Thanh → Cấp Quyền → Home) trong dưới 2 phút, hiển thị tiến trình ở mọi bước, và **không hiển thị paywall ở bất kỳ bước nào**.

**Input**:
- Trạng thái cài đặt: `hasCompletedOnboarding` (Bool, đọc từ App Group) — phải là `false`
- Bước hiện tại: `onboardingStep` (Int 1–4, mặc định 1)
- Không yêu cầu tài khoản, không yêu cầu kết nối mạng

**Processing**:
1. Nhận điều hướng từ FR-009 với `onboardingStep`; hiển thị WF-002 kèm `ProgressBar` 1/4.
2. Người dùng chạm "Bắt đầu" → tăng `onboardingStep`; chuyển WF-003 (bàn giao cho FR-004).
3. Sau khi xe được xác nhận → chuyển WF-004 (bàn giao cho FR-011 và FR-013), `ProgressBar` 3/4.
4. Sau khi sound được gán hoặc bỏ qua → chuyển WF-005 (bàn giao cho FR-007), `ProgressBar` 4/4.
5. Sau khi trạng thái quyền được xác định (dù là từ chối) → đặt `hasCompletedOnboarding = true`, ghi `onboarding_completed`, chuyển WF-006.
6. Ở mỗi bước, cập nhật `ProgressBar` theo số bước còn lại và cho phép quay lại bước trước mà giữ nguyên lựa chọn đã làm.

**Output**:
- `hasCompletedOnboarding = true`; xe đã chọn, sound Connect đã gán, trạng thái 2 quyền đã xác định
- Người dùng ở **WF-006** với ≥ 1 widget sẵn dùng ở gói Free
- Event `onboarding_started` (ở Processing 2) và `onboarding_completed` (ở Processing 5)

**Business Rules**:
- **BR-001.1**: Hệ thống **cấm** hiển thị WF-010 Paywall ở bất kỳ bước nào từ WF-002 đến WF-005. Đây là ràng buộc cứng từ PRD §7 F6, không phải lựa chọn thiết kế.
- **BR-001.2**: Nút "Tiếp tục" ở mọi bước phải bấm được, kể cả khi người dùng chưa cung cấp gì ở bước đó.
- **BR-001.3**: Onboarding **không** yêu cầu tạo tài khoản hay đăng nhập.
- **BR-001.4**: Số bước tối đa là 4 màn hình cấu hình + 1 màn Home. Thêm bước thứ 5 vào luồng cấu hình là vi phạm phạm vi F6.

**Validation Rules**:
- **VR-001.1**: `onboardingStep` phải nằm trong 1–4; giá trị ngoài dải được coi là dữ liệu hỏng và reset về 1.
- **VR-001.2**: `ProgressBar` phải hiển thị đúng `onboardingStep / 4`; lệch số bước là lỗi hiển thị.

**Error Handling**:
- **ERR-001.1** (từ AF-001.1): App bị kill hoặc người dùng thoát giữa luồng → bàn giao cho FR-002; lần mở kế tiếp vào đúng bước đang dở, **không** quay về WF-002.
- **ERR-001.2** (từ AF-001.2): Người dùng chạm quay lại → về bước trước, giữ nguyên mọi lựa chọn; không reset dữ liệu.
- **ERR-001.3** (từ State Variation WF-002 "Error"): Không lấy được trạng thái giao dịch từ StoreKit → **ẩn** dòng "Phục hồi giao dịch" thay vì hiện nút không hoạt động; luồng thiết lập vẫn đi được.

**Acceptance Criteria**:
- **AC-001.1**: WHEN người dùng mở app lần đầu THEN hệ thống hiển thị WF-002 và **không** hiển thị WF-010 Paywall tại bất kỳ bước nào của onboarding.
- **AC-001.2**: WHEN người dùng đi hết 4 bước không bỏ qua gì THEN tổng thời gian tối thiểu cần thiết ≤ 120 giây.
- **AC-001.4**: WHEN onboarding hoàn tất THEN hệ thống ghi `onboarding_completed`; tỉ lệ hoàn tất mục tiêu ≥ 70%.
- **AC-001.5**: WHEN người dùng ở bất kỳ bước nào của onboarding THEN thanh tiến trình hiển thị đúng số bước còn lại.

---

## FR-002: Lưu và phục hồi tiến trình onboarding 📱

**Source UC**: UC-001 (AF-001.1, AF-001.2)
**Priority**: High · **Status**: Planned

**Description**:
Hệ thống phải lưu tiến trình onboarding sau mỗi bước để người dùng bị ngắt giữa luồng có thể tiếp tục đúng chỗ đang dở, và phải cho phép bỏ qua từng bước mà không mất dữ liệu đã có.

**Input**:
- `onboardingStep` (Int) và các lựa chọn đã làm: `selectedVehicle` (make/model/year), `selectedConnectSound` (ID preset), `permissionStates` (Vị trí, Lịch)
- Sự kiện vòng đời app: `sceneWillResignActive`, `applicationWillTerminate`

**Processing**:
1. Sau mỗi bước hoàn tất, ghi `onboardingStep` và lựa chọn của bước đó xuống App Group **ngay tại thời điểm đó**, không chờ app vào background.
2. Khi app khởi động lại và `hasCompletedOnboarding == false`, đọc `onboardingStep` và định tuyến tới đúng màn hình của bước đó.
3. Khi người dùng quay lại bước trước, nạp lại lựa chọn đã lưu của bước đó vào UI.
4. Khi người dùng chạm "Bỏ qua bước này" (WF-003) hoặc "Chọn sau" (WF-004), ghi nhận bước đã bỏ qua, gán giá trị mặc định (ảnh silhouette theo phân khúc / preset Free đầu tiên) và tăng `onboardingStep`.
5. Khi onboarding hoàn tất, giữ lại toàn bộ lựa chọn và chỉ đặt `hasCompletedOnboarding = true` — **không** xoá state.

**Output**:
- Tiến trình bền vững qua mọi lần khởi động lại app
- Nếu bỏ dở: WF-006 chưa hiện; nếu đã hoàn tất: `CardTile` "Hoàn tất thiết lập" **không** hiện

**Business Rules**:
- **BR-002.1**: Bỏ qua một bước **không bao giờ** dẫn tới trạng thái không dùng được — mọi bước bỏ qua đều có giá trị mặc định hợp lệ.
- **BR-002.2**: Dữ liệu onboarding được ghi vào App Group (không phải `UserDefaults` của app) để widget extension đọc được ngay từ chuyến đầu tiên.

**Validation Rules**:
- **VR-002.1**: Nếu `onboardingStep` đọc được nhưng lựa chọn tương ứng bị thiếu, hệ thống lùi về bước gần nhất có dữ liệu đầy đủ thay vì hiển thị màn hình rỗng.

**Error Handling**:
- **ERR-002.1** (từ AF-001.1): Ghi App Group thất bại → giữ state trong bộ nhớ cho phiên hiện tại và thử lại ở bước kế tiếp; **không** chặn người dùng đi tiếp.
- **ERR-002.2** (từ State Variation WF-001 "Error"): Dữ liệu onboarding hỏng hoặc không đọc được → vào WF-006 ở trạng thái mặc định an toàn kèm một dòng thông báo, **không** bắt onboard lại từ đầu.

**Acceptance Criteria**:
- **AC-001.3**: IF người dùng thoát app ở bước N THEN lần mở kế tiếp hệ thống hiển thị đúng bước N.

---

## FR-003: Phục hồi giao dịch từ onboarding và paywall 📱

**Source UC**: UC-001 (AF-001.3), UC-029, UC-030
**Priority**: Medium · **Status**: Planned

**Description**:
Hệ thống phải cho phép người dùng đã từng mua lấy lại quyền của mình trên thiết bị mới hoặc sau khi cài lại, và phải nói rõ khi không tìm thấy giao dịch nào — thay vì báo lỗi chung.

**Input**:
- Apple ID hiện tại của thiết bị (do StoreKit cung cấp, app không đọc trực tiếp)
- Điểm khởi phát: WF-002 (onboarding), WF-010 (paywall), WF-025 (sheet đăng ký)

**Processing**:
1. Ở WF-002, truy vấn StoreKit xem có giao dịch nào thuộc Apple ID hiện tại; **chỉ hiện** `LinkRow` "Phục hồi giao dịch" nếu có.
2. Ở WF-010 và WF-025, luôn hiện nút "Phục hồi giao dịch" ngang hàng với các bậc giá (không ẩn trong menu con).
3. Khi người dùng chạm, gọi `AppStore.sync()` và đọc lại `Transaction.currentEntitlements`.
4. Cập nhật `EntitlementService` (bàn giao cho FR-043) và mở khóa tính năng tương ứng.
5. Nếu không có giao dịch nào, hiển thị thông báo nói rõ "không tìm thấy giao dịch nào thuộc Apple ID này" — **không** dùng thông báo lỗi chung.

**Output**:
- Entitlement được cập nhật đúng mức (Free / Premium / Lifetime)
- Nếu phục hồi thành công trong onboarding: nhãn khoá ở WF-004 biến mất

**Business Rules**:
- **BR-003.1**: Phục hồi giao dịch **không bao giờ** phát sinh khoản trừ tiền mới.
- **BR-003.2**: Nút phục hồi phải luôn khả dụng ở WF-010 và WF-025, không phụ thuộc trạng thái entitlement hiện tại.

**Validation Rules**:
- **VR-003.1**: Chỉ chấp nhận entitlement do StoreKit xác thực; **không** suy ra quyền từ dữ liệu cục bộ chưa xác thực.

**Error Handling**:
- **ERR-003.1** (từ AF-029.2): Không có giao dịch nào → nói rõ điều đó thay vì báo lỗi chung.
- **ERR-003.2** (từ AF-030.2): StoreKit không phản hồi → nêu lý do kèm nút thử lại; giữ nguyên entitlement hiện tại, **không** hạ xuống Free.
- **ERR-003.3** (từ ERR-001.3): Không truy vấn được ở WF-002 → ẩn dòng phục hồi, không hiện nút vô hiệu.

**Acceptance Criteria**:
- **AC-029.5**: WHEN người dùng chạm "Phục hồi giao dịch" mà không có giao dịch nào THEN hệ thống nói rõ điều đó thay vì báo lỗi chung.
- **AC-030.4**: WHEN người dùng cài lại app và phục hồi giao dịch THEN Lifetime được trả lại mà **không** phải trả tiền lần nữa.

---

## FR-004: Thư viện xe và tìm kiếm on-device 📱

**Source UC**: UC-002
**Priority**: High · **Status**: Planned

**Description**:
Hệ thống phải cung cấp thư viện ≥ 40 hãng và ≥ 400 model, đóng gói sẵn trên thiết bị, cho phép chọn theo ba tầng hãng → model → năm và tìm kiếm không cần mạng.

**Input**:
- Dataset xe đóng gói trong app bundle: `make` (String), `model` (String), `yearRange` (ClosedRange<Int>), `segment` (enum: sedan/SUV/pickup/hatchback/van/coupe)
- Chuỗi tìm kiếm do người dùng gõ (String, 0–40 ký tự)
- Storefront hiện tại (dùng để sắp thứ tự hãng theo mức phổ biến)

**Processing**:
1. Nạp dataset từ bundle vào SQLite ở lần chạy đầu; các lần sau đọc trực tiếp từ SQLite.
2. Hiển thị danh sách hãng sắp theo **mức phổ biến ở storefront hiện tại** (không theo thứ tự chữ cái); lọc theo chuỗi tìm kiếm trong ≤ 200ms, hoàn toàn on-device.
3. Người dùng chọn hãng → ghim hàng hãng thành hàng 44pt, hiện danh sách model của hãng đó (sub-flow SF-002).
4. Người dùng chọn model → ghim tầng hai, hiện bộ chọn năm giới hạn trong `yearRange` của model đó.
5. Người dùng chọn năm → bàn giao cho FR-005 để hiện ảnh xe đối chiếu; bật nút "Đúng xe của tôi".
6. Nếu người dùng vào từ thẻ xe trên WF-006 (đổi xe), ghim xe hiện tại ở đầu danh sách và đánh dấu; sau khi xác nhận, **giữ nguyên** mọi cấu hình widget và sound đã có.
7. Lưu `selectedVehicle` vào App Group.

**Output**:
- `selectedVehicle` (make + model + year) được lưu on-device
- Ảnh xe tương ứng được gán cho widget mặc định (bàn giao FR-005)
- Exit: WF-004 (nếu trong onboarding) hoặc WF-006 (nếu đổi xe)

**Business Rules**:
- **BR-004.1**: Thư viện phải có ≥ 40 hãng và ≥ 400 model tại thời điểm phát hành.
- **BR-004.2**: `trim` và `color` **không** thuộc phạm vi MVP 1 (dời MVP 3 theo PRD §6); hệ thống **không** hiển thị lựa chọn rỗng cho hai thuộc tính này.
- **BR-004.3**: Đổi xe **không** làm mất cấu hình widget hay sound.

**Validation Rules**:
- **VR-004.1**: Tìm kiếm khớp cả tên chính, **tên viết tắt** và tên nội địa của hãng (ví dụ "VW" khớp "Volkswagen").
- **VR-004.2**: Năm được chọn phải nằm trong `yearRange` của model đã chọn.
- **VR-004.3**: Chuỗi tìm kiếm dài hơn 40 ký tự bị cắt, không gây lỗi.

**Error Handling**:
- **ERR-004.1** (từ AF-002.1): Không tìm thấy hãng hoặc model → hiển thị dòng "Không tìm thấy xe của tôi" ở **cả ba tầng**; bàn giao FR-006.
- **ERR-004.2** (từ Recovery Path TF-001): Dataset không nạp được vào SQLite → đọc trực tiếp từ bundle ở chế độ chỉ đọc; luồng không bị chặn.

**Acceptance Criteria**:
- **AC-002.1**: WHEN người dùng mở WF-003 THEN thư viện chứa ≥ 40 hãng và ≥ 400 model.
- **AC-002.2**: WHEN người dùng chọn hãng, model và năm THEN hệ thống lưu cả ba giá trị và hiển thị ảnh xe tương ứng.
- **AC-002.5**: WHEN người dùng gõ vào ô tìm kiếm THEN kết quả được lọc trong ≤ 200ms và **không** yêu cầu kết nối mạng.
- **AC-002.6**: IF trim và color được người dùng tìm THEN hệ thống nêu rõ hai thuộc tính này thuộc MVP 3, không hiển thị lựa chọn rỗng.

---

## FR-005: Gán ảnh xe cho widget và fallback silhouette 📱🚗

**Source UC**: UC-002 (AF-002.3)
**Priority**: High · **Status**: Planned

**Description**:
Hệ thống phải gán đúng ảnh xe theo model đã chọn ở độ phân giải đủ nét cho màn hình xe lớn nhất trong test matrix, và phải có đường lui bằng ảnh silhouette theo phân khúc khi thiếu asset — có nói rõ cho người dùng.

**Input**:
- `selectedVehicle` từ FR-004
- Bộ asset ảnh xe theo model, mỗi model có ≥ 2 biến thể độ phân giải
- Bộ ảnh silhouette theo `segment` (6 phân khúc)
- Kích thước màn hình xe đã ghi nhận (nếu có, từ FR-029)

**Processing**:
1. Tra asset ảnh theo `make + model`; nếu có, chọn biến thể độ phân giải khớp kích thước màn hình xe đã biết (hoặc biến thể lớn nhất nếu chưa biết).
2. Nếu không có asset cho model đó, chọn ảnh silhouette theo `segment` và **hiển thị một dòng nói rõ đang dùng ảnh chung**.
3. Ghi nhận trường hợp thiếu asset vào telemetry (bàn giao FR-066) để bổ sung asset về sau.
4. Ghi đường dẫn ảnh đã chọn vào App Group để widget extension dùng.

**Output**:
- Ảnh xe (hoặc silhouette) được gán cho widget mặc định
- Nếu dùng silhouette: người dùng đã được thông báo, không bị hiểu nhầm là ảnh xe của mình

**Business Rules**:
- **BR-005.1**: Hệ thống **không bao giờ** để trống vùng ảnh xe — luôn có silhouette làm đường lui.
- **BR-005.2**: Khi dùng silhouette, hệ thống **phải** nói rõ; im lặng ở đây tạo kỳ vọng sai và dẫn tới review tiêu cực.

**Validation Rules**:
- **VR-005.1**: Ảnh được chọn phải có độ phân giải ≥ ngưỡng cần cho kích thước màn hình xe lớn nhất trong test matrix.

**Error Handling**:
- **ERR-005.1** (từ AF-002.3): Không có ảnh cho model → dùng silhouette theo phân khúc + thông báo.
- **ERR-005.2** (từ State Variation WF-003 "Error"): Cả ảnh model và silhouette đều không nạp được → dùng ảnh placeholder mặc định của app; **không** để Zone A trống.

**Acceptance Criteria**:
- **AC-002.3**: WHEN ảnh xe được hiển thị trên màn hình CarPlay THEN ảnh phải ở độ phân giải đủ để không bị mờ ở kích thước màn hình lớn nhất trong test matrix.
- **AC-002.4**: IF model của người dùng không có trong thư viện THEN hệ thống vẫn cho phép đi tiếp và dùng ảnh silhouette theo phân khúc.

---

## FR-006: Gửi yêu cầu thêm xe vào thư viện 📱

**Source UC**: UC-003
**Priority**: Medium · **Status**: Planned

**Description**:
Hệ thống phải cho người dùng báo xe của họ bị thiếu, xác nhận ngay mà không chờ mạng, và **không** thu bất kỳ dữ liệu định danh nào ngoài ba giá trị người dùng tự gõ.

**Input**:
- `make` (String, 1–40 ký tự, bắt buộc), `model` (String, 1–40 ký tự, bắt buộc), `year` (Int, 1980–năm hiện tại + 2, bắt buộc)
- Giá trị điền sẵn: phần chuỗi người dùng đã gõ ở WF-003

**Processing**:
1. Mở WF-021 dạng sheet, điền sẵn phần đã gõ ở WF-003.
2. Người dùng điền/sửa ba ô; hệ thống kiểm tính hợp lệ theo VR bên dưới.
3. Người dùng chạm "Gửi" → ghi request vào hàng chờ on-device và **xác nhận ngay** qua WF-030 trong ≤ 500ms, **không chờ phản hồi mạng**.
4. Khi có mạng, gửi request lên hàng đợi phía Firebase; nếu trùng với request đã gửi (cùng make+model+year), **gộp** thay vì gửi lại.
5. Sheet đóng; người dùng quay về WF-003 và có thể chọn phân khúc để đi tiếp (bàn giao FR-005).

**Output**:
- Request được ghi nhận (cục bộ hoặc đã gửi); người dùng vẫn hoàn tất được việc chọn xe
- Payload **không** chứa PII

**Business Rules**:
- **BR-006.1**: Việc thiếu xe trong thư viện **không bao giờ** chặn onboarding.
- **BR-006.2**: Request trùng (cùng make+model+year từ cùng thiết bị) được gộp, không gửi lặp.
- **BR-006.3**: Hệ thống không thu thêm bất kỳ trường nào ngoài ba giá trị người dùng tự gõ.

**Validation Rules**:
- **VR-006.1**: `make` và `model` không được rỗng; chấp nhận tên tự do, **không** validate theo danh sách có sẵn.
- **VR-006.2**: `year` phải nằm trong 1980 → năm hiện tại + 2.
- **VR-006.3**: Chuỗi dài hơn 40 ký tự bị cắt, không gây lỗi.

**Error Handling**:
- **ERR-006.1** (từ AF-003.1): Không có mạng → request xếp hàng on-device và gửi khi có mạng; toast vẫn xác nhận đã ghi nhận.
- **ERR-006.2** (từ AF-003.2): Người dùng đóng sheet mà không gửi → quay về WF-003, **không mất** phần đã gõ.
- **ERR-006.3** (từ AF-003.3): Gửi nhiều request liên tiếp → gộp, không gửi trùng.

**Acceptance Criteria**:
- **AC-003.1**: WHEN người dùng gửi request THEN hệ thống xác nhận bằng WF-030 trong ≤ 500ms, không chờ phản hồi mạng.
- **AC-003.2**: IF không có kết nối mạng THEN request được lưu on-device và gửi lại khi có mạng, không mất dữ liệu.
- **AC-003.3**: WHEN request được gửi THEN nội dung **không** chứa PII nào ngoài ba giá trị hãng/model/năm do người dùng tự gõ.

---

## FR-007: Trình bày lý do quyền và thu nhận quyết định 📱

**Source UC**: UC-004
**Priority**: High · **Status**: Planned

**Description**:
Hệ thống phải nêu rõ mục đích cụ thể của từng quyền (Vị trí, Lịch) bằng ngôn ngữ người dùng, cho phép đọc sâu hơn nếu muốn, và cho phép từ chối hoặc bỏ qua hoàn toàn mà không chặn luồng.

**Input**:
- Trạng thái quyền hệ thống: `CLAuthorizationStatus`, `EKAuthorizationStatus`
- Điểm khởi phát: WF-005 (onboarding bước 4) hoặc WF-012 (Settings, qua FR-062)

**Processing**:
1. Đọc trạng thái hiện tại của cả hai quyền; hiển thị `PermissionCard` cho mỗi quyền kèm lý do 1 dòng, một ví dụ cụ thể, và trạng thái (Đã cấp / Đã từ chối / Chưa hỏi).
2. Hiển thị một câu cam kết ở Zone A: dữ liệu ngữ cảnh không rời thiết bị.
3. Nếu người dùng chạm "Tìm hiểu thêm", mở WF-022 với biến thể đúng quyền đó: 2 ví dụ (có quyền được gì / không có mất gì) + link chính sách quyền riêng tư.
4. Nếu quyền ở trạng thái `notDetermined`, chạm "Cho phép" → gọi dialog quyền của iOS; nếu đã `denied`, nút đổi thành "Mở Cài đặt" và dẫn sang Cài đặt hệ thống.
5. Cập nhật trạng thái thẻ sau khi người dùng trả lời; nêu rõ tính năng nào bị ảnh hưởng và ở mức nào.
6. Người dùng chạm "Tiếp tục" (hoặc "Bỏ qua tất cả") → bàn giao FR-001 Processing 5.

**Output**:
- Trạng thái của cả hai quyền được xác định và lưu
- Event `location_permission_granted` khi quyền Vị trí được cấp
- Exit: WF-006

**Business Rules**:
- **BR-007.1**: Lý do của mỗi quyền phải cụ thể; **cấm** dùng câu chung như "để cải thiện trải nghiệm".
- **BR-007.2**: Hệ thống **không** gọi lại dialog quyền của iOS cho một quyền đã bị từ chối trong cùng phiên.
- **BR-007.3**: "Bỏ qua tất cả" luôn khả dụng và **không bị làm mờ**; chọn nó không tạo trạng thái lỗi.
- **BR-007.4**: Nút từ chối ở WF-022 ngang hàng thị giác với nút cho phép — không làm mờ nút từ chối.

**Validation Rules**:
- **VR-007.1**: Mọi tổ hợp trạng thái của hai quyền (9 tổ hợp) đều là trạng thái hợp lệ và phải xử lý được.

**Error Handling**:
- **ERR-007.1** (từ AF-004.1): Người dùng từ chối một quyền → nêu rõ tính năng bị ảnh hưởng, **không** hỏi lại, không chặn bước tiếp.
- **ERR-007.2** (từ AF-004.2): Từ chối cả hai → bàn giao FR-008.
- **ERR-007.3** (từ AF-004.3): Người dùng đổi ý sau này → lối vào từ WF-012 (FR-062).
- **ERR-007.4** (từ State Variation WF-005 "Error"): Dialog quyền iOS không mở được → nêu rõ và dẫn sang Cài đặt hệ thống; nút "Tiếp tục" vẫn bấm được.

**Acceptance Criteria**:
- **AC-004.1**: WHEN WF-005 hiển thị THEN mỗi quyền có nêu lý do cụ thể bằng ngôn ngữ người dùng, không dùng câu chung như "để cải thiện trải nghiệm".
- **AC-004.2**: IF người dùng từ chối một quyền THEN hệ thống **không** hiển thị lại dialog quyền đó trong cùng phiên và vẫn cho phép chạm "Tiếp tục".
- **AC-004.3**: WHEN người dùng cấp quyền Vị trí THEN hệ thống ghi `location_permission_granted`.
- **AC-004.4**: WHEN bất kỳ quyền nào bị từ chối THEN WF-005 hiển thị rõ tính năng nào bị ảnh hưởng và ở mức nào.
- **AC-004.5**: IF người dùng chạm "Tiếp tục" khi chưa trả lời quyền nào THEN hệ thống vẫn chuyển sang WF-006.

---

## FR-008: Suy giảm chức năng theo trạng thái quyền 📱🚗

**Source UC**: UC-005
**Priority**: High · **Status**: Planned

**Description**:
Hệ thống phải hoạt động đầy đủ ở mức cơ bản với **mọi tổ hợp** trạng thái quyền, kể cả khi cả hai quyền bị từ chối: widget render, sound phát, dashboard hiển thị, giọng chào phát ở biến thể chỉ dùng giờ trong ngày.

**Input**:
- `permissionStates` (Vị trí, Lịch) — 9 tổ hợp có thể
- Cấu hình nguồn ngữ cảnh của người dùng (từ FR-034)

**Processing**:
1. Tính tập nguồn ngữ cảnh **khả dụng thật** = (nguồn được người dùng bật) ∩ (nguồn có quyền tương ứng).
2. Nếu tập rỗng, dùng nguồn "giờ trong ngày" (không cần quyền) làm nguồn duy nhất.
3. Bàn giao tập nguồn khả dụng cho FR-037 (giọng chào) và FR-040 (sắp xếp dashboard).
4. Vô hiệu mục sound "Arrive" nếu thiếu quyền Vị trí, kèm lý do hiển thị tại chỗ (bàn giao FR-014).
5. Ẩn thẻ gợi ý điểm đến trên WF-016 nếu thiếu quyền Vị trí — **không** hiện thẻ rỗng.
6. Hiển thị tối đa **một** `StaticNotice` mời cấp quyền trên WF-006, dạng tĩnh, không popup, không nhắc lại theo phiên.
7. Khi quyền được cấp muộn, cập nhật tập nguồn và áp dụng từ **lần `carplay_connected` kế tiếp**.

**Output**:
- Widget, sound và dashboard cơ bản hoạt động đầy đủ ở mọi tổ hợp quyền
- Giọng chào luôn phát (dù ở biến thể tối giản), **không im lặng và không báo lỗi**

**Business Rules**:
- **BR-008.1**: Không tính năng nào bị **chặn hoàn toàn** vì thiếu quyền, ngoài phần phụ thuộc trực tiếp vào chính quyền đó.
- **BR-008.2**: Tối đa 1 lời mời cấp quyền dạng tĩnh trên mỗi màn hình; **cấm** popup và **cấm** nhắc lại theo phiên.
- **BR-008.3**: Mọi tổ hợp một phần (cấp một, từ chối một) đều phải xử lý được — không có tổ hợp nào là trạng thái lỗi.

**Validation Rules**:
- **VR-008.1**: Trước khi đọc bất kỳ nguồn ngữ cảnh nào, hệ thống phải kiểm quyền tương ứng; đọc mà không kiểm là lỗi.

**Error Handling**:
- **ERR-008.1** (từ AF-005.1): Người dùng thắc mắc vì sao dashboard không đổi → `InlineExplainer` tại WF-006 và WF-009 kèm lối vào cấp quyền; **không** dùng popup.
- **ERR-008.2** (từ AF-005.2): Quyền được cấp muộn → ngữ cảnh mới dùng từ lần kết nối kế tiếp, không cần khởi động lại app.
- **ERR-008.3** (từ State Variation WF-005 "Power User"): Quyền Vị trí ở mức "Khi dùng app" → nêu rõ tuyến đường chỉ học được khi app đang mở.

**Acceptance Criteria**:
- **AC-005.1**: IF mọi quyền đều bị từ chối THEN widget, sound và dashboard cơ bản vẫn hoạt động đầy đủ.
- **AC-005.2**: IF quyền Lịch bị từ chối THEN giọng chào vẫn phát, dùng ngữ cảnh giờ trong ngày, và **không** phát câu báo lỗi.
- **AC-005.3**: WHEN người dùng ở trạng thái không có quyền nào THEN hệ thống hiển thị tối đa **một** lời mời cấp quyền dạng tĩnh trên WF-006, không dùng popup và không nhắc lại theo phiên.
- **AC-005.4**: WHEN người dùng cấp quyền muộn THEN ngữ cảnh mới có hiệu lực từ lần kết nối CarPlay kế tiếp.

---

## FR-009: Splash, định tuyến khởi động và làm mới trạng thái 📱

**Source UC**: UC-001
**Priority**: High · **Status**: Planned

**Description**:
Hệ thống phải quyết định điểm đến khi khởi động (onboarding hay Home) mà không để người dùng chờ, và phải cho người dùng cách chủ động làm mới trạng thái kết nối sau mỗi chuyến.

**Input**:
- `hasCompletedOnboarding` (Bool), `onboardingStep` (Int) từ App Group
- Kết quả render của phiên CarPlay gần nhất (từ FR-029/FR-031)
- Nguồn khởi động: icon app · deep link · quay lại sau khi bị hệ thống thu hồi

**Processing**:
1. Hiển thị WF-001 với logo; chỉ báo tải **chỉ hiện nếu quá 1s**.
2. Đọc cấu hình từ App Group.
3. Nếu `hasCompletedOnboarding == false` → chuyển WF-002 (hoặc đúng bước đang dở, theo FR-002); hiển thị ≤ 1,5s.
4. Nếu `hasCompletedOnboarding == true` → chuyển WF-006; hiển thị ≤ 1,0s (không có trạng thái tải vì đọc từ cache).
5. Trên WF-006, khi người dùng kéo xuống > 60pt (sub-flow SF-001), đọc lại trạng thái kết nối và kết quả render gần nhất; cập nhật `WarningRow` (hiện nếu có lỗi, **tự xoá** nếu lần render kế tiếp thành công).
6. Nếu phiên gần nhất có `widget_render_failed`, hiển thị `WarningRow` dẫn WF-014 (bàn giao FR-031).

**Output**:
- Người dùng ở đúng điểm đến: WF-002 (chưa onboard) hoặc WF-006 (đã onboard)
- Event `app_opened` được ghi
- Trạng thái kết nối và cảnh báo tương thích trên WF-006 phản ánh dữ liệu mới nhất

**Business Rules**:
- **BR-009.1**: WF-001 **không có hành động người dùng nào** — mọi tương tác ở đây chỉ làm chậm việc mở app.
- **BR-009.2**: Cấu hình hỏng **không bao giờ** dẫn tới việc bắt người dùng onboard lại.
- **BR-009.3**: `WarningRow` tự xoá khi lần render kế tiếp thành công; hệ thống **không** để lại cảnh báo giả.

**Validation Rules**:
- **VR-009.1**: Nếu `hasCompletedOnboarding == true` nhưng thiếu `selectedVehicle`, vào WF-006 và hiển thị thẻ "Hoàn tất thiết lập" thay vì quay về onboarding.

**Error Handling**:
- **ERR-009.1** (từ State Variation WF-001 "Error"): Không đọc được cấu hình → vào WF-006 ở trạng thái mặc định an toàn kèm một dòng thông báo.
- **ERR-009.2** (từ SF-001 Recovery): Làm mới thất bại → giữ giá trị cũ kèm dòng "chưa cập nhật được"; **không** hiện trạng thái rỗng.

**Acceptance Criteria**:
- **AC-001.1**: WHEN người dùng mở app lần đầu THEN hệ thống hiển thị WF-002 và **không** hiển thị WF-010 Paywall tại bất kỳ bước nào của onboarding.
  > *Ghi chú truy vết*: AC-001.1 phủ đồng thời hành vi định tuyến của FR-009 và ràng buộc cấm-paywall của FR-001, nên nó xuất hiện ở cả hai FR. Đây là một AC được **chia sẻ**, không phải AC bị nhân bản.
- **AC-NFR-001.1**: WHEN người dùng chạm icon app THEN app trở nên tương tác được trong ≤ 2,0s trên iPhone 12.
- **AC-NFR-001.2**: WHEN đo trên toàn bộ thiết bị mục tiêu (iPhone 12 trở lên) THEN ≥ 95% lần khởi động đạt ngưỡng.

---

## Tổng hợp nhóm

| FR | Priority | UC nguồn | Số BR | Số VR | Số ERR | AC mang từ UC |
|---|---|---|---|---|---|---|
| FR-001 | High | UC-001 | 4 | 2 | 3 | AC-001.1, AC-001.2, AC-001.4, AC-001.5 |
| FR-002 | High | UC-001 | 2 | 1 | 2 | AC-001.3 |
| FR-003 | Medium | UC-001, UC-029, UC-030 | 2 | 1 | 3 | AC-029.5, AC-030.4 |
| FR-004 | High | UC-002 | 3 | 3 | 2 | AC-002.1, AC-002.2, AC-002.5, AC-002.6 |
| FR-005 | High | UC-002 | 2 | 1 | 2 | AC-002.3, AC-002.4 |
| FR-006 | Medium | UC-003 | 3 | 3 | 3 | AC-003.1, AC-003.2, AC-003.3 |
| FR-007 | High | UC-004 | 4 | 1 | 4 | AC-004.1 → AC-004.5 |
| FR-008 | High | UC-005 | 3 | 1 | 3 | AC-005.1 → AC-005.4 |
| FR-009 | High | UC-001 | 3 | 1 | 2 | AC-001.1 (chia sẻ), AC-NFR-001.1, AC-NFR-001.2 |

**Tổng nhóm**: 9 FR (7 High, 2 Medium) · 26 BR · 14 VR · 24 ERR · 24 AC mang từ UC-001 → UC-005 (đủ toàn bộ 23 AC của 5 UC này, cộng AC-029.5 và AC-030.4 dùng cho FR-003).
