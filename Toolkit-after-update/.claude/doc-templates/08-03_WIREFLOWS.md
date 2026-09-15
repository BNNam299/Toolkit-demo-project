---
doc_id: 08-03
title: Wireflows
phase: 08-screens
skill: screen-inventory-wireframe
profile: Bắt buộc
owner: Designer
reviewers: []
version: 0.1.0
status: draft
last_updated:
approved_by: ""
approved_at: ""
depends_on: [07-05, 08-01, 08-02]
feeds: [12-00, 12-01]
id_prefix: []
gate: G7
in_handover: true
confidence: low
---

# [Tên dự án] — Wireflows

> **Đầu ra của phase này là wireflow trong `wireframes/`, không phải bản vẽ trong file này.**
> Wireflow = một trang cho một luồng, các màn xếp cạnh nhau, nối bằng **mũi tên có nhãn "bấm gì"**, nhánh có
> nhãn **"điều kiện nào"**. Tài liệu này giữ phần **đếm, kiểm và quyết định**.
>
> Xem thử: `python -m http.server 8000` → `http://localhost:8000/wireframes/`
> Hướng dẫn: `wireframes/README.md` · CSS dùng chung: `wireframes/_wireframe.css`

## 0. Đọc nhanh

| Câu hỏi | Trả lời ngắn |
| --- | --- |
| **Tài liệu này là gì** | |
| **Ai cần đọc** | |
| **Đọc xong phải biết gì** | |
| **Quyết định nào chốt ở đây** | |

> Bốn dòng này viết **không dùng một thuật ngữ nào**, kể cả thuật ngữ của chính nghề mình. Người mới vào dự
> án — hoặc người ở vai trò khác — đọc bốn dòng là biết có cần đọc tiếp hay không. Để trống hoặc chép lại
> tên tài liệu là chưa làm.


## 1. Quy ước

| Trường | Nội dung |
| --- | --- |
| Đầu ra chính | **wireflow** — `wireframes/flow-FLOW-xxx.html`, một file cho một luồng |
| Đơn vị màn | một file cho **một ô** trong `08-02`, nhúng vào trang flow bằng `iframe` |
| Quy ước tên file màn | `SCR-012_ST-041_ket-qua-phan-tich.html` — **mã ba chữ số**, khớp `08-02` |
| Trong khung máy | **chỉ chữ người dùng sẽ đọc thật** — xem luật một câu bên dưới |
| Mức độ | lo-fi về thị giác, **thật về nội dung và bố cục** — màu và cỡ chữ là việc của phase 12 |
| Bản mẫu để bắt chước | `wireframes/_VD_*.html` — bảy màn và một trang flow đã dựng đúng chuẩn |
| Nút | **không bấm được**, không `href`, không JavaScript |
| Trang chủ | `wireframes/index.html` — danh sách luồng, khớp `07-05` |

### Luật một câu

**Trong khung máy chỉ có thứ người dùng sẽ đọc và chạm trên app thật.**

| Đúng | Sai |
| --- | --- |
| `Chọn cách giới hạn các app này` | `Tiêu đề màn, 22pt, tương phản cao nhất` |
| `Tiếp tục` | `Hành động chính của màn` |
| `Số lần mở mỗi ngày — 6 lần` | `Row 50pt, vùng tương tác lớn nhất` |
| `Chưa có nhóm chặn nào` | `Empty state, có CTA thoát` |

Cột phải là **kể về màn hình**; cột trái **là màn hình**. Bản kể thì đọc từng file vẫn thấy hợp lý, nhưng
mở cả trang wireflow ra thì không ai đọc được nó như một app nữa — và người đọc tài liệu mất đúng thứ họ cần
ở phase này: nhìn ra app sẽ như thế nào, đọc được chữ thật trên đó.

Mã truy nguyên (`FR`, `UC`, `CPY`, `SCR`, `ST`), điều kiện, câu JTBD ngôi thứ nhất: **để ở khối `.w-notes`
ngoài khung**, hoặc ở `figcaption` trên trang flow. Trong khung là không.

`check_build.py --wireframes` soi máy phần này: ghi chú lọt vào khung, số đo trong khung, mã trong khung,
và các cụm từ mô tả thiết kế đều ra **LỖI**, không phải cảnh báo.

### Bốn câu wireflow phải trả lời — và chỉ bốn câu này

1. Màn này phục vụ **chức năng** gì · 2. **vào từ** màn nào · 3. **bấm gì** ra màn nào ·
4. **tình huống nào** ra trạng thái nào.

**Không thuộc phase này:** khoảng cách, cỡ chữ, độ cao, bo góc, màu, thứ bậc thị giác. Chốt ở `12-00`
(Nghiên cứu UI) sau khi đọc moodboard. Chú thích số pt ở đây là ép quyết một thứ chưa tới lúc quyết, và làm
cả nhóm chuyển sang tranh luận thị giác trong khi hành vi còn chưa xong.

Riêng **hai** thông tin sau vẫn giữ, vì là hành vi chứ không phải thị giác: **thứ tự nội dung** trên màn, và
**cái gì thấy được ngay không cần cuộn**. Khung máy cao đúng một màn hình nên mở trên trình duyệt là biết.

## 2. Danh sách luồng

Một dòng cho mỗi `FLOW` trong `07-05`. Đây là bảng điều khiển của phase 08.

| `FLOW` | Tên luồng | Trang flow | Số bước đường chính | Số nhánh | Số màn | Trạng thái |
| --- | --- | --- | --- | --- | --- | --- |
| `FLOW-001` | | `flow-FLOW-001.html` | | | | chưa dựng / đã dựng / đã duyệt |

| Kiểm | Kết quả |
| --- | --- |
| Mọi `FLOW` trong `07-05` có một trang flow | |
| Số bước tới giá trị đầu tiên của luồng cốt lõi | và **có bước nào bỏ được** mà vẫn xong việc không |
| Mọi mũi tên có nhãn — *bấm gì* hoặc *tự chuyển* | mũi tên trống là chưa nghĩ xong |
| Mọi nhánh có nhãn **điều kiện** | |
| Mọi màn có **đường ra** | ngõ cụt là lỗi chặn cổng |

**Cột "số bước" là cột đáng nhìn nhất trong tài liệu này.** Wireflow tồn tại để bạn đếm được số bước và thấy
bước dư — chứ không phải để có tài liệu.

## 3. Danh sách màn

Một dòng cho **mỗi ô có mã `ST`** trong `08-02`.

| `SCR` | Tên màn | `ST` | Trạng thái | Điều kiện vào trạng thái | File | Xuất hiện ở flow nào |
| --- | --- | --- | --- | --- | --- | --- |
| `SCR-001` | | `ST-001` | | | `SCR-001_ST-001_....html` | `FLOW-001` |

**Tổng số màn phải có:** ___ (bằng số ô có mã `ST` trong `08-02`) · **Đã có:** ___

Cột **điều kiện vào trạng thái** là cột hay bị để trống nhất và cũng là cột Dev cần nhất. *"Trạng thái lỗi"*
không nói gì; *"khi độ tin cậy dưới 40%"* thì dựng được và test được.

Cột cuối trả lời câu *"màn này nằm ở đâu trong sản phẩm"*. Để trống nghĩa là màn mồ côi hoặc trang flow thiếu
một nhánh — cả hai đều phải xử trước khi đóng cổng.

## 4. Ghi chú hành vi nằm ở đâu

Chức năng của màn, vào từ đâu, bấm gì ra đâu, nút vô hiệu khi nào, đường thoát — **nằm trong khối `.w-notes`
của chính file màn**, không chép vào đây. Người dựng ở phase 12 mở file HTML, không mở tài liệu này.

Tài liệu này chỉ ghi những gì **áp cho nhiều màn**:

| Quyết định áp cho nhiều màn | Nội dung | Vì sao |
| --- | --- | --- |
| Vị trí hành động chính | ví dụ: luôn ở vùng cố định đáy, không nằm trong vùng cuộn | |
| Kiểu điều hướng | tab bar / stack / sheet | trích `PAT` ở `07-00` nếu có |
| Cách hiện lỗi | inline dưới ô nhập / toast / màn riêng — **chọn một, dùng nhất quán** | |
| Đường thoát mặc định | ví dụ: mọi sheet đóng được bằng vuốt xuống | |
| Xử lý chữ tràn | xuống dòng, không cắt bằng "…" | |

| Kiểm | Kết quả |
| --- | --- |
| Mọi file màn có khối `.w-notes`, **không mục nào để trống** | |
| Mọi khối `.w-notes` ghi rõ **đường thoát** | trạng thái không lối ra là chỗ người dùng bỏ app |
| Mọi hành động chính có ghi **điều kiện bị vô hiệu** | |
| Không file nào chú thích khoảng cách, cỡ chữ, màu | đó là phase 12 |

## 5. Phủ trạng thái

Chạy script, **dán nguyên kết quả vào đây**, không tóm tắt:

```
python .claude/scripts/check_build.py --wireframes wireframes/
```

```
<dán kết quả>
```

| `SCR` | Số `ST` trong `08-02` | Số màn đã dựng | Đã vào flow | Đủ chưa |
| --- | --- | --- | --- | --- |

Thiếu thì nói rõ thiếu ô nào. **Trạng thái hay bị bỏ nhất là đang tải, rỗng và lỗi** — màn có dữ liệu thì bao
giờ cũng được làm trước và làm đủ.

## 6. Kiểm

| Kiểm | Kết quả |
| --- | --- |
| **Không Lorem Ipsum** — chữ thật, hoặc câu thật mình định dùng | |
| Mọi `SCR` và `ST` trong `08-02` có file màn | |
| Tên file đúng quy ước, mã **ba chữ số** | |
| Mọi `FLOW` trong `07-05` có một trang flow, thứ tự khớp | |
| Mọi màn được **ít nhất một** trang flow nhúng | |
| `index.html` liệt kê mọi luồng và mọi màn | |
| Không màu thương hiệu, không font khác, không ảnh thật | |
| Không chú thích số đo trong file wireframe | |
| Chỉ thể hiện tương tác **triển khai được** | |
| Vùng chạm ≥44pt, đạt sàn tiếp cận theo `06-03` mục 4 | |
| Đã mở bằng trình duyệt, **đi hết một luồng bằng mắt** từ đầu tới cuối | |
| `check_build.py --wireframes` báo **0 lỗi** | điều kiện G7 |

## 7. Nguồn phương pháp

| Nguồn | Áp dụng ở mục nào |
| --- | --- |
| `references/` của skill này | |
| Skill chiều sâu đã dùng | |
| `wireframes/README.md` | mục 1 |
| `07-05_UX_FLOWS` | mục 2 |

## Thuật ngữ dùng trong tài liệu này

Chép nghĩa một câu từ `docs/_GLOSSARY.md` mục *Thuật ngữ chuyên môn*, và nghĩa của tiền tố mã từ
`docs/_ID_REGISTRY.md`. Chỉ liệt kê thứ **thật sự xuất hiện** trong tài liệu này.

| Thuật ngữ / tiền tố mã | Nghĩa một câu |
| --- | --- |
| | |

> Bảng này không phải để người trong nghề đọc — nó dành cho người ở vai trò khác đang phải duyệt tài liệu
> này. `validate_docs.py` đối chiếu: dùng mà không liệt kê là **LỖI**; liệt kê mà không dùng là cảnh báo.

<!-- QUALITY-GATE-MANIFEST:START
# Nguồn chân lý DUY NHẤT cho G7 phần tài liệu này. KHÔNG chép khối này vào file đầu ra ở docs/.
doc: 08-03_WIREFLOWS
gate: G7
required_major:
  - "0. Đọc nhanh"
  - "1. Quy ước"
  - "2. Danh sách luồng"
  - "3. Danh sách màn"
  - "4. Ghi chú hành vi nằm ở đâu"
  - "5. Phủ trạng thái"
  - "6. Kiểm"
  - "7. Nguồn phương pháp"
  - "Thuật ngữ dùng trong tài liệu này"
required_minor:
  "1. Quy ước":
    - "Luật một câu"
    - "Bốn câu wireflow phải trả lời — và chỉ bốn câu này"
quality_checks:
  - "Đầu ra là wireflow HTML trong wireframes/, KHÔNG vẽ luồng hay bố cục bằng ký tự trong tài liệu này"
  - "Mỗi FLOW trong 07-05 có đúng một trang flow-FLOW-xxx.html, thứ tự bước khớp 07-05"
  - "Mọi mũi tên trên trang flow có nhãn: bấm gì, hoặc tự chuyển — không mũi tên nào trống"
  - "Mọi nhánh trên trang flow có nhãn điều kiện"
  - "Một file màn cho MỘT ô trong 08-02 — không gộp trạng thái, không dùng JS bật tắt trạng thái"
  - "Trang flow NHÚNG file màn bằng iframe, không chép lại nội dung màn"
  - "Tên file màn đúng quy ước SCR-xxx_ST-xxx_ten.html, mã ba chữ số khớp 08-02"
  - "Mọi màn được ít nhất một trang flow nhúng; màn không vào flow nào đã được xử lý hoặc giải thích"
  - "Cột điều kiện vào trạng thái ở mục 3 không để trống"
  - "TRONG khung máy chỉ có chữ người dùng sẽ đọc thật — không mô tả khối, không lý do thiết kế, không câu JTBD ngôi thứ nhất"
  - "Trong khung máy KHÔNG có số đo (pt, px), KHÔNG có mã FR/UC/NFR/CPY/SCR/ST — mã chỉ ở .w-tag và .w-notes"
  - "Mọi khung máy giữ đúng 390x844, không nới chiều cao cho vừa nội dung — nội dung dài thì phải cuộn mới thấy"
  - "Dựng bằng phận tử có sẵn trong _wireframe.css; thiếu thì THÊM class, không mô tả bằng chữ trong khung"
  - "Khối .w-notes nằm NGOÀI .w-phone, và chỉ ba mục: màn để làm gì · vào từ đâu ra đi đâu · trạng thái khác"
  - "KHÔNG chú thích khoảng cách, cỡ chữ, độ cao, bo góc, màu ở bất kỳ đâu trong wireframe — đó là phase 12"
  - "Nút không có href và không có JavaScript — điều hướng thể hiện bằng mũi tên trên trang flow"
  - "Mọi màn có đường ra; không ngõ cụt"
  - "Không Lorem Ipsum — điều kiện G7"
  - "Mục 2 ghi số bước đường chính và đã trả lời có bước nào bỏ được hay không"
  - "Mục 5 dán NGUYÊN kết quả check_build.py --wireframes, không tóm tắt"
  - "check_build.py --wireframes báo 0 lỗi — điều kiện G7"
  - "Đạt sàn tiếp cận theo 06-03: vùng chạm ≥44pt"
QUALITY-GATE-MANIFEST:END -->
