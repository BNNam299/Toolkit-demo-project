# Carbina: Car Dashboard & Widgets — Wireframes

**Document Version**: 2.4
**Snapshot Date**: 2026-08-07 (đồng bộ PRD v2.4 · Project_Overview v2.4 · Use_Cases v2.4 · Functional_Requirements v2.4)
**Ngày tạo file**: 2026-08-17
**Status**: Draft — chờ PO review
**Design System**: `bento-grid` → [`.claude/shared/DESIGN_TOKEN_BENTO_GRID.json`](../../shared/DESIGN_TOKEN_BENTO_GRID.json)
**Dependencies**: `PRD.md` · `Project_Overview.md` · `Use_Cases.md` · `Functional_Requirements.md` (+ 7 sub-spec `FR_*.md`)

---

## 1. Introduction

### 1.1 Purpose

Tài liệu này là bản thiết kế thị giác nối **FR → màn hình**. Mỗi màn hình trong 30 màn của `Use_Cases.md` §0.3 có: archetype, thứ tự thị giác, bản đồ vùng nội dung, layout ASCII dùng token, danh sách component, ≥ 7 trạng thái, và luồng vào/ra.

Hai điều tài liệu này **không** làm: không định nghĩa lại hành vi hệ thống (thuộc `Functional_Requirements.md`), và không mô tả đường điều hướng xuyên màn hình (thuộc `UX_Flows.md` — Step 6).

### 1.2 Design Principles

- **Không có component iOS mặc định.** Nav bar, tab bar, button, card, input, sheet, alert, toast — tất cả đặc tả qua token của `bento-grid`. `NavigationStack`/`TabView` chỉ là **kỹ thuật triển khai**, không phải nguồn giá trị thị giác.
- **Hai bề mặt, hai ngôn ngữ.** 📱 iPhone dùng Bento đầy đủ (card, shadow nhẹ, bán kính 16). 🚗 CarPlay dùng biến thể **phẳng**: `shadow.elevation.0`, viền `borderStrong`, chữ ≥ 16pt, layout tính từ scene bounds tại runtime.
- **Glanceable trước, đẹp sau.** Trên màn hình xe, mỗi chuyển động là một chi phí an toàn. Chỉ crossfade, throttle 30s, cấm chuyển động vị trí.
- **Không affordance nào không có FR.** Mọi component và mọi tương tác đều truy vết được về một FR có AC — kiểm ở §10 (Affordance → FR Back-Trace Audit).
- **Trung thực về trạng thái.** Không màn trắng, không nút vô hiệu không giải thích, không giá cache, không "đã xong" khi chưa xong.

### 1.3 Design System

**Token file**: `.claude/shared/DESIGN_TOKEN_BENTO_GRID.json` — giá trị màu/bán kính/spacing/font **trích trực tiếp** từ `.claude/design-token/template-bento.pen` (77 biến, `variables` + `themes.Mode`). Mọi giá trị suy luận đã đánh dấu `INFERRED` trong file token.

| Nhóm | Token path | Light | Dark |
|---|---|---|---|
| Nền màn hình | `${color.palette.background}` | `#F2F3F0` | `#111111` |
| Bề mặt card | `${color.palette.surface}` | `#FFFFFF` | `#1A1A1A` |
| Bề mặt phụ | `${color.palette.surfaceVariant}` | `#E7E8E5` | `#2E2E2E` |
| Chữ chính | `${color.palette.textPrimary}` | `#111111` | `#FFFFFF` |
| Chữ phụ | `${color.palette.textSecondary}` | `#666666` | `#B8B9B6` |
| **Màu nhấn** | `${color.palette.accent}` | `#FF8400` | `#FF8400` |
| Chữ trên màu nhấn | `${color.palette.onAccent}` | `#111111` | `#111111` |
| Viền | `${color.palette.border}` | `#CBCCC9` | `#2E2E2E` |
| Viền đậm (CarPlay) | `${color.palette.borderStrong}` | `#666666` | `#B8B9B6` |
| Lỗi | `${color.semantic.error.color}` | `#8C1C00` | `#FF5C33` |
| Thành công | `${color.semantic.success.color}` | `#004D1A` | `#B6FFCE` |

- **Typography**: `${typography.family.primary}` = **Geist** cho mọi chữ · `${typography.family.mono}` = **JetBrains Mono** cho mọi **số** (counter, số ngày trial, kích thước màn hình, giá). Fallback `SF Pro`. Lý do dùng mono cho số: chiều rộng ký tự ổn định nên số không nhảy khi giá trị đổi — quan trọng khi người dùng chỉ nhìn thoáng.
- **Spacing**: `${spacing.xs}`=4 · `sm`=8 · `md`=12 · `lg`=16 · `xl`=24 · `xxl`=32 · `xxxl`=48. Thang này **tight hơn** thang 8pt mẫu của `DESIGN_SYSTEM_GUIDE.md` §3.3 — giữ theo `.pen` vì đó là design system thật của project.
- **Corner radius**: `${border.radius.sm}`=4 · `md`=8 · `lg`=**16** (bán kính đặc trưng Bento, dùng cho card và button) · `xl`=20 (sheet) · `full`=100.
- **Shadow**: `${shadow.elevation.1}` = (0,1,3, 5% `#1A1A1A`) là mức mặc định của card. Nút primary **không có shadow** — nổi bật bằng màu cam, không bằng độ cao. **Bề mặt CarPlay dùng `elevation.0` tuyệt đối.**
- **Animation**: `${animation.duration.normal}`=0.25s · `${animation.spring.smooth}`=0.4s/damping 0.7. CarPlay: **chỉ** crossfade 0.4s, cấm positional-move/scale/bounce/blink.

### 1.4 External References & Fallback

| External reference | Nếu có | Fallback nếu thiếu | Tình trạng thật trong project |
|---|---|---|---|
| `ios-components` skill | Dùng định nghĩa component của skill | Dùng danh sách inline ở §4 | **Có** — `.claude/skills/ios-components/` |
| `ios-ui-ux` skill | Dùng hướng dẫn UX của skill | Dùng §5–§7 trong tài liệu này | **Có** — `.claude/skills/ios-ui-ux/` |
| `mcp-figma` (Framelink) | Trích token/spec từ Figma | Dùng ASCII wireframe + §1.3 | **Chưa dùng** — không có Figma file cho dự án này |
| `DESIGN_TOKEN_[name].json` | Dùng giá trị token | Dùng token path nguyên dạng, không hardcode màu iOS | **Đã tạo** — `DESIGN_TOKEN_BENTO_GRID.json`. ⚠️ 9 file token khác mà `DESIGN_SYSTEM_GUIDE.md` §2 nhắc tới **không tồn tại** trong project; nguồn thật là 4 file `.pen` ở `.claude/design-token/` |
| Figma file | Link file | Ghi "(chưa tạo)"; wireframe ở đây là nguồn chân lý | **(chưa tạo)** — xem §9 |

> **Ghi chú về ID màn hình bắt buộc**: skill yêu cầu luôn có Splash, Onboarding, IAP/Paywall. Cả ba **đều có**, nhưng ở ID theo canvas của `Use_Cases.md` §0.3 chứ không theo ví dụ của template: **Splash = WF-001**, **Onboarding = WF-002** (đầu chuỗi 4 màn onboarding WF-002 → WF-005), **Paywall = WF-010**. Quy tắc 12 của skill (ID phải khớp canvas UC, cấm đánh số lại) thắng ví dụ đánh số trong template.

---

## 2. Screen Inventory

**MÀN HÌNH BẮT BUỘC** (mọi app đều phải có):

| Screen ID | Screen Name | Priority | Related FR | Related UC | Status |
|---|---|---|---|---|---|
| WF-001 | Splash / Launch | High | FR-009 | UC-001 | Draft |
| WF-002 | Onboarding — Welcome | High | FR-001, FR-003 | UC-001 | Draft |
| WF-010 | Paywall (IAP / Store) | High | FR-045, FR-046, FR-047, FR-003 | UC-024, UC-025, UC-030 | Draft |

**MÀN HÌNH BỔ SUNG** (dẫn xuất từ `Functional_Requirements.md`):

| Screen ID | Screen Name | Priority | Related FR | Related UC | Status |
|---|---|---|---|---|---|
| WF-003 | Onboarding — Chọn Xe | High | FR-004, FR-005 | UC-002, UC-003 | Draft |
| WF-004 | Onboarding — Chọn Âm Thanh | High | FR-010, FR-011, FR-013 | UC-006, UC-001 | Draft |
| WF-005 | Onboarding — Cấp Quyền | High | FR-007, FR-008 | UC-004, UC-005 | Draft |
| WF-006 | Home (iPhone) | High | FR-009, FR-021, FR-031, FR-044, FR-051 | UC-024, UC-005, UC-012, UC-016 | Draft |
| WF-007 | Thư Viện Âm Thanh | High | FR-010, FR-011, FR-013, FR-014 | UC-006, UC-007, UC-008 | Draft |
| WF-008 | Trình Tạo Widget | High | FR-021, FR-022, FR-023, FR-024 | UC-012 | Draft |
| WF-009 | Cài Đặt Giọng Chào | High | FR-033, FR-034, FR-035, FR-036 | UC-018, UC-019, UC-020 | Draft |
| WF-011 | Xác Nhận Giá | High | FR-048, FR-049, FR-054 | UC-026, UC-027, UC-030 | Draft |
| WF-012 | Cài Đặt Chung | Medium | FR-015, FR-055, FR-057, FR-059, FR-061, FR-062 | UC-009, UC-031, UC-032, UC-033, UC-036 | Draft |
| WF-013 | Nhắc Hết Trial | Medium | FR-052, FR-051 | UC-028, UC-027 | Draft |
| WF-014 | Chẩn Đoán Tương Thích | Medium | FR-032, FR-066 | UC-017, UC-016 | Draft |
| WF-015 | Account *(MVP 3)* | Low | FR-064, FR-065 | UC-035 | Deferred |
| WF-016 | CarPlay Dashboard 🚗 | High | FR-040, FR-041, FR-042 | UC-022, UC-023 | Draft |
| WF-017 | CarPlay Widget 🚗 | High | FR-029, FR-030, FR-061 | UC-015, UC-036 | Draft |
| WF-018 | CarPlay — Trạng Thái Free 🚗 | High | FR-041, FR-044 | UC-024, UC-022 | Draft |
| WF-019 | CarPlay — Fallback Lỗi 🚗 | High | FR-031 | UC-016 | Draft |
| WF-020 | Sheet — Nghe Thử Âm Thanh | High | FR-012, FR-015, FR-013 | UC-006, UC-007, UC-009 | Draft |
| WF-021 | Sheet — Không tìm thấy xe | Medium | FR-006 | UC-003 | Draft |
| WF-022 | Sheet — Lý Do Xin Quyền | High | FR-007, FR-035 | UC-004, UC-019 | Draft |
| WF-023 | Modal — Preview Widget Theo Màn Hình Xe | High | FR-025, FR-026 | UC-013 | Draft |
| WF-024 | Sheet — Chọn Ảnh Cho Widget | Medium | FR-027, FR-028 | UC-014 | Draft |
| WF-025 | Sheet — Quản Lý Đăng Ký | Medium | FR-053, FR-003 | UC-029 | Draft |
| WF-026 | Sheet — Chọn Ngôn Ngữ | Medium | FR-055, FR-056 | UC-031 | Draft |
| WF-027 | Alert — Xác Nhận Huỷ Trial | Medium | FR-053 | UC-029, UC-028 | Draft |
| WF-028 | Sheet — Gửi Báo Cáo Tương Thích | Medium | FR-032, FR-060 | UC-017, UC-033 | Draft |
| WF-029 | Alert — Xoá Dữ Liệu On-Device | Medium | FR-057, FR-058 | UC-032 | Draft |
| WF-030 | Overlay — Toast Xác Nhận | Medium | FR-059, FR-058 | UC-033, UC-007, UC-017 | Draft |

**Tổng: 30 màn hình** — khớp đúng canvas `Use_Cases.md` §0.3 (19 màn chính + 11 modal/overlay). Ngưỡng Medium là 20–35 ⇒ **Pass**.

**Screen coverage rule check**: 42/42 FR ưu tiên High đều có ≥ 1 màn hình. Bốn FR không có bề mặt riêng vì là hành vi nền (FR-016, FR-017, FR-018, FR-019, FR-020 — âm thanh; FR-037, FR-038, FR-039 — giọng chào; FR-043, FR-066 — service) được gán vào màn hình nơi chúng **xảy ra** (WF-016) và nơi chúng **được cấu hình** (WF-007, WF-009, WF-012) — chi tiết ở §10.

---

## 2 bis. Screen Taxonomy

### Archetype Catalog

| Archetype | Mục đích | Layout Pattern | Ưu tiên component | Engagement default | Màn hình của Carbina |
|---|---|---|---|---|---|
| **Discovery** | Duyệt, nghe thử, khám phá | Danh sách nhóm + nghe inline, scroll-driven | Row có waveform, card preset, nhãn khoá | Pull-to-refresh, nghe inline, gom nhóm, skeleton | WF-002, WF-004, WF-007, WF-016 |
| **Action** | Hoàn tất một việc | Form / CTA đơn mục đích, tối giản | Input, button, toggle, progress bar | Validation inline, một CTA duy nhất, đường thoát luôn thấy | WF-003, WF-005, WF-009, WF-010, WF-011, WF-013, WF-021, WF-024, WF-026, WF-027, WF-028, WF-029 |
| **Consumption** | Nhìn, đọc, nghe | Full-bleed / tối giản chrome | Media, khối chữ, điều khiển tối thiểu | Full-bleed, scrim khi chữ nằm trên ảnh, không modal | WF-001, WF-017, WF-018, WF-019, WF-020, WF-022, WF-023, WF-030 |
| **Management** | Tổ chức, xem lại, kiểm soát | Danh sách dòng / dashboard trạng thái, dày thông tin | Row có trạng thái ngay trên dòng, badge, bảng dữ liệu | Gom nhóm dòng, xác nhận cho hành động phá hủy, pull-to-refresh | WF-006, WF-008, WF-012, WF-014, WF-015, WF-025 |
| **Social** | Tương tác giữa người dùng | — | — | — | **Không có màn nào.** MVP 1 không có nội dung chia sẻ và không có tương tác giữa người dùng. Đây là kết luận, không phải bỏ sót |

### Screen Taxonomy Assignment Table

| WF-ID | Screen Name | Primary Archetype | Secondary Archetype | Density | Key Behaviors | Template |
|---|---|---|---|---|---|---|
| WF-001 | Splash / Launch | Consumption | — | Light | Tự chuyển, logo, chỉ báo tải chỉ khi > 1s | C |
| WF-002 | Onboarding — Welcome | Discovery | Action | Light | Một câu tuyên bố, một CTA, progress 1/4, phục hồi giao dịch | A |
| WF-003 | Onboarding — Chọn Xe | Action | Discovery | Medium | Picker 3 tầng ghim, tìm kiếm on-device, báo thiếu xe | B |
| WF-004 | Onboarding — Chọn Âm Thanh | Discovery | Action | Medium | Tự phát preset đầu, waveform thật, ducking thật, "Chọn sau" | A |
| WF-005 | Onboarding — Cấp Quyền | Action | — | Medium | 2 thẻ quyền có lý do + ví dụ, "Bỏ qua tất cả" luôn bấm được | B |
| WF-006 | Home (iPhone) | Management | Discovery | **Dense** | Hub trạng thái, pull-to-refresh, cảnh báo tự xoá, badge gói | D |
| WF-007 | Thư Viện Âm Thanh | Discovery | Action | **Dense** | Nghe inline, segmented 3 sự kiện giữ vị trí cuộn, nhãn khoá | A |
| WF-008 | Trình Tạo Widget | Management | Action | **Dense** | Preset gợi ý theo xe, preview nhúng, giới hạn theo entitlement | D |
| WF-009 | Cài Đặt Giọng Chào | Action | Management | Medium | Nghe thử sinh thật + chữ đồng thời, 4 toggle nguồn, toggle nảy | B |
| WF-010 | Paywall | Action | Discovery | Medium | 4 bậc giá từ StoreKit, bảng so sánh mở rộng, phục hồi giao dịch | B |
| WF-011 | Xác Nhận Giá | Action | — | Light | 4 mốc giá/ngày, Zone C **trống có chủ ý**, ghi `price_confirmed` | B |
| WF-012 | Cài Đặt Chung | Management | — | **Dense** | Dòng có trạng thái ngay trên dòng, slider âm lượng, xoá dữ liệu | D |
| WF-013 | Nhắc Hết Trial | Action | — | Light | 3 nút **ngang hàng thị giác**, số tiền thật, không đếm ngược | B |
| WF-014 | Chẩn Đoán Tương Thích | Management | — | Medium | Kích thước scene thật, dòng mở rộng có `failure_reason`, sao chép | D |
| WF-015 | Account *(MVP 3)* | Management | Action | Light | Đăng nhập tuỳ chọn, bảng "đồng bộ / không đồng bộ" | D |
| WF-016 | CarPlay Dashboard 🚗 | Discovery | — | Medium | Thẻ tự sắp xếp, crossfade 0.4s throttle 30s, 1 chạm, không modal | A |
| WF-017 | CarPlay Widget 🚗 | Consumption | — | Light | Layout từ scene bounds runtime, scrim khi cần, không tương tác | C |
| WF-018 | CarPlay — Trạng Thái Free 🚗 | Consumption | — | Light | **Một dòng chữ tĩnh**, không chắn nội dung, không mở paywall | C |
| WF-019 | CarPlay — Fallback Lỗi 🚗 | Consumption | — | Light | Chỉ đọc, không CTA, **không bao giờ vùng trắng** | C |
| WF-020 | Sheet — Nghe Thử Âm Thanh | Consumption | Action | Medium | Tự phát khi mở, mũi tên trước/sau không cuộn vòng, slider | C |
| WF-021 | Sheet — Không tìm thấy xe | Action | — | Light | 3 ô tự do, xếp hàng offline, xác nhận ≤ 500ms | B |
| WF-022 | Sheet — Lý Do Xin Quyền | Consumption | Action | Light | 2 ví dụ có/không có quyền, nút từ chối **ngang hàng** | C |
| WF-023 | Modal — Preview Widget | Consumption | Action | Medium | Vuốt qua tỉ lệ, nhãn thật/ước lượng, cảnh báo vượt vùng | C |
| WF-024 | Sheet — Chọn Ảnh Widget | Action | Discovery | Medium | Khung crop theo tỉ lệ xe, vùng cắt làm tối, cảnh báo mờ | B |
| WF-025 | Sheet — Quản Lý Đăng Ký | Management | Action | Medium | Trạng thái + huỷ ≤ 3 chạm, mở rộng tính năng đang có | D |
| WF-026 | Sheet — Chọn Ngôn Ngữ | Action | — | Light | Chọn là áp dụng ngay, ghi chú MVP 2 cho DE/FR/IT | B |
| WF-027 | Alert — Xác Nhận Huỷ Trial | Action | — | Light | **Một câu hỏi duy nhất**, nêu ngày hết quyền + cấu hình được giữ | B |
| WF-028 | Sheet — Gửi Báo Cáo | Action | Management | Medium | Liệt kê **từng mục** dữ liệu + giá trị thật + tick chọn | B |
| WF-029 | Alert — Xoá Dữ Liệu | Action | — | Light | Nêu **mất gì và giữ gì**, lựa chọn thứ hai tách riêng | B |
| WF-030 | Overlay — Toast Xác Nhận | Consumption | Action | Light | Tự đóng 2s, biến thể mời đánh giá bị chặn 7 ngày sau lỗi render | C |

**Kiểm tra**:
- 30/30 màn hình có Primary Archetype ⇒ **Pass**
- Phân bố: Consumption 8 · Action 12 · Management 6 · Discovery 4 · Social **0**
- Density khớp `Use_Cases.md` §4/§9: Light 14 · Medium 12 · Dense 4
- **Không màn CarPlay nào ở mức Dense** — giới hạn cứng vì an toàn khi lái
- Density khớp kỳ vọng archetype của skill: Discovery ở đây là Medium/Dense (WF-007 Dense, WF-016 Medium bị giới hạn bởi ràng buộc CarPlay — sai lệch có chủ ý, ghi ở §Notes của WF-016)

---

## 3. Screen Sections

> Mỗi màn hình dùng **template khớp archetype**: Discovery→A · Action→B · Consumption→C · Management→D. Zone A/B/C/D theo **Archetype Zone Override Table** của skill; nhãn mặc định của `Use_Cases.md` §4 chỉ áp dụng cho màn Discovery.

---

### 3.1 WF-001 — Splash / Launch 📱 · *Template C (Consumption)*

**Design System**: `bento-grid`
**Archetype**: Consumption | **Density**: Light (1 vùng, không tương tác)
**Source UC**: UC-001 | **Source FR**: **FR-009** (Splash, định tuyến khởi động và làm mới trạng thái)
**User Intent**: "Tôi muốn app mở ra thật nhanh."

**Action Layer → Visual Hierarchy**

| UC Action Layer | Slot | Ghi chú |
|---|---|---|
| Layer 1 — Primary: không có hành động người dùng | #1 | Hệ thống tự quyết điểm đến; đây là màn duy nhất không có Layer 1 dạng hành động |
| Layer 2/3/4 | — | **Trống có chủ ý** (`Use_Cases.md` §4.1): mọi tương tác ở đây chỉ làm chậm việc mở app |

**Visual Hierarchy**
1. **Logo Carbina** — canh giữa, phần tử duy nhất có nội dung. `${typography.scale.h1}` hoặc asset logo, chiều cao ~`${spacing.xxxl}`.
2. **Chỉ báo tải** — chỉ xuất hiện **nếu quá 1s**; nếu app khởi động đúng ngưỡng NFR-001 thì người dùng không bao giờ thấy nó.
3. — (không có)
4. — (không có)

*Self-check*: #1 là phần tử duy nhất ⇒ hiển nhiên nổi bật nhất. Người dùng không cần hoàn tất tác vụ gì ở đây. Không có CTA nên quy tắc "CTA tương phản cao nhất" không áp dụng.

**Required Features (FR)**
- FR-009 P1–P4: đọc `hasCompletedOnboarding` / `onboardingStep` từ App Group, định tuyến WF-002 (≤1,5s) hoặc WF-006 (≤1,0s)
- FR-009 BR-009.1: **không có hành động người dùng nào**
- FR-009 ERR-009.1: cấu hình hỏng → vào WF-006 trạng thái mặc định an toàn, **không** bắt onboard lại
- NFR-001: tương tác được trong ≤ 2,0s trên iPhone 12

**UX Enhancements** (`composition.consumption.defaults`)
- `full-bleed-media`: nền phủ toàn màn `${color.palette.background}`, không nav bar, không status bar chrome
- `no-modal`: không alert, không sheet ở màn này kể cả khi có lỗi đọc cấu hình
- Chỉ báo tải trễ 1s — tránh nhấp nháy spinner ở lần khởi động nhanh

**Content Zones Map**

```
┌─────────────────────────────────────┐
│                                     │
│ ZONE A: Hero Media (full-bleed)     │ ← fill, background ${color.palette.background}
│   [Logo Carbina] canh giữa          │   .ignoresSafeArea()
│                                     │
├─────────────────────────────────────┤
│ ZONE B: — (không có CTA)            │ ← height 0
│ ZONE C: — (unused)                  │ ← height 0
│ ZONE D: Chỉ báo tải (điều kiện)     │ ← ~${spacing.xl}, chỉ hiện nếu > 1s
└─────────────────────────────────────┘
```

**Layout**

```
┌──────────────────────────────────────────────┐
│ background: ${color.palette.background}      │  ZONE A (fill)
│ .ignoresSafeArea()                           │
│                                              │
│                                              │
│                                              │
│              ┌──────────────┐                │
│              │              │                │  Logo asset
│              │   CARBINA    │                │  ~${spacing.xxxl} cao
│              │              │                │  tint ${color.palette.textPrimary}
│              └──────────────┘                │
│                                              │
│                                              │
│         ⟳  (chỉ hiện nếu > 1s)               │  ZONE D
│         tint ${color.palette.accent}          │  ${spacing.xl}
│                                              │
└──────────────────────────────────────────────┘
   → định tuyến: WF-002 (chưa onboard) | WF-006 (đã onboard)
```

**Components**
- `SplashBrandMark` — logo, canh giữa. Tokens: `background: ${color.palette.background}`, tint `${color.palette.textPrimary}`. Không có biến thể dark riêng — token đã tự đảo.
- `DelayedSpinner` — chỉ báo tải trễ 1s. Tokens: tint `${color.palette.accent}`, `animation: ${animation.duration.normal}`.
- Triển khai SwiftUI: xem `ios-components` skill (không đặc tả inline).

**States** (7 — 3 user-context + 4 data)

| State | Loại | Context | Layout/Behavior |
|---|---|---|---|
| **First Visit** | user-context | `hasCompletedOnboarding == false` | Hiện ≤ 1,5s → WF-002 |
| **Returning** | user-context | Đã onboard | Hiện ≤ 1,0s → WF-006; đọc cache nên **không** có state Loading |
| **Error** | user-context | Không đọc được cấu hình on-device (ERR-009.1) | Vào WF-006 ở mặc định an toàn + một dòng thông báo trên WF-006; **không** hiện màn lỗi ở đây |
| **Default** | data | Cấu hình đọc bình thường | Logo hiện, chuyển đúng điểm đến |
| **Loading** | data | Đọc cấu hình > 1s | `DelayedSpinner` xuất hiện; không thay đổi layout khác |
| **Empty** | data | Không áp dụng — màn này không có dữ liệu người dùng | Trạng thái này **không tồn tại có chủ ý**; ghi lại để chứng minh đã cân nhắc |
| **Offline** | data | Không có mạng | Không ảnh hưởng: định tuyến chỉ đọc App Group, **không** gọi mạng |

**User Flow**
- **Entry**: chạm icon app · deep link · quay lại sau khi hệ thống thu hồi app
- **Exit**: **WF-002** (chưa onboard) · **WF-006** (đã onboard) · **WF-014** nếu phiên CarPlay gần nhất có `widget_render_failed` (qua cảnh báo trên WF-006, không nhảy trực tiếp)
- **Task Flow**: bước 1 của **TF-001**
- **Transitions**: crossfade `${animation.duration.normal}` sang màn kế tiếp — không dùng push/slide vì splash không thuộc cây điều hướng

---

### 3.2 WF-002 — Onboarding: Welcome 📱 · *Template A (Discovery)*

**Design System**: `bento-grid`
**Archetype**: Discovery | **Secondary**: Action | **Density**: Light (2 vùng)
**Source UC**: UC-001 | **Source FR**: **FR-001** (điều phối onboarding), **FR-003** (phục hồi giao dịch)
**User Intent**: "Tôi muốn biết app này làm gì trước khi bỏ thời gian thiết lập."

**Action Layer → Visual Hierarchy**

| UC Action Layer | Slot | Ghi chú |
|---|---|---|
| Layer 1 — Primary: chạm "Bắt đầu" | **#3** | CTA tương phản cao nhất sau hero |
| Layer 2 — Contextual: xem `ProgressBar` 1/4 | #4 | Chrome, chỉ đọc |
| Layer 3 — Discovery: **trống có chủ ý** | — | Không có gì để khám phá trước khi thiết lập; thêm vào sẽ làm loãng một câu tuyên bố duy nhất |
| Layer 4 — Personal: "Phục hồi giao dịch" | #4 | Chỉ hiện khi StoreKit báo có giao dịch cũ (FR-003 P1) |

**Visual Hierarchy**
1. **Hình minh họa widget trên màn hình xe** — full-width, ~`${spacing.xxxl}`×5 cao. Thứ đầu tiên mắt thấy, và nó nói app làm gì mà không cần đọc.
2. **Một câu tuyên bố** — `${typography.scale.h2}`, dưới hero. Nói app làm gì trong một câu.
3. **CTA "Bắt đầu"** — `${component.button.primary}` 50pt, nền `${color.palette.accent}`, chữ `${color.palette.onAccent}`. Tương phản cao nhất sau hero.
4. **`ProgressBar` 1/4 + dòng "Phục hồi giao dịch"** — chrome, `${typography.scale.caption}`, `${color.palette.textSecondary}`.

*Self-check*: hero cao gấp ~3× chiều cao CTA ⇒ đạt. Người dùng hiểu app làm gì trong < 3s vì chỉ có một câu. CTA là phần tử tương phản cao nhất sau hero ⇒ đạt. Phần tử phụ (#4) nhỏ hơn > 30% so với CTA ⇒ đạt.

**Required Features (FR)**
- FR-001 P1: hiển thị WF-002 + `ProgressBar` 1/4
- FR-001 P2: chạm "Bắt đầu" → tăng `onboardingStep`, chuyển WF-003; ghi `onboarding_started`
- FR-001 **BR-001.1**: **cấm** hiển thị WF-010 Paywall ở bất kỳ bước onboarding nào
- FR-003 P1: **chỉ hiện** "Phục hồi giao dịch" nếu StoreKit báo có giao dịch cũ
- FR-001 ERR-001.3: không lấy được trạng thái giao dịch → **ẩn** dòng phục hồi, không hiện nút vô hiệu

**UX Enhancements** (`composition.discovery.defaults` + đặc thù màn)
- `section-grouping`: một khối duy nhất — cố tình **không** dùng nhiều section ở màn này
- `skeleton-loading`: **không dùng** — nội dung là asset tĩnh trong bundle, skeleton sẽ là chuyển động vô nghĩa
- Haptic `${animation.haptics.light}` khi chạm "Bắt đầu"
- Đường thoát: không có nút bỏ qua ở màn này (chưa có gì để bỏ qua), nhưng bước sau đều có

**Content Zones Map**

```
┌─────────────────────────────────────┐
│ ZONE A: Hero                        │ ← ~${spacing.xxxl}×5, static
│   Minh họa widget trên màn hình xe  │
├─────────────────────────────────────┤
│ ZONE B: Engagement                  │ ← câu tuyên bố + CTA
│   Câu tuyên bố + [Bắt đầu]          │   button ${component.button.primary.height}=50
├─────────────────────────────────────┤
│ ZONE C: Discovery — TRỐNG CÓ CHỦ Ý  │ ← height 0
├─────────────────────────────────────┤
│ ZONE D: Chrome                      │ ← ${component.progressBar.height}=4 + dòng phục hồi
│   ProgressBar 1/4 · Phục hồi g.dịch │
└─────────────────────────────────────┘
```

**Layout**

```
┌──────────────────────────────────────────────┐
│ (không nav bar — onboarding không có back ở  │
│  bước đầu)                                   │
│ ┌──────────────────────────────────────────┐ │ ZONE A
│ │                                          │ │ ~240pt
│ │      [ Minh họa: widget Carbina          │ │ asset @2x/@3x
│ │        hiện trên màn hình xe ]           │ │
│ │                                          │ │
│ └──────────────────────────────────────────┘ │
│                                              │ ${spacing.xl}
│  Màn hình xe của bạn, tự biết bạn cần gì.    │ ZONE B
│  ${typography.scale.h2} · textPrimary        │ 28/700
│                                              │ ${spacing.md}
│  Widget, âm thanh lên xe và giọng chào       │ ${typography.scale.body}
│  cá nhân hóa — dùng thử miễn phí, vô hạn.    │ textSecondary
│                                              │ ${spacing.xl}
│ ┌──────────────────────────────────────────┐ │
│ │            Bắt đầu                       │ │ h=50 r=16
│ └──────────────────────────────────────────┘ │ bg ${color.palette.accent}
│                                              │ chữ ${color.palette.onAccent}
│         Phục hồi giao dịch                   │ ZONE D (điều kiện)
│         ${typography.scale.caption} accent   │
│                                              │
│  ▬▬▬▬▬▬▬░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   │ ProgressBar 1/4
│  h=4 r=100 · accent / surfaceVariant         │ ${spacing.lg} bottom
└──────────────────────────────────────────────┘
```

**Components**
- `OnboardHeroIllustration` — asset tĩnh. Tokens: `radius: ${border.radius.lg}`, không shadow.
- `BtnPrimary` — Tokens: `height: ${component.button.primary.height}`(50), `radius: ${component.button.primary.radius}`(16), `background: ${color.palette.accent}`, `foreground: ${color.palette.onAccent}`, `shadow: ${shadow.elevation.0}`, `font: ${typography.scale.button}`.
- `BtnTertiary` ("Phục hồi giao dịch") — Tokens: `height: ${component.button.tertiary.height}`(44), `foreground: ${color.palette.accent}`, `background: transparent`.
- `ProgressBarOnboard` — Tokens: `height: ${component.progressBar.height}`(4), `radius: ${border.radius.full}`, active `${color.palette.accent}`, track `${color.palette.surfaceVariant}`.
- Triển khai SwiftUI: `ios-components` skill.

**States** (7)

| State | Loại | Context | Layout/Behavior |
|---|---|---|---|
| **First Visit** | user-context | Cài mới | Một câu tuyên bố + một nút; **không paywall, không gì khác** |
| **Returning** | user-context | Cài lại, có giao dịch cũ | Thêm `BtnTertiary` "Phục hồi giao dịch" dưới CTA chính |
| **Error** | user-context | StoreKit không trả trạng thái giao dịch (ERR-001.3) | **Ẩn** dòng phục hồi thay vì hiện nút không hoạt động; CTA chính vẫn hoạt động |
| **Default** | data | Asset nạp xong | Layout như trên |
| **Loading** | data | Truy vấn StoreKit đang chạy | Vùng dòng phục hồi giữ chiều cao nhưng để trống — **không** hiện spinner (tránh nhấp nháy ở màn đầu tiên) |
| **Empty** | data | Không có giao dịch cũ | Dòng phục hồi **không** render; layout co lại tự nhiên |
| **Offline** | data | Không có mạng | CTA chính hoạt động bình thường; dòng phục hồi ẩn (như Empty) |

**User Flow**
- **Entry**: **WF-001** (lần đầu cài)
- **Exit**: **WF-003** (chạm "Bắt đầu") · **WF-006** (phục hồi giao dịch thành công **và** đã có cấu hình cũ)
- **Task Flow**: bước 2 của **TF-001**
- **Transitions**: push sang WF-003 với `${animation.spring.smooth}`; `ProgressBar` animate 1/4 → 2/4 cùng lúc

---

### 3.3 WF-003 — Onboarding: Chọn Xe 📱 · *Template B (Action)*

**Design System**: `bento-grid`
**Archetype**: Action | **Secondary**: Discovery | **Density**: Medium (4 vùng)
**Source UC**: UC-002 (chính), UC-003 | **Source FR**: **FR-004** (thư viện xe + tìm kiếm), **FR-005** (ảnh xe + fallback silhouette)
**User Intent**: "Tôi muốn app biết xe của tôi để widget trông giống xe thật."

**Action Layer → Visual Hierarchy**

| UC Action Layer | Slot | Ghi chú |
|---|---|---|
| Layer 1 — Primary: chọn hãng → model → năm và xác nhận | **#3** | CTA "Đúng xe của tôi", bật sáng khi đủ 3 giá trị |
| Layer 2 — Contextual: tìm kiếm · quay lại một tầng · xem ảnh xe đối chiếu | #2, #4 | Ô tìm kiếm ở #4 (chrome); ảnh đối chiếu ở #1 (hero) |
| Layer 3 — Discovery: danh sách hãng theo mức phổ biến · gợi ý hãng vừa xem | **#2** | Danh sách là nơi người dùng dành phần lớn thời gian |
| Layer 4 — Personal: "Không tìm thấy xe của tôi" · "Bỏ qua bước này" | #4 | Cuối danh sách và ở chrome |

**Visual Hierarchy**
1. **Ảnh xe ở Zone A** — hiện dần khi người dùng đi sâu 3 tầng. Đây là **bằng chứng** app hiểu đúng xe, nên nó phải là thứ mắt bắt đầu tiên khi đã có dữ liệu.
2. **Danh sách hãng/model/năm** — vùng tương tác lớn nhất, chiếm phần lớn màn hình. Row 50pt.
3. **CTA "Đúng xe của tôi"** — `${component.button.primary}`, cố định đáy, chỉ bật khi đủ 3 giá trị.
4. **Chrome**: ô tìm kiếm, `ProgressBar` 2/4, nút quay lại, dòng "Không tìm thấy xe của tôi", "Bỏ qua bước này".

*Self-check*: CTA cao 50pt với padding ngang `${spacing.xl}`=24 ⇒ đạt. CTA bị vô hiệu (nền `${color.palette.surfaceVariant}`) khi chưa đủ 3 giá trị ⇒ đạt. Mọi row ≥ 50pt > ngưỡng 44pt ⇒ đạt.

**Required Features (FR)**
- FR-004 P2: danh sách hãng sắp theo **mức phổ biến ở storefront**, lọc ≤ 200ms, on-device
- FR-004 P3–P5: picker 3 tầng ghim (sub-flow SF-002), hiện ảnh xe đối chiếu, bật CTA
- FR-004 P6: vào từ WF-006 (đổi xe) → ghim xe hiện tại đầu danh sách; **giữ nguyên** cấu hình widget/sound
- FR-004 VR-004.1: tìm kiếm khớp cả **tên viết tắt** và tên nội địa
- FR-004 BR-004.2: `trim`/`color` thuộc MVP 3 — **không** hiện lựa chọn rỗng
- FR-005 P2: thiếu asset ảnh → silhouette theo phân khúc + **nói rõ đang dùng ảnh chung**
- FR-006 (qua WF-021): dòng "Không tìm thấy xe của tôi" ở **cả ba tầng**

**UX Enhancements** (`composition.action.defaults`)
- `inline-validation`: CTA chỉ bật khi đủ hãng+model+năm; không có message lỗi vì không có input tự do
- `single-primary-cta`: đúng một CTA
- `escape-route-always-visible`: nút quay lại (chrome) + "Bỏ qua bước này" (Zone D) luôn thấy
- `progress-indicator`: `ProgressBar` 2/4
- Tầng đã chọn **ghim thành hàng 44pt** thay vì biến mất — người dùng luôn thấy mình đang ở đâu và lùi được (SF-002 P4)
- Haptic light mỗi lần xuống tầng, medium khi đủ 3 giá trị

**Content Zones Map**

```
┌─────────────────────────────────────┐
│ ZONE D: Navigation                  │ ← ${component.navBar.height}=44
│   [<]  Chọn xe của bạn              │   + ô tìm kiếm 50pt
│   [🔍 Tìm hãng hoặc model...]       │
├─────────────────────────────────────┤
│ ZONE A: Context / Summary           │ ← dynamic: 0 → ~140pt khi có ảnh xe
│   [ảnh xe] + hàng ghim 3 tầng       │   hàng ghim 44pt mỗi tầng
├─────────────────────────────────────┤
│ ZONE B: Input Area + Primary CTA    │ ← fill: danh sách + CTA đáy
│   Danh sách row 50pt · [Đúng xe...]│   CTA safeAreaInset bottom
├─────────────────────────────────────┤
│ ZONE C: — (unused cho Action)       │ ← height 0
└─────────────────────────────────────┘
```

**Layout** — *tầng 3 (đã chọn hãng + model, đang chọn năm)*

```
┌──────────────────────────────────────────────┐
│ navBar h=44 · bg rgba(242,243,240,0.85)      │ ZONE D
│ blur 20 · divider ${component.navBar.dividerColor}│
│  [<]        Chọn xe của bạn                  │ headline 17/600
├──────────────────────────────────────────────┤
│ ┌──────────────────────────────────────────┐ │ textField h=50 r=12
│ │ 🔍  Tìm hãng hoặc model…                 │ │ border ${color.palette.inputBorder}
│ └──────────────────────────────────────────┘ │
├──────────────────────────────────────────────┤
│ ┌──────────────────────────────────────────┐ │ ZONE A card r=16
│ │        [ ảnh Toyota Camry 2022 ]         │ │ ~140pt · shadow.1
│ │        crossfade 0.3s khi đổi            │ │ border 1px
│ └──────────────────────────────────────────┘ │
│  Toyota                              [đổi]  │ hàng ghim 44pt
│  ──────────────────────────────────────────  │ divider inset 16
│  Camry                               [đổi]  │ hàng ghim 44pt
├──────────────────────────────────────────────┤
│  Chọn năm                                    │ ZONE B
│  ${typography.scale.caption} textSecondary   │
│ ┌──────────────────────────────────────────┐ │
│ │  2024                                    │ │ row h=50
│ │  2023                                    │ │ mono cho SỐ
│ │ ▸2022                              ✓     │ │ chọn: accentSubtle
│ │  2021                                    │ │
│ │  2020                                    │ │
│ └──────────────────────────────────────────┘ │ scroll
│                                              │
│  Không tìm thấy xe của tôi                   │ BtnTertiary → WF-021
│  ${typography.scale.callout} accent          │ (hiện ở CẢ BA tầng)
├──────────────────────────────────────────────┤
│ .safeAreaInset(bottom):                      │
│ ┌──────────────────────────────────────────┐ │ h=50 r=16
│ │          Đúng xe của tôi                 │ │ bg accent (đã bật)
│ └──────────────────────────────────────────┘ │
│  Bỏ qua bước này        ▬▬▬▬▬▬▬▬▬▬▬▬▬░░░░░  │ ProgressBar 2/4
└──────────────────────────────────────────────┘
```

**Layout Variants** *(bắt buộc: Medium density)*

**Variant A — Tầng 1, chưa chọn gì (mặc định khi vào từ onboarding)**
```
┌──────────────────────────────────────────────┐
│ [<]  Chọn xe của bạn                         │
│ [🔍 Tìm hãng hoặc model…]                    │
├──────────────────────────────────────────────┤
│ ZONE A: rỗng (height 0) — chưa có ảnh xe     │ ← layout co lại
├──────────────────────────────────────────────┤
│  Hãng phổ biến                               │ sắp theo storefront,
│  ┌──────────────────────────────────────────┐│ KHÔNG theo chữ cái
│  │ Toyota                                   ││ row 50pt
│  │ Honda                                    ││
│  │ Ford                                     ││
│  │ BMW                                      ││
│  │ … (40+ hãng)                             ││
│  └──────────────────────────────────────────┘│
│  Không tìm thấy xe của tôi                   │
├──────────────────────────────────────────────┤
│ [        Đúng xe của tôi        ] ← VÔ HIỆU  │ bg surfaceVariant
│  Bỏ qua bước này       ▬▬▬▬▬▬▬░░░░░░░░░░░░  │ chữ textTertiary
└──────────────────────────────────────────────┘
```

**Variant B — Đổi xe (vào từ thẻ xe trên WF-006)**
```
┌──────────────────────────────────────────────┐
│ [Đóng]  Đổi xe                               │ ← "Đóng" thay "<",
│ [🔍 …]                                        │   KHÔNG có ProgressBar
├──────────────────────────────────────────────┤
│ ┌──────────────────────────────────────────┐ │ ảnh xe hiện NGAY
│ │      [ ảnh Toyota Camry 2022 ]           │ │ (đã có dữ liệu)
│ └──────────────────────────────────────────┘ │
│  ★ Xe hiện tại của bạn                       │ ghim đầu + đánh dấu
│  ┌──────────────────────────────────────────┐│
│  │ ▸Toyota Camry 2022               ✓ đang ││ accentSubtle
│  │  Toyota                                  ││
│  │  Honda                                   ││
│  └──────────────────────────────────────────┘│
├──────────────────────────────────────────────┤
│ [          Lưu thay đổi          ]           │ nhãn đổi
└──────────────────────────────────────────────┘
  Cấu hình widget và sound ĐƯỢC GIỮ (BR-004.3)
```

**Components**
- `NavBarStandard` — Tokens: `height: ${component.navBar.height}`(44), `background: ${component.navBar.background}`, `blur: ${component.navBar.blur}`(20), `dividerColor: ${component.navBar.dividerColor}`, title `${typography.scale.headline}`, icon 20pt medium.
- `TFSearch` — Tokens: `height: ${component.textField.height}`(50), `radius: ${component.textField.radius}`(12), `borderColor: ${component.textField.borderColor}`, `focusColor: ${component.textField.focusColor}`, `font: ${typography.scale.body}`.
- `CardVehiclePhoto` — Tokens: `radius: ${component.card.radius}`(16), `shadow: ${shadow.elevation.1}`, `border: 1px ${color.palette.border}`, crossfade `${animation.duration.slow}`(0.4).
- `PinnedTierRow` — hàng ghim tầng đã chọn. Tokens: `height: 44`, `background: ${color.palette.surface}`, divider `${component.divider}`, nhãn "đổi" `${typography.scale.caption}` accent.
- `RowSelectable` — Tokens: `height: ${component.row.height}`(50), selected background `${color.palette.accentSubtle}`, checkmark tint `${color.palette.accent}`. **Số năm dùng `${typography.family.mono}`**.
- `BtnPrimary` (Đúng xe của tôi) — trạng thái vô hiệu: `background: ${color.palette.surfaceVariant}`, `foreground: ${color.palette.textTertiary}`.
- `BtnTertiary` ×2 — "Không tìm thấy xe của tôi", "Bỏ qua bước này".
- `ProgressBarOnboard` — 2/4.

**States** (8)

| State | Loại | Context | Layout/Behavior |
|---|---|---|---|
| **First Visit** | user-context | Chưa chọn xe | **Variant A**: hãng theo mức phổ biến, Zone A rỗng, CTA vô hiệu |
| **Returning** | user-context | Đổi xe từ WF-006 | **Variant B**: xe hiện tại ghim đầu + đánh dấu, ảnh hiện ngay, nhãn CTA "Lưu thay đổi" |
| **Power User** | user-context | Xe nội địa / tên viết tắt | Tìm kiếm khớp tên viết tắt và tên nội địa (VR-004.1); không validate cứng theo danh sách |
| **Error** | user-context | Model không có asset ảnh (ERR-005.1) | Silhouette theo phân khúc ở Zone A + dòng **"đang dùng ảnh chung"**; CTA vẫn bật |
| **Default** | data | Dataset nạp xong | Layout như trên |
| **Loading** | data | Nạp dataset lần chạy đầu | Skeleton row ×6 (chiều cao 50pt, shimmer `${color.palette.surfaceVariant}`); ô tìm kiếm vô hiệu |
| **Empty** | data | Tìm kiếm không ra kết quả | "Không có kết quả cho «\<chuỗi\>»" + dòng "Không tìm thấy xe của tôi" được **nhấn mạnh** → WF-021 |
| **Offline** | data | Không có mạng | **Không ảnh hưởng** — dataset đóng gói sẵn on-device, tìm kiếm vẫn ≤ 200ms (AC-002.5) |

**User Flow**
- **Entry**: **WF-002** (onboarding bước 2) · thẻ xe trên **WF-006** (đổi xe)
- **Exit**: **WF-004** (onboarding) · **WF-006** (nếu vào từ Home) · **WF-021** (báo thiếu xe) · **WF-030** (toast sau khi WF-021 gửi)
- **Task Flow**: bước 3–4 của **TF-001**
- **Transitions**: tầng xuống bằng slide-in từ dưới `${animation.spring.smooth}`; tầng ghim thu lên 0,25s; ảnh xe crossfade 0,3s (SF-002)

---

### 3.4 WF-004 — Onboarding: Chọn Âm Thanh 📱 · *Template A (Discovery)*

**Design System**: `bento-grid`
**Archetype**: Discovery | **Secondary**: Action | **Density**: Medium (4 vùng)
**Source UC**: UC-006 (chính), UC-001 | **Source FR**: **FR-010** (danh mục + phân tầng), **FR-011** (nghe inline), **FR-013** (gán sound Connect)
**User Intent**: "Tôi muốn nghe xem app này nghe như thế nào."

**Action Layer → Visual Hierarchy**

| UC Action Layer | Slot | Ghi chú |
|---|---|---|
| Layer 1 — Primary: nghe thử và chọn sound cho lúc lên xe | **#3** | CTA "Dùng sound này" |
| Layer 2 — Contextual: chạm để nghe inline · dừng · chọn | **#2** | Danh sách preset — nơi người dùng dành thời gian |
| Layer 3 — Discovery: duyệt nhóm sound · xem preset Free vs khoá (**nghe thử được cả hai**) | #2, #4 | Header nhóm ở #4 |
| Layer 4 — Personal: "Chọn sau" (bỏ qua) | #4 | Chrome; hệ thống gán preset Free đầu tiên |

**Visual Hierarchy**
1. **Sound đang phát + waveform** — Zone A, `${component.waveform.height}`=40. Waveform chạy theo **tiến độ audio thật**, không phải animation giả — đây là bằng chứng app có tiếng thật.
2. **Danh sách preset theo nhóm** — vùng lớn nhất, row 50pt, nhãn Free/khoá rõ ràng.
3. **CTA "Dùng sound này"** — cố định đáy.
4. **Chrome**: `ProgressBar` 3/4, nút quay lại, "Chọn sau", header nhóm.

*Self-check*: Zone A (~120pt) không cao gấp 2× một row (50pt) nhưng cao gấp 2,4× ⇒ đạt. Header nhóm phân biệt bằng `${typography.scale.caption}` + `textSecondary` + không có divider trên ⇒ đạt.

**Required Features (FR)**
- FR-010 P3: `LockLabel` rõ ràng trên preset khoá — **không ẩn** preset khoá
- FR-010 BR-010.1: ≥ 12 preset, **đúng 3** preset Free
- FR-010 **BR-010.2**: preset khoá **nghe thử được toàn bộ**, không cắt, không watermark
- FR-011 P1–P4: phát ≤ 300ms, waveform theo tiến độ thật, chạm dòng khác **dừng ngay** dòng cũ
- FR-011 ERR-011.1/2/3: không phát chồng · phiên audio bị chiếm → nêu lý do tại chỗ · đang cắm tai nghe → nêu rõ trên xe sẽ phát qua loa xe
- FR-012 ERR-012.1 (dùng chung logic): đang phát nhạc → **ducking thật**
- FR-013 BR-013.2: "Chọn sau" → gán preset Free đầu tiên, **không** để trống
- SF-014: tự phát preset đầu tiên **một lần** khi vào màn

**UX Enhancements** (`composition.discovery.defaults`)
- `inline-audio-preview`: chạm dòng là phát, không mở sheet
- `section-grouping`: preset gom theo nhóm (Cổ điển / Hiện đại / Tối giản / Xe hơi)
- `skeleton-loading`: **không dùng** — asset trong bundle
- `pull-to-refresh`: **không dùng** — danh mục tĩnh; pull-to-refresh ở đây sẽ là affordance không có FR
- Ducking thật khi nghe thử (không phải nghe khô) — để bản nghe thử phản ánh đúng trải nghiệm trên xe
- Haptic light khi bắt đầu phát, medium khi gán

**Content Zones Map**

```
┌─────────────────────────────────────┐
│ ZONE D: Navigation                  │ ← ${component.navBar.height}=44
│   [<]  Chọn âm thanh lên xe         │
├─────────────────────────────────────┤
│ ZONE A: Hero — sound đang phát      │ ← ~120pt, static
│   Tên preset + waveform 40pt        │
├─────────────────────────────────────┤
│ ZONE C: Discovery Sections          │ ← header nhóm, ~24pt mỗi header
│   Nhóm: Cổ điển / Hiện đại / …      │
├─────────────────────────────────────┤
│ ZONE B: Main List                   │ ← fill, row 50pt, scroll
│   Row preset + nhãn Free/khoá       │
├─────────────────────────────────────┤
│ ZONE D: CTA + Chrome                │ ← CTA 50pt + ProgressBar 3/4
└─────────────────────────────────────┘
```

**Layout**

```
┌──────────────────────────────────────────────┐
│ navBar h=44                                  │ ZONE D
│  [<]     Chọn âm thanh lên xe                │
├──────────────────────────────────────────────┤
│ ┌──────────────────────────────────────────┐ │ ZONE A card r=16
│ │  Khởi Động Cổ Điển          ▶ đang phát  │ │ ~120pt shadow.1
│ │  ▁▃▅▇▆▄▂▁▃▅▇▅▃▁▂▄▆▇▅▃▁                  │ │ waveform h=40
│ │  bar 3px gap 2px · ${color.palette.accent}│ │ chạy theo audio THẬT
│ │  ♫ đang duck nhạc xuống 20%              │ │ caption textSecondary
│ └──────────────────────────────────────────┘ │
├──────────────────────────────────────────────┤
│  CỔ ĐIỂN                                     │ ZONE C header
│  caption 13/400 textSecondary                │ ~24pt
│ ┌──────────────────────────────────────────┐ │ ZONE B
│ │ ▸ Khởi Động Cổ Điển   1,2s    ✓ Free  ⏸ │ │ row 50pt
│ │   Tiếng Máy Ấm        1,8s      Free     │ │ số dùng mono
│ │   Chuông Nhẹ          0,9s      Free     │ │
│ └──────────────────────────────────────────┘ │
│  HIỆN ĐẠI                                    │
│ ┌──────────────────────────────────────────┐ │
│ │   Xung Điện           1,4s      🔒       │ │ LockLabel
│ │   Synth Lên Xe        2,1s      🔒       │ │ vẫn NGHE ĐƯỢC
│ │   Nhịp Tối            1,1s      🔒       │ │ ĐẦY ĐỦ
│ └──────────────────────────────────────────┘ │
│  XE HƠI                                      │
│ ┌──────────────────────────────────────────┐ │
│ │   V8 Khởi Động        2,4s      🔒       │ │
│ │   Turbo Spool         1,7s      🔒       │ │ … ≥12 preset
│ └──────────────────────────────────────────┘ │ scroll
├──────────────────────────────────────────────┤
│ .safeAreaInset(bottom):                      │ ZONE D
│ ┌──────────────────────────────────────────┐ │
│ │          Dùng sound này                  │ │ h=50 bg accent
│ └──────────────────────────────────────────┘ │
│  Chọn sau              ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬░░  │ ProgressBar 3/4
└──────────────────────────────────────────────┘
```

**Layout Variants** *(bắt buộc: Medium density)*

**Variant A — Preset khoá đang được nghe thử**
```
┌──────────────────────────────────────────────┐
│ ┌──────────────────────────────────────────┐ │
│ │  Synth Lên Xe    🔒         ▶ đang phát  │ │ nghe ĐẦY ĐỦ
│ │  ▁▃▅▇▆▄▂▁▃▅▇▅▃▁▂▄▆▇▅▃▁                  │ │ không cắt,
│ │  Preset này có ở gói Premium              │ │ không watermark
│ └──────────────────────────────────────────┘ │
│  … danh sách …                               │
├──────────────────────────────────────────────┤
│ ┌──────────────────────────────────────────┐ │ nhãn CTA đổi
│ │          Mở khoá                         │ │ nhưng KHÔNG mở
│ └──────────────────────────────────────────┘ │ paywall trong
│  Chọn sau              ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬░░  │ onboarding
└──────────────────────────────────────────────┘
  BR-001.1: chạm "Mở khoá" ở đây chỉ ghi nhận ý
  định và đi tiếp — paywall bị CẤM trong onboarding
```

**Variant B — Phiên audio bị chiếm (đang có cuộc gọi)**
```
┌──────────────────────────────────────────────┐
│ ┌──────────────────────────────────────────┐ │ ZONE A
│ │  Khởi Động Cổ Điển                       │ │ KHÔNG có waveform
│ │  ⚠ Không nghe thử được khi đang gọi      │ │ (VR-011.1: cấm hiện
│ │     [Thử lại]                            │ │  waveform khi không
│ └──────────────────────────────────────────┘ │  có tiếng)
│  … danh sách vẫn duyệt được bình thường …    │
├──────────────────────────────────────────────┤
│ [          Dùng sound này          ]         │ CTA VẪN hoạt động
│  Chọn sau              ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬░░  │ (ERR-011.2)
└──────────────────────────────────────────────┘
```

**Components**
- `NavBarStandard` — như WF-003.
- `CardNowPlaying` — Zone A. Tokens: `radius: ${component.card.radius}`(16), `padding: ${component.card.padding}`(16), `shadow: ${shadow.elevation.1}`.
- `WaveformLive` — Tokens: `height: ${component.waveform.height}`(40), `barWidth: 3`, `barGap: 2`, active `${color.palette.accent}`, inactive `${color.palette.textTertiary}`. **Chạy theo tiến độ audio thật** — không phải animation giả (VR-011.1).
- `RowSoundPreset` — Tokens: `height: ${component.row.height}`(50), `background: ${color.palette.surface}`, thời lượng dùng `${typography.family.mono}` + `${typography.scale.monoData}`.
- `LockLabel` — Tokens: `height: ${component.statusBadge.height}`(24), `radius: ${border.radius.full}`, `background: ${color.palette.surfaceVariant}`, `font: ${typography.scale.footnote}`.
- `SectionHeaderPlain` — Tokens: `font: ${typography.scale.caption}`, `color: ${color.palette.textSecondary}`, không divider.
- `BtnPrimary`, `BtnTertiary`, `ProgressBarOnboard` — như WF-002/003.

**States** (8)

| State | Loại | Context | Layout/Behavior |
|---|---|---|---|
| **First Visit** | user-context | Chưa nghe gì | Preset đầu tiên **tự phát một lần** (SF-014); người dùng biết ngay nút này làm gì |
| **Returning** | user-context | Vào lại từ WF-007, đã có sound | Sound hiện tại **ghim đầu** + đánh dấu "đang dùng" |
| **Power User** | user-context | Đang cắm tai nghe / đang phát nhạc | Áp dụng **ducking thật**; dòng nói rõ trên xe sẽ phát qua **loa xe** (ERR-011.3) |
| **Error** | user-context | Phiên audio bị chiếm | **Variant B**: lý do cụ thể + [Thử lại], **không** hiện waveform; danh sách vẫn duyệt được |
| **Default** | data | Danh mục nạp xong | Layout như trên, ≥ 12 preset, 3 Free |
| **Loading** | data | Chuẩn bị player | Row đang chọn hiện chỉ báo nhỏ ≤ 300ms; **không** skeleton toàn màn |
| **Empty** | data | Asset của một preset không nạp được (ERR-010.2) | Preset đó **bị loại khỏi danh sách** thay vì hiện dòng không phát được |
| **Offline** | data | Không có mạng | **Không ảnh hưởng** — asset trong bundle |

**User Flow**
- **Entry**: **WF-003** (onboarding bước 3)
- **Exit**: **WF-005** (tiếp tục) · **WF-020** (nếu người dùng mở sheet nghe kỹ — chỉ khả dụng từ WF-007, không từ onboarding)
- **Task Flow**: bước 5 của **TF-001**
- **Transitions**: push sang WF-005; waveform fade-in 0,2s **ngay khi audio bắt đầu**, không sớm hơn (SF-014)

---

### 3.5 WF-005 — Onboarding: Cấp Quyền 📱 · *Template B (Action)*

**Design System**: `bento-grid`
**Archetype**: Action | **Density**: Medium (4 vùng)
**Source UC**: UC-004 (chính), UC-001, UC-005 | **Source FR**: **FR-007** (trình bày lý do quyền), **FR-008** (suy giảm theo trạng thái quyền)
**User Intent**: "Tôi muốn biết app cần gì của tôi và để làm gì, trước khi tôi đồng ý."

**Action Layer → Visual Hierarchy**

| UC Action Layer | Slot | Ghi chú |
|---|---|---|
| Layer 1 — Primary: quyết định từng quyền rồi chạm "Tiếp tục" | **#3** | CTA luôn bấm được, kể cả khi chưa trả lời quyền nào (BR-001.2) |
| Layer 2 — Contextual: "Tìm hiểu thêm" → WF-022 · xem trạng thái từng quyền | **#2** | Hai thẻ quyền |
| Layer 3 — Discovery: xem ví dụ cụ thể app làm được gì khi có quyền | #2 | Nằm trong thẻ quyền |
| Layer 4 — Personal: "Bỏ qua tất cả" | #4 | **Luôn khả dụng, không bị làm mờ** (BR-007.3) |

**Visual Hierarchy**
1. **Câu cam kết "dữ liệu không rời thiết bị"** — Zone A, `${typography.scale.h3}`. Đặt trước cả thẻ quyền: ở một niche mà rating trung bình 2,2/5, câu này là thứ quyết định người dùng đọc tiếp hay bấm bừa.
2. **Hai thẻ quyền** — mỗi thẻ có lý do 1 dòng + một ví dụ cụ thể + trạng thái. Vùng tương tác chính.
3. **CTA "Tiếp tục"** — cố định đáy, **luôn bấm được**.
4. **Chrome**: `ProgressBar` 4/4, nút quay lại, "Bỏ qua tất cả".

*Self-check*: CTA 50pt + padding 24 ⇒ đạt. CTA **không** bị vô hiệu (khác WF-003) vì bỏ qua quyền là lựa chọn hợp lệ ⇒ đúng theo AC-004.5. Thẻ quyền cao ~104pt > 44pt ⇒ đạt.

**Required Features (FR)**
- FR-007 P1: thẻ quyền có lý do 1 dòng + ví dụ cụ thể + trạng thái (Đã cấp / Đã từ chối / Chưa hỏi)
- FR-007 **BR-007.1**: lý do phải cụ thể; **cấm** câu chung như "để cải thiện trải nghiệm"
- FR-007 P3: "Tìm hiểu thêm" → **WF-022** với biến thể đúng quyền đó
- FR-007 P4: quyền `notDetermined` → dialog iOS; quyền `denied` → nút đổi thành "Mở Cài đặt"
- FR-007 **BR-007.3**: "Bỏ qua tất cả" **luôn khả dụng, không bị làm mờ**
- FR-007 AC-004.4: quyền bị từ chối → hiện rõ **tính năng nào bị ảnh hưởng và ở mức nào**
- FR-008: mọi tổ hợp 9 trạng thái quyền đều hợp lệ và phải xử lý được

**UX Enhancements** (`composition.action.defaults`)
- `escape-route-always-visible`: "Bỏ qua tất cả" ở Zone D, cùng cấp thị giác với CTA nhưng nhỏ hơn
- `single-primary-cta`: một CTA
- `progress-indicator`: `ProgressBar` 4/4 — người dùng thấy đây là bước cuối
- `inline-validation`: **không áp dụng** (không có input tự do)
- Thứ tự đặt màn này **sau** WF-004: người dùng đã **nghe thấy giá trị** trước khi bị hỏi quyền — quyết định có chủ ý, ghi ở `Use_Cases.md` §4.5

**Content Zones Map**

```
┌─────────────────────────────────────┐
│ ZONE D: Navigation                  │ ← 44pt
│   [<]  Quyền truy cập               │
├─────────────────────────────────────┤
│ ZONE A: Context / Summary           │ ← ~72pt, static
│   Cam kết: dữ liệu không rời máy    │
├─────────────────────────────────────┤
│ ZONE B: Input Area + Primary CTA    │ ← fill: 2 thẻ quyền + CTA
│   PermissionCard ×2 (~104pt mỗi thẻ)│   CTA safeAreaInset
├─────────────────────────────────────┤
│ ZONE C: — (unused cho Action)       │ ← height 0
└─────────────────────────────────────┘
```

**Layout**

```
┌──────────────────────────────────────────────┐
│ navBar h=44                                  │ ZONE D
│  [<]        Quyền truy cập                   │
├──────────────────────────────────────────────┤
│  Dữ liệu của bạn không rời khỏi máy này.     │ ZONE A
│  ${typography.scale.h3} 22/600 textPrimary   │ ~72pt
│  Mọi thứ Carbina học đều nằm trên iPhone.    │ body textSecondary
├──────────────────────────────────────────────┤
│ ┌──────────────────────────────────────────┐ │ ZONE B
│ │ 📍 Vị trí                    Chưa hỏi   │ │ PermissionCard
│ │ ─────────────────────────────────────── │ │ r=16 p=16
│ │ Để nhận ra tuyến đường bạn hay đi và    │ │ shadow.1
│ │ gợi ý điểm đến trước khi bạn tìm.        │ │ body
│ │                                          │ │
│ │ Ví dụ: "Về nhà?" hiện sẵn lúc 18h.       │ │ callout accentSubtle
│ │                                          │ │
│ │  [Tìm hiểu thêm]        [Cho phép]       │ │ tertiary | secondary
│ └──────────────────────────────────────────┘ │ h=44 mỗi nút
│                                              │ ${spacing.md}
│ ┌──────────────────────────────────────────┐ │
│ │ 📅 Lịch                      Chưa hỏi   │ │
│ │ ─────────────────────────────────────── │ │
│ │ Để câu chào nhắc đúng cuộc họp sắp tới  │ │
│ │ thay vì chỉ nói "chào buổi sáng".        │ │
│ │                                          │ │
│ │ Ví dụ: "Họp 8:30 ở văn phòng — đi thôi." │ │
│ │                                          │ │
│ │  [Tìm hiểu thêm]        [Cho phép]       │ │
│ └──────────────────────────────────────────┘ │
├──────────────────────────────────────────────┤
│ .safeAreaInset(bottom):                      │ ZONE B (CTA)
│ ┌──────────────────────────────────────────┐ │
│ │            Tiếp tục                      │ │ h=50 bg accent
│ └──────────────────────────────────────────┘ │ LUÔN bấm được
│  Bỏ qua tất cả         ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬  │ ProgressBar 4/4
│  callout accent · KHÔNG làm mờ               │
└──────────────────────────────────────────────┘
```

**Layout Variants** *(bắt buộc: Medium density)*

**Variant A — Một quyền đã bị từ chối (nêu rõ tính năng bị ảnh hưởng)**
```
┌──────────────────────────────────────────────┐
│ ┌──────────────────────────────────────────┐ │
│ │ 📍 Vị trí                  Đã từ chối   │ │ trạng thái đổi
│ │ ─────────────────────────────────────── │ │
│ │ ⚠ Ảnh hưởng: âm thanh "Tới nơi" sẽ      │ │ AC-004.4:
│ │   không khả dụng; dashboard không có     │ │ nêu RÕ tính năng
│ │   thẻ gợi ý điểm đến.                    │ │ nào và ở MỨC nào
│ │   Widget, sound lên/xuống xe và giọng    │ │ semantic.warning
│ │   chào theo giờ vẫn hoạt động đầy đủ.    │ │
│ │                                          │ │
│ │  [Tìm hiểu thêm]      [Mở Cài đặt]      │ │ nút ĐỔI NHÃN
│ └──────────────────────────────────────────┘ │ (iOS không cho
│  … thẻ Lịch …                                │  hỏi lại lần hai)
├──────────────────────────────────────────────┤
│ [            Tiếp tục            ]           │ VẪN bấm được
└──────────────────────────────────────────────┘
```

**Variant B — Đã cấp cả hai quyền**
```
┌──────────────────────────────────────────────┐
│ ┌──────────────────────────────────────────┐ │
│ │ 📍 Vị trí                    ✓ Đã cấp   │ │ semantic.success
│ │ Tuyến đường sẽ được học trên máy này.    │ │ card thu gọn:
│ └──────────────────────────────────────────┘ │ bỏ ví dụ và nút,
│ ┌──────────────────────────────────────────┐ │ chỉ còn 1 dòng
│ │ 📅 Lịch                      ✓ Đã cấp   │ │ (~56pt thay 104pt)
│ │ Câu chào sẽ nhắc cuộc họp sắp tới.       │ │
│ └──────────────────────────────────────────┘ │ mật độ GIẢM khi
├──────────────────────────────────────────────┤ người dùng đã xong
│ [            Tiếp tục            ]           │
│  Bỏ qua tất cả  → ẨN (không còn ý nghĩa)     │
└──────────────────────────────────────────────┘
```

**Components**
- `NavBarStandard` — như WF-003.
- `PermissionCard` — Tokens: `radius: ${component.card.radius}`(16), `padding: ${component.card.padding}`(16), `shadow: ${shadow.elevation.1}`, `border: 1px ${color.palette.border}`. Trạng thái: Chưa hỏi → `${color.palette.textSecondary}`; Đã cấp → `${color.semantic.success.color}` + background `${color.semantic.success.background}`; Đã từ chối → `${color.semantic.warning.color}` + background `${color.semantic.warning.background}`.
- `ExampleChip` — ví dụ câu chào. Tokens: `background: ${color.palette.accentSubtle}`, `radius: ${border.radius.md}`(8), `font: ${typography.scale.callout}`.
- `BtnSecondary` ("Cho phép" / "Mở Cài đặt") — Tokens: `height: 44`, `radius: ${border.radius.lg}`(16), `borderWidth: 1`, `borderColor: ${color.palette.border}`, `background: ${color.palette.surface}`.
- `BtnTertiary` ("Tìm hiểu thêm", "Bỏ qua tất cả") — `foreground: ${color.palette.accent}`.
- `BtnPrimary` ("Tiếp tục") — **không có trạng thái vô hiệu** ở màn này.
- `ProgressBarOnboard` — 4/4.

**States** (8)

| State | Loại | Context | Layout/Behavior |
|---|---|---|---|
| **First Visit** | user-context | Chưa hỏi quyền nào | Cả hai thẻ "Chưa hỏi"; CTA **đã bấm được** |
| **Returning** | user-context | Vào lại từ WF-012 (qua FR-062) | Thẻ hiện trạng thái thật; quyền `denied` → nút "Mở Cài đặt"; **không** có `ProgressBar` |
| **Power User** | user-context | Cấp Vị trí ở mức "Khi dùng app" | Nêu rõ **tuyến đường chỉ học được khi app đang mở** (ERR-008.3) — không im lặng |
| **Error** | user-context | Dialog quyền iOS không mở được (ERR-007.4) | Nêu rõ + dẫn Cài đặt hệ thống; CTA **vẫn** bấm được |
| **Default** | data | Trạng thái quyền đọc xong | Layout như trên |
| **Loading** | data | Đang chờ người dùng trả lời dialog iOS | Nút "Cho phép" hiện trạng thái chờ; phần còn lại của thẻ **không** bị vô hiệu |
| **Empty** | data | Không áp dụng — luôn có đúng 2 quyền | Trạng thái này **không tồn tại có chủ ý** |
| **Offline** | data | Không có mạng | **Không ảnh hưởng** — quyền là API hệ thống, không cần mạng |

**User Flow**
- **Entry**: **WF-004** (onboarding bước 4) · dòng "Quyền" trên **WF-012** (qua FR-062)
- **Exit**: **WF-006** (hoàn tất) · **WF-022** ("Tìm hiểu thêm") · Cài đặt hệ thống iOS (quyền đã `denied`)
- **Task Flow**: bước 6–7 của **TF-001**; toàn bộ **TF-011** bắt đầu từ đây khi chọn "Bỏ qua tất cả"
- **Transitions**: push sang WF-006; thẻ quyền thu gọn từ 104pt → 56pt bằng `${animation.spring.smooth}` khi quyền được cấp (Variant B)

---

### 3.6 WF-006 — Home (iPhone) 📱 · *Template D (Management)*

**Design System**: `bento-grid`
**Archetype**: Management | **Secondary**: Discovery | **Density**: **Dense** (7 vùng tương tác)
**Source UC**: UC-024 (chính), UC-001, UC-002, UC-005, UC-007, UC-008, UC-012, UC-016, UC-017, UC-018, UC-027
**Source FR**: **FR-009** (làm mới trạng thái), **FR-021** (đổi widget nhanh), **FR-031** (cảnh báo render), **FR-044** (badge gói Free), **FR-051** (badge trial)
**User Intent**: "Tôi muốn biết mọi thứ đang ở trạng thái nào và sửa nhanh thứ tôi cần."

**Action Layer → Visual Hierarchy**

| UC Action Layer | Slot | Ghi chú |
|---|---|---|
| Layer 1 — Primary: xem trạng thái kết nối + trạng thái từng thành phần | **#1** | Đây là màn hình **để đọc**, không để hành động — Primary là hành vi đọc, nên nó chiếm slot #1 thay vì #3. Sai lệch có chủ ý, xem §Notes |
| Layer 2 — Contextual: chạm thẻ widget/sound/giọng chào/xe | **#2** | Bốn thẻ là vùng tương tác chính |
| Layer 3 — Discovery: thẻ "Chưa thử trên xe?" · gợi ý tính năng chưa dùng | #3 | Chỉ hiện khi còn tính năng chưa dùng |
| Layer 4 — Personal: badge gói · lối vào WF-012 · lối vào WF-014 khi có cảnh báo | #4 | Chrome + tab bar |

> **§Notes — sai lệch có chủ ý**: skill quy định Layer 1 phải ở slot #3 (CTA tương phản cao nhất sau hero). WF-006 **không có CTA** — Primary Action của nó là *xem trạng thái*. Gán một CTA giả vào đây để thoả quy tắc sẽ tạo affordance không có FR. Vì vậy Layer 1 → #1 (thẻ trạng thái kết nối là hero), và slot #3 thuộc Layer 3.

**Visual Hierarchy**
1. **Thẻ trạng thái kết nối CarPlay + ảnh xe** — card lớn nhất, `${component.card.heroHeight}`~200pt. Câu trả lời cho câu hỏi duy nhất người dùng mở app để hỏi: *"app đang chạy chứ?"*
2. **Thẻ widget đang dùng** — card lớn thứ hai. Đây là thứ người dùng thật sự trả tiền để thấy.
3. **Hai thẻ nhỏ song song: sound · giọng chào** — `${component.card.compactHeight}`=88pt, chia đôi chiều ngang.
4. **Chrome**: nav bar, tab bar 4 tab, badge gói ở Zone D, `WarningRow` cảnh báo tương thích (chỉ khi có).

*Self-check*: hero (200pt) cao gấp 2,3× thẻ nhỏ (88pt) ⇒ đạt. Người dùng biết app có chạy hay không trong < 1s vì đó là dòng đầu của hero ⇒ đạt. Không có CTA nên quy tắc tương phản CTA không áp dụng — đã ghi lý do ở §Notes.

**Required Features (FR)**
- FR-009 P5: kéo xuống > 60pt → đọc lại trạng thái kết nối + kết quả render (SF-001)
- FR-009 P6 / FR-031 P5: có `widget_render_failed` → hiện `WarningRow` dẫn WF-014
- FR-009 **BR-009.3** / FR-031 ERR-031.1: `WarningRow` **tự xoá** khi render kế tiếp thành công
- FR-021 P6: chạm thẻ widget → đổi nhanh, 2 chạm là xong
- FR-044 P5: `StatusBadge` gói hiện tại — nói "bạn đang có gì"
- FR-051 P2: `StatusBadge` "Trial còn N ngày" **kèm ngày trừ tiền**, tông trung tính
- FR-002 P4 / FR-001: thẻ "Hoàn tất thiết lập" nếu bỏ dở onboarding
- FR-008 P6: tối đa **một** `StaticNotice` mời cấp quyền, dạng tĩnh, **không popup**

**UX Enhancements** (`composition.management.defaults`)
- `grouped-rows` → ở đây là **grouped cards** (Bento): nhóm theo chủ đề, không phải danh sách phẳng
- `inline-status-on-row`: mỗi thẻ hiện trạng thái ngay trên thẻ, không cần mở ra mới biết
- `pull-to-refresh`: SF-001 — làm mới trạng thái kết nối; chỉ báo fade-in 0,2s
- `destructive-needs-confirm`: **không áp dụng** (màn này không có hành động phá hủy)
- Cảnh báo tự thu hồi: fade-out 0,4s — **chậm hơn** lúc vào (0,3s), để người dùng kịp nhận ra nó đã hết

**Content Zones Map**

```
┌─────────────────────────────────────┐
│ ZONE D: Navigation                  │ ← ${component.navBar.height}=44
│   Carbina                    [⚙]   │
├─────────────────────────────────────┤
│ ZONE B: Actionable Card Stack       │ ← fill, scroll, .refreshable
│   ┌ hero: trạng thái + ảnh xe ┐    │   heroHeight ~200pt
│   ┌ widget đang dùng           ┐    │   ~160pt
│   ┌ sound ┐ ┌ giọng chào ┐         │   compactHeight 88pt ×2
│   ┌ gợi ý (điều kiện)         ┐    │   ~72pt
├─────────────────────────────────────┤
│ ZONE D: Warning + Tab Bar           │ ← WarningRow 50pt (điều kiện)
│   [⚠ dẫn WF-014]                    │   + tabBar 49pt (+34 safe)
│   [Home][Sounds][Widget][Cài đặt]   │
├─────────────────────────────────────┤
│ ZONE A / ZONE C: — (unused)         │ ← Management archetype không dùng
└─────────────────────────────────────┘
```

**Layout**

```
┌──────────────────────────────────────────────┐
│ navBar h=44 blur 20                          │ ZONE D
│  Carbina                              [⚙]   │ headline · icon 20pt
├──────────────────────────────────────────────┤
│ ScrollView .refreshable {                    │ ZONE B (fill)
│ ┌──────────────────────────────────────────┐ │ card r=16 p=16
│ │ ● Đã kết nối CarPlay                     │ │ ~200pt shadow.1
│ │   semantic.success.color                 │ │ border 1px
│ │   Lần cuối: 07:42 hôm nay · render OK    │ │ caption mono
│ │                                          │ │
│ │      [ ảnh Toyota Camry 2022 ]           │ │
│ │                                          │ │
│ │   Toyota Camry 2022              [đổi >] │ │ row 44pt → WF-003
│ └──────────────────────────────────────────┘ │
│                                              │ ${spacing.md}=12
│ ┌──────────────────────────────────────────┐ │
│ │ WIDGET ĐANG DÙNG                    [>]  │ │ ~160pt
│ │ caption textSecondary                    │ │ → WF-008 (2 chạm)
│ │ ┌────────────────────────────────────┐   │ │
│ │ │   [preview widget tỉ lệ xe]        │   │ │ dùng cùng engine
│ │ └────────────────────────────────────┘   │ │ với FR-029
│ │ Ảnh xe · 142 chuyến                      │ │ số dùng mono
│ └──────────────────────────────────────────┘ │
│                                              │
│ ┌───────────────────┐ ┌────────────────────┐│ compactHeight 88
│ │ ÂM THANH      [>] │ │ GIỌNG CHÀO    [>] ││ chia đôi, gap 12
│ │ Khởi Động Cổ Điển │ │ ● Đang bật         ││ → WF-007 / WF-009
│ │ 3 sự kiện đã gán  │ │ 4 nguồn ngữ cảnh   ││ StatusRow chỉ đọc
│ └───────────────────┘ └────────────────────┘│
│                                              │
│ ┌──────────────────────────────────────────┐ │ Layer 3 (điều kiện)
│ │ 💡 Chưa thử giọng chào trên xe?     [>]  │ │ ~72pt
│ │    accentSubtle bg                        │ │ ẩn khi đã dùng hết
│ └──────────────────────────────────────────┘ │
│ }                                            │
├──────────────────────────────────────────────┤
│ ⚠ Widget chưa hiện đúng trên xe của bạn  [>] │ WarningRow 50pt
│   semantic.warning · → WF-014                │ CHỈ khi có lỗi
├──────────────────────────────────────────────┤
│ tabBar h=49 (+34 safe) blur 20               │ ZONE D
│  [🏠 Home] [♫ Sounds] [▦ Widget] [⚙ Cài đặt]│ active accent
│   ●Free                                      │ badge gói
└──────────────────────────────────────────────┘
```

**Layout Variants** *(bắt buộc: Dense density)*

**Variant A — Chưa cắm xe lần nào (First Visit)**
```
┌──────────────────────────────────────────────┐
│  Carbina                              [⚙]   │
├──────────────────────────────────────────────┤
│ ┌──────────────────────────────────────────┐ │ hero ĐỔI nội dung
│ │ ○ Chưa kết nối CarPlay                   │ │ textSecondary
│ │   Cắm iPhone vào xe để xem widget         │ │
│ │   hoạt động — không cần trả tiền.         │ │
│ │      [ ảnh Toyota Camry 2022 ]           │ │
│ │   Toyota Camry 2022              [đổi >] │ │
│ └──────────────────────────────────────────┘ │
│ ┌──────────────────────────────────────────┐ │ Layer 3 ĐƯỢC
│ │ 🚗 Cắm xe lần đầu để xem widget     [>]  │ │ NHẤN MẠNH
│ │    accentSubtle · hướng dẫn 3 bước        │ │ (thẻ mời thử)
│ └──────────────────────────────────────────┘ │
│ ┌ WIDGET ĐANG DÙNG ┐ ┌ ÂM THANH ┐ …         │
│  KHÔNG có WarningRow (chưa có dữ liệu render)│
└──────────────────────────────────────────────┘
```

**Variant B — Trial đang chạy + đã cấu hình đầy đủ (Power User)**
```
┌──────────────────────────────────────────────┐
│  Carbina                              [⚙]   │
├──────────────────────────────────────────────┤
│ ┌ ● Đã kết nối · render OK · ảnh xe ────────┐│ hero như mặc định
│ ┌ WIDGET ĐANG DÙNG ─────────────────────────┐│
│ ┌ ÂM THANH ┐ ┌ GIỌNG CHÀO ┐                 │
│  ✗ KHÔNG có thẻ gợi ý Layer 3                │ mật độ GIẢM khi
│    (đã dùng hết tính năng)                   │ người dùng thành thạo
├──────────────────────────────────────────────┤
│ tabBar                                       │
│  ●Trial còn 3 ngày · trừ 29,99 $ vào 20/08  │ StatusBadge
│   accentSubtle · KHÔNG đếm ngược gây áp lực  │ số dùng mono
└──────────────────────────────────────────────┘
```

**Components**
- `NavBarStandard` — như WF-003; icon `⚙` 20pt medium → WF-012.
- `CardConnectionStatus` (hero) — Tokens: `radius: 16`, `padding: 16`, `shadow: ${shadow.elevation.1}`, `border: 1px ${color.palette.border}`, height `${component.card.heroHeight}`~200. Chấm trạng thái: `${color.semantic.success.color}` (đã kết nối) / `${color.palette.textSecondary}` (chưa).
- `CardWidgetPreview` — Tokens: `radius: 16`, `shadow: ${shadow.elevation.1}`. Preview dùng **cùng layout engine** với FR-029 — nếu dùng engine khác thì preview sẽ nói dối.
- `CardCompactStatus` ×2 — Tokens: `height: ${component.card.compactHeight}`(88), `radius: 16`, `padding: 16`, gap `${spacing.md}`(12).
- `CardSuggestion` — Tokens: `background: ${color.palette.accentSubtle}`, `radius: 16`, `height: ~72`.
- `WarningRow` — Tokens: `height: ${component.row.height}`(50), `background: ${color.semantic.warning.background}`, `foreground: ${color.semantic.warning.color}`, slide-in 0,3s / fade-out **0,4s**.
- `TabBarCustom` — Tokens: `height: ${component.tabBar.height}`(49), `heightWithSafeArea: 83`, `background: ${component.tabBar.background}`, `blur: 20`, active `${color.palette.accent}`, inactive `${color.palette.textTertiary}`, icon 24pt, label `${typography.scale.footnote}`.
- `StatusBadge` — Tokens: `height: ${component.statusBadge.height}`(24), `radius: full`, `font: ${typography.scale.footnote}`; số dùng mono.
- `PullToRefreshIndicator` — Tokens: tint `${color.palette.accent}`, fade-in `${animation.duration.fast}`(0,15s).

**States** (9)

| State | Loại | Context | Layout/Behavior |
|---|---|---|---|
| **First Visit** | user-context | Vừa onboard, chưa cắm xe | **Variant A**: hero "Chưa kết nối" + hướng dẫn cắm xe; thẻ mời thử được nhấn mạnh; không `WarningRow` |
| **Returning** | user-context | Đã cắm xe ≥ 1 lần | Hero hiện lần kết nối gần nhất + kết quả render; thẻ gợi ý biến mất dần khi dùng hết |
| **Power User** | user-context | Premium/trial, cấu hình đầy đủ | **Variant B**: **không** thẻ mời/gợi ý — mật độ giảm khi người dùng thành thạo |
| **Error** | user-context | Có `widget_render_failed` ở phiên gần nhất | `WarningRow` ở Zone D dẫn WF-014; **tự xoá** khi render kế tiếp OK (BR-009.3) |
| **Default** | data | Mọi dữ liệu sẵn sàng | Layout như trên |
| **Loading** | data | Pull-to-refresh đang chạy (SF-001) | `PullToRefreshIndicator`; thẻ trạng thái **giữ giá trị cũ** trong lúc chờ, không hiện skeleton |
| **Empty** | data | Bỏ dở onboarding (thiếu `selectedVehicle`) | Thẻ "Hoàn tất thiết lập" ở đầu Zone B (FR-002 P4), bỏ qua được; hero hiện trạng thái tối giản |
| **Offline** | data | Không có mạng | **Không ảnh hưởng** — mọi trạng thái đọc từ App Group; pull-to-refresh vẫn chạy |
| **Refresh Error** | data | Làm mới thất bại (ERR-009.2) | **Giữ giá trị cũ** + dòng "chưa cập nhật được"; **không** hiện trạng thái rỗng |

**User Flow**
- **Entry**: **WF-001** (đã onboard) · **WF-005** (hoàn tất onboarding) · tab Home từ mọi tab · quay lại từ mọi màn con
- **Exit**: **WF-003** (thẻ xe) · **WF-007** (thẻ sound) · **WF-008** (thẻ widget) · **WF-009** (thẻ giọng chào) · **WF-012** (⚙ hoặc tab Cài đặt) · **WF-014** (`WarningRow`) · **WF-010** (badge gói Free)
- **Task Flow**: bước 8 của **TF-001** · bước 7 của **TF-002** · bước 3 của **TF-003** · bước 1 của **TF-004**, **TF-005** · bước 1 của **TF-007**
- **Transitions**: push cho mọi màn con; `WarningRow` slide-in 0,3s / fade-out 0,4s; thẻ trạng thái crossfade 0,25s sau refresh

---

### 3.7 WF-007 — Thư Viện Âm Thanh 📱 · *Template A (Discovery)*

**Design System**: `bento-grid`
**Archetype**: Discovery | **Secondary**: Action | **Density**: **Dense** (6 vùng)
**Source UC**: UC-006 (chính), UC-007, UC-008, UC-009, UC-024, UC-025
**Source FR**: **FR-010** (danh mục + phân tầng), **FR-011** (nghe inline), **FR-013** (gán Connect), **FR-014** (gán Disconnect/Arrive), **FR-015** (lối vào âm lượng)
**User Intent**: "Tôi muốn nghe hết các lựa chọn rồi chọn cái nghe hay nhất trên xe của tôi."

**Action Layer → Visual Hierarchy**

| UC Action Layer | Slot | Ghi chú |
|---|---|---|
| Layer 1 — Primary: nghe thử một preset và gán nó cho một sự kiện | **#3** | CTA nhãn động theo sự kiện đang chọn |
| Layer 2 — Contextual: chạm dòng nghe inline · mở WF-020 · gán · dừng | **#2** | Danh sách preset |
| Layer 3 — Discovery: `SegmentedControl` 3 sự kiện · duyệt nhóm · xem preset khoá | **#4** (segmented) + #2 (nhóm) | Segmented ở chrome |
| Layer 4 — Personal: nút âm lượng thanh trên · preset "đang dùng" ghim đầu | #4 | Lối vào WF-012, không phải nơi điều chỉnh |

**Visual Hierarchy**
1. **Sound đang phát + waveform** — Zone A card, ~120pt.
2. **Danh sách preset theo nhóm** — Zone B, vùng lớn nhất, row 50pt.
3. **CTA gán (nhãn động)** — cố định đáy: "Dùng cho lúc lên xe" / "…xuống xe" / "…tới nơi".
4. **Chrome**: nav bar + nút âm lượng, `SegmentedControl` 3 sự kiện, header nhóm, `LockLabel`.

*Self-check*: Zone A (120pt) cao gấp 2,4× row ⇒ đạt. Header nhóm phân biệt bằng caption + textSecondary ⇒ đạt. CTA tương phản cao nhất sau Zone A ⇒ đạt.

**Required Features (FR)**
- FR-010 P3–P6: nhãn khoá rõ ràng, preset đang dùng ghim đầu, nghe thử **mọi** preset, chạm preset khoá → WF-010 kèm ngữ cảnh
- FR-011 P1–P6: phát ≤ 300ms, waveform theo tiến độ thật, chạm dòng khác dừng ngay dòng cũ, chạm lại để dừng
- FR-013 P1–P6: gán sound Connect, ghi App Group ngay, "Không dùng" là lựa chọn hợp lệ **không nhắc nhở**
- FR-014 P1–P3: `SegmentedControl` **giữ nguyên vị trí cuộn** khi đổi sự kiện (SF-006); Arrive **vô hiệu kèm lý do** khi thiếu quyền Vị trí
- FR-015 P1: nút âm lượng ở thanh trên là **lối vào**, không phải nơi điều chỉnh

**UX Enhancements** (`composition.discovery.defaults`)
- `inline-audio-preview`: chạm dòng là phát (SF-003)
- `section-grouping`: 4 nhóm preset
- `pull-to-refresh`: **không dùng** — danh mục tĩnh; sẽ là affordance không có FR
- `skeleton-loading`: chỉ ở state Loading của lần nạp danh mục đầu
- Đổi sự kiện dùng **crossfade nhãn + dấu**, danh sách **không trượt ngang** — trượt ngang làm mất vị trí cuộn (SF-006)
- Haptic light khi phát/đổi sự kiện, medium khi gán

**Content Zones Map**

```
┌─────────────────────────────────────┐
│ ZONE D: Navigation + Tools          │ ← navBar 44 + segmented 36
│   [<] Âm thanh          [🔊 âm lượng]│
│   [Lên xe][Xuống xe][Tới nơi]        │
├─────────────────────────────────────┤
│ ZONE A: Hero — đang phát            │ ← ~120pt
├─────────────────────────────────────┤
│ ZONE C: Discovery Sections          │ ← header nhóm ~24pt ×4
├─────────────────────────────────────┤
│ ZONE B: Main List                   │ ← fill, row 50pt
├─────────────────────────────────────┤
│ ZONE D: CTA nhãn động               │ ← 50pt safeAreaInset
└─────────────────────────────────────┘
```

**Layout** — *sự kiện "Lên xe" đang chọn*

```
┌──────────────────────────────────────────────┐
│ navBar h=44                                  │ ZONE D
│  [<]     Âm thanh            [🔊]            │ → WF-012 (âm lượng)
│ ┌──────────────────────────────────────────┐ │ segmented h=36 r=12
│ │ ▸Lên xe✓│ Xuống xe✓│ Tới nơi🔒          │ │ bg surfaceVariant
│ └──────────────────────────────────────────┘ │ selected: surface
├──────────────────────────────────────────────┤
│ ┌──────────────────────────────────────────┐ │ ZONE A ~120pt
│ │  Tiếng Máy Ấm                ⏸ đang phát │ │
│ │  ▁▃▅▇▆▄▂▁▃▅▇▅▃▁▂▄▆▇▅▃▁                  │ │ waveform THẬT
│ │  ♫ đang duck nhạc xuống 20%              │ │
│ └──────────────────────────────────────────┘ │
├──────────────────────────────────────────────┤
│  ★ ĐANG DÙNG                                 │ ZONE C
│ ┌──────────────────────────────────────────┐ │ preset đang dùng
│ │ ▸ Khởi Động Cổ Điển  1,2s  Free   ✓ đang│ │ GHIM ĐẦU
│ └──────────────────────────────────────────┘ │ accentSubtle
│  CỔ ĐIỂN                                     │
│ ┌──────────────────────────────────────────┐ │ ZONE B
│ │   Tiếng Máy Ấm       1,8s  Free      ⏸  │ │ row 50pt
│ │   Chuông Nhẹ         0,9s  Free          │ │ số mono
│ └──────────────────────────────────────────┘ │
│  HIỆN ĐẠI                                    │
│ ┌──────────────────────────────────────────┐ │
│ │   Xung Điện          1,4s  🔒            │ │ chạm = nghe ĐẦY ĐỦ
│ │   Synth Lên Xe       2,1s  🔒            │ │ nút gán → "Mở khoá"
│ └──────────────────────────────────────────┘ │
│  TỐI GIẢN / XE HƠI … (≥12 preset)            │ scroll
├──────────────────────────────────────────────┤
│ ┌──────────────────────────────────────────┐ │ ZONE D
│ │       Dùng cho lúc lên xe                │ │ h=50 bg accent
│ └──────────────────────────────────────────┘ │ NHÃN ĐỘNG
│         Không dùng sound cho sự kiện này      │ BtnTertiary
└──────────────────────────────────────────────┘
```

**Layout Variants** *(bắt buộc: Dense density)*

**Variant A — Sự kiện "Tới nơi" khi thiếu quyền Vị trí**
```
┌──────────────────────────────────────────────┐
│ ┌──────────────────────────────────────────┐ │
│ │  Lên xe✓│ Xuống xe✓│ ▸Tới nơi           │ │
│ └──────────────────────────────────────────┘ │
├──────────────────────────────────────────────┤
│ ┌──────────────────────────────────────────┐ │ semantic.warning
│ │ ⚠ "Tới nơi" cần quyền Vị trí              │ │ thay Zone A
│ │   Không có quyền thì app không biết bạn   │ │
│ │   đã tới nơi, nên âm thanh này sẽ không   │ │ nêu RÕ lý do
│ │   bao giờ phát.                           │ │ tại chỗ
│ │              [Cấp quyền Vị trí]           │ │ → WF-022
│ └──────────────────────────────────────────┘ │
│  … danh sách vẫn NGHE THỬ được bình thường … │ nghe được,
├──────────────────────────────────────────────┤ gán thì không
│ [    Dùng cho lúc tới nơi    ] ← VÔ HIỆU     │ bg surfaceVariant
└──────────────────────────────────────────────┘  (VR-014.1)
```

**Variant B — Gói Free, đang nghe preset khoá**
```
┌──────────────────────────────────────────────┐
│ ┌──────────────────────────────────────────┐ │
│ │  Synth Lên Xe  🔒        ⏸ đang phát     │ │ ĐẦY ĐỦ, không cắt
│ │  ▁▃▅▇▆▄▂▁▃▅▇▅▃▁▂▄▆▇▅▃▁                  │ │ không watermark
│ │  Preset này có ở gói Premium              │ │
│ └──────────────────────────────────────────┘ │
│  ★ ĐANG DÙNG                                 │
│  … 3 preset Free có nhãn "Đang dùng được" …  │ LockLabel rõ ràng,
│  … 9+ preset khoá có 🔒 …                    │ KHÔNG ẩn
├──────────────────────────────────────────────┤
│ ┌──────────────────────────────────────────┐ │
│ │            Mở khoá                       │ │ → WF-010 với
│ └──────────────────────────────────────────┘ │ trigger_source =
│         Không dùng sound cho sự kiện này      │ sound_preset
└──────────────────────────────────────────────┘
```

**Components**
- `NavBarStandard` + `IconButtonVolume` (🔊) — Tokens: icon 20pt, tint `${color.palette.textPrimary}` → lối vào WF-012.
- `SegmentedControl3` — Tokens: `height: ${component.segmentedControl.height}`(36), `radius: 12`, `background: ${color.palette.surfaceVariant}`, selected `${color.palette.surface}`, `font: ${typography.scale.caption}`. Đổi tab: **crossfade 0,2s nhãn + dấu**, danh sách **không** trượt.
- `CardNowPlaying` + `WaveformLive` — như WF-004.
- `RowSoundPreset` + `LockLabel` — như WF-004; thêm biến thể "đang dùng": background `${color.palette.accentSubtle}` + `✓`.
- `SectionHeaderPlain` — như WF-004.
- `BtnPrimary` nhãn động — 3 nhãn theo sự kiện; trạng thái vô hiệu `background: ${color.palette.surfaceVariant}`.
- `BtnTertiary` ("Không dùng sound cho sự kiện này").
- `CardPermissionInline` (Variant A) — Tokens: `background: ${color.semantic.warning.background}`, `foreground: ${color.semantic.warning.color}`, `radius: 16`.

**States** (9)

| State | Loại | Context | Layout/Behavior |
|---|---|---|---|
| **First Visit** | user-context | Mới có 1 sound từ onboarding | Sound đã gán ghim đầu; các nhóm khác mở để khuyến khích nghe thử |
| **Returning** | user-context | Đã gán cả 3 sự kiện | `SegmentedControl` hiện `✓` ở từng sự kiện; mở ở sự kiện gần nhất |
| **Power User** | user-context | Nghe thử liên tục nhiều preset | Chạm dòng khác **dừng ngay** dòng cũ, không phát chồng, không cần chạm dừng |
| **Free tier** | user-context | Entitlement = Free | **Variant B**: 3 preset nhãn "Đang dùng được"; preset khoá nghe **đầy đủ**; CTA → "Mở khoá" |
| **Error** | user-context | Phiên audio bị chiếm (ERR-011.2) | Dòng hiện lý do tại chỗ, giữ icon tĩnh; **không** waveform; danh sách vẫn duyệt |
| **Default** | data | Danh mục nạp xong | Layout như trên |
| **Loading** | data | Nạp danh mục lần đầu | Skeleton row ×8 (50pt, shimmer `surfaceVariant`); `SegmentedControl` vô hiệu |
| **Empty** | data | Asset một preset không nạp được | Preset đó **bị loại khỏi danh sách** (ERR-010.2) — không hiện dòng chết |
| **Offline** | data | Không có mạng | **Không ảnh hưởng** — asset trong bundle |

**User Flow**
- **Entry**: tab **Sounds** · thẻ sound trên **WF-006** · quay lại từ **WF-020**
- **Exit**: **WF-020** (nghe kỹ) · **WF-010** (chạm preset khoá) · **WF-012** (nút âm lượng) · **WF-022** (cấp quyền Vị trí ở Variant A) · **WF-006** · **WF-030** (toast sau khi gán)
- **Task Flow**: bước 1–6 của **TF-005**
- **Transitions**: sheet WF-020 trượt lên 0,35s; segmented crossfade 0,2s; waveform fade-in 0,15s khi audio bắt đầu

---

### 3.8 WF-008 — Trình Tạo Widget 📱 · *Template D (Management)*

**Design System**: `bento-grid`
**Archetype**: Management | **Secondary**: Action | **Density**: **Dense** (6 vùng)
**Source UC**: UC-012 (chính), UC-013, UC-014
**Source FR**: **FR-021** (preset gợi ý theo xe), **FR-022** (lưu App Group), **FR-023** (giới hạn entitlement), **FR-024** (ngưỡng iOS 17.4)
**User Intent**: "Tôi muốn có một widget đẹp trên màn hình xe mà không phải học cách dùng công cụ."

**Action Layer → Visual Hierarchy**

| UC Action Layer | Slot | Ghi chú |
|---|---|---|
| Layer 1 — Primary: chọn một preset widget và lưu | **#3** | CTA "Lưu widget" / "Lưu thay đổi" / "Mở khoá" |
| Layer 2 — Contextual: chọn loại widget · chạm ô ảnh → WF-024 · đổi tên · lưu | **#2** | Hàng preset + ô ảnh |
| Layer 3 — Discovery: duyệt preset gợi ý theo xe · xem preset Premium (xem trước đầy đủ) | **#2** | Hàng cuộn ngang |
| Layer 4 — Personal: "Xem trước trên xe của tôi" → WF-023 · bản nháp đang làm | #4 | Chrome |

**Visual Hierarchy**
1. **Preview widget ở Zone A** — theo tỉ lệ xe đã biết (hoặc tỉ lệ tham chiếu). **Có nội dung ngay từ giây đầu** — cấm canvas rỗng (BR-021.1).
2. **Hàng preset gợi ý cuộn ngang + bộ chọn loại widget** — vùng tương tác chính.
3. **CTA "Lưu widget"** — cố định đáy.
4. **Chrome**: nav bar, nút "Xem trước trên xe của tôi", chỉ báo giới hạn widget của gói.

*Self-check*: preview (~180pt) cao gấp 1,5× card preset (120pt) — **không đạt ngưỡng 2×** của Discovery, nhưng đây là màn **Management**, ngưỡng đó không áp dụng; hierarchy Management yêu cầu list header → rows → actions, và preview đóng vai list header context. Đã ghi ở §Notes.

> **§Notes**: WF-008 là hybrid Management (quản lý cấu hình widget) + Action (lưu). Zone A được dùng dù bảng override cho Management ghi "—", vì preview là **ngữ cảnh bắt buộc** để người dùng biết mình đang sửa cái gì. Sai lệch có chủ ý, đúng theo quy tắc "custom override cần justification".

**Required Features (FR)**
- FR-021 P2: chưa có widget → hiện **≥ 3 preset gợi ý theo xe đã chọn** + preview có nội dung ngay
- FR-021 P3: chạm preset → preview cập nhật **tại chỗ** crossfade 0,25s (SF-007)
- FR-021 P5: preset Premium → **xem trước đầy đủ**, nút chuyển "Mở khoá"
- FR-021 P6: vào từ thẻ WF-006 → nạp sẵn widget hiện tại, lưu chỉ 2 chạm
- FR-022 P1–P4: ghi App Group **ngay tại thời điểm lưu**, đọc lại xác nhận
- FR-023 P2–P3: Free đã có 1 widget → `LimitNotice` + cho **đổi**; "Thêm widget thứ hai" → WF-010
- FR-024 P2: iOS < 17.4 → `VersionNotice` nêu rõ, **vẫn cho cấu hình và lưu**
- FR-026 P3–P4 (qua WF-023): bật/tắt lớp thông tin để tự giảm bớt

**UX Enhancements** (`composition.management.defaults`)
- `grouped-rows` → grouped controls: preset · loại widget · ảnh · lớp thông tin
- `inline-status-on-row`: chỉ báo giới hạn widget hiện ngay ở Zone D
- `destructive-needs-confirm`: **không áp dụng** — không có hành động phá hủy ở đây
- `pull-to-refresh`: **không dùng** — nội dung là cấu hình cục bộ
- Bản nháp: thoát giữa lúc tạo → giữ nháp; lần mở lại hỏi "Tiếp tục widget đang làm?" (ERR-021.2)

**Content Zones Map**

```
┌─────────────────────────────────────┐
│ ZONE D: Navigation                  │ ← 44pt
│   [<] Widget    [Xem trước trên xe] │
├─────────────────────────────────────┤
│ ZONE A: Context — preview widget    │ ← ~180pt (override, xem §Notes)
├─────────────────────────────────────┤
│ ZONE B: Actionable List             │ ← fill: preset + loại + ảnh + lớp
├─────────────────────────────────────┤
│ ZONE D: CTA + chỉ báo giới hạn      │ ← 50pt + 24pt
├─────────────────────────────────────┤
│ ZONE C: — (unused)                  │ ← height 0
└─────────────────────────────────────┘
```

**Layout**

```
┌──────────────────────────────────────────────┐
│ navBar h=44                                  │ ZONE D
│  [<]  Widget        [Xem trước trên xe >]    │ → WF-023
├──────────────────────────────────────────────┤
│ ┌──────────────────────────────────────────┐ │ ZONE A ~180pt
│ │  ┌────────────────────────────────────┐  │ │ card r=16 shadow.1
│ │  │   [ ảnh Camry + counter 142 ]      │  │ │ khung theo tỉ lệ
│ │  │   tỉ lệ 1180×420 (xe của bạn)      │  │ │ THẬT nếu đã cắm xe
│ │  └────────────────────────────────────┘  │ │ crossfade 0,25s
│ │  ● Kích thước thật của xe bạn            │ │ caption success
│ └──────────────────────────────────────────┘ │
├──────────────────────────────────────────────┤
│  GỢI Ý CHO TOYOTA CAMRY                      │ ZONE B
│ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐         │ cuộn ngang
│ │▸Ảnh  │ │ Ảnh  │ │Counter│ │ Ảnh  │  →→   │ card 120×120
│ │ xe ✓ │ │ xe 2 │ │      │ │cá nhân│        │ selected: viền
│ └──────┘ └──────┘ └──────┘ └──────┘         │ accent 2px
│                                              │ ≥3 preset (BR-021.2)
│  LOẠI WIDGET                                 │
│ ┌──────────────────────────────────────────┐ │
│ │ ▸ Ảnh xe theo model              ✓       │ │ row 50pt
│ │   Ảnh cá nhân                    🔒      │ │
│ │   Counter chuyến đi              🔒      │ │
│ └──────────────────────────────────────────┘ │
│                                              │
│  ẢNH                                         │
│ ┌──────────────────────────────────────────┐ │
│ │ [thumb] Camry 2022 (mặc định)      [>]   │ │ → WF-024
│ └──────────────────────────────────────────┘ │
│                                              │
│  LỚP THÔNG TIN                               │
│ ┌──────────────────────────────────────────┐ │
│ │ Tên xe                          [ ●━ ]   │ │ toggle 51×31
│ │ Số chuyến đi                    [ ●━ ]   │ │ ưu tiên thấp nhất
│ │ Thời tiết                       [ ━● ]   │ │ → bỏ trước khi
│ └──────────────────────────────────────────┘ │   thiếu chỗ (FR-030)
├──────────────────────────────────────────────┤
│ .safeAreaInset(bottom):                      │ ZONE D
│ ┌──────────────────────────────────────────┐ │
│ │            Lưu widget                    │ │ h=50 bg accent
│ └──────────────────────────────────────────┘ │
│  Gói Free: 1 widget · đang dùng 1/1          │ caption textSecondary
└──────────────────────────────────────────────┘
```

**Layout Variants** *(bắt buộc: Dense density)*

**Variant A — Gói Free đã dùng hết 1 widget**
```
┌──────────────────────────────────────────────┐
│ ┌ preview widget hiện tại ─────────────────┐ │
│ ┌──────────────────────────────────────────┐ │ LimitNotice
│ │ ℹ Gói Free có 1 widget. Bạn có thể ĐỔI   │ │ accentSubtle
│ │   widget này bất cứ lúc nào.              │ │ r=16 ~64pt
│ │        [Thêm widget thứ hai >]            │ │ → WF-010
│ └──────────────────────────────────────────┘ │ trigger_source =
│  … preset · loại · ảnh · lớp thông tin …     │ widget_limit
├──────────────────────────────────────────────┤
│ [          Lưu thay đổi          ]           │ nhãn ĐỔI (đang sửa
│  Gói Free: 1 widget · đang dùng 1/1          │ widget có sẵn)
└──────────────────────────────────────────────┘
   Widget hiện có KHÔNG bị xoá (AC-012.3)
```

**Variant B — iOS 16.4–17.3 (chưa hỗ trợ widget CarPlay)**
```
┌──────────────────────────────────────────────┐
│ ┌ preview widget (VẪN hiện bình thường) ────┐│
│  … preset · loại · ảnh · lớp thông tin …     │
├──────────────────────────────────────────────┤
│ ┌──────────────────────────────────────────┐ │ VersionNotice
│ │ ℹ Widget CarPlay cần iOS 17.4 trở lên.   │ │ semantic.info
│ │   Bạn đang dùng iOS 17.2.                 │ │ r=16 ~72pt
│ │   Cấu hình bên trên vẫn được LƯU và sẽ    │ │
│ │   hiện ngay sau khi bạn nâng cấp iOS.     │ │ KHÔNG giả vờ
│ │   Âm thanh, giọng chào và dashboard vẫn   │ │ widget đang chạy
│ │   hoạt động đầy đủ.                       │ │ (BR-024.2)
│ └──────────────────────────────────────────┘ │
├──────────────────────────────────────────────┤
│ [          Lưu widget          ]             │ VẪN cho lưu
└──────────────────────────────────────────────┘  (AC-012.4)
```

**Components**
- `NavBarStandard` + `BtnTertiary` ("Xem trước trên xe") → WF-023.
- `CardWidgetPreviewLive` — Tokens: `radius: 16`, `padding: 16`, `shadow: ${shadow.elevation.1}`; khung trong theo **tỉ lệ scene bounds thật** nếu đã có, dùng **cùng engine** FR-029; crossfade `${animation.duration.normal}`(0,25s).
- `PresetCarousel` + `CardPresetWidget` — Tokens: card 120×120, `radius: ${border.radius.lg}`(16), selected `borderWidth: ${border.width.strong}`(2) `borderColor: ${color.palette.accent}`.
- `RowSelectable` + `LockLabel` — như WF-003/WF-004.
- `RowImageSlot` — Tokens: `height: ${component.row.heightWithSubtitle}`(68), thumb 44×44 `radius: ${border.radius.md}`(8) → WF-024.
- `RowToggle` — Tokens: `height: 50`, toggle `${component.toggle}` 51×31, on `${color.palette.accent}`.
- `LimitNotice` — Tokens: `background: ${color.palette.accentSubtle}`, `radius: 16`.
- `VersionNotice` — Tokens: `background: ${color.semantic.info.background}`, `foreground: ${color.semantic.info.color}`, `radius: 16`.
- `BtnPrimary` nhãn động ("Lưu widget" / "Lưu thay đổi" / "Mở khoá").

**States** (9)

| State | Loại | Context | Layout/Behavior |
|---|---|---|---|
| **First Visit** | user-context | Chưa có widget | **≥ 3 preset gợi ý theo xe**; Zone A có preview ngay — **tuyệt đối không canvas rỗng** |
| **Returning** | user-context | Đã có widget | Widget hiện tại nạp sẵn Zone A; nhãn CTA "Lưu thay đổi" |
| **Power User** | user-context | Premium, dùng ảnh cá nhân | Mở thêm loại "Ảnh cá nhân" + "Counter"; lối vào WF-024 nổi bật hơn |
| **Free tier** | user-context | Đã dùng hết 1 widget | **Variant A**: `LimitNotice` + cho đổi; "Thêm widget thứ hai" → WF-010 |
| **iOS < 17.4** | user-context | Thiết bị chưa hỗ trợ | **Variant B**: `VersionNotice`, **vẫn cho cấu hình và lưu** |
| **Error** | user-context | Ghi App Group thất bại (ERR-022.1) | Nêu lỗi cụ thể + [Thử lại]; **giữ bản nháp**, preview không reset |
| **Default** | data | Preset + asset nạp xong | Layout như trên |
| **Loading** | data | Đang nén và ghi ảnh (FR-028) | CTA hiện spinner, các control khác vô hiệu tạm |
| **Empty** | data | Không nạp được preset gợi ý (ERR-021.3) | Dùng preset mặc định của app + ảnh silhouette; **không** để Zone A trống |

**User Flow**
- **Entry**: tab **Widget** · thẻ widget trên **WF-006** · quay lại từ **WF-023**/**WF-024** · từ **WF-014** (sửa sau lỗi render, qua WF-023)
- **Exit**: **WF-023** (xem trước) · **WF-024** (chọn ảnh) · **WF-010** (preset/loại Premium hoặc thêm widget) · **WF-006** · **WF-030** (toast sau khi lưu)
- **Task Flow**: bước 1–8 của **TF-004**; bước 4a của **TF-003** (sửa sau lỗi render)
- **Transitions**: preview crossfade 0,25s (**không** slide — slide gợi ý "trang khác" trong khi chỉ là đổi nội dung, SF-007); modal WF-023 trượt lên 0,35s

---

### 3.9 WF-009 — Cài Đặt Giọng Chào 📱 · *Template B (Action)*

**Design System**: `bento-grid`
**Archetype**: Action | **Secondary**: Management | **Density**: Medium (5 vùng)
**Source UC**: UC-019 (chính), UC-005, UC-018, UC-020
**Source FR**: **FR-033** (bật/tắt), **FR-034** (nguồn ngữ cảnh), **FR-035** (chặn nguồn thiếu quyền), **FR-036** (nghe thử on-device)
**User Intent**: "Tôi muốn nghe thử và quyết định app được biết gì về tôi."

**Action Layer → Visual Hierarchy**

| UC Action Layer | Slot | Ghi chú |
|---|---|---|
| Layer 1 — Primary: chạm "Nghe thử" rồi bật/tắt từng nguồn | **#3** | CTA "Nghe thử" — đây là hành động xác minh tính năng có thật |
| Layer 2 — Contextual: công tắc chính · toggle từng nguồn · nghe lại | **#2**, #4 | Toggle nguồn ở #2; công tắc chính ở #4 (chrome, tránh tắt nhầm) |
| Layer 3 — Discovery: xem ví dụ câu chào của từng nguồn · xem chữ câu đang phát | **#1** | Chữ câu chào ở Zone A là **bằng chứng** — nên nó là #1 |
| Layer 4 — Personal: lối vào cấp quyền cho nguồn còn thiếu | #4 | Trong dòng nguồn |

**Visual Hierarchy**
1. **Câu chào vừa sinh, hiển thị bằng chữ** — Zone A. Đây là **bằng chứng kiểm chứng được** rằng giọng chào là thật; đối trọng trực tiếp với R-10 và R-13. Vì vậy nó đứng trên cả CTA.
2. **4 dòng nguồn ngữ cảnh** — mỗi dòng có toggle + ví dụ + trạng thái quyền.
3. **CTA "Nghe thử"** — `${component.button.primary}`.
4. **Chrome**: nav bar, công tắc chính ở đầu màn, nhãn "cần quyền" + nút hành động.

*Self-check*: CTA 50pt + padding 24 ⇒ đạt. CTA **không** vô hiệu (nghe thử luôn hoạt động, kể cả gói Free) ⇒ đúng BR-036.2. Dòng nguồn cao 68pt (có subtitle ví dụ) > 44pt ⇒ đạt.

**Required Features (FR)**
- FR-033 P1–P2: `ToggleMain` đầu màn; khi tắt, mục dưới **mờ nhưng vẫn đọc được**
- FR-033 P6: `StatusRow` trên WF-006 **chỉ đọc** — công tắc thật chỉ ở đây
- FR-034 P1–P2: 4 `ToggleRow` có toggle + **ví dụ câu chào cụ thể** + trạng thái quyền, theo đúng ngôn ngữ app
- FR-034 P5 / ERR-034.2: tắt hết 4 nguồn → vẫn phát **câu chào trung tính**, không im lặng
- FR-035 P2: bật nguồn thiếu quyền → toggle **nảy nhẹ về tắt** 0,2s + nhãn "cần quyền" + nút hành động (SF-012)
- FR-036 P1–P5: sinh câu chào từ **ngữ cảnh thật lúc đó**, chữ hiện **đồng thời** với âm thanh, chạm lần nữa cho câu **khác**
- FR-036 ERR-036.1: TTS lỗi → **vẫn hiện chữ** kèm lý do
- FR-036 ERR-036.2: gói Free → nghe thử **đầy đủ**, công tắc chính khoá

**UX Enhancements** (`composition.action.defaults`)
- `single-primary-cta`: "Nghe thử" là CTA duy nhất
- `inline-validation`: toggle nảy về tắt là **phản hồi validation dạng chuyển động** — truyền đạt "điều kiện chưa đủ" rõ hơn một dòng chữ (BR-035.2)
- `escape-route-always-visible`: nút quay lại; công tắc chính cho phép tắt hẳn bất cứ lúc nào
- Chữ câu chào hiện **theo tiến độ đọc của TTS**, không phải typewriter giả (SF-011)
- Ghi nguồn ngữ cảnh đã dùng nhỏ bên dưới câu chào — người dùng thấy **tại sao** câu đó được chọn

**Content Zones Map**

```
┌─────────────────────────────────────┐
│ ZONE D: Navigation + công tắc chính │ ← 44pt + row 50pt
│   [<] Giọng chào                    │
│   Giọng chào khi lên xe   [ ●━ ]    │
├─────────────────────────────────────┤
│ ZONE A: Context — câu chào bằng chữ │ ← ~140pt, static
├─────────────────────────────────────┤
│ ZONE B: Input Area + Primary CTA    │ ← fill: 4 nguồn + CTA
│   ToggleRow ×4 (68pt) · [Nghe thử]  │
├─────────────────────────────────────┤
│ ZONE C: — (unused cho Action)       │ ← height 0
└─────────────────────────────────────┘
```

**Layout**

```
┌──────────────────────────────────────────────┐
│ navBar h=44                                  │ ZONE D
│  [<]        Giọng chào                       │
│ ┌──────────────────────────────────────────┐ │ row 50pt
│ │ Giọng chào khi lên xe          [ ●━ ]    │ │ công tắc CHÍNH
│ └──────────────────────────────────────────┘ │ on: accent
├──────────────────────────────────────────────┤
│ ┌──────────────────────────────────────────┐ │ ZONE A ~140pt
│ │ "Sáng mưa rồi, Alex. Họp 8:30 ở văn      │ │ card r=16 p=16
│ │  phòng — đi sớm 5 phút nhé."             │ │ body 17/400
│ │  ${typography.scale.body} textPrimary    │ │ hiện theo tiến độ
│ │                                          │ │ đọc của TTS
│ │  ⏸ đang đọc                              │ │
│ │  Nguồn: giờ · thời tiết · lịch           │ │ caption
│ └──────────────────────────────────────────┘ │ textSecondary
│                                              │
│ ┌──────────────────────────────────────────┐ │ ZONE B
│ │            Nghe thử                      │ │ h=50 bg accent
│ └──────────────────────────────────────────┘ │ LUÔN hoạt động
├──────────────────────────────────────────────┤
│  NGUỒN NGỮ CẢNH                              │
│ ┌──────────────────────────────────────────┐ │
│ │ Giờ trong ngày                  [ ●━ ]   │ │ ToggleRow 68pt
│ │ "Chào buổi sáng, Alex."                  │ │ ví dụ: caption
│ │ ✓ Không cần quyền                        │ │ success
│ ├──────────────────────────────────────────┤ │
│ │ Thời tiết                       [ ●━ ]   │ │
│ │ "Sáng nay mưa, đi cẩn thận nhé."         │ │
│ ├──────────────────────────────────────────┤ │
│ │ Lịch                            [ ●━ ]   │ │
│ │ "Họp 8:30 ở văn phòng — đi thôi."        │ │
│ │ ✓ Đã cấp quyền Lịch                      │ │
│ ├──────────────────────────────────────────┤ │
│ │ Điểm đến dự đoán                [ ━● ]   │ │ toggle TẮT
│ │ "Về nhà? Đường Nguyễn Trãi đang thoáng." │ │
│ │ ⚠ Cần quyền Vị trí    [Cấp quyền]        │ │ warning + nút
│ └──────────────────────────────────────────┘ │ → WF-022
└──────────────────────────────────────────────┘
```

**Layout Variants** *(bắt buộc: Medium density)*

**Variant A — Gói Free (nghe thử đầy đủ, tính năng khoá)**
```
┌──────────────────────────────────────────────┐
│ ┌──────────────────────────────────────────┐ │
│ │ Giọng chào khi lên xe    🔒 [ ━● ]       │ │ công tắc KHOÁ
│ └──────────────────────────────────────────┘ │
├──────────────────────────────────────────────┤
│ ┌──────────────────────────────────────────┐ │ ZONE A vẫn ĐẦY ĐỦ
│ │ "Sáng mưa rồi, Alex. Họp 8:30 ở văn      │ │ nghe thử KHÔNG
│ │  phòng — đi sớm 5 phút nhé."             │ │ bị cắt, KHÔNG
│ │  ⏸ đang đọc · Nguồn: giờ · thời tiết     │ │ watermark
│ └──────────────────────────────────────────┘ │ (BR-036.2)
│ ┌──────────────────────────────────────────┐ │
│ │            Nghe thử                      │ │ VẪN hoạt động
│ └──────────────────────────────────────────┘ │
│ ┌──────────────────────────────────────────┐ │
│ │ 🔒 Giọng chào trên xe có ở gói Premium.  │ │ accentSubtle
│ │    Bạn vừa nghe đúng thứ sẽ phát.         │ │
│ │              [Xem các gói >]              │ │ → WF-010
│ └──────────────────────────────────────────┘ │
│  … 4 nguồn ngữ cảnh (mờ nhưng đọc được) …    │
└──────────────────────────────────────────────┘
```

**Variant B — TTS không phát được (vẫn hiện chữ)**
```
┌──────────────────────────────────────────────┐
│ ┌──────────────────────────────────────────┐ │ ZONE A
│ │ "Sáng mưa rồi, Alex. Họp 8:30 ở văn      │ │ CHỮ VẪN HIỆN
│ │  phòng — đi sớm 5 phút nhé."             │ │ đầy đủ
│ │                                          │ │
│ │ ⚠ Không phát được tiếng lúc này          │ │ warning
│ │   (đang có cuộc gọi)          [Thử lại]  │ │ nêu LÝ DO
│ │  Nguồn: giờ · thời tiết · lịch           │ │
│ └──────────────────────────────────────────┘ │
│  … CTA và 4 nguồn hoạt động bình thường …    │ nội dung VẪN
└──────────────────────────────────────────────┘  kiểm chứng được
                                                  (ERR-036.1)
```

**Components**
- `NavBarStandard`.
- `RowToggleMain` — công tắc chính. Tokens: `height: 50`, toggle `${component.toggle}`, on `${color.palette.accent}`. Biến thể khoá: thêm `LockLabel`, toggle `${color.palette.surfaceVariant}`.
- `CardGreetingProof` — Zone A. Tokens: `radius: 16`, `padding: 16`, `shadow: ${shadow.elevation.1}`, `font: ${typography.scale.body}`; chữ hiện theo tiến độ TTS.
- `BtnPrimary` ("Nghe thử") — **không có trạng thái vô hiệu**.
- `RowToggleContext` ×4 — Tokens: `height: ${component.row.heightWithSubtitle}`(68), ví dụ `${typography.scale.caption}` `${color.palette.textSecondary}`, trạng thái quyền: `✓` `${color.semantic.success.color}` / `⚠` `${color.semantic.warning.color}`. Toggle nảy về tắt: `${animation.duration.normal}` 0,2s.
- `BtnSecondary` ("Cấp quyền") → WF-022.
- `CardUpsellInline` (Variant A) — Tokens: `background: ${color.palette.accentSubtle}`, `radius: 16`.

**States** (8)

| State | Loại | Context | Layout/Behavior |
|---|---|---|---|
| **First Visit** | user-context | Chưa có quyền nào | Chỉ nguồn "Giờ trong ngày" hoạt động; 3 nguồn kia "cần quyền" + lối vào — **không** im lặng |
| **Returning** | user-context | Đã có quyền, dùng vài ngày | Cả 4 nguồn hoạt động; câu chào ở Zone A **phong phú hơn rõ rệt** |
| **Power User** | user-context | Chạm "Nghe thử" ≥ 4 lần | Mỗi lần một câu khác; sau 4 lần thấy đủ dải ≥ 4 biến thể (AC-020.2) |
| **Free tier** | user-context | Entitlement = Free | **Variant A**: nghe thử **đầy đủ**; công tắc chính khoá; `CardUpsellInline` → WF-010 |
| **Error** | user-context | TTS không phát được (ERR-036.1) | **Variant B**: **vẫn hiện chữ** + lý do + [Thử lại] |
| **Default** | data | Ngữ cảnh và quyền đọc xong | Layout như trên |
| **Loading** | data | ContextEngine đang sinh câu (≤ 1,0s NFR-005) | CTA hiện spinner; Zone A giữ câu trước, **không** để trống |
| **Empty** | data | Tắt hết 4 nguồn | Zone A hiện **câu chào trung tính** + dòng "đang dùng câu chào chung"; **không** để trống, **không** báo lỗi |

**User Flow**
- **Entry**: tab **Widget** (nhóm cấu hình) · thẻ giọng chào trên **WF-006**
- **Exit**: **WF-022** (cấp quyền cho một nguồn) · **WF-010** (gói Free) · **WF-006** · Cài đặt hệ thống iOS (quyền đã `denied`)
- **Task Flow**: bước 1–6 của **TF-006**; bước 6–6a của **TF-011**; bước 4 của **TF-012**
- **Transitions**: chữ câu chào hiện theo tiến độ TTS; câu cũ fade 0,2s trước khi câu mới vào (SF-011); toggle nảy về tắt 0,2s (SF-012); sheet WF-022 trượt lên 0,35s

---

### 3.10 WF-010 — Paywall (IAP / Store) 📱 · *Template B (Action)*

**Design System**: `bento-grid`
**Archetype**: Action | **Secondary**: Discovery | **Density**: Medium (5 vùng)
**Source UC**: UC-025 (chính), UC-006, UC-012, UC-018, UC-020, UC-024, UC-030
**Source FR**: **FR-045** (chính sách hiển thị), **FR-046** (4 bậc giá từ StoreKit), **FR-047** (cấm giá cache), **FR-003** (phục hồi giao dịch)
**User Intent**: "Tôi muốn biết mình phải trả bao nhiêu để có thứ tôi vừa chạm vào, và có lựa chọn nào khác."

**Action Layer → Visual Hierarchy**

| UC Action Layer | Slot | Ghi chú |
|---|---|---|
| Layer 1 — Primary: chọn một trong 4 lựa chọn | **#3** | Bốn `PriceTierCard`; bậc phù hợp `trigger_source` được nhấn mạnh |
| Layer 2 — Contextual: xem tính năng mở khoá từng bậc · đóng paywall | #2, #4 | Nút đóng ở #4 |
| Layer 3 — Discovery: bảng so sánh Free ↔ Premium mở rộng inline | **#4** | SF-015, thu gọn mặc định |
| Layer 4 — Personal: "Phục hồi giao dịch" · "Tiếp tục dùng gói Free" | #4 | **Ngang hàng với các bậc, không ẩn trong menu con** |

**Visual Hierarchy**
1. **Zone A — nói về đúng tính năng người dùng vừa chạm** — `${typography.scale.h3}` + minh họa nhỏ. Không phải quảng cáo chung.
2. **4 thẻ giá** — vùng tương tác chính, giá cuối bằng tiền tệ địa phương.
3. **Bậc được nhấn mạnh** (viền accent 2px) — tương phản cao nhất trong nhóm thẻ.
4. **Chrome**: nút đóng, "Phục hồi giao dịch", "Tiếp tục dùng gói Free", link điều khoản, dòng "So sánh các gói".

*Self-check*: mỗi thẻ giá cao 88pt > 44pt ⇒ đạt. Thẻ Free **không bị làm mờ** ⇒ đúng BR-046.2. Không có "CTA duy nhất" vì đây là màn **chọn**, không phải màn submit — CTA thật nằm ở WF-011.

**Required Features (FR)**
- FR-045 P1–P2: kiểm `days_since_install > 0` **hoặc** hành động chủ động; nếu không thoả thì **từ chối hiển thị** và ghi nhận lần từ chối
- FR-045 **BR-045.3**: **cấm** mọi đường mở paywall từ bề mặt CarPlay
- FR-045 P5: Zone A nói về **đúng tính năng vừa chạm**
- FR-046 P2: 4 `PriceTierCard`; Free đánh dấu "gói bạn đang dùng", **không làm mờ**
- FR-046 **BR-046.1**: **không có bậc weekly**
- FR-046 BR-046.3/4: giá cuối bằng tiền tệ địa phương; **cấm** quy đổi "$0,48/tuần"; **cấm** discount phần trăm không đúng thực tế
- FR-047 P2–P4: StoreKit lỗi → báo lỗi rõ + thử lại; **chặn** đường sang WF-011; **cấm** giá cache/hardcode
- FR-003 P2: "Phục hồi giao dịch" **luôn hiện, ngang hàng các bậc giá**

**UX Enhancements** (`composition.action.defaults`)
- `single-primary-cta`: **sai lệch có chủ ý** — màn này có 4 lựa chọn ngang hàng, không có một CTA. CTA thật ở WF-011. Ghi ở §Notes.
- `escape-route-always-visible`: nút đóng + "Tiếp tục dùng gói Free" luôn thấy
- `inline-validation`: **không áp dụng**
- Bảng so sánh mở rộng inline (SF-015) bằng spring 0,3s damping cao — chiều cao đổi mượt, nội dung dưới không nhảy
- Đóng paywall → **không hỏi lại trong cùng phiên** (BR-045.4)

> **§Notes**: Bảng override cho Action ghi Zone C = "—", nhưng WF-010 **dùng Zone C** cho bảng so sánh. Justification: bảng so sánh là **nội dung khám phá** giúp người dùng tự quyết thay vì tin vào một bậc được nhấn mạnh — bỏ nó đi sẽ làm màn này thành trang bán hàng một chiều, ngược với luận điểm minh bạch của PRD §11.

**Content Zones Map**

```
┌─────────────────────────────────────┐
│ ZONE D: Navigation                  │ ← 44pt: [✕] + Phục hồi giao dịch
├─────────────────────────────────────┤
│ ZONE A: Context — tính năng vừa chạm│ ← ~120pt, static
├─────────────────────────────────────┤
│ ZONE B: 4 thẻ giá (lựa chọn chính)  │ ← 4×88pt + gap 12
├─────────────────────────────────────┤
│ ZONE C: Bảng so sánh (mở rộng)      │ ← 44pt thu gọn / ~280pt mở
├─────────────────────────────────────┤
│ ZONE D: Chrome                      │ ← Tiếp tục Free + điều khoản
└─────────────────────────────────────┘
```

**Layout** — *mở từ preset sound khoá, `days_since_install = 12`*

```
┌──────────────────────────────────────────────┐
│  [✕]                    Phục hồi giao dịch   │ ZONE D 44pt
├──────────────────────────────────────────────┤
│ ┌──────────────────────────────────────────┐ │ ZONE A ~120pt
│ │ 🔒 "Synth Lên Xe" có ở gói Premium       │ │ h3 22/600
│ │    Mở khoá toàn bộ 12 âm thanh, widget    │ │ body textSecondary
│ │    không giới hạn và giọng chào AI.       │ │ NÓI VỀ ĐÚNG
│ └──────────────────────────────────────────┘ │ tính năng vừa chạm
├──────────────────────────────────────────────┤
│ ┌──────────────────────────────────────────┐ │ ZONE B
│ │ Gói Free              ✓ bạn đang dùng    │ │ card 88pt r=16
│ │ 1 widget · 3 âm thanh · dashboard cơ bản │ │ KHÔNG làm mờ
│ │ 0 $                                      │ │ mono
│ └──────────────────────────────────────────┘ │
│ ┌──────────────────────────────────────────┐ │
│ │ Hằng tháng                               │ │
│ │ Mọi tính năng Premium                    │ │
│ │ 4,99 $ / tháng                           │ │ mono · giá CUỐI
│ └──────────────────────────────────────────┘ │ từ StoreKit
│ ┌══════════════════════════════════════════┐ │ viền accent 2px
│ ║ Hằng năm                    Tiết kiệm 50%║ │ NHẤN MẠNH
│ ║ Mọi tính năng · dùng thử 7 ngày          ║ │ (đúng thực tế:
│ ║ 29,99 $ / năm                            ║ │  4,99×12=59,88)
│ └══════════════════════════════════════════┘ │
│ ┌──────────────────────────────────────────┐ │
│ │ Vĩnh viễn                     Một lần    │ │
│ │ Mọi tính năng, trả một lần               │ │
│ │ 49,99 $                                  │ │ mono
│ └──────────────────────────────────────────┘ │
│                                              │ KHÔNG có bậc weekly
├──────────────────────────────────────────────┤
│  So sánh các gói                        [v]  │ ZONE C thu gọn 44pt
├──────────────────────────────────────────────┤
│  Tiếp tục dùng gói Free                      │ ZONE D
│  Điều khoản · Chính sách quyền riêng tư      │ footnote textTertiary
└──────────────────────────────────────────────┘
```

**Layout Variants** *(bắt buộc: Medium density)*

**Variant A — Bảng so sánh đã mở rộng (SF-015)**
```
┌──────────────────────────────────────────────┐
│  … Zone A + 4 thẻ giá …                      │
├──────────────────────────────────────────────┤
│  So sánh các gói                        [^]  │ ZONE C mở ~280pt
│ ┌──────────────────────────────────────────┐ │ spring 0,3s
│ │                      Free    Premium     │ │ damping cao
│ │ Widget CarPlay        1      không giới hạn│ mono cho số
│ │ Âm thanh              3      12+          │ │
│ │ Giọng chào AI         —      ✓            │ │
│ │ Ảnh cá nhân           —      ✓            │ │
│ │ Dashboard AI học      —      ✓            │ │
│ │ Thư viện xe đầy đủ    —      ✓            │ │
│ │ Quảng cáo             không  không        │ │ Free cũng KHÔNG
│ │ Giới hạn thời gian    không  không        │ │ có quảng cáo
│ └──────────────────────────────────────────┘ │
│  Tiếp tục dùng gói Free                      │
└──────────────────────────────────────────────┘
```

**Variant B — StoreKit không trả về giá (ERR-047.1)**
```
┌──────────────────────────────────────────────┐
│  [✕]                    Phục hồi giao dịch   │
├──────────────────────────────────────────────┤
│ ┌ 🔒 "Synth Lên Xe" có ở gói Premium ───────┐│ Zone A giữ nguyên
├──────────────────────────────────────────────┤
│ ┌──────────────────────────────────────────┐ │ ZONE B thay bằng
│ │ ⚠ Không tải được bảng giá                │ │ error state
│ │   Không kết nối được App Store. Bảng giá  │ │ semantic.error
│ │   phải lấy trực tiếp từ Apple nên chúng   │ │
│ │   tôi không hiển thị con số có thể sai.    │ │ nói RÕ vì sao
│ │              [Thử lại]                    │ │ không đoán giá
│ └──────────────────────────────────────────┘ │
│  ✗ KHÔNG có thẻ giá nào                      │ cấm giá cache/
│  ✗ Đường sang WF-011 BỊ CHẶN                 │ hardcode
├──────────────────────────────────────────────┤
│  Tiếp tục dùng gói Free                      │ vẫn dùng được
└──────────────────────────────────────────────┘
```

**Components**
- `NavBarModal` — Tokens: `height: 44`, `[✕]` icon 20pt, không divider (paywall là sheet toàn màn).
- `CardContextUpsell` (Zone A) — Tokens: `radius: 16`, `padding: 16`, `background: ${color.palette.accentSubtle}`.
- `PriceTierCard` ×4 — Tokens: `height: 88`, `radius: ${border.radius.lg}`(16), `padding: ${component.card.padding}`(16), `background: ${color.palette.surface}`, `border: 1px ${color.palette.border}`, `shadow: ${shadow.elevation.1}`. Biến thể nhấn mạnh: `borderWidth: 2` `borderColor: ${color.palette.accent}`. Biến thể "đang dùng": badge `${color.semantic.success.color}`. **Giá dùng `${typography.family.mono}`**.
- `ComparisonTableExpandable` (Zone C) — Tokens: thu gọn `height: 44`, mở `~280`, `background: ${color.palette.surface}`, `radius: 16`, animation `${animation.spring.smooth}`.
- `BtnTertiary` ×2 — "Phục hồi giao dịch", "Tiếp tục dùng gói Free".
- `CardErrorInline` (Variant B) — Tokens: `background: ${color.semantic.error.background}`, `foreground: ${color.semantic.error.color}`, `radius: 16`.

**States** (8)

| State | Loại | Context | Layout/Behavior |
|---|---|---|---|
| **First Visit** | user-context | Lần đầu chạm tính năng khoá (`days_since_install > 0`) | Zone A nói về **đúng tính năng vừa chạm** |
| **Returning** | user-context | Đã xem paywall trước đó | Nhấn mạnh bậc Yearly; **không** lặp lại cùng nội dung Zone A |
| **Power User** | user-context | Dùng Free lâu, nhiều thiết bị | "Phục hồi giao dịch" và bậc Lifetime nổi bật hơn |
| **Trial đã dùng** | user-context | Từng dùng trial | Bậc giá **không** hiện ưu đãi trial; nêu rõ là mua trực tiếp (ERR-046.3) |
| **Error** | user-context | StoreKit không trả giá | **Variant B**: báo lỗi rõ + [Thử lại]; **không** giá cache; **chặn** sang WF-011 |
| **Default** | data | Giá lấy được | Layout như trên, đúng 4 bậc |
| **Loading** | data | Truy vấn StoreKit đang chạy | Skeleton 4 thẻ giá (88pt, shimmer); Zone A đã hiện đầy đủ |
| **Empty** | data | Không áp dụng — luôn có đúng 4 bậc | Trạng thái này **không tồn tại có chủ ý**; nếu StoreKit trả về < 3 product thì đó là **lỗi cấu hình App Store Connect** (VR-046.1), xử lý như Error |

**User Flow**
- **Entry**: preset khoá trên **WF-007** · loại widget khoá / "Thêm widget thứ hai" trên **WF-008** · công tắc khoá trên **WF-009** · dòng "Nâng cấp" trên **WF-012** · badge gói Free trên **WF-006**. **Không có entry nào từ WF-016/017/018/019** (BR-045.3)
- **Exit**: **WF-011** (chọn một bậc) · màn hình trước đó (đóng / "Tiếp tục dùng gói Free")
- **Task Flow**: bước 2–4 của **TF-007**; bước 1 của **TF-009**
- **Transitions**: sheet toàn màn trượt lên `${animation.spring.smooth}`; bảng so sánh mở rộng spring 0,3s

---

### 3.11 WF-011 — Xác Nhận Giá 📱 · *Template B (Action)*

**Design System**: `bento-grid`
**Archetype**: Action | **Density**: Light (2 vùng — **cố ý tối giản**)
**Source UC**: UC-026 (chính), UC-027, UC-030
**Source FR**: **FR-048** (điểm chặn duy nhất), **FR-049** (xử lý giao dịch), **FR-054** (Lifetime không có ngày gia hạn)
**User Intent**: "Tôi muốn thấy chính xác con số sẽ bị trừ và ngày bị trừ, trước khi tôi đồng ý."

**Action Layer → Visual Hierarchy**

| UC Action Layer | Slot | Ghi chú |
|---|---|---|
| Layer 1 — Primary: chạm "Xác nhận" | **#3** | Mở dialog thanh toán của Apple; ghi `price_confirmed` **trước** |
| Layer 2 — Contextual: quay lại WF-010 đổi bậc | #4 | Nút quay lại |
| Layer 3 — Discovery: **trống có chủ ý** | — | Màn này **không được có gì để khám phá**; mọi thứ gây phân tán làm tăng nguy cơ bấm mà không đọc (BR-048.3) |
| Layer 4 — Personal: xem điều khoản và chính sách hoàn tiền | #4 | Chrome |

**Visual Hierarchy**
1. **Bảng 4 mốc** — bậc đã chọn · **giá cuối bằng tiền tệ địa phương** · ngày hết trial · **ngày bị trừ tiền**. `${typography.scale.h3}` cho số tiền, mono.
2. **Chu kỳ gia hạn** — dòng dưới bảng, `${typography.scale.body}`.
3. **CTA "Xác nhận"** — cố định đáy.
4. **Chrome**: nút quay lại, link điều khoản + chính sách hoàn tiền.

*Self-check*: CTA 50pt ⇒ đạt. Bốn mốc **cùng hiển thị** (không cần cuộn, không cần mở ra) ⇒ đúng AC-026.1. Zone C trống ⇒ đúng BR-048.3.

**Required Features (FR)**
- FR-048 P1: Zone A hiện **đồng thời** 4 mốc + chu kỳ gia hạn
- FR-048 P2 / FR-054: bậc Lifetime → **không** hiện ngày gia hạn; nêu rõ "một lần, không tự động gia hạn"
- FR-048 **P3**: Zone C **trống có chủ ý**
- FR-048 P5: ghi `price_confirmed` **trước khi** gọi dialog thanh toán
- FR-048 **BR-048.1**: **không có đường nào** tới thanh toán mà bỏ qua màn này
- FR-047 ERR-047.2: đổi vùng App Store giữa lúc mua → **đọc lại** giá từ StoreKit
- FR-049 P3: thành công → mở khoá ≤ 2s, **không** cần khởi động lại app
- FR-049 ERR-049.1/2: thất bại → nêu nguyên nhân StoreKit + [Thử lại], **giữ nguyên ở màn này**; huỷ ở dialog → giữ lựa chọn

**UX Enhancements** (`composition.action.defaults`)
- `single-primary-cta`: đúng một CTA
- `escape-route-always-visible`: nút quay lại
- `confirmation-dialog`: chính màn này **là** bước xác nhận — không thêm alert thứ hai
- **Không** có `progress-indicator`, **không** có nội dung khám phá, **không** có bán thêm — sự thiếu vắng là thiết kế

**Content Zones Map**

```
┌─────────────────────────────────────┐
│ ZONE D: Navigation                  │ ← 44pt: [<] Xác nhận
├─────────────────────────────────────┤
│ ZONE A: Context — bảng 4 mốc        │ ← ~200pt, static
├─────────────────────────────────────┤
│ ZONE B: Primary CTA                 │ ← 50pt safeAreaInset
├─────────────────────────────────────┤
│ ZONE C: — TRỐNG CÓ CHỦ Ý            │ ← height 0 (BR-048.3)
└─────────────────────────────────────┘
```

**Layout** — *bậc Yearly có trial*

```
┌──────────────────────────────────────────────┐
│  [<]              Xác nhận                   │ ZONE D 44pt
├──────────────────────────────────────────────┤
│ ┌──────────────────────────────────────────┐ │ ZONE A ~200pt
│ │  Carbina Premium — Hằng năm              │ │ card r=16 p=16
│ │  ──────────────────────────────────────  │ │ shadow.1
│ │                                          │ │
│ │  Dùng thử miễn phí       7 ngày          │ │ row 44pt
│ │  Trial hết hạn           24/08/2026      │ │ mono cho ngày
│ │  ──────────────────────────────────────  │ │ divider inset 16
│ │  Bị trừ tiền vào         24/08/2026      │ │ NHẤN MẠNH
│ │  Số tiền                 29,99 $         │ │ h3 22/600 mono
│ │  ──────────────────────────────────────  │ │
│ │  Sau đó tự động gia hạn 29,99 $/năm      │ │ body textSecondary
│ │  cho tới khi bạn huỷ.                    │ │
│ └──────────────────────────────────────────┘ │
│                                              │
│  (Zone C: KHÔNG có nội dung — có chủ ý)      │
│                                              │
├──────────────────────────────────────────────┤
│ .safeAreaInset(bottom):                      │ ZONE B
│ ┌──────────────────────────────────────────┐ │
│ │             Xác nhận                     │ │ h=50 bg accent
│ └──────────────────────────────────────────┘ │ ghi price_confirmed
│  Điều khoản · Chính sách hoàn tiền           │ TRƯỚC dialog Apple
└──────────────────────────────────────────────┘
```

**Components**
- `NavBarStandard` — `[<]` quay lại WF-010, giữ lựa chọn.
- `CardPriceConfirm` — Tokens: `radius: 16`, `padding: 16`, `shadow: ${shadow.elevation.1}`, `border: 1px ${color.palette.border}`. Row 44pt, divider `${component.divider}` inset 16. **Mọi số và ngày dùng `${typography.family.mono}`**; số tiền dùng `${typography.scale.h3}`.
- `BtnPrimary` ("Xác nhận").
- `LinkFootnote` ×2 — Tokens: `font: ${typography.scale.footnote}`, `color: ${color.palette.textTertiary}`.

**States** (7)

| State | Loại | Context | Layout/Behavior |
|---|---|---|---|
| **First Visit** | user-context | Bậc có trial (Monthly/Yearly) | Hiện đủ 4 mốc: bắt đầu trial · hết trial · ngày trừ · số tiền |
| **Returning** | user-context | Bậc Lifetime | **Không** hiện ngày gia hạn; nêu rõ "một lần, không tự động gia hạn" — **sự thiếu vắng thông tin gia hạn chính là thông điệp** |
| **Error** | user-context | Thanh toán thất bại (ERR-049.1) | Nêu **nguyên nhân từ StoreKit** + [Thử lại]; **giữ nguyên ở màn này**, không trả về WF-010 |
| **Default** | data | Giá xác thực từ StoreKit | Layout như trên |
| **Loading** | data | Dialog Apple đang mở / giao dịch `pending` | CTA hiện spinner; nêu rõ "giao dịch đang xử lý"; **không** mở khoá trước khi xác thực (BR-049.1) |
| **Empty** | data | Không áp dụng — luôn có bậc đã chọn | **Không tồn tại có chủ ý**; vào màn này mà không có bậc là lỗi điều hướng |
| **Offline** | data | Mất mạng trước khi xác nhận | Đọc lại giá thất bại → báo lỗi rõ + [Thử lại]; **cấm** dùng giá đã cache (BR-047.1) |

**User Flow**
- **Entry**: chọn một bậc giá trên **WF-010** — **entry duy nhất** (BR-048.1)
- **Exit**: dialog thanh toán iOS → màn hình trước paywall (thành công, ≤ 2s) · **WF-010** (quay lại, giữ lựa chọn) · **WF-030** (toast xác nhận sau khi mua)
- **Task Flow**: bước 5–7 của **TF-007**; bước 2–3 của **TF-009**
- **Transitions**: push từ WF-010; dialog Apple là modal hệ thống; sau thành công crossfade về màn trước paywall 0,25s

---

### 3.12 WF-012 — Cài Đặt Chung 📱 · *Template D (Management)*

**Design System**: `bento-grid`
**Archetype**: Management | **Density**: **Dense** (7 vùng)
**Source UC**: UC-009 (chính), UC-004, UC-029, UC-031, UC-032, UC-033, UC-035, UC-036
**Source FR**: **FR-015** (âm lượng sound), **FR-055** (ngôn ngữ), **FR-057** (xoá dữ liệu), **FR-059** (đánh giá), **FR-061** (theme), **FR-062** (lối vào quyền)
**User Intent**: "Tôi muốn tìm và điều chỉnh một thứ cụ thể mà tôi biết là có ở đâu đây."

**Action Layer → Visual Hierarchy**

| UC Action Layer | Slot | Ghi chú |
|---|---|---|
| Layer 1 — Primary: điều chỉnh âm lượng sound | **#3** | Mục được dùng nhiều nhất ở màn này; là control, không phải nút |
| Layer 2 — Contextual: slider âm lượng · bộ chọn theme · dòng "Ngôn ngữ" | **#2** | Nhóm "Trình bày" |
| Layer 3 — Discovery: dòng "Quyền" · "Về Carbina" · "Đánh giá Carbina" | #4 | Nhóm "Thông tin" |
| Layer 4 — Personal: "Đăng ký của tôi" · "Quyền riêng tư & dữ liệu" · "Tài khoản" *(MVP 3)* | **#1** (badge gói), #4 | Badge gói ở Zone A là thứ mắt bắt đầu tiên |

**Visual Hierarchy**
1. **Badge trạng thái gói hiện tại** — Zone A, `${component.statusBadge}` + dòng phụ. Câu hỏi số 1 khi mở Cài đặt là *"tôi đang ở gói nào"*.
2. **Slider âm lượng sound + nút nghe thử** — nhóm đầu tiên, control lớn nhất.
3. **Các nhóm dòng cài đặt** — row 50pt, có trạng thái **ngay trên dòng**.
4. **Chrome**: nav bar, tab bar, nhóm quản trị ở đáy.

*Self-check*: có thể quét 7–8 dòng không cần cuộn ⇒ đạt. Row nhất quán 50pt (68pt khi có subtitle) ⇒ đạt. Không có swipe action ở màn này (không có gì để xoá theo dòng) ⇒ đúng, và đó là lý do không vẽ.

**Required Features (FR)**
- FR-015 P1–P5: slider lưu ngay **không cần nút Lưu**; kéo → sound mẫu ≤ 300ms; 0 → hiện chữ "đang tắt"; **không** đổi âm lượng nhạc
- FR-055 P1: dòng "Ngôn ngữ" hiện **giá trị hiện tại ngay trên dòng**
- FR-061 P1–P4: bộ chọn theme + **preview widget nhỏ cập nhật ngay** (SF-021)
- FR-057 P1–P2: dòng "Quyền riêng tư & dữ liệu" → liệt kê **từng loại** dữ liệu + số ngày sẽ mất
- FR-059 ERR-059.2: dòng "Đánh giá Carbina" **luôn có sẵn**, không có điều kiện kích hoạt
- FR-053 P1: dòng "Đăng ký của tôi" hiện **trạng thái ngay trên dòng**
- FR-062 P1–P2: dòng "Quyền" hiện số quyền đã cấp / tổng + tính năng bị ảnh hưởng
- FR-064: dòng "Tài khoản" **chỉ xuất hiện từ MVP 3** — ở MVP 1 **không** render

**UX Enhancements** (`composition.management.defaults`)
- `grouped-rows`: 3 nhóm — Trình bày · Thông tin · Quản trị
- `inline-status-on-row`: mọi dòng có trạng thái hiện ngay trên dòng
- `destructive-needs-confirm`: "Xoá dữ liệu" → WF-029 alert
- `pull-to-refresh`: **không dùng** — nội dung là cấu hình cục bộ, không có gì để làm mới
- Slider có phản hồi âm thanh tức thì (SF-004); nhãn giá trị hiện cạnh núm khi kéo rồi mờ sau 1s
- Đổi theme dùng **crossfade toàn màn 0,25s** — chuyển động khi đổi màu gây cảm giác giật (SF-021)

**Content Zones Map**

```
┌─────────────────────────────────────┐
│ ZONE D: Navigation                  │ ← 44pt: Cài đặt
├─────────────────────────────────────┤
│ ZONE A: badge gói hiện tại (override)│ ← ~72pt (xem §Notes)
├─────────────────────────────────────┤
│ ZONE B: Actionable List (3 nhóm)    │ ← fill, row 50/68pt, scroll
├─────────────────────────────────────┤
│ ZONE D: Tab Bar                     │ ← 49pt (+34 safe)
├─────────────────────────────────────┤
│ ZONE C: — (unused)                  │ ← height 0
└─────────────────────────────────────┘
```

> **§Notes**: Management override ghi Zone A = "—", nhưng WF-012 dùng Zone A cho badge gói. Justification: trạng thái gói là **ngữ cảnh chi phối** mọi mục cài đặt bên dưới (mục nào khoá, mục nào không) — đặt nó vào một dòng trong danh sách sẽ làm nó bị chìm.

**Layout**

```
┌──────────────────────────────────────────────┐
│ navBar h=44                                  │ ZONE D
│               Cài đặt                        │
├──────────────────────────────────────────────┤
│ ┌──────────────────────────────────────────┐ │ ZONE A ~72pt
│ │ ●Gói Free                                │ │ StatusBadge 24pt
│ │  1 widget · 3 âm thanh · vô thời hạn      │ │ caption
│ │                        [Xem các gói >]   │ │ → WF-010
│ └──────────────────────────────────────────┘ │
├──────────────────────────────────────────────┤
│  TRÌNH BÀY                                   │ ZONE B nhóm 1
│ ┌──────────────────────────────────────────┐ │
│ │ Âm lượng âm thanh Carbina            [▶] │ │ row 68pt
│ │ ━━━━━━━━━━━━●────────────  70%           │ │ slider t=4 thumb=28
│ │ Độc lập với âm lượng nhạc                │ │ caption
│ ├──────────────────────────────────────────┤ │
│ │ Giao diện        Sáng│Tối│▸Theo hệ thống │ │ segmented 36pt
│ │ ┌────────┐  preview widget cập nhật ngay │ │ SF-021
│ │ │[widget]│                                │ │
│ │ └────────┘                                │ │
│ ├──────────────────────────────────────────┤ │
│ │ Ngôn ngữ              Theo hệ thống  [>] │ │ row 50pt
│ └──────────────────────────────────────────┘ │ → WF-026
│                                              │
│  THÔNG TIN                                   │ nhóm 2
│ ┌──────────────────────────────────────────┐ │
│ │ Quyền                      1/2 đã cấp[>] │ │ trạng thái NGAY
│ │ Đánh giá Carbina                     [>] │ │ trên dòng
│ │ Về Carbina                    2.4    [>] │ │ mono cho version
│ └──────────────────────────────────────────┘ │
│                                              │
│  QUẢN TRỊ                                    │ nhóm 3
│ ┌──────────────────────────────────────────┐ │
│ │ Đăng ký của tôi              Gói Free[>] │ │ → WF-025
│ │ Quyền riêng tư & dữ liệu             [>] │ │ → WF-029
│ └──────────────────────────────────────────┘ │
│  (dòng "Tài khoản" KHÔNG render ở MVP 1)     │
├──────────────────────────────────────────────┤
│ tabBar h=49 · [🏠][♫][▦][▸⚙]                │ ZONE D
└──────────────────────────────────────────────┘
```

**Layout Variants** *(bắt buộc: Dense density)*

**Variant A — Premium / Trial đang chạy**
```
┌──────────────────────────────────────────────┐
│ ┌──────────────────────────────────────────┐ │ ZONE A đổi
│ │ ●Trial còn 3 ngày                        │ │ accentSubtle
│ │  Trừ 29,99 $ vào 24/08/2026               │ │ mono · KHÔNG
│ │                    [Quản lý đăng ký >]   │ │ đếm ngược
│ └──────────────────────────────────────────┘ │ → WF-025
│  … TRÌNH BÀY (như mặc định) …                │
│  QUẢN TRỊ                                    │
│ ┌──────────────────────────────────────────┐ │
│ │ Đăng ký của tôi   Hằng năm · gia hạn 24/08│ trạng thái ĐẦY ĐỦ
│ │ Quyền riêng tư & dữ liệu   14 ngày dữ liệu│ số ngày sẽ mất
│ └──────────────────────────────────────────┘ │
└──────────────────────────────────────────────┘
```

**Variant B — Lifetime (không có gì để huỷ)**
```
┌──────────────────────────────────────────────┐
│ ┌──────────────────────────────────────────┐ │
│ │ ●Đã mua vĩnh viễn                        │ │ semantic.success
│ │  Mọi tính năng Premium, không gia hạn     │ │
│ └──────────────────────────────────────────┘ │ KHÔNG có nút
│  … TRÌNH BÀY …                               │ "Xem các gói"
│  QUẢN TRỊ                                    │
│ ┌──────────────────────────────────────────┐ │
│ │ Đăng ký của tôi        Vĩnh viễn     [>] │ │ WF-025 sẽ KHÔNG
│ │ Quyền riêng tư & dữ liệu             [>] │ │ hiện nút huỷ
│ └──────────────────────────────────────────┘ │ (AC-029.3)
└──────────────────────────────────────────────┘
```

**Components**
- `NavBarStandard` (không có nút back — đây là tab root).
- `CardPlanStatus` (Zone A) — Tokens: `radius: 16`, `padding: 16`, `background: ${color.palette.surface}` / `${color.palette.accentSubtle}` (trial) / `${color.semantic.success.background}` (lifetime).
- `RowSliderVolume` — Tokens: `height: ${component.row.heightWithSubtitle}`(68), slider `trackHeight: 4`, `thumbSize: 28`, active `${color.palette.accent}`, track `${color.palette.surfaceVariant}`; nhãn % dùng mono; lưu ngay khi nhả tay.
- `RowSegmentedTheme` + `MiniWidgetPreview` — Tokens: segmented `height: 36`, `radius: 12`; preview 64×40 `radius: ${border.radius.md}`(8); crossfade toàn màn `${animation.duration.normal}`(0,25s).
- `RowNavigable` — Tokens: `height: ${component.row.height}`(50), `chevronSize: 14`, trạng thái phải `${typography.scale.callout}` `${color.palette.textSecondary}`.
- `SectionHeaderGroup` — Tokens: `font: ${typography.scale.caption}`, `color: ${color.palette.textSecondary}`.
- `TabBarCustom` — như WF-006, tab Cài đặt active.

**States** (8)

| State | Loại | Context | Layout/Behavior |
|---|---|---|---|
| **First Visit** | user-context | Gói Free, vừa onboard | Zone A "Gói Free" + [Xem các gói]; dòng "Tài khoản" **không** render |
| **Returning** | user-context | Premium hoặc trial đang chạy | **Variant A**: Zone A hiện gói + ngày gia hạn; dòng đăng ký hiện trạng thái đầy đủ |
| **Power User** | user-context | Lifetime | **Variant B**: "Đã mua vĩnh viễn"; **không** nút "Xem các gói"; WF-025 sẽ không hiện nút huỷ |
| **Error** | user-context | Không đọc được trạng thái subscription | Zone A hiện "chưa xác định" + [Phục hồi giao dịch]; **các mục khác vẫn dùng được bình thường** |
| **Default** | data | Mọi cấu hình đọc xong | Layout như trên |
| **Loading** | data | Truy vấn StoreKit cho Zone A | Zone A hiện skeleton 72pt; **nhóm TRÌNH BÀY vẫn dùng được ngay** (không phụ thuộc StoreKit) |
| **Empty** | data | Chưa có dữ liệu học | Dòng "Quyền riêng tư & dữ liệu" hiện **"chưa có dữ liệu học nào"**; nút xoá trong WF-029 sẽ bị vô hiệu (VR-057.1) |
| **Offline** | data | Không có mạng | Nhóm TRÌNH BÀY và THÔNG TIN hoạt động đầy đủ; Zone A dùng entitlement cache đã xác thực (BR-043.3) |

**User Flow**
- **Entry**: tab **Cài đặt** · icon ⚙ trên **WF-006** · badge gói trên **WF-006**
- **Exit**: **WF-010** · **WF-025** · **WF-026** · **WF-029** · **WF-005** (dòng "Quyền", qua FR-062) · **WF-015** *(MVP 3)* · **WF-028** (qua dòng Đánh giá nếu không hài lòng) · Cài đặt hệ thống iOS · **WF-030** (toast)
- **Task Flow**: bước 7 của **TF-005** · bước 1 của **TF-012** · bước 1 của **TF-008** (nếu chủ động huỷ)
- **Transitions**: push cho các màn con; sheet cho WF-025/WF-026/WF-028; alert cho WF-029; theme crossfade toàn màn 0,25s

---

### 3.13 WF-013 — Nhắc Hết Trial 📱 · *Template B (Action)*

**Design System**: `bento-grid`
**Archetype**: Action | **Density**: Light (3 vùng)
**Source UC**: UC-028 (chính), UC-027 | **Source FR**: **FR-052** (nhắc hết trial), **FR-051** (quản lý trial)
**User Intent**: "Tôi muốn biết mình sắp bị trừ bao nhiêu và khi nào, để tôi kịp quyết định."

**Action Layer → Visual Hierarchy**

| UC Action Layer | Slot | Ghi chú |
|---|---|---|
| Layer 1 — Primary: chọn một trong ba — "Nhắc sau" · "Đăng ký" · **"Huỷ trial"** | **#3** | Ba nút **ngang hàng thị giác** (BR-052.1) |
| Layer 2 — Contextual: xem lại tính năng đang có nhờ trial | #4 | Dòng phụ, thu gọn |
| Layer 3 — Discovery: **trống có chủ ý** | — | Màn hình **quyết định**, không phải màn bán thêm (BR-052.4) |
| Layer 4 — Personal: lối vào WF-025 xem chi tiết đăng ký | #4 | Chrome |

**Visual Hierarchy**
1. **Số ngày còn lại + số tiền + ngày bị trừ** — Zone A, số tiền `${typography.scale.h3}` mono. Ba con số này là toàn bộ lý do màn này tồn tại.
2. **Dòng giải thích chu kỳ** — `${typography.scale.body}`.
3. **Ba nút ngang hàng** — cùng chiều cao 50pt, cùng chiều rộng; "Đăng ký" là `BtnPrimary`, hai nút kia là `BtnSecondary`/`BtnDestructiveOutline` — **khác màu nhưng không khác trọng lượng thị giác**.
4. **Chrome**: nút đóng, dòng "Xem chi tiết đăng ký".

*Self-check*: cả ba nút 50pt ⇒ đạt. Nút "Huỷ trial" **không** bị ẩn hay làm mờ ⇒ đúng AC-028.2. Không có đếm ngược ⇒ đúng AC-028.4.

**Required Features (FR)**
- FR-052 P1: Zone A hiện số ngày còn lại · **số tiền chính xác** · **ngày bị trừ**
- FR-052 P2 / **BR-052.1**: ba nút **ngang hàng thị giác**, gồm cả "Huỷ trial"
- FR-052 P3 / BR-052.2: "Nhắc sau" tối đa **2 lần**; sau đó nút biến mất
- FR-052 **BR-052.3**: **cấm** đếm ngược gây áp lực và ngôn từ khan hàng giả tạo
- FR-052 **BR-052.4**: Zone C **cấm** có nội dung bán thêm
- FR-051 ERR-051.4: không đọc được ngày hết trial → nêu rõ **không xác định được** + dẫn trang subscription iOS; **tuyệt đối không đoán một con số**

**UX Enhancements** (`composition.action.defaults`)
- `escape-route-always-visible`: cả "Nhắc sau" và "Huỷ trial" đều là đường thoát
- `confirmation-dialog`: "Huỷ trial" → WF-027 alert
- `single-primary-cta`: **sai lệch có chủ ý** — ba lựa chọn ngang hàng là **yêu cầu chống dark pattern**, không phải thiếu sót thiết kế
- **Không** progress indicator, **không** đếm ngược, **không** bán thêm

**Content Zones Map**

```
┌─────────────────────────────────────┐
│ ZONE D: Navigation                  │ ← 44pt: [✕]
├─────────────────────────────────────┤
│ ZONE A: Context — 3 con số          │ ← ~160pt, static
├─────────────────────────────────────┤
│ ZONE B: 3 nút ngang hàng            │ ← 3×50pt + gap 12
├─────────────────────────────────────┤
│ ZONE C: — TRỐNG CÓ CHỦ Ý            │ ← height 0 (BR-052.4)
└─────────────────────────────────────┘
```

**Layout** — *ngày 6 của trial*

```
┌──────────────────────────────────────────────┐
│  [✕]                                         │ ZONE D 44pt
├──────────────────────────────────────────────┤
│ ┌──────────────────────────────────────────┐ │ ZONE A ~160pt
│ │  Trial của bạn còn 1 ngày                │ │ h3 22/600
│ │  ──────────────────────────────────────  │ │
│ │  Sẽ bị trừ         29,99 $               │ │ h3 mono
│ │  Vào ngày          24/08/2026            │ │ body mono
│ │  ──────────────────────────────────────  │ │
│ │  Sau đó gia hạn 29,99 $/năm cho tới khi   │ │ body textSecondary
│ │  bạn huỷ. Huỷ bất cứ lúc nào.             │ │ tông TRUNG TÍNH
│ └──────────────────────────────────────────┘ │ KHÔNG đếm ngược
│                                              │
│  (Zone C: KHÔNG có nội dung bán thêm)        │
│                                              │
├──────────────────────────────────────────────┤
│ ┌──────────────────────────────────────────┐ │ ZONE B
│ │              Đăng ký                     │ │ BtnPrimary h=50
│ └──────────────────────────────────────────┘ │ bg accent
│ ┌──────────────────────────────────────────┐ │ ${spacing.md}
│ │              Nhắc sau                    │ │ BtnSecondary h=50
│ └──────────────────────────────────────────┘ │ border 1px
│ ┌──────────────────────────────────────────┐ │
│ │             Huỷ trial                    │ │ BtnDestructive h=50
│ └──────────────────────────────────────────┘ │ border + chữ đỏ
│  Xem chi tiết đăng ký                        │ → WF-025
│  BA NÚT CÙNG CHIỀU CAO VÀ CHIỀU RỘNG          │
└──────────────────────────────────────────────┘
```

**Components**
- `NavBarModal` — `[✕]` đóng.
- `CardTrialSummary` — Tokens: `radius: 16`, `padding: 16`, `shadow: ${shadow.elevation.1}`; số tiền `${typography.scale.h3}` + mono; ngày mono.
- `BtnPrimary` ("Đăng ký"), `BtnSecondary` ("Nhắc sau"), `BtnDestructiveOutline` ("Huỷ trial") — Tokens: cả ba `height: 50`, `radius: 16`, `font: ${typography.scale.button}`. Destructive: `background: transparent`, `foreground: ${color.semantic.destructive.color}`, `borderColor: ${color.semantic.destructive.color}`.
- `BtnTertiary` ("Xem chi tiết đăng ký") → WF-025.

**States** (7)

| State | Loại | Context | Layout/Behavior |
|---|---|---|---|
| **First Visit** | user-context | Ngày 6 của trial | "còn 1 ngày" + số tiền + ngày trừ; tông trung tính |
| **Returning** | user-context | Ngày 7, đã chọn "Nhắc sau" 1 lần | Nêu rõ đây là lần nhắc cuối; sau lần thứ hai nút "Nhắc sau" **biến mất** |
| **Power User** | user-context | Muốn huỷ ngay | "Huỷ trial" → WF-027 → WF-025; **tối đa 3 chạm** là huỷ được |
| **Error** | user-context | Không đọc được ngày hết trial (ERR-051.4) | Nêu rõ **"không xác định được ngày"** + dẫn trang subscription iOS; **không đoán con số**; ba nút vẫn hiện |
| **Default** | data | Dữ liệu trial đọc xong | Layout như trên |
| **Loading** | data | Truy vấn StoreKit | Zone A hiện skeleton 160pt; **các nút bị vô hiệu tạm** — cấm cho quyết định khi chưa biết số tiền |
| **Empty** | data | Không áp dụng — chỉ hiện khi có trial | **Không tồn tại có chủ ý**; hệ thống không hiển thị màn này nếu không có trial đang chạy |

**User Flow**
- **Entry**: hệ thống kích hoạt vào **ngày 6 và ngày 7** của trial (FR-052 P1) — không có entry thủ công
- **Exit**: **WF-006** ("Nhắc sau" / "Đăng ký") · **WF-027** → **WF-025** ("Huỷ trial") · **WF-025** ("Xem chi tiết")
- **Task Flow**: bước 1–4 của **TF-008**
- **Transitions**: sheet trượt lên `${animation.spring.smooth}`; alert WF-027 fade-in 0,2s

---

### 3.14 WF-014 — Chẩn Đoán Tương Thích 📱 · *Template D (Management)*

**Design System**: `bento-grid`
**Archetype**: Management | **Density**: Medium (4 vùng)
**Source UC**: UC-017 (chính), UC-013, UC-016 | **Source FR**: **FR-032** (chẩn đoán + báo cáo), **FR-066** (telemetry)
**User Intent**: "Tôi muốn biết chuyện gì đã xảy ra trên xe tôi, và làm gì để nó được sửa."

**Action Layer → Visual Hierarchy**

| UC Action Layer | Slot | Ghi chú |
|---|---|---|
| Layer 1 — Primary: xem dữ liệu kỹ thuật và gửi báo cáo nếu có lỗi | **#3** | CTA "Gửi báo cáo" → WF-028 |
| Layer 2 — Contextual: xem kích thước scene · xem trạng thái render từng lần · mở rộng dòng | **#2** | Danh sách lịch sử |
| Layer 3 — Discovery: "Xem widget ở kích thước này" → WF-023 · đọc giải thích vì sao lỗi | #4 | Trong dòng mở rộng |
| Layer 4 — Personal: sao chép dữ liệu chẩn đoán · xoá lịch sử chẩn đoán | #4 | Chrome |

**Visual Hierarchy**
1. **Kích thước màn hình xe đã nhận** — Zone A, `${typography.scale.stat}` mono 40pt. Con số **thật**, không suy đoán. Đây là thứ biến "app rác" thành "một vấn đề chẩn đoán được".
2. **Danh sách các lần kết nối gần nhất** — row 68pt, có kết quả render.
3. **CTA "Gửi báo cáo"** — cố định đáy; nổi bật khi lần gần nhất thất bại.
4. **Chrome**: nav bar, nút sao chép, dòng xoá lịch sử, phiên bản iOS + xe đã chọn.

*Self-check*: quét được 5–6 dòng lịch sử không cuộn ⇒ đạt. Row nhất quán 68pt ⇒ đạt. Không có swipe action — xoá lịch sử là hành động **toàn bộ**, không theo dòng ⇒ đúng, nên không vẽ swipe.

**Required Features (FR)**
- FR-032 P1: hiển thị **kích thước scene thật đã nhận**, không phải giá trị suy đoán
- FR-032 P2: danh sách lần kết nối gần nhất + kết quả render; đánh dấu đỏ nếu lần gần nhất thất bại
- FR-032 P3: mở rộng dòng → `failure_reason` phân biệt `overflow` / `memory` + nút "Xem widget ở kích thước này" → WF-023 (SF-016)
- FR-032 P6–P7: nút sao chép payload; nút xoá lịch sử chẩn đoán (**không** ảnh hưởng cấu hình widget hay entitlement)
- FR-032 ERR-032.1: chưa từng kết nối → **hướng dẫn cắm xe**, **không** bảng trống
- FR-066 ERR-066.3: lỗi lặp ≥ 3 lần cùng kích thước → đánh dấu ưu tiên cao

**UX Enhancements** (`composition.management.defaults`)
- `grouped-rows`: nhóm "Thiết bị & xe" và "Lịch sử kết nối"
- `inline-status-on-row`: mỗi dòng lịch sử có chấm trạng thái + kết quả
- `destructive-needs-confirm`: "Xoá lịch sử chẩn đoán" cần xác nhận
- `pull-to-refresh`: **dùng** — đọc lại lịch sử kết nối sau khi vừa từ xe vào
- Chỉ **một** dòng mở rộng tại một thời điểm; dòng khác thu lại đồng thời để chiều cao tổng không nhảy (SF-016)
- Dữ liệu kỹ thuật dùng **mono đơn sắc** — để đọc rõ đây là số liệu, không phải nội dung marketing

**Content Zones Map**

```
┌─────────────────────────────────────┐
│ ZONE D: Navigation + Tools          │ ← 44pt: [<] + [copy]
├─────────────────────────────────────┤
│ ZONE A: kích thước scene thật(override)│ ← ~140pt (xem §Notes WF-012)
├─────────────────────────────────────┤
│ ZONE B: Actionable List — lịch sử   │ ← fill, row 68pt, .refreshable
├─────────────────────────────────────┤
│ ZONE D: CTA + xoá lịch sử           │ ← 50pt + 44pt
└─────────────────────────────────────┘
```

**Layout** — *lần gần nhất thất bại*

```
┌──────────────────────────────────────────────┐
│ navBar h=44                                  │ ZONE D
│  [<]   Chẩn đoán tương thích        [⧉]     │ nút sao chép
├──────────────────────────────────────────────┤
│ ┌──────────────────────────────────────────┐ │ ZONE A ~140pt
│ │ MÀN HÌNH XE ĐÃ NHẬN ĐƯỢC                 │ │ caption
│ │                                          │ │
│ │      1180 × 420                          │ │ stat 40pt MONO
│ │      accent · số THẬT, không suy đoán     │ │
│ │  ──────────────────────────────────────  │ │
│ │  iOS 17.4.1 · Toyota Camry 2022          │ │ monoData 13pt
│ │  ⚠ Lần gần nhất: render thất bại          │ │ semantic.error
│ └──────────────────────────────────────────┘ │
├──────────────────────────────────────────────┤
│  LỊCH SỬ KẾT NỐI                             │ ZONE B
│ ┌──────────────────────────────────────────┐ │ .refreshable
│ │ ● 17/08 07:42   1180×420   thất bại  [v] │ │ row 68pt
│ │   semantic.error · overflow                │ │ mở rộng được
│ ├──────────────────────────────────────────┤ │
│ │ ● 16/08 18:10   1180×420   OK            │ │ semantic.success
│ ├──────────────────────────────────────────┤ │
│ │ ● 16/08 07:38   1180×420   OK            │ │
│ ├──────────────────────────────────────────┤ │
│ │ ● 15/08 17:55   1180×420   OK            │ │
│ └──────────────────────────────────────────┘ │ scroll
├──────────────────────────────────────────────┤
│ ┌──────────────────────────────────────────┐ │ ZONE D
│ │           Gửi báo cáo                    │ │ h=50 bg accent
│ └──────────────────────────────────────────┘ │ → WF-028
│  Xoá lịch sử chẩn đoán                       │ BtnTertiary
│  KHÔNG ảnh hưởng widget hay gói của bạn      │ footnote
└──────────────────────────────────────────────┘
```

**Layout Variants** *(bắt buộc: Medium density)*

**Variant A — Dòng lịch sử đã mở rộng (SF-016)**
```
┌──────────────────────────────────────────────┐
│ ┌ 1180 × 420 · iOS 17.4.1 · Camry 2022 ─────┐│
├──────────────────────────────────────────────┤
│ ┌──────────────────────────────────────────┐ │ dòng MỞ RỘNG
│ │ ● 17/08 07:42   1180×420   thất bại  [^] │ │
│ │ ──────────────────────────────────────── │ │
│ │  Nguyên nhân   vượt vùng an toàn         │ │ overflow ≠ memory
│ │  Phần tử       counter chuyến đi         │ │ nêu RÕ phần tử
│ │  Loại widget   carPhoto                  │ │ monoData
│ │  Dynamic Type  1.35×                     │ │ mono
│ │                                          │ │
│ │  [Xem widget ở kích thước này >]         │ │ → WF-023
│ └──────────────────────────────────────────┘ │
│ │ ● 16/08 18:10 … (thu lại đồng thời)      │ │ chỉ MỘT dòng mở
├──────────────────────────────────────────────┤
│ [           Gửi báo cáo           ]          │
└──────────────────────────────────────────────┘
```

**Variant B — Chưa từng kết nối CarPlay (ERR-032.1)**
```
┌──────────────────────────────────────────────┐
│  [<]   Chẩn đoán tương thích        [⧉]     │
├──────────────────────────────────────────────┤
│ ┌──────────────────────────────────────────┐ │ ZONE A đổi HOÀN
│ │ 🚗 Chưa có dữ liệu từ xe của bạn         │ │ TOÀN — KHÔNG
│ │                                          │ │ bảng trống
│ │ Cắm iPhone vào xe một lần, Carbina sẽ    │ │ body
│ │ ghi lại kích thước màn hình xe và hiện   │ │
│ │ ở đây.                                   │ │ hướng dẫn cụ thể
│ │                                          │ │
│ │ 1. Cắm cáp hoặc bật CarPlay không dây     │ │
│ │ 2. Chờ Carbina hiện trên màn hình xe      │ │
│ │ 3. Mở lại màn này                        │ │
│ └──────────────────────────────────────────┘ │
│  ✗ KHÔNG có danh sách lịch sử                │
├──────────────────────────────────────────────┤
│ [        Gửi báo cáo        ] ← VÔ HIỆU      │ chưa có dữ liệu
└──────────────────────────────────────────────┘  để gửi (VR-032.2)
```

**Components**
- `NavBarStandard` + `IconButtonCopy` (⧉) — sao chép payload dạng chữ.
- `CardSceneMetrics` (Zone A) — Tokens: `radius: 16`, `padding: 16`, `shadow: ${shadow.elevation.1}`; số kích thước `${typography.scale.stat}`(40, mono) `${color.palette.accent}`; metadata `${typography.scale.monoData}`(13, mono).
- `RowDiagnosticExpandable` — Tokens: `height: ${component.row.heightWithSubtitle}`(68), chấm trạng thái `${color.semantic.success.color}` / `${color.semantic.error.color}`; mở rộng `${animation.duration.normal}`(0,25s); mọi giá trị kỹ thuật dùng mono.
- `BtnPrimary` ("Gửi báo cáo") — vô hiệu khi chưa có dữ liệu.
- `BtnTertiary` ("Xoá lịch sử chẩn đoán").
- `CardEmptyGuide` (Variant B) — Tokens: `background: ${color.palette.surface}`, `radius: 16`; danh sách 3 bước.
- `PullToRefreshIndicator` — như WF-006.

**States** (8)

| State | Loại | Context | Layout/Behavior |
|---|---|---|---|
| **First Visit** | user-context | Chưa từng kết nối CarPlay | **Variant B**: hướng dẫn cắm xe 3 bước; CTA vô hiệu; **không** bảng trống |
| **Returning** | user-context | Đã kết nối, mọi lần đều OK | Danh sách toàn `${color.semantic.success.color}`; CTA vẫn có nhưng **không nổi bật** |
| **Power User** | user-context | QA / người dùng gặp lỗi lặp lại | **Variant A**: `failure_reason` phân biệt `overflow`/`memory`; nút sao chép nổi bật |
| **Error** | user-context | Lần gần nhất thất bại | Zone A đánh dấu `${color.semantic.error.color}`; CTA là hành động chính; câu nói rõ **đây là vấn đề tương thích màn hình, không phải lỗi của bạn** |
| **Default** | data | Có lịch sử kết nối | Layout như trên |
| **Loading** | data | Pull-to-refresh đọc lại lịch sử | `PullToRefreshIndicator`; Zone A giữ giá trị cũ |
| **Empty** | data | Đã xoá lịch sử chẩn đoán | Zone A **vẫn hiện kích thước đã biết**; danh sách hiện "đã xoá lịch sử" — phân biệt rõ với Variant B (chưa từng kết nối) |
| **Offline** | data | Không có mạng | Toàn bộ dữ liệu đọc on-device nên hiện đầy đủ; gửi báo cáo sẽ **xếp hàng** (ERR-032.2) |

**User Flow**
- **Entry**: `WarningRow` trên **WF-006** · hướng dẫn từ **WF-019** (khi người dùng mở app iPhone sau chuyến lỗi) · lối vào chủ động từ **WF-006**
- **Exit**: **WF-028** (gửi báo cáo) · **WF-023** ("Xem widget ở kích thước này") · **WF-006** · **WF-030** (toast sau khi gửi)
- **Task Flow**: bước 4–6 của **TF-003**
- **Transitions**: dòng mở rộng 0,25s, dòng khác thu lại đồng thời (SF-016); modal WF-023 trượt lên 0,35s

---

### 3.15 WF-015 — Account 📱 *(MVP 3)* · *Template D (Management)*

**Design System**: `bento-grid`
**Archetype**: Management | **Secondary**: Action | **Density**: Light (3 vùng)
**Source UC**: UC-035 | **Source FR**: **FR-064** (đăng nhập + đồng bộ opt-in), **FR-065** (xoá tài khoản)
**Status**: **Deferred (MVP 3 — tháng 3/2027)** — dòng "Tài khoản" trên WF-012 **không render** ở MVP 1 và MVP 2
**User Intent**: "Tôi muốn cấu hình của mình có mặt trên thiết bị mới, nếu tôi chọn như vậy."

**Action Layer → Visual Hierarchy**

| UC Action Layer | Slot | Ghi chú |
|---|---|---|
| Layer 1 — Primary: đăng nhập email và bật đồng bộ cấu hình | **#3** | CTA "Đăng nhập" hoặc toggle "Đồng bộ cấu hình" |
| Layer 2 — Contextual: đăng xuất · xem thời điểm đồng bộ gần nhất | #4 | Dòng phụ |
| Layer 3 — Discovery: đọc rõ **cái gì được đồng bộ và cái gì không** | **#2** | Bảng hai cột — đây là nội dung quan trọng nhất về niềm tin |
| Layer 4 — Personal: xoá tài khoản và dữ liệu cloud | #4 | Zone D, tách khỏi đăng xuất |

**Visual Hierarchy**
1. **Trạng thái tài khoản + đồng bộ** — Zone A. Kèm câu nêu rõ đây là **tuỳ chọn**.
2. **Bảng hai cột "đồng bộ / không đồng bộ"** — vì cam kết "dữ liệu học không rời thiết bị" phải kiểm tra được, không chỉ được nghe.
3. **CTA đăng nhập / toggle đồng bộ**.
4. **Chrome**: nav bar, dòng đăng xuất, dòng xoá tài khoản.

*Self-check*: CTA 50pt ⇒ đạt. Dòng "Xoá tài khoản" tách khỏi "Đăng xuất" bằng nhóm riêng ⇒ đúng BR-065.3.

**Required Features (FR)**
- FR-064 P1: dòng "Tài khoản" **chỉ xuất hiện từ MVP 3**
- FR-064 **BR-064.1**: tài khoản là **tuỳ chọn tuyệt đối**; app chạy đủ mà không cần nó
- FR-064 P4 / **BR-064.2**: bảng hai cột nêu rõ **chỉ cấu hình** được đồng bộ; **dữ liệu học ngữ cảnh không rời thiết bị**
- FR-064 P6 / BR-064.4: đăng xuất **không** xoá cấu hình cục bộ
- FR-064 P7 / **BR-064.3**: xung đột → **hỏi người dùng chọn bản nào**, cấm tự ghi đè
- FR-065 P1–P2: dòng "Xoá tài khoản" ở Zone D, tách khỏi đăng xuất, cần xác nhận nêu rõ **dữ liệu on-device vẫn còn**

**UX Enhancements** (`composition.management.defaults`)
- `grouped-rows`: nhóm "Đồng bộ" và nhóm "Tài khoản"
- `destructive-needs-confirm`: xoá tài khoản cần xác nhận riêng
- `inline-status-on-row`: thời điểm đồng bộ gần nhất hiện ngay trên dòng
- `pull-to-refresh`: **không dùng** ở MVP 3 phiên bản đầu — sẽ xem lại khi có dữ liệu thật

**Content Zones Map**

```
┌─────────────────────────────────────┐
│ ZONE D: Navigation                  │ ← 44pt: [✕] Tài khoản
├─────────────────────────────────────┤
│ ZONE A: trạng thái tài khoản(override)│ ← ~88pt
├─────────────────────────────────────┤
│ ZONE B: bảng 2 cột + toggle đồng bộ │ ← fill
├─────────────────────────────────────┤
│ ZONE D: đăng xuất + xoá tài khoản   │ ← 2×50pt
└─────────────────────────────────────┘
```

**Layout** — *chưa đăng nhập*

```
┌──────────────────────────────────────────────┐
│  [✕]            Tài khoản                    │ ZONE D 44pt
├──────────────────────────────────────────────┤
│ ┌──────────────────────────────────────────┐ │ ZONE A ~88pt
│ │ Chưa đăng nhập                            │ │ headline
│ │ Đăng nhập là TUỲ CHỌN. Carbina hoạt động  │ │ body
│ │ đầy đủ mà không cần tài khoản.             │ │ textSecondary
│ └──────────────────────────────────────────┘ │ BR-064.1
├──────────────────────────────────────────────┤
│  ĐỒNG BỘ NHỮNG GÌ                            │ ZONE B
│ ┌──────────────────────────────────────────┐ │ bảng 2 cột
│ │                    Đồng bộ  Ở lại máy    │ │ caption header
│ │ Widget đã cấu hình    ✓        —         │ │
│ │ Âm thanh đã gán       ✓        —         │ │
│ │ Ngôn ngữ, giao diện   ✓        —         │ │
│ │ ─────────────────────────────────────    │ │
│ │ Dữ liệu học ngữ cảnh  —        ✓         │ │ NHẤN MẠNH:
│ │ Tuyến đường quen      —        ✓         │ │ KHÔNG rời máy
│ │ Lịch sử chẩn đoán     —        ✓         │ │ (BR-064.2)
│ └──────────────────────────────────────────┘ │
│                                              │
│ ┌──────────────────────────────────────────┐ │
│ │      Đăng nhập bằng email                │ │ h=50 bg accent
│ └──────────────────────────────────────────┘ │
├──────────────────────────────────────────────┤
│  (nhóm đăng xuất / xoá tài khoản: ẩn khi     │ ZONE D
│   chưa đăng nhập)                            │
└──────────────────────────────────────────────┘
```

**Components**
- `NavBarModal` — `[✕]`.
- `CardAccountStatus` (Zone A) — Tokens: `radius: 16`, `padding: 16`, `background: ${color.palette.surface}`.
- `SyncScopeTable` — Tokens: `radius: 16`, `background: ${color.palette.surface}`, `border: 1px ${color.palette.border}`; hàng "không đồng bộ" nhấn mạnh bằng `${color.palette.accentSubtle}`.
- `BtnPrimary` ("Đăng nhập bằng email"), `RowToggle` ("Đồng bộ cấu hình"), `RowNavigable` ("Đăng xuất"), `BtnTertiaryDestructive` ("Xoá tài khoản").

**States** (7)

| State | Loại | Context | Layout/Behavior |
|---|---|---|---|
| **First Visit** | user-context | Chưa có tài khoản | Nêu rõ đây là **tuỳ chọn**; app hoạt động đầy đủ không cần tài khoản |
| **Returning** | user-context | Đã đăng nhập, đồng bộ bật | Hiện thời điểm đồng bộ gần nhất + thiết bị đã liên kết; nhóm đăng xuất/xoá xuất hiện |
| **Power User** | user-context | Hai thiết bị cấu hình khác nhau | Hiện lựa chọn **giữ bản nào**; **cấm** tự ghi đè (BR-064.3) |
| **Error** | user-context | Không kết nối được cloud | Nêu rõ đang dùng cấu hình cục bộ; **mọi tính năng vẫn hoạt động** vì cloud chỉ là lớp tiện ích |
| **Default** | data | Trạng thái tài khoản đọc xong | Layout như trên |
| **Loading** | data | Đang đăng nhập / đang đồng bộ | CTA hiện spinner; bảng 2 cột vẫn đọc được |
| **Empty** | data | Đã đăng nhập nhưng chưa đồng bộ lần nào | Dòng thời điểm hiện "chưa đồng bộ lần nào"; toggle vẫn bật được |

**User Flow**
- **Entry**: dòng "Tài khoản" trên **WF-012** — **chỉ hiện từ MVP 3**
- **Exit**: **WF-012**
- **Task Flow**: chưa có task flow ở MVP 1 — sẽ viết khi lên kế hoạch MVP 3 (`Use_Cases.md` §5 ghi rõ UC-035 chưa có TF)
- **Transitions**: sheet trượt lên `${animation.spring.smooth}`

---

> ### ⚠️ Ràng buộc chung cho 4 màn CarPlay (WF-016 → WF-019)
>
> Bốn màn dưới đây dùng **`composition.carplay`**, không phải composition của archetype thông thường. Ràng buộc áp dụng cho **cả bốn**, không nhắc lại ở từng màn:
>
> | Ràng buộc | Giá trị | Nguồn |
> |---|---|---|
> | Shadow | **`${shadow.elevation.0}` tuyệt đối** | `NFR-007` — render shadow/blur trong widget extension ≤ 25MB là tiêu ngân sách bộ nhớ cho hiệu ứng người lái không có thời gian nhìn |
> | Viền | `${color.palette.borderStrong}` (đậm hơn iPhone) | Giữ ranh giới khi không có độ cao |
> | Cỡ chữ tối thiểu | **16pt** (`${typography.scale.carplayMin}`) | `BR-030.2` — nhỏ hơn thì chữ không phục vụ mục đích gì khi đang lái |
> | Touch target | ≥ 44pt | `AC-023.2`, `AC-NFR-014.3` |
> | Mọi kích thước | **Tỉ lệ theo scene bounds tại runtime** | `BR-029.1` — cấm hằng số kích thước màn hình xe. Số pt trong ASCII dưới đây là **ví dụ ở tỉ lệ 1180×420**, không phải giá trị hardcode |
> | Animation | **Chỉ crossfade 0,4s**, throttle 30s | `BR-040.3` — thẻ trượt qua nhau kéo mắt người lái khỏi đường |
> | Modal / nhập liệu | **Cấm tuyệt đối** | `BR-042.2`, `BR-031.3` |
> | Paywall | **Cấm mọi đường mở paywall** | `BR-045.3` |
> | Haptic | `none` | `animation.haptics.carplay` |
> | Dynamic Type | Giới hạn scale 1,35× | `typography.dynamicType.carplayMaxScale` |
> | Vùng trắng | **0 trường hợp, mọi nhánh lỗi** | `NFR-020` |

---

### 3.16 WF-016 — CarPlay Dashboard 🚗 · *Template A (Discovery)*

**Design System**: `bento-grid` → biến thể **`composition.carplay`**
**Archetype**: Discovery | **Density**: Medium (3–5 vùng — **giới hạn cứng, không được là Dense**)
**Source UC**: UC-022 (chính), UC-005, UC-010, UC-011, UC-021, UC-023, UC-034
**Source FR**: **FR-040** (sắp xếp theo ngữ cảnh), **FR-041** (cấu hình theo entitlement + offline), **FR-042** (chạm thẻ). Hành vi nền diễn ra tại đây: **FR-016/017/018** (sound lên xe), **FR-019/020** (sound xuống xe), **FR-037/038/039** (giọng chào)
**User Intent**: "Tôi muốn nhìn một lượt là thấy thứ tôi cần, và chạm một lần là xong."

**Action Layer → Visual Hierarchy**

| UC Action Layer | Slot | Ghi chú |
|---|---|---|
| Layer 1 — Primary: chạm thẻ liên quan nhất | **#1 + #3** | Thẻ ở Zone A **vừa là hero vừa là hành động chính** — trên màn hình xe, thứ nổi bật nhất phải chính là thứ chạm được |
| Layer 2 — Contextual: chạm một thẻ khác (nhạc / thời tiết / điểm đến / shortcut) | **#2** | Zone B |
| Layer 3 — Discovery | — | **Trống có chủ ý**: không có "xem thêm" trên màn hình xe; mọi thứ đòi người lái đi sâu hơn một tầng là rủi ro an toàn |
| Layer 4 — Personal | — | **Trống có chủ ý**: không có cấu hình trên màn hình xe; mọi cấu hình ở iPhone |

> **§Notes — hai sai lệch có chủ ý**: (1) Layer 1 chiếm **cả #1 và #3** thay vì chỉ #3 — trên bề mặt glanceable, tách "thứ nổi bật nhất" khỏi "thứ chạm được" sẽ buộc người lái nhìn hai lần. (2) Density là Medium dù archetype Discovery thường Dense — giới hạn cứng vì an toàn, ghi ở §2 bis.

**Visual Hierarchy**
1. **Thẻ ưu tiên cao nhất theo ngữ cảnh** — Zone A, chiếm diện tích lớn nhất (~45% bounds). Chạm được. Đây là câu trả lời cho *"tôi cần gì lúc này"*.
2. **2–3 thẻ còn lại** — Zone B, mỗi thẻ chạm một lần là ra hành động.
3. — (gộp vào #1: thẻ hero **là** hành động chính)
4. **Một dòng trạng thái ở mép** — Zone D, **không chắn nội dung**.

*Self-check*: thẻ hero chiếm ~45% bounds, gấp ~2,2× thẻ Zone B ⇒ đạt. Người dùng hoàn tất tác vụ #1 trong < 3s vì chỉ cần một chạm ⇒ đạt. Thẻ hero là phần tử tương phản cao nhất ⇒ đạt.

**Required Features (FR)**
- FR-040 P1: layout tính từ `CPTemplateApplicationScene` bounds **tại runtime**
- FR-040 P3: chưa đủ dữ liệu → thứ tự mặc định + **một dòng nói rõ dashboard sẽ tự đổi sau vài chuyến**
- FR-040 P5–P6: cập nhật thứ tự bằng **crossfade tại chỗ 0,4s**, throttle 1 lần/30s; **hoãn** khi một thẻ đang được chạm
- FR-040 P7: bỏ qua một thẻ → hạ trọng số (phản hồi ngầm, không cần vào Settings)
- FR-041 P3: gói Free → WF-018 **một dòng chữ tĩnh**, không popup, **không chắn nội dung**
- FR-041 P4: mất mạng → thẻ dùng cache + **ghi rõ thời điểm cập nhật cuối**
- FR-042 P1–P4: chạm thẻ → hành động ≤ 1s; thẻ Premium hiện khoá **bằng chữ**, **không** mở paywall; lỗi báo **trên thẻ**, không modal; chạm thẻ mới **huỷ** hành động cũ

**UX Enhancements** (`composition.carplay.defaults`)
- `flat-no-shadow` · `high-contrast` · `min-16pt-text` · `no-modal` · `single-tap-only` · `runtime-bounds-layout` · `crossfade-only`
- **Không** pull-to-refresh (đòi cử chỉ hai giai đoạn khi đang lái)
- **Không** skeleton loading — thẻ giữ dữ liệu cache và ghi thời điểm, tốt hơn shimmer trống
- Thẻ lỗi báo **tại chỗ trên thẻ**, các thẻ khác không bị ảnh hưởng

**Content Zones Map** — *mọi chiều cao là **tỉ lệ** theo bounds*

```
┌─────────────────────────────────────┐
│ ZONE A: Priority Card (hero)        │ ← ~45% bounds.height
│   Thẻ ngữ cảnh cao điểm nhất        │   static, chạm được
├─────────────────────────────────────┤
│ ZONE B: Remaining Cards             │ ← ~45% bounds.height
│   2–3 thẻ, grid tĩnh, 1 chạm        │   static-grid
├─────────────────────────────────────┤
│ ZONE C: — TRỐNG CÓ CHỦ Ý            │ ← 0 (cấm "xem thêm")
├─────────────────────────────────────┤
│ ZONE D: Edge Status Line            │ ← ~24pt-ratio, KHÔNG chắn
└─────────────────────────────────────┘
   safeAreaInset = 6% bounds (tỉ lệ, không phải pt)
```

**Layout** — *ví dụ ở bounds 1180×420, 18:10 thứ Sáu, Premium*

```
╔══════════════════════════════════════════════════════╗
║ bounds đọc từ CPTemplateApplicationScene tại runtime ║
║ inset = 6% × bounds · KHÔNG hằng số                  ║
║ ┌──────────────────────────────────────────────────┐ ║ ZONE A ~45%
║ │  VỀ NHÀ                                          │ ║ carplayCard
║ │  carplayTitle 22/600 textPrimary                 │ ║ r=16 p=16
║ │                                                  │ ║ shadow.0
║ │  Nguyễn Trãi đang thoáng · 18 phút               │ ║ border 1px
║ │  carplayBody 17/500 textSecondary                │ ║ borderStrong
║ │                                          [→]     │ ║ touch ≥44pt
║ └──────────────────────────────────────────────────┘ ║
║ ┌───────────────────────┐ ┌────────────────────────┐ ║ ZONE B ~45%
║ │ ĐANG PHÁT             │ │ THỜI TIẾT              │ ║ 2 thẻ, gap
║ │ Chiều Thứ Sáu         │ │ 31° · nhiều mây        │ ║ ${spacing.md}
║ │ carplayBody 17/500    │ │ cập nhật 18:05         │ ║ mono cho SỐ
║ │                  [▶]  │ │                        │ ║
║ └───────────────────────┘ └────────────────────────┘ ║
║  Carbina Premium                                     ║ ZONE D ~24pt
║  carplayMin 16pt textTertiary · KHÔNG chắn nội dung  ║ tỉ lệ
╚══════════════════════════════════════════════════════╝
   Hành vi nền tại màn này (không có UI):
   · sound Connect + ducking 20% → FR-016/017/018
   · giọng chào ≤2s sau connect  → FR-037/038/039
   · sound Disconnect lúc tắt máy → FR-019/020
```

**Layout Variants** *(bắt buộc: Medium density)*

**Variant A — Chưa đủ dữ liệu để cá nhân hóa (First Visit)**
```
╔══════════════════════════════════════════════════════╗
║ ┌──────────────────────────────────────────────────┐ ║ thứ tự MẶC ĐỊNH
║ │  ĐANG PHÁT                                       │ ║
║ │  Chưa có nhạc                            [▶]     │ ║
║ └──────────────────────────────────────────────────┘ ║
║ ┌───────────────────────┐ ┌────────────────────────┐ ║
║ │ THỜI TIẾT   31°       │ │ SHORTCUT               │ ║
║ └───────────────────────┘ └────────────────────────┘ ║
║  Dashboard sẽ tự đổi theo thói quen sau vài chuyến   ║ ZONE D
║  carplayMin 16pt textSecondary                       ║ NÓI RÕ chưa
╚══════════════════════════════════════════════════════╝ cá nhân hóa
   FR-040 P3: KHÔNG tuyên bố đã cá nhân hóa khi chưa
```

**Variant B — Mất mạng + một thẻ lỗi (Offline / Error)**
```
╔══════════════════════════════════════════════════════╗
║ ┌──────────────────────────────────────────────────┐ ║ thẻ dùng CACHE
║ │  VỀ NHÀ                                          │ ║ + ghi rõ thời
║ │  Địa điểm đã lưu · cập nhật 17:40        [→]     │ ║ điểm cập nhật
║ └──────────────────────────────────────────────────┘ ║ (AC-022.6)
║ ┌───────────────────────┐ ┌────────────────────────┐ ║
║ │ ĐANG PHÁT             │ │ THỜI TIẾT              │ ║
║ │ ⚠ Không tải được      │ │ 31° · cập nhật 18:05   │ ║ lỗi báo TRÊN
║ │   Phát từ máy    [▶]  │ │ (dữ liệu đã lưu)       │ ║ THẺ, không
║ └───────────────────────┘ └────────────────────────┘ ║ modal; thẻ
║  Carbina Premium                                     ║ khác KHÔNG
╚══════════════════════════════════════════════════════╝ bị ảnh hưởng
```

**Components**
- `CarPlayPriorityCard` (Zone A) — Tokens: `${component.carplayCard}`: `radius: 16`, `padding: 16`, `background: ${color.palette.surface}`, `border: 1px ${color.palette.borderStrong}`, **`shadow: ${shadow.elevation.0}`**, `minTouchTarget: 44`, `minFontSize: 16`. Chiều cao = **tỉ lệ** bounds, không phải pt.
- `CarPlayActionCard` ×2–3 (Zone B) — cùng token, kích thước nhỏ hơn theo tỉ lệ.
- `CarPlayCardError` — biến thể lỗi: `foreground: ${color.semantic.error.color}`, thông báo + hành động thay thế **trên thẻ**.
- `CarPlayEdgeStatus` (Zone D) — Tokens: `font: ${typography.scale.carplayMin}`(16), `color: ${color.palette.textTertiary}`, **không** background (để không chắn nội dung).
- **Không có** component nào cho modal, sheet, alert, text field trên bề mặt này — theo thiết kế.

**States** (9)

| State | Loại | Context | Layout/Behavior |
|---|---|---|---|
| **First Visit** | user-context | Chưa đủ dữ liệu học | **Variant A**: thứ tự mặc định + dòng "sẽ tự đổi sau vài chuyến" — **không** giả vờ đã cá nhân hóa |
| **Returning** | user-context | Đã học được thói quen | Thẻ hay dùng ở Zone A; thứ tự đổi theo giờ và tuyến đường |
| **Power User** | user-context | Premium, dùng hằng ngày | Đủ thẻ, ngữ cảnh chính xác nhất — đây là trạng thái đo tap-through ≥ 30% |
| **Free tier** | user-context | Entitlement = Free | Dashboard cơ bản (nhạc · thời tiết · 1 shortcut) + WF-018 một dòng tĩnh |
| **Error** | user-context | Một thẻ không lấy được dữ liệu | **Variant B**: thông báo gọn **trên thẻ** + hành động thay thế; **không modal**; thẻ khác không ảnh hưởng |
| **Default** | data | Mọi dữ liệu sẵn sàng | Layout như trên |
| **Loading** | data | ContextEngine đang tính thứ tự (≤ 1,0s) | **Giữ thứ tự hiện tại** cho tới khi có kết quả — không skeleton, không thẻ trống (ERR-040.3) |
| **Empty** | data | Không có thẻ nào khả dụng (mọi nguồn thất bại) | Hiện **một thẻ duy nhất** với dòng chữ giải thích; **không bao giờ** vùng trắng (NFR-020) |
| **Offline** | data | Mất mạng | Thẻ nhạc/thời tiết dùng cache + **ghi rõ thời điểm cập nhật cuối**; shortcut vẫn hoạt động |

**User Flow**
- **Entry**: `carplay_connected` → scene active · quay lại từ app hệ thống (nhạc / Maps / điện thoại)
- **Exit**: app hệ thống tương ứng · **WF-019** (nếu widget lỗi) · kết thúc phiên khi tắt máy. **Không có exit nào tới WF-010** (BR-045.3)
- **Task Flow**: bước 3–6 của **TF-002** · bước 2–7 của **TF-010** · bước 4–5 của **TF-011** · bước 5 của **TF-012**
- **Transitions**: **chỉ crossfade 0,4s** khi thẻ đổi thứ tự (SF-017); **cấm** chuyển động vị trí; throttle 1 lần/30s; hoãn khi thẻ đang được chạm

---

### 3.17 WF-017 — CarPlay Widget 🚗 · *Template C (Consumption)*

**Design System**: `bento-grid` → biến thể **`composition.carplay`**
**Archetype**: Consumption | **Density**: Light (1–2 vùng)
**Source UC**: UC-015 (chính), UC-005, UC-010, UC-036
**Source FR**: **FR-029** (render theo scene bounds runtime), **FR-030** (giảm cấp layout), **FR-061** (theme dùng chung với app)
**User Intent**: "Tôi muốn thấy widget của tôi, đúng như tôi đã cấu hình, không bị cắt."

**Action Layer → Visual Hierarchy**

| UC Action Layer | Slot | Ghi chú |
|---|---|---|
| Layer 1 — Primary: **không có hành động** — đây là bề mặt để **nhìn** | **#1** | Và đó là chủ ý; widget tương tác hai chiều thuộc MVP 2 |
| Layer 2/3/4 | — | **Trống có chủ ý** — cấu hình nằm ở WF-008 trên iPhone |

**Visual Hierarchy**
1. **Ảnh xe / ảnh cá nhân** — full-bleed, chiếm gần toàn bộ diện tích.
2. **Lớp thông tin** (tên xe · counter · thời tiết) — co theo Dynamic Type, truncate có ellipsis, **≥ 16pt**.
3. — (không có primary action)
4. — (widget không có chrome)

*Self-check*: media chiếm > 50% diện tích ⇒ đạt. Không có key info sticky vì không có scroll ⇒ đúng bản chất widget. Không có primary action ⇒ đã ghi lý do.

**Required Features (FR)**
- FR-029 P1: đọc bounds **tại runtime**; **không** tra bảng xe, **không** giá trị mặc định
- FR-029 P5–P6: chữ co theo Dynamic Type, truncate **có ellipsis**; touch target ≥ 44pt; đúng ở **cả** dark và light mode
- FR-029 P7: render OK → ghi `widget_render_ok` + **lưu kích thước** để WF-023 dùng làm tỉ lệ preview
- FR-029 **BR-029.3**: widget extension **không** nạp Core ML, **không** gọi mạng
- FR-030 P2–P5: giảm cấp theo thứ tự ưu tiên (bỏ phần tử → co chữ → truncate), **tối đa 3 vòng**, rồi chuyển WF-019
- FR-030 **BR-030.2**: chữ **không bao giờ** nhỏ hơn 16pt
- FR-061 BR-061.1: widget dùng **cùng theme** với app; hai bề mặt không được lệch
- `component.carplayWidget.scrimRequired`: áp scrim khi chữ nằm trên ảnh và tương phản < 4,5:1 (AC-NFR-014.4)

**UX Enhancements** (`composition.carplay.defaults` + `consumption`)
- `full-bleed-media` · `scrim-for-text-over-image` · `flat-no-shadow` · `min-16pt-text` · `runtime-bounds-layout`
- **Không** pinch-to-zoom, **không** swipe, **không** double-tap — mọi cử chỉ trên màn hình xe là rủi ro an toàn và không có FR nào backing
- **Không** page indicator (widget đơn, không carousel ở MVP 1)

**Content Zones Map** — *tỉ lệ theo bounds*

```
┌─────────────────────────────────────┐
│ ZONE A: Hero Media (full-bleed)     │ ← ~100% bounds trừ Zone B
│   Ảnh xe / ảnh cá nhân              │   static, không tương tác
│   + scrim nếu tương phản < 4,5:1    │
├─────────────────────────────────────┤
│ ZONE B: Key Info (không sticky)     │ ← ~20% bounds, overlay đáy
│   Tên xe · counter · thời tiết      │   ≥16pt, truncate ellipsis
├─────────────────────────────────────┤
│ ZONE C / ZONE D: — (unused)         │ ← widget không có chrome
└─────────────────────────────────────┘
   safeAreaInsetRatio = 0.06 × bounds (TỈ LỆ, không pt)
```

**Layout** — *ví dụ ở bounds 1180×420, light mode, 3 lớp thông tin*

```
╔══════════════════════════════════════════════════════╗
║ bounds runtime · inset 6% · shadow.0 · r=16          ║
║┌────────────────────────────────────────────────────┐║ ZONE A
║│                                                    │║ full-bleed
║│         [ ảnh Toyota Camry 2022 ]                  │║ ảnh đã crop
║│         .aspectRatio(fill)                         │║ theo tỉ lệ này
║│                                                    │║ ở WF-024
║│ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  │║ scrim
║│ overlayScrim rgba(0,0,0,0.35) — CHỈ khi cần        │║ điều kiện
║│  Toyota Camry                                      │║ ZONE B
║│  carplayTitle 22/600 · textInverse trên scrim      │║
║│  142 chuyến · 31°                                  │║ carplayBody
║│  mono cho SỐ · ≥16pt                               │║ 17/500
║└────────────────────────────────────────────────────┘║
╚══════════════════════════════════════════════════════╝
   ✓ ghi widget_render_ok(screen_width:1180, screen_height:420,
     widget_type:carPhoto) + LƯU kích thước cho WF-023
```

**Components**
- `CarPlayWidgetSurface` — Tokens: `${component.carplayWidget}`: `radius: 16`, `safeAreaInsetRatio: 0.06`, **`shadow: elevation.0`**, `scrimRequired: true`, `minFontSize: 16`. Mọi kích thước là **tỉ lệ bounds**.
- `WidgetImageLayer` — ảnh đã nén ≤ 2MB đọc từ App Group; `.aspectRatio(fill)`.
- `WidgetScrim` — Tokens: `${color.overlayScrim}` light `rgba(0,0,0,0.35)` / dark `rgba(0,0,0,0.45)`. **Chỉ áp khi** tương phản chữ/ảnh < 4,5:1.
- `WidgetInfoLayer` — Tokens: title `${typography.scale.carplayTitle}`(22/600), body `${typography.scale.carplayBody}`(17/500), số dùng `${typography.family.mono}`; truncate **có ellipsis**; **không** xuống dưới 16pt.
- **Không có** component tương tác nào (MVP 1).

**States** (8)

| State | Loại | Context | Layout/Behavior |
|---|---|---|---|
| **First Visit** | user-context | Lần cắm xe đầu tiên | Render bằng bounds vừa đọc; **lưu kích thước** cho WF-023 dùng về sau |
| **Returning** | user-context | Kích thước xe đã biết | Đường render ngắn hơn vì layout đã có tham số; kết quả giống hệt lần trước |
| **Power User** | user-context | Ảnh cá nhân, 3 lớp thông tin | Khi hết chỗ, **giảm cấp theo thứ tự ưu tiên** (FR-030) thay vì cắt bừa |
| **Error** | user-context | Vượt bounds sau 3 vòng giảm cấp, hoặc hết bộ nhớ | Chuyển **WF-019**; ghi `widget_render_failed` với `failure_reason` **phân biệt** `overflow` / `memory` |
| **Dark / Light** | user-context | Theo hệ thống xe hoặc theo `appTheme` (FR-061) | Cả hai mode đều hỗ trợ; tương phản chữ trên ảnh ≥ 4,5:1 ở **cả hai** — áp scrim nếu cần |
| **Default** | data | Cấu hình + ảnh đọc từ App Group xong | Layout như trên; ghi `widget_render_ok` |
| **Loading** | data | Đang đọc App Group container | Hiện **ảnh xe theo model** (asset bundle, luôn có sẵn) làm nền tạm; **không** vùng trắng, **không** skeleton |
| **Empty** | data | Chưa có cấu hình widget (chưa qua WF-008) | Hiện ảnh xe theo model + tên xe — cấu hình mặc định từ FR-005; **không bao giờ** vùng trắng |

**User Flow**
- **Entry**: `carplay_connected` → scene active, hệ thống yêu cầu vẽ widget
- **Exit**: **WF-016** (dashboard) · **WF-019** (render thất bại). **Không có exit nào do người dùng chủ động** — widget không tương tác ở MVP 1
- **Task Flow**: bước 1–2 của **TF-002** · bước 1 của **TF-003** · bước 1 của **TF-010** · bước 3 của **TF-011**
- **Transitions**: crossfade 0,4s khi cấu hình đổi (sau khi lưu ở WF-008); **không** chuyển động vị trí

---

### 3.18 WF-018 — CarPlay: Trạng Thái Free 🚗 · *Template C (Consumption)*

**Design System**: `bento-grid` → biến thể **`composition.carplay`**
**Archetype**: Consumption | **Density**: Light (2 vùng)
**Source UC**: UC-024 (chính), UC-021, UC-022, UC-023
**Source FR**: **FR-041** (dashboard theo entitlement), **FR-044** (cấu hình gói Free)
**User Intent**: "Tôi muốn dùng cái tôi đang có mà không bị quấy rầy trong lúc lái."

**Action Layer → Visual Hierarchy**

| UC Action Layer | Slot | Ghi chú |
|---|---|---|
| Layer 1 — Primary: **không có hành động bắt buộc** — người dùng tiếp tục dùng widget và dashboard Free | **#1** | Đây là **lớp thông tin**, không phải màn chuyển đổi |
| Layer 2 — Contextual: đọc dòng gợi ý nâng cấp — **chỉ đọc, không chạm được để mở paywall** | **#4** | Biểu đạt yếu nhất có thể |
| Layer 3/4 | — | **Trống có chủ ý** |

**Visual Hierarchy**
1. **Widget + dashboard Free đang hoạt động bình thường** — nội dung thật, không bị làm mờ.
2. — (không có)
3. — (không có)
4. **Một dòng chữ tĩnh** nói tính năng nào có ở Premium — ở mép, **không chắn nội dung**.

*Self-check*: nội dung Free chiếm ~96% diện tích, dòng gợi ý ~4% ⇒ tỉ lệ đúng với ý định "an toàn > conversion". Không có CTA ⇒ đúng BR-041.2.

**Required Features (FR)**
- FR-041 P3: **một dòng chữ tĩnh**, **không** popup, **không** chắn nội dung, **không có exit nào dẫn tới paywall từ màn hình xe**
- FR-041 **BR-041.1**: cấu hình Free là **cấu hình đã chốt** của PRD §11 (nhạc đang phát · thời tiết · 1 shortcut), không phải bản cắt bớt tuỳ ý
- FR-041 **BR-041.3**: không đọc được entitlement → mặc định Free và **vẫn cho dùng**
- FR-044 P1–P4: widget **đầy đủ chức năng** — không watermark, không làm mờ, không giới hạn thời gian, không quảng cáo
- FR-044 P6: ghi `free_tier_widget_used`
- FR-045 P4 / FR-044 ERR-044.1: **không** nhắc lại theo phiên; tần suất theo định mức, không theo mỗi chuyến

**UX Enhancements** (`composition.carplay.defaults`)
- `flat-no-shadow` · `high-contrast` · `min-16pt-text` · `no-modal` · `single-tap-only`
- **Không** có bất kỳ affordance nâng cấp nào chạm được — đây là quyết định có chủ ý, không phải thiếu sót
- Dòng gợi ý xuất hiện theo **tần suất định mức**, không mỗi chuyến (BR-045.4)

**Content Zones Map** — *tỉ lệ theo bounds*

```
┌─────────────────────────────────────┐
│ ZONE A: Hero — nội dung Free thật   │ ← ~96% bounds
│   widget + dashboard cơ bản         │   ĐẦY ĐỦ CHỨC NĂNG
├─────────────────────────────────────┤
│ ZONE B: một dòng chữ tĩnh           │ ← ~4% bounds, ở mép
│   "Giọng chào AI có ở Premium"      │   KHÔNG chạm được
├─────────────────────────────────────┤
│ ZONE C / ZONE D: — (unused)         │ ← 0
└─────────────────────────────────────┘
```

**Layout** — *ví dụ ở bounds 1180×420, gói Free*

```
╔══════════════════════════════════════════════════════╗
║ ┌──────────────────────────────────────────────────┐ ║ ZONE A ~96%
║ │  ĐANG PHÁT                                       │ ║ dashboard cơ
║ │  Chiều Thứ Sáu                           [▶]     │ ║ bản: 3 thẻ
║ │  carplayBody 17/500                              │ ║ (cấu hình Free
║ └──────────────────────────────────────────────────┘ ║  ĐÃ CHỐT)
║ ┌───────────────────────┐ ┌────────────────────────┐ ║
║ │ THỜI TIẾT             │ │ SHORTCUT               │ ║
║ │ 31° · nhiều mây       │ │ Về nhà           [→]   │ ║
║ └───────────────────────┘ └────────────────────────┘ ║
║  Giọng chào AI và widget không giới hạn có ở Premium ║ ZONE B ~4%
║  carplayMin 16pt · textTertiary · KHÔNG background  ║ CHỈ ĐỌC
║  ✗ không chạm được  ✗ không popup  ✗ không paywall  ║ (BR-041.2)
╚══════════════════════════════════════════════════════╝
   Widget ở WF-017 vẫn ĐẦY ĐỦ CHỨC NĂNG: không watermark,
   không làm mờ, không giới hạn thời gian (BR-044.2)
```

**Components**
- `CarPlayActionCard` ×3 — như WF-016; đúng cấu hình Free đã chốt.
- `CarPlayStaticUpsellLine` (Zone B) — Tokens: `font: ${typography.scale.carplayMin}`(16), `color: ${color.palette.textTertiary}`, **không** background, **không** border, **không** gesture recognizer. Đây là component **cố ý không tương tác**.
- **Không có** `BtnUpgrade`, không `PriceTierCard`, không sheet — theo thiết kế.

**States** (7)

| State | Loại | Context | Layout/Behavior |
|---|---|---|---|
| **First Visit** | user-context | Lần đầu lên xe với gói Free | Dòng gợi ý xuất hiện **một lần**, ngắn, ở mép — mục đích là **thông tin**, không phải chuyển đổi |
| **Returning** | user-context | Đã dùng Free nhiều chuyến | Dòng gợi ý **không** hiện lại mỗi chuyến; theo tần suất định mức |
| **Power User** | user-context | Dùng Free lâu dài có ý thức | Trải nghiệm gần như **không có dấu hiệu** của trạng thái Free — đây là chủ ý |
| **Error** | user-context | Không đọc được entitlement | Mặc định về Free và **vẫn cho dùng**; **không** chặn, **không** hiện lỗi trên màn hình xe (BR-041.3) |
| **Default** | data | Entitlement = Free, dữ liệu sẵn sàng | Layout như trên |
| **Loading** | data | ContextEngine đang tính | Giữ thứ tự hiện tại; dòng Zone B đã hiện (không phụ thuộc ContextEngine) |
| **Offline** | data | Mất mạng | Thẻ dùng cache + thời điểm cập nhật; dòng Zone B **không** phụ thuộc mạng |

**User Flow**
- **Entry**: scene active khi entitlement là `free`
- **Exit**: **WF-016** · kết thúc phiên. **Không có exit nào dẫn tới paywall từ màn hình xe** (BR-045.3) — người dùng muốn nâng cấp phải mở app iPhone, và đó là thiết kế
- **Task Flow**: nhánh Free của **TF-002** bước 4 · **TF-010** · bước 1 của **TF-007** (người dùng dùng Free nhiều chuyến trước khi tự chạm tính năng khoá trên iPhone)
- **Transitions**: crossfade 0,4s như WF-016; dòng Zone B fade-in 0,4s rồi giữ nguyên (không tự ẩn — tự ẩn tạo chuyển động không cần thiết)

---

### 3.19 WF-019 — CarPlay: Fallback Lỗi 🚗 · *Template C (Consumption)*

**Design System**: `bento-grid` → biến thể **`composition.carplay`**
**Archetype**: Consumption | **Density**: Light (1 vùng)
**Source UC**: UC-016 (chính), UC-015 | **Source FR**: **FR-031** (fallback khi render thất bại)
**User Intent**: "Có gì đó không ổn — tôi muốn biết đó là gì và nó có phải lỗi của tôi không."

**Action Layer → Visual Hierarchy**

| UC Action Layer | Slot | Ghi chú |
|---|---|---|
| Layer 1 — Primary: **không có hành động trên xe** — người dùng chỉ đọc | **#1** | Hành động diễn ra sau, trên iPhone (WF-014) |
| Layer 2/3/4 | — | **Trống có chủ ý** — người dùng đang lái (BR-031.3) |

**Visual Hierarchy**
1. **Một thông báo gọn** — nêu rõ **đây là vấn đề tương thích với màn hình xe này**, kèm hướng dẫn mở màn Chẩn Đoán trên iPhone. Đây là phần tử duy nhất.
2. — (không có)
3. — (**không có CTA nào** trên bề mặt đang lái)
4. — (không có)

*Self-check*: phần tử duy nhất ⇒ hiển nhiên nổi bật nhất. **Không** có CTA ⇒ đúng BR-031.3. **Không** vùng trắng ⇒ đúng NFR-020.

**Required Features (FR)**
- FR-031 P1: `FallbackNotice` nêu rõ **vấn đề tương thích màn hình xe này** + hướng dẫn mở màn Chẩn Đoán trên iPhone
- FR-031 P2 / **BR-031.3**: **chỉ để đọc** — không CTA, không modal, không nhập liệu
- FR-031 P3 / **BR-031.4**: chỉ widget lỗi → **chỉ** thay vùng widget; WF-016 hoạt động đầy đủ
- FR-031 **BR-031.1**: **0 trường hợp** vùng trắng, mọi nhánh lỗi
- FR-031 **BR-031.2**: **cấm** câu chung như "đã xảy ra lỗi" — câu đó khiến người dùng kết luận app rác
- FR-031 P5–P7: đánh dấu phiên cần chẩn đoán; lần mở app kế tiếp hiện `WarningRow` trên WF-006; lỗi lặp ≥ 3 lần → ưu tiên cao trong telemetry
- FR-031 VR-031.1: `FallbackNotice` **luôn có nội dung chữ khác rỗng**, ở mọi kích thước màn hình

**UX Enhancements** (`composition.carplay.defaults`)
- `flat-no-shadow` · `high-contrast` · `min-16pt-text` · `no-modal`
- **Không** có nút thử lại trên xe — thử lại là hành động cần chú ý, và người dùng đang lái. Hệ thống tự thử lại ở lần cắm kế tiếp.
- **Không** hiện mã lỗi kỹ thuật — mã lỗi thuộc WF-014 trên iPhone

**Content Zones Map** — *tỉ lệ theo bounds*

```
┌─────────────────────────────────────┐
│ ZONE A: Hero — thông báo bằng chữ   │ ← ~100% vùng widget lỗi
│   "Vấn đề tương thích màn hình xe"  │   CHỈ ĐỌC
├─────────────────────────────────────┤
│ ZONE B: — (KHÔNG có CTA)            │ ← 0 (BR-031.3)
│ ZONE C / ZONE D: — (unused)         │ ← 0
└─────────────────────────────────────┘
```

**Layout** — *ví dụ ở bounds 1180×420, chỉ widget lỗi*

```
╔══════════════════════════════════════════════════════╗
║ ┌──────────────────────────────────────────────────┐ ║ ZONE A
║ │                                                  │ ║ carplayCard
║ │  ⚠  Widget chưa hiện đúng trên màn hình xe này   │ ║ r=16 p=16
║ │     carplayTitle 22/600 · semantic.warning       │ ║ shadow.0
║ │                                                  │ ║ border 1px
║ │     Đây là vấn đề tương thích kích thước màn      │ ║ borderStrong
║ │     hình, không phải lỗi thiết bị của bạn.        │ ║
║ │     carplayBody 17/500 · textSecondary           │ ║ NÓI RÕ vấn đề
║ │                                                  │ ║ (BR-031.2)
║ │     Mở Carbina trên iPhone → Chẩn đoán           │ ║ hướng dẫn,
║ │     tương thích để gửi báo cáo.                   │ ║ KHÔNG phải nút
║ │                                                  │ ║
║ │  ✗ không CTA  ✗ không modal  ✗ không nhập liệu   │ ║ BR-031.3
║ └──────────────────────────────────────────────────┘ ║
╚══════════════════════════════════════════════════════╝
   ✓ ghi widget_render_failed(screen_width, screen_height,
     widget_type, failure_reason: overflow | memory)
   ✓ đánh dấu phiên cần chẩn đoán → WarningRow trên WF-006
```

**Layout Variants** — *Light density không bắt buộc, nhưng biến thể này là **ràng buộc chức năng** nên vẫn đặc tả*

**Variant A — Chỉ widget lỗi, dashboard vẫn hoạt động (BR-031.4)**
```
╔══════════════════════════════════════════════════════╗
║ ┌──────────────────────────────────────────────────┐ ║ vùng WIDGET
║ │ ⚠ Widget chưa hiện đúng trên màn hình xe này     │ ║ bị thay bằng
║ │   Mở Carbina trên iPhone → Chẩn đoán tương thích │ ║ FallbackNotice
║ └──────────────────────────────────────────────────┘ ║
║ ┌───────────────────────┐ ┌────────────────────────┐ ║ WF-016 vẫn
║ │ ĐANG PHÁT             │ │ THỜI TIẾT              │ ║ HOẠT ĐỘNG
║ │ Chiều Thứ Sáu    [▶]  │ │ 31° · nhiều mây        │ ║ ĐẦY ĐỦ
║ └───────────────────────┘ └────────────────────────┘ ║
║  Carbina Premium                                     ║ (BR-031.4)
╚══════════════════════════════════════════════════════╝
   Lỗi widget KHÔNG hạ toàn bộ bề mặt CarPlay
```

**Components**
- `CarPlayFallbackNotice` — Tokens: `${component.carplayCard}` với `foreground: ${color.semantic.warning.color}`, `background: ${color.semantic.warning.background}`, title `${typography.scale.carplayTitle}`(22/600), body `${typography.scale.carplayBody}`(17/500). **Không** gesture recognizer, **không** button. `VR-031.1`: nội dung chữ **luôn khác rỗng** ở mọi kích thước.
- `CarPlayActionCard` (Variant A) — thẻ dashboard vẫn hoạt động bình thường.
- **Không có** component tương tác nào.

**States** (7)

| State | Loại | Context | Layout/Behavior |
|---|---|---|---|
| **First Visit** | user-context | Lỗi ở lần cắm xe đầu tiên | Thông báo **phải nói rõ vấn đề tương thích màn hình** — đây là khoảnh khắc quyết định người dùng ở lại hay để 1★ |
| **Returning** | user-context | Lỗi lẻ một lần rồi hết | Lần cắm kế tiếp render bình thường; `WarningRow` trên WF-006 **tự xoá** (ERR-031.1) |
| **Power User** | user-context | Lỗi lặp ≥ 3 lần cùng kích thước | Telemetry đánh dấu **ưu tiên cao** để phát hiện xe không tương thích trong 24h; nội dung màn không đổi (người lái không cần biết) |
| **Error (bộ phận)** | user-context | Chỉ widget lỗi, dashboard vẫn được | **Variant A**: chỉ vùng widget bị thay; WF-016 hoạt động đầy đủ |
| **Default** | data | `failure_reason = overflow` | Layout như trên |
| **Loading** | data | Đang thử vòng giảm cấp (FR-030, tối đa 3 vòng) | **Chưa** hiện WF-019 — giữ widget trạng thái trước trong lúc thử; chỉ chuyển sau khi 3 vòng đều thất bại |
| **Empty** | data | `failure_reason = memory` (widget extension bị thu hồi) | Cùng thông báo cho người dùng, nhưng telemetry ghi `memory` — **phân biệt rõ** với `overflow` (BR-029.4) |

**User Flow**
- **Entry**: render thất bại trong **WF-017** (vượt bounds sau 3 vòng giảm cấp, hoặc hết bộ nhớ)
- **Exit**: **WF-016** (dashboard vẫn hoạt động nếu chỉ widget lỗi) · **WF-014** (khi người dùng mở app iPhone sau đó, qua `WarningRow` trên WF-006). **Không có exit nào do người dùng chủ động trên xe**
- **Task Flow**: bước 2 của **TF-003**; nhánh Recovery của **TF-002**
- **Transitions**: crossfade 0,4s từ widget sang notice; **không** chuyển động vị trí, **không** nhấp nháy

---

### 3.20 WF-020 — Sheet: Nghe Thử Âm Thanh 📱 · *Template C (Consumption)*

**Design System**: `bento-grid`
**Archetype**: Consumption | **Secondary**: Action | **Density**: Medium (4 vùng)
**Source UC**: UC-006 (chính), UC-007, UC-009, UC-010 | **Source FR**: **FR-012** (nghe thử trong sheet), **FR-015** (âm lượng inline), **FR-013** (gán)
**User Intent**: "Tôi muốn nghe kỹ preset này đúng như nó sẽ nghe trên xe, rồi quyết định."

**Action Layer → Visual Hierarchy**

| UC Action Layer | Slot | Ghi chú |
|---|---|---|
| Layer 1 — Primary: nghe ở mức âm lượng thật và chạm "Dùng sound này" | **#3** | CTA gán |
| Layer 2 — Contextual: phát lại · slider âm lượng phản hồi tức thì · chọn sự kiện áp dụng | **#2** | Điều khiển dưới waveform |
| Layer 3 — Discovery: chuyển preset trước/sau trong cùng nhóm **không đóng sheet** | **#4** | Mũi tên hai bên |
| Layer 4 — Personal | — | **Trống có chủ ý** — sheet này chỉ có một việc; thêm mục cá nhân hoá sẽ biến nó thành màn cấu hình thứ hai |

**Visual Hierarchy**
1. **Tên preset + waveform lớn** — Zone A, waveform 40pt chạy theo audio thật.
2. **Slider âm lượng + bộ chọn sự kiện** — Zone B, điều khiển có phản hồi tức thì.
3. **CTA "Dùng sound này"** — đáy sheet.
4. **Chrome**: drag indicator, mũi tên trước/sau, nút đóng.

*Self-check*: waveform (40pt) + tên preset chiếm ~35% chiều cao sheet ⇒ media chiếm phần lớn nửa trên, đúng bản chất Consumption. CTA nằm nửa dưới, chạm được bằng một ngón ⇒ đạt.

**Required Features (FR)**
- FR-012 P1: **tự phát một lần** ngay khi sheet mở — người dùng không phải tìm nút play
- FR-012 P3–P4: mũi tên trước/sau nạp preset kế tiếp **cùng nhóm** và tự phát, **giữ nguyên mức âm lượng**; hết nhóm → mũi tên **vô hiệu**, **không** cuộn vòng (SF-018)
- FR-012 ERR-012.1: đang phát nhạc → **ducking thật**
- FR-012 ERR-012.3: không phát được → nêu lý do + [Thử lại]; sheet **không** tự đóng
- FR-015 P2–P3: kéo slider → sound mẫu đổi ≤ 300ms; **không** đổi âm lượng nhạc; lưu ngay khi nhả tay
- FR-013 P1–P2: gán ngay tại khoảnh khắc nghe thấy; preset khoá → WF-010

**UX Enhancements** (`composition.consumption.defaults` + `action`)
- `no-modal`: sheet này **là** modal cuối — không mở modal thứ hai từ đây
- `sticky-key-info`: tên preset + waveform luôn ở trên, không cuộn
- Slider có phản hồi âm thanh tức thì (SF-004); nhãn giá trị hiện cạnh núm rồi mờ sau 1s
- Mũi tên **không cuộn vòng** — cuộn vòng làm người dùng mất phương hướng (SF-018 P4)

**Content Zones Map**

```
┌─────────────────────────────────────┐
│ ZONE A: Hero — tên + waveform       │ ← ~35% sheet, static
├─────────────────────────────────────┤
│ ZONE B: Key Info + CTA (sticky)     │ ← slider + segmented + CTA
├─────────────────────────────────────┤
│ ZONE C: Detailed Content            │ ← mũi tên trước/sau ~44pt
├─────────────────────────────────────┤
│ ZONE D: — (unused cho Consumption)  │ ← 0
└─────────────────────────────────────┘
```

**Layout** — *detent medium (~50% screen)*

```
┌──────────────────────────────────────────────┐
│              ▬▬▬▬                            │ dragIndicator
│                                              │ 36×5 r=full
│ ┌──────────────────────────────────────────┐ │ ZONE A
│ │  Tiếng Máy Ấm                    1,8s    │ │ h3 22/600
│ │  ▁▃▅▇▆▄▂▁▃▅▇▅▃▁▂▄▆▇▅▃▁▃▅▇▆▄▂▁            │ │ mono cho SỐ
│ │  waveform h=40 · bar 3px gap 2px          │ │ waveform THẬT
│ │  ♫ đang duck nhạc xuống 20%               │ │ caption
│ └──────────────────────────────────────────┘ │
├──────────────────────────────────────────────┤
│  Âm lượng                              70%   │ ZONE B
│  ━━━━━━━━━━━━●────────────                   │ slider t=4 thumb=28
│  Độc lập với âm lượng nhạc                   │ caption
│                                              │
│  Áp dụng cho                                 │
│ ┌──────────────────────────────────────────┐ │ segmented h=36
│ │ ▸Lên xe │ Xuống xe │ Tới nơi🔒           │ │ r=12
│ └──────────────────────────────────────────┘ │
│                                              │
│ ┌──────────────────────────────────────────┐ │
│ │          Dùng sound này                  │ │ h=50 bg accent
│ └──────────────────────────────────────────┘ │
├──────────────────────────────────────────────┤
│  [◀ Chuông Nhẹ]            [Xung Điện ▶]    │ ZONE C ~44pt
│  cùng nhóm CỔ ĐIỂN · không cuộn vòng         │ BtnTertiary
└──────────────────────────────────────────────┘
```

**Layout Variants** *(bắt buộc: Medium density)*

**Variant A — Preset đang dùng (nhãn CTA đổi)**
```
┌──────────────────────────────────────────────┐
│              ▬▬▬▬                            │
│ ┌ Khởi Động Cổ Điển  1,2s · ▁▃▅▇▆▄▂▁ ───────┐│
│  Âm lượng 70% · ━━━━━━━━━━━━●──────           │
│  Áp dụng cho: ▸Lên xe │ Xuống xe │ Tới nơi🔒 │
│ ┌──────────────────────────────────────────┐ │ nhãn ĐỔI, trạng
│ │        ✓ Đang dùng                       │ │ thái đã chọn
│ └──────────────────────────────────────────┘ │ bg surfaceVariant
│  [◀ —]                     [Tiếng Máy Ấm ▶] │ mũi tên trái VÔ
└──────────────────────────────────────────────┘ HIỆU (đầu nhóm)
```

**Variant B — Hết nhóm + không phát được (SF-018 P4 + ERR-012.3)**
```
┌──────────────────────────────────────────────┐
│              ▬▬▬▬                            │
│ ┌──────────────────────────────────────────┐ │
│ │  V8 Khởi Động                    2,4s    │ │
│ │  ⚠ Không phát được (đang có cuộc gọi)    │ │ KHÔNG waveform
│ │                          [Thử lại]       │ │ (VR-011.1)
│ └──────────────────────────────────────────┘ │
│  Âm lượng 70% · slider VẪN điều chỉnh được   │ ERR-015.3
│  Áp dụng cho: ▸Lên xe │ …                    │
│ ┌──────────────────────────────────────────┐ │
│ │          Dùng sound này                  │ │ VẪN gán được
│ └──────────────────────────────────────────┘ │
│  [◀ Turbo Spool]                    [— ▶]   │ mũi tên phải VÔ
│  sheet KHÔNG tự đóng (ERR-012.3)             │ HIỆU (cuối nhóm)
└──────────────────────────────────────────────┘
```

**Components**
- `SheetContainer` — Tokens: `${component.sheet}`: `radius: 20`, `dragIndicator: 36×5`, `overlayColor: rgba(0,0,0,0.4)`, `background: ${color.palette.surfaceElevated}`, `shadow: ${shadow.elevation.3}`, `detentMedium: 50%`.
- `CardNowPlayingLarge` + `WaveformLive` — như WF-004/WF-007, waveform lớn hơn.
- `RowSliderVolume` — như WF-012.
- `SegmentedControl3` — như WF-007; "Tới nơi" có `LockLabel` khi thiếu quyền Vị trí.
- `BtnPrimary` nhãn động ("Dùng sound này" / "✓ Đang dùng" / "Mở khoá").
- `BtnTertiary` ×2 (mũi tên trước/sau) — trạng thái vô hiệu: `foreground: ${color.palette.textTertiary}`.

**States** (8)

| State | Loại | Context | Layout/Behavior |
|---|---|---|---|
| **First Visit** | user-context | Mở sheet lần đầu | **Tự phát một lần** ngay khi sheet mở |
| **Returning** | user-context | Preset đang dùng | **Variant A**: nút chính "✓ Đang dùng"; mũi tên đầu/cuối nhóm vô hiệu |
| **Power User** | user-context | Đang phát nhạc từ app khác | **Ducking thật** để bản nghe thử phản ánh đúng trải nghiệm trên xe |
| **Free tier** | user-context | Preset khoá | Nghe **đầy đủ**, không cắt, không watermark; nút chính → "Mở khoá" → WF-010 |
| **Error** | user-context | Không phát được | **Variant B**: lý do + [Thử lại]; **không** waveform; sheet **không** tự đóng |
| **Default** | data | Player sẵn sàng | Layout như trên |
| **Loading** | data | Chuẩn bị player (≤ 300ms) | Waveform ở trạng thái tĩnh; **chưa** hiện thanh chạy cho tới khi audio thật bắt đầu |
| **Empty** | data | Hết nhóm ở cả hai đầu (nhóm chỉ có 1 preset) | Cả hai mũi tên vô hiệu; các phần khác hoạt động bình thường |

**User Flow**
- **Entry**: chạm một preset trên **WF-007** · "nghe kỹ" từ **WF-004**
- **Exit**: **WF-007** (đã gán hoặc đóng) · **WF-010** (preset khoá) · **WF-030** (toast xác nhận sau khi gán)
- **Task Flow**: bước 2a của **TF-005**
- **Transitions**: sheet trượt lên 0,35s; tên preset crossfade 0,2s khi đổi; waveform reset về đầu ngay khi audio mới bắt đầu (SF-018)

---

### 3.21 WF-021 — Sheet: Không tìm thấy xe của tôi 📱 · *Template B (Action)*

**Design System**: `bento-grid`
**Archetype**: Action | **Density**: Light (3 vùng)
**Source UC**: UC-003 (chính), UC-002 | **Source FR**: **FR-006** (gửi yêu cầu thêm xe)
**User Intent**: "Xe tôi không có trong danh sách — tôi muốn nói ra và vẫn đi tiếp được."

**Action Layer → Visual Hierarchy**

| UC Action Layer | Slot | Ghi chú |
|---|---|---|
| Layer 1 — Primary: điền hãng/model/năm và chạm "Gửi" | **#3** | CTA "Gửi" |
| Layer 2 — Contextual: sửa ba ô (điền sẵn phần đã gõ ở WF-003) · đóng sheet | **#2** | Ba `TextField` |
| Layer 3 — Discovery: chọn phân khúc xe để vẫn có ảnh dùng được | **#4** | Chip phân khúc |
| Layer 4 — Personal | — | **Trống có chủ ý** — **không** thu thập gì thêm về người dùng ở đây, đúng cam kết không PII (BR-006.3) |

**Visual Hierarchy**
1. **Một câu trung thực** — "thư viện chưa có xe này, và điều đó không chặn bạn". `${typography.scale.h3}`.
2. **Ba ô nhập** — vùng tương tác chính, mỗi ô 50pt.
3. **CTA "Gửi"**.
4. **Chrome**: drag indicator, chip phân khúc, nút đóng.

*Self-check*: CTA 50pt ⇒ đạt. Ô nhập 50pt > 44pt ⇒ đạt. CTA vô hiệu khi hãng/model rỗng ⇒ đúng VR-006.1.

**Required Features (FR)**
- FR-006 P1: điền sẵn phần chuỗi đã gõ ở WF-003
- FR-006 P3: chạm "Gửi" → xác nhận **ngay ≤ 500ms**, **không chờ phản hồi mạng**
- FR-006 P4: request trùng → **gộp**, không gửi lại
- FR-006 **BR-006.1**: thiếu xe **không bao giờ** chặn onboarding
- FR-006 **BR-006.3**: **không** thu thêm bất kỳ trường nào ngoài ba giá trị người dùng tự gõ
- FR-006 VR-006.1–3: `make`/`model` không rỗng, chấp nhận **tên tự do** không validate theo danh sách; `year` trong 1980 → năm hiện tại + 2; > 40 ký tự thì cắt
- FR-006 ERR-006.1/2: offline → xếp hàng on-device, toast vẫn xác nhận; đóng sheet → **không mất** phần đã gõ

**UX Enhancements** (`composition.action.defaults`)
- `inline-validation`: CTA bật khi hãng+model không rỗng; `year` sai dải → viền `${color.semantic.error.color}` + dòng lý do dưới ô
- `keyboard-handling`: Return chuyển ô kế tiếp; `year` dùng bàn phím số
- `escape-route-always-visible`: nút đóng + chip phân khúc (đi tiếp mà không cần gửi)
- `single-primary-cta`: một CTA

**Content Zones Map**

```
┌─────────────────────────────────────┐
│ ZONE D: Navigation                  │ ← dragIndicator + [✕]
├─────────────────────────────────────┤
│ ZONE A: Context — câu trung thực    │ ← ~72pt
├─────────────────────────────────────┤
│ ZONE B: 3 ô nhập + CTA              │ ← 3×50pt + CTA 50pt
├─────────────────────────────────────┤
│ ZONE C: — (unused cho Action)       │ ← 0; chip phân khúc ở Zone B
└─────────────────────────────────────┘
```

**Layout**

```
┌──────────────────────────────────────────────┐
│              ▬▬▬▬                     [✕]    │ ZONE D
├──────────────────────────────────────────────┤
│  Thư viện chưa có xe này.                    │ ZONE A ~72pt
│  h3 22/600 textPrimary                       │
│  Bạn vẫn thiết lập được ngay — chọn phân      │ body textSecondary
│  khúc bên dưới. Chúng tôi sẽ thêm xe của bạn. │
├──────────────────────────────────────────────┤
│  Hãng                                        │ ZONE B
│ ┌──────────────────────────────────────────┐ │ textField h=50
│ │ VinFast                                  │ │ r=12 điền sẵn từ
│ └──────────────────────────────────────────┘ │ WF-003
│  Model                                       │
│ ┌──────────────────────────────────────────┐ │
│ │ VF8                                      │ │ tên TỰ DO,
│ └──────────────────────────────────────────┘ │ không validate
│  Năm                                         │ theo danh sách
│ ┌──────────────────────────────────────────┐ │
│ │ 2024                                     │ │ bàn phím số
│ └──────────────────────────────────────────┘ │ mono
│                                              │
│  Phân khúc (để có ảnh dùng ngay)             │
│  [Sedan] [▸SUV] [Pickup] [Hatchback] […]     │ chip h=32 r=full
│                                              │ selected: accent
│ ┌──────────────────────────────────────────┐ │
│ │                Gửi                       │ │ h=50 bg accent
│ └──────────────────────────────────────────┘ │
│  Chỉ gửi ba giá trị bạn vừa gõ. Không gì khác.│ footnote
└──────────────────────────────────────────────┘   BR-006.3
```

**Components**
- `SheetContainer` — Tokens: `radius: 20`, `detentMedium: 50%`; như WF-020.
- `TFField` ×3 — Tokens: `${component.textField}`: `height: 50`, `radius: 12`, `borderColor: ${color.palette.inputBorder}`, `focusColor: ${color.palette.focusRing}`, `errorColor: ${color.semantic.error.color}`. Ô `year` dùng mono + bàn phím số.
- `ChipSegment` ×6 — Tokens: `${component.chip}`: `height: 32`, `radius: full`, `paddingH: 12`, selected `background: ${color.palette.accent}` `foreground: ${color.palette.onAccent}`.
- `BtnPrimary` ("Gửi") — vô hiệu khi hãng/model rỗng.
- `LabelFootnote` — cam kết không PII.

**States** (7)

| State | Loại | Context | Layout/Behavior |
|---|---|---|---|
| **First Visit** | user-context | Trong onboarding | Sheet ngắn, ba ô, **không** bắt buộc mô tả thêm — không làm onboarding dài ra |
| **Returning** | user-context | Đã gửi request cho cùng hãng trước đó | Nêu rõ **"đã gửi rồi"** và không gửi trùng (ERR-006.3) |
| **Power User** | user-context | Xe nội địa hoặc xe rất mới | Chấp nhận **tên tự do**; không validate cứng theo danh sách có sẵn |
| **Error** | user-context | `year` ngoài dải 1980 → +2 năm | Viền ô đỏ + dòng lý do dưới ô; CTA vô hiệu tới khi sửa |
| **Default** | data | Ba ô hợp lệ | CTA bật |
| **Loading** | data | Đang ghi vào hàng chờ on-device | CTA hiện spinner ≤ 500ms rồi đóng sheet — **không** chờ mạng |
| **Offline** | data | Không có mạng | Request **xếp hàng on-device**; **WF-030** toast vẫn xác nhận đã ghi nhận (ERR-006.1) |

**User Flow**
- **Entry**: nút "Không tìm thấy xe của tôi" ở **cả ba tầng** của **WF-003**
- **Exit**: **WF-003** (tiếp tục luồng chọn xe) · **WF-030** (toast xác nhận)
- **Task Flow**: bước 3a của **TF-001**
- **Transitions**: sheet trượt lên 0,35s; đóng sheet trượt xuống 0,3s; toast xuất hiện sau khi sheet đã đóng

---

### 3.22 WF-022 — Sheet: Lý Do Xin Quyền 📱 · *Template C (Consumption)*

**Design System**: `bento-grid`
**Archetype**: Consumption | **Secondary**: Action | **Density**: Light (3 vùng)
**Source UC**: UC-004 (chính), UC-019 | **Source FR**: **FR-007** (trình bày lý do quyền), **FR-035** (chặn nguồn thiếu quyền)
**User Intent**: "Tôi muốn hiểu app dùng quyền này để làm chính xác điều gì."

**Action Layer → Visual Hierarchy**

| UC Action Layer | Slot | Ghi chú |
|---|---|---|
| Layer 1 — Primary: đọc lý do rồi chạm "Cho phép" hoặc "Không, cảm ơn" | **#3** | Hai nút **ngang hàng** (BR-007.4) |
| Layer 2 — Contextual: đóng sheet mà **không** quyết định | **#4** | Vuốt xuống hoặc [✕] |
| Layer 3 — Discovery: xem hai ví dụ — có quyền được gì / không có mất gì | **#2** | Nội dung chính của sheet |
| Layer 4 — Personal: xem chính sách quyền riêng tư | #4 | Link ở đáy |

**Visual Hierarchy**
1. **Một câu nói app dùng quyền này để làm gì + cam kết dữ liệu không rời thiết bị** — `${typography.scale.h3}`.
2. **Hai ví dụ đối chiếu** — "có quyền" (`${color.semantic.success.background}`) vs "không có quyền" (`${color.semantic.warning.background}`). Đây là nội dung thuyết phục thật.
3. **Hai nút ngang hàng** — "Cho phép" và "Không, cảm ơn", cùng chiều cao 50pt.
4. **Chrome**: drag indicator, link chính sách.

*Self-check*: nội dung ví dụ chiếm ~45% chiều cao sheet ⇒ đúng bản chất Consumption (đọc là hành vi chính). Nút từ chối **không** bị làm mờ ⇒ đúng BR-007.4.

**Required Features (FR)**
- FR-007 P3: hai ví dụ (có quyền được gì / không có mất gì) + link chính sách
- FR-007 **BR-007.1**: lý do **cụ thể**, cấm câu chung
- FR-007 **BR-007.4**: nút từ chối **ngang hàng thị giác** với nút cho phép
- FR-007 P4: quyền `notDetermined` → gọi dialog iOS; quyền `denied` → nút đổi thành **"Mở Cài đặt"**
- FR-007 ERR-007.4: dialog iOS không mở được → nêu rõ + dẫn Cài đặt hệ thống
- FR-035 P3: vào từ WF-009 khi bật nguồn thiếu quyền
- Đóng sheet **không bao giờ** ngầm cấp hay ngầm từ chối quyền (SF-013 Recovery)

**UX Enhancements** (`composition.consumption.defaults`)
- `no-modal`: đây là modal cuối — không mở modal thứ hai
- `scrim-for-text-over-image`: **không áp dụng** (không có ảnh)
- Sheet trượt lên 0,35s; nội dung phía sau **mờ nhẹ nhưng vẫn thấy** để giữ ngữ cảnh (SF-013)
- Hai biến thể nội dung: Location và Calendar — cùng layout, khác chữ và khác ví dụ

**Content Zones Map**

```
┌─────────────────────────────────────┐
│ ZONE A: Hero — lý do + cam kết      │ ← ~100pt
├─────────────────────────────────────┤
│ ZONE B: Key Info + CTA (sticky)     │ ← 2 nút ngang hàng 50pt
├─────────────────────────────────────┤
│ ZONE C: Detailed Content            │ ← 2 ví dụ đối chiếu ~160pt
├─────────────────────────────────────┤
│ ZONE D: — (unused)                  │ ← 0; link chính sách ở Zone C
└─────────────────────────────────────┘
```

**Layout** — *biến thể Location*

```
┌──────────────────────────────────────────────┐
│              ▬▬▬▬                            │ dragIndicator
├──────────────────────────────────────────────┤
│  📍 Vì sao Carbina cần quyền Vị trí          │ ZONE A ~100pt
│  h3 22/600                                   │
│  Để nhận ra tuyến đường bạn hay đi. Dữ liệu   │ body textSecondary
│  này ở lại trên iPhone của bạn.               │
├──────────────────────────────────────────────┤
│ ┌──────────────────────────────────────────┐ │ ZONE C ~160pt
│ │ ✓ Khi bạn cho phép                       │ │ success.background
│ │   · Thẻ "Về nhà?" hiện sẵn lúc 18h        │ │ success.color
│ │   · Âm thanh "Tới nơi" hoạt động          │ │ body
│ │   · Câu chào biết bạn đang đi đâu          │ │
│ └──────────────────────────────────────────┘ │
│ ┌──────────────────────────────────────────┐ │
│ │ — Khi bạn không cho phép                 │ │ warning.background
│ │   · Widget, sound lên/xuống xe và         │ │ warning.color
│ │     dashboard vẫn hoạt động ĐẦY ĐỦ        │ │ NÊU RÕ cái gì
│ │   · Chỉ mất thẻ gợi ý điểm đến và          │ │ VẪN hoạt động
│ │     âm thanh "Tới nơi"                    │ │
│ └──────────────────────────────────────────┘ │
├──────────────────────────────────────────────┤
│ ┌────────────────────┐ ┌───────────────────┐ │ ZONE B
│ │   Không, cảm ơn    │ │    Cho phép       │ │ CẢ HAI h=50
│ └────────────────────┘ └───────────────────┘ │ NGANG HÀNG
│  BtnSecondary          BtnPrimary            │ (BR-007.4)
│  Chính sách quyền riêng tư                   │ footnote
└──────────────────────────────────────────────┘
```

**Components**
- `SheetContainer` — như WF-020, `detentMedium: 50%`.
- `CardExampleContrast` ×2 — Tokens: `radius: 16`, `padding: 16`; biến thể tích cực `background: ${color.semantic.success.background}` `foreground: ${color.semantic.success.color}`; biến thể trung tính `background: ${color.semantic.warning.background}` `foreground: ${color.semantic.warning.color}`.
- `BtnPrimary` ("Cho phép" / "Mở Cài đặt"), `BtnSecondary` ("Không, cảm ơn") — **cùng `height: 50`, cùng `radius: 16`, chia đôi chiều ngang**.
- `LinkFootnote` (chính sách quyền riêng tư).

**States** (7)

| State | Loại | Context | Layout/Behavior |
|---|---|---|---|
| **First Visit (Location)** | user-context | Chưa hỏi quyền Vị trí | Ví dụ về học tuyến đường và gợi ý điểm đến |
| **First Visit (Calendar)** | user-context | Chưa hỏi quyền Lịch | Ví dụ về câu chào nhắc cuộc họp sắp tới |
| **Returning** | user-context | Quyền đã bị từ chối trước đó | Nút "Cho phép" đổi thành **"Mở Cài đặt"** — iOS không cho hỏi lại lần hai |
| **Error** | user-context | Dialog quyền iOS không mở được (ERR-007.4) | Nêu rõ + dẫn Cài đặt hệ thống; **không** để nút bấm không phản hồi |
| **Default** | data | Nội dung nạp xong | Layout như trên |
| **Loading** | data | Đang chờ người dùng trả lời dialog iOS | Nút "Cho phép" hiện trạng thái chờ; nội dung ví dụ vẫn đọc được |
| **Empty** | data | Không áp dụng — nội dung là chuỗi tĩnh trong bundle | **Không tồn tại có chủ ý** |

**User Flow**
- **Entry**: "Tìm hiểu thêm" trên **WF-005** · dòng "cần quyền" / nút "Cấp quyền" trên **WF-009** · nút "Cấp quyền Vị trí" trên **WF-007** (Variant A)
- **Exit**: **WF-005** hoặc **WF-009** hoặc **WF-007** (trở về đúng nơi vào) · dialog quyền iOS · Cài đặt hệ thống iOS
- **Task Flow**: bước 6a của **TF-001** · bước 4a của **TF-006** · bước 6a của **TF-011**
- **Transitions**: sheet trượt lên 0,35s; nội dung phía sau mờ nhẹ; đóng sheet **không** đổi trạng thái quyền (SF-013)

---

### 3.23 WF-023 — Modal: Preview Widget Theo Màn Hình Xe 📱 · *Template C (Consumption)*

**Design System**: `bento-grid`
**Archetype**: Consumption | **Secondary**: Action | **Density**: Medium (4 vùng)
**Source UC**: UC-013 (chính), UC-012, UC-014 | **Source FR**: **FR-025** (preview theo tỉ lệ), **FR-026** (phát hiện vượt vùng an toàn)
**User Intent**: "Tôi muốn thấy widget của tôi trên đúng màn hình xe của tôi trước khi ra xe."

**Action Layer → Visual Hierarchy**

| UC Action Layer | Slot | Ghi chú |
|---|---|---|
| Layer 1 — Primary: xem widget ở từng tỉ lệ và chạm "Dùng bản này" | **#3** | CTA xác nhận |
| Layer 2 — Contextual: vuốt ngang qua các tỉ lệ · bật/tắt lớp thông tin | **#2** | Khung preview + toggle lớp |
| Layer 3 — Discovery: xem cảnh báo phần tử vượt vùng an toàn · chuyển dark/light | **#4** | Dải chọn tỉ lệ + công tắc mode |
| Layer 4 — Personal: đổi loại widget hoặc đổi ảnh **ngay tại đây** → WF-024 | **#4** | Sửa tại nơi phát hiện vấn đề (AF-013.2) |

**Visual Hierarchy**
1. **Khung preview widget ở tỉ lệ thật** — Zone A, chiếm ~50% chiều cao modal. Media là lý do modal này tồn tại.
2. **Nhãn "kích thước thật của xe bạn" / "ước lượng"** — Zone B sticky. Người dùng **phải** biết con số này thật hay đoán.
3. **CTA "Dùng bản này"** — Zone B.
4. **Chrome**: dải chọn tỉ lệ, công tắc dark/light, cảnh báo vượt vùng, nút đổi ảnh, nút đóng.

*Self-check*: preview chiếm ~50% chiều cao ⇒ đạt ngưỡng Consumption. Nhãn thật/ước lượng luôn thấy (sticky) ⇒ đạt. CTA nằm nửa dưới ⇒ chạm được bằng một ngón.

**Required Features (FR)**
- FR-025 P2–P3: có kích thước đã ghi nhận → dùng làm tỉ lệ mặc định, nhãn **"kích thước thật của xe bạn"**; chưa có → **≥ 4 tỉ lệ tham chiếu**, nhãn **"ước lượng"**
- FR-025 P4: vuốt ngang chuyển tỉ lệ (SF-009); công tắc dark/light **giữ nguyên** tỉ lệ đang xem
- FR-025 P5: đổi loại widget hoặc ảnh **ngay trong modal** — không quay về WF-008
- FR-025 **BR-025.2**: layout tính từ tỉ lệ đang chọn **tại runtime**, dùng **cùng engine** với FR-029 — engine khác thì preview nói dối
- FR-025 VR-025.1: bộ tỉ lệ tham chiếu ≥ 4 và **phải bao gồm nhóm màn 8"**
- FR-026 P3–P6: viền cảnh báo (fade 0,2s, **không nhấp nháy**) + **tên phần tử** + gợi ý "Giảm bớt phần tử này"; chữ truncate **có ellipsis**; sau cùng nêu rõ sẽ dùng bản giảm cấp
- FR-026 VR-026.2: phép kiểm chạy ở **cả** Dynamic Type mặc định và mức lớn nhất

**UX Enhancements** (`composition.consumption.defaults`)
- `full-bleed-media`: khung preview chiếm gần hết chiều ngang
- `sticky-key-info`: nhãn thật/ước lượng + CTA luôn thấy
- `no-modal`: **sai lệch có chủ ý** — WF-023 mở được WF-024. Justification: đổi ảnh là hành động **sửa tại nơi phát hiện vấn đề** (AF-013.2); buộc người dùng đóng modal rồi quay về WF-008 sẽ làm mất ngữ cảnh tỉ lệ đang kiểm
- Khung preview đổi kích thước bằng spring 0,3s **damping cao, không nảy** — người dùng cần thấy **sự khác biệt kích thước**, nên chuyển động phải làm nổi bật đúng chiều đó (SF-009)

**Content Zones Map**

```
┌─────────────────────────────────────┐
│ ZONE A: Hero Media — khung preview  │ ← ~50% modal
├─────────────────────────────────────┤
│ ZONE B: Key Info + CTA (sticky)     │ ← nhãn thật/ước lượng + CTA
├─────────────────────────────────────┤
│ ZONE C: Detailed Content            │ ← dải tỉ lệ + cảnh báo + đổi ảnh
├─────────────────────────────────────┤
│ ZONE D: — (unused)                  │ ← 0; [✕] ở góc Zone A
└─────────────────────────────────────┘
```

**Layout** — *đã cắm xe, tỉ lệ thật 1180×420*

```
┌──────────────────────────────────────────────┐
│  [✕]                          Sáng│▸Tối      │ ZONE A overlay
│ ┌──────────────────────────────────────────┐ │
│ │╔════════════════════════════════════════╗│ │ khung theo TỈ LỆ
│ ││  [ ảnh Camry + Toyota Camry + 142 ]    ││ │ THẬT 1180×420
│ ││  render bằng CÙNG engine với FR-029    ││ │ spring 0,3s
│ │╚════════════════════════════════════════╝│ │ damping cao
│ └──────────────────────────────────────────┘ │
├──────────────────────────────────────────────┤
│  ● 1180 × 420 — kích thước thật của xe bạn   │ ZONE B sticky
│  caption success · mono cho SỐ               │ NHÃN BẮT BUỘC
│ ┌──────────────────────────────────────────┐ │
│ │           Dùng bản này                   │ │ h=50 bg accent
│ └──────────────────────────────────────────┘ │
├──────────────────────────────────────────────┤
│  ◀  ● ○ ○ ○ ○  ▶   vuốt để đổi tỉ lệ        │ ZONE C
│  1180×420 · 800×480 · 1024×768 · 720×300 …   │ ≥4 tỉ lệ, GỒM
│                                              │ nhóm màn 8"
│  LỚP THÔNG TIN                               │
│  [✓ Tên xe] [✓ Số chuyến] [ Thời tiết]       │ chip toggle
│                                              │
│  Đổi ảnh                              [>]    │ → WF-024
└──────────────────────────────────────────────┘
```

**Layout Variants** *(bắt buộc: Medium density)*

**Variant A — Chưa từng cắm xe (dùng tỉ lệ ước lượng)**
```
┌──────────────────────────────────────────────┐
│  [✕]                          ▸Sáng│Tối      │
│ ┌ ╔══════════════════════════╗ ────────────┐ │ khung nhỏ hơn
│ │ ║ [ ảnh Camry + 142 ]      ║             │ │ (800×480)
│ │ ╚══════════════════════════╝             │ │
├──────────────────────────────────────────────┤
│  ○ 800 × 480 — ƯỚC LƯỢNG                     │ NHÃN KHÁC
│  caption textSecondary · chưa cắm xe lần nào  │ NÓI RÕ là đoán
│ ┌──────────────────────────────────────────┐ │ (AC-013.2)
│ │           Dùng bản này                   │ │
│ └──────────────────────────────────────────┘ │
│  ◀  ○ ● ○ ○ ○  ▶   4 tỉ lệ tham chiếu       │
└──────────────────────────────────────────────┘
```

**Variant B — Có phần tử vượt vùng an toàn (SF-008)**
```
┌──────────────────────────────────────────────┐
│  [✕]                          Sáng│▸Tối      │
│ ┌──────────────────────────────────────────┐ │
│ │╔════════════════════════════════════════╗│ │ tỉ lệ 720×300
│ ││  [ ảnh Camry ]                         ││ │ (màn 8")
│ ││  Toyota Camry                          ││ │
│ ││ ┌╌╌╌╌╌╌╌╌╌╌┐ ← viền cảnh báo fade 0,2s ││ │ KHÔNG nhấp nháy
│ ││ ╎142 chuyến╎    warning.color          ││ │
│ ││ └╌╌╌╌╌╌╌╌╌╌┘                           ││ │
│ │╚════════════════════════════════════════╝│ │
│ └──────────────────────────────────────────┘ │
├──────────────────────────────────────────────┤
│ ⚠ "Số chuyến đi" vượt vùng an toàn ở tỉ lệ    │ NÊU TÊN phần tử
│   này. Trên xe, nó sẽ bị bỏ tự động.          │ (AC-013.3)
│        [Giảm bớt phần tử này]                 │ BtnSecondary
│ ┌──────────────────────────────────────────┐ │ KHÔNG tự cắt
│ │           Dùng bản này                   │ │ âm thầm
│ └──────────────────────────────────────────┘ │
│  ◀  ○ ○ ○ ● ○  ▶                            │
└──────────────────────────────────────────────┘
```

**Components**
- `ModalFullContainer` — Tokens: `radius: ${border.radius.xl}`(20), `background: ${color.palette.surfaceElevated}`, `shadow: ${shadow.elevation.3}`, `overlayColor: rgba(0,0,0,0.4)`, `detentLarge: 90%`.
- `WidgetPreviewFrame` — khung theo **tỉ lệ đang chọn**; render bằng **cùng engine** với `FR-029`; đổi kích thước `${animation.spring.stiff}`(0,3s damping 0,9).
- `RatioSourceLabel` — Tokens: `font: ${typography.scale.caption}`; biến thể thật `${color.semantic.success.color}` + `●`; biến thể ước lượng `${color.palette.textSecondary}` + `○`. **Component bắt buộc** — không có nó thì preview có thể bị hiểu là chính xác khi chưa chắc.
- `RatioPager` — Tokens: dot 8pt, active `${color.palette.accent}`; ≥ 4 tỉ lệ.
- `SegmentedControl2` (Sáng/Tối) — Tokens: `height: 36`, `radius: 12`.
- `ChipToggleLayer` ×3 — Tokens: `${component.chip}`, selected `${color.palette.accent}`.
- `OverflowWarningBanner` (Variant B) — Tokens: `background: ${color.semantic.warning.background}`, `foreground: ${color.semantic.warning.color}`, viền phần tử vượt: `borderWidth: 2` dashed, fade 0,2s **không nhấp nháy**.
- `BtnPrimary` ("Dùng bản này"), `BtnSecondary` ("Giảm bớt phần tử này"), `RowNavigable` ("Đổi ảnh") → WF-024.

**States** (8)

| State | Loại | Context | Layout/Behavior |
|---|---|---|---|
| **First Visit** | user-context | Chưa từng cắm xe | **Variant A**: ≥ 4 tỉ lệ tham chiếu, nhãn **"ước lượng"** — không tuyên bố chính xác khi chưa có dữ liệu |
| **Returning** | user-context | Đã cắm xe ≥ 1 lần | Tỉ lệ mặc định là **kích thước thật**; nhãn nói rõ đây là số thật |
| **Power User** | user-context | Có 2 xe khác kích thước | Cho chọn giữa các kích thước **đã từng gặp**; kiểm được cả hai trước khi lưu |
| **Error** | user-context | Có phần tử vượt vùng an toàn | **Variant B**: nêu **tên phần tử** + [Giảm bớt phần tử này]; **không** tự cắt âm thầm |
| **Default** | data | Cấu hình + ảnh sẵn sàng | Layout như trên |
| **Loading** | data | Đang tính layout cho tỉ lệ mới | Khung giữ kích thước cũ trong lúc tính (≤ 100ms); **không** hiện khung trống |
| **Empty** | data | Chưa có ảnh cho widget | Dùng ảnh xe theo model (FR-005); **không** để khung trống |
| **Dark / Light** | data | Công tắc mode | Đổi mode **giữ nguyên tỉ lệ** đang xem; tương phản chữ/ảnh kiểm lại ở mode mới |

**User Flow**
- **Entry**: nút "Xem trước trên xe của tôi" trên **WF-008** · "Xem widget ở kích thước này" trong dòng mở rộng của **WF-014**
- **Exit**: **WF-008** ("Dùng bản này" hoặc đóng) · **WF-024** ("Đổi ảnh")
- **Task Flow**: bước 5–7 của **TF-004** · bước 4a của **TF-003**
- **Transitions**: modal trượt lên 0,35s; khung đổi kích thước spring 0,3s damping cao (SF-009); viền cảnh báo fade 0,2s

---

### 3.24 WF-024 — Sheet: Chọn Ảnh Cho Widget 📱 · *Template B (Action)*

**Design System**: `bento-grid`
**Archetype**: Action | **Secondary**: Discovery | **Density**: Medium (4 vùng)
**Source UC**: UC-014 | **Source FR**: **FR-027** (chọn ảnh + crop), **FR-028** (độ phân giải + nén)
**User Intent**: "Tôi muốn đặt ảnh xe của tôi lên widget và biết trước phần nào sẽ bị cắt."

**Action Layer → Visual Hierarchy**

| UC Action Layer | Slot | Ghi chú |
|---|---|---|
| Layer 1 — Primary: chọn ảnh, điều chỉnh khung crop, chạm "Xong" | **#3** | CTA "Xong" |
| Layer 2 — Contextual: kéo/zoom khung crop · đổi nguồn ảnh · xoay ảnh | **#2** | Vùng crop |
| Layer 3 — Discovery: duyệt bộ ảnh xe theo model (**không cần quyền ảnh**) | **#4** | Hàng cuộn ngang |
| Layer 4 — Personal: mở thư viện ảnh cá nhân (cần quyền) · gỡ ảnh hiện tại | #4 | Chrome |

**Visual Hierarchy**
1. **Ảnh với khung crop, vùng bị cắt làm tối** — Zone A. Vùng tối chính là thông tin quan trọng nhất của màn này.
2. **Hàng ảnh xe theo model** — Zone B, cuộn ngang.
3. **CTA "Xong"** — Zone B đáy.
4. **Chrome**: drag indicator, bộ chọn nguồn ảnh, cảnh báo độ phân giải, nút "Đặt lại khung".

*Self-check*: CTA 50pt ⇒ đạt. Vùng crop chiếm ~45% chiều cao sheet ⇒ đủ để thao tác chính xác. Không có animation trong lúc kéo ⇒ đúng SF-010 (mọi độ trễ ở đây làm mất cảm giác trực tiếp).

**Required Features (FR)**
- FR-027 P2: hàng ảnh xe theo model dùng được **không cần quyền** thư viện ảnh
- FR-027 P3: quyền ảnh bị từ chối → chỉ dùng ảnh xe theo model, **luồng không bị chặn**
- FR-027 P4: khung crop theo **đúng tỉ lệ màn hình xe**, **làm tối rõ ràng vùng sẽ bị cắt** (SF-010); kéo, zoom, xoay, "Đặt lại khung"
- FR-027 **BR-027.1**: vùng bị cắt hiển thị **trước khi lưu**
- FR-027 **BR-027.3**: ảnh cá nhân thuộc Premium — **xem trước và crop được đầy đủ**, chỉ chặn ở bước lưu
- FR-027 VR-027.1: khung crop **luôn** giữ đúng tỉ lệ; người dùng không thể tạo khung sai tỉ lệ
- FR-028 P2–P3: ảnh độ phân giải thấp → **cảnh báo sẽ mờ** + mức tối thiểu cần thiết; cảnh báo **không chặn** việc lưu
- FR-028 VR-028.1: dung lượng sau nén **≤ 2MB** — bắt buộc, không ngoại lệ

**UX Enhancements** (`composition.action.defaults`)
- `inline-validation`: cảnh báo độ phân giải hiện ngay khi chọn ảnh, không chờ tới lúc lưu
- `escape-route-always-visible`: nút đóng + "Đặt lại khung"
- `single-primary-cta`: một CTA
- Vùng cắt tối dần 0,2s khi khung xuất hiện; **không** animation trong lúc kéo (SF-010)

**Content Zones Map**

```
┌─────────────────────────────────────┐
│ ZONE D: Navigation                  │ ← dragIndicator + [✕]
├─────────────────────────────────────┤
│ ZONE A: Context — ảnh + khung crop  │ ← ~45% sheet
├─────────────────────────────────────┤
│ ZONE B: nguồn ảnh + CTA             │ ← hàng ảnh + CTA 50pt
├─────────────────────────────────────┤
│ ZONE C: — (unused cho Action)       │ ← 0; cảnh báo ở Zone B
└─────────────────────────────────────┘
```

**Layout**

```
┌──────────────────────────────────────────────┐
│              ▬▬▬▬                     [✕]    │ ZONE D
├──────────────────────────────────────────────┤
│ ┌──────────────────────────────────────────┐ │ ZONE A ~45%
│ │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│ │ vùng SẼ BỊ CẮT
│ │▓┌────────────────────────────────────┐▓▓│ │ làm tối rõ ràng
│ │▓│                                    │▓▓│ │ (BR-027.1)
│ │▓│   [ ảnh Camry của người dùng ]     │▓▓│ │
│ │▓│   khung crop tỉ lệ 1180×420        │▓▓│ │ LUÔN đúng tỉ lệ
│ │▓│                                    │▓▓│ │ (VR-027.1)
│ │▓└────────────────────────────────────┘▓▓│ │
│ │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│ │
│ └──────────────────────────────────────────┘ │
│  Kéo và zoom để chọn vùng hiện trên xe        │ caption
│  [↻ Xoay]                    [Đặt lại khung] │ BtnTertiary ×2
├──────────────────────────────────────────────┤
│  NGUỒN ẢNH                                   │ ZONE B
│  [▸Ảnh xe theo model] [Ảnh của tôi 🔒]       │ chip h=32
│                                              │ ảnh model KHÔNG
│ ┌────┐ ┌────┐ ┌────┐ ┌────┐                 │ cần quyền
│ │Cam │ │Cam │ │Cam │ │Cam │  →→             │ thumb 64×64 r=8
│ │ ry1│ │ ry2│ │ ry3│ │ ry4│                 │ cuộn ngang
│ └────┘ └────┘ └────┘ └────┘                 │
│                                              │
│ ┌──────────────────────────────────────────┐ │
│ │                 Xong                     │ │ h=50 bg accent
│ └──────────────────────────────────────────┘ │
└──────────────────────────────────────────────┘
```

**Layout Variants** *(bắt buộc: Medium density)*

**Variant A — Ảnh độ phân giải thấp (cảnh báo, không chặn)**
```
┌──────────────────────────────────────────────┐
│              ▬▬▬▬                     [✕]    │
│ ┌ ▓▓▓ [ ảnh 640×480 ] ▓▓▓ ─────────────────┐│
│  Kéo và zoom để chọn vùng hiện trên xe        │
├──────────────────────────────────────────────┤
│ ┌──────────────────────────────────────────┐ │ warning
│ │ ⚠ Ảnh này sẽ hơi mờ trên màn hình xe     │ │ background
│ │   Màn hình xe của bạn cần ảnh rộng ít    │ │
│ │   nhất 2360px. Ảnh này rộng 640px.        │ │ mono cho SỐ
│ │   Bạn vẫn dùng được nếu muốn.             │ │ KHÔNG chặn
│ └──────────────────────────────────────────┘ │ (BR-028.2)
│  … nguồn ảnh …                               │
│ ┌──────────────────────────────────────────┐ │
│ │                 Xong                     │ │ VẪN bật
│ └──────────────────────────────────────────┘ │
└──────────────────────────────────────────────┘
```

**Variant B — Quyền thư viện ảnh bị từ chối (ERR-027.1)**
```
┌──────────────────────────────────────────────┐
│              ▬▬▬▬                     [✕]    │
│ ┌ ▓▓▓ [ ảnh Camry theo model ] ▓▓▓ ─────────┐│
├──────────────────────────────────────────────┤
│  NGUỒN ẢNH                                   │
│  [▸Ảnh xe theo model] [Ảnh của tôi]          │
│ ┌──────────────────────────────────────────┐ │ info background
│ │ ℹ Chưa có quyền truy cập ảnh              │ │
│ │   Bạn vẫn dùng được bộ ảnh xe theo model   │ │ luồng KHÔNG
│ │   bên dưới — đầy đủ, không cần quyền gì.   │ │ bị chặn
│ │              [Mở Cài đặt]                 │ │
│ └──────────────────────────────────────────┘ │
│ ┌────┐ ┌────┐ ┌────┐ ┌────┐  →→             │ vẫn duyệt được
│ └────┘ └────┘ └────┘ └────┘                 │
│ ┌──────────────────────────────────────────┐ │
│ │                 Xong                     │ │ VẪN bật
│ └──────────────────────────────────────────┘ │
└──────────────────────────────────────────────┘
```

**Components**
- `SheetContainer` — `detentLarge: 90%` (cần chỗ để thao tác crop).
- `ImageCropCanvas` — Tokens: vùng cắt `background: rgba(0,0,0,0.55)`; khung crop viền `${color.palette.accent}` 2px; **không** animation trong lúc kéo; vùng tối fade-in 0,2s khi khung xuất hiện.
- `BtnTertiary` ×2 ("Xoay", "Đặt lại khung").
- `ChipSourcePicker` ×2 — Tokens: `${component.chip}`; "Ảnh của tôi" có `LockLabel` khi là Premium.
- `ThumbCarousel` + `ThumbVehicle` — Tokens: thumb 64×64, `radius: ${border.radius.md}`(8), selected viền `${color.palette.accent}` 2px.
- `ResolutionWarningBanner` (Variant A) — Tokens: `background: ${color.semantic.warning.background}`, `foreground: ${color.semantic.warning.color}`; số px dùng mono.
- `PermissionInfoBanner` (Variant B) — Tokens: `background: ${color.semantic.info.background}`, `foreground: ${color.semantic.info.color}`.
- `BtnPrimary` ("Xong" / "Mở khoá").

**States** (8)

| State | Loại | Context | Layout/Behavior |
|---|---|---|---|
| **First Visit** | user-context | Chưa chọn ảnh | Mặc định là **ảnh xe theo model** — có kết quả tốt mà không phải chọn gì |
| **Returning** | user-context | Đã có ảnh | Ảnh hiện tại nạp sẵn kèm **khung crop cũ**; chỉnh tiếp được, không phải làm lại |
| **Power User** | user-context | Ảnh cá nhân tỉ lệ lạ | Tự đề xuất khung crop tốt nhất; vùng cắt hiện rõ trước khi lưu |
| **Free tier** | user-context | Ảnh cá nhân thuộc Premium | Chọn và crop **được đầy đủ**; nút "Xong" → "Mở khoá" → WF-010 |
| **Error** | user-context | Ảnh độ phân giải thấp | **Variant A**: cảnh báo sẽ mờ + mức tối thiểu; **vẫn cho lưu** |
| **Default** | data | Ảnh nạp xong | Layout như trên |
| **Loading** | data | Đang nén ảnh xuống ≤ 2MB | CTA hiện spinner; canvas crop bị khoá tạm |
| **Empty** | data | Quyền thư viện ảnh bị từ chối | **Variant B**: chỉ dùng bộ ảnh theo model; **luồng không bị chặn** |

**User Flow**
- **Entry**: ô ảnh trên **WF-008** · nút "Đổi ảnh" trong **WF-023**
- **Exit**: **WF-008** hoặc **WF-023** (trở về đúng nơi vào) · **WF-010** (ảnh cá nhân thuộc Premium)
- **Task Flow**: bước 3–4 của **TF-004**
- **Transitions**: sheet trượt lên 0,35s; vùng cắt tối dần 0,2s; **không** animation khi kéo/zoom (SF-010)

---

### 3.25 WF-025 — Sheet: Quản Lý Đăng Ký 📱 · *Template D (Management)*

**Design System**: `bento-grid`
**Archetype**: Management | **Secondary**: Action | **Density**: Medium (4 vùng)
**Source UC**: UC-029 (chính), UC-027, UC-028, UC-030 | **Source FR**: **FR-053** (quản lý/huỷ), **FR-003** (phục hồi giao dịch)
**User Intent**: "Tôi muốn biết tôi đang trả cho cái gì và huỷ được nếu tôi muốn."

**Action Layer → Visual Hierarchy**

| UC Action Layer | Slot | Ghi chú |
|---|---|---|
| Layer 1 — Primary: xem trạng thái đăng ký và huỷ nếu muốn | **#3** | Nút "Huỷ đăng ký" — **không ẩn, không làm mờ** |
| Layer 2 — Contextual: xem ngày gia hạn kế tiếp | **#1** | Zone A |
| Layer 3 — Discovery: mở rộng danh sách tính năng đang có · xem các bậc khác | **#2** | SF-019 |
| Layer 4 — Personal: "Phục hồi giao dịch" · xem lịch sử giao dịch qua iOS | #4 | Zone D |

**Visual Hierarchy**
1. **Gói hiện tại · giá · ngày gia hạn** — Zone A. Câu trả lời trực tiếp cho câu hỏi người dùng mở sheet này để hỏi.
2. **Danh sách tính năng đang có (mở rộng được)** — Zone B, SF-019.
3. **Nút "Huỷ đăng ký"** — Zone B, **không ẩn, không làm mờ, không animation làm chậm đường tới nó**.
4. **Chrome**: drag indicator, "Phục hồi giao dịch", link trang subscription iOS.

*Self-check*: đường huỷ = WF-012 → WF-025 → WF-027 = **3 chạm** ⇒ đúng AC-029.2. Nút huỷ **không** bị làm mờ ⇒ đúng BR-053.4. Row nhất quán 50pt ⇒ đạt.

**Required Features (FR)**
- FR-053 P2: Zone A hiện gói · giá · ngày gia hạn kế tiếp (hoặc "đã mua vĩnh viễn")
- FR-053 P3: mở rộng inline danh sách tính năng, **đánh dấu rõ tính năng nào vẫn còn ở gói Free** (SF-019) — trình bày trung thực, không phải chiêu níu giữ
- FR-053 P4 / **BR-053.4**: nút huỷ ở Zone B, **cấm** animation hay bước trung gian làm chậm đường tới nó
- FR-053 P5: chạm huỷ → **WF-027** alert nêu rõ **ngày quyền Premium kết thúc** và **cấu hình được giữ**
- FR-053 P8 / **BR-053.2**: Lifetime → **không** hiện nút huỷ; nếu còn subscription cũ thì **nhắc huỷ để không trả trùng**
- FR-053 **BR-053.1**: đường huỷ **tối đa 3 chạm** kể từ WF-012
- FR-003 P2: "Phục hồi giao dịch" **luôn hiện**

**UX Enhancements** (`composition.management.defaults`)
- `grouped-rows`: nhóm "Gói hiện tại" và nhóm "Tính năng đang có"
- `destructive-needs-confirm`: huỷ → WF-027
- `inline-status-on-row`: trạng thái hiện ngay trên dòng
- `pull-to-refresh`: **không dùng** — dữ liệu đến từ StoreKit, có nút "Phục hồi giao dịch" làm việc đó rõ ràng hơn
- Mở rộng danh sách tính năng 0,25s; **không** có animation nào trên đường tới nút huỷ (BR-053.4)

**Content Zones Map**

```
┌─────────────────────────────────────┐
│ ZONE D: Navigation                  │ ← dragIndicator + [✕]
├─────────────────────────────────────┤
│ ZONE A: gói hiện tại (override)     │ ← ~120pt
├─────────────────────────────────────┤
│ ZONE B: tính năng + nút huỷ         │ ← fill
├─────────────────────────────────────┤
│ ZONE D: Phục hồi + link iOS         │ ← 44pt + footnote
└─────────────────────────────────────┘
```

**Layout** — *subscription Yearly đang chạy*

```
┌──────────────────────────────────────────────┐
│              ▬▬▬▬                     [✕]    │ ZONE D
├──────────────────────────────────────────────┤
│ ┌──────────────────────────────────────────┐ │ ZONE A ~120pt
│ │  Carbina Premium — Hằng năm              │ │ h3 22/600
│ │  ──────────────────────────────────────  │ │
│ │  Giá              29,99 $ / năm          │ │ mono
│ │  Gia hạn kế tiếp  24/08/2027             │ │ mono
│ └──────────────────────────────────────────┘ │
├──────────────────────────────────────────────┤
│  Xem tính năng đang có                  [v]  │ ZONE B row 50pt
│                                              │ → SF-019
│ ┌──────────────────────────────────────────┐ │
│ │             Huỷ đăng ký                  │ │ h=50 border
│ └──────────────────────────────────────────┘ │ destructive
│  KHÔNG ẩn · KHÔNG làm mờ · KHÔNG animation   │ (BR-053.4)
│  làm chậm đường tới nút này                  │
│                                              │
│  Xem các gói khác                       [>]  │ → WF-010
├──────────────────────────────────────────────┤
│  Phục hồi giao dịch                          │ ZONE D
│  Quản lý trong Cài đặt iOS               [>] │ footnote
└──────────────────────────────────────────────┘
```

**Layout Variants** *(bắt buộc: Medium density)*

**Variant A — Danh sách tính năng đã mở rộng (SF-019)**
```
┌──────────────────────────────────────────────┐
│ ┌ Carbina Premium — Hằng năm · 29,99 $ ─────┐│
├──────────────────────────────────────────────┤
│  Xem tính năng đang có                  [^]  │ mở rộng 0,25s
│ ┌──────────────────────────────────────────┐ │
│ │ Widget không giới hạn    → còn 1 ở Free  │ │ ĐÁNH DẤU RÕ
│ │ 12 âm thanh              → còn 3 ở Free  │ │ cái gì VẪN CÒN
│ │ Giọng chào AI            → mất            │ │ (trình bày
│ │ Ảnh cá nhân              → mất            │ │  trung thực,
│ │ Dashboard AI học         → mất            │ │  không níu giữ)
│ │ Thư viện xe đầy đủ       → mất            │ │
│ │ ────────────────────────────────────────  │ │
│ │ Cấu hình widget/sound bạn đã tạo VẪN ĐƯỢC │ │ AC-027.3
│ │ GIỮ NGUYÊN sau khi huỷ.                   │ │
│ └──────────────────────────────────────────┘ │
│ ┌──────────────────────────────────────────┐ │
│ │             Huỷ đăng ký                  │ │ vẫn ở đúng chỗ
│ └──────────────────────────────────────────┘ │
└──────────────────────────────────────────────┘
```

**Variant B — Lifetime (không có gì để huỷ) + còn subscription cũ**
```
┌──────────────────────────────────────────────┐
│              ▬▬▬▬                     [✕]    │
├──────────────────────────────────────────────┤
│ ┌──────────────────────────────────────────┐ │ ZONE A
│ │  ✓ Đã mua vĩnh viễn                      │ │ success.color
│ │  Mọi tính năng Premium, không gia hạn.    │ │
│ └──────────────────────────────────────────┘ │
│ ┌──────────────────────────────────────────┐ │ warning
│ │ ⚠ Bạn vẫn còn subscription Hằng năm      │ │ background
│ │   Gói Vĩnh viễn đã bao trùm mọi tính năng.│ │
│ │   Huỷ subscription để không trả trùng.     │ │ NHẮC huỷ
│ │        [Huỷ subscription cũ]              │ │ (BR-054.3)
│ └──────────────────────────────────────────┘ │
│  Xem tính năng đang có                  [v]  │
│  ✗ KHÔNG có nút "Huỷ đăng ký" cho Lifetime   │ (AC-029.3)
├──────────────────────────────────────────────┤
│  Phục hồi giao dịch                          │
└──────────────────────────────────────────────┘
```

**Components**
- `SheetContainer` — `detentMedium: 50%`.
- `CardSubscriptionStatus` (Zone A) — Tokens: `radius: 16`, `padding: 16`; giá và ngày dùng mono; biến thể Lifetime `background: ${color.semantic.success.background}`.
- `FeatureListExpandable` — Tokens: row 44pt, mở rộng `${animation.duration.normal}`(0,25s); nhãn "còn ở Free" `${color.semantic.success.color}`; nhãn "mất" `${color.palette.textSecondary}`.
- `BtnDestructiveOutline` ("Huỷ đăng ký") — Tokens: `height: 50`, `radius: 16`, `background: transparent`, `foreground: ${color.semantic.destructive.color}`, `borderColor: ${color.semantic.destructive.color}`. **Không** ẩn sau menu, **không** làm mờ.
- `DoubleChargeWarning` (Variant B) — Tokens: `background: ${color.semantic.warning.background}`, `foreground: ${color.semantic.warning.color}`.
- `RowNavigable` ("Xem các gói khác" → WF-010, "Quản lý trong Cài đặt iOS"), `BtnTertiary` ("Phục hồi giao dịch").

**States** (8)

| State | Loại | Context | Layout/Behavior |
|---|---|---|---|
| **First Visit** | user-context | Gói Free | Zone A "Gói Free"; **không có gì để huỷ**; Zone B hiện tính năng đang có ở Free + lối vào WF-010 |
| **Returning** | user-context | Subscription đang chạy | Đủ giá + ngày gia hạn; nút huỷ ở Zone B; đường huỷ **≤ 3 chạm** từ WF-012 |
| **Trial đang chạy** | user-context | Ngày 1–7 của trial | Nêu rõ ngày hết trial và ngày trừ tiền; nút huỷ **nhấn mạnh hơn** nút xem gói khác |
| **Power User** | user-context | Lifetime (+ subscription cũ) | **Variant B**: "đã mua vĩnh viễn"; **không** nút huỷ; nhắc huỷ subscription cũ để không trả trùng |
| **Error** | user-context | Không đọc được trạng thái từ StoreKit | Zone A "chưa xác định được" + [Phục hồi giao dịch]; nếu không có giao dịch nào thì **nói rõ điều đó** (ERR-053.2) |
| **Default** | data | Trạng thái đọc xong | Layout như trên |
| **Loading** | data | Truy vấn StoreKit | Zone A skeleton 120pt; nút huỷ **vô hiệu tạm** — cấm huỷ khi chưa biết đang huỷ cái gì |
| **Empty** | data | Đã huỷ trước đó | Hiện rõ **ngày quyền Premium kết thúc**; nút huỷ biến mất; nút "Xem các gói khác" nổi bật hơn |

**User Flow**
- **Entry**: dòng "Đăng ký của tôi" trên **WF-012** · nút "Huỷ trial" / "Xem chi tiết đăng ký" trên **WF-013**
- **Exit**: **WF-027** (xác nhận huỷ) · **WF-012** · **WF-010** ("Xem các gói khác") · trang subscription của iOS
- **Task Flow**: bước 4–6 của **TF-008** · bước 5 của **TF-009**
- **Transitions**: sheet trượt lên 0,35s; danh sách tính năng mở rộng 0,25s; alert WF-027 fade-in 0,2s. **Không** animation nào trên đường tới nút huỷ

---

### 3.26 WF-026 — Sheet: Chọn Ngôn Ngữ 📱 · *Template B (Action)*

**Design System**: `bento-grid`
**Archetype**: Action | **Density**: Light (2 vùng)
**Source UC**: UC-031 | **Source FR**: **FR-055** (chọn ngôn ngữ), **FR-056** (fallback bản dịch)
**User Intent**: "Tôi muốn dùng app bằng tiếng của tôi, kể cả phần giọng nói."

**Action Layer → Visual Hierarchy**

| UC Action Layer | Slot | Ghi chú |
|---|---|---|
| Layer 1 — Primary: chọn một ngôn ngữ | **#3** | **Chọn là áp dụng ngay** — không có nút Lưu |
| Layer 2 — Contextual: chọn "Theo hệ thống" · đóng sheet | **#2** | Trong danh sách |
| Layer 3 — Discovery: xem ngôn ngữ nào sẽ có ở MVP 2 | **#4** | Ghi chú ở đáy — nêu rõ **chưa có**, không hiện lựa chọn không hoạt động |
| Layer 4 — Personal | — | **Trống có chủ ý** — ngôn ngữ giọng chào theo ngôn ngữ app, **không** tách thành lựa chọn thứ hai ở MVP 1 |

**Visual Hierarchy**
1. **Danh sách 4 lựa chọn** — Zone A, ngôn ngữ hiện tại được đánh dấu. Đây là toàn bộ nội dung.
2. **Ghi chú DE/FR/IT thuộc MVP 2** — Zone B, `${typography.scale.caption}`.
3. — (**không có CTA** vì chọn là áp dụng ngay)
4. **Chrome**: drag indicator, nút đóng.

*Self-check*: row 50pt > 44pt ⇒ đạt. Không có CTA — đúng vì chọn là áp dụng ngay (không có trạng thái "đã chọn nhưng chưa lưu" để cần một nút xác nhận). **Không** hiện lựa chọn không hoạt động ⇒ đúng BR-055.2.

**Required Features (FR)**
- FR-055 P2–P3: 4 lựa chọn (English · Español · Português (Brasil) · Theo hệ thống); ngôn ngữ hiện tại được đánh dấu; **chọn là áp dụng ngay**, không nút Lưu, **không** khởi động lại app
- FR-055 P4 / **BR-055.2**: ghi chú DE/FR/IT thuộc MVP 2 — **cấm** hiện lựa chọn chưa hỗ trợ
- FR-055 P5: bàn giao FR-039 để đổi ngôn ngữ **nội dung giọng chào** từ lượt phát kế tiếp
- FR-055 **BR-055.1**: ngôn ngữ UI và tiền tệ giá là **hai chiều độc lập**
- FR-056 ERR-056.2: ngôn ngữ hệ thống không thuộc 3 ngôn ngữ → dùng English và **nêu rõ lý do**
- FR-039 ERR-039.1: đổi ngôn ngữ khi đang cắm CarPlay → câu chào đang phát **không bị cắt giữa câu**

**UX Enhancements** (`composition.action.defaults`)
- `single-primary-cta`: **sai lệch có chủ ý** — không có CTA vì chọn là áp dụng ngay; thêm nút "Lưu" sẽ tạo một bước không cần thiết và một trạng thái trung gian không có FR
- `escape-route-always-visible`: nút đóng
- `inline-validation`: **không áp dụng**
- Áp dụng ngay bằng crossfade toàn app 0,25s — cùng cơ chế với đổi theme (SF-021)

**Content Zones Map**

```
┌─────────────────────────────────────┐
│ ZONE D: Navigation                  │ ← dragIndicator + [✕]
├─────────────────────────────────────┤
│ ZONE A: Context — danh sách 4 lựa chọn│ ← 4×50pt
├─────────────────────────────────────┤
│ ZONE B: ghi chú MVP 2               │ ← ~56pt (không phải CTA)
├─────────────────────────────────────┤
│ ZONE C: — (unused cho Action)       │ ← 0
└─────────────────────────────────────┘
```

**Layout**

```
┌──────────────────────────────────────────────┐
│              ▬▬▬▬                     [✕]    │ ZONE D
├──────────────────────────────────────────────┤
│  Ngôn ngữ                                    │ headline
│ ┌──────────────────────────────────────────┐ │ ZONE A
│ │ ▸ Theo hệ thống              ✓           │ │ row 50pt
│ │   Đang dùng: English                     │ │ accentSubtle
│ ├──────────────────────────────────────────┤ │ caption
│ │   English                                │ │
│ ├──────────────────────────────────────────┤ │
│ │   Español                                │ │
│ ├──────────────────────────────────────────┤ │
│ │   Português (Brasil)                     │ │
│ └──────────────────────────────────────────┘ │
│  Chọn là áp dụng ngay, kể cả nội dung         │ caption
│  giọng chào AI.                              │ textSecondary
├──────────────────────────────────────────────┤
│  Deutsch, Français và Italiano sẽ có ở        │ ZONE B ~56pt
│  bản cập nhật sau. Chưa có ở bản này.         │ footnote
│  KHÔNG hiện lựa chọn không hoạt động          │ textTertiary
└──────────────────────────────────────────────┘
```

**Components**
- `SheetContainer` — `detentMedium: 50%`.
- `RowSelectableLanguage` ×4 — Tokens: `height: ${component.row.height}`(50), selected `background: ${color.palette.accentSubtle}` + `✓` tint `${color.palette.accent}`; dòng phụ "Đang dùng: …" `${typography.scale.caption}`.
- `NoteFootnote` — Tokens: `font: ${typography.scale.footnote}`, `color: ${color.palette.textTertiary}`.

**States** (7)

| State | Loại | Context | Layout/Behavior |
|---|---|---|---|
| **First Visit** | user-context | Chưa từng đổi | "Theo hệ thống" được chọn; dòng phụ hiện ngôn ngữ đang thực dùng |
| **Returning** | user-context | Đã chọn thủ công | Ngôn ngữ đã chọn được đánh dấu; đổi lại áp dụng ngay không khởi động lại |
| **Power User** | user-context | Đang cắm CarPlay khi đổi | UI CarPlay cập nhật ở lần vẽ kế tiếp; **câu chào đang phát không bị cắt giữa câu** (ERR-039.1) |
| **Error** | user-context | Ngôn ngữ hệ thống không thuộc 3 ngôn ngữ | Dòng phụ nêu rõ **"Đang dùng: English"** kèm lý do (ERR-056.2) |
| **Default** | data | Bảng chuỗi nạp xong | Layout như trên |
| **Loading** | data | Đang áp dụng ngôn ngữ mới | Crossfade toàn app 0,25s; sheet **không** hiện spinner (thao tác cục bộ, nhanh hơn ngưỡng cảm nhận) |
| **Empty** | data | Thiếu bản dịch một chuỗi | Rơi về English cho **đúng chuỗi đó**; phần còn lại giữ ngôn ngữ đã chọn; **cấm** hiện khoá dịch thô (ERR-056.1) |

**User Flow**
- **Entry**: dòng "Ngôn ngữ" trên **WF-012**
- **Exit**: **WF-012**
- **Task Flow**: bước 1–2 của **TF-012**
- **Transitions**: sheet trượt lên 0,35s; crossfade toàn app 0,25s khi áp dụng; sheet **tự đóng** sau khi chọn (không cần chạm đóng)

---

### 3.27 WF-027 — Alert: Xác Nhận Huỷ Trial 📱 · *Template B (Action)*

**Design System**: `bento-grid`
**Archetype**: Action | **Density**: Light (1 vùng)
**Source UC**: UC-029 (chính), UC-028 | **Source FR**: **FR-053** (quản lý/huỷ đăng ký)
**User Intent**: "Tôi muốn chắc chắn mình hiểu hậu quả trước khi huỷ."

**Action Layer → Visual Hierarchy**

| UC Action Layer | Slot | Ghi chú |
|---|---|---|
| Layer 1 — Primary: xác nhận huỷ (hoặc quay lại) | **#3** | Hai nút, "Huỷ đăng ký" là destructive |
| Layer 2 — Contextual: "Giữ đăng ký" — quay lại không làm gì | **#3** | Ngang hàng với nút huỷ |
| Layer 3 — Discovery | — | **Trống có chủ ý** — alert phải chỉ có **một câu hỏi**; mọi thứ thêm vào đều là dark pattern níu giữ (BR-027 của UC-029) |
| Layer 4 — Personal | — | **Trống có chủ ý** |

**Visual Hierarchy**
1. **Một câu nêu rõ quyền Premium còn tới ngày nào + cấu hình sẽ được giữ** — nội dung duy nhất.
2. — (không có)
3. **Hai nút** — "Giữ đăng ký" (`BtnSecondary`) và "Huỷ đăng ký" (`BtnDestructiveOutline`).
4. — (alert không có chrome)

*Self-check*: alert chỉ có một câu hỏi ⇒ đạt. Cả hai nút 50pt ⇒ đạt. **Không** có nội dung níu giữ (ưu đãi, giảm giá, "bạn sẽ mất…" dài dòng) ⇒ đúng chủ ý.

**Required Features (FR)**
- FR-053 P5: alert nêu rõ **quyền Premium còn dùng tới ngày nào** và **cấu hình đã tạo sẽ được giữ**
- FR-053 P6: xác nhận → chuyển trang quản lý subscription của iOS; ghi `subscription_cancelled`
- FR-053 ERR-053.4: không mở được trang subscription iOS → nêu rõ + **hướng dẫn đường đi thủ công** trong Cài đặt hệ thống
- FR-051 AC-027.3: cấu hình widget/sound **được giữ nguyên** sau khi về Free — phải nói ra ở đây, không để người dùng tự đoán

**UX Enhancements** (`composition.action.defaults`)
- `confirmation-dialog`: đây **là** hộp xác nhận
- `escape-route-always-visible`: "Giữ đăng ký"
- **Không** progress indicator, **không** nội dung khám phá, **không** ưu đãi giữ chân — sự thiếu vắng là thiết kế chống dark pattern

**Content Zones Map**

```
┌─────────────────────────────────────┐
│ ZONE A: Context — một câu hỏi        │ ← ~120pt
├─────────────────────────────────────┤
│ ZONE B: 2 nút                        │ ← 2×50pt
├─────────────────────────────────────┤
│ ZONE C / ZONE D: — (unused)          │ ← 0
└─────────────────────────────────────┘
```

**Layout**

```
        ┌────────────────────────────────────┐   alert maxWidth 300
        │                                    │   r=20 p=20
        │  Huỷ đăng ký Carbina Premium?      │   headline 17/600
        │                                    │
        │  Bạn vẫn dùng Premium tới           │   callout 16/400
        │  24/08/2026. Sau đó về gói Free.    │   mono cho NGÀY
        │                                    │
        │  Widget và âm thanh bạn đã tạo      │   NÊU RÕ cấu hình
        │  vẫn được giữ nguyên.               │   được giữ
        │                                    │   (AC-027.3)
        │ ┌────────────────────────────────┐ │
        │ │        Giữ đăng ký             │ │   BtnSecondary h=50
        │ └────────────────────────────────┘ │
        │ ┌────────────────────────────────┐ │
        │ │        Huỷ đăng ký             │ │   BtnDestructive h=50
        │ └────────────────────────────────┘ │
        │                                    │
        └────────────────────────────────────┘
          shadow.elevation.5 · overlay rgba(0,0,0,0.4)
          ✗ không ưu đãi giữ chân  ✗ không nội dung thêm
```

**Components**
- `AlertContainer` — Tokens: `${component.alert}`: `radius: 20`, `maxWidth: 300`, `padding: 20`, `background: ${color.palette.surfaceElevated}`, `shadow: ${shadow.elevation.5}`, title `${typography.scale.headline}`, body `${typography.scale.callout}`; overlay `rgba(0,0,0,0.4)`.
- `BtnSecondary` ("Giữ đăng ký"), `BtnDestructiveOutline` ("Huỷ đăng ký") — cùng `height: 50`, `radius: 16`.
- **Không có** component nào khác — theo thiết kế.

**States** (7)

| State | Loại | Context | Layout/Behavior |
|---|---|---|---|
| **First Visit** | user-context | Huỷ trong trial | Nêu rõ vẫn dùng Premium **tới hết ngày 7**, sau đó về gói Free |
| **Returning** | user-context | Huỷ subscription đang trả phí | Nêu rõ **ngày kết thúc chu kỳ đã trả tiền** |
| **Power User** | user-context | Có cả Lifetime và subscription | Nêu rõ **Lifetime đã bao trùm** nên huỷ subscription **không** làm mất quyền gì |
| **Error** | user-context | Không mở được trang subscription iOS (ERR-053.4) | Nêu rõ + **hướng dẫn đường đi thủ công**: Cài đặt → Apple ID → Đăng ký |
| **Default** | data | Ngày kết thúc đọc được từ StoreKit | Layout như trên |
| **Loading** | data | Đang đọc ngày kết thúc | Alert **chưa hiện** cho tới khi có ngày — **cấm** hiện alert huỷ mà không nói được ngày nào (nguyên tắc "không đoán con số" của ERR-051.4) |
| **Empty** | data | Không áp dụng — chỉ hiện khi có đăng ký để huỷ | **Không tồn tại có chủ ý** |

**User Flow**
- **Entry**: nút "Huỷ đăng ký" trên **WF-025** · nút "Huỷ trial" trên **WF-013**
- **Exit**: trang quản lý subscription của iOS (xác nhận) · **WF-025** ("Giữ đăng ký")
- **Task Flow**: bước 4–5 của **TF-008**
- **Transitions**: fade-in 0,2s + scale 0,97→1,0; fade-out 0,15s

---

### 3.28 WF-028 — Sheet: Gửi Báo Cáo Tương Thích 📱 · *Template B (Action)*

**Design System**: `bento-grid`
**Archetype**: Action | **Secondary**: Management | **Density**: Medium (4 vùng)
**Source UC**: UC-017 (chính), UC-033 | **Source FR**: **FR-032** (gửi báo cáo chẩn đoán), **FR-060** (kênh phản hồi cho người không hài lòng)
**User Intent**: "Tôi muốn gửi vấn đề của mình đi, và muốn biết chính xác dữ liệu gì rời khỏi máy tôi."

**Action Layer → Visual Hierarchy**

| UC Action Layer | Slot | Ghi chú |
|---|---|---|
| Layer 1 — Primary: xem danh sách dữ liệu sẽ gửi và chạm "Gửi" | **#3** | CTA "Gửi" |
| Layer 2 — Contextual: thêm ghi chú (≤ 500 ký tự) · **bỏ tick** một mục dữ liệu | **#2** | Danh sách có tick + ô ghi chú |
| Layer 3 — Discovery: mở rộng để xem **giá trị thật** của từng mục | **#2** | SF-020 |
| Layer 4 — Personal: sao chép toàn bộ nội dung báo cáo để tự gửi kênh khác | #4 | Chrome |

> **Hai biến thể có mục tiêu khác nhau dù cùng màn hình** (FR-032 vs FR-060): vào từ **WF-014** thì danh sách dữ liệu là chính và ô ghi chú là phụ; vào từ nhánh "không hài lòng" của **WF-030** thì **ô ghi chú được nhấn mạnh** vì ở ngữ cảnh đó lời của người dùng quan trọng hơn số liệu (BR-060.2).

**Visual Hierarchy**
1. **Danh sách từng mục dữ liệu sẽ gửi, có tick** — Zone A. Đây là cách biến cam kết "không thu PII" thành thứ người dùng **tự kiểm tra được**.
2. **Ô ghi chú tuỳ chọn** — Zone B.
3. **CTA "Gửi"**.
4. **Chrome**: drag indicator, nút sao chép, cam kết không PII.

*Self-check*: CTA 50pt ⇒ đạt. Mỗi mục dữ liệu là row 50pt ⇒ đạt. CTA vô hiệu khi bỏ tick hết mọi mục ở biến thể FR-032 ⇒ đúng VR-032.2.

**Required Features (FR)**
- FR-032 P4: liệt kê **từng mục** dữ liệu; chạm một mục → mở rộng hiện **giá trị thật** (ví dụ `screen_width: 1180`) (SF-020)
- FR-032 P5: bỏ tick một mục → mục đó **bị loại khỏi payload**
- FR-032 P6: nút "Sao chép" copy toàn bộ payload dạng chữ
- FR-032 P8: chạm "Gửi" → xác nhận **≤ 500ms không chờ mạng**; xếp hàng on-device nếu offline
- FR-032 **BR-032.2**: liệt kê từng mục **kèm giá trị thật**
- FR-032 **BR-032.3**: payload **không** chứa PII (NFR-011)
- FR-032 VR-032.1–2: ghi chú ≤ 500 ký tự (vượt thì cắt); bỏ tick hết → CTA **vô hiệu** kèm lời nhắc cần ít nhất kích thước màn hình
- FR-060 P2 / **BR-060.2**: biến thể "không hài lòng" → **Zone C (ô ghi chú) được nhấn mạnh**
- FR-060 **BR-060.1**: **cấm tuyệt đối** mở dialog đánh giá App Store trong nhánh này
- FR-060 VR-060.1: nhánh FR-060 cho phép gửi **không kèm** dữ liệu chẩn đoán nào

**UX Enhancements** (`composition.action.defaults`)
- `inline-validation`: bỏ tick hết → CTA vô hiệu + lời nhắc
- `keyboard-handling`: ô ghi chú có toolbar "Xong"; đếm ký tự còn lại khi > 400
- `escape-route-always-visible`: nút đóng — đóng sheet là kết thúc hợp lệ, **không** đẩy ra App Store (BR-060.3)
- `single-primary-cta`: một CTA
- Giá trị kỹ thuật hiện dạng **mono đơn sắc** — để đọc rõ đây là dữ liệu, không phải nội dung marketing (SF-020)

**Content Zones Map**

```
┌─────────────────────────────────────┐
│ ZONE D: Navigation                  │ ← dragIndicator + [✕] + [⧉]
├─────────────────────────────────────┤
│ ZONE A: Context — danh sách dữ liệu │ ← 4×50pt (mở rộng được)
├─────────────────────────────────────┤
│ ZONE B: ô ghi chú + CTA             │ ← textarea ~100pt + CTA 50pt
├─────────────────────────────────────┤
│ ZONE C: — (Action) / nhấn mạnh ở    │ ← 0 ở biến thể FR-032
│   biến thể FR-060                   │
└─────────────────────────────────────┘
```

**Layout** — *biến thể FR-032, vào từ WF-014*

```
┌──────────────────────────────────────────────┐
│              ▬▬▬▬            [⧉]      [✕]    │ ZONE D
├──────────────────────────────────────────────┤
│  Dữ liệu sẽ được gửi                         │ headline
│  Chạm một mục để xem giá trị thật.            │ caption
│ ┌──────────────────────────────────────────┐ │ ZONE A
│ │ ✓ Kích thước màn hình xe            [v] │ │ row 50pt
│ │   screen_width: 1180                     │ │ MỞ RỘNG: mono
│ │   screen_height: 420                     │ │ đơn sắc
│ ├──────────────────────────────────────────┤ │
│ │ ✓ Phiên bản iOS                          │ │
│ ├──────────────────────────────────────────┤ │
│ │ ✓ Xe đã chọn                             │ │ bỏ tick được
│ ├──────────────────────────────────────────┤ │
│ │ ✓ Nguyên nhân lỗi render                 │ │
│ └──────────────────────────────────────────┘ │
│  Không gửi tên, email, số điện thoại, vị trí  │ footnote
│  hay nội dung lịch của bạn.                   │ cam kết không PII
├──────────────────────────────────────────────┤
│  Ghi chú (tuỳ chọn)                          │ ZONE B
│ ┌──────────────────────────────────────────┐ │
│ │                                          │ │ textarea ~100pt
│ │                                          │ │ r=12 max 500 ký tự
│ └──────────────────────────────────────────┘ │
│ ┌──────────────────────────────────────────┐ │
│ │                 Gửi                      │ │ h=50 bg accent
│ └──────────────────────────────────────────┘ │
└──────────────────────────────────────────────┘
```

**Layout Variants** *(bắt buộc: Medium density)*

**Variant A — Biến thể FR-060: vào từ nhánh "không hài lòng" của WF-030**
```
┌──────────────────────────────────────────────┐
│              ▬▬▬▬            [⧉]      [✕]    │
├──────────────────────────────────────────────┤
│  Có gì chưa ổn?                              │ headline ĐỔI
│  Cho chúng tôi biết để sửa.                   │
│ ┌──────────────────────────────────────────┐ │ ZONE B ĐƯỢC
│ │                                          │ │ NHẤN MẠNH:
│ │  (con trỏ ở đây, bàn phím mở sẵn)        │ │ textarea ~160pt,
│ │                                          │ │ lên TRƯỚC danh
│ │                                          │ │ sách dữ liệu
│ └──────────────────────────────────────────┘ │ (BR-060.2)
│  Dữ liệu kỹ thuật kèm theo (tuỳ chọn)   [v]  │ danh sách THU GỌN
│ ┌──────────────────────────────────────────┐ │
│ │                 Gửi                      │ │ VẪN bật dù không
│ └──────────────────────────────────────────┘ │ tick mục nào
│  ✗ KHÔNG có đường nào ra App Store            │ (VR-060.1,
└──────────────────────────────────────────────┘  BR-060.1)
```

**Variant B — Bỏ tick hết mọi mục (biến thể FR-032)**
```
┌──────────────────────────────────────────────┐
│  Dữ liệu sẽ được gửi                         │
│ ┌──────────────────────────────────────────┐ │
│ │ ○ Kích thước màn hình xe                 │ │ tất cả BỎ TICK
│ │ ○ Phiên bản iOS                          │ │
│ │ ○ Xe đã chọn                             │ │
│ │ ○ Nguyên nhân lỗi render                 │ │
│ └──────────────────────────────────────────┘ │
│  Ghi chú (tuỳ chọn) …                        │
│ ┌──────────────────────────────────────────┐ │
│ │                 Gửi                      │ │ VÔ HIỆU
│ └──────────────────────────────────────────┘ │ bg surfaceVariant
│  ⚠ Cần ít nhất kích thước màn hình xe để      │ lời nhắc cụ thể
│    chẩn đoán được.                            │ (VR-032.2)
└──────────────────────────────────────────────┘
```

**Components**
- `SheetContainer` — `detentLarge: 90%` (cần chỗ cho bàn phím).
- `RowDataDisclosureExpandable` ×4 — Tokens: `height: 50`, checkbox tint `${color.palette.accent}`; mở rộng 0,2s; giá trị thật `${typography.scale.monoData}`(13, mono) `${color.palette.textSecondary}`.
- `TFTextArea` — Tokens: `radius: 12`, `borderColor: ${color.palette.inputBorder}`, `focusColor: ${color.palette.focusRing}`, `font: ${typography.scale.body}`; đếm ký tự khi > 400.
- `IconButtonCopy` (⧉) — sao chép payload dạng chữ.
- `BtnPrimary` ("Gửi") — vô hiệu ở Variant B.
- `LabelNoPII` — Tokens: `font: ${typography.scale.footnote}`, `color: ${color.palette.textTertiary}`.

**States** (8)

| State | Loại | Context | Layout/Behavior |
|---|---|---|---|
| **First Visit** | user-context | Vào từ WF-014 sau lỗi render | Danh sách dữ liệu **đã điền sẵn**; người dùng chỉ cần chạm "Gửi" |
| **Returning** | user-context | Vào từ nhánh "không hài lòng" của WF-030 | **Variant A**: ô ghi chú được nhấn mạnh, lên trước danh sách; bàn phím mở sẵn |
| **Power User** | user-context | QA gửi báo cáo có chủ đích | Mở rộng từng mục xem giá trị thật; nút sao chép payload |
| **Error** | user-context | Bỏ tick hết mọi mục (biến thể FR-032) | **Variant B**: CTA vô hiệu + lời nhắc cần ít nhất kích thước màn hình |
| **Default** | data | Dữ liệu chẩn đoán sẵn sàng | Layout như trên |
| **Loading** | data | Đang ghi vào hàng chờ | CTA hiện spinner ≤ 500ms rồi đóng sheet — **không** chờ mạng |
| **Empty** | data | Chưa có dữ liệu chẩn đoán (vào từ WF-030) | Danh sách dữ liệu thu gọn và **rỗng**; gửi **vẫn được** vì nhánh FR-060 chỉ cần ghi chú (VR-060.1) |
| **Offline** | data | Không có mạng | Báo cáo **xếp hàng on-device**; **WF-030** toast vẫn xác nhận (ERR-032.2) |

**User Flow**
- **Entry**: nút "Gửi báo cáo" trên **WF-014** (biến thể FR-032) · nhánh "không hài lòng" từ **WF-030** (biến thể FR-060) · dòng "Đánh giá Carbina" trên **WF-012** khi người dùng chọn mức không hài lòng
- **Exit**: **WF-014** hoặc **WF-012** (trở về đúng nơi vào) · **WF-030** (toast xác nhận). **Không có exit nào ra App Store** (BR-060.1)
- **Task Flow**: bước 5–6 của **TF-003** · bước 5–6 của **TF-013**
- **Transitions**: sheet trượt lên 0,35s; mục mở rộng 0,2s; sheet đóng 0,3s rồi toast xuất hiện

---

### 3.29 WF-029 — Alert: Xoá Dữ Liệu On-Device 📱 · *Template B (Action)*

**Design System**: `bento-grid`
**Archetype**: Action | **Density**: Light (1 vùng)
**Source UC**: UC-032 | **Source FR**: **FR-057** (xoá dữ liệu học), **FR-058** (tách xoá học khỏi xoá cấu hình)
**User Intent**: "Tôi muốn xoá thứ app đã học về tôi, và muốn chắc mình không xoá luôn cấu hình đã dựng."

**Action Layer → Visual Hierarchy**

| UC Action Layer | Slot | Ghi chú |
|---|---|---|
| Layer 1 — Primary: xác nhận xoá **dữ liệu học** | **#3** | Lựa chọn mặc định, ở Zone B |
| Layer 2 — Contextual: "Huỷ" — không xoá gì | **#3** | Ngang hàng |
| Layer 3 — Discovery | — | **Trống có chủ ý** — alert cho hành động phá hủy chỉ được có **một câu hỏi** |
| Layer 4 — Personal: "Xoá cả cấu hình" — **tách riêng**, cần **một xác nhận nữa** | **#4** | Zone D, tách khỏi lựa chọn thứ nhất (BR-058.1) |

**Visual Hierarchy**
1. **Câu nêu rõ mất gì và giữ gì** — nội dung chính. "Mất: dữ liệu học ngữ cảnh. Giữ: widget, sound, gói của bạn."
2. — (không có)
3. **Hai nút** — "Huỷ" và "Xoá dữ liệu học".
4. **Dòng "Xoá cả cấu hình"** — tách riêng ở đáy, `${typography.scale.caption}`, cần xác nhận thứ hai.

*Self-check*: alert có một câu hỏi chính ⇒ đạt. Lựa chọn phá hủy mạnh hơn (xoá cả cấu hình) **tách riêng và cần thêm một bước** ⇒ đúng BR-058.1. Nút xoá **không** là nút mặc định của bàn phím ⇒ tránh xác nhận vô thức.

**Required Features (FR)**
- FR-057 P3: alert nêu rõ **mất gì** (dữ liệu học ngữ cảnh) và **giữ gì** (widget, sound, entitlement)
- FR-057 P2: hiển thị **số ngày dữ liệu sẽ mất** để người dùng biết cái giá
- FR-057 **BR-057.2**: xoá dữ liệu học **không bao giờ** ảnh hưởng entitlement
- FR-057 VR-057.1: chưa có dữ liệu học → nút xoá **bị vô hiệu** thay vì xoá một thứ không tồn tại
- FR-058 P1–P2 / **BR-058.1**: hai lựa chọn **tách biệt về thị giác và về số bước xác nhận**
- FR-058 **BR-058.2**: **cấm** xoá entitlement trong mọi biến thể
- FR-058 P6 / BR-058.3: xoá cấu hình có **"Hoàn tác" 5 giây** trên WF-030; xoá dữ liệu học thì không cần (nó tự học lại)
- FR-057 ERR-057.2: xoá thất bại một phần → nêu rõ phần nào chưa xoá + [Thử lại]; **cấm** báo "đã xoá xong" khi chưa xong

**UX Enhancements** (`composition.action.defaults`)
- `confirmation-dialog`: đây **là** hộp xác nhận; lựa chọn phá hủy hơn cần **hộp thứ hai**
- `escape-route-always-visible`: "Huỷ"
- `undo`: chỉ cho nhánh "Xoá cả cấu hình" — 5 giây trên WF-030
- **Không** nội dung khám phá, **không** ưu đãi giữ chân

**Content Zones Map**

```
┌─────────────────────────────────────┐
│ ZONE A: Context — mất gì / giữ gì   │ ← ~140pt
├─────────────────────────────────────┤
│ ZONE B: 2 nút                        │ ← 2×50pt
├─────────────────────────────────────┤
│ ZONE D: "Xoá cả cấu hình" tách riêng │ ← ~44pt
├─────────────────────────────────────┤
│ ZONE C: — (unused)                   │ ← 0
└─────────────────────────────────────┘
```

**Layout**

```
        ┌────────────────────────────────────┐   alert maxWidth 300
        │                                    │   r=20 p=20
        │  Xoá dữ liệu học?                  │   headline 17/600
        │                                    │
        │  SẼ MẤT                            │   caption warning
        │  · Thói quen nghe nhạc              │   callout
        │  · Tuyến đường quen                 │
        │  · Thứ tự thẻ dashboard đã học      │
        │  · 14 ngày dữ liệu                  │   mono cho SỐ
        │                                    │
        │  ĐƯỢC GIỮ                          │   caption success
        │  · Widget và âm thanh bạn đã tạo    │
        │  · Gói Premium của bạn              │   BR-057.2
        │                                    │
        │ ┌────────────────────────────────┐ │
        │ │            Huỷ                 │ │   BtnSecondary h=50
        │ └────────────────────────────────┘ │
        │ ┌────────────────────────────────┐ │
        │ │      Xoá dữ liệu học           │ │   BtnDestructive h=50
        │ └────────────────────────────────┘ │
        │ ────────────────────────────────── │   divider
        │  Xoá cả cấu hình widget và sound   │   ZONE D caption
        │  Cần xác nhận thêm một lần          │   TÁCH RIÊNG
        └────────────────────────────────────┘   (BR-058.1)
          shadow.elevation.5 · overlay rgba(0,0,0,0.4)
```

**Components**
- `AlertContainer` — như WF-027, cao hơn để chứa hai danh sách.
- `DataLossList` / `DataKeptList` — Tokens: header `${typography.scale.caption}`; "sẽ mất" `${color.semantic.warning.color}`; "được giữ" `${color.semantic.success.color}`; item `${typography.scale.callout}`; số ngày dùng mono.
- `BtnSecondary` ("Huỷ"), `BtnDestructiveOutline` ("Xoá dữ liệu học") — vô hiệu khi chưa có dữ liệu học.
- `RowSecondaryDestructive` ("Xoá cả cấu hình") — Tokens: `font: ${typography.scale.caption}`, `color: ${color.semantic.destructive.color}`, tách bằng `${component.divider}`; mở **alert thứ hai** khi chạm.

**States** (7)

| State | Loại | Context | Layout/Behavior |
|---|---|---|---|
| **First Visit** | user-context | Chưa có dữ liệu học | Nêu rõ **"chưa có dữ liệu học nào"**; nút xoá **vô hiệu** (VR-057.1) |
| **Returning** | user-context | Đã dùng vài tuần | Nêu **số ngày dữ liệu sẽ mất** để người dùng biết cái giá |
| **Power User** | user-context | Bán xe / đổi xe, muốn xoá sạch | Dùng dòng "Xoá cả cấu hình" ở Zone D, có **xác nhận thứ hai**; WF-030 cho "Hoàn tác" 5 giây |
| **Error** | user-context | Xoá thất bại một phần (ERR-057.2) | Nêu rõ **phần nào chưa xoá được** + [Thử lại]; **cấm** báo "đã xoá xong" |
| **Default** | data | Có dữ liệu học | Layout như trên |
| **Loading** | data | Đang xoá | Nút xoá hiện spinner; alert **không** tự đóng cho tới khi biết kết quả |
| **Empty** | data | Không áp dụng — trạng thái "chưa có dữ liệu" đã là First Visit | **Không tồn tại riêng có chủ ý** |

**User Flow**
- **Entry**: nút xoá trong mục "Quyền riêng tư & dữ liệu" trên **WF-012**
- **Exit**: **WF-012** · **WF-030** (toast xác nhận, kèm "Hoàn tác" 5 giây nếu xoá cả cấu hình)
- **Task Flow**: UC-032 **không có task flow riêng** (`Use_Cases.md` §5 ghi rõ: hành động một bước, không tạo thành hành trình xuyên màn hình)
- **Transitions**: fade-in 0,2s + scale 0,97→1,0; alert thứ hai (xoá cả cấu hình) thay thế alert thứ nhất bằng crossfade 0,2s

---

### 3.30 WF-030 — Overlay: Toast Xác Nhận 📱 · *Template C (Consumption)*

**Design System**: `bento-grid`
**Archetype**: Consumption | **Secondary**: Action | **Density**: Light (1–2 vùng)
**Source UC**: UC-033 (chính), UC-003, UC-007, UC-012, UC-017, UC-026, UC-032
**Source FR**: **FR-059** (mời đánh giá có điều kiện), **FR-058** ("Hoàn tác" 5 giây)
**User Intent**: "Tôi muốn biết việc tôi vừa làm đã xong, mà không bị chặn lại."

**Action Layer → Visual Hierarchy**

| UC Action Layer | Slot | Ghi chú |
|---|---|---|
| Layer 1 — Primary: **không có hành động bắt buộc** — overlay tự biến mất | **#1** | Biến thể xác nhận |
| Layer 2 — Contextual: chạm để đóng ngay · "Hoàn tác" (chỉ biến thể có thể hoàn tác) | **#3** | Nút inline |
| Layer 3 — Discovery | — | **Trống có chủ ý** ở biến thể xác nhận |
| Layer 4 — Personal: ở **biến thể mời đánh giá** — chọn mức hài lòng, dẫn App Store (hài lòng) hoặc **WF-028** (không hài lòng) | **#3** | Đây là biến thể duy nhất có hành động thật |

**Visual Hierarchy**
1. **Một dòng nói việc gì đã xong** — nội dung duy nhất ở biến thể xác nhận.
2. — (không có)
3. **Nút "Hoàn tác"** (biến thể hoàn tác) hoặc **bộ chọn mức hài lòng** (biến thể mời đánh giá).
4. **Chrome**: nút đóng một chạm.

*Self-check*: overlay **không chặn** tác vụ đang làm ⇒ đúng AC-033.4. Đóng bằng **một chạm** ⇒ đạt. Toast mới **thay** toast cũ, không xếp chồng ⇒ đúng State "Power User".

**Required Features (FR)**
- FR-059 P1: kiểm **ba điều kiện** — `sound_played` thành công ≥ 5 lần **và** không có `widget_render_failed` trong 7 ngày **và** lần mời gần nhất bị đóng ≥ 30 ngày
- FR-059 P3–P6: overlay nhẹ, đóng **một chạm**, **không chặn**; hài lòng → dialog đánh giá iOS; **không hài lòng → WF-028**, **không** mở App Store
- FR-059 **BR-059.1**: **cấm** mời đánh giá khi có `widget_render_failed` trong 7 ngày gần nhất
- FR-059 P7: đóng → **không** hiện lại trong ≥ 30 ngày
- FR-058 P6: "Hoàn tác" 5 giây cho nhánh xoá cả cấu hình
- FR-006 P3 / FR-032 P8: toast xác nhận trong ≤ 500ms, **không chờ mạng**
- FR-032 ERR-032.2 / FR-006 ERR-006.1: offline → toast vẫn xác nhận đã ghi nhận

**UX Enhancements** (`composition.consumption.defaults`)
- `no-modal`: overlay **không** phải modal — không có overlay màu, không chặn tương tác phía sau
- Toast xác nhận tự đóng **2s**; toast lỗi tồn **4s** để người dùng đọc kịp
- Toast mới **thay** toast cũ — không xếp chồng
- Biến thể mời đánh giá **không** tự đóng (cần người dùng chọn hoặc đóng)

**Content Zones Map**

```
┌─────────────────────────────────────┐
│ ZONE A: Hero — một dòng nội dung    │ ← ~50pt (biến thể xác nhận)
├─────────────────────────────────────┤
│ ZONE B: Key Info + CTA              │ ← "Hoàn tác" / mức hài lòng
├─────────────────────────────────────┤
│ ZONE C / ZONE D: — (unused)         │ ← 0
└─────────────────────────────────────┘
   Vị trí: .safeAreaInset(edge: .bottom), trên tab bar
```

**Layout** — *biến thể xác nhận (mặc định)*

```
        ┌────────────────────────────────────┐   toast minHeight 50
        │  ✓  Đã lưu widget                  │   r=16 p=16
        │     callout 16/400 textPrimary      │   shadow.4
        └────────────────────────────────────┘   bg surfaceElevated
          tự đóng sau 2s · chạm để đóng ngay
          KHÔNG chặn tương tác phía sau
```

**Layout Variants** — *ba biến thể chức năng, đặc tả dù Light density*

**Variant A — Có "Hoàn tác" (sau khi xoá cả cấu hình)**
```
        ┌────────────────────────────────────┐
        │  ✓  Đã xoá cấu hình      [Hoàn tác]│   nút inline
        │     callout                accent   │   5 giây
        └────────────────────────────────────┘
          tự đóng sau 5s (dài hơn mặc định vì
          đây là hành động tốn công dựng lại)
```

**Variant B — Biến thể mời đánh giá (FR-059)**
```
        ┌────────────────────────────────────┐   ~120pt
        │  Carbina đang chạy ổn chứ?    [✕]  │   headline
        │                                    │
        │  ┌──────────┐    ┌──────────┐      │
        │  │   👍     │    │   👎     │      │   2 nút 50pt
        │  │  Tốt     │    │ Chưa ổn  │      │
        │  └──────────┘    └──────────┘      │
        └────────────────────────────────────┘
          👍 → dialog đánh giá App Store của iOS
          👎 → WF-028 (KHÔNG ra App Store · BR-060.1)
          KHÔNG tự đóng · đóng bằng 1 chạm [✕]
          ✗ BỊ CHẶN nếu có widget_render_failed trong 7 ngày
```

**Variant C — Toast lỗi (tồn lâu hơn)**
```
        ┌────────────────────────────────────┐
        │  ⚠  Không lưu được widget  [Thử lại]│   semantic.error
        │     Ghi App Group thất bại          │   caption
        └────────────────────────────────────┘
          tự đóng sau 4s (dài hơn để đọc kịp)
```

**Components**
- `ToastOverlay` — Tokens: `${component.toast}`: `minHeight: 50`, `radius: 16`, `background: ${color.palette.surfaceElevated}`, `shadow: ${shadow.elevation.4}`, `font: ${typography.scale.callout}`, `durationDefault: 2000`, `durationError: 4000`, `paddingH: 16`. **Không** overlay màu, **không** chặn tương tác phía sau.
- `BtnInlineUndo` ("Hoàn tác") — Tokens: `foreground: ${color.palette.accent}`, `font: ${typography.scale.button}`; hiện 5 giây.
- `SatisfactionPicker` (Variant B) — Tokens: 2 nút `height: 50`, `radius: 16`, chia đôi chiều ngang; 👍 `BtnSecondary`, 👎 `BtnSecondary`. **Không** có nút nào dẫn App Store trực tiếp — nhánh được quyết bởi lựa chọn.
- `BtnInlineRetry` ("Thử lại") — Variant C.

**States** (8)

| State | Loại | Context | Layout/Behavior |
|---|---|---|---|
| **First Visit (xác nhận)** | user-context | Vừa lưu một thay đổi | Một dòng, tự đóng sau 2s, **không chặn** tác vụ đang làm |
| **Returning (mời đánh giá)** | user-context | `sound_played` ≥ 5 lần, không lỗi render 7 ngày, ≥ 30 ngày từ lần đóng | **Variant B**: bộ chọn mức hài lòng; **không** tự đóng |
| **Power User** | user-context | Thực hiện nhiều tác vụ liên tiếp | Toast mới **thay** toast cũ, **không** xếp chồng |
| **Bị chặn có chủ ý** | user-context | Có `widget_render_failed` trong 7 ngày gần nhất | **Không** hiện biến thể mời đánh giá — mời đánh giá ngay sau khi app vừa lỗi là cách nhanh nhất để nhận 1★ (BR-059.1) |
| **Error** | user-context | Tác vụ thất bại | **Variant C**: trạng thái thất bại + lý do, tồn **4s**, có [Thử lại] nếu áp dụng được |
| **Default** | data | Tác vụ thành công | Layout mặc định |
| **Loading** | data | Không áp dụng — toast chỉ xuất hiện **sau khi** tác vụ kết thúc | **Không tồn tại có chủ ý** |
| **Offline** | data | Gửi request khi không có mạng | Toast vẫn xác nhận **"đã ghi nhận"** trong ≤ 500ms; người dùng **không cần biết** chuyện mạng (ERR-006.1) |

**User Flow**
- **Entry**: hoàn tất tác vụ ở **WF-003** (báo thiếu xe) · **WF-007**/**WF-020** (gán sound) · **WF-008** (lưu widget) · **WF-011** (mua thành công) · **WF-021** (gửi yêu cầu xe) · **WF-028** (gửi báo cáo) · **WF-029** (xoá dữ liệu) · hệ thống kích hoạt biến thể mời đánh giá sau chuỗi tích cực · dòng "Đánh giá Carbina" trên **WF-012**
- **Exit**: tự đóng 2s (xác nhận) / 4s (lỗi) · dialog đánh giá App Store của iOS (hài lòng) · **WF-028** (không hài lòng) · màn hình trước đó
- **Task Flow**: bước 2–6 của **TF-013** · toast xác nhận ở **TF-001** bước 3a, **TF-004** bước 8, **TF-005** bước 3, **TF-007** bước 7, **TF-003** bước 6
- **Transitions**: trượt lên từ mép dưới 0,25s; fade-out 0,2s; biến thể mời đánh giá fade-in 0,3s

---

## 4. Common Components

Đặc tả triển khai SwiftUI của từng component nằm ở **`ios-components` skill** — **không** nhân bản catalog ở đây. Bảng dưới đây chỉ ánh xạ component → token của `bento-grid` và → màn hình dùng nó.

### 4.1 Navigation

| Component | Token chính | Dùng ở |
|---|---|---|
| `NavBarStandard` | `${component.navBar}`: h=44, bg rgba(242,243,240,0.85), blur 20, divider `${color.palette.border}`, title `${typography.scale.headline}`, icon 20pt medium | WF-003, 004, 005, 006, 007, 008, 009, 011, 012, 014 |
| `NavBarModal` | h=44, `[✕]` 20pt, **không** divider | WF-010, 013, 015 |
| `TabBarCustom` | `${component.tabBar}`: h=49 (+34 safe), bg rgba(255,255,255,0.92), blur 20, active `${color.palette.accent}`, inactive `${color.palette.textTertiary}`, icon 24pt, label `${typography.scale.footnote}`, 4 tab | WF-006, 012 |
| `SheetContainer` | `${component.sheet}`: r=20, dragIndicator 36×5, overlay rgba(0,0,0,0.4), bg `${color.palette.surfaceElevated}`, shadow.3 | WF-020, 021, 022, 024, 025, 026, 028 |
| `ModalFullContainer` | r=20, detentLarge 90%, shadow.3 | WF-023 |
| `AlertContainer` | `${component.alert}`: r=20, maxWidth 300, p=20, shadow.5 | WF-027, 029 |

> **Không dùng** giao diện mặc định của `NavigationStack`/`TabView`/`.sheet`. Ba API đó chỉ là **kỹ thuật triển khai**; mọi giá trị thị giác đến từ token.

### 4.2 Core UI Elements

| Component | Token chính | Dùng ở |
|---|---|---|
| `BtnPrimary` | `${component.button.primary}`: h=50, r=16, bg `${color.palette.accent}`, fg `${color.palette.onAccent}`, **shadow.0**, font `${typography.scale.button}`. Vô hiệu: bg `${color.palette.surfaceVariant}`, fg `${color.palette.textTertiary}` | 14 màn |
| `BtnSecondary` | h=50, r=16, bg `${color.palette.surface}`, border 1px `${color.palette.border}` | WF-005, 013, 022, 023, 027, 029, 030 |
| `BtnTertiary` | h=44, r=12, bg transparent, fg `${color.palette.accent}` | 12 màn |
| `BtnDestructiveOutline` | h=50, r=16, bg transparent, fg + border `${color.semantic.destructive.color}` | WF-013, 025, 027, 029 |
| `TFField` / `TFSearch` / `TFTextArea` | `${component.textField}`: h=50, r=12, border `${color.palette.inputBorder}`, focus `${color.palette.focusRing}`, error `${color.semantic.error.color}` | WF-003, 021, 028 |
| `RowNavigable` / `RowSelectable` / `RowToggle` / `RowSliderVolume` | `${component.row}`: h=50 (68 khi có subtitle), paddingH 16, chevron 14pt, divider inset 16 | WF-003, 004, 007, 008, 012, 015, 026, 028 |
| `CardConnectionStatus` / `CardWidgetPreview` / `CardCompactStatus` / `PermissionCard` / `PriceTierCard` | `${component.card}`: r=16, p=16, bg `${color.palette.surface}`, border 1px, shadow.1; hero 200pt, compact 88pt | WF-005, 006, 008, 010, 011, 014, 025 |
| `SegmentedControl3` / `SegmentedControl2` | `${component.segmentedControl}`: h=36, r=12, bg `${color.palette.surfaceVariant}`, selected `${color.palette.surface}` | WF-007, 012, 020, 023 |
| `ChipSegment` / `ChipFilter` / `ChipToggleLayer` | `${component.chip}`: h=32, r=full, paddingH 12, selected bg `${color.palette.accent}` | WF-021, 023, 024 |
| `ProgressBarOnboard` | `${component.progressBar}`: h=4, r=full, active `${color.palette.accent}` | WF-002, 003, 004, 005 |
| `StatusBadge` / `LockLabel` | `${component.statusBadge}`: h=24, r=full, paddingH 10, font `${typography.scale.footnote}` | WF-004, 006, 007, 008, 012 |
| `WaveformLive` | `${component.waveform}`: h=40, bar 3px, gap 2px, active `${color.palette.accent}` — **chạy theo tiến độ audio thật** | WF-004, 007, 020 |

### 4.3 Feedback Components

| Component | Token chính | Dùng ở |
|---|---|---|
| `ToastOverlay` | `${component.toast}`: minH=50, r=16, bg `${color.palette.surfaceElevated}`, shadow.4, default 2000ms, error 4000ms | WF-030 (dùng bởi 8 màn) |
| `WarningRow` | h=50, bg `${color.semantic.warning.background}`, fg `${color.semantic.warning.color}`, slide-in 0,3s / fade-out **0,4s** | WF-006 |
| `CardErrorInline` / `OverflowWarningBanner` / `ResolutionWarningBanner` / `PermissionInfoBanner` / `VersionNotice` / `LimitNotice` / `DoubleChargeWarning` | r=16 + cặp màu semantic tương ứng (`error` / `warning` / `info` / `accentSubtle`) | WF-005, 007, 008, 010, 020, 023, 024, 025 |
| `CarPlayFallbackNotice` | `${component.carplayCard}` + `${color.semantic.warning}`, **shadow.0**, **không** gesture recognizer | WF-019 |
| `DelayedSpinner` | tint `${color.palette.accent}`, chỉ hiện nếu > 1s | WF-001 |
| `PullToRefreshIndicator` | tint `${color.palette.accent}`, fade-in 0,15s | WF-006, 014 |

**Component riêng của bề mặt CarPlay** (biến thể `composition.carplay`, **shadow.0 tuyệt đối**):
`CarPlayPriorityCard` · `CarPlayActionCard` · `CarPlayCardError` · `CarPlayCardLocked` · `CarPlayEdgeStatus` · `CarPlayStaticUpsellLine` · `CarPlayWidgetSurface` · `WidgetImageLayer` · `WidgetScrim` · `WidgetInfoLayer` · `CarPlayFallbackNotice`.

---

## 5. Responsive Design

### 5.1 Device Support

| Thiết bị | Chiều rộng | Trạng thái | Ghi chú |
|---|---|---|---|
| iPhone SE (gen 3) | 375pt | **Không hỗ trợ** | Thiếu Apple Neural Engine ⇒ ngoài danh sách hỗ trợ (AC-NFR-022.4) |
| iPhone 12 / 13 / 14 | 390pt | **Chuẩn** | Thiết bị đo mọi ngưỡng hiệu năng (NFR-001, NFR-005, NFR-006) |
| iPhone 14/15/16 Plus · Pro Max | 428–440pt | Hỗ trợ | Card hero giãn theo chiều ngang; số cột không đổi |
| iPad Air 5 / iPad Pro | 768pt+ | Tùy chọn | PRD §9 ghi "optional"; MVP 1 dùng layout iPhone giãn, **không** có layout iPad riêng |
| **Màn hình CarPlay** | **không biết trước** | **Bắt buộc** | Đây là ràng buộc chi phối: layout tính từ scene bounds tại runtime, test matrix ≥ 4 kích thước + ≥ 1 xe thật/nhóm (NFR-021) |

### 5.2 Orientation

- **iPhone**: Portrait là chính. Landscape hỗ trợ ở WF-023 (preview widget) vì tỉ lệ màn hình xe thường là ngang — xem widget ở landscape gần với thực tế hơn.
- **CarPlay**: theo hướng của màn hình xe, **không** do app quyết định. Layout không giả định tỉ lệ nào.
- Không màn hình nào **yêu cầu** landscape để dùng được.

### 5.3 Adaptive Layout

- **iPhone**: `spacing` từ token; card giãn theo chiều ngang, chiều cao cố định theo `${component.card.heroHeight}` / `compactHeight`. Safe area luôn tôn trọng; chỉ WF-001 dùng `.ignoresSafeArea()`.
- **CarPlay**: **mọi kích thước là tỉ lệ theo scene bounds**, `safeAreaInsetRatio: 0.06`. Số pt trong ASCII của WF-016 → WF-019 là **ví dụ ở 1180×420**, không phải giá trị hardcode (BR-029.1).
- **Dynamic Type**: iPhone tới 1,6×; CarPlay giới hạn 1,35× (`typography.dynamicType.carplayMaxScale`) — vượt mức đó thì layout cần giảm cấp (FR-030) ở phần lớn kích thước trong test matrix.
- **Giảm cấp có thứ tự**: khi thiếu chỗ, bỏ phần tử ưu tiên thấp nhất → co chữ theo Dynamic Type → truncate có ellipsis, tối đa 3 vòng (FR-030). Chữ **không bao giờ** dưới 16pt trên màn hình xe.
- **Kiểm bằng property-based test**: với **mọi** cặp (width, height) trong dải hợp lệ, không phần tử nào vượt bounds (AC-NFR-024.3) — đây là cách kiểm R-11 không phụ thuộc danh sách xe.

---

## 6. Accessibility

### 6.1 VoiceOver

- Mọi phần tử tương tác có nhãn **mô tả hành động**, không phải "Button": ví dụ `"Dùng cho lúc lên xe, sound Tiếng Máy Ấm"`, không phải `"Chọn"`.
- `WaveformLive` là **decorative** — bị ẩn khỏi VoiceOver; trạng thái phát được thông báo qua nhãn của dòng preset.
- `CardPriceConfirm` (WF-011) đọc **liền mạch một câu**: bậc giá, số tiền, ngày hết trial, ngày trừ tiền — để người dùng VoiceOver không phải ghép bốn ô rời.
- 4 màn CarPlay: nhãn ngắn, ưu tiên nội dung trước trang trí; `CarPlayEdgeStatus` và `CarPlayStaticUpsellLine` là `.isStaticText`, **không** phải button.
- **Ngưỡng đạt**: Accessibility Inspector 0 lỗi mức error trên WF-002, WF-006, WF-007, WF-008, WF-010 (AC-NFR-014.1).

### 6.2 Dynamic Type

- Mọi chữ dùng `${typography.scale.*}` và co giãn theo cài đặt hệ thống.
- **iPhone**: tới 1,6×; không có chữ nào bị cắt giữa chữ ở mức lớn nhất (AC-NFR-014.2).
- **CarPlay**: tới 1,35×; sàn tuyệt đối **16pt** (`${typography.scale.carplayMin}`, BR-030.2).
- Số dùng `${typography.family.mono}` — chiều rộng ký tự ổn định nên số **không nhảy** khi giá trị đổi.
- Layout thích ứng: `PermissionCard` (WF-005) và `RowToggleContext` (WF-009) chuyển từ một hàng sang hai hàng ở mức Dynamic Type lớn.

### 6.3 Color Contrast

| Cặp màu | Tỉ lệ | Ngưỡng | Kết quả |
|---|---|---|---|
| `onAccent` `#111111` trên `accent` `#FF8400` | ~7,4:1 | 4,5:1 | **Pass** — đây là lý do màu nhấn dùng chữ tối, không dùng chữ trắng |
| `textPrimary` `#111111` trên `background` `#F2F3F0` | ~15,8:1 | 4,5:1 | Pass |
| `textPrimary` `#FFFFFF` trên `background` `#111111` (dark) | ~18,9:1 | 4,5:1 | Pass |
| `textSecondary` `#666666` trên `surface` `#FFFFFF` | ~5,7:1 | 4,5:1 | Pass |
| `textTertiary` `#9E9E9E` trên `surface` `#FFFFFF` | ~2,8:1 | 3:1 (non-text) | **Chỉ dùng cho chữ trang trí và chỉ báo**, không dùng cho chữ mang thông tin |
| Chữ trên ảnh widget (WF-017) | phụ thuộc ảnh | 4,5:1 ở **cả** hai mode | Áp `${color.overlayScrim}` khi không đạt — **bắt buộc** (AC-NFR-014.4) |

- High Contrast mode: viền card chuyển từ `border` sang `borderStrong`; `textTertiary` chuyển sang `textSecondary`.

### 6.4 Touch Targets

- Tối thiểu **44pt** ở mọi bề mặt (AC-NFR-014.3); khuyến nghị 50pt cho CTA — `${component.button.primary.height}` = 50.
- Row 50pt, `BtnTertiary` 44pt, `ChipSegment` 32pt **nhưng vùng chạm mở rộng lên 44pt** bằng padding trong suốt.
- `CarPlayPriorityCard` / `CarPlayActionCard`: vùng chạm là **toàn bộ thẻ**, luôn ≥ 44pt vì tính theo tỉ lệ bounds.
- Khoảng cách giữa hai target liền kề ≥ `${spacing.sm}` (8pt); ba nút của WF-013 cách nhau `${spacing.md}` (12pt) để không chạm nhầm nút huỷ.

---

## 7. Dark Mode

`bento-grid` có **đủ cặp light/dark** cho mọi token màu — đây là một trong ba lý do chọn hệ này (điều kiện cứng của AC-015.4).

| Yếu tố | Light | Dark | Ghi chú |
|---|---|---|---|
| Nền màn hình | `#F2F3F0` | `#111111` | Không phải đen thuần — giữ độ sâu cho card |
| Bề mặt card | `#FFFFFF` | `#1A1A1A` | Tương phản với nền ở cả hai mode |
| Viền card | `#CBCCC9` | `#2E2E2E` | **Card Bento có cả viền và shadow** — vì shadow gần như vô hình ở dark mode, viền là thứ giữ ranh giới |
| Màu nhấn | `#FF8400` | `#FF8400` | **Không đổi** — nhận diện thương hiệu giữ nguyên ở cả hai mode |
| Shadow | 5% `#1A1A1A` | 5% `#1A1A1A` | Giữ nguyên opacity; ở dark mode gần như vô hình và đó là lý do có viền |
| Scrim widget | `rgba(0,0,0,0.35)` | `rgba(0,0,0,0.45)` | Dark mode cần scrim đậm hơn vì ảnh xe thường sáng hơn nền |

- **Nguồn mode**: theo hệ thống, hoặc theo `appTheme` do người dùng chọn ở WF-012 (FR-061). Widget CarPlay dùng **cùng** theme với app — hai bề mặt **không được lệch** (BR-061.1).
- Mọi màu qua token semantic; **không** hardcode hex trong code layout.
- WF-023 có công tắc Sáng/Tối để người dùng kiểm widget ở **cả hai mode trước khi ra xe**.

---

## 8. Design Assets

### 8.1 Icons

- **SF Symbols** cho icon hệ thống: `chevron.left`(20pt medium) · `gearshape`(20pt) · `play.fill`/`pause.fill` · `lock.fill` · `checkmark` · `exclamationmark.triangle.fill` · `doc.on.doc`(sao chép) · `magnifyingglass` · `speaker.wave.2.fill` · `arrow.clockwise`.
- **Icon tab bar** (24pt): `house` · `music.note` · `square.grid.2x2` · `gearshape`.
- Icon tuỳ chỉnh (nếu cần): 24×24pt, stroke 1pt, có biến thể light/dark trong asset catalog.
- **App icon**: sinh bằng `ios-icon-gen` skill ở giai đoạn thi công; **chưa** thuộc phạm vi tài liệu này.

### 8.2 Images

- **Ảnh xe theo model**: ≥ 2 biến thể độ phân giải mỗi model (FR-005); biến thể lớn nhất phải đủ cho màn hình xe lớn nhất trong test matrix.
- **Ảnh silhouette theo phân khúc**: 6 phân khúc (sedan/SUV/pickup/hatchback/van/coupe) — đường lui bắt buộc, **không bao giờ** để trống vùng ảnh (BR-005.1).
- **Ảnh cá nhân**: nén xuống **≤ 2MB** trước khi ghi App Group (VR-028.1); crop theo tỉ lệ màn hình xe.
- @2x và @3x cho mọi asset iPhone; lazy loading cho hàng cuộn ngang (WF-008, WF-024).
- **Widget extension không nạp ảnh chưa giảm kích thước** — đây là điều kiện của NFR-007 (≤ 25MB).

### 8.3 Animations

| Chuyển động | Giá trị | Dùng ở |
|---|---|---|
| Crossfade chuẩn | `${animation.duration.normal}` 0,25s | Đổi preview widget, đổi theme, cập nhật thẻ trạng thái |
| Spring mượt | `${animation.spring.smooth}` 0,4s damping 0,7 | Push màn hình, sheet trượt lên (0,35s) |
| Spring chặt | `${animation.spring.stiff}` 0,3s damping 0,9 | Khung preview đổi kích thước (SF-009) — damping cao để **không nảy** |
| Micro | `${animation.duration.fast}` 0,15s | Icon đổi trạng thái, chỉ báo tải fade-in |
| **CarPlay crossfade** | **0,4s, throttle 30s** | Thẻ đổi thứ tự (SF-017) — **cố ý chậm hơn iPhone** |
| Toggle nảy về tắt | 0,2s | SF-012 — truyền đạt "điều kiện chưa đủ" |
| Cảnh báo tự thu hồi | fade-out **0,4s** | `WarningRow` — chậm hơn lúc vào (0,3s) để người dùng kịp nhận ra nó đã hết |

- **Haptics**: `light` khi chọn/phát · `medium` khi hoàn tất (gán sound, lưu widget, mua) · `heavy` **không dùng** · **CarPlay: none**.
- **Cấm trên CarPlay**: positional-move · scale · bounce · blink (`animation.carplay.forbidden`).

### 8.4 SwiftUI Style Files

Ánh xạ token → file style ở giai đoạn thi công (`Project_Overview.md` §3.3 Quyết định 7):

| Token nhóm | File |
|---|---|
| `color.palette` + `color.semantic` | `shared/Styles/AppColors.swift` |
| `typography.family` + `typography.scale` | `shared/Styles/AppFonts.swift` |
| `spacing` + `border.radius` | `shared/Styles/AppSpacing.swift` |
| `shadow.elevation` | `shared/Styles/AppShadows.swift` |
| `animation` (gồm biến thể `carplay`) | `shared/Styles/AppMotion.swift` |
| `component.*` | `shared/Components/[Type]/` theo bảng ở §4 |
| `composition.carplay` | `Core/CarPlay/CarPlayLayoutTokens.swift` — **nơi duy nhất** được biết về tỉ lệ bounds |

---

## 9. Figma Integration

**Trạng thái: (chưa tạo).** Không có Figma file cho dự án này. Wireframe trong tài liệu này **là nguồn chân lý** cho layout, đúng theo bảng fallback ở §1.4.

- **Design Tokens**: nguồn thật là [`.claude/design-token/template-bento.pen`](../../design-token/template-bento.pen) (Pencil, 77 biến + `themes.Mode`) → đã trích sang [`.claude/shared/DESIGN_TOKEN_BENTO_GRID.json`](../../shared/DESIGN_TOKEN_BENTO_GRID.json).
- **Component Library**: chưa có; bảng §4 là đặc tả tạm cho tới khi có.
- **Screen Specs**: chưa có; §3 là đặc tả.
- **Nếu về sau dùng Figma**: dùng `mcp-figma` skill để trích token và layout context, rồi ánh xạ về đúng các file style ở §8.4 **trước khi** thi công. Nếu giá trị Figma lệch với token file, **token file thắng** — vì nó trích từ design system thật của project.

---

## 10. Affordance → FR Back-Trace Audit *(BLOCKING)*

Mọi Component và Interaction của cả 30 màn hình được back-trace về một FR có AC. Ba trạng thái theo skill: **✓ backed** · **✓ deferred** (out-of-scope, có chủ sở hữu) · **✗ GAP** (phải sửa upstream trước khi pass).

### 10.1 Nhóm chrome điều hướng — khai out-of-scope tường minh

| Affordance | Trạng thái | Chủ sở hữu |
|---|---|---|
| Tab bar 4 tab (Home · Sounds · Widget · Cài đặt) | ✓ deferred | `Use_Cases.md` §0.3 Screen Architecture Canvas (hợp đồng ràng buộc cây màn hình, theo quy tắc 12 của skill) + `UX_Flows.md` Step 6 (sở hữu đường điều hướng) |
| Nút back `[<]` trên mọi màn con | ✓ deferred | `UX_Flows.md` Step 6 |
| Nút đóng `[✕]` trên mọi sheet/modal | ✓ deferred | `UX_Flows.md` Step 6 |
| Drag indicator trên mọi sheet | ✓ deferred | `UX_Flows.md` Step 6 |
| Lối tắt `⚙` trên WF-006 → WF-012 | ✓ deferred | `UX_Flows.md` Step 6 (đường thứ hai tới cùng đích của tab Cài đặt) |
| Chuyển tab / push / pop giữa các màn | ✓ deferred | `UX_Flows.md` Step 6 |

> Đây là **nhóm duy nhất** được khai out-of-scope, và lý do là hợp lệ: điều hướng là domain của `UX_Flows.md` theo Boundary Contract của `project-docs-contract`. Mọi affordance **không** thuộc bảng này đều phải có FR.

### 10.2 Back-trace theo màn hình

| WF | Component / Interaction | → FR (AC) |
|---|---|---|
| **001** | `SplashBrandMark`, định tuyến khởi động | FR-009 (AC-001.1, AC-NFR-001.1) ✓ |
| **001** | `DelayedSpinner` (chỉ > 1s) | FR-009 (AC-NFR-001.2) ✓ |
| **002** | `OnboardHeroIllustration`, câu tuyên bố | FR-001 (AC-001.1) ✓ |
| **002** | `BtnPrimary` "Bắt đầu" | FR-001 (AC-001.2, AC-001.4) ✓ |
| **002** | `BtnTertiary` "Phục hồi giao dịch" | FR-003 (AC-029.5, AC-030.4) ✓ |
| **002** | `ProgressBarOnboard` 1/4 | FR-001 (AC-001.5) ✓ |
| **003** | `TFSearch` + lọc ≤ 200ms | FR-004 (AC-002.5), VR-004.1 ✓ |
| **003** | `PickerCascade` 3 tầng + `PinnedTierRow` | FR-004 (AC-002.1, AC-002.2) ✓ |
| **003** | `CardVehiclePhoto` + fallback silhouette | FR-005 (AC-002.3, AC-002.4) ✓ |
| **003** | `BtnPrimary` "Đúng xe của tôi" | FR-004 (AC-002.2) ✓ |
| **003** | `BtnTertiary` "Không tìm thấy xe của tôi" | FR-006 (AC-003.1) ✓ |
| **003** | `BtnTertiary` "Bỏ qua bước này" | FR-002 (AC-001.3), BR-002.1 ✓ |
| **003** | Nhắc "trim/color thuộc MVP 3" | FR-004 (AC-002.6) ✓ |
| **004** | `AutoPlayOnAppear` (tự phát preset đầu) | FR-012 (AC-006.4), SF-014 ✓ |
| **004** | `WaveformLive` | FR-011 (AC-006.1) ✓ |
| **004** | `RowSoundPreset` + `LockLabel` | FR-010 (AC-006.2, AC-006.3) ✓ |
| **004** | Chạm dòng khác dừng ngay dòng cũ | FR-011 (AC-006.5) ✓ |
| **004** | `BtnPrimary` "Dùng sound này" | FR-013 (AC-007.1) ✓ |
| **004** | `BtnTertiary` "Chọn sau" | FR-013 (AC-007.2), BR-013.2 ✓ |
| **004** | Dòng "trên xe phát qua loa xe" (khi cắm tai nghe) | FR-011 ERR-011.3, FR-020 (AC-011.2) ✓ |
| **005** | `PermissionCard` ×2 + lý do cụ thể | FR-007 (AC-004.1) ✓ |
| **005** | `ExampleChip` (ví dụ câu chào) | FR-007 (AC-004.1) ✓ |
| **005** | `BtnSecondary` "Cho phép" / "Mở Cài đặt" | FR-007 (AC-004.2, AC-004.3) ✓ |
| **005** | `BtnTertiary` "Tìm hiểu thêm" → WF-022 | FR-007 P3 (AC-004.1) ✓ |
| **005** | `BtnTertiary` "Bỏ qua tất cả" | FR-007 BR-007.3 (AC-004.5) ✓ |
| **005** | Dòng "tính năng nào bị ảnh hưởng" | FR-007 (AC-004.4), FR-008 (AC-005.1) ✓ |
| **006** | `CardConnectionStatus` (hero) | FR-009 (AC-001.1), FR-031 (AC-016.3) ✓ |
| **006** | `CardWidgetPreview` + chạm để đổi | FR-021 (AC-012.1) ✓ |
| **006** | `CardCompactStatus` sound | FR-014 (AC-008.1) ✓ |
| **006** | `CardCompactStatus` giọng chào (`StatusRow` chỉ đọc) | FR-033 (AC-018.1), BR-033.3 ✓ |
| **006** | Thẻ xe + "đổi" → WF-003 | FR-004 P6 (AC-002.2) ✓ |
| **006** | `CardSuggestion` (thẻ gợi ý tính năng chưa dùng) | FR-044 (AC-024.3), FR-036 (AC-020.1) ✓ |
| **006** | `WarningRow` + tự xoá | FR-031 (AC-016.3, AC-016.4) ✓ |
| **006** | `StatusBadge` gói / "Trial còn N ngày" | FR-044 (AC-024.2), FR-051 (AC-027.2) ✓ |
| **006** | Pull-to-refresh (SF-001) | FR-009 P5 (AC-001.1) ✓ |
| **006** | `StaticNotice` mời cấp quyền (tối đa 1, tĩnh) | FR-008 (AC-005.3) ✓ |
| **006** | Thẻ "Hoàn tất thiết lập" (bỏ dở onboarding) | FR-002 (AC-001.3) ✓ |
| **007** | `SegmentedControl3` 3 sự kiện, giữ vị trí cuộn | FR-014 (AC-008.1), SF-006 ✓ |
| **007** | Nghe inline + `WaveformLive` | FR-011 (AC-006.1, AC-006.5) ✓ |
| **007** | `RowSoundPreset` + `LockLabel` + ghim "đang dùng" | FR-010 (AC-006.2, AC-006.3) ✓ |
| **007** | `BtnPrimary` nhãn động (3 sự kiện) | FR-013 (AC-007.1), FR-014 (AC-008.1) ✓ |
| **007** | `BtnTertiary` "Không dùng sound cho sự kiện này" | FR-013 (AC-007.2) ✓ |
| **007** | `IconButtonVolume` 🔊 → WF-012 | FR-015 P1 (AC-009.1) ✓ |
| **007** | `CardPermissionInline` (Arrive thiếu quyền) + CTA cấp quyền | FR-014 (AC-008.2), FR-007 (AC-004.2) ✓ |
| **008** | `PresetCarousel` + `CardPresetWidget` (≥3 gợi ý) | FR-021 (AC-012.1) ✓ |
| **008** | `CardWidgetPreviewLive` (preview nhúng) | FR-025 (AC-013.4) ✓ |
| **008** | `RowSelectable` loại widget + `LockLabel` | FR-021 (AC-012.6), FR-023 (AC-012.3) ✓ |
| **008** | `RowImageSlot` → WF-024 | FR-027 (AC-014.1) ✓ |
| **008** | `RowToggle` lớp thông tin (bật/tắt) | FR-026 (AC-013.3) ✓ |
| **008** | `BtnPrimary` "Lưu widget" / "Lưu thay đổi" | FR-022 (AC-012.2) ✓ |
| **008** | `BtnTertiary` "Xem trước trên xe của tôi" → WF-023 | FR-025 (AC-013.1, AC-013.2) ✓ |
| **008** | `LimitNotice` + "Thêm widget thứ hai" | FR-023 (AC-012.3), FR-045 (AC-024.4) ✓ |
| **008** | `VersionNotice` iOS < 17.4 | FR-024 (AC-012.4) ✓ |
| **008** | Nhắc bản nháp "Tiếp tục widget đang làm?" | FR-021 ERR-021.2 (AC-012.1) ✓ |
| **009** | `RowToggleMain` công tắc chính | FR-033 (AC-018.1, AC-018.2, AC-018.3) ✓ |
| **009** | `CardGreetingProof` (chữ câu chào + nguồn) | FR-036 (AC-020.3) ✓ |
| **009** | `BtnPrimary` "Nghe thử" | FR-036 (AC-020.1, AC-020.2, AC-020.4) ✓ |
| **009** | `RowToggleContext` ×4 + ví dụ câu chào | FR-034 (AC-019.1, AC-019.3, AC-019.4) ✓ |
| **009** | Toggle nảy về tắt + nhãn "cần quyền" + CTA | FR-035 (AC-019.2), SF-012 ✓ |
| **009** | `CardUpsellInline` (gói Free) → WF-010 | FR-033 ERR-033.2, FR-045 (AC-024.4) ✓ |
| **010** | `CardContextUpsell` (nói về đúng tính năng vừa chạm) | FR-045 (AC-025.6) ✓ |
| **010** | `PriceTierCard` ×4 (gồm Free không làm mờ) | FR-046 (AC-025.1, AC-025.2, AC-025.4) ✓ |
| **010** | `ComparisonTableExpandable` (SF-015) | FR-046 P4 (AC-025.4) ✓ |
| **010** | `BtnTertiary` "Phục hồi giao dịch" | FR-003 (AC-029.5, AC-030.4) ✓ |
| **010** | `BtnTertiary` "Tiếp tục dùng gói Free" | FR-045 BR-045.4 (AC-024.4) ✓ |
| **010** | `CardErrorInline` + [Thử lại] khi StoreKit lỗi | FR-047 (AC-025.5) ✓ |
| **010** | Link điều khoản · chính sách quyền riêng tư | FR-048 P4 (AC-026.1) ✓ |
| **011** | `CardPriceConfirm` (4 mốc + chu kỳ) | FR-048 (AC-026.1, AC-026.5) ✓ |
| **011** | `BtnPrimary` "Xác nhận" + ghi `price_confirmed` | FR-048 (AC-026.2), FR-049 (AC-026.4) ✓ |
| **011** | Biến thể Lifetime (bỏ ngày gia hạn) | FR-054 (AC-026.3, AC-030.1) ✓ |
| **011** | `LinkFootnote` điều khoản · chính sách hoàn tiền | FR-050 (AC-026.6) ✓ |
| **012** | `CardPlanStatus` + [Xem các gói] | FR-044 (AC-024.2), FR-045 (AC-024.4) ✓ |
| **012** | `RowSliderVolume` + nghe thử (SF-004) | FR-015 (AC-009.1 → AC-009.4) ✓ |
| **012** | `RowSegmentedTheme` + `MiniWidgetPreview` (SF-021) | FR-061 (AC-036.1, AC-036.2, AC-036.3) ✓ |
| **012** | `RowNavigable` "Ngôn ngữ" + giá trị hiện tại | FR-055 (AC-031.1, AC-031.3) ✓ |
| **012** | `RowNavigable` "Quyền" (n/2 đã cấp) | FR-062 (AC-004.2) ✓ |
| **012** | `RowNavigable` "Đánh giá Carbina" | FR-059 ERR-059.2 (AC-033.3) ✓ |
| **012** | `RowNavigable` "Về Carbina" (phiên bản) | FR-066 (AC-NFR-011.1) ✓ |
| **012** | `RowNavigable` "Đăng ký của tôi" + trạng thái | FR-053 (AC-029.1) ✓ |
| **012** | `RowNavigable` "Quyền riêng tư & dữ liệu" | FR-057 (AC-032.1, AC-032.3) ✓ |
| **012** | `RowNavigable` "Tài khoản" *(chỉ MVP 3)* | FR-064 (AC-035.1) ✓ deferred (MVP 3) |
| **013** | `CardTrialSummary` (3 con số) | FR-052 (AC-028.1) ✓ |
| **013** | 3 nút ngang hàng gồm "Huỷ trial" | FR-052 (AC-028.2, AC-028.3, AC-028.4) ✓ |
| **013** | `BtnTertiary` "Xem chi tiết đăng ký" → WF-025 | FR-053 (AC-029.1) ✓ |
| **014** | `CardSceneMetrics` (kích thước thật) | FR-032 (AC-017.1) ✓ |
| **014** | `RowDiagnosticExpandable` + `failure_reason` (SF-016) | FR-032 (AC-017.1), FR-030 (AC-015.6) ✓ |
| **014** | "Xem widget ở kích thước này" → WF-023 | FR-025 (AC-013.1) ✓ |
| **014** | `BtnPrimary` "Gửi báo cáo" → WF-028 | FR-032 (AC-017.2, AC-017.4) ✓ |
| **014** | `IconButtonCopy` ⧉ (sao chép payload) | FR-032 P6 (AC-017.2) ✓ |
| **014** | `BtnTertiary` "Xoá lịch sử chẩn đoán" | FR-032 P7, BR-032.4 (AC-017.1) ✓ |
| **014** | `CardEmptyGuide` (hướng dẫn 3 bước) | FR-032 (AC-017.3) ✓ |
| **014** | Pull-to-refresh | FR-032 P2 (AC-017.1) ✓ |
| **015** | `CardAccountStatus` + `BtnPrimary` đăng nhập | FR-064 (AC-035.1) ✓ deferred (MVP 3) |
| **015** | `SyncScopeTable` (đồng bộ / ở lại máy) | FR-064 (AC-035.2) ✓ deferred |
| **015** | `RowToggle` "Đồng bộ cấu hình" · "Đăng xuất" | FR-064 (AC-035.2, AC-035.3) ✓ deferred |
| **015** | `BtnTertiaryDestructive` "Xoá tài khoản" | FR-065 (AC-035.4) ✓ deferred |
| **016** | `CarPlayPriorityCard` + `CarPlayActionCard` (chạm 1 lần) | FR-040 (AC-022.1 → AC-022.4), FR-042 (AC-023.1, AC-023.2) ✓ |
| **016** | Thứ tự thẻ đổi bằng crossfade throttle 30s (SF-017) | FR-040 (AC-022.2, AC-022.3) ✓ |
| **016** | `CarPlayCardError` (lỗi báo trên thẻ) | FR-042 (AC-023.3) ✓ |
| **016** | `CarPlayCardLocked` (khoá bằng chữ) | FR-042 (AC-023.4) ✓ |
| **016** | Thẻ dùng cache + thời điểm cập nhật | FR-041 (AC-022.6) ✓ |
| **016** | `CarPlayEdgeStatus` | FR-041 (AC-022.5) ✓ |
| **016** | Hành vi nền: sound Connect + ducking | FR-016 (AC-010.1 → AC-010.5), FR-017 (AC-010.4), FR-018 (AC-010.6) ✓ |
| **016** | Hành vi nền: sound Disconnect | FR-019 (AC-011.1, AC-011.3, AC-011.4), FR-020 (AC-011.2) ✓ |
| **016** | Hành vi nền: giọng chào | FR-037 (AC-021.1, AC-021.2, AC-021.5), FR-038 (AC-021.3, AC-021.4, AC-021.6), FR-039 (AC-021.7, AC-031.2, AC-031.5) ✓ |
| **016** | Thẻ liên hệ 1 chạm *(MVP 2)* | FR-063 (AC-034.1 → AC-034.4) ✓ deferred (MVP 2) |
| **017** | `CarPlayWidgetSurface` + layout từ bounds runtime | FR-029 (AC-015.1, AC-015.2, AC-015.5, AC-015.7) ✓ |
| **017** | `WidgetImageLayer` + `WidgetInfoLayer` (truncate ellipsis) | FR-030 (AC-015.3), FR-029 (AC-015.4) ✓ |
| **017** | `WidgetScrim` (khi tương phản < 4,5:1) | FR-029 (AC-015.4), AC-NFR-014.4 ✓ |
| **017** | Theme dùng chung với app | FR-061 (AC-036.1) ✓ |
| **018** | `CarPlayActionCard` ×3 (cấu hình Free đã chốt) | FR-041 (AC-022.5), FR-044 (AC-024.2, AC-024.3) ✓ |
| **018** | `CarPlayStaticUpsellLine` (**không chạm được**) | FR-041 BR-041.2, FR-045 (AC-024.4) ✓ |
| **019** | `CarPlayFallbackNotice` (chỉ đọc, không CTA) | FR-031 (AC-016.1, AC-016.2) ✓ |
| **019** | Chỉ widget lỗi → dashboard vẫn hoạt động | FR-031 (AC-016.5) ✓ |
| **020** | Tự phát khi sheet mở | FR-012 (AC-006.4) ✓ |
| **020** | `WaveformLive` lớn | FR-011 (AC-006.1) ✓ |
| **020** | `RowSliderVolume` inline | FR-015 (AC-009.2, AC-009.3) ✓ |
| **020** | `SegmentedControl3` (chọn sự kiện áp dụng) | FR-014 (AC-008.1, AC-008.2) ✓ |
| **020** | `BtnTertiary` mũi tên trước/sau (không cuộn vòng) | FR-012 P3–P4 (AC-006.4), SF-018 ✓ |
| **020** | `BtnPrimary` "Dùng sound này" / "Mở khoá" | FR-013 (AC-007.1), FR-010 (AC-006.2) ✓ |
| **021** | `TFField` ×3 (tên tự do) | FR-006 (AC-003.3), VR-006.1 ✓ |
| **021** | `ChipSegment` phân khúc xe | FR-005 (AC-002.4) ✓ |
| **021** | `BtnPrimary` "Gửi" | FR-006 (AC-003.1, AC-003.2) ✓ |
| **021** | `LabelFootnote` cam kết không PII | FR-006 (AC-003.3) ✓ |
| **022** | `CardExampleContrast` ×2 (có/không có quyền) | FR-007 (AC-004.1, AC-004.4) ✓ |
| **022** | `BtnPrimary` "Cho phép" / "Mở Cài đặt" | FR-007 (AC-004.2, AC-004.3) ✓ |
| **022** | `BtnSecondary` "Không, cảm ơn" (ngang hàng) | FR-007 BR-007.4 (AC-004.5) ✓ |
| **022** | `LinkFootnote` chính sách quyền riêng tư | FR-057 (AC-032.1) ✓ |
| **023** | `WidgetPreviewFrame` (cùng engine FR-029) | FR-025 (AC-013.4) ✓ |
| **023** | `RatioSourceLabel` (thật / ước lượng) | FR-025 (AC-013.1, AC-013.2) ✓ |
| **023** | `RatioPager` vuốt ngang (≥4 tỉ lệ, gồm màn 8") | FR-025 (AC-013.2), VR-025.1 ✓ |
| **023** | `SegmentedControl2` Sáng/Tối | FR-029 (AC-015.4), FR-061 (AC-036.2) ✓ |
| **023** | `ChipToggleLayer` ×3 (bật/tắt lớp thông tin) | FR-026 (AC-013.3) ✓ |
| **023** | `OverflowWarningBanner` + "Giảm bớt phần tử này" | FR-026 (AC-013.3), FR-030 (AC-015.3) ✓ |
| **023** | `RowNavigable` "Đổi ảnh" → WF-024 | FR-027 (AC-014.1) ✓ |
| **023** | `BtnPrimary` "Dùng bản này" | FR-025 (AC-013.4) ✓ |
| **024** | `ImageCropCanvas` + vùng cắt làm tối | FR-027 (AC-014.1), VR-027.1 ✓ |
| **024** | `BtnTertiary` "Xoay" · "Đặt lại khung" | FR-027 P4 (AC-014.1) ✓ |
| **024** | `ChipSourcePicker` (ảnh model / ảnh của tôi) | FR-027 (AC-014.4) ✓ |
| **024** | `ThumbCarousel` bộ ảnh theo model | FR-005 (AC-002.3), FR-027 P2 (AC-014.4) ✓ |
| **024** | `ResolutionWarningBanner` | FR-028 (AC-014.2) ✓ |
| **024** | `PermissionInfoBanner` + [Mở Cài đặt] | FR-027 (AC-014.4) ✓ |
| **024** | `BtnPrimary` "Xong" (nén ≤ 2MB) | FR-028 (AC-014.3) ✓ |
| **025** | `CardSubscriptionStatus` | FR-053 (AC-029.1) ✓ |
| **025** | `FeatureListExpandable` (SF-019) | FR-053 P3 (AC-029.1) ✓ |
| **025** | `BtnDestructiveOutline` "Huỷ đăng ký" | FR-053 (AC-029.2, AC-029.4) ✓ |
| **025** | Biến thể Lifetime (không nút huỷ) | FR-053 (AC-029.3), FR-054 (AC-030.3) ✓ |
| **025** | `DoubleChargeWarning` + "Huỷ subscription cũ" | FR-054 (AC-030.3) ✓ |
| **025** | `BtnTertiary` "Phục hồi giao dịch" | FR-003 (AC-029.5) ✓ |
| **025** | `RowNavigable` "Xem các gói khác" → WF-010 | FR-045 (AC-024.4) ✓ |
| **025** | `RowNavigable` "Quản lý trong Cài đặt iOS" | FR-053 (AC-029.4) ✓ |
| **026** | `RowSelectableLanguage` ×4 (áp dụng ngay) | FR-055 (AC-031.1, AC-031.3, AC-031.4) ✓ |
| **026** | `NoteFootnote` DE/FR/IT thuộc MVP 2 | FR-055 BR-055.2 (AC-031.4) ✓ |
| **027** | `AlertContainer` + câu nêu ngày hết quyền | FR-053 (AC-029.4), FR-051 (AC-027.3) ✓ |
| **027** | `BtnSecondary` "Giữ đăng ký" | FR-053 (AC-029.2) ✓ |
| **027** | `BtnDestructiveOutline` "Huỷ đăng ký" | FR-053 (AC-029.4) ✓ |
| **028** | `RowDataDisclosureExpandable` ×4 + giá trị thật (SF-020) | FR-032 (AC-017.2), FR-066 (AC-NFR-011.1) ✓ |
| **028** | Bỏ tick một mục dữ liệu | FR-032 (AC-017.2), VR-032.2 ✓ |
| **028** | `TFTextArea` ghi chú ≤ 500 ký tự | FR-032 VR-032.1, FR-060 (AC-033.1) ✓ |
| **028** | `IconButtonCopy` ⧉ | FR-032 P6 (AC-017.2) ✓ |
| **028** | `BtnPrimary` "Gửi" | FR-032 (AC-017.4), FR-060 (AC-033.1) ✓ |
| **028** | `LabelNoPII` | FR-066 (AC-NFR-011.1) ✓ |
| **029** | `DataLossList` / `DataKeptList` + số ngày | FR-057 (AC-032.1, AC-032.3, AC-032.4) ✓ |
| **029** | `BtnDestructiveOutline` "Xoá dữ liệu học" | FR-057 (AC-032.2, AC-032.4) ✓ |
| **029** | `RowSecondaryDestructive` "Xoá cả cấu hình" | FR-058 (AC-032.2), BR-058.1 ✓ |
| **029** | `BtnSecondary` "Huỷ" | FR-057 (AC-032.3) ✓ |
| **030** | `ToastOverlay` xác nhận (tự đóng 2s) | FR-006 (AC-003.1), FR-032 (AC-017.4) ✓ |
| **030** | `BtnInlineUndo` "Hoàn tác" 5s | FR-058 (AC-032.2), BR-058.3 ✓ |
| **030** | `SatisfactionPicker` (👍/👎) | FR-059 (AC-033.2, AC-033.3, AC-033.4) ✓ |
| **030** | Nhánh 👎 → WF-028 (**không** ra App Store) | FR-060 (AC-033.1) ✓ |
| **030** | `BtnInlineRetry` "Thử lại" (toast lỗi 4s) | FR-022 ERR-022.1 (AC-012.2) ✓ |

### 10.3 Kết quả audit

| Trạng thái | Số lượng | Ghi chú |
|---|---|---|
| **✓ backed** | **152** | Mọi affordance map tới ≥ 1 FR có AC |
| **✓ deferred** | **6 nhóm chrome + 6 affordance MVP 2/3** | Chrome điều hướng → `UX_Flows.md` Step 6 (§10.1); WF-015 và thẻ liên hệ WF-016 → FR-063/064/065 `Deferred` |
| **✗ GAP** | **0** | Không còn affordance nào không có FR |

**Kiểm tra "mỗi WF có FR backing riêng và đúng chủ đề"**: 30/30 màn hình có FR chuyên đề riêng — kể cả modal. Hai trường hợp dùng chung màn hình được phân biệt bằng **hai FR khác nhau**, không phải gán gượng: **WF-028** có FR-032 (gửi báo cáo chẩn đoán, bắt buộc có kích thước màn hình) và FR-060 (kênh phản hồi, bắt buộc có ghi chú) — khác điểm khởi phát, khác dữ liệu bắt buộc, khác mục tiêu đo. **WF-030** có FR-059 (mời đánh giá) và FR-058 (Hoàn tác) — hai biến thể, hai FR.

---

## 11. Cross-Screen Component Consistency Audit

### 11.1 Component dùng ở ≥ 2 màn hình

```
BtnPrimary        → 14 màn (002,003,004,005,009,010*,011,013,014,015,020,021,023,024,028)
BtnSecondary      → 7 màn  (005,013,022,023,027,029,030)
BtnTertiary       → 12 màn (002,003,004,005,007,008,012,013,020,025,026,028)
BtnDestructiveOutline → 4 màn (013,025,027,029)
NavBarStandard    → 10 màn (003,004,005,006,007,008,009,011,012,014)
NavBarModal       → 3 màn  (010,013,015)
SheetContainer    → 7 màn  (020,021,022,024,025,026,028)
AlertContainer    → 2 màn  (027,029)
TabBarCustom      → 2 màn  (006,012)
WaveformLive      → 3 màn  (004,007,020)
RowSoundPreset    → 2 màn  (004,007)
LockLabel         → 5 màn  (004,007,008,012,024)
SegmentedControl3 → 2 màn  (007,020)
RowSliderVolume   → 2 màn  (012,020)
ProgressBarOnboard→ 4 màn  (002,003,004,005)
StatusBadge       → 2 màn  (006,012)
IconButtonCopy    → 2 màn  (014,028)
PullToRefreshIndicator → 2 màn (006,014)
CarPlayActionCard → 3 màn  (016,018,019)
ToastOverlay      → 1 màn định nghĩa (030), dùng bởi 8 màn
```
*(WF-010 dùng `PriceTierCard` làm lựa chọn chính; `BtnPrimary` thật ở WF-011.)*

### 11.2 Kiểm tính nhất quán

| Component | Size | Position | Icon | Label | Color | Behavior | State | Kết luận |
|---|---|---|---|---|---|---|---|---|
| `BtnPrimary` | ✓ h=50 mọi màn | ✓ đáy / safeAreaInset | — | nhãn động theo ngữ cảnh — **hợp lệ** | ✓ accent | ✓ chạm = hành động chính | ✓ vô hiệu = surfaceVariant + textTertiary | **Pass** |
| `BtnSecondary` | ✓ h=50 | ✓ cạnh BtnPrimary | — | ✓ | ✓ surface + border | ✓ | ✓ | **Pass** |
| `BtnTertiary` | ✓ h=44 | ✓ dưới CTA hoặc trong row | — | ✓ | ✓ accent | ✓ | ✓ vô hiệu = textTertiary | **Pass** |
| `BtnDestructiveOutline` | ✓ h=50 | ✓ | — | ✓ | ✓ destructive | ✓ luôn cần xác nhận | ✓ | **Pass** |
| `NavBarStandard` | ✓ h=44 | ✓ trên | ✓ `chevron.left` 20pt | ✓ | ✓ | ✓ | ✓ | **Pass** |
| `SheetContainer` | detent khác nhau (50% / 90%) | ✓ | ✓ dragIndicator 36×5 | — | ✓ | ✓ | ✓ | **Pass** — xem ngoại lệ 11.3-a |
| `WaveformLive` | ✓ h=40 | Zone A ở 004/007, lớn hơn ở 020 | — | — | ✓ accent | ✓ chạy theo audio thật | ✓ ẩn khi không có tiếng | **Pass** |
| `LockLabel` | ✓ h=24 | ✓ cuối row / trên thẻ | ✓ `lock.fill` | ✓ | ✓ surfaceVariant | ✓ **luôn nghe/xem trước được** | ✓ | **Pass** |
| `RowSliderVolume` | ✓ h=68 | WF-012 trong nhóm; WF-020 dưới waveform | — | ✓ | ✓ accent | ✓ phản hồi âm thanh tức thì | ✓ 0 = "đang tắt" | **Pass** |
| `ProgressBarOnboard` | ✓ h=4 | ✓ đáy | — | — | ✓ | ✓ 1/4→4/4 | — | **Pass** |
| `CarPlayActionCard` | tỉ lệ bounds | ✓ | — | ✓ | ✓ borderStrong | ✓ 1 chạm | ✓ error/locked | **Pass** |
| `ToastOverlay` | ✓ minH=50 | ✓ mép dưới | — | ✓ | ✓ surfaceElevated | 2s / 4s / không tự đóng | ✓ | **Pass** — xem ngoại lệ 11.3-b |

### 11.3 Ngoại lệ được ghi nhận có lý do

**a) `SheetContainer` — detent khác nhau giữa các màn**
- `detentMedium: 50%` ở WF-020, 021, 022, 025, 026 · `detentLarge: 90%` ở WF-024, 028.
- **Lý do**: WF-024 cần chỗ để thao tác crop chính xác; WF-028 cần chỗ cho bàn phím khi gõ ghi chú. Cùng component, khác detent theo **nhu cầu thao tác**, không phải khác thẩm mỹ.
- **Không** tách tên component vì mọi thuộc tính thị giác giống nhau.

**b) `ToastOverlay` — ba biến thể thời lượng và hành vi**
- Xác nhận: tự đóng **2s**, không nút · Lỗi: tự đóng **4s**, có [Thử lại] · Hoàn tác: **5s**, có [Hoàn tác] · Mời đánh giá: **không tự đóng**, có bộ chọn.
- **Lý do**: thời lượng tỉ lệ với lượng chữ cần đọc và mức hệ quả. Biến thể mời đánh giá không tự đóng vì nó **cần** một quyết định.
- **Tách tên**: `ToastConfirm` · `ToastError` · `ToastUndo` · `RatingPromptOverlay` — bốn component riêng dùng chung base `ToastOverlay`. Tách tên để giai đoạn thi công không nhầm chúng là một.

**c) `CardCompactStatus` vs `CardConnectionStatus` vs `CardPlanStatus`** — ba card trạng thái, ba chiều cao (88 / 200 / 72), ba nội dung.
- **Lý do**: kích thước phản ánh **mức ưu tiên** trong hierarchy của từng màn, không phải sự thiếu nhất quán.
- **Tách tên** đã làm — ba component riêng, cùng token `${component.card}`.

**d) `CarPlayActionCard` vs `CardCompactStatus`** — thẻ trên xe vs thẻ trên iPhone.
- **Lý do**: `CarPlayActionCard` dùng `shadow.elevation.0` + `borderStrong` và kích thước tỉ lệ bounds; `CardCompactStatus` dùng `shadow.elevation.1` + `border` và kích thước pt.
- **Tách tên** đã làm — **đây là ngoại lệ quan trọng nhất của tài liệu**: hai bề mặt có ngôn ngữ thị giác khác nhau vì có ràng buộc khác nhau (NFR-007, an toàn khi lái). Gộp chúng lại sẽ dẫn tới việc render shadow trong widget extension.

**e) `WaveformLive` — kích thước khác nhau giữa WF-004/007 và WF-020**
- **Lý do**: ở WF-020 người dùng đang **nghe kỹ** một preset nên waveform là nội dung chính; ở WF-004/007 nó là chỉ báo phụ trong danh sách.
- **Không** tách tên vì mọi token giống nhau, chỉ khác kích thước khung chứa.

### 11.4 Kết quả

| Phép kiểm | Kết quả |
|---|---|
| Component dùng ở ≥ 2 màn được nhận diện | **20 component** |
| Nhất quán 7 chiều (size/position/icon/label/color/behavior/state) | **12/12 Pass** |
| Ngoại lệ có lý do được ghi nhận | **5** (a → e) |
| Ngoại lệ cần tách tên component | **3 đã tách**: 4 biến thể Toast · 3 card trạng thái · CarPlay vs iPhone card |
| Không nhất quán chưa giải thích | **0** |

---

**Document Version**: 2.4
**Last Updated**: 2026-08-07 (snapshot bộ tài liệu; file tạo ngày 2026-08-17)
**Status**: Draft — chờ PO review
**Design System**: `bento-grid` · [`DESIGN_TOKEN_BENTO_GRID.json`](../../shared/DESIGN_TOKEN_BENTO_GRID.json)
**Dependencies**: `PRD.md` v2.4 · `Project_Overview.md` v2.4 · `Use_Cases.md` v2.4 · `Functional_Requirements.md` v2.4 (+ 7 sub-spec)
**Thống kê**: 30 màn hình · 4 archetype (Social = 0, có lý do) · 16 màn có Layout Variants · 152 affordance đã back-trace · 0 GAP
**Bước kế tiếp**: `gate-wireframes` → phê duyệt → **Step 6: `UX_Flows.md`** (sở hữu đường điều hướng — gồm cả nhóm chrome đã khai deferred ở §10.1)
