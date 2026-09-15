# Phương pháp — Bàn giao Dev

> Skill viết mới. Pipeline v2 mục 4 xác định đây là khoảng trống: gói bàn giao và hợp đồng tech-input.

Đây là phase cuối. Mục tiêu không phải gửi đi thật nhiều tài liệu, mà là để một Dev **chưa từng tham gia** đọc
xong biết phải làm gì, làm theo thứ tự nào, và điều gì còn chưa chốt.

---

## Bước 1 — Handover Package (13-01)

### Thứ tự đọc cho Dev mới

Đừng đưa 57 file rồi bảo đọc đi. Chỉ định rõ thứ tự và mục đích từng bước:

1. `05-03_PROJECT_OVERVIEW.md` — hiểu dự án trong 10 phút
2. `00-02_SCOPE_LOCK.md` — biết ranh giới và **danh sách bị cấm**
3. `_GLOSSARY.md` — dùng đúng từ ngay từ đầu
4. `06-02_FUNCTIONAL_REQUIREMENTS.md` + `06-03_NFR` — biết phải xây gì tới mức nào
5. `08-01_SCREEN_INVENTORY.md` + `08-02_STATE_MATRIX.md` — biết đủ số màn và trạng thái
6. `13-04_ACCEPTANCE_CRITERIA_PACK.md` — biết nghiệm thu thế nào
7. Còn lại tra khi cần

### Bảng mục lục gói bàn giao

Liệt kê mọi file có `in_handover: Có`, kèm doc_id, mục đích một dòng, và **phiên bản tại thời điểm bàn giao**.
Ghi phiên bản là quan trọng: ba tháng sau khi có tranh cãi, bạn cần biết Dev đã nhận bản nào.

### Ranh giới trách nhiệm

Ghi thành bảng rõ ràng, không để ngầm hiểu. PO sở hữu phạm vi, ưu tiên, giá, phê duyệt cuối. Designer sở hữu
giải pháp UX trong phạm vi đã duyệt. Dev sở hữu kiến trúc, khả thi kỹ thuật, và mọi thứ trong `tech-input/`.

Kèm một câu rõ ràng: **mọi thay đổi phạm vi đi qua `_CHANGE_LOG.md`, không thoả thuận miệng.**

### Điều chưa chốt

Liệt kê thẳng mọi `[ASM]` còn sống và mọi `DQ` chưa trả lời. Giấu chúng đi không làm chúng biến mất, chỉ làm
chúng nổ muộn hơn và đắt hơn.

---

## Bước 2 — Dev Question Log (13-02)

**Mở từ phase 03**, không phải tới phase 13 mới lập.

Mỗi khi bất kỳ phase nào cần một thông tin kỹ thuật mà chưa có, ghi một dòng vào đây thay vì đoán.

Mỗi `DQ` gồm: ID · câu hỏi · **ảnh hưởng tới tài liệu hoặc quyết định nào** · ai hỏi · ngày hỏi · trạng thái
(`mở` / `đã trả lời` / `không còn liên quan`) · câu trả lời · ngày trả lời · **tài liệu đã cập nhật theo**.

Trường "ảnh hưởng tới cái gì" quyết định mức ưu tiên. `DQ` chặn một FR quan trọng khác hẳn `DQ` chỉ ảnh hưởng
một chi tiết phụ.

**Cổng G11 không đóng nếu còn `DQ` mở đang chặn.**

---

## Bước 3 — Tech Input Contract (13-03)

Đây là hợp đồng hai chiều: Dev nộp gì, và AI được phép làm gì với thứ đã nộp.

### Bảy file Dev nộp

| File | Nội dung tối thiểu | Điền vào tài liệu nào | Cần trước phase |
| --- | --- | --- | --- |
| `TECH-00_FEASIBILITY_SCREEN` | Với từng **`CAP`**: khả thi / có điều kiện / không khả thi, mức đạt thực tế, chi phí, phương án thay thế | `03-05` mục 5 — **căn cứ quyết định đi tiếp hay dừng** | **trước cổng G2** |
| `TECH-01_ARCHITECTURE` | Thành phần, cái gì chạy trên máy / gọi ra ngoài, luồng dữ liệu | `05-03` Project Overview | 05 |
| `TECH-02_API_CONTRACT` | Endpoint, input/output, **mã lỗi → trạng thái UI**, thời gian phản hồi, quota | `06-02`, `08-02` | 06 |
| `TECH-03_DATA_MODEL` | Thực thể, quan hệ, nơi lưu, thời hạn, hành vi khi xoá và khi đổi thiết bị | `06-05`, `05-03` | 06 |
| `TECH-04_PLATFORM_CONSTRAINTS` | OS thấp nhất, thiết bị tham chiếu, **ngưỡng hiệu năng khả thi**, giới hạn quyền | `06-03` NFR | 06 |
| `TECH-05_FEASIBILITY_NOTES` | Vòng thô theo **`FEAT`**, rồi vòng mịn theo **`FR`**: khả thi / khó, tốn công / không khả thi, lý do, phương án thay thế | `06-00` mục 2, rồi `06-02` | 06, ngay sau `06-00` |
| `TECH-06_ESTIMATE` | Ước lượng ba con số, giả định, đường găng | `12-01` Roadmap, `13-01` | 12 |

**`TECH-00` là file có giá trị cao nhất và phải xin sớm nhất — nó là điều kiện đóng cổng G2.**

Nghiên cứu công nghệ đứng **trước** quyết định có phát triển sản phẩm, không phải sau khi viết xong PRD.
Nếu một năng lực cốt lõi không làm được thì dự án dừng ở cuối phase 03, trước khi tiêu phase 04 nghiên cứu
người dùng và phase 05 viết PRD. Chỉ khi công nghệ đã được chốt khả thi thì PRD mới hoàn thiện dần, và Dev
điền tiếp các phần technical qua `TECH-01` đến `TECH-06`.

Hai vòng khả thi, đơn vị xét khác nhau, đừng lẫn:

| | `TECH-00` | `TECH-05` |
| --- | --- | --- |
| Đơn vị | `CAP` — năng lực | `FEAT` rồi `FR` |
| Câu hỏi | *có làm được không* | *tốn bao nhiêu, đánh đổi gì* |
| Thời điểm | cuối phase 03, trước G2 | ngay sau `06-00`, rồi mịn dần trong phase 06 |
| Hệ quả nếu xấu | **dừng dự án** hoặc xoay concept | cắt tính năng hoặc hạ ngưỡng |

Đã có phán quyết ở `TECH-00` thì `TECH-05` trích lại, không đánh giá lại từ đầu.

Biết một yêu cầu không khả thi ở phase 03 rẻ hơn phase 06, và phase 06 rẻ hơn phase 12 rất nhiều.

### Quy trình khi Dev nộp

1. AI **đọc**, không sửa gì.
2. AI báo cáo: nội dung này sẽ điền vào section nào của tài liệu nào.
3. AI **liệt kê mâu thuẫn** giữa ràng buộc kỹ thuật và mong muốn sản phẩm. Đây là bước quan trọng nhất và
   không được bỏ — mâu thuẫn bị hoà tan vào văn bản là mâu thuẫn sẽ nổ lúc build.
4. PO duyệt.
5. AI cập nhật, ghi rõ **nguồn file và ngày nhận** vào từng chỗ đã điền.

**AI không bao giờ sửa nội dung trong `tech-input/`.** Đó là tài sản của Dev.

---

## Bước 4 — Acceptance Criteria Pack (13-04)

Gom toàn bộ `AC` từ `06-02` thành một bộ nghiệm thu dùng được, nhóm theo tính năng và theo phase triển khai.

Mỗi mục nghiệm thu gồm: ID · FR nguồn · điều kiện · các bước kiểm · kết quả mong đợi · màn hình và trạng thái
liên quan · dữ liệu cần chuẩn bị.

### Không quên nhóm dễ sót

Các trạng thái lỗi và đường phục hồi · từ chối quyền và **từ chối vĩnh viễn** · mất mạng giữa chừng · chạm
ngưỡng giới hạn free · **đủ các kết cục giao dịch** — thành công, thất bại, đang chờ, huỷ giữa chừng, hoàn tiền,
hết hạn, gia hạn thất bại, khôi phục mua hàng · phóng cỡ chữ hệ thống lên mức lớn nhất · chế độ tối.

### Kiểm cuối

Mọi `FR` có ít nhất một mục nghiệm thu chưa? FR không nghiệm thu được thì hoặc AC viết chưa đủ, hoặc FR đó
không nên tồn tại.

---

## Điều kiện đóng cổng G11

Mọi file bắt buộc có `status: approved` · không còn `DQ` mở đang chặn · bảng mục lục gói bàn giao có phiên bản
từng file · mọi `[ASM]` còn sống đã được liệt kê tường minh · ranh giới trách nhiệm đã ghi thành bảng.
