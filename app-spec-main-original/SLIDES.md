# Slide Deck — iOS Spec-Driven Development Toolkit

> File mô tả các màn slide giới thiệu dự án.
> Mỗi slide gồm: **Tiêu đề**, **Nội dung hiển thị**, và **Ghi chú thuyết trình**.
> Thời lượng đề xuất: ~15–20 phút · 18 slide.

---

## Tổng quan dự án

**Một câu (elevator pitch):**
*iOS Spec-Driven Development Toolkit là bộ công cụ biến AI thành một quy trình phát triển iOS có kỷ luật — dẫn dắt từ tài liệu sản phẩm, qua đặc tả tính năng, đến code SwiftUI, với truy vết đầy đủ từ yêu cầu đến từng dòng code.*

**Đoạn mô tả:**
Thay vì những cuộc trò chuyện AI rời rạc và khó kiểm soát, toolkit này áp một khung làm việc có cấu trúc gồm ba tầng — **tài liệu dự án → đặc tả tính năng → triển khai code**. Mỗi bước đều có template chuẩn, cổng phê duyệt của con người (Approve / Modify / Pause) và cổng chất lượng tự động. Điểm khác biệt cốt lõi là **traceability**: mọi yêu cầu (PRD, Use Case, Functional Requirement) được gắn ID ổn định và liên kết xuôi tới Acceptance Criteria, thiết kế, task và cuối cùng là code — có script kiểm tra tự động chặn mọi tham chiếu gãy. Toolkit được cài như một lớp cấu hình vào project và chạy được trên cả **Claude Code** lẫn **OpenCode**, tự động convert đúng định dạng cho từng IDE. Phần UI/UX được hỗ trợ bởi hệ thống design token và các MCP server (Pencil, Figma, Xcode) để nối liền thiết kế với code.

**Điểm nhấn:**
- **Có kỷ luật:** tốc độ của AI + sự kiểm soát của quy trình kỹ thuật.
- **Truy vết đầu-cuối:** từ nhu cầu thị trường tới từng dòng SwiftUI.
- **Nhất quán:** quality gate + design system dùng chung, không hardcode style.
- **Không khoá công cụ:** một nguồn nội dung, cài cho nhiều IDE.
- **Nhanh:** tài liệu ~15 phút, đặc tả ~10 phút, triển khai tự động theo phase.

---

## Slide 1 — Trang bìa

**Nội dung hiển thị**
- Tên: **iOS Spec-Driven Development Toolkit**
- Phụ đề: *Xây dựng ứng dụng iOS — Với AI có kỷ luật*
- Logo / tên nhóm · phiên bản `v3.2.0`

**Ghi chú**
- Một câu mở: "Thay vì chat AI rời rạc, chúng ta có một quy trình có cấu trúc từ tài liệu sản phẩm đến code production."

---

## Slide 2 — Vấn đề

**Nội dung hiển thị**
- Dùng AI code iOS hiện nay bị: prompt rời rạc, mất ngữ cảnh, không truy vết được yêu cầu → code.
- Không rõ *tại sao* một dòng code tồn tại; khó review, khó bàn giao.
- Thiếu chuẩn UI/UX, mỗi lần mỗi khác.

**Ghi chú**
- Nhấn "pain": AI viết nhanh nhưng không kiểm soát được chất lượng & tính nhất quán.

---

## Slide 3 — Giải pháp (tổng quan)

**Nội dung hiển thị**
- Một **toolkit** cài vào project, biến AI (Claude Code / OpenCode) thành một quy trình kỷ luật.
- 3 tầng: **Tài liệu dự án → Đặc tả tính năng → Triển khai code**.
- Cột sống: **Traceability** (truy vết xuyên suốt) + **Approval gates** (cổng phê duyệt).

**Ghi chú**
- Đây KHÔNG phải một app iOS — đây là bộ công cụ/quy trình dùng để *tạo ra* app iOS bằng AI.

---

## Slide 4 — 3 lệnh cốt lõi

**Nội dung hiển thị**

| Lệnh | Mục đích |
|---|---|
| `/ios-project-docs` | Tạo tài liệu dự án (PRD, Overview, Use Cases, FR, Wireframes, UX Flows, Roadmap) |
| `/ios-spec` | Tạo đặc tả tính năng (requirements → design → tasks) |
| `/ios-execute` | Triển khai code SwiftUI + test từ tasks đã duyệt |

**Ghi chú**
- Ngoài ra có cặp lệnh nhẹ độc lập `/quick-plan` + `/quick-implement` cho tác vụ nhanh (dùng CodeGraph MCP).

---

## Slide 5 — Kiến trúc 3 lớp

**Nội dung hiển thị**
- **Command** (điểm vào mỏng) → **Workflow skill** (điều phối) → **Contract skill** (luật chơi).
- Sơ đồ: `/lệnh` → `*-workflow` → gọi các sub-skill + `*-quality-gates`; tất cả tuân `*-contract`.

**Ghi chú**
- Contract định nghĩa: quy ước ID, ranh giới tài liệu, state machine, gate. Workflow chỉ chạy theo luật đó.
- 35 skill được cài, chia theo tầng.

---

## Slide 6 — Workflow 1: Tài liệu dự án

**Nội dung hiển thị**
- `/ios-project-docs MyApp` → chuỗi 7 tài liệu:
  PRD → Project_Overview → Use_Cases → Functional_Requirements → Wireframes → UX_Flows → Roadmap.
- Mỗi bước: đọc template → sinh nội dung → quality gate → hỏi **Approve / Modify / Pause**.
- PRD có nghiên cứu thị trường (Evidence Table ≥ nguồn có ngày & độ tin cậy).

**Ghi chú**
- Kết quả: nền tảng dự án hoàn chỉnh ~15 phút. Có nhánh phụ phân tích UI/UX.

---

## Slide 7 — Workflow 2: Đặc tả tính năng

**Nội dung hiển thị**
- `/ios-spec user-login` → `requirements.md` → `design.md` → `tasks.md`.
- State machine: `draft_requirements → approved_requirements → draft_design → approved_design → draft_tasks → approved_tasks → executing → done`.
- `spec-state.json` theo dõi trạng thái; không được nhảy bước.

**Ghi chú**
- `design.md` bị **chặn phê duyệt** nếu còn Acceptance Criteria chưa được thiết kế che phủ.

---

## Slide 8 — Workflow 3: Triển khai

**Nội dung hiển thị**
- `/ios-execute user-login` → Load Context → Execute Tasks → Verify → Commit.
- Chế độ **autopilot** (mặc định) / step-by-step.
- 5 phase gate: **Build · Test · Traceability · AC Coverage · Integration**.

**Ghi chú**
- Mỗi task là một "transaction": validate deps → in_progress → code → check → done/blocked → cập nhật traceability.

---

## Slide 9 — Traceability (trái tim của toolkit)

**Nội dung hiển thị**
- Chuỗi: `PRD Evidence → User Story → AC (EARS) → Design §/Property → Task → Code/Test`.
- Quy ước ID: `UC-XXX`, `FR-XXX`, `AC-XXX.Y`, `WF-XXX`, `P1/P2…`.
- `validate_traceability.py` **tự động fail** nếu task tham chiếu AC/design không tồn tại, hoặc thiếu ref.

**Ghi chú**
- Đây là điểm khác biệt lớn nhất: mọi dòng code đều truy về được yêu cầu gốc.

---

## Slide 10 — Chuẩn EARS cho Acceptance Criteria

**Nội dung hiển thị**
- `WHEN [sự kiện] THEN THE SYSTEM SHALL [phản hồi]`
- `IF [điều kiện] THEN THE SYSTEM SHALL [phản hồi]`
- `WHILE [trạng thái] THE SYSTEM SHALL [phản hồi]`

**Ghi chú**
- AC viết theo EARS → kiểm thử được, không mơ hồ → làm nền cho property-based testing (SwiftCheck).

---

## Slide 11 — Hệ thống thiết kế (Design System)

**Nội dung hiển thị**
- `DESIGN_SYSTEM_GUIDE` + 10 bộ **design token** (Glassmorphism, Neobrutalism, Bento Grid, Aurora, Motion First, Dark-mode First, …).
- Token gồm: color / typography / spacing / border / shadow / animation / component / composition.
- Rút "Product DNA" từ PRD → chọn/tùy biến một hệ.

**Ghi chú**
- DSS gate: UI task **không hardcode** style; token nguồn ở `shared/Styles/*.swift`.

---

## Slide 12 — Thiết kế UI với Pencil & MCP

**Nội dung hiển thị**
- **Pencil** (CLI/MCP): sinh file `.pen` + export ảnh màn hình.
- **Framelink Figma MCP**: rút token/spec từ Figma → SwiftUI style files.
- **XcodeBuildMCP**: cổng build/screenshot/UI-automation trong autopilot.

**Ghi chú**
- Design không phải trang trí: token truy về yêu cầu, hiện thực thành mockup, map vào style system dùng chung.

---

## Slide 13 — Đa IDE: Claude Code & OpenCode

**Nội dung hiển thị**
- Một nguồn nội dung, cài cho 2 IDE: `--ide claude` → `.claude/` · `--ide opencode` → `.opencode/`.
- Installer tự **convert đúng format**:
  - Claude: skills + `.mcp.json` + permission rules `mcp__server__tool`.
  - OpenCode: agent `tools:` → `permission:` YAML.

**Ghi chú**
- Có kiểm tra format tự động: chặn cấu hình sai (vd MCP đặt nhầm chỗ, key không chuẩn).

---

## Slide 14 — Yêu cầu môi trường

**Nội dung hiển thị**

*Nền tảng & runtime cho installer*
- **macOS** (bắt buộc — build iOS + Pencil chỉ chạy trên macOS; MCP Pencil dùng binary `darwin-arm64`).
- **Python ≥ 3.8** · installer phụ thuộc `click ≥ 8.0` + `rich ≥ 13.0`.
- **UV / uvx** — công cụ chạy & cài installer.
- **Node.js + npx** — chạy các MCP server (Figma, XcodeBuildMCP). Dự án không pin version; các gói MCP cần **Node ≥ 18**, khuyến nghị **LTS 20/22**.
- **Git** — commit & chạy validate traceability.

*IDE (chọn 1)*
- **Claude Code** hoặc **OpenCode**.

*Bộ công cụ iOS (khi triển khai code)*
- **Xcode + iOS Simulator** (target **iOS 15+**, SwiftUI + MVVM).
- **SwiftCheck ≥ 0.12.0** cho property-based testing (thêm qua SPM).

*MCP & khoá API (tuỳ tính năng, mặc định tắt)*
- **Framelink Figma MCP** → cần `FIGMA_TOKEN`.
- **XcodeBuildMCP** (không cần key) · **MiniMax** → `MINIMAX_API_KEY`.
- **Pencil.app** cài sẵn cục bộ (cho MCP `pencil`).
- OpenCode có thêm **exa / tavily** (web search) → cần key riêng.

**Ghi chú**
- Tối thiểu để chạy 3 lệnh cốt lõi: macOS + Python/UV + IDE. Xcode/Figma/Pencil chỉ cần khi tới bước build/design tương ứng.
- Mọi MCP server đều **off-by-default** — người dùng tự bật + nạp key khi cần.

---

## Slide 15 — Cài đặt

**Nội dung hiển thị**
- Yêu cầu: cài **UV** trước.
- Lệnh:
  ```bash
  uvx --from 'git+...app-spec.git@main' ios-spec-driven install
  ```
- Chọn IDE (Claude Code / OpenCode) → xong.

**Ghi chú**
- `status` / `uninstall` / `info` để quản lý; có backup tự động khi cài đè.

---

## Slide 16 — Demo: Mood Tracker

**Nội dung hiển thị**
- Ví dụ chạy end-to-end trong `test-agent/`.
- Từ specs (PRD → Use Cases → FR → Wireframes) → thiết kế Pencil `.pen` → 10 mockup màn hình.

**Ghi chú**
- Cho khán giả xem ảnh `screens/*.png` để minh hoạ kết quả thật.

---

## Slide 17 — Lợi ích

**Nội dung hiển thị**
- Truy vết đầy đủ: yêu cầu ↔ code, dễ review & bàn giao.
- Chất lượng nhất quán: quality gate + design system chung.
- Nhanh: docs ~15', spec ~10', execute tự động theo phase.
- Không khoá IDE: chạy cả Claude Code lẫn OpenCode.

**Ghi chú**
- Nhấn: "kỷ luật hoá" AI — tốc độ của AI + kiểm soát của quy trình kỹ thuật.

---

## Slide 18 — Kết luận & bước tiếp

**Nội dung hiển thị**
- Toolkit spec-driven cho iOS: từ ý tưởng → tài liệu → spec → code có truy vết.
- Bước tiếp: cài vào project của bạn → `/ios-project-docs` → `/ios-spec` → `/ios-execute`.
- Q&A.

**Ghi chú**
- Kêu gọi hành động: chọn một tính năng nhỏ, chạy trọn workflow để cảm nhận.
