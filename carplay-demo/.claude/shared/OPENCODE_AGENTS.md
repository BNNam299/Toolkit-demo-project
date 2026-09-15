# OpenCode Agents

Agents là specialized AI assistants được configure cho specific tasks và workflows.

## Agent Types

### Primary Agents

Main assistants bạn tương tác trực tiếp. Có thể switch giữa các primary agents bằng **Tab** key.

**Built-in Primary Agents:**
- **Build**: Default agent, all tools enabled
- **Plan**: Restricted agent cho planning/analysis (file edits và bash = ask)

### Subagents

Specialized assistants được primary agents invoke hoặc user @mention.

**Built-in Subagents:**
- **General**: Multi-step tasks, full tool access
- **Explore**: Fast, read-only codebase exploration
- **Compaction**: Hidden, auto-compacts long context
- **Title**: Hidden, generates session titles
- **Summary**: Hidden, creates session summaries

## Invocation

### Primary Agents

| Method | Action |
|--------|--------|
| **Tab** | Cycle through primary agents |
| `/switch` | Switch to specific agent |
| Tab key | Switch agent |

### Subagents

| Method | Action |
|--------|--------|
| `@agent-name` | Invoke subagent manually |
| Task tool | Primary agent invokes subagent |

**Example:**
```
@general help me search for this function
```

## Creating Custom Agents

### Markdown Format

**.opencode/agents/<name>.md**

```markdown
---
description: Reviews code for quality and best practices
mode: subagent
model: anthropic/claude-sonnet-4-20250514
temperature: 0.1
tools:
  write: false
  edit: false
  bash: false
---

You are in code review mode. Focus on:
- Code quality and best practices
- Potential bugs and edge cases
- Performance implications
```

### JSON Format (opencode.json)

```json
{
  "agent": {
    "code-reviewer": {
      "description": "Reviews code for best practices",
      "mode": "subagent",
      "model": "anthropic/claude-sonnet-4-20250514",
      "prompt": "{file:./prompts/code-review.txt}",
      "tools": {
        "write": false,
        "edit": false
      }
    }
  }
}
```

## Agent Options

### Required

| Option | Description |
|--------|-------------|
| `description` | What agent does, when to use |
| `mode` | `primary`, `subagent`, or `all` |

### Optional

| Option | Default | Description |
|--------|---------|-------------|
| `model` | Global/parent | Override model |
| `temperature` | Model default | 0.0-1.0 |
| `top_p` | Model default | Alternative to temperature |
| `steps` | Unlimited | Max iterations before text-only |
| `prompt` | None | Custom system prompt file |
| `hidden` | false | Hide from @ autocomplete |
| `color` | Default | Hex color or theme color |
| `tools` | All allowed | Legacy - prefer permissions |
| `permission` | Allow all | Fine-grained control |

### Mode Values

| Mode | Description |
|------|-------------|
| `primary` | Main agent, user interacts directly |
| `subagent` | Invoked by primary or @mention |
| `all` | Can be both (default) |

## Permissions

### Permission Types

```json
{
  "permission": {
    "edit": "ask|allow|deny",
    "bash": "ask|allow|deny",
    "webfetch": "ask|allow|deny",
    "task": { "<pattern>": "ask|allow|deny" }
  }
}
```

| Value | Behavior |
|-------|----------|
| `ask` | User prompted before running |
| `allow` | Run without prompt |
| `deny` | Blocked |

### Bash Command Patterns

```json
{
  "permission": {
    "bash": {
      "*": "ask",
      "git status *": "allow",
      "git push": "deny"
    }
  }
}
```

**Rule order**: Last matching rule wins.

### Task Permissions

Control which subagents can be invoked:

```json
{
  "permission": {
    "task": {
      "*": "deny",
      "orchestrator-*": "allow",
      "code-reviewer": "ask"
    }
  }
}
```

## Agent Configuration Examples

### Orchestrator Agent

```json
{
  "agent": {
    "project-docs-orchestrator": {
      "description": "Primary orchestrator for project documentation",
      "mode": "primary",
      "prompt": "{file:./.opencode/agents/project-docs-orchestrator.md}",
      "tools": {
        "write": false,
        "edit": false,
        "read": true,
        "task": true
      },
      "permission": {
        "task": {
          "*": "deny",
          "project-docs-*": "allow",
          "spec-orchestrator": "allow"
        }
      }
    }
  }
}
```

### Execution Skills

Use skills instead of agents for execution tasks:

```markdown
---
name: execution-implement
description: Execute implementation tasks with build verification
allowed-tools: Read, Edit, Write, Bash, MCP
---
```

Skills provide the same functionality as agents with better integration and composability.

### Read-Only Explorer Agent

```json
{
  "agent": {
    "spec-explorer": {
      "description": "Explore and analyze specifications",
      "mode": "subagent",
      "tools": {
        "read": true,
        "grep": true,
        "glob": true
      }
    }
  }
}
```

## Hidden Agents

Agents có thể ẩn khỏi @ autocomplete:

```json
{
  "agent": {
    "internal-helper": {
      "mode": "subagent",
      "hidden": true
    }
  }
}
```

**Use case**: Internal subagents invoked programmatically, not by user.

## Temperature Guidelines

| Range | Use Case |
|-------|----------|
| 0.0-0.2 | Code analysis, planning |
| 0.3-0.5 | General development |
| 0.6-1.0 | Brainstorming, creative |

## Session Navigation

Khi subagents tạo child sessions:

| Key | Action |
|-----|--------|
| `session_child_first` (<Leader>+Down) | Enter first child |
| `session_child_cycle` (Right) | Next child |
| `session_child_cycle_reverse` (Left) | Previous child |
| `session_parent` (Up) | Return to parent |

## Skills trong dự án

### Orchestrators (Skills)

| Skill | Description |
|-------|-------------|
| `project-docs-orchestrator` | PRD → Overview → UC → FR → Wireframes → UX Flows |
| `spec-orchestrator` | Requirements → Design → Tasks |
| `execution-workflow` | Implement → Verify → Refine |

### Creators (Skills)

| Skill | Creates |
|-------|---------|
| `project-docs-prd-creator` | PRD.md |
| `project-docs-overview-creator` | Project_Overview.md |
| `project-docs-uc-creator` | Use_Cases.md |
| `project-docs-fr-creator` | Functional_Requirements.md |
| `project-docs-wireframes-creator` | Wireframes.md |
| `project-docs-flows-creator` | UX_Flows.md |
| `spec-creator-requirements` | requirements.md |
| `spec-creator-design` | design.md |
| `spec-creator-tasks` | tasks.md |

### Execution Skills

| Skill | Role |
|-------|------|
| `execution-implement` | Execute implementation tasks |
| `execution-verify` | Verify implementation against specs |
| `execution-quick` | Quick prototype implementation |

### Refiners (Skills)

| Skill | Role |
|-------|------|
| `spec-refiner-impact` | Impact-based refinement routing |
| `spec-refiner-patch` | Minor format-safe updates |

## Tool Permissions for Execution Skills

### execution-implement

```yaml
---
name: execution-implement
description: Execute implementation tasks with build verification
allowed-tools: Read, Edit, Write, Bash, MCP
---
```

### execution-verify

```yaml
---
name: execution-verify
description: Verify implementation against specifications
allowed-tools: Read, Grep, Glob, Bash
---
```

### Spec UI/UX Analyzer

```yaml
---
name: spec-uiux-analyzer
description: Analyze and validate UI/UX specifications
allowed-tools: Read, Edit, Write, Grep, Glob
---
```

## Best Practices

1. **Use mode correctly**: Orchestrators = `primary`, creators = `subagent`
2. **Set clear descriptions**: Giúp agent chọn đúng tool
3. **Restrict permissions**: execution-implement vs execution-verify
4. **Use task permissions**: Orchestrators chỉ invoke allowed subagents
5. **Set temperature**: 0.1-0.3 cho code tasks, 0.5+ cho brainstorming
