# TECH-00 — Sàng lọc khả thi công nghệ

| Trường | Nội dung |
| --- | --- |
| Người điền | |
| Ngày | |
| Phiên bản | 0.1.0 |
| Trạng thái | chưa nộp / đã nộp |

> **Đây là biểu mẫu quan trọng nhất và cần sớm nhất trong cả thư mục này.**
>
> PO sẽ dùng file này để quyết định **có làm sản phẩm hay không**. Cổng G2 không đóng được khi còn `CAP`
> nào ở trạng thái *chưa trả lời*, và dự án sẽ **dừng** nếu một năng lực cốt lõi không khả thi.
>
> Nghĩa là: trả lời "không khả thi" ở đây không làm ai thất vọng — nó tiết kiệm cho cả team vài tháng.
> Điều gây thiệt hại là trả lời "được" cho êm chuyện rồi ba tháng sau mới nói lại.

## Cách dùng

Đọc `docs/03-opportunity/03-05_TECH_FEASIBILITY_BRIEF.md`, mục 2 (danh sách `CAP`), mục 3 (câu hỏi `DQ`)
và mục 4 (ràng buộc ngân sách, quyền riêng tư, mốc thời gian, nhân sự). Trả lời theo từng `CAP`.

Không cần chọn xong công nghệ. Chỉ cần trả lời: **làm được hay không, ở mức nào, tốn bao nhiêu, và đánh đổi gì.**

## 1. Phán quyết theo từng năng lực

Lặp khối này cho mỗi `CAP`.

### CAP-001 · [tên năng lực, chép từ 03-05]

| Trường | Nội dung |
| --- | --- |
| **Phán quyết** | KHẢ THI / KHẢ THI CÓ ĐIỀU KIỆN / KHÔNG KHẢ THI |
| Mức đạt được thực tế | ví dụ: nhận ra ~45% món phổ biến, không phải 60% như PO mong |
| Cách tiếp cận khả dĩ | mô tả ngắn, chưa cần chốt |
| Chạy trên máy hay cần mạng | |
| Dữ liệu có phải rời khỏi máy | |
| Chi phí hạ tầng dự kiến / tháng | |
| Công sức thô | ngày người, ba con số: lạc quan / thường / xấu |
| Điều kiện để KHẢ THI | ghi rõ nếu phán quyết là *có điều kiện* |
| Rủi ro lớn nhất | |
| Phương án thay thế nếu không khả thi | |
| Độ tự tin của tôi | cao / trung bình / thấp — và vì sao |

## 2. Trả lời câu hỏi DQ

| `DQ` | Trả lời | Có đạt ngưỡng PO nêu không | Ghi chú |
| --- | --- | --- | --- |
| `DQ-001` | | Có / Không / Đạt một phần | |

Câu hỏi nào **không trả lời được ở giai đoạn này** thì ghi rõ *"cần dựng thử mới biết"*, kèm ước lượng thời
gian dựng thử. Đừng đoán — PO đang dùng câu trả lời này để quyết định dừng hay đi.

## 3. Điều PO chưa hỏi mà cần biết

Phần giá trị nhất của biểu mẫu này thường nằm ở đây. PO không phải Dev nên sẽ không nghĩ tới:

| Điều PO chưa hỏi | Vì sao quan trọng | Ảnh hưởng tới quyết định thế nào |
| --- | --- | --- |
| | | |

Ví dụ những thứ hay bị bỏ sót: giới hạn của store, ràng buộc quyền riêng tư của nền tảng, chi phí tăng theo
số người dùng chứ không phải theo tính năng, ràng buộc phiên bản OS thấp nhất, hoặc một năng lực dễ hơn
nhiều so với PO tưởng — **cái này cũng phải nói**, vì nó có thể mở ra phạm vi tốt hơn.

## 4. Kết luận tổng

| Trường | Nội dung |
| --- | --- |
| Có `CAP` cốt lõi nào KHÔNG KHẢ THI không | Có / Không — nếu có, `CAP` nào |
| Khuyến nghị của tôi | đi tiếp / đi tiếp có điều kiện / xoay hướng / dừng |
| Điều tôi cần từ PO để chắc chắn hơn | |

Quyết định cuối là của PO. Phần của bạn là làm cho quyết định đó dựa trên sự thật.
