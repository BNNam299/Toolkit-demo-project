# Agent Compatibility Checklist (Claude + OpenCode)

Use this checklist before every release to ensure all `agents/*.md` files can be transformed correctly by the installer for both targets:
- Claude Code (`.claude/agents/*.md`)
- OpenCode (`.opencode/agents/*.md`)

Reference implementation:
- `src/ios_spec_driven_installer/installer.py`
- methods: `_copy_and_transform_agent`, `_transform_content_file`

---

## 1) Required Frontmatter Shape

Every agent file must start with YAML frontmatter in this structure:

```markdown
---
name: agent-name
description: ...
tools: Read, Write, Edit, Grep, Glob
skills: ...
---
```

Compatibility rules:
- frontmatter must be bounded by `---` at top and end
- `tools:` must be a single-line comma-separated list
- avoid multiline YAML object for `tools:` in source templates

Why:
- OpenCode transform parses `tools:` with regex expecting one-line CSV format.

---

## 2) Tool Name Compatibility (Source -> OpenCode)

Use only these source tool names in `tools:` for safe transform:

| Source (agent markdown) | OpenCode output key |
|---|---|
| `Read` | skipped (auto-read behavior in installer mapping) |
| `Write` | `write` |
| `Edit` | `edit` |
| `Task` | `task` |
| `Grep` | `grepSearch` |
| `Glob` | `fileSearch` |
| `Bash` | `bash` |
| `WebSearch` | `webSearch` |
| `WebFetch` | `webFetch` |

Do not use unrecognized tokens in `tools:` unless installer mapping is updated.

---

## 3) Path Placeholder Rules

All agent body paths must use placeholder form:

```text
{{IDE_CONFIG_DIR}}
```

Supported variants replaced by installer:
- `{{IDE_CONFIG_DIR}}`
- `{{{{IDE_CONFIG_DIR}}}}` (escaped form)

Legacy note:
- installer also rewrites hardcoded `.claude/` -> `.opencode/` for backward compatibility.
- still prefer `{{IDE_CONFIG_DIR}}` for all new content.

---

## 4) Workflow and Invocation Checks

For orchestrator/subagent patterns:
- ensure agent names in `task({ agent: "..." })` match actual file names
- ensure `prompt` references in OpenCode config resolve to installed paths
- ensure required files in each step use `{{IDE_CONFIG_DIR}}specs/...` format

---

## 5) Pre-release Validation Steps

Run these checks before publishing:

Recommended command:

```bash
python {{IDE_CONFIG_DIR}}scripts/validate_agent_compatibility.py
```

1. **Frontmatter presence**
- every `templates/content/agents/*.md` starts with valid frontmatter

2. **Tools field shape**
- verify each file has one-line `tools:` CSV form

3. **Placeholder coverage**
- no newly introduced hardcoded `.claude/` or `.opencode/` in agent body paths

4. **Installer dry verification**
- install to temp Claude target and confirm agent files exist under `.claude/agents/`
- install to temp OpenCode target and confirm transformed files exist under `.opencode/agents/`

5. **OpenCode config validity**
- validate `templates/formats/opencode/opencode.json` JSON syntax

---

## 6) Common Failure Modes

1. `tools:` changed to multiline YAML in source agent file
- effect: regex transform misses conversion for OpenCode

2. Unsupported tool token added in source
- effect: tool silently omitted from OpenCode transformed output

3. Missing/invalid frontmatter delimiters
- effect: file falls back to raw copy behavior and loses tool transform

4. Hardcoded IDE directory path in body
- effect: wrong target path after installation on the other IDE

---

## 7) Release Gate (Pass/Fail)

Release is allowed only if all are true:
- all agent files pass frontmatter + tools checks
- placeholder/path checks pass
- installer succeeds for both `--ide claude` and `--ide opencode`
- installed agent files are present and readable in target config directories

If any check fails:
- block release
- fix source markdown or installer mapping
- rerun full checklist
