---
doc_id: 13-01
title: Handover Package
phase: 13-handover
skill: dev-handover
profile: Bắt buộc
owner: PO
reviewers: []
version: 0.1.0
status: draft
last_updated:
approved_by: ""
approved_at: ""
depends_on: [05-03, 12-03, 13-02, 13-04]
feeds: []
id_prefix: []
gate: G11
in_handover: true
confidence: low
---

# [Tên dự án] — Handover Package

> Mục tiêu không phải gửi thật nhiều tài liệu, mà để một Dev **chưa từng tham gia** đọc xong biết phải làm gì,
> theo thứ tự nào, và điều gì còn chưa chốt.

## 0. Đọc nhanh

| Câu hỏi | Trả lời ngắn |
| --- | --- |
| **Tài liệu này là gì** | |
| **Ai cần đọc** | |
| **Đọc xong phải biết gì** | |
| **Quyết định nào chốt ở đây** | |

> Bốn dòng này viết **không dùng một thuật ngữ nào**, kể cả thuật ngữ của chính nghề mình. Người mới vào dự
> án — hoặc người ở vai trò khác — đọc bốn dòng là biết có cần đọc tiếp hay không. Để trống hoặc chép lại
> tên tài liệu là chưa làm.


## 1. Thứ tự đọc cho Dev mới
| # | File | Vì sao đọc | Thời gian dự kiến |
| --- | --- | --- | --- |
| 1 | `05-03_PROJECT_OVERVIEW.md` | hiểu dự án trong 10 phút | |
| 2 | `00-02_SCOPE_LOCK.md` | biết ranh giới và danh sách bị cấm | |
| 3 | `_GLOSSARY.md` | dùng đúng từ ngay từ đầu | |
| 4 | `06-02` + `06-03` | biết phải xây gì tới mức nào | |
| 5 | `08-01` + `08-02` | biết đủ số màn và trạng thái | |
| 6 | `13-04_ACCEPTANCE_CRITERIA_PACK.md` | biết nghiệm thu thế nào | |
| 7 | còn lại | tra khi cần | |

## 2. Mục lục gói bàn giao
> Ghi **phiên bản tại thời điểm bàn giao**. Ba tháng sau khi có tranh cãi, bạn cần biết Dev đã nhận bản nào.

| `doc_id` | File | Mục đích một dòng | **Version** | `status` |
| --- | --- | --- | --- | --- |

## 3. Ranh giới trách nhiệm
| Vai trò | Sở hữu | Quyền quyết định |
| --- | --- | --- |
| Product Owner | | phạm vi, ưu tiên, giá, duyệt cuối |
| Designer | | giải pháp UX trong phạm vi đã duyệt |
| Developer | `tech-input/`, kiến trúc, khả thi | kiến trúc, công nghệ trong allowlist |

> **Mọi thay đổi phạm vi đi qua `_CHANGE_LOG.md`, không thoả thuận miệng.**

## 4. Điều chưa chốt
> Liệt kê thẳng. Giấu đi không làm chúng biến mất, chỉ làm chúng nổ muộn hơn và đắt hơn.

| Loại | ID | Nội dung | Ảnh hưởng | Ai giải quyết | Hạn |
| --- | --- | --- | --- | --- | --- |
| Giả định còn sống | `ASM-` | | | | |
| Câu hỏi cho Dev còn mở | `DQ-` | | | | |
| Câu hỏi mở khác | `OQ-` | | | | |

## 5. Tài sản kèm theo
| Loại | Ở đâu | Ghi chú |
| --- | --- | --- |
| File Figma | | |
| Export ảnh | | |
| Design token | `12-02` | |
| Copy deck | `09-06` | |

## 6. Thứ tự thi công — khối máy đọc được

Mục 1 là thứ tự **đọc** cho người. Mục này là thứ tự **làm**, viết dưới dạng máy đọc được để agent lập trình
lấy trực tiếp không phải suy từ văn xuôi.

```json
{
  "project": "<tên dự án>",
  "snapshot": "<phiên bản bộ tài liệu, ví dụ 1.0 / 2026-08-18>",
  "units": [
    {
      "id": "nen-tang",
      "name": "Nền tảng dùng chung",
      "depends_on": [],
      "covers": { "FR": [], "UC": [], "SCR": [] },
      "must_not_cut": false
    },
    {
      "id": "<đơn vị tiếp theo>",
      "name": "",
      "depends_on": ["nen-tang"],
      "covers": { "FR": ["FR-001"], "UC": ["UC-001"], "SCR": ["SCR-001"] },
      "must_not_cut": true
    }
  ]
}
```

| Trường | Nghĩa |
| --- | --- |
| `id` | tên đơn vị thi công, chữ thường không dấu, dùng làm khoá phụ thuộc |
| `depends_on` | các `id` phải xong trước. **Không được có vòng** |
| `covers` | đơn vị này phủ những mã nào — đây là chỗ Dev truy về tài liệu chi tiết |
| `must_not_cut` | `true` nếu đơn vị chứa hạng mục trong danh sách *Không được cắt* ở `05-01` mục 11 |

| Kiểm | Kết quả |
| --- | --- |
| Khối JSON parse được | `validate_docs.py` kiểm tự động |
| Mọi `FR` mức Must xuất hiện ở đúng **một** đơn vị | không màn nào, không yêu cầu nào mồ côi |
| Mọi `SCR` trong `08-01` xuất hiện ở đúng **một** đơn vị | ai sở hữu màn nào là rõ |
| `depends_on` không có vòng | |
| Đơn vị nào chứa hạng mục không được cắt đã gắn `must_not_cut: true` | |

### Affordance nằm trên màn của đơn vị khác

Chỗ hay tranh chấp nhất khi chia việc: một nút thuộc tính năng A nhưng **nằm trên màn do đơn vị B dựng**.
Không ghi ra thì cả hai đều tưởng người kia làm.

| Affordance | Nằm trên `SCR` | Màn do đơn vị nào sở hữu | Hành vi thuộc `FR` nào | Ai dựng | Ai nối hành vi |
| --- | --- | --- | --- | --- | --- |
| | | | | | |

## 7. Kiểm đóng cổng G11
| Kiểm | Kết quả |
| --- | --- |
| Mọi file `Bắt buộc` theo profile có `status: approved` | |
| Không còn `DQ` mở đang chặn | |
| Mục lục có version từng file | |
| Mọi `[ASM]` còn sống đã liệt kê ở mục 4 | |
| Mọi `FR` có mục nghiệm thu ở `13-04` | |

## 8. Nguồn phương pháp

## Thuật ngữ dùng trong tài liệu này

Chép nghĩa một câu từ `docs/_GLOSSARY.md` mục *Thuật ngữ chuyên môn*, và nghĩa của tiền tố mã từ
`docs/_ID_REGISTRY.md`. Chỉ liệt kê thứ **thật sự xuất hiện** trong tài liệu này.

| Thuật ngữ / tiền tố mã | Nghĩa một câu |
| --- | --- |
| | |

> Bảng này không phải để người trong nghề đọc — nó dành cho người ở vai trò khác đang phải duyệt tài liệu
> này. `validate_docs.py` đối chiếu: dùng mà không liệt kê là **LỖI**; liệt kê mà không dùng là cảnh báo.

<!-- QUALITY-GATE-MANIFEST:START
# Nguồn chân lý DUY NHẤT cho G11 phần tài liệu này. KHÔNG chép khối này vào file đầu ra ở docs/.
doc: 13-01_HANDOVER_PACKAGE
gate: G11
required_major:
  - "0. Đọc nhanh"
  - "1. Thứ tự đọc cho Dev mới"
  - "2. Mục lục gói bàn giao"
  - "3. Ranh giới trách nhiệm"
  - "4. Điều chưa chốt"
  - "5. Tài sản kèm theo"
  - "6. Thứ tự thi công — khối máy đọc được"
  - "7. Kiểm đóng cổng G11"
  - "8. Nguồn phương pháp"
  - "Thuật ngữ dùng trong tài liệu này"
required_minor:
  {}
quality_checks:
  - "Mục lục ghi version từng file tại thời điểm bàn giao — điều kiện G11"
  - "Mọi [ASM] còn sống liệt kê tường minh ở mục 4 — điều kiện G11"
  - "Không còn DQ mở đang chặn — điều kiện G11"
  - "Ranh giới trách nhiệm ghi thành bảng, không để ngầm hiểu"
  - "Mục 6 có khối JSON parse được, mọi FR mức Must và mọi SCR xuất hiện ở đúng một đơn vị, depends_on không có vòng"
  - "Bảng Affordance ở mục 6 đã điền cho mọi nút thuộc tính năng khác mà nằm trên màn của đơn vị khác"
QUALITY-GATE-MANIFEST:END -->
