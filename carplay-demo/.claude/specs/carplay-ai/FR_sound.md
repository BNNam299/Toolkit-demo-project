# FR — Âm Thanh Lên/Xuống Xe

**Sub-spec của**: [`Functional_Requirements.md`](./Functional_Requirements.md) · **Version** 2.4 · **Snapshot** 2026-08-07
**Phạm vi**: FR-010 → FR-020 · **UC nguồn**: UC-006 → UC-011 · **PRD Feature**: F1
**Màn hình liên quan**: WF-004, WF-007, WF-012, WF-016, WF-017, WF-020, WF-030

> Nhóm này phục vụ **tính năng có PMF cao nhất** theo PRD §6. Ba complaint cụ thể của đối thủ được chuyển thành ràng buộc kỹ thuật ở đây: sound bị nhạc lấn (FR-016), sound phát qua loa iPhone (FR-020), sound disconnect lệch thời điểm tắt máy (FR-019).

---

## FR-010: Danh mục sound và phân tầng Free/Premium 📱

**Source UC**: UC-006
**Priority**: High · **Status**: Planned

**Description**:
Hệ thống phải cung cấp ≥ 12 preset âm thanh chia theo nhóm, trong đó đúng 3 preset thuộc gói Free, và phải cho nghe thử **đầy đủ** cả preset khoá — không cắt ngắn, không watermark.

**Input**:
- Danh mục preset đóng gói trong bundle: `id`, `name`, `group`, `durationMs`, `tier` (free/premium), `assetPath`
- Entitlement hiện tại từ FR-043

**Processing**:
1. Nạp danh mục preset; nhóm theo `group`.
2. Với mỗi preset, tính trạng thái hiển thị = `tier` × entitlement: `unlocked` hoặc `locked`.
3. Hiển thị danh sách với `LockLabel` rõ ràng trên preset `locked` — **không ẩn** preset khoá.
4. Ghim preset đang dùng lên đầu danh sách và đánh dấu.
5. Cho phép nghe thử **mọi** preset bất kể trạng thái khoá (bàn giao FR-011, FR-012).
6. Nút gán trên preset `locked` đổi thành "Mở khoá" và dẫn WF-010 kèm ngữ cảnh đúng preset đó.

**Output**:
- Danh sách preset với trạng thái khoá chính xác; preset đang dùng được ghim đầu
- Nếu người dùng chạm preset khoá: chuyển WF-010 với `trigger_source = sound_preset`

**Business Rules**:
- **BR-010.1**: Có ≥ 12 preset tại thời điểm phát hành, trong đó **đúng 3** preset thuộc gói Free.
- **BR-010.2**: Preset khoá **phải** nghe thử được toàn bộ, chất lượng đầy đủ. Cắt ngắn hoặc chèn watermark là vi phạm chiến lược free tier của PRD §11.
- **BR-010.3**: Preset khoá **không được ẩn** — người dùng phải thấy mình đang bỏ lỡ gì, đó là cơ chế chuyển đổi trung thực.

**Validation Rules**:
- **VR-010.1**: Mỗi preset phải có `assetPath` trỏ tới file tồn tại trong bundle; preset thiếu asset bị loại khỏi danh mục ở giai đoạn build.
- **VR-010.2**: `durationMs` của mọi preset ≤ 4000ms để không kéo dài khoảnh khắc lên xe.

**Error Handling**:
- **ERR-010.1** (từ State Variation WF-007 "Free tier"): Entitlement không đọc được → mặc định coi là Free; 3 preset Free vẫn dùng được bình thường.
- **ERR-010.2** (từ Recovery Path TF-005): Asset của một preset không nạp được → loại preset đó khỏi danh sách hiển thị thay vì hiện dòng không phát được.

**Acceptance Criteria**:
- **AC-006.2**: IF sound thuộc nhóm khoá THEN người dùng vẫn nghe thử được **toàn bộ** sound, không bị cắt ngắn và không bị chèn watermark.
- **AC-006.3**: WHEN thư viện được mở THEN có ≥ 12 preset, trong đó đúng 3 preset thuộc gói Free.

---

## FR-011: Nghe thử sound inline trong danh sách 📱

**Source UC**: UC-006
**Priority**: High · **Status**: Planned

**Description**:
Hệ thống phải phát preset ngay khi người dùng chạm một dòng trong danh sách, trong ≤ 300ms, với waveform phản ánh audio thật, và phải dừng dòng đang phát khi người dùng chạm dòng khác — không phát chồng.

**Input**:
- `presetId` của dòng được chạm
- Trạng thái phiên audio hiện tại (`AVAudioSession.isOtherAudioPlaying`)
- Mức âm lượng sound hiện tại (từ FR-015)

**Processing**:
1. Người dùng chạm dòng → chuẩn bị player cho `presetId` và bắt đầu phát trong ≤ 300ms.
2. Nếu có audio khác đang phát, áp dụng **ducking thật** (giống logic FR-016) để bản nghe thử phản ánh đúng trải nghiệm trên xe.
3. Đổi icon dòng sang waveform chạy theo **tiến độ thật** của audio (không phải animation giả).
4. Nếu người dùng chạm dòng khác trong lúc đang phát: dừng ngay dòng cũ, trả icon về trạng thái tĩnh, phát dòng mới.
5. Khi audio kết thúc, trả icon về trạng thái tĩnh và đánh dấu dòng là "vừa nghe".
6. Chạm lại dòng đang phát → dừng phát.

**Output**:
- Người dùng đã nghe ≥ 1 preset; không có hai preset phát chồng
- Trạng thái "vừa nghe" giúp người dùng biết mình đã thử những preset nào

**Business Rules**:
- **BR-011.1**: Tại một thời điểm chỉ có **tối đa một** preset đang phát.
- **BR-011.2**: Nghe thử **không** thay đổi cấu hình đã gán — nghe và gán là hai hành động tách biệt.

**Validation Rules**:
- **VR-011.1**: Waveform chỉ được hiển thị khi audio thật đang phát; hiện waveform khi không có tiếng là lỗi hiển thị.

**Error Handling**:
- **ERR-011.1** (từ AF-006.4): Chạm dòng khác khi đang phát → dừng dòng cũ ngay, không phát chồng.
- **ERR-011.2** (từ State Variation WF-007 "Error"): Phiên audio bị chiếm (đang có cuộc gọi) → dòng hiện lý do cụ thể tại chỗ, giữ icon tĩnh; danh sách vẫn duyệt được bình thường.
- **ERR-011.3** (từ AF-006.3): Người dùng đang cắm tai nghe → nêu rõ trên xe âm thanh sẽ phát qua loa xe.

**Acceptance Criteria**:
- **AC-006.1**: WHEN người dùng chạm một dòng sound THEN sound bắt đầu phát trong ≤ 300ms.
- **AC-006.5**: WHEN người dùng chạm dòng thứ hai trong lúc dòng thứ nhất đang phát THEN sound thứ nhất dừng ngay, không phát chồng.

---

## FR-012: Nghe thử sound trong sheet chuyên dụng 📱

**Source UC**: UC-006
**Priority**: High · **Status**: Planned

**Description**:
Hệ thống phải cung cấp một sheet nghe kỹ (WF-020) cho phép nghe ở mức âm lượng thật, chuyển preset trước/sau trong cùng nhóm mà không đóng sheet, và gán ngay tại khoảnh khắc nghe thấy.

**Input**:
- `presetId` được chọn từ WF-007 hoặc WF-004
- Nhóm preset hiện tại (để điều hướng trước/sau)
- Mức âm lượng sound hiện tại; sự kiện đang cấu hình (connect/disconnect/arrive)

**Processing**:
1. Mở sheet và **tự phát một lần** ngay khi sheet xuất hiện — người dùng không phải tìm nút play.
2. Hiển thị waveform lớn, tên preset, slider âm lượng, bộ chọn sự kiện.
3. Người dùng chạm mũi tên trước/sau → nạp preset kế tiếp trong cùng nhóm và tự phát; **giữ nguyên** mức âm lượng đang đặt (sub-flow SF-018).
4. Nếu hết nhóm, mũi tên bị vô hiệu — **không** cuộn vòng (cuộn vòng làm người dùng mất phương hướng).
5. Người dùng kéo slider → bàn giao FR-015 với phản hồi âm thanh tức thì.
6. Người dùng chạm "Dùng sound này" → bàn giao FR-013 hoặc FR-014 theo sự kiện đang chọn; sheet đóng; WF-030 toast.

**Output**:
- Preset được gán cho sự kiện đang chọn, hoặc sheet đóng mà không thay đổi gì
- Nếu preset khoá: chuyển WF-010

**Business Rules**:
- **BR-012.1**: Sheet tự phát **đúng một lần** khi mở; không tự phát lặp lại.
- **BR-012.2**: Điều hướng preset chỉ trong **cùng nhóm**, không vượt sang nhóm khác.

**Validation Rules**:
- **VR-012.1**: Mức âm lượng đặt trong sheet phải được giữ khi chuyển preset trong cùng phiên sheet.

**Error Handling**:
- **ERR-012.1** (từ AF-006.2): Đang phát nhạc từ app khác → áp dụng ducking thật, để bản nghe thử phản ánh đúng trải nghiệm trên xe.
- **ERR-012.2** (từ SF-018 Recovery): Preset kế tiếp không phát được → giữ preset cũ và nêu lý do; **không** để sheet ở trạng thái trống.
- **ERR-012.3** (từ State Variation WF-020 "Error"): Không phát được → nêu lý do cụ thể kèm nút thử lại; sheet **không** tự đóng để người dùng không mất ngữ cảnh.

**Acceptance Criteria**:
- **AC-006.4**: IF đang có nhạc phát từ app khác THEN lượt nghe thử áp dụng ducking giống hệt lúc chạy thật.

---

## FR-013: Gán sound cho sự kiện Connect 📱

**Source UC**: UC-007
**Priority**: High · **Status**: Planned

**Description**:
Hệ thống phải lưu preset người dùng chọn cho sự kiện lên xe, ghi vào App Group để CarPlay scene đọc được khi app ở background, và có hiệu lực từ lần kết nối kế tiếp mà không cần khởi động lại app.

**Input**:
- `presetId` được chọn, hoặc giá trị đặc biệt `none` ("Không dùng")
- Điểm khởi phát: WF-007 hoặc WF-020

**Processing**:
1. Nhận `presetId` từ FR-011/FR-012 khi người dùng chạm nút gán.
2. Nếu preset `locked` → **không gán**, chuyển WF-010 với ngữ cảnh đúng preset đó.
3. Ghi `connectSoundId` vào **App Group container** ngay tại thời điểm gán.
4. Cập nhật dòng sound trên WF-006 và dấu "đang dùng" trong danh sách.
5. Hiển thị WF-030 toast xác nhận.
6. Nếu người dùng chọn "Không dùng", ghi `none` và **không** hiển thị nhắc nhở nào về việc này.

**Output**:
- `connectSoundId` được lưu trong App Group; có hiệu lực từ lần `carplay_connected` kế tiếp
- Nếu bỏ qua bước chọn sound trong onboarding: preset Free đầu tiên được gán làm mặc định

**Business Rules**:
- **BR-013.1**: Cấu hình phải ghi vào **App Group**, không phải `UserDefaults` của app — nếu không, CarPlay scene và widget extension sẽ không đọc được.
- **BR-013.2**: "Không dùng" là lựa chọn **hợp lệ**, không phải trạng thái lỗi; hệ thống **không** nhắc nhở người dùng về nó. Nếu người dùng bỏ qua bước chọn sound trong onboarding, hệ thống gán preset Free đầu tiên thay vì để trống.
- **BR-013.3**: Đổi sound **không** yêu cầu khởi động lại app.

**Validation Rules**:
- **VR-013.1**: `presetId` phải tồn tại trong danh mục và có `tier` mà entitlement hiện tại cho phép; nếu không, thao tác gán bị từ chối.

**Error Handling**:
- **ERR-013.1** (từ AF-007.1): Preset thuộc Premium → chuyển WF-010, **không** gán.
- **ERR-013.2** (từ AF-007.2): Người dùng chọn "Không dùng" → ghi nhận, không phát sound lúc connect, không nhắc nhở.
- **ERR-013.3** (từ ERR-002.1): Ghi App Group thất bại → giữ trong bộ nhớ cho phiên hiện tại, thử lại; nêu lỗi kèm nút thử lại.

**Acceptance Criteria**:
- **AC-007.1**: WHEN người dùng gán một sound THEN lựa chọn có hiệu lực ở lần `carplay_connected` kế tiếp mà không cần khởi động lại app.
- **AC-007.2**: IF người dùng chọn "Không dùng" THEN hệ thống không phát sound nào lúc connect và **không** hiển thị nhắc nhở về việc này.
- **AC-007.3**: WHEN sound được gán THEN cấu hình được ghi vào App Group container để CarPlay scene đọc được khi app iPhone ở background.

---

## FR-014: Gán sound cho Disconnect và Arrive 📱

**Source UC**: UC-008
**Priority**: Medium · **Status**: Planned

**Description**:
Hệ thống phải cho phép gán sound độc lập cho ba sự kiện (Connect, Disconnect, Arrive), và phải vô hiệu mục Arrive kèm lý do khi thiếu quyền Vị trí — thay vì để người dùng chờ một âm thanh không bao giờ phát.

**Input**:
- Sự kiện đang cấu hình: `connect` | `disconnect` | `arrive`
- `presetId` được chọn cho sự kiện đó
- Trạng thái quyền Vị trí (từ FR-008)

**Processing**:
1. Hiển thị `SegmentedControl` ba sự kiện; đổi sự kiện **giữ nguyên vị trí cuộn** của danh sách (sub-flow SF-006).
2. Cập nhật nhãn nút gán theo sự kiện đang chọn và dấu "đang dùng" của sự kiện đó.
3. Nếu sự kiện là `arrive` và quyền Vị trí bị từ chối: hiển thị trạng thái **không khả dụng kèm lý do** và **vô hiệu** nút gán.
4. Người dùng gán → lưu độc lập cho từng sự kiện; đổi một sự kiện **không** ảnh hưởng hai sự kiện còn lại.
5. Cập nhật dòng tóm tắt cả ba sự kiện trên WF-006.
6. Khi quyền Vị trí được cấp muộn, mục Arrive tự mở khoá ở lần vào màn kế tiếp.

**Output**:
- Ba giá trị độc lập: `connectSoundId`, `disconnectSoundId`, `arriveSoundId` (mỗi giá trị có thể là `none`)
- Event `sound_played` khi phát sẽ kèm `sound_type` phân biệt ba sự kiện

**Business Rules**:
- **BR-014.1**: Để trống hai sự kiện Disconnect và Arrive là **mặc định hợp lệ**; onboarding chỉ hỏi sound Connect để giữ 5 bước.
- **BR-014.2**: Mục Arrive bị vô hiệu (không phải chỉ ẩn nhãn) khi thiếu quyền Vị trí, và lý do phải hiển thị tại chỗ.
- **BR-014.3**: Ba sự kiện lưu độc lập; không có phụ thuộc chéo.

**Validation Rules**:
- **VR-014.1**: Không cho gán sound cho `arrive` khi quyền Vị trí không ở trạng thái đã cấp.

**Error Handling**:
- **ERR-014.1** (từ AF-008.1): Người dùng chỉ muốn sound Connect → hai sự kiện còn lại để trống, hợp lệ.
- **ERR-014.2** (từ AF-008.2): Thiếu quyền Vị trí → Arrive không khả dụng kèm lý do, không cho gán.
- **ERR-014.3** (từ SF-006 Recovery): Quyền được cấp sau → Arrive tự mở khoá ở lần vào màn kế tiếp.

**Acceptance Criteria**:
- **AC-008.1**: WHEN người dùng gán sound cho ba sự kiện THEN mỗi sự kiện lưu độc lập, đổi một cái không ảnh hưởng hai cái còn lại.
- **AC-008.2**: IF quyền Vị trí bị từ chối THEN mục Arrive hiển thị rõ là không khả dụng kèm lý do, và **không** cho gán để tránh kỳ vọng sai.
- **AC-008.3**: WHEN mỗi sound phát THEN hệ thống ghi `sound_played` kèm `sound_type` phân biệt connect/disconnect/arrive.

---

## FR-015: Âm lượng sound độc lập với nhạc 📱

**Source UC**: UC-009
**Priority**: High · **Status**: Planned

**Description**:
Hệ thống phải cho người dùng đặt mức âm lượng riêng cho sound của Carbina, có phản hồi âm thanh tức thì khi kéo, lưu ngay mà không cần nút Lưu, và **không** làm thay đổi âm lượng nhạc đang phát.

**Input**:
- `soundVolume` (Float 0.0–1.0, mặc định 0.7)
- Điểm khởi phát: WF-012 (slider bền vững) · WF-020 (slider trong sheet) · nút âm lượng trên WF-007 (lối vào)

**Processing**:
1. Hiển thị slider kèm nút nghe thử; nút âm lượng trên WF-007 chỉ là **lối vào**, không phải nơi điều chỉnh.
2. Khi người dùng bắt đầu kéo, phát sound mẫu ở mức hiện tại (sub-flow SF-004).
3. Khi kéo, cập nhật âm lượng của sound mẫu theo tay trong ≤ 300ms; **không** chạm vào âm lượng của nguồn audio khác.
4. Khi nhả tay, lưu `soundVolume` ngay — không có nút Lưu.
5. Nếu giá trị = 0, hiển thị chữ "đang tắt" thay vì để trống.
6. Áp dụng `soundVolume` cho cả ba sự kiện ở lần phát kế tiếp trên xe.

**Output**:
- `soundVolume` được lưu và áp dụng cho cả ba sự kiện
- Âm lượng nhạc của app khác **không** bị thay đổi

**Business Rules**:
- **BR-015.1**: `soundVolume` áp dụng cho cả ba sự kiện; **không** có âm lượng riêng theo từng sự kiện ở MVP 1.
- **BR-015.2**: Âm lượng cuối cùng nghe được còn phụ thuộc âm lượng hệ thống của xe; hệ thống phải nêu rõ điều này để người dùng không tưởng app lỗi.
- **BR-015.3**: Slider **không** xuất hiện trong onboarding — thêm nó vào sẽ vượt giới hạn 5 bước của F6.

**Validation Rules**:
- **VR-015.1**: `soundVolume` bị kẹp trong 0.0–1.0; giá trị ngoài dải reset về mặc định 0.7.

**Error Handling**:
- **ERR-015.1** (từ AF-009.1): Đặt về 0 → nêu rõ trạng thái "đang tắt" bằng chữ, không để người dùng tưởng app lỗi.
- **ERR-015.2** (từ AF-009.2): Âm lượng hệ thống của xe rất thấp → nêu rõ âm lượng cuối phụ thuộc âm lượng xe.
- **ERR-015.3** (từ SF-004 Recovery): Không phát được sound mẫu → slider vẫn điều chỉnh và lưu được; hiện dòng nói rõ không nghe thử được lúc này.

**Acceptance Criteria**:
- **AC-009.1**: WHEN người dùng đổi âm lượng sound THEN âm lượng nhạc đang phát **không** bị thay đổi.
- **AC-009.2**: WHEN người dùng kéo slider THEN sound mẫu phát ở đúng mức mới trong ≤ 300ms.
- **AC-009.3**: IF âm lượng sound bằng 0 THEN hệ thống hiển thị rõ trạng thái "đang tắt" thay vì để trống.
- **AC-009.4**: WHEN giá trị được đổi THEN nó được lưu ngay và áp dụng ở lần phát kế tiếp trên xe.

---

## FR-016: Phát sound Connect kèm ducking 🚗

**Source UC**: UC-010
**Priority**: High · **Status**: Planned

**Description**:
Hệ thống phải phát sound Connect qua **loa xe** trong ≤ 1,5s kể từ `carplay_connected`, giảm nguồn audio đang phát xuống 20% trong lúc phát, rồi phục hồi đúng mức và đúng vị trí trước đó.

**Input**:
- Sự kiện hệ thống `carplay_connected`
- `connectSoundId` và `soundVolume` từ App Group
- Trạng thái audio hiện tại: có nguồn nào đang phát, loại nguồn (nhạc / podcast / cuộc gọi / chỉ dẫn dẫn đường)
- Tuyến đầu ra hiện tại (`AVAudioSession.currentRoute`)

**Processing**:
1. Nhận `carplay_connected`; đọc `connectSoundId`; nếu là `none` thì kết thúc, không làm gì.
2. Bàn giao FR-017 để quyết định có được phát hay phải nhường/bỏ lượt.
3. Bàn giao FR-018 để kiểm chống phát trùng.
4. Nếu được phát: cấu hình `AVAudioSession` với `.duckOthers`, giảm nguồn đang phát xuống **20%**.
5. Phát sound qua tuyến đầu ra là **loa xe**, ở mức `soundVolume`, bắt đầu trong ≤ 1,5s kể từ sự kiện.
6. Khi sound kết thúc, huỷ ducking và **phục hồi nguồn cũ về đúng mức và đúng vị trí** trước đó.
7. Ghi `sound_played` kèm `sound_type = connect`, `music_was_playing`, `output_route`; ghi `sound_ducking_applied` nếu đã áp dụng ducking.

**Output**:
- Sound đã phát qua loa xe; nguồn audio cũ trở lại nguyên trạng
- Hai event telemetry đã ghi, đủ để xác minh cả ba complaint của đối thủ đã được giải quyết

**Business Rules**:
- **BR-016.1**: Mức ducking là **20%** của âm lượng nguồn cũ, không phải im lặng hoàn toàn — người dùng vẫn nhận biết nhạc đang tiếp tục.
- **BR-016.2**: Sau khi phát, nguồn cũ phải trở lại **đúng mức và đúng vị trí**; phục hồi sai mức là lỗi chức năng.
- **BR-016.3**: Tuyến đầu ra phải là loa xe; phát qua loa iPhone khi đang trong phiên CarPlay là lỗi chức năng (xem FR-020).

**Validation Rules**:
- **VR-016.1**: `connectSoundId` phải tồn tại trong danh mục; nếu asset thiếu thì bỏ lượt phát và ghi lý do, không phát preset khác thay thế.

**Error Handling**:
- **ERR-016.1** (từ AF-010.1): Đang có cuộc gọi → bàn giao FR-017, bỏ lượt phát.
- **ERR-016.2** (từ AF-010.2): Đang có chỉ dẫn dẫn đường bằng giọng nói → bàn giao FR-017, nhường rồi phát sau, chờ tối đa 3s.
- **ERR-016.3** (từ AF-010.3): Tuyến đầu ra không phải loa xe → vẫn phát nhưng ghi `output_route` để phát hiện sai định tuyến.
- **ERR-016.4** (từ AF-010.4): Connect/disconnect liên tiếp trong 3s → bàn giao FR-018, chỉ phát 1 lần.

**Acceptance Criteria**:
- **AC-010.1**: WHEN `carplay_connected` xảy ra THEN sound Connect bắt đầu phát trong ≤ 1,5s.
- **AC-010.2**: IF có audio đang phát THEN hệ thống giảm nguồn đó xuống 20% trong lúc phát sound và phục hồi đúng mức cũ sau khi phát xong.
- **AC-010.3**: WHEN sound phát trên xe THEN tuyến đầu ra là **loa xe**, không phải loa iPhone.
- **AC-010.5**: WHEN sound phát xong THEN hệ thống ghi `sound_played` kèm `sound_type`, `music_was_playing`, `output_route`, và ghi `sound_ducking_applied` nếu đã áp dụng ducking.

---

## FR-017: Chính sách nhường phiên audio 🚗

**Source UC**: UC-010 (AF-010.1, AF-010.2)
**Priority**: High · **Status**: Planned

**Description**:
Hệ thống phải quyết định đúng khi nào **không** được phát: bỏ hẳn lượt phát khi đang có cuộc gọi, nhường chỗ cho chỉ dẫn dẫn đường rồi phát sau trong cửa sổ 3 giây, và **không bao giờ phát bù** một lượt đã bỏ.

**Input**:
- Loại nguồn audio đang chiếm phiên: `voiceCall` | `navigationPrompt` | `music` | `podcast` | `none`
- Thời điểm sự kiện gốc (`carplay_connected` hoặc tín hiệu ngắt kết nối)

**Processing**:
1. Phân loại nguồn đang chiếm phiên audio.
2. Nếu là `voiceCall`: **bỏ hẳn** lượt phát; ghi lý do; **không** đặt hàng chờ phát bù.
3. Nếu là `navigationPrompt`: chờ chỉ dẫn kết thúc, tối đa **3 giây**; nếu trong 3s chỉ dẫn xong thì phát, nếu không thì bỏ lượt.
4. Nếu là `music` hoặc `podcast`: cho phép phát kèm ducking (bàn giao FR-016).
5. Nếu là `none`: phát trực tiếp ở `soundVolume`.
6. Mọi quyết định bỏ lượt phải hoàn tất trong ≤ 100ms để không treo chờ.

**Output**:
- Quyết định nhị phân: phát (kèm hoặc không kèm ducking) / bỏ lượt kèm lý do ghi nhận
- Không có lượt phát bù nào được xếp hàng

**Business Rules**:
- **BR-017.1**: Cuộc gọi có ưu tiên **tuyệt đối**; sound của Carbina không bao giờ chèn vào cuộc gọi.
- **BR-017.2**: Lượt phát đã bỏ **không bao giờ được phát bù**. Phát một câu chào giữa chuyến đi còn tệ hơn không phát.
- **BR-017.3**: Cửa sổ chờ chỉ dẫn dẫn đường là **3 giây**, không nhiều hơn — sau 3s thì khoảnh khắc lên xe đã qua.

**Validation Rules**:
- **VR-017.1**: Quyết định nhường/bỏ phải hoàn tất trong ≤ 100ms; vượt ngưỡng này là lỗi hiệu năng (xem AC-NFR-003.3).

**Error Handling**:
- **ERR-017.1** (từ AF-010.1): Cuộc gọi → bỏ lượt, không phát bù.
- **ERR-017.2** (từ AF-010.2): Chỉ dẫn dẫn đường → nhường, chờ ≤ 3s, rồi phát hoặc bỏ.
- **ERR-017.3** (từ AF-021.2): Cùng chính sách áp dụng cho giọng chào (FR-037) — hai đường dùng chung logic này để hành vi nhất quán.

**Acceptance Criteria**:
- **AC-010.4**: IF đang có cuộc gọi THEN hệ thống bỏ lượt phát và không phát bù.
- **AC-NFR-003.3**: WHEN phiên audio không khả dụng THEN lượt phát bị bỏ **trong ≤ 100ms** thay vì treo chờ.

---

## FR-018: Chống phát trùng khi kết nối chập chờn 🚗

**Source UC**: UC-010 (AF-010.4)
**Priority**: High · **Status**: Planned

**Description**:
Hệ thống phải phát tối đa một lần cho mỗi khoảnh khắc lên xe, kể cả khi tín hiệu kết nối CarPlay chập chờn hoặc người dùng cắm lại dây trong vài giây.

**Input**:
- Chuỗi sự kiện `carplay_connected` / ngắt kết nối kèm dấu thời gian
- Dấu thời gian lượt phát gần nhất cho từng `sound_type`

**Processing**:
1. Khi nhận `carplay_connected`, so dấu thời gian với lượt phát Connect gần nhất.
2. Nếu khoảng cách < **3 giây**, bỏ lượt phát mới (coi là cùng một khoảnh khắc lên xe).
3. Nếu ≥ 3 giây, cho phép phát và cập nhật dấu thời gian.
4. Áp dụng cùng cửa sổ cho từng cặp connect/disconnect độc lập; **không** tích lũy nợ phát.
5. Ghi nhận số lượt bị bỏ do chống trùng vào telemetry để phân biệt với lỗi thật.

**Output**:
- Tối đa 1 lượt phát Connect cho mỗi khoảng 3 giây
- Số lượt bị bỏ do chống trùng được ghi nhận riêng, không bị đếm thành lỗi

**Business Rules**:
- **BR-018.1**: Cửa sổ chống trùng là **3 giây** cho mỗi `sound_type`.
- **BR-018.2**: Không có hàng chờ phát bù; lượt bị bỏ do chống trùng biến mất hoàn toàn.

**Validation Rules**:
- **VR-018.1**: Dấu thời gian phải dùng đồng hồ đơn điệu của hệ thống, không dùng giờ tường (để không bị ảnh hưởng khi người dùng đổi múi giờ).

**Error Handling**:
- **ERR-018.1** (từ AF-010.4): Cắm lại dây trong 3s → chỉ phát 1 lần.
- **ERR-018.2** (từ State Variation FR-018 "Error"): Kết nối chập chờn nhiều lần liên tiếp → mỗi cặp connect/disconnect được xét độc lập, không tích lũy nợ phát.

**Acceptance Criteria**:
- **AC-010.6**: IF connect rồi disconnect trong vòng 3s THEN chỉ phát tối đa 1 lần.

---

## FR-019: Phát sound Disconnect đúng thời điểm tắt máy 🚗

**Source UC**: UC-011
**Priority**: High · **Status**: Planned

**Description**:
Hệ thống phải phát sound Disconnect qua loa xe trong cửa sổ ≤ 1 giây kể từ tín hiệu ngắt kết nối CarPlay, và phải bỏ lượt nếu sound Arrive vừa phát trong 10 giây trước đó.

**Input**:
- Tín hiệu ngắt kết nối CarPlay (tắt máy hoặc rút dây)
- `disconnectSoundId` và `soundVolume` từ App Group
- Dấu thời gian lượt phát Arrive gần nhất

**Processing**:
1. Nhận tín hiệu ngắt kết nối; đọc `disconnectSoundId`; nếu `none` thì kết thúc.
2. Kiểm dấu thời gian Arrive: nếu Arrive đã phát trong **10 giây** trước đó, **bỏ** lượt Disconnect để không phát 2 tiếng liền nhau.
3. Bàn giao FR-017 để kiểm điều kiện phiên audio.
4. Phát sound qua **loa xe** trước khi phiên audio bị hệ thống thu hồi; lệch **≤ 1 giây** so với tín hiệu.
5. Ghi `sound_played` kèm `sound_type = disconnect` và `output_route`.

**Output**:
- Sound Disconnect đã phát qua loa xe, hoặc bị bỏ có ghi nhận lý do
- Phiên CarPlay kết thúc

**Business Rules**:
- **BR-019.1**: Cửa sổ lệch cho phép là **≤ 1 giây**; lệch nhiều hơn làm mất cảm giác "sound là phần của việc xuống xe".
- **BR-019.2**: Arrive và Disconnect **loại trừ nhau** trong cửa sổ 10 giây; Arrive thắng vì nó xảy ra trước.
- **BR-019.3**: Rút dây mà không tắt máy được coi là disconnect bình thường — cùng hành vi.

**Validation Rules**:
- **VR-019.1**: Chỉ phát khi phiên audio còn khả dụng; kiểm trước khi phát, không phát rồi mới kiểm.

**Error Handling**:
- **ERR-019.1** (từ AF-011.1): Phiên audio bị thu hồi trước khi kịp phát → bàn giao FR-020 (bỏ lượt, không phát bù qua loa iPhone).
- **ERR-019.2** (từ AF-011.2): Rút dây thay vì tắt máy → coi là disconnect bình thường.
- **ERR-019.3** (từ AF-011.3): Arrive vừa phát trong 10s → bỏ sound Disconnect.

**Acceptance Criteria**:
- **AC-011.1**: WHEN người dùng tắt máy THEN sound Disconnect phát qua **loa xe**, không qua loa iPhone.
- **AC-011.3**: WHEN sound Arrive đã phát trong 10s trước đó THEN hệ thống bỏ sound Disconnect.
- **AC-011.4**: WHEN sound Disconnect phát THEN thời điểm phát lệch không quá 1s so với tín hiệu ngắt kết nối.

---

## FR-020: Định tuyến đầu ra loa xe và chính sách không phát bù 🚗

**Source UC**: UC-011 (AF-011.1)
**Priority**: High · **Status**: Planned

**Description**:
Hệ thống phải luôn ưu tiên loa xe làm tuyến đầu ra trong phiên CarPlay, và khi không phát được thì phải **im lặng** — tuyệt đối không chuyển sang loa iPhone. Đây là phản ứng trực tiếp với complaint *"you only hear the sound through your phone"* của đối thủ.

**Input**:
- `AVAudioSession.currentRoute` và danh sách output port
- Trạng thái khả dụng của phiên audio tại thời điểm phát

**Processing**:
1. Trước khi phát bất kỳ sound nào trong phiên CarPlay, kiểm tuyến đầu ra hiện tại.
2. Nếu tuyến là loa xe (`carAudio`), phát bình thường.
3. Nếu tuyến **không** phải loa xe, vẫn phát nhưng ghi `output_route` với giá trị thật để phát hiện sai định tuyến ở tầng telemetry.
4. Nếu phiên audio đã bị thu hồi (không phát được gì): **bỏ lượt phát**, ghi `sound_played` với trạng thái thất bại kèm lý do.
5. **Cấm tuyệt đối** việc chuyển tuyến sang loa iPhone như một đường lui.
6. Ghi nhận tỉ lệ `output_route != carAudio` theo tuần để phát hiện lớp thiết bị có vấn đề định tuyến.

**Output**:
- Sound phát qua loa xe, hoặc không phát gì cả kèm lý do ghi nhận
- Số liệu `output_route` đủ để phát hiện sai định tuyến trong vòng một tuần

**Business Rules**:
- **BR-020.1**: **Cấm** phát bù qua loa iPhone trong mọi hoàn cảnh. Im lặng là hành vi đúng; chuyển tuyến là hành vi sai.
- **BR-020.2**: Mọi lượt phát trong phiên CarPlay đều phải ghi `output_route` với giá trị thật, không phải giá trị mong đợi.

**Validation Rules**:
- **VR-020.1**: `output_route` được ghi từ `AVAudioSession.currentRoute` tại thời điểm phát, không phải từ cấu hình dự kiến.

**Error Handling**:
- **ERR-020.1** (từ AF-011.1): Phiên audio bị thu hồi trước khi phát được → bỏ lượt, ghi trạng thái thất bại kèm lý do, **không** phát bù qua loa iPhone.
- **ERR-020.2** (từ State Variation FR-020 "Power User"): Người dùng đang cắm tai nghe → ghi `output_route` để phát hiện; hành vi vẫn ưu tiên loa xe.

**Acceptance Criteria**:
- **AC-011.2**: IF phiên audio bị thu hồi trước khi phát được THEN hệ thống bỏ lượt phát và ghi `sound_played` với trạng thái thất bại kèm lý do — **không** phát bù qua loa iPhone.

---

## Tổng hợp nhóm

| FR | Priority | UC nguồn | Số BR | Số VR | Số ERR | AC mang từ UC |
|---|---|---|---|---|---|---|
| FR-010 | High | UC-006 | 3 | 2 | 2 | AC-006.2, AC-006.3 |
| FR-011 | High | UC-006 | 2 | 1 | 3 | AC-006.1, AC-006.5 |
| FR-012 | High | UC-006 | 2 | 1 | 3 | AC-006.4 |
| FR-013 | High | UC-007 | 3 | 1 | 3 | AC-007.1, AC-007.2, AC-007.3 |
| FR-014 | Medium | UC-008 | 3 | 1 | 3 | AC-008.1, AC-008.2, AC-008.3 |
| FR-015 | High | UC-009 | 3 | 1 | 3 | AC-009.1 → AC-009.4 |
| FR-016 | High | UC-010 | 3 | 1 | 4 | AC-010.1, AC-010.2, AC-010.3, AC-010.5 |
| FR-017 | High | UC-010 | 3 | 1 | 3 | AC-010.4, AC-NFR-003.3 |
| FR-018 | High | UC-010 | 2 | 1 | 2 | AC-010.6 |
| FR-019 | High | UC-011 | 3 | 1 | 3 | AC-011.1, AC-011.3, AC-011.4 |
| FR-020 | High | UC-011 | 2 | 1 | 2 | AC-011.2 |

**Tổng nhóm**: 11 FR (10 High, 1 Medium) · 29 BR · 12 VR · 31 ERR · **25 AC** — phủ đủ toàn bộ 25 AC của UC-006 → UC-011, không thiếu, không viết lại.
