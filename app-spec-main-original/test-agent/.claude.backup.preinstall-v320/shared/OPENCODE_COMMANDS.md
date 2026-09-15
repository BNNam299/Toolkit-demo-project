# OpenCode Commands

Custom commands cho phép bạn định nghĩa các prompt tái sử dụng, được thực thi khi gõ `/command-name` trong TUI.

## Quick Reference

| Feature | Syntax |
|---------|--------|
| Gọi command | `/<name>` hoặc `/<name> <arguments>` |
| Arguments | `$ARGUMENTS`, `$1`, `$2`, `$3` |
| Shell output | `!`command`` |
| File reference | `@filename` |

## Tạo Command Files

Commands được định nghĩa bằng markdown files trong thư mục `commands/`.

### Vị trí

- **Global**: `~/.config/opencode/commands/`
- **Per-project**: `.opencode/commands/`

### Cấu trúc File

```markdown
---
description: Mô tả command
agent: <agent-name>      # Optional
model: <model-id>        # Optional
---

Nội dung prompt với $ARGUMENTS
```

## Frontmatter Options

| Field | Required | Description |
|-------|----------|-------------|
| `description` | Yes | Mô tả hiển thị trong TUI |
| `agent` | No | Agent thực thi (subagent mặc định) |
| `model` | No | Override model cho command này |

## Placeholders

### Arguments (`$ARGUMENTS`)

```markdown
---
description: Tạo component mới
---
Create a new React component named $ARGUMENTS with TypeScript support.
```

**Usage**: `/component Button`

### Positional Arguments (`$1`, `$2`, `$3`)

```markdown
---
description: Tạo file với nội dung
---
Create a file named $1 in the directory $2 with content: $3
```

**Usage**: `/create-file config.json src "{ \"key\": \"value\" }"`

### Shell Output (`!`command``)

```markdown
---
description: Phân tích test coverage
---
Here are the current test results:
!`npm test`
Based on these results, suggest improvements.
```

### File References (`@filename`)

```markdown
---
description: Review component
---
Review @src/components/Button.tsx for issues.
```

## Ví dụ trong dự án

### `/project-docs`

```markdown
---
description: Create project documentation (PRD, Overview, Use Cases, FR, Wireframes, UX Flows)
agent: project-docs-orchestrator
---

@project-docs-orchestrator

Create full project documentation for $ARGUMENTS.

Output directory: .claude/specs/$ARGUMENTS/
Mode: fast
```

### `/spec`

```markdown
---
description: Create feature specification (requirements, design, tasks)
agent: spec-orchestrator
---

@spec-orchestrator

Create spec for $ARGUMENTS feature.

Output directory: .claude/specs/$ARGUMENTS/
```

### `/execute`

```markdown
---
description: Execute feature implementation (implement, verify, refine)
---

Use the `execution-workflow` skill to implement $ARGUMENTS feature.

Prerequisites:
- Spec must be complete (approved_tasks stage)
- spec-state.json exists
```

## Command Options

### Agent Selection

```markdown
---
description: Code review
agent: build
---
```

### Model Override

```markdown
---
description: Deep analysis
model: anthropic/claude-sonnet-4-20250514
---
```

### Subtask Mode

Đặt trong frontmatter của agent để force subagent behavior.

## Built-in Commands

OpenCode có sẵn: `/init`, `/undo`, `/redo`, `/share`, `/help`

**Note**: Custom commands có thể override built-in commands cùng tên.

## Workflow với Orchestrators

```
User gõ /project-docs MyApp
  → OpenCode load project-docs.md
  → Replace $ARGUMENTS = MyApp
  → Invoke @project-docs-orchestrator
  → Orchestrator executes workflow
```

## Tips

1. **Use descriptive names**: Command name nên mô tả action (e.g., `project-docs` not `docs`)
2. **Provide context**: Include `@file` references khi cần thiết
3. **Set appropriate agent**: Orchestrators nên specify agent để invoke
4. **Use arguments**: Giúp commands linh hoạt hơn thay vì hardcode values
