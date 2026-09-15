# Phương pháp — Prototype Figma

> Skill viết mới. Pipeline v2 mục 4 xác định đây là khoảng trống: cần spec để **người dựng tay** và cần quy
> trình review sau khi dựng.

**Phase này không dựng UI.** Người làm dựng tay trong Figma. Skill này viết spec trước khi dựng, và đối chiếu
sau khi dựng.

---

## Bước 1 — Prototype Build Spec (12-01)

Spec này là danh sách công việc cho người ngồi trước Figma. Viết đủ để người chưa đọc toàn bộ tài liệu vẫn dựng
đúng.

### Danh sách frame bắt buộc

Lấy từ `08-01_SCREEN_INVENTORY.md` và `08-02_STATE_MATRIX.md`. **Mỗi ô trong state matrix là một frame.**
Không gộp, không bỏ trạng thái vì "chắc giống nhau".

### Quy ước đặt tên frame

Tên frame trong Figma phải **khớp mã tài liệu**, nếu không thì bước đối chiếu sau này thành thủ công và sẽ
không ai làm.

```
SCR-012 · Kết quả phân tích · ST-04 Lỗi mạng
SCR-012 · Kết quả phân tích · ST-01 Mặc định
```

### Với mỗi frame, spec ghi

Mã `SCR` và `ST` · flow nào dẫn tới · dữ liệu hiển thị lấy từ đâu · CTA chính và phụ · **mã `CPY` cho mọi chuỗi
văn bản** · đường thoát khi người dùng không làm gì được ở trạng thái này.

**Không dùng Lorem Ipsum.** Chữ thật lấy từ `09-06_COPY_DECK.md` theo mã `CPY`. Chữ giả làm layout trông ổn
trong khi chữ thật sẽ tràn.

### Thứ tự dựng

Dựng theo flow, không theo thứ tự mã màn hình. Dựng trọn một flow rồi bấm thử từ đầu tới cuối sẽ phát hiện
thiếu sót nhanh hơn dựng rời từng màn.

---

## Bước 2 — Design System & Accessibility Baseline (12-02)

Đây là nguồn chân lý duy nhất cho token và component. Mọi màu, cỡ chữ, khoảng cách dùng trong Figma phải
truy được về một token có tên ở đây.

### Token

**Màu** — nền, chữ, nhấn, trạng thái thành công/cảnh báo/lỗi, viền. Mỗi màu có giá trị cho chế độ sáng và tối.
**Chữ** — thang cỡ chữ, độ đậm, chiều cao dòng, và **hành vi khi người dùng phóng cỡ chữ hệ thống**.
**Khoảng cách** — thang spacing, bo góc, đổ bóng.

### Component

Mỗi component ghi: tên · các biến thể · **đủ trạng thái** (mặc định, nhấn, vô hiệu, đang tải, lỗi, tập trung) ·
kích thước tối thiểu.

Trạng thái vô hiệu và đang tải là hai cái hay bị quên nhất, và là hai cái người dùng gặp nhiều nhất khi mạng chậm.

### Ngưỡng tiếp cận — kiểm được, không phải lời chúc

Tương phản chữ thường tối thiểu **4.5:1**, chữ lớn **3:1** · vùng chạm tối thiểu **44pt** mỗi chiều · layout
không vỡ khi phóng cỡ chữ hệ thống lên mức lớn nhất · **màu không phải kênh truyền tin duy nhất** — trạng thái
lỗi phải có cả biểu tượng hoặc chữ · mọi thành phần tương tác có nhãn cho trình đọc màn hình · thứ tự đọc hợp lý.

Mỗi ngưỡng phải kiểm được bằng công cụ hoặc bằng mắt theo cách lặp lại được.

---

## Bước 3 — Prototype Review (12-03)

Chạy **sau khi** người dựng xong. Đây là lúc skill này có giá trị cao nhất.

### Bốn phép đối chiếu

**Màn thiếu.** Mã `SCR` và `ST` nào có trong tài liệu mà chưa có frame tương ứng trong Figma?

**Màn thừa.** Frame nào có trong Figma mà không có mã trong tài liệu? Đây thường là dấu hiệu tốt — người dựng
phát hiện một trạng thái mà tài liệu bỏ sót. Nhưng phải **cập nhật ngược** vào `08-01` và `08-02`, không để nó
chỉ tồn tại trong Figma.

**Trạng thái thiếu.** Với mỗi màn có dữ liệu, đủ bốn trạng thái đang tải, rỗng, lỗi, có dữ liệu chưa? Với mỗi
màn có quyền, đủ nhánh đồng ý, từ chối, từ chối vĩnh viễn chưa?

**Chữ lệch.** Chữ trên frame có khớp `CPY` trong copy deck không? Lệch thì bên nào đúng? Copy deck là nguồn
chân lý — nếu chữ trong Figma hay hơn thì sửa copy deck rồi mới sửa Figma, đừng để hai bên nói khác nhau.

### Quy tắc cập nhật ngược

Khi dựng phát hiện tài liệu sai hoặc thiếu, **sửa tài liệu trước**, rồi mới sửa Figma. Ngược lại thì sáu tháng
sau không ai biết bản nào đúng.

Sai lệch phát hiện được ghi vào `12-03`, và nếu chạm tài liệu đã `approved` thì đi qua `CHG`.

---

## Điều kiện đóng cổng G10

Mọi frame bắt buộc đã dựng · tên frame khớp mã tài liệu · không còn Lorem Ipsum · mọi sai lệch đã cập nhật
ngược vào tài liệu nguồn · baseline tiếp cận đã kiểm và ghi kết quả.
