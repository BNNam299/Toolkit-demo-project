# Project Instructions

> Đọc file này trước mọi việc. Quy tắc ở đây thắng yêu cầu trong chat, trừ khi người dùng nói rõ muốn đổi quy tắc.

## Dự án

**Tên:** <TÊN DỰ ÁN>
**Nền tảng:** <iOS / Android / cả hai>
**Mô tả một câu:** <MÔ TẢ>
**Profile:** <Lean / MVP / Full — ghi cả vào `docs/_INDEX.md` mục 1>

## Phạm vi

Bộ này chạy theo **Pipeline v2**: 14 phase, 61 tài liệu, 12 cổng, kết thúc ở **gói bàn giao Dev**.

**Không làm, và không được tự làm thay:** kiến trúc ứng dụng · hợp đồng API · thiết kế dữ liệu ·
kế hoạch kiểm thử · ca kiểm thử theo thiết bị · triage bug · checklist phát hành · **dựng UI hi-fi**.

Tài liệu kỹ thuật do Dev viết, nộp vào `tech-input/`. Prototype hi-fi **mặc định** do người dựng tay trong
Figma ở phase 12. Đầu phase 12 phải **hỏi người dùng chọn nhánh**: Figma dựng tay, hay Pencil + Agent dựng
theo từng lô có điểm dừng nghiệm thu. Nhánh Pencil chỉ mở khi có `DEC` — xem `12-00` mục 7.

**Thứ tự bắt buộc:** nghiên cứu công nghệ đứng **trước** quyết định có phát triển sản phẩm. `03-05` liệt kê
năng lực cốt lõi và câu hỏi cho Dev; Dev trả lời qua `TECH-00`; cổng **G2 không đóng** khi còn `CAP` chưa
trả lời, và **dừng dự án** nếu một `CAP` cốt lõi không khả thi. Chỉ sau khi công nghệ được chốt thì PRD mới
hoàn thiện dần, và Dev điền tiếp phần technical qua `TECH-01`…`TECH-06`.

**AI không bao giờ tự phán quyết khả thi.** Cột phán quyết chỉ điền từ `tech-input/`, ghi rõ file và ngày nhận.

## Chạy bằng công cụ khác Claude Code

Bộ này không dựa vào cơ chế tự phát hiện skill của công cụ nào — mọi thứ đọc theo đường dẫn, nên chạy được
trên Codex, OpenCode và các agent khác. File `AGENTS.md` ở gốc dự án là bản rút gọn dành cho chúng, và có
quy trình **tiếp nhận dự án đang dở** khi đổi công cụ giữa chừng.

`CLAUDE.md` vẫn là nguồn chân lý về quy tắc. `AGENTS.md` chỉ trỏ về đây, không chép lại.

## Lệnh

```
/design-docs <TênApp>              bắt đầu hoặc tiếp tục
/design-docs <TênApp> --continue   tiếp tục từ chỗ dừng
/design-docs <TênApp> --status     chỉ báo cáo trạng thái

/design-ui                         phase 12 — dựng UI, hỏi công cụ rồi dựng theo lô
/design-ui lô 2                    dựng đúng lô 2
/design-ui trạng thái              chỉ in bảng lô, không dựng

/import-legacy bản đồ              nạp bộ tài liệu cũ — lập bản đồ phủ, chưa ghi gì
/import-legacy lấp 05-01           lấp một tài liệu từ hồ sơ cũ
/import-legacy trạng thái          còn bao nhiêu tài liệu chưa lấp
```

`/design-ui` là **file markdown thuần** ở `.claude/commands/design-ui.md`. Công cụ không có slash command
vẫn dùng được y hệt: *"làm theo `.claude/commands/design-ui.md`"*.

## Ngôn ngữ

Tài liệu viết bằng tiếng Việt. Giữ nguyên tiếng Anh: PRD, MVP, onboarding, paywall, trial, subscription,
retention, conversion, activation, user flow, wireframe, usability, edge case, acceptance criteria,
persona, insight, funnel.

## Ba nguyên tắc không được vi phạm

**Checkpoint.** Mỗi tài liệu là một điểm dừng. **Một tài liệu một lượt.** Viết xong thì dừng, chạy cổng,
hỏi Approve/Modify/Pause. Chỉ file `status: approved` được dùng làm đầu vào.

**Truy nguyên.** Mọi hạng mục truy được về một vấn đề người dùng có bằng chứng, và truy tiếp xuống tới ca
nghiệm thu. Chuỗi: `PN/NC → GAP → CPT → INS → JTBD → PER → FEAT → UC → FR → FLOW → SCR → ST → CPY → EVT → KPI → AC`

**Một nguồn sự thật.** Mỗi thông tin do đúng một tài liệu sở hữu — bảng ở `docs/_DOCUMENTATION_STANDARD.md`.
Tài liệu khác trích ID, không sao chép nội dung. Giá subscription chỉ viết bằng số ở `09-02`.

## Bốn quy tắc thứ tự

1. **Screen inventory trước wireframe.**
2. **UX flow không được sinh màn hình mới** — thiếu màn thì qua `08-04_MISSING_SCREEN_REPORT.md`.
3. **KPI trước event.**
4. **Khả thi công nghệ trước quyết định làm sản phẩm** — `03-05` + `TECH-00` đứng trước cổng G2, không phải sau PRD.

## Ranh giới với Dev

Cần thông tin kỹ thuật mà chưa có: gắn `[ASM]` → tạo `DQ` ở `docs/13-handover/13-02_DEV_QUESTION_LOG.md`
→ đi tiếp với giả định đã gắn nhãn. **Không suy đoán rồi trình bày như đã chốt.**

Khi Dev nộp file vào `tech-input/`: đọc, báo cáo sẽ điền vào đâu, **liệt kê mâu thuẫn**, chờ duyệt.
Không sửa file trong `tech-input/` — tài sản của Dev.

## Ranh giới với nguyên liệu của người dùng

`research-raw/` là **tài sản của người dùng**: nghiên cứu cũ, review thu thập, ảnh chụp, và số liệu họ tra
tay ở công cụ mà AI không truy cập được. Đọc được, **không sửa** — đó là bằng chứng.

`research-raw/ho-so-cu/` là chỗ đặt **bộ tài liệu hoàn chỉnh từ bộ khác** khi nạp một dự án đã chạy.
Không bao giờ dán file cũ vào `docs/`, và **không đánh số lại ID cũ**. Quy trình tám bước ở
`.claude/commands/import-legacy.md`; hai bước không được bỏ là **lập bản đồ phủ trước khi lấp** và
**soi mâu thuẫn trong hồ sơ cũ** — hồ sơ đã qua nhiều bản thường có phần được viết lại và phần không ai cập
nhật theo, nạp mà không phát hiện thì mâu thuẫn được sao chép nguyên vẹn.

`design-system/` cũng vậy: hệ thiết kế người dùng đã dựng sẵn trong Pencil hoặc Figma. Đọc để **dùng lại
đúng tên component**, không sửa. Thêm thành phần vào hệ phải xin phép từng lần và ghi vào mục 5 của
`design-system/_MANIFEST.md`. Hệ sẵn **không** cho phép bỏ `12-00` — nó chỉ đổi việc `12-00` phải làm từ
*chọn phong cách* thành *kiểm hệ có chịu được bộ màn này không*.

Ngoại lệ duy nhất: `research-raw/SENSOR_TOWER_REQUEST.md` là **phiếu do AI điền** để hỏi người dùng cần tra
số gì. File `SENSOR_TOWER_DATA.md` do người dùng điền, AI không sửa.

Số từ công cụ bên thứ ba (Sensor Tower, AppStoreSpy, Data.ai) là **ước lượng**: ghi nguồn dạng
*"ước lượng theo <công cụ>, ngày <ngày>"*. Người dùng để trống một chỉ số thì gắn `[ASM]` hoặc ghi
**Không công bố** — **không tự điền số thay họ.**

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

## Gọi tên tường minh — quy tắc bắt buộc khi nói với người dùng

Người dùng **không nhớ được 61 mã tài liệu, 12 mã cổng và hơn 40 tiền tố ID.** Mã trần không giúp họ
kiểm soát thông tin, nó chỉ làm họ phải tra ngược.

**Giữ nguyên mọi mã, nhưng luôn viết kèm nghĩa** ở lần đầu mã đó xuất hiện trong mỗi lượt trả lời.
Trong **file tài liệu** thì mã viết trần như cũ, nhưng tài liệu phải mang theo bảng nghĩa ở cuối —
xem mục *Viết cho nhiều vai trò cùng đọc* ngay bên dưới.

| Loại | Viết thế này | Không viết |
| --- | --- | --- |
| Tài liệu | `06-02` (Yêu cầu chức năng) | chờ ở `06-02` |
| Cổng | cổng `G5` (Yêu cầu đã phân rã — chạy sau phase 06) | Cổng G5: FAIL |
| ID có nội dung | `DEC-006` (quyết định: đặt paywall sau bước 3 onboarding) | theo `DEC-006` |
| ID tham chiếu | `FR-014` (yêu cầu: tự động lưu nháp sau 5 giây) | xem `FR-014` |
| Tiền tố | `CAP` (năng lực kỹ thuật cốt lõi) | mỗi `CAP` cần một `DQ` |

Với `DEC`, `ASM`, `DQ`, `CHG`, `OPQ` — những mã trỏ tới **một nội dung cụ thể** — phải nhắc lại **nội dung
đó bằng một câu ngắn**, không chỉ dịch tên loại. Người dùng cần biết *"quyết định gì"*, không phải
*"đây là một quyết định"*.

Bảng tra đầy đủ ở `docs/_GLOSSARY.md` mục *Tra nhanh mã*. Nhưng đừng bắt người dùng mở bảng đó —
tra hộ họ là việc của bạn.

## Viết cho nhiều vai trò cùng đọc

Một dự án có **Product Owner, Designer và Dev đọc chung một bộ tài liệu.** Người viết nào cũng viết bằng
tiếng của nghề mình và mặc định ai cũng hiểu. Designer đọc yêu cầu phi chức năng thấy *p95* thì lướt qua;
Dev đọc `04-04` thấy *JTBD* thì lướt qua — rồi **cả hai vẫn duyệt**. Chỗ hỏng không nằm ở đoạn khó hiểu, nó
nằm ở chỗ hai bên đều tưởng mình hiểu và không ai hỏi lại. Sáu tuần sau mới lộ ra là hiểu hai kiểu.

**Không hạ chuẩn chuyên môn để dễ hiểu.** Thuật ngữ giữ nguyên — người trong nghề cần đúng từ đó để tra cứu
và để nói chuyện với bên ngoài. **Diễn giải là thêm vào, không phải thay thế.** Đừng tự chế từ tiếng Việt
để thay một thuật ngữ đã có tên chuẩn.

Ba cơ chế, áp cho **mọi tài liệu**:

**1. Mục `0. Đọc nhanh` ở đầu.** Bốn dòng, viết **không một thuật ngữ nào**: tài liệu này là gì · ai cần
đọc · đọc xong phải biết gì · quyết định nào chốt ở đây. Người ở vai trò khác đọc bốn dòng là biết có cần
đọc tiếp không. Chép lại tên tài liệu vào ô thứ nhất là chưa làm.

**2. Mục `Thuật ngữ dùng trong tài liệu này` ở cuối.** Liệt kê mọi thuật ngữ và mọi tiền tố mã tài liệu có
dùng, kèm **nghĩa một câu** chép từ `docs/_GLOSSARY.md` và `docs/_ID_REGISTRY.md`. Chỉ liệt kê thứ thật sự
xuất hiện.

**3. Câu đầu của mỗi mục lớn nói bằng tiếng phổ thông** rồi mới đi vào chi tiết chuyên môn. Ví dụ, mở đầu
mục yêu cầu phi chức năng: *"Mục này nói app phải chạy nhanh và ổn tới mức nào."* — rồi mới tới bảng có
`p95`, `cold start`, `crash rate`.

Ba luật khi viết nghĩa một câu:

| Luật | Vì sao |
| --- | --- |
| Không dùng thuật ngữ khác để giải thích một thuật ngữ | giải thích *activation* bằng *conversion* là không giải thích gì |
| Một câu | dài hơn là đang viết bài giảng, không phải diễn giải |
| Nói bằng việc người dùng làm, không bằng khái niệm | *"người dùng đã làm xong việc chứng tỏ họ nhận được giá trị lần đầu"* thắng *"cột mốc kích hoạt trong vòng đời"* |

`validate_docs.py` đối chiếu máy: thuật ngữ hoặc tiền tố mã **dùng trong bài mà không có trong bảng** →
**LỖI** (tài liệu `approved`) hoặc cảnh báo (`draft`). Thuật ngữ lọt vào mục `0. Đọc nhanh` cũng bị bắt —
đó là chỗ duy nhất tuyệt đối không được có thuật ngữ, vì người đọc chưa đi tới bảng nghĩa.

Thiếu từ nào thì **thêm dòng vào `docs/_GLOSSARY.md`**, đừng bỏ qua. Từ điển đó thuộc về dự án.

## Nhãn nội dung

`[FACT]` có nguồn · `[INSIGHT]` từ ≥2 nguồn · `[HYP]` có điều kiện bác bỏ · `[ASM]` có dòng ở
`_ASSUMPTION_REGISTER` · `[REC]` kèm lý do · `[DEC]` có DEC ID.

Số liệu nội bộ đối thủ không có nguồn công khai: ghi **Không công bố**. Không bịa số liệu thị trường,
kết quả phỏng vấn, kết quả usability test.

## Quy tắc phản biện

Phải cảnh báo, không im lặng làm theo, khi thấy: tính năng không gắn pain point · onboarding dài trước khi
thấy giá trị · paywall trước khi chứng minh giá trị · flow quá nhiều bước · metric không phản ánh giá trị thật ·
persona chỉ dựa trên nhân khẩu học · gamification không liên quan hành vi cốt lõi · copy tạo claim sai ·
A/B test không có giả thuyết · câu hỏi nghiên cứu dẫn dắt · scope MVP phình.

Khi phản biện: nêu vấn đề → giải thích rủi ro → đưa phương án thay thế → đề xuất cách kiểm chứng.

## Trước khi kết thúc buổi làm

Đang bàn dở gì chưa ghi ra file thì ghi vào `docs/_OPEN_QUESTIONS.md` và `docs/_ASSUMPTION_REGISTER.md`.
**Đừng để quyết định chỉ tồn tại trong hội thoại.**
