# Kế hoạch thu hoạch — Claude điền, bạn duyệt

| Trường | Nội dung |
| --- | --- |
| Claude điền ngày | |
| Lĩnh vực / need zone | _lấy từ `00-01` và `00-02`_ |
| Phase đang phục vụ | 01 / 02 |
| Tài liệu sẽ viết từ dữ liệu này | `01-02` · `02-03` · … |
| Định mức | ≥50 dòng · ≥3 loại nguồn |
| Bạn duyệt kế hoạch này chưa | chưa / rồi |

> **Claude viết file này trước khi tạm dừng phiên.** Không dùng khuôn chung — lúc này Claude đã đọc brief
> dự án và danh sách bị cấm, nên phải đề xuất **nguồn cụ thể, cụm từ cụ thể, tên app cụ thể**.
>
> Bạn xem, sửa chỗ nào biết rõ hơn Claude, rồi mới mang sang công cụ đi đào.

## 1. Đào ở đâu, theo thứ tự nào

| # | Nguồn | Cụ thể là gì | Vì sao nguồn này | Vòng thứ mấy |
| --- | --- | --- | --- | --- |
| 1 | Review App Store | app nào, link nào | | vòng 1 |
| 2 | Review Google Play | | | vòng 1 |
| 3 | Reddit | subreddit nào | | vòng 2 |
| 4 | Diễn đàn / cộng đồng VN | | | vòng 2 |
| 5 | YouTube / TikTok comment | | | vòng 3 |

Chia vòng để mỗi lần dừng lại bạn soi được. Đừng dồn hết vào một vòng.

## 2. Cụm từ tìm đề xuất

| Cụm từ | Ngôn ngữ | Tìm ở nguồn nào | Vì sao cụm này |
| --- | --- | --- | --- |
| | vi / en | | |

Ưu tiên **ngôn ngữ người dùng thật**, không phải thuật ngữ sản phẩm. Người ta viết *"app cứ đơ khi chụp"*
chứ không viết *"hiệu năng camera kém"*.

## 3. Loại phàn nàn đang tìm

Ghi ra để công cụ đi đào biết cái gì là liên quan, cái gì bỏ qua.

| Đang tìm | Bỏ qua |
| --- | --- |
| | phàn nàn về giá của app khác lĩnh vực, spam, review một sao không nội dung |

## 4. Điều kiện dừng

| Điều kiện | Ngưỡng |
| --- | --- |
| Số dòng tối thiểu | 50 |
| Số loại nguồn tối thiểu | 3 |
| Dấu hiệu bão hoà | 2 vòng liên tiếp không ra loại phàn nàn mới |

## 5. Điều Claude chưa chắc, cần bạn xác nhận

| Điều chưa chắc | Vì sao quan trọng |
| --- | --- |
| | |

Ví dụ: tập app đối thủ có đúng không, người dùng mục tiêu có tụ ở nguồn nào khác không, có nguồn tiếng Việt
nào Claude không biết không. **Bạn biết thị trường rõ hơn Claude ở chỗ này.**

## 6. Sau khi bạn duyệt

Claude ghi một dòng vào `docs/_INDEX.md` mục 8 *Sổ đổi công cụ*, rồi **dừng phiên**. Không viết `01-02`,
không đào gì cả.

Bạn nối KimiBridge với Codex hoặc OpenCode, rồi làm theo `README.md` trong thư mục này.
