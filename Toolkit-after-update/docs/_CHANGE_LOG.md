---
doc_id: _CHANGE_LOG
title: Sổ thay đổi
owner: PO
version: 0.1.0
status: draft
---

# _CHANGE_LOG — Sổ thay đổi

**Tài liệu đã `approved` mà cần đổi thì tuyệt đối không sửa file trước.** Đi qua sáu bước dưới đây.

## Sáu bước bắt buộc

1. Cấp `CHG ID` và tạo một mục ở bảng dưới
2. Viết **Change Impact Report** theo khuôn ở cuối file
3. Chờ Product Owner duyệt
4. Cập nhật theo đúng **thứ tự lan truyền**
5. **Giữ ID cũ** nếu logic chưa bị thay thế
6. Cập nhật `_INDEX.md` và tăng `version` từng file đã chạm

## Thứ tự lan truyền

```
00-01 Brief → 05-01 PRD → 06-01 UC → 06-02 FR → 06-04 BR
→ 07-05 FLOW → 08-01 SCR → 08-02 ST → 08-03 Wireframe
→ 09-06 Copy → 10-02 EVT → 13-04 AC → 12-01 Roadmap → _INDEX
```

## Bảng thay đổi

| ID | Ngày | Yêu cầu thay đổi | Nguồn | Trạng thái | Số file bị chạm | Người duyệt |
| --- | --- | --- | --- | --- | --- | --- |
| `CHG-001` | | | | | | |

---

## Khuôn Change Impact Report

```
## CHG-XXX — <tên thay đổi>

**Yêu cầu:** <mô tả bằng lời người dùng>
**Nguồn:** <ai yêu cầu, vì sao>
**Ngày:**

### Tài liệu bị ảnh hưởng

| File | Mục bị chạm | Nội dung phải đổi | ID bị ảnh hưởng |
| --- | --- | --- | --- |

### ID mới phải cấp

### ID bị archive

### Rủi ro nếu chỉ sửa một phần

### Ước lượng công cập nhật tài liệu

### Quyết định
- [ ] Duyệt, cập nhật đủ theo thứ tự lan truyền
- [ ] Duyệt một phần — ghi rõ phần nào hoãn và rủi ro
- [ ] Từ chối — ghi lý do vào `_DECISION_LOG.md`
```

> **Ví dụ vì sao không được sửa lẻ.** Yêu cầu *"người dùng free được scan ba lần mỗi ngày"*. Nếu chỉ sửa paywall
> sẽ thiếu bảy chỗ: quy tắc reset theo múi giờ nào (`06-04`), trạng thái hết lượt (`08-02`), chỗ hiển thị còn
> mấy lượt (`08-01`, `09-06`), event `free_limit_reached` (`10-02`), ảnh hưởng phễu (`10-03`), ca nghiệm thu
> lượt thứ ba và thứ tư (`13-04`), và lượt còn lại có cộng dồn không (`06-04` lần nữa).
