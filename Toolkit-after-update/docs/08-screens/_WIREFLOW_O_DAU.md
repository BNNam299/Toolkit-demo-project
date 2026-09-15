# Wireflow của chặng 08 không nằm trong thư mục này

Thư mục này chỉ chứa **4 tài liệu markdown** của chặng 08: kiểm kê màn hình `08-01`, ma trận trạng thái
`08-02`, đặc tả wireflow `08-03`, báo cáo màn còn thiếu `08-04`.

**Bản wireflow xem được bằng mắt nằm ở `wireframes/` ngoài gốc dự án.**

```
wireframes/
├── index.html                    danh sách luồng + thư viện màn
├── flow-FLOW-001_ten-luong.html  một trang một luồng — mở cái này
├── SCR-012_ST-041_ten-man.html   một màn một trạng thái
└── _wireframe.css
```

Xem: mở terminal ở gốc dự án, gõ `python -m http.server 8000`, rồi vào
`http://localhost:8000/wireframes/`.

## Vì sao tách ra, không nhét vào đây

| Lý do | Cụ thể |
| --- | --- |
| Khác loại, khác cách kiểm | `docs/` chỉ chứa markdown có front-matter 13 trường, có tên trong `_INDEX`, đi qua cổng. Wireflow là **bản dựng**, không phải tài liệu — kiểm bằng `check_build.py`, không phải `validate_docs.py` |
| Người xem khác người viết | Wireflow là thứ mở cho Dev và người quyết định xem. Họ không cần đi vào thư mục tài liệu |
| Bàn giao | Chặng 13 gửi `wireframes/` cho Dev như một gói riêng |

`08-03` là **đặc tả**: mỗi luồng gồm màn nào, mũi tên nào, nhánh theo điều kiện gì. `wireframes/` là **bản
dựng theo đặc tả đó**. Hai bên phải khớp, và `check_build.py` là thứ bắt lúc lệch:

```
python .claude/scripts/check_build.py --wireframes wireframes/
```
