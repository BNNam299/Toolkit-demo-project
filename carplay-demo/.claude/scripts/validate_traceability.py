#!/usr/bin/env python3
"""
Traceability validation for spec-driven workflow.

Validates references across:
- requirements.md (AC IDs, FR/UC source references, Evidence summary)
- design.md (design sections + properties)
- tasks.md (task registry + checklist tasks + traceability matrix)

Extended validation:
- FR/UC upstream traceability
- Evidence References presence
"""

import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Set


@dataclass
class ValidationResult:
    is_valid: bool
    broken_references: List[str]
    orphaned_items: List[str]
    missing_references: List[str]
    warnings: List[str]


@dataclass
class TaskMeta:
    task_id: str
    title: str
    task_type: str
    status: str
    ac_refs: List[str]
    design_refs: List[str]


class TraceabilityValidator:
    def __init__(self, feature_name: str):
        self.feature_name = feature_name
        self.spec_dir = Path(f".claude/specs/{feature_name}")

        self.acceptance_criteria: Set[str] = set()
        self.design_sections: Set[str] = set()
        self.properties: Set[str] = set()
        self.property_ac_refs: Dict[str, List[str]] = {}

        # Upstream traceability
        self.functional_requirements: Set[str] = set()  # FR-\d+
        self.use_cases: Set[str] = set()  # UC-\d+
        self.requirement_fr_refs: Dict[str, List[str]] = {}  # req_id -> [FR-XXX, UC-XXX]
        self.requirement_nfr_refs: Dict[str, List[str]] = {}  # req_id -> [NFR-XXX]
        self.has_evidence_references: bool = False

        # Infra-spec allowance: a spec the roadmap registry declares with an empty
        # covers ({fr: [], uc: [], wf: []}) has no FR/UC to cite by construction, so
        # NFR-XXX counts as a valid Source. None = registry not readable (strict mode).
        self.spec_type: Optional[str] = None
        self.covers_empty: bool = False
        self.infra_source_note: Optional[str] = None

        self.tasks: Dict[str, TaskMeta] = {}
        self.traceability_rows: Dict[str, Dict[str, str]] = {}

    def validate(self) -> ValidationResult:
        if not self.spec_dir.exists():
            return ValidationResult(
                is_valid=False,
                broken_references=[f"Spec directory not found: {self.spec_dir}"],
                orphaned_items=[],
                missing_references=[],
                warnings=[],
            )

        self._load_roadmap_registry()
        self._parse_requirements()
        self._parse_design()
        self._parse_tasks()

        broken = self._find_broken_references()
        orphaned = self._find_orphaned_items()
        missing = self._find_missing_references()
        warnings = self._find_warnings()
        upstream_issues = self._find_upstream_issues()

        # Add upstream issues to broken if present
        broken.extend(upstream_issues)

        # Surface the infra allowance so an NFR-sourced spec is auditable, not silent
        if self.infra_source_note:
            warnings.append(self.infra_source_note)

        return ValidationResult(
            is_valid=(len(broken) == 0 and len(missing) == 0),
            broken_references=broken,
            orphaned_items=orphaned,
            missing_references=missing,
            warnings=warnings,
        )

    def _load_roadmap_registry(self) -> None:
        """Read this spec's entry in the roadmap registry to learn its type and covers.

        Resolution: spec-state.json -> project -> that project's
        Project_Implementation_Roadmap.md -> first ```json fence holding "specs".
        Any failure leaves covers_empty = False, i.e. the strict FR/UC rule applies.
        """
        state_file = self.spec_dir / "spec-state.json"
        if not state_file.exists():
            return
        try:
            project = json.loads(state_file.read_text()).get("project")
        except (json.JSONDecodeError, OSError):
            return
        if not project:
            return

        roadmap = Path(f".claude/specs/{project}/Project_Implementation_Roadmap.md")
        if not roadmap.exists():
            return

        entry = None
        for block in re.findall(r"```json\s*\n(.*?)\n```", roadmap.read_text(), re.DOTALL):
            if '"specs"' not in block:
                continue
            try:
                specs = json.loads(block).get("specs")
            except json.JSONDecodeError:
                continue
            if isinstance(specs, dict) and self.feature_name in specs:
                entry = specs[self.feature_name]
                break

        if not isinstance(entry, dict):
            return

        self.spec_type = entry.get("type")
        covers = entry.get("covers") or {}
        self.covers_empty = not any(covers.get(k) for k in ("fr", "uc", "wf"))

    def _parse_requirements(self) -> None:
        req_file = self.spec_dir / "requirements.md"
        if not req_file.exists():
            return

        content = req_file.read_text()

        # Parse AC IDs
        ac_pattern = r"\b(AC-\d+\.\d+)\b"
        self.acceptance_criteria = set(re.findall(ac_pattern, content))

        # Parse FR/UC source references
        # Format: **Source:** [FR-XXX], [UC-XXX]
        fr_pattern = r"\b(FR-\d+)\b"
        uc_pattern = r"\b(UC-\d+)\b"
        nfr_pattern = r"\b(NFR-\d+)\b"

        # Map every AC to the Source field of the requirement block it lives in.
        # Blocks are delimited by the requirement headings themselves (### REQ-XXX / ###
        # Requirement N), so an AC is attributed to its own requirement rather than to
        # whatever Source happens to sit within N characters of it.
        req_heading = r"^#{2,4}\s+(?:REQ-\d+|Requirement\s+\d+)\b.*$"
        starts = [m.start() for m in re.finditer(req_heading, content, re.MULTILINE)]
        blocks = [
            content[s:(starts[i + 1] if i + 1 < len(starts) else len(content))]
            for i, s in enumerate(starts)
        ]

        source_section_pattern = r"\*\*Source\*\*:\s*\[([^\]]+)\]"
        for block in blocks:
            source_match = re.search(source_section_pattern, block)
            source_str = source_match.group(1) if source_match else ""
            frs = re.findall(fr_pattern, source_str)
            ucs = re.findall(uc_pattern, source_str)
            nfrs = re.findall(nfr_pattern, source_str)
            for ac in re.findall(ac_pattern, block):
                self.requirement_fr_refs[ac] = frs + ucs
                self.requirement_nfr_refs[ac] = nfrs

        # Check for Evidence References section
        evidence_pattern = r"## Evidence References"
        self.has_evidence_references = bool(re.search(evidence_pattern, content, re.MULTILINE))

    def _parse_design(self) -> None:
        design_file = self.spec_dir / "design.md"
        if not design_file.exists():
            return

        content = design_file.read_text()

        # Markdown heading sections like "## 4. Data Models" or "### 3.1 Feature"
        section_pattern = r"^#{2,3}\s+(\d+(?:\.\d+)*)\b"
        self.design_sections = set(re.findall(section_pattern, content, re.MULTILINE))

        # Property rows in markdown tables
        for line in content.splitlines():
            m = re.match(r"^\|\s*(P\d+)\s*\|", line)
            if m:
                prop = m.group(1)
                self.properties.add(prop)
                acs = re.findall(r"\bAC-\d+\.\d+\b", line)
                if acs:
                    self.property_ac_refs[prop] = acs

    def _parse_tasks(self) -> None:
        tasks_file = self.spec_dir / "tasks.md"
        if not tasks_file.exists():
            return

        content = tasks_file.read_text()
        self._parse_task_registry(content)
        self._parse_checklist_tasks(content)
        self._parse_traceability_matrix(content)

    def _parse_task_registry(self, content: str) -> None:
        # Expected row:
        # | 2.1.1 | Create model | normal | pending | AC-001.1 | 4 | file.swift | 2.1 |
        row_pattern = re.compile(
            r"^\|\s*(\d+(?:\.\d+)+)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*"
            r"([^|]+?)\s*\|\s*([^|]*?)\s*\|\s*([^|]*?)\s*\|\s*([^|]*?)\s*\|\s*([^|]*?)\s*\|$"
        )

        for line in content.splitlines():
            m = row_pattern.match(line.strip())
            if not m:
                continue
            task_id, title, ttype, status, ac_refs, design_refs, _, _ = m.groups()
            ac_list = re.findall(r"\bAC-\d+\.\d+\b", ac_refs)
            design_list = re.findall(r"\b\d+(?:\.\d+)*\b", design_refs)
            self.tasks[task_id] = TaskMeta(
                task_id=task_id,
                title=title.strip(),
                task_type=ttype.strip().lower(),
                status=status.strip().lower(),
                ac_refs=ac_list,
                design_refs=design_list,
            )

    def _parse_checklist_tasks(self, content: str) -> None:
        # Supports:
        # - [ ] **3.1.1** Build ViewModel
        # - [x] 3.1.2 Wire navigation
        pattern = re.compile(
            r"^-\s+\[[x\s]\]\s+(?:\*\*)?(\d+(?:\.\d+)+)(?:\*\*)?\s+(.+)$",
            re.MULTILINE,
        )

        for m in pattern.finditer(content):
            task_id = m.group(1)
            title = m.group(2).strip()
            if task_id not in self.tasks:
                inferred_type = "pbt" if "[pbt]" in title.lower() else "normal"
                self.tasks[task_id] = TaskMeta(
                    task_id=task_id,
                    title=title,
                    task_type=inferred_type,
                    status="unknown",
                    ac_refs=[],
                    design_refs=[],
                )

    def _parse_traceability_matrix(self, content: str) -> None:
        # Expected row:
        # | 2.1.1 | AC-001.1 | 4 | P1 | pending |
        row_pattern = re.compile(
            r"^\|\s*(\d+(?:\.\d+)+)\s*\|\s*([^|]*?)\s*\|\s*([^|]*?)\s*\|\s*([^|]*?)\s*\|\s*([^|]*?)\s*\|$"
        )

        for line in content.splitlines():
            m = row_pattern.match(line.strip())
            if not m:
                continue
            task_id, acs, design_ref, prop, status = m.groups()
            if task_id.lower() == "task id":
                continue
            self.traceability_rows[task_id] = {
                "acs": ", ".join(re.findall(r"\bAC-\d+\.\d+\b", acs)),
                "design": ", ".join(re.findall(r"\b\d+(?:\.\d+)*\b", design_ref)),
                "property": ", ".join(re.findall(r"\bP\d+\b", prop)),
                "status": status.strip().lower(),
            }

    def _find_broken_references(self) -> List[str]:
        broken: List[str] = []

        for task in self.tasks.values():
            for ac in task.ac_refs:
                if ac not in self.acceptance_criteria:
                    broken.append(f"Task {task.task_id} references {ac} (NOT FOUND)")
            for dref in task.design_refs:
                if dref not in self.design_sections:
                    broken.append(
                        f"Task {task.task_id} references Design {dref} (NOT FOUND)"
                    )

        for prop, acs in self.property_ac_refs.items():
            for ac in acs:
                if ac not in self.acceptance_criteria:
                    broken.append(f"Property {prop} validates {ac} (NOT FOUND)")

        for task_id, row in self.traceability_rows.items():
            for ac in re.findall(r"\bAC-\d+\.\d+\b", row["acs"]):
                if ac not in self.acceptance_criteria:
                    broken.append(
                        f"Traceability row {task_id} references {ac} (NOT FOUND)"
                    )

        return broken

    def _find_orphaned_items(self) -> List[str]:
        orphaned: List[str] = []

        referenced_acs: Set[str] = set()
        for task in self.tasks.values():
            referenced_acs.update(task.ac_refs)
        for prop_acs in self.property_ac_refs.values():
            referenced_acs.update(prop_acs)
        for row in self.traceability_rows.values():
            referenced_acs.update(re.findall(r"\bAC-\d+\.\d+\b", row["acs"]))

        for ac in sorted(self.acceptance_criteria):
            if ac not in referenced_acs:
                orphaned.append(f"{ac} not referenced by any task/property/matrix row")

        return orphaned

    def _find_missing_references(self) -> List[str]:
        missing: List[str] = []
        for task in self.tasks.values():
            if not task.ac_refs:
                missing.append(f"Task {task.task_id} has no AC reference")
            if not task.design_refs:
                missing.append(f"Task {task.task_id} has no Design reference")
        return missing

    def _find_upstream_issues(self) -> List[str]:
        """Check for upstream traceability issues (FR/UC linkage)"""
        issues: List[str] = []

        # Check if Evidence References section exists
        if not self.has_evidence_references:
            issues.append("requirements.md is missing Evidence References section")

        # Check if any requirements have FR/UC source references.
        # Infra allowance: when the roadmap registry declares this spec with an empty
        # covers, there is no FR/UC to cite honestly, so an NFR-XXX Source is accepted.
        # Citing an unrelated FR to satisfy the check would be trace laundering.
        requirements_without_source = []
        nfr_sourced = []
        for ac in sorted(self.acceptance_criteria):
            if self.requirement_fr_refs.get(ac):
                continue
            if self.covers_empty and self.requirement_nfr_refs.get(ac):
                nfr_sourced.append(ac)
                continue
            requirements_without_source.append(ac)

        for ac in requirements_without_source:
            if self.covers_empty:
                issues.append(
                    f"AC {ac} lacks FR/UC source reference "
                    f"(spec covers is empty, so an NFR-XXX Source would also be accepted)"
                )
            else:
                issues.append(f"AC {ac} lacks FR/UC source reference")

        if nfr_sourced:
            self.infra_source_note = (
                f"{len(nfr_sourced)} AC(s) sourced from NFR-XXX instead of FR/UC — accepted "
                f"because the roadmap registry declares '{self.feature_name}' "
                f"(type={self.spec_type or 'unknown'}) with an empty covers"
            )

        return issues

    def _find_warnings(self) -> List[str]:
        warnings: List[str] = []

        if len(self.properties) == 0:
            warnings.append("No correctness properties defined")

        pbt_tasks = [
            t
            for t in self.tasks.values()
            if t.task_type == "pbt" or "[pbt]" in t.title.lower()
        ]
        if len(pbt_tasks) == 0:
            warnings.append("No PBT tasks found")

        if len(self.traceability_rows) == 0:
            warnings.append("No Traceability Matrix rows found")

        return warnings


def print_result(result: ValidationResult, feature_name: str) -> None:
    print(f"\n{'=' * 60}")
    print(f"Traceability Validation: {feature_name}")
    print(f"{'=' * 60}\n")

    print("✅ VALIDATION PASSED\n" if result.is_valid else "❌ VALIDATION FAILED\n")

    if result.broken_references:
        print(f"🔴 Broken References ({len(result.broken_references)}):")
        for ref in result.broken_references:
            print(f"  - {ref}")
        print()

    if result.missing_references:
        print(f"🟡 Missing References ({len(result.missing_references)}):")
        for ref in result.missing_references:
            print(f"  - {ref}")
        print()

    if result.orphaned_items:
        print(f"🟠 Orphaned Items ({len(result.orphaned_items)}):")
        for item in result.orphaned_items:
            print(f"  - {item}")
        print()

    if result.warnings:
        print(f"⚠️  Warnings ({len(result.warnings)}):")
        for warning in result.warnings:
            print(f"  - {warning}")
        print()

    if not any(
        [
            result.broken_references,
            result.missing_references,
            result.orphaned_items,
            result.warnings,
        ]
    ):
        print("✨ No issues found!\n")

    print(f"{'=' * 60}\n")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python validate_traceability.py <feature-name>")
        sys.exit(1)

    feature_name = sys.argv[1]
    validator = TraceabilityValidator(feature_name)
    result = validator.validate()
    print_result(result, feature_name)

    sys.exit(0 if result.is_valid else 1)


if __name__ == "__main__":
    main()
