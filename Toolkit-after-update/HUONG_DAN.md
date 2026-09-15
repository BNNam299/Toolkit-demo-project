# Hướng dẫn sử dụng — Pipeline v2 · bộ mẫu v1.0

Viết cho người chưa từng dùng. Không cần biết lập trình. Đường dẫn dưới đây là ví dụ, bạn đổi được.

`Pipeline v2` là tên quy trình. `v1.0` là bản đóng gói của bộ mẫu bạn đang cầm.

---

## Mục lục

1. [Ba thứ cần phân biệt](#1)
2. [Cài đặt lần đầu](#2)
3. [Chạy trong VS Code](#3)
4. [Bắt đầu dự án khi chưa có ý tưởng gì](#4)
5. [Bắt đầu khi đã có ý tưởng sẵn](#5)
6. [Nhịp làm việc hằng ngày](#6)
7. [Brainstorm với Claude Code](#7)
8. [Thoát rồi quay lại](#8)
9. [Làm việc với Dev](#9)
10. [Wireflow rồi sang UI](#10)
11. [Khi cổng fail](#11)
12. [Sửa tài liệu đã duyệt](#12)
13. [Bỏ bớt tài liệu hoặc cổng](#13)
14. [Nhiều dự án cùng lúc](#14)
15. [Thêm và cập nhật skill](#15)
16. [Sự cố thường gặp](#16)

---

<a name="1"></a>
## 1. Ba thứ cần phân biệt

**Bộ mẫu** — thư mục gốc chứa skill, template, quy trình. Để một chỗ, **không bao giờ làm việc trực tiếp trong đó**.
Giống khuôn bánh.

**Dự án** — bản sao của bộ mẫu, đổi tên theo app. Mỗi app một bản riêng. Đây là nơi bạn làm việc. Giống cái bánh.

**Claude Code** — chương trình chạy trong cửa sổ dòng lệnh. Mở nó *bên trong* thư mục dự án rồi gõ lệnh.

Vì mỗi dự án là bản sao độc lập nên sửa hỏng một dự án không ảnh hưởng dự án khác, và cập nhật bộ mẫu
không tự lan sang dự án đang chạy. Đây là chủ ý.

---

<a name="2"></a>
## 2. Cài đặt lần đầu

Làm một lần trên máy.

**Cài Claude Code.** Mở PowerShell:

```
npm install -g @anthropic-ai/claude-code
claude --version
```

Báo lỗi không tìm thấy `npm` thì cài Node.js tại nodejs.org trước, đóng PowerShell, mở lại.

**Cài Python.** Tải tại python.org, **tick ô "Add Python to PATH"** khi cài.

```
python --version
```

**Đặt bộ mẫu.** Tạo `D:\TOOLKIT`, giải nén bộ mẫu vào đó thành `D:\TOOLKIT\pipeline-v2\`.
Từ giờ không mở, không sửa thư mục này.

---

<a name="3"></a>
## 3. Chạy trong VS Code

Chạy trong PowerShell thuần vẫn được, nhưng bạn sẽ không thấy dự án. VS Code cho bạn cây 61 tài liệu ở
bên trái, nội dung ở giữa, Claude Code ở dưới.

### Điều quan trọng nhất phải biết trước

> **Chạy Claude Code trong terminal tích hợp, không dùng khung chat của extension.**
> Extension có khung chat riêng, nhưng theo tài liệu Anthropic thì khung đó **chỉ hỗ trợ một tập con**
> các command và skill, còn CLI hỗ trợ đủ. `/design-docs` là command tự tạo trong `.claude/commands/`
> nên có thể không xuất hiện trong khung chat.
>
> Cách chắc ăn: mở thư mục dự án bằng VS Code để **nhìn**, rồi gõ `claude` trong terminal tích hợp để **chạy**.

### Cài VS Code và extension

Tải tại code.visualstudio.com, cần bản **1.94 trở lên**.

`File → Open Folder`, chọn `D:\PROJECTS\HealthApp`. Lần đầu mở, chọn **Yes, I trust the authors**
vì bộ có script Python.

Bộ đã có sẵn `.vscode/extensions.json` nên VS Code sẽ hiện gợi ý cài extension — bấm **Install All**:

| Extension | Vì sao cần |
| --- | --- |
| Claude Code | tích hợp, xem diff trong IDE khi Claude sửa file |
| Markdown All in One | preview, phím tắt, mục lục tự động |
| Markdown Preview Mermaid Support | **xem được sơ đồ** trong `07-05_UX_FLOWS`, `07-03_SITEMAP` |
| markdownlint | bắt lỗi định dạng markdown |
| YAML | kiểm khối front-matter 13 trường |

Thiếu extension Mermaid thì sơ đồ UX flow hiện ra dạng khối chữ thay vì hình vẽ.

### Bố trí màn hình

```
┌───────────────┬──────────────────────┬─────────────────────┐
│  Cây thư mục  │  Tài liệu đang mở    │  Preview markdown   │
├───────────────┴──────────────────────┴─────────────────────┤
│  Terminal — claude đang chạy ở đây                         │
└─────────────────────────────────────────────────────────────┘
```

1. Mở terminal tích hợp: `Ctrl` + dấu huyền. Kéo cao khoảng một phần ba màn hình.
2. Gõ `claude`. Không cần `cd` vì terminal mở sẵn ở thư mục dự án.
3. Mở một tài liệu trong `docs/`, bấm `Ctrl+K` rồi `V` để mở preview sang bên.

### Năm phím tắt dùng nhiều nhất

| Phím | Làm gì | Dùng khi nào |
| --- | --- | --- |
| `` Ctrl+` `` | bật/tắt terminal | chuyển giữa đọc và nói với Claude |
| `Ctrl+P` | mở nhanh file theo tên | gõ `06-02` là nhảy tới ngay |
| `Ctrl+Shift+F` | **tìm trong toàn bộ dự án** | tra một mã ID xem xuất hiện ở đâu |
| `Ctrl+K` rồi `V` | mở preview sang bên | đọc tài liệu, xem sơ đồ Mermaid |
| `Ctrl+Shift+O` | nhảy tới mục trong file | tài liệu dài |

> **Phím quan trọng nhất là `Ctrl+Shift+F`.** Bộ có 61 tài liệu nối nhau bằng ID. Muốn biết `FR-014`
> dùng ở đâu hay `SCR-012` xuất hiện trong flow nào thì tìm toàn dự án là nhanh nhất. Đây cũng là cách
> tự kiểm mồ côi bằng tay: tìm một mã mà chỉ ra đúng một chỗ thì nó đang mồ côi.

### Nhìn dự án qua cây thư mục

```
HealthApp/
├── CLAUDE.md              ← quy tắc, sửa lúc đầu
├── HUONG_DAN.md           ← tài liệu này
├── .claude/               ← bộ não, không sửa
├── docs/                  ← TÀI LIỆU SINH RA Ở ĐÂY
│   ├── _INDEX.md          bảng điều khiển, mở mỗi tuần
│   ├── _GATE_CHECKLIST.md 12 cổng
│   └── 00-khoi-tao/ … 13-handover/
├── tech-input/            ← Dev nộp vào đây
├── design-system/         ← hệ thiết kế bạn dựng sẵn (Pencil / Figma)
└── research-raw/          ← BẠN bỏ nguyên liệu thô vào đây
```

Bốn thư mục cần để mắt: `docs/` là kết quả công việc, `tech-input/` là chỗ Dev nộp, `design-system/` là hệ
thiết kế của bạn, `research-raw/` là nguyên liệu thô. Ba thư mục sau là **tài sản của bạn và của Dev** —
Claude đọc, không sửa. Muốn chứa export từ Figma thì tự tạo thêm `design/`, bộ không tạo sẵn.

### Xem Claude sửa gì

Chạy `claude` trong terminal tích hợp thì Claude Code tự nối với VS Code. Mỗi lần sửa file, bạn thấy
**so sánh hai bên** ngay trong IDE trước khi quyết định cho sửa.

Đã `git init` thì cột bên trái editor hiện vạch màu ở dòng vừa đổi, và tab **Source Control** cho xem
toàn bộ thay đổi trước khi commit.

### Mở lại dự án hôm sau

`File → Open Recent`, bật terminal bằng `Ctrl` + dấu huyền, rồi:

```
claude
/design-docs HealthApp --continue
```

---

<a name="4"></a>
## 4. Bắt đầu dự án khi chưa có ý tưởng gì

Đây là kịch bản đầy đủ nhất — bạn chỉ có một lĩnh vực quan tâm, chưa biết làm app gì.

**Bước 1 — Tạo thư mục dự án.** Copy `D:\TOOLKIT\pipeline-v2` sang `D:\PROJECTS`, đổi tên thành tên tạm.
Chưa có ý tưởng thì đặt theo lĩnh vực, ví dụ `HealthApp`.

```
xcopy /E /I "D:\TOOLKIT\pipeline-v2" "D:\PROJECTS\HealthApp"
```

**Bước 2 — Không cần điền gì bằng tay.** `CLAUDE.md` có bốn chỗ trống là tên, nền tảng, mô tả và profile.
**Claude tự phát hiện và tự hỏi bạn** ở lần chạy đầu tiên, rồi tự điền. Bạn chỉ cần trả lời bốn câu.

Muốn điền tay vẫn được — mở `CLAUDE.md` bằng Notepad, sửa bốn dòng đầu. Nhưng để Claude hỏi thì tốt hơn,
vì bốn câu đó trùng với những câu phase 00 sẽ hỏi, và nó điền luôn vào `docs/_INDEX.md` cho khớp.

**Bước 3 — Mở Claude Code.**

```
cd D:\PROJECTS\HealthApp
claude
```

Kiểm dòng hiển thị thư mục hiện tại — phải là `D:\PROJECTS\HealthApp`.

**Bước 4 — Lệnh đầu tiên.**

```
/design-docs HealthApp
```

Claude đọc `CLAUDE.md`, hỏi bạn chọn profile nếu chưa ghi, rồi bắt đầu **phase 00** — hỏi về vấn đề,
người dùng, ràng buộc, định nghĩa thành công. Nó viết `00-01_PROJECT_BRIEF.md` rồi dừng.

**Bước 5 — Đi tiếp.** Approve xong, nó sang `00-02_SCOPE_LOCK.md`. Đây là lúc bạn phải điền
**danh sách bị cấm** — cổng G0 không đóng nếu để trống. Ghi thẳng những thứ không muốn dính vào, ví dụ
backend riêng, hệ thống tài khoản, đồng bộ đám mây.

**Bước 6 — Phase 01 tới 03.** Claude đào pain point từ store, Reddit, keyword; lập bản đồ đối thủ;
chấm Need Score. Đây là phần tốn thời gian nhất và cũng đáng nhất.

**Bước 7 — Giữa phase 03, gửi Dev nghiên cứu công nghệ.** Ngay sau khi chốt concept ở `03-02`, Claude viết
`03-05_TECH_FEASIBILITY_BRIEF.md`: liệt kê **năng lực cốt lõi** mà concept phụ thuộc (`CAP-001`, `CAP-002`…)
và câu hỏi cụ thể cho Dev. Bạn gửi file đó cùng `tech-input/TECH-00_FEASIBILITY_SCREEN.md` cho Dev.

Trong lúc Dev nghiên cứu, bạn chạy tiếp `03-03` và `03-04` để kiểm chứng nhu cầu. **Hai việc song song,
không xếp hàng.** Dev trả `TECH-00` về thì Claude điền vào `03-05` mục 5.

> **Cổng G2 là điểm dừng quan trọng nhất trong cả chuỗi, và nó có HAI điều kiện dừng độc lập.**
>
> *Nhu cầu:* không cluster nào đạt Need Score 25/35 → **dừng dự án**.
>
> *Công nghệ:* có `CAP` **cốt lõi** bị Dev phán quyết **KHÔNG KHẢ THI** → **dừng dự án hoặc xoay concept**.
>
> Ghi quyết định vào `_DECISION_LOG.md`. Dừng ở đây là thắng — bạn vừa tiết kiệm cả phase 04 nghiên cứu
> người dùng và phase 05 viết PRD. Đây chính là lý do nghiên cứu công nghệ phải nằm ở phase 03 chứ không
> phải sau khi PRD đã xong.

**Bước 8 — Qua được G2 thì đổi profile.** Mở `docs/_INDEX.md` mục 1, đổi từ Lean sang MVP, rồi chạy tiếp.

---

<a name="5"></a>
## 5. Bắt đầu khi đã có ý tưởng sẵn

Vẫn làm phase 00. Nhưng phase 01–03 chạy nhanh hơn vì bạn đã có định hướng — Claude sẽ dùng phase đó
để **kiểm chứng** ý tưởng chứ không phải tìm ý tưởng.

Đừng bỏ phase 03. Ý tưởng bạn tin chắc là ý tưởng đáng chấm điểm nhất.

Nếu đề bài do người khác giao và bạn không có quyền dừng, vẫn chạy phase 03 nhưng ghi rõ ở
`_DECISION_LOG.md` rằng kết quả chấm điểm chỉ để tham khảo, không dùng để dừng.

### Nếu đã có nghiên cứu sẵn từ trước

Bỏ hết file cũ vào `research-raw/` rồi đọc `research-raw/README.md` — trong đó có sẵn câu prompt để Claude
**lập bản đồ phủ trước, chưa viết gì**. Có bản đồ rồi mới lấp từng tài liệu, theo thứ tự phase.

Điều phải nói rõ khi lấp: *"chỉ dùng nội dung có trong research-raw, không bổ sung kiến thức chung của bạn"*.
Không có câu đó, Claude điền chỗ trống bằng thứ nghe hợp lý và bạn mất khả năng phân biệt đâu là dữ liệu thật.

### Nếu phải tra số tay ở công cụ Claude không vào được

Ví dụ Sensor Tower: tài khoản không dùng được qua extension điều khiển browser.

Cách làm là **để Claude khai thác hết những nguồn nó vào được trước** — trang store, review, cộng đồng,
Google Trends, AppStoreSpy — rồi mới sinh **một phiếu duy nhất** `research-raw/SENSOR_TOWER_REQUEST.md` ghi
rõ cần số gì, của app nào, ở nước nào, và **con số đó trả lời câu hỏi gì**. Bạn tra một lần, dán vào
`SENSOR_TOWER_DATA.md`.

Đừng để nó hỏi lẻ từng con số qua nhiều lượt — bạn sẽ mở đóng tab hàng chục lần. Câu để bắt nó làm đúng:

```
Khai thác hết những nguồn bạn vào được trước.
Xong rồi sinh MỘT phiếu research-raw/SENSOR_TOWER_REQUEST.md cho những gì tôi phải tra tay.
Mỗi chỉ số phải ghi rõ nó trả lời câu hỏi gì và điền vào tài liệu nào.
Chỉ số nào không trả lời câu hỏi nào thì bỏ. Đánh dấu chỉ số nào bắt buộc để đóng cổng.
```

Cột *bắt buộc để đóng cổng* cho bạn biết chỗ nào được phép bỏ trống. Chỉ số nào công cụ **không có** thì
ghi thẳng *"không có trong công cụ"*, đừng để trống — trống thì Claude không phân biệt được *chưa tra* với
*tra rồi mà không có*.

Số của Sensor Tower và AppStoreSpy là **ước lượng**, sai số với app nhỏ có thể rất lớn. Dùng để **so tương
đối giữa các app**, không dùng để tính doanh thu dự kiến của mình.


### Trường hợp đã có cả một bộ tài liệu từ bộ khác

Khác hẳn với nghiên cứu rời. Bộ cũ có **hệ mã ID riêng** — `WF`, `TF`, `ERR`, `VR` — và chính hệ mã đó là chỗ
dễ phá truy nguyên nhất. Có lệnh riêng cho việc này:

```
/import-legacy bản đồ
```

Đặt file cũ vào `research-raw/ho-so-cu/`, **nguyên vẹn, không sửa**. Rồi Claude làm tám bước, trong đó hai
bước không được bỏ:

**Lập bản đồ phủ trước khi lấp một dòng nào.** Với từng tài liệu trong `_INDEX`, nội dung đã có ở file nào,
mức phủ đủ / một phần / không có, và **có dẫn nguồn hay không**. Cột cuối là cột quan trọng nhất: hồ sơ cũ
thường rất chắc ở chỗ có nguồn và **bịa hoàn toàn** ở chỗ không có nguồn, mà đọc bề ngoài hai chỗ giống nhau.

**Soi mâu thuẫn trong hồ sơ cũ.** Bốn phép soi, và phép thứ hai là phép đáng nhất: *định vị sản phẩm hiện tại
so với persona* — persona có đang mô tả đúng sản phẩm, hay mô tả một sản phẩm đã bị bỏ từ bản trước? Tôi tìm
thấy đúng lỗi này trong một dự án thật, và nếu nạp mà không soi thì mâu thuẫn được sao chép nguyên vẹn rồi
trông chính danh vì đã qua cổng.

> **Bốn quy tắc bất di bất dịch:** không dán file cũ vào `docs/` · **không đánh số lại ID cũ** (có `FR-066`
> thì cấp mới từ `FR-067`) · prefix lạ phải đổi kèm bảng ánh xạ từng mã · **không kế thừa `approved`** —
> bản lấp đầu tiên luôn là `draft`.

Ba thứ gần như chắc chắn **không lấp được**, phải làm mới: tầng bằng chứng dưới persona (nếu không còn bản ghi
phỏng vấn thì ghi rõ **proto-persona**) · `03-05` khả thi công nghệ (cần Dev trả lời qua `TECH-00`) ·
`12-00` nghiên cứu UI (cần moodboard).

Phiếu công tác ở `research-raw/ho-so-cu/_MAP.md` — bạn và Claude cùng điền.

---

<a name="6"></a>
## 6. Nhịp làm việc hằng ngày

**Mỗi lượt Claude chỉ viết một tài liệu rồi dừng.** Không phải nó chậm hay lỗi — đó là quy tắc cố ý.

Sau mỗi tài liệu, Claude báo:

```
Tài liệu: 06-02 Functional Requirements
Cổng G5: PASS
ID mới cấp: FR-001 … FR-014
Mâu thuẫn phát hiện: FR-009 mâu thuẫn với BR-003 về quy tắc reset

Approve / Modify / Pause
```

**Approve** — đã đọc và đồng ý. **Modify** — nói chỗ cần sửa. **Pause** — dừng.

Đọc thật rồi mới Approve. Bấm cho nhanh là cách chắc chắn nhất để có bộ tài liệu đẹp mà sai.

**Mở `docs/_INDEX.md` mỗi tuần.** Năm phút đọc bảng điều khiển phát hiện vấn đề sớm hơn đọc từng tài liệu.

---

<a name="7"></a>
## 7. Brainstorm với Claude Code

Không phải phần nào cũng nên để Claude viết thẳng ra tài liệu. Có những chỗ bạn cần **bàn trước, chốt sau** —
và đây là chỗ bộ này dễ bị dùng sai nhất: hỏi một câu, Claude viết luôn một tài liệu sáu trang, bạn đọc thấy
hay hay nên Approve, rồi ba phase sau mới nhận ra hướng đi đã lệch từ đầu.

### Câu thần chú: "Đừng viết file"

Claude mặc định hướng tới việc sinh tài liệu. Muốn bàn thì phải nói rõ, ngay câu đầu:

```
Đừng viết file nào cả. Tôi muốn bàn trước.
```

Giữ câu đó ở đầu mỗi lượt trao đổi cho tới khi bạn thật sự muốn chốt. Bỏ câu đó ra là nó viết.

### Ba kiểu brainstorm hay dùng

**Kiểu 1 — Mở rộng lựa chọn.** Khi bạn mới có một hướng và sợ bị đóng khung quá sớm.

```
Đừng viết file. Cho tôi 5 hướng khác nhau cho <vấn đề>, mỗi hướng 3 dòng:
giải quyết cho ai, khác biệt ở đâu, rủi ro lớn nhất là gì.
Đừng khuyên tôi chọn cái nào vội — tôi muốn thấy dải lựa chọn trước.
```

**Kiểu 2 — Phản biện.** Khi bạn đã thích một hướng và cần ai đó đấm thử. Đây là lúc dùng Claude đáng giá nhất.

```
Đừng viết file. Tôi đang nghiêng về <hướng>.
Đóng vai người phản đối: 5 lý do mạnh nhất khiến hướng này thất bại.
Với mỗi lý do, nói rõ tôi kiểm chứng bằng cách nào trước khi tốn tiền.
Đừng an ủi tôi.
```

**Kiểu 3 — Khoan sâu một điểm.** Khi bạn biết vấn đề nằm ở đâu nhưng chưa gọi tên được.

```
Đừng viết file. Hỏi tôi từng câu một để làm rõ <chủ đề>.
Mỗi lượt một câu. Câu sau dựa trên câu trả lời trước.
Khi thấy tôi trả lời mâu thuẫn với điều tôi nói trước đó thì chỉ ra ngay.
```

Cụm **"mỗi lượt một câu"** quan trọng. Không có nó, Claude hỏi dồn tám câu và bạn trả lời qua loa cả tám.

### Chốt lại — bước không được bỏ

Bàn xong mà không ghi thì coi như chưa bàn. **Quyết định chỉ nằm trong hội thoại là quyết định đã mất.**

```
Chốt lại buổi bàn này:
- Điều tôi đã quyết → ghi DEC vào docs/_DECISION_LOG.md, kèm lý do và phương án đã loại
- Điều còn treo → docs/_OPEN_QUESTIONS.md
- Điều tôi đang tạm tin mà chưa có bằng chứng → docs/_ASSUMPTION_REGISTER.md, gắn [ASM]
Đọc lại cho tôi ba danh sách đó trước khi ghi.
```

Câu cuối — *đọc lại trước khi ghi* — bắt được chỗ Claude hiểu sai ý bạn, lúc sửa còn rẻ.

Ghi xong mới quay lại `/design-docs`. Tài liệu viết sau đó sẽ **dùng lại** các `DEC` này thay vì bịa lại
từ đầu.

### Phase nào nên brainstorm, phase nào không

| Phase | Nên brainstorm | Vì sao |
| --- | --- | --- |
| 00 khởi tạo | **Rất nên** | danh sách bị cấm sai từ đây thì cả chuỗi lệch |
| 01–02 thị trường, đối thủ | Không | đây là việc đào bằng chứng, không phải việc nghĩ |
| 03 cơ hội | **Rất nên** | đây là chỗ dừng dự án, phải cãi cho ra nhẽ |
| 04 người dùng | Không | tổng hợp từ dữ liệu, bàn thêm chỉ làm nhiễu |
| 05 PRD | Nên, ở phần scope | ranh giới MVP là quyết định, không phải suy luận |
| 06–08 breakdown, cấu trúc, màn hình | Không | đã có đầu vào rõ, cứ chạy tuần tự |
| 09 onboarding, paywall | **Rất nên** | vị trí paywall là đánh đổi, không có đáp án đúng sẵn |
| 10 đo lường | Nên, ở phần North Star | chọn sai chỉ số thì cả team tối ưu sai hướng |
| 11–13 | Không | đối chiếu và đóng gói, không phải sáng tạo |

Quy tắc chung: **brainstorm ở chỗ có đánh đổi, chạy thẳng ở chỗ có bằng chứng.** Phase nào mà câu trả lời
nằm trong dữ liệu thì bàn thêm chỉ tốn thời gian. Phase nào mà câu trả lời phụ thuộc bạn muốn gì thì bàn
kỹ trước khi để nó viết.

### Ba dấu hiệu bạn đang brainstorm sai

Claude đồng ý với mọi thứ bạn nói — bạn đang hỏi dẫn dắt, thử hỏi lại bằng Kiểu 2.

Bàn 40 phút rồi vẫn chưa có gì ghi vào `_DECISION_LOG.md` — đang xoay vòng. Chốt tạm một phương án và gắn
`[ASM]` còn hơn treo mãi.

Claude tự viết file dù bạn không bảo — bạn quên câu "đừng viết file", và tài liệu vừa sinh ra dựa trên
hội thoại chưa chốt. Xoá nó đi, đừng Approve.

---

<a name="8"></a>
## 8. Thoát rồi quay lại

Đóng cửa sổ lúc nào cũng được. Tài liệu đã nằm trên ổ đĩa.

Có **hai chữ "tiếp tục" khác nhau**, đừng lẫn:

| Lệnh | Tiếp tục cái gì | Nguồn |
| --- | --- | --- |
| `claude --continue` | cuộc trò chuyện | bộ nhớ phiên |
| `/design-docs <Tên> --continue` | chuỗi tài liệu | trạng thái trên ổ đĩa |

**Cách nên dùng** — mở phiên hoàn toàn mới:

```
cd D:\PROJECTS\HealthApp
claude
/design-docs HealthApp --continue
```

Tới phase 12 thì dùng lệnh riêng: `/design-ui` hỏi công cụ rồi dựng lô kế tiếp, `/design-ui lô 2` dựng
đúng lô 2, `/design-ui trạng thái` chỉ in bảng lô mà không dựng gì.

Claude quét `docs/`, đọc `_INDEX.md`, thấy file nào `approved` file nào chưa, rồi vào lại đúng chỗ dở.
Nó làm được **mà không cần nhớ gì** về hôm qua.

Ngữ cảnh sạch thì Claude sắc bén hơn, tốn ít hạn mức hơn, và quan trọng nhất là không mang theo những
ngã rẽ sai của hôm trước.

**Khi nào cần `claude --continue`?** Khi đang giữa chừng một cuộc tranh luận **chưa ghi ra file**.
Nhưng cách tốt hơn là đừng để rơi vào tình huống đó — trước khi thoát, bảo Claude:

> Tôi dừng ở đây. Ghi những điều đang bàn dở vào `docs/_OPEN_QUESTIONS.md`, và giả định tôi đang tạm
> chấp nhận vào `docs/_ASSUMPTION_REGISTER.md`.

**Đừng để quyết định chỉ tồn tại trong hội thoại.**

### Hết hạn mức Claude, chạy tiếp bằng Codex hoặc OpenCode

Làm được, và không mất gì. Lý do là **trạng thái nằm trên ổ đĩa, không nằm trong hội thoại** — đúng cái
tính chất khiến `--continue` hoạt động khi mở phiên mới. Đổi công cụ cũng chỉ là mở một phiên mới, bằng
chương trình khác.

Bộ đã có sẵn `AGENTS.md` ở gốc dự án — Codex và OpenCode tự đọc file đó, trong đó có quy trình tiếp nhận
dự án đang dở.

**Đổi ở ranh giới, đừng đổi giữa chừng.** Tốt nhất là đổi sau khi một tài liệu đã `approved`; tốt nhì là
sau khi một cổng đã đóng. Thấy hạn mức sắp hết thì **viết nốt tài liệu đang làm, duyệt, rồi mới đổi** —
đừng để dở nửa tài liệu.

Trước khi đóng Claude lần cuối, gõ:

```
Tôi sắp hết hạn mức và sẽ chạy tiếp bằng công cụ khác.
Ghi mọi thứ đang bàn dở ra file: DEC vào _DECISION_LOG, câu hỏi treo vào _OPEN_QUESTIONS,
giả định vào _ASSUMPTION_REGISTER. Cập nhật _INDEX cho khớp thực tế.
Rồi nói cho tôi biết đang dở đúng ở đâu.
```

Sang công cụ mới, mở đúng thư mục dự án đó rồi gõ:

```
Đọc AGENTS.md, CLAUDE.md, .claude/commands/design-docs.md và docs/_INDEX.md.
Chạy python .claude/scripts/validate_docs.py.
Báo cho tôi: đang ở phase nào, tài liệu tiếp theo là gì, script báo lỗi gì không.
Chưa viết gì cả.
```

Câu **"chưa viết gì cả"** quan trọng. Agent mới tiếp nhận thường muốn chứng tỏ bằng cách viết ngay, mà
lúc đó nó chưa nắm được những gì đã chốt.

`validate_docs.py` là chỗ dựa khách quan nhất lúc này — nó không phụ thuộc agent nào, nên nếu nó báo sạch
thì bộ tài liệu đang lành lặn, bất kể ai viết ra.

Ghi một dòng vào `docs/_INDEX.md` mục 8 *Sổ đổi công cụ*. Không phải thủ tục — nó cho bạn biết chỗ nào
cần soi kỹ khi đọc lại, vì **giọng văn và độ sâu tài liệu sẽ lệch** giữa hai agent.

**Tài liệu đang viết dở thì đừng viết tiếp vào giữa.** Bảo agent mới đọc rồi hỏi bạn muốn giữ và sửa hay
viết lại từ template. Nửa đầu một giọng, nửa sau một giọng là chỗ khó phát hiện hơn nhiều so với viết lại.

### Điều thứ hai cần nhắc khi đổi công cụ: bắt nó liệt kê, đừng để nó tóm tắt

Đây là khác biệt lớn nhất giữa các công cụ khi chạy bộ này, và nó **nguy hiểm âm thầm**. Agent nào cũng có
xu hướng đọc nhiều rồi viết cô đọng. Ở phase 01 đến 04 thì cô đọng là **phá tầng bằng chứng**.

Lý do: thiếu sót ở phase 06–08 thì bắt được — ma trận còn ô `?`, tính năng không có use case, script báo ra
ngay. Thiếu sót ở phase 01–04 thì **không có gì để đối chiếu**, vì không ai biết ngoài kia còn bao nhiêu
pain point chưa đào. Một sổ đào pain point sơ sài trông **y hệt** một sổ đầy đủ.

Nên khi giao phase 01–04 cho công cụ có xu hướng tóm tắt, thêm ràng buộc đếm được vào câu lệnh:

```
Liệt kê từng dòng, không tóm tắt.
Mỗi pain point một dòng riêng: câu nguyên văn của người dùng, URL, ngày lấy.
Tối thiểu 30 dòng từ ít nhất 3 nguồn khác nhau trước khi gom cụm.
Không gộp hai lời phàn nàn khác nhau thành một dòng.
Chỗ nào bạn diễn giải lại thay vì trích nguyên văn thì ghi rõ [INSIGHT], không ghi [FACT].
```

Con số cụ thể là thứ ép được; câu *"làm kỹ vào"* thì không.

Nếu công cụ đó vẫn trả về bản tóm tắt sau khi đã ràng buộc, thì đó là tín hiệu rõ: **giữ phase 01–04 cho
công cụ mạnh hơn**, giao cho nó phase 06–08 và 10 và 13 — nơi thiếu sót bị máy chấm bắt.

Một điều tôi nói thẳng: **kỷ luật "một tài liệu một lượt" là quy tắc bằng lời, không có gì ép được.**
Claude Code có `.claude/commands/` ràng buộc chặt hơn. Công cụ khác có thể viết liền hai ba tài liệu nếu
bạn không nhắc. Thấy nó làm vậy thì dừng lại, bảo nó đọc lại `AGENTS.md` mục *Chín quy tắc tối thiểu*.

---

<a name="9"></a>
## 9. Làm việc với Dev

Dev **không chờ tới cuối**, và cũng không chờ tới phase 06. Nghiên cứu công nghệ đứng **trước** quyết
định có làm sản phẩm hay không.

Bảy biểu mẫu trong `tech-input/`. Có **hai lần gửi Dev**, ở hai thời điểm khác nhau:

| Lần | Bạn gửi gì | Khi nào | Dev trả về | Nếu xấu thì sao |
| --- | --- | --- | --- | --- |
| 1 | `03-05_TECH_FEASIBILITY_BRIEF` + `TECH-00` | giữa phase 03, ngay sau khi chốt concept | phán quyết theo từng `CAP` | **dừng dự án** hoặc xoay concept |
| 2 | `06-00_FEATURE_BRIEF_FOR_DEV` + `TECH-01`…`TECH-05` | đầu phase 06 | khả thi theo từng `FEAT` rồi `FR` | cắt tính năng hoặc hạ ngưỡng |

**Lần 1 là lần quan trọng nhất.** `TECH-00_FEASIBILITY_SCREEN.md` là biểu mẫu có giá trị cao nhất trong cả
thư mục — nó trả lời câu *"có làm được không"*, và câu trả lời "không" ở phase 03 tiết kiệm cho bạn hai
phase công việc.

Điều cần nói rõ với Dev: **trả lời "không khả thi" không làm ai thất vọng.** Điều gây thiệt hại là trả lời
"được" cho êm chuyện rồi ba tháng sau mới nói lại.

Khi Dev nộp file:

> Đọc `tech-input/TECH-00_FEASIBILITY_SCREEN.md`. Điền vào `03-05` mục 5, liệt kê nội dung sẽ điền vào
> tài liệu nào, và **liệt kê mâu thuẫn** với tài liệu sản phẩm hiện có. Chưa sửa gì cả.

Claude báo cáo → bạn duyệt → mới cho sửa. **Đừng để Claude tự sửa ngay** — bạn cần thấy mâu thuẫn trước
khi nó bị hoà tan vào văn bản.

Trong lúc làm, mỗi khi thiếu thông tin kỹ thuật, Claude gắn `[ASM]` và ghi câu hỏi vào
`docs/13-handover/13-02_DEV_QUESTION_LOG.md`. Định kỳ mở file đó, gửi Dev trả lời.

**Claude không bao giờ được tự phán quyết khả thi.** Cột phán quyết ở `03-05` mục 5 và `06-00` mục 3 chỉ
điền từ `tech-input/`, kèm tên file và ngày nhận. Thấy Claude viết "cái này chắc làm được" mà không dẫn
nguồn `tech-input` thì bắt nó sửa — đó là vi phạm nặng nhất trong cả bộ.

---

<a name="10"></a>
### Đưa tài liệu cho người ở vai trò khác đọc

Bộ này có **ba nghề cùng đọc chung một bộ tài liệu**: bạn, Designer và Dev. Vấn đề không phải ai đó viết khó
hiểu — mà là người ở nghề khác **lướt qua chỗ lạ, tưởng mình hiểu, rồi vẫn duyệt**. Designer thấy `p95` thì
bỏ qua; Dev thấy `JTBD` thì bỏ qua. Sáu tuần sau mới lộ ra hai bên hiểu hai kiểu.

Nên **mọi tài liệu** đều có hai mục cố định:

| Mục | Ở đâu | Chứa gì |
| --- | --- | --- |
| `0. Đọc nhanh` | đầu tài liệu | bốn dòng viết **không một thuật ngữ nào**: tài liệu này là gì · ai cần đọc · đọc xong phải biết gì · quyết định nào chốt ở đây |
| `Thuật ngữ dùng trong tài liệu này` | cuối tài liệu | mọi thuật ngữ và mã có dùng, kèm nghĩa **một câu** |

**Thuật ngữ không bị thay, chỉ được giải thích thêm.** Đừng để Claude đổi `NFR` thành "yêu cầu phi chức năng"
rồi bỏ luôn từ gốc, hay tự chế từ tiếng Việt thay cho một thuật ngữ đã có tên chuẩn — người trong nghề cần
đúng từ đó để tra cứu và để nói chuyện với bên ngoài.

Từ điển chung ở `docs/_GLOSSARY.md` mục *Thuật ngữ chuyên môn*: 75 từ, mỗi từ một câu nghĩa và một cột ghi
vai trò nào hay không hiểu từ đó. Gặp từ chưa có thì thêm dòng — từ điển đó thuộc về dự án của bạn.

`validate_docs.py` kiểm hộ: dùng thuật ngữ mà không liệt kê ở bảng cuối bài thì báo **LỖI**; thuật ngữ lọt
vào mục `0. Đọc nhanh` cũng bị bắt, vì đó là bốn dòng duy nhất phải đọc được bởi bất kỳ ai.

## 10. Wireflow rồi sang UI

### Phase 08 — đầu ra là wireflow, xem được trên trình duyệt

Đầu ra phase 08 **không phải hình vẽ bằng ký tự** `---|||`, và cũng không phải bản vẽ bố cục có ghi số đo.
Nó là **wireflow**: một trang HTML cho một luồng, các màn xếp cạnh nhau, nối bằng **mũi tên**, trên mũi tên
ghi *bấm gì*, ở nhánh ghi *điều kiện nào*.

```
python -m http.server 8000
```

rồi mở **http://localhost:8000/wireframes/** — thấy danh sách luồng, bấm vào một luồng là thấy trọn luồng đó.

Wireflow trả lời **bốn câu**, và cố tình chỉ bốn câu:

| Câu | Trả lời ở đâu |
| --- | --- |
| Màn này phục vụ **chức năng** gì | nhãn dưới mỗi màn trên trang flow |
| **Vào từ** màn nào | mũi tên đi vào, và khối ghi chú trong file màn |
| **Bấm gì** thì ra màn nào | nhãn trên mũi tên |
| **Tình huống nào** ra trạng thái nào | nhãn điều kiện ở nhánh, và mục *Trạng thái còn lại* |

> **Không có khoảng cách, cỡ chữ, độ cao, màu.** Đó là việc của `12-00` sau khi đọc moodboard. Ghi số pt ở
> phase 08 là ép bạn quyết một thứ chưa tới lúc quyết, và làm cả nhóm chuyển sang tranh luận thị giác trong
> khi hành vi còn chưa xong. **Nút cũng không bấm được** — điều hướng nằm ở mũi tên, không ở nút.

Mỗi trang flow có ba mục, và mục thứ ba là mục cứu bạn: **đường chính** (happy path) · **nhánh theo điều
kiện** (*nếu mã sai 3 lần*, *nếu mất mạng*) · **trạng thái còn lại** — mọi ô của `08-02` (Ma trận trạng thái)
chưa xuất hiện ở hai mục trên, kèm điều kiện vào trạng thái. Đường chính thì ai cũng làm; đang tải, rỗng,
mất mạng, hết quyền thì luôn là chỗ bị bỏ.

Kiểm phủ: `python .claude/scripts/check_build.py --wireframes wireframes/` — báo màn nào thiếu, **màn nào chưa
nằm trong luồng nào**, mũi tên nào **trống nhãn**, tên file nào sai mã. 0 lỗi là điều kiện cổng `G7`.

Công đó không bị bỏ đi: ở phase 12, trang flow là bản tham chiếu thứ tự dựng khi bạn làm Figma; chọn Pencil
thì nạp từng file màn vào Pencil để import thành layer sửa được.

### Phase 12 — trước khi mở Figma: chốt phong cách đã

Phase 12 **bắt đầu bằng `12-00_UI_RESEARCH`**, không bắt đầu bằng việc dựng. Lý do rất thực tế: không chốt
phong cách trước thì phong cách sẽ được chốt ngầm ở màn thứ ba, và hai màn dựng trước đó phải dựng lại.

Nguyên liệu là thư mục `research-raw/moodboard/` — ảnh tham chiếu UI. Năm thư mục con:

```
mau-sac/  kieu-chu/  thanh-phan/  man-hinh-hay/  khong-thich/
```

Thư mục cuối không phải cho vui. **Biết mình không muốn gì định hình style mạnh ngang biết mình muốn gì**,
và nó ngăn Claude đề xuất đúng thứ bạn đã loại. Bảng nghiệm thu đòi ít nhất 3 ảnh ở đó.

Ảnh này bạn tự thu, hoặc để Codex/OpenCode + KimiBridge thu — Claude sẽ hỏi ở đầu phase 12, y như đầu
phase 01. Khối lệnh giao việc nằm sẵn ở `research-raw/moodboard/_MANIFEST.md` mục 4.

Có ảnh rồi, `12-00` làm sáu việc:

1. Đọc `08-01`, `08-03`, `07-05`, `09-06` **trước khi mở ảnh** — để phong cách phải chịu được đúng bộ màn
   và đúng độ dài chữ bạn đã viết, không phải một phong cách đẹp với ba dòng chữ trên Dribbble.
2. Đọc ảnh thành các mẫu `UIP`, mỗi mẫu một quyết định **Áp dụng / Điều chỉnh / Không dùng**. Lý do
   *"vì đẹp"* và *"vì đang là trend"* bị chặn.
3. Đưa **ba** hướng thiết kế khác nhau, bạn chọn một, ghi `DEC`, và ghi cả vì sao loại hai hướng kia.
4. Chốt hệ màu và hệ chữ, kiểm tương phản từng cặp — kể cả chữ phụ, chỗ trượt nhiều nhất.
5. **Quét lại ảnh đối thủ lần hai.** Lần một ở `07-00` là để hiểu luồng; lần này là để xem *"chức năng này
   họ vẽ ra sao"*, và chỉ với những chức năng có trong `08-01` của bạn.
6. Lọc màn nào cần chốt thị giác trước — **nên ≤5 màn**. Nhiều hơn là chưa lọc, chỉ đang chép lại `08-01`.

### Hai nhánh dựng — Claude sẽ hỏi bạn chọn

Đầu phase 12, trước khi viết mục nào của `12-00`, Claude phải hỏi:

```
  A. Pencil + Agent dựng  — tôi dựng theo từng luồng, bạn kiểm rồi approve, tôi dựng tiếp
  B. Figma bạn dựng tay   — tôi viết spec rồi TẠM DỪNG dự án, bạn dựng xong thì gọi tôi đối chiếu
```

Đúng như bạn đã hình dung: **app dạng tool, ít tính năng** thì chọn A cho nhanh; **app lớn** thì chọn B và
tự làm Figma. Lựa chọn ghi vào `12-00` mục 7 kèm một `DEC`, và **nhánh B là mặc định** — nhánh A đảo quy
tắc *"AI không dựng UI"* nên không có `DEC` thì Claude không được dựng.

Có hệ thiết kế dựng sẵn thì để nó ở thư mục `design-system/` và điền `_MANIFEST.md`. Thư mục đó là **tài
sản của bạn** giống `tech-input/` là của Dev: Claude đọc để **gọi đúng tên component**, không sửa file hệ.

> **Mục 4 của `design-system/_MANIFEST.md` là mục đừng bỏ.** Nó đếm số thành phần mà `08-03` (Wireflow)
> cần nhưng hệ chưa có. Số đó lớn thì dựng bổ sung hệ **trước** — component sinh ra trong lúc dựng màn gần
> như luôn lệch nhau, và bạn phát hiện ở màn thứ hai mươi.

Dù nhánh nào, Claude vẫn viết hai file này:

- `12-01_PROTOTYPE_BUILD_SPEC.md` — danh sách chính xác các frame phải dựng, tên từng frame, và **bảng lô**
- `12-02_DESIGN_SYSTEM_AND_A11Y.md` — màu, chữ, khoảng cách, component, ngưỡng tiếp cận

Bảng lô ở `12-01` mục 4 là chỗ bạn kiểm soát nhánh A: **một lô một lượt**, mỗi lô là một luồng, lô chưa
nghiệm thu thì không dựng lô sau. Sau mỗi lô Claude xuất ảnh, chạy `check_build.py`, báo bốn dòng rồi dừng.
Dòng cuối là dòng đáng đọc nhất: *"chỗ tôi phải tự quyết vì tài liệu không nói rõ"* — mỗi mục ở đó là một
chỗ `08-03` hoặc `09-06` (Bộ văn bản giao diện) còn thiếu.

**Đặt tên frame đúng quy ước** là điều quan trọng nhất khi dựng:

```
SCR-012 · Kết quả phân tích · ST-041 Mặc định
SCR-012 · Kết quả phân tích · ST-044 Lỗi mạng
```

Không đặt đúng thì bước đối chiếu sau đây thành thủ công và sẽ không ai làm.

Dựng **theo flow**, không theo thứ tự mã màn hình. Dựng trọn một flow rồi bấm thử từ đầu tới cuối sẽ
phát hiện thiếu sót nhanh hơn.

Dựng xong thì quay lại — đây là lúc Claude hữu ích nhất cho bạn:

> Tôi đã dựng xong Figma. Chạy `12-03_PROTOTYPE_REVIEW`: màn nào trong `08-01` mà tôi chưa dựng,
> frame nào tôi dựng mà không có mã trong tài liệu, trạng thái nào còn thiếu so với `08-02`,
> và chữ nào lệch so với `09-06_COPY_DECK`.

Đúng ba việc bạn cần: kiểm UX writing, đếm đủ màn chưa, đủ trạng thái chưa.

> Nếu Claude phát hiện frame thừa — thường là **dấu hiệu tốt**, bạn vừa nghĩ ra một trạng thái tài liệu
> bỏ sót. Nhưng phải cập nhật ngược vào `08-01` và `08-02`, đừng để nó chỉ tồn tại trong Figma.

---

<a name="11"></a>
## 11. Khi cổng fail

Cổng fail là bình thường, không phải sự cố.

```
Giải thích cổng G5 fail vì mục nào và cần bổ sung gì, nói bằng tiếng Việt đơn giản.
```

Chạy kiểm độc lập bất cứ lúc nào, không cần mở Claude:

```
cd D:\PROJECTS\HealthApp
python .claude\scripts\validate_docs.py
python .claude\scripts\validate_docs.py --gate G5
```

Script bắt: front-matter thiếu trường, file `approved` phụ thuộc file chưa `approved`, `[ASM]` không có
dòng trong sổ, ID cấp trùng ở hai tài liệu, hạng mục mồ côi, **tham chiếu treo**, từ không đo được trong
acceptance criteria, Lorem Ipsum còn sót, và lệch giữa `_INDEX` với thư mục template.

**Tham chiếu treo** là lỗi đáng sợ nhất trong nhóm này vì nó im lặng: `06-02` trích `UC-007` trong khi
`06-01` mới cấp tới `UC-005`. Đọc từng tài liệu riêng thì cả hai đều trông đúng; chỉ lộ ra khi đối chiếu
chéo. Script báo dạng:

```
LỖI      THAM CHIẾU TREO — 06-02 trích UC-007 nhưng ID này chưa được cấp
CẢNH BÁO prefix SCR: chưa có tài liệu nào sở hữu nên không kiểm được SCR-004
```

Dòng **CẢNH BÁO** không phải lỗi — nghĩa là tài liệu cấp mã đó chưa viết. Viết xong thì chạy lại, nó tự
chuyển thành đạt hoặc thành lỗi thật.

---

<a name="12"></a>
## 12. Sửa tài liệu đã duyệt

**Tuyệt đối không sửa thẳng.** Nói với Claude:

> Tôi cần đổi: người dùng free được scan ba lần mỗi ngày thay vì năm.
> Cấp `CHG` và viết Change Impact Report trước. Chưa sửa file nào.

Claude sẽ liệt kê mọi chỗ bị ảnh hưởng. Với ví dụ trên là bảy chỗ: quy tắc reset theo múi giờ nào,
trạng thái hết lượt, chỗ hiển thị còn mấy lượt, event `free_limit_reached`, ảnh hưởng phễu chuyển đổi,
ca nghiệm thu cho lượt thứ ba và thứ tư, và việc lượt còn lại có cộng dồn không.

Bạn duyệt xong Claude mới cập nhật, theo đúng thứ tự lan truyền.

Đây là lý do quy trình này tồn tại: sửa lẻ một chỗ sẽ để lại sáu chỗ sai mà không ai biết.

---

<a name="13"></a>
## 13. Bỏ bớt tài liệu hoặc cổng

Được, nhưng phải bỏ **có ý thức**.

Tài liệu ngoài profile đã tự động bỏ. Muốn bỏ thêm thì nói với Claude, và nó sẽ ghi lý do vào
`_INDEX.md` mục 6.

Bỏ cổng cũng vậy — ghi cổng nào, vì sao, rủi ro gì.

> Một tài liệu bị bỏ vì không cần khác hoàn toàn một tài liệu bị quên. Ghi lại là để sáu tháng sau
> bạn phân biệt được hai thứ đó.

Nguyên tắc phân xử khi phân vân: **một tài liệu chỉ đáng tồn tại nếu thiếu nó thì có người phải hỏi lại,
hoặc có người sẽ làm sai.**

---

<a name="14"></a>
## 14. Nhiều dự án cùng lúc

Không xung đột. Claude Code đọc cấu hình từ thư mục bạn mở nó lên, nên hai dự án ở hai thư mục là hai
bộ cấu hình tách biệt. Chạy song song trong hai cửa sổ cũng được.

Ba điều cần giữ:

**Không cài gì vào cấp người dùng.** Kiểm bằng `dir %USERPROFILE%\.claude\skills` — trống là tốt.
Có skill nằm đó thì nó xuất hiện ở mọi dự án và bạn không đoán được cái nào được nạp.

**Kiểm thư mục trước mỗi lần bắt đầu.** Sau khi `claude` khởi động, hỏi *"Tôi đang ở project nào?"* —
mất năm giây, tránh được cả buổi làm nhầm chỗ.

**Cẩn thận với lệnh cài của bộ khác.** Nếu bạn còn dùng bộ app-spec cài bằng `uvx`, lệnh đó copy vào
**thư mục hiện tại**. Chạy nhầm trong thư mục Pipeline v2 sẽ đè lên. Luôn `cd` kiểm tra trước.

Thứ duy nhất thật sự dùng chung là hạn mức tài khoản.

---

<a name="15"></a>
## 15. Thêm và cập nhật skill

**Thêm kiến thức cho skill đã có** — thả file `.md` vào `references/` của skill đó. Không phải sửa
`SKILL.md`, vì nó đọc mọi file trong thư mục chứ không liệt kê cứng.

**Thêm skill chiều sâu cho một phase** — thả thư mục skill vào `.claude/skills/_depth/<phase>/`. Hết.
Không phải sửa `_INDEX`, `_ID_REGISTRY` hay file khung nào.

```
_depth/09-growth/paywall-pricing-psychology/
├── SKILL.md          ← frontmatter cần `name` và `description` một dòng thật rõ
└── references/
```

`description` quan trọng: skill phụ trách tài liệu đọc description trước và chỉ mở toàn bộ nội dung của
cái nào thật sự liên quan. Mơ hồ thì hoặc bị bỏ qua, hoặc bị nạp thừa làm loãng trọng tâm.

**Thêm một tài liệu mới vào phase đã có** — đắt hơn, vì phải chạm năm chỗ. Dùng script:

```
python add_doc.py --kit D:\TOOLKIT\pipeline-v2 --phase 09 ^
    --name LOCALIZATION_SPEC --title "Localization Spec" --ids LOC --depends 09-06
```

Nó tự cấp số tiếp theo còn trống, tạo template có manifest, thêm dòng vào `_INDEX`, đăng ký prefix ID,
cập nhật bảng phụ trách của skill — rồi **nhắc bạn chỗ thứ năm phải làm tay** là thêm dòng kiểm vào
`_GATE_CHECKLIST`.

**Khi nào skill chiều sâu nên nâng thành skill phụ trách tài liệu?** Nếu nó chỉ thay đổi *cách nghĩ*
thì để ở `_depth`. Nếu nó tạo ra *sản phẩm mà có người phải đọc và ký duyệt* thì nó cần một tài liệu
và một cổng.

**Cập nhật bộ mẫu.** Bộ này là kết quả build, không phải nơi sửa tay. Sửa ở nguồn rồi chạy lại:

```
python build_kit.py --appspec <app-spec> --new .\new --out D:\TOOLKIT\pipeline-v2 --force
```

Dự án đang chạy **không** tự cập nhật — chủ ý, vì tài liệu phải đọc được bằng đúng chuẩn đã sinh ra nó.
Thật sự cần nâng thì:

```
python update_project.py --project D:\PROJECTS\HealthApp --kit D:\TOOLKIT\pipeline-v2
```

Script chỉ thay `.claude/`, tuyệt đối không chạm `docs/`, `tech-input/`, `design/`, `CLAUDE.md`.
Nó sao lưu bản cũ và cảnh báo nếu bạn đã có tài liệu `approved` theo chuẩn cũ.

---

<a name="16"></a>
## 16. Sự cố thường gặp

**Không thấy lệnh `/design-docs`.** Chạy sai thư mục. `/exit`, `cd` cho đúng, mở lại.

**Claude viết liền mấy tài liệu trong một lượt.** Nhắc: *"Quy tắc một tài liệu một lượt trong `CLAUDE.md`.
Dừng lại, chỉ hoàn thành tài liệu hiện tại."* Lặp lại nhiều lần thì kiểm xem `CLAUDE.md` có bị sửa mất không.

**Claude đề xuất backend, tài khoản, cloud sync mà bạn không muốn.** Chỉ vào `docs/00-khoi-tao/00-02_SCOPE_LOCK.md`.
Danh sách bị cấm còn trống thì điền ngay — đó là công cụ mạnh nhất để giữ phạm vi.

**Claude tự đoán thông tin kỹ thuật.** Nhắc quy tắc: gắn `[ASM]`, tạo `DQ`, không suy đoán.
Kiểm `13-02_DEV_QUESTION_LOG.md` xem có dòng tương ứng chưa.

**Muốn làm lại một tài liệu từ đầu.** Xoá file trong `docs/` rồi chạy `--continue`. Nhưng nếu tài liệu sau
đã trích ID từ nó thì phải chạy Change Impact Report trước.

**Số màn hình có vẻ thiếu.** Đó là lý do phase 08 tồn tại. Kiểm `08-02_STATE_MATRIX.md` xem còn ô `?` không,
và `08-01` mục 2 xem đã đi hết 23 nhóm chưa.

**Khung chat của extension không thấy `/design-docs`.** Bình thường — extension chỉ hỗ trợ một tập con
command. Dùng terminal tích hợp: `Ctrl` + dấu huyền rồi gõ `claude`.

**Gõ `claude` trong terminal báo không tìm thấy.** Cài extension **không** thêm `claude` vào PATH.
Phải cài CLI riêng theo phần 2.

**Sơ đồ UX flow hiện ra dạng khối chữ.** Thiếu extension Markdown Preview Mermaid Support.

**Tài liệu nhiều quá, không ai đọc.** Dấu hiệu chọn sai profile. Xem `_DOCUMENTATION_STANDARD.md` mục
"Khi nào chuẩn này là quá nhiều". Sản phẩm rất nhỏ thì chỉ cần `06-02`, `08-01`, `08-02`, `13-04`.

---

## Ba việc nên làm đều

**Sao lưu `docs/`.** Đây là tài sản duy nhất không tái tạo được. Copy sang ổ khác hoặc dùng git,
commit sau mỗi tài liệu được duyệt.

**Mở `_INDEX.md` mỗi tuần.** Năm phút.

**Chạy `validate_docs.py` trước mỗi lần đóng cổng.** Nhanh hơn để Claude tự phát hiện.
