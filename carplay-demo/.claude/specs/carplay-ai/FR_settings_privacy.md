# FR — Ngôn Ngữ, Quyền Riêng Tư, Phản Hồi & Telemetry

**Sub-spec của**: [`Functional_Requirements.md`](./Functional_Requirements.md) · **Version** 2.4 · **Snapshot** 2026-08-07
**Phạm vi**: FR-055 → FR-062, FR-066 · **UC nguồn**: UC-004, UC-017, UC-026, UC-029, UC-031 → UC-033, UC-036 · **PRD Feature**: F9, F10, F12
**Màn hình liên quan**: WF-006, WF-012, WF-014, WF-026, WF-028, WF-029, WF-030

> **FR-060** có vai trò kinh doanh đặc biệt: nó là cơ chế trực tiếp phục vụ KPI **Recent 1★ Ratio < 15%** bằng cách phân luồng người đang gặp vấn đề sang kênh sửa lỗi thay vì đẩy họ ra App Store.

---

## FR-055: Chọn ngôn ngữ và áp dụng tức thì 📱

**Source UC**: UC-031
**Priority**: Medium · **Status**: Planned

**Description**:
Hệ thống phải cho chọn EN / ES / PT-BR hoặc "Theo hệ thống", áp dụng ngay không cần khởi động lại app, và giữ giá theo tiền tệ storefront **độc lập** với ngôn ngữ UI.

**Input**:
- `appLanguage` (enum: system | en | es | ptBR), mặc định `system`
- Ngôn ngữ hệ thống của iOS
- Storefront hiện tại (quyết định tiền tệ, không phụ thuộc ngôn ngữ)

**Processing**:
1. Trên WF-012, dòng "Ngôn ngữ" hiển thị **giá trị hiện tại** ngay trên dòng.
2. Chạm dòng → mở WF-026 với 4 lựa chọn: English · Español · Português (Brasil) · Theo hệ thống; đánh dấu lựa chọn hiện tại.
3. Chọn một ngôn ngữ → **áp dụng ngay** cho toàn app; không có nút Lưu, không cần khởi động lại.
4. Ghi chú ở Zone C: DE/FR/IT thuộc MVP 2 — nêu rõ là **chưa có**, không hiện lựa chọn không hoạt động.
5. Bàn giao FR-039 để đổi ngôn ngữ nội dung giọng chào từ lượt phát kế tiếp.
6. Giá tiếp tục lấy từ `Product.displayPrice` theo storefront — **không** đổi theo ngôn ngữ UI.

**Output**:
- `appLanguage` được lưu; UI, nội dung giọng chào và ví dụ câu chào đổi theo
- Giá vẫn theo tiền tệ storefront

**Business Rules**:
- **BR-055.1**: Ngôn ngữ UI và tiền tệ giá là **hai chiều độc lập**; người dùng ở storefront US chọn tiếng Tây Ban Nha vẫn thấy giá USD.
- **BR-055.2**: **Cấm** hiển thị lựa chọn ngôn ngữ chưa được hỗ trợ.
- **BR-055.3**: Áp dụng ngay, **không** yêu cầu khởi động lại app.

**Validation Rules**:
- **VR-055.1**: `appLanguage` chỉ nhận 4 giá trị hợp lệ; giá trị lạ reset về `system`.

**Error Handling**:
- **ERR-055.1** (từ AF-031.1): Ngôn ngữ hệ thống không thuộc 3 ngôn ngữ hỗ trợ → bàn giao FR-056 (dùng English và nêu rõ).
- **ERR-055.2** (từ AF-031.2): Đổi ngôn ngữ khi đang cắm CarPlay → UI CarPlay cập nhật ở lần vẽ kế tiếp; câu chào đang phát **không bị cắt** (FR-039 ERR-039.1).
- **ERR-055.3** (từ AF-031.3): Người dùng tìm DE/FR/IT → nêu rõ thuộc MVP 2.

**Acceptance Criteria**:
- **AC-031.1**: WHEN người dùng chọn một ngôn ngữ THEN toàn bộ UI chuyển sang ngôn ngữ đó ngay, không cần khởi động lại app.
- **AC-031.3**: WHEN giá được hiển thị THEN dùng đúng tiền tệ địa phương của storefront, độc lập với ngôn ngữ UI.

---

## FR-056: Fallback khi thiếu bản dịch 📱

**Source UC**: UC-031 (AF-031.1)
**Priority**: Medium · **Status**: Planned

**Description**:
Hệ thống phải rơi về English cho **đúng chuỗi bị thiếu bản dịch** — không hiện khoá dịch thô, không để ô trống — và phải nêu rõ khi ngôn ngữ hệ thống của người dùng không thuộc ba ngôn ngữ được hỗ trợ.

**Input**:
- `appLanguage` đang dùng
- Bảng chuỗi của ngôn ngữ đó và bảng English (bảng cơ sở)

**Processing**:
1. Khi tra một khoá chuỗi, nếu bảng của ngôn ngữ hiện tại không có khoá đó, tra bảng English.
2. Nếu English cũng thiếu, hiển thị **nội dung mặc định đã định nghĩa trong code**, tuyệt đối **không** hiển thị chính khoá dịch.
3. Nếu ngôn ngữ hệ thống không thuộc EN/ES/PT-BR và `appLanguage == system`: dùng English và **nêu rõ lý do** ở WF-026.
4. Ghi nhận mọi lần fallback vào telemetry (bàn giao FR-066) để phát hiện chuỗi thiếu trước khi phát hành.
5. Ở giai đoạn build, kiểm số khoá chưa dịch = 0 cho cả ba ngôn ngữ (AC-NFR-015.1).

**Output**:
- Người dùng **không bao giờ** thấy khoá dịch thô hay ô trống
- Danh sách chuỗi thiếu được ghi nhận để bổ sung

**Business Rules**:
- **BR-056.1**: **Cấm** hiển thị khoá dịch thô cho người dùng. Đây là lỗi làm app trông chưa hoàn thiện, và ở niche này ấn tượng đó rất tốn kém.
- **BR-056.2**: Fallback ở mức **từng chuỗi**, không phải mức toàn app — thiếu một chuỗi không làm cả app về English.

**Validation Rules**:
- **VR-056.1**: Ở giai đoạn build, số khoá chưa dịch phải = 0 cho cả ba ngôn ngữ; khác 0 là lỗi build.

**Error Handling**:
- **ERR-056.1** (từ State Variation WF-026 "Error"): Thiếu bản dịch một chuỗi → rơi về English cho đúng chuỗi đó, phần còn lại giữ ngôn ngữ đã chọn.
- **ERR-056.2** (từ AF-031.1): Ngôn ngữ hệ thống không được hỗ trợ → dùng English và nêu rõ.

**Acceptance Criteria**:
- **AC-031.4**: IF ngôn ngữ hệ thống không thuộc 3 ngôn ngữ hỗ trợ THEN app dùng English và nêu rõ lý do.
- **AC-NFR-015.3**: IF một chuỗi thiếu bản dịch THEN hệ thống rơi về English cho **đúng chuỗi đó**, không hiện khoá dịch thô (liên quan FR-056).

---

## FR-057: Hiển thị và xoá dữ liệu học on-device 📱

**Source UC**: UC-032
**Priority**: Medium · **Status**: Planned

**Description**:
Hệ thống phải liệt kê các loại dữ liệu đang giữ trên thiết bị, nêu rõ chúng nằm trên máy, và cho xoá dữ liệu học sau một bước xác nhận nêu rõ **mất gì và giữ gì**.

**Input**:
- Danh mục dữ liệu on-device: lịch sử ngữ cảnh, lịch sử chạm thẻ, tuyến quen, lịch sử chẩn đoán
- Số ngày dữ liệu đã tích lũy

**Processing**:
1. Trên WF-012, dòng "Quyền riêng tư & dữ liệu" dẫn tới mục liệt kê **từng loại** dữ liệu đang giữ, kèm câu nêu rõ chúng nằm trên thiết bị.
2. Hiển thị số ngày dữ liệu sẽ mất, để người dùng biết cái giá của thao tác.
3. Chạm "Xoá toàn bộ dữ liệu học" → WF-029 alert nêu rõ **mất gì** (dữ liệu học ngữ cảnh) và **giữ gì** (widget, sound, entitlement).
4. Xác nhận → xoá dữ liệu ngữ cảnh khỏi SQLite; **giữ nguyên** cấu hình widget/sound và entitlement.
5. Dashboard trở về thứ tự mặc định và bắt đầu học lại từ đầu (bàn giao FR-040).
6. Hiển thị WF-030 toast xác nhận.
7. Nếu chưa có dữ liệu học: nêu rõ "chưa có dữ liệu học nào" và **vô hiệu** nút xoá.

**Output**:
- Dữ liệu học bị xoá; cấu hình và entitlement còn nguyên
- Dashboard reset về mặc định

**Business Rules**:
- **BR-057.1**: Dữ liệu **học** và dữ liệu **cấu hình** là hai loại khác nhau; xoá loại này **không** được xoá loại kia.
- **BR-057.2**: Xoá dữ liệu học **không bao giờ** ảnh hưởng entitlement.
- **BR-057.3**: Hành động phá hủy **phải** đi qua một bước xác nhận nêu rõ hậu quả.

**Validation Rules**:
- **VR-057.1**: Nếu không có dữ liệu học, nút xoá bị vô hiệu thay vì xoá một thứ không tồn tại.

**Error Handling**:
- **ERR-057.1** (từ AF-032.2): Người dùng huỷ ở alert → không xoá gì.
- **ERR-057.2** (từ State Variation WF-029 "Error"): Xoá thất bại một phần → nêu rõ phần nào chưa xoá được kèm nút thử lại; **không** báo "đã xoá xong" khi chưa xong.
- **ERR-057.3** (từ AF-032.3): Người dùng xoá app → mọi dữ liệu on-device mất theo, đúng cam kết PRD §9.

**Acceptance Criteria**:
- **AC-032.1**: WHEN người dùng mở mục quyền riêng tư THEN hệ thống liệt kê các loại dữ liệu đang giữ và nêu rõ chúng nằm trên thiết bị.
- **AC-032.3**: WHEN hành động xoá được yêu cầu THEN hệ thống bắt xác nhận qua WF-029 và nêu rõ điều gì sẽ mất.
- **AC-032.4**: WHEN dữ liệu bị xoá THEN dashboard trở về thứ tự mặc định và bắt đầu học lại từ đầu.

---

## FR-058: Tách xoá dữ liệu học khỏi xoá cấu hình 📱

**Source UC**: UC-032 (AF-032.1)
**Priority**: Medium · **Status**: Planned

**Description**:
Hệ thống phải cung cấp hai hành động xoá **tách biệt rõ ràng**: xoá dữ liệu học (mặc định) và xoá cả cấu hình (cần một xác nhận nữa) — để không ai xoá mất widget và sound của mình vì chạm nhầm.

**Input**:
- Lựa chọn của người dùng: `learningOnly` | `learningAndConfig`
- Danh mục dữ liệu tương ứng mỗi lựa chọn

**Processing**:
1. Ở WF-029, lựa chọn thứ nhất là "Xoá dữ liệu học" — đặt ở Zone B, là hành động mặc định.
2. Lựa chọn thứ hai "Xoá cả cấu hình" đặt ở Zone D, **tách riêng**, và cần **một xác nhận nữa** trước khi thực hiện.
3. Với `learningOnly`: xoá lịch sử ngữ cảnh, giữ widget/sound/entitlement (bàn giao FR-057).
4. Với `learningAndConfig`: xoá thêm cấu hình widget và sound; **entitlement vẫn được giữ** (quyền đã mua không bị xoá bởi hành động này).
5. Sau khi xoá cấu hình: WF-006 hiện thẻ "Hoàn tất thiết lập" để người dùng dựng lại nhanh.
6. Cung cấp "Hoàn tác" trên WF-030 trong 5 giây đầu cho trường hợp `learningAndConfig` — vì đó là hành động tốn công dựng lại nhất.

**Output**:
- Đúng phạm vi dữ liệu được xoá theo lựa chọn của người dùng
- Entitlement **không bao giờ** bị xoá bởi FR này

**Business Rules**:
- **BR-058.1**: Hai lựa chọn xoá phải **tách biệt về thị giác và về số bước xác nhận**; gộp chúng lại sẽ dẫn tới xoá nhầm.
- **BR-058.2**: **Cấm** xoá entitlement trong mọi biến thể của hành động này.
- **BR-058.3**: Xoá cấu hình có "Hoàn tác" 5 giây; xoá dữ liệu học thì không cần (nó tự học lại).

**Validation Rules**:
- **VR-058.1**: Lựa chọn `learningAndConfig` chỉ thực thi sau **hai** lần xác nhận rõ ràng.

**Error Handling**:
- **ERR-058.1** (từ AF-032.1): Người dùng muốn xoá tất cả → lựa chọn thứ hai ở Zone D, có xác nhận thứ hai.
- **ERR-058.2** (từ WF-030 Layer 2 "Hoàn tác"): Người dùng đổi ý trong 5 giây → phục hồi cấu hình từ bản sao tạm.

**Acceptance Criteria**:
- **AC-032.2**: WHEN người dùng xoá dữ liệu học THEN dữ liệu ngữ cảnh bị xoá nhưng cấu hình widget/sound và entitlement **được giữ nguyên**.

---

## FR-059: Mời đánh giá có điều kiện và phân luồng 📱

**Source UC**: UC-033
**Priority**: Medium · **Status**: Planned

**Description**:
Hệ thống phải mời đánh giá **chỉ sau chuỗi trải nghiệm tích cực**, **chặn** lời mời nếu có lỗi render trong 7 ngày gần nhất, và phân luồng theo mức hài lòng — hài lòng ra App Store, không hài lòng sang kênh sửa lỗi.

**Input**:
- Số lần `sound_played` thành công liên tiếp (ngưỡng: ≥ 5)
- Có `widget_render_failed` trong 7 ngày gần nhất hay không
- Thời điểm lần mời gần nhất bị đóng
- Mức hài lòng người dùng chọn

**Processing**:
1. Kiểm điều kiện kích hoạt: `sound_played` thành công ≥ 5 lần **và** không có `widget_render_failed` trong 7 ngày **và** lần mời gần nhất bị đóng cách đây ≥ 30 ngày.
2. Nếu điều kiện không thoả: **không** hiển thị lời mời; kết thúc.
3. Nếu thoả: hiển thị WF-030 biến thể "mời đánh giá" — overlay nhẹ, đóng được bằng **một chạm**, **không chặn** tác vụ đang làm.
4. Người dùng chọn mức hài lòng.
5. Nếu **hài lòng**: mở dialog đánh giá App Store của iOS; ghi `in_app_rating_submitted`.
6. Nếu **không hài lòng**: bàn giao FR-060 (mở WF-028), **không** mở dialog App Store.
7. Nếu người dùng đóng: không hiển thị lại trong ≥ 30 ngày.
8. Ngoài ra, dòng "Đánh giá Carbina" luôn có trên WF-012 cho người muốn tự tìm — lối này **không** có điều kiện kích hoạt.

**Output**:
- Lời mời chỉ xuất hiện ở thời điểm hợp lý; hoặc không xuất hiện
- Người dùng được dẫn tới **đúng kênh** theo mức hài lòng của họ

**Business Rules**:
- **BR-059.1**: **Cấm** mời đánh giá khi có `widget_render_failed` trong 7 ngày gần nhất. Mời đánh giá ngay sau khi app vừa lỗi là cách nhanh nhất để nhận 1★ — và KPI Recent 1★ Ratio < 15% phụ thuộc trực tiếp vào quy tắc này.
- **BR-059.2**: Người dùng **không hài lòng** phải được dẫn sang kênh sửa lỗi, **không** ra App Store.
- **BR-059.3**: Lời mời đóng được bằng một chạm và **không chặn** tác vụ đang làm.
- **BR-059.4**: Đóng lời mời → im lặng ≥ 30 ngày.

**Validation Rules**:
- **VR-059.1**: Cả ba điều kiện kích hoạt phải cùng thoả; thiếu một là không hiển thị.

**Error Handling**:
- **ERR-059.1** (từ AF-033.1): Người dùng đóng overlay → không hiện lại trong ≥ 30 ngày.
- **ERR-059.2** (từ AF-033.2): Người dùng tự tìm → dòng trên WF-012, không có điều kiện kích hoạt.
- **ERR-059.3** (từ AF-033.3): Có lỗi render trong 7 ngày → **không** hiện lời mời; thay vào đó giữ lối vào WF-014.

**Acceptance Criteria**:
- **AC-033.2**: IF có `widget_render_failed` trong 7 ngày gần nhất THEN hệ thống **không** hiển thị lời mời đánh giá.
- **AC-033.3**: WHEN người dùng đóng lời mời THEN hệ thống không hiển thị lại trong ≥ 30 ngày.
- **AC-033.4**: WHEN lời mời hiển thị THEN nó đóng được bằng một chạm và **không** chặn tác vụ đang làm.

---

## FR-060: Kênh phản hồi cho người không hài lòng 📱

**Source UC**: UC-033
**Priority**: Medium · **Status**: Planned

**Description**:
Khi người dùng chọn mức **không hài lòng**, hệ thống phải mở kênh báo lỗi (WF-028) với ô ghi chú được nhấn mạnh, và **tuyệt đối không** mở dialog đánh giá App Store — kể cả như một đường lui.

**Input**:
- Mức hài lòng người dùng chọn (từ FR-059)
- Dữ liệu chẩn đoán khả dụng (nếu có, từ FR-032)
- Ghi chú của người dùng (0–500 ký tự)

**Processing**:
1. Nhận tín hiệu "không hài lòng" từ FR-059.
2. Mở WF-028 với **Zone C (ô ghi chú) được nhấn mạnh** — ở ngữ cảnh này lời của người dùng quan trọng hơn số liệu kỹ thuật.
3. Điền sẵn dữ liệu chẩn đoán nếu có; người dùng bỏ tick được từng mục (bàn giao FR-032 Processing 5).
4. Người dùng chạm "Gửi" → xác nhận trong ≤ 500ms; xếp hàng on-device nếu offline.
5. **Không** mở dialog đánh giá App Store ở bất kỳ nhánh nào của luồng này.
6. Nếu người dùng không muốn gõ gì và đóng sheet: kết thúc; hệ thống **không** đẩy họ ra App Store như một đường lui.

**Output**:
- Phản hồi tiêu cực đi vào kênh sửa lỗi thay vì vào App Store
- Ý kiến người dùng được ghi nhận kèm dữ liệu kỹ thuật họ đồng ý gửi

**Business Rules**:
- **BR-060.1**: **Cấm tuyệt đối** mở dialog đánh giá App Store trong nhánh "không hài lòng", kể cả khi người dùng đóng sheet mà không gửi gì.
- **BR-060.2**: Ở nhánh này, ô ghi chú là thành phần chính; dữ liệu kỹ thuật là phụ. Đây là điểm khác biệt với FR-032 dù dùng chung màn hình WF-028.
- **BR-060.3**: Không gõ gì cũng là kết thúc hợp lệ; **cấm** ép người dùng phải nói ra lý do.

**Validation Rules**:
- **VR-060.1**: Ở nhánh FR-060, việc gửi được phép **không** kèm dữ liệu chẩn đoán nào — khác FR-032 (bắt buộc có kích thước màn hình, xem VR-032.2).

**Error Handling**:
- **ERR-060.1** (từ Recovery Path TF-013): Người dùng không muốn gõ gì → đóng sheet; không đẩy ra App Store.
- **ERR-060.2** (từ AF-017.2): Không gửi được → xếp hàng on-device và gửi khi có mạng.

**Acceptance Criteria**:
- **AC-033.1**: WHEN người dùng chọn mức không hài lòng THEN hệ thống mở WF-028 và **không** mở dialog đánh giá App Store.

---

## FR-061: Đổi theme và áp dụng tức thì 📱

**Source UC**: UC-036
**Priority**: Medium · **Status**: Planned

**Description**:
Hệ thống phải cho chọn theme (sáng / tối / theo hệ thống), áp dụng ngay trên toàn app, và cập nhật preview widget để người dùng thấy hiệu ứng trên màn hình xe **trước khi ra xe**.

**Input**:
- `appTheme` (enum: system | light | dark), mặc định `system`
- Cài đặt sáng/tối của iOS
- Cấu hình widget hiện tại (để cập nhật preview)

**Processing**:
1. Trên WF-012 Zone C, hiển thị bộ chọn theme kèm giá trị hiện tại.
2. Người dùng chọn một theme → áp dụng ngay cho toàn app bằng crossfade 0,25s (sub-flow SF-021); **không** cần khởi động lại.
3. Cập nhật preview widget nhỏ trong Zone C để người dùng thấy hiệu ứng trên màn hình xe.
4. Nếu chọn "Theo hệ thống": theo cài đặt sáng/tối của iOS và đổi theo khi hệ thống đổi.
5. Ghi `appTheme` vào App Group để widget extension dùng cùng theme.
6. Nếu một thành phần không áp được theme: thành phần đó dùng theme hệ thống thay vì hiện màu sai.

**Output**:
- `appTheme` được lưu và áp dụng cho cả app và widget
- Người dùng thấy trước hiệu ứng trên widget

**Business Rules**:
- **BR-061.1**: Theme áp dụng cho **cả** app iPhone và widget CarPlay; hai bề mặt không được lệch theme.
- **BR-061.2**: Đổi theme dùng **crossfade, không chuyển động** — chuyển động khi đổi màu gây cảm giác giật.
- **BR-061.3**: Widget phải đúng ở **cả** dark và light mode (đã là ràng buộc của AC-015.4).

**Validation Rules**:
- **VR-061.1**: `appTheme` chỉ nhận 3 giá trị hợp lệ; giá trị lạ reset về `system`.
- **VR-061.2**: Sau khi đổi theme, độ tương phản chữ trên ảnh widget vẫn đạt ≥ 4,5:1 (AC-NFR-014.4).

**Error Handling**:
- **ERR-061.1** (từ SF-021 Recovery): Theme không áp được cho một thành phần → thành phần đó dùng theme hệ thống, **không** hiện màu sai.
- **ERR-061.2** (từ AF-036.2): Ghi App Group thất bại → widget tạm dùng theme hệ thống; thử lại ở lần lưu kế tiếp.

**Acceptance Criteria**:
- **AC-036.1**: WHEN người dùng chọn một theme THEN toàn bộ UI chuyển sang theme đó ngay, không cần khởi động lại app.
- **AC-036.2**: WHEN theme được đổi THEN preview widget trong Cài Đặt Chung cập nhật theo để người dùng thấy hiệu ứng trên màn hình xe.
- **AC-036.3**: IF người dùng chọn "Theo hệ thống" THEN app đổi theo cài đặt sáng/tối của iOS mà không cần thao tác thêm.

---

## FR-062: Lối vào trạng thái quyền từ Settings 📱

**Source UC**: UC-004 (AF-004.3)
**Priority**: Medium · **Status**: Planned

**Description**:
Hệ thống phải cho người dùng xem trạng thái từng quyền từ Settings và mở Cài đặt hệ thống để đổi — vì iOS không cho app hỏi lại một quyền đã bị từ chối.

**Input**:
- Trạng thái hiện tại của quyền Vị trí, Lịch, Thư viện ảnh
- Tính năng bị ảnh hưởng bởi từng quyền

**Processing**:
1. Trên WF-012 Zone C, dòng "Quyền" hiển thị số quyền đã cấp / tổng số ngay trên dòng.
2. Chạm dòng → hiển thị trạng thái từng quyền kèm **tính năng bị ảnh hưởng** nếu chưa cấp.
3. Với quyền ở trạng thái `notDetermined`: mở WF-022 để giải thích rồi gọi dialog iOS (bàn giao FR-007).
4. Với quyền ở trạng thái `denied`: nút đổi thành "Mở Cài đặt" và dẫn sang Cài đặt hệ thống.
5. Khi quay lại app, đọc lại trạng thái quyền và cập nhật; bàn giao FR-008 để tính lại tập nguồn khả dụng.

**Output**:
- Người dùng thấy trạng thái quyền và có đường đổi nó
- Tập nguồn ngữ cảnh khả dụng được cập nhật ngay khi quay lại app

**Business Rules**:
- **BR-062.1**: Với quyền đã `denied`, **cấm** gọi lại dialog iOS (iOS sẽ không hiện, tạo cảm giác nút không hoạt động); phải dẫn sang Cài đặt hệ thống.
- **BR-062.2**: Mỗi quyền chưa cấp phải nêu rõ **tính năng nào bị ảnh hưởng** — nếu không, người dùng không có lý do để cấp.

**Validation Rules**:
- **VR-062.1**: Trạng thái quyền phải đọc lại mỗi lần app vào foreground, không dùng giá trị cache từ phiên trước.

**Error Handling**:
- **ERR-062.1** (từ AF-004.3): Người dùng đổi ý sau onboarding → lối vào từ WF-012.
- **ERR-062.2** (từ ERR-007.4): Không mở được Cài đặt hệ thống → nêu rõ và hướng dẫn đường đi thủ công.

**Acceptance Criteria**:
- **AC-004.2**: IF người dùng từ chối một quyền THEN hệ thống **không** hiển thị lại dialog quyền đó trong cùng phiên và vẫn cho phép chạm "Tiếp tục".
  > *Ghi chú truy vết*: AC-004.2 được **chia sẻ** với FR-007. FR-007 sở hữu hành vi trong onboarding; FR-062 sở hữu cùng ràng buộc ở lối vào từ Settings. Không phải AC bị nhân bản.

---

## FR-066: Telemetry, sự kiện vận hành và cảnh báo 📱🚗

**Source UC**: UC-017, UC-026, UC-029, UC-032
**Priority**: Medium · **Status**: Planned

**Description**:
Hệ thống phải ghi đủ 28 event của PRD §12 **không kèm PII**, phải có `widget_render_failed` và `refund_detected` hoạt động **từ ngày launch**, và phải phát cảnh báo tự động cho PM khi Widget Render Success Rate tụt dưới 90%.

**Input**:
- Sự kiện từ toàn bộ các FR khác (28 event schema của PRD §12)
- App Store Server Notification V2 (cho `refund_detected`)
- Ngưỡng cảnh báo: Widget Render Success Rate < 90%

**Processing**:
1. Đăng ký 28 event schema; mỗi event có danh sách tham số cố định, **không** cho phép tham số tự do.
2. Trước khi gửi, lọc payload theo whitelist tham số — bảo đảm **không có PII** (NFR-011).
3. Ghi `widget_render_ok` / `widget_render_failed` kèm `screen_width`, `screen_height`, `widget_type`, `failure_reason` (từ FR-029, FR-030, FR-031).
4. Nhận App Store Server Notification V2 tại endpoint backend; chuyển thành `refund_detected` (nguồn cho Refund Rate, phục vụ R-04 và R-12).
5. Tính Widget Render Success Rate theo ngày, chia nhóm theo cặp kích thước; nếu < 90% trong bất kỳ ngày nào, phát **cảnh báo tự động cho PM trong ≤ 24 giờ**.
6. Nếu cùng một cặp kích thước thất bại ≥ 3 lần, đánh dấu ưu tiên cao.
7. Ghi nhận mỗi lần fallback bản dịch (từ FR-056) và mỗi lần thiếu asset ảnh xe (từ FR-005) để bổ sung nội dung.
8. Khi Firebase gặp sự cố: **app vẫn hoạt động đầy đủ**; event được xếp hàng on-device và gửi lại.

**Output**:
- 28 event được ghi đúng schema, không PII
- Cảnh báo tự động khi chỉ số tương thích tụt dưới ngưỡng
- Refund Rate đo được từ ngày launch

**Business Rules**:
- **BR-066.1**: `widget_render_failed` và `refund_detected` **bắt buộc hoạt động từ build TestFlight đầu tiên**, không phải bổ sung trước launch (PRD §12). Đây là cơ chế phát hiện sớm cho R-11 và R-12.
- **BR-066.2**: `paywall_shown` phải luôn kèm `days_since_install` để **audit** chính sách paywall (FR-045).
- **BR-066.3**: Payload đi qua whitelist tham số; **cấm** tham số tự do — đó là cách PII lọt ra.
- **BR-066.4**: Sự cố Firebase **không** được hạ trải nghiệm người dùng (AC-NFR-023.3).

**Validation Rules**:
- **VR-066.1**: Mọi event gửi đi phải khớp schema đã đăng ký; event lạ bị chặn ở tầng client.
- **VR-066.2**: Rà soát payload thực tế trước mỗi lần submit; phát hiện PII là lỗi chặn phát hành.

**Error Handling**:
- **ERR-066.1** (từ AF-017.2, AF-003.1): Không có mạng → event xếp hàng on-device và gửi khi có mạng.
- **ERR-066.2** (từ AC-NFR-023.3): Firebase gặp sự cố → app hoạt động đầy đủ, chỉ mất telemetry tạm thời.
- **ERR-066.3** (từ ERR-031.2): Lỗi render lặp ≥ 3 lần cùng kích thước → đánh dấu ưu tiên cao trong cảnh báo.

**Acceptance Criteria**:
- **AC-NFR-011.1**: WHEN bất kỳ event nào được gửi THEN payload **không** chứa user ID, email, số điện thoại, toạ độ GPS, hay nội dung lịch.
- **AC-NFR-019.2**: IF tỉ lệ tụt dưới 90% trong bất kỳ ngày nào THEN hệ thống phát cảnh báo tự động cho PM **trong ≤ 24 giờ** (liên quan FR-066).
- **AC-017.2**: WHEN WF-028 mở THEN hệ thống liệt kê **từng mục** dữ liệu sẽ gửi và báo cáo **không** chứa PII.
  > *Ghi chú truy vết*: AC-017.2 được **chia sẻ** với FR-032. FR-032 sở hữu bề mặt hiển thị danh sách dữ liệu; FR-066 sở hữu ràng buộc không-PII ở tầng gửi. Không phải AC bị nhân bản.

---

## Tổng hợp nhóm

| FR | Priority | UC nguồn | Số BR | Số VR | Số ERR | AC mang từ UC |
|---|---|---|---|---|---|---|
| FR-055 | Medium | UC-031 | 3 | 1 | 3 | AC-031.1, AC-031.3 |
| FR-056 | Medium | UC-031 | 2 | 1 | 2 | AC-031.4, AC-NFR-015.3 |
| FR-057 | Medium | UC-032 | 3 | 1 | 3 | AC-032.1, AC-032.3, AC-032.4 |
| FR-058 | Medium | UC-032 | 3 | 1 | 2 | AC-032.2 |
| FR-059 | Medium | UC-033 | 4 | 1 | 3 | AC-033.2, AC-033.3, AC-033.4 |
| FR-060 | Medium | UC-033 | 3 | 1 | 2 | AC-033.1 |
| FR-061 | Medium | UC-036 | 3 | 2 | 2 | AC-036.1, AC-036.2, AC-036.3 |
| FR-062 | Medium | UC-004 | 2 | 1 | 2 | AC-004.2 (chia sẻ với FR-007) |
| FR-066 | Medium | UC-017, UC-026, UC-029, UC-032 | 4 | 2 | 3 | AC-NFR-011.1, AC-NFR-019.2, AC-017.2 (chia sẻ với FR-032) |

**Tổng nhóm**: 9 FR (toàn bộ Medium) · 27 BR · 11 VR · 22 ERR · **16 AC** — phủ đủ 13 AC của UC-031 → UC-033, cộng 3 AC của UC-036 (theme).

**Ghi chú về UC-036**: khi viết nhóm này, việc rà soát hành động phụ ở `Use_Cases.md` §4.12 phát hiện **đổi theme** là một hành vi người dùng thấy được nhưng chưa có UC và chưa có AC. Theo `project-docs-contract` ("nếu một tài liệu downstream phát hiện lỗ hổng upstream thì sửa upstream trước"), **UC-036 đã được bổ sung vào `Use_Cases.md`** với AC-036.1 → AC-036.3, rồi FR-061 mang các AC đó sang. Đây là một gap được phát hiện và đóng, không phải AC do tầng FR tự nghĩ ra.
