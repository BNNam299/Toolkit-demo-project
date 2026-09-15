# design-system — hệ thiết kế có sẵn của bạn

| Trường | Nội dung |
| --- | --- |
| Nhánh dựng đã chọn | **Pencil + Agent** / **Figma dựng tay** — ghi `DEC` ở `12-00` mục 7 |
| File hệ thiết kế | ví dụ `design-system/amobear-ds.pen` hoặc key file Figma |
| Phiên bản hệ | |
| Cập nhật lần cuối | |
| Loại hệ | **hệ nhà** dùng cho nhiều dự án / **hệ riêng** cho dự án này |
| Trạng thái | đang dựng / đã đủ để chạy dự án / đã đối chiếu với `08-03` |

> **Đây là tài sản của bạn.** AI **đọc, không sửa** — giống `tech-input/` là tài sản của Dev.
> Muốn AI thêm component vào hệ thì phải nói rõ từng lần, và ghi vào mục 5 bên dưới.

---

## 0. Vì sao có thư mục này

Bạn dựng hệ thiết kế **trước** khi chạy dự án. Điều đó tốt — nhưng chỉ tốt khi hệ đó là **hệ nhà**, tức
là hệ dùng lại được cho nhiều dự án: màu thương hiệu, hệ chữ, nút, thẻ, input, tab bar, bottom sheet.

**Cảnh báo:** hệ dựng riêng cho một dự án **trước khi biết dự án có những màn nào** sẽ thiếu component, và
bạn phát hiện ra ở màn thứ hai mươi. Đó là lý do mục 4 bên dưới là mục bắt buộc, không phải mục cho vui.

Thứ tự không đổi: `08-01` (Kiểm kê màn hình) → `08-03` (Wireframe) → `12-00` (UI Research) → dựng.
Hệ thiết kế có sẵn **không** cho phép bỏ `12-00`; nó chỉ đổi việc `12-00` phải làm:

| Không có hệ sẵn | Có hệ sẵn |
| --- | --- |
| `12-00` chọn phong cách từ moodboard | `12-00` **kiểm hệ sẵn có chịu được bộ màn này không** |
| `12-02` sáng tác token và component | `12-02` **trích từ hệ sẵn**, chỉ khai báo phần thiếu |
| Ba hướng thiết kế → chọn một | Một hướng đã có; ba hướng thu về *"dùng nguyên / mở rộng / phá lệ ở đâu"* |

## 1. Kiểm kê token

Điền bằng tay hoặc nhờ AI đọc file hệ rồi bạn xác nhận. **Cột cuối là cột AI không tự suy được.**

| Loại | Tên trong hệ | Giá trị | Dùng cho |
| --- | --- | --- | --- |
| Màu | | | nền · chữ chính · chữ phụ · hành động · thành công · cảnh báo · lỗi |
| Chữ | | | tiêu đề · thân · nhãn · số |
| Khoảng cách | | | |
| Bo góc | | | |
| Đổ bóng | | | |

Token nào **không có** trong hệ mà `12-00` mục 4 cần thì ghi ở mục 5, đừng để AI tự đặt số.

## 2. Kiểm kê component

| Component trong hệ | Các biến thể | Các trạng thái có sẵn | Dùng cho `SCR` nào |
| --- | --- | --- | --- |
| | ví dụ: chính / phụ / nguy hiểm | mặc định · nhấn · vô hiệu · đang tải | |

**Cột "trạng thái có sẵn" quyết định bạn dựng được bao nhiêu ô của `08-02`.** Component chỉ có trạng thái
mặc định thì mọi màn lỗi, rỗng, đang tải sẽ phải dựng tay từng cái.

## 3. Quy ước đặt tên trong hệ

```
Ghi đúng cách bạn đã đặt tên trong Pencil hoặc Figma, ví dụ:
  Button/Primary/Default
  Card/List-item/With-thumbnail
  Input/Text/Error
```

Ghi lại ở đây vì AI cần **gọi đúng tên** để dùng lại component thay vì vẽ một component na ná mới.
Đây là chỗ hay sai nhất: dựng ra thứ trông giống hệ nhưng không phải instance của hệ, và sáu tháng sau
đổi màu thương hiệu thì những màn đó không đổi theo.

## 4. Bảng phủ — hệ có đủ cho dự án này không

**Mục bắt buộc.** Làm sau khi `08-03` (Wireframe) đã `approved`, trước khi dựng frame đầu tiên.

| Loại thành phần `08-03` cần | Có trong hệ? | Tên component | Thiếu gì |
| --- | --- | --- | --- |
| | Có / Có nhưng thiếu biến thể / Không có | | |

| Kết luận | Số lượng |
| --- | --- |
| Thành phần dùng nguyên được | |
| Thành phần cần thêm biến thể | |
| **Thành phần chưa có, phải dựng mới** | |

Con số cuối là con số đáng nhìn. Lớn quá thì hệ chưa sẵn cho dự án này — dựng bổ sung hệ **trước**, đừng
vừa dựng màn vừa sinh component, vì component sinh trong lúc dựng màn gần như luôn lệch nhau.

## 5. Sổ mở rộng hệ

Ghi lại mọi thứ thêm vào hệ trong lúc chạy dự án. Không ghi thì lần sau không ai biết cái nào là hệ gốc.

| # | Thêm gì | Vì sao dự án này cần | Ngày | Nên đưa vào hệ nhà? |
| --- | --- | --- | --- | --- |
| 1 | | | | Có / Không, chỉ dùng cho dự án này |

## 6. Nếu chọn nhánh Figma

Không cần điền mục 1–3 bằng tay. Ghi key file Figma vào bảng đầu, rồi để AI đọc qua Figma MCP khi cần
(`get_variable_defs` cho token, `get_metadata` cho cấu trúc frame). Vẫn phải điền **mục 4** — bảng phủ là
việc của người, không phải của công cụ.
