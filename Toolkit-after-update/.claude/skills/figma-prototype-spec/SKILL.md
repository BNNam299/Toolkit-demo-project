---
name: figma-prototype-spec
description: "Chốt hướng thị giác từ moodboard, viết spec để người dựng tay trong Figma, chốt design system và baseline accessibility, rồi đối chiếu bản đã dựng ngược lại tài liệu. Phase 12 của Pipeline v2, cổng G10. Phụ trách 4 tài liệu trong `docs/12-prototype/`. Chỉ dùng khi làm đúng phase này; mỗi lượt chỉ viết MỘT tài liệu rồi dừng chờ duyệt."
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

# Prototype Figma (dựng tay) — phase 12

## Tài liệu phụ trách

| doc_id | File | Mức bắt buộc | Owner | Trong gói bàn giao |
| --- | --- | --- | --- | --- |
| `12-00` | `12-00_UI_RESEARCH.md` | Bắt buộc | Designer | Có |
| `12-01` | `12-01_PROTOTYPE_BUILD_SPEC.md` | Bắt buộc | Designer | Có |
| `12-02` | `12-02_DESIGN_SYSTEM_AND_A11Y.md` | Bắt buộc | Designer | Có |
| `12-03` | `12-03_PROTOTYPE_REVIEW.md` | Bắt buộc | Designer | — |

Thư mục đích: `docs/12-prototype/`. Prefix ID skill này được cấp: `UIP`, `TOK`, `CMP`.
Cổng đóng sau phase: **G10** — checklist ở `docs/_GATE_CHECKLIST.md`.

## Thứ tự bắt buộc trong phase này

**`12-00` (UI Research) viết TRƯỚC `12-01`.** Không chốt hướng thị giác trước khi ai mở Figma thì phong
cách sẽ được chốt ngầm ở màn hình thứ ba, và những màn dựng trước đó phải dựng lại.

`12-00` cần nguyên liệu ở `research-raw/moodboard/` — ảnh tham chiếu UI mà người dùng, hoặc Codex/OpenCode
đi thu về. Mục lục ở `research-raw/moodboard/_MANIFEST.md`.

**Hỏi trước khi tự đi tìm ảnh:**

```
Moodboard cần ảnh tham chiếu UI. Bạn muốn:
  A. Tôi (Claude) tự đi tìm và mô tả — tốn token, và tôi không lưu được ảnh về máy bạn
  B. Bạn tự thu, hoặc dùng Codex/OpenCode + KimiBridge đi thu vào research-raw/moodboard/
     → tôi tạm dừng phiên, bạn thu xong quay lại, tôi đọc mục lục rồi viết 12-00
```

Chọn B thì làm đúng như `research-raw/moodboard/_MANIFEST.md` mục 4 hướng dẫn, rồi **dừng phiên**.
Đừng vừa chờ vừa viết `12-00` bằng ảnh chưa có.

Khi đã có ảnh: đọc `_MANIFEST.md` **trước**, rồi chỉ mở những ảnh cần cho kết luận đang viết. Đừng mở
cả sáu mươi ảnh — vừa tốn vừa không giúp gì.

## Hỏi nhánh dựng — việc đầu tiên của phase 12

**Hỏi trước khi viết mục nào của `12-00`.** Câu trả lời đổi cả `12-01` và `12-02`, nên hỏi sau thì phải viết lại.

```
Sang phase 12 (dựng prototype). Có hai nhánh, bạn chọn:

  A. Pencil + Agent dựng  — phù hợp app dạng tool, ít tính năng, có hệ thiết kế sẵn.
                            Tôi dựng theo từng luồng, bạn mở Pencil kiểm rồi approve, tôi dựng tiếp.
  B. Figma bạn dựng tay   — phù hợp app lớn. Tôi viết spec rồi TẠM DỪNG dự án ở đây.
                            Bạn dựng xong thì nói "đã dựng xong, đọc Figma qua MCP", tôi đối chiếu.

Hệ thiết kế có sẵn của bạn ở đâu? (đường dẫn file .pen, hoặc key file Figma, hoặc "chưa có")
```

Ghi lựa chọn vào `12-00` mục 7 kèm `DEC`, và vào `docs/_DECISION_LOG.md`. **Không tự chọn thay người dùng.**
Nhánh B là mặc định của bộ; nhánh A đảo quy tắc *"AI không dựng UI"* nên **không có `DEC` thì không được dựng**,
kể cả khi người dùng nhắc qua trong chat.

### Có hệ thiết kế sẵn

Đọc `design-system/_MANIFEST.md` **trước** khi viết `12-00`. Hệ sẵn đổi việc phải làm, không bỏ được `12-00`:

| Không có hệ sẵn | Có hệ sẵn |
| --- | --- |
| `12-00` chọn phong cách từ moodboard | `12-00` **kiểm hệ sẵn có chịu được bộ màn này không** |
| `12-02` sáng tác token và component | `12-02` **trích từ hệ sẵn**, chỉ khai báo phần thiếu |

**Bảng phủ ở `design-system/_MANIFEST.md` mục 4 phải điền trước khi dựng frame đầu tiên.** Nó đếm số thành
phần `08-03` cần mà hệ chưa có. Số đó lớn thì dựng bổ sung hệ trước — component sinh ra trong lúc dựng màn
gần như luôn lệch nhau.

Thư mục `design-system/` là **tài sản của người dùng**: đọc, không sửa. Thêm component vào hệ phải xin phép
từng lần và ghi vào mục 5 của manifest.

### Nhánh A — Pencil + Agent: vòng lặp dựng theo lô

Ba thứ **không được quyết**: danh sách màn (đóng ở `08-01`), bố cục (đóng ở `08-03`), câu chữ (đóng ở
`09-06`). Việc là **lắp từ hệ thiết kế**, không phải thiết kế. Gọi component đúng tên trong
`design-system/_MANIFEST.md` mục 3 — vẽ một thành phần na ná mới là tạo ra thứ sẽ không đổi theo khi hệ đổi.

Mỗi lô = một `FLOW` hoặc một nhóm `FEAT`, theo bảng lô ở `12-01` mục 4. **Một lô một lượt:**

1. Đọc `12-01` mục 3 cho từng frame của lô, `12-02` cho token, `09-06` cho chữ theo mã `CPY`.
2. Dựng. Đặt tên frame đúng quy ước `12-01` mục 1 — **mã ba chữ số**, khớp `08-02`.
3. Xuất ảnh để người dùng xem.
4. Chạy `python .claude/scripts/check_build.py --frames <file>` và **dán nguyên kết quả**, không tóm tắt.
5. Báo cáo bốn dòng theo khuôn ở `12-01` mục 4, rồi **dừng chờ nghiệm thu**.

Lô chưa nghiệm thu thì không dựng lô sau. Dòng *"chỗ tôi phải tự quyết vì tài liệu không nói rõ"* là dòng
quan trọng nhất trong báo cáo — mỗi mục là một chỗ `08-03` hoặc `09-06` còn thiếu, sửa ngược qua `CHG`.

Nối Pencil và các ràng buộc chi tiết: `.claude/skills/_depth/12-prototype/pencil-design/`.

### Nhánh B — Figma dựng tay: dừng rồi quay lại

Viết `12-00` → `12-01` → `12-02`, approve đủ, rồi **tạm dừng dự án** và nói rõ người dùng cần làm gì và câu
nào để tiếp tục. Ghi vào `docs/_INDEX.md` là đang chờ dựng Figma.

Khi người dùng quay lại: đọc cấu trúc frame qua Figma MCP (`get_metadata` cho cây frame,
`get_variable_defs` cho token), ghi danh sách tên frame ra một file text, chạy `check_build.py` trên file
đó, rồi mới viết `12-03`. **Không đối chiếu bằng cách đọc rồi tự đếm** — đó là chỗ dễ tóm tắt nhất.

Không có MCP thì bảo người dùng dán danh sách tên frame vào một file `.txt` và chạy `check_build.py` trên đó.

## Tài nguyên dùng chung có sẵn

`.claude/shared/DESIGN_SYSTEM_GUIDE.md` — hướng dẫn design system lấy từ app-spec, dùng làm đối chiếu khi
viết `12-02_DESIGN_SYSTEM_AND_A11Y`. Không phải bộ quy tắc bắt buộc: dự án có design system riêng thì
design system của dự án thắng, và ghi vào mục *Nguồn phương pháp* là đã tham chiếu file này ở chỗ nào.

## Step 0 — Nạp chiều sâu

Liệt kê `.claude/skills/_depth/12-prototype/`. Với mỗi thư mục con, đọc **description trong frontmatter trước**.
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

**Sở hữu:** Danh sách frame phải dựng, token, component, ngưỡng a11y, biên bản đối chiếu

**Không sở hữu:** danh sách màn (`08-01`) · bố cục (`08-03`) · câu chữ (`09-06`) · hệ thiết kế của người dùng
(`design-system/`, đọc không sửa). Mặc định **không dựng UI thay người**; nhánh A chỉ mở khi có `DEC`, và
ngay cả khi mở thì việc là **lắp từ hệ thiết kế**, không phải thiết kế

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
