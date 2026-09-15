---
doc_id: 07-00
title: UX Research
phase: 07-structure
skill: ux-structure-architect
profile: Bắt buộc
owner: PO
reviewers: []
version: 0.1.0
status: draft
last_updated:
approved_by: ""
approved_at: ""
depends_on: [02-01, 04-04, 04-06]
feeds: [07-01, 07-02, 07-03, 07-05, 08-01, 09-01]
id_prefix: [PAT]
gate: G6
in_handover: true
confidence: medium
---

# [Tên dự án] — UX Research

> **Tài liệu đầu tiên của phase 07.** Mổ xẻ UX, UI, luồng và kiến trúc thông tin của các app đối thủ từ
> ảnh chụp màn hình, rồi quyết định lấy gì, sửa gì, bỏ gì.
>
> Nguồn ảnh: `research-raw/man-hinh-doi-thu/<tên-app>/`, mục lục ở `_MANIFEST.md` cùng thư mục.
> Tập app phải khớp `02-01` (Bản đồ đối thủ) — thêm app ngoài tập thì ghi lý do ở mục 1.

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


## 0. Đọc trước khi mở ảnh — chống neo vào đối thủ

**Đọc `04-04` (Việc người dùng cần làm xong) và `04-06` (Hành trình người dùng) TRƯỚC khi xem ảnh đầu tiên.**

Lý do: xem giao diện đối thủ trước rồi mới nghĩ về người dùng của mình là cách chắc chắn nhất để sao chép.
Đọc JTBD trước thì mỗi mẫu quan sát được sẽ tự động bị đặt câu hỏi *"cái này phục vụ job nào của người
dùng của tôi?"* — và mẫu nào không trả lời được thì trượt ngay.

| Trường | Nội dung |
| --- | --- |
| `JTBD` chính của sản phẩm mình | `JTBD-xxx` — … |
| Khoảnh khắc aha đã xác định ở `04-06` | |
| Bối cảnh dùng đặc thù của người dùng mình | ví dụ: một tay, trong quán đông, đang vội |

## 1. Phạm vi

| App | Thư mục ảnh | Số ảnh | Luồng đã chụp | Có trong `02-01`? | Phiên bản / ngày chụp |
| --- | --- | --- | --- | --- | --- |
| | `research-raw/man-hinh-doi-thu/<tên>/` | | onboarding · ghi bản ghi · paywall · … | Có / Không, lý do | |

Ghi **ngày chụp**: giao diện app đổi liên tục, một bản phân tích không có ngày sẽ bị dùng lại khi đã lỗi thời.

## 2. Mổ xẻ theo từng app

Lặp khối này cho mỗi app.

### [Tên app]

**Kiến trúc thông tin**

| Trường | Nội dung |
| --- | --- |
| Kiểu điều hướng chính | tab bar · drawer · stack · nút nổi trung tâm |
| Số mục điều hướng cấp 1 | |
| Nhóm nội dung theo cách nào | theo tính năng · theo thời gian · theo đối tượng · theo tần suất dùng |
| Cái gì được đẩy lên cấp 1 | và **điều đó nói lên họ ưu tiên gì** |
| Cái gì bị chôn sâu | mấy lần chạm mới tới |

**Luồng cốt lõi**

| Bước | Màn hình | Người dùng phải làm gì | Ảnh nguồn |
| --- | --- | --- | --- |
| 1 | | | `01_...png` |

| Trường | Nội dung |
| --- | --- |
| Số bước từ mở app tới giá trị đầu tiên | |
| Số trường bắt buộc nhập trước khi thấy giá trị | |
| Có bỏ qua được onboarding không | |
| Vị trí paywall so với khoảnh khắc giá trị | trước · ngay sau · sau vài lần dùng |

**Giao diện đáng chú ý**

| Quan sát | Ảnh nguồn | Vì sao đáng chú ý |
| --- | --- | --- |
| | | |

## 3. Mẫu quan sát được và quyết định

Đây là **mục quan trọng nhất của tài liệu**. Không có mục này thì bản phân tích chỉ là một danh mục đẹp mà
không ai dùng.

| `PAT` | Mẫu quan sát được | Thấy ở app nào | Ảnh nguồn | Quyết định | Lý do — neo vào `INS` hoặc `JTBD` của mình | Đổ vào tài liệu nào |
| --- | --- | --- | --- | --- | --- | --- |
| `PAT-001` | | | | Áp dụng / Điều chỉnh / Không dùng | | `07-02` · `07-05` · `08-01` · `09-01` |

**Cột lý do không được viết "vì đối thủ làm vậy".** Không giải thích được bằng nhu cầu người dùng của mình
thì đó là sao chép, không phải học hỏi — và mẫu đó phải chuyển sang **Không dùng**.

Ba quyết định có nghĩa khác nhau:

| Quyết định | Nghĩa | Bắt buộc kèm |
| --- | --- | --- |
| **Áp dụng** | lấy nguyên cách làm | `INS` hoặc `JTBD` cho thấy người dùng mình cũng cần đúng thứ đó |
| **Điều chỉnh** | lấy ý, đổi cách | đổi cái gì, và **vì sao bối cảnh người dùng mình khác** |
| **Không dùng** | bỏ | vì sao — và đây thường là chỗ sinh ra cơ hội, ghi tiếp vào `02-04` qua `CHG` nếu phát hiện `GAP` mới |

## 4. So sánh chéo — chỗ nào là quy ước, chỗ nào là không gian thiết kế

| Hạng mục | Các app làm giống nhau? | Kết luận |
| --- | --- | --- |
| Vị trí nút hành động chính | | |
| Cách vào màn tạo bản ghi | | |
| Thứ tự bước onboarding | | |
| Thời điểm hiện paywall | | |

Cách đọc bảng này:

**Mọi app làm giống nhau** → đó là **quy ước ngành**. Người dùng đã học rồi. Phá quy ước phải có lý do
mạnh, và phải trả giá bằng việc dạy lại người dùng. Ghi rõ nếu định phá.

**Mỗi app một kiểu** → đó là **không gian thiết kế còn mở**. Không có đáp án đúng sẵn, và đây là chỗ đáng
để mình làm khác — nhưng phải khác vì người dùng mình khác, không phải khác cho khác.

## 5. Luồng đề xuất cho sản phẩm mình

| Trường | Nội dung |
| --- | --- |
| Theo luồng của app nào, hay kết hợp, hay tự làm khác | |
| Nếu kết hợp: lấy phần nào của ai | trích `PAT` |
| Số bước tới giá trị đầu tiên **mình nhắm tới** | so với con số của từng đối thủ ở mục 2 |
| Chỗ mình cố ý làm khác | và cái giá phải trả |
| `DEC` ghi lại quyết định này | |

Đây mới là đề xuất. `07-05` (Luồng trải nghiệm) mới là nơi vẽ ra thật, và nó **phải trích `PAT`** chứ không
chép lại nội dung ở đây.

## 6. Điều KHÔNG học được từ ảnh chụp

| Thứ không thấy được | Vì sao quan trọng | Cách biết nếu cần |
| --- | --- | --- |
| Chuyển động, thời gian phản hồi, phản hồi rung | quyết định cảm giác "mượt" mà ảnh không cho thấy | dùng thật, quay màn hình |
| Hành vi khi mất mạng, khi lỗi | chỗ sinh ra nhiều màn hình nhất ở `08-02` | dùng thật, bật chế độ máy bay |
| Cá nhân hoá sau vài tuần dùng | giao diện lần đầu khác hẳn lần thứ hai mươi | dùng thật, dài ngày |
| Vì sao họ chọn cách đó | ảnh chỉ cho thấy kết quả, không cho thấy lý do | đọc review ở `02-03` |

**Ảnh chụp bổ sung cho `02-02` (Mổ xẻ đối thủ), không thay thế việc dùng thật.** Kết luận nào phụ thuộc vào
những thứ ở bảng trên mà chỉ dựa trên ảnh thì gắn `[ASM]`.

## 7. Nguồn phương pháp

| Nguồn | Áp dụng ở mục nào |
| --- | --- |
| `references/` của skill này | |
| Skill chiều sâu đã dùng | |
| Thư mục ảnh, ngày chụp | mục 1, 2 |

## Thuật ngữ dùng trong tài liệu này

Chép nghĩa một câu từ `docs/_GLOSSARY.md` mục *Thuật ngữ chuyên môn*, và nghĩa của tiền tố mã từ
`docs/_ID_REGISTRY.md`. Chỉ liệt kê thứ **thật sự xuất hiện** trong tài liệu này.

| Thuật ngữ / tiền tố mã | Nghĩa một câu |
| --- | --- |
| | |

> Bảng này không phải để người trong nghề đọc — nó dành cho người ở vai trò khác đang phải duyệt tài liệu
> này. `validate_docs.py` đối chiếu: dùng mà không liệt kê là **LỖI**; liệt kê mà không dùng là cảnh báo.

<!-- QUALITY-GATE-MANIFEST:START
# Nguồn chân lý DUY NHẤT cho G6 phần tài liệu này. KHÔNG chép khối này vào file đầu ra ở docs/.
doc: 07-00_UX_RESEARCH
gate: G6
required_major:
  - "0. Đọc nhanh"
  - "0. Đọc trước khi mở ảnh — chống neo vào đối thủ"
  - "1. Phạm vi"
  - "2. Mổ xẻ theo từng app"
  - "3. Mẫu quan sát được và quyết định"
  - "4. So sánh chéo — chỗ nào là quy ước, chỗ nào là không gian thiết kế"
  - "5. Luồng đề xuất cho sản phẩm mình"
  - "6. Điều KHÔNG học được từ ảnh chụp"
  - "7. Nguồn phương pháp"
  - "Thuật ngữ dùng trong tài liệu này"
required_minor:
  {}
quality_checks:
  - "Mục 0 điền TRƯỚC khi mô tả app nào — JTBD và aha moment của mình phải có mặt"
  - "Tập app ở mục 1 khớp 02-01; app ngoài tập có ghi lý do"
  - "Mỗi app ở mục 1 có ngày chụp — không có ngày là không dùng được"
  - "Mọi PAT ở mục 3 có quyết định Áp dụng / Điều chỉnh / Không dùng, không để trống"
  - "Không PAT nào có lý do là 'vì đối thủ làm vậy' — lý do phải neo vào INS hoặc JTBD cụ thể"
  - "Mọi PAT quyết định Áp dụng hoặc Điều chỉnh đều ghi đổ vào tài liệu nào"
  - "Mục 4 phân biệt rõ quy ước ngành với không gian thiết kế còn mở"
  - "Mục 5 có DEC ID"
  - "Mục 6 không bỏ trống — phải nêu điều ảnh chụp KHÔNG cho biết"
  - "Kết luận chỉ dựa trên ảnh mà cần dùng thật mới chắc đã gắn [ASM]"
QUALITY-GATE-MANIFEST:END -->
