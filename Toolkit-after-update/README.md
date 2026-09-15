# Pipeline v2 — bộ tài liệu sản phẩm mobile app

**Bộ mẫu v1.0** · 14 phase · 61 tài liệu · 12 cổng · kết thúc ở **gói bàn giao Dev**.

> `Pipeline v2` là tên phương pháp. `v1.0` là bản đóng gói của bộ mẫu này.
> Xem `.claude/KIT_MANIFEST.md` để biết chính xác bản mình đang dùng.

Dựng từ 11 skill UX của team, cộng 5 skill lấp khoảng trống, cộng engine chấm cổng và tài nguyên thiết kế
lấy từ bộ app-spec.

## Hai tài nguyên dùng chung, ít ai để ý

`.claude/agents/ask.md` — subagent **chỉ đọc**, không sửa được file nào. Dùng khi muốn hỏi hoặc nghiên cứu
mà chắc chắn không muốn nó chạm vào tài liệu: gõ trong Claude Code *"dùng agent ask để …"*.

`.claude/shared/DESIGN_SYSTEM_GUIDE.md` — hướng dẫn design system, dùng ở phase 12 khi viết
`12-02_DESIGN_SYSTEM_AND_A11Y`.

`.claude/scripts/validate_docs.py` — kiểm **tài liệu**: front-matter, mục theo manifest, ID mồ côi, ID trích
mà chưa cấp, định mức khối lượng ở phase 01–04, **định mức chiều sâu ở phase 06**, **đầu vào mới hơn tài liệu**
(tài liệu `approved` mà `depends_on` đã sửa sau đó), và khối JSON thứ tự thi công ở `13-01`.

`.claude/scripts/check_build.py` — đối chiếu **wireframe** hoặc **bản đã dựng** với `08-01` (kiểm kê màn
hình) và `08-02` (ma trận trạng thái): màn thiếu, màn thừa, trạng thái thiếu, tên sai mã.

```
python .claude/scripts/check_build.py --wireframes wireframes/   phase 08, điều kiện G7
python .claude/scripts/check_build.py --frames build.pen         phase 12, điều kiện G10
python .claude/scripts/check_build.py --frames frames.txt        nhánh Figma
```

`wireframes/` — đầu ra phase 08 là **wireflow**: một trang HTML cho một luồng, các màn xếp cạnh nhau, nối
bằng **mũi tên có nhãn "bấm gì"**, nhánh có nhãn **"điều kiện nào"**. Mở một trang là thấy trọn luồng và biết
ngay chỗ nào dư bước, chỗ nào không có đường ra.

Xem thử: `python -m http.server 8000` → `http://localhost:8000/wireframes/`

Wireflow trả lời **bốn câu**, và chỉ bốn câu: màn này phục vụ chức năng gì · vào từ màn nào · bấm gì ra màn
nào · tình huống nào ra trạng thái nào. Khoảng cách, cỡ chữ, màu là việc của `12-00`. Nút **không bấm được** —
điều hướng nằm ở mũi tên.

`/import-legacy` — nạp một bộ tài liệu hoàn chỉnh từ bộ khác vào bộ này. Tám bước, hai bước không được bỏ:
**lập bản đồ phủ trước khi lấp** và **soi mâu thuẫn trong hồ sơ cũ**. File cũ nằm ở `research-raw/ho-so-cu/`,
**không bao giờ dán vào `docs/`**, và **không đánh số lại ID cũ**.

`/design-ui` — lệnh dựng UI ở phase 12: hỏi công cụ (Pencil / Figma), dựng theo lô, dừng cho bạn nghiệm thu
từng lô. File ở `.claude/commands/design-ui.md`, là markdown thuần nên Codex và OpenCode dùng được y hệt.

## Dùng cho dự án mới

1. Copy toàn bộ thư mục này, đổi tên theo dự án. Ví dụ `D:\PROJECTS\CalorieSnap`.
2. **Không cần điền `CLAUDE.md` bằng tay.** Lần chạy đầu Claude phát hiện bốn chỗ trống, tự hỏi rồi tự điền.
3. Copy `.mcp.example.json` thành `.mcp.json`, điền khoá Figma nếu dùng.
4. Mở PowerShell trong thư mục đó, gõ `claude`.
5. Gõ `/design-docs CalorieSnap`.

## Chuỗi 14 phase

```
00 Khởi tạo & khoá phạm vi        G0
01 Thị trường & need zone      ┐  G1
02 Nghiên cứu đối thủ          ┘
03 Chấm điểm & kiểm chứng cơ hội  G2   ← không đạt 25/35 thì DỪNG
04 Định nghĩa người dùng          G3
05 PRD                            G4
06 Phân rã yêu cầu                G5
07 UX research, IA & UX flow      G6
08 Kiểm kê màn hình & wireframe   G7
09 Onboarding, monetization    ┐  G8
10 Đo lường                    ┘
11 Đánh giá trước khi dựng UI     G9
12 UI research → Prototype        G10   ← 12-00 chốt hướng, rồi /design-ui dựng theo lô
13 Bàn giao Dev                   G11
```

Song song: `tech-input/` — Dev nộp tài liệu kỹ thuật.

## Cấu trúc

```
.
├── CLAUDE.md
├── .mcp.example.json          copy thành .mcp.json rồi điền khoá
├── .claude/
│   ├── commands/              /design-docs
│   ├── skills/                14 skill phụ trách tài liệu + 3 engine
│   │   └── _depth/            skill chiều sâu, gắn theo phase
│   ├── doc-templates/         61 template kèm QUALITY-GATE-MANIFEST
│   ├── shared/  design-token/  agents/
│   └── KIT_MANIFEST.md        phiên bản bộ mẫu này
├── AGENTS.md                  cửa vào cho Codex / OpenCode
├── docs/                      ← tài liệu sinh ra ở đây
│   ├── _INDEX.md              bảng điều khiển — mở đọc mỗi tuần
│   ├── _ID_REGISTRY.md  _GATE_CHECKLIST.md  _DECISION_LOG.md
│   ├── _CHANGE_LOG.md  _OPEN_QUESTIONS.md  _ASSUMPTION_REGISTER.md
│   ├── _GLOSSARY.md  _DOCUMENTATION_STANDARD.md
│   └── 00-khoi-tao/ … 13-handover/
├── tech-input/                Dev nộp vào đây
├── design-system/             hệ thiết kế bạn dựng sẵn (Pencil / Figma) — AI đọc, không sửa
├── wireframes/                wireflow HTML — màn nối bằng mũi tên, xem trên trình duyệt
└── research-raw/              BẠN nạp nguyên liệu thô
    ├── ho-so-cu/              bộ tài liệu hoàn chỉnh từ bộ khác → /import-legacy
    ├── thu-hoach/             dữ liệu công cụ khác đi đào về
    ├── sensor-tower/          số liệu tra tay
    ├── man-hinh-doi-thu/      ảnh màn hình đối thủ, mỗi app một thư mục
    └── moodboard/             ảnh tham chiếu UI cho phase 12
```

## Hai loại skill

**Skill phụ trách tài liệu** — 14 cái, mỗi phase một cái, sở hữu tài liệu `PP-NN`, gọi cổng, cấp ID.
Bộ này cố định. Thêm vào đây thì đắt: dùng `add_doc.py`.

**Skill chiều sâu** — nằm ở `.claude/skills/_depth/<phase>/`, không sinh tài liệu, không có cổng.
Thêm chỉ là thả thư mục vào đúng phase. Xem `_depth/README.md`.

Thêm kiến thức cho skill cũ: thả file `.md` vào `references/` của skill đó. Không phải sửa `SKILL.md`.

## Cập nhật bộ mẫu

Bộ này là **kết quả build**, không phải nơi sửa tay. Sửa ở nguồn rồi chạy lại:

```
python build_kit.py --appspec <đường-dẫn-app-spec> --new ./new --out <đích> --force
```

Dự án đang chạy **không** tự cập nhật theo — chủ ý, vì tài liệu phải đọc được bằng đúng chuẩn đã sinh ra nó.
Mỗi dự án ghi phiên bản bộ mẫu trong `.claude/KIT_MANIFEST.md`.

## Commit gì vào git

Bắt buộc: `docs/` — tài sản duy nhất không tái tạo được.
Nên: `.claude/skills/` và `.claude/doc-templates/` — để sáu tháng sau vẫn đọc được tài liệu bằng đúng chuẩn.
Không: `.mcp.json` (chứa khoá) — đã có trong `.gitignore`.
