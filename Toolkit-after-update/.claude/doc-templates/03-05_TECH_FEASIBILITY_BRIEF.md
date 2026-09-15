---
doc_id: 03-05
title: Tech Feasibility Brief
phase: 03-opportunity
skill: opportunity-validator
profile: Bắt buộc
owner: PO
reviewers: [Dev]
version: 0.1.0
status: draft
last_updated:
approved_by: ""
approved_at: ""
depends_on: [03-02]
feeds: [05-01, 06-00, 13-03]
id_prefix: [CAP]
gate: G2
in_handover: true
confidence: low
---

# [Tên dự án] — Tech Feasibility Brief

> **Viết ngay sau `03-02`, không chờ tới cuối phase 03.** File này chạy song song với `03-03`/`03-04`:
> trong lúc bạn kiểm chứng nhu cầu, Dev kiểm chứng công nghệ. Cả hai đều là điều kiện đóng cổng G2.
>
> **Đây KHÔNG phải tài liệu kỹ thuật.** Bạn không đánh giá công nghệ — bạn liệt kê **năng lực** mà concept
> đã chọn phụ thuộc vào, và đặt câu hỏi. Dev trả lời qua `tech-input/TECH-00_FEASIBILITY_SCREEN.md`.
>
> Lý do file này tồn tại: nếu một năng lực cốt lõi không làm được, dự án phải dừng **ở đây** — trước khi
> tiêu phase 04 nghiên cứu người dùng và phase 05 viết PRD.

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


## 1. Concept đang xét

| Trường | Nội dung |
| --- | --- |
| Concept đã chọn | `CPT-xxx` — [tên] |
| Câu một dòng | |
| Nguồn | `03-02_CONCEPT_CANDIDATES.md` mục 5 |

## 2. Năng lực cốt lõi mà concept phụ thuộc

Một `CAP` là **một việc sản phẩm phải làm được**, mô tả bằng ngôn ngữ người dùng, không bằng ngôn ngữ công nghệ.
Viết *"nhận ra món ăn từ ảnh chụp bữa cơm"*, không viết *"dùng CoreML"* — chọn công nghệ là việc của Dev.

| `CAP` | Năng lực — sản phẩm phải làm được gì | Cốt lõi hay phụ | Không có thì sao | `FEAT` liên quan |
| --- | --- | --- | --- | --- |
| `CAP-001` | | Cốt lõi / Phụ | sản phẩm vô nghĩa / vẫn dùng được nhưng yếu / chỉ mất một tính năng | |

**Cột "Cốt lõi hay phụ" là cột quan trọng nhất của cả file.** Một `CAP` cốt lõi không khả thi thì dự án dừng.
Một `CAP` phụ không khả thi thì chỉ cắt phạm vi. Đừng gắn nhãn cốt lõi cho mọi thứ — làm vậy thì cột này
mất tác dụng phân loại.

## 3. Câu hỏi cho Dev

Mỗi `CAP` phải có **ít nhất một câu hỏi trả lời được bằng có hoặc không**, kèm ngưỡng cụ thể.
Câu hỏi mơ hồ nhận về câu trả lời mơ hồ.

| `DQ` | `CAP` | Câu hỏi | Ngưỡng chấp nhận được | Vì sao cần biết bây giờ |
| --- | --- | --- | --- | --- |
| `DQ-001` | `CAP-001` | | | |

Ví dụ câu hỏi đúng và sai:

| Sai | Đúng |
| --- | --- |
| *"Nhận diện ảnh có làm được không?"* | *"Nhận ra được ít nhất 60% món ăn Việt phổ biến từ ảnh chụp bằng camera điện thoại, chạy trên máy, không cần mạng — được không?"* |
| *"Đồng bộ có khó không?"* | *"Hai máy cùng tài khoản sửa cùng một bản ghi khi offline, khi có mạng lại thì giải quyết xung đột thế nào, và mất bao lâu để làm?"* |

Ghi mọi `DQ` ở đây vào `docs/13-handover/13-02_DEV_QUESTION_LOG.md` để không mất dấu.

## 4. Ràng buộc phi công nghệ đã biết

Những thứ Dev cần biết trước khi trả lời, mà không ai khác nói cho Dev.

| Loại | Nội dung | Nguồn |
| --- | --- | --- |
| Ngân sách hạ tầng mỗi tháng | | |
| Chấp nhận gọi dịch vụ ngoài không | | `00-02_SCOPE_LOCK.md` |
| Dữ liệu người dùng được rời khỏi máy không | | |
| Mốc thời gian mong muốn | | `00-01_PROJECT_BRIEF.md` |
| Người làm — mấy Dev, nền tảng nào | | |

Điều nào chưa biết thì gắn `[ASM]` và ghi vào `_ASSUMPTION_REGISTER.md`. **Không tự đặt ngân sách hộ ai.**

## 5. Phán quyết từ Dev

Điền sau khi nhận `tech-input/TECH-00_FEASIBILITY_SCREEN.md`. **Cột phán quyết do Dev quyết, không phải bạn.**

| `CAP` | Phán quyết | Điều kiện kèm theo | Chi phí / công sức thô | Nguồn |
| --- | --- | --- | --- | --- |
| `CAP-001` | KHẢ THI / KHẢ THI CÓ ĐIỀU KIỆN / KHÔNG KHẢ THI / CHƯA TRẢ LỜI | | | `TECH-00` ngày … |

Ba nhãn có nghĩa khác nhau, đừng gộp:

| Phán quyết | Nghĩa | Việc phải làm |
| --- | --- | --- |
| **KHẢ THI** | làm được, trong ngân sách và mốc thời gian đã nêu ở mục 4 | đi tiếp |
| **KHẢ THI CÓ ĐIỀU KIỆN** | làm được nhưng phải đánh đổi — hạ ngưỡng, cần mạng, tốn tiền hạ tầng, hoặc lùi mốc | ghi điều kiện thành `[DEC]`, sửa `00-02_SCOPE_LOCK` nếu đổi phạm vi |
| **KHÔNG KHẢ THI** | không làm được ở mức đã nêu, kể cả khi hạ ngưỡng | xem mục 6 |
| **CHƯA TRẢ LỜI** | Dev chưa nghiên cứu xong | **cổng G2 chưa đủ điều kiện xét** |

## 6. Quyết định

Chỉ ghi mục này khi mục 5 không còn ô `CHƯA TRẢ LỜI`.

| Trường | Nội dung |
| --- | --- |
| `DEC` ID | |
| Kết luận | ĐI TIẾP / ĐI TIẾP CÓ ĐIỀU KIỆN / XOAY CONCEPT / DỪNG DỰ ÁN |
| Lý do | |
| `CAP` nào quyết định kết luận này | |
| Phạm vi phải sửa lại | |

**Quy tắc dừng:** có ít nhất một `CAP` **cốt lõi** nhận phán quyết **KHÔNG KHẢ THI** → không được đi sang
phase 04. Hai lựa chọn hợp lệ: **xoay concept** (quay lại `03-02`, chọn concept khác không phụ thuộc `CAP`
đó) hoặc **dừng dự án** (ghi `DEC` vào `_DECISION_LOG.md`).

Lựa chọn **không** hợp lệ: đi tiếp và hy vọng tìm được cách sau. Đó chính là cách một dự án tiêu sáu tháng
để dựng tài liệu cho một sản phẩm không dựng được.

Dừng ở đây là thắng. Bạn vừa tiết kiệm phase 04 và phase 05.

## 7. Điều chưa biết còn lại

| Điều chưa biết | Ảnh hưởng nếu đoán sai | Khi nào sẽ biết | Nhãn |
| --- | --- | --- | --- |
| | | | `[ASM]` / `[HYP]` |

## 8. Nguồn phương pháp

| Nguồn | Áp dụng ở mục nào |
| --- | --- |
| `references/` của skill này | |
| Skill chiều sâu đã dùng | |
| `tech-input/TECH-00_FEASIBILITY_SCREEN.md` phiên bản … ngày … | mục 5 |

## Thuật ngữ dùng trong tài liệu này

Chép nghĩa một câu từ `docs/_GLOSSARY.md` mục *Thuật ngữ chuyên môn*, và nghĩa của tiền tố mã từ
`docs/_ID_REGISTRY.md`. Chỉ liệt kê thứ **thật sự xuất hiện** trong tài liệu này.

| Thuật ngữ / tiền tố mã | Nghĩa một câu |
| --- | --- |
| | |

> Bảng này không phải để người trong nghề đọc — nó dành cho người ở vai trò khác đang phải duyệt tài liệu
> này. `validate_docs.py` đối chiếu: dùng mà không liệt kê là **LỖI**; liệt kê mà không dùng là cảnh báo.

<!-- QUALITY-GATE-MANIFEST:START
# Nguồn chân lý DUY NHẤT cho G2 phần tài liệu này. KHÔNG chép khối này vào file đầu ra ở docs/.
doc: 03-05_TECH_FEASIBILITY_BRIEF
gate: G2
required_major:
  - "0. Đọc nhanh"
  - "1. Concept đang xét"
  - "2. Năng lực cốt lõi mà concept phụ thuộc"
  - "3. Câu hỏi cho Dev"
  - "4. Ràng buộc phi công nghệ đã biết"
  - "5. Phán quyết từ Dev"
  - "6. Quyết định"
  - "7. Điều chưa biết còn lại"
  - "8. Nguồn phương pháp"
  - "Thuật ngữ dùng trong tài liệu này"
required_minor:
  {}
quality_checks:
  - "Mục 2 có ít nhất 1 CAP, và mỗi CAP được gắn nhãn Cốt lõi hoặc Phụ — không để trống"
  - "Mỗi CAP mô tả bằng ngôn ngữ NĂNG LỰC, không nêu tên công nghệ, thư viện, hay kiến trúc"
  - "Mỗi CAP cốt lõi có ít nhất 1 DQ ở mục 3, và DQ đó có ngưỡng chấp nhận được cụ thể"
  - "Mọi DQ ở mục 3 đã có dòng tương ứng ở 13-02_DEV_QUESTION_LOG.md"
  - "Mục 4 không có dòng nào bị bỏ trắng mà không gắn [ASM]"
  - "Mục 5 điền từ tech-input/TECH-00, ghi rõ phiên bản và ngày nhận — không do PO hoặc AI tự phán quyết"
  - "Mục 6 chỉ được ghi khi mục 5 không còn ô CHƯA TRẢ LỜI"
  - "Nếu có CAP cốt lõi KHÔNG KHẢ THI: mục 6 phải là XOAY CONCEPT hoặc DỪNG DỰ ÁN, và có DEC ở _DECISION_LOG.md"
QUALITY-GATE-MANIFEST:END -->
