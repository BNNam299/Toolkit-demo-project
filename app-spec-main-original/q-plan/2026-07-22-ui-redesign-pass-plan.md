# Blueprint: Luồng "Cải tiến UI theo phong cách riêng" (post-build) — LUỒNG ĐỘC LẬP

- **Ngày**: 2026-07-22
- **Loại**: Năng lực MỚI, **luồng độc lập** cho framework `ios-spec-driven-installer` (1 command + 3 skill: `ui-redesign` / `ui-redesign-craft` / `ui-redesign-contract`)
- **Tách biệt**: KHÔNG thuộc pipeline project-docs; KHÔNG sửa gate/roadmap của project-docs
- **Phạm vi kiến trúc**: template content tại `src/ios_spec_driven_installer/templates/content/`
- **Trạng thái**: Blueprint (chỉ thiết kế — không chứa code chức năng)

> Nhiệm vụ: sau khi app code xong mọi phase, chạy **một luồng riêng biệt** — người dùng cấp phong cách qua **1 trong 3 nguồn**:
> (a) **ảnh mẫu**, (b) **mô tả text**, (c) **file `.pen` (Pencil)** trong thư mục `design-token/` — AI học thiết kế & rút
> **design token** từ file `.pen` qua **Pencil MCP**. Sau đó AI **audit UI của app đã build**, rồi sinh **một thư mục đề xuất
> redesign** (các màn hình theo phong cách mới + **mermaid luồng** + **design token mới** + **component mới tối đa reuse**,
> **dễ đọc cho người và AI**), duyệt, rồi áp dụng vào code với các gate execution sẵn có. Luồng này **đứng riêng**, gọi bằng 1 command mới.

> **LƯU Ý QUAN TRỌNG — contract KHÔNG đủ để sáng tạo:** `ui-redesign-contract` chỉ là *validator* (đảm bảo gói redesign
> đủ file/đúng cấu trúc/truy vết/dễ đọc/vượt SÀN UX) — nó KHÔNG tạo ra thiết kế đẹp/cá tính. "Đúng chuẩn" ≠ "sáng tạo".
> Vì vậy blueprint tách 4 vai: **`ui-redesign` = cỗ máy sinh (Creative Method §4.9)** · **`ui-redesign-craft` = kiến thức
> craft/signature-moments** · **`ui-redesign-contract` = validator + gate (gồm distinctiveness bar)** · **vòng
> screenshot-critique (P7) = đánh giá thẩm mỹ lặp**. Chất liệu sáng tạo (Style DNA từ `.pen`/ảnh/mô tả + 10 DESIGN_TOKEN +
> design-ui creative-direction) phải được *nạp vào bước sinh*, không chỉ để validate.

---

## 0. Nguyên tắc tách biệt (theo yêu cầu)

- Đây là **luồng thứ 4**, song song với: `/ios-project-docs` (docs), `/ios-spec` (spec feature), `/ios-execute` (code).
  Gọi bằng command riêng `/ios-ui-redesign`. **Không** nối vào chuỗi project-docs, **không** dùng `project-docs-quality-gates`,
  **không** sửa `project-docs-roadmap`.
- **Tự chứa**: gate của luồng nằm trong `ui-redesign-contract` (tiền lệ: `uiux-analysis-contract` đã tự có §7 Quality Gate,
  không phụ thuộc project-docs).
- **Nguồn màn hình = app đã build** (`Features/*/Views/*.swift`), KHÔNG bắt buộc `Wireframes.md`. `Wireframes.md` +
  `design-ui/*` chỉ là **input tham chiếu tùy chọn** (dùng nếu có). ⇒ luồng chạy được ngay cả khi project-docs không đầy đủ,
  miễn app build được.
- Chỉ **tái dùng gate ở tầng code** (Structure/Reuse-First/UX Compliance/DSS/Build-Integration) làm rào chắn khi áp dụng —
  đây là gate execution, không phải project-docs.

---

## 1. Bối cảnh nghiên cứu (ràng buộc thiết kế)

Nguồn: 2 lần khảo sát toàn framework.

- **Execution per-feature**, terminal `stage: done`; **không có trạng thái app-wide** → luồng tự quản state riêng cấp project.
- **"App build/launch được"** = Integration Gate 5 (`execution-contract`): "App launches / no regressions".
- **DSS runtime tokens** (đích redesign) = `{{IDE_CONFIG_DIR}}shared/Styles/AppColors.swift`, `AppFonts.swift`, `AppSpacing.swift`.
- **Vị trí UI**: màn `Features/[Feature]/Views/*.swift`; component `{{IDE_CONFIG_DIR}}shared/Components/[Type]/`; style `shared/Styles/`; modifier `shared/Modifiers/`.
- **3 lỗ hổng gốc khiến app "nhạt"** (luồng phải xử lý trực tiếp):
  1. `design-ui/*` không được code-time đọc.
  2. Không có cầu nối `DESIGN_TOKEN_*.json` → `shared/Styles/*.swift` (Swift là stub #007AFF).
  3. Không có pha "nhìn app đã build rồi nâng cấp".
- **Gate tái dùng làm rào chắn (tầng code)**: Structure (`ios-architecture`), Reuse-First (`ios-components`), UX Compliance (`ios-ui-ux`), DSS Gate, Build/Integration (`execution-quality-gates`).
- **Quy ước bám theo**: command = frontmatter + bảng bước + Rules + Usage (`commands/ios-spec.md`); contract tự chứa gate (`uiux-analysis-contract` §7).
- **Quyết định người dùng**: nguồn phong cách = ảnh / mô tả / **file `.pen` qua Pencil MCP**; phạm vi = toàn quyền refactor UI (không đổi business logic); audit = kết hợp static + screenshot; **luồng riêng, tách project-docs**.
- **Có sẵn thư mục `content/design-token/` với 4 template `.pen`**: `template-Swiss-Clean.pen`, `template-Monochrome-Type.pen`, `template-neo.pen`, `template-bento.pen`. File `.pen` **mã hoá** → chỉ truy cập qua **Pencil MCP** (cấm Read/Grep trực tiếp). Pencil variables ≈ design token → map thẳng `.pen` → token mới → `shared/Styles/*.swift`.
- **Installer HIỆN CHƯA copy `design-token/`** (chỉ copy `*.md` + skills/shared/scripts/hooks) → cần bổ sung bước copy verbatim (binary, không transform text).

---

## 2. Scope of Impact (danh sách file chính xác)

### 2.1 File TẠO MỚI (lõi luồng — tự chứa)

| Path | Vai trò |
|------|---------|
| `src/.../content/commands/ios-ui-redesign.md` | Command mới — entry point luồng redesign độc lập |
| `src/.../content/skills/ui-redesign/SKILL.md` | Pipeline chính (P0–P7) **+ Creative Method (§4.9): cỗ máy biến Style DNA → quyết định thị giác/màn** |
| `src/.../content/skills/ui-redesign-craft/SKILL.md` | **Kiến thức craft sáng tạo**: distinctiveness principles, **signature-moments catalog**, cách vượt iOS-stock, motion biểu cảm; relax "clarity over decoration" mà giữ SÀN |
| `src/.../content/skills/ui-redesign-contract/SKILL.md` | Output contract TỰ CHỨA: cây `redesign/`, đặt tên, schema từng file, readability, **§Quality Gate (gate-redesign) inline gồm distinctiveness bar** |

> KHÔNG tạo template-có-manifest và KHÔNG thêm gate vào project-docs — schema file định nghĩa inline trong contract
> (giống `uiux-analysis-contract`), để luồng không phụ thuộc máy manifest của project-docs.

### 2.2 File SỬA (tối thiểu — KHÔNG chạm project-docs)

| Path | Thay đổi | Vì sao không phải project-docs |
|------|----------|-------------------------------|
| `src/.../content/commands/ios-execute.md` | Completion: gợi ý (tùy chọn) "bước cuối: `/ios-ui-redesign`" | `ios-execute` là luồng code, không phải project-docs |
| `src/.../content/skills/ios-ui-ux/SKILL.md` | Ghi chú: trong luồng redesign, cá tính phong cách GHI ĐÈ mặc định "native/clarity"; **SÀN UX bất di bất dịch** | `ios-ui-ux` là skill code-time, dùng làm rào chắn |
| `src/ios_spec_driven_installer/installer.py` | **Thêm bước copy `content/design-token/` → `{{IDE_CONFIG_DIR}}design-token/`** (copy verbatim `*.pen` bằng `shutil.copy2`, KHÔNG `_transform_content_file` vì binary/mã hoá) | Để 4 template `.pen` được cài kèm |
| `CHANGELOG.md`, `pyproject.toml`, `SLIDES.md` | Bump `3.1.0 → 3.2.0` + mô tả | metadata |

### 2.3 File TÁI DÙNG (KHÔNG sửa — chỉ đọc/tham chiếu)

`skills/ios-architecture` (Structure Gate + `shared/Styles`), `skills/ios-components` (Reuse-First),
`skills/execution-quality-gates` (Build/Integration + Xcode MCP), `shared/DESIGN_TOKEN_*.json` (điểm tựa phong cách),
`content/design-token/*.pen` (**nguồn phong cách qua Pencil MCP** — đã có 4 template), Pencil MCP (`mcp__pencil__*`),
`skills/uiux-analysis-workflow` (**nguồn khái niệm distinctiveness/Signature Opportunities** để `ui-redesign-craft` kế thừa) + output `design-ui/*` + `Wireframes.md` (**tham chiếu TÙY CHỌN**).

### 2.4 Output do luồng sinh ra (runtime)

`{{IDE_CONFIG_DIR}}specs/[project-name]/redesign/` (chi tiết §5) — artifact của app, do luồng độc lập tạo (không phải sản phẩm project-docs pipeline).

---

## 3. Detailed Usecases

### 3.1 Primary flow
1. Chạy `/ios-ui-redesign <ảnh|mô tả>` sau khi app hoàn thiện (độc lập, không cần trạng thái project-docs).
2. Prereq: app build/launch được (mọi `specs/*/spec-state.json` = `done`). Tạo `redesign/` + `redesign-state.json` (state=`intake`).
3. **Intake** (1 trong 3 nguồn): (a) ảnh, (b) mô tả text, (c) **file `.pen`** trong `design-token/` → dùng **Pencil MCP** học thiết kế + rút variables/tokens (§4.8). Tổng hợp → **Style DNA** → `style-reference.md` (state=`audit`).
4. **Audit (kết hợp)**: liệt kê màn hình từ **app đã build** (`Features/*/Views/*`), đọc `shared/Styles/*`, `shared/Components/*`; build→boot sim→chụp **screenshot before**; (tùy chọn) đối chiếu `design-ui/*`, `Wireframes.md` → `current-ui-audit.md`.
5. **Hệ mới**: `design-tokens.md` (token mới + **bảng map token→`shared/Styles/*.swift`**; nếu nguồn là `.pen` thì map thẳng Pencil variables → token) + `components.md` (bảng old→new, tối đa reuse; tham chiếu node/spec `.pen` nếu có).
6. **Redesign màn + luồng**: `screens/screen-[view-name].md` (before→after từng màn của app) + `flows.md` (mermaid) (state=`proposed`).
7. **Index + gate**: `README.md` + `redesign-summary.md` + `manifest.json`; chạy **gate-redesign (trong contract)**; **PAUSE duyệt**.
8. **Apply (sau duyệt)**: token→`shared/Styles/*.swift`; dựng component mới; refactor từng View — mỗi bước qua gate code Structure/Reuse/UX/DSS; `build_sim` sau mỗi phase (state=`applying`).
9. **Verify**: screenshot after; so sánh before/after; Integration gate (build/launch, no regression, no behavior change) → cập nhật `redesign-summary.md`, state=`done`.

### 3.2 Alternate flows
- **AF-1** Đổi nguồn phong cách → cập nhật `style-reference.md`, re-derive DNA, giữ audit.
- **AF-2** Duyệt theo nhóm (token+component trước, screens sau).
- **AF-3** Apply theo lô (shared → màn core → màn phụ), pause giữa lô.
- **AF-4** Resume: đọc `redesign-state.json`, tiếp từ state dở; không ghi đè file đã PASS nếu chưa xác nhận.

### 3.3 Edge cases
- **E-1** App không build / spec chưa `done` → DỪNG, yêu cầu hoàn tất `/ios-execute` trước.
- **E-2** Không có input phong cách, HOẶC `--pen` không khớp file trong `design-token/`, HOẶC Pencil MCP không khả dụng → hỏi tương tác / liệt kê `.pen` có sẵn / đề nghị dùng `--image|--desc`; vẫn trống → DỪNG (không tự chế identity).
- **E-3** Sim không boot → hạ xuống audit tĩnh, ghi rõ "screenshot skipped" (không âm thầm).
- **E-4** Phong cách phá SÀN UX (contrast <4.5:1, mất state) → gate CHẶN; phải chỉnh, không đánh đổi.
- **E-5** Đề xuất chạm business logic → tách ra, KHÔNG tự đổi; báo cần `/ios-spec`.
- **E-6** Component mới trùng cái có → Reuse-First bắt buộc reuse/parameterize.
- **E-7** Refactor gây regression → rollback bước đó, giữ app xanh; không `done`.
- **E-8** Không có `design-ui/`/`Wireframes.md` → vẫn chạy (nguồn màn = Views; DNA = input); ghi chú thiếu nguồn tham chiếu.

---

## 4. Interface & Function Signatures (skeleton kiến trúc)

> Hệ skill markdown + gate tự chứa → "signature" = hợp đồng vào/ra từng phase + cấu trúc section file + schema JSON.
> Không có code Swift/Python chức năng.

### 4.1 `commands/ios-ui-redesign.md` (skeleton)
```
---
description: Standalone post-build UI redesign to a distinctive style (style ref → proposal → apply)
allowed-tools: Read, Write, Edit, Grep, Glob, Task, Bash, mcp__pencil__*
---
# COMMAND: Redesign App UI to a Distinctive Style (independent flow)
Input: $ARGUMENTS = 1 trong 3 nguồn phong cách:
  - --image <path...>   : ảnh mẫu
  - --desc "<text>"     : mô tả phong cách
  - --pen <name>        : tên file .pen trong design-token/ (vd: neo | bento | Swiss-Clean | Monochrome-Type)
                          → đọc qua Pencil MCP để học thiết kế + rút design token (§4.8)
Prereq: app build/launch được (mọi specs/*/spec-state.json = done)
Bảng bước (đều gọi skill ui-redesign, KHÔNG gọi skill project-docs):
  | Step | Giai đoạn | Skill |
  | 1 | Intake + Audit | ui-redesign (P1–P2) |
  | 2 | Proposal + gate-redesign | ui-redesign (P3–P5) |
  | 3 | Apply + verify | ui-redesign (P6–P7) |
Sau mỗi step: Approve / Modify / Pause.
Rules: giai đoạn đề xuất chỉ ghi dưới specs/[project]/redesign/; giai đoạn áp dụng chỉ ghi shared/Styles|Components + Features/*/Views; không đổi business logic; không qua gate fail.
Usage:
  /ios-ui-redesign --pen neo
  /ios-ui-redesign --image ./ref/home.png ./ref/detail.png
  /ios-ui-redesign --desc "neo-brutalist, high-contrast, bold borders"
```

### 4.2 `skills/ui-redesign/SKILL.md` — hợp đồng từng phase (in → out)
```
P0 Prereq        (in: app build state)                    → tạo redesign/ + redesign-state.json(intake) | STOP(E-1)
P1 IntakeStyle   (in: --image | --desc | --pen <name>)     → style-reference.md {Style DNA: mood,palette,type,shape,motion,density,refs}; state=audit
                  · nếu --pen: dùng Pencil MCP (§4.8) rút variables/guidelines/screenshot → tokens thô + ảnh tham chiếu
P2 AuditCurrent  (in: Features/*/Views/*, shared/Styles, shared/Components; [design-ui, Wireframes optional]; screenshots-before)
                                                          → current-ui-audit.md {screen inventory từ Views, screenshot refs, gap-vs-DNA}
P3 DesignSystem  (in: Style DNA + current tokens/components) → design-tokens.md {token set + BẢNG map token→shared/Styles/*.swift}; components.md {old→new + reuse tier}
P4 RedesignScreens (in: screen inventory + tokens/components + Style DNA)
                  → ÁP Creative Method (§4.9) + craft catalog (ui-redesign-craft): mỗi màn quyết định composition/hierarchy/màu/type/spacing/motion + ≥1–3 signature moment
                  → screens/screen-[view].md (1/màn, giữ SÀN) + flows.md (mermaid)
P5 IndexAndGate  (in: mọi file trên)                       → README.md + redesign-summary.md + manifest.json; chạy gate-redesign (gồm distinctiveness bar); state=proposed; PAUSE
P6 ApplyToCode   (in: manifest.json đã duyệt)             → sửa shared/Styles/*.swift, shared/Components/*, Features/*/Views/*; qua Structure/Reuse/UX/DSS gate; build_sim mỗi phase; state=applying
P7 VerifyCritique (in: build + screenshots-after)         → VÒNG LẶP: build→chụp→tự phê bình như chuyên gia UI/UX (bám Style DNA + distinctiveness) → nếu chưa đạt thì sửa & lặp (≤N vòng) → so sánh before/after; Integration gate; state=done
```
Non-negotiable: chỉ chuyển phase khi output pass gate; ghi state sau mỗi phase; không đổi business logic; sim fail → E-3.

### 4.3 `skills/ui-redesign-contract/SKILL.md` — output contract TỰ CHỨA
- Đường dẫn CHÍNH XÁC: `{{IDE_CONFIG_DIR}}specs/[project-name]/redesign/` (cấm biến thể).
- Đặt tên màn: `screen-[view-name].md` (view-name = tên file View, lowercase-hyphen; vd `screen-diary-view.md`).
- Front-matter mỗi file `{doc_id, version, date, style_ref}` để AI parse.
- Readability: heading nhất quán, mọi quyết định lớn dẫn nguồn Style DNA, không placeholder, README có read-order + bảng single-source-of-truth.
- **§Quality Gate (gate-redesign) — inline, tự chứa** (§4.6). Không tham chiếu project-docs-quality-gates.

### 4.4 Schema `redesign-state.json`
```
{
  "project": "<name>",
  "state": "intake|audit|proposed|approved|applying|done",
  "style_ref": {
    "source": "image|desc|pen",
    "images": ["<path>"],
    "description": "<text>",
    "pen_file": "design-token/template-neo.pen",
    "pen_variables": { "<var>": "<value>" },
    "dna_summary": "<text>"
  },
  "screens_source": "built-app-views",
  "screenshots": { "before": ["<path>"], "after": ["<path>"] },
  "gate_redesign": "pending|pass|fail",
  "applied_screens": ["<ViewName>"],
  "updated": "<timestamp truyền vào>"
}
```

### 4.5 Schema `manifest.json` (đề xuất → áp dụng)
```
{
  "tokens":     [ { "name":"color.accent", "value":"<hex/spec>", "swift_target":"shared/Styles/AppColors.swift", "symbol":"accent" } ],
  "components": [ { "new":"<Name>", "replaces":"<Old|null>", "reuse_tier":"as-is|parameterize|compose|extend|new", "file":"shared/Components/<Type>/<Name>.swift" } ],
  "screens":    [ { "view":"DiaryView", "view_file":"Features/Diary/Views/DiaryView.swift", "proposal":"redesign/screens/screen-diary-view.md", "flow_changed":true } ]
}
```

### 4.6 `gate-redesign` — tiêu chí (inline trong contract, tự chứa)
- Đủ file bắt buộc: README, style-reference, current-ui-audit, design-tokens, components, flows, screens/*, redesign-summary, manifest.json.
- **Mỗi màn của app đã build** (mỗi View trong `Features/*/Views/*`) có 1 file redesign tương ứng (đủ độ phủ).
- `design-tokens` có **bảng map token→`shared/Styles/*.swift`** (không token treo docs).
- `components` có bảng **old→new** + reuse tier + lý do (ưu tiên reuse).
- Có mermaid ở `flows.md` và mỗi màn có luồng.
- **Readability**: front-matter + không placeholder + `manifest.json` parse được.
- **SÀN UX giữ nguyên**: mỗi màn khai đủ 4 state + a11y + contrast ≥4.5:1 + ≥44pt + dark mode.
- **Distinctiveness bar (thước đo cá tính)**: mỗi màn có ≥1 signature moment dẫn nguồn Style DNA; token/màn **lệch rõ khỏi iOS-stock** (không còn #007AFF / system-default font/spacing); `README` nêu "signature system" của app.
- **Trace**: mọi quyết định lớn dẫn nguồn `style-reference` (Style DNA).

### 4.7 Section skeleton `screens/screen-[view].md`
```
## Metadata (doc_id, view, view_file, style_ref)
## Before (mô tả/ảnh hiện tại)
## After — Layout mới (zones, hero, hierarchy theo phong cách)
## Components Used (link components.md; đánh dấu reuse/new)
## States (Loading/Empty/Error+recovery/Success — GIỮ SÀN)
## Signature Moments (1–3, dẫn nguồn Style DNA)
## Screen Flow (mermaid)
## Accessibility (VoiceOver/Dynamic Type/contrast/≥44pt/dark mode)
```

### 4.8 Pencil MCP intake (khi nguồn = `--pen <name>`)

Mục tiêu: học thiết kế + rút design token từ file `.pen`. **File `.pen` mã hoá — CẤM Read/Grep; chỉ dùng `mcp__pencil__*`.**

Thứ tự gọi (hợp đồng):
```
1. get_editor_state(include_schema: true)   # BẮT BUỘC đầu tiên — nạp schema để dùng các tool khác
2. get_variables()                           # → design tokens: color / typography / spacing / radius / shadow (nguồn chính cho design-tokens.md)
3. get_guidelines()                          # → nguyên tắc phong cách (spacing rule, usage) → nạp vào Style DNA
4. get_screenshot() / snapshot_layout()      # → ảnh/khung layout tham chiếu (lưu path vào style-reference.md)
5. export_nodes() / export_html() (tùy chọn) # → spec component/layout mẫu → gợi ý components.md
```
Xử lý:
- Map `pen_variables` → `design-tokens.md` (mỗi biến → 1 token) → tiếp tục map token→`shared/Styles/*.swift` (chuỗi `.pen`→token→Swift liền mạch, lấp lỗ hổng #2).
- Ghi `style_ref.source="pen"`, `pen_file`, `pen_variables` vào `redesign-state.json`.
- Tên `.pen` hợp lệ = tên file trong `{{IDE_CONFIG_DIR}}design-token/` (bỏ tiền tố `template-`, bỏ đuôi `.pen`). Không khớp → liệt kê các lựa chọn có sẵn.
- Nếu Pencil MCP không khả dụng → E-2 (hỏi nguồn khác), không âm thầm bỏ qua.

### 4.9 Creative Method (cỗ máy sinh — trong `skills/ui-redesign/SKILL.md`)

Đây là phần LÀM RA thiết kế (contract không có). Hợp đồng biến **Style DNA → quyết định thị giác** cho mỗi màn:
```
INPUT : Style DNA {mood, palette, type-vibe, shape-language, motion, density} + screen role + current screenshot
STEPS :
  1. Chọn "signature system": 1 ý tưởng hình thức xuyên suốt (vd: bố cục bento, viền đậm neo, typographic-hero) từ craft catalog
  2. Quyết định per-màn: composition/zones · visual hierarchy (#1..#4) · vai trò màu (bg/surface/accent/semantic) · type scale · nhịp spacing · elevation · motion/transition
  3. Chọn ≥1–3 signature moment/màn từ craft catalog, gắn vào điểm nhấn (hero, empty state, CTA, chuyển cảnh)
  4. Ghi rõ vì sao mỗi quyết định BÁM Style DNA (trace) và LỆCH khỏi iOS-stock (distinctiveness)
OUTPUT: nội dung cho screens/screen-[view].md (§4.7) + token/component cần có
GUARD : giữ SÀN UX; không đổi business logic; ưu tiên reuse component
```

### 4.10 `skills/ui-redesign-craft/SKILL.md` — kiến thức craft (mảnh sáng tạo)
- **Distinctiveness principles**: khi nào phá "clarity over decoration" của `ios-ui-ux` (được phép trong pha này) mà vẫn giữ SÀN.
- **Signature-moments catalog**: danh mục có tên (vd: hero-typography, layered-depth, expressive-empty-state, springy-transition, bold-border, gradient-wash…) — mỗi moment: mô tả, khi nào dùng, token/motion cần, chi phí a11y.
- **Vượt iOS-stock**: cách thay system-default (màu/blur/shadow/spring/shape) bằng token phong cách; checklist "còn generic không?".
- **Kế thừa** khái niệm distinctiveness/Signature Opportunities của `uiux-analysis-workflow` nhưng đưa xuống **code-time** (áp lên app đã build).

---

## 5. Cây output `specs/[project-name]/redesign/`
```
redesign/
├── README.md              # index người+AI: tóm tắt phong cách, read-order, bảng nguồn chân lý
├── redesign-state.json    # §4.4
├── style-reference.md     # ảnh + mô tả + Style DNA
├── current-ui-audit.md    # audit từ app đã build + screenshot before + gap vs DNA
├── design-tokens.md       # token mới + map token→shared/Styles/*.swift
├── components.md          # component mới + old→new + reuse tier
├── flows.md               # mermaid luồng redesigned
├── screens/screen-[view].md   # 1/màn (nguồn = Features/*/Views/*)
├── redesign-summary.md    # thay đổi, thứ tự migration, rủi ro, kết quả before/after
└── manifest.json          # §4.5
```

---

## 6. Verification
1. **Fixture**: dùng `test-agent/.claude/specs/Calo-AI` làm sân thử P1–P5; xác nhận sinh đúng cây `redesign/` + mermaid + token map + old→new + readability; **screen inventory lấy từ Views**, không phụ thuộc Wireframes.
2. **gate-redesign (trong contract)**: thiếu file / thiếu token-map / thiếu màn / mất SÀN UX / **thiếu signature moment / vẫn dùng #007AFF-system-default** → FAIL; đủ → PASS.
3. **Apply P6 + critique P7 trên 1 màn (DiaryView)**: token vào `shared/Styles/*.swift`; component mới đúng chỗ (Structure Gate); UX Compliance + DSS pass; `build_sim` xanh; **vòng screenshot-critique chạy ≥1 vòng và screenshot after có cá tính rõ (khác iOS-stock)**, ≠ before.
4. **Installer**: cài thử → `commands/ios-ui-redesign.md` + `skills/ui-redesign/` + `skills/ui-redesign-craft/` + `skills/ui-redesign-contract/` được copy; **`design-token/*.pen` được copy verbatim** (không hỏng binary) sang `{{IDE_CONFIG_DIR}}design-token/`; placeholder `{{IDE_CONFIG_DIR}}` thay đúng. Xác nhận KHÔNG có thay đổi nào ở project-docs.
5. **Pencil MCP intake**: chạy `--pen neo` → `get_editor_state(schema)` → `get_variables` rút được tokens → `design-tokens.md` có bảng map `.pen`→token→Swift; screenshot tham chiếu lưu trong `style-reference.md`. MCP không khả dụng → rơi vào E-2, không crash.
6. **Regression**: sau apply, app build/launch, không đổi hành vi (Integration Gate 5).

---

## 7. Guardrails
- Không code chức năng — chỉ skeleton/hợp đồng/schema.
- Chỉ ghi trong `/q-plan/` (blueprint này); path §2 là ĐỀ XUẤT cho bước thực thi sau.
- **Tách project-docs**: không sửa `project-docs-*`; gate tự chứa trong contract; nguồn màn = app đã build.
- **Contract không đủ để sáng tạo** → tách 4 vai: `ui-redesign` (cỗ máy sinh, Creative Method §4.9) · `ui-redesign-craft` (kiến thức craft + signature-moments) · `ui-redesign-contract` (validator + gate gồm distinctiveness bar) · vòng screenshot-critique P7 (đánh giá thẩm mỹ lặp).
- Đường đi DUY NHẤT & chắc chắn: 1 command + 3 skill (redesign / craft / contract) tự chứa; nguồn phong cách 3 kiểu (ảnh / mô tả / `.pen` qua Pencil MCP); tái dùng gate execution làm rào chắn; state cấp project; cầu nối `.pen`/JSON→token→`shared/Styles/*.swift` bắt buộc; installer copy `design-token/*.pen` verbatim.
```
