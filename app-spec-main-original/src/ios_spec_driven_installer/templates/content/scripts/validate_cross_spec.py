#!/usr/bin/env python3
"""
Cross-document / cross-spec consistency validation for the spec-driven workflow.

Where `validate_traceability.py` checks ONE feature's requirements/design/tasks internally,
this script checks the project-wide traceability that silently rots between docs and specs
(gap "type C"): orphan specs, dangling WF references, mis-cited WF IDs, duplicate FRs, and
NFR-ID collisions across specs.

Checks (hard fails):
  1. Orphan spec        — a specs/<feature>/ dir that the Roadmap registry never lists.
  2. Dangling WF ref    — a WF-XXX cited in a spec/roadmap that no screen in Wireframes defines.
  3. Duplicate FR       — an FR whose body is just "Same as FR-XXX".
  4. NFR-ID collision   — the same NFR-XXX id defined by more than one spec (namespace clash).

Checks (warnings — likely wrong, but navigation refs make them non-blocking):
  5. Mis-cited WF       — a spec's requirements/design Source cites a WF the Roadmap did NOT
                          assign to it (e.g. account-management citing WF-003 Confirmation).
  6. FR-label mismatch  — an FR title in the Roadmap traceability differs from Functional_Requirements.

Usage:
    python validate_cross_spec.py <project-name> [specs-root]

`specs-root` defaults to the installed `{{IDE_CONFIG_DIR}}specs` location; pass an explicit path
to run against a checkout (e.g. a test fixture).
"""

import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Set

# Directories under a project that are infrastructure, not user-facing feature specs.
# They are exempt from the "must own a screen" expectations but NOT from orphan checks.
INFRA_SPECS = {"project-structure", "shared-foundations", "performance-optimization", "testing-integration"}


@dataclass
class CrossSpecResult:
    is_valid: bool
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)


class CrossSpecValidator:
    def __init__(self, project_name: str, specs_root: Path):
        self.project_name = project_name
        self.project_dir = specs_root / project_name

        # WF-XXX -> screen title, from Wireframes.md
        self.wf_screens: Dict[str, str] = {}
        # FR-XXX -> title, from Functional_Requirements.md
        self.fr_titles: Dict[str, str] = {}
        # FR-XXX with a "Same as FR-YYY" body
        self.duplicate_frs: Dict[str, str] = {}
        # spec-name -> set(WF-XXX) assigned by the roadmap Feature->Screen mapping
        self.roadmap_spec_screens: Dict[str, Set[str]] = {}
        # FR-XXX -> title as written in the roadmap traceability matrix
        self.roadmap_fr_titles: Dict[str, str] = {}
        # spec dirs actually present on disk
        self.spec_dirs: List[str] = []

    # ---------- parsing ----------

    def _read(self, name: str) -> str:
        f = self.project_dir / name
        return f.read_text(encoding="utf-8") if f.exists() else ""

    def parse(self) -> None:
        self._parse_wireframes()
        self._parse_fr()
        self._parse_roadmap()
        self._collect_spec_dirs()

    def _parse_wireframes(self) -> None:
        content = self._read("Wireframes.md")
        # Screen headings:  ### WF-004: Màn Hình Nhật Ký (Log Hàng Ngày)
        for m in re.finditer(r"^#{2,4}\s+(WF-\d+)\s*[:\-–]\s*(.+)$", content, re.MULTILINE):
            self.wf_screens.setdefault(m.group(1), m.group(2).strip())
        # Fallback: inventory table rows  | WF-004 | Nhật Ký | ...
        for m in re.finditer(r"^\|\s*(WF-\d+)\s*\|\s*([^|]+?)\s*\|", content, re.MULTILINE):
            self.wf_screens.setdefault(m.group(1), m.group(2).strip())

    def _parse_fr(self) -> None:
        content = self._read("Functional_Requirements.md")
        # FR headings: ### FR-012: Display Daily Log   (also matches table forms loosely)
        for m in re.finditer(r"(FR-\d+)\s*[:\-–]\s*([^\n|]+)", content):
            title = m.group(2).strip()
            self.fr_titles.setdefault(m.group(1), title)
        # Duplicate bodies: a "same as FR-YYY" line is attributed to the nearest preceding FR heading.
        current_fr = None
        for line in content.splitlines():
            h = re.match(r"^#{2,4}\s+(FR-\d+)\b", line)
            if h:
                current_fr = h.group(1)
                continue
            d = re.search(r"[Ss]ame as (FR-\d+)", line)
            if d and current_fr and d.group(1) != current_fr:
                self.duplicate_frs.setdefault(current_fr, d.group(1))

    def _parse_roadmap(self) -> None:
        content = self._read("Project_Implementation_Roadmap.md")
        # Feature->Screen rows:  | `dashboard-view` | WF-005 (Dashboard), WF-015 (Share Modal) | ...
        for line in content.splitlines():
            m = re.match(r"^\|\s*`([a-z0-9][a-z0-9-]*)`\s*\|(.*)$", line)
            if not m:
                continue
            spec = m.group(1)
            wfs = set(re.findall(r"\bWF-\d+\b", m.group(2)))
            if wfs:
                self.roadmap_spec_screens.setdefault(spec, set()).update(wfs)
        # JSON registry keys:  "dashboard-view": {"status": ...}
        for m in re.finditer(r'"([a-z0-9][a-z0-9-]*)":\s*\{[^\n]*"(?:status|phase|priority)"', content):
            self.roadmap_spec_screens.setdefault(m.group(1), set())
        # JSON "wf": ["WF-005", "WF-015"] attached to the nearest preceding spec key
        for m in re.finditer(r'"([a-z0-9][a-z0-9-]*)":\s*\{[^}]*?"wf":\s*\[([^\]]*)\]', content):
            spec = m.group(1)
            wfs = set(re.findall(r"\bWF-\d+\b", m.group(2)))
            self.roadmap_spec_screens.setdefault(spec, set()).update(wfs)
        # Roadmap FR labels: FR-024 = "Cancel subscription"  /  | FR-024 | Cancel ... |
        for m in re.finditer(r"(FR-\d+)\s*[=:]\s*\"?([^\"|\n]+)", content):
            self.roadmap_fr_titles.setdefault(m.group(1), m.group(2).strip())

    def _collect_spec_dirs(self) -> None:
        if not self.project_dir.exists():
            return
        for child in sorted(self.project_dir.iterdir()):
            if child.is_dir() and (child / "requirements.md").exists():
                self.spec_dirs.append(child.name)

    # ---------- checks ----------

    def validate(self) -> CrossSpecResult:
        if not self.project_dir.exists():
            return CrossSpecResult(False, [f"Project dir not found: {self.project_dir}"])
        self.parse()

        errors: List[str] = []
        warnings: List[str] = []

        known_specs = set(self.roadmap_spec_screens.keys())

        # 1. Orphan spec
        for spec in self.spec_dirs:
            if spec not in known_specs:
                errors.append(
                    f"Orphan spec '{spec}': has requirements.md but is absent from the Roadmap "
                    f"registry / Feature→Screen mapping / dependency JSON"
                )

        # 3. Duplicate FR
        for dup, src in sorted(self.duplicate_frs.items()):
            errors.append(f"Duplicate FR: {dup} body is 'Same as {src}' — merge or differentiate (each FR-ID unique in content)")

        # 2/5 per-spec WF reference checks + 4 NFR collision
        nfr_owner: Dict[str, str] = {}
        for spec in self.spec_dirs:
            text = ""
            for fname in ("requirements.md", "design.md"):
                text += "\n" + (self.project_dir / spec / fname).read_text(encoding="utf-8") if (self.project_dir / spec / fname).exists() else ""

            cited_wfs = set(re.findall(r"\bWF-\d+\b", text))
            for wf in sorted(cited_wfs):
                if self.wf_screens and wf not in self.wf_screens:
                    errors.append(f"Dangling WF ref in '{spec}': {wf} is not defined in Wireframes.md")
            assigned = self.roadmap_spec_screens.get(spec, set())
            if assigned and spec not in INFRA_SPECS:
                stray = sorted(w for w in cited_wfs if w not in assigned and w in self.wf_screens)
                if stray:
                    warnings.append(
                        f"Possible mis-cited WF in '{spec}': cites {', '.join(stray)} but the roadmap "
                        f"assigns it {', '.join(sorted(assigned)) or '(none)'} — verify these are navigation refs, not wrong IDs"
                    )

            # 4. NFR-ID collision across specs
            for nfr in set(re.findall(r"\bNFR-[A-Z]{1,4}-\d+\b", text)):
                if nfr in nfr_owner and nfr_owner[nfr] != spec:
                    errors.append(f"NFR-ID collision: {nfr} defined in both '{nfr_owner[nfr]}' and '{spec}' — namespaces must be unique per spec")
                else:
                    nfr_owner.setdefault(nfr, spec)

        # 2b. Dangling WF in roadmap mapping
        for spec, wfs in self.roadmap_spec_screens.items():
            for wf in sorted(wfs):
                if self.wf_screens and wf not in self.wf_screens:
                    errors.append(f"Dangling WF ref in Roadmap for '{spec}': {wf} not defined in Wireframes.md")

        # 6. FR label mismatch (warning; token-overlap heuristic)
        for fr, rtitle in sorted(self.roadmap_fr_titles.items()):
            ftitle = self.fr_titles.get(fr)
            if ftitle and not self._titles_overlap(rtitle, ftitle):
                warnings.append(
                    f"FR-label mismatch for {fr}: Roadmap says '{rtitle}' but Functional_Requirements says '{ftitle}' — possible swapped/mislabeled FR"
                )

        return CrossSpecResult(is_valid=(len(errors) == 0), errors=errors, warnings=warnings)

    @staticmethod
    def _titles_overlap(a: str, b: str) -> bool:
        stop = {"the", "a", "an", "of", "to", "and", "or", "for", "vs", "with", "subscription", "user"}
        def toks(s: str) -> Set[str]:
            return {w for w in re.findall(r"[a-z]+", s.lower()) if w not in stop and len(w) > 2}
        ta, tb = toks(a), toks(b)
        if not ta or not tb:
            return True
        return len(ta & tb) > 0


def print_result(result: CrossSpecResult, project: str) -> None:
    print(f"\n{'=' * 64}")
    print(f"Cross-Spec Consistency Validation: {project}")
    print(f"{'=' * 64}\n")
    print("✅ VALIDATION PASSED\n" if result.is_valid else "❌ VALIDATION FAILED\n")
    if result.errors:
        print(f"🔴 Errors ({len(result.errors)}):")
        for e in result.errors:
            print(f"  - {e}")
        print()
    if result.warnings:
        print(f"⚠️  Warnings ({len(result.warnings)}):")
        for w in result.warnings:
            print(f"  - {w}")
        print()
    if not result.errors and not result.warnings:
        print("✨ No cross-spec issues found!\n")
    print(f"{'=' * 64}\n")


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python validate_cross_spec.py <project-name> [specs-root]")
        sys.exit(1)
    project = sys.argv[1]
    specs_root = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("{{IDE_CONFIG_DIR}}specs")
    result = CrossSpecValidator(project, specs_root).validate()
    print_result(result, project)
    sys.exit(0 if result.is_valid else 1)


if __name__ == "__main__":
    main()
