# tech-input — Dev nộp tài liệu kỹ thuật vào đây

Thư mục này là **tài sản của Dev**. PO và AI không viết, không sửa nội dung trong đây.

## Nguyên tắc thứ tự — đọc trước

**Nghiên cứu công nghệ diễn ra TRƯỚC khi chốt có phát triển sản phẩm, không phải sau khi viết xong PRD.**

Nếu một năng lực cốt lõi không làm được thì dự án dừng ở cổng **G2**, tức là ngay sau phase 03 — trước khi
tiêu phase 04 nghiên cứu người dùng và phase 05 viết PRD. Vì thế `TECH-00` là biểu mẫu cần sớm nhất và
quan trọng nhất trong thư mục này.

Sau khi công nghệ được chốt là khả thi, PRD mới hoàn thiện dần, và Dev điền tiếp các phần technical
theo bảng dưới.

## Cách dùng

1. Dev điền file tương ứng, ghi `version` và `ngày` ở đầu file, đổi `status` thành `đã nộp`.
2. PO yêu cầu AI: *"Đọc `tech-input/TECH-0X_*.md`, liệt kê nội dung sẽ điền vào đâu và liệt kê
   mâu thuẫn với tài liệu sản phẩm. Chưa sửa gì."*
3. AI báo cáo. PO duyệt.
4. AI cập nhật, ghi rõ nguồn file và ngày nhận vào từng chỗ đã điền.

## Bảng hợp đồng

| File | Nội dung tối thiểu | Điền vào đâu | Cần trước |
|---|---|---|---|
| `TECH-00_FEASIBILITY_SCREEN.md` | Với từng `CAP`: khả thi / khả thi có điều kiện / không khả thi, mức đạt được thực tế, chi phí, rủi ro, phương án thay thế | `03-05_TECH_FEASIBILITY_BRIEF` mục 5 — **là căn cứ quyết định đi tiếp hay dừng** | **cổng G2** · cuối phase 03 |
| `TECH-01_ARCHITECTURE.md` | Thành phần, cái gì chạy trên máy / gọi ra ngoài, luồng dữ liệu chính | `05-03_PROJECT_OVERVIEW` §Kiến trúc | cuối phase 05 |
| `TECH-04_PLATFORM_CONSTRAINTS.md` | OS thấp nhất, ngưỡng hiệu năng khả thi, giới hạn quyền, ràng buộc store | `06-03_NON_FUNCTIONAL_REQUIREMENTS` | phase 06 |
| `TECH-02_API_CONTRACT.md` | Endpoint, input/output, mã lỗi, thời gian phản hồi, rate limit, chi phí | `06-02_FUNCTIONAL_REQUIREMENTS` (dependencies) · `08-03_WIREFLOWS` (map mã lỗi → trạng thái UI) | phase 06 |
| `TECH-03_DATA_MODEL.md` | Thực thể, thuộc tính, quan hệ, nơi lưu, thời hạn, hành vi khi xoá | `06-02_FUNCTIONAL_REQUIREMENTS` · `06-05_PERMISSION_AND_DATA_NEEDS` | phase 06 |
| `TECH-05_FEASIBILITY_NOTES.md` | Với từng `FEAT` rồi từng `FR`: khả thi / khó, tốn công / không khả thi, lý do, phương án thay thế | `06-00_FEATURE_BRIEF_FOR_DEV` mục 2 → sau đó `06-02_FUNCTIONAL_REQUIREMENTS` | vòng thô: ngay sau `06-00` · vòng mịn: trong phase 06 |
| `TECH-06_ESTIMATE.md` | Ước lượng theo `FR` hoặc theo phase, ba con số, giả định | `13-01_HANDOVER_PACKAGE` | phase 13 |

## Hai vòng khả thi, đừng lẫn

| | `TECH-00` | `TECH-05` |
| --- | --- | --- |
| Đơn vị xét | `CAP` — năng lực | `FEAT` rồi `FR` — tính năng và yêu cầu |
| Câu hỏi | *có làm được không* | *làm mất bao nhiêu, đánh đổi gì* |
| Thời điểm | cuối phase 03, trước cổng G2 | ngay sau `06-00`, rồi mịn dần trong phase 06 |
| Hệ quả nếu xấu | **dừng dự án** hoặc xoay concept | cắt tính năng hoặc hạ ngưỡng yêu cầu |

Đã có phán quyết ở `TECH-00` thì `TECH-05` **trích lại**, không đánh giá lại từ đầu.

## Ghi chú cho Dev

Câu hỏi không thuộc file nào thì trả lời trong `docs/13-handover/13-02_DEV_QUESTION_LOG.md` thay vì qua chat
— để không bị mất.

Nếu một yêu cầu sản phẩm **không khả thi** hoặc tốn công gấp nhiều lần vẻ ngoài của nó, nói càng sớm càng tốt.
Biết ở phase 03 rẻ hơn phase 06, và phase 06 rẻ hơn phase 12 rất nhiều.

Nếu một việc **dễ hơn** PO tưởng, cũng nói — nó có thể mở ra phạm vi tốt hơn mà PO đang tự loại vì nghĩ là khó.
