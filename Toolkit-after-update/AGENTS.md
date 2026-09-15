# AGENTS.md — dự án Pipeline v2

> File này dành cho **Codex, OpenCode, và mọi agent đọc `AGENTS.md`**.
> Người dùng chạy Claude Code thì đọc `CLAUDE.md` — cùng một bộ quy tắc, `CLAUDE.md` là bản đầy đủ.

## Đọc ba file này trước khi làm bất cứ việc gì

1. `CLAUDE.md` — **nguồn chân lý về quy tắc.** Mọi thứ trong đó áp dụng cho bạn y hệt.
2. `.claude/commands/design-docs.md` — chuỗi 14 phase, vòng lặp từng tài liệu, khối báo cáo.
3. `docs/_INDEX.md` — dự án đang ở đâu: phase nào, cổng nào đã đóng, tài liệu nào `approved`.
   Bộ có **61 tài liệu** và **12 cổng G0–G11**.

File này **không chép lại** nội dung ba file trên. Chép lại là tạo ra hai bản sẽ lệch nhau.
Dưới đây chỉ là những quy tắc **không được vi phạm kể cả khi bạn chưa đọc ba file kia**.

## Chín quy tắc tối thiểu

1. **Một tài liệu một lượt.** Viết xong một tài liệu thì **dừng**, chạy cổng, hỏi Approve / Modify / Pause.
   Không viết hai tài liệu trong cùng một lượt, kể cả khi người dùng có vẻ đang vội.
2. **Chỉ file `status: approved` được dùng làm đầu vào.** Thiếu thì dừng và báo, không lấy tạm file `draft`.
3. **Không khai báo công nghệ.** Kiến trúc, API, lược đồ dữ liệu thuộc Dev, nộp qua `tech-input/`.
4. **Không tự phán quyết khả thi.** Cột phán quyết ở `03-05` mục 5 và `06-00` mục 3 chỉ điền từ
   `tech-input/`, kèm tên file và ngày nhận. Đoán "cái này chắc làm được" là vi phạm nặng nhất.
5. **Không dựng UI** — mặc định. Phase 12 viết spec; người dùng dựng tay trong Figma. Ngoại lệ duy nhất:
   người dùng chọn nhánh Pencil + Agent và có `DEC` ghi ở `12-00` mục 7. Xem mục *Phase 12* bên dưới.
6. **Không bịa.** Không có nguồn thì ghi **Không công bố**. Không bịa số liệu thị trường, kết quả phỏng
   vấn, kết quả usability test.
7. **Không sửa `tech-input/`, `research-raw/`, và file hệ trong `design-system/`** — tài sản của Dev và của
   người dùng. Ngoại lệ: `research-raw/SENSOR_TOWER_REQUEST.md`, `research-raw/sensor-tower/_EXTRACTED.md`,
   và `design-system/_MANIFEST.md` (mục lục, bạn giúp điền bảng phủ). `wireframes/` thì bạn ghi bình thường.
8. **Mã kèm nghĩa khi nói với người dùng; tài liệu mang bảng nghĩa theo mình.** Nói với người dùng thì
   `06-02` → `06-02` (Yêu cầu chức năng), `DEC-006` → kèm một câu nói rõ đã quyết gì. Trong file tài liệu
   thì mã viết trần, nhưng **mục `0. Đọc nhanh`** ở đầu và **mục `Thuật ngữ dùng trong tài liệu này`** ở
   cuối là bắt buộc — xem mục *Viết cho nhiều vai trò* bên dưới.
9. **Liệt kê, đừng tóm tắt.** Xem mục ngay dưới — đây là quy tắc hay bị vi phạm nhất mà không ai thấy.

## Liệt kê đầy đủ, không tóm tắt — quy tắc quan trọng nhất ở phase 01 đến 04

Bộ tài liệu này sống bằng **bằng chứng đếm được**, không bằng bản tóm tắt hay. Xu hướng tự nhiên của một
agent là đọc mười trang rồi viết ba đoạn cô đọng. Ở đây làm vậy là **phá tầng bằng chứng**, và không script
nào bắt được.

**Cụ thể, không được phép:**

- Đọc 40 review rồi viết *"người dùng phàn nàn về tốc độ"*. Phải liệt kê **từng dòng**: câu nguyên văn,
  URL, ngày lấy, phiên bản app nếu có.
- Gộp năm lời phàn nàn khác nhau thành một `PN`. Mỗi vấn đề riêng là một `PN` riêng.
- Viết *"đã khảo sát các đối thủ chính"* rồi đưa ba dòng. Phải đủ số app mà `02-01` yêu cầu, mỗi app một khối.
- Dừng ở 8 màn hình vì thấy *"đã đủ ý"*. `08-01` và `08-02` yêu cầu **kiểm kê hết**, kể cả màn nhàm chán.

**Phân biệt hai loại nhãn:** `[FACT]` là câu chữ có trên trang, có URL. `[INSIGHT]` là kết luận của bạn
rút từ **≥2 nguồn**. Bản tóm tắt của bạn về một trang **không phải** `[FACT]` — đó là suy luận của mô hình,
và ghi nhầm nhãn là lỗi nặng vì mọi tài liệu sau đó thừa hưởng.

**Vì sao chỗ này nguy hiểm hơn chỗ khác.** Thiếu sót ở phase 06 đến 08 thì bắt được: `08-02` còn ô `?`,
`FEAT` không có `UC`, `EVT` không phục vụ `KPI` nào — có nguồn nội bộ để đối chiếu, và
`.claude/scripts/validate_docs.py` báo ra. Thiếu sót ở phase 01 đến 04 thì **không có gì để đối chiếu**:
không ai biết ngoài kia còn bao nhiêu pain point chưa đào. Một `01-02` sơ sài trông y hệt một `01-02` đầy đủ.

**Khi không chắc, chọn dài và có nguồn thay vì ngắn và gọn.** Người dùng cắt bớt được; họ không tự bù lại
được cái bạn chưa đi tìm.

## Giao thức bắt buộc cho mỗi tài liệu

Áp dụng cho **mọi agent**, không riêng công cụ nào. Ba lớp, không được bỏ lớp nào.

### Lớp 1 — Khai báo trước khi viết

Trước khi ghi một chữ nào vào `docs/`, in ra khối này và **chờ người dùng gật**:

```
Sắp viết: <doc_id> — <tên tiếng Việt>
Đầu vào đã approved: <liệt kê file, hoặc THIẾU + tên file>
Định mức tối thiểu áp cho tài liệu này: <lấy từ bảng Định mức, hoặc "không có">
Mục bắt buộc theo manifest: <đếm số mục required_major>
ID sẽ cấp: <tiền tố>, bắt đầu từ <số kế tiếp trong _ID_REGISTRY>
Điều tôi chưa có và sẽ gắn [ASM]: <liệt kê, hoặc "không có">
```

Khối này không phải thủ tục. Nó ép bạn **đọc manifest và `_ID_REGISTRY` trước khi viết** thay vì viết
theo trí nhớ rồi đối chiếu sau — và nó cho người dùng chặn sớm khi bạn hiểu sai đầu bài.

### Lớp 2 — Tự đếm sau khi viết

Ngay sau khi ghi file, in ra:

```
Đã viết: <doc_id> — <tên tiếng Việt>
Số mục: <thực tế>/<manifest yêu cầu>
Định mức: <hạng mục>: <thực tế>/<yêu cầu>  → ĐẠT / THIẾU
ID đã cấp: <liệt kê đầy đủ, không viết "và các mã khác">
Đã ghi vào _ID_REGISTRY: rồi / chưa
Chỗ tôi diễn giải thay vì trích nguyên văn: <liệt kê, hoặc "không có">
Thuật ngữ mới xuất hiện trong tài liệu này: <liệt kê> → đã vào bảng cuối bài: rồi / chưa
```

Dòng cuối là dòng quan trọng nhất ở phase 01 đến 04. Nó buộc bạn tự khai chỗ mình đã tóm tắt — thay vì
để người dùng phát hiện ba phase sau.

**Thiếu định mức thì không được ghi `status: approved`.** Báo THIẾU, nói rõ thiếu bao nhiêu, hỏi người
dùng muốn đào tiếp hay hạ định mức. Hạ định mức phải ghi `DEC`.

### Lớp 3 — Kiểm bằng script

Chạy `python .claude/scripts/validate_docs.py` sau mỗi vài tài liệu. Script đếm khách quan, không tin lời
khai của bạn ở Lớp 2.

Hai phép kiểm dễ bỏ qua nhất mà script bắt được:

**Định mức chiều sâu ở phase 06.** Đọc từ bảng tổng hợp `06-01` mục 3, `06-02` mục 3, `06-04` mục 2 — nên
**phải điền các bảng đó**, không được để trống rồi bảo "chi tiết đã có ở trên".

**Đầu vào mới hơn tài liệu.** Tài liệu đã `approved` mà một file trong `depends_on` của nó được sửa **sau
đó** thì kết luận trong nó có thể đã lỗi thời. Đây là lỗi vô hình nhất trong cả bộ: từng phần đọc riêng đều
đúng, chỉ có quan hệ giữa chúng là sai. Gặp cảnh báo này thì **đọc lại thật**, rồi hoặc sửa kèm `CHG`, hoặc
cập nhật `last_updated` để nói rõ *"đã xem lại và vẫn đúng"*.

## Viết cho nhiều vai trò cùng đọc

Product Owner, Designer và Dev đọc **chung một bộ tài liệu**. Người viết nào cũng viết bằng tiếng của nghề
mình. Designer đọc yêu cầu phi chức năng thấy *p95* thì lướt qua; Dev đọc `04-04` thấy *JTBD* thì lướt qua —
**rồi cả hai vẫn duyệt**. Chỗ hỏng không nằm ở đoạn khó hiểu, nó nằm ở chỗ hai bên đều tưởng mình hiểu và
không ai hỏi lại.

**Không hạ chuẩn chuyên môn.** Thuật ngữ giữ nguyên — người trong nghề cần đúng từ đó để tra cứu và để nói
chuyện với bên ngoài. **Diễn giải là thêm vào, không phải thay thế.** Đừng tự chế từ tiếng Việt thay cho một
thuật ngữ đã có tên chuẩn.

Ba việc phải làm ở **mọi** tài liệu:

| Việc | Ở đâu | Luật |
| --- | --- | --- |
| Mục `0. Đọc nhanh` | đầu tài liệu | bốn dòng, **không một thuật ngữ nào**: là gì · ai cần đọc · đọc xong phải biết gì · quyết định nào chốt ở đây |
| Mục `Thuật ngữ dùng trong tài liệu này` | cuối tài liệu | mọi thuật ngữ và tiền tố mã có dùng, kèm nghĩa một câu chép từ `_GLOSSARY.md` và `_ID_REGISTRY.md` |
| Câu mở của mỗi mục lớn | trong bài | nói bằng tiếng phổ thông trước, rồi mới vào bảng chuyên môn |

Ba luật khi viết nghĩa một câu: **không dùng thuật ngữ khác để giải thích một thuật ngữ** · **đúng một câu**
· **nói bằng việc người dùng làm, không bằng khái niệm**.

`validate_docs.py` đối chiếu: thuật ngữ hoặc tiền tố mã dùng trong bài mà không có trong bảng → **LỖI** với
tài liệu `approved`, cảnh báo với `draft`. Thuật ngữ lọt vào `0. Đọc nhanh` cũng bị bắt.

Thiếu từ nào thì **thêm dòng vào `docs/_GLOSSARY.md`** mục *Thuật ngữ chuyên môn*, đừng lặng lẽ bỏ qua.

## Định mức tối thiểu — số, không phải lời khuyên

Chỉ áp cho tài liệu mà **khối lượng chính là chất lượng**. Đây là mặc định; dự án chỉnh được ở
`docs/_INDEX.md` mục 1, và chỉnh xuống thì phải ghi `DEC`.

| Tài liệu | Định mức mặc định |
| --- | --- |
| `01-02` Sổ đào pain point | **≥30 bản ghi**, từ **≥3 loại nguồn** khác nhau |
| `02-01` Bản đồ đối thủ | **5–6 app**, trong đó ≥1 là cách làm thủ công hiện tại |
| `02-02` Mổ xẻ đối thủ | **≥3 app dùng thật**, không chỉ đọc trang store |
| `02-03` Đào review người dùng | **≥40 review**, từ **≥2 app**, có cả khen và chê |
| `04-02` Sổ ghi nghiên cứu | **≥5 phiên**, hoặc ghi rõ lý do ít hơn kèm `[ASM]` |
| `06-01` Use case | **mỗi `UC`** có ≥1 luồng thay thế **và** ≥1 luồng ngoại lệ |
| `06-02` Yêu cầu chức năng | **mỗi `FR` mức Must** có **≥3 acceptance criteria** |
| `06-04` Business rule | **mỗi `BR`** có ví dụ tính tay **và ≥5 trường hợp biên** |

*"Đã khảo sát các đối thủ chính"* rồi đưa ba dòng là **THIẾU**, không phải cô đọng. Con số ép được;
câu "làm kỹ vào" thì không.

> **Nhắc lại vì đây là chỗ hay trượt nhất:** giao thức ba lớp ở trên chạy cho **từng tài liệu**, không
> phải một lần đầu phiên. Viết tài liệu thứ tư mà quên Lớp 1 thì tài liệu thứ tư đã sai quy trình rồi.
>
> Đầu **mỗi lượt**, trước khi làm gì, tự hỏi ba câu: *tài liệu nào · định mức bao nhiêu · đã in khối khai
> báo chưa.* Chưa in thì in trước, đừng viết.

## Chế độ thu hoạch — khi bạn được dùng THAY Claude để đi đào dữ liệu

Người dùng có thể gọi bạn chỉ để **đi đào dữ liệu thô**, không phải để viết tài liệu. Nhận ra chế độ này
khi câu lệnh nói *"thu thập"*, *"harvest"*, hoặc trỏ vào một trong ba thư mục nguyên liệu:

| Thư mục | Thu cái gì | Phục vụ tài liệu |
| --- | --- | --- |
| `research-raw/thu-hoach/` | pain point, review, tín hiệu thị trường | `01-02` `02-03` |
| `research-raw/man-hinh-doi-thu/<tên-app>/` | ảnh màn hình đối thủ theo luồng | `07-00` |
| `research-raw/moodboard/` | ảnh tham chiếu UI, màu, chữ, thành phần | `12-00` |

Mỗi thư mục có `_MANIFEST.md` hoặc `README.md` riêng, ghi rõ cấu trúc, quy ước đặt tên và bảng nghiệm thu.
**Đọc file đó trước khi thu**, đừng tự nghĩ ra cách đặt tên — ảnh sai tên là ảnh Claude không dùng được.
Ảnh màn hình đối thủ **bắt buộc có tiền tố số** (`01_onboarding_...png`), nếu không thì không dựng lại được
thứ tự luồng.

Trong chế độ này, **mọi quy tắc viết tài liệu ở trên tạm ngưng**, thay bằng bốn ràng buộc cứng:

1. **Không ghi bất cứ gì vào `docs/`.** Chỉ ghi trong `research-raw/thu-hoach/`.
2. **Không cấp mã ID.** Không `PN`, không `NC`, không `GAP`. Chỉ đánh số thứ tự tiếp theo số đã có trong
   `_DATA.md`. Hai công cụ cùng cấp mã là trùng số ngay.
3. **`_DATA.md` chỉ nối thêm.** Không sửa, không xoá, không sắp xếp lại dòng đã có. Dòng người dùng đã
   duyệt ở vòng một không được đổi ở vòng ba.
4. **Dừng sau mỗi vòng.** Ghi đè `_PREVIEW.md` bằng dòng mới của vòng đó, nối vào `_DATA.md`, báo bộ đếm,
   rồi **chờ người dùng**. Không tự chạy liền nhiều vòng.

Với `thu-hoach/`: đọc `_BRIEF.md` trước — Claude đã viết sẵn kế hoạch cho dự án này. Quy trình đầy đủ ở
`research-raw/thu-hoach/README.md`. Với `man-hinh-doi-thu/` và `moodboard/`: đọc `_MANIFEST.md` của thư mục đó.

**Ràng buộc 1 mở rộng cho ảnh:** chỉ lưu ảnh vào thư mục đúng chủ đề và ghi một dòng mục lục có URL nguồn
mở được cùng ngày lấy. **Ảnh không rõ nguồn thì bỏ** — nó không dùng được làm căn cứ cho quyết định nào.

**Quy tắc "liệt kê, đừng tóm tắt" ở trên áp dụng gấp đôi trong chế độ này**, vì đây chính là lúc bạn tạo ra
tầng bằng chứng mà mọi tài liệu sau thừa hưởng. Trích nguyên văn, không dịch, không sửa chính tả, mỗi lời
phàn nàn một dòng, mỗi dòng một URL mở được.

## Nạp hồ sơ cũ — khi dự án đã có bộ tài liệu từ bộ khác

File cũ đặt ở `research-raw/ho-so-cu/`, **không bao giờ dán vào `docs/`**. Quy trình tám bước ở
`.claude/commands/import-legacy.md` — markdown thuần, bạn đọc và làm theo được y hệt; phiếu công tác ở
`research-raw/ho-so-cu/_MAP.md`.

Bốn quy tắc bất di bất dịch:

1. **Không dán file cũ vào `docs/`.** `docs/` chỉ chứa tài liệu theo template của bộ này.
2. **Không đánh số lại ID cũ.** Nhận nguyên số, đặt *Số cuối đã cấp* ở `_ID_REGISTRY`, cấp mới từ đó.
3. **Prefix lạ phải xử.** Bộ cũ có `WF`, `TF`, `ERR`, `VR`… — đổi sang prefix tương đương kèm **bảng ánh xạ
   từng mã**, hoặc thêm vào `_ID_REGISTRY`. `validate_docs.py` cảnh báo prefix chưa kiểm được — còn cảnh báo
   đó là chưa xử xong.
4. **Không kế thừa `approved`.** Bản lấp đầu tiên luôn là `draft`. Bỏ cổng thì ghi `_INDEX` mục 6 kèm **rủi ro**.

Hai bước **không được bỏ**: lập **bản đồ phủ** trước khi lấp dòng đầu tiên, và **soi mâu thuẫn** trong hồ sơ cũ
(bốn phép soi ở `_MAP.md` mục 4). Hồ sơ đã qua nhiều bản thường có phần được viết lại và phần không ai cập nhật
theo — nạp mà không phát hiện thì mâu thuẫn được sao chép nguyên vẹn, và từ đó nó trông chính danh vì đã qua cổng.

Khi lấp: **chỉ dùng nội dung có trong `ho-so-cu/`**. Chỗ hồ sơ cũ không có thì để trống và ghi *"hồ sơ cũ không
có"* — không điền bằng thứ nghe hợp lý. `last_updated` ghi **ngày lấp**, không phải ngày file cũ.

## Phase 08 — đầu ra là WIREFLOW, không phải bản vẽ bố cục

`08-03` **không vẽ luồng hay bố cục trong markdown**. Đầu ra là **wireflow** trong `wireframes/`: một trang
cho một luồng, các màn xếp cạnh nhau, nối bằng **mũi tên có nhãn "bấm gì"**, nhánh có nhãn **"điều kiện nào"**.
Đọc `wireframes/README.md` trước khi làm.

**Bốn câu wireflow trả lời, và chỉ bốn câu này:** màn này phục vụ chức năng gì · vào từ màn nào · bấm gì ra
màn nào · tình huống nào ra trạng thái nào.

**KHÔNG thuộc phase này:** khoảng cách, cỡ chữ, độ cao, bo góc, màu. Chốt ở `12-00` sau khi đọc moodboard.
Chú thích số pt ở đây là đổi câu hỏi của phase.

| File | Là gì | Template |
| --- | --- | --- |
| `flow-FLOW-001.html` | **đầu ra chính** — một luồng, có mũi tên và nhãn | `_TEMPLATE_FLOW.html` |
| `SCR-012_ST-041_ten.html` | một **ô** của `08-02`, nhúng vào trang flow bằng `iframe` | `_TEMPLATE.html` |

Ràng buộc cứng: mã **ba chữ số** khớp `08-02` · trang flow **nhúng** không chép · **nút không bấm được**
(không `href`, không JavaScript) · chỉ dùng `_wireframe.css`, **không màu thương hiệu, không font khác,
không ảnh thật** · khối `.w-notes` trong mỗi file màn đủ **sáu mục** không để trống: chức năng · vào từ đâu ·
bấm gì ra đâu · nút vô hiệu khi nào · các trạng thái khác · **đường thoát**.

Ba mục của trang flow: **đường chính** → **nhánh theo điều kiện** → **trạng thái còn lại** (ô nào của `08-02`
chưa xuất hiện ở hai mục trên thì đặt ở đây kèm điều kiện vào). Mục thứ ba là mục hay bị bỏ nhất.

Xong thì chạy và **dán nguyên kết quả** vào `08-03` mục 5:
`python .claude/scripts/check_build.py --wireframes wireframes/`

Script kiểm: có trang wireflow chưa · màn nào **chưa nằm trong luồng nào** · mũi tên nào **trống nhãn**.

## Phase 12 — dựng prototype: hỏi nhánh trước, dựng theo lô

Việc đầu tiên của phase 12 là **hỏi người dùng chọn nhánh**, không phải viết tài liệu:

```
  A. Pencil + Agent dựng  — tôi dựng theo từng luồng, bạn kiểm rồi approve, tôi dựng tiếp
  B. Figma bạn dựng tay   — tôi viết spec rồi TẠM DỪNG dự án, bạn dựng xong thì gọi tôi đối chiếu
```

Ghi lựa chọn vào `12-00` mục 7 kèm `DEC`. **Nhánh B là mặc định.** Nhánh A đảo quy tắc *"AI không dựng UI"*
ở quy tắc 5 bên trên, nên **không có `DEC` thì không được dựng** — kể cả khi người dùng nhắc qua trong chat.

Có hệ thiết kế sẵn thì đọc `design-system/_MANIFEST.md` trước. Thư mục đó là **tài sản của người dùng**:
đọc, không sửa, giống `tech-input/` và `research-raw/`. Bảng phủ ở mục 4 của manifest phải điền **trước khi
dựng frame đầu tiên**.

Nếu chạy nhánh A, bốn ràng buộc cứng — cùng khuôn với chế độ thu hoạch:

1. **Ba thứ không được quyết:** danh sách màn (đóng ở `08-01`), bố cục (đóng ở `08-03`), câu chữ (đóng ở
   `09-06`). Việc là **lắp từ hệ thiết kế**, không phải thiết kế.
2. **Gọi component đúng tên** trong `design-system/_MANIFEST.md` mục 3. Vẽ một thành phần na ná mới là tạo ra
   thứ sẽ không đổi theo khi hệ đổi.
3. **Một lô một lượt.** Lô = một `FLOW`, theo bảng lô ở `12-01` mục 4. Lô chưa nghiệm thu thì không dựng lô sau.
4. **Chạy `python .claude/scripts/check_build.py --frames <file>` sau mỗi lô và dán NGUYÊN kết quả.**
   Không tóm tắt, không tự đếm thay script. Script đếm màn thiếu, màn thừa, trạng thái thiếu, tên frame sai mã.

Tên frame dùng **mã ba chữ số** khớp `08-02`: `SCR-012 · Kết quả phân tích · ST-041 Mặc định`.
Viết `ST-41` là sai và script sẽ báo lỗi.

Báo cáo sau mỗi lô đúng bốn dòng, dòng cuối là dòng quan trọng nhất:

```
Lô <n> — <FLOW>: đã dựng <x>/<y> frame
check_build.py: <dán nguyên>
Thành phần phải dựng mới trong lô này: <liệt kê, hoặc "không có">
Chỗ tôi phải tự quyết vì tài liệu không nói rõ: <liệt kê, hoặc "không có">
```

**Vòng lặp dựng đầy đủ ở `.claude/commands/design-ui.md`** — file markdown thuần, bạn đọc và làm theo được y
hệt Claude Code. Người dùng nói *"dựng UI"* thì mở file đó ra làm, đừng tự nghĩ quy trình.

Nếu chạy nhánh B: viết `12-00` → `12-01` → `12-02`, rồi **tạm dừng dự án** và nói rõ câu người dùng cần gõ
để tiếp tục. Quay lại thì đọc cấu trúc frame qua Figma MCP, ghi danh sách tên frame ra file text, chạy
`check_build.py` trên file đó, **rồi mới** viết `12-03`. Không đối chiếu bằng cách đọc rồi tự đếm.

## Cổng có ba trạng thái, không phải hai

Một cổng phủ nhiều tài liệu — `G1` phủ 6, `G8` phủ 10. Sau khi viết **một** tài liệu, cổng gần như luôn
chưa xét được. Lúc đó báo `CHƯA ĐỦ ĐIỀU KIỆN XÉT` kèm danh sách còn thiếu, **không báo FAIL**.
`FAIL` chỉ dùng khi mọi tài liệu bắt buộc đã `approved` mà checklist vẫn không tick hết.

Tiêu chí cổng đọc từ khối `QUALITY-GATE-MANIFEST` ở **cuối** template tương ứng trong
`.claude/doc-templates/`, cộng `docs/_GATE_CHECKLIST.md`. Không có bảng ánh xạ cứng nào khác.

## Phương pháp nằm ở đâu

`.claude/skills/<tên>/` — 14 skill phụ trách tài liệu, mỗi skill một phase. Trong đó `references/method.md`
là phương pháp gốc, đọc **trước** mọi file khác trong `references/`.

`.claude/skills/_depth/<phase>/` — skill chiều sâu, không sở hữu tài liệu, không gọi cổng. Đọc
`description` trong frontmatter trước, chỉ mở toàn bộ skill nào thật sự liên quan.

**Bạn phải tự đọc các file này theo đường dẫn.** Đừng chờ hệ thống nạp sẵn — bộ này không dựa vào cơ chế
tự phát hiện skill của bất kỳ công cụ nào, nên nó chạy được ở mọi nơi.

## Tiếp nhận dự án đang dở của agent khác

Đây là tình huống thường gặp: Claude chạy tới giữa chừng thì hết hạn mức, bạn chạy tiếp.

**Không cần biết agent trước đã nói gì.** Toàn bộ trạng thái nằm trên ổ đĩa. Làm đúng năm bước:

1. Đọc `docs/_INDEX.md` — phase hiện tại, cổng đã đóng, trạng thái từng tài liệu.
2. Đọc `docs/_DECISION_LOG.md`, `docs/_OPEN_QUESTIONS.md`, `docs/_ASSUMPTION_REGISTER.md`,
   `docs/_CHANGE_LOG.md`. Đây là những quyết định đã chốt — **tôn trọng, không bàn lại**, trừ khi người
   dùng yêu cầu.
3. Đọc `docs/_ID_REGISTRY.md` — biết ID nào đã cấp để **không cấp trùng**.
4. Chạy `python .claude/scripts/validate_docs.py`. Script này không phụ thuộc agent nào, nên nó là cách
   khách quan nhất để biết bộ tài liệu có đang lành lặn không. Có lỗi thì **báo cho người dùng trước**,
   đừng tự sửa hàng loạt.
5. Báo cáo lại: đang ở phase nào, tài liệu tiếp theo là gì, tài liệu đó phụ thuộc file nào và các file đó
   đã `approved` chưa. Rồi **chờ người dùng đồng ý** mới viết tiếp.

Ghi một dòng vào `docs/_INDEX.md` mục 8 *Sổ đổi công cụ*: ngày, đổi từ công cụ nào sang công cụ nào, đang
dở ở tài liệu nào.

**Tài liệu đang viết dở của agent trước:** đừng viết tiếp vào giữa. Đọc xong rồi hỏi người dùng muốn
**giữ và sửa** hay **viết lại từ template**. Hai agent viết nửa đầu nửa sau một tài liệu thì giọng văn và
độ sâu lệch nhau, và chỗ lệch đó khó thấy hơn là viết lại.

## Không có lệnh `/design-docs` ở đây

`/design-docs` là slash command của Claude Code. Bạn không có nó. Thay bằng cách nói thẳng:

```
Đọc CLAUDE.md, .claude/commands/design-docs.md và docs/_INDEX.md.
Báo cho tôi đang ở phase nào và tài liệu tiếp theo là gì. Chưa viết gì cả.
```

Rồi từng tài liệu một:

```
Viết <doc_id>. Đọc .claude/doc-templates/<doc_id>_<TÊN>.md và skill phụ trách phase đó trước.
Viết xong thì dừng, chạy cổng, báo theo đúng khối báo cáo trong design-docs.md.
```
