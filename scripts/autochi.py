#!/usr/bin/env python3
"""Terminal-first project scaffolding and status tracking for AutoCHIResearch."""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List


ROOT = Path(__file__).resolve().parents[1]
LEGACY_PROJECTS_DIR = ROOT / "projects"
DEFAULT_PROJECTS_BASENAME = "autochiresearch-projects"


@dataclass(frozen=True)
class PhaseSpec:
    phase_id: str
    label: str
    label_zh: str
    description: str


@dataclass(frozen=True)
class StageSpec:
    stage_id: str
    label: str
    label_zh: str
    phase_id: str
    artifact: str
    skills: List[str]
    description: str


PHASES = [
    PhaseSpec(
        "pre",
        "Pre",
        "前期",
        "Idea shaping, literature retrieval, novelty judgment, and topic keep/pivot decisions.",
    ),
    PhaseSpec(
        "mid",
        "Mid",
        "中期",
        "Study design, optional questionnaire or prototype work, deployment, collection, and analysis setup.",
    ),
    PhaseSpec(
        "post",
        "Post",
        "后期",
        "Writing, result synthesis, and conclusion-building after the experimental work is complete.",
    ),
]


STAGES = [
    StageSpec(
        "brief",
        "Research Brief",
        "研究简报",
        "pre",
        "artifacts/research-brief.md",
        ["chi-project-runner"],
        "Translate the raw idea into a concrete HCI problem, users, contribution, and constraints.",
    ),
    StageSpec(
        "novelty",
        "Novelty Matrix",
        "文献与新颖性矩阵",
        "pre",
        "artifacts/novelty-matrix.md",
        ["citation-management", "chi-topic-scout"],
        "Search adjacent work, validate citations, and decide keep / pivot / drop.",
    ),
    StageSpec(
        "study",
        "Study Spec",
        "研究设计与问卷/原型方案",
        "mid",
        "artifacts/study-spec.md",
        ["hci-study-designer"],
        "Decide whether a user study, questionnaire, prototype, or mixed-methods setup is needed and specify it.",
    ),
    StageSpec(
        "deployment",
        "Deployment and Collection",
        "部署与收数准备",
        "mid",
        "deploy/deployment-plan.md",
        ["study-deployment-ops", "playwright"],
        "Prepare deployment, questionnaire distribution, session flow, monitoring, and data collection readiness.",
    ),
    StageSpec(
        "analysis",
        "Analysis and Findings",
        "分析与结果整理",
        "mid",
        "analysis/analysis-plan.md",
        ["hci-analysis-writer"],
        "Pre-commit analysis logic and define how the study data will turn into concrete findings.",
    ),
    StageSpec(
        "paper",
        "Writing and Synthesis",
        "写作与结论综合",
        "post",
        "paper/paper-brief.md",
        ["scientific-writing", "citation-management"],
        "Turn the findings into a paper narrative, synthesize results, and prepare LaTeX drafting.",
    ),
]

STAGE_INDEX = {stage.stage_id: stage for stage in STAGES}
PHASE_INDEX = {phase.phase_id: phase for phase in PHASES}
REQUIRED_PAPER_SECTION_SPECS = [
    ("Abstract", r"\\begin\{abstract\}"),
    ("Introduction", r"\\section\{Introduction\}"),
    ("Related Work", r"\\section\{Related Work\}"),
    ("Method", r"\\section\{Method\}"),
    ("Results", r"\\section\{Results\}"),
    ("Discussion", r"\\section\{Discussion\}"),
    ("Limitations", r"\\section\{Limitations\}"),
    ("Ethics and Privacy", r"\\section\{Ethics and Privacy\}"),
    ("Conclusion", r"\\section\{Conclusion\}"),
]
PAPER_REVIEW_DIMENSION_LABELS = [
    "CHI Framing and Contribution",
    "Related Work Coverage",
    "Method and Analysis Alignment",
    "Results Sufficiency",
    "Ethics and Privacy Framing",
    "Citation Hygiene",
    "Writing Cohesion",
]


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def slugify(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    if not slug:
        slug = "idea"
    words = [word for word in slug.split("-") if word]
    return "-".join(words[:8])[:64]


def title_from_idea(idea: str) -> str:
    clean = " ".join(idea.strip().split())
    if not clean:
        return "Untitled AutoCHIResearch Project"
    if len(clean) > 96:
        clean = clean[:93].rstrip() + "..."
    return clean


def resolve_project(path_or_slug: str) -> Path:
    raw = Path(path_or_slug).expanduser()
    if raw.exists():
        return raw.resolve()
    identifiers, preferred_identifier = project_identifiers(path_or_slug)
    for identifier in identifiers:
        for base_dir in project_search_dirs():
            candidate = base_dir / identifier
            if candidate.exists():
                return candidate.resolve()
    return (default_projects_dir() / preferred_identifier).resolve()


def project_identifiers(path_or_slug: str) -> tuple[List[str], str]:
    raw = Path(path_or_slug).expanduser()
    identifiers = [path_or_slug]
    preferred_identifier = path_or_slug
    if raw.parent.name == "projects" and raw.name:
        identifiers.append(raw.name)
        preferred_identifier = raw.name

    unique: List[str] = []
    for identifier in identifiers:
        if identifier not in unique:
            unique.append(identifier)
    return unique, preferred_identifier


def default_projects_dir() -> Path:
    env_path = os.environ.get("AUTOCHI_PROJECTS_DIR")
    if env_path:
        return Path(env_path).expanduser().resolve()
    return (ROOT.parent / DEFAULT_PROJECTS_BASENAME).resolve()


def project_search_dirs() -> List[Path]:
    dirs = [default_projects_dir(), LEGACY_PROJECTS_DIR]
    seen: set[Path] = set()
    ordered: List[Path] = []
    for directory in dirs:
        resolved = directory.resolve()
        if resolved in seen:
            continue
        seen.add(resolved)
        ordered.append(resolved)
    return ordered


def build_state(project_name: str, slug: str, idea: str, venue: str) -> Dict:
    return {
        "schema_version": 2,
        "project": {
            "name": project_name,
            "slug": slug,
            "idea": idea,
            "venue": venue,
            "created_at": now_iso(),
            "updated_at": now_iso(),
        },
        "phases": [
            {
                "id": phase.phase_id,
                "label": phase.label,
                "label_zh": phase.label_zh,
                "description": phase.description,
                "stage_ids": [stage.stage_id for stage in STAGES if stage.phase_id == phase.phase_id],
                "status": "pending",
            }
            for phase in PHASES
        ],
        "workflow": [
            {
                "id": stage.stage_id,
                "label": stage.label,
                "label_zh": stage.label_zh,
                "phase": stage.phase_id,
                "artifact": stage.artifact,
                "skills": stage.skills,
                "description": stage.description,
                "status": "pending",
            }
            for stage in STAGES
        ],
        "current_phase": PHASES[0].phase_id,
        "current_stage": STAGES[0].stage_id,
        "next_action": f"Start with {STAGES[0].label} in {PHASES[0].label} phase: {STAGES[0].artifact}",
    }


def enrich_state_schema(state: Dict) -> Dict:
    old_workflow = {stage["id"]: stage for stage in state.get("workflow", []) if "id" in stage}
    state["schema_version"] = max(int(state.get("schema_version", 1)), 2)
    state["phases"] = [
        {
            "id": phase.phase_id,
            "label": phase.label,
            "label_zh": phase.label_zh,
            "description": phase.description,
            "stage_ids": [stage.stage_id for stage in STAGES if stage.phase_id == phase.phase_id],
            "status": "pending",
        }
        for phase in PHASES
    ]
    state["workflow"] = [
        {
            "id": stage.stage_id,
            "label": stage.label,
            "label_zh": stage.label_zh,
            "phase": stage.phase_id,
            "artifact": stage.artifact,
            "skills": stage.skills,
            "description": stage.description,
            "status": old_workflow.get(stage.stage_id, {}).get("status", "pending"),
        }
        for stage in STAGES
    ]
    if "current_phase" not in state:
        state["current_phase"] = PHASES[0].phase_id
    if "current_stage" not in state:
        state["current_stage"] = STAGES[0].stage_id
    if "next_action" not in state:
        state["next_action"] = f"Start with {STAGES[0].label} in {PHASES[0].label} phase: {STAGES[0].artifact}"
    return state


def render_research_brief(idea: str, venue: str) -> str:
    return f"""# Research Brief
<!-- STATUS: pending -->

## Original Idea
{idea}

## Working Title
TODO

## Research Problem
TODO

## Target Users / Population
TODO

## Interaction or System Concept
TODO

## Expected Contribution
TODO

## Candidate Methods
TODO

## Target Venue
{venue}

## Constraints
TODO

## Success Criteria
TODO
"""


def render_novelty_matrix(idea: str) -> str:
    return f"""# Novelty Matrix
<!-- STATUS: pending -->

## Original Idea
{idea}

## Search Queries
- TODO
- TODO
- TODO

## Source Coverage
- TODO

## Related Work Table
| Paper | Venue/Year | Problem | Method | Population | System/Prototype | Main Finding | Gap vs Us |
| --- | --- | --- | --- | --- | --- | --- | --- |
| TODO | TODO | TODO | TODO | TODO | TODO | TODO | TODO |

## Decision
- Topic status: TODO
- Main novelty axis: TODO
- Keep / Pivot / Drop: TODO
- Why: TODO
"""


def render_study_spec(idea: str) -> str:
    return f"""# Study Specification
<!-- STATUS: pending -->

## Idea Anchor
{idea}

## Research Questions
TODO

## Hypotheses / Evidence Needed
TODO

## Study Type
TODO

## Participants
TODO

## Recruitment Plan
TODO

## Tasks / Flow
TODO

## Measures
TODO

## Prototype Requirements
TODO

## Pilot Checklist
TODO

## Stop Criteria
TODO

## Ethics / Privacy Notes
TODO
"""


def render_deployment_plan(idea: str) -> str:
    return f"""# Deployment Plan
<!-- STATUS: pending -->

## Idea Anchor
{idea}

## Runtime Stack
TODO

## Server / Host
TODO

## Study Routes and Session Flow
TODO

## Operational Checklist
- HTTPS: TODO
- Logging: TODO
- Backups: TODO
- Health checks: TODO
- Session linking: TODO

## Smoke Test Script
TODO

## Collection Monitor Rules
TODO

## Sample Target
TODO

## Data Export Plan
TODO
"""


def render_analysis_plan(idea: str) -> str:
    return f"""# Analysis Plan
<!-- STATUS: pending -->

## Idea Anchor
{idea}

## Inclusion / Exclusion Rules
TODO

## Derived Variables
TODO

## Statistical Analysis
TODO

## Qualitative Analysis
TODO

## Figures and Tables
TODO

## Reporting Notes
TODO
"""


def render_paper_brief(idea: str, venue: str) -> str:
    return f"""# Paper Brief
<!-- STATUS: pending -->

## Original Idea
{idea}

## Target Venue
{venue}

## Working Title
TODO

## Abstract Focus
TODO

## Introduction Claim
TODO

## Related Work Angle
TODO

## Method Story
TODO

## Results Spine
TODO

## Discussion Arc
TODO

## Limitations
TODO
"""


def render_paper_review() -> str:
    return """# Paper Judge Review
<!-- STATUS: pending -->

## Scope
- Manuscript: `paper/main.tex`
- Brief: `paper/paper-brief.md`
- Results Summary: `output/analysis/results_summary.md`
- References: `paper/references.bib`

## Decision
Overall Verdict: REVISE
Ready for completion: NO

## Dimension Ratings
CHI Framing and Contribution: REVISE
Related Work Coverage: REVISE
Method and Analysis Alignment: REVISE
Results Sufficiency: REVISE
Ethics and Privacy Framing: REVISE
Citation Hygiene: REVISE
Writing Cohesion: REVISE

## Blocking Issues
- TODO

## Revision Priorities
- TODO

## Evidence Notes
- TODO
"""


def render_project_readme(project_title: str, project_slug: str, idea: str) -> str:
    return f"""# {project_title}

## Original Idea
{idea}

## Core Principle

The human provides one raw idea. Codex is expected to take over the remaining research workflow unless blocked by ethics, credentials, or deployment access.

## Workflow Model

### Pre

- research brief
- literature retrieval
- novelty gate

### Mid

- if needed, user study and questionnaire design
- if needed, prototype design and implementation
- questionnaire / prototype deployment and distribution
- experiment execution and data collection
- analysis planning and findings preparation

### Post

- writing
- result synthesis and conclusion building

## How Codex Should Use This Project

1. Read the root `program.md`.
2. Run `python3 scripts/autochi.py status {project_slug}` from the repo root.
3. Work on the current stage artifact and any support files it requires.
4. Run `python3 scripts/autochi.py sync {project_slug}` after each completed stage.
5. Continue until the project reaches `CurrentStage: done`.

## Key Paths

- `STATE.json`: project workflow state
- `artifacts/`: main markdown outputs
- `literature/`: search log and references
- `studies/`: study materials
- `prototype/`: prototype notes or code
- `deploy/`: deployment notes
- `analysis/`: analysis plan and scripts
- `paper/`: LaTeX manuscript files
- `output/`: run outputs, exported tables, screenshots, figures, and intermediate analysis artifacts
"""


def render_project_readme_zh(project_title: str, project_slug: str, idea: str) -> str:
    return f"""# {project_title}

## 原始 Idea
{idea}

## 核心原则

人只需要提供一个原始 idea。除非被伦理审批、服务器权限、账号凭据或部署条件阻塞，否则剩下的研究流程默认由 Codex 接管并推进。

## 工作流结构

### Pre 阶段

- 研究问题整理
- 文献检索
- novelty 判断

### Mid 阶段

- 如有需要，设计 user study / questionnaire
- 如有需要，设计并实现 prototype
- 将问卷或原型部署出去并分发
- 执行实验并收集数据
- 规划分析并整理结果

### Post 阶段

- 写作
- 将实验结果综合成论文叙事和结论

## Codex 使用方式

1. 先读仓库根目录的 `program.md` 或 `program.zh-CN.md`。
2. 在仓库根目录运行 `python3 scripts/autochi.py status {project_slug}`。
3. 根据当前阶段完成对应 artifact 和支撑文件。
4. 每完成一个阶段后运行 `python3 scripts/autochi.py sync {project_slug}`。
5. 持续推进直到项目显示 `CurrentStage: done`。

## 关键路径

- `STATE.json`：项目状态机
- `artifacts/`：核心 markdown 产物
- `literature/`：检索日志与参考文献
- `studies/`：问卷、协议、实验材料
- `prototype/`：原型代码或说明
- `deploy/`：部署与分发
- `analysis/`：分析脚本与结果
- `paper/`：LaTeX 论文
- `output/`：每次运行的导出结果、截图、图表和中间分析产物
"""


def render_project_progress() -> str:
    return """# Progress

## Pre

- [ ] Research brief
- [ ] Novelty matrix

## Mid

- [ ] Study spec
- [ ] Deployment and collection
- [ ] Analysis and findings

## Post

- [ ] Writing and synthesis
"""


def render_output_readme() -> str:
    return """# Output

This directory stores run artifacts rather than source-of-truth study design files.

Recommended subdirectories:

- `analysis/`: generated tables, summaries, and figures
- `collection/`: canonical CSV templates and imported external CSV snapshots
- `exports/`: explicit database or admin exports
- `playwright/`: screenshots and browser-validation artifacts

Keep raw respondent data and identifiable contact exports out of version control when required by ethics or privacy constraints.
"""


def render_literature_log() -> str:
    return """# Search Log
<!-- STATUS: pending -->

## Search Sessions
- TODO

## Citation Notes
- TODO
"""


def render_references_bib() -> str:
    return "% TODO: add validated BibTeX entries here.\n"


def render_project_tex() -> str:
    return r"""\documentclass[sigconf]{acmart}

\title{TODO}

\author{TODO}
\affiliation{%
  \institution{TODO}
  \city{TODO}
  \country{TODO}
}
\email{TODO}

\begin{document}

\begin{abstract}
TODO
\end{abstract}

\maketitle

\section{Introduction}
TODO

\section{Related Work}
TODO

\section{Method}
TODO

\section{Results}
TODO

\section{Discussion}
TODO

\section{Limitations}
TODO

\section{Ethics and Privacy}
TODO

\section{Conclusion}
TODO

\bibliographystyle{ACM-Reference-Format}
\bibliography{references}

\end{document}
"""


def project_files(idea: str, venue: str, project_title: str, project_slug: str) -> Dict[str, str]:
    return {
        "README.md": render_project_readme(project_title, project_slug, idea),
        "README.zh-CN.md": render_project_readme_zh(project_title, project_slug, idea),
        "IDEA.md": f"# Raw Idea\n\n{idea}\n",
        "PROGRESS.md": render_project_progress(),
        "artifacts/research-brief.md": render_research_brief(idea, venue),
        "artifacts/novelty-matrix.md": render_novelty_matrix(idea),
        "artifacts/study-spec.md": render_study_spec(idea),
        "deploy/deployment-plan.md": render_deployment_plan(idea),
        "analysis/analysis-plan.md": render_analysis_plan(idea),
        "paper/paper-brief.md": render_paper_brief(idea, venue),
        "paper/paper-review.md": render_paper_review(),
        "literature/search-log.md": render_literature_log(),
        "literature/references.bib": render_references_bib(),
        "paper/main.tex": render_project_tex(),
        "paper/references.bib": render_references_bib(),
        "studies/survey.md": "# Survey Draft\n<!-- STATUS: pending -->\n\nTODO\n",
        "studies/protocol.md": "# Study Protocol\n<!-- STATUS: pending -->\n\nTODO\n",
        "prototype/README.md": "# Prototype Notes\n<!-- STATUS: pending -->\n\nTODO\n",
        "output/README.md": render_output_readme(),
        "output/analysis/.gitkeep": "",
        "output/collection/.gitkeep": "",
        "output/exports/.gitkeep": "",
        "output/playwright/.gitkeep": "",
    }


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def artifact_complete(path: Path) -> bool:
    if not path.exists():
        return False
    text = path.read_text(encoding="utf-8").strip()
    if not text:
        return False
    return "TODO" not in text and "<!-- STATUS: pending -->" not in text


def tex_visible_word_count(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    text = re.sub(r"(?<!\\)%.*", " ", text)
    for command in ["title", "section", "subsection", "subsubsection", "caption"]:
        text = re.sub(rf"\\{command}\{{([^}}]*)\}}", r" \1 ", text)
    text = re.sub(r"\\(begin|end)\{[^}]*\}", " ", text)
    text = re.sub(r"\\[A-Za-z]+\*?(?:\[[^\]]*\])?(?:\{[^}]*\})?", " ", text)
    text = re.sub(r"[{}\\]", " ", text)
    words = re.findall(r"[A-Za-z0-9][A-Za-z0-9'_-]*", text)
    return len(words)


def paper_review_status(review_path: Path) -> Dict[str, object]:
    status: Dict[str, object] = {
        "exists": review_path.exists(),
        "complete": False,
        "verdict": None,
        "ready_flag": False,
        "dimension_statuses": {},
        "all_dimensions_pass": False,
    }
    if not review_path.exists():
        return status

    review_text = review_path.read_text(encoding="utf-8")
    status["complete"] = artifact_complete(review_path)

    verdict_match = re.search(r"(?mi)^Overall Verdict:\s*(ready|revise|blocked)\s*$", review_text)
    if verdict_match:
        status["verdict"] = verdict_match.group(1).lower()

    ready_match = re.search(r"(?mi)^Ready for completion:\s*(yes|no)\s*$", review_text)
    status["ready_flag"] = bool(ready_match and ready_match.group(1).lower() == "yes")

    dimension_statuses: Dict[str, str | None] = {}
    for label in PAPER_REVIEW_DIMENSION_LABELS:
        match = re.search(rf"(?mi)^{re.escape(label)}:\s*(pass|revise)\s*$", review_text)
        dimension_statuses[label] = match.group(1).lower() if match else None
    status["dimension_statuses"] = dimension_statuses
    status["all_dimensions_pass"] = all(value == "pass" for value in dimension_statuses.values())
    return status


def paper_stage_diagnostics(project_dir: Path, brief_path: Path) -> Dict[str, object]:
    manuscript_path = project_dir / "paper" / "main.tex"
    references_path = project_dir / "paper" / "references.bib"
    review_path = project_dir / "paper" / "paper-review.md"
    results_summary_path = project_dir / "output" / "analysis" / "results_summary.md"

    diagnostics: Dict[str, object] = {
        "brief_complete": artifact_complete(brief_path),
        "manuscript_path": manuscript_path,
        "manuscript_complete": manuscript_path.exists() and artifact_complete(manuscript_path),
        "missing_sections": [],
        "word_count": 0,
        "references_complete": references_path.exists() and artifact_complete(references_path),
        "reference_count": 0,
        "results_summary_complete": results_summary_path.exists() and artifact_complete(results_summary_path),
        "review": paper_review_status(review_path),
    }

    if manuscript_path.exists():
        manuscript_text = manuscript_path.read_text(encoding="utf-8")
        diagnostics["missing_sections"] = [
            label
            for label, pattern in REQUIRED_PAPER_SECTION_SPECS
            if re.search(pattern, manuscript_text) is None
        ]
        diagnostics["word_count"] = tex_visible_word_count(manuscript_path)

    if references_path.exists():
        diagnostics["reference_count"] = len(
            re.findall(r"(?m)^@", references_path.read_text(encoding="utf-8"))
        )

    return diagnostics


def paper_stage_next_action(project_dir: Path, brief_path: Path) -> str:
    diagnostics = paper_stage_diagnostics(project_dir, brief_path)

    if not diagnostics["brief_complete"]:
        return "Complete paper/paper-brief.md before manuscript review."

    if not diagnostics["manuscript_complete"]:
        return (
            "Complete a stand-alone paper draft in paper/main.tex. Short outlines do not count as a "
            "completed paper stage."
        )

    missing_sections = diagnostics["missing_sections"]
    if missing_sections:
        return (
            "Expand paper/main.tex into a full ACM sigconf draft. Missing required sections include: "
            + ", ".join(missing_sections)
            + "."
        )

    word_count = int(diagnostics["word_count"])
    if word_count < 3000:
        return (
            f"Expand paper/main.tex before review. The manuscript currently has about {word_count} visible words; "
            "paper completion requires a stand-alone draft of at least 3000 words."
        )

    if not diagnostics["references_complete"] or int(diagnostics["reference_count"]) < 8:
        return (
            "Complete paper/references.bib with validated citations before paper completion. "
            f"Current BibTeX entry count: {diagnostics['reference_count']}."
        )

    if not diagnostics["results_summary_complete"]:
        return "Complete output/analysis/results_summary.md before paper completion."

    review = diagnostics["review"]
    if not review["exists"] or not review["complete"]:
        return (
            "Spawn a dedicated paper-judge sub-agent, have it independently review the manuscript, and "
            "write paper/paper-review.md. Paper completion requires a READY verdict from that review."
        )

    if review["verdict"] != "ready" or not review["ready_flag"] or not review["all_dimensions_pass"]:
        failing_dimensions = [
            label
            for label, value in review["dimension_statuses"].items()
            if value != "pass"
        ]
        if failing_dimensions:
            return (
                "Address the blocking items in paper/paper-review.md, revise the manuscript, and rerun the "
                "paper-judge sub-agent. Outstanding review dimensions: "
                + ", ".join(failing_dimensions)
                + "."
            )
        return (
            "Address the blocking items in paper/paper-review.md, revise the manuscript, and rerun the "
            "paper-judge sub-agent until the review verdict is READY."
        )

    return "Paper review is READY. The manuscript can be treated as complete for the tracked paper stage."


def paper_stage_complete(project_dir: Path, brief_path: Path) -> bool:
    diagnostics = paper_stage_diagnostics(project_dir, brief_path)
    review = diagnostics["review"]
    return (
        bool(diagnostics["brief_complete"])
        and bool(diagnostics["manuscript_complete"])
        and not diagnostics["missing_sections"]
        and int(diagnostics["word_count"]) >= 3000
        and bool(diagnostics["references_complete"])
        and int(diagnostics["reference_count"]) >= 8
        and bool(diagnostics["results_summary_complete"])
        and bool(review["exists"])
        and bool(review["complete"])
        and review["verdict"] == "ready"
        and bool(review["ready_flag"])
        and bool(review["all_dimensions_pass"])
    )


def stage_complete(project_dir: Path, stage: Dict) -> bool:
    artifact_path = project_dir / stage["artifact"]
    if stage["id"] == "paper":
        return paper_stage_complete(project_dir, artifact_path)
    return artifact_complete(artifact_path)


def novelty_gate_decision(project_dir: Path) -> str | None:
    novelty_path = project_dir / "artifacts" / "novelty-matrix.md"
    if not novelty_path.exists():
        return None
    text = novelty_path.read_text(encoding="utf-8")
    match = re.search(r"Keep\s*/\s*Pivot\s*/\s*Drop:\s*([A-Za-z]+)", text, re.IGNORECASE)
    if not match:
        return None
    decision = match.group(1).strip().lower()
    if decision in {"keep", "pivot", "drop"}:
        return decision
    return None


def refresh_phase_statuses(state: Dict) -> None:
    workflow = state["workflow"]
    for phase in state["phases"]:
        statuses = [stage["status"] for stage in workflow if stage["phase"] == phase["id"]]
        if statuses and all(status == "complete" for status in statuses):
            phase["status"] = "complete"
        elif any(status == "complete" for status in statuses):
            phase["status"] = "in_progress"
        else:
            phase["status"] = "pending"


def sync_project(project_dir: Path) -> Dict:
    state_path = project_dir / "STATE.json"
    if not state_path.exists():
        raise SystemExit(f"Missing STATE.json in {project_dir}")

    state = enrich_state_schema(json.loads(state_path.read_text(encoding="utf-8")))
    current = None
    for stage in state["workflow"]:
        complete = stage_complete(project_dir, stage)
        stage["status"] = "complete" if complete else "pending"
        if current is None and not complete:
            current = stage

    refresh_phase_statuses(state)
    gate_decision = novelty_gate_decision(project_dir)
    if gate_decision in {"pivot", "drop"}:
        state["current_phase"] = "pre"
        state["current_stage"] = "novelty"
        state["next_action"] = (
            f"Novelty gate decision: {gate_decision.upper()}. "
            "Stop before study design and reformulate the idea into a keep-worthy HCI direction."
        )
    elif current:
        phase = PHASE_INDEX[current["phase"]]
        state["current_phase"] = current["phase"]
        state["current_stage"] = current["id"]
        if current["id"] == "paper":
            state["next_action"] = paper_stage_next_action(project_dir, project_dir / current["artifact"])
        else:
            state["next_action"] = (
                f"Complete {current['label']} in {phase.label} phase at {current['artifact']} "
                f"using {', '.join(current['skills'])}."
            )
    else:
        state["current_phase"] = "done"
        state["current_stage"] = "done"
        state["next_action"] = "All tracked stage artifacts are complete. Move into implementation, deployment, data collection, or manuscript polishing."
    state["project"]["updated_at"] = now_iso()

    state_path.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return state


def init_project(args: argparse.Namespace) -> int:
    projects_dir = Path(args.workspace).resolve()
    projects_dir.mkdir(parents=True, exist_ok=True)
    slug = args.slug or slugify(args.idea)
    project_title = title_from_idea(args.idea)
    project_dir = projects_dir / slug
    if project_dir.exists() and any(project_dir.iterdir()):
        raise SystemExit(f"Project already exists and is not empty: {project_dir}")

    project_dir.mkdir(parents=True, exist_ok=True)
    state = build_state(project_name=project_title, slug=slug, idea=args.idea.strip(), venue=args.venue)
    write_file(project_dir / "STATE.json", json.dumps(state, indent=2, ensure_ascii=False) + "\n")

    for rel_path, content in project_files(args.idea.strip(), args.venue, project_title, slug).items():
        write_file(project_dir / rel_path, content)

    print(project_dir)
    print(f"Initialized project '{slug}' for venue {args.venue}.")
    print("Next:")
    print(f"  python3 scripts/autochi.py status {project_dir}")
    return 0


def migrate_legacy_projects_cmd(args: argparse.Namespace) -> int:
    source_dir = LEGACY_PROJECTS_DIR.resolve()
    target_dir = Path(args.workspace).resolve()

    if source_dir == target_dir:
        raise SystemExit("Legacy projects directory and target directory are the same.")

    if not source_dir.exists():
        print(f"No legacy projects directory found at {source_dir}.")
        return 0

    target_dir.mkdir(parents=True, exist_ok=True)
    legacy_projects = [entry for entry in sorted(source_dir.iterdir()) if entry.is_dir() and not entry.is_symlink()]

    moved: List[Path] = []
    skipped: List[str] = []
    for project_dir in legacy_projects:
        destination = target_dir / project_dir.name
        if destination.exists():
            skipped.append(f"{project_dir.name} (destination exists: {destination})")
            continue
        shutil.move(str(project_dir), str(destination))
        moved.append(destination)

    print(f"Legacy source: {source_dir}")
    print(f"Target:        {target_dir}")
    print(f"Moved:         {len(moved)} project(s)")
    for destination in moved:
        print(f"  - {destination}")
    if skipped:
        print(f"Skipped:       {len(skipped)} project(s)")
        for item in skipped:
            print(f"  - {item}")
    if not moved and not skipped:
        print("No legacy projects to migrate.")
    return 0


def print_status(state: Dict, project_dir: Path, as_json: bool = False) -> int:
    state = enrich_state_schema(state)
    refresh_phase_statuses(state)
    if as_json:
        print(json.dumps(state, indent=2, ensure_ascii=False))
        return 0

    print(f"Project:      {state['project']['name']}")
    print(f"Venue:        {state['project']['venue']}")
    print(f"CurrentPhase: {state['current_phase']}")
    print(f"CurrentStage: {state['current_stage']}")
    print(f"NextAction:   {state['next_action']}")
    print("Phases:")
    for phase in state["phases"]:
        print(
            f"  - {phase['id']:<5} {phase['status']:<11} "
            f"{phase['label']} / {phase['label_zh']}"
        )
        for stage in [stage for stage in state["workflow"] if stage["phase"] == phase["id"]]:
            artifact = project_dir / stage["artifact"]
            print(
                f"      * {stage['id']:<10} {stage['status']:<8} "
                f"{stage['artifact']} | skills={','.join(stage['skills'])}"
            )
            if artifact.exists():
                size = len(artifact.read_text(encoding="utf-8").strip().splitlines())
                print(f"        lines={size}")
    return 0


def status_project(args: argparse.Namespace) -> int:
    project_dir = resolve_project(args.project)
    state_path = project_dir / "STATE.json"
    if not state_path.exists():
        raise SystemExit(f"Missing STATE.json in {project_dir}")
    state = json.loads(state_path.read_text(encoding="utf-8"))
    return print_status(state, project_dir, as_json=args.json)


def sync_project_cmd(args: argparse.Namespace) -> int:
    project_dir = resolve_project(args.project)
    state = sync_project(project_dir)
    return print_status(state, project_dir, as_json=args.json)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="AutoCHIResearch terminal orchestrator")
    subparsers = parser.add_subparsers(dest="command", required=True)
    default_workspace = default_projects_dir()

    init_parser = subparsers.add_parser("init", help="Create a new project from a raw idea")
    init_parser.add_argument("--idea", required=True, help="Raw project idea")
    init_parser.add_argument("--slug", help="Optional project slug")
    init_parser.add_argument("--venue", default="CHI", help="Target venue (default: CHI)")
    init_parser.add_argument(
        "--workspace",
        default=str(default_workspace),
        help=(
            "Projects directory "
            f"(default: {default_workspace}; override globally with AUTOCHI_PROJECTS_DIR)"
        ),
    )
    init_parser.set_defaults(func=init_project)

    status_parser = subparsers.add_parser("status", help="Show project workflow status")
    status_parser.add_argument("project", help="Project path or slug")
    status_parser.add_argument("--json", action="store_true", help="Print JSON")
    status_parser.set_defaults(func=status_project)

    sync_parser = subparsers.add_parser("sync", help="Recompute stage status from artifact files")
    sync_parser.add_argument("project", help="Project path or slug")
    sync_parser.add_argument("--json", action="store_true", help="Print JSON")
    sync_parser.set_defaults(func=sync_project_cmd)

    migrate_parser = subparsers.add_parser(
        "migrate-legacy-projects",
        help="Move in-repo legacy projects/ directories into the external projects directory",
    )
    migrate_parser.add_argument(
        "--workspace",
        default=str(default_workspace),
        help=(
            "Target projects directory "
            f"(default: {default_workspace}; override globally with AUTOCHI_PROJECTS_DIR)"
        ),
    )
    migrate_parser.set_defaults(func=migrate_legacy_projects_cmd)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    try:
        return args.func(args)
    except KeyboardInterrupt:
        return 130


if __name__ == "__main__":
    sys.exit(main())
