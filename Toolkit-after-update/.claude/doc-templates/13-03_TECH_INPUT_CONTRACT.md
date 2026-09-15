---
doc_id: 13-03
title: Tech Input Contract
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
depends_on: []
feeds: [13-01]
id_prefix: []
gate: G11
in_handover: false
confidence: low
---

# [Tên dự án] — Tech Input Contract

> Hợp đồng hai chiều: **Dev nộp gì**, và **AI được phép làm gì** với thứ đã nộp.

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


## 1. Sáu file Dev nộp
| File | Nội dung tối thiểu | Điền vào tài liệu nào | **Cần trước phase** | Trạng thái | Ngày nhận | Version |
| --- | --- | --- | --- | --- | --- | --- |
| `TECH-01_ARCHITECTURE` | Thành phần, cái gì chạy trên máy / gọi ra ngoài, luồng dữ liệu | `05-03` | 05 | chưa nộp | | |
| `TECH-02_API_CONTRACT` | Endpoint, input/output, **mã lỗi → trạng thái UI**, thời gian phản hồi, quota, chi phí | `06-02`, `08-02` | 06 | | | |
| `TECH-03_DATA_MODEL` | Thực thể, quan hệ, nơi lưu, thời hạn, hành vi khi xoá và đổi thiết bị | `06-05`, `05-03` | 06 | | | |
| `TECH-04_PLATFORM_CONSTRAINTS` | OS thấp nhất, thiết bị tham chiếu, **ngưỡng hiệu năng khả thi**, giới hạn quyền | `06-03` | 06 | | | |
| `TECH-05_FEASIBILITY_NOTES` | Với từng `FR`: khả thi / khó / không khả thi, lý do, phương án thay thế | `06-02` | 06 | | | |
| `TECH-06_ESTIMATE` | Ước lượng ba con số, giả định, đường găng | `13-01` | 12 | | | |

> **`TECH-05` là file có giá trị cao nhất và nên xin sớm nhất.** Biết một yêu cầu không khả thi ở phase 06
> rẻ hơn biết ở phase 12 rất nhiều.

## 2. Quy trình khi Dev nộp
| Bước | Ai làm | Việc |
| --- | --- | --- |
| 1 | AI | **Đọc, không sửa gì** |
| 2 | AI | Báo cáo: nội dung này sẽ điền vào section nào của tài liệu nào |
| 3 | AI | **Liệt kê mâu thuẫn** giữa ràng buộc kỹ thuật và mong muốn sản phẩm |
| 4 | PO | Duyệt |
| 5 | AI | Cập nhật, ghi rõ **nguồn file và ngày nhận** vào từng chỗ đã điền |

> Bước 3 quan trọng nhất và **không được bỏ**. Mâu thuẫn bị hoà tan vào văn bản là mâu thuẫn sẽ nổ lúc build.

## 3. Quy tắc bất di bất dịch
| # | Quy tắc |
| --- | --- |
| 1 | **AI không bao giờ sửa nội dung trong `tech-input/`** — đó là tài sản của Dev |
| 2 | Thiếu thông tin thì gắn `[ASM]` và tạo `DQ`, **không suy đoán** |
| 3 | Có mâu thuẫn thì **nêu ra**, không lặng lẽ chọn một bên |
| 4 | Mọi nội dung điền từ `tech-input/` phải ghi nguồn và ngày nhận |

## 4. Mâu thuẫn đã phát hiện
| # | Ràng buộc kỹ thuật | Mong muốn sản phẩm | Cách giải quyết | `DEC` | `CHG` |
| --- | --- | --- | --- | --- | --- |

## 5. Nguồn phương pháp

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
doc: 13-03_TECH_INPUT_CONTRACT
gate: G11
required_major:
  - "0. Đọc nhanh"
  - "1. Sáu file Dev nộp"
  - "2. Quy trình khi Dev nộp"
  - "3. Quy tắc bất di bất dịch"
  - "4. Mâu thuẫn đã phát hiện"
  - "5. Nguồn phương pháp"
  - "Thuật ngữ dùng trong tài liệu này"
required_minor:
  {}
quality_checks:
  - "Bảng mục 1 có trạng thái, ngày nhận, version cho từng file"
  - "AI không sửa nội dung trong tech-input/"
  - "Mọi nội dung điền từ tech-input ghi nguồn và ngày nhận"
  - "Mâu thuẫn được nêu ở mục 4, không lặng lẽ chọn một bên"
QUALITY-GATE-MANIFEST:END -->
