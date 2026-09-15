"""
Installation logic for iOS Spec-Driven Toolkit
"""

import shutil
import re
import subprocess
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, Literal

IDEType = Literal["claude", "opencode"]


class Installer:
    """Handles installation, uninstallation, and validation of the toolkit"""

    def __init__(self, target_dir: Path, ide: IDEType = "claude", backup: bool = True):
        """Initialize installer

        Args:
            target_dir: Target directory for installation
            ide: Target IDE ("claude" or "opencode")
            backup: Whether to backup existing files
        """
        self.target_dir = Path(target_dir).resolve()
        self.ide = ide
        self.backup_enabled = backup

        # Get templates directory
        self.templates_dir = Path(__file__).parent / "templates"

        # Source paths
        self.content_dir = self.templates_dir / "content"
        self.format_dir = self.templates_dir / "formats" / ide

        # Target paths based on IDE
        if ide == "claude":
            self.target_config_dir = self.target_dir / ".claude"
            self.target_mcp = self.target_dir / ".mcp.json"
        else:  # opencode
            self.target_config_dir = self.target_dir / ".opencode"
            self.target_config_file = self.target_dir / "opencode.json"

    def is_installed(self) -> bool:
        """Check if toolkit is already installed

        Returns:
            True if toolkit is installed, False otherwise
        """
        if not self.target_config_dir.exists():
            return False

        # Check for key skill files (3 orchestrator system)
        docs_contract = (
            self.target_config_dir / "skills" / "project-docs-contract" / "SKILL.md"
        )
        spec_contract = (
            self.target_config_dir / "skills" / "spec-creation-contract" / "SKILL.md"
        )
        exec_contract = (
            self.target_config_dir / "skills" / "execution-contract" / "SKILL.md"
        )
        return (
            docs_contract.exists() and spec_contract.exists() and exec_contract.exists()
        )

    def backup(self) -> Path:
        """Backup existing installation

        Returns:
            Path to backup directory
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_dir = self.target_dir / f".{self.ide}.backup.{timestamp}"

        if self.target_config_dir.exists():
            shutil.copytree(self.target_config_dir, backup_dir)

        return backup_dir

    def install(self):
        """Install toolkit files

        Copies content and applies IDE-specific format
        """
        self._run_agent_compatibility_preflight()

        # Ensure target directory exists
        self.target_dir.mkdir(parents=True, exist_ok=True)

        # Remove existing if present
        if self.target_config_dir.exists():
            shutil.rmtree(self.target_config_dir)

        # Create config directory
        self.target_config_dir.mkdir(parents=True, exist_ok=True)

        # Copy content (skills, agents, shared, scripts, hooks)
        self._copy_content()

        # Apply IDE-specific format
        self._apply_format()

    def _run_agent_compatibility_preflight(self):
        """Skip preflight if no agents directory or only placeholder (agents are optional/skill-based now)."""
        agent_dir = self.content_dir / "agents"
        if not agent_dir.exists():
            return  # No agents dir = skip preflight
        
        agent_files = list(agent_dir.glob("*.md"))
        if len(agent_files) == 1 and (agent_files[0].stem == "placeholder"):
            return  # Only placeholder = skip preflight

        script_path = self.content_dir / "scripts" / "validate_agent_compatibility.py"

        if not script_path.exists():
            raise RuntimeError(
                "Missing required preflight script: "
                f"{script_path}. Cannot continue installation."
            )

        result = subprocess.run(
            [sys.executable, str(script_path)],
            capture_output=True,
            text=True,
            cwd=str(self.target_dir),
        )

        if result.returncode != 0:
            details = (result.stdout or "") + (
                "\n" + result.stderr if result.stderr else ""
            )
            raise RuntimeError(
                "Agent compatibility preflight failed. "
                "Fix agent markdown issues before installation.\n"
                f"{details.strip()}"
            )

    def _transform_content_file(self, source_file: Path, target_file: Path):
        """Transform content file paths for target IDE

        Replaces {{IDE_CONFIG_DIR}} placeholder with IDE-specific directory:
        - Claude Code: .claude/
        - OpenCode: .opencode/

        Also handles {{{{IDE_CONFIG_DIR}}}} (escaped for Python f-strings)
        Also handles legacy .claude/ references for backward compatibility
        """
        content = source_file.read_text(encoding="utf-8")

        # Get IDE-specific directory
        ide_dir = ".claude/" if self.ide == "claude" else ".opencode/"

        # Replace escaped placeholder (for Python f-strings)
        content = content.replace("{{{{IDE_CONFIG_DIR}}}}", ide_dir)

        # Replace normal placeholder
        content = content.replace("{{IDE_CONFIG_DIR}}", ide_dir)

        # Legacy: Also replace hardcoded .claude/ for backward compatibility
        if self.ide == "opencode":
            content = content.replace(".claude/", ".opencode/")

        target_file.write_text(content, encoding="utf-8")

    def _copy_content(self):
        """Copy shared content to target directory"""
        # Copy skills (with path transformation)
        if (self.content_dir / "skills").exists():
            skills_target = self.target_config_dir / "skills"
            skills_target.mkdir(parents=True, exist_ok=True)

            for skill_dir in (self.content_dir / "skills").iterdir():
                if skill_dir.is_dir():
                    skill_target_dir = skills_target / skill_dir.name
                    skill_target_dir.mkdir(parents=True, exist_ok=True)

                    # Recurse so nested assets (e.g. scripts/) ship with the skill.
                    # Markdown gets path-transformed; everything else is copied
                    # verbatim to preserve executable bits and non-text content.
                    for skill_file in skill_dir.rglob("*"):
                        if skill_file.is_dir():
                            continue
                        dest = skill_target_dir / skill_file.relative_to(skill_dir)
                        dest.parent.mkdir(parents=True, exist_ok=True)
                        if skill_file.suffix == ".md":
                            self._transform_content_file(skill_file, dest)
                        else:
                            shutil.copy2(skill_file, dest)

        # Copy agents (with transformation for both IDEs)
        if (self.content_dir / "agents").exists():
            agents_target = self.target_config_dir / "agents"
            agents_target.mkdir(parents=True, exist_ok=True)

            for agent_file in (self.content_dir / "agents").glob("*.md"):
                # Transform for both Claude Code and OpenCode
                self._copy_and_transform_agent(
                    agent_file, agents_target / agent_file.name
                )

        # Copy shared guides (with path transformation)
        if (self.content_dir / "shared").exists():
            shared_target = self.target_config_dir / "shared"
            shared_target.mkdir(parents=True, exist_ok=True)

            for shared_file in (self.content_dir / "shared").glob("*.md"):
                self._transform_content_file(
                    shared_file, shared_target / shared_file.name
                )

        # Copy scripts (with path transformation for Python files)
        if (self.content_dir / "scripts").exists():
            scripts_target = self.target_config_dir / "scripts"
            scripts_target.mkdir(parents=True, exist_ok=True)

            for script_file in (self.content_dir / "scripts").iterdir():
                if script_file.is_file():
                    self._transform_content_file(
                        script_file, scripts_target / script_file.name
                    )

        # Copy hooks (with path transformation for Python files)
        if (self.content_dir / "hooks").exists():
            hooks_target = self.target_config_dir / "hooks"
            hooks_target.mkdir(parents=True, exist_ok=True)

            for hook_file in (self.content_dir / "hooks").iterdir():
                if hook_file.is_file():
                    self._transform_content_file(
                        hook_file, hooks_target / hook_file.name
                    )

        # Copy commands (OpenCode custom commands)
        if (self.content_dir / "commands").exists():
            commands_target = self.target_config_dir / "commands"
            commands_target.mkdir(parents=True, exist_ok=True)

            for cmd_file in (self.content_dir / "commands").glob("*.md"):
                self._transform_content_file(cmd_file, commands_target / cmd_file.name)

        # Copy doc-templates (document templates for project-docs workflow)
        if (self.content_dir / "doc-templates").exists():
            templates_target = self.target_config_dir / "doc-templates"
            templates_target.mkdir(parents=True, exist_ok=True)

            for template_file in (self.content_dir / "doc-templates").glob("*.md"):
                self._transform_content_file(
                    template_file, templates_target / template_file.name
                )

        # Copy design-token .pen files (Pencil design templates for /ios-ui-redesign).
        # .pen files are encrypted binary — copy verbatim, NEVER text-transform them.
        if (self.content_dir / "design-token").exists():
            design_token_target = self.target_config_dir / "design-token"
            design_token_target.mkdir(parents=True, exist_ok=True)

            for token_file in (self.content_dir / "design-token").iterdir():
                if token_file.is_file():
                    shutil.copy2(token_file, design_token_target / token_file.name)

    def _copy_and_transform_agent(self, source_file: Path, target_file: Path):
        """Transform agent content for target IDE

        For Claude Code:
        - Keep tools format as-is (comma-separated)
        - Replace {{IDE_CONFIG_DIR}} with .claude/

        For OpenCode:
        - Transform tools CSV to permission YAML format (https://opencode.ai/docs/agents/#permissions)
        - Replace {{IDE_CONFIG_DIR}} with .opencode/
        """
        content = source_file.read_text(encoding="utf-8")

        # Get IDE-specific directory
        ide_dir = ".claude/" if self.ide == "claude" else ".opencode/"

        # Extract frontmatter
        frontmatter_pattern = r"^---\n(.*?)\n---\n(.*)$"
        frontmatter_match = re.match(frontmatter_pattern, content, re.DOTALL)

        if not frontmatter_match:
            # No frontmatter, just replace placeholders
            content = content.replace("{{IDE_CONFIG_DIR}}", ide_dir)
            # Legacy: Also replace hardcoded .claude/ for backward compatibility
            if self.ide == "opencode":
                content = content.replace(".claude/", ".opencode/")
            target_file.write_text(content, encoding="utf-8")
            return

        frontmatter = frontmatter_match.group(1)
        body = frontmatter_match.group(2)

        # Transform tools field ONLY for OpenCode
        # OpenCode uses `permission` (not deprecated `tools`) with keys:
        # read, edit, grep, glob, bash, task, webfetch, websearch, lsp, etc.
        # See: https://opencode.ai/docs/agents/#permissions
        if self.ide == "opencode":
            tools_pattern = r"^tools:\s*(.+)$"
            tools_match = re.search(tools_pattern, frontmatter, re.MULTILINE)

            if tools_match:
                tools_str = tools_match.group(1).strip()

                # Map Claude Code tool names to OpenCode permission keys
                # OpenCode 'edit' gates write, edit, apply_patch tools
                tool_to_permission = {
                    "Read": "read",
                    "Write": "edit",
                    "Edit": "edit",
                    "Task": "task",
                    "Grep": "grep",
                    "Glob": "glob",
                    "Bash": "bash",
                    "WebSearch": "websearch",
                    "WebFetch": "webfetch",
                }

                # Parse tools list and deduplicate permission keys
                tools = [t.strip() for t in tools_str.split(",")]
                permissions = {}
                for tool in tools:
                    perm_key = tool_to_permission.get(tool)
                    if perm_key:
                        permissions[perm_key] = "allow"

                # Build OpenCode permission format (replaces deprecated tools:)
                if permissions:
                    permission_yaml = "permission:\n" + "\n".join(
                        f"  {key}: {value}" for key, value in permissions.items()
                    )
                else:
                    permission_yaml = "permission: {}"

                # Replace in frontmatter
                frontmatter = re.sub(
                    r"^tools:\s*.+$", permission_yaml, frontmatter, flags=re.MULTILINE
                )

        # Replace placeholders in body
        body = body.replace("{{IDE_CONFIG_DIR}}", ide_dir)

        # Legacy: Also replace hardcoded .claude/ for backward compatibility
        if self.ide == "opencode":
            body = body.replace(".claude/", ".opencode/")

        # Reconstruct file
        new_content = f"---\n{frontmatter}\n---\n{body}"
        target_file.write_text(new_content, encoding="utf-8")

    def _apply_format(self):
        """Apply IDE-specific format and config files"""
        if self.ide == "claude":
            # Copy Claude-specific settings
            if (self.format_dir / "settings.json").exists():
                shutil.copy2(
                    self.format_dir / "settings.json",
                    self.target_config_dir / "settings.json",
                )

            if (self.format_dir / "settings.local.json").exists():
                shutil.copy2(
                    self.format_dir / "settings.local.json",
                    self.target_config_dir / "settings.local.json",
                )

            # Copy MCP config
            mcp_source = self.templates_dir / ".mcp.json"
            if mcp_source.exists():
                shutil.copy2(mcp_source, self.target_mcp)

        else:  # opencode
            # Copy OpenCode config
            if (self.format_dir / "opencode.json").exists():
                shutil.copy2(self.format_dir / "opencode.json", self.target_config_file)

    def validate(self) -> bool:
        """Validate installation

        Checks if all required files are present.

        Returns:
            True if validation passes, False otherwise
        """
        config_prefix = ".claude" if self.ide == "claude" else ".opencode"

        required_files = [
            # UI/UX Analysis Workflow (skill-based, replaces agent)
            f"{config_prefix}/skills/uiux-analysis-workflow/SKILL.md",
            # Execution Skills
            f"{config_prefix}/skills/project-docs-contract/SKILL.md",
            f"{config_prefix}/skills/project-docs-lifecycle/SKILL.md",
            f"{config_prefix}/skills/project-docs-workflow/SKILL.md",
            f"{config_prefix}/skills/project-docs-quality-gates/SKILL.md",
            # Spec Skills
            f"{config_prefix}/skills/spec-creation-contract/SKILL.md",
            f"{config_prefix}/skills/spec-workflow/SKILL.md",
            f"{config_prefix}/skills/spec-requirements/SKILL.md",
            f"{config_prefix}/skills/spec-design/SKILL.md",
            f"{config_prefix}/skills/spec-tasks/SKILL.md",
            f"{config_prefix}/skills/spec-refine/SKILL.md",
            f"{config_prefix}/skills/spec-quality-gates/SKILL.md",
            # Execution Skills
            f"{config_prefix}/skills/execution-workflow/SKILL.md",
            f"{config_prefix}/skills/execution-implement/SKILL.md",
            f"{config_prefix}/skills/execution-verify/SKILL.md",
            f"{config_prefix}/skills/execution-quick/SKILL.md",
            f"{config_prefix}/skills/execution-quality-gates/SKILL.md",
            f"{config_prefix}/skills/execution-contract/SKILL.md",
            f"{config_prefix}/skills/uiux-analysis-contract/SKILL.md",
            # UI Redesign Skills (independent post-build flow)
            f"{config_prefix}/skills/ui-redesign/SKILL.md",
            f"{config_prefix}/skills/ui-redesign-craft/SKILL.md",
            f"{config_prefix}/skills/ui-redesign-contract/SKILL.md",
            # Per-Doc Skills
            f"{config_prefix}/skills/project-docs-prd/SKILL.md",
            f"{config_prefix}/skills/project-docs-overview/SKILL.md",
            f"{config_prefix}/skills/project-docs-uc/SKILL.md",
            f"{config_prefix}/skills/project-docs-fr/SKILL.md",
            f"{config_prefix}/skills/project-docs-wireframes/SKILL.md",
            f"{config_prefix}/skills/project-docs-flows/SKILL.md",
            f"{config_prefix}/skills/project-docs-roadmap/SKILL.md",
            f"{config_prefix}/skills/project-docs-review/SKILL.md",
            # iOS Skills
            f"{config_prefix}/skills/ios-architecture/SKILL.md",
            f"{config_prefix}/skills/ios-components/SKILL.md",
            f"{config_prefix}/skills/ios-ui-ux/SKILL.md",
            f"{config_prefix}/skills/ios-debug/SKILL.md",
            f"{config_prefix}/skills/mcp-xcode/SKILL.md",
            f"{config_prefix}/skills/mcp-figma/SKILL.md",
            # Doc Templates (Project Docs)
            f"{config_prefix}/doc-templates/PRD.md",
            f"{config_prefix}/doc-templates/Project_Overview.md",
            f"{config_prefix}/doc-templates/Use_Cases.md",
            f"{config_prefix}/doc-templates/Functional_Requirements.md",
            f"{config_prefix}/doc-templates/Wireframes.md",
            f"{config_prefix}/doc-templates/UX_Flows.md",
            f"{config_prefix}/doc-templates/Project_Implementation_Roadmap.md",
            # Doc Templates (Specs)
            f"{config_prefix}/doc-templates/spec-requirements.md",
            f"{config_prefix}/doc-templates/spec-design.md",
            f"{config_prefix}/doc-templates/spec-tasks.md",
            # Doc Templates (Execution)
            f"{config_prefix}/doc-templates/verification-report.md",
            # Scripts
            f"{config_prefix}/scripts/validate_traceability.py",
            f"{config_prefix}/scripts/validate_cross_spec.py",
            f"{config_prefix}/scripts/validate_agent_compatibility.py",
            # Design-token Pencil templates (for /ios-ui-redesign)
            f"{config_prefix}/design-token/template-neo.pen",
            # Guides
            f"{config_prefix}/shared/COMPONENT_FORMAT.md",
            f"{config_prefix}/shared/PBT_GUIDE.md",
            f"{config_prefix}/shared/PARALLEL_EXECUTION_GUIDE.md",
            f"{config_prefix}/shared/SPEC_WORKFLOW_GUIDE.md",
            f"{config_prefix}/shared/AGENT_COMPATIBILITY_CHECKLIST.md",
            # Commands (OpenCode)
            f"{config_prefix}/commands/ios-project-docs.md",
            f"{config_prefix}/commands/ios-spec.md",
            f"{config_prefix}/commands/ios-execute.md",
            f"{config_prefix}/commands/ios-ui-redesign.md",
        ]

        # Add IDE-specific config files
        if self.ide == "claude":
            required_files.append(".mcp.json")
        else:
            required_files.append("opencode.json")

        for file_path in required_files:
            full_path = self.target_dir / file_path
            if not full_path.exists():
                print(f"Missing: {file_path}")
                return False

        # Claude Code format checks: MCP servers belong in .mcp.json (not settings.json),
        # and .mcp.json only honors standard per-server keys (autoApprove/disabled/
        # disabledTools are silently ignored by Claude Code).
        if self.ide == "claude" and not self._validate_claude_mcp_format():
            return False

        return True

    def _validate_claude_mcp_format(self) -> bool:
        """Ensure Claude Code MCP config uses the correct format.

        Returns False (with a printed reason) if:
        - settings.json defines `mcpServers` (Claude Code does not load them there)
        - .mcp.json uses non-standard per-server keys that Claude Code ignores
        """
        import json

        settings_path = self.target_config_dir / "settings.json"
        if settings_path.exists():
            try:
                settings = json.loads(settings_path.read_text(encoding="utf-8"))
            except json.JSONDecodeError as e:
                print(f"Invalid JSON in {settings_path}: {e}")
                return False
            if "mcpServers" in settings:
                print(
                    "Invalid Claude Code format: settings.json must not define "
                    "'mcpServers'. Define MCP servers in .mcp.json instead."
                )
                return False

        forbidden_keys = {"autoApprove", "disabled", "disabledTools"}
        if self.target_mcp.exists():
            try:
                mcp = json.loads(self.target_mcp.read_text(encoding="utf-8"))
            except json.JSONDecodeError as e:
                print(f"Invalid JSON in {self.target_mcp}: {e}")
                return False
            for name, server in (mcp.get("mcpServers") or {}).items():
                if isinstance(server, dict):
                    bad = forbidden_keys & set(server)
                    if bad:
                        print(
                            f"Invalid Claude Code format: server '{name}' in "
                            f".mcp.json uses unsupported key(s) {sorted(bad)}. "
                            "Use permission rules (mcp__<server>__<tool>) instead."
                        )
                        return False

        return True

    def uninstall(self):
        """Remove toolkit files

        Removes:
        - Config directory (.claude/ or .opencode/)
        - Config files (.mcp.json or opencode.json)
        """
        # Remove config directory
        if self.target_config_dir.exists():
            shutil.rmtree(self.target_config_dir)

        # Remove config files
        if self.ide == "claude" and self.target_mcp.exists():
            self.target_mcp.unlink()
        elif self.ide == "opencode" and self.target_config_file.exists():
            self.target_config_file.unlink()

    def get_installed_components(self) -> Dict[str, bool]:
        """Get status of installed components

        Returns:
            Dictionary mapping component names to installation status
        """
        return {
            "Skills": (self.target_config_dir / "skills").exists(),
            "Agents": (self.target_config_dir / "agents").exists() if (self.content_dir / "agents").exists() else False,
            "Doc Templates": (self.target_config_dir / "doc-templates").exists(),
            "Scripts": (self.target_config_dir / "scripts").exists(),
            "Guides": (self.target_config_dir / "shared").exists(),
            "Commands": (self.target_config_dir / "commands").exists(),
            "Design Tokens (.pen)": (self.target_config_dir / "design-token").exists() if (self.content_dir / "design-token").exists() else False,
            "Config": (
                self.target_mcp.exists()
                if self.ide == "claude"
                else self.target_config_file.exists()
            ),
        }
