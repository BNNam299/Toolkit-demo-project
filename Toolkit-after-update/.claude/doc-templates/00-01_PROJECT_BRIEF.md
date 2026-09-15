---
doc_id: 00-01
title: Project Brief
phase: 00-khoi-tao
skill: doc-orchestrator
profile: Bắt buộc
owner: PO
reviewers: []
version: 0.1.0
status: draft
last_updated:
approved_by: ""
approved_at: ""
depends_on: []
feeds: [00-02, 05-01]
id_prefix: []
gate: G0
in_handover: true
confidence: low
---

# [Tên dự án] — Project Brief

> Brief **không phải** bản mô tả ý tưởng. Nó ghi lại bối cảnh và ràng buộc để phase sau không phải đoán.
> Không đề xuất tính năng, không chọn công nghệ, không viết PRD ở đây.

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


## 1. Vấn đề

### 1.1 Ai đang gặp khó khăn gì
_Mô tả bằng ngôn ngữ của người dùng, không dùng từ kỹ thuật._

### 1.2 Họ đang xử lý bằng cách nào
_Cách hiện tại — thủ công, sản phẩm khác, hoặc chịu đựng._

### 1.3 Cách đó dở ở chỗ nào
_Cụ thể: tốn bao lâu, sai chỗ nào, khó chịu ở đâu._

### 1.4 Nếu không có sản phẩm này
_Chuyện gì xảy ra với họ. Nếu câu trả lời là "không sao cả" thì cân nhắc lại._

## 2. Người dùng

### 2.1 Ai sẽ mở app nhiều lần một tuần
### 2.2 Bối cảnh sử dụng
_Đang đứng, đang vội, đang rảnh, một tay hay hai tay, có mạng hay không._

### 2.3 Người trả tiền có phải người dùng không

## 3. Ràng buộc

| Ràng buộc | Nội dung | Mức cứng |
| --- | --- | --- |
| Ngân sách | | Cứng / Mềm |
| Thời gian | | |
| Nhân lực | | |
| Pháp lý, ngành nghề | | |
| Nền tảng | | |

## 4. Định nghĩa thành công

### 4.1 Ba tháng sau phát hành, con số nào cho biết đã thành công
### 4.2 Con số nào cho biết nên dừng
_Đặt ngưỡng dừng ngay từ đầu. Đặt sau khi thấy kết quả là tự lừa mình._

## 5. Điều đã quyết trước

| # | Điều đã chốt | Ai chốt | Có thương lượng lại được không |
| --- | --- | --- | --- |
| | | | |

## 6. Điều chưa biết

| ID | Chưa biết gì | Ảnh hưởng tới quyết định nào | Đã ghi ở `_ASSUMPTION_REGISTER` |
| --- | --- | --- | --- |
| `ASM-` | | | |

## 7. Nguồn phương pháp
_Skill chiều sâu đã áp dụng, nếu có._

## Thuật ngữ dùng trong tài liệu này

Chép nghĩa một câu từ `docs/_GLOSSARY.md` mục *Thuật ngữ chuyên môn*, và nghĩa của tiền tố mã từ
`docs/_ID_REGISTRY.md`. Chỉ liệt kê thứ **thật sự xuất hiện** trong tài liệu này.

| Thuật ngữ / tiền tố mã | Nghĩa một câu |
| --- | --- |
| | |

> Bảng này không phải để người trong nghề đọc — nó dành cho người ở vai trò khác đang phải duyệt tài liệu
> này. `validate_docs.py` đối chiếu: dùng mà không liệt kê là **LỖI**; liệt kê mà không dùng là cảnh báo.

<!-- QUALITY-GATE-MANIFEST:START
# Nguồn chân lý DUY NHẤT cho G0 phần tài liệu này. KHÔNG chép khối này vào file đầu ra ở docs/.
doc: 00-01_PROJECT_BRIEF
gate: G0
required_major:
  - "0. Đọc nhanh"
  - "1. Vấn đề"
  - "2. Người dùng"
  - "3. Ràng buộc"
  - "4. Định nghĩa thành công"
  - "5. Điều đã quyết trước"
  - "6. Điều chưa biết"
  - "7. Nguồn phương pháp"
  - "Thuật ngữ dùng trong tài liệu này"
required_minor:
  "1. Vấn đề": ["1.1", "1.2", "1.3", "1.4"]
  "2. Người dùng": ["2.1", "2.2", "2.3"]
  "4. Định nghĩa thành công": ["4.1", "4.2"]
quality_checks:
  - "Mọi câu chưa trả lời được đã gắn [ASM] và có dòng ở _ASSUMPTION_REGISTER"
  - "Không đề xuất tính năng cụ thể"
  - "Không khai báo công nghệ"
  - "Mục 4.2 có ngưỡng dừng bằng số, không bỏ trống"
QUALITY-GATE-MANIFEST:END -->
