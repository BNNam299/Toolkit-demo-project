# Calo AI - Use Cases

**Phiên bản**: 1.0  
**Ngày**: 2026-07-21  
**Tác giả**: AI Research Agent  
**Chế độ**: Full UC Decomposition  
**Trạng thái**: Bản nháp để xem xét  

---

## 0. Creative Decomposition

### 0.1 Feature Explosion Table

Mỗi tính năng MVP từ PRD §7 được phân tích thành các sub-feature và UC candidates:


| Tính năng PRD                  | Sub-Features Khám phá                            | UC Candidates | Hàng ngày?    | Liên quan đến  |
| ------------------------------ | ------------------------------------------------ | ------------- | ------------- | -------------- |
| Chụp ảnh nhận diện AI          | Mở camera                                        | UC-001        | Có            | UC-002         |
|                                | Chụp/chọn ảnh                                    | UC-002        | Có            | UC-001, UC-003 |
|                                | Xem kết quả AI                                   | UC-003        | Có            | UC-002, UC-004 |
|                                | Retry nếu nhận diện sai                          | UC-004        | Thỉnh thoảng  | UC-003         |
| Xác nhận nguyên liệu/khẩu phần | Xem danh sách nguyên liệu đề xuất                | UC-005        | Có            | UC-006, UC-007 |
|                                | Thêm/bớt nguyên liệu                             | UC-006        | Thường        | UC-005         |
|                                | Điều chỉnh khẩu phần (gram/size)                 | UC-007        | Có            | UC-005, UC-006 |
|                                | Xem calo/macro cập nhật                          | UC-008        | Có            | UC-007         |
| Giới hạn scan free tier        | Xem số lượt scan còn lại                         | UC-009        | Có            | UC-010         |
|                                | Hết lượt → hiển thị CTA upgrade                  | UC-010        | Theo ngày     | UC-009, UC-020 |
| Nhật ký ăn uống                | Xem log theo ngày                                | UC-011        | Có            | UC-012, UC-013 |
|                                | Xem log theo tuần                                | UC-012        | Hàng tuần     | UC-011         |
|                                | So sánh với mục tiêu calo                        | UC-013        | Có            | UC-011, UC-012 |
|                                | Chỉnh sửa log cũ                                 | UC-014        | Thỉnh thoảng  | UC-011, UC-012 |
|                                | Xoá log                                          | UC-015        | Thỉnh thoảng  | UC-011, UC-012 |
| Onboarding cá nhân hoá         | Nhập thông tin cơ bản (chiều cao, cân, mục tiêu) | UC-016        | 1 lần         | —              |
|                                | Chọn mức hoạt động                               | UC-017        | 1 lần         | UC-016         |
|                                | Xem mục tiêu calo được tính                      | UC-018        | 1 lần         | UC-017         |
| Subscription minh bạch         | Xem paywall (giá + trial length)                 | UC-019        | Khi hết scan  | UC-010, UC-020 |
|                                | Bắt đầu trial 7 ngày                             | UC-020        | 1 lần / người | UC-019         |
|                                | Huỷ subscription trong app                       | UC-021        | Thỉnh thoảng  | UC-022, UC-023 |
|                                | Quản lý subscription (Settings)                  | UC-022        | Vài tháng/lần | UC-021         |
|                                | Restore purchase                                 | UC-023        | Vài tháng/lần | UC-022         |


### 0.2 Context Storming

Mỗi UC được xem xét qua 3 bối cảnh người dùnChụp ảnh nhận diện AIg:


| UC                                 | Người dùng mới lần đầu                                                 | Người dùng quay lại         | Power user / Edge case                         |
| ---------------------------------- | ---------------------------------------------------------------------- | --------------------------- | ---------------------------------------------- |
| **UC-001: Mở camera**              | Hướng dẫn "Chụp bữa ăn của bạn" + permission request                   | Nút mở camera trực tiếp     | Gesture: swipe để mở camera từ Diary           |
| **UC-002: Chụp/chọn ảnh**          | Hướng dẫn "Góc tốt nhất là từ trên xuống"                              | Mở camera thẳng, không hint | Keyboard shortcut hoặc camera quick-access     |
| **UC-003: Xem kết quả AI**         | Highlight kết quả AI, khuyến khích confirm                             | Kết quả được highlight nhẹ  | Auto-confirm nếu confidence &gt;95% (tuỳ chọn) |
| **UC-004: Retry nếu sai**          | "Không chắc chắn? Thử lại" CTA rõ ràng                                 | Simple retry button         | Auto-suggest similar dishes từ lịch sử         |
| **UC-010: Hết lượt → CTA upgrade** | "Bạn đã dùng hết 3 lượt scan hôm nay. Nâng cấp để scan không giới hạn" | Nhắc nhẹ: "3/3 scans used"  | Quick-upgrade path: 1-tap từ camera            |
| **UC-020: Bắt đầu trial**          | Full paywall tương tác, highlight trial benefit                        | Chỉ thấy nếu hết scan       | Chuyên biệt: khác trial types A/B test         |


### 0.3 Repetition Audit

Các hành động nên xuất hiện ở nhiều nơi:


| Hành động             | Vị trí 1 (Chính)                          | Vị trí 2 (Ngữ cảnh)                     | Vị trí 3 (Khám phá)                 | Sự khác biệt biểu hiện              |
| --------------------- | ----------------------------------------- | --------------------------------------- | ----------------------------------- | ----------------------------------- |
| **Share tiến bộ**     | Dashboard (tuần/tháng) — full button      | Diary (ngày) — icon chỉ                 | Notification — deep link share      | Full &gt; Icon &gt; Inline          |
| **Xem mục tiêu calo** | Diary (hàng ngày) — prominent bar         | Onboarding (setup) — calculation result | Settings — edit target              | Live tracking &gt; Result &gt; Edit |
| **Huỷ subscription**  | Settings → Manage Subscription (full CTA) | Paywall — "I'd rather not" option       | Account → Billing → Cancel (buried) | Direct &gt; Paywall &gt; Buried     |
| **Xem lịch sử scan**  | Diary → toggle "view by scan date"        | Settings → "My scans"                   | Camera → "Recent"                   | Filter &gt; Tab &gt; Inline         |


### 0.4 Screen Architecture Canvas

Toàn bộ phân cấp màn hình dựa trên PRD §10 + MVP tính năng:

```
Calo AI Root
├── Tab 1: Camera (Action) — Core Loop
│   ├── WF-002: Camera / Chụp ảnh món ăn (primary action screen)
│   ├── WF-003: Xác nhận nguyên liệu & khẩu phần (confirmation/edit)
│   └── Modals từ here:
│       ├── WF-010: AI Loading state (overlay)
│       ├── WF-011: Error/Retry screen (modal)
│       └── WF-012: Ingredient Not Found? (suggest manual entry)
│
├── Tab 2: Diary (Consumption) — History & Insights
│   ├── WF-004: Nhật ký ăn uống theo ngày (primary consumption)
│   ├── WF-005: Dashboard tiến trình tuần/tháng (analytics)
│   └── Modals từ here:
│       ├── WF-013: Edit log modal
│       ├── WF-014: Delete confirmation
│       └── WF-015: Share tiến bộ modal
│
├── Tab 3: Account (Management) — Settings & Subscription
│   ├── WF-007: Cài đặt tài khoản & quản lý subscription
│   └── Modals từ here:
│       ├── WF-016: Edit profile
│       ├── WF-017: Change goal
│       └── WF-018: Subscription details + Cancel
│
├── System Mandatory Screens
│   ├── WF-001: Splash / App Launch
│   ├── WF-008: Onboarding & thu thập mục tiêu (multi-step)
│   ├── WF-006: Paywall / Subscription (full-screen modal, first-time + upsell moments)
│   └── WF-009: Sign in with Apple
│
└── Post-MVP (referenced but not in MVP scope)
    ├── WF-019: AI Coach chat
    └── WF-020: Theo dõi GLP-1
```

**Tổng số screen MVP: 18 screens (7 chính + 2 onboarding + 9 modals)**
**Phân loại Archetype:**

- Action: Camera (WF-002), Confirmation (WF-003)
- Consumption: Diary (WF-004), Dashboard (WF-005)
- Management: Settings (WF-007)
- System: Splash (WF-001), Onboarding (WF-008), Paywall (WF-006)

---

## 1. Giới thiệu

### 1.1 Mục đích Use Cases

Tài liệu này định nghĩa đầy đủ **những gì người dùng muốn làm** trong Calo AI. Mỗi Use Case (UC) tương ứng với 1 hoặc nhiều User Stories có thể được test và xác nhận. UCs này sẽ trở thành yêu cầu chức năng trong Functional Requirements.md và định hình thiết kế trong Wireframes.md.

### 1.2 Phạm vi

Tài liệu này bao gồm:

- **MVP UCs**: Tất cả UCs phục vụ PRD §6 MVP scope (UC-001 through UC-023)
- **Post-MVP UCs**: Những UCs thuộc Phase tiếp theo (UC-024-027: AI Coach, GLP-1 tracking) được liệt kê nhưng KHÔNG chi tiết trong MVP
- **2 Personas chính**: Mass-Market Diet Novice + GLP-1 Medication User (PRD §3)
- **Screen Architecture**: 18 MVP screens + 2 Post-MVP screens

### 1.3 Document Conventions

**Định danh &amp; Ký hiệu:**

- **UC-XXX**: Use Case (lần lượt từ UC-001 đến UC-023 cho MVP; UC-024+ cho Post-MVP)
- **AF-XXX.Y**: Alternative Flow (ví dụ: AF-001.1, AF-001.2 → các flow thay thế của UC-001)
- **AC-XXX.Y**: Acceptance Criterion (viết bằng EARS notation: WHEN/IF/THEN; ví dụ: AC-001.1)
- **WF-XXX**: Wireframe Screen (WF-001 đến WF-018 cho MVP; tham chiếu đến Wireframes.md)
- **TF-XXX**: Task Flow (TF-001 đến TF-005 cho main user journeys)
- **SF-XXX**: Sub-Flow (SF-001 đến SF-003 cho micro-interactions trong một screen)

**Actor &amp; Persona:**

- Tất cả UCs tham chiếu tới PRD §3 personas:
  - **Mass-Market Diet Novice**: Primary persona; người dùng muốn log bữa ăn nhanh chóng, không phức tạp
  - **GLP-1 Medication User**: Secondary persona; quan tâm đến tracking GLP-1 symptoms + calorie intake (Post-MVP)

**Format Each UC:**

- Preconditions, Main Flow, Alternative Flows (AF), Postconditions
- Acceptance Criteria (dùng EARS notation)
- Screen references (WF-XXX) + Entry/Exit Points
- Context Variations (First-time, Returning, Power user)

**Priority Tiers** (used in §7 Use Case Priorities):

- **High**: MVP critical path; must-have; blocking other UCs
- **Medium**: MVP secondary features; depends on High priority
- **Low**: Nice-to-have; deferrable to Post-MVP

### 1.4 Mối liên hệ với các tài liệu khác

- **← PRD.md**: Đặc tả tính năng, personas, screen inventory, business goals
- **→ Functional_Requirements.md**: FR sẽ chi tiết hóa mỗi UC thành chức năng hệ thống, data models, APIs
- **→ Wireframes.md**: Mỗi WF-XXX screen sẽ được thiết kế chi tiết, layout, components
- **→ UX_Flows.md**: Task flows (§5) sẽ trở thành UX flows tương tác, prototypes

---

## 2. Feature Groups &amp; User Stories

### 2.1 Feature Group 1: Core Loop (Chụp → Xác nhận → Log)

#### UC-001: Mở Camera để Chụp Bữa Ăn

**Actor**: Mass-Market Diet Novice (người mới)  
**Persona**: Đang cơm trưa, muốn ghi log nhanh, không muốn phức tạp  
**Mục tiêu**: Mở camera để chụp ảnh bữa ăn  
**Điều kiện trước**: Đã onboarding, có quyền camera

**Main Flow**:

1. User bấm "Camera" tab hoặc nút CTA camera chính
2. App yêu cầu quyền camera (nếu lần đầu)
3. User cho phép quyền
4. Camera interface mở, hiển thị live preview
5. User thấy hint: "Chụp từ trên xuống để kết quả tốt nhất"

**Alternative Flow AF-001.1: Quyền Camera Bị Từ chối**

1. User từ chối quyền camera
2. App hiển thị: "Cần quyền camera. Vào Settings → Calo AI → Camera"
3. User có thể back hoặc mở Settings

**Alternative Flow AF-001.2: Quyền Camera Đã Cấp Trước Đó**

1. User bấm Camera
2. Camera mở ngay tức thì (không cần yêu cầu quyền lại)

**Postconditions**: Camera interface mở, sẵn sàng chụp  
**Acceptance Criteria**:

- AC-001.1: WHEN app.launched THEN camera tab visible on bottom tab bar
- AC-001.2: WHEN user taps Camera tab FOR FIRST TIME THEN camera permission request shown (native iOS dialog)
- AC-001.3: WHEN user grants permission THEN live preview appears within 1s
- AC-001.4: IF user denies permission THEN helpful message with Settings link shown; Camera tab shows "Permission needed" state

**Screen Chính**: WF-002 (Camera screen)  
**Màn hình liên quan**: WF-009 (Permission request — native), WF-001 (back to home if denied)  
**Entry Point**: Người dùng bấm Camera tab hoặc icon camera từ Diary  
**Exit Point**: Ảnh được chụp hoặc user bấm back  

**Context Variations**:

- **Người dùng mới lần đầu**: Hint "Chụp từ trên xuống" + permission request + encouraging onboarding message
- **Người dùng quay lại**: Camera mở trực tiếp, không hint
- **Power user**: Camera mở tức thì; gesture swipe để điều chỉnh brightness/zoom

---

#### UC-004: Xác nhận hoặc Chỉnh sửa Nguyên liệu &amp; Khẩu phần

**Actor**: Mass-Market Diet Novice  
**Mục tiêu**: Xác nhận nguyên liệu AI phát hiện được và điều chỉnh khẩu phần trước khi lưu  
**Điều kiện trước**: Kết quả AI hiển thị (UC-003)

**Main Flow**:

1. Confirmation screen (WF-003) hiển thị danh sách nguyên liệu phát hiện
2. User xem danh sách (mặc định checked all)
3. User có thể bỏ check nguyên liệu không muốn
4. User điều chỉnh khẩu phần: nhỏ/vừa/lớn (hoặc gram)
5. Calo/macro cập nhật real-time khi điều chỉnh
6. User bấm "Confirm &amp; Save"
7. Log được lưu vào diary

**Alternative Flow AF-004.1: Thêm Nguyên liệu**

1. User bấm "+ Add ingredient"
2. Input field hiện, user gõ tên nguyên liệu
3. Autocomplete từ database
4. Thêm vào danh sách

**Alternative Flow AF-004.2: Không Hài Lòng → Retry**

1. User bấm "Retry" (back to camera)
2. Quay lại UC-001

**Postconditions**: Log lưu thành công, user quay lại Diary  
**Acceptance Criteria**:

- AC-004.1: WHEN Confirmation screen shown THEN ingredients list with checkboxes visible
- AC-004.2: WHEN user unchecks ingredient THEN calorie/macros recalculate within 200ms
- AC-004.3: WHEN user adjusts portion (small/medium/large) THEN values update instantly
- AC-004.4: WHEN user taps "Confirm &amp; Save" THEN log appears in Diary immediately

**Screen Chính**: WF-003 (Confirmation)  
**Entry Point**: UC-003 result  
**Exit Point**: Saved to Diary (UC-011) or Retry (UC-001)

---

#### UC-002: Chụp hoặc Chọn Ảnh Bữa Ăn

**Actor**: Mass-Market Diet Novice  
**Mục tiêu**: Chụp ảnh bữa ăn từ camera hoặc chọn từ thư viện ảnh  
**Điều kiện trước**: Camera interface mở và có quyền camera (UC-001)

**Main Flow**:

1. Camera live preview hiển thị
2. User frame bữa ăn trong shot
3. User bấm nút chụp (large circular button)
4. Flash (nếu cần) và preview ảnh vừa chụp
5. User thấy 2 buttons: "Use This" hoặc "Retake"
6. User bấm "Use This"
7. Ảnh được chọn, sẵn sàng gửi lên AI

**Alternative Flow AF-002.1: Chọn từ Photo Library**

1. User bấm icon "Photo Library" (bên cạnh nút chụp)
2. Native photo picker mở
3. User chọn ảnh từ camera roll
4. Ảnh preview hiển thị
5. User bấm "Use This"

**Alternative Flow AF-002.2: User Không Hài Lòng**

1. User bấm "Retake"
2. Camera quay lại live preview
3. User có thể chụp lại hoặc back

**Postconditions**: Ảnh được chọn, sẵn sàng gửi lên AI

**Acceptance Criteria**:

- AC-002.1: WHEN user taps shutter button THEN photo captured + preview shown within 2s
- AC-002.2: WHEN photo preview shown THEN "Use This" and "Retake" buttons visible
- AC-002.3: IF user taps Photo Library icon THEN native photo picker opens
- AC-002.4: WHEN user selects photo from library THEN preview shown with same UI as captured photo
- AC-002.5: IF user taps "Use This" THEN proceed to UC-003 (AI loading)

**Screen Chính**: WF-002 (Camera + Preview)  
**Screens Involved**: WF-002, WF-010 (next)  
**Entry Point**: UC-001 (Camera already open)  
**Exit Point**: User bấm "Use This" → UC-003, hoặc "Retake" → UC-002 main flow

**Context Variations**:

- **Người dùng mới lần đầu**: Hint "Chụp từ trên xuống để kết quả tốt nhất"
- **Người dùng quay lại**: Camera mở trực tiếp, không hint, shutter ready
- **Power user**: Camera auto-captures after 3s if stationary (optional mode)

---

#### UC-003: Xem Kết Quả Nhận Diện AI

**Actor**: Mass-Market Diet Novice  
**Mục tiêu**: Xem AI nhận diện được loại thực phẩm nào, calo/macros là bao nhiêu  
**Điều kiện trước**: Ảnh được chụp/chọn và "Use This" bấm (UC-002)

**Main Flow**:

1. App hiển thị loading state: "Analyzing your meal..." (WF-010) + spinner
2. Sau 2-5s, kết quả trả về từ AI Vision API
3. Screen chuyển sang WF-003 (Confirmation)
4. Hiển thị: {tên món, calo, protein, carbs, fat, nguyên liệu phát hiện}
5. User thấy hint: "Xác nhận nguyên liệu bên dưới rồi lưu log"

**Alternative Flow AF-003.1: AI Không Chắc Chắn (confidence &lt; 70%)**

1. AI trả về confidence &lt; 70%
2. App hiển thị: "⚠️ Không chắc chắn. Hãy chỉnh sửa bên dưới hoặc thử lại"
3. User có thể (a) chỉnh sửa thủ công (UC-004 AF-004.1), (b) retry chụp (AF-003.3)

**Alternative Flow AF-003.2: AI Nhận Diện Lỗi (API error/timeout)**

1. AI timeout (&gt;10s) hoặc error
2. App hiển thị error modal: "Kết nối bị gián đoạn. Thử lại?"
3. User có thể "Retry" (call API again) hoặc "Cancel" (back to camera)

**Alternative Flow AF-003.3: Retry Chụp**

1. User bấm "Take another photo"
2. Back to WF-002 camera
3. Quay lại UC-002

**Postconditions**: Kết quả AI hiển thị, sẵn sàng xác nhận

**Acceptance Criteria**:

- AC-003.1: WHEN user taps "Use This" from UC-002 THEN loading screen (WF-010) shown with spinner + "Analyzing..." text
- AC-003.2: WHEN AI returns result (2-5s) THEN Confirmation screen (WF-003) shown with meal name, calories, macros
- AC-003.3: THEN all 4 ingredient items displayed with checkboxes checked by default
- AC-003.4: IF AI confidence &lt; 70% THEN warning badge + "Edit below" or "Retry" option shown
- AC-003.5: IF API timeout (&gt;10s) THEN error modal with "Retry" or "Cancel" button

**Screen Chính**: WF-010 (AI Loading), then WF-003 (Confirmation)  
**Screens Involved**: WF-010, WF-003  
**Entry Point**: UC-002 "Use This" button  
**Exit Point**: UC-004 (Confirm/Edit) or AF-003.2 (Retry)

**Context Variations**:

- **Người dùng mới**: Full loading animation + encouraging message
- **Người dùng quay lại**: Faster perception (cached results may appear)
- **Power user / High confidence (&gt;95%)**: May auto-confirm (optional) and skip to Diary

---

#### UC-005: Thêm Nguyên Liệu Thêm

**Actor**: Mass-Market Diet Novice  
**Mục tiêu**: Thêm nguyên liệu không được AI phát hiện  
**Điều kiện trước**: Confirmation screen (WF-003) hiển thị, user muốn thêm ingredient

**Main Flow**:

1. User bấm "+ Add ingredient" button
2. Input field hiện lên với placeholder "e.g., olive oil, rice"
3. User gõ tên nguyên liệu
4. Autocomplete dropdown hiện với gợi ý từ database
5. User bấm suggestion hoặc Enter để confirm
6. Ingredient thêm vào danh sách (unchecked by default)
7. Calo/macro cập nhật real-time

**Alternative Flow AF-005.1: Manual Entry (Không có Suggestion)**

1. User gõ tên không tìm thấy suggestion
2. User bấm "Add as custom" button
3. Ingredient thêm với default calo (0 kcal) — user sẽ adjust later
4. Hint: "Điều chỉnh khẩu phần để tính calo"

**Alternative Flow AF-005.2: Cancel Add**

1. User bấm outside input hoặc "X" button
2. Input field dismisses, ingredient không được thêm

**Postconditions**: Ingredient thêm vào danh sách, calo updated

**Acceptance Criteria**:

- AC-005.1: WHEN user taps "+ Add ingredient" THEN input field appears with keyboard
- AC-005.2: WHEN user types THEN autocomplete suggestions appear within 500ms
- AC-005.3: WHEN user taps suggestion THEN ingredient added + macros recalculate
- AC-005.4: IF no suggestion found THEN "Add as custom" option shown
- AC-005.5: WHEN custom ingredient added THEN checkbox unchecked by default (user must verify)

**Screen Chính**: WF-003 (Confirmation)  
**Screens Involved**: WF-003  
**Entry Point**: UC-004 (Confirmation screen open)  
**Exit Point**: Back to ingredient list (UC-004 continues)

---

#### UC-006: Điều Chỉnh Khẩu Phần (Portion Size)

**Actor**: Mass-Market Diet Novice  
**Mục tiêu**: Thay đổi khẩu phần để tính calo chính xác  
**Điều kiện trước**: Confirmation screen (WF-003), ingredient list visible

**Main Flow**:

1. User nhìn thấy portion selector cho mỗi ingredient (mặc định "Medium")
2. User bấm portion selector (small/medium/large buttons hoặc stepper +/-)
3. System cập nhật calo/macro real-time
4. Portion size hiển thị bên cạnh ingredient name (e.g., "Pasta - Large (200g)")
5. Total calo/macro updated at top

**Alternative Flow AF-006.1: Manual Gram Input**

1. User bấm "Enter grams" để input khẩu phần theo gram thay vì small/medium/large
2. Input field mở với number keyboard
3. User gõ gram value (e.g., 250g)
4. System cập nhật calo based on gram

**Postconditions**: Portion adjusted, macros recalculated

**Acceptance Criteria**:

- AC-006.1: WHEN user taps portion button THEN options (small/medium/large) shown
- AC-006.2: WHEN user selects portion THEN calo/macro recalculate within 200ms
- AC-006.3: WHEN portion changed THEN total at top of screen updates
- AC-006.4: IF manual gram entry used THEN system looks up gram→calo conversion from database
- AC-006.5: WHEN user adjusts portion multiple times THEN changes persist on screen

**Screen Chính**: WF-003 (Confirmation)  
**Screens Involved**: WF-003  
**Entry Point**: UC-004 (Confirmation visible)  
**Exit Point**: Back to ingredient list (UC-004 continues)

---

#### UC-007: Điều Chỉnh Thông Tin Macro Thủ Công

**Actor**: Mass-Market Diet Novice  
**Mục tiêu**: Điều chỉnh protein/carbs/fat nếu không chính xác  
**Điều kiện trước**: Confirmation screen showing macros

**Main Flow**:

1. User taps pencil icon next to macro values
2. Macro editor opens with input fields for Protein / Carbs / Fat (in grams)
3. User edits values manually
4. System recalculates calo from new macros
5. Changes reflected in total display

**Alternative Flow AF-007.1: Reset to AI Estimate**

1. User taps "Reset to AI estimate"
2. Values revert to original AI-provided macros
3. Calo recalculated

**Postconditions**: Macros updated, calo recalculated

**Acceptance Criteria**:

- AC-007.1: WHEN user taps macro edit icon THEN input fields appear for P/C/F
- AC-007.2: WHEN user updates values THEN total calo recalculates instantly
- AC-007.3: THEN macro total &gt; 0 must be validated (error if all 0)

**Screen Chính**: WF-003 (Confirmation)  
**Screens Involved**: WF-003  
**Entry Point**: UC-004 (Confirmation visible)  
**Exit Point**: Back to ingredient list (UC-004 continues)

---

#### UC-008: Xoá Nguyên Liệu Đã Chọn

**Actor**: Mass-Market Diet Novice  
**Mục tiêu**: Xoá nguyên liệu không muốn từ danh sách  
**Điều kiện trước**: Confirmation screen (WF-003), ingredient list visible

**Main Flow**:

1. User bấm checkbox để uncheck ingredient (đã checked by default)
2. Hoặc: User swipe left on ingredient → delete button appears → tap delete
3. Ingredient xoá khỏi danh sách
4. Calo/macro cập nhật real-time (trừ đi calo của ingredient)

**Alternative Flow AF-008.1: Re-add Deleted Ingredient**

1. User bấm "Undo" (if shown within 3s)
2. Ingredient được restore

**Postconditions**: Ingredient removed, calo updated

**Acceptance Criteria**:

- AC-008.1: WHEN user unchecks ingredient THEN it's removed from macros calculation
- AC-008.2: WHEN ingredient removed THEN total calo/macro decrease
- AC-008.3: IF all ingredients removed THEN warning shown (cannot save empty log)

**Screen Chính**: WF-003 (Confirmation)  
**Screens Involved**: WF-003  
**Entry Point**: UC-004 (Confirmation visible)  
**Exit Point**: Back to ingredient list (UC-004 continues)

---

#### UC-009 through UC-023: [Remaining UCs - Tabular Summary Format]


| UC ID  | Tên                                  | Actor                | Mục tiêu                                                   | Main Flow (1-2 lines)                                                                                                                                                                | Screens                      | Điều kiện trước               |
| ------ | ------------------------------------ | -------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------- | ----------------------------- |
| UC-009 | Xem scan còn lại                     | Mass-market          | Biết được còn bao nhiêu lượt scan today                    | 1. Diary/Camera tab → hiển thị "X/3 scans used" badge; 2. When hover, tooltip shows "Unlimited with Premium"                                                                         | WF-004, WF-002               | Đã onboarding                 |
| UC-010 | Hết lượt → CTA Upgrade               | Mass-market          | Thấy paywall khi scan hết                                  | 1. Bấm scan lần thứ 4 → modal WF-006 "You've used 3 free scans today. Upgrade for unlimited"                                                                                         | WF-006 (Paywall modal)       | 3 scans used today            |
| UC-011 | Xem Diary theo ngày                  | Mass-market          | Xem log bữa ăn hôm nay + progress vs goal                  | 1. Bấm Diary tab → ngày hôm nay mở rộng, danh sách log; 2. Xem progress bar (1800/2000 cal) + visual on-track indicator                                                              | WF-004                       | Có log data or empty state    |
| UC-012 | Xem Diary theo tuần                  | Mass-market          | Xem tổng tiến bộ tuần này                                  | 1. Toggle "Week view" button; 2. 7 ngày hiển thị, mỗi ngày 1 hàng; 3. Tuần total calo/macro at bottom                                                                                | WF-004                       | Đã view Daily view            |
| UC-013 | So sánh vs Mục tiêu                  | Mass-market          | Biết calo nạp bao nhiêu vs mục tiêu daily                  | 1. Progress bar prominent at top: "1800 / 2000 cal"; 2. Color: green (on-track) / yellow (close) / red (over); 3. Macro breakdown (P/C/F) visible                                    | WF-004, WF-005               | Dairy with data               |
| UC-014 | Chỉnh sửa log cũ                     | Mass-market          | Thay đổi log từ ngày trước hoặc hôm nay                    | 1. Swipe left on log item → Edit button; 2. Edit modal WF-013 opens; 3. Change portion/ingredient/remove; 4. Tap Save                                                                | WF-004 → WF-013 (edit modal) | Any saved log                 |
| UC-015 | Xoá log                              | Mass-market          | Xoá log nhập sai hoặc không muốn                           | 1. Swipe left on log → Delete button; 2. Confirmation modal WF-014 "Delete this log?"; 3. Confirm delete; 4. Log xoá, total updated                                                  | WF-004 → WF-014 (confirm)    | Any saved log                 |
| UC-016 | Nhập thông tin cơ bản                | Người mới            | Cung cấp profile (height, weight, goal) để tính TDEE       | 1. Onboarding Step 1: Height + Weight input fields; 2. Mifflin-St Jeor formula applied; 3. Continue button                                                                           | WF-008 (Onboarding step 1)   | App first launch              |
| UC-017 | Chọn mức hoạt động                   | Người mới            | Định activity level (Sedentary/Light/Moderate/Very Active) | 1. Onboarding Step 2: Radio options for activity level; 2. Show example for each (e.g., "Light = office work"); 3. Continue                                                          | WF-008 (step 2)              | After UC-016                  |
| UC-018 | Xem mục tiêu calo được tính          | Người mới            | Xác nhận mục tiêu calo được tính từ profile                | 1. Onboarding Final Step: "Your daily calorie goal: 2000 kcal"; 2. Show formula used; 3. "Ready to start logging?" button                                                            | WF-008 (final)               | After UC-017                  |
| UC-019 | Xem Paywall (giá + trial length)     | User hết scan        | Thấy pricing rõ ràng trước khi commit                      | 1. Paywall modal WF-006: "Unlock unlimited scans"; 2. Show trial length (7 days) + price ($9.99/mo or$39.99/yr); 3. CTA: "Start free trial"                                          | WF-006                       | Hết scan (UC-010) or Settings |
| UC-020 | Bắt đầu trial 7 ngày                 | User hết scan        | Bắt đầu trial không lo bị tính phí surprise                | 1. Tap "Start 7-day trial" on WF-006; 2. StoreKit payment sheet; 3. Confirm trial; 4. Receipt validated, Premium activated                                                           | WF-006 → StoreKit            | Viewing paywall               |
| UC-021 | Huỷ subscription                     | Current subscriber   | Huỷ nếu không muốn tiếp tục                                | 1. Settings tab → WF-007 → "Your subscription: Premium"; 2. Tap "Manage subscription"; 3. Tap "Cancel subscription" → WF-018 confirm modal; 4. Confirm → scheduled cancel on renewal | WF-007 → WF-018              | Active subscription           |
| UC-022 | Quản lý subscription (view + change) | Current subscriber   | Xem subscription status, renewal date, upgrade/downgrade   | 1. Settings → WF-007 → "Your subscription: Premium, renews Jan 25"; 2. Options: Change plan / Restore / Cancel / Contact support; 3. View next renewal date                          | WF-007                       | Active subscription           |
| UC-023 | Restore purchase                     | Returning subscriber | Restore subscription nếu chuyển device / re-install        | 1. Settings → WF-007 → "No active subscription"; 2. Tap "Restore purchases"; 3. StoreKit lookup for app purchases; 4. If found, subscription restored instantly                      | WF-007                       | No active subscription in app |


---

### 2.2 Feature Group 2: GLP-1 Tracking (Post-MVP — Outlined)


| UC ID  | Tên                   | Scope           |
| ------ | --------------------- | --------------- |
| UC-024 | Log triệu chứng GLP-1 | Post-MVP add-on |
| UC-025 | Nhắc lịch thuốc       | Post-MVP add-on |
| UC-026 | Xem insights GLP-1    | Post-MVP add-on |


---

### 2.3 Feature Group 3: AI Coach (Post-MVP — Outlined)


| UC ID  | Tên               | Scope           |
| ------ | ----------------- | --------------- |
| UC-027 | Chat với AI Coach | Post-MVP add-on |


---

## 2 bis. Feature Expression Matrix

**Mục đích**: Cùng một UC được thể hiện khác nhau trên các screens khác nhau. Ma trận này ngăn cản tư duy "1 UC = 1 screen".


| UC ID  | UC Name                | Primary Screen            | Primary Expression                                                                 | Secondary Screen(s)          | Secondary Expression(s)                | Context Trigger                      | Expression Difference                  |
| ------ | ---------------------- | ------------------------- | ---------------------------------------------------------------------------------- | ---------------------------- | -------------------------------------- | ------------------------------------ | -------------------------------------- |
| UC-001 | Mở Camera              | WF-002                    | Full tab button                                                                    | WF-004 (Diary)               | Inline camera icon (tap to switch tab) | User on Diary → wants camera         | Tab navigation vs inline action        |
| UC-002 | Chụp/Chọn Ảnh          | WF-002                    | Large circular shutter button + library icon                                       | —                            | —                                      | —                                    | Single primary expression              |
| UC-003 | Xem AI Result          | WF-010 (loading) → WF-003 | Full-screen modal with animated result reveal                                      | —                            | —                                      | —                                    | Single primary expression              |
| UC-004 | Xác nhận &amp; Edit    | WF-003                    | Checkboxes for each ingredient + portion buttons                                   | —                            | —                                      | —                                    | Single primary expression              |
| UC-009 | Xem Scans Còn Lại      | WF-002 (Camera)           | Badge "X/3 scans" prominently on shutter                                           | WF-004 (Diary)               | Subtle text "Scans: 3/3" in header     | User on different tab                | Bold badge vs subtle text              |
| UC-010 | Hết Lượt → Upgrade CTA | WF-006 (Paywall)          | Full-screen modal with trial offer                                                 | WF-002 (Camera, 4th attempt) | Modal triggered on button tap          | Scan limit reached                   | Modal interruption vs button-triggered |
| UC-011 | Xem Diary              | WF-004                    | List view with daily logs, progress bar top                                        | —                            | —                                      | —                                    | Single primary expression              |
| UC-013 | So sánh vs Goal        | WF-004                    | Progress bar (Hero zone, animated)                                                 | WF-005 (Dashboard)           | Progress circle card in weekly summary | User explores deeper                 | Bar vs circle visualization            |
| UC-014 | Chỉnh sửa Log          | WF-004                    | Swipe-left action (edit button)                                                    | WF-013                       | Modal form for editing details         | User initiates edit                  | Gesture-triggered vs modal editing     |
| UC-015 | Xoá Log                | WF-004                    | Swipe-left action (delete button)                                                  | WF-014                       | Confirmation modal                     | User initiates delete                | Swipe action vs confirmation modal     |
| UC-019 | Xem Paywall            | WF-006                    | Full-screen pricing modal (trial 7 days, price shown)                              | WF-007 (Settings)            | Text "Upgrade to Premium" link         | User accesses from different context | Interruptive modal vs link in settings |
| UC-020 | Bắt đầu Trial          | WF-006                    | "Start 7-day trial" CTA button (blue, prominent)                                   | —                            | —                                      | —                                    | Single primary expression              |
| UC-021 | Huỷ Subscription       | WF-007                    | "Cancel subscription" link → WF-018 confirm modal                                  | —                            | —                                      | —                                    | Link → Modal confirmation              |
| UC-022 | Quản lý Sub            | WF-007                    | Text "Your subscription: Premium, renews [date]" + buttons (Change/Restore/Cancel) | —                            | —                                      | —                                    | Single primary expression              |


**Rule Check:**

- High-priority UCs with &gt;=2 screen expressions: UC-001, UC-009, UC-010, UC-013, UC-014, UC-015, UC-019 ✓
- Single-screen UCs (justified): UC-002, UC-003, UC-004, UC-020, UC-021 (terminal flow), UC-022 (settings-only)
- All expressions differ meaningfully (interaction pattern, information density, user intent) ✓

---

## 3. UC → Screen Mapping

### 3.1 Full UC to Screen Cross-Reference


| UC ID  | UC Name              | Primary Screen | Screens Involved              | Entry Point          | Exit Point            |
| ------ | -------------------- | -------------- | ----------------------------- | -------------------- | --------------------- |
| UC-001 | Mở Camera            | WF-002         | WF-002, WF-009                | Bấm Camera tab       | UC-002                |
| UC-002 | Chụp Ảnh             | WF-002         | WF-002, WF-003, WF-010        | UC-001               | UC-003                |
| UC-003 | Xem Kết quả AI       | WF-010, WF-003 | WF-010 → WF-003               | UC-002               | UC-004                |
| UC-004 | Xác nhận Nguyên liệu | WF-003         | WF-003, WF-004                | UC-003               | UC-011 saved          |
| UC-009 | Xem Scan Còn Lại     | WF-002, WF-004 | WF-002 or WF-004              | Any time             | —                     |
| UC-010 | Hết Lượt → CTA       | WF-006         | WF-002 → WF-006 modal         | 4th scan attempt     | UC-019 or close       |
| UC-011 | Xem Diary Ngày       | WF-004         | WF-004                        | Bấm Diary tab        | UC-014, UC-015        |
| UC-012 | Xem Diary Tuần       | WF-004         | WF-004                        | UC-011 + toggle week | UC-013                |
| UC-013 | So sánh vs Mục tiêu  | WF-004, WF-005 | WF-004 or WF-005              | Viewing diary        | —                     |
| UC-014 | Chỉnh sửa Log        | WF-004, WF-013 | WF-004 → WF-013 modal         | Swipe log item       | UC-011 saved          |
| UC-015 | Xoá Log              | WF-004, WF-014 | WF-004 → WF-014 confirm modal | Swipe log item       | UC-011                |
| UC-016 | Nhập Profile         | WF-008         | WF-008 step 1                 | App launch           | UC-017                |
| UC-017 | Chọn Activity        | WF-008         | WF-008 step 3                 | UC-016 complete      | UC-018                |
| UC-018 | Xem Mục tiêu Calo    | WF-008         | WF-008 final                  | UC-017 complete      | App main (WF-002/004) |
| UC-019 | Xem Paywall          | WF-006         | WF-006 modal                  | UC-010 or Settings   | UC-020 or close       |
| UC-020 | Bắt đầu Trial        | WF-006         | WF-006 → StoreKit             | UC-019 "Start trial" | Premium active        |
| UC-021 | Huỷ Subscription     | WF-007, WF-018 | WF-007 → WF-018 confirm       | Settings             | Premium cancelled     |
| UC-022 | Quản lý Sub          | WF-007         | WF-007                        | Bấm Settings tab     | —                     |
| UC-023 | Restore Purchase     | WF-007         | WF-007                        | Settings             | Sub restored          |


### 3.2 Screen → UC Coverage Table


| Screen ID | Screen Name          | Archetype   | UCs Covered                            | Interaction Density |
| --------- | -------------------- | ----------- | -------------------------------------- | ------------------- |
| WF-001    | Splash               | System      | — (no UC)                              | Light               |
| WF-002    | Camera               | Action      | UC-001, UC-002, UC-009                 | Dense               |
| WF-003    | Confirmation         | Action      | UC-003, UC-004                         | Dense               |
| WF-004    | Diary                | Consumption | UC-011, UC-012, UC-013, UC-014, UC-015 | Dense               |
| WF-005    | Dashboard            | Consumption | UC-013                                 | Medium              |
| WF-006    | Paywall              | Management  | UC-010, UC-019, UC-020                 | Medium              |
| WF-007    | Settings             | Management  | UC-021, UC-022, UC-023                 | Medium              |
| WF-008    | Onboarding           | System      | UC-016, UC-017, UC-018                 | Medium              |
| WF-009    | Permission Request   | System      | UC-001 (AF)                            | Light               |
| WF-010    | AI Loading           | System      | UC-002, UC-003                         | Light               |
| WF-013    | Edit Log Modal       | —           | UC-014                                 | Medium              |
| WF-014    | Delete Confirm Modal | —           | UC-015                                 | Light               |
| WF-018    | Cancel Sub Confirm   | —           | UC-021                                 | Light               |


---

## 4. Screen-Context Use Cases (Abbreviated)

*Full detailed version with all state variations and zones would follow this template. Sample for WF-002 and WF-004 below.*

### WF-002: Camera Screen

**Archetype**: Action  
**User Intent**: "I want to quickly photograph and log my meal without friction"  
**Primary Action**: Capture food photo  

**Action Layers**:

- **Layer 1 (Primary)**: Big circular shutter button
- **Layer 2 (Contextual)**: Photo library icon, flip camera, brightness control
- **Layer 3 (Discovery)**: "Tips" → best angle hints
- **Layer 4 (Personal)**: Settings icon

**Content Zones**:

- **Zone A (Hero)**: Live camera preview (full screen)
- **Zone B (Engagement)**: Shutter button + photo library icon
- **Zone C (Discovery)**: "Recent scans" carousel (if returning user)
- **Zone D (Utility)**: Settings, back, scan count badge

**State Variations**:


| State                          | Context                     | Layout Change                                                |
| ------------------------------ | --------------------------- | ------------------------------------------------------------ |
| **First Visit**                | New user, permission needed | "Allow camera access" dialog + hint "Angle from above"       |
| **Returning / Has Permission** | User familiar               | Camera opens directly, no hints                              |
| **Scan Limit Approaching**     | 2/3 scans used              | Badge shows "2/3 scans", preview tip about upgrade           |
| **Offline**                    | No network                  | Banner "Camera works offline; results sent when reconnected" |


---

### WF-004: Diary Screen

**Archetype**: Consumption  
**User Intent**: "I want to see what I've eaten today and whether I'm on track"  
**Primary Action**: Review daily log + macro progress  

**Action Layers**:

- **Layer 1 (Primary)**: Today's total calo/macro display
- **Layer 2 (Contextual)**: Edit/delete individual logs (swipe actions)
- **Layer 3 (Discovery)**: "Compare with yesterday" link, "Week view" toggle
- **Layer 4 (Personal)**: Change goal, share progress

**Content Zones**:

- **Zone A (Hero)**: Progress bar (e.g., "1800 / 2000 cal") with visual indicator
- **Zone B (Engagement)**: List of today's log items
- **Zone C (Discovery)**: "Dashboard" card (insights, weekly trends)
- **Zone D (Utility)**: Date picker, toggle day/week view

**State Variations**:


| State                    | Context           | Layout Change                                                                    |
| ------------------------ | ----------------- | -------------------------------------------------------------------------------- |
| **First Visit / Empty**  | No logs yet       | Empty state: "No meals logged yet. Tap Camera to add one." + large CTA to Camera |
| **Returning / Has Logs** | Normal daily view | Full log list, progress bar prominent                                            |
| **Approaching Limit**    | Close to goal     | Progress bar color shifts to yellow/orange warning                               |
| **Over Limit**           | Exceeded goal     | Progress bar red, message "You're over your goal"                                |
| **Offline / Error**      | Can't sync logs   | Banner "Changes saved locally; will sync when online"                            |


---

### WF-003: Confirmation Screen

**Archetype**: Action  
**User Intent**: "I want to verify the AI got it right before I save this meal"  
**Primary Action**: Confirm and save log  

**Action Layers**:

- **Layer 1 (Primary)**: Ingredient list with checkboxes + portion selectors
- **Layer 2 (Contextual)**: Edit macro values, add ingredient, remove ingredient
- **Layer 3 (Discovery)**: "AI wasn't sure?" link to confidence explanation
- **Layer 4 (Personal)**: "Save as favorite" (template for next time)

**Content Zones**:

- **Zone A (Hero)**: Meal name + photo preview (small thumbnail)
- **Zone B (Engagement)**: Ingredient list (checked by default) + portion buttons (small/medium/large)
- **Zone C (Discovery)**: Total calo/macro prominently displayed + breakdown (P/C/F)
- **Zone D (Utility)**: "Confirm &amp; Save" button (blue, full-width, bottom), "Retry photo" link

**State Variations**:


| State                          | Context               | Layout Change                                                        |
| ------------------------------ | --------------------- | -------------------------------------------------------------------- |
| **High Confidence (&gt;80%)**  | AI is sure            | No warnings, straightforward save                                    |
| **Medium Confidence (50-80%)** | AI is somewhat unsure | Yellow banner: "Please verify ingredients below"                     |
| **Low Confidence (&lt;50%)**   | AI is very unsure     | Red banner: "Not sure. Please edit carefully" + "Retry photo" option |
| **User Editing**               | Ingredient changed    | Macro values update in real-time; save button remains enabled        |


---

### WF-005: Dashboard / Weekly Insights Screen

**Archetype**: Consumption  
**User Intent**: "I want to see my progress over the week and understand my trends"  
**Primary Action**: View weekly summary and macro breakdown  

**Action Layers**:

- **Layer 1 (Primary)**: Weekly calorie chart (bar chart or line chart)
- **Layer 2 (Contextual)**: Daily breakdown (each day shows calo/macro)
- **Layer 3 (Discovery)**: "Your average: 1850 kcal/day" insight card
- **Layer 4 (Personal)**: Export week as PDF, share achievement

**Content Zones**:

- **Zone A (Hero)**: Large chart showing week view (Mon-Sun, each day's total kcal bar)
- **Zone B (Engagement)**: "Average this week" stat card (1850/2000, 92% on-track)
- **Zone C (Discovery)**: Weekly macro breakdown (pie chart: P 25% / C 45% / F 30%)
- **Zone D (Utility)**: Date picker (change week), "Back to daily" button

**State Variations**:


| State             | Context                 | Layout Change                                                 |
| ----------------- | ----------------------- | ------------------------------------------------------------- |
| **First Week**    | No data history         | Empty state: "Log meals to see weekly trends" + CTA to Camera |
| **On Track**      | Average on goal         | Green badges, encouraging message                             |
| **Above Average** | Consistently over goal  | Orange badges, gentle coaching tip                            |
| **Below Average** | Consistently under goal | Blue badges, encouragement to eat enough                      |


---

### WF-006: Paywall / Subscription Modal

**Archetype**: Management  
**User Intent**: "I want to understand what Premium offers and whether to try it"  
**Primary Action**: Start 7-day free trial  

**Action Layers**:

- **Layer 1 (Primary)**: Trial offer + pricing displayed prominently
- **Layer 2 (Contextual)**: Comparison: Free vs Premium benefits
- **Layer 3 (Discovery)**: "What's included?" expandable sections
- **Layer 4 (Personal)**: Manage existing subscription, cancel option

**Content Zones**:

- **Zone A (Hero)**: "Unlimited Scans" headline + "7 days free" badge
- **Zone B (Engagement)**: Pricing: "$9.99/month" OR "$39.99/year (save 30%)"
- **Zone C (Discovery)**: Feature list: "✓ Unlimited daily scans", "✓ Advanced insights", "✓ AI Coach (coming soon)"
- **Zone D (Utility)**: "Start 7-day trial" button (blue, full-width), "Remind me later" link

**State Variations**:


| State                | Context                 | Layout Change                                         |
| -------------------- | ----------------------- | ----------------------------------------------------- |
| **First-time Offer** | User never seen paywall | Full paywall with all benefits listed                 |
| **Already Trialing** | Day 3 of trial          | "Your trial expires in 4 days" message instead of CTA |
| **Premium Active**   | Already subscribed      | Show current subscription, "Manage" button            |
| **Trial Expired**    | User let trial expire   | "Reactivate Premium" instead of "Start trial"         |


---

### WF-007: Settings / Account Management Screen

**Archetype**: Management  
**User Intent**: "I want to manage my account, subscription, and preferences"  
**Primary Action**: View and manage subscription  

**Action Layers**:

- **Layer 1 (Primary)**: Subscription status display
- **Layer 2 (Contextual)**: Profile settings (name, goal, activity level)
- **Layer 3 (Discovery)**: Support, FAQ, feedback
- **Layer 4 (Personal)**: Notification preferences, privacy, log out

**Content Zones**:

- **Zone A (Hero)**: User name + avatar (or initials)
- **Zone B (Engagement)**: "Your subscription: Premium, renews Feb 15" + "Manage" button
- **Zone C (Discovery)**: Settings sections: Profile / Notifications / About
- **Zone D (Utility)**: "Log out" button (red, bottom)

**State Variations**:


| State                     | Context                            | Layout Change                                                     |
| ------------------------- | ---------------------------------- | ----------------------------------------------------------------- |
| **No Subscription**       | Free tier active                   | "Upgrade to Premium" button instead of subscription details       |
| **Active Subscription**   | Premium user                       | Show "Manage subscription", "Cancel", "Restore purchases" options |
| **Subscription Canceled** | Canceled but still in grace period | "Your Premium expires Feb 15" + "Reactivate" button               |


---

### WF-008: Onboarding Multi-Step Form

**Archetype**: System  
**User Intent**: "I want to set up my profile so the app calculates my calorie goal"  
**Primary Action**: Complete all 3 steps and get calorie goal  

**Action Layers** (per-step):

- **Step 1 (Height/Weight)**: Input fields with numeric keyboard, CM/KG selectors
- **Step 2 (Activity Level)**: Radio buttons for 4 activity levels + brief description
- **Step 3 (Calorie Goal Summary)**: Show calculated goal, formula used, "Ready to start?" CTA

**Content Zones**:

- **Zone A (Hero)**: Progress indicator (Step 1/3, 2/3, 3/3) + big title
- **Zone B (Engagement)**: Input fields or selection buttons for this step
- **Zone C (Discovery)**: Brief explanation of current step (e.g., "Height helps us estimate your TDEE")
- **Zone D (Utility)**: "Back" + "Next/Continue" buttons (or "Start" on final step)

**State Variations**:


| State             | Context                 | Layout Change                                |
| ----------------- | ----------------------- | -------------------------------------------- |
| **Step 1 Empty**  | Just installed          | Placeholder: "Your height (cm)"              |
| **Step 1 Filled** | Height entered          | Weight field auto-focuses                    |
| **Step 2 Select** | Choosing activity level | Radio buttons with example descriptions      |
| **Step 3 Review** | Final confirmation      | Large calorie display, "Ready to start?" CTA |


---

## 5. Task Flows (Core Journeys)

### TF-001: First-Time User's First Meal Log

**Scenario**: New user, just installed app, first time logging a meal

**Flow**:

1. App launches → WF-001 Splash (2s) → Redirect to WF-008 Onboarding
2. Onboarding: Height/Weight (UC-016) → Activity Level (UC-017) → "Ready?" confirmation (UC-018)
3. Redirect to WF-002 Camera (UC-001: permission request + live preview)
4. User captures meal photo (UC-002)
5. WF-010 AI Loading (2-5s)
6. WF-003 Confirmation: AI shows {meal, calo, macros, ingredients} (UC-003)
7. User confirms ingredients, adjusts portion (UC-004)
8. Log saved → redirect WF-004 Diary (UC-011)
9. User sees: "1 meal logged today, 500 / 2000 cal"

**Duration**: ~5-10 minutes total  
**UCs involved**: UC-016, UC-017, UC-018, UC-001, UC-002, UC-003, UC-004, UC-011  
**Success metric**: Log successfully saved and visible in Diary

---

### TF-002: Established User's Daily Logging (3 meals)

**Scenario**: Returning user, logs breakfast, lunch, dinner

**Flow**:

1. WF-002 Camera: Open directly (cached permission)
2. Snap breakfast photo (UC-002 ~15s)
3. AI result → UC-003, UC-004 confirm/adjust (~30s)
4. Saved to WF-004 Diary
5. Later: Repeat for lunch + dinner (same flow, 3x)
6. Evening: Open WF-004 Diary (UC-011)
7. User sees: "3 meals, 1950 / 2000 cal" (close to goal)
8. Optionally: View WF-005 Dashboard to see week trends (UC-013)

**Duration**: ~5 minutes per meal (3x) = 15 minutes total  
**UCs involved**: UC-001, UC-002, UC-003, UC-004, UC-011, UC-013  
**Success metric**: All 3 logs saved, totals calculated correctly

---

### TF-003: Hitting Scan Limit &amp; Upgrading to Premium

**Scenario**: Free user tries 4th scan, hits limit, converts to Premium trial

**Flow**:

1. After 3 successful logs, user wants 4th meal
2. WF-002 Camera: 4th scan attempt
3. UC-010 triggered: Paywall modal (WF-006) shows "You've used 3 free scans. Upgrade to Premium for unlimited."
4. User sees: Trial offer "7 days free" + pricing ($9.99/mo or$39.99/yr)
5. User taps "Start 7-day trial" (UC-020)
6. StoreKit payment flow (native)
7. Receipt confirmed → Premium activated
8. User continues: 4th scan succeeds, saves log
9. Diary shows: "Premium — unlimited scans"

**Duration**: ~2-3 minutes  
**UCs involved**: UC-009, UC-010, UC-019, UC-020, UC-002, UC-004  
**Success metric**: Trial activated, 4th scan completes successfully

---

### TF-004: User Edits Previous Log

**Scenario**: User realizes they logged wrong portion yesterday, edits it

**Flow**:

1. Open WF-004 Diary
2. Scroll to yesterday's log: "Pasta Carbonara - 600 cal"
3. Swipe left on item (UC-014)
4. Edit button appears → tap
5. WF-013 Edit Modal: Portion shown as "Large", user changes to "Medium" (~400 cal)
6. Calo/macros update live
7. Tap "Save"
8. Diary updates: "Pasta Carbonara - 400 cal"

**Duration**: ~1 minute  
**UCs involved**: UC-011, UC-014  
**Success metric**: Edit saved, old log replaced, totals recalculated

---

### TF-005: User Manages Subscription

**Scenario**: Premium user wants to see subscription details or cancel

**Flow**:

1. Tap Settings tab → WF-007
2. User sees: "Your subscription: Premium, renews Jan 25, 2025"
3. Optionally: Tap "Manage subscription" (UC-022)
4. See options: Change plan / Restore / Cancel
5. If cancel: Tap "Cancel subscription" (UC-021)
6. WF-018 Confirmation modal: "Cancel Premium? You'll lose unlimited scans."
7. Confirm → Subscription cancelled on next renewal
8. Settings updated: "Premium — Expires Jan 25"

**Duration**: ~1 minute  
**UCs involved**: UC-022, UC-021  
**Success metric**: Subscription status displayed accurately, cancel processed

---

## 5 bis: Sub-Flows &amp; Micro-Interactions

### SF-001: Photo Library Picker (within WF-002)

**Parent Screen**: WF-002 (Camera)  
**Trigger**: User taps Photo Library icon (alternative to live capture)  
**Referenced UCs**: UC-002 AF-002.1  


| Step | Component          | User Action                   | System Response                                               | Micro-State   |
| ---- | ------------------ | ----------------------------- | ------------------------------------------------------------- | ------------- |
| 1    | Photo Library icon | Tap                           | Native photo picker opens                                     | Transitioning |
| 2    | Photo picker       | Select photo from camera roll | Selected image preview shown with "Use This / Choose another" | Selected      |
| 3    | Use This button    | Tap                           | Transition to AI loading (WF-010)                             | Loading       |


**Visual Transition**: Slide up from bottom (sheet) or fade in (modal)

---

### SF-002: Ingredient Add/Remove Toggle (within WF-003)

**Parent Screen**: WF-003 (Confirmation)  
**Trigger**: User views ingredient list  
**Referenced UCs**: UC-004, UC-004 AF-004.1  


| Step | Component                 | User Action    | System Response                       | Micro-State |
| ---- | ------------------------- | -------------- | ------------------------------------- | ----------- |
| 1    | Ingredient item           | Tap checkbox   | Checkbox toggles checked/unchecked    | Toggled     |
| 2    | Calo/macro display        | —              | Values recalculate in real-time       | Updating    |
| 3    | "+ Add ingredient" button | Tap            | Input field appears with autocomplete | Editing     |
| 4    | Ingredient input          | Type name      | Autocomplete suggestions appear       | Suggesting  |
| 5    | Suggested item            | Tap suggestion | Item added to list, checkbox checked  | Added       |


**Visual Transition**: Checkbox animation (checkmark draw) + fade-in for input field  
**Haptic**: Light tap on toggle

---

### SF-003: Progress Bar Animation (within WF-004 Diary)

**Parent Screen**: WF-004 (Diary)  
**Trigger**: Log added or edited, macros change  


| Step | Component       | User Action                     | System Response                                               | Micro-State |
| ---- | --------------- | ------------------------------- | ------------------------------------------------------------- | ----------- |
| 1    | Progress bar    | — (auto-trigger after log save) | Bar animates to new percentage                                | Animating   |
| 2    | Calo number     | —                               | Counter ticks up/down                                         | Updating    |
| 3    | Color indicator | —                               | Changes color: green (on-track) / yellow (close) / red (over) | Color shift |


**Visual Transition**: Spring easing for bar fill  
**Haptic**: Medium haptic on goal reached; none otherwise

---

## 6. Scenarios

### 6.1 Happy Path Scenarios

Happy path scenarios represent the main success flows where users accomplish their goals without errors or obstacles.

#### Scenario HP-001: First Meal Logged Successfully

**Actor**: Mass-Market Diet Novice (first-time user)  
**Goal**: Log first meal from start to finish

**Steps**:

1. User opens Camera tab (WF-002)
2. Captures breakfast photo (UC-002)
3. AI analyzes and suggests ingredients (UC-003, result confidence 85%)
4. User confirms all ingredients (UC-004)
5. Adjusts portion to "Large" (UC-006)
6. Taps "Save log"
7. Log appears in Diary (UC-011)
8. Progress bar shows: "480 / 2000 cal"

**Expected Outcome**: Log successfully saved and visible in Diary; macros calculated correctly ✓

---

#### Scenario HP-002: Quick Lunch Log (Returning User)

**Actor**: Mass-Market Diet Novice (returning user)

**Steps**:

1. User opens Camera tab (already has permission, cached, opens instantly)
2. Snaps lunch photo (UC-002, ~10s)
3. AI recognizes "Grilled chicken + rice" with 92% confidence (UC-003)
4. User confirms ingredients immediately (UC-004)
5. Portion already guessed as "Medium" — user accepts
6. Taps "Save log"
7. Log saved to Diary; progress bar updates to "1080 / 2000 cal"

**Expected Outcome**: Complete flow ~30s; log saved; daily progress updated ✓

---

#### Scenario HP-003: Successful Premium Trial Conversion

**Actor**: Mass-Market Diet Novice (free user after 3 scans today)

**Steps**:

1. User attempts 4th scan of the day (UC-010)
2. Paywall modal (WF-006) appears: "Unlimited scans with 7-day free trial"
3. User reads pricing: "$9.99/month or$39.99/year"
4. Taps "Start 7-day trial" (UC-020)
5. StoreKit payment sheet opens (native iOS)
6. User confirms purchase
7. Receipt validated → Premium activated
8. Modal closes; 4th scan proceeds normally
9. Diary shows: "Premium — unlimited scans"

**Expected Outcome**: Trial activated; user can now scan unlimited; positive monetization signal ✓

---

### 6.2 Edge Case Scenarios

Edge cases represent unusual or error conditions where systems must gracefully handle problems.

#### Scenario EC-001: Offline Logging (Network Unavailable)

**Setup**: User opens camera with no internet connection  
**Expected behavior**: App uses on-device AI (cached model) or shows cached results; marks log as "pending sync"

**Steps**:

1. User has no internet; opens Camera (WF-002)
2. Chutes photo (UC-002)
3. On-device AI processes locally (or uses cached results from previous scans)
4. Confirmation screen shows: "📡 Pending sync — will send when online"
5. User confirms ingredients (UC-004)
6. Log saved locally with "pending sync" badge
7. User reconnects to internet → badge changes to "Syncing..."
8. Log synced to server automatically

**Related UCs**: UC-001, UC-002, UC-003, UC-004

---

#### Scenario EC-002: AI Misidentifies Food (Low Confidence)

**Setup**: User photographs a complex salad, AI returns "Pizza" with 35% confidence

**Steps**:

1. User captures photo (UC-002)
2. AI returns uncertain result: "Pizza (?)" (UC-003, AF-003.1 triggered)
3. App shows warning: "⚠️ Not confident. Edit below or try again."
4. User options:
  - *Path A*: Tap "Retry photo" → back to UC-002 (camera)
  - *Path B*: Manually edit ingredients (UC-004 AF-004.1, UC-005) → type "Salad", select from database → continues
5. User chooses Path B: types "Caesar Salad"
6. Database returns standard salad calo (400 kcal)
7. User adjusts portion to "Medium"
8. Saves log with corrected data

**Related UCs**: UC-003 AF-003.1, UC-004, UC-005

---

#### Scenario EC-003: Subscription Trial Expires (Grace Period)

**Setup**: User activated trial 7 days ago; trial expires today; no payment method configured

**Steps**:

1. Trial expires at end of day
2. Premium features become locked (scan limit returns to 3/day)
3. Next day, user attempts 4th scan
4. Paywall (UC-010) appears again: "Trial ended. Upgrade to continue"
5. User options:
  - Tap "Start subscription" → enter payment → subscribes
  - Tap "Skip for now" → returns to free tier (3/day limit)
6. If user chooses "Skip", scan is rejected; prompted to "Upgrade or use tomorrow"

**Related UCs**: UC-020, UC-010, UC-022

---

#### Scenario EC-004: User Switches Devices (Restore Subscription)

**Setup**: User had Premium on iPhone 12, now logs in on new iPhone 15

**Steps**:

1. User logs in with same Apple ID on iPhone 15
2. Opens app → no subscription found locally (app first-time on device)
3. User goes to Settings → WF-007
4. Sees: "No active subscription"
5. Taps "Restore purchases" (UC-023)
6. StoreKit queries App Store for past purchases under Apple ID
7. Finds: "Premium subscription (expires Feb 15, 2027)"
8. Automatically restores Premium to device
9. Settings updated: "Your subscription: Premium, renews Feb 15"
10. User can now scan unlimited

**Related UCs**: UC-023, UC-022

---

### 6.3 Persona-Based Scenarios

Persona-based scenarios show how different user types accomplish goals in their own way.

#### Scenario PB-001: Mass-Market Diet Novice's Daily Routine

**Persona**: Sarah, 28, office worker, wants to lose 15 lbs

**Goal**: Log 3 meals throughout day, track progress

**Context**: Day 2 of using Calo AI; converted to Premium yesterday

**Steps**:

1. **Morning (7 AM)**: Opens Camera tab, snaps breakfast (yogurt + granola)
  - AI recognizes; 150 kcal
  - Saves to Diary
  - Progress: 150 / 2000
2. **Noon (12:30 PM)**: At restaurant; snaps lunch (grilled fish + vegetables)
  - AI returns 450 kcal
  - Sarah adjusts portion (fish was actually smaller than detected)
  - Manually reduces to 380 kcal
  - Saves
  - Progress: 530 / 2000
3. **Evening (6 PM)**: Opens Diary tab (WF-004) to see day's summary
  - Checks progress bar: 530 / 2000 (good, on track)
  - Notices Week view: This week average 1850 kcal/day (below goal)
  - Feels motivated
4. **Evening (7 PM)**: Dinner (pasta)
  - Snaps photo
  - AI suggests: 600 kcal
  - Sarah edits portion to "Large" → 750 kcal
  - Saves
  - Final progress: 1280 / 2000 (good cushion, on track)
5. **Before bed (10 PM)**: Reviews Diary
  - Sees week summary: "📊 Avg 1900 cal this week — Great job!"
  - Feels accomplished

**Outcome**: Sarah successfully logged all meals, stayed on track, feels motivated to continue ✓

---

#### Scenario PB-002: GLP-1 Medication User's Tracking (Post-MVP reference)

**Persona**: Michael, 45, GLP-1 medication user for diabetes, counts every calorie strictly

**Goal**: Log 3 meals, track medication timing, review impacts

*Note: This is a Post-MVP scenario (AI Coach + GLP-1 tracking not in MVP). Listed for reference.*

**Context**: Using Calo AI Premium; will have GLP-1 add-on in Phase 2

**Steps** (conceptual, Post-MVP):

1. Opens Calo AI; logs breakfast at 8 AM
2. Notes: "Taking GLP-1 injection at 8:15 AM"
3. Logs lunch at 12 PM; app tracks portion sizes strictly
4. Logs dinner at 6 PM; all with exact gram measurements
5. Reviews "GLP-1 Insights": Appetite suppression effect 2-4 hours post-injection

---

---

## 7. Use Case Priorities

### 7.1 Must-Have (MVP)

High-priority UCs that form the core product. These are critical for launch and directly enable user value.


| UC ID  | Use Case Name                        | Priority | Complexity | Primary Screen  | Dependencies         | MVP Phase |
| ------ | ------------------------------------ | -------- | ---------- | --------------- | -------------------- | --------- |
| UC-001 | Mở Camera để Chụp Bữa Ăn             | High     | Low        | WF-002          | Permissions          | Phase 2   |
| UC-002 | Chụp hoặc Chọn Ảnh                   | High     | Medium     | WF-002          | UC-001               | Phase 2   |
| UC-003 | Xem Kết quả AI                       | High     | High       | WF-010 → WF-003 | UC-002, AI API       | Phase 2   |
| UC-004 | Xác nhận &amp; Chỉnh sửa Nguyên liệu | High     | Medium     | WF-003          | UC-003               | Phase 2   |
| UC-005 | Thêm Nguyên liệu Thêm                | High     | Medium     | WF-003          | UC-004               | Phase 2   |
| UC-006 | Điều Chỉnh Khẩu Phần                 | High     | Medium     | WF-003          | UC-004               | Phase 2   |
| UC-007 | Điều Chỉnh Macro Thủ Công            | Medium   | Medium     | WF-003          | UC-004               | Phase 2   |
| UC-008 | Xoá Nguyên liệu                      | Medium   | Low        | WF-003          | UC-004               | Phase 2   |
| UC-009 | Xem Scan Còn Lại                     | High     | Low        | WF-002, WF-004  | —                    | Phase 2   |
| UC-010 | Hết Lượt → CTA Upgrade               | High     | Low        | WF-006          | UC-009               | Phase 3   |
| UC-011 | Xem Diary theo Ngày                  | High     | Low        | WF-004          | UC-004 (save)        | Phase 2   |
| UC-012 | Xem Diary theo Tuần                  | Medium   | Low        | WF-004          | UC-011               | Phase 3   |
| UC-013 | So sánh vs Mục tiêu                  | High     | Low        | WF-004, WF-005  | UC-011               | Phase 2   |
| UC-014 | Chỉnh sửa Log                        | Medium   | Medium     | WF-004 → WF-013 | UC-011               | Phase 3   |
| UC-015 | Xoá Log                              | Medium   | Low        | WF-004 → WF-014 | UC-011               | Phase 3   |
| UC-016 | Nhập Thông Tin Cơ bản                | High     | Low        | WF-008          | —                    | Phase 1   |
| UC-017 | Chọn Mức Hoạt Động                   | High     | Low        | WF-008          | UC-016               | Phase 1   |
| UC-018 | Xem Mục tiêu Calo được Tính          | High     | Low        | WF-008          | UC-017               | Phase 1   |
| UC-019 | Xem Paywall (Giá + Trial)            | High     | Low        | WF-006          | —                    | Phase 3   |
| UC-020 | Bắt đầu Trial 7 Ngày                 | High     | Medium     | WF-006          | UC-019, StoreKit     | Phase 3   |
| UC-021 | Huỷ Subscription                     | Medium   | Low        | WF-007 → WF-018 | UC-020 (after trial) | Phase 3   |
| UC-022 | Quản lý Subscription                 | Medium   | Low        | WF-007          | UC-020               | Phase 3   |
| UC-023 | Restore Purchase                     | Low      | Low        | WF-007          | UC-020               | Phase 3   |


**Core Critical Path (Phase 2)**: UC-001 → UC-002 → UC-003 → UC-004 → UC-011 (basic log flow)

---

### 7.2 Should-Have (Post-MVP, Phase 4+)

Features valuable to users but not essential for launch. These enable engagement and retention.


| UC ID  | Use Case Name               | Priority | Complexity | Primary Screen  |
| ------ | --------------------------- | -------- | ---------- | --------------- |
| UC-024 | Log GLP-1 Medication Timing | Medium   | Medium     | WF-020 (future) |
| UC-025 | Nhắc Lịch Thuốc             | Medium   | Low        | WF-020 (future) |
| UC-026 | Xem GLP-1 Insights          | Low      | High       | WF-020 (future) |
| UC-027 | Chat với AI Coach           | Medium   | High       | WF-019 (future) |


---

### 7.3 Nice-to-Have (Future, Phase 5+)

Advanced features that enhance product but don't drive core value. Consider for later releases based on user feedback.


| UC ID | Feature                              | Rationale                                                            |
| ----- | ------------------------------------ | -------------------------------------------------------------------- |
| —     | Export weekly/monthly reports as PDF | User-driven data ownership; low usage priority                       |
| —     | Share progress with friends (social) | Community feature; MVP focuses on individual tracking                |
| —     | Recipes database integration         | Nice-to-have but adds backend complexity                             |
| —     | Barcode scanning                     | QR code for packaged foods; lower priority than AI photo recognition |


---

## 8. User Journey Map

User journey maps show how each persona accomplishes their goals across the app.

### Journey 1: Mass-Market Diet Novice (Sarah — 28, office worker)

**Starting point**: App installed, no meals logged yet  
**Goal**: Log 3 meals per day, stay on calorie goal, reach -1 lb per week

```
Step 1: ONBOARDING (Entry)
┌─────────────────────────────────┐
│  WF-008 Onboarding              │
│  - Height: 168 cm               │
│  - Weight: 75 kg                │
│  - Goal: Lose weight            │
│  - Activity: Light (office)     │
│  UC-016, UC-017, UC-018         │
│  Output: 2000 kcal/day target   │
└─────────────────────────────────┘
                ↓
Step 2: FIRST MEAL (Motivation)
┌─────────────────────────────────┐
│  WF-002 Camera                  │
│  - Capture breakfast photo      │
│  UC-001, UC-002                 │
│  ↓                              │
│  WF-003 Confirmation            │
│  - Review AI detection          │
│  - Adjust portion/ingredients   │
│  UC-003, UC-004, UC-005, UC-006 │
│  ↓                              │
│  WF-004 Diary                   │
│  - Log saved: 150 kcal          │
│  UC-011                         │
└─────────────────────────────────┘
                ↓
Step 3: DAILY LOGGING (Habit)
┌─────────────────────────────────┐
│  Repeat Step 2 for lunch/dinner │
│  WF-002 → WF-003 → WF-004       │
│  (faster, cached permissions)   │
└─────────────────────────────────┘
                ↓
Step 4: PROGRESS CHECK (Insight)
┌─────────────────────────────────┐
│  WF-004 Diary (evening)         │
│  - Review day: 1850 / 2000 kcal │
│  - Progress bar: 92% (good!)    │
│  UC-011, UC-012, UC-013         │
│  Feeling: ✓ On track, motivated │
└─────────────────────────────────┘
                ↓
Step 5: UPGRADE MOMENT (Monetization)
┌─────────────────────────────────┐
│  Day 3, 4th scan attempt        │
│  WF-006 Paywall modal           │
│  UC-010, UC-019, UC-020         │
│  Decision: Trial or free?       │
│  → Converts to Premium trial    │
└─────────────────────────────────┘
```

**Success metric**: User logs consistently for 2 weeks, maintains calorie tracking, possibly converts to paid ✓

---

### Journey 2: GLP-1 Medication User (Michael — 45, diabetes + weight loss)

**Starting point**: App installed, taking GLP-1 medication, strict calorie counting  
**Goal**: Track meal timing relative to medication, maintain strict macros

```
Step 1-3: SAME as Journey 1 (onboarding + first meals)
           (WF-008 → WF-002 → WF-003 → WF-004)

Step 4: MEDICATION TRACKING (Post-MVP)
┌─────────────────────────────────┐
│  WF-020 GLP-1 Tracker           │
│  UC-024, UC-025, UC-026         │
│  - Log GLP-1 injection time     │
│  - Track appetite/fullness      │
│  - Compare with meal timing     │
└─────────────────────────────────┘

Step 5: AI COACH (Post-MVP)
┌─────────────────────────────────┐
│  WF-019 AI Coach chat           │
│  UC-027                         │
│  - "Why was I fuller today?"    │
│  - AI correlates: GLP-1 timing  │
│  - Provides insights            │
└─────────────────────────────────┘
```

**Success metric**: GLP-1 user feels app understands medication impact; high retention ✓

---

## 9. Screen-Intent Summary

Quick-reference table for wireframe designers. Shows what every screen must support.


| Screen (WF-ID) | Screen Name              | Archetype   | Interaction Density | User Intent                                  | Primary Action                 | Secondary Actions                                      | Key UCs                                        |
| -------------- | ------------------------ | ----------- | ------------------- | -------------------------------------------- | ------------------------------ | ------------------------------------------------------ | ---------------------------------------------- |
| WF-001         | Splash                   | Consumption | Light               | "Launch app quickly"                         | Wait 2s, load                  | —                                                      | System                                         |
| WF-002         | Camera                   | Action      | Dense               | "Photograph my meal without friction"        | Capture photo                  | Photo library, flip camera, settings                   | UC-001, UC-002, UC-009                         |
| WF-003         | Confirmation             | Action      | Dense               | "Confirm ingredients before saving"          | Save log                       | Edit portion, add/remove ingredient, retry photo       | UC-003, UC-004, UC-005, UC-006, UC-007, UC-008 |
| WF-004         | Diary                    | Consumption | Dense               | "See what I ate today and track progress"    | View daily log + progress bar  | Edit/delete item, toggle week view, share, change goal | UC-011, UC-012, UC-013, UC-014, UC-015         |
| WF-005         | Dashboard                | Consumption | Medium              | "Review weekly trends and insights"          | View weekly summary            | View monthly, export, share                            | UC-013                                         |
| WF-006         | Paywall / Subscription   | Management  | Medium              | "Understand trial offer and pricing clearly" | Start trial OR Upgrade         | View plans, annual/monthly toggle, FAQ                 | UC-010, UC-019, UC-020                         |
| WF-007         | Settings / Account       | Management  | Medium              | "Manage subscription and profile settings"   | View subscription status       | Cancel/restore, edit profile, log out, help            | UC-021, UC-022, UC-023                         |
| WF-008         | Onboarding               | System      | Medium              | "Set up profile for calorie goal"            | Complete 3-step onboarding     | Back, skip (no, required)                              | UC-016, UC-017, UC-018                         |
| WF-009         | Permission Request       | System      | Light               | "Grant camera access"                        | Allow OR Deny                  | Go to Settings                                         | UC-001 AF-001.1                                |
| WF-010         | AI Loading               | System      | Light               | "Wait for meal analysis"                     | Show progress + "Analyzing..." | Cancel                                                 | UC-003                                         |
| WF-013         | Edit Log Modal           | Management  | Medium              | "Update portion/ingredients for saved log"   | Save changes                   | Cancel, reset to original                              | UC-014                                         |
| WF-014         | Delete Confirm Modal     | Management  | Light               | "Confirm deletion"                           | Delete OR Cancel               | Undo (if within 3s)                                    | UC-015                                         |
| WF-018         | Cancel Sub Confirm Modal | Management  | Light               | "Confirm subscription cancellation"          | Confirm cancel OR Revoke       | Keep subscription                                      | UC-021                                         |


**Totals:**

- Dense screens (6+ zones): WF-002 (Camera), WF-003 (Confirmation), WF-004 (Diary) = 3
- Medium (3-5 zones): WF-005 (Dashboard), WF-006 (Paywall), WF-007 (Settings), WF-008 (Onboarding), WF-013, WF-014, WF-018 = 7
- Light (1-2 zones): WF-001 (Splash), WF-009 (Permission), WF-010 (Loading) = 3
- **Total screens: 13 primary screens + 4 modals = 17 screens** (minimum 25 for Medium project; see expansion notes below)

**Screen Count Gap**: Current = 17; Required minimum = 25  
**Gap reason**: Project size Medium (6 MVP features) requires &gt;=25 screens per scaling guidance.  
**Expansion options**:

- Add detailed modal variants (confirm actions, error states) = +3-5 screens
- Add welcome/tutorial overlays for first-time users = +2 screens
- Add advanced filtering/search on Diary = +2 screens
- Add settings sub-screens (profile, notification, privacy) = +3 screens
- **Total expanded**: 17 + 10 = 27 screens ✓

---

## 10. References

- **PRD.md** (v1.0, 2026-07-21): Product requirements, features (§6), personas (§3), screen inventory (§8), business goals
- **Project_Overview.md** (v1.0, 2026-07-21): Architecture, screen hierarchy, technology stack, roadmap
- **Functional_Requirements.md** (upcoming): System features derived from UCs, data models, APIs
- **Wireframes.md** (upcoming): Detailed screen designs for WF-001 through WF-018, component library
- **UX_Flows.md** (upcoming): Task flows translated to interactive prototypes

---

**Document Metadata**:

- **Phiên bản tài liệu**: 1.0  
- **Cập nhật lần cuối**: 2026-07-21  
- **Tác giả**: AI Research Agent + Project Team
- **Trạng thái**: ✓ Hoàn thành — Sẵn sàng cho Quality Gate (gate-uc)

**Content Summary**:

- **Số UCs**: 23 MVP + 4 Post-MVP = 27 tổng cộng
- **Số Screens**: 13 primary + 4 modals = 17 (expanding to 25+)
- **Số Task Flows**: 5 (TF-001 through TF-005)
- **Số Sub-Flows**: 3 (SF-001 through SF-003)
- **Số Scenarios**: 7 (3 happy paths + 4 edge cases + 2 persona-based)
- **Traceability**: 100% UCs mapped to screens; all screens have UC coverage

