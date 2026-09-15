---
doc_id: 06-00
title: Feature Brief For Dev
phase: 06-breakdown
skill: product-breakdown
profile: Bắt buộc
owner: PO
reviewers: [Dev]
version: 0.1.0
status: draft
last_updated:
approved_by: ""
approved_at: ""
depends_on: [05-01, 03-05]
feeds: [06-01, 06-02, 06-03, 06-05, 13-03]
id_prefix: []
gate: G5
in_handover: true
confidence: medium
---

# [Tên dự án] — Feature Brief For Dev

> **Tài liệu ĐẦU TIÊN của phase 06.** Viết xong thì gửi Dev ngay, rồi chạy tiếp `06-01` → `06-05`
> **song song** trong lúc Dev nghiên cứu. Đây là điều duy nhất khiến phản hồi `TECH-02` đến `TECH-05`
> về kịp để *định hình* FR, thay vì đến muộn và *phủ định* FR đã viết.
>
> File này ở giữa hai mức độ chín:
> `05-01` mục 10 nói **làm tính năng gì** · file này nói **tính năng đó cần gì và chỗ nào chưa chắc** ·
> `06-02` nói **yêu cầu chính xác kèm acceptance criteria**.
>
> Vòng khả thi thô đã chạy ở `03-05` theo `CAP`. Vòng này mịn hơn, theo `FEAT`. Đừng hỏi lại những gì
> `03-05` đã có phán quyết — trích lại và chỉ hỏi phần mới.

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


## 1. Phạm vi bản brief này

| Trường | Nội dung |
| --- | --- |
| Nguồn danh sách `FEAT` | `05-01_PRD.md` mục 10 |
| Phán quyết khả thi đã có | `03-05_TECH_FEASIBILITY_BRIEF.md` mục 5 |
| Số `FEAT` mức Must | |
| Ngày gửi Dev | |
| Hạn mong muốn có phản hồi | |

**Chỉ đưa vào đây `FEAT` mức Must và Should.** Could thì để sau — hỏi Dev về tính năng có thể không làm là
cách nhanh nhất làm loãng thứ thật sự cần trả lời.

## 2. Brief theo từng tính năng

Lặp khối này cho mỗi `FEAT`.

### FEAT-001 · [tên tính năng]

| Trường | Nội dung |
| --- | --- |
| Mức ưu tiên | Must / Should |
| `CAP` liên quan | `CAP-xxx` — phán quyết ở `03-05`: … |
| Vấn đề người dùng nó giải quyết | `PN-xxx` / `NC-xxx` |
| Người dùng làm gì với nó | mô tả bằng hành vi, 2–3 dòng |
| Kết quả người dùng nhận được | |

**Hành vi mong muốn** — viết bằng ngôn ngữ người dùng, chưa cần chính xác như FR:

- người dùng …
- hệ thống …
- nếu … thì …

**Dữ liệu tính năng này cần**

| Cần gì | Từ đâu | Có phải rời khỏi máy không | Lưu bao lâu |
| --- | --- | --- | --- |
| | người dùng nhập / cảm biến / dịch vụ ngoài / có sẵn trong máy | | |

**Quyền hệ thống dự đoán cần**

| Quyền | Dùng để làm gì | Bắt buộc hay tuỳ chọn | Người dùng từ chối thì sao |
| --- | --- | --- | --- |
| | | | |

Cột cuối là cột hay bị bỏ trống nhất, và là cột sinh ra nhiều màn hình nhất ở phase 08. Đừng để trống.

**Phụ thuộc bên ngoài dự đoán**

| Phụ thuộc | Bắt buộc hay thay được | Nếu chết thì tính năng còn dùng được không |
| --- | --- | --- |
| dịch vụ / API / SDK / thiết bị | | |

**Chỗ tôi chưa chắc** — nêu thẳng, đây là phần Dev đọc trước tiên:

| Điều chưa chắc | Nếu đoán sai thì hỏng ở đâu |
| --- | --- |
| | |

**Câu hỏi cho Dev**

| `DQ` | Câu hỏi | Ngưỡng chấp nhận được | Cần trả lời trước |
| --- | --- | --- | --- |
| `DQ-xxx` | | | `06-02` / `06-03` / `08-03` |

**Phản hồi của Dev** — điền từ `tech-input/`, không tự suy đoán:

| Trường | Nội dung |
| --- | --- |
| Khả thi | KHẢ THI / KHÓ, TỐN CÔNG / KHÔNG KHẢ THI / CHƯA TRẢ LỜI |
| Điều kiện kèm theo | |
| Phương án thay thế Dev đề xuất | |
| Ảnh hưởng tới `FEAT` khác | |
| Nguồn | `TECH-0x` phiên bản … ngày … |

## 3. Bảng tổng hợp gửi Dev

Một trang Dev đọc trước khi mở chi tiết.

| `FEAT` | Tính năng | Mức | `CAP` | Số `DQ` | Khả thi | Cần trả lời trước |
| --- | --- | --- | --- | --- | --- | --- |
| `FEAT-001` | | Must | | | CHƯA TRẢ LỜI | `06-02` |

## 4. Điều đã thay đổi sau phản hồi Dev

Ghi lại, đừng sửa im lặng. Đây là căn cứ để `06-01` và `06-02` viết đúng ngay từ đầu.

| `FEAT` | Đã đổi gì | Vì sao | `DEC` | `CHG` nếu tài liệu đã approved |
| --- | --- | --- | --- | --- |
| | | | | |

`FEAT` nào bị **cắt** vì không khả thi: phải cập nhật `05-01` mục 10 và mục 11 qua `CHG`, không được chỉ
xoá khỏi file này.

## 5. Nguồn phương pháp

| Nguồn | Áp dụng ở mục nào |
| --- | --- |
| `references/` của skill này | |
| Skill chiều sâu đã dùng | |
| `tech-input/` file nào, phiên bản, ngày nhận | mục 2 phần Phản hồi, mục 4 |

## Thuật ngữ dùng trong tài liệu này

Chép nghĩa một câu từ `docs/_GLOSSARY.md` mục *Thuật ngữ chuyên môn*, và nghĩa của tiền tố mã từ
`docs/_ID_REGISTRY.md`. Chỉ liệt kê thứ **thật sự xuất hiện** trong tài liệu này.

| Thuật ngữ / tiền tố mã | Nghĩa một câu |
| --- | --- |
| | |

> Bảng này không phải để người trong nghề đọc — nó dành cho người ở vai trò khác đang phải duyệt tài liệu
> này. `validate_docs.py` đối chiếu: dùng mà không liệt kê là **LỖI**; liệt kê mà không dùng là cảnh báo.

<!-- QUALITY-GATE-MANIFEST:START
# Nguồn chân lý DUY NHẤT cho G5 phần tài liệu này. KHÔNG chép khối này vào file đầu ra ở docs/.
doc: 06-00_FEATURE_BRIEF_FOR_DEV
gate: G5
required_major:
  - "0. Đọc nhanh"
  - "1. Phạm vi bản brief này"
  - "2. Brief theo từng tính năng"
  - "3. Bảng tổng hợp gửi Dev"
  - "4. Điều đã thay đổi sau phản hồi Dev"
  - "5. Nguồn phương pháp"
  - "Thuật ngữ dùng trong tài liệu này"
required_minor:
  "2. Brief theo từng tính năng":
    - "Hành vi mong muốn"
    - "Dữ liệu tính năng này cần"
    - "Quyền hệ thống dự đoán cần"
    - "Phụ thuộc bên ngoài dự đoán"
    - "Chỗ tôi chưa chắc"
    - "Câu hỏi cho Dev"
    - "Phản hồi của Dev"
quality_checks:
  - "Mọi FEAT mức Must ở 05-01 mục 10 đều có một khối ở mục 2 — không thiếu tính năng nào"
  - "Mỗi FEAT có ít nhất 1 DQ, và mọi DQ đã có dòng ở 13-02_DEV_QUESTION_LOG.md"
  - "Cột 'Người dùng từ chối thì sao' của bảng quyền không để trống ở FEAT nào có xin quyền"
  - "Mỗi FEAT trích lại phán quyết CAP tương ứng từ 03-05, không hỏi lại điều đã có phán quyết"
  - "Cột Khả thi ở mục 3 điền từ tech-input, ghi rõ nguồn và ngày — PO và AI không tự phán quyết"
  - "FEAT bị cắt vì không khả thi đã có CHG và đã cập nhật 05-01 mục 10 và mục 11"
  - "Không mô tả kiến trúc, tên thư viện, hay lược đồ dữ liệu — đó là nội dung của tech-input"
QUALITY-GATE-MANIFEST:END -->
