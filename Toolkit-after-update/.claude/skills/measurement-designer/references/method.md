# Phương pháp — Đo lường

> Skill viết mới. Pipeline v2 mục 4 xác định KPI, event taxonomy và funnel là khoảng trống không skill nào
> trong bộ 11 phụ trách.

Phase này tồn tại để tránh hai thất bại rất phổ biến: phát hành xong mới phát hiện không đo được điều mình
quan tâm, và bắn hàng trăm event mà không event nào trả lời được câu hỏi kinh doanh nào.

---

## Quy tắc thứ tự — KPI trước event

**Không định nghĩa event nếu chưa biết nó phục vụ chỉ số nào.** Vi phạm quy tắc này là sai chuẩn.

Làm ngược lại — liệt kê event trước rồi mới nghĩ đo gì — luôn dẫn tới một danh sách event dài, tốn công cài đặt,
mà vẫn không trả lời được câu hỏi quan trọng nhất.

---

## Bước 1 — KPI Framework (10-01)

### Ba tầng

**North Star.** Đúng một chỉ số, phản ánh giá trị người dùng thật sự nhận được, không phải hoạt động bề mặt.
Nếu chỉ số này tăng mà người dùng không được lợi gì hơn thì bạn chọn sai.

**Input metrics.** Ba đến năm chỉ số mà đội ngũ tác động trực tiếp được, và cộng lại thì đẩy North Star.

**Guardrail metrics.** Chỉ số không được xấu đi khi tối ưu các chỉ số trên. Ví dụ: tăng tỷ lệ mua nhưng tỷ lệ
hoàn tiền và tỷ lệ gỡ app không được tăng. Thiếu guardrail thì tối ưu ngắn hạn sẽ phá dài hạn.

### Mỗi KPI phải có đủ bảy trường

ID · tên · **định nghĩa bằng lời** · **công thức** (tử số, mẫu số, cửa sổ thời gian) · nguồn dữ liệu · tần suất
đo · **baseline** và **target**.

Baseline chưa có thì ghi `[ASM]` kèm cơ sở ước lượng, và ghi rõ sẽ thay bằng số thật sau khi phát hành. Không
bịa con số nghe hợp lý.

### Chống vanity metric

Với mỗi KPI, hỏi: *"nếu chỉ số này tăng gấp đôi mà không có gì khác thay đổi, doanh nghiệp có tốt hơn không?"*
Trả lời không thì đó là vanity metric. Tổng lượt tải, tổng lượt xem màn hình, tổng số tài khoản là những ví dụ
kinh điển.

---

## Bước 2 — Event Taxonomy (10-02)

### Quy ước đặt tên

`<đối_tượng>_<hành_động>`, snake_case, động từ ở **thì quá khứ** — event ghi lại việc đã xảy ra.

Đúng: `paywall_viewed`, `trial_started`, `scan_completed`, `free_limit_reached`
Sai: `viewPaywall`, `user_clicks_button`, `Paywall View`, `startTrial`

Tên event một khi đã phát hành thì **không đổi**. Đổi tên làm gãy toàn bộ dữ liệu lịch sử. Cần đổi thì tạo
event mới và cho event cũ trạng thái `deprecated`.

### Mỗi event phải có đủ sáu trường

ID · tên event · **khi nào bắn** (mô tả chính xác thời điểm, không mơ hồ) · **thuộc tính** kèm kiểu dữ liệu và
giá trị hợp lệ · **KPI hoặc bước phễu mà nó phục vụ** · màn hình `SCR` liên quan.

Trường thứ năm là bộ lọc quan trọng nhất. Event không phục vụ KPI hay bước phễu nào thì **xoá đi**, đừng cài.

### Thuộc tính

Chỉ thu thập thuộc tính thật sự cần cho phân tích đã dự kiến. Mỗi thuộc tính là một khoản nợ về quyền riêng tư
và một chỗ có thể sai. Không thu thập dữ liệu cá nhân ngoài danh sách đã duyệt ở `06-05`.

### Không quên nhóm event dễ sót

Trạng thái lỗi và hành vi phục hồi · từ chối quyền · mất mạng · chạm ngưỡng giới hạn free · các kết cục giao
dịch ngoài thành công và thất bại.

---

## Bước 3 — Funnel Definition (10-03)

### Phễu chính

Định nghĩa từng bước bằng **event cụ thể**, không bằng mô tả. Mỗi bước ghi: tên · event đánh dấu · điều kiện ·
tỷ lệ chuyển đổi kỳ vọng.

Phễu điển hình của app subscription: cài đặt → mở lần đầu → xong onboarding → **chạm aha moment** → xem paywall
→ bắt đầu trial → chuyển thành trả tiền → giữ được sau kỳ đầu.

### Activation

Định nghĩa activation bằng **hành vi**, không bằng thời gian. Không phải "dùng trong 7 ngày" mà là "hoàn thành
hành động cốt lõi ít nhất N lần trong M ngày đầu". Aha moment lấy từ `04-06_CUSTOMER_JOURNEY.md`, đừng định
nghĩa lại ở đây.

### Retention

Ghi rõ đang dùng loại nào — retention theo ngày mốc (D1/D7/D30) hay theo khoảng — vì hai cách cho ra con số
khác nhau và hay bị so sánh nhầm. Định nghĩa thế nào là "còn hoạt động".

---

## Kiểm chéo trước cổng G8

- Mọi KPI **tính được** từ ít nhất một event đã định nghĩa chưa?
- Mọi event **phục vụ** ít nhất một KPI hoặc bước phễu chưa?
- Mọi bước phễu có event đánh dấu chưa?
- Đủ **các trạng thái giao dịch** chưa — không chỉ thành công và thất bại, mà cả đang chờ, huỷ giữa chừng,
  hoàn tiền, hết hạn, gia hạn thất bại, khôi phục mua hàng?
- Mỗi thí nghiệm có **target** và **kill rule** đặt trước chưa?

---

## Ranh giới

Phase này định nghĩa **đo cái gì** và **tên gọi là gì**. Không viết cách cài đặt, không chọn công cụ analytics,
không viết code tracking. Những thứ đó Dev quyết và nộp qua `tech-input/`.
