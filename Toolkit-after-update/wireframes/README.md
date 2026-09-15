# wireframes — wireflow HTML xem được trên trình duyệt

Đầu ra của phase 08 là **wireflow**, không phải bản vẽ bố cục và không phải hình vẽ bằng ký tự `---|||`.

Wireflow là **một trang cho một luồng**: các màn xếp cạnh nhau, nối bằng **mũi tên**, trên mũi tên ghi
*bấm gì*, ở nhánh ghi *điều kiện nào*. Mở một trang là thấy trọn luồng và biết ngay chỗ nào dư bước, chỗ nào
không có đường ra.

## Bốn câu wireflow phải trả lời — và chỉ bốn câu này

1. Màn này phục vụ **chức năng** gì?
2. **Vào từ** màn nào?
3. **Bấm cái gì** thì ra màn nào?
4. **Tình huống nào** thì rơi vào trạng thái nào?

**Không phải việc của phase này:** khoảng cách, cỡ chữ, độ cao, bo góc, màu. Chốt ở `12-00` (UI Research) sau
khi đọc moodboard. Chú thích số pt ở đây là ép quyết một thứ chưa tới lúc quyết, và làm cả nhóm chuyển sang
tranh luận thị giác trong khi hành vi còn chưa xong.

**Nút không cần bấm được.** Không `href`, không JavaScript. Điều hướng thể hiện bằng mũi tên trên trang flow.

## Xem thử

```
python -m http.server 8000
```

→ **http://localhost:8000/wireframes/**

Bắt buộc chạy qua `http`. Mở bằng nháy đúp (`file://`) thì trang flow trắng trơn, vì trình duyệt chặn nhúng
iframe từ `file://`. VS Code có extension **Live Preview** thì chuột phải vào file → *Show Preview*.

## Cấu trúc

```
wireframes/
├── _wireframe.css                            CSS lo-fi — ĐỌC KHỐI COMMENT ĐẦU FILE TRƯỚC KHI SỬA
├── _TEMPLATE.html                            copy để làm một MÀN
├── _TEMPLATE_FLOW.html                       copy để làm một LUỒNG
├── index.html                                danh sách luồng + thư viện màn rời
├── flow-FLOW-001.html                        ← ĐẦU RA CHÍNH, một file cho một luồng
└── SCR-012_ST-041_ket-qua-phan-tich.html     một file cho MỘT ô trong 08-02
```

**Một file màn cho một ô trong `08-02` (Ma trận trạng thái).** Không gộp trạng thái vào một file, không dùng
JavaScript bật tắt trạng thái — vì mỗi ô là một frame phải dựng ở phase 12, gộp lại thì `check_build.py`
không đếm được, còn người review bỏ sót đúng những trạng thái hay bị bỏ.

**Trang flow nhúng file màn bằng `iframe`.** Không chép nội dung màn vào trang flow — sửa màn thì flow tự cập
nhật theo. Một nguồn sự thật.

Tên file màn: `SCR-012_ST-041_ten-goi-nho.html`, mã **ba chữ số** khớp `08-02`. Viết `ST-41` là sai.

## Ba mục của một trang flow

| Mục | Nội dung | Vì sao cần |
| --- | --- | --- |
| **Đường chính** | happy path, các màn nối tiếp bằng mũi tên có nhãn | đây là thứ đọc trước |
| **Nhánh theo điều kiện** | mỗi nhánh một nhãn điều kiện: *nếu mã sai 3 lần* · *nếu mất mạng* | chỗ sản phẩm thật sự khó |
| **Trạng thái còn lại** | ô nào của `08-02` chưa xuất hiện ở hai mục trên thì đặt ở đây, kèm điều kiện vào | để **không bỏ sót** ô nào |

Mục thứ ba là mục cứu bạn. Đường chính và nhánh chính thì ai cũng làm; đang tải, rỗng, mất mạng, hết quyền
thì luôn là chỗ bị bỏ.

## Kiểm phủ

```
python .claude/scripts/check_build.py --wireframes wireframes/
```

Script so danh sách file màn với `08-01` (Kiểm kê màn hình) và `08-02`: màn nào thiếu, file nào thừa, trạng
thái nào chưa có, tên nào sai mã, và **màn nào chưa được trang flow nào nhúng**. Điều kiện đóng cổng **G7**.

Màn không nằm trong flow nào là dấu hiệu: hoặc nó mồ côi thật, hoặc trang flow còn thiếu một nhánh.

## Ranh giới với tài liệu `08-03`

| Thứ này | Nguồn chân lý là | Không nằm ở |
| --- | --- | --- |
| Luồng, mũi tên, điều kiện rẽ nhánh | `flow-FLOW-xxx.html` | `08-03` |
| Nội dung một màn, thứ tự nội dung | file màn `SCR-xxx_ST-xxx_*.html` | `08-03` |
| Chức năng · vào từ đâu · bấm gì ra đâu · điều kiện vô hiệu · đường thoát | khối `.w-notes` trong file màn | `08-03` |
| Bảng đếm, bảng kiểm, quyết định áp cho nhiều màn | `docs/08-screens/08-03_WIREFLOWS.md` | file HTML |

`08-03` **không mô tả lại luồng bằng lời**. Nó giữ phần đếm và phần kiểm.

## Ba điều không được làm

1. **Không màu thương hiệu.** Chỉ dùng biến `--w-*` trong `_wireframe.css`. Cả bộ xám, có chủ đích.
2. **Không font khác, không đổi thang cỡ chữ.**
3. **Không ảnh thật.** Dùng `.w-ph` — khối giữ chỗ **có nhãn** nói rõ chỗ đó là gì.

Thiếu class thì thêm ở **cuối** `_wireframe.css` kèm comment nói vì sao. Không sửa biến ở đầu file.

## Không Lorem Ipsum

Chữ thật, lấy theo mã `CPY` ở `docs/09-growth/09-06_COPY_DECK.md`. Chưa tới phase 09 thì viết câu thật mình
định dùng. **Chữ giả làm layout trông ổn trong khi chữ thật sẽ tràn** — và đó chính là thứ wireframe tồn tại
để phát hiện.

## Dùng lại ở phase 12

Wireflow không bị bỏ đi sau phase 08:

| Nhánh | Dùng thế nào |
| --- | --- |
| **Figma dựng tay** | mở trang flow cạnh Figma — có luôn thứ tự dựng và điều hướng, không phải đoán từ chữ |
| **Pencil + Agent** | nạp từng file màn vào Pencil rồi *import-to-canvas* → thành layer sửa được → áp token `12-02` và component `design-system/` |

Đường thứ hai biến việc *"AI sáng tác giao diện"* thành *"AI áp phong cách đã chốt lên bố cục đã chốt"*.

## Mở bản mẫu trước khi dựng file đầu tiên

`_VD_flow-FLOW-101.html` — một trang wireflow đã dựng đúng chuẩn, cùng bảy file màn `_VD_SCR-*.html`.
File bắt đầu bằng `_` nên `check_build.py` bỏ qua, không tính vào số màn của dự án.

Mở nó lên, rồi bắt chước. Ba điều đáng để ý:

1. **Trong khung máy chỉ có chữ người dùng sẽ đọc thật** — `"Tiếp tục"`, không phải
   `"Hành động chính của màn"`; `"Số lần mở mỗi ngày — 6 lần"`, không phải `"Row 50pt"`.
2. **Mã truy nguyên và điều kiện nằm ở khối ghi chú DƯỚI khung**, không nằm trong khung.
3. **Mũi tên nào cũng có nhãn "bấm gì"** — đó là tầng chú thích luồng, và là tầng duy nhất
   người đọc tài liệu cần để hiểu từ màn nào ra màn nào.

Sai kiểu hay gặp nhất là "kể" thay vì "vẽ": điền vào chỗ của tiêu đề một câu mô tả tiêu đề. Đọc từng file
thì thấy hợp lý; mở cả trang wireflow thì không ai đọc được nó như một app nữa.
