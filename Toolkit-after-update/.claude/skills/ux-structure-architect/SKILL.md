---
name: ux-structure-architect
description: "Phân tích nhiệm vụ, dựng information architecture và sitemap, viết user story map, rồi vẽ UX flow phủ đủ nhánh. Phase 07 của Pipeline v2, cổng G6. Phụ trách 6 tài liệu trong `docs/07-structure/`, mở đầu bằng UX research trên ảnh màn hình đối thủ. Chỉ dùng khi làm đúng phase này; mỗi lượt chỉ viết MỘT tài liệu rồi dừng chờ duyệt."
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - Bash
  - WebSearch
  - WebFetch
---

# Kiến trúc thông tin & UX flow — phase 07

## Tài liệu phụ trách

| doc_id | File | Mức bắt buộc | Owner | Trong gói bàn giao |
| --- | --- | --- | --- | --- |
| `07-00` | `07-00_UX_RESEARCH.md` | Bắt buộc | PO | Có |
| `07-01` | `07-01_TASK_ANALYSIS.md` | Bắt buộc | Designer | — |
| `07-02` | `07-02_INFORMATION_ARCHITECTURE.md` | Bắt buộc | Designer | — |
| `07-03` | `07-03_SITEMAP.md` | Bắt buộc | Designer | — |
| `07-04` | `07-04_USER_STORY_MAP.md` | Bắt buộc | PO | Có |
| `07-05` | `07-05_UX_FLOWS.md` | Bắt buộc | Designer | Có |

**`07-00` viết TRƯỚC `07-01`.** Nó mổ xẻ ảnh màn hình đối thủ ở `research-raw/man-hinh-doi-thu/` — mục lục
ở `_MANIFEST.md` cùng thư mục, **đọc mục lục trước rồi chỉ mở ảnh cần**.

Bắt buộc đọc `04-04` và `04-06` **trước khi mở ảnh đầu tiên** — xem giao diện đối thủ trước rồi mới nghĩ về
người dùng của mình là cách chắc chắn nhất để sao chép. Mỗi mẫu quan sát được phải có quyết định
**Áp dụng / Điều chỉnh / Không dùng** kèm lý do neo vào `INS` hoặc `JTBD`; lý do *"vì đối thủ làm vậy"*
không hợp lệ.

Thư mục đích: `docs/07-structure/`. Prefix ID skill này được cấp: `PAT`, `TSK`, `IA`, `US`, `FLOW`.
Cổng đóng sau phase: **G6** — checklist ở `docs/_GATE_CHECKLIST.md`.

## Step 0 — Nạp chiều sâu

Liệt kê `.claude/skills/_depth/07-structure/`. Với mỗi thư mục con, đọc **description trong frontmatter trước**.
Chỉ mở toàn bộ nội dung của skill nào thật sự liên quan tới dự án đang làm — nạp hết mọi thứ làm loãng trọng tâm.

Khi skill chiều sâu mâu thuẫn với phương pháp gốc ở `references/`, **skill chiều sâu thắng**, nhưng phải ghi
vào mục "Nguồn phương pháp" cuối tài liệu là đã áp dụng skill nào và ở chỗ nào. Không được đổi đầu ra trong im lặng.

## Step 1 — Kiểm đầu vào

Đọc `docs/_INDEX.md`. Kiểm mọi file trong `depends_on` của tài liệu sắp viết có `status: approved` chưa.
**Chỉ file `approved` được dùng làm đầu vào.** Thiếu thì dừng và báo, không tự đi tiếp bằng file `draft`.

Nếu `tech-input/` có file liên quan mà Dev đã nộp, đọc và dùng. Thiếu thông tin kỹ thuật thì gắn `[ASM]`
vào chỗ đang thiếu và tạo `DQ` ở `docs/13-handover/13-02_DEV_QUESTION_LOG.md`. **Không suy đoán.**

## Step 2 — Đọc phương pháp

Đọc `references/method*.md` trước, rồi mọi file `.md` còn lại trong `references/`.
Danh sách file **không** được liệt kê cứng ở đây — thêm một mảng kiến thức mới chỉ là thả thêm file vào thư mục đó.

## Step 3 — Viết MỘT tài liệu

Đọc template tương ứng ở `.claude/doc-templates/`. Khối `QUALITY-GATE-MANIFEST` ở cuối template là nguồn chân lý
về các mục bắt buộc — tái tạo đủ các mục đó, **KHÔNG chép khối manifest vào file đầu ra**.

Front-matter bắt buộc: `doc_id`, `phase`, `skill`, `profile`, `owner`, `version`, `status`, `depends_on`,
`feeds`, `id_prefix`, `gate`, `in_handover`, `confidence`.

Gắn nhãn mọi mệnh đề quan trọng: `[FACT]` có nguồn · `[INSIGHT]` từ ≥2 nguồn · `[HYP]` có điều kiện bác bỏ ·
`[ASM]` có dòng ở `_ASSUMPTION_REGISTER` · `[REC]` kèm lý do · `[DEC]` có DEC ID.

## Step 4 — Cổng

Chạy **hai** phép kiểm, đừng lẫn hai cái:

**4a. Kiểm tài liệu vừa viết.** Gọi `project-docs-quality-gates` chỉ với tài liệu này: đối chiếu
`required_major`, `required_minor`, `quality_checks` trong manifest của template tương ứng.
Đây là phép kiểm bắt buộc phải PASS trước khi hỏi Approve.

**4b. Báo trạng thái cổng của phase.** Một cổng phủ **nhiều tài liệu**, có cổng phủ cả hai phase.
Sau khi viết một tài liệu, cổng gần như luôn **chưa đủ điều kiện xét** vì các tài liệu khác chưa tồn tại.

Lúc đó báo `CHƯA ĐỦ ĐIỀU KIỆN XÉT`, kèm danh sách tài liệu `Bắt buộc` còn thiếu — **không báo FAIL**.
`FAIL` chỉ dùng khi mọi tài liệu bắt buộc của cổng đã có mà checklist vẫn không tick hết.

```
Tài liệu 01-01 — Thị trường và vùng nhu cầu: gate-check PASS
Cổng G1 — Cơ hội có bằng chứng (chạy sau phase 01–02): CHƯA ĐỦ ĐIỀU KIỆN XÉT
  còn thiếu: 01-02 Sổ đào pain point · 02-01 Bản đồ đối thủ · 02-02 Mổ xẻ đối thủ ·
             02-03 Đào review người dùng · 02-04 Khoảng trống cơ hội
```

**Mã trần là không đủ.** Mỗi `doc_id`, mã cổng và ID cấp mới khi **nói với người dùng** phải kèm nghĩa
hoặc kèm nội dung một dòng — người dùng không nhớ 61 mã tài liệu và hơn 40 tiền tố. Quy tắc đầy đủ ở
`CLAUDE.md` mục *Gọi tên tường minh*; bảng tra ở `docs/_GLOSSARY.md` mục *Tra nhanh mã*.
Trong file tài liệu vẫn giữ mã trần như cũ.

Chỉ khi tài liệu cuối cùng của cổng được approve thì mới chạy đủ checklist ở `docs/_GATE_CHECKLIST.md`
và kết luận cổng đóng hay không.

## Step 5 — Dừng

Cập nhật `docs/_INDEX.md`: trạng thái tài liệu, ID mới cấp, mồ côi phát hiện được, mâu thuẫn với tài liệu khác.
Báo cáo cho người dùng và **dừng lại**. Không tự sang tài liệu tiếp theo.

## Ranh giới

**Sở hữu:** Task analysis, IA, sitemap, story map, flow

**Không sở hữu:** **Không được sinh màn hình mới.** Thiếu màn thì ghi vào `08-04_MISSING_SCREEN_REPORT.md`, SCR do 08-01 cấp

## Quy tắc không được vi phạm

- **Một tài liệu một lượt.** Không tạo hai tài liệu trong cùng một lượt làm việc.
- **Không sửa file `approved`.** Cần đổi thì qua quy trình `CHG` ở `docs/_CHANGE_LOG.md`.
- **ID không đổi, không tái sử dụng, không đánh số lại.**
- **Mã kèm nghĩa khi nói với người dùng.** `06-02` → `06-02` (Yêu cầu chức năng). `DEC-006` → kèm một câu nói rõ đã quyết gì.

**Không bịa.** Không có nguồn thì ghi **Không công bố**. Không bịa số liệu thị trường, kết quả phỏng vấn,
  kết quả usability test hay chỉ số đối thủ.
- **Không khai báo công nghệ.** Kiến trúc, API, schema thuộc Dev, nộp qua `tech-input/`.
- **Phản biện, không gật.** Thấy tính năng không gắn pain point, paywall trước khi chứng minh giá trị,
  metric không phản ánh giá trị thật, hay scope MVP phình thì phải nêu: vấn đề → rủi ro → phương án thay thế → cách kiểm chứng.
