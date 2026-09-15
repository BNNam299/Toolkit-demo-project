---
name: market-data-sourcing
description: Bản đồ nguồn dữ liệu thị trường mobile app và danh mục chỉ số cần lấy cho từng nguồn — trang store, AppStoreSpy, Sensor Tower, review, Google Trends. Dùng ở phase 01 và 02 khi đào số liệu đối thủ, đặc biệt khi một phần dữ liệu phải do người dùng tự tra tay ở công cụ mà AI không truy cập được. Sinh phiếu yêu cầu dữ liệu để người dùng điền, thay vì hỏi rời rạc từng con số.
---

# Lấy dữ liệu thị trường: nguồn nào cho gì, và hỏi thế nào

Skill chiều sâu cho phase 01 và 02. Đọc cùng `ai-research-provenance` — skill đó lo **cách ghi nguồn**,
skill này lo **lấy gì và lấy ở đâu**.

## Vấn đề skill này giải

PO mới thường không biết một công cụ intelligence có những chỉ số gì, nên hoặc lấy thiếu, hoặc lấy một
đống số không dùng được vào tài liệu nào. Tệ hơn: khi AI không truy cập được công cụ, nó hỏi rời rạc từng
con số qua nhiều lượt, PO phải mở đóng tab hàng chục lần.

Cách làm đúng: **khai thác hết những nguồn AI vào được trước**, xác định chính xác còn thiếu gì, rồi sinh
**một phiếu yêu cầu duy nhất** để người dùng tra một lần và dán về.

## Bản đồ nguồn

| Nguồn | AI vào được không | Cho gì | Độ tin |
| --- | --- | --- | --- |
| Trang App Store / Google Play | Có, đọc trực tiếp | mô tả, ảnh, giá gói, ngày cập nhật, điểm số, số lượt đánh giá, changelog | cao — dữ liệu công bố |
| Review trên store | Có | pain point nguyên văn, lời phàn nàn theo phiên bản | cao cho câu chữ, thấp cho tỷ lệ |
| Reddit, diễn đàn, TikTok, YouTube | Có | ngôn ngữ người dùng thật, workaround thủ công | trung bình |
| Google Trends | Có | hướng quan tâm theo thời gian, tính mùa | trung bình — chỉ là tương đối |
| Công cụ keyword ASO | Thường có | volume tìm kiếm, độ khó, biến thể từ khoá | trung bình |
| **AppStoreSpy** (người dùng có tài khoản, extension điều khiển được) | Có, qua browser | xếp hạng, ước lượng download và doanh thu, lịch sử update, keyword ranking | **ước lượng**, không phải số thật |
| **Sensor Tower** (tài khoản không dùng được qua extension) | **Không** — người dùng tra tay | ước lượng download/doanh thu theo quốc gia, retention, thời lượng dùng, chồng lấn người dùng, chi tiêu quảng cáo | **ước lượng**, thường coi là mạnh nhất trong nhóm này |
| Bản báo cáo công khai của công ty | Có | số thật nếu là công ty đại chúng | cao |

**Quy tắc nhãn:** mọi số từ AppStoreSpy và Sensor Tower là **ước lượng của bên thứ ba**, ghi `[FACT]` với
nguồn là *"ước lượng theo <công cụ>, ngày <ngày>"* — không ghi như số liệu nội bộ của đối thủ. Số liệu nội
bộ thật mà không có nguồn công khai thì ghi **Không công bố**.

## Thứ tự khai thác — đừng làm ngược

1. **Trang store + review + cộng đồng.** Miễn phí, có câu chữ nguyên văn, nuôi `01-02` (Sổ đào pain point)
   và `02-03` (Đào review người dùng). Làm hết bước này trước.
2. **AppStoreSpy.** Xác định tập đối thủ thật và thứ hạng, nuôi `02-01` (Bản đồ đối thủ).
3. **Dùng thật 5–6 app.** Không công cụ nào thay được bước này; nuôi `02-02` (Mổ xẻ đối thủ).
4. **Chỉ khi đó mới sinh phiếu Sensor Tower.** Vì tới lúc này mới biết cần số của **app nào**, ở **quốc gia
   nào**, cho **câu hỏi nào** — hỏi trước bước 3 là hỏi bừa.

Bước 4 sinh file `research-raw/SENSOR_TOWER_REQUEST.md`. Xem mục dưới.

## Danh mục chỉ số Sensor Tower — lấy gì và để làm gì

Đây là phần PO mới hay bỏ sót. **Không lấy hết** — chỉ lấy những dòng có cột *Dùng vào* trỏ tới tài liệu
đang viết.

### Nhóm 1 — Quy mô, để biết ngách có đủ lớn

| Chỉ số | Nghĩa | Đọc thế nào | Dùng vào |
| --- | --- | --- | --- |
| Downloads / tháng | ước lượng lượt tải mới | so giữa các đối thủ, đừng tin con số tuyệt đối | `01-01` vùng nhu cầu, `03-01` chấm điểm |
| Revenue / tháng | ước lượng doanh thu in-app | chia cho downloads được ARPU thô | `03-01`, `09-02` đặc tả kiếm tiền |
| Phân bố theo quốc gia | tải và doanh thu theo nước | ngách có thể lớn ở nước khác mà nhỏ ở VN | `01-01`, `00-02` khoá phạm vi |
| Xu hướng 12–24 tháng | đường tăng giảm | **quan trọng hơn con số tuyệt đối** — ngách đang lên hay đang chết | `01-01`, `03-01` |

### Nhóm 2 — Sức khoẻ sản phẩm đối thủ, để biết họ yếu ở đâu

| Chỉ số | Nghĩa | Đọc thế nào | Dùng vào |
| --- | --- | --- | --- |
| Retention D1 / D7 / D30 | % người còn quay lại sau 1, 7, 30 ngày | D30 thấp mà tải cao = mua traffic, sản phẩm không giữ được người → khoảng trống | `02-04` khoảng trống cơ hội, `10-01` khung chỉ số |
| Thời lượng phiên, số phiên/ngày | mức độ dùng | ngắn và ít mà doanh thu cao = mô hình dựa subscription bị quên huỷ | `09-03` giữ chân, `10-03` phễu |
| Chồng lấn người dùng | % người dùng nhiều app cùng lúc | chồng lấn cao = người dùng chưa tìm được app đủ tốt | `02-01`, `02-04` |
| Tỷ lệ giữ theo bản cập nhật | retention đổi sau update | rơi sau một bản = họ vừa làm hỏng gì đó | `02-02` mổ xẻ đối thủ |

### Nhóm 3 — Kiếm tiền, để đặt giá và chọn vị trí paywall

| Chỉ số | Nghĩa | Đọc thế nào | Dùng vào |
| --- | --- | --- | --- |
| Cấu trúc gói và giá theo nước | tuần / tháng / năm / vĩnh viễn | giá VN thường lệch mạnh so với US | `09-02` — **chỉ tài liệu này được ghi giá bằng số** |
| Tỷ lệ doanh thu theo gói | gói nào ra tiền | phần lớn doanh thu từ gói năm là tín hiệu khác hẳn từ gói tuần | `09-02`, `10-01` |
| Ước lượng chuyển đổi trial → paid | nếu công cụ có | dùng làm mốc so, không dùng làm cam kết | `09-04` kế hoạch A/B, `10-01` |
| Chi tiêu quảng cáo, kênh chạy | họ mua traffic ở đâu | tiêu nhiều mà retention thấp = mô hình dễ vỡ | `02-04`, `03-01` |

### Nhóm 4 — chỉ lấy khi cần trả lời một câu cụ thể

Từ khoá đang mua, sáng tạo quảng cáo, phiên bản SDK, lịch sử đổi tên app. **Đừng lấy sẵn.** Mỗi dòng dữ
liệu không gắn với một câu hỏi là một dòng làm loãng tài liệu.

## Ba bẫy đọc số

**Ước lượng không phải số thật.** Sai số của công cụ intelligence với app nhỏ có thể vài trăm phần trăm.
Dùng để **so tương đối giữa các app**, không dùng để tính doanh thu dự kiến của mình.

**Tải cao không có nghĩa là ngách tốt.** Có thể họ đang đốt tiền quảng cáo. Luôn đọc downloads **cùng với**
retention D30.

**Một công cụ là một nguồn.** Lấy ba chỉ số từ Sensor Tower vẫn là **một** nguồn, không phải ba. Muốn dán
nhãn `[INSIGHT]` thì cần thêm một nguồn độc lập — review, cộng đồng, hoặc trải nghiệm dùng thật.

## Đọc dữ liệu người dùng nộp dạng file thô

Người dùng có thể nộp nhiều file trong `research-raw/sensor-tower/`: file xuất CSV/XLSX, PDF báo cáo, và
ảnh chụp dashboard. Quy trình bắt buộc, **ba lớp**:

| Lớp | File | Quyền của bạn |
| --- | --- | --- |
| Thô | file người dùng nộp | **chỉ đọc** |
| Bản đọc | `sensor-tower/_EXTRACTED.md` | **được ghi** — đây là file duy nhất trong `research-raw/` bạn được viết |
| Tài liệu | `docs/…` | chỉ số **đã được xác nhận** mới được vào |

### Thứ tự

1. **Đọc `_MANIFEST.md` trước.** Nếu mục lục trống thì liệt kê file, mở từng file, **đề xuất** điền mục lục,
   đọc cho người dùng sửa. Đừng mở hết mọi file rồi mới hỏi — mục lục tồn tại để bạn chỉ mở đúng file cần
   cho tài liệu đang viết.
2. **Ghi vào `_EXTRACTED.md`**, mỗi con số một dòng, kèm bốn thứ: **file nguồn · cách đọc · độ tin · kỳ và
   quốc gia**.
3. **Đọc lại cho người dùng những dòng độ tin thấp**, chờ xác nhận.
4. Chỉ điền vào tài liệu những dòng đã xác nhận. Dòng không xác nhận: bỏ, hoặc chuyển `[ASM]` kèm dòng ở
   `_ASSUMPTION_REGISTER.md`. **Không im lặng dùng số chưa xác nhận.**

### Cột "cách đọc" — bắt buộc, không được bỏ

| Cách đọc | Độ tin cho phép |
| --- | --- |
| ô số trong bảng (CSV, XLSX, bảng trong ảnh) | cao |
| nhãn số in trên biểu đồ | cao hoặc trung bình |
| **suy từ vị trí cột trên biểu đồ không có nhãn số** | **thấp — không bao giờ được ghi là cao** |

Đọc biểu đồ không có nhãn số là **ước theo chiều cao cột so với trục**. Sai số thật. Ghi độ tin `cao` cho
dòng như vậy là vi phạm, vì người dùng sẽ bỏ qua bước soi và một con số lệch đi thẳng vào `01-01`
(Thị trường và vùng nhu cầu) và `03-01` (Chấm điểm nhu cầu và cơ hội) — nơi họ quyết định có làm sản phẩm
hay không.

Ảnh mờ, biểu đồ bị che, hoặc không thấy chỉ số cần: ghi vào `_EXTRACTED.md` mục 3 *"số không đọc được"*
kèm lý do. Người dùng mở lại công cụ chụp cái khác nhanh hơn nhiều so với việc phát hiện một con số bịa ba
phase sau.

### File xuất thì dùng công cụ, đừng đọc bằng mắt

CSV và XLSX nhiều dòng: dùng Bash để đọc và tổng hợp thay vì đọc thủ công — chính xác hơn và không bỏ sót
dòng. Đọc xong vẫn ghi vào `_EXTRACTED.md` với `cách đọc = ô số trong bảng`, `độ tin = cao`.

### Hai công cụ cho hai con số khác nhau

Bình thường — chúng đều là ước lượng. **Không lấy trung bình.** Chọn một nguồn, ghi rõ vì sao chọn, ghi con
số kia vào ghi chú, và điền vào `_EXTRACTED.md` mục 4 *"mâu thuẫn với dữ liệu đã có"*.

## Cách sinh phiếu yêu cầu

Khi tới bước 4, ghi ra `research-raw/SENSOR_TOWER_REQUEST.md` theo đúng khuôn có sẵn trong file đó, và:

- Chỉ liệt kê chỉ số có cột *Dùng vào* trỏ tới tài liệu đang viết hoặc sắp viết.
- Với mỗi dòng, ghi rõ **câu hỏi mà con số này trả lời**. Không giải thích được thì bỏ dòng đó.
- Ghi rõ app nào, quốc gia nào, khoảng thời gian nào. *"Retention của đối thủ"* là yêu cầu không tra được.
- Gộp mọi thứ vào **một phiếu**, đừng hỏi lẻ qua nhiều lượt.
- Nói rõ chỉ số nào **bắt buộc** để đóng cổng G1, chỉ số nào chỉ là *tốt nếu có* — để người dùng biết
  chỗ nào được phép bỏ trống.

Sau khi người dùng dán số vào `research-raw/SENSOR_TOWER_DATA.md`: đọc, báo cáo sẽ điền vào tài liệu nào,
**liệt kê chỗ mâu thuẫn với dữ liệu đã có**, chờ duyệt. Không sửa file người dùng đã điền.

Chỉ số người dùng để trống: gắn `[ASM]` nếu vẫn phải suy luận tiếp, hoặc ghi **Không công bố** nếu bỏ hẳn.
**Không tự điền số thay người dùng** — đó là bịa số liệu thị trường.
