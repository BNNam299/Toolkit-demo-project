<!-- PROVENANCE — do build script sinh, KHÔNG sửa tay
nguồn      : ux-research-planner.skill  →  references/methods-catalog.md
nhập ngày  : 2026-08-09
trạng thái : chép nguyên văn, không tóm tắt, không diễn giải
cập nhật   : xuất lại file .skill từ Claude rồi chạy lại build script
-->

# Catalog Phương pháp & Khung phân loại

## Phân loại người dùng (6 nhóm)

1. Người tương tác **trực tiếp** với sản phẩm để đạt nhiệm vụ
2. Người **quản lý** trực tiếp người sử dụng khác (app phân quyền: quản lý xem nhân viên tương tác thế nào)
3. Người **nhận sản phẩm từ hệ thống** mà không dùng nó (được share kết quả, ảnh chụp màn hình)
4. Người **kiểm tra** hệ thống
5. Người **quyết định mua** dù không dùng (app trẻ em — bố mẹ trả tiền: vẫn phải quan tâm họ muốn gì)
6. Người đang dùng **sản phẩm cạnh tranh** (họ có đặc điểm gì? làm sao thu hút và giữ user khỏi bị lôi kéo ngược?)

**Mức độ quan trọng**: *Quan trọng* = dùng thường xuyên + trực tiếp (trẻ em trong ví dụ đồ chơi — thiết kế cho họ dù bố mẹ trả tiền) · *Bình thường* = thỉnh thoảng dùng / gián tiếp qua trung gian · *Không quan trọng/yếu* = đến vì quảng cáo/trend/giá, xóa app khi xong việc — không thiết kế quanh nhóm này.

## Phương pháp thu thập yêu cầu (giai đoạn đầu, Buổi 8)

| Phương pháp | Khi dùng | Đặc điểm chính |
|---|---|---|
| **Phỏng vấn** | Khai thác vấn đề chưa biết | Bắt buộc có kịch bản trước. Tốt nhất khi user đang dùng sản phẩm. Ít người, tốn thời gian. 3 loại câu hỏi: **mở** (không cấu trúc — để họ tự nói), **đóng** (có cấu trúc — option chọn), **bán cấu trúc** (kết hợp) |
| **Bảng hỏi** | Khi kế hoạch ĐÃ rõ, cần chứng minh suy nghĩ là đúng | KHÔNG dùng khi chưa biết vấn đề là gì. Phân phối số lượng lớn. Người trả lời không được gợi ý → câu hỏi phải cực rõ |
| **Nhóm mục tiêu** | Cần nhiều dữ liệu nhanh từ đúng tệp | Cần người dẫn dắt có nghệ thuật; khó tập trung người tham gia |
| **Quan sát tự nhiên** | Rèn luyện thường xuyên, tìm vấn đề thật | Nhạy bén, ít hỏi, luôn ghi sổ tay. Dữ liệu lớn, tốn thời gian |
| **Nghiên cứu tài liệu** | Không làm phiền user; có sẵn data cũ, review, hồ sơ | Chỉ mang tính **dự đoán** — chưa chạm user thật thì trải nghiệm chưa chắc hiệu quả |

## Nghiên cứu ĐỊNH LƯỢNG (Quantitative)

Đo lường bằng số & thống kê; kết quả **tập trung, hẹp**; giải thích/minh chứng cho điều đã tìm ra. Áp dụng cho hiện tượng quy đổi được bằng số (hài lòng, tần suất, nhân khẩu học).

- **Survey** — câu hỏi đóng. Kiểu đáp án: multiple choice, checkbox, rating scale, ranking, Yes/No, matrix, image choice, **Likert**. Mỗi câu tự hỏi: kết quả thu về giúp giải quyết gì? Tránh câu dẫn dắt.
- **A/B Testing** — thường sau khi release. Chỉ test **một yếu tố khác biệt** mỗi lần (vd wording CTA "Xem báo giá" vs "Tìm hiểu thêm"). Nhiều yếu tố cùng lúc → Multivariate Testing.
- **Five-second testing** — 5 giây nhìn design → hỏi ấn tượng. Đo first impression.
- **Eye-tracking** — cần công cụ chuyên dụng; ≥30 người cùng nhiệm vụ trên cùng giao diện thì xu hướng mới có ý nghĩa.
- **Web/App Analytics** — GA/Mixpanel/Hotjar. Trả lời: họ xem gì, click đâu, tính năng nào được dùng, đến từ đâu, rời ở đâu. Chỉ số hay lấy: Bounce Rate, Conversion Rate, Retention Rate, User Profile/Demographics, Search Behavior.
- **Nghiên cứu thứ cấp** — khai thác nghiên cứu có sẵn, không "tạo lại bánh xe".
- **Remote Usability Testing** — user làm task trong môi trường tự nhiên; đo tỷ lệ hoàn thành, thời gian; công cụ: UserTesting, Lookback, Maze.

## Nghiên cứu ĐỊNH TÍNH (Qualitative)

Không cần nhóm lớn; dữ liệu dạng chữ, **đa chiều và sâu sắc**; đào động lực sau hành vi (nhu cầu, thói quen, VHXH). Có thể **lượng hóa** (mã hóa thành số) khi cần thống kê.

- **Phỏng vấn chuyên sâu (In-depth)** — đề tài nhạy cảm (tài chính, sức khỏe sinh lý) → one-on-one; khách mời đặc biệt (khó gom lịch nhóm) → one-on-one.
- **Usability Testing** — user làm task, mình quan sát + ghi chép; **hạn chế chỉ dẫn mang tính định hướng**. Thời điểm dùng: trước khi thiết kế / khi có wireframe-lofi prototype / trước launch rộng / sau launch. (Chi tiết cách chạy: skill `ux-usability-evaluator`.)
- **Card Sorting** — tạo hoặc đánh giá Navigation/IA; ~5 users. **Mở** (tự đặt nhóm — sinh ý tưởng mới) / **Đóng** (nhóm định sẵn) / **Hybrid**.
- **Tree Testing** — đánh giá phân cấp & khả năng tìm kiếm. Chỉ đưa TÊN mục, user tìm vị trí item. Phiên ~20 phút, tối đa 10 nhiệm vụ. Chuẩn bị: xác định cấu trúc cây → tạo nhiệm vụ theo mục đích → test thử với đồng đội → chọn người tham gia → chạy thật.
- **Focus Group** — 6-10 người, giống nhau về nhân khẩu học ở khía cạnh liên quan.
- **Field Studies** — nghiên cứu tại thực địa.

## Cây quyết định chọn phương pháp

- Chưa biết vấn đề là gì → phỏng vấn mở / quan sát tự nhiên / field study. **Không dùng bảng hỏi.**
- Đã có giả thuyết, cần chứng minh trên diện rộng → survey đóng / analytics.
- Cần quyết định giữa 2 phương án cụ thể → A/B test (một yếu tố).
- Câu hỏi về IA/điều hướng → card sorting (tạo mới) / tree testing (đánh giá cấu trúc có sẵn).
- Câu hỏi "design này có dùng được không" → usability testing (định tính) hoặc remote UT (định lượng).
- Ấn tượng đầu / thẩm mỹ → five-second test.
- Ngân sách ~0 → nghiên cứu thứ cấp + tài liệu + analytics có sẵn, dán nhãn "dự đoán".

## Template research_plan.md

```markdown
# Kế hoạch UX Research — <tên dự án>
**Ngày**: · **Người thực hiện**: · **Liên kết PRD**: <link>

## 1. Mục đích nghiên cứu
- Câu hỏi cần trả lời:
- Đối tượng người dùng (B1): <nhóm nào, đặc điểm, nhóm nào quan trọng>
- Mục tiêu nghiên cứu (B2): <chức năng / nội dung / hành vi — hoặc: vấn đề bản cũ / cái mới>
- Loại yêu cầu cần làm rõ: [ ]chức năng [ ]dữ liệu [ ]môi trường [ ]kỹ năng user [ ]tâm lý

## 2. Phương thức
| Mục tiêu | Phương pháp | Vì sao chọn |
|---|---|---|

## 3. Người tham gia
- Tiêu chí tuyển: · Số lượng: · Incentive:

## 4. Địa điểm / kênh

## 5. Kịch bản
<script phỏng vấn / bảng hỏi / task list đính kèm>

## Kế hoạch phân tích & bàn giao
- Dữ liệu thô lưu tại: · Tổng hợp bằng: Affinity Diagram → chuyển ux-persona-journey
```
