# Danh mục file trong thư mục này

| Trường | Nội dung |
| --- | --- |
| Cập nhật lần cuối | |
| Số file đã có | |
| Trạng thái | đang thu thập / đã đủ theo phiếu |

> **Cách dùng nhanh nhất:** bỏ hết file vào thư mục này, rồi gõ cho Claude:
>
> ```
> Liệt kê mọi file trong research-raw/sensor-tower/, mở từng file,
> rồi đề xuất điền bảng mục 2 của _MANIFEST.md.
> Chưa ghi vào file, đọc cho tôi xem trước để tôi sửa chỗ sai.
> ```
>
> Claude tự nhận diện app nào, chỉ số gì, nước nào — anh chỉ sửa chỗ nó đọc sai. Đỡ phải tự gõ bảng.

## 1. Vì sao cần file này

Claude đọc được ảnh và file, nhưng **hai chục file không tên tuổi thì nó phải mở hết mới biết cái nào chứa
gì** — chậm, tốn hạn mức, và dễ lẫn số của app này sang app khác.

File này là **mục lục**. Claude đọc mục lục trước, rồi chỉ mở đúng file cần cho tài liệu đang viết.

## 2. Bảng mục lục

| # | Tên file | App | Chỉ số chứa trong đó | Quốc gia | Khoảng thời gian | Ngày tra | Dạng |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | | | | | | | CSV / XLSX / PDF / ảnh |

## 3. Quy ước đặt tên

Đặt tên tự mô tả thì đỡ được phần lớn công việc của mục 2:

```
<ngày tra>_<app>_<chỉ số>_<quốc gia>.<đuôi>

2026-08-12_myfitnesspal_downloads_VN.csv
2026-08-12_myfitnesspal_retention_VN.png
2026-08-12_lifesum_pricing_US.png
```

Ngày tra là phần quan trọng nhất — số của công cụ intelligence đổi theo tháng, và tài liệu sẽ ghi nguồn
kèm ngày.

## 4. Dạng file: cái nào đáng tin hơn

| Dạng | Độ tin khi Claude đọc | Nên dùng khi |
| --- | --- | --- |
| **CSV / XLSX xuất từ công cụ** | cao nhất — số nguyên vẹn, không phải đọc hình | luôn ưu tiên nếu công cụ cho xuất |
| PDF báo cáo | cao | công cụ chỉ cho xuất PDF |
| **Ảnh chụp dashboard** | trung bình — **có thể đọc lệch số** | công cụ không cho xuất, hoặc anh chỉ cần nhìn nhanh |
| Ảnh chụp có chú thích tay của anh | cao hơn ảnh trơn | biểu đồ khó đọc, anh ghi thẳng con số lên ảnh |

**Xuất được file thì đừng chụp ảnh.** Claude đọc chart trong ảnh bằng cách suy từ vị trí cột và trục — sai
số thật, nhất là với biểu đồ không có nhãn số trên từng điểm.

Chỉ có ảnh thôi thì vẫn dùng được, nhưng bắt buộc qua bước xác nhận ở mục 5.

## 5. Bước xác nhận — không được bỏ

Sau khi Claude đọc file, nó ghi những gì đọc được vào `_EXTRACTED.md` **kèm con số và tên file nguồn**,
rồi đọc lại cho anh xác nhận.

Anh chỉ cần xác nhận những dòng Claude tự đánh dấu **độ tin thấp** — thường là số đọc từ biểu đồ trong ảnh.
Dòng lấy từ CSV thì không cần soi.

**Số chưa xác nhận không được chảy vào tài liệu ở `docs/`.** Một con số đọc lệch ở đây sẽ đi thẳng vào
`01-01` (Thị trường và vùng nhu cầu) và `03-01` (Chấm điểm nhu cầu và cơ hội) — nơi anh quyết định có làm
sản phẩm hay không.
