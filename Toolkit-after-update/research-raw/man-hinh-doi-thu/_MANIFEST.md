# Mục lục ảnh màn hình đối thủ

| Trường | Nội dung |
| --- | --- |
| Cập nhật lần cuối | |
| Số app đã chụp | |
| Tổng số ảnh | |
| Trạng thái | đang chụp / đã đủ |

> Ảnh ở đây là nguyên liệu cho `07-00_UX_RESEARCH` (UX Research). Claude đọc **mục lục này trước**, rồi chỉ
> mở đúng thư mục cần cho luồng đang phân tích — đọc hai trăm ảnh một lượt là tốn hạn mức vô ích.
>
> **Đây là bằng chứng của bạn. Claude đọc, không sửa, không xoá.**

## 1. Cấu trúc thư mục

```
research-raw/man-hinh-doi-thu/
├── _MANIFEST.md          ← file này
├── myfitnesspal/
│   ├── 01_onboarding_chon-muc-tieu.png
│   ├── 02_onboarding_nhap-can-nang.png
│   ├── 03_paywall_sau-buoc-3.png
│   └── 04_home_lan-dau.png
├── lifesum/
└── yazio/
```

**Tên thư mục = tên app**, viết thường, không dấu, gạch ngang thay khoảng trắng. Phải khớp tên trong
`02-01` (Bản đồ đối thủ) để đối chiếu được.

## 2. Quy ước đặt tên ảnh — phần quan trọng nhất

```
<số thứ tự>_<luồng>_<nội dung màn>.png

01_onboarding_chon-muc-tieu.png
02_onboarding_nhap-can-nang.png
03_paywall_sau-buoc-3.png
```

**Tiền tố số là bắt buộc.** Không có nó Claude không dựng lại được **thứ tự luồng** — nó chỉ thấy một đống
màn rời rạc và sẽ đoán sai đâu là bước một, đâu là bước cuối. Đây là lỗi khiến cả bản phân tích sai.

Chụp nhiều luồng của cùng một app thì đánh số liên tục theo từng luồng: `01_`…`05_` cho onboarding,
`10_`…`14_` cho luồng ghi bản ghi. Chừa khoảng trống để sau chèn thêm.

Chụp cả **trạng thái đặc biệt** nếu bắt được: rỗng, lỗi, mất mạng, hết hạn gói. Đặt tên rõ:
`22_ghi-ban-ghi_trang-thai-rong.png`. Đây là những màn mà `08-02` (Ma trận trạng thái) cần nhất và cũng là
những màn khó nghĩ ra nhất.

## 3. Bảng mục lục

| App | Thư mục | Số ảnh | Luồng đã chụp | Phiên bản app | Ngày chụp | Thiết bị |
| --- | --- | --- | --- | --- | --- | --- |
| | | | onboarding · ghi bản ghi · paywall · cài đặt | | | iPhone 15 / … |

**Ngày chụp bắt buộc.** Giao diện app đổi liên tục — một bản phân tích không có ngày sẽ bị dùng lại khi đã
lỗi thời, và không ai biết.

## 4. Luồng đã cố chụp nhưng không được

| App | Luồng | Vì sao không chụp được |
| --- | --- | --- |
| | | cần tài khoản trả phí · chỉ có ở nước khác · không tìm thấy lối vào |

Không được để trống nếu có. Chỗ **không vào được** cũng là thông tin: nó cho biết đối thủ giấu gì sau
paywall, hoặc lối vào của họ khó tìm tới mức chính bạn cũng không thấy.

## 5. Điều bạn nhận ra khi chụp

| Điều nhận ra | App | Ảnh nào |
| --- | --- | --- |
| | | |

Bạn đang thao tác thật nên thấy được thứ ảnh không ghi lại: chỗ nào lag, chỗ nào phải thử hai lần mới hiểu,
chỗ nào bực. **Ghi ngay lúc chụp** — vài hôm sau là quên, và Claude không bao giờ suy ra được từ ảnh tĩnh.
