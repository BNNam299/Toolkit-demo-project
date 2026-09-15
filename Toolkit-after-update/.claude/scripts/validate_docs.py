#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kiểm tra bộ tài liệu Pipeline v2 trước khi đóng cổng hoặc commit.

Kiểm: front-matter 13 trường · depends_on đã approved · nhãn nội dung có đăng ký ·
ID trùng và ID thiếu số · mồ côi theo chuỗi truy nguyên · **tham chiếu treo giữa các tài liệu** ·
từ cấm trong acceptance criteria · Lorem Ipsum · _INDEX khớp template ·
**định mức bằng chứng cho tài liệu phase 01–04**.

    python .claude/scripts/validate_docs.py
    python .claude/scripts/validate_docs.py --gate G5
    python .claude/scripts/validate_docs.py --strict     # cảnh báo cũng tính là lỗi

Chạy được ngoài phiên Claude. Trả mã thoát 1 nếu có LỖI.
"""
import argparse, json, re, sys
from pathlib import Path
from collections import defaultdict

FM_REQUIRED = ["doc_id","title","phase","skill","profile","owner","version","status",
               "depends_on","feeds","id_prefix","gate","in_handover","confidence"]
STATUS_OK = {"draft","in-review","approved","superseded","archived"}
LABELS = ["FACT","INSIGHT","HYP","ASM","REC","DEC"]

# (prefix cấp tại doc nào, prefix phải xuất hiện ở doc nào để không mồ côi)
CHAIN = [
    ("FEAT","05-01","UC","06-01","Tính năng không có use case"),
    ("UC","06-01","FR","06-02","Use case không có requirement"),
    ("SCR","08-01","FLOW","07-05","Màn hình không xuất hiện trong flow nào"),
]

C = dict(r="\033[31m", y="\033[33m", g="\033[32m", d="\033[2m", x="\033[0m")
if not sys.stdout.isatty(): C = {k: "" for k in C}

E, W = [], []
def err(m): E.append(m)
def warn(m): W.append(m)


def parse_fm(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m: return None, text
    fm = {}
    for line in m.group(1).split("\n"):
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip().strip('"')
    return fm, text[m.end():]


def load(docs: Path):
    out = {}
    for f in sorted(docs.rglob("*.md")):
        if f.name.startswith("_"): continue
        fm, body = parse_fm(f.read_text(encoding="utf-8"))
        if fm is None:
            err(f"{f.name}: không có front-matter"); continue
        out[fm.get("doc_id", f.name[:5])] = dict(file=f, fm=fm, body=body)
    return out


def check_frontmatter(D):
    for did, d in D.items():
        miss = [k for k in FM_REQUIRED if k not in d["fm"]]
        if miss: err(f"{d['file'].name}: thiếu front-matter {', '.join(miss)}")
        st = d["fm"].get("status")
        if st and st not in STATUS_OK:
            err(f"{d['file'].name}: status '{st}' không hợp lệ")


def check_depends(D):
    for did, d in D.items():
        if d["fm"].get("status") != "approved": continue
        dep = d["fm"].get("depends_on", "[]").strip("[]")
        for r in [x.strip() for x in dep.split(",") if x.strip()]:
            if r not in D:
                err(f"{did}: approved nhưng phụ thuộc {r} không tồn tại")
            elif D[r]["fm"].get("status") != "approved":
                err(f"{did}: approved nhưng {r} mới ở status "
                    f"'{D[r]['fm'].get('status')}' — chỉ file approved được dùng làm đầu vào")


def check_labels(D, docs: Path):
    def registered(f: Path, pre: str) -> set:
        """ID chỉ tính là đã đăng ký nếu dòng đó có nội dung thật, không phải dòng mẫu rỗng."""
        if not f.exists(): return set()
        out = set()
        for line in f.read_text(encoding="utf-8").split("\n"):
            m = re.match(rf"^\|\s*`({pre}-\d{{3}})`\s*\|(.*)$", line)
            if not m: continue
            # cột: | ID | Ngày | <NỘI DUNG> | … — dòng mẫu để trống cột nội dung
            cells = [c.strip() for c in m.group(2).split("|")]
            if len(cells) > 1 and cells[1]:
                out.add(m.group(1))
        return out

    asm_ids = registered(docs/"_ASSUMPTION_REGISTER.md", "ASM")
    dec_ids = registered(docs/"_DECISION_LOG.md", "DEC")
    for did, d in D.items():
        for m in re.finditer(r"\[ASM\]", d["body"]):
            pass
        used_asm = set(re.findall(r"`(ASM-\d{3})`", d["body"]))
        for a in used_asm - asm_ids:
            err(f"{did}: dùng {a} nhưng không có dòng ở _ASSUMPTION_REGISTER.md")
        used_dec = set(re.findall(r"`(DEC-\d{3})`", d["body"]))
        for x in used_dec - dec_ids:
            err(f"{did}: dùng {x} nhưng không có dòng ở _DECISION_LOG.md")
        if "[ASM]" in d["body"] and not used_asm:
            warn(f"{did}: có nhãn [ASM] nhưng không trích ASM ID nào")


def check_ids(D):
    seen = defaultdict(dict)          # prefix -> {id: doc}
    for did, d in D.items():
        for pid in re.findall(r"`([A-Z]{2,4})-(\d{3})`", d["body"]):
            pre, num = pid
            declared = d["fm"].get("id_prefix", "").strip("[]")
            if pre in [x.strip() for x in declared.split(",") if x.strip()]:
                key = f"{pre}-{num}"
                if key in seen[pre] and seen[pre][key] != did:
                    err(f"{key} bị cấp ở cả {seen[pre][key]} và {did} — ID phải cấp tại đúng một tài liệu")
                seen[pre][key] = did
    for pre, ids in seen.items():
        nums = sorted(int(k.split("-")[1]) for k in ids)
        gaps = [n for n in range(1, (nums[-1] if nums else 0)+1) if n not in nums]
        if gaps: warn(f"prefix {pre}: thiếu số {gaps[:5]}{'…' if len(gaps)>5 else ''} — ID bị bỏ phải archived, không bỏ trống")
    return seen


def check_dangling_refs(D, ids):
    """Tài liệu trích một ID mà ID đó chưa từng được cấp ở tài liệu sở hữu prefix.

    Đây là lỗi hay gặp nhất khi 61 tài liệu nối nhau bằng ID: 06-02 viết `UC-007`
    trong khi 06-01 mới cấp tới `UC-005`. Không ai thấy cho tới lúc bàn giao.
    """
    owner = {}                                   # prefix -> doc_id sở hữu
    for did, d in D.items():
        for pre in [x.strip() for x in d["fm"].get("id_prefix", "").strip("[]").split(",") if x.strip()]:
            owner[pre] = did

    dangling, unchecked = defaultdict(set), defaultdict(set)
    for did, d in D.items():
        for pre, num in re.findall(r"`([A-Z]{2,4})-(\d{3})`", d["body"]):
            if pre not in owner:                 # prefix chưa có tài liệu sở hữu nào tồn tại
                unchecked[pre].add(f"{pre}-{num}")
                continue
            if did == owner[pre]:                # chính tài liệu cấp ID, bỏ qua
                continue
            if f"{pre}-{num}" not in ids.get(pre, {}):
                dangling[did].add(f"{pre}-{num}")

    for did, refs in sorted(dangling.items()):
        s = sorted(refs)
        err(f"THAM CHIẾU TREO — {did} trích {', '.join(s[:8])}{' …' if len(s)>8 else ''} "
            f"nhưng ID này chưa được cấp ở tài liệu sở hữu prefix")
    for pre, refs in sorted(unchecked.items()):
        s = sorted(refs)
        warn(f"prefix {pre}: chưa có tài liệu nào sở hữu nên không kiểm được "
             f"{', '.join(s[:5])}{' …' if len(s)>5 else ''} — viết tài liệu đó rồi chạy lại")


def check_orphans(D, ids):
    for src_pre, src_doc, tgt_pre, tgt_doc, label in CHAIN:
        if src_doc not in D or tgt_doc not in D: continue
        declared = set(ids.get(src_pre, {}))
        referenced = set(re.findall(rf"`({src_pre}-\d{{3}})`", D[tgt_doc]["body"]))
        orphan = declared - referenced
        if orphan:
            err(f"MỒ CÔI — {label}: {', '.join(sorted(orphan)[:8])}"
                f"{' …' if len(orphan)>8 else ''}")
    # FR không có AC
    if "06-02" in D:
        frs = set(re.findall(r"`(FR-\d{3})`", D["06-02"]["body"]))
        ac_body = D.get("13-04", {}).get("body", "") + D["06-02"]["body"]
        no_ac = {f for f in frs if not re.search(rf"{f}\b.*?AC-\d{{3}}", ac_body, re.S)}
        if no_ac and "13-04" in D:
            err(f"MỒ CÔI — Requirement không có acceptance criteria: "
                f"{', '.join(sorted(no_ac)[:8])}{' …' if len(no_ac)>8 else ''}")
    # EVT không phục vụ KPI/FNL
    if "10-02" in D:
        b = D["10-02"]["body"]
        for row in re.findall(r"^\|\s*`(EVT-\d{3})`\s*\|(.*)$", b, re.M):
            if not re.search(r"`(KPI|FNL)-\d{3}`", row[1]):
                err(f"MỒ CÔI — {row[0]} không phục vụ KPI hay bước phễu nào")


# Định mức tối thiểu — chỉ áp cho tài liệu mà khối lượng CHÍNH LÀ chất lượng.
# (doc_id, số dòng bảng tối thiểu, mô tả)
VOLUME = [
    ("01-02", 30, "bản ghi pain point từ ≥3 loại nguồn"),
    ("02-01",  5, "đối thủ trong bản đồ"),
    ("02-02",  3, "app đã mổ xẻ bằng cách dùng thật"),
    ("02-03", 40, "review đã đào từ ≥2 app"),
    ("04-02",  5, "phiên nghiên cứu đã ghi"),
]


def count_rows(body: str) -> int:
    """Đếm dòng bảng có nội dung thật — bỏ dòng tiêu đề, dòng kẻ, dòng mẫu rỗng."""
    n = 0
    for line in body.split("\n"):
        s = line.strip()
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if not cells or all(set(c) <= set("-: ") for c in cells):   # dòng kẻ
            continue
        if sum(1 for c in cells if c) < 2:                          # dòng mẫu để trống
            continue
        n += 1
    return max(0, n - 1)                                            # trừ dòng tiêu đề


def check_volume(D):
    """Bắt tài liệu bằng chứng bị viết sơ sài — lỗi mà không cổng nào bắt được.

    Ở phase 06-08 thiếu sót lộ ra vì có nguồn nội bộ để đối chiếu. Ở phase 01-04 thì
    không có gì đối chiếu: một sổ đào pain point sơ sài trông y hệt một sổ đầy đủ.
    """
    for did, need, what in VOLUME:
        d = D.get(did)
        if not d:
            continue
        got = count_rows(d["body"])
        if got >= need:
            continue
        msg = (f"ĐỊNH MỨC — {did} mới có ~{got} dòng, định mức {need} ({what}). "
               f"Đào tiếp, hoặc hạ định mức và ghi DEC vào _DECISION_LOG.md")
        if d["fm"].get("status") == "approved":
            err(msg + " — đang là approved mà chưa đạt định mức")
        else:
            warn(msg)


def _table_rows(body: str, prefix: str):
    """Lấy các dòng bảng có ô đầu là mã `PREFIX-nnn`. Trả về list[list[str]] các ô."""
    out = []
    for line in body.split("\n"):
        s = line.strip()
        if not s.startswith("|"):
            continue
        cells = [c.strip().strip("`").strip("*") for c in s.strip("|").split("|")]
        if cells and re.fullmatch(rf"{prefix}-\d{{3}}", cells[0]):
            out.append(cells)
    return out


def _bad(d, msg):
    if d["fm"].get("status") == "approved":
        err(msg + " — đang là approved mà chưa đạt định mức")
    else:
        warn(msg)


def check_depth(D):
    """Định mức CHIỀU SÂU ở phase 06 — đọc từ bảng tổng hợp, không đoán.

    Phase 01-04 đã có định mức khối lượng. Phase 06 trước đây không có gì ép, nên một
    `06-02` viết 20 dòng vẫn qua cổng G5 miễn mỗi FR có một AC. Đây là chỗ bộ tài liệu
    mỏng đi mà không ai thấy, vì cấu trúc vẫn đúng.
    """
    NO = ("không", "chưa", "thiếu", "-", "—", "")

    # 06-02 mục 3: | FR | Phát biểu | UC | Ưu tiên | Số AC | Khả thi |
    d = D.get("06-02")
    if d:
        thin = []
        for c in _table_rows(d["body"], "FR"):
            must = any("must" in x.lower() for x in c)
            nums = [int(x) for x in c if re.fullmatch(r"\d+", x)]
            if must and nums and max(nums) < 3:
                thin.append(f"{c[0]} (Must, {max(nums)} AC)")
            elif must and not nums:
                thin.append(f"{c[0]} (Must, chưa ghi số AC)")
        if thin:
            _bad(d, "ĐỊNH MỨC CHIỀU SÂU — 06-02: mỗi FR mức Must cần ≥3 acceptance criteria.\n"
                    "    Chưa đạt: " + " · ".join(thin) +
                    "\n    Một AC cho một yêu cầu Must nghĩa là chỉ nghĩ tới đường đi thuận lợi.")

    # 06-01 mục 3: | UC | Có luồng thay thế | Có luồng ngoại lệ | Mọi nhánh có kết cục |
    d = D.get("06-01")
    if d:
        thin = []
        for c in _table_rows(d["body"], "UC"):
            if len(c) < 3:
                continue
            if any(c[i].lower().strip(" .") in NO for i in (1, 2)):
                thin.append(c[0])
        if thin:
            _bad(d, "ĐỊNH MỨC CHIỀU SÂU — 06-01: mỗi UC cần ≥1 luồng thay thế VÀ ≥1 luồng ngoại lệ.\n"
                    "    Chưa đạt: " + " · ".join(thin) +
                    "\n    UC chỉ có luồng chính thì gần như chắc chắn viết chưa xong.")

    # 06-04 mục 2: | BR | Tên | Công thức | FR | Có ví dụ | Số trường hợp biên |
    d = D.get("06-04")
    if d:
        thin = []
        for c in _table_rows(d["body"], "BR"):
            nums = [int(x) for x in c if re.fullmatch(r"\d+", x)]
            no_ex = any(x.lower().strip(" .") in NO[:3] for x in c[3:])
            if no_ex or (nums and max(nums) < 5):
                thin.append(c[0])
        if thin:
            _bad(d, "ĐỊNH MỨC CHIỀU SÂU — 06-04: mỗi BR cần ví dụ tính tay và ≥5 trường hợp biên.\n"
                    "    Chưa đạt: " + " · ".join(thin) +
                    "\n    Công thức không có ví dụ tính tay là công thức chưa ai thử.")


def check_stale_inputs(D):
    """Tài liệu đã approved mà ĐẦU VÀO của nó được sửa sau đó — nguy hiểm và vô hình.

    Đây là lỗi tôi tìm thấy trong một dự án thật: phần nghiên cứu cạnh tranh được viết
    lại hoàn toàn ở v2.0 và sản phẩm xoay hướng, nhưng persona ở section trước KHÔNG ai
    cập nhật. Kết quả: tầng người dùng mô tả một sản phẩm đã bị bỏ, và cổng tự chấm vẫn
    báo Pass vì mỗi section riêng lẻ đều đúng.
    """
    def when(d):
        v = str(d["fm"].get("last_updated", "")).strip().strip('"')
        m = re.match(r"(\d{4})-(\d{2})-(\d{2})", v)
        return tuple(int(x) for x in m.groups()) if m else None

    for did, d in sorted(D.items()):
        mine = when(d)
        if not mine:
            continue
        stale = []
        for dep in [x.strip() for x in str(d["fm"].get("depends_on", "")).strip("[]").split(",") if x.strip()]:
            dd = D.get(dep)
            if not dd:
                continue
            theirs = when(dd)
            if theirs and theirs > mine:
                stale.append(f"{dep} (sửa {'-'.join(f'{x:02d}' for x in theirs)})")
        if not stale:
            continue
        msg = (f"ĐẦU VÀO MỚI HƠN — {did} cập nhật {'-'.join(f'{x:02d}' for x in mine)} "
               f"nhưng đầu vào đã sửa sau đó: " + " · ".join(stale) +
               "\n    Đọc lại xem kết luận ở đây còn đúng không. Đổi thì ghi CHG; không đổi thì"
               "\n    cập nhật last_updated để nói rõ 'đã xem lại và vẫn đúng'.")
        if d["fm"].get("status") == "approved":
            err(msg)
        else:
            warn(msg)


def check_handover_units(D):
    """13-01 mục 6: khối JSON thứ tự thi công phải parse được và không có vòng phụ thuộc."""
    d = D.get("13-01")
    if not d:
        return
    m = re.search(r"```json\s*(\{.*?\})\s*```", d["body"], re.S)
    if not m:
        if d["fm"].get("status") == "approved":
            err("13-01 mục 6 thiếu khối ```json``` thứ tự thi công — agent lập trình không có gì để đọc.")
        return
    try:
        data = json.loads(m.group(1))
    except json.JSONDecodeError as e:
        err(f"13-01 mục 6: khối JSON không parse được ({e}). Sửa trước khi bàn giao.")
        return
    units = data.get("units") or []
    if not units:
        warn("13-01 mục 6: khối JSON parse được nhưng `units` rỗng.")
        return
    have = {u.get("id") for u in units}
    for u in units:
        for dep in u.get("depends_on") or []:
            if dep not in have:
                err(f"13-01 mục 6: đơn vị `{u.get('id')}` phụ thuộc `{dep}` không tồn tại.")
    # vòng phụ thuộc
    graph = {u.get("id"): list(u.get("depends_on") or []) for u in units}
    state = {}
    def walk(n, path):
        if state.get(n) == 2:
            return
        if state.get(n) == 1:
            err("13-01 mục 6: VÒNG phụ thuộc — " + " → ".join(path + [n]))
            return
        state[n] = 1
        for x in graph.get(n, []):
            walk(x, path + [n])
        state[n] = 2
    for n in graph:
        walk(n, [])
    # mọi SCR trong 08-01 phải thuộc đúng một đơn vị
    inv = set(re.findall(r"(?<![A-Z0-9])SCR-\d{3}(?!\d)", D.get("08-01", {}).get("body", "")))
    if inv:
        seen = {}
        for u in units:
            for s in (u.get("covers") or {}).get("SCR") or []:
                seen.setdefault(s, []).append(u.get("id"))
        missing = sorted(inv - set(seen))
        dup = {k: v for k, v in seen.items() if len(v) > 1}
        if missing:
            warn("13-01 mục 6: màn chưa thuộc đơn vị nào — " + ", ".join(missing[:15]) +
                 ("…" if len(missing) > 15 else "") + "\n    Ai dựng màn đó là chưa rõ.")
        if dup:
            err("13-01 mục 6: màn thuộc NHIỀU đơn vị — " +
                ", ".join(f"{k}: {'/'.join(v)}" for k, v in list(dup.items())[:10]))


# ─────────────── viết cho nhiều vai trò cùng đọc ───────────────
# Một dự án có Product Owner, Designer và Dev đọc chung một bộ tài liệu, và người
# viết nào cũng viết bằng tiếng của nghề mình. Chỗ hỏng không nằm ở đoạn khó hiểu
# — nó nằm ở chỗ người ở vai trò khác đọc lướt qua thuật ngữ lạ, tưởng mình hiểu,
# rồi vẫn gật đầu duyệt. Sáu tuần sau mới lộ ra là hai bên hiểu hai kiểu.
#
# Phép kiểm này KHÔNG bắt viết đơn giản — nó bắt mỗi tài liệu tự mang theo bảng
# nghĩa cho những từ nó dùng. Thuật ngữ giữ nguyên; diễn giải là thêm vào.

TERM_SEC = "Thuật ngữ dùng trong tài liệu này"
READ_SEC = "0. Đọc nhanh"


def _section(body: str, heading: str) -> str:
    """Cắt phần thân của một mục `## <heading>` cho tới mục `##` kế tiếp."""
    m = re.search(rf"^##\s+{re.escape(heading)}\s*$", body, re.M)
    if not m:
        return ""
    nxt = re.search(r"^##\s+", body[m.end():], re.M)
    return body[m.end(): m.end() + nxt.start()] if nxt else body[m.end():]


def _first_cells(section: str) -> list[str]:
    """Ô đầu của mỗi dòng bảng, đã bỏ backtick và dấu đậm."""
    out = []
    for line in section.split("\n"):
        t = line.strip()
        if not t.startswith("|") or set(t) <= set("| -:"):
            continue
        c = t.strip("|").split("|")[0].strip().strip("`").strip("*").strip()
        if c and c.lower() not in {"thuật ngữ / tiền tố mã", "thuật ngữ", "câu hỏi"}:
            out.append(c)
    return out


def load_dictionary(docs: Path):
    """Thuật ngữ từ _GLOSSARY + tiền tố mã từ _ID_REGISTRY.

    CHỈ tự động kiểm những thuật ngữ viết bằng ký tự latin không dấu — đó đúng là
    nhóm chặn người đọc ở vai trò khác. Mục từ đặt tên tiếng Việt ("trạng thái",
    "cổng", "truy nguyên") vẫn nằm trong từ điển cho người tra, nhưng không ép,
    vì chúng là từ thường và sẽ khớp ở mọi trang — báo động giả nhiều thì người
    ta bắt đầu bỏ qua cả những báo động thật.
    """
    terms: set[str] = set()
    g = docs / "_GLOSSARY.md"
    if g.exists():
        sec = _section(g.read_text(encoding="utf-8"), "Thuật ngữ chuyên môn — nghĩa một câu")
        for t in _first_cells(sec):
            if re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9 /()\-\.]*", t):
                terms.add(t)
    prefixes: set[str] = set()
    r = docs / "_ID_REGISTRY.md"
    if r.exists():
        for c in _first_cells(_section(r.read_text(encoding="utf-8"), "Bảng prefix")):
            if re.fullmatch(r"[A-Z]{2,6}", c):
                prefixes.add(c)
    return terms, prefixes


def _used_terms(text: str, terms: set[str]) -> set[str]:
    """Khớp dài nhất thắng: có "event taxonomy" thì không đòi liệt kê thêm "event"."""
    spans = []
    for t in terms:
        for m in re.finditer(rf"(?<![\w-]){re.escape(t)}(?![\w-])", text, re.I):
            spans.append((m.start(), m.end(), t))
    keep = []
    for a, b, t in spans:
        if not any(x <= a and b <= y and (y - x) > (b - a) for x, y, _ in spans):
            keep.append(t)
    return set(keep)


def check_plain_language(D, docs: Path):
    terms, prefixes = load_dictionary(docs)
    if not terms and not prefixes:
        return
    for did, d in D.items():
        body, name = d["body"], d["file"].name
        approved = d["fm"].get("status") == "approved"
        report = err if approved else warn

        # 1. Mục 0 — bốn dòng, không được để trống
        rs = _section(body, READ_SEC)
        if not rs.strip():
            report(f"{name}: thiếu mục `{READ_SEC}` — người ở vai trò khác không biết có cần đọc file này không.")
        else:
            empty = []
            for line in rs.split("\n"):
                t = line.strip()
                if not t.startswith("|") or set(t) <= set("| -:"):
                    continue
                cells = [c.strip() for c in t.strip("|").split("|")]
                if len(cells) >= 2 and cells[0].strip("* ").lower() != "câu hỏi" and not cells[1]:
                    empty.append(cells[0].strip("* "))
            if empty:
                report(f"{name}: mục `{READ_SEC}` còn ô trống — {', '.join(empty)}.")
            jargon = _used_terms(rs, terms)
            if jargon:
                warn(f"{name}: mục `{READ_SEC}` có thuật ngữ ({', '.join(sorted(jargon))}). "
                     "Bốn dòng này là chỗ DUY NHẤT phải viết không thuật ngữ — người đọc chưa tới bảng nghĩa.")

        # 2. Bảng thuật ngữ cuối tài liệu, đối chiếu hai chiều
        ts = _section(body, TERM_SEC)
        listed = {c.lower() for c in _first_cells(ts)}
        rest = body.replace(ts, " ") if ts else body

        used = _used_terms(rest, terms)
        used |= {p for p in prefixes if re.search(rf"(?<![A-Z0-9]){p}-\d", rest)}

        missing = sorted(t for t in used if t.lower() not in listed)
        if missing:
            report(f"{name}: dùng {len(missing)} thuật ngữ/mã mà không có trong bảng `{TERM_SEC}`:\n"
                   f"    {', '.join(missing)}\n"
                   "    Chép nghĩa một câu từ `_GLOSSARY.md` / `_ID_REGISTRY.md`. Giữ nguyên thuật ngữ "
                   "trong bài — diễn giải là thêm vào, không phải thay thế.")
        if ts:
            extra = sorted(c for c in _first_cells(ts)
                           if c.lower() not in {t.lower() for t in used} and c.strip())
            if extra:
                warn(f"{name}: bảng `{TERM_SEC}` liệt kê thứ không xuất hiện trong bài: {', '.join(extra[:8])}.")


def check_banned_words(D):
    BAN = ["nhanh","mượt","dễ dùng","trực quan","hợp lý","đầy đủ","tối ưu"]
    if "06-02" not in D: return
    for line in D["06-02"]["body"].split("\n"):
        if not re.search(r"\|.*(Given|Then)", line): continue
        for w in BAN:
            if re.search(rf"\b{w}\b", line, re.I):
                err(f"06-02: acceptance criteria dùng từ không đo được '{w}' → {line.strip()[:80]}")


def check_index(D, docs: Path, tpl: Path):
    idx = docs/"_INDEX.md"
    if not idx.exists(): err("không thấy docs/_INDEX.md"); return
    listed = set(re.findall(r"^\| `(\d\d-\d\d)`", idx.read_text(encoding="utf-8"), re.M))
    templates = {f.name[:5] for f in tpl.glob("*.md")} if tpl.is_dir() else set()
    for x in listed - templates: err(f"_INDEX liệt kê {x} nhưng không có template")
    for x in templates - listed: err(f"có template {x} nhưng _INDEX không liệt kê")
    for did in D:
        if did not in listed: warn(f"{did} tồn tại trong docs/ nhưng _INDEX chưa liệt kê")


def check_lorem(D):
    for did, d in D.items():
        if re.search(r"lorem ipsum", d["body"], re.I):
            err(f"{did}: còn Lorem Ipsum")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--root", default=".")
    p.add_argument("--gate")
    p.add_argument("--strict", action="store_true")
    a = p.parse_args()
    root = Path(a.root).resolve()
    docs, tpl = root/"docs", root/".claude"/"doc-templates"
    if not docs.is_dir(): sys.exit(f"LỖI: không thấy {docs} — chạy từ thư mục gốc dự án")

    D = load(docs)
    if a.gate:
        D = {k: v for k, v in D.items() if v["fm"].get("gate") == a.gate}
        print(f"{C['d']}Lọc theo cổng {a.gate}: {len(D)} tài liệu{C['x']}\n")

    check_frontmatter(D); check_depends(D); check_labels(D, docs)
    ids = check_ids(D); check_orphans(D, ids); check_dangling_refs(D, ids)
    check_banned_words(D); check_lorem(D); check_index(D, docs, tpl); check_volume(D)
    check_depth(D); check_stale_inputs(D); check_handover_units(D)
    check_plain_language(D, docs)

    print(f"Đã kiểm {len(D)} tài liệu trong {docs}\n")
    approved = sum(1 for d in D.values() if d["fm"].get("status") == "approved")
    print(f"  approved: {approved}/{len(D)}")
    for pre, v in sorted(ids.items()):
        if v: print(f"  {pre:5} {len(v):>3} ID")
    print()
    for m in E: print(f"{C['r']}LỖI{C['x']}      {m}")
    for m in W: print(f"{C['y']}CẢNH BÁO{C['x']}  {m}")
    if not E and not W: print(f"{C['g']}Không phát hiện vấn đề.{C['x']}")
    print(f"\n{len(E)} lỗi · {len(W)} cảnh báo")
    sys.exit(1 if E or (a.strict and W) else 0)


if __name__ == "__main__":
    main()
