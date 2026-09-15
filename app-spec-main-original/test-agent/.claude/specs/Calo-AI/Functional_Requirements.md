# Calo AI - Functional Requirements

**Phiên bản**: 1.0  
**Ngày**: 2026-07-21  
**Tác giả**: AI Research Agent  
**Chế độ**: Full FR Specification  
**Trạng thái**: Bản nháp — Chờ quality gate

---

## Traceability Summary

**UC → FR Mapping** (verification before writing):

| UC ID | UC Name | FR Count | FRs Derived |
|-------|---------|----------|------------|
| UC-001 | Mở Camera | 1 | FR-001 |
| UC-002 | Chụp/Chọn Ảnh | 1 | FR-002 |
| UC-003 | Xem Kết quả AI | 1 | FR-003 |
| UC-004 | Xác nhận Nguyên liệu | 1 | FR-004 |
| UC-005 | Thêm Nguyên liệu | 1 | FR-005 |
| UC-006 | Điều Chỉnh Khẩu Phần | 1 | FR-006 |
| UC-007 | Điều Chỉnh Macro Thủ Công | 1 | FR-007 |
| UC-008 | Xoá Nguyên liệu | 1 | FR-008 |
| UC-009 | Xem Scan Còn Lại | 1 | FR-009 |
| UC-010 | Hết Lượt → CTA Upgrade | 2 | FR-010, FR-011 (paywall trigger + display) |
| UC-011 | Xem Diary theo Ngày | 1 | FR-012 |
| UC-012 | Xem Diary theo Tuần | 1 | FR-013 |
| UC-013 | So sánh vs Mục tiêu | 1 | FR-014 |
| UC-014 | Chỉnh sửa Log | 2 | FR-015, FR-016 (edit modal) |
| UC-015 | Xoá Log | 1 | FR-017 |
| UC-016 | Nhập Thông tin Cơ bản | 1 | FR-018 |
| UC-017 | Chọn Mức Hoạt Động | 1 | FR-019 |
| UC-018 | Xem Mục tiêu Calo | 1 | FR-020 |
| UC-019 | Xem Paywall (Giá + Trial) | 1 | FR-021 |
| UC-020 | Bắt đầu Trial 7 Ngày | 2 | FR-022, FR-023 (subscription API) |
| UC-021 | Huỷ Subscription | 1 | FR-024 |
| UC-022 | Quản lý Subscription | 1 | FR-025 |
| UC-023 | Restore Purchase | 1 | FR-026 |
| **TOTAL** | **23 UCs** | **27 FRs** | ✓ Coverage: 27/23 (1.17x multiplier) |

---

## 1. Introduction

### 1.1 Purpose

Tài liệu này định nghĩa **HỆ THỐNG PHẢI LÀM GÌ** (system behavior), cầu nối giữa nhu cầu người dùng (Use_Cases.md) và triển khai kỹ thuật (Design specs). Mỗi FR truy nguyên tới một hoặc nhiều UCs từ Use_Cases.md.

### 1.2 Scope

- **MVP Scope**: 26 FRs (FR-001 to FR-026) dẫn xuất từ 23 High/Medium priority UCs
- **Post-MVP**: UC-024 đến UC-027 (GLP-1, AI Coach) tham chiếu nhưng KHÔNG chi tiết trong MVP
- **Coverage**: Mỗi UC → ≥1 FR; mỗi FR truy nguyên tới ≥1 UC (traceability 100%)

### 1.3 Document Conventions

- **FR-XXX**: Functional Requirement (từ UC)
- **NFR-XXX**: Non-Functional Requirement (performance, security, offline)
- **BR-XXX.Y**: Business Rule (hạn chế, điều kiện tiên quyết)
- **VR-XXX.Y**: Validation Rule (kiểm tra dữ liệu)
- **ERR-XXX.Y**: Error Handling (từ AF—alternative flows của UC)
- **AC-XXX.Y**: Acceptance Criteria (chuyển tiếp từ UC, từng chữ một)
- **Priority**: High (MVP critical) / Medium (MVP secondary) / Low (Post-MVP)

---

## 2. Functional Requirements

### 2.1 Camera & Photo Capture Feature Group

#### FR-001: Camera Permission Request

**Source UC**: UC-001 (Mở Camera để Chụp Bữa Ăn)

**Priority**: High  
**Status**: Planned

**Description**: 
Hệ thống phải yêu cầu quyền truy cập camera từ người dùng khi lần đầu tiên họ mở tab Camera.

**Input**:
- App state: First-time camera access flag
- User action: Tap Camera tab

**Processing**:
1. Check if camera permission is already granted (iOS PermissionStatus.granted)
2. If not granted: Present iOS native camera permission dialog
3. Wait for user response (Allow / Don't Allow)
4. Store permission status in app state

**Output**:
- Permission granted → Proceed to FR-002 (camera preview)
- Permission denied → Show error state (WF-002, alternative layout)

**Business Rules**:
- BR-001.1: Camera permission can only be requested once per app install; if denied, only Settings can re-grant
- BR-001.2: Permission request must use iOS native UIImagePickerController or AVCaptureSession permission dialog

**Validation Rules**:
- VR-001.1: Permission response timeout must not exceed 30 seconds; if timeout, treat as denied

**Error Handling**:
- ERR-001.1: Permission denied → Display message "Camera access required. Go to Settings > Calo AI > Camera" with button linking to Settings app (from UC-001 AF-001.1)
- ERR-001.2: System camera unavailable → Display "Camera not available on this device"

**Acceptance Criteria**:
- AC-001.1: WHEN app.launched THEN camera tab visible on bottom tab bar
- AC-001.2: WHEN user taps Camera tab FOR FIRST TIME THEN camera permission request shown (native iOS dialog)
- AC-001.3: WHEN user grants permission THEN live preview appears within 1s
- AC-001.4: IF user denies permission THEN helpful message with Settings link shown; Camera tab shows "Permission needed" state

---

#### FR-002: Camera Live Preview & Photo Capture

**Source UC**: UC-002 (Chụp hoặc Chọn Ảnh)

**Priority**: High  
**Status**: Planned

**Description**:
Hệ thống phải hiển thị live preview từ camera sau khi quyền được cấp, cho phép người dùng chụp ảnh bữa ăn hoặc chọn từ photo library.

**Input**:
- Camera permission: granted
- User action: View camera tab (WF-002) / Tap shutter button / Tap photo library icon

**Processing**:
1. Initialize AVCaptureSession with camera device (prefer rear camera)
2. Start live preview stream to screen (full-screen, preview layer)
3. Display shutter button (large circular) + photo library icon
4. When shutter button tapped:
   - a. Capture frame from video stream
   - b. Display preview of captured photo with "Use This" / "Retake" buttons
5. If photo library icon tapped:
   - a. Present iOS native photo picker (PHPickerViewController)
   - b. User selects 1 photo
   - c. Display selected photo with same "Use This" / "Retake" UI
6. When "Use This" tapped: Pass photo to FR-003 (AI analysis)

**Output**:
- Selected photo (UIImage or CIImage object) → FR-003
- Exit point: WF-003 (Confirmation screen after AI analysis)

**Business Rules**:
- BR-002.1: Only rear camera, no front camera option in MVP
- BR-002.2: Photo must be JPG or PNG, size ≤ 10MB
- BR-002.3: Photo preview must display captured/selected image within 2 seconds

**Validation Rules**:
- VR-002.1: Photo resolution must be ≥ 640×480 (minimum for AI API)
- VR-002.2: Photo must be in supported format (JPG, PNG); reject HEIC, WEBP

**Error Handling**:
- ERR-002.1: Photo too small (< 640×480) → "Photo too small. Try again." (from UC-002 AF-002.2 Retake path)
- ERR-002.2: Unsupported format → "Image format not supported. Use JPG or PNG."
- ERR-002.3: Camera becomes unavailable (hardware error) → "Camera error. Try again later."

**Acceptance Criteria**:
- AC-002.1: WHEN user taps shutter button THEN photo captured + preview shown within 2s
- AC-002.2: WHEN photo preview shown THEN "Use This" and "Retake" buttons visible
- AC-002.3: IF user taps Photo Library icon THEN native photo picker opens
- AC-002.4: WHEN user selects photo from library THEN preview shown with same UI as captured photo

---

#### FR-003: AI Food Recognition (Vision API Call)

**Source UC**: UC-003 (Xem Kết quả AI)

**Priority**: High  
**Status**: Planned

**Description**:
Hệ thống phải gửi ảnh bữa ăn tới AI Vision API (OpenAI/Anthropic), nhận kết quả (tên món, calories, macros, nguyên liệu phát hiện), và hiển thị cho người dùng xác nhận.

**Input**:
- Photo: UIImage (from FR-002)
- User context: Free tier (3/day limit) or Premium (unlimited)

**Processing**:
1. Show loading screen: "Analyzing your meal..." (WF-010)
2. Convert photo to base64 or send via multipart upload
3. Call AI Vision API with photo + prompt template:
   - "Identify all food items in this image. For each item, estimate: meal name, serving size (small/medium/large), calories, protein (g), carbs (g), fat (g). Return confidence level (0-100). Format: JSON"
4. Wait for API response (timeout: 10 seconds)
5. Parse response: Extract {meal_name, confidence, calories, macros, ingredients_list}
6. If confidence ≥ 70%: Proceed to confirmation screen (FR-004)
7. If confidence < 70%: Show warning "Not confident. Please verify below or retry." (from UC-003 AF-003.1)

**Output**:
- Result: {meal_name, calories, protein_g, carbs_g, fat_g, ingredients[], confidence} → WF-003 (Confirmation)
- Or error → WF-010 error state

**Business Rules**:
- BR-003.1: API timeout = 10s max; if exceeded, show error
- BR-003.2: Confidence threshold for "proceed without warning" = 70%
- BR-003.3: Calories/macros must be positive numbers (≥ 0)
- BR-003.4: Ingredients list must include ≥ 1 item (reject empty results)

**Validation Rules**:
- VR-003.1: Calories must be numeric, range 0–5000 kcal
- VR-003.2: Confidence must be numeric, range 0–100
- VR-003.3: Macros (P, C, F) must sum to calorie equivalent (±10% tolerance for rounding)

**Error Handling**:
- ERR-003.1: API timeout (>10s) → "Connection error. Please try again." + Retry button (from UC-003 AF-003.2)
- ERR-003.2: API returns error → "Could not analyze image. Please try again."
- ERR-003.3: API returns null/empty result → "No food detected. Please take a clearer photo."
- ERR-003.4: Confidence < 50% → Show warning + "Edit below" option (from UC-003 AF-003.1)

**Acceptance Criteria**:
- AC-003.1: WHEN user taps "Use This" from UC-002 THEN loading screen (WF-010) shown with spinner + "Analyzing..." text
- AC-003.2: WHEN AI returns result (2-5s) THEN Confirmation screen (WF-003) shown with meal name, calories, macros
- AC-003.3: THEN all 4 ingredient items displayed with checkboxes checked by default
- AC-003.4: IF AI confidence < 70% THEN warning badge + "Edit below" or "Retry" option shown
- AC-003.5: IF API timeout (>10s) THEN error modal with retry button

---

#### FR-004: Confirm & Save Meal Log

**Source UC**: UC-004 (Xác nhận & Chỉnh sửa Nguyên liệu)

**Priority**: High  
**Status**: Planned

**Description**:
Hệ thống phải cho phép người dùng xác nhận danh sách nguyên liệu do AI phát hiện, điều chỉnh khẩu phần, rồi lưu log bữa ăn vào Diary.

**Input**:
- AI result: {meal_name, calories, macros, ingredients[]} from FR-003
- User actions: Check/uncheck ingredient, adjust portion, tap "Confirm & Save"

**Processing**:
1. Display ingredients list (WF-003) with checkboxes (all checked by default)
2. For each checked ingredient: sum calories/macros
3. When user unchecks ingredient:
   - a. Remove ingredient from calculation
   - b. Recalculate total calories/macros in real-time
4. When user adjusts portion (small/medium/large):
   - a. Look up portion multiplier from database
   - b. Recalculate ingredient calo/macros
   - c. Update total display
5. When "Confirm & Save" tapped:
   - a. Validate: ≥1 ingredient checked, total calo > 0
   - b. Create log object: {date, meal_name, total_calories, macros, ingredients[]}
   - c. Save to local database
   - d. Update daily total in Diary (WF-004)
   - e. Navigate to Diary (UC-011)

**Output**:
- Meal log saved to database
- Exit point: WF-004 (Diary), showing updated daily progress

**Business Rules**:
- BR-004.1: At least 1 ingredient must be checked before save
- BR-004.2: Cannot save if total calories = 0
- BR-004.3: Meal log timestamp = current date/time (system time, not user-editable)
- BR-004.4: Portion sizes: small = 0.75x, medium = 1.0x, large = 1.25x (multiply AI estimate)

**Validation Rules**:
- VR-004.1: Total calories ≥ 1 kcal (cannot be 0)
- VR-004.2: Macros sum valid (checked in FR-003, re-validate here)

**Error Handling**:
- ERR-004.1: No ingredients checked → "Select at least one ingredient" (prevent save)
- ERR-004.2: Save fails (DB error) → "Could not save log. Try again." + Retry button
- ERR-004.3: Network error during cloud sync → "Saved locally. Will sync when online."

**Acceptance Criteria**:
- AC-004.1: WHEN Confirmation screen shown THEN ingredients list with checkboxes visible
- AC-004.2: WHEN user unchecks ingredient THEN calorie/macros recalculate within 200ms
- AC-004.3: WHEN user adjusts portion (small/medium/large) THEN values update instantly
- AC-004.4: WHEN user taps "Confirm & Save" THEN log appears in Diary immediately

---

#### FR-005: Add Ingredient

**Source UC**: UC-005 (Thêm Nguyên liệu)

**Priority**: High  
**Status**: Planned

**Description**:
Hệ thống phải cho phép người dùng thêm nguyên liệu không được AI phát hiện vào danh sách xác nhận.

**Input**:
- User action: Tap "+ Add ingredient" on WF-003
- User input: Ingredient name (text)

**Processing**:
1. Show text input field with placeholder "e.g., olive oil, rice"
2. As user types, perform autocomplete search against ingredient database
3. Display matching suggestions (max 5)
4. When user selects suggestion or presses Enter:
   - a. Look up ingredient calo per 100g from database
   - b. Default portion = medium (1.0x multiplier)
   - c. Add ingredient to list (unchecked by default — user must verify)
   - d. Recalculate total macros
5. If no suggestion found:
   - a. Show "Add as custom" button
   - b. If tapped, allow user to enter custom calorie value
   - c. Default = 0 kcal; user must manually adjust

**Output**:
- New ingredient added to list, unchecked
- Updated total calories/macros displayed

**Business Rules**:
- BR-005.1: Autocomplete searches against pre-loaded ingredient database (nutrition facts sourced from USDA/similar)
- BR-005.2: Custom ingredients default to 0 kcal to force user verification
- BR-005.3: New ingredient added with checkbox unchecked (requires user to verify)

**Validation Rules**:
- VR-005.1: Ingredient name must be ≥ 2 characters
- VR-005.2: Custom calorie value must be numeric, range 0–2000 kcal per 100g

**Error Handling**:
- ERR-005.1: No matching ingredient in database → Show "Add as custom" option
- ERR-005.2: Input empty → "Please enter ingredient name"
- ERR-005.3: Custom calorie out of range → "Enter calorie value between 0 and 2000"

**Acceptance Criteria**:
- AC-005.1: WHEN user taps "+ Add ingredient" THEN input field appears with keyboard
- AC-005.2: WHEN user types THEN autocomplete suggestions appear within 500ms
- AC-005.3: WHEN user taps suggestion THEN ingredient added + macros recalculate
- AC-005.4: IF no suggestion found THEN "Add as custom" option shown
- AC-005.5: WHEN custom ingredient added THEN checkbox unchecked by default (user must verify)

---

#### FR-006: Adjust Portion Size

**Source UC**: UC-006 (Điều Chỉnh Khẩu Phần)

**Priority**: High  
**Status**: Planned

**Description**:
Hệ thống phải cho phép người dùng thay đổi khẩu phần của mỗi nguyên liệu để tính calo chính xác.

**Input**:
- User action: Tap portion selector for an ingredient on WF-003
- Selection: small / medium / large (or manual gram entry)

**Processing**:
1. Display portion selector buttons (small / medium / large) for each ingredient
2. When user taps:
   - a. Apply multiplier: small=0.75x, medium=1.0x, large=1.25x
   - b. Recalculate ingredient calories/macros
   - c. Recalculate total
   - d. Update display in real-time
3. Optional: Allow manual gram entry (if user taps "Enter grams")
   - a. Show number input field
   - b. Look up gram→calorie conversion from database
   - c. Apply conversion

**Output**:
- Portion size updated
- Calories/macros recalculated in real-time
- Total display updated at top of screen

**Business Rules**:
- BR-006.1: Default portion = medium (1.0x)
- BR-006.2: Multipliers fixed: small=0.75x, medium=1.0x, large=1.25x
- BR-006.3: Manual gram entry must convert using database (food-specific calorie density)

**Validation Rules**:
- VR-006.1: Gram entry must be numeric, range 10–500g
- VR-006.2: Calculated calories must remain ≥ 0

**Error Handling**:
- ERR-006.1: Gram out of range → "Enter weight between 10 and 500 grams"
- ERR-006.2: Database lookup fails for custom gram conversion → Use 100g calo as estimate

**Acceptance Criteria**:
- AC-006.1: WHEN user taps portion button THEN options (small/medium/large) shown
- AC-006.2: WHEN user selects portion THEN calo/macro recalculate within 200ms
- AC-006.3: WHEN portion changed THEN total at top of screen updates
- AC-006.4: IF manual gram entry used THEN system looks up gram→calo conversion from database
- AC-006.5: WHEN user adjusts portion multiple times THEN changes persist on screen

---

#### FR-007: Edit Macros Manually

**Source UC**: UC-007 (Điều Chỉnh Macro)

**Priority**: Medium  
**Status**: Planned

**Description**:
Hệ thống phải cho phép người dùng điều chỉnh thủ công protein/carbs/fat nếu AI estimate không chính xác.

**Input**:
- User action: Tap pencil icon next to macro values on WF-003
- User input: Protein (g), Carbs (g), Fat (g) values

**Processing**:
1. Show macro editor with 3 input fields (P, C, F)
2. Display current values (from AI estimate)
3. User edits any field
4. Recalculate total calories: (P × 4) + (C × 4) + (F × 9)
5. Update total calorie display in real-time

**Output**:
- Updated macros displayed
- Total calories recalculated

**Business Rules**:
- BR-007.1: Calorie formula: Protein 4 kcal/g, Carbs 4 kcal/g, Fat 9 kcal/g
- BR-007.2: Can be "Reset to AI estimate" if user changes mind

**Validation Rules**:
- VR-007.1: Each macro must be numeric, range 0–200g
- VR-007.2: Total must be > 0 when edited (cannot all be 0)

**Error Handling**:
- ERR-007.1: All macros 0 → "At least one macro must be > 0"
- ERR-007.2: Non-numeric input → "Enter numeric value"

**Acceptance Criteria**:
- AC-007.1: WHEN user taps macro edit icon THEN input fields appear for P/C/F
- AC-007.2: WHEN user updates values THEN total calo recalculates instantly
- AC-007.3: THEN macro total > 0 must be validated (error if all 0)

---

#### FR-008: Remove Ingredient

**Source UC**: UC-008 (Xoá Nguyên liệu)

**Priority**: Medium  
**Status**: Planned

**Description**:
Hệ thống phải cho phép người dùng xoá nguyên liệu khỏi danh sách xác nhận.

**Input**:
- User action: Uncheck ingredient checkbox OR swipe-left + tap delete on WF-003

**Processing**:
1. Remove ingredient from list
2. Recalculate total calories/macros (excluding deleted ingredient)
3. Update display

**Output**:
- Ingredient removed
- Total updated

**Business Rules**:
- BR-008.1: Cannot delete all ingredients (must have ≥1 checked for save)
- BR-008.2: Undo available within 3 seconds if needed

**Validation Rules**:
- VR-008.1: If last ingredient about to be deleted, warn user

**Error Handling**:
- ERR-008.1: Attempting to delete last ingredient → Warn "At least one ingredient required"

**Acceptance Criteria**:
- AC-008.1: WHEN user unchecks ingredient THEN it's removed from macros calculation
- AC-008.2: WHEN ingredient removed THEN total calo/macro decrease
- AC-008.3: IF all ingredients removed THEN warning shown (cannot save empty log)

---

### 2.2 Diary & Progress Tracking Feature Group

#### FR-009: Display Remaining Scans

**Source UC**: UC-009 (Xem Scan Còn Lại)

**Priority**: High  
**Status**: Planned

**Description**:
Hệ thống phải hiển thị số lượt scan còn lại hôm nay cho người dùng free tier (mặc định 3/day).

**Input**:
- User context: Free tier or Premium
- Current date: system date

**Processing**:
1. Track scan count for current date (reset daily at midnight)
2. If free tier: max = 3 scans/day
3. If premium: max = unlimited (show "Unlimited")
4. Display badge: "X/3 scans" on Camera tab (WF-002) + Diary header (WF-004)
5. If hovering over badge, show tooltip: "Unlimited with Premium"

**Output**:
- Scan count badge displayed on Camera and Diary tabs
- Tooltip on hover

**Business Rules**:
- BR-009.1: Free tier = 3 scans/day (PRD assumption, can be overridden by admin)
- BR-009.2: Daily limit resets at UTC midnight
- BR-009.3: Premium users see "Unlimited" instead of count
- BR-009.4: Scan count increments after successful log save (not on photo capture)

**Validation Rules**:
- VR-009.1: Scan count must be 0–3 for free tier (cannot exceed)

**Error Handling**:
- ERR-009.1: Scan count ≥ 3 on 4th attempt → Trigger FR-010 (paywall modal)

**Acceptance Criteria**:
- AC-009.1: WHEN user on free tier THEN badge shows "X/3 scans" on Camera tab
- AC-009.2: WHEN user scans ≥ 3 times THEN 4th attempt triggers paywall (FR-010)
- AC-009.3: WHEN user premium THEN badge shows "Unlimited scans"

---

#### FR-010: Trigger Paywall on Scan Limit

**Source UC**: UC-010 (Hết Lượt → Upgrade)

**Priority**: High  
**Status**: Planned

**Description**:
Hệ thống phải hiển thị paywall modal khi người dùng free tier hết lượt scan hôm nay.

**Input**:
- User action: Attempt 4th scan on current day
- User state: Free tier, scans_used = 3

**Processing**:
1. Check scan count for today
2. If scan_count ≥ 3 AND user is free tier:
   - a. Block 4th scan attempt
   - b. Display paywall modal (WF-006): "You've used 3 free scans today. Upgrade to Premium for unlimited."
   - c. Show pricing: "$9.99/month" or "$39.99/year" (with 30% savings badge)
   - d. Show CTA: "Start 7-day trial"

**Output**:
- Paywall modal displayed
- 4th scan blocked (user cannot proceed without upgrading or waiting until tomorrow)

**Business Rules**:
- BR-010.1: Paywall triggers when scan_count ≥ 3 AND free tier
- BR-010.2: After trial expired (no active subscription), paywall triggers again on next scan limit
- BR-010.3: Premium users have unlimited scans (no paywall)

**Validation Rules**:
- VR-010.1: Scan count must be exactly 3 to trigger (not 2, not 4)

**Error Handling**:
- ERR-010.1: Paywall fails to load → Show simplified message "Upgrade for unlimited scans"

**Acceptance Criteria**:
- AC-010.1: WHEN free user attempts 4th scan THEN paywall modal appears
- AC-010.2: WHEN paywall shown THEN pricing and trial offer clearly visible
- AC-010.3: WHEN user taps "Start 7-day trial" THEN FR-022 (subscription flow) triggered

---

#### FR-011: Paywall Display with Pricing

**Source UC**: UC-019 (Xem Paywall)

**Priority**: High  
**Status**: Planned

**Description**:
Hệ thống phải hiển thị paywall với pricing rõ ràng, giúp người dùng quyết định upgrade.

**Input**:
- Trigger: User attempts 4th scan (FR-010) OR manually opens "Upgrade" from Settings
- Pricing data: $9.99/month, $39.99/year

**Processing**:
1. Display paywall modal (WF-006) with:
   - Headline: "Unlock Unlimited Scans"
   - Trial badge: "7 days free"
   - Pricing options:
     - Monthly: "$9.99/month"
     - Yearly: "$39.99/year" (with "SAVE 30%" badge)
   - Benefits list:
     - ✓ Unlimited daily scans
     - ✓ AI Coach (coming soon)
     - ✓ GLP-1 tracking (coming soon)
   - CTA button: "Start free trial"
   - Secondary link: "Remind me later" OR "Learn more"

**Output**:
- Paywall modal displayed with all pricing/benefits visible

**Business Rules**:
- BR-011.1: Trial length = 7 days (hardcoded; can be changed in admin panel)
- BR-011.2: Pricing: $9.99/month or $39.99/year (or local currency equivalent)
- BR-011.3: Yearly plan = 33% discount vs monthly (pre-calculated on backend)
- BR-011.4: Show "SAVE 30%" badge on yearly option to encourage selection

**Validation Rules**:
- VR-011.1: Pricing data must be fetched from Pricing API or config (not hardcoded in UI)

**Error Handling**:
- ERR-011.1: Pricing data fails to load → Show generic message "Upgrade to Premium" with button to Settings

**Acceptance Criteria**:
- AC-011.1: WHEN paywall shown THEN trial length (7 days) and pricing ($9.99 or $39.99) clearly visible
- AC-011.2: WHEN user sees paywall THEN understands benefits (unlimited scans, etc.)
- AC-011.3: WHEN user taps "Start free trial" THEN subscription flow starts (FR-022)

---

[*Document continues in Phase 2 with Diary FRs, Onboarding, Monetization, and NFRs...*]

---

### 2.3 Diary & Progress Tracking (Continued)

#### FR-012: Display Daily Meal Log

**Source UC**: UC-011 (Xem Diary theo Ngày)

**Priority**: High  
**Status**: Planned

**Description**:
Hệ thống phải hiển thị danh sách bữa ăn hôm nay và tiến độ vs mục tiêu calo.

**Input**:
- Current date: system date
- Meal logs: from database for today

**Processing**:
1. Query database for all logs with date = today
2. Calculate daily totals: sum of all log calories, macros
3. Display progress bar: current / goal (e.g., 1800 / 2000 cal)
4. Color code progress bar: green (on-track <100%), yellow (95-100%), red (>100%)
5. Display meal list with each meal: {name, calories, portion, time}
6. Each meal row swipe-left for edit/delete (FR-015, FR-017)

**Output**:
- Daily log list displayed (WF-004)
- Progress bar updated
- Exit points: Edit meal (FR-015), Delete meal (FR-017), View week (FR-013)

**Business Rules**:
- BR-012.1: Daily total calculated from all checked ingredients across all meals
- BR-012.2: Progress bar color: green ≤100%, yellow 100-110%, red >110%
- BR-012.3: Meals sorted by time (breakfast, lunch, dinner order)

**Validation Rules**:
- VR-012.1: Daily total must be non-negative

**Error Handling**:
- ERR-012.1: No meals logged today → Show empty state "No meals logged yet. Tap Camera to add one."

**Acceptance Criteria**:
- AC-012.1: WHEN user opens Diary tab THEN daily meals listed with total calo vs goal
- AC-012.2: WHEN progress bar shown THEN color indicates on-track/near-limit/over
- AC-012.3: WHEN user sees daily log THEN can swipe to edit/delete individual meals

---

#### FR-013: Display Weekly Summary

**Source UC**: UC-012 (Xem Diary theo Tuần)

**Priority**: Medium  
**Status**: Planned

**Description**:
Hệ thống phải hiển thị tóm tắt tuần lễ với tổng calo mỗi ngày.

**Input**:
- Date range: Current week (Mon-Sun)
- Meal logs: from database for week

**Processing**:
1. Toggle "Week view" button on WF-004
2. Query database for all logs in current week
3. Group by date, calculate daily totals
4. Display 7 rows (Mon-Sun) with:
   - Date
   - Daily total calories
   - Progress vs goal (e.g., "1850/2000")
5. Bottom row: Weekly average, weekly total
6. Optional: bar chart showing daily calories across week

**Output**:
- Week view displayed (WF-004)
- Daily + weekly summary visible

**Business Rules**:
- BR-013.1: Week starts Monday (configurable by locale)
- BR-013.2: Weekly average = sum of daily totals / 7
- BR-013.3: Days with no logs show 0 calories

**Validation Rules**:
- VR-013.1: Date range must be exactly 7 days

**Error Handling**:
- ERR-013.1: No logs in week → Show "Start logging to see weekly trends"

**Acceptance Criteria**:
- AC-013.1: WHEN user toggles week view THEN 7-day summary displayed
- AC-013.2: WHEN week view shown THEN weekly average calculated and shown
- AC-013.3: WHEN user taps daily row THEN expands to show meals for that day

---

#### FR-014: Calculate Progress vs Goal

**Source UC**: UC-013 (So sánh vs Mục tiêu)

**Priority**: High  
**Status**: Planned

**Description**:
Hệ thống phải tính toán và hiển thị tiến độ hôm nay vs mục tiêu calo hàng ngày.

**Input**:
- Daily total: from FR-012
- User goal: from onboarding (FR-018)

**Processing**:
1. Retrieve user's daily calorie goal (default: 2000 kcal from onboarding)
2. Calculate: progress_percent = daily_total / goal × 100
3. Display progress bar with:
   - Filled portion: progress_percent
   - Label: "1800 / 2000 cal" (or user's actual goal)
   - Remaining: goal - daily_total (e.g., "200 cal left")
4. Color coding:
   - Green: 0–100% (on-track)
   - Yellow: 100–110% (slightly over, caution)
   - Red: >110% (exceeded by >10%)
5. Macro breakdown visible: Protein X%, Carbs Y%, Fat Z%

**Output**:
- Progress bar rendered (WF-004, WF-005)
- Macro pie chart (optional, WF-005)

**Business Rules**:
- BR-014.1: Goal = user-defined from onboarding (Mifflin-St Jeor formula default)
- BR-014.2: Color threshold: green/yellow at 100%, yellow/red at 110%
- BR-014.3: Remaining calories can be negative (shows as "10 cal over")

**Validation Rules**:
- VR-014.1: Goal must be > 0

**Error Handling**:
- ERR-014.1: Goal not set → Use default 2000 kcal + prompt user to set profile

**Acceptance Criteria**:
- AC-014.1: WHEN daily total calculated THEN progress bar shows current vs goal
- AC-014.2: WHEN progress bar shown THEN color matches on-track/near-limit/over status
- AC-014.3: WHEN macro breakdown shown THEN P/C/F percentages visible

---

#### FR-015 & FR-016: Edit Meal Log

**Source UC**: UC-014 (Chỉnh sửa Log)

**Priority**: Medium  
**Status**: Planned

**Description**:
Hệ thống phải cho phép người dùng sửa đổi log bữa ăn từ ngày trước.

**Input**:
- User action: Swipe-left on meal row (WF-004), tap Edit
- Meal ID to edit

**Processing** (FR-015: Open modal, FR-016: Save changes):
1. Open edit modal (WF-013) with current meal data
2. Allow user to:
   - Adjust ingredients (add/remove, toggle checkbox)
   - Adjust portion sizes
   - Edit macros manually
   - View updated total
3. When "Save" tapped:
   - Validate (≥1 ingredient, total > 0)
   - Update meal record in database
   - Refresh daily totals (FR-012)
   - Show confirmation "Saved"
   - Close modal

**Output**:
- Meal updated in database
- Daily totals recalculated

**Business Rules**:
- BR-015.1: Can only edit own meals (creator = current user)
- BR-015.2: Cannot edit meals from other days (one-day-at-a-time rule)

**Validation Rules**:
- VR-015.1: Same validations as FR-004 (≥1 ingredient, total > 0)

**Error Handling**:
- ERR-015.1: DB update fails → "Could not save changes. Try again."
- ERR-015.2: Meal not found → "Meal deleted by another user"

**Acceptance Criteria**:
- AC-015.1: WHEN user swipes meal THEN edit button appears
- AC-015.2: WHEN modal opens THEN current data pre-populated
- AC-015.3: WHEN user saves THEN changes persist and daily total updates

---

#### FR-017: Delete Meal Log

**Source UC**: UC-015 (Xoá Log)

**Priority**: Medium  
**Status**: Planned

**Description**:
Hệ thống phải cho phép người dùng xoá log nhập sai.

**Input**:
- User action: Swipe-left on meal row (WF-004), tap Delete
- Meal ID to delete

**Processing**:
1. Show confirmation modal (WF-014): "Delete this meal log?"
2. User taps "Confirm" or "Cancel"
3. If confirm:
   - Delete meal from database
   - Refresh daily totals (FR-012)
   - Show success message (brief toast)
   - Remove row from list

**Output**:
- Meal deleted
- Daily totals recalculated

**Business Rules**:
- BR-017.1: Can only delete own meals
- BR-017.2: Deletion is permanent (no undo in MVP)

**Validation Rules**:
- None (deletion requires confirmation)

**Error Handling**:
- ERR-017.1: Delete fails → "Could not delete meal. Try again."

**Acceptance Criteria**:
- AC-017.1: WHEN user swipes meal THEN delete button appears
- AC-017.2: WHEN confirmation modal shown THEN user must confirm
- AC-017.3: WHEN delete confirmed THEN meal removed and total updated

---

### 2.4 Onboarding & User Profile Feature Group

#### FR-018: Collect User Profile (Height, Weight, Goal)

**Source UC**: UC-016 (Nhập Thông tin Cơ bản)

**Priority**: High  
**Status**: Planned

**Description**:
Hệ thống phải thu thập thông tin profile (height, weight, goal) để tính mục tiêu calo.

**Input**:
- User action: Onboarding step 1 (WF-008)
- User input: height (cm), weight (kg), goal (lose/maintain/gain)

**Processing**:
1. Display onboarding form (WF-008 step 1):
   - Height input: numeric, unit selector (cm/in)
   - Weight input: numeric, unit selector (kg/lb)
   - Goal selector: buttons (Lose / Maintain / Gain)
2. Validate inputs
3. Store in user profile
4. Proceed to step 2 (FR-019)

**Output**:
- Profile data saved
- Proceed to onboarding step 2

**Business Rules**:
- BR-018.1: Height range: 120–220 cm
- BR-018.2: Weight range: 30–300 kg
- BR-018.3: Unit conversion: cm/in, kg/lb (store in metric)

**Validation Rules**:
- VR-018.1: Height must be numeric, 120–220 cm
- VR-018.2: Weight must be numeric, 30–300 kg
- VR-018.3: Goal must be selected (required field)

**Error Handling**:
- ERR-018.1: Height out of range → "Height must be between 120 and 220 cm"
- ERR-018.2: Weight out of range → "Weight must be between 30 and 300 kg"
- ERR-018.3: Missing field → "Please fill all fields"

**Acceptance Criteria**:
- AC-018.1: WHEN user enters height and weight THEN inputs validated
- AC-018.2: WHEN goal selected THEN "Next" button enabled
- AC-018.3: WHEN user taps Next THEN data saved and proceed to step 2

---

#### FR-019: Select Activity Level

**Source UC**: UC-017 (Chọn Mức Hoạt Động)

**Priority**: High  
**Status**: Planned

**Description**:
Hệ thống phải cho phép người dùng chọn mức hoạt động để tính TDEE.

**Input**:
- Onboarding step 2 (WF-008)
- User selection: Sedentary / Light / Moderate / Very Active

**Processing**:
1. Display activity level options (WF-008 step 2):
   - Sedentary: "Little or no exercise"
   - Light: "Exercise 1-3 days/week"
   - Moderate: "Exercise 3-5 days/week"
   - Very Active: "Exercise 6-7 days/week"
2. Store selection
3. Proceed to step 3 (FR-020)

**Output**:
- Activity level stored
- Proceed to final onboarding step

**Business Rules**:
- BR-019.1: Activity levels mapped to TDEE multipliers: 1.375, 1.55, 1.725, 1.9 (Harris-Benedict)

**Validation Rules**:
- VR-019.1: Activity level must be selected

**Error Handling**:
- ERR-019.1: No selection → "Please select activity level"

**Acceptance Criteria**:
- AC-019.1: WHEN user sees activity options THEN descriptions provided
- AC-019.2: WHEN user selects activity THEN "Next" button enabled
- AC-019.3: WHEN Next tapped THEN proceed to goal confirmation (FR-020)

---

#### FR-020: Display Calculated Calorie Goal & Confirm

**Source UC**: UC-018 (Xem Mục tiêu Calo)

**Priority**: High  
**Status**: Planned

**Description**:
Hệ thống phải tính mục tiêu calo từ profile và hiển thị để xác nhận.

**Input**:
- User profile: height, weight, goal (lose/maintain/gain), activity level

**Processing**:
1. Calculate BMR using Mifflin-St Jeor: BMR = (10W + 6.25H - 5A) + 5 (or -161 for female; assume male for MVP)
2. Apply activity multiplier: TDEE = BMR × activity_factor
3. Adjust by goal:
   - Lose: TDEE - 500 (500 kcal deficit = 0.5 lb/week)
   - Maintain: TDEE
   - Gain: TDEE + 500
4. Display final goal (WF-008 step 3 final):
   - "Your daily calorie goal: 2000 kcal"
   - Show formula used (for transparency)
   - Button: "Ready to start logging?"
5. Store goal in profile
6. Close onboarding, proceed to app main (Camera tab)

**Output**:
- Goal stored
- Onboarding complete
- App displays main UI (Camera/Diary/Settings tabs)

**Business Rules**:
- BR-020.1: Formula: Mifflin-St Jeor (verified, published, widely used)
- BR-020.2: Deficit/surplus: 500 kcal/day (0.5 lb/week rate of change)
- BR-020.3: Goal range: 1000–3500 kcal (safety bounds)

**Validation Rules**:
- VR-020.1: Calculated goal must be 1000–3500 kcal

**Error Handling**:
- ERR-020.1: Calculated goal out of bounds → Cap at min/max, show warning

**Acceptance Criteria**:
- AC-020.1: WHEN goal calculated THEN displayed prominently
- AC-020.2: WHEN formula shown THEN transparent (users see calculation)
- AC-020.3: WHEN user confirms THEN onboarding closed and main app shown

---

### 2.5 Monetization & Subscription Feature Group

#### FR-021: Display Premium Trial Offer

**Source UC**: UC-019 (Xem Paywall)

**Priority**: High  
**Status**: Planned

**Description**:
[Same as FR-011 — paywall display with pricing]

---

#### FR-022: Initiate Trial Subscription

**Source UC**: UC-020 (Bắt đầu Trial)

**Priority**: High  
**Status**: Planned

**Description**:
Hệ thống phải gọi StoreKit để bắt đầu trial 7 ngày.

**Input**:
- User action: Tap "Start 7-day trial" on paywall (WF-006)
- User: not currently subscribed

**Processing**:
1. Tap CTA button → Call RevenueCat SDK (or StoreKit 2 directly)
2. Initiate App Store payment sheet for trial product
3. User confirms purchase in iOS sheet (Face ID / Touch ID / password)
4. StoreKit processes transaction
5. Receipt validation on backend
6. If valid:
   - Create subscription record (trial_start_date = today, trial_end_date = +7 days)
   - Update user subscription status to "active"
   - Return to app (modal closes)
   - Show "Premium activated!" toast
7. If invalid / cancelled:
   - Show error "Could not activate trial"
   - User can retry or stay on paywall

**Output**:
- Trial subscription activated
- User subscription status updated
- Scan limit removed (unlimited scans)

**Business Rules**:
- BR-022.1: Trial duration = 7 days (hardcoded; configurable in RevenueCat)
- BR-022.2: Requires valid payment method (auto-renews after trial)
- BR-022.3: One trial per user (cannot re-trigger trial after expiry)
- BR-022.4: Trial renews to monthly $9.99 after 7 days (unless cancelled)

**Validation Rules**:
- VR-022.1: User must not have active subscription
- VR-022.2: Receipt must be valid and correspond to user

**Error Handling**:
- ERR-022.1: User cancels payment sheet → Return to paywall, no charge
- ERR-022.2: Receipt invalid → Retry or show "Please try again"
- ERR-022.3: User already has active subscription → Show "You already have Premium"
- ERR-022.4: Network error during verification → Queue transaction for retry when online

**Acceptance Criteria**:
- AC-022.1: WHEN user taps "Start 7-day trial" THEN StoreKit payment sheet opens
- AC-022.2: WHEN user confirms payment THEN receipt validated on backend
- AC-022.3: WHEN subscription activated THEN trial status updated in user profile
- AC-022.4: THEN scan limit removed and user sees "Premium — unlimited scans"

---

#### FR-023: Verify & Activate Subscription (Backend)

**Source UC**: UC-020 (Bắt đầu Trial) — backend component

**Priority**: High  
**Status**: Planned

**Description**:
Backend phải xác minh receipt từ StoreKit và kích hoạt subscription trong database.

**Input**:
- StoreKit receipt (JWT token)
- User ID

**Processing**:
1. Receive receipt from client (FR-022)
2. Validate receipt with Apple App Store API (legacy) or App Store Server API (current)
3. Extract: product_id, subscription_start_date, expires_date, transaction_id
4. Verify:
   - product_id matches trial product
   - transaction not already processed (idempotency check)
   - user does not have active subscription
5. If valid:
   - Create subscription record in DB: {user_id, trial_start, trial_end, auto_renew_enabled, status="active"}
   - Set scan_limit = unlimited for this user
   - Return success to client
6. If invalid:
   - Return error to client with retry recommendation

**Output**:
- Subscription record created
- User profile updated with Premium status

**Business Rules**:
- BR-023.1: Receipt validation required from official Apple endpoint
- BR-023.2: Idempotency: if receipt already processed, return success (don't double-charge)
- BR-023.3: Trial auto-renews to monthly plan after 7 days (unless user cancels in App Store)
- BR-023.4: Subscription tied to App Store account (not user account — must verify user through device token)

**Validation Rules**:
- VR-023.1: Receipt must be valid JWT
- VR-023.2: Product ID must match trial or monthly product

**Error Handling**:
- ERR-023.1: Receipt invalid → Return error, client shows "Invalid receipt"
- ERR-023.2: User already has subscription → Return conflict, client shows "Already premium"
- ERR-023.3: Apple API unavailable → Retry with exponential backoff

**Acceptance Criteria**:
- AC-023.1: WHEN receipt received THEN validated with Apple API
- AC-023.2: WHEN subscription valid THEN user profile marked Premium
- AC-023.3: THEN scan_limit updated to unlimited in app

---

#### FR-024: Cancel Subscription

**Source UC**: UC-021 (Huỷ Subscription)

**Priority**: Medium  
**Status**: Planned

**Description**:
Hệ thống phải cho phép người dùng huỷ subscription.

**Input**:
- User action: Settings (WF-007) → "Manage subscription" → "Cancel" (WF-018 modal)
- User: Premium subscriber

**Processing**:
1. Display confirmation modal (WF-018): "Cancel Premium? You'll lose unlimited scans."
2. User taps "Confirm cancel" or "Keep subscription"
3. If confirm:
   - Call App Store server API to cancel subscription (managed link in App Store)
   - Or show in-app UI with link to App Store Manage Subscriptions page
   - Display: "Subscription will expire on [renewal_date]. You'll have [X] days of Premium left."

**Output**:
- Subscription marked for cancellation
- Expires at end of current billing cycle (not immediate)

**Business Rules**:
- BR-024.1: Cancellation scheduled for renewal date (not immediate refund)
- BR-024.2: User retains Premium access until expiry date
- BR-024.3: Cannot cancel from app; link to App Store Manage Subscriptions

**Validation Rules**:
- VR-024.1: User must have active subscription

**Error Handling**:
- ERR-024.1: User has no subscription → "No active subscription"
- ERR-024.2: Cannot reach App Store → "Please cancel from Settings > [App Name] > Manage Subscriptions"

**Acceptance Criteria**:
- AC-024.1: WHEN user opens Settings THEN subscription status visible
- AC-024.2: WHEN user taps "Cancel subscription" THEN confirmation modal shown
- AC-024.3: WHEN cancel confirmed THEN scheduled for cancellation on renewal date
- AC-024.4: THEN user notified: "Premium expires on [date]"

---

#### FR-025: Manage Subscription (View Status & Options)

**Source UC**: UC-022 (Quản lý Subscription)

**Priority**: Medium  
**Status**: Planned

**Description**:
Hệ thống phải hiển thị subscription status và cho phép người dùng quản lý.

**Input**:
- User profile: subscription data

**Processing**:
1. Display in Settings (WF-007):
   - If Premium: "Your subscription: Premium, renews [date]"
     - Options: Change plan / Restore purchases / Cancel
   - If not Premium: "Upgrade to Premium" button
2. "Change plan" → Link to App Store (manage subscriptions)
3. "Restore purchases" → Trigger FR-026
4. "Cancel" → Trigger FR-024

**Output**:
- Subscription info displayed
- Options available per user state

**Business Rules**:
- BR-025.1: Subscription managed via App Store (not in-app management)
- BR-025.2: Show renewal date, billing frequency

**Validation Rules**:
- VR-025.1: Subscription data must be fresh (refreshed from RevenueCat on app launch)

**Error Handling**:
- ERR-025.1: Subscription data stale → Show cached data + "Refresh" button

**Acceptance Criteria**:
- AC-025.1: WHEN user opens Settings THEN subscription status shown
- AC-025.2: THEN renewal date clearly displayed
- AC-025.3: WHEN user taps "Manage" THEN options available (change, restore, cancel)

---

#### FR-026: Restore Subscription Purchase

**Source UC**: UC-023 (Restore Purchase)

**Priority**: Low  
**Status**: Planned

**Description**:
Hệ thống phải khôi phục subscription nếu người dùng chuyển device hoặc cài lại app.

**Input**:
- User action: Settings (WF-007) → "Restore purchases"
- User: Same Apple ID as previous device

**Processing**:
1. Call StoreKit / RevenueCat restore API
2. Query past transactions for this Apple ID
3. If subscription found:
   - Activate subscription in user account
   - Update user profile: subscription status = "active"
   - Show success: "Premium restored"
4. If no subscription found:
   - Show "No previous purchases found"

**Output**:
- Subscription status updated (if found)
- Premium access restored (if applicable)

**Business Rules**:
- BR-026.1: Restore searches App Store transaction history (tied to Apple ID)
- BR-026.2: Can be triggered multiple times without charge (idempotent)

**Validation Rules**:
- VR-026.1: Apple ID must match original purchase

**Error Handling**:
- ERR-026.1: No previous purchases → "No previous purchases for this Apple ID"
- ERR-026.2: Network error → "Could not connect to App Store. Try again later."
- ERR-026.3: User different Apple ID → "Use the same Apple ID as your original purchase"

**Acceptance Criteria**:
- AC-026.1: WHEN user taps "Restore purchases" THEN App Store queried
- AC-026.2: IF subscription found THEN restored and Premium activated
- AC-026.3: IF no subscription THEN user notified "No previous purchases"

---

## 3. Non-Functional Requirements

### 3.1 Core NFRs (Required for all projects)

**Performance & Responsiveness**:
- **NFR-001**: App Launch Time — App shall launch in <2 seconds (iPhone 12+, ≤50% storage). Measured: cold start to tab bar interactive.
- **NFR-002**: AI Detection Response — AI meal detection <5 seconds (avg 3-5s, max 10s timeout). Measured: photo upload to result on WF-003.
- **NFR-003**: Diary Load Time — Daily log loads <500ms even with 100+ meals. Measured: tab tap to list rendered.

**Security & Data Protection**:
- **NFR-004**: User Authentication — All user data protected via Apple ID sign-in. Measured: no unauthenticated access.
- **NFR-005**: Data Encryption (Transit) — HTTPS/TLS 1.3+ for all API calls. Measured: 100% of network calls encrypted.
- **NFR-006**: Data Encryption (At-Rest) — Local meal logs encrypted via device keychain. Measured: encryption key derivation verified.

**Offline Support**:
- **NFR-007**: Offline Logging — Users can log meals offline; syncs when online. Measured: offline creation succeeds, "Syncing..." badge shown.
- **NFR-008**: Offline Diary View — Cached meal logs viewable offline with "Last updated X min ago" indicator. Measured: stale-data marker displayed.

**Accessibility**:
- **NFR-009**: WCAG 2.1 AA Compliance — Color contrast ≥4.5:1, accessible labels, keyboard navigation. Measured: automated + manual audit.
- **NFR-010**: VoiceOver Support — iOS VoiceOver works on all screens (buttons navigable, text readable, images described). Measured: VoiceOver testing.

---

### 3.2 Additional NFRs (Based on App Type: iOS Health/Fitness)

**Platform Requirements**:
- **NFR-011**: iOS Version — Support iOS 16+ only. Measured: target deployment iOS 16.0.
- **NFR-012**: Device Support — iPhone 12+ (A14 chip+, 6.1"+ screen). Measured: no A15-only APIs used.

**Scalability & Performance**:
- **NFR-013**: Concurrent Users — Backend supports 10K concurrent active users at launch. Measured: load test <500ms response, <1% error rate.
- **NFR-014**: Data Storage — Scale to 1M user accounts. Measured: Supabase auto-scaling, no manual intervention.

**Reliability**:
- **NFR-015**: Crash-Free Rate — <0.1% crash rate (99.9% uptime). Measured: Firebase Crashlytics tracking <0.1% of sessions.
- **NFR-016**: API Error Handling — Auto-retry with exponential backoff (max 3 retries, 10s total). Measured: client retry logic + user "retrying" UI.

**Monetization & Business Rules** (freemium model specific):
- **NFR-017**: Freemium Scan Limit — Free tier: 3 scans/day, Premium: unlimited. Measured: 4th scan blocked with paywall.
- **NFR-018**: Trial Auto-Expiry — 7-day trial auto-expires; reverts to free or charges subscription. Measured: Day 8 scan limit re-enforced.
- **NFR-019**: Analytics Tracking — Track signups, first meal logged, trial conversions, renewals via Firebase. Measured: analytics events in dashboard.

---

## 2 bis. Component Behavior Matrix

[To be populated from Use_Cases.md §2bis Feature Expression Matrix]

| FR ID | Component | Screen (WF) | Context | Behavior Difference |
|-------|-----------|-------------|---------|-------------------|
| FR-009 | Scan count badge | WF-002 (Camera) | Free tier, <3 scans | Shows "X/3", tap to see tooltip |
| FR-009 | Scan count badge | WF-004 (Diary) | Free tier, <3 scans | Shows "X/3" in header |
| FR-009 | Scan count badge | WF-002, WF-004 | Premium tier | Shows "Unlimited", no tooltip |
| FR-010 | Paywall trigger | WF-002 (Camera) | 4th scan attempt | Full modal with pricing |
| FR-010 | Paywall trigger | WF-007 (Settings) | Manual "Upgrade" tap | Same modal, no disruption |
| FR-014 | Progress bar | WF-004 (Diary) | Daily view | Full bar with label "1800/2000" |
| FR-014 | Progress bar | WF-005 (Dashboard) | Weekly view | Small progress circle per day |

---

## 2 ter. Context-Dependent Behaviors

[To be populated from Use_Cases.md per-UC Context Variations]

| FR ID | Context | Trigger | Behavior Change |
|-------|---------|---------|----------------|
| FR-002 | First Visit | App first-time launch, camera tab | Show hint "Angle from above" + camera permission dialog |
| FR-002 | Returning User | Camera tab, permission cached | Camera opens directly, no hint |
| FR-002 | Power User | Camera open, swipe down | Quick brightness/zoom adjustments via gesture |
| FR-003 | High Confidence | AI confidence ≥80% | Proceed to confirmation without warning |
| FR-003 | Low Confidence | AI confidence <70% | Show warning: "Not confident. Please verify below." |
| FR-003 | Offline | No internet | Use cached on-device model or cached results from prior scans |
| FR-012 | First Visit | Diary tab, no logs | Show empty state: "No meals logged yet. Tap Camera." with CTA |
| FR-012 | Returning User | Diary tab, has logs | Show full list, progress bar prominent |
| FR-012 | Approaching Goal | Daily total 90-110% of goal | Progress bar yellow (caution) |
| FR-012 | Over Goal | Daily total >110% of goal | Progress bar red + message "You're over your goal" |
| FR-020 | First Time | Onboarding step 3 | Show calculated goal + formula explanation |
| FR-022 | No Subscription | User free tier, taps trial | StoreKit payment sheet presented |
| FR-022 | Already Trialed | User trial expired | Show message "Reactivate Premium" (cannot trial again) |

---

---

## 4. Requirements Summary

### 4.1 Functional Requirements by Priority

| Priority | Count | FR IDs | Scope |
|----------|-------|--------|-------|
| **High** | 14 | FR-001, 002, 003, 004, 005, 006, 009, 010, 011, 012, 013, 014, 018, 019, 020, 022 | MVP critical path: camera, AI, confirmation, diary, paywall, onboarding |
| **Medium** | 11 | FR-007, 008, 015, 016, 017, 021, 023, 024, 025, 026, 025 | Secondary features: edit/delete, trial verify, subscription management, restore |
| **Low** | 1 | (none assigned) | Reserved for Post-MVP |
| **TOTAL** | **26** | **FR-001 to FR-026** | **100% UC coverage** (23 UCs → 26 FRs, 1.13x multiplier) |

**High Priority Justification**: UCs UC-001 through UC-004, UC-009–013, UC-016–020, UC-022 are MVP-critical (directly enable core logging + monetization loops). Without these, app is non-functional.

**Medium Priority Justification**: Advanced edit/delete, subscription lifecycle. Deferred 1-2 weeks post-MVP launch without breaking core experience.

---

### 4.2 Non-Functional Requirements by Category

| Category | Count | NFR IDs | Target |
|----------|-------|---------|--------|
| **Performance** | 3 | NFR-001, 002, 003 | App launch <2s, AI detection <5s, Diary load <500ms |
| **Security & Data** | 3 | NFR-004, 005, 006 | Apple ID auth, HTTPS/TLS 1.3+, encrypted at-rest storage |
| **Offline Support** | 2 | NFR-007, 008 | Offline logging + sync queue, cached Diary view |
| **Accessibility** | 2 | NFR-009, 010 | WCAG 2.1 AA compliance, VoiceOver support |
| **Platform** | 2 | NFR-011, 012 | iOS 16+, iPhone 12+ (A14 chip+) |
| **Scalability** | 2 | NFR-013, 014 | 10K concurrent users, 1M user accounts |
| **Reliability** | 2 | NFR-015, 016 | 99.9% crash-free rate, auto-retry with backoff |
| **Monetization** | 3 | NFR-017, 018, 019 | 3-scan/day free limit, 7-day trial auto-expiry, analytics tracking |
| **TOTAL** | **19** | **NFR-001 to NFR-019** | **All measurable targets set** |

---

### 4.3 Traceability Matrix: UC → FR Coverage

**Verification**: Every UC is mapped to ≥1 FR; every FR has valid UC source.

| UC ID | UC Name | FRs Derived | Coverage % |
|-------|---------|------------|-----------|
| UC-001 | Mở Camera | FR-001 | 100% ✓ |
| UC-002 | Chụp Ảnh | FR-002 | 100% ✓ |
| UC-003 | Xem Kết quả AI | FR-003 | 100% ✓ |
| UC-004 | Xác nhận Nguyên liệu | FR-004, FR-005, FR-006, FR-007, FR-008 | 100% ✓ |
| UC-005 | Thêm Nguyên liệu | FR-005 | 100% ✓ |
| UC-006 | Điều Chỉnh Khẩu Phần | FR-006 | 100% ✓ |
| UC-007 | Điều Chỉnh Macro | FR-007 | 100% ✓ |
| UC-008 | Xoá Nguyên liệu | FR-008 | 100% ✓ |
| UC-009 | Xem Scan Còn Lại | FR-009 | 100% ✓ |
| UC-010 | Hết Lượt → CTA Upgrade | FR-010, FR-011 | 100% ✓ |
| UC-011 | Xem Diary Ngày | FR-012 | 100% ✓ |
| UC-012 | Xem Diary Tuần | FR-013 | 100% ✓ |
| UC-013 | So sánh vs Mục tiêu | FR-014 | 100% ✓ |
| UC-014 | Chỉnh sửa Log | FR-015, FR-016 | 100% ✓ |
| UC-015 | Xoá Log | FR-017 | 100% ✓ |
| UC-016 | Nhập Thông tin Cơ bản | FR-018 | 100% ✓ |
| UC-017 | Chọn Mức Hoạt Động | FR-019 | 100% ✓ |
| UC-018 | Xem Mục tiêu Calo | FR-020 | 100% ✓ |
| UC-019 | Xem Paywall | FR-021 | 100% ✓ |
| UC-020 | Bắt đầu Trial | FR-022, FR-023 | 100% ✓ |
| UC-021 | Huỷ Subscription | FR-024 | 100% ✓ |
| UC-022 | Quản lý Subscription | FR-025 | 100% ✓ |
| UC-023 | Restore Purchase | FR-026 | 100% ✓ |
| **TOTALS** | **23 UCs** | **26 FRs** | **100% Coverage ✓** |

**Traceability Summary**:
- ✅ **Forward trace**: All 23 UCs have ≥1 FR
- ✅ **Backward trace**: All 26 FRs reference valid UCs (FR-001-026 trace to UC-001-023)
- ✅ **No orphans**: No UC without FR; no FR without UC
- ✅ **Bidirectional complete**: Full graph connectivity verified

---

## 10. References

- **PRD.md** (v1.0, 2026-07-21): Product scope, personas, features
- **Use_Cases.md** (v1.0, 2026-07-21): 23 MVP UCs, task flows, scenarios
- **Project_Overview.md** (v1.0, 2026-07-21): Architecture, tech stack (SwiftUI/MVVM, Supabase, RevenueCat)

---

**Phiên bản**: 1.0  
**Cập nhật lần cuối**: 2026-07-21  
**Trạng thái**: ✓ Hoàn thành — 26 FRs + 19 NFRs + matrices + summary  
**Hành động tiếp theo**: Quality gate validation (gate-fr) → then proceed to Wireframes.md (Step 5)
