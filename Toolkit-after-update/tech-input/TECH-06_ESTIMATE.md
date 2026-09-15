---
file: TECH-06_ESTIMATE.md
title: Ước lượng công
owner: Dev
version: 0.1.0
status: chưa nộp        # chưa nộp | đang viết | đã nộp | đã cập nhật
date:
---

# Ước lượng công

> File này do **Dev** viết. PO và AI không sửa nội dung ở đây.
> Điền `version`, `date` và đổi `status` khi nộp.

## Nội dung tối thiểu cần có

- Ước lượng theo FR hoặc theo phase
- **Ba con số**: lạc quan / thực tế / dự phòng
- **Bốn giả định định lượng** — bảng ngay dưới, không được bỏ trống
- Đường găng: việc nào chặn việc nào
- Điều gì làm ước lượng sai và dấu hiệu sớm

## Bốn giả định định lượng — bắt buộc

Không có bốn dòng này thì hai ước lượng "20 ngày" của hai người có thể lệch nhau ba lần mà không ai
biết vì sao. Đây là thứ khiến ước lượng **đối chiếu được**, thay vì chỉ là một con số.

| Giả định | Giá trị | Ghi chú |
| --- | --- | --- |
| Số Dev chạy song song | | ước lượng cho mấy người cùng làm |
| Có dùng AI hỗ trợ code không | có / không | ảnh hưởng rất mạnh tới phần lặp lại |
| Một ngày công bằng bao nhiêu giờ làm thật | | thường 5–6h, không phải 8h |
| Phần trăm dự phòng đã cộng vào chưa | | nếu đã cộng thì ba con số ở trên hiểu thế nào |

**File này là nguồn duy nhất về công sức.** Tài liệu sản phẩm chỉ ghi mức ưu tiên và độ phức tạp,
không ghi số ngày. Thấy số ngày ở tài liệu nào khác là mâu thuẫn, báo cho PO.

---

## Nội dung

_TBD_

---

## Điều PO cần biết nhưng không nằm trong các mục trên

_TBD_

## Câu hỏi ngược lại cho PO

| # | Câu hỏi | Ảnh hưởng tới FR / quyết định nào |
| --- | --- | --- |
