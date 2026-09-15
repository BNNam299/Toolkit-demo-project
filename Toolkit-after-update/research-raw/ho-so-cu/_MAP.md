# Hồ sơ cũ — phiếu công tác nạp vào Pipeline v2

| Trường | Nội dung |
| --- | --- |
| Dự án cũ tên gì | |
| Bộ tài liệu cũ viết bằng gì | ví dụ app-spec, Notion, Confluence, Word |
| Số file | |
| Ngày nhận hồ sơ | |
| Trạng thái nạp | chưa bắt đầu / đã có bản đồ / đang lấp / đã xong |

> Quy trình đầy đủ: `.claude/commands/import-legacy.md`. Gõ `/import-legacy bản đồ` để bắt đầu.
>
> **File cũ trong thư mục này là bằng chứng — AI đọc, không sửa, không xoá.**
> Chỉ file `_MAP.md` này là nơi AI được ghi.

## 1. Kiểm kê file cũ

| # | File | Số dòng | Ngày cập nhật cuối | Phiên bản (nếu có) | Nội dung chính |
| --- | --- | --- | --- | --- | --- |
| 1 | | | | | |

**Cột ngày dùng ở mục 4.** File nào mới hơn hẳn các file khác thì các file cũ hơn là nghi phạm mâu thuẫn.

## 2. Bản đồ phủ — làm trước, chưa lấp gì

Một dòng cho **từng** tài liệu trong `docs/_INDEX.md`. Đừng chỉ ghi những dòng có nội dung; dòng
**Không có** cũng là thông tin.

| `doc_id` | Tên tài liệu | Nguồn ở hồ sơ cũ (file + mục) | Mức phủ | Có dẫn nguồn? | Đã lấp chưa |
| --- | --- | --- | --- | --- | --- |
| `00-01` | Bản mô tả dự án | | Đủ / Một phần / Không có | Có / Không / Một phần | |

**Cột "Có dẫn nguồn" là cột quan trọng nhất của phiếu này.** Hồ sơ cũ thường rất chắc ở chỗ có nguồn và
**bịa hoàn toàn** ở chỗ không có nguồn — mà đọc bề ngoài hai chỗ giống nhau. Chỗ *Không* khi lấp sang phải
gắn `[ASM]`, tuyệt đối không thành `[FACT]`.

| Tổng kết | Số lượng |
| --- | --- |
| Đủ | |
| Một phần | |
| Không có | |
| **Trong đó không dẫn nguồn** | |

## 3. Hệ mã — chốt trước khi lấp dòng đầu tiên

### 3.1 Prefix trùng nghĩa — nhận nguyên số cũ

| Prefix | Số cuối đã cấp ở hồ sơ cũ | Số bắt đầu cấp mới | Đã cập nhật `_ID_REGISTRY` |
| --- | --- | --- | --- |
| `FR` | | | |
| `UC` | | | |
| `NFR` | | | |
| `BR` | | | |

**Không đánh số lại.** Có `FR-001`…`FR-066` thì nhận nguyên, đặt *Số cuối đã cấp* = `066`, ID mới từ `067`.
Đánh số lại là làm chết mọi tham chiếu trong ticket, commit và lịch sử chat của dự án.

### 3.2 Prefix cũ không có trong bộ này

| Prefix cũ | Nghĩa ở hồ sơ cũ | Xử lý | Prefix mới | Lý do |
| --- | --- | --- | --- | --- |
| | | Đổi / Thêm vào `_ID_REGISTRY` | | |

Ví dụ hay gặp: `WF` (màn wireframe) → `SCR` · `TF` (task flow xuyên màn) → `FLOW` · `SF` (sub-flow trong một
màn) → nhánh trong `FLOW` hoặc `ST` · `AF` (luồng thay thế) → nhánh trong `UC` · `ERR` (tình huống lỗi) →
nhánh ngoại lệ trong `UC` + `AC` · `VR` (quy tắc kiểm tra dữ liệu) → `BR` · `R` (rủi ro) → mục rủi ro trong
`05-01`.

**Chọn "Thêm" khi prefix cũ mang một loại thông tin bộ này chưa có chỗ chứa** — đừng nhồi nó vào một prefix
gần gần, vì như thế là mất một tầng thông tin mà không ai biết.

### 3.3 Bảng ánh xạ từng mã — bắt buộc nếu mục 3.2 có dòng "Đổi"

| Mã cũ | Mã mới | Ghi chú |
| --- | --- | --- |
| `WF-017` | `SCR-017` | |

Ánh xạ prefix là **không đủ**. Sáu tháng sau sẽ có người tra `WF-017` trong ticket cũ và cần biết nó thành gì.

`DEC` ghi lại quyết định hệ mã: `DEC-___`

## 4. Mâu thuẫn tìm được trong hồ sơ cũ — bước không được bỏ

Bộ tài liệu đã qua nhiều bản thường có phần được viết lại và phần **không ai cập nhật theo**. Nạp mà không
phát hiện thì mâu thuẫn được sao chép nguyên vẹn — và từ đó nó trông chính danh vì đã qua cổng.

Bốn phép soi, làm theo thứ tự:

| # | Phép soi | Đã làm | Tìm thấy gì |
| --- | --- | --- | --- |
| 1 | Section nào ghi *"viết lại ở bản vX"* → mọi section **không** viết lại là nghi phạm | | |
| 2 | Định vị sản phẩm hiện tại **so với** persona và nhu cầu người dùng | | |
| 3 | Bảng bằng chứng **so với** các kết luận — số nào bị đánh dấu sai mà vẫn dùng như số thật | | |
| 4 | Các con số tổng ở phần tóm tắt **so với** phần chi tiết | | |

| # | Mâu thuẫn | Vị trí A | Vị trí B | Bên nào đúng | Xử lý |
| --- | --- | --- | --- | --- | --- |
| 1 | | file + mục | file + mục | A / B / **chưa biết** | lấp theo bên đúng / `OQ` + hoãn lấp |

**Chưa biết bên nào đúng thì ghi `OQ` vào `docs/_OPEN_QUESTIONS.md` và KHÔNG lấp phần đó** cho tới khi người
dùng chốt. Chọn bừa một bên rồi lấp là biến một câu hỏi mở thành một sự thật giả.

Không tìm thấy gì thì ghi thẳng *"đã soi bốn phép, không thấy mâu thuẫn"* — để trống trông giống hệt chưa làm.

## 5. Không lấp được, phải làm mới

| Tài liệu | Vì sao không lấp được | Kế hoạch |
| --- | --- | --- |
| `03-05` Khả thi công nghệ | Dev chưa phán quyết theo khuôn này | gửi `TECH-00`, chờ Dev |
| `04-03`…`04-06` Persona, hành trình | không còn bản ghi phỏng vấn | ghi **proto-persona**, hoặc chạy lại phase 04 |
| `12-00` Nghiên cứu UI | hồ sơ cũ chọn phong cách không có tài liệu lý do | cần `research-raw/moodboard/` |
| `08-02` mục 1b Trạng thái theo ngữ cảnh | bộ cũ gần như không bao giờ có trục này | điền mới |
| `05-01` Danh sách không được cắt | bộ cũ không có khái niệm này | điền mới |

## 6. Quyết định về cổng

Hồ sơ cũ **không kế thừa** cổng. Với mỗi cổng, chọn một — rồi ghi vào `docs/_INDEX.md` mục 6.

| Cổng | Lựa chọn | Lý do | **Rủi ro kèm theo nếu bỏ** |
| --- | --- | --- | --- |
| `G0` | Chạy thật / Bỏ có ý thức / Chạy lại phase | | |
| `G1` | | | |
| `G2` | | | |
| `G3` | | | |
| `G4` | | | |
| `G5` | | | |
| `G6` | | | |
| `G7` | | | |

**Cột cuối là cột đừng bỏ trống.** Bỏ `G3` nghĩa là tầng người dùng của dự án này không có bằng chứng — đó là
một rủi ro thật, và người đọc tài liệu sáu tháng sau cần biết.

## 7. Nghiệm thu việc nạp

| Kiểm | Đạt khi |
| --- | --- |
| File cũ còn nguyên trong thư mục này | không sửa, không xoá, không đổi tên |
| Không file cũ nào bị dán vào `docs/` | `docs/` chỉ chứa tài liệu theo template của bộ này |
| Mục 2 điền **đủ mọi dòng** của `_INDEX` | kể cả dòng *Không có* |
| Mục 3 chốt xong, `_ID_REGISTRY` đã cập nhật | và có `DEC` |
| Mục 4 có nội dung hoặc câu *"đã soi bốn phép, không thấy"* | |
| Mục 6 điền đủ, cột rủi ro không trống | |
| `validate_docs.py` **không còn cảnh báo prefix lạ** | mã cũ đã xử hết |
| Không tài liệu nào `approved` mà chưa qua cổng hoặc chưa ghi bỏ cổng | |
