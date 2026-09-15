# FR — Giọng Chào AI & Dashboard Ngữ Cảnh

**Sub-spec của**: [`Functional_Requirements.md`](./Functional_Requirements.md) · **Version** 2.4 · **Snapshot** 2026-08-07
**Phạm vi**: FR-033 → FR-042 · **UC nguồn**: UC-018 → UC-023 · **PRD Feature**: F3, F8
**Màn hình liên quan**: WF-006, WF-009, WF-010, WF-016, WF-018, WF-022

> Nhóm này chứa **điểm khác biệt hóa số 1** của sản phẩm. Hai ràng buộc bao trùm: **(1) 0 lệnh gọi mạng** trong toàn bộ đường xử lý ngữ cảnh (NFR-012); **(2) R-13 nhắc rằng ý tưởng "giọng AI trong xe" đã có người thử và thất bại** — nên mọi AC ở đây phải đo được, không dừng ở mức "có tính năng".

---

## FR-033: Bật hoặc tắt hoàn toàn giọng chào 📱

**Source UC**: UC-018
**Priority**: High · **Status**: Planned

**Description**:
Hệ thống phải cho người dùng tắt hẳn giọng chào bằng một công tắc, tôn trọng trạng thái đó ở mọi lần kết nối sau, và giữ nguyên cấu hình nguồn ngữ cảnh khi họ bật lại.

**Input**:
- `voiceGreetingEnabled` (Bool, mặc định `true` sau onboarding)
- Cấu hình nguồn ngữ cảnh hiện tại (từ FR-034)
- Entitlement hiện tại từ FR-043

**Processing**:
1. Hiển thị `ToggleMain` ở đầu WF-009.
2. Khi tắt: mọi mục cấu hình bên dưới **mờ đi nhưng vẫn đọc được** — người dùng thấy mình đang tắt cái gì.
3. Ghi `voiceGreetingEnabled` vào App Group; có hiệu lực từ lần `carplay_connected` kế tiếp, **không** cần khởi động lại app.
4. Khi bật lại: nạp lại cấu hình nguồn ngữ cảnh cũ, **không** reset về mặc định.
5. Nếu entitlement là Free: công tắc hiển thị trạng thái khoá, nhưng **nghe thử vẫn hoạt động đầy đủ** (bàn giao FR-036); nút mở khoá dẫn WF-010.
6. Hiển thị `StatusRow` trạng thái giọng chào trên WF-006 — **chỉ đọc**, không bấm được để tắt (tránh tắt nhầm từ Home).

**Output**:
- `voiceGreetingEnabled` được lưu và tôn trọng ở mọi lần kết nối
- Cấu hình nguồn ngữ cảnh được bảo toàn qua các lần tắt/bật

**Business Rules**:
- **BR-033.1**: Tắt giọng chào là trạng thái **hợp lệ và bền vững**; hệ thống không nhắc nhở người dùng bật lại.
- **BR-033.2**: Tắt rồi bật lại **không** reset cấu hình nguồn.
- **BR-033.3**: `StatusRow` trên WF-006 chỉ đọc — công tắc thật chỉ tồn tại ở WF-009.

**Validation Rules**:
- **VR-033.1**: Khi `voiceGreetingEnabled == false`, FR-037 **không** được gọi ContextEngine — tiết kiệm tài nguyên và bảo đảm hành vi đúng.

**Error Handling**:
- **ERR-033.1** (từ AF-018.1): Tắt rồi bật lại → cấu hình nguồn cũ được giữ nguyên.
- **ERR-033.2** (từ AF-018.2): Entitlement là Free → công tắc khoá, nghe thử vẫn đầy đủ, nút mở khoá dẫn WF-010.
- **ERR-033.3** (từ ERR-010.1): Entitlement không đọc được → mặc định về Free; công tắc ở trạng thái khoá nhưng nghe thử vẫn hoạt động.

**Acceptance Criteria**:
- **AC-018.1**: WHEN người dùng tắt giọng chào THEN hệ thống **không** phát bất kỳ câu chào nào ở các lần kết nối sau, cho tới khi được bật lại.
- **AC-018.2**: WHEN người dùng tắt rồi bật lại THEN cấu hình nguồn ngữ cảnh trước đó được giữ nguyên.
- **AC-018.3**: WHEN trạng thái được đổi THEN nó có hiệu lực ở lần `carplay_connected` kế tiếp mà không cần khởi động lại app.

---

## FR-034: Quản lý nguồn ngữ cảnh của giọng chào 📱

**Source UC**: UC-019
**Priority**: Medium · **Status**: Planned

**Description**:
Hệ thống phải cho người dùng bật/tắt độc lập 4 nguồn ngữ cảnh (giờ trong ngày, thời tiết, lịch, điểm đến dự đoán), kèm một ví dụ câu chào cụ thể cho từng nguồn, và chỉ đọc dữ liệu từ nguồn được bật.

**Input**:
- `enabledContextSources` (Set: time | weather | calendar | destination), mặc định tất cả bật
- Trạng thái quyền tương ứng từ FR-008
- Ví dụ câu chào mẫu cho từng nguồn (đóng gói trong `Resources`, theo từng ngôn ngữ)

**Processing**:
1. Hiển thị 4 `ToggleRow`, mỗi dòng có: tên nguồn, toggle, trạng thái quyền, và **một ví dụ câu chào cụ thể** sinh từ nguồn đó.
2. Hiển thị ví dụ bằng đúng ngôn ngữ app hiện tại (bàn giao FR-039).
3. Khi người dùng tắt một nguồn, ContextEngine **không** đọc dữ liệu từ nguồn đó ở các lượt sinh sau.
4. Khi người dùng bật một nguồn cần quyền mà chưa có quyền: bàn giao FR-035.
5. Nếu cả 4 nguồn đều tắt: hệ thống vẫn phát **câu chào trung tính**, không im lặng và không báo lỗi.
6. Tính tập nguồn khả dụng thật = `enabledContextSources` ∩ (nguồn có quyền), bàn giao FR-008 và FR-037.

**Output**:
- `enabledContextSources` được lưu; ContextEngine chỉ đọc đúng những nguồn được bật và có quyền
- Người dùng biết cụ thể mỗi nguồn tạo ra loại câu chào nào

**Business Rules**:
- **BR-034.1**: Nguồn "giờ trong ngày" **không cần quyền** và luôn khả dụng — đó là đường lui bảo đảm giọng chào không bao giờ im lặng.
- **BR-034.2**: Mỗi nguồn phải kèm **một ví dụ cụ thể**; danh sách toggle không có ví dụ thì người dùng không có cơ sở để quyết định.
- **BR-034.3**: Bốn nguồn độc lập; mọi tổ hợp 16 khả năng đều hợp lệ.

**Validation Rules**:
- **VR-034.1**: Trước khi đọc bất kỳ nguồn nào, kiểm cả `enabledContextSources` **và** trạng thái quyền; thiếu một trong hai phép kiểm là lỗi.

**Error Handling**:
- **ERR-034.1** (từ AF-019.1): Nguồn được bật nhưng quyền bị từ chối → bàn giao FR-035, hiện trạng thái "cần quyền".
- **ERR-034.2** (từ AF-019.2): Tắt hết 4 nguồn → vẫn phát câu chào trung tính, không im lặng.
- **ERR-034.3** (từ AF-019.3): Nguồn thời tiết không lấy được dữ liệu → bỏ qua nguồn đó cho lượt này, dùng nguồn còn lại.

**Acceptance Criteria**:
- **AC-019.1**: WHEN người dùng tắt một nguồn THEN ContextEngine **không** đọc dữ liệu từ nguồn đó ở các lượt sinh câu chào sau.
- **AC-019.3**: IF cả 4 nguồn đều tắt THEN hệ thống vẫn phát một câu chào trung tính, không im lặng và không báo lỗi.
- **AC-019.4**: WHEN mỗi nguồn được hiển thị THEN có kèm một ví dụ câu chào cụ thể sinh ra từ nguồn đó.

---

## FR-035: Chặn bật nguồn ngữ cảnh thiếu quyền 📱

**Source UC**: UC-019 (AF-019.1)
**Priority**: Medium · **Status**: Planned

**Description**:
Hệ thống **cấm** tồn tại trạng thái "toggle đã bật nhưng nguồn âm thầm không hoạt động". Khi thiếu quyền, toggle phải trả về tắt kèm nhãn "cần quyền" và một lối vào cấp quyền.

**Input**:
- Nguồn người dùng vừa bật và quyền tương ứng
- Trạng thái quyền: `notDetermined` | `denied` | `authorized`

**Processing**:
1. Người dùng bật toggle của một nguồn cần quyền.
2. Kiểm quyền tương ứng. Nếu **không** `authorized`: toggle **nảy nhẹ về vị trí tắt** trong 0,2s (sub-flow SF-012) và hiện nhãn "cần quyền" kèm nút hành động.
3. Nếu quyền là `notDetermined`: nút hành động mở WF-022 (bàn giao FR-007).
4. Nếu quyền là `denied`: nút hành động đổi thành "Mở Cài đặt" và dẫn sang Cài đặt hệ thống (iOS không cho hỏi lại).
5. Khi quyền được cấp: toggle chuyển sang bật và ví dụ câu chào của nguồn đó xuất hiện.
6. Nếu quyền vẫn bị từ chối: toggle giữ tắt, nhãn nêu rõ cần cấp trong Cài đặt.

**Output**:
- Không tồn tại tổ hợp (toggle bật) × (không có quyền)
- Người dùng luôn có một đường đi tiếp từ mọi trạng thái

**Business Rules**:
- **BR-035.1**: **Cấm** trạng thái bật-mà-không-chạy. Trạng thái đó là nguyên nhân người dùng kết luận "app không hoạt động".
- **BR-035.2**: Chuyển động nảy về tắt là **có chủ ý** — nó truyền đạt "không phải bạn bấm sai, mà điều kiện chưa đủ" rõ hơn một dòng chữ.

**Validation Rules**:
- **VR-035.1**: `enabledContextSources` chỉ được chứa nguồn có quyền tương ứng (hoặc nguồn không cần quyền); bất biến này phải luôn đúng.

**Error Handling**:
- **ERR-035.1** (từ AF-019.1): Bật nguồn thiếu quyền → toggle nảy về tắt + nhãn "cần quyền".
- **ERR-035.2** (từ ERR-007.4): Dialog quyền không mở được → dẫn sang Cài đặt hệ thống.

**Acceptance Criteria**:
- **AC-019.2**: IF một nguồn được bật nhưng quyền tương ứng bị từ chối THEN WF-009 hiển thị rõ trạng thái "cần quyền" kèm lối vào cấp quyền.

---

## FR-036: Nghe thử giọng chào sinh on-device 📱

**Source UC**: UC-020
**Priority**: High · **Status**: Planned

**Description**:
Hệ thống phải sinh câu chào từ **ngữ cảnh thật tại thời điểm nghe thử** (không phải câu mẫu cố định), phát kèm chữ hiện đồng thời, và trả về câu **khác** khi người dùng nghe thử lần nữa. Đây là cơ chế để người dùng tự xác minh tính năng có thật — đối trọng trực tiếp với R-10 và R-13.

**Input**:
- Tập nguồn ngữ cảnh khả dụng (từ FR-034, FR-008)
- Giá trị ngữ cảnh thật lúc này: giờ hiện tại, thời tiết hiện tại, sự kiện lịch sắp tới, điểm đến dự đoán
- Câu chào của lượt nghe thử trước (để chống lặp)
- Ngôn ngữ app hiện tại

**Processing**:
1. Người dùng chạm "Nghe thử" → ContextEngine đọc các nguồn đang bật và có quyền.
2. Sinh câu chào **on-device** bằng Core ML chọn biến thể + `AVSpeechSynthesizer`; **0 lệnh gọi mạng**.
3. So với câu của lượt trước; nếu giống, chọn biến thể khác (bàn giao FR-038).
4. Phát qua loa iPhone và **hiển thị chữ đồng thời** — chữ hiện theo tiến độ đọc của TTS, không hiện trước, không hiện sau (sub-flow SF-011).
5. Ghi nhỏ bên dưới câu chào: nguồn ngữ cảnh đã dùng (time / weather / calendar / destination).
6. Nếu đang có nhạc phát: áp dụng ducking thật để bản nghe thử phản ánh đúng trải nghiệm trên xe.
7. Nếu entitlement là Free: nghe thử **đầy đủ**, nhưng nút sau đó là "Mở khoá" thay vì "Áp dụng".

**Output**:
- Người dùng đã nghe ≥ 1 câu chào thật do ContextEngine sinh, kèm chữ và nguồn ngữ cảnh
- Sau ≥ 4 lần nghe thử, người dùng thấy đủ dải biến thể

**Business Rules**:
- **BR-036.1**: Câu chào nghe thử **phải** sinh từ ngữ cảnh thật lúc đó; dùng câu mẫu cố định ở đây là nói dối về năng lực sản phẩm.
- **BR-036.2**: Nghe thử phải hoạt động đầy đủ ở gói Free — đây là cơ chế xây niềm tin, không phải tính năng để khoá.
- **BR-036.3**: Chữ và âm thanh phải đồng thời; hiện chữ khi không phát được âm thanh vẫn hợp lệ (xem ERR-036.1), nhưng phát âm thanh mà không hiện chữ là thiếu.

**Validation Rules**:
- **VR-036.1**: Hai lượt nghe thử liên tiếp phải cho hai câu khác nhau; giống nhau là lỗi chức năng.
- **VR-036.2**: Không có lệnh gọi mạng nào trong đường sinh câu chào — kiểm bằng test chế độ máy bay.

**Error Handling**:
- **ERR-036.1** (từ State Variation WF-009 "Error"): TTS không phát được → **vẫn hiển thị chữ** câu chào kèm lý do; nội dung vẫn kiểm chứng được dù âm thanh lỗi.
- **ERR-036.2** (từ AF-020.1): Entitlement là Free → nghe thử đầy đủ, không cắt, không watermark; nút mở khoá dẫn WF-010.
- **ERR-036.3** (từ AF-020.2): Không có quyền nào → nghe thử vẫn hoạt động với nguồn "giờ".
- **ERR-036.4** (từ AF-020.3): Đang phát nhạc → áp dụng ducking như trên xe.

**Acceptance Criteria**:
- **AC-020.1**: WHEN người dùng chạm "Nghe thử" THEN câu chào được sinh từ ngữ cảnh thật tại thời điểm đó, **không** phải câu mẫu cố định.
- **AC-020.2**: WHEN người dùng chạm "Nghe thử" hai lần liên tiếp THEN hai câu chào **không** giống y hệt nhau.
- **AC-020.3**: WHEN câu chào phát THEN chữ tương ứng được hiển thị đồng thời trên màn hình.
- **AC-020.4**: WHEN nghe thử THEN toàn bộ quá trình sinh câu chào diễn ra on-device, **không có lệnh gọi mạng nào**.

---

## FR-037: Sinh và phát giọng chào khi lên xe 🚗

**Source UC**: UC-021
**Priority**: High · **Status**: Planned

**Description**:
Hệ thống phải sinh câu chào on-device và phát qua loa xe trong **≤ 2 giây** kể từ `carplay_connected`, sau sound Connect, và phải rơi về câu chào theo giờ khi không đủ ngữ cảnh — **không im lặng và không báo lỗi**.

**Input**:
- Sự kiện `carplay_connected`
- `voiceGreetingEnabled`, tập nguồn khả dụng, entitlement
- Giá trị ngữ cảnh thật tại thời điểm đó
- Trạng thái phiên audio

**Processing**:
1. Nếu `voiceGreetingEnabled == false` hoặc entitlement là Free: kết thúc; nếu Free thì bàn giao FR-041 để WF-018 hiện một dòng chữ tĩnh.
2. Nạp sẵn mô hình Core ML trong lúc chuẩn bị phiên CarPlay (**warm**, không nạp lười lúc scene active) để đạt ngưỡng 2s.
3. ContextEngine đọc nguồn khả dụng và chọn biến thể phù hợp — hoàn toàn on-device, **0 lệnh gọi mạng**.
4. Bàn giao FR-038 để kiểm chống lặp và ràng buộc nội dung.
5. Bàn giao FR-017 để kiểm điều kiện phiên audio (cuộc gọi / chỉ dẫn dẫn đường) — dùng **chung** chính sách với sound.
6. Phát qua `AVSpeechSynthesizer` ra **loa xe**, sau sound Connect, trong ≤ 2s kể từ `carplay_connected`.
7. Nếu không đủ ngữ cảnh: dùng biến thể theo giờ trong ngày; câu đó vẫn phải nghe tự nhiên, **không** nghe như bản rút gọn.
8. Ghi `voice_greeting_played` kèm `context_used` phân biệt time / weather / calendar / destination.

**Output**:
- Câu chào đã phát qua loa xe, hoặc lượt phát bị bỏ có lý do ghi nhận
- Event `voice_greeting_played` kèm nguồn ngữ cảnh đã dùng

**Business Rules**:
- **BR-037.1**: **Cấm** mọi lệnh gọi mạng trong đường sinh câu chào (NFR-012). Không có fallback cloud (`Project_Overview.md` §3.3 Quyết định 4).
- **BR-037.2**: Thiếu ngữ cảnh **không bao giờ** dẫn tới im lặng hoặc câu báo lỗi — luôn có biến thể theo giờ.
- **BR-037.3**: Giọng chào dùng **chung** chính sách nhường phiên audio với sound (FR-017), để hành vi nhất quán.
- **BR-037.4**: Mô hình Core ML phải được nạp sẵn; nạp lười tại scene active sẽ phá ngưỡng 2s (AC-NFR-004.3).

**Validation Rules**:
- **VR-037.1**: Câu chào chỉ được phát **sau** khi sound Connect kết thúc, để hai âm thanh không chồng nhau.

**Error Handling**:
- **ERR-037.1** (từ AF-021.1): Câu vừa chọn giống lần trước → bàn giao FR-038 để chọn biến thể khác.
- **ERR-037.2** (từ AF-021.2): Đang có cuộc gọi → bỏ lượt phát, **không phát bù** (FR-017).
- **ERR-037.3** (từ AF-021.3): Không đủ ngữ cảnh → rơi về câu theo giờ; không im lặng, không báo lỗi.
- **ERR-037.4** (từ AF-021.4): Entitlement là Free → không phát; WF-018 nêu bằng một dòng chữ tĩnh, **không popup**.
- **ERR-037.5** (từ AF-021.5): Ngôn ngữ là ES hoặc PT-BR → bàn giao FR-039.

**Acceptance Criteria**:
- **AC-021.1**: WHEN `carplay_connected` xảy ra THEN câu chào bắt đầu phát trong ≤ 2s.
- **AC-021.2**: WHEN câu chào được sinh THEN toàn bộ quá trình chạy on-device và **không có lệnh gọi mạng nào**.
- **AC-021.5**: IF không có ngữ cảnh nào khả dụng THEN hệ thống phát câu chào theo giờ trong ngày, không im lặng.

---

## FR-038: Chống lặp câu chào và ràng buộc nội dung 🚗📱

**Source UC**: UC-021
**Priority**: High · **Status**: Planned

**Description**:
Hệ thống phải bảo đảm có ≥ 4 biến thể ngữ cảnh khả dụng, **không lặp lại câu y hệt hai lần liên tiếp**, và **cấm** mọi tham chiếu Marvel/Disney (bao gồm tên "Jarvis") trong tập nội dung — ràng buộc trực tiếp từ R-10.

**Input**:
- Tập biến thể câu chào theo từng nguồn ngữ cảnh và từng ngôn ngữ
- Câu chào của lượt phát gần nhất (lưu on-device)
- Danh sách từ/tên bị cấm

**Processing**:
1. Ở giai đoạn dựng dữ liệu (build time): rà toàn bộ tập biến thể theo danh sách từ bị cấm; biến thể vi phạm bị **loại khỏi bundle**, không phải lọc tại runtime.
2. Ở runtime: sau khi ContextEngine chọn biến thể, so với câu của lượt gần nhất.
3. Nếu trùng: chọn biến thể khác **trước khi phát**.
4. Nếu tập biến thể khả dụng chỉ còn 1 phần tử (trường hợp ngữ cảnh rất hẹp): cho phép lặp nhưng ghi nhận vào telemetry để bổ sung nội dung.
5. Lưu câu vừa phát để so ở lượt sau.
6. Kiểm số biến thể khả dụng ≥ 4 cho mỗi ngôn ngữ ở giai đoạn build; thiếu là lỗi build.

**Output**:
- Câu chào không lặp y hệt hai lần liên tiếp
- Tập nội dung không chứa tham chiếu bị cấm — được bảo đảm ở build time

**Business Rules**:
- **BR-038.1**: Lọc nội dung bị cấm diễn ra ở **build time**, không phải runtime. Lọc runtime có thể bị bỏ sót và để lọt ra người dùng.
- **BR-038.2**: **Cấm tuyệt đối** tên "Jarvis" và mọi tham chiếu Marvel/Disney — đây là ràng buộc trademark, không phải lựa chọn văn phong (R-10).
- **BR-038.3**: Số biến thể ngữ cảnh khả dụng ≥ 4 cho **mỗi** ngôn ngữ; thiếu là lỗi build, không phải nợ nội dung.

**Validation Rules**:
- **VR-038.1**: Ở giai đoạn build, kiểm mỗi ngôn ngữ có ≥ 4 biến thể; kiểm 0 kết quả khớp danh sách từ bị cấm.
- **VR-038.2**: Ở runtime, câu sắp phát khác câu vừa phát (trừ trường hợp tập chỉ còn 1 phần tử, và trường hợp đó phải được ghi nhận).

**Error Handling**:
- **ERR-038.1** (từ AF-021.1): Câu trùng câu trước → chọn biến thể khác trước khi phát.
- **ERR-038.2** (từ State Variation FR-038 "Error"): Tập biến thể của một ngữ cảnh cạn → ghi nhận vào telemetry, cho phép lặp tạm thời thay vì im lặng.

**Acceptance Criteria**:
- **AC-021.3**: WHEN hệ thống chọn câu chào THEN có ≥ 4 biến thể ngữ cảnh khả dụng và **không lặp lại câu y hệt hai lần liên tiếp**.
- **AC-021.4**: WHEN câu chào phát xong THEN hệ thống ghi `voice_greeting_played` kèm `context_used` phân biệt time/weather/calendar/destination.
- **AC-021.6**: WHEN nội dung câu chào được sinh THEN **không** chứa tên "Jarvis" hoặc bất kỳ tham chiếu Marvel/Disney nào (R-10).

---

## FR-039: Nội dung giọng chào theo ngôn ngữ 📱🚗

**Source UC**: UC-021, UC-031
**Priority**: Medium · **Status**: Planned

**Description**:
Hệ thống phải phát câu chào bằng **đúng ngôn ngữ app đang chọn** (EN / ES / PT-BR) — nội dung câu chào, không chỉ chuỗi UI — và không cắt câu đang phát khi người dùng đổi ngôn ngữ giữa phiên.

**Input**:
- Ngôn ngữ app hiện tại (từ FR-055)
- Tập biến thể câu chào theo từng ngôn ngữ trong `Resources`
- Voice của `AVSpeechSynthesizer` khả dụng cho ngôn ngữ đó

**Processing**:
1. Đọc ngôn ngữ app hiện tại.
2. Chọn tập biến thể câu chào của đúng ngôn ngữ đó.
3. Chọn voice `AVSpeechSynthesizer` khớp locale; nếu không có voice cho locale đó, dùng voice mặc định của ngôn ngữ gần nhất và ghi nhận.
4. Nếu người dùng đổi ngôn ngữ trong lúc một câu chào đang phát: **không cắt câu đang phát**; ngôn ngữ mới áp dụng từ lượt kế tiếp.
5. Ví dụ câu chào ở WF-009 cũng đổi theo ngôn ngữ (bàn giao FR-034 Processing 2).

**Output**:
- Câu chào bằng đúng ngôn ngữ đã chọn, cả trong nghe thử và trên xe
- Câu đang phát không bị cắt giữa câu khi đổi ngôn ngữ

**Business Rules**:
- **BR-039.1**: Localize nội dung giọng chào là **bắt buộc**, không phải tuỳ chọn. PRD §7 F9 nêu rõ "bao gồm cả nội dung giọng chào AI, không chỉ UI".
- **BR-039.2**: **Cấm** cắt câu đang phát giữa câu khi đổi ngôn ngữ.

**Validation Rules**:
- **VR-039.1**: Mỗi ngôn ngữ phải có ≥ 4 biến thể cho mỗi nguồn ngữ cảnh (kiểm ở build time, xem VR-038.1).

**Error Handling**:
- **ERR-039.1** (từ AF-031.2): Đổi ngôn ngữ khi đang cắm CarPlay → câu đang phát không bị cắt; ngôn ngữ mới từ lượt kế tiếp.
- **ERR-039.2** (từ ERR-056.1): Thiếu biến thể cho một ngôn ngữ → dùng biến thể English cho đúng ngữ cảnh đó và ghi nhận; **không** phát chuỗi khoá dịch thô.

**Acceptance Criteria**:
- **AC-021.7**: WHEN ngôn ngữ app là ES hoặc PT-BR THEN nội dung câu chào phát bằng đúng ngôn ngữ đó.
- **AC-031.2**: WHEN ngôn ngữ là ES hoặc PT-BR THEN **nội dung giọng chào AI** cũng bằng ngôn ngữ đó, không chỉ UI.
- **AC-031.5**: IF người dùng đổi ngôn ngữ khi đang cắm CarPlay THEN câu chào đang phát **không** bị cắt giữa câu.

---

## FR-040: Sắp xếp thẻ dashboard theo ngữ cảnh on-device 🚗

**Source UC**: UC-022
**Priority**: High · **Status**: Planned

**Description**:
Hệ thống phải tự sắp xếp thứ tự thẻ trên dashboard CarPlay theo ngữ cảnh, học hoàn toàn on-device, **không bắt người dùng tự tạo hay cấu hình gì**, và phải nói rõ khi chưa đủ dữ liệu để cá nhân hóa.

**Input**:
- Lịch sử hành vi on-device: thẻ nào được chạm, vào giờ nào, trên tuyến nào (SQLite)
- Ngữ cảnh hiện tại: giờ, tuyến quen, thói quen nghe nhạc
- Danh sách thẻ khả dụng theo entitlement (từ FR-041)
- `CPTemplateApplicationScene` bounds

**Processing**:
1. Khi CarPlay scene active, tính layout dashboard theo scene bounds **tại runtime** (cùng nguyên tắc FR-029).
2. ContextEngine tính điểm ưu tiên cho từng thẻ dựa trên lịch sử on-device — **dữ liệu không rời thiết bị**.
3. Nếu chưa đủ dữ liệu: dùng thứ tự mặc định và hiển thị **một dòng nói rõ dashboard sẽ tự đổi sau vài chuyến** — không tuyên bố đã cá nhân hóa.
4. Nếu đủ dữ liệu: đặt thẻ điểm cao nhất vào Zone A (diện tích lớn nhất), phần còn lại vào Zone B.
5. Khi ngữ cảnh đổi giữa phiên: cập nhật thứ tự bằng **crossfade tại chỗ 0,4s**, không dùng chuyển động vị trí; throttle **tối đa 1 lần mỗi 30 giây** (sub-flow SF-017).
6. Nếu một thẻ đang được chạm: **hoãn** việc sắp xếp lại tới khi hành động kết thúc.
7. Khi người dùng bỏ qua một thẻ được gợi ý: hạ trọng số thẻ đó — phản hồi ngầm, **không** yêu cầu vào Settings.
8. Nếu ContextEngine không có kết luận chắc chắn: **giữ nguyên** thứ tự hiện tại.

**Output**:
- Dashboard hiển thị đúng trong bounds với thứ tự phản ánh ngữ cảnh (hoặc thứ tự mặc định được nói rõ)
- Trọng số thẻ được cập nhật từ phản hồi ngầm của người dùng, lưu on-device

**Business Rules**:
- **BR-040.1**: Toàn bộ dữ liệu học **không rời thiết bị** (NFR-012).
- **BR-040.2**: Hệ thống **không bao giờ** yêu cầu người dùng tự tạo hoặc cấu hình widget/thẻ để dashboard hoạt động — đây là phản ứng trực tiếp với complaint *"you had to create it yourself"* của đối thủ.
- **BR-040.3**: Sắp xếp lại dùng **crossfade, không chuyển động vị trí**, và throttle 1 lần/30s. Thẻ trượt qua nhau trên màn hình xe kéo mắt người lái khỏi đường — đây là quyết định an toàn.
- **BR-040.4**: Khi không chắc chắn, **giữ nguyên** thứ tự cũ. Thà thứ tự cũ còn hơn một thay đổi gây phân tán không có lý do rõ.

**Validation Rules**:
- **VR-040.1**: Layout dashboard tính từ scene bounds tại runtime; **không** hằng số kích thước (cùng ràng buộc NFR-021).
- **VR-040.2**: Không sắp xếp lại khi một thẻ đang trong trạng thái được chạm.

**Error Handling**:
- **ERR-040.1** (từ AF-022.1): Chưa đủ dữ liệu để học → thứ tự mặc định + dòng nói rõ; không giả vờ đã cá nhân hóa.
- **ERR-040.2** (từ AF-022.2): Ngữ cảnh đoán sai → người dùng bỏ qua thẻ, hệ thống hạ trọng số; không cần vào Settings.
- **ERR-040.3** (từ SF-017 Recovery): ContextEngine không có kết luận chắc chắn → giữ nguyên thứ tự hiện tại.

**Acceptance Criteria**:
- **AC-022.1**: WHEN CarPlay scene active THEN layout dashboard được tính theo scene bounds tại runtime, không dùng hằng số kích thước.
- **AC-022.2**: WHEN ContextEngine sắp thẻ THEN toàn bộ dữ liệu học **không rời thiết bị**.
- **AC-022.3**: IF chưa đủ dữ liệu để cá nhân hóa THEN hệ thống dùng thứ tự mặc định và nói rõ điều đó, không tuyên bố đã cá nhân hóa.
- **AC-022.4**: WHEN người dùng dùng app THEN hệ thống **không bao giờ** yêu cầu người dùng tự tạo hoặc tự cấu hình widget/thẻ để dashboard hoạt động.

---

## FR-041: Cấu hình dashboard theo entitlement và trạng thái offline 🚗

**Source UC**: UC-022
**Priority**: High · **Status**: Planned

**Description**:
Hệ thống phải hiển thị đúng cấu hình dashboard theo entitlement (gói Free = nhạc đang phát + thời tiết + 1 shortcut), và khi mất mạng phải dùng dữ liệu cache **kèm thời điểm cập nhật cuối** thay vì hiện thẻ rỗng.

**Input**:
- Entitlement hiện tại từ FR-043
- Trạng thái mạng
- Dữ liệu cache của từng thẻ kèm dấu thời gian cập nhật

**Processing**:
1. Hỏi `EntitlementService` tập thẻ khả dụng: Free = {nhạc đang phát, thời tiết, 1 shortcut}; Premium/Lifetime = toàn bộ.
2. Bàn giao FR-040 để sắp thứ tự trong tập thẻ khả dụng.
3. Nếu entitlement là Free: hiển thị WF-018 với **một dòng chữ tĩnh** nêu tính năng nào có ở Premium — không popup, **không chắn nội dung**, và **không có exit nào dẫn tới paywall từ màn hình xe**.
4. Nếu mất mạng: thẻ nhạc và thời tiết dùng dữ liệu cache và **ghi rõ thời điểm cập nhật cuối**; thẻ shortcut vẫn hoạt động bình thường.
5. Nếu một thẻ không lấy được dữ liệu: hiện thông báo gọn **trên thẻ đó** kèm hành động thay thế; các thẻ khác không bị ảnh hưởng.
6. Nếu entitlement không đọc được: mặc định về Free và **vẫn cho dùng**; không chặn, không hiện lỗi trên màn hình xe.

**Output**:
- Dashboard đúng cấu hình entitlement; ở gói Free là **cấu hình đã chốt của PRD §11**, không phải bản bị làm mờ
- Ở trạng thái offline: thẻ có nội dung kèm thời điểm cập nhật, không có thẻ rỗng

**Business Rules**:
- **BR-041.1**: Cấu hình Free là **cấu hình đã chốt** (PRD §11), không phải bản cắt bớt tuỳ ý.
- **BR-041.2**: `StaticNotice` trên WF-018 **cấm** chắn nội dung và **cấm** mở paywall từ màn hình xe — an toàn khi lái quan trọng hơn conversion.
- **BR-041.3**: Không đọc được entitlement → mặc định Free và **vẫn cho dùng**; chặn người dùng vì lỗi đọc entitlement là hành vi sai.
- **BR-041.4**: Thẻ dùng cache **phải** hiện thời điểm cập nhật cuối; cache không có nhãn thời gian là dữ liệu gây nhầm.

**Validation Rules**:
- **VR-041.1**: Số thẻ hiển thị ≤ giới hạn của entitlement hiện tại tại mọi thời điểm.

**Error Handling**:
- **ERR-041.1** (từ AF-022.3): Mất mạng → thẻ dùng cache kèm thời điểm cập nhật; shortcut vẫn hoạt động.
- **ERR-041.2** (từ AF-022.4): Entitlement là Free → dashboard cơ bản theo cấu hình đã chốt + WF-018.
- **ERR-041.3** (từ State Variation WF-018 "Error"): Không đọc được entitlement → mặc định Free, vẫn cho dùng.

**Acceptance Criteria**:
- **AC-022.5**: IF người dùng ở gói Free THEN dashboard hiển thị đúng cấu hình Free đã chốt: nhạc đang phát, thời tiết, 1 shortcut.
- **AC-022.6**: WHEN mất mạng THEN thẻ dùng dữ liệu cache và hiển thị rõ thời điểm cập nhật cuối.

---

## FR-042: Thực thi hành động khi chạm thẻ dashboard 🚗

**Source UC**: UC-023
**Priority**: High · **Status**: Planned

**Description**:
Hệ thống phải thực hiện hành động của thẻ trong ≤ 1 giây sau khi người dùng chạm, báo lỗi **trên thẻ** (không modal), và **không mở paywall trên màn hình xe** khi thẻ thuộc Premium.

**Input**:
- Thẻ được chạm và loại hành động: `playMusic` | `navigate` | `callShortcut`
- Trạng thái entitlement và trạng thái mạng
- Hành động đang chạy (nếu có)

**Processing**:
1. Người dùng chạm thẻ → nếu thẻ thuộc Premium mà entitlement là Free: hiển thị trạng thái khoá **bằng chữ trên thẻ**; **không** mở paywall.
2. Nếu thẻ khả dụng: bắt đầu hành động tương ứng trong ≤ 1s (phát nhạc / mở Apple Maps / gọi shortcut hệ thống).
3. Nếu người dùng chạm thẻ khác trong lúc hành động đang chạy: **huỷ** hành động trước, không xếp hàng.
4. Nếu hành động thất bại: hiện thông báo gọn **trên thẻ** kèm một hành động thay thế; **không modal**; các thẻ khác không bị ảnh hưởng.
5. Nếu mất mạng: thẻ nhạc chuyển sang nguồn cục bộ; thẻ dẫn đường dùng địa điểm đã cache.
6. Ghi `ai_recommendation_tapped`; bàn giao FR-040 để cập nhật trọng số thẻ.

**Output**:
- Hành động đã thực hiện, hoặc đã báo thất bại kèm đường thay thế
- Phản hồi ngầm được ghi để FR-040 học

**Business Rules**:
- **BR-042.1**: Mọi touch target trên WF-016 ≥ 44pt (NFR-014).
- **BR-042.2**: **Cấm** modal trên bề mặt CarPlay; lỗi báo trên thẻ.
- **BR-042.3**: **Cấm** mở paywall từ màn hình xe trong mọi hoàn cảnh.
- **BR-042.4**: Chạm thẻ mới **huỷ** hành động cũ; xếp hàng hành động khi đang lái tạo hành vi khó đoán.

**Validation Rules**:
- **VR-042.1**: Hành động chỉ được thực thi nếu entitlement cho phép; kiểm trước khi thực thi, không thực thi rồi mới kiểm.

**Error Handling**:
- **ERR-042.1** (từ AF-023.1): Hành động thất bại → thông báo gọn trên thẻ + hành động thay thế; không modal.
- **ERR-042.2** (từ AF-023.2): Mất mạng → thẻ nhạc dùng nguồn cục bộ; thẻ dẫn đường dùng địa điểm cache.
- **ERR-042.3** (từ AF-023.3): Thẻ thuộc Premium → trạng thái khoá bằng chữ, **không** mở paywall trên xe.
- **ERR-042.4** (từ AF-023.4): Chạm nhiều thẻ liên tiếp → huỷ hành động trước, không xếp hàng.

**Acceptance Criteria**:
- **AC-023.1**: WHEN người dùng chạm một thẻ THEN hành động tương ứng bắt đầu trong ≤ 1s.
- **AC-023.2**: WHEN thẻ được hiển thị THEN mọi touch target ≥ 44pt.
- **AC-023.3**: IF hành động thất bại THEN hệ thống hiển thị thông báo gọn kèm hành động thay thế, và **không** dùng modal trên bề mặt CarPlay.
- **AC-023.4**: IF thẻ thuộc tính năng Premium THEN hệ thống hiển thị trạng thái khoá bằng chữ và **không** mở paywall trên màn hình xe.
- **AC-023.5**: WHEN người dùng chạm thẻ THEN hệ thống ghi `ai_recommendation_tapped`; mục tiêu tap-through rate ≥ 30%.

---

## Tổng hợp nhóm

| FR | Priority | UC nguồn | Số BR | Số VR | Số ERR | AC mang từ UC |
|---|---|---|---|---|---|---|
| FR-033 | High | UC-018 | 3 | 1 | 3 | AC-018.1, AC-018.2, AC-018.3 |
| FR-034 | Medium | UC-019 | 3 | 1 | 3 | AC-019.1, AC-019.3, AC-019.4 |
| FR-035 | Medium | UC-019 | 2 | 1 | 2 | AC-019.2 |
| FR-036 | High | UC-020 | 3 | 2 | 4 | AC-020.1 → AC-020.4 |
| FR-037 | High | UC-021 | 4 | 1 | 5 | AC-021.1, AC-021.2, AC-021.5 |
| FR-038 | High | UC-021 | 3 | 2 | 2 | AC-021.3, AC-021.4, AC-021.6 |
| FR-039 | Medium | UC-021, UC-031 | 2 | 1 | 2 | AC-021.7, AC-031.2, AC-031.5 |
| FR-040 | High | UC-022 | 4 | 2 | 3 | AC-022.1 → AC-022.4 |
| FR-041 | High | UC-022 | 4 | 1 | 3 | AC-022.5, AC-022.6 |
| FR-042 | High | UC-023 | 4 | 1 | 4 | AC-023.1 → AC-023.5 |

**Tổng nhóm**: 10 FR (7 High, 3 Medium) · 32 BR · 13 VR · 31 ERR · **31 AC** — phủ đủ toàn bộ 29 AC của UC-018 → UC-023, cộng AC-031.2 và AC-031.5 của UC-031 (hai AC về ngôn ngữ giọng chào, thuộc FR-039).
