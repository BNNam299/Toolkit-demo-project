---
doc_id: 12-01
title: Prototype Build Spec (Figma)
phase: 12-prototype
skill: figma-prototype-spec
profile: Bắt buộc
owner: Designer
reviewers: []
version: 0.1.0
status: draft
last_updated:
approved_by: ""
approved_at: ""
depends_on: [12-00, 08-01, 08-02, 08-03, 09-06]
feeds: [12-03]
id_prefix: []
gate: G10
in_handover: true
confidence: low
---

# [Tên dự án] — Prototype Build Spec

> **File này là danh sách công việc cho người — hoặc cho agent — sẽ dựng.**
> Viết đủ để người chưa đọc toàn bộ tài liệu vẫn dựng đúng.
> Nhánh dựng đã chọn ở `12-00` mục 7. Dù nhánh nào, file này **vẫn phải viết**: nó là căn cứ đối chiếu ở `12-03`.

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


## 0. Nhánh dựng và nguồn thành phần

| Trường | Nội dung | Nguồn |
| --- | --- | --- |
| Nhánh dựng | **A. Pencil + Agent** / **B. Figma dựng tay** | `12-00` mục 7, kèm `DEC` |
| Hệ thiết kế dùng | đường dẫn file, hoặc **dựng mới từ `12-02`** | `design-system/_MANIFEST.md` |
| Bảng phủ đã điền chưa | Có / Chưa — **chưa thì dừng, điền trước** | `design-system/_MANIFEST.md` mục 4 |
| Số thành phần phải dựng mới | | `design-system/_MANIFEST.md` mục 4 |
| Hướng thiết kế đã chốt | | `12-00` mục 3 |

**Nếu nhánh A:** ba thứ agent **không được quyết** — danh sách màn (đóng ở `08-01`), bố cục (đóng ở `08-03`),
câu chữ (đóng ở `09-06`). Việc của agent là **lắp từ hệ thiết kế**, không phải thiết kế. Component phải gọi
đúng tên trong `design-system/_MANIFEST.md` mục 3, **không vẽ một thành phần na ná mới** — thứ trông giống hệ
mà không phải instance của hệ là thứ sẽ không đổi theo khi hệ đổi.

## 1. Quy ước đặt tên frame
> **Bắt buộc khớp mã tài liệu.** Không khớp thì bước đối chiếu ở `12-03` thành thủ công và sẽ không ai làm.

```
SCR-012 · Kết quả phân tích · ST-041 Mặc định
SCR-012 · Kết quả phân tích · ST-044 Lỗi mạng
```

**Mã ba chữ số, giống `08-02`.** Viết `ST-01` thay vì `ST-041` là tên frame không khớp mã, và
`.claude/scripts/check_build.py` sẽ báo sai — đó là lỗi hay gặp nhất ở bước này.

## 2. Danh sách frame bắt buộc
> **Mỗi ô trong `08-02` state matrix là một frame.** Không gộp, không bỏ trạng thái vì "chắc giống nhau".

| # | Tên frame | `SCR` | `ST` | `FLOW` dẫn tới | Ưu tiên dựng |
| --- | --- | --- | --- | --- | --- |

**Tổng số frame phải dựng:** ___

## 3. Chi tiết từng frame
### SCR-001 · [tên] · ST-001
| Trường | Nội dung |
| --- | --- |
| Vào từ đâu | |
| Đi tới đâu | |
| Dữ liệu hiển thị lấy từ đâu | |
| CTA chính | `CPY-` |
| CTA phụ | `CPY-` |
| **Mọi chuỗi văn bản** | `CPY-001`, `CPY-002` |
| **Đường thoát** | |

> **Không Lorem Ipsum.** Chữ thật lấy từ `09-06` theo mã `CPY`.

## 4. Lô dựng và điểm dừng nghiệm thu
> Dựng **theo flow**, không theo thứ tự mã màn hình. Dựng trọn một flow rồi bấm thử từ đầu tới cuối sẽ
> phát hiện thiếu sót nhanh hơn dựng rời từng màn.
>
> **Một lô một lượt.** Dựng xong một lô thì dừng, xuất ảnh, chạy `check_build.py`, chờ người dùng nghiệm thu.
> Đây là bản sao của quy tắc *một tài liệu một lượt* áp cho việc dựng.

| Lô | `FLOW` hoặc nhóm `FEAT` | Frame thuộc lô | Số frame | Trạng thái | Người nghiệm thu |
| --- | --- | --- | --- | --- | --- |
| 1 | | | | chưa dựng / đã dựng / đã nghiệm thu | |

**Lô đầu tiên nên là luồng cốt lõi**, và nên chứa những màn *"Chốt trước"* ở `12-00` mục 6 — vì đó là lô
định hình phong cách cho các lô sau. Lô một chưa nghiệm thu thì không dựng lô hai.

Sau mỗi lô, báo cáo đúng bốn dòng:

```
Lô <n> — <FLOW>: đã dựng <x>/<y> frame
check_build.py: <màn thiếu> · <màn thừa> · <trạng thái thiếu> · <tên frame sai mã>
Thành phần phải dựng mới trong lô này: <liệt kê, hoặc "không có">
Chỗ tôi phải tự quyết vì tài liệu không nói rõ: <liệt kê, hoặc "không có">
```

Dòng cuối là dòng quan trọng nhất. Mỗi mục trong đó là một chỗ `08-03` hoặc `09-06` còn thiếu — sửa ngược
vào tài liệu qua `CHG`, đừng để nó chỉ tồn tại trong bản đã dựng.

## 5. Liên kết prototype
| Từ frame | Tương tác | Tới frame | Hiệu ứng |
| --- | --- | --- | --- |

## 6. Nguồn phương pháp

## Thuật ngữ dùng trong tài liệu này

Chép nghĩa một câu từ `docs/_GLOSSARY.md` mục *Thuật ngữ chuyên môn*, và nghĩa của tiền tố mã từ
`docs/_ID_REGISTRY.md`. Chỉ liệt kê thứ **thật sự xuất hiện** trong tài liệu này.

| Thuật ngữ / tiền tố mã | Nghĩa một câu |
| --- | --- |
| | |

> Bảng này không phải để người trong nghề đọc — nó dành cho người ở vai trò khác đang phải duyệt tài liệu
> này. `validate_docs.py` đối chiếu: dùng mà không liệt kê là **LỖI**; liệt kê mà không dùng là cảnh báo.

<!-- QUALITY-GATE-MANIFEST:START
# Nguồn chân lý DUY NHẤT cho G10 phần tài liệu này. KHÔNG chép khối này vào file đầu ra ở docs/.
doc: 12-01_PROTOTYPE_BUILD_SPEC
gate: G10
required_major:
  - "0. Đọc nhanh"
  - "1. Quy ước đặt tên frame"
  - "2. Danh sách frame bắt buộc"
  - "3. Chi tiết từng frame"
  - "0. Nhánh dựng và nguồn thành phần"
  - "4. Lô dựng và điểm dừng nghiệm thu"
  - "5. Liên kết prototype"
  - "6. Nguồn phương pháp"
  - "Thuật ngữ dùng trong tài liệu này"
required_minor:
  {}
quality_checks:
  - "Số frame bằng số ô có giá trị trong state matrix 08-02"
  - "Tên frame khớp mã SCR và ST — điều kiện G10"
  - "Mọi chuỗi văn bản trích CPY từ 09-06, không Lorem Ipsum"
  - "Mục 0 ghi rõ nhánh dựng đã chọn ở 12-00 và có DEC"
  - "Có hệ thiết kế sẵn thì bảng phủ design-system/_MANIFEST.md mục 4 đã điền TRƯỚC khi dựng frame đầu tiên"
  - "Mã ST và SCR trong tên frame là ba chữ số, khớp 08-02 — không viết ST-01 thay cho ST-041"
  - "Thứ tự dựng theo flow, không theo mã màn hình"
  - "Mục 4 chia thành lô, mỗi lô có điểm dừng nghiệm thu — không dựng cả bộ trong một lượt"
QUALITY-GATE-MANIFEST:END -->
