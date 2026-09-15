---
description: Chuỗi 14 phase Pipeline v2 — từ khởi tạo tới gói bàn giao Dev. Mỗi lượt một tài liệu.
allowed-tools: Read, Write, Edit, Grep, Glob, Bash, WebSearch, WebFetch
---

# /design-docs

Sinh tài liệu sản phẩm theo Pipeline v2. Phạm vi kết thúc ở **gói bàn giao Dev**.
Không sinh spec cấp feature, không viết code, **không dựng UI** — prototype dựng tay trong Figma.

## Usage

```
/design-docs <TênDựÁn>                  bắt đầu hoặc tiếp tục
/design-docs <TênDựÁn> --continue       tiếp tục từ chỗ dừng
/design-docs <TênDựÁn> --phase 06       nhảy tới phase cụ thể (chỉ khi phase trước đã đóng cổng)
/design-docs <TênDựÁn> --status         chỉ báo cáo trạng thái, không viết gì
```

## Bước 0 — Luôn làm đầu mỗi lượt

1. Đọc `CLAUDE.md`.
2. **Nếu `CLAUDE.md` còn chỗ chưa điền** — dấu hiệu là còn dấu ngoặc nhọn như `<TÊN DỰ ÁN>`, `<MÔ TẢ>`,
   `<iOS / Android / cả hai>` — thì đây là lần chạy đầu tiên. Xem mục **Lần chạy đầu tiên** ngay dưới.
3. Đọc `docs/_INDEX.md` — profile đang dùng, phase hiện tại, cổng đã đóng, trạng thái từng tài liệu.
4. Nếu `_INDEX.md` mục 1 chưa ghi profile: hỏi người dùng chọn **Lean / MVP / Full** rồi ghi vào.
5. Báo cáo ngắn: đang ở phase nào, tài liệu tiếp theo là gì, tài liệu đó phụ thuộc file nào và các file đó đã `approved` chưa.

## Lần chạy đầu tiên — tự điền CLAUDE.md

Người dùng **không phải sửa file cấu hình bằng tay**. Phát hiện `CLAUDE.md` còn chỗ trống thì tự làm việc này
trước khi viết tài liệu nào.

Nói rõ với người dùng là bạn sẽ hỏi vài câu để điền hồ sơ dự án, rồi hỏi **từng câu một, không hỏi dồn**:

| # | Hỏi gì | Điền vào |
| --- | --- | --- |
| 1 | Dự án tên gì? Chưa có tên chính thức thì đặt tạm theo lĩnh vực, đổi sau được. | `CLAUDE.md` **Tên**, và `_INDEX.md` mục 1 |
| 2 | Làm cho nền tảng nào — iOS, Android, hay cả hai? | `CLAUDE.md` **Nền tảng** |
| 3 | Mô tả app trong một câu. Chưa rõ thì mô tả lĩnh vực cũng được. | `CLAUDE.md` **Mô tả một câu** |
| 4 | Đã quyết định sẽ làm app này chưa, hay còn đang cân nhắc? | quyết `profile` — xem quy tắc dưới |

**Quy tắc chọn profile từ câu 4:**

- Còn đang cân nhắc, chưa chắc có làm → **Lean** (phase 00–03, khoảng 12 tài liệu). Giải thích cho người
  dùng: chạy tới cổng G2 để biết cơ hội có đáng làm không, chưa cam kết gì.
- Đã quyết làm, đây là MVP → **MVP** (bỏ tài liệu `Có điều kiện`, khoảng 38 tài liệu).
- Nhiều người tham gia, hoặc sản phẩm đã qua MVP → **Full** (mọi tài liệu).

Không chắc thì **đề xuất Lean** và nói rõ vì sao: đổi từ Lean sang MVP về sau chỉ là sửa một dòng, còn viết
PRD đầy đủ cho một ý tưởng có thể bị bỏ trong hai tuần là lãng phí.

Sau khi có đủ bốn câu trả lời:

1. Sửa `CLAUDE.md` — thay bốn chỗ trống bằng câu trả lời. **Không đụng vào phần quy tắc phía dưới.**
2. Ghi vào `docs/_INDEX.md` mục 1: tên dự án, nền tảng, profile kèm lý do chọn, ngày bắt đầu, và phiên bản
   bộ mẫu lấy từ `.claude/KIT_MANIFEST.md`.
3. Báo cho người dùng biết đã điền gì, rồi **mới** bắt đầu phase 00.

Bốn câu trên là tập con của những câu `00-01_PROJECT_BRIEF` sẽ hỏi, nên đừng hỏi lại — dùng luôn câu trả lời
đã có và hỏi tiếp phần còn thiếu.

## Chuỗi 14 phase

| Phase | Thư mục | Skill | Cổng | Số tài liệu |
| --- | --- | --- | --- | --- |
| 00 | `docs/00-khoi-tao/` | `doc-orchestrator` | G0 | 2 |
| 01 | `docs/01-market/` | `market-niche-scout` | G1 | 2 |
| 02 | `docs/02-competitor/` | `competitor-intel` | G1 | 4 |
| 03 | `docs/03-opportunity/` | `opportunity-validator` | G2 | 5 |
| 04 | `docs/04-user/` | `user-research-synthesizer` | G3 | 7 |
| 05 | `docs/05-prd/` | `prd-architect` | G4 | 3 |
| 06 | `docs/06-breakdown/` | `product-breakdown` | G5 | 6 |
| 07 | `docs/07-structure/` | `ux-structure-architect` | G6 | 5 |
| 08 | `docs/08-screens/` | `screen-inventory-wireframe` | G7 | 4 | ← wireframe là HTML ở `wireframes/` |
| 09 | `docs/09-growth/` | `growth-and-copy` | G8 | 7 |
| 10 | `docs/10-measurement/` | `measurement-designer` | G8 | 3 |
| 11 | `docs/11-evaluation/` | `design-quality-auditor` | G9 | 3 |
| 12 | `docs/12-prototype/` | `figma-prototype-spec` | G10 | 4 |
| 13 | `docs/13-handover/` | `dev-handover` | G11 | 4 |

**Đầu phase 01, hỏi người dùng một lần:** tự đào hay để họ dùng Codex/OpenCode đào rồi nạp về. Chọn
phương án hai thì viết `research-raw/thu-hoach/_BRIEF.md`, ghi sổ đổi công cụ, rồi **dừng phiên**. Chi tiết
ở Step 1 của skill `market-niche-scout`.

Phase 01 và 02 chạy song song được. Phase 09 và 10 chạy song song được. Còn lại tuần tự.

**Hai chỗ có việc của Dev chạy song song, đừng chờ tuần tự:**

| Trong phase | Viết tài liệu này rồi gửi Dev ngay | Trong lúc Dev nghiên cứu thì làm gì | Dev trả về |
| --- | --- | --- | --- |
| 03 | `03-05_TECH_FEASIBILITY_BRIEF` — viết ngay sau `03-02` | chạy `03-03`, `03-04` kiểm chứng nhu cầu | `TECH-00` → điền vào `03-05` mục 5 |
| 06 | `06-00_FEATURE_BRIEF_FOR_DEV` — tài liệu đầu tiên của phase | chạy `06-01` → `06-05` | `TECH-02`…`TECH-05` |

Thứ tự viết trong phase 03 **không theo số**: `03-01` → `03-02` → `03-05` → `03-03` → `03-04`.

## Vòng lặp cho mỗi tài liệu

**Trước tiên chạy Lớp 1 của giao thức ba lớp ở `CLAUDE.md` mục *Giao thức bắt buộc cho mỗi tài liệu*** —
in khối khai báo, chờ người dùng gật. Rồi mới gọi skill.

Gọi skill phụ trách phase đó. Skill tự chạy 6 bước của nó: nạp `_depth` → kiểm đầu vào → đọc phương pháp →
viết một tài liệu → chạy cổng → dừng.

Viết xong thì chạy **Lớp 2** — in khối tự đếm, gồm cả dòng *"chỗ tôi diễn giải thay vì trích nguyên văn"*.
Định mức chưa đạt thì **không được ghi `status: approved`**, kể cả khi người dùng bấm Approve: báo THIẾU,
hỏi đào tiếp hay hạ định mức, hạ thì ghi `DEC`.

Sau khi skill xong, **dừng lại** và hỏi:

```
Tài liệu: 06-02 — Yêu cầu chức năng (Functional Requirements)
gate-check tài liệu: PASS

Cổng G5 — Yêu cầu đã phân rã (chạy sau phase 06): CHƯA ĐỦ ĐIỀU KIỆN XÉT
  còn thiếu: 06-03 Yêu cầu phi chức năng · 06-04 Quy tắc nghiệp vụ · 06-05 Nhu cầu quyền và dữ liệu

ID mới cấp:
  FR-012  hiển thị cảnh báo khi vượt hạn mức ngày
  FR-013  cho phép sửa bản ghi trong 24 giờ
  FR-014  tự động lưu nháp sau 5 giây không thao tác

Mâu thuẫn phát hiện:
  FR-009 (chỉ sửa được trong 1 giờ) mâu thuẫn với BR-003 (quy tắc: cho sửa trong 24 giờ)

Approve  — ghi status: approved, cập nhật _INDEX, sang tài liệu tiếp theo
Modify   — nói chỗ cần sửa
Pause    — dừng ở đây
```

**Mã trần là không đủ.** Người dùng không nhớ `06-02` hay `G5` nghĩa là gì, và không nhớ `FR-014` nói gì.
Mỗi mã phải kèm nghĩa hoặc kèm nội dung một dòng — quy tắc đầy đủ ở `CLAUDE.md` mục *Gọi tên tường minh*,
bảng tra ở `docs/_GLOSSARY.md`.

**Không tự sang tài liệu tiếp theo khi chưa được Approve.**

## Quy tắc không được vi phạm

- **Một tài liệu một lượt.** Không viết hai tài liệu trong cùng một lượt.
- **Giao thức ba lớp chạy cho TỪNG tài liệu**, không phải một lần đầu phiên. Quên Lớp 1 ở tài liệu thứ tư
  thì tài liệu thứ tư đã sai quy trình.
- **Định mức là số, không phải lời khuyên.** Bảng ở `CLAUDE.md`; script `validate_docs.py` đếm độc lập.
- **Mọi mã nói với người dùng phải kèm nghĩa.** `06-02` → `06-02` (Yêu cầu chức năng). `DEC-006` → kèm
  một câu nói rõ đã quyết gì. Không bắt người dùng tự tra.
- **Chỉ file `approved` được dùng làm đầu vào.** Thiếu thì dừng và báo.
- **Cổng phủ nhiều tài liệu.** Sau mỗi tài liệu, cổng thường `CHƯA ĐỦ ĐIỀU KIỆN XÉT` — đó là bình thường, không phải lỗi.
- **Cổng cascade.** Cổng chưa đóng thì không sang phase sau. Bỏ cổng phải ghi lý do vào `_INDEX.md` mục 6.
- **Không sửa file `approved`.** Đi qua `CHG` ở `docs/_CHANGE_LOG.md`.
- **Không khai báo công nghệ.** Kiến trúc, API, schema thuộc Dev, nộp qua `tech-input/`.
- **Không tự phán quyết khả thi.** Cột phán quyết ở `03-05` mục 5 và `06-00` mục 3 chỉ điền từ `tech-input/`,
  ghi rõ file và ngày nhận. AI đoán "cái này chắc làm được" là vi phạm nặng nhất trong cả bộ.
- **Nghiên cứu công nghệ đứng trước quyết định làm sản phẩm**, không phải sau khi viết xong PRD.
- **Không dựng UI.** Phase 12 viết spec, người dựng tay trong Figma. Nhánh dựng bằng AI (Pencil) chỉ mở
  khi có `DEC` ở `12-00` mục 7 — xem `_depth/12-prototype/pencil-design/`.
- **Không bịa.** Không nguồn thì ghi **Không công bố**.

## Ba điểm dừng đáng chú ý

**Cổng G2 sau phase 03 — cổng này có HAI điều kiện dừng độc lập, không phải một.**

*Điều kiện nhu cầu:* Need Score không đạt 25/35 → **dừng dự án**.

*Điều kiện công nghệ:* có `CAP` **cốt lõi** nhận phán quyết **KHÔNG KHẢ THI** trong
`tech-input/TECH-00_FEASIBILITY_SCREEN.md` → **dừng dự án hoặc xoay concept**. Không được đi sang phase 04.

Cả hai đều ghi `DEC` vào `_DECISION_LOG.md`. Dừng ở đây là thắng — vừa tiết kiệm phase 04 nghiên cứu người
dùng và phase 05 viết PRD.

Còn `CAP` nào ở trạng thái `CHƯA TRẢ LỜI` thì cổng là **CHƯA ĐỦ ĐIỀU KIỆN XÉT**, không phải FAIL — đang chờ Dev.

**Cổng G7 sau phase 08.** State matrix còn ô `?` thì không đi tiếp. Đây là chỗ số màn hình thường thiếu
40–60% nếu vẽ trước khi kiểm kê.

**Phase 12 có lệnh riêng: `/design-ui`.** Nó hỏi công cụ (Pencil / Figma), dựng theo lô, dừng cho người
dùng nghiệm thu từng lô. Chi tiết ở `.claude/commands/design-ui.md` — markdown thuần, Codex và OpenCode
đọc và làm theo được y hệt.

**Cổng G10 sau phase 12 — có một điểm dừng nữa trước khi dựng.** `12-00_UI_RESEARCH` phải `approved`
trước khi `12-01` bắt đầu. Nó cần ảnh tham chiếu UI ở `research-raw/moodboard/`, nên **đầu phase 12 hỏi
người dùng một lần** giống đầu phase 01: tự đi tìm, hay để họ dùng Codex/OpenCode + KimiBridge thu về.
Chọn phương án hai thì ghi sổ đổi công cụ rồi **dừng phiên**.

Sau khi bạn dựng Figma xong, quay lại chạy đối chiếu:

```
Tôi đã dựng xong Figma. Chạy 12-03_PROTOTYPE_REVIEW: màn thiếu, màn thừa,
trạng thái thiếu, chữ lệch so với 09-06_COPY_DECK.
```

## Resume

`--continue` quét `docs/`, đọc `_INDEX.md`, chạy lại cổng cho từng file đã có, bỏ qua file pass, vào lại
đúng tài liệu đang dở.

File tồn tại nhưng fail cổng thì hỏi **Fix** (sửa rồi validate lại) hay **Recreate** (xoá và sinh lại).

Trạng thái nằm trên ổ đĩa chứ không nằm trong ngữ cảnh hội thoại — nên mở một phiên hoàn toàn mới rồi
`--continue` vẫn hoạt động bình thường.

## Trước khi kết thúc một buổi làm

Nếu đang bàn dở điều gì chưa ghi ra file, ghi vào `docs/_OPEN_QUESTIONS.md` và `docs/_ASSUMPTION_REGISTER.md`
trước khi thoát. **Đừng để quyết định chỉ tồn tại trong hội thoại.**
