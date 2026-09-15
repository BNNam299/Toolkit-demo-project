<!-- PROVENANCE — do build script sinh, KHÔNG sửa tay
nguồn      : ux-usability-evaluator.skill  →  references/usability-framework.md
nhập ngày  : 2026-08-09
trạng thái : chép nguyên văn, không tóm tắt, không diễn giải
cập nhật   : xuất lại file .skill từ Claude rồi chạy lại build script
-->

# Usability Framework — 5 thành phần, tiêu chí con & ví dụ chấm mẫu

Định nghĩa: **Usability = khả năng, mức độ sử dụng sản phẩm để đạt mục tiêu do con người quy định trong một bối cảnh cụ thể.** Lấy người dùng làm trung tâm. UX = LOOK + FEEL + USABILITY.

## 1. Learnability — Dễ dùng (lần đầu sử dụng)

- **Khả năng dự đoán**: user xác định được kết quả của hành động trong tương lai; **đã dự đoán thì phải đúng, đã hành động thì phải ra kết quả đã đoán**. Nút bấm không có gì xảy ra = phá dự đoán = thất vọng.
- **Khả năng nhận biết**: nhìn thấy và hiểu được dễ dàng; không phân biệt được đối tượng (nút lẫn trong text) thì không thể dự đoán.
- **Tương tác ẩn**: cho phép khi dựa trên **kinh nghiệm sử dụng trước đó** của user (thẻ flashcard bấm vào tự lật — ai từng học lật thẻ sẽ đoán được); tương tác ẩn không có nền kinh nghiệm = lỗi nhận biết.

## 2. Efficiency — Hiệu suất (sau khi đã biết dùng)

Rút ngắn thời gian thực hiện nhiệm vụ. 4 tiêu chí:
- **Điều hướng**: bản đồ di chuyển giữa các phần; đường đi rõ, dấu hiệu rõ, cung cấp đường ngắn nhất. Liên quan trực tiếp **kiến trúc thông tin**.
- **Điều khiển**: user kiểm soát được nội dung (cá nhân hóa) — hiển thị giao diện theo ý muốn, playlist/yêu thích.
- **Phản hồi**: rõ ràng, nhất quán, nhanh, liên tục — xong bước 1 phải biết ngay thành công/lỗi để sang bước 2.
- **Hệ thống thông minh**: tiện ích giảm thao tác — gợi ý từ khóa khi gõ, sửa chính tả, autofill.

## 3. Memorability — Ghi nhớ (quay lại sau thời gian dài)

- **Sự quen thuộc**: ngôn ngữ/biểu tượng quen thuộc; chỉ tạo nhận dạng mới khi mang nghĩa đặc thù. User không nhớ nổi biểu tượng mới chỉ dùng một lần → trang đầu để icon kèm chú thích, các trang sau mới bỏ chú thích.
- **Tính nhất quán**: thống nhất trong toàn hệ thống (hệ ký hiệu, mức độ, thuật ngữ).

## 4. Errors — Lỗi

Tính đến các trường hợp user mắc lỗi + phân tích mức nghiêm trọng:
| Mức | Định nghĩa | Ví dụ gốc |
|---|---|---|
| **Không nghiêm trọng** | User tự sửa được | Tìm thanh long ở mục ôn đới không thấy → back lại chọn nhiệt đới |
| **Trung tính** | Không để lại hậu quả lớn nhưng gây phiền | Quên đổi địa chỉ Shopee → hủy đơn đặt lại (và có thể mất đơn sang bên khác) |
| **Nghiêm trọng** | Kết quả xấu | Thoát không lưu, xóa nhầm file |

3 cơ chế bắt buộc kiểm tra:
- **Cảnh báo** — báo nguy cơ trước hành động rủi ro ("thoát mà không lưu?").
- **Tự bảo vệ** — hệ thống tự cứu: auto-save khi sập nguồn; chặn mở file chưa quét virus.
- **Khả năng phục hồi** — sửa được sai lầm: thùng rác giữ 15-30 ngày, khôi phục được.

## 5. Satisfaction — Thỏa mãn (CẦN người dùng thật)

- **Tính linh hoạt**: nhiều cách làm việc cho trình độ/kinh nghiệm/mối quan tâm khác nhau; thiết kế phù hợp từng nền tảng (desktop/mobile); người mới khác người lâu năm.
- **Phong cách thiết kế**: thể hiện phong cách, hấp dẫn đúng đối tượng mục tiêu.
- Tương tác thân thiện, **tránh thay đổi đột ngột** gây gián đoạn.

> Chế độ chuyên gia chấm 4 thành phần đầu; Satisfaction đánh giá qua người dùng thật (câu hỏi sau phiên test, thang điểm, NPS/CSAT).

## Thang điểm 0-4

4 = OK không sửa · 3 = chưa tốt lắm, sửa hoặc không · 2 = khá nghiêm trọng, cần sửa · 1 = rất nghiêm trọng, bắt buộc sửa sớm · 0 = bắt buộc sửa nếu không user không dùng được.

## Ví dụ chấm mẫu (case MyTV — giữ làm chuẩn giọng văn báo cáo)

Kịch bản trước: Who/When/Why/How. Sau đó:

- Poster chuyển động khiến icon lúc thấy lúc không → **lỗi nhận biết (2đ)**.
- Icon không rõ nghĩa với một số user → **lỗi dự đoán (3đ)**.
- Poster bóp méo, text không đủ — giảm hiệu quả truyền thông điệp dù có text dưới → **lỗi nhận biết (3đ)**.
- Bấm "Tất cả" của *Phim đề xuất* lại nhảy sang mục *Phim lẻ* → dự đoán sai hoàn toàn, điều hướng sai → **lỗi dự đoán + điều hướng (0đ)**.
- "Tất cả" của *Kênh đề xuất* ra *tất cả các kênh* thay vì kênh của tôi → **lỗi dự đoán (1đ)**.
- "Tất cả" của Tin tức mở trong trang chủ nhưng không có nút back → **lỗi điều hướng**.
- Đề xuất không cá nhân hóa → đặt câu hỏi thiết kế: *mục đề xuất tạo ra với mục đích gì khi không biết nhu cầu người dùng?* → **lỗi điều khiển (3đ)**; khắc phục: hỏi sở thích khi onboarding, playlist/yêu thích, kênh hiển thị chương trình đang phát trực tiếp (chạm cả "hệ thống thông minh").
- Search chỉ tìm được phim, không tìm kênh/nhạc → **lỗi dự đoán**; gõ text không gợi ý → **lỗi hệ thống thông minh**.
- Icon điều khiển ít gặp, chưa hiểu được → **lỗi ghi nhớ (3đ)**; icon chưa đồng nhất → **lỗi nhất quán**.
- Gõ search dừng một chút thì bàn phím tự mất → **lỗi ứng dụng** (Errors).

Cấu trúc mỗi finding: *vị trí → hiện tượng → kỳ vọng của user (dự đoán) → tiêu chí vi phạm → điểm → giải pháp*. Kết mỗi thành phần bằng đoạn "Từ những lỗi trên, giải pháp:" gộp các fix liên quan.

## User testing (chế độ B) — checklist vận hành

1. **Thời điểm**: trước khi thiết kế / khi có wireframe hoặc lo-fi prototype / trước launch rộng / sau launch.
2. **Tuyển**: người dùng thực sự đúng persona (persona = tiêu chí tuyển — đúng vai trò của persona trong giai đoạn Test).
3. **Kịch bản task**: từ Who-When-Why-How; task diễn đạt theo mục tiêu ("hãy tìm và xem một bộ phim bạn thích") chứ không theo đường đi ("bấm vào tab Phim truyện").
4. **Moderate**: hạn chế chỉ dẫn mang tính định hướng; quan sát + ghi chép (thời gian, lỗi, chỗ khựng, lời than).
5. **Nhiều người tham gia** để có dữ liệu phân tích; đo hiệu quả bằng chính 5 tiêu chí.
6. **Satisfaction**: hỏi sau phiên (thang điểm/Likert; CSAT/NPS nếu cần số liệu chuỗi).
7. Tổng hợp về cùng format thang 0-4 để merge với đánh giá chuyên gia.
