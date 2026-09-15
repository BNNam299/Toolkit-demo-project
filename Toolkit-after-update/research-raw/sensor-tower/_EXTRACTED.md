# Số Claude đọc được từ file thô — chờ bạn xác nhận

| Trường | Nội dung |
| --- | --- |
| Claude cập nhật ngày | |
| Đã đọc bao nhiêu file | |
| Số dòng chờ xác nhận | |
| Trạng thái | chờ xác nhận / đã xác nhận xong |

> **File này Claude ghi, bạn xác nhận.** Đây là file duy nhất trong `research-raw/` mà AI được viết vào —
> vì nó là *bản đọc* của AI, không phải bằng chứng của bạn.
>
> File thô bạn nộp và `SENSOR_TOWER_DATA.md` thì AI **không sửa**.

## 1. Vì sao có thêm một lớp nữa

Bạn nộp ảnh và file xuất. Ai đó phải chuyển thành số có cấu trúc để điền vào tài liệu. Nếu AI ghi thẳng vào
tài liệu ở `docs/` thì bạn mất cơ hội bắt chỗ nó đọc lệch — mà đọc lệch số từ biểu đồ trong ảnh là chuyện
xảy ra thật.

Nên: **AI đọc → ghi vào đây kèm nguồn và độ tin → bạn xác nhận → mới chảy vào tài liệu.**

## 2. Số đã đọc

| # | App | Chỉ số | Giá trị Claude đọc được | Quốc gia | Kỳ | File nguồn | Cách đọc | Độ tin | Bạn xác nhận |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | | | | | | | ô số trong bảng / nhãn trên biểu đồ / **suy từ vị trí cột** | cao / trung bình / **thấp** | ⬜ |

Ý nghĩa cột **Cách đọc** — đây là cột quyết định bạn có phải soi dòng đó hay không:

| Cách đọc | Nghĩa | Bạn cần làm gì |
| --- | --- | --- |
| ô số trong bảng | số nằm sẵn dạng chữ trong CSV, XLSX, hoặc bảng trong ảnh | không cần soi |
| nhãn trên biểu đồ | biểu đồ có in số ngay trên điểm | xem qua |
| **suy từ vị trí cột** | biểu đồ **không có số**, Claude ước theo chiều cao cột so với trục | **phải soi** — đây là chỗ sai |

**Claude không được ghi độ tin `cao` cho dòng đọc bằng cách suy từ vị trí cột.** Nếu thấy dòng nào như vậy
thì đó là lỗi, bắt sửa.

## 3. Số Claude không đọc được

| File nguồn | Chỉ số cần | Vì sao không đọc được |
| --- | --- | --- |
| | | ảnh mờ / biểu đồ không có trục số / bị che / không thấy chỉ số này trong file |

Ghi ra đây thay vì đoán. Bạn mở lại công cụ chụp cái khác nhanh hơn nhiều so với việc phát hiện một con số
bịa ba phase sau.

## 4. Mâu thuẫn với dữ liệu đã có

| Số ở đây | Số đã có trong tài liệu | Tài liệu nào | Chênh bao nhiêu | Chọn số nào, vì sao |
| --- | --- | --- | --- | --- |
| | | | | |

Hai công cụ cho hai con số khác nhau là bình thường — chúng đều là ước lượng. **Đừng lấy trung bình.**
Chọn một nguồn, ghi rõ vì sao chọn, và ghi cả con số kia vào ghi chú để sau này còn truy được.

## 5. Sau khi bạn xác nhận

Claude làm ba việc, theo đúng thứ tự:

1. Điền số **đã xác nhận** vào tài liệu đích, nguồn ghi dạng
   *"ước lượng theo Sensor Tower, file `<tên file>`, ngày tra `<ngày>`"*.
2. Dòng bạn **không xác nhận** hoặc đánh dấu sai: bỏ, hoặc chuyển thành `[ASM]` kèm dòng ở
   `docs/_ASSUMPTION_REGISTER.md`. **Không im lặng dùng số chưa xác nhận.**
3. Cập nhật `_MANIFEST.md` mục 1 và báo cáo còn thiếu chỉ số nào so với phiếu
   `../SENSOR_TOWER_REQUEST.md`.
