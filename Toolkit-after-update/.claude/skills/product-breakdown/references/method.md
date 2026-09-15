# Phương pháp — Phân rã yêu cầu

> Skill viết mới. Pipeline v2 mục 4 gọi đây là **khoảng trống lớn nhất**: không skill nào trong bộ 11 sở hữu
> khâu Use Case → Functional Requirement.

Phase này biến danh sách tính năng thành thứ Dev có thể xây và QA có thể nghiệm thu. Đây là chỗ mơ hồ chết
người nhất trong cả chuỗi: PRD nói *"app cho phép chụp ảnh món ăn"*, Dev cần biết chụp bằng camera nào, ảnh mờ
thì sao, không có mạng thì sao, nhận sai thì người dùng sửa kiểu gì.

---

## Bước 1 — FEAT → Use Case (06-01)

Mỗi `FEAT` trong PRD phải sinh ra ít nhất một `UC`. Không có UC nghĩa là tính năng đó chưa ai nghĩ đến việc
người dùng thật sự làm gì với nó.

Use case mô tả **người dùng làm gì**, không mô tả hệ thống làm gì. Viết từ góc nhìn người dùng, dùng từ ngữ
của họ, không dùng từ kỹ thuật.

Mỗi UC gồm: ID và tên · actor · tiền điều kiện · kích hoạt · **luồng chính** đánh số từng bước · **luồng thay
thế** · **luồng ngoại lệ** · hậu điều kiện · FEAT liên quan.

Hai luồng sau cùng là chỗ hay bị bỏ, và cũng là chỗ đắt nhất khi phát hiện muộn. Với mỗi bước trong luồng
chính, hỏi: bước này hỏng được không, và hỏng thì người dùng đi đâu?

**Kiểm tra:** UC nào chỉ có luồng chính, không có nhánh nào, thì gần như chắc chắn viết chưa xong.

---

## Bước 2 — UC → Functional Requirement (06-02)

FR mô tả **hệ thống phải làm gì**. Một UC thường sinh ra nhiều FR.

Mỗi FR gồm: ID · phát biểu · UC nguồn · mức ưu tiên · **acceptance criteria** · phụ thuộc.

### Acceptance criteria phải đo được

Đây là quy tắc không thương lượng: **không hành vi nào không có acceptance criteria**.

AC viết theo Given / When / Then, hoặc dạng checklist có thể tick. Điều kiện là người khác đọc xong phải trả
lời được câu *"cái này đạt hay không đạt"* mà không cần hỏi lại bạn.

Những từ **không được** xuất hiện trong AC vì không đo được: nhanh, mượt, dễ dùng, trực quan, đẹp, hợp lý,
đầy đủ, tối ưu. Thay bằng số hoặc bằng mô tả hành vi cụ thể.

Sai: *"Kết quả hiển thị nhanh."*
Đúng: *"Given ảnh đã chụp xong, When người dùng bấm Phân tích, Then màn hình kết quả hiển thị trong vòng 3
giây trên thiết bị tham chiếu; nếu quá 3 giây thì hiện trạng thái đang xử lý kèm nút Huỷ."*

### Mỗi FR phải trả lời được năm câu

Nó giải quyết vấn đề gì · dành cho ai · trong bối cảnh nào · người dùng nhận được giá trị gì · đo hiệu quả
bằng cách nào. Không trả lời được câu nào thì FR đó đáng nghi.

---

## Bước 3 — Non-Functional Requirements (06-03)

NFR là ngưỡng chất lượng. Mỗi NFR **phải có số và điều kiện đo**, nếu không nó chỉ là lời chúc.

Sáu nhóm cần phủ: **hiệu năng** (thời gian khởi động, thời gian phản hồi, kích thước app) · **độ tin cậy**
(hành vi khi mất mạng, khi bị kill, khi hết dung lượng) · **tiếp cận** (tương phản, vùng chạm, cỡ chữ hệ thống
phóng to, trình đọc màn hình) · **tương thích** (phiên bản OS thấp nhất, thiết bị tham chiếu) · **bảo mật và
riêng tư** (dữ liệu nào lưu ở đâu, mã hoá gì, giữ bao lâu) · **vận hành** (crash rate, khả năng theo dõi lỗi).

Với mỗi ngưỡng, ghi rõ **đo trên thiết bị nào, trong điều kiện nào**. "Dưới 2 giây" là vô nghĩa nếu không nói
trên máy nào và mạng nào.

**Ngưỡng nào chưa xác nhận được thì gắn `[ASM]` và tạo `DQ` cho Dev.** Đừng bịa con số nghe hợp lý.

---

## Bước 4 — Business Rules (06-04)

Business rule là logic nghiệp vụ tồn tại độc lập với giao diện. Đây là nơi duy nhất được định nghĩa công thức.

Mỗi BR gồm: phát biểu · **công thức** · **ít nhất một ví dụ tính tay** · **các trường hợp biên** · điều gì xảy
ra khi vi phạm · FR nào áp dụng.

Ví dụ tính tay là bắt buộc. Công thức không có ví dụ thì mỗi người hiểu một kiểu.

Trường hợp biên hay bị quên: giá trị bằng 0, giá trị âm, đúng ngưỡng, vượt ngưỡng một đơn vị, reset theo thời
gian thì reset lúc mấy giờ theo múi giờ nào, phần dư có cộng dồn không, người dùng đổi múi giờ giữa chừng.

---

## Bước 5 — Permission & Data Needs (06-05)

Với mỗi quyền hệ thống cần xin: **vì sao cần** · **xin vào lúc nào trong luồng** · màn hình giải thích trước
khi xin · hành vi khi người dùng **đồng ý** · hành vi khi **từ chối** · hành vi khi **từ chối vĩnh viễn** ·
FR nào phụ thuộc quyền này.

Nhánh từ chối vĩnh viễn hay bị bỏ nhất. Trên di động, khi người dùng đã từ chối vĩnh viễn thì app **không thể
hỏi lại**, chỉ có thể hướng dẫn mở cài đặt hệ thống. Mọi FR liên quan quyền phải có nhánh này.

Với dữ liệu: thu thập gì · vì sao · lưu ở đâu · giữ bao lâu · người dùng xoá được không · đổi thiết bị thì sao.

---

## Bước 6 — Kiểm mồ côi trước cổng G5

Bốn phép kiểm bắt buộc:

- Mọi `FEAT` có ít nhất một `UC` chưa?
- Mọi `UC` có ít nhất một `FR` chưa?
- Mọi `FR` có `AC` đo được chưa? (quét các từ cấm: nhanh, mượt, dễ dùng…)
- Mọi `BR` có công thức kèm ví dụ chưa?

Bất kỳ câu nào trả lời không thì G5 không đóng.

---

## Ranh giới với Dev — nhắc lại vì phase này dễ vượt nhất

Phase này viết **cái gì** và **nghiệm thu thế nào**. Không viết **làm thế nào**.

Không được xuất hiện ở đây: sơ đồ kiến trúc, endpoint, tên bảng, schema, tên thư viện, mô hình dữ liệu chi tiết.
Những thứ đó Dev viết và nộp vào `tech-input/`. Khi cần một thông tin kỹ thuật để viết tiếp, gắn `[ASM]` và
tạo `DQ`, không tự đoán rồi trình bày như đã chốt.
