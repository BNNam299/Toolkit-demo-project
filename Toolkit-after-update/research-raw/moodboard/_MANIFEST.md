# Moodboard — mục lục ảnh tham chiếu UI

| Trường | Nội dung |
| --- | --- |
| Cập nhật lần cuối | |
| Số ảnh | |
| Số nguồn | |
| Trạng thái | đang thu / đã đủ, chờ nghiệm thu / đã nghiệm thu |

> Nguyên liệu cho `12-00_UI_RESEARCH` (UI Research). Claude đọc **mục lục này trước**, rồi chỉ mở ảnh cần.
>
> **Đây là bằng chứng của bạn. Claude đọc, không sửa, không xoá.**

## 1. Cấu trúc

```
research-raw/moodboard/
├── _MANIFEST.md              ← file này
├── mau-sac/                  bảng màu, gradient, dark mode
├── kieu-chu/                 hệ chữ, cỡ, cân nặng
├── thanh-phan/               nút, thẻ, input, tab bar, bottom sheet
├── man-hinh-hay/             màn hoàn chỉnh đáng học
└── khong-thich/              ← ảnh phản ví dụ, quan trọng ngang phần trên
```

Thư mục `khong-thich/` không phải cho vui. **Biết mình không muốn gì cũng định hình style mạnh như biết
mình muốn gì**, và nó ngăn Claude đề xuất đúng thứ bạn đã loại.

## 2. Quy ước đặt tên

```
<nguồn>_<chủ đề>_<ghi chú>.png

dribbble_mau-sac_pastel-am.png
mobbin_thanh-phan_bottom-sheet-3-buoc.png
appstore_man-hinh-hay_home-lifesum.png
```

Nguồn đứng đầu để truy được. Ảnh không biết nguồn thì bỏ — không dùng làm căn cứ cho quyết định style.

## 3. Bảng mục lục

| # | File | Nguồn + URL | Chủ đề | Cái gì đáng học ở đây | Ngày lấy |
| --- | --- | --- | --- | --- | --- |
| 1 | | Mobbin / Dribbble / Behance / store / … | màu · chữ · thành phần · màn · không thích | | |

**Cột "cái gì đáng học"** là cột duy nhất Claude không tự suy ra được từ ảnh. Bạn lưu ảnh đó vì một lý do —
ghi lý do lại, nếu không sáu mươi ảnh sẽ thành sáu mươi thứ na ná nhau.

## 4. Giao cho Codex hoặc OpenCode đi thu

Dán khối này sau khi đã nối KimiBridge:

```
Nhiệm vụ: THU THẬP ảnh tham chiếu UI cho moodboard. Không phân tích, không kết luận.

Lĩnh vực: <X>. Đọc docs/12-prototype/12-00_UI_RESEARCH.md mục 0 nếu đã có, để biết đang tìm gì.
Lưu ảnh vào research-raw/moodboard/<thư mục con đúng chủ đề>/
Ghi mục lục vào research-raw/moodboard/_MANIFEST.md mục 3, CHỈ NỐI THÊM.

Nguồn nên đào: Mobbin, Dribbble, Behance, Pinterest, trang store của app cùng lĩnh vực,
Awwwards cho hướng thị giác.

Quy tắc:
- Mỗi ảnh một dòng mục lục, có URL nguồn mở được và ngày lấy.
- KHÔNG cấp mã ID. Chỉ đánh số thứ tự.
- Không lưu ảnh không rõ nguồn.
- Tối thiểu 30 ảnh, từ ≥3 nguồn, phủ cả 4 chủ đề: màu, chữ, thành phần, màn hoàn chỉnh.
- Không ghi gì vào docs/.
- Dừng sau mỗi vòng, báo bộ đếm theo chủ đề, chờ tôi gửi nguồn tiếp.
```

Cùng khuôn với `thu-hoach/`: **dừng từng vòng để bạn soi**, đừng chạy liền một lúc.

## 5. Nghiệm thu

| Kiểm | Đạt khi |
| --- | --- |
| Số ảnh | ≥30 |
| Phủ chủ đề | có ảnh ở cả 4 thư mục màu, chữ, thành phần, màn hoàn chỉnh |
| Nguồn | mỗi dòng có URL mở được |
| `khong-thich/` | **có ít nhất 3 ảnh** — không có nghĩa là bạn chưa nghĩ về điều mình muốn tránh |
| Trùng lặp | không có 5 ảnh cùng một style, giữ 1–2 đại diện |

## 6. Điều bạn nhận ra khi tìm

| Điều nhận ra | Ảnh nào | Vì sao đáng chú ý |
| --- | --- | --- |
| | | |

Trong lúc lướt, bạn sẽ thấy những thứ ảnh không nói: style nào đang bão hoà, style nào lỗi thời, style nào
đẹp nhưng chắc chắn khó dựng. **Ghi ngay** — đây là phần Claude không suy ra được từ ảnh tĩnh.
