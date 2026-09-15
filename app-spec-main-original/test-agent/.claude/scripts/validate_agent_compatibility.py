#!/usr/bin/env python3
"""
Validate agent markdown compatibility for Claude Code and OpenCode installer transforms.

Checks align with Installer._copy_and_transform_agent expectations:
- Frontmatter exists and is delimited by ---
- tools field is single-line CSV in frontmatter
- tools tokens are in supported mapping set
- no hardcoded .claude/ or .opencode/ in agent body
- task({ agent: "..." }) references point to existing agent file names
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Set


SUPPORTED_TOOLS = {
    "Read",
    "Write",
    "Edit",
    "Task",
    "Grep",
    "Glob",
    "Bash",
    "WebSearch",
    "WebFetch",
}

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.DOTALL)
TOOLS_LINE_RE = re.compile(r"^tools:\s*(.+)$", re.MULTILINE)
TASK_AGENT_RE = re.compile(r"agent:\s*\"([a-z0-9-]+)\"")


@dataclass
class ValidationReport:
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return len(self.errors) == 0


def load_agents(agent_dir: Path) -> List[Path]:
    return sorted(agent_dir.glob("*.md"))


def validate_agent_file(agent_file: Path, known_agents: Set[str]) -> ValidationReport:
    report = ValidationReport()
    text = agent_file.read_text(encoding="utf-8")

    m = FRONTMATTER_RE.match(text)
    if not m:
        report.errors.append(f"{agent_file.name}: missing or invalid frontmatter block")
        return report

    frontmatter, body = m.group(1), m.group(2)

    tools_match = TOOLS_LINE_RE.search(frontmatter)
    if not tools_match:
        report.errors.append(f"{agent_file.name}: missing single-line tools field")
    else:
        tools_value = tools_match.group(1).strip()
        if "\n" in tools_value:
            report.errors.append(f"{agent_file.name}: tools must be single-line CSV")
        else:
            raw_tokens = [t.strip() for t in tools_value.split(",") if t.strip()]
            if not raw_tokens:
                report.errors.append(f"{agent_file.name}: tools list is empty")
            for token in raw_tokens:
                if token not in SUPPORTED_TOOLS:
                    report.errors.append(
                        f"{agent_file.name}: unsupported tool token '{token}' in tools field"
                    )

    if ".claude/" in body:
        report.errors.append(
            f"{agent_file.name}: hardcoded '.claude/' found in body; use .claude/"
        )
    if ".opencode/" in body:
        report.errors.append(
            f"{agent_file.name}: hardcoded '.opencode/' found in body; use .claude/"
        )

    referenced_agents = set(TASK_AGENT_RE.findall(body))
    for ref in sorted(referenced_agents):
        if ref not in known_agents:
            report.errors.append(
                f"{agent_file.name}: references unknown task agent '{ref}'"
            )

    if ".claude/" not in body and ".claude/" not in body:
        report.warnings.append(
            f"{agent_file.name}: no IDE placeholder found in body (verify paths are intentional)"
        )

    return report


def main() -> int:
    script_dir = Path(__file__).resolve().parent
    content_dir = script_dir.parent
    agent_dir = content_dir / "agents"

    if not agent_dir.exists():
        print(f"ERROR: agent directory not found: {agent_dir}")
        return 1

    agent_files = load_agents(agent_dir)
    if not agent_files:
        print("ERROR: no agent markdown files found")
        return 1

    known_agents = {p.stem for p in agent_files}

    all_errors: List[str] = []
    all_warnings: List[str] = []
    for agent_file in agent_files:
        report = validate_agent_file(agent_file, known_agents)
        all_errors.extend(report.errors)
        all_warnings.extend(report.warnings)

    if all_warnings:
        print("WARNINGS:")
        for warning in all_warnings:
            print(f"- {warning}")
        print()

    if all_errors:
        print("AGENT COMPATIBILITY CHECK: FAILED")
        print(f"Errors: {len(all_errors)}")
        for err in all_errors:
            print(f"- {err}")
        return 1

    print("AGENT COMPATIBILITY CHECK: PASSED")
    print(f"Checked agents: {len(agent_files)}")
    if all_warnings:
        print(f"Warnings: {len(all_warnings)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
