---
doc_id: 12-00
title: UI Research
phase: 12-prototype
skill: figma-prototype-spec
profile: Bắt buộc
owner: Designer
reviewers: []
version: 0.1.0
status: draft
last_updated:
approved_by: ""
approved_at: ""
depends_on: [07-00, 07-05, 08-01, 08-03, 09-06]
feeds: [12-01, 12-02]
id_prefix: [UIP]
gate: G10
in_handover: true
confidence: medium
---

# [Tên dự án] — UI Research

> **Tài liệu đầu tiên của phase 12, viết TRƯỚC `12-01` (Spec để dựng prototype).**
> Chốt phong cách thị giác trước khi ai mở Figma. Không chốt ở đây thì phong cách sẽ được chốt ngầm
> ở màn hình thứ ba, và mười màn sau sẽ phải dựng lại.
>
> Nguyên liệu: `research-raw/moodboard/` (ảnh tham chiếu UI, mục lục ở `_MANIFEST.md`) và
> `research-raw/man-hinh-doi-thu/` (ảnh màn hình đối thủ — quét lần hai, xem mục 4).

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


## 0. Đọc trước khi mở ảnh — chống chọn phong cách theo cảm tính

**Đọc bốn thứ này TRƯỚC khi xem ảnh moodboard đầu tiên:** `08-01` (Kiểm kê màn hình), `08-03` (Wireframe),
`07-05` (Luồng trải nghiệm), `09-06` (Bộ văn bản giao diện).

Lý do: phong cách thị giác không phải chuyện thẩm mỹ độc lập. Nó phải chịu được **đúng bộ màn hình mình
có**, **đúng độ dài chữ mình đã viết**, và **đúng bối cảnh người dùng của mình**. Một phong cách đẹp trên
Dribbble với ba dòng chữ sẽ vỡ khi gặp một nhãn mười bốn từ ở `09-06`.

| Trường | Nội dung | Nguồn |
| --- | --- | --- |
| Số màn hình phải dựng | | `08-01` |
| Loại nội dung nặng nhất | danh sách dài · biểu đồ · ảnh · form nhiều trường | `08-03` |
| Chuỗi văn bản dài nhất trong bộ | ghi cả mã `CPY` và số ký tự | `09-06` |
| Bối cảnh dùng chi phối thị giác | một tay · ngoài trời nắng · buổi tối trên giường · trong quán thiếu sáng | `04-06` |
| Cảm giác người dùng cần có sau khi xong việc | nhẹ đầu · được kiểm soát · được khen · yên tâm | `04-04` `04-06` |
| Ràng buộc thương hiệu đã có | logo · màu đã dùng ở landing page · tên · Không có | |

**Dòng "cảm giác người dùng cần có" là dòng chi phối cả tài liệu.** Một app ghi chép chi tiêu cần cảm giác
*được kiểm soát* — phong cách rực rỡ, nhiều chuyển động sẽ đánh nhau với chính giá trị đó, dù ảnh tham
chiếu có đẹp thế nào.

## 1. Phạm vi moodboard đã thu

| Trường | Nội dung |
| --- | --- |
| Số ảnh trong `research-raw/moodboard/` | |
| Số nguồn | |
| Công cụ đã thu | Claude · Codex · OpenCode + KimiBridge |
| Ngày thu | |
| Đã nghiệm thu theo bảng mục 5 của `_MANIFEST.md`? | |

| Chủ đề | Số ảnh | Có đủ để kết luận? |
| --- | --- | --- |
| Màu sắc | | |
| Kiểu chữ | | |
| Thành phần | | |
| Màn hoàn chỉnh | | |
| **Không thích** | | **có ít nhất 3 ảnh — nếu không, mục 3 sẽ thiếu một nửa căn cứ** |

Chủ đề nào chưa đủ thì **nói rõ và hạ độ tự tin của mục liên quan**, không kết luận rồi mới xin lỗi sau.

## 2. Mẫu thị giác quan sát được

| `UIP` | Mẫu thị giác | Ảnh nguồn | Chủ đề | Quyết định | Lý do — neo vào mục 0 | Đổ vào đâu |
| --- | --- | --- | --- | --- | --- | --- |
| `UIP-001` | | `dribbble_mau-sac_...png` | màu · chữ · thành phần · màn | Áp dụng / Điều chỉnh / Không dùng | | `12-01` · `12-02` |

**Cột lý do không được viết "vì đẹp" hoặc "vì đang là trend".** Phải nối được về một dòng trong mục 0:
loại nội dung, độ dài chữ, bối cảnh dùng, hoặc cảm giác cần tạo ra. Không nối được thì chuyển sang
**Không dùng** — kể cả khi thích.

### Đọc từ thư mục `khong-thich/`

| Ảnh | Cụ thể là **chi tiết nào** khiến loại | Suy ra ràng buộc gì cho mình |
| --- | --- | --- |
| | không phải "không thích cả ảnh" — chỉ ra chi tiết | ví dụ: không dùng gradient tím-cam trên nền tối |

Mục này rẻ mà hiệu quả cao: **một ràng buộc phủ định loại được hàng chục phương án** trong khi một mẫu
tích cực chỉ thêm một phương án.

## 3. Ba hướng thiết kế — chọn một

Đưa **ba** hướng khác nhau thật, không phải một hướng ba biến thể. Rồi chọn một và ghi `DEC`.

| Hạng mục | Hướng A | Hướng B | Hướng C |
| --- | --- | --- | --- |
| Tên gọi một câu | | | |
| Ngôn ngữ thiết kế | ví dụ: phẳng, nhiều khoảng trắng · đậm khối, tương phản cao · mềm, bo lớn, đổ bóng nhẹ | | |
| `UIP` làm nền cho hướng này | | | |
| Cảm giác tạo ra | và có khớp dòng "cảm giác cần có" ở mục 0 không | | |
| Chịu được nội dung nặng nhất ở mục 0? | | | |
| Chịu được chuỗi chữ dài nhất ở `09-06`? | | | |
| Công sức dựng | thấp / trung / cao — và **vì sao** | | |
| Rủi ro | ví dụ: bão hoà, khó đọc ngoài nắng, lệ thuộc ảnh chất lượng cao | | |

**Hướng đã chọn:** ___ · `DEC-___`

**Vì sao không chọn hai hướng còn lại:** (ghi lại — sáu tuần sau sẽ có người hỏi, và không có dòng này thì
tranh luận sẽ chạy lại từ đầu)

## 4. Hệ màu và chữ

### Màu

| Vai trò | Giá trị | Nguồn `UIP` | Tương phản với nền | Đạt ≥4.5:1? |
| --- | --- | --- | --- | --- |
| Nền chính | | | — | — |
| Chữ chính trên nền | | | | |
| Chữ phụ trên nền | | | | **chỗ trượt nhiều nhất** |
| Màu hành động chính | | | | |
| Màu chữ trên nút hành động | | | | |
| Thành công | | | | |
| Cảnh báo | | | | |
| Lỗi | | | | |

| Kiểm | Kết quả |
| --- | --- |
| Có dùng màu làm **kênh truyền tin duy nhất** ở đâu không | trạng thái, biểu đồ, hợp lệ / không hợp lệ |
| Người mù màu đỏ-lục còn phân biệt được lỗi với thành công? | |
| Chế độ tối: có làm hay không, và **quyết định ở đây** | không quyết ở đây thì sẽ phải dựng lại toàn bộ |

Số cụ thể của token đi vào `12-02` (Design system và khả năng tiếp cận) theo mã `TOK`. **Ở đây chốt hướng
và kiểm tương phản; `12-02` mới là nơi sở hữu con số.**

### Chữ

| Trường | Nội dung |
| --- | --- |
| Hệ chữ | và có sẵn cho cả iOS và Android không |
| Vì sao hệ chữ này | neo vào loại nội dung ở mục 0 |
| Cỡ nhỏ nhất dùng | ≥11pt, và ở đâu |
| Thang cỡ chữ | |
| Chịu được cỡ chữ hệ thống lớn nhất? | wireframe nào ở `08-03` sẽ vỡ trước |

## 5. Quét lần hai ảnh đối thủ — theo từng chức năng

Đây là **lần quét khác** với `07-00` (UX Research). Ở `07-00` đọc ảnh để hiểu **luồng và kiến trúc**.
Ở đây đọc lại đúng những ảnh đó để xem **họ vẽ chức năng ấy ra sao**.

Chỉ quét những chức năng **có trong `08-01` của mình**. Không mở rộng.

| Chức năng của mình | `SCR` | App đối thủ | Ảnh nguồn | Họ giải quyết thị giác thế nào | Có dùng được với hướng đã chọn ở mục 3? |
| --- | --- | --- | --- | --- | --- |
| | | | `03_...png` | bố cục · thứ bậc · mật độ · cách hiện trạng thái rỗng | Được / Được nếu sửa … / Không |

| Kiểm | Kết quả |
| --- | --- |
| Chức năng nào **không** tìm thấy ảnh đối thủ nào | đây là chỗ mình phải tự thiết kế — ghi ra, đừng để trống |
| Chỗ nào cả ba đối thủ làm giống nhau | quy ước thị giác, phá phải có lý do |
| Có mẫu nào đánh nhau với hướng đã chọn | và xử thế nào: đổi mẫu, hay đổi hướng kèm `CHG` |

**Không sinh màn hình mới ở mục này.** Thấy đối thủ có màn mình không có mà thấy cần thì đi qua
`08-04` (Báo cáo màn hình thiếu) và `CHG`, không thêm lặng lẽ vào đây.

## 6. Lọc màn hình cần dựng thị giác trước

Không phải màn nào cũng cần chốt thị giác cùng lúc. Lọc theo **luồng cốt lõi**, không theo số thứ tự màn.

| `SCR` | Tên màn | Có trong luồng cốt lõi nào (`FLOW`) | Ưu tiên thị giác | Vì sao |
| --- | --- | --- | --- | --- |
| | | | Chốt trước / Theo sau / Suy ra từ token | |

Ba mức có nghĩa khác nhau:

| Mức | Nghĩa |
| --- | --- |
| **Chốt trước** | màn định hình phong cách cho cả bộ — thường là màn đầu luồng cốt lõi và màn mang giá trị chính |
| **Theo sau** | dựng sau khi phong cách đã chốt, không tự quyết thị giác |
| **Suy ra từ token** | loading, rỗng, lỗi — chỉ cần token và mẫu thành phần, không cần vòng thiết kế riêng |

| Kiểm | Kết quả |
| --- | --- |
| Số màn "Chốt trước" | **nên ≤5** — nhiều hơn thì chưa lọc, chỉ đang liệt kê lại `08-01` |
| Mọi màn "Chốt trước" có wireframe ở `08-03` chưa | thiếu thì **dừng**, quay lại phase 08 |
| Có màn nào ở đây **không** có trong `08-01` | có là **lỗi** — sửa ngay, tài liệu này không cấp màn hình mới |

## 7. Nhánh dựng — chọn một, hỏi người dùng trước khi chọn

**Câu hỏi này phải hỏi người dùng, không được tự quyết.** Hỏi ngay khi bắt đầu phase 12, trước khi viết
mục nào của tài liệu này, vì nó đổi cả `12-01` và `12-02`.

```
Sang phase 12 (dựng prototype). Có hai nhánh, bạn chọn:

  A. Pencil + Agent dựng  — phù hợp app dạng tool, ít tính năng, có hệ thiết kế sẵn.
                            Tôi dựng theo từng luồng, bạn mở Pencil kiểm rồi approve, tôi dựng tiếp.
  B. Figma bạn dựng tay   — phù hợp app lớn. Tôi viết spec rồi TẠM DỪNG dự án ở đây.
                            Bạn dựng xong thì nói "đã dựng xong, đọc Figma qua MCP", tôi đối chiếu.

Hệ thiết kế có sẵn của bạn ở đâu? (đường dẫn file .pen, hoặc key file Figma, hoặc "chưa có")
```

| Trường | Nội dung |
| --- | --- |
| Nhánh đã chọn | **A. Pencil + Agent** / **B. Figma dựng tay** |
| `DEC` ghi lại lựa chọn | `DEC-___` |
| Hệ thiết kế có sẵn | đường dẫn, hoặc **chưa có** |
| Đã điền `design-system/_MANIFEST.md` mục 4 (bảng phủ) chưa | |
| Ai chịu trách nhiệm bản cuối | |

**Nhánh B là mặc định của bộ.** Nhánh A đảo quy tắc phạm vi *"AI không dựng UI"* ở `CLAUDE.md` và
`AGENTS.md`, nên phải có `DEC`; thiếu `DEC` thì không được dựng, kể cả khi người dùng nhắc qua trong chat.

### Nếu chọn nhánh A — Pencil + Agent

| Trường | Nội dung |
| --- | --- |
| Phạm vi AI được dựng | chỉ màn "Chốt trước" ở mục 6 · theo luồng · cả bộ |
| Chia lô theo | `FLOW` (khuyến nghị) hoặc nhóm `FEAT` |
| Component lấy từ | tên component trong `design-system/_MANIFEST.md` mục 3 — **gọi đúng tên, không vẽ lại** |
| Token lấy từ | `12-02`, và `12-02` trích từ hệ sẵn |
| Chữ lấy từ | `09-06` theo mã `CPY` — **không Lorem Ipsum, không tự viết chữ mới** |
| Ảnh tham chiếu nạp kèm | `UIP` đã quyết Áp dụng/Điều chỉnh ở mục 2 — **không nạp ảnh `khong-thich/`** |
| Điểm dừng | **sau mỗi lô**, chờ người dùng mở Pencil kiểm rồi approve |
| Đường ra | xuất `png` đối chiếu · `html` nếu cần · hoặc dựng lại trong Figma khi bàn giao |

**Ba thứ AI không được quyết ở nhánh này:** danh sách màn (đóng ở `08-01`), bố cục (đóng ở `08-03`), câu chữ
(đóng ở `09-06`). Việc của AI là **lắp**, không phải thiết kế. Thấy thiếu màn thì đi qua `08-04` và `CHG`.

### Nếu chọn nhánh B — Figma dựng tay

| Trường | Nội dung |
| --- | --- |
| Dự án tạm dừng ở đâu | sau khi `12-01` và `12-02` `approved` |
| Câu người dùng nói để tiếp tục | *"đã dựng xong, đọc Figma qua MCP"* |
| AI làm gì khi quay lại | đọc cấu trúc frame qua Figma MCP → chạy `12-03` → đối chiếu `08-01`, `08-02`, `09-06` |
| Chưa có MCP thì sao | người dùng dán danh sách tên frame vào một file text, AI đối chiếu từ đó |

**Dù nhánh nào, `12-01` vẫn phải viết.** Nó là danh sách frame bắt buộc và là căn cứ đối chiếu ở `12-03`.
Bỏ `12-01` vì "AI dựng rồi" là mất luôn cách biết đã dựng đủ chưa.

## 8. Điều KHÔNG học được từ ảnh tĩnh

| Thứ không thấy được | Vì sao quan trọng | Cách biết nếu cần |
| --- | --- | --- |
| Chuyển động và thời gian chuyển màn | quyết định cảm giác "mượt" | dùng thật, quay màn hình |
| Màu thật trên máy thật | ảnh chụp đã bị nén và đổi màu | dựng thử, xem trên điện thoại |
| Chữ ở cỡ hệ thống lớn nhất | chỗ layout vỡ | dựng thử một màn, bật cỡ chữ lớn nhất |
| Đọc được ngoài nắng không | | ra ngoài, cầm máy thật |

Kết luận nào phụ thuộc vào bảng trên mà chỉ dựa trên ảnh thì gắn `[ASM]`, và ghi vào
`docs/_ASSUMPTION_REGISTER.md`.

## 9. Nguồn phương pháp

| Nguồn | Áp dụng ở mục nào |
| --- | --- |
| `research-raw/moodboard/_MANIFEST.md` | mục 1, 2 |
| `research-raw/man-hinh-doi-thu/` | mục 5 |
| `.claude/shared/DESIGN_SYSTEM_GUIDE.md` | mục 4 |
| Skill chiều sâu đã dùng | |

## Thuật ngữ dùng trong tài liệu này

Chép nghĩa một câu từ `docs/_GLOSSARY.md` mục *Thuật ngữ chuyên môn*, và nghĩa của tiền tố mã từ
`docs/_ID_REGISTRY.md`. Chỉ liệt kê thứ **thật sự xuất hiện** trong tài liệu này.

| Thuật ngữ / tiền tố mã | Nghĩa một câu |
| --- | --- |
| | |

> Bảng này không phải để người trong nghề đọc — nó dành cho người ở vai trò khác đang phải duyệt tài liệu
> này. `validate_docs.py` đối chiếu: dùng mà không liệt kê là **LỖI**; liệt kê mà không dùng là cảnh báo.

<!-- QUALITY-GATE-MANIFEST:START
# Nguồn chân lý DUY NHẤT cho G10 phần tài liệu này. KHÔNG chép khối này vào file đầu ra ở docs/.
doc: 12-00_UI_RESEARCH
gate: G10
required_major:
  - "0. Đọc nhanh"
  - "0. Đọc trước khi mở ảnh — chống chọn phong cách theo cảm tính"
  - "1. Phạm vi moodboard đã thu"
  - "2. Mẫu thị giác quan sát được"
  - "3. Ba hướng thiết kế — chọn một"
  - "4. Hệ màu và chữ"
  - "5. Quét lần hai ảnh đối thủ — theo từng chức năng"
  - "6. Lọc màn hình cần dựng thị giác trước"
  - "7. Nhánh dựng — chọn một, hỏi người dùng trước khi chọn"
  - "8. Điều KHÔNG học được từ ảnh tĩnh"
  - "9. Nguồn phương pháp"
  - "Thuật ngữ dùng trong tài liệu này"
required_minor:
  "2. Mẫu thị giác quan sát được":
    - "Đọc từ thư mục `khong-thich/`"
  "4. Hệ màu và chữ":
    - "Màu"
    - "Chữ"
  "7. Nhánh dựng — chọn một, hỏi người dùng trước khi chọn":
    - "Nếu chọn nhánh A — Pencil + Agent"
    - "Nếu chọn nhánh B — Figma dựng tay"
quality_checks:
  - "Mục 0 điền TRƯỚC khi mô tả ảnh nào — số màn, nội dung nặng nhất, chuỗi chữ dài nhất, cảm giác cần có đều có mặt"
  - "Mục 0 dòng cảm giác cần có neo vào 04-04 hoặc 04-06 cụ thể, không viết chung chung"
  - "Mục 1 khớp bảng nghiệm thu của research-raw/moodboard/_MANIFEST.md; chủ đề chưa đủ ảnh thì đã nói rõ và hạ confidence"
  - "Thư mục khong-thich/ có ≥3 ảnh và đã đọc thành ràng buộc ở mục 2"
  - "Mọi UIP có quyết định Áp dụng / Điều chỉnh / Không dùng, không để trống"
  - "Không UIP nào lấy lý do là 'vì đẹp' hoặc 'vì đang là trend' — lý do phải nối về một dòng ở mục 0"
  - "Mục 3 có đủ BA hướng khác nhau thật, không phải ba biến thể của một hướng"
  - "Mục 3 đã chọn một hướng, có DEC ID, và ghi vì sao loại hai hướng còn lại"
  - "Mọi cặp màu chữ trên nền ở mục 4 đã kiểm tương phản, kể cả chữ phụ"
  - "Mục 4 đã trả lời chế độ tối làm hay không làm"
  - "Mục 4 không chốt giá trị token thay 12-02 — chỉ chốt hướng và kiểm tương phản"
  - "Mục 5 chỉ quét chức năng có trong 08-01, và đã nêu chức năng nào không tìm được ảnh đối thủ"
  - "Mục 5 không sinh màn hình mới; phát hiện màn thiếu thì đi qua 08-04 và CHG"
  - "Mục 6 mọi SCR đều tồn tại trong 08-01 — không có SCR lạ"
  - "Mục 6 số màn Chốt trước ≤5, hoặc có lý do vì sao nhiều hơn"
  - "Mục 6 mọi màn Chốt trước đã có wireframe ở 08-03"
  - "Mục 7 đã HỎI người dùng chọn nhánh, không tự quyết; lựa chọn có DEC ID"
  - "Mục 7 nếu chọn nhánh A (Pencil + Agent) thì DEC ghi rõ, và có điểm dừng approve sau mỗi lô"
  - "Có hệ thiết kế sẵn thì design-system/_MANIFEST.md mục 4 (bảng phủ) đã điền trước khi dựng frame đầu tiên"
  - "Có hệ thiết kế sẵn thì mục 3 và 4 của tài liệu này KIỂM hệ đó chịu được bộ màn hay không, không sáng tác phong cách mới"
  - "Mục 8 không bỏ trống; kết luận phụ thuộc thứ ảnh tĩnh không cho biết đã gắn [ASM]"
QUALITY-GATE-MANIFEST:END -->