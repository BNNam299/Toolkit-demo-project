---
name: pencil-design
description: >
  Create high-quality visual designs â€” websites, app screens, dashboards, slides, marketing materials, social media graphics â€” using the Pencil CLI tool. Use this skill whenever the user wants to create, generate, or visualize any kind of UI design, mockup, wireframe, layout, webpage, app screen, presentation slide, poster, banner, or marketing asset. Also use it when the user says things like "design me a...", "make a visual for...", "create a mockup of...", "what would X look like?", or wants to turn an idea into a visual. Even if the user doesn't mention "Pencil" or "design tool" explicitly â€” if they want something visual created, this is the skill to use.
---

<!-- PIPELINE-V2-PENCIL-NOTE -->

# RÀNG BUỘC PIPELINE V2 — nhánh này mặc định TẮT

**Khối này thắng toàn bộ phần dưới.** Phần dưới là hướng dẫn gốc của Pencil, viết cho hoàn cảnh không có
bộ tài liệu nào; nó bảo bạn cứ nhận yêu cầu rồi dựng. Trong bộ này thì không.

## Phải có `DEC` mới được dùng

`CLAUDE.md` và `AGENTS.md` của bộ này có một quy tắc phạm vi đang có hiệu lực: **AI không dựng UI.**
Phase 12 viết spec, người dựng tay trong Figma.

Skill này **đảo quy tắc đó**, nên nó là **nhánh tuỳ chọn phải bật tường minh**:

1. `docs/12-prototype/12-00_UI_RESEARCH.md` mục 7 chọn **nhánh A — Pencil + Agent**, kèm một `DEC` ID.
2. `DEC` đó có mặt trong `docs/_DECISION_LOG.md`.

Người dùng phải được **hỏi** rồi tự chọn nhánh; agent không tự chọn thay.

Chưa có cả hai thì **không dựng**, kể cả khi người dùng nhắc qua trong chat. Nói rõ đang thiếu gì rồi dừng.

## Không dựng trước khi có hướng thị giác

Dựng bằng AI mà chưa chốt hướng thì được một loạt màn đẹp rời rạc không thành một sản phẩm. Bắt buộc có
trước, đều `status: approved`:

| Cần có | Vì sao |
| --- | --- |
| `12-00_UI_RESEARCH` | hướng thiết kế đã chọn, hệ màu, hệ chữ, danh sách màn "Chốt trước" |
| `12-01_PROTOTYPE_BUILD_SPEC` | danh sách frame bắt buộc và **bảng lô** ở mục 4 |
| `design-system/_MANIFEST.md` | **tên component để gọi lại**, và bảng phủ ở mục 4 phải đã điền |
| `08-01_SCREEN_INVENTORY` | **danh sách màn là đóng.** Không dựng màn không có trong đây |
| `08-03_WIREFLOWS` + `wireframes/` | luồng và nội dung màn đã chốt. Pencil đổi thị giác, không đổi luồng |
| `09-06_COPY_DECK` | **chữ thật theo mã `CPY`. Không Lorem Ipsum, không tự viết chữ mới** |

## Dùng lại hệ thiết kế, đừng vẽ lại

Có `design-system/` thì **gọi component đúng tên** ghi ở mục 3 của manifest đó. Vẽ một thành phần trông
giống hệ nhưng không phải instance của hệ là tạo ra thứ **sẽ không đổi theo khi hệ đổi** — sáu tháng sau
đổi màu thương hiệu thì đúng những màn đó đứng im.

Thiếu component thì **không tự sinh trong lúc dựng màn**. Ghi vào mục 5 của
`design-system/_MANIFEST.md`, xin phép, dựng bổ sung vào hệ trước, rồi mới dùng.

## Một lô một lượt

Lô = một `FLOW` hoặc một nhóm `FEAT`, theo **bảng lô ở `12-01` mục 4**. Không dựng cả bộ trong một lệnh.
Lô đầu nên chứa những màn *"Chốt trước"* ở `12-00` mục 6. **Lô chưa nghiệm thu thì không dựng lô sau.**

Sau mỗi lô: xuất ảnh → chạy `python .claude/scripts/check_build.py --frames <file>` → **dán nguyên kết quả,
không tóm tắt** → báo cáo bốn dòng theo khuôn ở `12-01` mục 4 → **dừng chờ nghiệm thu**.

Prompt cho Pencil viết từ wireframe, `12-00` và tên component trong hệ; không tự sáng tác thêm. Ảnh tham
chiếu nạp kèm lấy từ `research-raw/moodboard/`, đúng những `UIP` đã quyết **Áp dụng** hoặc **Điều chỉnh** —
không nạp ảnh ở `khong-thich/`.

## Đặt tên và đường ra

Đặt tên file theo mã màn hình, cùng quy ước với `12-01`:

```
designs/SCR-012_ST-041_ket-qua-phan-tich.pen
designs/SCR-012_ST-041_ket-qua-phan-tich.png
```

**Mã ba chữ số, khớp `08-02`.** Viết `ST-41` thay cho `ST-041` là tên sai và `check_build.py` sẽ báo lỗi.
Không đặt tên theo nội dung sáng tạo. Không khớp mã thì bước đối chiếu ở `12-03` thành thủ công và sẽ không
ai làm.

## Hai cách nối Pencil — chọn một

| Cách | Cần gì | Ghi chú |
| --- | --- | --- |
| **CLI** (phần dưới hướng dẫn cách này) | `npm install -g @pencil.dev/cli`, tài khoản Pencil | chạy được trong Claude Code, Codex, OpenCode |
| **MCP** | thêm server Pencil vào `.mcp.json` cạnh Framelink Figma | chỉ dùng được ở công cụ có hỗ trợ MCP |

Dùng MCP thì **quy tắc ở khối này vẫn áp nguyên** — `DEC`, danh sách màn đóng, chữ theo `CPY`, một màn một
lượt, tên file theo mã. Cách nối đổi, ràng buộc không đổi.

## `12-01` vẫn phải viết

Bỏ `12-01_PROTOTYPE_BUILD_SPEC` vì "AI dựng rồi" là mất luôn thứ để đối chiếu ở `12-03`. `12-01` là danh
sách frame bắt buộc; không có nó thì không ai biết đã dựng đủ chưa.

---

*Hết phần ràng buộc. Phần dưới là hướng dẫn gốc của Pencil — dùng để biết cách chạy công cụ, không dùng để
quyết định dựng gì.*


<!-- APPSPEC-PRELUDE -->

> **ĐỌC KHỐI NÀY TRƯỚC.** File này lấy nguyên văn từ bộ **app-spec** rồi đưa vào Pipeline v2.
> Nội dung chuyên môn bên dưới dùng bình thường, nhưng **ba loại tham chiếu trong đó đã lỗi** — bỏ qua chúng,
> đừng đi tìm.
>
> **1. Skill không tồn tại trong bộ này.** `project-docs-contract` · `project-docs-workflow` ·
> `project-docs-prd` · `project-docs-overview` · `project-docs-uc` · `project-docs-fr` ·
> `project-docs-wireframes` · `project-docs-flows` · `project-docs-roadmap` · mọi `spec-*` · mọi
> `execution-*` · `ui-redesign` · `quick-*` · `dev-spec-driven` · `ios-debug` · `ios-icon-gen` · `mcp-xcode`.
> Chúng bị loại **có chủ đích** vì thuộc phạm vi sau bàn giao. Danh sách đầy đủ ở `.claude/KIT_MANIFEST.md`.
> Gặp câu *"phải đọc skill X trước"* mà X nằm trong danh sách này thì **bỏ qua câu đó**, không dừng, không đi tìm.
>
> **2. Đường dẫn `.claude/specs/<tên dự án>/...`** — cấu trúc của app-spec, **không có** ở đây.
> Bộ này ghi tài liệu ra `docs/<thư-mục-phase>/<doc_id>_<TÊN>.md`. Danh sách 61 tài liệu ở `docs/_INDEX.md`.
>
> **3. Bảng ánh xạ 1:1 gate→file** kiểu `gate-prd → PRD.md`. Pipeline v2 có 61 tài liệu và 12 cổng G0–G11;
> cổng đọc từ khối `QUALITY-GATE-MANIFEST` ở **cuối template tương ứng**, không từ bảng cứng.
>
> **Đây là skill CHIỀU SÂU.** Nó không sở hữu tài liệu nào, không cấp ID, không gọi cổng. Vai của nó là làm
> skill phụ trách phase hiểu sâu hơn. Mọi thứ ghi ra file vẫn do skill phụ trách phase quyết định.


# Pencil Design

Create professional visual designs from natural language descriptions using the Pencil CLI. Pencil is a headless design tool that generates `.pen` files (a structured JSON design format) and can export them as images.

## Setup

Before designing, make sure the Pencil CLI is available.

### Check installation

```bash
which pencil || npx pencil version
```

If `pencil` is not found, install it:

```bash
npm install -g @pencil.dev/cli
```

If global install fails due to permissions, install locally instead:

```bash
npm install @pencil.dev/cli
```

Then run it via `npx pencil` (or `./node_modules/.bin/pencil`) instead of `pencil`.
You can learn about the available commands via the `pencil --help` command.

### Authentication

#### Pencil user

To use the CLI, an authenticated user logged in to Pencil is required. First, check
the current user configuration on the machine with the `pencil status` command.

If not logged in, there are the following options:

- use `pencil signup --email you@example.com --username johndoe --name "John Doe"` command, to create a new user.
- use `pencil login --email you@example.com [--code abc123]` to authenticate an existing or newly created user.
- optionally, the `PENCIL_CLI_KEY` env var can also be used for authentication if its set in your session.

#### Claude Code agent

The CLI needs auth to run its AI agent for which Claude Code is required. For that
there needs to be an authenticated Claude Code user set in the system configuration
either via env var or a user subscription.

If none of these are available, tell the user what options they have and help them set one up.

### Staying up to date

This skill stays in sync with the **Pencil CLI npm package** (`@pencil.dev/cli`). The published package includes `SKILL.md` at its root; the package version is the skill version.

**Check for a newer CLI / skill**

- Latest version on the registry: `npm view @pencil.dev/cli version`
- Installed CLI: `pencil version`, or `npm list -g @pencil.dev/cli` (global) / `npm list @pencil.dev/cli` (project)

**Upgrade the CLI**, then refresh your copied skill file (agents do not auto-update skill files you placed in config folders):

```bash
npm install -g @pencil.dev/cli
```

**Where to copy the skill from after installing**

- From a dependency tree: `node_modules/@pencil.dev/cli/SKILL.md` (path is the same for global and local installs; resolve from your project root or global `node_modules` prefix).

**Fetch the same file without cloning the repo** (mirrors the npm tarball; optional third-party CDNs):

- `https://unpkg.com/@pencil.dev/cli@latest/SKILL.md`
- `https://cdn.jsdelivr.net/npm/@pencil.dev/cli@latest/SKILL.md`

Use `@latest` for the newest publish, or pin (e.g. `@0.2.4`) for a reproducible snapshot.

**If you donâ€™t know where skills live on this machine**

Agents donâ€™t always get the skills directory from context. When the path isnâ€™t obvious:

- **Ask the user** where their agent or IDE loads skills from, or where they want this skill installed.
- **Check the productâ€™s docs** for â€œskillsâ€, â€œagent skillsâ€, or â€œpluginsâ€ â€” paths differ by tool and version.
- You can still **use the skill content without installing**: fetch or open the **`SKILL.md` URL above** (unpkg/jsDelivr) in the session so guidance applies even when the on-disk path is unknown. For a persistent install, copy the fetched file into the path the user or docs specify.

**Typical skill locations** (confirm with your toolâ€™s current docs â€” layouts change):

| Environment | Where to put `SKILL.md` |
|-------------|-------------------------|
| **Cursor** | Project: `.cursor/skills/pencil-design/SKILL.md`; user-level: under `~/.cursor/skills/` |
| **Claude Code** | Often `.claude/skills/pencil-design/SKILL.md` or user-level under `~/.claude/` |
| **OpenClaw** | Often `~/.openclaw/skills/`, workspace `.agents/skills/`, or paths in [OpenClaw skills docs](https://docs.openclaw.ai/skills/) â€” verify for the userâ€™s setup |
| **Other agents (Codex, etc.)** | Use the directory your product uses for skills or prompts |

Example (adjust the destination path to match your agent):

```bash
curl -fsSL "https://unpkg.com/@pencil.dev/cli@latest/SKILL.md" -o .cursor/skills/pencil-design/SKILL.md
```

**When to check for an update**

- **Early in the session**, before the first Pencil design run (compare `npm view @pencil.dev/cli version` to the installed CLI), so you arenâ€™t following stale instructions.
- **Again** if the user says they upgraded the CLI, or if behavior doesnâ€™t match this doc (flags, auth, timing).
- **Not** before every single command â€” once per session is enough unless something changed or errors suggest a version mismatch.

## Creating a Design

The core command:

```bash
pencil --out <output.pen> --prompt "<design description>" --export <output.png> --export-scale 2
```

Key flags:
- `--out, -o` â€” where to save the `.pen` file (required)
- `--prompt, -p` â€” what to design (required)
- `--prompt-file, -f` â€” attach an image or text file to send with the prompt (repeatable). Same idea as attaching reference images in the Pencil editor chat; not for loading the prompt text from a file.
- `--export, -e` â€” export an image of the result
- `--export-scale` â€” image resolution multiplier (use 2 for crisp output)
- `--export-type` â€” format: `png` (default), `jpeg`, `webp`, `pdf`
- `--in, -i` â€” start from an existing `.pen` file (for iteration)
- `--model, -m` â€” Claude model to use (defaults to Opus)

### Passing the Prompt

Pass the user's request directly as the prompt â€” do not expand, or add detail beyond what the user actually said. The Pencil CLI has its own AI designer agent that handles creative decisions like layout structure, color palettes, typography, spacing, and content. Adding your own design specifics on top of the user's request will conflict with the CLI agent's own judgment and produce worse results.

If the user says "make me a landing page for a coffee shop", the prompt should be exactly that â€” not a paragraph with hero sections, color palettes, and font choices you invented.

### Timing Expectations

Design generation is not instant â€” the CLI runs an AI agent that plans the layout, creates each element, and validates the result visually. Expect:

- **Simple designs** (a card, a single component): 1-2 minutes
- **Medium designs** (an app screen, a landing page section): 2-3 minutes
- **Complex designs** (full landing page, detailed dashboard): 3-5+ minutes

Let the user know upfront that generation will take a few minutes so they're not left wondering. Use a generous timeout (at least 600000ms / 10 minutes) when running the command.

### Showing the Result

After the command completes, read the exported image to show it to the user:

```bash
# The command exports to the path you specified
pencil --out design.pen --prompt "..." --export design.png --export-scale 2
```

Then use the Read tool on the exported PNG â€” it will render visually since you're a multimodal model.

Always show the image to the user after creating it. This is the whole point â€” they want to see the visual.

## Iterating on a Design

When the user wants changes to an existing design, use the `--in` flag to load the previous `.pen` file:

```bash
pencil --in design.pen --out design-v2.pen --prompt "Make the header larger and change the accent color to green" --export design-v2.png --export-scale 2
```

The agent will read the existing design and apply modifications rather than starting from scratch.

For quick successive iterations, keep a consistent naming pattern:
- `design.pen` â†’ `design-v2.pen` â†’ `design-v3.pen`
- Or use a single file: `--in design.pen --out design.pen` (overwrites)

## Working Directory

Save design files in the user's current working directory or a subdirectory like `designs/`. Don't use temp directories â€” the user will want to find and iterate on these files later.
