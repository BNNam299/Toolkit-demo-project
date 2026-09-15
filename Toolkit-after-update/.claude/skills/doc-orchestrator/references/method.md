# Phương pháp — Khởi tạo & điều phối tài liệu

> Skill viết mới. Pipeline v2 mục 4 xác định đây là một trong năm skill lấp khoảng trống mà bộ 11 UX skill
> không phủ. Nguồn: Pipeline v2 mục 7–11 và Chuẩn quản lý tài liệu mục 9–13.

Skill này có hai vai. Vai thứ nhất là viết hai tài liệu của phase 00. Vai thứ hai là **xuyên suốt**: mọi phiên
làm việc ở mọi phase đều bắt đầu và kết thúc bằng nó.

---

## Phần A — Project Brief (00-01)

Brief không phải bản mô tả ý tưởng. Nó là bản ghi những điều đã biết và những điều chưa biết, để phase sau
không phải đoán.

### Câu hỏi bắt buộc

Hỏi từng câu, không hỏi dồn. Câu nào người dùng chưa trả lời được thì ghi `[ASM]` kèm giả định tạm và đưa vào
`_ASSUMPTION_REGISTER.md`, đừng bỏ trống.

**Về vấn đề.** Ai đang gặp khó khăn gì? Họ đang xử lý nó bằng cách nào? Cách đó dở ở chỗ nào? Nếu không có
sản phẩm này thì chuyện gì xảy ra với họ?

**Về người dùng.** Ai sẽ mở app này nhiều lần một tuần? Họ mở trong hoàn cảnh nào — đang đứng, đang vội, đang
rảnh? Có ai trả tiền mà không phải người dùng không?

**Về ràng buộc.** Ngân sách và thời gian tới đâu? Ai làm — một mình, có Dev, có Designer? Có ràng buộc pháp lý
hay ngành nghề nào không?

**Về thành công.** Ba tháng sau khi phát hành, con số nào cho bạn biết đã thành công? Con số nào cho bạn biết
nên dừng?

**Về điều đã quyết trước.** Có gì đã chốt mà không thương lượng lại — nền tảng, mô hình kiếm tiền, thương hiệu?

### Điều không được làm ở brief

Không đề xuất tính năng. Không chọn công nghệ. Không viết luôn PRD. Brief chỉ ghi lại bối cảnh và ràng buộc.

---

## Phần B — Scope Lock (00-02)

Đây là tài liệu ngắn nhất và có sức mạnh lớn nhất trong cả bộ. Nó tồn tại để khi AI hoặc freelancer đề xuất
thêm backend, hệ thống tài khoản hay cloud sync, bạn có một file cụ thể để chỉ vào.

### Ba danh sách

**Trong phạm vi.** Những gì chắc chắn làm ở bản này.

**Ngoài phạm vi, đã cân nhắc.** Những gì đã nghĩ tới và **cố ý** không làm, kèm lý do. Đây là phần quan trọng
nhất — nó khác hoàn toàn với việc quên.

**Bị cấm.** Những gì không được đề xuất, không được thêm, kể cả khi nghe có vẻ hợp lý. Ví dụ: backend riêng,
đăng nhập tài khoản, đồng bộ đám mây, thu thập dữ liệu cá nhân ngoài danh sách đã duyệt.

**Danh sách bị cấm không được rỗng.** Cổng G0 không đóng nếu nó rỗng. Một dự án không cấm gì cả là một dự án
sẽ phình ra.

### Ai được mở khoá

Chỉ Product Owner. Và mở khoá phải đi qua `CHG` ở `_CHANGE_LOG.md`, không thoả thuận miệng.

---

## Phần C — Cấp và giữ ID

Mọi hạng mục có ID dạng `<PREFIX>-<ba chữ số>`. ID cấp tại đúng một tài liệu, ghi vào `_ID_REGISTRY.md`.

Ba quy tắc, vi phạm là hỏng truy nguyên: **không bao giờ đổi ID**, **không bao giờ tái sử dụng ID đã bỏ**,
**không bao giờ đánh số lại**. Hạng mục bị bỏ thì giữ ID ở trạng thái `archived`.

Khi cấp ID mới, ghi ngay vào registry cùng tài liệu cấp và ngày cấp. Đừng để tới cuối phase mới ghi.

---

## Phần D — Kiểm mồ côi

Chạy trước mỗi cổng. Chuỗi truy nguyên chuẩn:

```
PN/NC → GAP → CPT → INS → JTBD → PER → FEAT → UC → FR → FLOW → SCR → ST → CPY → EVT → KPI → AC
```

Mười hai loại mồ côi phải kiểm:

1. Pain point không dẫn tới concept nào
2. Concept không dựa trên pain point nào
3. Insight không dùng ở đâu
4. Persona không xuất hiện trong flow nào
5. **Tính năng không có use case**
6. **Use case không có requirement**
7. Requirement không có acceptance criteria
8. Flow tham chiếu SCR không tồn tại
9. **Màn hình không xuất hiện trong flow nào**
10. Trạng thái màn hình còn ô `?` trong state matrix
11. Chuỗi văn bản không gắn với màn hình nào, hoặc màn hình có chữ mà không có CPY
12. **Event không phục vụ KPI nào**, hoặc KPI không tính được từ event nào

Bốn loại in đậm là nghiêm trọng nhất. Báo cáo mồ côi ghi vào `_INDEX.md` mục 5.

Đọc ngược chuỗi để kiểm: *"cái này tồn tại để làm gì?"* Không trả lời được thì nó nên bị xoá, chứ không phải
được giữ lại cho chắc.

---

## Phần E — Ba quy tắc thứ tự

Vi phạm là sai chuẩn, không phải sở thích:

1. **Screen inventory trước wireframe.** Vẽ trước khi kiểm kê thì số màn luôn thiếu 40–60%, và thiếu đúng ở
   chỗ đắt nhất: trạng thái lỗi, empty, offline, hết lượt, các kết cục thanh toán.
2. **UX flow không được sinh màn hình mới.** Thiếu màn thì ghi vào `08-04_MISSING_SCREEN_REPORT.md`, rồi SCR
   được cấp ở `08-01`, rồi flow mới trích lại.
3. **KPI trước event.** Không định nghĩa event nếu chưa biết nó phục vụ chỉ số nào.

---

## Phần F — Change Impact Report

Khi một tài liệu đã `approved` mà cần đổi, **tuyệt đối không sửa file trước**. Sáu bước:

1. Cấp `CHG ID` ở `_CHANGE_LOG.md`
2. Viết Change Impact Report: đổi gì, vì sao, những tài liệu nào bị ảnh hưởng
3. Chờ Product Owner duyệt
4. Cập nhật theo đúng thứ tự lan truyền
5. Giữ ID cũ nếu logic chưa bị thay thế
6. Cập nhật `_INDEX.md` và tăng `version` từng file đã chạm

Thứ tự lan truyền:

```
00-01 Brief → 05-01 PRD → 06-01 UC → 06-02 FR → 06-04 BR
→ 07-05 FLOW → 08-01 SCR → 08-02 ST → 08-03 Wireframe
→ 09-06 Copy → 10-02 EVT → 13-04 AC → 12-01 Roadmap → _INDEX
```

**Ví dụ vì sao không được sửa lẻ.** Yêu cầu: *"người dùng free được scan ba lần mỗi ngày"*. Nếu chỉ sửa paywall,
dự án sẽ thiếu bảy thứ: quy tắc reset theo múi giờ nào (`06-04`), trạng thái đã hết lượt (`08-02`), chỗ hiển thị
còn mấy lượt (`08-01` và `09-06`), event `free_limit_reached` (`10-02`), ảnh hưởng tới phễu chuyển đổi (`10-03`),
ca nghiệm thu cho lượt thứ ba và thứ tư (`13-04`), và việc lượt còn lại có cộng dồn hay không (`06-04` lần nữa).

Change Impact Report tồn tại để buộc bảy chỗ đó lộ ra **trước** khi có người bắt đầu code.

---

## Phần G — Chọn profile

Chọn ở đầu dự án, ghi vào `_INDEX.md` mục 1.

**Lean** — phase 00 đến 03, khoảng 12 file. Dùng khi chưa quyết định có làm hay không. Viết PRD đầy đủ cho một
ý tưởng có thể bị bỏ trong hai tuần là lãng phí, và tệ hơn, nó tạo cảm giác cam kết khiến việc bỏ ý tưởng trở
nên khó về mặt tâm lý.

**MVP** — toàn bộ phase, bỏ các file `Có điều kiện`, khoảng 38 file. Mức mặc định.

**Full** — mọi file. Khi nhiều người tham gia hoặc sản phẩm đã qua MVP.

File bị loại khỏi profile thì **ghi lý do** vào `_INDEX.md`. Một tài liệu bị bỏ vì không cần khác hoàn toàn
một tài liệu bị quên.

---

## Phần H — Chạy cổng

Cổng có thể bỏ qua, nhưng phải bỏ **có ý thức**: ghi vào `_INDEX.md` mục 6 rằng cổng nào bị bỏ, vì sao, và
rủi ro kèm theo đã được ghi ở đâu.

Khi cổng fail, liệt kê chính xác mục nào thiếu và cần bổ sung gì. Không nói chung chung kiểu "cần chi tiết hơn".

---

## Phần I — Nguyên tắc quan trọng nhất

> **Một tài liệu một lượt.** Viết xong một file thì dừng, báo cáo, chờ xác nhận.
> Không chạy từ ý tưởng đến bàn giao trong một lượt.

Chậm hơn, nhưng sai sót được phát hiện khi nó còn ở một file thay vì đã lan xuống bảy file.
