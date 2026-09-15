---
name: screen-inventory-wireframe
description: "Kiểm kê đầy đủ màn hình và trạng thái TRƯỚC khi vẽ, lập state matrix không còn ô trống, rồi dựng wireframe lo-fi/mid-fi bằng nội dung thật. Phase 08 của Pipeline v2, cổng G7. Phụ trách 4 tài liệu trong `docs/08-screens/`. Chỉ dùng khi làm đúng phase này; mỗi lượt chỉ viết MỘT tài liệu rồi dừng chờ duyệt."
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - Bash
  - WebSearch
  - WebFetch
---

# Kiểm kê màn hình & wireframe — phase 08

## Tài liệu phụ trách

| doc_id | File | Mức bắt buộc | Owner | Trong gói bàn giao |
| --- | --- | --- | --- | --- |
| `08-01` | `08-01_SCREEN_INVENTORY.md` | Bắt buộc | Designer | Có |
| `08-02` | `08-02_STATE_MATRIX.md` | Bắt buộc | Designer | Có |
| `08-03` | `08-03_WIREFLOWS.md` | Bắt buộc | Designer | Có |
| `08-04` | `08-04_MISSING_SCREEN_REPORT.md` | Bắt buộc khi làm flow | Designer | — |

Thư mục đích: `docs/08-screens/`. Prefix ID skill này được cấp: `SCR`, `ST`.
Cổng đóng sau phase: **G7** — checklist ở `docs/_GATE_CHECKLIST.md`.

## Đầu ra của phase này là WIREFLOW

`08-03` **không vẽ luồng hay bố cục trong markdown**. Đầu ra là **wireflow** trong `wireframes/`: một trang
cho một luồng, các màn xếp cạnh nhau, nối bằng **mũi tên có nhãn "bấm gì"**, nhánh có nhãn **"điều kiện nào"**.

Đọc `wireframes/README.md` trước khi làm `08-03`.

### Bốn câu wireflow phải trả lời — và chỉ bốn câu này

1. Màn này phục vụ **chức năng** gì · 2. **vào từ** màn nào · 3. **bấm gì** ra màn nào ·
4. **tình huống nào** ra trạng thái nào.

**KHÔNG thuộc phase này:** khoảng cách, cỡ chữ, độ cao, bo góc, màu. (Bố cục và thứ tự nội dung
thì CÓ thuộc phase này — đó là thứ người đọc tài liệu cần nhìn ra.) Chốt ở `12-00`
(Nghiên cứu UI) sau khi đọc moodboard. Chú thích số pt ở đây là ép người dùng quyết một thứ chưa tới lúc
quyết, và làm cả nhóm chuyển sang tranh luận thị giác trong khi hành vi còn chưa xong.

Giữ đúng **hai** thông tin có tính hành vi: thứ tự nội dung trên màn, và cái gì thấy được ngay không cần cuộn.

### Hai loại file

| File | Là gì | Template |
| --- | --- | --- |
| `flow-FLOW-001.html` | **đầu ra chính** — một luồng, có mũi tên và nhãn | `_TEMPLATE_FLOW.html` |
| `SCR-012_ST-041_ten.html` | một **ô** của `08-02`, nhúng vào trang flow bằng `iframe` | `_TEMPLATE.html` |

Mã **ba chữ số**, khớp `08-02`. Trang flow **nhúng** file màn, không chép nội dung — sửa màn thì flow tự
cập nhật. **Nút không bấm được**: không `href`, không JavaScript; điều hướng nằm ở mũi tên.

### Ba mục của một trang flow

**Đường chính** (happy path) → **Nhánh theo điều kiện** (mỗi nhánh một nhãn: *nếu mã sai 3 lần*, *nếu mất
mạng*) → **Trạng thái còn lại** (ô nào của `08-02` chưa xuất hiện ở hai mục trên thì đặt ở đây kèm điều kiện
vào trạng thái).

Mục thứ ba là mục cứu bạn: đường chính thì ai cũng làm, còn đang tải, rỗng, mất mạng, hết quyền luôn bị bỏ.

### Luật một câu — chỗ sai nhiều nhất của cả phase

**Trong khung máy chỉ có thứ người dùng sẽ đọc và chạm trên app thật.**

| Viết thế này | Không viết thế này |
| --- | --- |
| `Chọn cách giới hạn các app này` | `Tiêu đề màn, 22pt, tương phản cao nhất` |
| `Tiếp tục` | `Hành động chính của màn` |
| `Số lần mở mỗi ngày — 6 lần` | `Row 50pt, vùng tương tác lớn nhất` |
| `Chưa có nhóm chặn nào` | `Empty state, có CTA thoát` |

Cột phải **kể về** màn hình; cột trái **là** màn hình. Bản kể đọc từng file vẫn thấy hợp lý, nhưng mở cả trang
wireflow ra thì không ai đọc được nó như một app — mà đó đúng là thứ người đọc tài liệu cần ở phase này.

**Có bản mẫu, hãy mở ra xem trước khi dựng file đầu tiên:** `wireframes/_VD_*.html` — bảy màn và một trang
flow dựng đúng chuẩn. Bắt chước bản đó, đừng tự nghĩ cấu trúc mới.

**Dựng bằng phận tử có sẵn** trong `_wireframe.css`: `.w-seg` segmented · `.w-rowval` hàng có giá trị ·
`.w-group` nhóm hàng · `.w-check` `.w-radio` `.w-switch` · `.w-field` `.w-search` · `.w-kb` bàn phím ·
`.w-sheet` + `.w-grab` · `.w-tabbar` · `.w-chip` · `.w-steps` · `.w-empty` · `.w-toast` · `.w-ph` giữ chỗ.
Cần thứ chưa có thì **thêm class vào cuối `_wireframe.css`** — mô tả bằng chữ trong khung là sai.

**Khung giữ đúng 390×844.** Nội dung dài hơn thì phải cuộn mới thấy, và đó là thông tin thật: mở trình duyệt
lên là biết CTA chính có nằm trong tầm nhìn đầu tiên hay không. Đừng nới chiều cao khung cho vừa nội dung.

### Khối `.w-notes` — NGOÀI khung, và chỉ ba mục

**Màn này để làm gì** (kèm mã `FLOW` / `UC` / `FR`) · **vào từ đâu, ra đi đâu** (kèm nút nào bị vô hiệu khi
nào, và đường thoát) · **các trạng thái khác của màn này** kèm điều kiện.

Ba mục, không hơn. Mã truy nguyên và câu JTBD ngôi thứ nhất nằm ở đây — **không** nằm trong khung. Không một
con số pt nào, ở cả hai chỗ.

Cập nhật `wireframes/index.html` (danh sách luồng + thư viện màn) mỗi khi thêm file. Xong thì chạy và
**dán nguyên kết quả** vào `08-03` mục 5:

```
python .claude/scripts/check_build.py --wireframes wireframes/
```

Script kiểm hai tầng. **Tầng luồng:** có trang wireflow chưa · màn nào **chưa nằm trong luồng nào** · mũi
tên nào **trống nhãn** · màn nào thiếu so với `08-02` · tên nào sai mã. **Tầng từng màn:** ghi chú lọt vào
trong khung · số đo (pt, px) trong khung · mã `FR`/`UC`/`SCR`/`ST` trong khung · các cụm từ mô tả thiết kế
thay cho nội dung thật. Cả hai tầng ra **LỖI**, không phải cảnh báo — nghĩa là cổng `G7` không đóng.

**Vì sao vẫn xám dù là HTML.** Wireflow HTML dễ thành hi-fi sớm, và khi đó cả nhóm tranh luận màu nút thay vì
tranh luận *"màn này có cần bước xác nhận không"*. Phase 08 chốt **hành vi, bố cục và nội dung**; **màu, cỡ
chữ, khoảng cách** chốt ở `12-00`. Hai chuyện khác nhau: xám là ràng buộc về **màu**, không phải lý do để
màn hình thành hộp xám có chú thích.

## Step 0 — Nạp chiều sâu

Liệt kê `.claude/skills/_depth/08-screens/`. Với mỗi thư mục con, đọc **description trong frontmatter trước**.
Chỉ mở toàn bộ nội dung của skill nào thật sự liên quan tới dự án đang làm — nạp hết mọi thứ làm loãng trọng tâm.

Khi skill chiều sâu mâu thuẫn với phương pháp gốc ở `references/`, **skill chiều sâu thắng**, nhưng phải ghi
vào mục "Nguồn phương pháp" cuối tài liệu là đã áp dụng skill nào và ở chỗ nào. Không được đổi đầu ra trong im lặng.

## Step 1 — Kiểm đầu vào

Đọc `docs/_INDEX.md`. Kiểm mọi file trong `depends_on` của tài liệu sắp viết có `status: approved` chưa.
**Chỉ file `approved` được dùng làm đầu vào.** Thiếu thì dừng và báo, không tự đi tiếp bằng file `draft`.

Nếu `tech-input/` có file liên quan mà Dev đã nộp, đọc và dùng. Thiếu thông tin kỹ thuật thì gắn `[ASM]`
vào chỗ đang thiếu và tạo `DQ` ở `docs/13-handover/13-02_DEV_QUESTION_LOG.md`. **Không suy đoán.**

## Step 2 — Đọc phương pháp

Đọc `references/method*.md` trước, rồi mọi file `.md` còn lại trong `references/`.
Danh sách file **không** được liệt kê cứng ở đây — thêm một mảng kiến thức mới chỉ là thả thêm file vào thư mục đó.

## Step 3 — Viết MỘT tài liệu

Đọc template tương ứng ở `.claude/doc-templates/`. Khối `QUALITY-GATE-MANIFEST` ở cuối template là nguồn chân lý
về các mục bắt buộc — tái tạo đủ các mục đó, **KHÔNG chép khối manifest vào file đầu ra**.

Front-matter bắt buộc: `doc_id`, `phase`, `skill`, `profile`, `owner`, `version`, `status`, `depends_on`,
`feeds`, `id_prefix`, `gate`, `in_handover`, `confidence`.

Gắn nhãn mọi mệnh đề quan trọng: `[FACT]` có nguồn · `[INSIGHT]` từ ≥2 nguồn · `[HYP]` có điều kiện bác bỏ ·
`[ASM]` có dòng ở `_ASSUMPTION_REGISTER` · `[REC]` kèm lý do · `[DEC]` có DEC ID.

## Step 4 — Cổng

Chạy **hai** phép kiểm, đừng lẫn hai cái:

**4a. Kiểm tài liệu vừa viết.** Gọi `project-docs-quality-gates` chỉ với tài liệu này: đối chiếu
`required_major`, `required_minor`, `quality_checks` trong manifest của template tương ứng.
Đây là phép kiểm bắt buộc phải PASS trước khi hỏi Approve.

**4b. Báo trạng thái cổng của phase.** Một cổng phủ **nhiều tài liệu**, có cổng phủ cả hai phase.
Sau khi viết một tài liệu, cổng gần như luôn **chưa đủ điều kiện xét** vì các tài liệu khác chưa tồn tại.

Lúc đó báo `CHƯA ĐỦ ĐIỀU KIỆN XÉT`, kèm danh sách tài liệu `Bắt buộc` còn thiếu — **không báo FAIL**.
`FAIL` chỉ dùng khi mọi tài liệu bắt buộc của cổng đã có mà checklist vẫn không tick hết.

```
Tài liệu 01-01 — Thị trường và vùng nhu cầu: gate-check PASS
Cổng G1 — Cơ hội có bằng chứng (chạy sau phase 01–02): CHƯA ĐỦ ĐIỀU KIỆN XÉT
  còn thiếu: 01-02 Sổ đào pain point · 02-01 Bản đồ đối thủ · 02-02 Mổ xẻ đối thủ ·
             02-03 Đào review người dùng · 02-04 Khoảng trống cơ hội
```

**Mã trần là không đủ.** Mỗi `doc_id`, mã cổng và ID cấp mới khi **nói với người dùng** phải kèm nghĩa
hoặc kèm nội dung một dòng — người dùng không nhớ 61 mã tài liệu và hơn 40 tiền tố. Quy tắc đầy đủ ở
`CLAUDE.md` mục *Gọi tên tường minh*; bảng tra ở `docs/_GLOSSARY.md` mục *Tra nhanh mã*.
Trong file tài liệu vẫn giữ mã trần như cũ.

Chỉ khi tài liệu cuối cùng của cổng được approve thì mới chạy đủ checklist ở `docs/_GATE_CHECKLIST.md`
và kết luận cổng đóng hay không.

## Step 5 — Dừng

Cập nhật `docs/_INDEX.md`: trạng thái tài liệu, ID mới cấp, mồ côi phát hiện được, mâu thuẫn với tài liệu khác.
Báo cáo cho người dùng và **dừng lại**. Không tự sang tài liệu tiếp theo.

## Ranh giới

**Sở hữu:** Mã màn hình SCR, trạng thái ST, wireframe

**Không sở hữu:** Thiết kế hi-fi — **người làm tay trong Figma**, xem phase 12

## Quy tắc không được vi phạm

- **Một tài liệu một lượt.** Không tạo hai tài liệu trong cùng một lượt làm việc.
- **Không sửa file `approved`.** Cần đổi thì qua quy trình `CHG` ở `docs/_CHANGE_LOG.md`.
- **ID không đổi, không tái sử dụng, không đánh số lại.**
- **Mã kèm nghĩa khi nói với người dùng.** `06-02` → `06-02` (Yêu cầu chức năng). `DEC-006` → kèm một câu nói rõ đã quyết gì.

**Không bịa.** Không có nguồn thì ghi **Không công bố**. Không bịa số liệu thị trường, kết quả phỏng vấn,
  kết quả usability test hay chỉ số đối thủ.
- **Không khai báo công nghệ.** Kiến trúc, API, schema thuộc Dev, nộp qua `tech-input/`.
- **Phản biện, không gật.** Thấy tính năng không gắn pain point, paywall trước khi chứng minh giá trị,
  metric không phản ánh giá trị thật, hay scope MVP phình thì phải nêu: vấn đề → rủi ro → phương án thay thế → cách kiểm chứng.
