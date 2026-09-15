#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check_build.py — đối chiếu bản ĐÃ DỰNG với 08-01 (Kiểm kê màn hình) và 08-02 (Ma trận trạng thái).

Trả lời đúng bốn câu, bằng số, không bằng cảm nhận:

  1. Màn nào tài liệu có mà chưa dựng?            (thiếu — chỗ đắt nhất)
  2. Frame nào đã dựng mà tài liệu không có?      (thừa — thường là dấu hiệu tốt, nhưng phải ghi ngược lại)
  3. Trạng thái nào của một màn còn thiếu?        (chỗ agent hay bỏ nhất: lỗi, rỗng, đang tải)
  4. Tên frame nào không khớp quy ước mã?         (không khớp thì mọi kiểm sau thành thủ công)

Cách dùng
---------
    python .claude/scripts/check_build.py --wireframes wireframes/    # phase 08, cổng G7
    python .claude/scripts/check_build.py --frames build.pen          # phase 12, cổng G10
    python .claude/scripts/check_build.py --frames frames.txt --docs docs

Hai chế độ, cùng một phép đối chiếu:

  --wireframes <thư mục>   lấy tên từ **tên file** .html trong thư mục wireframe (bỏ qua
                           `_*`, `index.html`, `flow-*.html`). Dùng ở cuối phase 08.
                           Kiểm thêm: có trang wireflow chưa · màn nào chưa vào luồng nào ·
                           mũi tên nào trống nhãn.

  --frames <file>          lấy tên từ bản đã dựng.
                           Dùng ở phase 12 sau mỗi lô dựng.

`--frames` nhận ba dạng, tự nhận biết:

  *.pen        file Pencil (JSON). Script rút mọi trường tên trong cây node.
  *.json       bất kỳ JSON nào — rút mọi giá trị của khoá "name".
  *.txt / khác mỗi dòng một tên frame. Dùng cho nhánh Figma: dán danh sách frame vào đây,
               hoặc để AI ghi ra từ Figma MCP (get_metadata).

Script này KHÔNG đọc Figma và KHÔNG đọc Pencil qua mạng. Nó chỉ đọc file. Chủ ý: kết quả phải
tái lập được, và không phụ thuộc vào phiên làm việc nào còn mở.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# KHÔNG dùng \b ở cuối: tên file là `SCR-012_ST-041_ten.html`, và `_` là word char
# nên \b không khớp giữa `2` và `_`. Dùng lookahead (?!\d) thay thế.
SCR = re.compile(r"(?<![A-Z0-9])SCR-(\d{3})(?!\d)")
ST = re.compile(r"(?<![A-Z0-9])ST-(\d{3})(?!\d)")
# mã dưới ba chữ số — lỗi hay gặp nhất, bắt riêng để báo cho rõ
SHORT = re.compile(r"(?<![A-Z0-9])(SCR|ST)-(\d{1,2})(?!\d)")

errors: list[str] = []
warnings: list[str] = []


def err(m: str) -> None:
    errors.append(m)


def warn(m: str) -> None:
    warnings.append(m)


# ─────────────────────────── đọc tài liệu ───────────────────────────

def find_doc(docs: Path, doc_id: str) -> Path | None:
    for p in docs.rglob(f"{doc_id}_*.md"):
        return p
    return None


def read_inventory(docs: Path) -> dict[str, str]:
    """08-01 mục 1 — nguồn DUY NHẤT cấp mã SCR. Trả về {SCR-001: tên màn}."""
    f = find_doc(docs, "08-01")
    if not f:
        err("Không thấy 08-01 (Kiểm kê màn hình) trong docs/ — không có gì để đối chiếu.")
        return {}
    out: dict[str, str] = {}
    for line in f.read_text(encoding="utf-8").splitlines():
        if not line.lstrip().startswith("|"):
            continue
        cells = [c.strip().strip("`") for c in line.strip().strip("|").split("|")]
        if not cells:
            continue
        m = SCR.fullmatch(cells[0])
        if m:
            name = cells[1] if len(cells) > 1 else ""
            out.setdefault(cells[0], name)
    if not out:
        err("08-01 chưa có dòng SCR nào ở mục 1 — chưa kiểm kê thì chưa đối chiếu được.")
    return out


def read_states(docs: Path) -> dict[str, set[str]]:
    """08-02 — mỗi ô có mã ST là một frame phải dựng. Trả về {SCR-001: {ST-001, ST-002}}."""
    f = find_doc(docs, "08-02")
    if not f:
        err("Không thấy 08-02 (Ma trận trạng thái) trong docs/.")
        return {}
    t = f.read_text(encoding="utf-8")
    out: dict[str, set[str]] = {}

    # nguồn 1 — ma trận ở mục 1: dòng bắt đầu bằng SCR, các ô chứa ST
    for line in t.splitlines():
        if not line.lstrip().startswith("|"):
            continue
        cells = [c.strip().strip("`") for c in line.strip().strip("|").split("|")]
        if not cells or not SCR.fullmatch(cells[0]):
            continue
        for c in cells[1:]:
            for m in ST.finditer(c):
                out.setdefault(cells[0], set()).add(f"ST-{m.group(1)}")

    # nguồn 2 — tiêu đề chi tiết ở mục 2: "### ST-001 · SCR-001 · tên"
    for line in t.splitlines():
        if not line.startswith("#"):
            continue
        s, c = ST.search(line), SCR.search(line)
        if s and c:
            out.setdefault(f"SCR-{c.group(1)}", set()).add(f"ST-{s.group(1)}")

    if not out:
        err("08-02 chưa có cặp SCR/ST nào đọc được — ma trận còn trống hoặc còn ô `?`.")
    return out


# ─────────────────────────── đọc bản đã dựng ───────────────────────────

def walk_names(node, acc: list[str]) -> None:
    if isinstance(node, dict):
        v = node.get("name")
        if isinstance(v, str):
            acc.append(v)
        for x in node.values():
            walk_names(x, acc)
    elif isinstance(node, list):
        for x in node:
            walk_names(x, acc)


def read_wireframe_dir(d: Path) -> list[str]:
    """Lấy tên màn từ TÊN FILE .html. `SCR-012_ST-041_ket-qua.html` → `SCR-012 ST-041`.

    Bỏ qua `_*.html` (template), `index.html`, và `flow-*.html` (trang wireflow) —
    những file đó không phải một ô của 08-02.
    """
    if not d.is_dir():
        err(f"Không thấy thư mục wireframe: {d}")
        return []
    names = [p.stem for p in sorted(d.glob("*.html"))
             if not p.name.startswith(("_", "index", "flow-"))]
    flows = sorted(p for p in d.glob("flow-*.html"))
    if not names:
        err(f"{d} chưa có file màn nào (bỏ qua _TEMPLATE*.html, index.html, flow-*.html).")
        return []

    # 0. Soi từng file màn TRƯỚC khi đối chiếu số lượng. Đủ màn mà màn nào cũng
    #    toàn chú thích thì vẫn là chưa xong.
    lint_screen_files(d, names)

    # 1. Wireflow là đầu ra chính của phase 08 — không có trang flow thì chưa xong
    if not flows:
        err("KHÔNG CÓ TRANG WIREFLOW — chỉ thấy file màn rời, không thấy `flow-FLOW-xxx.html`.\n"
            "    Đầu ra của phase 08 là wireflow: các màn nối bằng mũi tên có nhãn.\n"
            "    Copy `_TEMPLATE_FLOW.html` cho mỗi FLOW trong 07-05.")
    else:
        # 2. Mọi màn phải được ít nhất một trang flow nhúng
        embedded = set()
        for f in flows:
            raw = f.read_text(encoding="utf-8", errors="ignore")
            embedded.update(n for n in names if f"{n}.html" in raw)
        orphan = [n for n in names if n not in embedded]
        if orphan:
            err("MÀN KHÔNG NẰM TRONG LUỒNG NÀO — không trang flow nào nhúng:\n" +
                "\n".join(f"    {n}.html" for n in orphan) +
                "\n    Hoặc màn này mồ côi thật (xử qua 08-04), hoặc trang flow còn thiếu một nhánh."
                "\n    Trạng thái lỗi / rỗng / đang tải hay nằm ở đây — đặt vào mục"
                "\n    'Trạng thái còn lại' của trang flow kèm điều kiện vào trạng thái.")

        # 3. Mũi tên không nhãn = chưa nghĩ xong bước chuyển
        for f in flows:
            raw = f.read_text(encoding="utf-8", errors="ignore")
            blank = len(re.findall(r'class="wf-arrow"[^>]*>\s*</div>', raw))
            if blank:
                err(f"MŨI TÊN TRỐNG NHÃN — {f.name} có {blank} mũi tên không ghi 'bấm gì'.\n"
                    "    Mũi tên không nhãn là bước chuyển chưa nghĩ xong.")

    # 4. index.html phải liệt kê mọi luồng và mọi màn
    idx = d / "index.html"
    if idx.exists():
        raw = idx.read_text(encoding="utf-8", errors="ignore")
        forgotten = [n for n in names if f"{n}.html" not in raw]
        missing_flow = [f.name for f in flows if f.name not in raw]
        if missing_flow:
            warn("CHƯA VÀO TRANG CHỦ — index.html không trỏ tới trang flow: " +
                 ", ".join(missing_flow))
        if forgotten:
            warn("CHƯA VÀO THƯ VIỆN MÀN — index.html không trỏ tới:\n" +
                 "\n".join(f"    {n}.html" for n in forgotten))
    else:
        warn("Không thấy wireframes/index.html — không có trang liệt kê luồng.")
    return names


# ─────────────────── soi từng file màn ───────────────────
# Luật một câu của phase 08: TRONG KHUNG MÁY chỉ có thứ người dùng sẽ đọc và
# chạm trên app thật. Mọi thứ khác — mã truy nguyên, điều kiện, số đo — nằm ở
# khối .w-notes NGOÀI khung, hoặc không tồn tại.
#
# Vì sao phải soi bằng máy: agent rất hay "kể" thay vì "vẽ" — điền vào chỗ của
# tiêu đề một câu mô tả tiêu đề ("Tiêu đề màn, 22pt"), điền vào chỗ của nút một
# câu mô tả nút ("Hành động chính của màn"). Đọc từng file thì thấy hợp lý; xem
# cả trang wireflow thì không ai đọc được nó như một màn hình nữa.

# Comment phải đứng TRƯỚC trong nhánh: `<[^>]*>` sẽ cắt sai một comment
# có dấu ">" bên trong và để lại phần ruột thành "chữ trong màn".
TAG_RE   = re.compile(r"<!--.*?-->|<[^>]*>", re.S)
SIZE_RE  = re.compile(r"\b\d+\s*(pt|px|dp|sp|rem)\b", re.I)
CODE_RE  = re.compile(r"\b(?:FR|NFR|UC|SCR|ST|CPY|FLOW|EVT|KPI|BR|GAP|CPT|INS|PER|AC)-\d{1,3}\b")

# Cụm từ mô tả thiết kế. Xuất hiện trong khung nghĩa là đang kể, không phải vẽ.
BANNED_IN_FRAME = [
    "layout như", "layout nhu", "vùng tương tác", "hành động chính của màn",
    "tiêu đề màn", "cta chính", "cta phụ", "tương phản", "lorem ipsum",
    "placeholder", "chrome", "tôi muốn", "nội dung thật", "khối giữ chỗ",
    "empty state", "wireframe", "mô tả khối",
]


def _phone_inner(raw: str) -> str | None:
    """Cắt đúng phần bên trong <div class="w-phone">…</div>.

    Đếm độ sâu theo thẻ div: span/p/h1/input không ảnh hưởng, input là thẻ rỗng.
    Trả None khi không tìm thấy khung.
    """
    m = re.search(r'<div[^>]*class="[^"]*\bw-phone\b[^"]*"[^>]*>', raw)
    if not m:
        return None
    i, depth = m.end(), 1
    for t in re.finditer(r"<div\b|</div>", raw[i:]):
        depth += 1 if t.group().startswith("<div") else -1
        if depth == 0:
            return raw[i:i + t.start()]
    return raw[i:]          # thiếu thẻ đóng — check riêng bên dưới bắt


def lint_screen_files(d: Path, names: list[str]) -> None:
    for n in names:
        f = d / f"{n}.html"
        raw = f.read_text(encoding="utf-8", errors="ignore")

        nph = len(re.findall(r'class="[^"]*\bw-phone\b', raw))
        if nph == 0:
            err(f"{f.name}: không có khung máy `.w-phone`. Một file màn phải là MỘT màn hình.")
            continue
        if nph > 1:
            err(f"{f.name}: có {nph} khung `.w-phone`. Mỗi file đúng một màn, một trạng thái.")

        inner = _phone_inner(raw)
        if inner is None:
            continue
        if inner.count("<div") - inner.count("</div>") != 0:
            err(f"{f.name}: thẻ div trong khung không khớp — khung máy không đóng đúng chỗ.")

        if "w-notes" in inner:
            err(f"{f.name}: KHỐI GHI CHÚ NẰM TRONG KHUNG MÁY.\n"
                "    `.w-notes` phải ở NGOÀI `.w-phone`. Nằm trong thì người xem đọc nó như\n"
                "    nội dung app, và màn hình biến thành một trang toàn chú thích.")
        if "w-notes" not in raw:
            warn(f"{f.name}: không có khối `.w-notes` — thiếu 'vào từ đâu, ra đi đâu'.")

        text = TAG_RE.sub(" ", inner)

        hits = SIZE_RE.findall(text)
        if hits:
            err(f"{f.name}: có số đo trong khung máy ({', '.join(sorted(set(h for h in hits)))}).\n"
                "    Cỡ chữ, khoảng cách, độ cao là việc của `12-00` (Nghiên cứu UI), không phải phase 08.")

        codes = sorted({m.group() for m in CODE_RE.finditer(text)})
        if codes:
            err(f"{f.name}: có mã truy nguyên trong khung máy ({', '.join(codes[:6])}).\n"
                "    Mã chỉ được nằm ở nhãn `.w-tag` phía trên khung và trong `.w-notes` dưới khung.")

        low = text.lower()
        bad = [w for w in BANNED_IN_FRAME if w in low]
        if bad:
            err(f"{f.name}: trong khung máy có chữ mô tả thiết kế thay vì nội dung thật "
                f"({', '.join(bad)}).\n"
                "    Viết đúng câu người dùng sẽ đọc: \"Tiếp tục\", không phải \"Hành động chính của màn\".")


def read_frames(src: Path) -> list[str]:
    if not src.exists():
        err(f"Không thấy file bản đã dựng: {src}")
        return []
    raw = src.read_text(encoding="utf-8", errors="ignore")
    if src.suffix.lower() in {".pen", ".json"}:
        try:
            acc: list[str] = []
            walk_names(json.loads(raw), acc)
            if not acc:
                warn(f"{src.name} đọc được nhưng không thấy trường 'name' nào. "
                     "Kiểm lại đúng file chưa, hoặc xuất danh sách frame ra .txt rồi chạy lại.")
            return acc
        except json.JSONDecodeError as e:
            err(f"{src.name} không phải JSON hợp lệ ({e}). Nếu đây là danh sách tên frame thì đổi sang .txt.")
            return []
    return [ln.strip() for ln in raw.splitlines() if ln.strip() and not ln.lstrip().startswith("#")]


# ─────────────────────────── đối chiếu ───────────────────────────

def report(inv: dict[str, str], states: dict[str, set[str]], frames: list[str]) -> None:
    built: dict[str, set[str]] = {}
    unparsed: list[str] = []
    short: list[str] = []

    for name in frames:
        for m in SHORT.finditer(name):
            if not re.search(rf"(?<![A-Z0-9]){m.group(1)}-\d{{3}}(?!\d)", name):
                short.append(name)
                break
        c, s = SCR.search(name), ST.search(name)
        if not c:
            unparsed.append(name)
            continue
        built.setdefault(f"SCR-{c.group(1)}", set())
        if s:
            built[f"SCR-{c.group(1)}"].add(f"ST-{s.group(1)}")

    print(f"Tài liệu: {len(inv)} màn · {sum(len(v) for v in states.values())} trạng thái")
    print(f"Đã dựng : {len(built)} màn · {sum(len(v) for v in built.values())} trạng thái"
          f" (đọc từ {len(frames)} tên)\n")

    # 1. màn thiếu
    missing = [s for s in inv if s not in built]
    if missing:
        err("MÀN THIẾU — có trong 08-01 mà chưa dựng:\n" +
            "\n".join(f"    {s} · {inv[s]}" for s in sorted(missing)))

    # 2. màn thừa
    extra = [s for s in built if s not in inv]
    if extra:
        warn("MÀN THỪA — đã dựng mà 08-01 không có: " + ", ".join(sorted(extra)) +
             "\n    Thừa thường là dấu hiệu tốt: bạn vừa nghĩ ra màn tài liệu bỏ sót."
             "\n    Nhưng phải cập nhật ngược vào 08-01 qua 08-04 và CHG, đừng để nó chỉ tồn tại trong bản dựng.")

    # 3. trạng thái thiếu
    st_missing: list[str] = []
    for scr, need in states.items():
        if scr not in built:
            continue  # đã báo ở mục 1
        for st in sorted(need - built[scr]):
            st_missing.append(f"    {scr} · {inv.get(scr, '')} — thiếu {st}")
    if st_missing:
        err("TRẠNG THÁI THIẾU — ô trong 08-02 chưa có frame:\n" + "\n".join(st_missing) +
            "\n    Đây là chỗ bị bỏ nhiều nhất: màn mặc định thì đẹp, còn lỗi / rỗng / đang tải thì trống.")

    # 4. tên frame sai quy ước
    if short:
        err("MÃ THIẾU CHỮ SỐ — phải ba chữ số như 08-02 (ST-041, không phải ST-41):\n" +
            "\n".join(f"    {n}" for n in sorted(set(short))))
    if unparsed:
        warn(f"KHÔNG ĐỌC ĐƯỢC MÃ — {len(unparsed)} tên không chứa mã SCR:\n" +
             "\n".join(f"    {n}" for n in sorted(set(unparsed))[:20]) +
             ("\n    …" if len(set(unparsed)) > 20 else "") +
             "\n    Component, layer con và nhóm phụ nằm ở đây là bình thường."
             "\n    Nhưng FRAME màn hình không có mã thì 12-03 không đối chiếu được.")

    # trạng thái dựng thừa
    st_extra: list[str] = []
    for scr, got in built.items():
        if scr not in states:
            continue
        for st in sorted(got - states[scr]):
            st_extra.append(f"    {scr} — {st} không có trong 08-02")
    if st_extra:
        warn("TRẠNG THÁI THỪA:\n" + "\n".join(st_extra))


def main() -> int:
    ap = argparse.ArgumentParser(description="Đối chiếu wireframe hoặc bản đã dựng với 08-01 và 08-02.")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--frames", help="file .pen / .json, hoặc .txt mỗi dòng một tên frame")
    g.add_argument("--wireframes", help="thư mục chứa wireframe .html (thường là wireframes/)")
    ap.add_argument("--docs", default="docs", help="thư mục docs (mặc định: docs)")
    a = ap.parse_args()

    docs = Path(a.docs)
    if not docs.is_dir():
        print(f"LỖI: không thấy thư mục {docs}", file=sys.stderr)
        return 2

    inv = read_inventory(docs)
    states = read_states(docs)
    if a.wireframes:
        print(f"Chế độ: WIREFRAME ({a.wireframes}) — cổng G7\n")
        frames = read_wireframe_dir(Path(a.wireframes))
    else:
        print(f"Chế độ: BẢN ĐÃ DỰNG ({a.frames}) — cổng G10\n")
        frames = read_frames(Path(a.frames))
    if inv and frames:
        report(inv, states, frames)

    for m in errors:
        print(f"\nLỖI       {m}")
    for m in warnings:
        print(f"\nCẢNH BÁO  {m}")
    print(f"\n{len(errors)} lỗi · {len(warnings)} cảnh báo")

    if errors:
        print("\nCòn LỖI thì cổng chưa đóng. Sửa bản dựng, hoặc sửa ngược tài liệu qua CHG —"
              "\nnhưng phải chọn một, không để hai bên lệch nhau trong im lặng.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
