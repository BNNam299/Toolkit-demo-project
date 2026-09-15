---
description: Dựng UI — chọn công cụ (Pencil / Figma), dựng theo lô, nghiệm thu từng lô
argument-hint: "[lô 1 | tiếp | trạng thái]"
---

# /design-ui — vòng lặp dựng UI của phase 12

> **File này là markdown thuần.** Claude Code gọi bằng `/design-ui`. Codex, OpenCode và mọi agent khác
> dùng được y hệt bằng cách nói: *"làm theo `.claude/commands/design-ui.md`"*. Một nguồn, không hai bản.

## Bước 0 — Kiểm điều kiện trước khi làm gì

Không đủ thì **dừng và báo thiếu gì**, không dựng tạm.

| Cần | Trạng thái phải có | Nếu thiếu |
| --- | --- | --- |
| `docs/08-screens/08-01_SCREEN_INVENTORY.md` | `approved` | quay lại phase 08 |
| `docs/08-screens/08-02_STATE_MATRIX.md` | `approved`, **không còn ô `?`** | quay lại phase 08 |
| `wireframes/` | có trang `flow-*.html`, `check_build.py --wireframes` 0 lỗi | quay lại `08-03` |
| `docs/09-growth/09-06_COPY_DECK.md` | `approved` | không có chữ thật thì **không dựng** |
| `docs/12-prototype/12-00_UI_RESEARCH.md` | `approved` | chạy `12-00` trước — đây là điều kiện G10 |
| `docs/12-prototype/12-01_PROTOTYPE_BUILD_SPEC.md` | `approved`, mục 4 có **bảng lô** | viết `12-01` trước |
| `design-system/_MANIFEST.md` | mục 4 (bảng phủ) đã điền, nếu có hệ sẵn | điền trước khi dựng frame đầu |

## Bước 1 — Hỏi công cụ, mỗi phiên một lần

Đọc `12-00` mục 7 xem nhánh đã chốt chưa. **Chưa chốt thì hỏi**, không tự chọn:

```
Dựng UI. Bạn muốn dùng công cụ nào phiên này?

  1. Pencil  — tôi dựng trực tiếp trong Pencil, bạn mở Pencil kiểm rồi approve
  2. Figma   — tôi không dựng; tôi tạm dừng để bạn dựng tay, xong thì gọi tôi đối chiếu

Đang chạy trên: <Claude Code / Codex / OpenCode>
Nhánh đã chốt ở 12-00 mục 7: <A Pencil / B Figma / chưa chốt>
```

Chọn Pencil mà `12-00` mục 7 **chưa có `DEC`**: ghi `DEC` vào `12-00` và `docs/_DECISION_LOG.md` **trước
khi dựng**. Nhánh này đảo quy tắc *"AI không dựng UI"* ở `CLAUDE.md`, nên nó phải là quyết định được ghi lại,
không phải một câu nói qua trong chat.

Chọn Figma: nói rõ người dùng cần làm gì, ghi vào `docs/_INDEX.md` là đang chờ dựng Figma, rồi **dừng phiên**.
Câu để tiếp tục: *"đã dựng xong, đọc Figma qua MCP"*.

Kiểm Pencil có nối được chưa (chạy đúng một lần đầu phiên): thử `pencil status` hoặc gọi một tool
`pencil__*`. Chưa nối thì báo hai đường và hỏi người dùng chọn:

| Đường nối | Cần gì | Ai trả token phần dựng |
| --- | --- | --- |
| MCP | server Pencil trong `.mcp.json` | **agent đang chạy** |
| CLI | `npm i -g @pencil.dev/cli` | AI designer trong CLI cần đăng nhập Claude Code — vẫn là **Claude**, dù bạn gõ lệnh từ Codex |

Nói rõ điều thứ hai khi người dùng đang chạy Codex để tiết kiệm token Claude, vì nó phá đúng mục đích đó.

## Bước 2 — Chọn lô

Đọc **bảng lô** ở `12-01` mục 4. Một lô = một `FLOW` hoặc một nhóm `FEAT`.

- `/design-ui lô 1` → dựng lô 1
- `/design-ui tiếp` → lô đầu tiên chưa ở trạng thái *đã nghiệm thu*
- `/design-ui trạng thái` → chỉ in bảng lô kèm trạng thái, **không dựng gì**

**Lô chưa nghiệm thu thì không dựng lô sau.** Người dùng nói *"dựng hết đi"* thì vẫn dựng một lô rồi dừng, và
nói rõ vì sao: dựng cả bộ một lượt cho ra một loạt màn rời rạc, và sai ở lô một sẽ được nhân ra tất cả các lô.

## Bước 3 — Dựng một lô

Với **từng frame** trong lô, theo đúng thứ tự người dùng đi qua:

1. Mở trang `flow-*.html` để thấy vị trí màn trong luồng, rồi mở file màn tương ứng ở `wireframes/` —
   **đó là nội dung và thứ tự, không được đổi.** Khối `.w-notes` trong file màn ghi điều hướng và đường thoát.
2. Lấy token từ `12-02`, hướng thị giác từ `12-00` mục 3–4.
3. Lấy **tên component** từ `design-system/_MANIFEST.md` mục 3. Gọi lại đúng tên đó.
4. Lấy **mọi chuỗi chữ** từ `09-06` theo mã `CPY`.
5. Đặt tên frame theo `12-01` mục 1: `SCR-012 · Kết quả phân tích · ST-041 Mặc định`. **Mã ba chữ số.**

Đường nhanh nhất nếu dùng Pencil qua MCP: nạp từng file màn HTML vào trình duyệt tích hợp của Pencil rồi
**import-to-canvas** để có sẵn cấu trúc thành layer, sau đó áp token và thay bằng component của hệ. Việc còn
lại là *áp phong cách đã chốt lên bố cục đã chốt* — ít chỗ để tự quyết, nên ít chỗ sai.

**Ba thứ không được quyết:** danh sách màn (đóng ở `08-01`) · bố cục (đóng ở `08-03` và file HTML) ·
câu chữ (đóng ở `09-06`). Thấy thiếu màn thì đi qua `08-04` (Báo cáo màn hình thiếu) và `CHG`, không thêm lặng lẽ.

**Thiếu component trong hệ:** không tự sinh trong lúc dựng màn. Ghi vào mục 5 của `design-system/_MANIFEST.md`,
xin phép, dựng bổ sung vào hệ, rồi mới dùng. Component sinh giữa lúc dựng màn gần như luôn lệch nhau.

## Bước 4 — Xuất, kiểm, báo cáo, dừng

1. Xuất ảnh từng frame để người dùng xem.
2. Ghi danh sách tên frame ra một file text hoặc dùng file `.pen`, rồi chạy:

```
python .claude/scripts/check_build.py --frames <file>
```

3. **Dán nguyên kết quả**, không tóm tắt.
4. Báo cáo đúng bốn dòng:

```
Lô <n> — <FLOW>: đã dựng <x>/<y> frame
check_build.py: <dán nguyên>
Thành phần phải dựng mới trong lô này: <liệt kê, hoặc "không có">
Chỗ tôi phải tự quyết vì tài liệu không nói rõ: <liệt kê, hoặc "không có">
```

5. **Dừng.** Hỏi Approve / Modify / Pause. Cập nhật trạng thái lô ở `12-01` mục 4.

Dòng thứ tư là dòng quan trọng nhất. Mỗi mục trong đó là một chỗ `08-03`, `12-02` hoặc `09-06` còn thiếu —
sửa ngược vào tài liệu qua `CHG`, đừng để nó chỉ tồn tại trong bản đã dựng. Để trống dòng đó khi thực tế đã
tự quyết là **che mất chỗ tài liệu cần sửa**.

## Bước 5 — Khi mọi lô đã nghiệm thu

Viết `12-03_PROTOTYPE_REVIEW` rồi chạy đủ checklist `G10` ở `docs/_GATE_CHECKLIST.md`.

## Đổi công cụ giữa chừng

Đang dựng bằng Claude mà hết token, hoặc muốn chuyển sang Codex: **không cần làm gì đặc biệt.** Trạng thái
nằm trong bảng lô ở `12-01` mục 4 và trong file `.pen`, không nằm trong hội thoại. Công cụ mới đọc
`AGENTS.md` → `12-01` mục 4 → dựng lô kế tiếp.

Ghi một dòng vào `docs/_INDEX.md` mục 8 (Sổ đổi công cụ): đổi từ gì sang gì, ở lô nào, ngày nào.
