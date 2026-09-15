# _depth — skill chiều sâu

Thư mục này chứa **skill chiều sâu**: skill làm agent hiểu đúng hơn khi làm một phase,
nhưng **không** sinh tài liệu, **không** có cổng, **không** cấp prefix ID.

## Thêm một skill chiều sâu

Thả thư mục skill vào đúng phase. Hết. Không phải sửa `_INDEX`, `_ID_REGISTRY`, hay bất kỳ file khung nào.

```
_depth/09-growth/paywall-pricing-psychology/
├── SKILL.md          ← frontmatter cần `name` và `description` một dòng thật rõ
└── references/       ← tuỳ chọn
```

`description` quan trọng hơn bạn nghĩ: skill phụ trách tài liệu đọc description trước và chỉ mở
toàn bộ nội dung của skill nào thật sự liên quan tới dự án đang làm. Description mơ hồ thì hoặc
bị bỏ qua, hoặc bị nạp thừa và làm loãng trọng tâm.

## Khi nào một skill chiều sâu nên được nâng thành skill phụ trách tài liệu

Nếu nó chỉ thay đổi **cách nghĩ** thì để ở đây.
Nếu nó tạo ra một **sản phẩm mà có người phải đọc và ký duyệt** thì nó cần một tài liệu và một cổng —
lúc đó dùng `add_doc.py`, vì phải chạm năm chỗ: thư mục skill, số `NN` tiếp theo trong phase,
template kèm `QUALITY-GATE-MANIFEST`, đăng ký cổng, và bảng danh mục ở `_INDEX` cùng `_ID_REGISTRY`.

## Quy tắc mâu thuẫn

Khi skill chiều sâu nói khác `references/` của skill phụ trách tài liệu, **skill chiều sâu thắng** —
nhưng tài liệu đầu ra phải ghi rõ đã áp dụng skill nào ở chỗ nào, trong mục "Nguồn phương pháp" cuối file.
