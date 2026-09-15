# Phiếu yêu cầu dữ liệu — công cụ bạn phải tra tay

| Trường | Nội dung |
| --- | --- |
| Công cụ | Sensor Tower / Data.ai / khác |
| Claude điền phiếu này ngày | |
| Tài liệu đang cần | ví dụ `02-01` Bản đồ đối thủ, `03-01` Chấm điểm nhu cầu |
| Cổng đang nhắm | ví dụ `G1` Cơ hội có bằng chứng |
| Trạng thái | chờ điền / đã điền một phần / đã điền xong |

> **Claude điền phiếu này, bạn đi tra, rồi dán số vào `SENSOR_TOWER_DATA.md`.**
>
> Phiếu chỉ được sinh **sau khi** đã khai thác hết trang store, review, cộng đồng, AppStoreSpy, và đã
> dùng thật 5–6 app. Sinh sớm hơn là hỏi bừa, vì chưa biết cần số của app nào cho câu hỏi nào.
>
> Quy tắc chọn chỉ số ở `.claude/skills/_depth/02-competitor/market-data-sourcing/SKILL.md`.

## 1. Tập app cần tra

| # | Tên app | Bundle ID / link store | Vì sao app này trong tập | Quốc gia cần xem | Khoảng thời gian |
| --- | --- | --- | --- | --- | --- |
| 1 | | | | VN / US / … | 12 tháng gần nhất |

Tập này phải khớp `02-01_COMPETITOR_LANDSCAPE.md`. Thêm app ngoài tập thì ghi lý do.

## 2. Chỉ số cần lấy

**Claude chỉ được liệt kê chỉ số trả lời một câu hỏi cụ thể.** Cột *Câu hỏi con số này trả lời* để trống
thì xoá dòng đó.

| # | Chỉ số | Ở app nào | Câu hỏi con số này trả lời | Điền vào tài liệu | Bắt buộc để đóng cổng |
| --- | --- | --- | --- | --- | --- |
| 1 | Downloads / tháng | 1, 2, 3 | ngách này có đủ lớn để đáng làm không | `01-01`, `03-01` | Có |
| 2 | Retention D30 | 1, 2 | đối thủ giữ được người dùng không, hay chỉ mua traffic | `02-04`, `10-01` | Có |
| 3 | Cấu trúc gói và giá tại VN | 1, 2, 3 | mức giá thị trường đang chấp nhận | `09-02` | Có |
| 4 | | | | | Tốt nếu có |

Cột cuối cho bạn biết chỗ nào **được phép bỏ trống**. Chỉ số *Tốt nếu có* mà không tra được thì bỏ, ghi
một dòng ở `docs/_ASSUMPTION_REGISTER.md` là xong — không chặn cổng.

## 3. Chỉ số Claude đã cân nhắc rồi bỏ

Ghi ra để bạn biết Claude không bỏ sót vì quên.

| Chỉ số | Vì sao không lấy |
| --- | --- |
| | ví dụ: chưa có câu hỏi nào cần tới nó ở phase này |

## 4. Ghi chú khi tra

- Xuất được file thì bỏ nguyên file vào `research-raw/`, chỉ dán con số tổng vào `SENSOR_TOWER_DATA.md`.
- Chụp ảnh dashboard cũng được, bỏ vào `research-raw/anh-chup/`.
- Số nào công cụ không có thì ghi thẳng **không có trong công cụ**, đừng để trống — trống thì Claude không
  phân biệt được *chưa tra* với *tra rồi mà không có*.
- Thấy chỉ số nào hay mà phiếu không hỏi thì cứ ghi thêm vào mục 4 của `SENSOR_TOWER_DATA.md`.
