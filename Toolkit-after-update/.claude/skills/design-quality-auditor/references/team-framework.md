<!-- PROVENANCE — do build script sinh, KHÔNG sửa tay
nguồn      : ux-design-review.skill  →  references/team-framework.md
nhập ngày  : 2026-08-09
trạng thái : chép nguyên văn, không tóm tắt, không diễn giải
cập nhật   : xuất lại file .skill từ Claude rồi chạy lại build script
-->

# Team Framework — PACT & 5 thành phần Usability (bản rút gọn để chấm trong audit)

Bản đầy đủ nằm ở skill `ux-engagement-designer` (PACT) và `ux-usability-evaluator` (5 thành phần + case mẫu MyTV). File này đủ để chạy pass trong một audit.

## PACT — khung dựng ngữ cảnh trước khi chấm (dùng trước khi redesign)

- **People**: ai dùng — khả năng và hạn chế của con người; con người là trung tâm mọi giai đoạn.
- **Activities** — 5 đặc điểm: (1) **Thời gian**: tần suất dùng chức năng (dùng nhiều → vị trí dễ thấy; ít → ẩn nhưng tìm được) · tính liên tục qua gián đoạn (auto-save, draft) · thời gian đáp ứng (**~100ms** cho thao tác tay-mắt, **>5s** = thất vọng bỏ đi); (2) **Hợp tác**: một người hay nhiều người tương tác, ai thấy gì của ai; (3) **Phức tạp**: đơn giản hóa nhiệm vụ phức tạp bằng cách tách bước; (4) **An toàn**: confirm trước hành động rủi ro, cơ chế bảo vệ; (5) **Bản chất nội dung**: loại dữ liệu (text/ghi âm/video/ảnh) và cách tương tác với từng loại.
- **Context**: tổ chức (quy định, phân quyền, cơ chế thưởng) · xã hội (cộng đồng định hình hành vi) · vật lý (ánh sáng, găng tay, khẩu trang → cân nhắc giọng nói).
- **Technology**: đầu vào (chạm, bàn phím, vân tay, mặt, giọng) · đầu ra (màn hình, loa) · nền tảng.

Dùng PACT ở bước Establish context: phán xét thiết kế phải đặt trong PACT của nó.

## 5 thành phần Usability + tiêu chí con (pass nội bộ)

Điều kiện tiên quyết: dựng **kịch bản sử dụng Who-When-Why-How** trước, chấm dựa trên kịch bản đó.

1. **Learnability** — *dự đoán* (đoán được kết quả hành động; đã đoán phải đúng) · *nhận biết* (nhìn thấy, hiểu được; nút không lẫn text). Tương tác ẩn chỉ hợp lệ khi dựa trên kinh nghiệm sẵn có của user.
2. **Efficiency** — *điều hướng* (đường đi rõ, ngắn nhất — dính IA) · *điều khiển* (cá nhân hóa, kiểm soát hiển thị) · *phản hồi* (rõ, nhất quán, nhanh, liên tục) · *hệ thống thông minh* (gợi ý, giảm thao tác).
3. **Memorability** — *quen thuộc* (ngôn ngữ/icon quen; icon mới kèm chú thích lần đầu) · *nhất quán* toàn hệ thống.
4. **Errors** — mức: *không nghiêm trọng* (tự sửa) / *trung tính* (phiền, không hậu quả lớn) / *nghiêm trọng* (mất dữ liệu). Ba cơ chế bắt buộc: **cảnh báo** · **tự bảo vệ** (auto-save, chặn nguy hiểm) · **phục hồi** (thùng rác, undo).
5. **Satisfaction** — *linh hoạt* (nhiều cách làm theo trình độ; responsive) · *phong cách đúng đối tượng* · tránh thay đổi đột ngột. **Chỉ đo được với user thật** → đánh dấu "cần user testing", route sang ux-usability-evaluator mode B.

## Thang 0-4 của team & ánh xạ severity

| Điểm team | Nghĩa | Severity quốc tế |
|---|---|---|
| 4 | OK, không phải sửa | — (strength) |
| 3 | Chưa tốt lắm, sửa hoặc không | Minor |
| 2 | Khá nghiêm trọng, cần sửa | Moderate |
| 1 | Rất nghiêm trọng, bắt buộc sửa sớm | Critical |
| 0 | Không sửa thì user không dùng được | Critical (blocker) |

Format finding của team: *vị trí → hiện tượng → kỳ vọng/dự đoán của user → tiêu chí vi phạm (có thể nhiều: "lỗi dự đoán + điều hướng") → điểm → giải pháp*. Kết mỗi thành phần bằng cụm "Từ những lỗi trên, giải pháp:". Lỗi lộ ra thiết kế thiếu mục đích thì giải pháp phải trả lời cả câu "chức năng này tạo ra để làm gì" (đề xuất không cá nhân hóa thì đề xuất để làm gì?).

## Khi báo cáo song song hai hệ

Một bảng findings duy nhất, hai cột điểm (0-4 team + severity). Vấn đề bị cả Nielsen/Shneiderman LẪN framework team gắn cờ → nâng ưu tiên lên ít nhất một bậc. Điểm 0-100 tổng của audit giữ nguyên cách tính scoring.md; điểm 0-4 áp cho từng finding, không quy đổi ngược thành tổng.
