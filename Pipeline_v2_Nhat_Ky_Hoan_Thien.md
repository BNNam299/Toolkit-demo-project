# Pipeline v2 — nhật ký hoàn thiện bộ mẫu

> Ghi lại **toàn bộ** các đợt cập nhật từ bản đầu tới bản hiện tại: bạn muốn gì, nhận ra điều gì, đã đổi gì
> trong bộ, và cái giá phải trả. Mục đích là để phiên làm việc sau — hoặc người khác trong team — không phải
> brainstorm lại, và không vô tình gỡ bỏ một cơ chế mà quên mất nó sinh ra để chặn lỗi gì.
>
> **Cập nhật lần cuối:** 2026-09-15 · Bổ sung cho `claude/Bo_Mau_Pipeline_v2_Ban_v1.0_Chot_Gi.md`
> (những gì đã chốt) và `claude/Chuoi_Dung_UI_Wireframe_HTML_Den_Prototype.md` (chuỗi dựng UI).
> Hai file đó trả lời *"bộ này là gì"*. File này trả lời *"vì sao nó thành ra như vậy"*.

---

## 0. Đọc nhanh

| Câu hỏi | Trả lời ngắn |
| --- | --- |
| **File này là gì** | Nhật ký các đợt sửa bộ mẫu, kèm lý do đằng sau từng thay đổi |
| **Ai cần đọc** | Bạn khi quay lại sau vài tuần · người tiếp quản bộ mẫu · agent được giao sửa bộ mẫu |
| **Đọc xong phải biết gì** | Mỗi cơ chế trong bộ sinh ra để chặn lỗi gì, và gỡ nó ra thì mất gì |
| **Quyết định nào chốt ở đây** | Không chốt gì mới — đây là bản ghi những thứ đã chốt ở các phiên trước |

---

## 1. Xuất phát điểm

Bộ mẫu dựng từ **bộ `app-spec` của công ty** (11 skill UX trên `svn.as.local`), cộng 5 skill lấp khoảng
trống, cộng engine chấm cổng. `build_kit.py` **chỉ đọc** từ app-spec, không bao giờ ghi ngược.

Phạm vi ngay từ đầu: **từ chưa có ý tưởng gì đến gói bàn giao Dev.** Không sinh code, không dựng UI hi-fi
bằng AI — trừ một nhánh bật có điều kiện ở phase 12.

Bản nền chốt ngày **2026-08-17/18**: 14 phase · 60 tài liệu · 12 cổng G0–G11 · 3 profile (Lean/MVP/Full).

---

## 2. Dòng thời gian — chín đợt

### Đợt 1 · Nghiên cứu UI và nối Pencil

**Bạn muốn:** trước khi thiết kế UI phải có một bước research riêng — dùng Codex/OpenCode + KimiBridge đi
gom moodboard, rồi Claude đọc toàn bộ để đề xuất hướng thiết kế; sau đó quét lại ảnh đối thủ lần hai xem
từng chức năng họ vẽ thế nào; rồi lọc ra các màn nên có. Và: *"có thể nối thẳng sang Pencil để dựng luôn UI
được không?"*

**Nhận ra:**

Đọc ảnh đối thủ **một lần** là sai. Cùng một tập ảnh phục vụ hai câu hỏi khác nhau ở hai thời điểm khác
nhau: `07-00` đọc để hiểu **luồng và kiến trúc thông tin**; `12-00` đọc lại để xem **từng chức năng được vẽ
ra sao**. Đọc thị giác quá sớm là cách chắc nhất để sao chép giao diện trước khi hiểu vì sao nó có.

Về Pencil, điểm dễ nhầm nhất là **chi phí token**: Pencil CLI có AI designer riêng, cần đăng nhập Claude Code
và mặc định chạy Opus. Nghĩa là gõ lệnh CLI **từ Codex vẫn tiêu token Claude** — Codex chỉ đóng vai người bấm
lệnh. Muốn Codex gánh thật thì phải nối bằng **MCP**.

**Đã đổi:**

- Thêm `12-00_UI_RESEARCH.md` — tài liệu thứ **61**. Mục §0 ép đọc `08-01`/`08-03`/`07-05`/`09-06` **trước
  khi mở bất kỳ ảnh nào**. Mỗi `UIP` phải kèm Áp dụng/Điều chỉnh/Không dùng với lý do neo vào §0 — lý do
  *"vì đẹp"* và *"vì đang là trend"* bị chặn thẳng.
- Bắt buộc `moodboard/khong-thich/` có **≥3 ảnh**. Biết mình không muốn gì thì quyết nhanh hơn nhiều so với
  chỉ biết mình thích gì.
- §3 ép ra **ba hướng thiết kế khác nhau** rồi mới chọn một, kèm `DEC`.
- §6 lọc **≤5 màn "chốt trước"** — dựng năm màn đúng rồi nhân ra, thay vì dựng ba mươi màn sai đều.
- Nhánh Pencil: chèn khối ràng buộc **lên đầu** skill `pencil-design` (không phải nối vào cuối), mặc định
  **TẮT**, chỉ mở khi có `DEC`. Ba thứ nhánh này không được quyết: danh sách màn `08-01`, luồng và nội dung
  `08-03`, câu chữ `09-06`.
- Lệnh `/design-ui` — **markdown thuần** để Codex/OpenCode dùng y hệt. Bước 1 bắt buộc hỏi Pencil hay Figma,
  và bắt buộc cảnh báo về chi phí token nếu người dùng đang chạy Codex.
- `design-system/` thành thư mục cấp gốc, tài sản người dùng, AI **đọc không sửa**. Kèm `_MANIFEST.md` có
  **bảng phủ** phải điền trước khi dựng frame đầu tiên. Có hệ sẵn **không** cho phép bỏ `12-00` — nó chỉ
  đổi việc `12-00` phải làm từ *chọn phong cách* thành *kiểm hệ có chịu được bộ màn này không*.

---

### Đợt 2 · Bộ permissions và wireframe thành HTML

**Bạn muốn:** hiểu bộ `permissions` làm gì; và **wireframe phải là màn hình preview được trong khi dự án
đang chạy, không phải nét đứt `---|||`**.

**Nhận ra:**

Một hộp ASCII không cho biết chữ có tràn không, danh sách dài có đẩy CTA xuống dưới màn hình không, nút có
đủ vùng chạm không. Đó đúng là **ba thứ wireframe tồn tại để phát hiện**. Vẽ bằng ký tự là bỏ đi lý do tồn
tại của wireframe.

Về permissions: `deny` biến quy tắc bằng lời thành **ràng buộc cứng**. *"AI không sửa tài sản của Dev"*
trước đây là một câu trong `CLAUDE.md` mà mô hình có thể lỡ vi phạm; sau khi vào `deny` thì công cụ chặn.

**Đã đổi:**

- `wireframes/` với `_wireframe.css` (chỉ biến xám `--w-*`), `_TEMPLATE.html`, `index.html`.
- **Một file cho một ô trong `08-02`.** Không gộp trạng thái, không dùng JS bật tắt — vì mỗi ô là một frame
  phải dựng ở phase 12, gộp lại thì script không đếm được và người review bỏ sót đúng những trạng thái hay
  bị bỏ.
- `check_build.py` hai chế độ: `--wireframes` (phase 08, cổng G7) và `--frames` (phase 12, cổng G10).
- `settings.json`: `allow` cho ghi `docs/**` `wireframes/**`; `deny` ghi `tech-input/**`, `.pen`/`.fig`,
  các thư mục bằng chứng, và **đọc `.mcp.json`** (chứa khoá Figma); `ask` cho `rm *` và `git push*`.

---

### Đợt 3 · Bỏ chú thích số đo — lần tôi phải rút lại đề xuất của chính mình

**Bạn nói:** *"ở wireframe thực tế sử dụng tôi không quan tâm đến chú thích khoảng cách, kích thước chữ…
chỉ quan tâm màn đấy phục vụ chức năng gì, từ màn nào dẫn đến màn nào, bấm nút này thì ra màn nào, trạng
thái gì."*

**Nhận ra — và đây là một insight về cách làm việc, không phải về sản phẩm:**

Tôi đã tự thêm vào một *annotation rail* có số đo, nửa bố cục archetype, và dòng tự kiểm bằng số. Ba thứ đó
đều hợp lý **nếu** wireframe là tài liệu giao cho người dựng. Nhưng ở đúng thời điểm này nó **ép quyết một
thứ chưa tới lúc quyết**, và kéo cả nhóm sang tranh luận thị giác trong khi hành vi còn chưa xong.

Bài học: một bổ sung "đúng về chuyên môn" vẫn có thể sai vì **sai thời điểm trong quy trình**.

**Đã đổi:** rút cả ba, chuyển sang phase 12. Giữ lại đúng **hai** thông tin có tính hành vi: **thứ tự nội
dung** trên màn, và **cái gì thấy được ngay không cần cuộn**.

---

### Đợt 4 · Wireframe → wireflow

**Bạn muốn:** *"Nút không cần bấm được, không cần tương tác làm gì cả. Bạn có thể nâng cấp nó lên thành
wireflow — có các đường mũi tên dẫn, khi ấn từ đây thì ra đâu, tình huống nào thì ra trạng thái này."*

**Nhận ra:**

Một phiên trước đó tôi đã đề xuất nút **bấm được** bằng thẻ `<a>`. Sai. Nút bấm được cho người xem cảm giác
đang dùng app, nhưng nó **giấu mất bản đồ**: bạn chỉ thấy một màn tại một thời điểm, không bao giờ thấy trọn
luồng để phát hiện chỗ dư bước hay chỗ không có đường ra. Mũi tên trên một trang phẳng thắng, vì nó làm
được đúng việc mà bấm không làm được.

**Đã đổi:**

- Đổi tên `08-03_WIREFRAMES` → `08-03_WIREFLOWS`.
- `_TEMPLATE_FLOW.html`: **đường chính** → **nhánh theo điều kiện** → **trạng thái còn lại**. Mục thứ ba là
  mục cứu — đường chính thì ai cũng làm, còn đang tải, rỗng, mất mạng, hết quyền thì luôn bị bỏ.
- Màn **nhúng bằng iframe**, không chép nội dung vào trang flow — một nguồn sự thật, sửa màn thì flow tự
  cập nhật.
- `check_build.py` thêm: chưa có trang wireflow · **màn không nằm trong luồng nào** · **mũi tên trống nhãn**.
  Mũi tên không nhãn là một bước chuyển chưa nghĩ xong.
- `08-02` thêm **§1b — trục ngữ cảnh người dùng**: lần đầu vào / quay lại / **đã thành thạo** / còn lỗi từ
  phiên trước. Cột *Đã thành thạo* buộc phải quyết định **khi nào thôi hướng dẫn** — hầu hết sản phẩm để
  thẻ gợi ý ở màn chính mãi không thôi.

---

### Đợt 5 · Đối chiếu dự án thật `carplay` (Carbina) và vá lỗi

**Bạn muốn:** đọc một dự án đã chạy bằng app-spec gốc, so từng chặng với bộ mới, nói dễ hiểu với UI/UX
designer; rồi rút ra bài học; rồi *"vá lỗi đi, tôi ưu tiên khiến toolkit hoàn thiện nhất có thể."*

**Ba lỗi nặng tìm được trong hồ sơ thật — đây là phần giá trị nhất của cả quá trình:**

1. **PRD 1.504 dòng, 0 lần xuất hiện chữ "phỏng vấn".** Ba persona bịa hoàn toàn — nhân khẩu học thuần, số
   liệu tự nghĩ, không nguồn, không nhãn `[ASM]`, không ghi proto-persona.
2. **Persona mô tả một sản phẩm khác với sản phẩm đang làm.** §6 bản v2.0 ghi rõ đã bỏ một hướng vì không có
   bằng chứng; persona ở §3 **vẫn** mô tả đúng hướng đó. Hai chỗ tự mâu thuẫn cách nhau hai mươi dòng.
3. **Cổng tự chấm nằm cùng file với thứ nó chấm, nên nó cho qua.** *"Evidence Quality ✅ Pass"* trong khi §3
   là bịa; *"đã validate mức giá"* trong khi bảng bằng chứng **cùng file** đánh dấu con số đó đã bị chứng
   minh sai.

**Insight lớn nhất rút ra:** lỗi nguy hiểm nhất **không nằm trong một tài liệu nào cả**. Từng phần đọc riêng
đều đúng; chỉ **quan hệ giữa chúng** là sai. Không phép kiểm nào đọc một file mà bắt được loại lỗi này.

**Đã đổi — ba cơ chế, mỗi cơ chế chặn đúng một lỗi trên:**

| Lỗi | Cơ chế |
| --- | --- |
| Persona bịa | Phase 04 bị khoá ở **mức công cụ**: skill `user-research-synthesizer` **không có** `WebSearch`/`WebFetch`, nên nó không thể bịa từ web |
| Đầu vào đổi mà kết luận không đổi theo | **`check_stale_inputs`** — tài liệu đã `approved` mà một file trong `depends_on` sửa sau đó thì báo lỗi |
| Cổng tự chấm | Cổng tách khỏi file được chấm; `QUALITY-GATE-MANIFEST` là nguồn chân lý; script đếm khách quan, **không tin lời khai Lớp 2** |

**Vá thêm trong cùng đợt:**

- **Định mức chiều sâu phase 06** (`06-01` mỗi UC ≥1 luồng thay thế + ≥1 ngoại lệ · `06-02` mỗi FR Must ≥3
  acceptance criteria · `06-04` mỗi BR có ví dụ tính tay + ≥5 trường hợp biên). Đọc từ **bảng tổng hợp** đã
  có sẵn, nên không sinh việc mới cho người viết.
- **Danh sách "không được cắt trong mọi trường hợp"** ở `05-01` §11. Không phải danh sách tính năng quan
  trọng — là danh sách thứ **không bán được nên bị cắt đầu tiên khi scope phình**, mà cắt xong thì sản phẩm
  sập: đường đi khi bị từ chối quyền · fallback khi thứ chính lỗi · màn chẩn đoán · cam kết đã hứa công khai.
  Cột *"cắt thì hỏng thế nào"* là cột không được bỏ trống.
- **Khối JSON thứ tự thi công** ở `13-01` §6 — agent lập trình đọc trực tiếp thay vì suy từ văn xuôi. Script
  kiểm JSON parse được, **không có vòng phụ thuộc**, mọi `SCR` thuộc đúng một đơn vị. Kèm bảng *affordance
  nằm trên màn của đơn vị khác* — chỗ hay tranh chấp nhất khi chia việc.

**Một điều phải ghi lại cho công bằng:** chất lượng phần nghiên cứu đối thủ của Carbina là **công của người
điều khiển**, không phải của toolkit — chính PO mang số Sensor Tower thật vào và tự phát hiện bảng giá sai.
Bộ mới ép được cái **sàn**; nó không tự tạo ra cái **đỉnh** đó.

---

### Đợt 6 · Nạp hồ sơ cũ vào dự án chạy bộ mới

**Bạn muốn:** đã có sẵn bộ tài liệu như carplay thì đẩy vào dự án chạy toolkit mới thế nào mà vẫn ổn định.

**Nhận ra:** chỗ dễ phá nhất không phải nội dung mà là **hệ mã ID**. Đánh số lại là làm chết mọi tham chiếu
trong ticket, commit và lịch sử chat của dự án. Và bộ tài liệu đã qua nhiều bản luôn có phần được viết lại
và phần **không ai cập nhật theo** — nạp mà không phát hiện thì mâu thuẫn được sao chép nguyên vẹn, rồi từ
đó nó trông chính danh vì đã qua cổng.

**Đã đổi:** lệnh `/import-legacy` (8 bước) + phiếu công tác `research-raw/ho-so-cu/_MAP.md`.

Bốn quy tắc bất di bất dịch: không bao giờ dán file cũ vào `docs/` · **không đánh số lại ID cũ** · prefix lạ
phải xử từng mã, không để lọt · **không kế thừa trạng thái `approved`**.

Hai bước không được bỏ: **lập bản đồ phủ trước khi lấp** và **soi bốn phép tìm mâu thuẫn**. Cột quan trọng
nhất của phiếu là cột *"nội dung cũ đó có dẫn nguồn không"* — hồ sơ cũ thường rất chắc ở chỗ có nguồn và
**bịa hoàn toàn** ở chỗ không có nguồn, mà đọc bề ngoài hai chỗ giống hệt nhau. Chỗ không nguồn khi lấp sang
phải gắn `[ASM]`, tuyệt đối không thành `[FACT]`.

---

### Đợt 7 · Gốc dự án bị "bung ra"

**Bạn nói:** *"toàn bộ tài liệu trong toolkit của tôi bị bung ra hết mà không được gom cụm và sắp xếp."*
(gốc có 15 dòng, bộ app-spec mẫu chỉ 4)

**Nhận ra:** bạn đúng một nửa. Cái "gọn" của bộ mẫu là **gọn giả** — nó giấu hết vào `.claude/specs/<app>/`,
và trong đó 13 file `.md` nằm phẳng lì, không thư mục con, không đánh chặng. Còn bộ của bạn có 61 tài liệu
chia sẵn 14 thư mục theo chặng. Ở đúng chỗ mà "gom cụm" có ý nghĩa, bộ của bạn gom kỹ hơn nhiều. Thứ bị bung
là **gốc dự án**, không phải tài liệu.

Và di chuyển thư mục thì giá rất đắt: `tech-input/` bị nhắc 78 lần trong 37 file, `research-raw/` 89 lần
trong 26 file, `wireframes/` 42 lần trong 14 file, `design-system/` 30 lần. Gần 240 chỗ hard-code, để đổi
lấy việc gốc bớt 4 dòng.

**Đã đổi — làm gốc trông gọn mà không đụng một đường dẫn nào:**

- `.vscode/settings.json` thêm `explorer.fileNesting.patterns`: năm file hướng dẫn gom thành một mũi tên
  dưới `README.md`. Cây thư mục còn **9 dòng** thay vì 15. Nhược điểm phải nói rõ: chỉ có tác dụng trong
  VS Code, mở bằng Windows Explorer vẫn thấy đủ 15.
- Sửa lỗi thật trong `BAT_DAU_TU_DAY.txt`: bước 3 vẫn bảo *"phải thấy đủ 4 thứ"* và sót `research-raw/`,
  `design-system/`, `wireframes/`. Đó chính là thứ làm gốc trông "bung ra" — **file hướng dẫn đầu tiên đang
  mô tả một bộ khác với bộ đang cầm**.
- Thêm `docs/08-screens/_WIREFLOW_O_DAU.md` — file chỉ đường, vì mở thư mục chặng 08 ra thì không biết
  wireflow nằm đâu.

**Lý do `wireframes/` nằm ngoài, ghi lại để không ai hỏi lại:** không có lý do kỹ thuật bắt buộc —
`validate_docs.py` chỉ quét `*.md` và `check_build.py` nhận đường dẫn qua tham số. Ba lý do thật: `docs/` có
**một luật duy nhất** (markdown, front-matter 13 trường, có tên trong `_INDEX`, đi qua cổng) mà wireflow
không thoả điều nào · người xem wireflow không phải người viết tài liệu · chặng 13 gửi `wireframes/` cho Dev
như một gói riêng. Đánh đổi đã chấp nhận: đầu ra của một chặng nằm ở hai chỗ.

---

### Đợt 8 · Wireframe "kể" thay vì "vẽ" — đợt sửa lớn nhất về chất lượng

**Bạn đưa hai ảnh so sánh và nói:** *"Wireframe phải là màn hình đúng tỉ lệ, và nội dung của nó là thứ sau
này sẽ nằm trên UI, chứ không phải đưa một đống thông số vào… thứ tôi cần là layout, nội dung đúng gần với
UI sau này nhất mà user sẽ đọc. Hiện tại rất rất rắc rối."*

**Nhận ra — gốc rễ, và nó không phải chỗ tôi tưởng:**

Agent **kể về** màn hình thay vì **vẽ** màn hình: chỗ dành cho tiêu đề thì nó viết một câu mô tả tiêu đề
(*"Tiêu đề màn, 22pt, tương phản cao nhất"*), chỗ dành cho nút thì nó viết *"Hành động chính của màn"*.

Nhưng nguyên nhân không phải agent lười. **CSS không có phận tử để dựng.** Gặp segmented control hay hàng có
giá trị mà không có class tương ứng thì lựa chọn duy nhất còn lại là mô tả bằng chữ. Và trớ trêu nhất: agent
khi đó viết ra đúng thứ bạn nói không cần (52pt, row 50pt, tương phản) và thiếu đúng thứ bạn cần (nhìn ra bố
cục và vị trí nút).

Thêm hai lỗi thật: khung **không có chiều cao cố định** nên giãn theo nội dung rồi kẹp bằng thanh cuộn —
mất đúng thông tin *cái gì trên màn đầu, cái gì ghim đáy*; và khối ghi chú **lọt vào trong khung máy**, khiến
người xem đọc nó như nội dung app.

**Đã đổi — bốn việc:**

1. **Luật một câu**, viết vào CSS, template, skill và `08-03`: *trong khung máy chỉ có thứ người dùng sẽ đọc
   và chạm trên app thật.* Kèm bảng đúng/sai lấy nguyên các câu sai có thật. Mã truy nguyên và câu JTBD ngôi
   thứ nhất chuyển ra khối ghi chú ngoài khung; khối đó cắt từ **sáu mục xuống ba**.
2. **Bổ sung phận tử**: `.w-seg` · `.w-rowval` (kèm stepper) · `.w-group` · `.w-check` `.w-radio`
   `.w-switch` · `.w-search` · `.w-kb` (bàn phím thật — bàn phím mở là mất nửa vùng nhìn thấy, đó là thông
   tin) · `.w-sheet` + tay nắm · `.w-steps` · `.w-badge` · nút X trên nav. Thiếu gì thì **thêm class**, cấm
   mô tả bằng chữ.
3. **Bộ mẫu để bắt chước**, không phải thêm lời khuyên: `wireframes/_VD_*.html` — bảy màn và một trang
   wireflow dựng đúng chuẩn. Với agent thì **một bản mẫu đúng chặn tốt hơn ba trang quy tắc**.
4. **Máy soi từng file màn**, ra LỖI chứ không phải cảnh báo: ghi chú lọt vào khung · số đo `pt`/`px` trong
   chữ · mã `FR`/`UC`/`SCR`/`ST` trong khung · các cụm mô tả thiết kế.

**Đã đo bằng trình duyệt, không đoán:** cả bảy khung đúng 844px, không khung nào tràn hay sinh thanh cuộn
trong, mọi khung trên trang flow cùng tỉ lệ 203×439. Khối ghi chú đoạn giờ luôn xuống dòng riêng — trước nó
chen giữa các màn nên cao bằng khung máy và bị đọc nhầm là một màn hình.

---

### Đợt 9 · Tầng diễn giải cho nhiều vai trò

**Bạn muốn:** *"UI/UX designer có những thuật ngữ về PO mà họ không hiểu, Dev thì có những thuật ngữ về
UI/UX mà họ không hiểu… nếu vẫn giữ được đầy đủ thông tin khi diễn giải nội dung tài liệu dễ hiểu với nhiều
người hơn thì là tối ưu nhất."*

**Nhận ra:** chỗ nguy hiểm **không phải** đoạn khó hiểu. Nó là chỗ người ở vai trò khác **lướt qua thuật ngữ
lạ, tưởng mình hiểu, rồi vẫn bấm duyệt**. Designer thấy `p95` bỏ qua, Dev thấy `JTBD` bỏ qua, cả hai cùng
gật, sáu tuần sau mới lộ ra hai bên hiểu hai kiểu. Một đoạn khó hiểu thì người ta còn hỏi lại; một đoạn
tưởng-hiểu thì không.

**Nguyên tắc bạn đặt ra và tôi giữ nguyên:** giữ thuật ngữ, **diễn giải là thêm vào chứ không thay thế**.
Người trong nghề cần đúng từ đó để tra cứu và để nói chuyện với bên ngoài.

**Đã đổi — ba cơ chế, áp cho cả 61 tài liệu:**

| Cơ chế | Nội dung |
| --- | --- |
| Mục **`0. Đọc nhanh`** ở đầu | bốn dòng viết **không một thuật ngữ nào**: là gì · ai cần đọc · đọc xong phải biết gì · quyết định nào chốt ở đây |
| Mục **`Thuật ngữ dùng trong tài liệu này`** ở cuối | mọi thuật ngữ và tiền tố mã có dùng, kèm nghĩa một câu |
| Từ điển chung | `docs/_GLOSSARY.md` mục *Thuật ngữ chuyên môn* — **75 từ**, mỗi từ một câu nghĩa và một cột ghi *vai trò nào hay không hiểu từ đó* |

`validate_docs.py` thêm `check_plain_language`: dùng thuật ngữ hoặc mã mà không liệt kê ở bảng cuối →
**LỖI** với tài liệu `approved`, cảnh báo với `draft`; liệt kê thừa → cảnh báo; ô trong `0. Đọc nhanh` để
trống → lỗi; **thuật ngữ lọt vào `0. Đọc nhanh`** → cảnh báo, vì đó là bốn dòng duy nhất phải đọc được bởi
bất kỳ ai.

**Hai chi tiết kỹ thuật quyết định script này có bị bỏ qua hay không:** khớp **dài nhất thắng** (bài viết
*event taxonomy* thì không đòi liệt kê thêm *event*); và script **chỉ tự động ép những từ viết bằng ký tự
latin** — các mục từ tiếng Việt như *trạng thái*, *cổng*, *truy nguyên* vẫn nằm trong từ điển cho người tra
nhưng không ép, vì chúng là từ thường và sẽ khớp ở mọi trang. **Báo động giả nhiều thì người ta bắt đầu bỏ
qua cả báo động thật.**

---

## 3. Bảy nguyên tắc rút ra — phần dùng lại được

Đây là phần đáng đọc nhất nếu sau này bạn sửa tiếp bộ mẫu, hoặc xây một bộ khác.

**1. Con số ép được, lời khuyên thì không.** *"Đã khảo sát các đối thủ chính"* rồi đưa ba dòng là THIẾU,
không phải cô đọng. Câu *"làm kỹ vào"* không bao giờ thay được *"≥40 review từ ≥2 app"*.

**2. Một bản mẫu đúng chặn tốt hơn ba trang quy tắc.** Đợt 8 chứng minh điều này: viết thêm luật vào skill
có tác dụng hạn chế; đặt bảy file mẫu dựng sẵn ngay cạnh để agent bắt chước thì tác dụng lớn hơn hẳn.

**3. Lỗi nguy hiểm nhất nằm ở quan hệ giữa các tài liệu, không nằm trong tài liệu nào.** Từng phần đọc riêng
đều đúng. Đây là lý do `check_stale_inputs` tồn tại, và là lý do cổng phải tách khỏi thứ nó chấm.

**4. Ràng buộc ở mức công cụ thắng ràng buộc bằng lời.** Skill phase 04 **không có** `WebSearch` thì nó
không thể bịa; `deny` trong `settings.json` thì công cụ chặn. Một câu trong `CLAUDE.md` chỉ là một câu.

**5. Chèn lên đầu, không nối vào cuối.** Bản vá nối vào cuối một file 343 dòng là vô dụng: agent đã đọc hai
trăm dòng hướng dẫn *"cứ dựng đi"* trước khi tới được ràng buộc. Mọi khối vá đều chèn lên đầu, kèm câu
*"khối này thắng phần dưới"*.

**6. Đúng chuyên môn vẫn có thể sai vì sai thời điểm.** Chú thích số đo trên wireframe là thứ tốt — ở phase
12. Ở phase 08 nó ép quyết một thứ chưa tới lúc quyết.

**7. Báo động giả giết cả hệ thống kiểm.** Nên `check_plain_language` chỉ ép thuật ngữ latin, và
`check_build.py` được thử bằng fixture để chắc bộ mẫu chuẩn chạy qua **0 lỗi** trước khi phát hành.

---

## 4. Danh mục cơ chế hiện có — cái nào chặn cái gì

| Cơ chế | Chặn lỗi gì | Gỡ ra thì mất gì |
| --- | --- | --- |
| `QUALITY-GATE-MANIFEST` cuối mỗi template | ánh xạ cổng↔tài liệu bị hard-code rải rác rồi lệch nhau | không còn nguồn chân lý duy nhất về cổng |
| Cổng **ba trạng thái** | báo FAIL khi thật ra chỉ là chưa đủ tài liệu | người dùng tưởng chất lượng kém trong khi chỉ là chưa viết xong |
| Giao thức **ba lớp** | agent viết theo trí nhớ rồi đối chiếu sau | mất điểm chặn sớm khi agent hiểu sai đầu bài |
| Định mức **khối lượng** (phase 01–04) | tóm tắt ba dòng rồi gọi là đã khảo sát | tầng bằng chứng rỗng |
| Định mức **chiều sâu** (phase 06) | mỗi FR Must một AC, UC không có nhánh ngoại lệ | Dev phải tự đoán phần khó |
| `check_stale_inputs` | đầu vào sửa sau khi kết luận đã duyệt | lỗi vô hình nhất trong cả bộ |
| Phase 04 **không có WebSearch** | persona bịa | quay lại đúng lỗi số 1 của carplay |
| `check_build.py` tầng luồng | màn mồ côi, mũi tên trống nhãn | luồng thiếu nhánh mà không ai thấy |
| `check_build.py` tầng từng màn | wireframe "kể" thay vì "vẽ" | quay lại đúng vấn đề đợt 8 |
| `check_handover_units` | vòng phụ thuộc, màn không thuộc đơn vị nào | Dev nhận gói bàn giao không thi công được theo thứ tự |
| `check_plain_language` | tài liệu chỉ đọc được bởi người cùng nghề | vai trò khác duyệt mà không thật sự hiểu |
| Danh sách **không được cắt** | cắt nhầm thứ giữ sản phẩm đứng được | sập ở chỗ không ai để ý khi scope phình |
| `/import-legacy` bốn quy tắc | đánh số lại ID, dán file cũ vào `docs/` | chết mọi tham chiếu trong ticket và commit |

---

## 5. Lỗi đã mắc khi xây bộ — và dạng chung của chúng

| Lỗi | Dạng |
| --- | --- |
| `\bSCR-(\d{3})\b` không khớp trong `SCR-012_ST-041_ten.html` vì `_` là word char | giả định về dữ liệu không kiểm lại |
| `12-01` nêu ví dụ `ST-01` trong khi `08-02` cấp `ST-001` | hai chỗ cùng nói một quy ước |
| Thêm `Edit(research-raw/ho-so-cu/**)` vào **deny** trong khi vẫn allow `_MAP.md` — deny thắng | không kiểm thứ tự ưu tiên của luật |
| Script sửa nhiều chỗ thất bại ở assertion thứ hai nên **không ghi gì**, âm thầm mất cả thay đổi thứ nhất | thao tác không nguyên tử |
| `TECH-05` phụ thuộc vòng · `tech-input/README.md` trỏ vào đường dẫn app-spec không tồn tại | bản vá **nối vào cuối** file dài |
| `BAT_DAU_TU_DAY.txt` vẫn bảo "đủ 4 thứ" sau khi gốc đã có 7 | tài liệu hướng dẫn không đi theo thay đổi |

**Dạng chung:** phần lớn không phải lỗi logic mà là **hai chỗ cùng nói một điều rồi lệch nhau**. Đây chính
là lý do nguyên tắc *một nguồn sự thật* được đặt ngang hàng với *checkpoint* và *truy nguyên*.

---

## 6. Trạng thái bản mới nhất

Bản build cuối (2026-08-27): **225 file mới** · 61 template đều có manifest và đủ hai mục mới ·
`validate_docs.py` **0 lỗi 0 cảnh báo** trên bộ trống · `check_build.py` báo đúng ba lỗi mong đợi trên bộ
trống · bảy file mẫu wireflow chạy qua linter **0 lỗi** (không có báo động giả) · gói zip ~1,13 MB.

Từ điển: **75 thuật ngữ**, trong đó **68** được tự động kiểm, cộng **48** tiền tố mã đọc từ `_ID_REGISTRY`.

> Lưu ý: không gian làm việc trên cloud đã bị thu hồi sau phiên 2026-08-27. Bản duy nhất còn lại là **file
> zip bạn đã tải về**. Nếu cần sửa tiếp, phải tải nó lên lại ở phiên mới.

---

## 7. Còn mở và chưa kiểm chứng

**Chưa ai chạy thật:** chưa chạy `/design-docs` từ đầu tới cuối để sinh một tài liệu thật · chưa chạy
Codex/OpenCode thật trên bộ này · chưa nối Pencil thật · `new-project.bat` chưa thử trên Windows.

**Câu còn mở:**

- **Phase QA/nghiệm thu sau bàn giao** — nếu Dev làm test thì có cần phase 14, hay `13-04` là đủ.
- **Bộ `permissions`** — đang mặc định **giữ**, dù bạn từng nói *"không cần vá gì"*. Muốn xem từng diff
  trước khi ghi thì đổi `acceptEdits` thành `default`.
- **Copy deck đi sau wireframe.** `09-06` chốt câu chữ ở chặng 09, tức là **sau** wireflow ở chặng 08. Chữ ở
  chặng 08 là chữ thật mình định dùng, và khi chốt copy deck phải quay lại sửa wireflow cho khớp — hiện
  **chưa có script nào bắt chỗ lệch đó**. Đây là khoảng trống đã biết, chưa vá.
- **Nạp hồ sơ cũ sẽ thiếu hai mục mới.** Tài liệu lấp ra bằng `/import-legacy` không có `0. Đọc nhanh` và
  bảng thuật ngữ cho tới khi điền; script sẽ báo, nhưng ở mức cảnh báo vì bản lấp luôn là `draft`.

**Chín chỗ đáng để mắt ở dự án đầu tiên:** tài liệu đầu phase 01 báo `CHƯA ĐỦ ĐIỀU KIỆN XÉT` chứ không phải
`FAIL` · có hỏi *"tự đào hay để Codex đào"* ở đầu phase 01 và 12 · có **hỏi nhánh dựng** thay vì tự chọn ·
có viết `03-05` ngay sau `03-02` · có tự phán quyết khả thi khi chưa có `TECH-00` · ID mới có được ghi vào
`_ID_REGISTRY` · `12-00` có bị viết sau `12-01` · wireframe có **giữ xám** hay tự thêm màu · nhánh Pencil có
thật sự **dừng sau một lô** hay dựng liền cả bộ.

---

## 8. Ràng buộc bảo mật còn hiệu lực

`.mcp.json` chứa khoá Figma, nằm trong `.gitignore` — **không commit**. Ở repo GitLab của team cho dự án
`carplay` thì `.mcp.json` **đã được commit**, khoá có thể đã lộ: nên hỏi ViTu, thêm vào `.gitignore` và
**xoay khoá**.

Không đẩy 11 skill gốc hay nội dung app-spec lên GitHub kể cả repo private khi chưa được phép — app-spec là
tài sản công ty trên `svn.as.local`, chỗ hợp lệ là **GitLab nội bộ**.

Không chạy lệnh cài `uvx` bên trong một thư mục dự án đã có. Không nên mặc định
`--dangerously-skip-permissions`, nhất là khi có `.mcp.json`.

---

## 9. Thuật ngữ dùng trong tài liệu này

| Thuật ngữ / tiền tố mã | Nghĩa một câu |
| --- | --- |
| `AC` | Acceptance criteria — điều kiện cụ thể để nói một yêu cầu đã làm xong |
| `ASM` | Giả định tạm thời do thiếu dữ liệu, có ghi ở sổ giả định |
| `BR` | Business rule — quy tắc tính toán hoặc nghiệp vụ, đúng ở mọi màn hình |
| `CAP` | Năng lực kỹ thuật cốt lõi, mô tả bằng năng lực chứ không nêu tên công nghệ |
| `DEC` | Một quyết định đã chốt, có ghi vào sổ quyết định |
| `DQ` | Câu hỏi gửi Dev, ghi ở sổ câu hỏi bàn giao |
| `FR` | Functional requirement — một việc app phải làm được |
| `JTBD` | Việc người dùng đang cần làm xong, mô tả theo việc họ muốn xong chứ không theo tính năng |
| `SCR` / `ST` | Một màn hình / một trạng thái của màn hình đó |
| `UC` | Use case — một lượt người dùng dùng app để xong một việc, kể theo từng bước |
| `UIP` | Một quan sát rút từ moodboard ở bước nghiên cứu UI |
| Acceptance criteria | Điều kiện kiểm được bằng thao tác để nói một yêu cầu đã xong |
| Affordance | Dấu hiệu thị giác cho người dùng đoán được cái này bấm được hay kéo được |
| Edge case | Tình huống hiếm nhưng có thật, dễ làm hỏng: mất mạng, dữ liệu rỗng, bấm hai lần |
| Moodboard | Tập ảnh tham khảo gom lại để chốt hướng thị giác trước khi thiết kế |
| MVP | Bản đầu tiên nhỏ nhất vẫn giải quyết trọn vấn đề cho một nhóm người |
| Persona / proto-persona | Bản mô tả một kiểu người dùng; *proto* nghĩa là dựng khi chưa có dữ liệu, tức là phỏng đoán |
| PRD | Tài liệu mô tả sản phẩm sẽ làm gì và vì sao |
| p95 | Con số mà 95 trên 100 lần đo nằm dưới mức đó — dùng thay số trung bình vì trung bình giấu mất lần chậm |
| Wireframe / wireflow | Bản vẽ màn hình chưa có màu; *wireflow* là nhiều bản như vậy nối bằng mũi tên có nhãn |
