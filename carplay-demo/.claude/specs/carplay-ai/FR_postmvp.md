# FR — Post-MVP

**Sub-spec của**: [`Functional_Requirements.md`](./Functional_Requirements.md) · **Version** 2.4 · **Snapshot** 2026-08-07
**Phạm vi**: FR-063 → FR-065 · **UC nguồn**: UC-034, UC-035 · **PRD Feature**: F13, Cloud sync
**Màn hình liên quan**: WF-012, WF-015, WF-016

> **Ba FR trong file này KHÔNG thuộc phạm vi thi công MVP 1.** Chúng được đặc tả ở đây để cây màn hình và lược đồ dữ liệu không phải đập đi làm lại — cụ thể: lược đồ SQLite chừa sẵn bảng chuyến đi từ MVP 1, và dòng "Tài khoản" trên WF-012 chỉ **xuất hiện** ở MVP 3 nhưng vị trí của nó đã được giữ. Status của cả ba là `Deferred`.

---

## FR-063: Contacts favorites và gọi một chạm 🚗 *(MVP 2 — tháng 12/2026)*

**Source UC**: UC-034
**Priority**: Medium · **Status**: Deferred (MVP 2)

**Description**:
Hệ thống phải cho người dùng chọn tối đa 5 liên hệ favorite trên iPhone và gọi họ bằng **một chạm** từ dashboard CarPlay, qua hệ thống điện thoại của iOS.

**Input**:
- Danh bạ của người dùng (Contacts framework, cần quyền)
- Tối đa 5 `favoriteContactIds` kèm số điện thoại mặc định đã chọn sẵn
- Trạng thái quyền Contacts

**Processing**:
1. Trên iPhone (màn hình mới sẽ thêm ở MVP 2), người dùng chọn tối đa 5 favorite và chọn **số mặc định** cho liên hệ có nhiều số.
2. Ghi `favoriteContactIds` vào App Group.
3. Trên WF-016, hiển thị thẻ shortcut liên hệ trong tập thẻ khả dụng (bàn giao FR-041 để lọc theo entitlement).
4. Người dùng chạm một liên hệ → bắt đầu cuộc gọi qua hệ thống trong ≤ 1s; app **không** xử lý cuộc gọi.
5. Nếu quyền Contacts bị từ chối: **không** hiển thị thẻ liên hệ; **cấm** hiện thẻ rỗng.
6. Trên xe, **không** hỏi lại số nào cần gọi — dùng số mặc định đã chọn trên iPhone.

**Output**:
- Cuộc gọi được thực hiện qua hệ thống điện thoại của iOS
- Người dùng không phải rời mắt khỏi đường để tìm số

**Business Rules**:
- **BR-063.1**: Tối đa **5** favorite; nhiều hơn sẽ làm dashboard vượt giới hạn mật độ Medium của bề mặt CarPlay.
- **BR-063.2**: **Cấm** hỏi chọn số điện thoại trên màn hình xe — mọi quyết định phải làm xong trên iPhone.
- **BR-063.3**: **Cấm** hiện thẻ liên hệ rỗng khi thiếu quyền hoặc chưa cấu hình favorite; thay bằng lời mời cấu hình trên iPhone.
- **BR-063.4**: App **không** xử lý cuộc gọi; chỉ khởi phát qua hệ thống.

**Validation Rules**:
- **VR-063.1**: Số favorite ≤ 5 tại mọi thời điểm.
- **VR-063.2**: Mỗi favorite phải có một số điện thoại mặc định đã xác định trước khi thẻ xuất hiện trên WF-016.

**Error Handling**:
- **ERR-063.1** (từ AF-034.1): Quyền Contacts bị từ chối → thẻ không xuất hiện; không hiện thẻ rỗng.
- **ERR-063.2** (từ AF-034.2): Liên hệ có nhiều số → dùng số mặc định, không hỏi lại trên xe.
- **ERR-063.3** (từ State Variation UC-034 "First-time"): Chưa chọn favorite nào → thẻ hiện lời mời cấu hình trên iPhone, không hiện danh sách rỗng.

**Acceptance Criteria**:
- **AC-034.1**: WHEN người dùng chạm một thẻ liên hệ THEN cuộc gọi bắt đầu qua hệ thống trong ≤ 1s.
- **AC-034.2**: WHEN thẻ liên hệ hiển thị THEN có tối đa 5 favorite và mọi touch target ≥ 44pt.
- **AC-034.3**: IF quyền Contacts bị từ chối THEN thẻ liên hệ **không** xuất hiện trên WF-016.
- **AC-034.4**: IF liên hệ có nhiều số THEN hệ thống dùng số mặc định và **không** hỏi lại trên màn hình xe.

---

## FR-064: Đăng nhập và đồng bộ cấu hình opt-in 📱 *(MVP 3 — tháng 3/2027)*

**Source UC**: UC-035
**Priority**: Low · **Status**: Deferred (MVP 3)

**Description**:
Hệ thống phải cho người dùng **tuỳ chọn** đăng nhập email và bật đồng bộ cấu hình giữa các thiết bị, trong khi **dữ liệu học ngữ cảnh vẫn không rời thiết bị**. App phải hoạt động đầy đủ khi người dùng không bao giờ tạo tài khoản.

**Input**:
- Email và phương thức xác thực (Firebase Authentication)
- Cấu hình đồng bộ được: widget, sound, ngôn ngữ, theme
- Cấu hình **không** đồng bộ: dữ liệu học ngữ cảnh, lịch sử chẩn đoán

**Processing**:
1. Dòng "Tài khoản" trên WF-012 **chỉ xuất hiện từ MVP 3**; ở MVP 1 và MVP 2 nó không hiện.
2. Người dùng mở WF-015 → đăng nhập email (tuỳ chọn).
3. Bật "Đồng bộ cấu hình" → đẩy cấu hình widget/sound/ngôn ngữ/theme lên Firestore.
4. Hiển thị bảng hai cột ở Zone C: **cái gì được đồng bộ** và **cái gì không** — nêu rõ dữ liệu học ngữ cảnh không rời thiết bị.
5. Trên thiết bị thứ hai, đăng nhập cùng email → tải cấu hình về.
6. Người dùng đăng xuất → cấu hình cục bộ **giữ nguyên**; chỉ ngắt đồng bộ.
7. Nếu có xung đột cấu hình giữa hai thiết bị: **hỏi người dùng chọn bản nào**; cấm tự ghi đè.

**Output**:
- Cấu hình có mặt trên các thiết bị đã đăng nhập
- Dữ liệu học ngữ cảnh **vẫn ở lại trên từng thiết bị**

**Business Rules**:
- **BR-064.1**: Tài khoản là **tuỳ chọn tuyệt đối**; bắt tạo tài khoản làm giảm conversion (PRD §14) và app phải chạy đủ mà không cần nó.
- **BR-064.2**: **Chỉ cấu hình** được đồng bộ; dữ liệu học ngữ cảnh **không rời thiết bị** — giữ nguyên cam kết của NFR-012 sang MVP 3.
- **BR-064.3**: **Cấm** tự ghi đè khi xung đột; luôn hỏi người dùng.
- **BR-064.4**: Đăng xuất **không** xoá cấu hình cục bộ.

**Validation Rules**:
- **VR-064.1**: Payload đồng bộ chỉ chứa các trường trong whitelist cấu hình; trường ngoài whitelist bị chặn ở client.

**Error Handling**:
- **ERR-064.1** (từ AF-035.1): Người dùng không muốn tài khoản → app hoạt động đầy đủ như MVP 1.
- **ERR-064.2** (từ AF-035.2): Xung đột cấu hình → hỏi giữ bản nào, không tự ghi đè.
- **ERR-064.3** (từ State Variation WF-015 "Error"): Không kết nối được cloud → dùng cấu hình cục bộ; mọi tính năng vẫn hoạt động vì cloud chỉ là lớp tiện ích.

**Acceptance Criteria**:
- **AC-035.1**: WHEN người dùng không bật đồng bộ THEN app hoạt động đầy đủ và **không** yêu cầu tài khoản.
- **AC-035.2**: WHEN đồng bộ được bật THEN chỉ cấu hình được đẩy lên cloud; **dữ liệu học ngữ cảnh không rời thiết bị**.
- **AC-035.3**: IF có xung đột cấu hình THEN hệ thống hỏi người dùng chọn bản nào, không tự ghi đè.

---

## FR-065: Xoá tài khoản và dữ liệu cloud 📱 *(MVP 3 — tháng 3/2027)*

**Source UC**: UC-035 (AF-035.3)
**Priority**: Low · **Status**: Deferred (MVP 3)

**Description**:
Hệ thống phải cho người dùng xoá tài khoản và **toàn bộ dữ liệu cloud** của họ, trong khi dữ liệu on-device vẫn còn để app tiếp tục dùng được.

**Input**:
- Tài khoản đang đăng nhập
- Danh mục dữ liệu cloud: cấu hình widget/sound/ngôn ngữ/theme

**Processing**:
1. Dòng "Xoá tài khoản" ở WF-015 Zone D, tách khỏi nút đăng xuất.
2. Yêu cầu xác nhận nêu rõ: dữ liệu cloud sẽ bị xoá, **dữ liệu on-device vẫn còn**, và app vẫn dùng được sau đó.
3. Xác nhận → xoá bản ghi Firestore và tài khoản Firebase Auth.
4. Ngắt đồng bộ; giữ nguyên cấu hình cục bộ.
5. Xác nhận hoàn tất cho người dùng; nếu xoá thất bại một phần, nêu rõ phần nào chưa xoá được kèm nút thử lại.

**Output**:
- Dữ liệu cloud bị xoá hoàn toàn; app tiếp tục hoạt động với dữ liệu on-device
- Người dùng có xác nhận rõ ràng về những gì đã và chưa bị xoá

**Business Rules**:
- **BR-065.1**: Xoá tài khoản **không** làm mất dữ liệu on-device; app phải dùng được ngay sau đó.
- **BR-065.2**: Xoá tài khoản phải xoá **toàn bộ** dữ liệu cloud, không để lại bản ghi mồ côi (yêu cầu GDPR/CCPA của PRD §9).
- **BR-065.3**: Dòng xoá tài khoản tách khỏi đăng xuất, và cần xác nhận rõ ràng.

**Validation Rules**:
- **VR-065.1**: Sau khi xoá, truy vấn lại phải trả về không có bản ghi nào thuộc tài khoản đó; còn bản ghi là xoá thất bại.

**Error Handling**:
- **ERR-065.1** (từ AF-035.3): Người dùng xoá tài khoản → dữ liệu cloud bị xoá; dữ liệu on-device vẫn còn.
- **ERR-065.2** (từ ERR-057.2): Xoá thất bại một phần → nêu rõ phần nào chưa xoá được kèm nút thử lại; **không** báo "đã xoá xong" khi chưa xong.

**Acceptance Criteria**:
- **AC-035.4**: WHEN người dùng xoá tài khoản THEN toàn bộ dữ liệu cloud bị xoá.

---

## Tổng hợp nhóm

| FR | Priority | Status | UC nguồn | Số BR | Số VR | Số ERR | AC mang từ UC |
|---|---|---|---|---|---|---|---|
| FR-063 | Medium | Deferred (MVP 2) | UC-034 | 4 | 2 | 3 | AC-034.1 → AC-034.4 |
| FR-064 | Low | Deferred (MVP 3) | UC-035 | 4 | 1 | 3 | AC-035.1, AC-035.2, AC-035.3 |
| FR-065 | Low | Deferred (MVP 3) | UC-035 (AF-035.3) | 3 | 1 | 2 | AC-035.4 |

**Tổng nhóm**: 3 FR (1 Medium, 2 Low — **toàn bộ `Deferred`**) · 11 BR · 4 VR · 8 ERR · **8 AC** — phủ đủ toàn bộ 8 AC của UC-034 và UC-035.

**Hai ảnh hưởng của nhóm này tới thiết kế MVP 1** (đây là lý do nhóm được đặc tả sớm thay vì để trống):
1. **Lược đồ SQLite ở MVP 1 phải chừa sẵn bảng chuyến đi** cho trip history của MVP 3, để không phải migrate dữ liệu về sau (`Project_Overview.md` §2.1 persona Sam).
2. **Vị trí dòng "Tài khoản" trên WF-012 Zone D được giữ sẵn** nhưng **không hiển thị** ở MVP 1 và MVP 2 — để khi bật lên ở MVP 3, thứ tự các dòng cài đặt không bị xáo trộn với người dùng đã quen.
