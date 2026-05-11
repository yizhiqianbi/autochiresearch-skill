#!/usr/bin/env python3
"""Terminal-first project scaffolding and status tracking for AutoCHIResearch."""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List


ROOT = Path(__file__).resolve().parents[1]
LEGACY_PROJECTS_DIR = ROOT / "projects"
DEFAULT_PROJECTS_BASENAME = "autochiresearch-projects"
TEMPLATES_DIR = ROOT / "templates"
PAPER_EXPORTS_DIR = Path("output") / "exports"
PAPER_BUILD_DIR = PAPER_EXPORTS_DIR / "paper-build"
PAPER_OUTPUT_PDF = PAPER_EXPORTS_DIR / "paper.pdf"
PAPER_BUILD_STATUS = PAPER_EXPORTS_DIR / "paper-build-status.md"
PAPER_BUILD_LOG = PAPER_EXPORTS_DIR / "paper-build.log"
PAPER_RENDERED_PAGES_DIR = PAPER_EXPORTS_DIR / "rendered-pages"
PAPER_FIGURE_PLAN = Path("paper") / "figure-plan.md"
PAPER_ADVERSARIAL_REVIEW = Path("paper") / "adversarial-review.md"
PAPER_FIGURE_EXPORTS_DIR = PAPER_EXPORTS_DIR / "figures"
MIN_PAPER_WORD_COUNT = 10000
MIN_PAPER_PAGE_COUNT = 10
MIN_PAPER_REFERENCE_COUNT = 40
ARK_DEFAULT_BASE_URL = "https://ark.cn-beijing.volces.com/api/v3"
ARK_DEFAULT_VLM_MODEL = "doubao-seed-2-0-pro-260215"
ARK_DEFAULT_IMAGE_MODEL = "doubao-seedream-5-0-260128"
OPENROUTER_DEFAULT_VLM_MODEL = "google/gemini-2.5-flash"
OPENROUTER_DEFAULT_IMAGE_MODEL = "google/gemini-3.1-flash-image-preview"
DEFAULT_FIGURE_GOAL = (
    "Create a publication-ready CHI figure that explains the method or pipeline at a glance without "
    "looking like marketing art."
)
DEFAULT_FIGURE_VISUAL_STYLE = (
    "Elegant CHI-style academic diagram. Clean layout, restrained palette, strong hierarchy, vector-like "
    "shapes, high-contrast labels, generous whitespace, and a polished but understated look."
)
DEFAULT_FIGURE_MUST_INCLUDE = (
    "Show the core workflow, the role of the human in the loop, the main prototype or instrument "
    "components, and the handoffs between study, build, deployment, analysis, and paper artifacts using "
    "terminology that matches the manuscript."
)
DEFAULT_FIGURE_MUST_AVOID = (
    "Avoid photorealistic scenes, glossy marketing aesthetics, decorative 3D effects, dense background "
    "textures, tiny unreadable labels, clip-art, and any visual element not grounded in the manuscript."
)


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
        "build",
        "Prototype and Instrument Build",
        "原型与问卷构建",
        "mid",
        "artifacts/build-report.md",
        ["hci-study-designer", "playwright"],
        "Build the prototype, questionnaire, or instrument specified in study-spec. Deliver working artifacts, not just plans.",
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
PAPER_ADVERSARIAL_REVIEWER_LABELS = [
    "Reviewer A Methods and Validity",
    "Reviewer B Systems and Interaction Contribution",
    "Reviewer C Related Work and Novelty",
    "Reviewer D Writing Claims and CHI Fit",
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
        "data_mode": None,
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


def render_template(relative_path: str, **replacements: str) -> str:
    template_path = TEMPLATES_DIR / relative_path
    text = template_path.read_text(encoding="utf-8")
    for key, value in replacements.items():
        text = text.replace(f"{{{{{key}}}}}", str(value))
    return text


def render_research_brief(idea: str, venue: str) -> str:
    return render_template("project/artifacts/research-brief.md.tmpl", IDEA=idea, VENUE=venue)


def render_novelty_matrix(idea: str) -> str:
    return render_template("project/artifacts/novelty-matrix.md.tmpl", IDEA=idea)


def render_study_spec(idea: str) -> str:
    return render_template("project/artifacts/study-spec.md.tmpl", IDEA=idea)


def render_deployment_plan(idea: str) -> str:
    return render_template("project/deploy/deployment-plan.md.tmpl", IDEA=idea)


def render_analysis_plan(idea: str) -> str:
    return render_template("project/analysis/analysis-plan.md.tmpl", IDEA=idea)


def render_paper_brief(idea: str, venue: str) -> str:
    return render_template("project/paper/paper-brief.md.tmpl", IDEA=idea, VENUE=venue)


def render_paper_review() -> str:
    return render_template("project/paper/paper-review.md.tmpl")


def render_adversarial_review() -> str:
    return render_template("project/paper/adversarial-review.md.tmpl")


def render_paper_figure_plan(
    *,
    decision: str = "TODO",
    content_source: str = "TODO",
    content_file: str = "TODO",
    figure_goal: str = DEFAULT_FIGURE_GOAL,
    visual_style: str = DEFAULT_FIGURE_VISUAL_STYLE,
    must_include: str = DEFAULT_FIGURE_MUST_INCLUDE,
    must_avoid: str = DEFAULT_FIGURE_MUST_AVOID,
    figure_caption: str = "TODO",
    figure_output: str = "TODO",
    teaser_asset: str = "TODO",
    teaser_caption: str = "TODO",
    teaser_description: str = "TODO",
    main_figure_asset: str = "TODO",
    main_figure_caption: str = "TODO",
    main_figure_description: str = "TODO",
    aspect_ratio: str = "16:9",
    candidate_count: int = 1,
    retrieval_setting: str = "auto",
    pipeline_mode: str = "demo_full",
    main_model_name: str = "",
    image_model_name: str = "",
    human_approval: str = "pending",
    human_review_notes: str = "TODO",
    visual_qa_notes: str = (
        "Pending build. After the first compiled PDF, inspect output/exports/rendered-pages and replace "
        "this note with specific fixes or `No issues found.`"
    ),
    additional_notes: str = "TODO",
) -> str:
    return render_template(
        "project/paper/figure-plan.md.tmpl",
        FIGURE_DECISION=decision,
        CONTENT_SOURCE=content_source,
        CONTENT_FILE=content_file,
        FIGURE_GOAL=figure_goal,
        VISUAL_STYLE=visual_style,
        MUST_INCLUDE=must_include,
        MUST_AVOID=must_avoid,
        FIGURE_CAPTION=figure_caption,
        FIGURE_OUTPUT=figure_output,
        TEASER_ASSET=teaser_asset,
        TEASER_CAPTION=teaser_caption,
        TEASER_DESCRIPTION=teaser_description,
        MAIN_FIGURE_ASSET=main_figure_asset,
        MAIN_FIGURE_CAPTION=main_figure_caption,
        MAIN_FIGURE_DESCRIPTION=main_figure_description,
        ASPECT_RATIO=aspect_ratio,
        CANDIDATE_COUNT=str(candidate_count),
        RETRIEVAL_SETTING=retrieval_setting,
        PIPELINE_MODE=pipeline_mode,
        MAIN_MODEL_NAME=main_model_name,
        IMAGE_MODEL_NAME=image_model_name,
        HUMAN_APPROVAL=human_approval,
        HUMAN_REVIEW_NOTES=human_review_notes,
        VISUAL_QA_NOTES=visual_qa_notes,
        ADDITIONAL_NOTES=additional_notes,
    )


def render_project_readme(project_title: str, project_slug: str, idea: str) -> str:
    return render_template(
        "project/README.md.tmpl",
        PROJECT_TITLE=project_title,
        PROJECT_SLUG=project_slug,
        IDEA=idea,
    )


def render_project_readme_zh(project_title: str, project_slug: str, idea: str) -> str:
    return render_template(
        "project/README.zh-CN.md.tmpl",
        PROJECT_TITLE=project_title,
        PROJECT_SLUG=project_slug,
        IDEA=idea,
    )


def render_project_progress() -> str:
    return render_template("project/PROGRESS.md.tmpl")


def render_output_readme() -> str:
    return render_template("project/output/README.md.tmpl")


def render_literature_log() -> str:
    return render_template("project/literature/search-log.md.tmpl")


def render_references_bib() -> str:
    return render_template("project/literature/references.bib.tmpl")


def render_project_tex() -> str:
    return render_template("project/paper/main.tex.tmpl")


def project_files(idea: str, venue: str, project_title: str, project_slug: str) -> Dict[str, str]:
    return {
        "README.md": render_project_readme(project_title, project_slug, idea),
        "README.zh-CN.md": render_project_readme_zh(project_title, project_slug, idea),
        "IDEA.md": render_template("project/IDEA.md.tmpl", IDEA=idea),
        "PROGRESS.md": render_project_progress(),
        "artifacts/research-brief.md": render_research_brief(idea, venue),
        "artifacts/novelty-matrix.md": render_novelty_matrix(idea),
        "artifacts/study-spec.md": render_study_spec(idea),
        "deploy/deployment-plan.md": render_deployment_plan(idea),
        "analysis/analysis-plan.md": render_analysis_plan(idea),
        "paper/paper-brief.md": render_paper_brief(idea, venue),
        "paper/figure-plan.md": render_paper_figure_plan(),
        "paper/adversarial-review.md": render_adversarial_review(),
        "paper/paper-review.md": render_paper_review(),
        "literature/search-log.md": render_literature_log(),
        "literature/references.bib": render_references_bib(),
        "paper/main.tex": render_project_tex(),
        "paper/references.bib": render_references_bib(),
        "studies/survey.md": render_template("project/studies/survey.md.tmpl"),
        "studies/protocol.md": render_template("project/studies/protocol.md.tmpl"),
        "prototype/README.md": render_template("project/prototype/README.md.tmpl"),
        "output/README.md": render_output_readme(),
        "output/analysis/.gitkeep": "",
        "output/collection/.gitkeep": "",
        "output/exports/.gitkeep": "",
        "output/exports/figures/.gitkeep": "",
        "output/playwright/.gitkeep": "",
    }


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def scaffold_project_files(project_dir: Path, state: Dict, *, legacy_backfill: bool = False) -> None:
    project_meta = state.get("project", {})
    idea = str(project_meta.get("idea", "")).strip()
    venue = str(project_meta.get("venue", "CHI")).strip() or "CHI"
    project_title = str(project_meta.get("name", "")).strip() or title_from_idea(idea)
    project_slug = str(project_meta.get("slug", "")).strip() or slugify(project_title or idea)

    for rel_path, content in project_files(idea, venue, project_title, project_slug).items():
        target_path = project_dir / rel_path
        if target_path.exists():
            continue
        if legacy_backfill and rel_path == str(PAPER_FIGURE_PLAN):
            content = render_paper_figure_plan(
                decision="skip",
                content_source="method",
                content_file="",
                figure_caption="",
                figure_output="",
                aspect_ratio="16:9",
                candidate_count=1,
                retrieval_setting="auto",
                pipeline_mode="demo_full",
                main_model_name="",
                image_model_name="",
                additional_notes=(
                    "Backfilled by AutoCHIResearch for a legacy project. Change `Figure Decision` to "
                    "`generate` if this paper needs a PaperBanana figure."
                ),
            ).replace("<!-- STATUS: pending -->\n\n", "")
        write_file(target_path, content)


def artifact_complete(path: Path) -> bool:
    if not path.exists():
        return False
    text = path.read_text(encoding="utf-8").strip()
    if not text:
        return False
    return "TODO" not in text and "<!-- STATUS: pending -->" not in text


def markdown_section_map(path: Path) -> Dict[str, str]:
    text = path.read_text(encoding="utf-8")
    sections: Dict[str, str] = {}
    current_label: str | None = None
    current_lines: List[str] = []

    for line in text.splitlines():
        heading_match = re.match(r"^##\s+(.*\S)\s*$", line)
        if heading_match:
            if current_label is not None:
                sections[current_label] = "\n".join(current_lines).strip()
            current_label = heading_match.group(1).strip()
            current_lines = []
            continue
        if current_label is not None:
            current_lines.append(line)

    if current_label is not None:
        sections[current_label] = "\n".join(current_lines).strip()
    return sections


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


def extract_tex_section(path: Path, section_name: str) -> str:
    text = path.read_text(encoding="utf-8")
    pattern = re.compile(
        rf"\\section\{{{re.escape(section_name)}\}}(.*?)(?=\\section\{{|\Z)",
        re.DOTALL,
    )
    match = pattern.search(text)
    if not match:
        return ""
    section_text = match.group(1)
    section_text = re.sub(r"(?<!\\)%.*", " ", section_text)
    section_text = re.sub(r"\\cite\{[^}]*\}", " ", section_text)
    section_text = re.sub(r"\\ref\{[^}]*\}", " ", section_text)
    section_text = re.sub(r"\\label\{[^}]*\}", " ", section_text)
    section_text = re.sub(r"\\[A-Za-z]+\*?(?:\[[^\]]*\])?(?:\{[^}]*\})?", " ", section_text)
    section_text = re.sub(r"[{}\\]", " ", section_text)
    section_text = re.sub(r"\s+", " ", section_text)
    return section_text.strip()


def detect_paperbanana_root() -> Path | None:
    candidates: List[Path] = []
    env_root = os.environ.get("PAPERBANANA_ROOT")
    if env_root:
        candidates.append(Path(env_root).expanduser())
    candidates.extend(
        [
            ROOT.parent / "paperbanana",
            Path.home() / ".openclaw" / "workspace" / "skills" / "paperbanana",
            Path.home() / ".codex" / "skills" / "paperbanana",
        ]
    )
    for candidate in candidates:
        if (candidate / "pyproject.toml").exists() and (candidate / "paperbanana" / "cli.py").exists():
            return candidate
        if (candidate / "run.py").exists() and (candidate / "SKILL.md").exists():
            return candidate
    return None


def paperbanana_runtime_mode(root: Path | None) -> str | None:
    if root is None:
        return None
    if (root / "pyproject.toml").exists() and (root / "paperbanana" / "cli.py").exists():
        return "repo"
    if all((root / path).exists() for path in ["run.py", "agents", "configs", "utils"]):
        return "legacy_wrapper"
    if (root / "run.py").exists():
        return "wrapper_only"
    return None


def paperbanana_is_complete_checkout(root: Path | None) -> bool:
    return paperbanana_runtime_mode(root) in {"repo", "legacy_wrapper"}


def paperbanana_provider_overrides() -> Dict[str, str]:
    if os.environ.get("OPENROUTER_API_KEY"):
        return {
            "provider_source": "openrouter",
            "vlm_provider": "openrouter",
            "image_provider": "openrouter_imagen",
        }
    if os.environ.get("ARK_API_KEY"):
        return {
            "provider_source": "ark",
            "vlm_provider": "openai",
            "image_provider": "openai_imagen",
        }
    if os.environ.get("OPENAI_API_KEY"):
        return {
            "provider_source": "openai",
            "vlm_provider": "openai",
            "image_provider": "openai_imagen",
        }
    if os.environ.get("GOOGLE_API_KEY"):
        return {
            "provider_source": "google",
            "vlm_provider": "gemini",
            "image_provider": "google_imagen",
        }
    return {}


def paperbanana_subprocess_env(figure_plan: Dict[str, object], provider_overrides: Dict[str, str]) -> Dict[str, str]:
    env = os.environ.copy()
    if provider_overrides.get("provider_source") != "ark":
        return env

    env["OPENAI_API_KEY"] = os.environ.get("ARK_API_KEY", "")
    env["OPENAI_BASE_URL"] = os.environ.get("ARK_BASE_URL", ARK_DEFAULT_BASE_URL)
    env["OPENAI_VLM_MODEL"] = (
        str(figure_plan["main_model_name"]).strip()
        or os.environ.get("ARK_VLM_MODEL")
        or ARK_DEFAULT_VLM_MODEL
    )
    env["OPENAI_IMAGE_MODEL"] = (
        str(figure_plan["image_model_name"]).strip()
        or os.environ.get("ARK_IMAGE_MODEL")
        or ARK_DEFAULT_IMAGE_MODEL
    )
    env["ARK_IMAGE_SIZE"] = os.environ.get("ARK_IMAGE_SIZE", "2K")
    env["ARK_WATERMARK"] = os.environ.get("ARK_WATERMARK", "false")
    return env


def paperbanana_runtime_status() -> Dict[str, object]:
    root = detect_paperbanana_root()
    return {
        "installed": root is not None,
        "root": root,
        "mode": paperbanana_runtime_mode(root),
        "complete_checkout": paperbanana_is_complete_checkout(root),
        "uv_available": shutil.which("uv") is not None,
        "api_key_available": bool(
            os.environ.get("OPENROUTER_API_KEY")
            or os.environ.get("ARK_API_KEY")
            or os.environ.get("GOOGLE_API_KEY")
            or os.environ.get("OPENAI_API_KEY")
        ),
    }


def parse_paper_figure_plan(plan_path: Path) -> Dict[str, object]:
    status: Dict[str, object] = {
        "exists": plan_path.exists(),
        "complete": False,
        "decision": None,
        "content_source": "",
        "content_file": "",
        "figure_goal": "",
        "visual_style": "",
        "must_include": "",
        "must_avoid": "",
        "figure_caption": "",
        "output_path": "",
        "teaser_asset": "",
        "teaser_caption": "",
        "teaser_description": "",
        "main_figure_asset": "",
        "main_figure_caption": "",
        "main_figure_description": "",
        "aspect_ratio": "16:9",
        "candidate_count": 1,
        "retrieval_setting": "auto",
        "pipeline_mode": "demo_full",
        "main_model_name": "",
        "image_model_name": "",
        "human_approval": "",
        "human_review_notes": "",
        "visual_qa_notes": "",
        "notes": "",
    }
    if not plan_path.exists():
        return status

    sections = markdown_section_map(plan_path)
    raw_count = sections.get("Candidate Count", "1").strip()
    try:
        candidate_count = max(1, int(raw_count))
    except ValueError:
        candidate_count = 1

    status.update(
        {
            "complete": artifact_complete(plan_path),
            "decision": sections.get("Figure Decision", "").strip().lower() or None,
            "content_source": sections.get("Content Source", "").strip().lower(),
            "content_file": sections.get("Content File", "").strip(),
            "figure_goal": sections.get("Figure Goal", "").strip(),
            "visual_style": sections.get("Visual Style", "").strip(),
            "must_include": sections.get("Must Include", "").strip(),
            "must_avoid": sections.get("Must Avoid", "").strip(),
            "figure_caption": sections.get("Figure Caption", "").strip(),
            "output_path": sections.get("Figure Output", "").strip(),
            "teaser_asset": sections.get("Teaser Asset", "").strip(),
            "teaser_caption": sections.get("Teaser Caption", "").strip(),
            "teaser_description": sections.get("Teaser Description", "").strip(),
            "main_figure_asset": sections.get("Main Figure Asset", "").strip(),
            "main_figure_caption": sections.get("Main Figure Caption", "").strip(),
            "main_figure_description": sections.get("Main Figure Description", "").strip(),
            "aspect_ratio": sections.get("Aspect Ratio", "16:9").strip() or "16:9",
            "candidate_count": candidate_count,
            "retrieval_setting": sections.get("Retrieval Setting", "auto").strip() or "auto",
            "pipeline_mode": sections.get("Pipeline Mode", "demo_full").strip() or "demo_full",
            "main_model_name": sections.get("Main Model Name", "").strip(),
            "image_model_name": sections.get("Image Model Name", "").strip(),
            "human_approval": sections.get("Human Approval", "").strip().lower(),
            "human_review_notes": sections.get("Human Review Notes", "").strip(),
            "visual_qa_notes": sections.get("Visual QA Notes", "").strip(),
            "notes": sections.get("Additional Notes", "").strip(),
        }
    )
    return status


def build_structured_figure_brief(
    project_dir: Path,
    figure_plan: Dict[str, object],
    *,
    source_label: str,
    source_text: str,
) -> str:
    goal = str(figure_plan["figure_goal"]).strip() or DEFAULT_FIGURE_GOAL
    visual_style = str(figure_plan["visual_style"]).strip() or DEFAULT_FIGURE_VISUAL_STYLE
    must_include = str(figure_plan["must_include"]).strip() or DEFAULT_FIGURE_MUST_INCLUDE
    must_avoid = str(figure_plan["must_avoid"]).strip() or DEFAULT_FIGURE_MUST_AVOID
    human_approval = str(figure_plan["human_approval"]).strip() or "pending"
    human_review_notes = str(figure_plan["human_review_notes"]).strip() or "No human review notes provided."
    additional_notes = str(figure_plan["notes"]).strip() or "No additional notes."

    return "\n\n".join(
        [
            "# Paper Figure Brief",
            f"Project: {project_dir.name}",
            f"Figure output: {figure_plan['output_path']}",
            f"Aspect ratio: {figure_plan['aspect_ratio']}",
            "## Goal\n" + goal,
            "## Visual Style\n" + visual_style,
            "## Must Include\n" + must_include,
            "## Must Avoid\n" + must_avoid,
            "## Caption\n" + str(figure_plan["figure_caption"]).strip(),
            "## Teaser Requirements\n"
            + f"Asset placeholder: {figure_plan['teaser_asset']}\n"
            + f"Caption: {figure_plan['teaser_caption']}\n"
            + f"Description: {figure_plan['teaser_description']}",
            "## Main Figure Requirements\n"
            + f"Asset placeholder: {figure_plan['main_figure_asset']}\n"
            + f"Caption: {figure_plan['main_figure_caption']}\n"
            + f"Description: {figure_plan['main_figure_description']}",
            "## Human Review\n"
            + f"Approval: {human_approval}\n"
            + f"Notes: {human_review_notes}",
            "## Additional Notes\n" + additional_notes,
            f"## Source Material ({source_label})\n" + source_text.strip(),
        ]
    )


def detect_paper_compiler() -> Dict[str, object]:
    latexmk = shutil.which("latexmk")
    tectonic = shutil.which("tectonic")
    pdflatex = shutil.which("pdflatex")
    bibtex = shutil.which("bibtex")

    if latexmk:
        return {"available": True, "name": "latexmk", "command": latexmk}
    if tectonic:
        return {"available": True, "name": "tectonic", "command": tectonic}
    if pdflatex and bibtex:
        return {
            "available": True,
            "name": "pdflatex+bibtex",
            "command": pdflatex,
            "bibtex": bibtex,
        }

    missing: List[str] = []
    if not latexmk:
        missing.append("latexmk")
    if not tectonic:
        missing.append("tectonic")
    if not pdflatex:
        missing.append("pdflatex")
    if not bibtex:
        missing.append("bibtex")
    return {"available": False, "name": None, "missing": missing}


def render_pdf_preview_pages(pdf_path: Path, output_dir: Path, max_pages: int = 12) -> Dict[str, object]:
    output_dir.mkdir(parents=True, exist_ok=True)
    for old_page in output_dir.glob("page-*.png"):
        old_page.unlink()

    try:
        import fitz  # type: ignore

        document = fitz.open(pdf_path)
        rendered = min(len(document), max_pages)
        for index in range(rendered):
            pix = document[index].get_pixmap(matrix=fitz.Matrix(2, 2), alpha=False)
            pix.save(output_dir / f"page-{index + 1:02d}.png")
        return {"rendered": rendered > 0, "count": rendered, "mode": "pymupdf"}
    except Exception:
        pass

    pdftoppm = shutil.which("pdftoppm")
    if not pdftoppm:
        return {"rendered": False, "count": 0, "mode": None}

    prefix = output_dir / "page"
    result = subprocess.run(
        [
            pdftoppm,
            "-f",
            "1",
            "-l",
            str(max_pages),
            "-png",
            str(pdf_path),
            str(prefix),
        ],
        text=True,
        capture_output=True,
    )
    count = len(list(output_dir.glob("page-*.png")))
    return {
        "rendered": result.returncode == 0 and count > 0,
        "count": count,
        "mode": "pdftoppm",
        "stderr": result.stderr.strip(),
    }


def write_paper_build_status(
    project_dir: Path,
    status: str,
    compiler_name: str,
    reason: str,
) -> Path:
    status_path = project_dir / PAPER_BUILD_STATUS
    pdf_path = project_dir / PAPER_OUTPUT_PDF
    log_path = project_dir / PAPER_BUILD_LOG
    content = "\n".join(
        [
            "# Paper Build Status",
            "",
            f"Build Status: {status}",
            f"Compiler: {compiler_name}",
            f"Generated At: {now_iso()}",
            "Source: `paper/main.tex`",
            f"PDF Output: `{PAPER_OUTPUT_PDF.as_posix()}`",
            f"Log Path: `{PAPER_BUILD_LOG.as_posix()}`",
            "",
            "## Notes",
            f"- {reason}",
            f"- PDF exists: {'yes' if pdf_path.exists() else 'no'}",
            f"- Build log exists: {'yes' if log_path.exists() else 'no'}",
            "",
        ]
    )
    write_file(status_path, content)
    return status_path


def paper_build_status(project_dir: Path) -> Dict[str, object]:
    status_path = project_dir / PAPER_BUILD_STATUS
    log_path = project_dir / PAPER_BUILD_LOG
    pdf_path = project_dir / PAPER_OUTPUT_PDF
    rendered_pages_dir = project_dir / PAPER_RENDERED_PAGES_DIR
    compiler = detect_paper_compiler()
    status: Dict[str, object] = {
        "exists": status_path.exists(),
        "status": None,
        "compiler": None,
        "pdf_exists": pdf_path.exists(),
        "log_exists": log_path.exists(),
        "success": False,
        "compiler_available": bool(compiler["available"]),
        "available_compiler": compiler["name"],
    }
    if not status_path.exists():
        return status

    text = status_path.read_text(encoding="utf-8")
    match = re.search(r"(?mi)^Build Status:\s*(success|failed|blocked)\s*$", text)
    if match:
        status["status"] = match.group(1).lower()
    compiler_match = re.search(r"(?mi)^Compiler:\s*(.+?)\s*$", text)
    if compiler_match:
        status["compiler"] = compiler_match.group(1).strip()
    status["success"] = status["status"] == "success" and pdf_path.exists()
    return status


def paper_review_status(review_path: Path) -> Dict[str, object]:
    status: Dict[str, object] = {
        "exists": review_path.exists(),
        "complete": False,
        "verdict": None,
        "ready_flag": False,
        "adversarial_scope": False,
        "dimension_statuses": {},
        "all_dimensions_pass": False,
    }
    if not review_path.exists():
        return status

    review_text = review_path.read_text(encoding="utf-8")
    status["complete"] = artifact_complete(review_path)
    status["adversarial_scope"] = "paper/adversarial-review.md" in review_text

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


def adversarial_review_status(review_path: Path) -> Dict[str, object]:
    status: Dict[str, object] = {
        "exists": review_path.exists(),
        "complete": False,
        "review_complete": False,
        "revision_complete": False,
        "reviewer_statuses": {},
        "all_reviewers_addressed": False,
    }
    if not review_path.exists():
        return status

    review_text = review_path.read_text(encoding="utf-8")
    status["complete"] = artifact_complete(review_path)

    review_complete_match = re.search(
        r"(?mi)^Adversarial Review Complete:\s*(yes|no)\s*$", review_text
    )
    status["review_complete"] = bool(
        review_complete_match and review_complete_match.group(1).lower() == "yes"
    )

    revision_complete_match = re.search(
        r"(?mi)^Author Revision Complete:\s*(yes|no)\s*$", review_text
    )
    status["revision_complete"] = bool(
        revision_complete_match and revision_complete_match.group(1).lower() == "yes"
    )

    reviewer_statuses: Dict[str, str | None] = {}
    for label in PAPER_ADVERSARIAL_REVIEWER_LABELS:
        match = re.search(rf"(?mi)^{re.escape(label)}:\s*(addressed|waived|pending)\s*$", review_text)
        reviewer_statuses[label] = match.group(1).lower() if match else None
    status["reviewer_statuses"] = reviewer_statuses
    status["all_reviewers_addressed"] = all(
        value in {"addressed", "waived"} for value in reviewer_statuses.values()
    )
    return status


def paper_stage_diagnostics(project_dir: Path, brief_path: Path) -> Dict[str, object]:
    manuscript_path = project_dir / "paper" / "main.tex"
    references_path = project_dir / "paper" / "references.bib"
    figure_plan_path = project_dir / PAPER_FIGURE_PLAN
    adversarial_review_path = project_dir / PAPER_ADVERSARIAL_REVIEW
    review_path = project_dir / "paper" / "paper-review.md"
    results_summary_path = project_dir / "output" / "analysis" / "results_summary.md"
    figure_plan = parse_paper_figure_plan(figure_plan_path)
    figure_output_path = None
    if figure_plan["output_path"]:
        figure_output_path = project_dir / str(figure_plan["output_path"])

    diagnostics: Dict[str, object] = {
        "brief_complete": artifact_complete(brief_path),
        "manuscript_path": manuscript_path,
        "manuscript_complete": manuscript_path.exists() and artifact_complete(manuscript_path),
        "missing_sections": [],
        "word_count": 0,
        "teaser_present": False,
        "figure_count": 0,
        "description_count": 0,
        "references_complete": references_path.exists() and artifact_complete(references_path),
        "reference_count": 0,
        "results_summary_complete": results_summary_path.exists() and artifact_complete(results_summary_path),
        "rendered_page_count": 0,
        "figure_plan": figure_plan,
        "figure_output_path": figure_output_path,
        "figure_output_exists": bool(figure_output_path and figure_output_path.exists()),
        "paperbanana": paperbanana_runtime_status(),
        "adversarial_review": adversarial_review_status(adversarial_review_path),
        "review": paper_review_status(review_path),
        "build": paper_build_status(project_dir),
    }

    if manuscript_path.exists():
        manuscript_text = manuscript_path.read_text(encoding="utf-8")
        diagnostics["missing_sections"] = [
            label
            for label, pattern in REQUIRED_PAPER_SECTION_SPECS
            if re.search(pattern, manuscript_text) is None
        ]
        diagnostics["word_count"] = tex_visible_word_count(manuscript_path)
        diagnostics["teaser_present"] = re.search(r"\\begin\{teaserfigure\}", manuscript_text) is not None
        diagnostics["figure_count"] = len(re.findall(r"\\includegraphics(?:\[[^\]]*\])?\{[^}]+\}", manuscript_text))
        diagnostics["description_count"] = len(re.findall(r"\\Description\{", manuscript_text))

    if references_path.exists():
        diagnostics["reference_count"] = len(
            re.findall(r"(?m)^@", references_path.read_text(encoding="utf-8"))
        )

    if (project_dir / PAPER_RENDERED_PAGES_DIR).exists():
        diagnostics["rendered_page_count"] = len(
            list((project_dir / PAPER_RENDERED_PAGES_DIR).glob("page-*.png"))
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
    if word_count < MIN_PAPER_WORD_COUNT:
        return (
            f"Expand paper/main.tex before review. The manuscript currently has about {word_count} visible words; "
            f"paper completion requires a stand-alone draft of at least {MIN_PAPER_WORD_COUNT} words."
        )

    if not diagnostics["teaser_present"]:
        return (
            "Add a teaser figure near the front matter of paper/main.tex. The paper stage now expects a "
            "`teaserfigure` with a real asset, caption, and description."
        )

    if int(diagnostics["figure_count"]) > int(diagnostics["description_count"]):
        return (
            "Add a `\\Description{...}` block for every figure in paper/main.tex before paper review. "
            f"Current figures: {diagnostics['figure_count']}, descriptions: {diagnostics['description_count']}."
        )

    if not diagnostics["references_complete"] or int(diagnostics["reference_count"]) < MIN_PAPER_REFERENCE_COUNT:
        return (
            "Complete paper/references.bib with validated citations before paper completion. "
            f"Current BibTeX entry count: {diagnostics['reference_count']}; the paper stage now expects at least "
            f"{MIN_PAPER_REFERENCE_COUNT} validated citations and a real reading pass behind them."
        )

    if not diagnostics["results_summary_complete"]:
        return "Complete output/analysis/results_summary.md before paper completion."

    figure_plan = diagnostics["figure_plan"]
    if not figure_plan["complete"]:
        return (
            "Complete paper/figure-plan.md. Decide whether to generate a PaperBanana figure, set the "
            "caption, and choose an output path under output/exports/figures/."
        )

    if not (
        figure_plan["teaser_asset"]
        and figure_plan["teaser_caption"]
        and figure_plan["teaser_description"]
    ):
        return (
            "Complete `Teaser Asset`, `Teaser Caption`, and `Teaser Description` in paper/figure-plan.md "
            "before paper review."
        )

    if not (
        figure_plan["main_figure_asset"]
        and figure_plan["main_figure_caption"]
        and figure_plan["main_figure_description"]
    ):
        return (
            "Complete `Main Figure Asset`, `Main Figure Caption`, and `Main Figure Description` in "
            "paper/figure-plan.md before paper review."
        )

    if figure_plan["decision"] not in {"generate", "skip", "gpt-image-2"}:
        return (
            "Set `Figure Decision` in paper/figure-plan.md to `gpt-image-2`, `generate` (legacy), or `skip` "
            "before paper review."
        )

    if figure_plan["decision"] == "gpt-image-2":
        if figure_plan["human_approval"] not in {"approved", "waived"}:
            return (
                "Review paper/figure-plan.md with the human and set `Human Approval` to `approved` or `waived` "
                "before using GPT Image 2 paper assets."
            )
        if not figure_plan["figure_caption"] or not figure_plan["output_path"]:
            return "Complete `Figure Caption` and `Figure Output` for the GPT Image 2 figure."
        if not diagnostics["figure_output_exists"]:
            return (
                "Generate or copy the GPT Image 2 paper figure into the `Figure Output` path under "
                "output/exports/figures before paper review."
            )

    if figure_plan["decision"] == "generate":
        if figure_plan["human_approval"] not in {"approved", "waived"}:
            return (
                "Review paper/figure-plan.md with the human, confirm which prototype, screenshot, or method view "
                "the figure should show, and set `Human Approval` to `approved` or `waived` before running "
                "PaperBanana."
            )
        if figure_plan["content_source"] not in {"method", "content-file"}:
            return (
                "Set `Content Source` in paper/figure-plan.md to `method` or `content-file` before running "
                "PaperBanana."
            )
        if not figure_plan["figure_caption"] or not figure_plan["output_path"]:
            return (
                "Complete `Figure Caption` and `Figure Output` in paper/figure-plan.md before running "
                "PaperBanana."
            )
        if figure_plan["content_source"] == "content-file" and not figure_plan["content_file"]:
            return "Set `Content File` in paper/figure-plan.md because the figure plan uses `content-file`."
        paperbanana = diagnostics["paperbanana"]
        if not paperbanana["installed"]:
            return (
                "Paper figure generation is requested, but PaperBanana is not installed. Install it or switch "
                "`Figure Decision` to `skip` with rationale in paper/figure-plan.md."
            )
        if not paperbanana["complete_checkout"]:
            return (
                "PaperBanana is detected, but the local install is only the skill wrapper. Point "
                "`PAPERBANANA_ROOT` at a full PaperBanana checkout, or clone it next to this repo as "
                "`../paperbanana`, before running figure generation."
            )
        if not paperbanana["uv_available"]:
            return (
                "Paper figure generation is requested, but `uv` is missing. Install `uv` so AutoCHIResearch can "
                "run PaperBanana under Python 3.11."
            )
        if not paperbanana["api_key_available"]:
            return (
                "PaperBanana is installed, but no image-generation API key is configured. Set `OPENROUTER_API_KEY`, "
                "`ARK_API_KEY`, `OPENAI_API_KEY`, or `GOOGLE_API_KEY`, then run "
                "`python3 scripts/autochi.py generate-paper-figure <project>`."
            )
        if not diagnostics["figure_output_exists"]:
            return (
                "Generate the paper figure with `python3 scripts/autochi.py generate-paper-figure <project>` "
                "before paper review."
            )

    adversarial_review = diagnostics["adversarial_review"]
    if not adversarial_review["exists"] or not adversarial_review["complete"] or not adversarial_review["review_complete"]:
        return (
            "Run the adversarial reviewer subagent pass and write paper/adversarial-review.md. "
            "Use at least four reviewer roles: methods/validity, systems/interaction contribution, "
            "related work/novelty, and writing/claim-evidence/CHI fit."
        )

    if not adversarial_review["revision_complete"] or not adversarial_review["all_reviewers_addressed"]:
        pending_reviewers = [
            label
            for label, value in adversarial_review["reviewer_statuses"].items()
            if value not in {"addressed", "waived"}
        ]
        if pending_reviewers:
            return (
                "Revise the manuscript against paper/adversarial-review.md and mark each reviewer response "
                "as addressed or waived. Pending reviewer responses: "
                + ", ".join(pending_reviewers)
                + "."
            )
        return (
            "Revise the manuscript against paper/adversarial-review.md and set "
            "`Author Revision Complete: yes` before the final paper-judge review."
        )

    review = diagnostics["review"]
    if not review["exists"] or not review["complete"]:
        return (
            "After the adversarial subagent revisions, spawn a final paper-judge sub-agent and write "
            "paper/paper-review.md. Paper completion requires a READY verdict from that review."
        )

    if not review["adversarial_scope"]:
        return (
            "Rerun the final paper-judge sub-agent after adversarial revisions. The current "
            "paper/paper-review.md does not list paper/adversarial-review.md as review input."
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

    build = diagnostics["build"]
    if build["success"]:
        page_count = int(diagnostics["rendered_page_count"])
        if page_count < MIN_PAPER_PAGE_COUNT:
            return (
                f"Expand paper/main.tex and rerun `python3 scripts/autochi.py build-paper <project>`. "
                f"The compiled manuscript currently renders to {page_count} pages; paper completion requires "
                f"at least {MIN_PAPER_PAGE_COUNT} rendered pages."
            )
        visual_qa_notes = str(figure_plan["visual_qa_notes"]).strip().lower()
        if not visual_qa_notes or visual_qa_notes.startswith("pending build"):
            return (
                "Inspect output/exports/rendered-pages after the PDF build and replace the placeholder "
                "`Visual QA Notes` in paper/figure-plan.md with concrete layout findings or `No issues found.`"
            )
        return "Paper review is READY and a compiled PDF exists. The manuscript can be treated as complete."
    if not build["compiler_available"]:
        return (
            "Paper review is READY, but no local TeX compiler is available. Install `tectonic` or "
            "`latexmk` (or `pdflatex` + `bibtex`), then run `python3 scripts/autochi.py build-paper <project>`."
        )
    if build["status"] == "failed":
        return (
            "Paper review is READY, but PDF compilation failed. Check output/exports/paper-build.log, fix the "
            "LaTeX errors, and rerun `python3 scripts/autochi.py build-paper <project>`."
        )
    return (
        "Paper review is READY. Compile the manuscript with "
        "`python3 scripts/autochi.py build-paper <project>` to produce output/exports/paper.pdf."
    )


def paper_stage_complete(project_dir: Path, brief_path: Path) -> bool:
    diagnostics = paper_stage_diagnostics(project_dir, brief_path)
    adversarial_review = diagnostics["adversarial_review"]
    review = diagnostics["review"]
    build = diagnostics["build"]
    figure_plan = diagnostics["figure_plan"]
    figure_step_complete = bool(
        figure_plan["complete"]
        and figure_plan["decision"] in {"generate", "skip", "gpt-image-2"}
        and (figure_plan["decision"] == "skip" or diagnostics["figure_output_exists"])
        and (
            figure_plan["decision"] == "skip"
            or str(figure_plan["human_approval"]).strip().lower() in {"approved", "waived"}
        )
        and bool(figure_plan["teaser_asset"])
        and bool(figure_plan["teaser_caption"])
        and bool(figure_plan["teaser_description"])
        and bool(figure_plan["main_figure_asset"])
        and bool(figure_plan["main_figure_caption"])
        and bool(figure_plan["main_figure_description"])
        and bool(figure_plan["human_review_notes"])
        and bool(figure_plan["visual_qa_notes"])
        and not str(figure_plan["visual_qa_notes"]).strip().lower().startswith("pending build")
    )
    return (
        bool(diagnostics["brief_complete"])
        and bool(diagnostics["manuscript_complete"])
        and not diagnostics["missing_sections"]
        and int(diagnostics["word_count"]) >= MIN_PAPER_WORD_COUNT
        and bool(diagnostics["teaser_present"])
        and int(diagnostics["figure_count"]) <= int(diagnostics["description_count"])
        and bool(diagnostics["references_complete"])
        and int(diagnostics["reference_count"]) >= MIN_PAPER_REFERENCE_COUNT
        and bool(diagnostics["results_summary_complete"])
        and figure_step_complete
        and bool(adversarial_review["exists"])
        and bool(adversarial_review["complete"])
        and bool(adversarial_review["review_complete"])
        and bool(adversarial_review["revision_complete"])
        and bool(adversarial_review["all_reviewers_addressed"])
        and bool(review["exists"])
        and bool(review["complete"])
        and bool(review["adversarial_scope"])
        and review["verdict"] == "ready"
        and bool(review["ready_flag"])
        and bool(review["all_dimensions_pass"])
        and bool(build["success"])
        and int(diagnostics["rendered_page_count"]) >= MIN_PAPER_PAGE_COUNT
    )


def build_paper_cmd(args: argparse.Namespace) -> int:
    project_dir = resolve_project(args.project)
    manuscript_path = project_dir / "paper" / "main.tex"
    references_path = project_dir / "paper" / "references.bib"
    exports_dir = project_dir / PAPER_EXPORTS_DIR
    build_dir = project_dir / PAPER_BUILD_DIR
    log_path = project_dir / PAPER_BUILD_LOG
    pdf_path = project_dir / PAPER_OUTPUT_PDF
    rendered_pages_dir = project_dir / PAPER_RENDERED_PAGES_DIR

    if not manuscript_path.exists():
        raise SystemExit(f"Missing manuscript at {manuscript_path}")

    exports_dir.mkdir(parents=True, exist_ok=True)
    build_dir.mkdir(parents=True, exist_ok=True)

    compiler = detect_paper_compiler()
    if not compiler["available"]:
        write_file(log_path, "No supported LaTeX compiler found on PATH.\n")
        write_paper_build_status(
            project_dir,
            status="BLOCKED",
            compiler_name="none",
            reason="Missing local TeX compiler. Prefer `tectonic`; `latexmk` also works. `pdflatex` requires `bibtex`.",
        )
        print("No supported LaTeX compiler found.")
        print("Install `tectonic`, `latexmk`, or `pdflatex` + `bibtex`, then rerun build-paper.")
        return 1

    if compiler["name"] == "pdflatex+bibtex" and references_path.exists():
        shutil.copy2(references_path, build_dir / references_path.name)

    commands: List[List[str]] = []
    cwd = manuscript_path.parent
    if compiler["name"] == "latexmk":
        commands = [
            [
                str(compiler["command"]),
                "-pdf",
                "-interaction=nonstopmode",
                "-halt-on-error",
                "-file-line-error",
                f"-outdir={build_dir}",
                manuscript_path.name,
            ]
        ]
    elif compiler["name"] == "tectonic":
        commands = [
            [
                str(compiler["command"]),
                "--keep-logs",
                "--synctex",
                "--outdir",
                str(build_dir),
                manuscript_path.name,
            ]
        ]
    elif compiler["name"] == "pdflatex+bibtex":
        commands = [
            [
                str(compiler["command"]),
                "-interaction=nonstopmode",
                "-halt-on-error",
                f"-output-directory={build_dir}",
                manuscript_path.name,
            ],
            [str(compiler["bibtex"]), str(build_dir / manuscript_path.stem)],
            [
                str(compiler["command"]),
                "-interaction=nonstopmode",
                "-halt-on-error",
                f"-output-directory={build_dir}",
                manuscript_path.name,
            ],
            [
                str(compiler["command"]),
                "-interaction=nonstopmode",
                "-halt-on-error",
                f"-output-directory={build_dir}",
                manuscript_path.name,
            ],
        ]

    log_chunks: List[str] = []
    success = True
    for command in commands:
        result = subprocess.run(
            command,
            cwd=cwd,
            text=True,
            capture_output=True,
        )
        log_chunks.append("$ " + " ".join(command))
        if result.stdout:
            log_chunks.append(result.stdout)
        if result.stderr:
            log_chunks.append(result.stderr)
        if result.returncode != 0:
            success = False
            break

    write_file(log_path, "\n\n".join(log_chunks).strip() + "\n")

    built_pdf = build_dir / f"{manuscript_path.stem}.pdf"
    if success and built_pdf.exists():
        shutil.copy2(built_pdf, pdf_path)
        preview_status = render_pdf_preview_pages(pdf_path, rendered_pages_dir)
        write_paper_build_status(
            project_dir,
            status="SUCCESS",
            compiler_name=str(compiler["name"]),
            reason="Paper compiled successfully.",
        )
        print(f"Compiled PDF: {pdf_path}")
        print(f"Build log:     {log_path}")
        if preview_status["rendered"]:
            print(f"Rendered pages: {rendered_pages_dir}")
        return 0

    write_paper_build_status(
        project_dir,
        status="FAILED",
        compiler_name=str(compiler["name"]),
        reason="LaTeX compilation failed. Check output/exports/paper-build.log for errors.",
    )
    print("Paper build failed.")
    print(f"Build log: {log_path}")
    return 1


def generate_paper_figure_cmd(args: argparse.Namespace) -> int:
    project_dir = resolve_project(args.project)
    figure_plan_path = project_dir / PAPER_FIGURE_PLAN
    if not figure_plan_path.exists():
        raise SystemExit(f"Missing figure plan at {figure_plan_path}")

    figure_plan = parse_paper_figure_plan(figure_plan_path)
    if figure_plan["decision"] == "skip":
        print("Figure plan is set to skip. No PaperBanana run was started.")
        return 0
    if figure_plan["decision"] != "generate":
        raise SystemExit("Set `Figure Decision` in paper/figure-plan.md to `generate` before running this command.")

    runtime = paperbanana_runtime_status()
    if not runtime["installed"]:
        raise SystemExit(
            "PaperBanana is not installed. Install it first or set PAPERBANANA_ROOT to a local paperbanana checkout."
        )
    if not runtime["complete_checkout"]:
        raise SystemExit(
            "PaperBanana was found, but it is not a full checkout. Set PAPERBANANA_ROOT to a cloned PaperBanana repo, "
            "or place a full checkout at ../paperbanana."
        )
    if not runtime["uv_available"]:
        raise SystemExit("`uv` is required to run PaperBanana under Python 3.11.")
    if not args.dry_run and not runtime["api_key_available"]:
        raise SystemExit(
            "Set OPENROUTER_API_KEY, ARK_API_KEY, OPENAI_API_KEY, or GOOGLE_API_KEY before running PaperBanana."
        )

    output_rel = str(figure_plan["output_path"]).strip()
    if not output_rel:
        raise SystemExit("Missing `Figure Output` in paper/figure-plan.md")
    output_path = project_dir / output_rel
    output_path.parent.mkdir(parents=True, exist_ok=True)

    content_source = str(figure_plan["content_source"]).strip().lower()
    source_label: str
    source_text: str
    if content_source == "method":
        manuscript_path = project_dir / "paper" / "main.tex"
        if not manuscript_path.exists():
            raise SystemExit(f"Missing manuscript at {manuscript_path}")
        method_text = extract_tex_section(manuscript_path, "Method")
        if not method_text:
            raise SystemExit("Could not extract a `Method` section from paper/main.tex")
        source_label = "paper/main.tex::Method"
        source_text = method_text
    elif content_source == "content-file":
        raw_path = str(figure_plan["content_file"]).strip()
        if not raw_path:
            raise SystemExit("Missing `Content File` in paper/figure-plan.md")
        candidate = Path(raw_path)
        source_path = candidate if candidate.is_absolute() else project_dir / candidate
        if not source_path.exists():
            raise SystemExit(f"Missing content file for PaperBanana at {source_path}")
        source_label = str(source_path)
        source_text = source_path.read_text(encoding="utf-8")
    else:
        raise SystemExit("`Content Source` must be `method` or `content-file`")

    content_file_path = output_path.parent / f"{output_path.stem}_paperbanana_brief.txt"
    write_file(
        content_file_path,
        build_structured_figure_brief(
            project_dir,
            figure_plan,
            source_label=source_label,
            source_text=source_text,
        )
        + "\n",
    )

    runtime_mode = runtime["mode"]
    provider_overrides = paperbanana_provider_overrides()
    command: List[str]
    if runtime_mode == "repo":
        output_format = output_path.suffix.lower().lstrip(".") or "png"
        if output_format == "jpg":
            output_format = "jpeg"
        if output_format not in {"png", "jpeg", "webp"}:
            raise SystemExit(f"Unsupported figure output extension for PaperBanana repo mode: {output_path.suffix}")
        if int(figure_plan["candidate_count"]) != 1:
            raise SystemExit(
                "The current PaperBanana CLI generates one final figure per run. Set `Candidate Count` to `1` "
                "in paper/figure-plan.md."
            )
        command = [
            "uv",
            "run",
            "--python",
            "3.11",
        ]
        if provider_overrides.get("provider_source") in {"ark", "openai"}:
            command.extend(["--with", "openai"])
        command.extend([
            "paperbanana",
            "generate",
            "--input",
            str(content_file_path),
            "--caption",
            str(figure_plan["figure_caption"]),
            "--output",
            str(output_path),
            "--aspect-ratio",
            str(figure_plan["aspect_ratio"]),
            "--format",
            output_format,
        ])
        if provider_overrides.get("vlm_provider"):
            command.extend(["--vlm-provider", provider_overrides["vlm_provider"]])
        if provider_overrides.get("image_provider"):
            command.extend(["--image-provider", provider_overrides["image_provider"]])
        main_model_name = str(figure_plan["main_model_name"]).strip()
        image_model_name = str(figure_plan["image_model_name"]).strip()
        if provider_overrides.get("provider_source") == "ark":
            main_model_name = main_model_name or os.environ.get("ARK_VLM_MODEL", ARK_DEFAULT_VLM_MODEL)
            image_model_name = image_model_name or os.environ.get("ARK_IMAGE_MODEL", ARK_DEFAULT_IMAGE_MODEL)
        elif provider_overrides.get("provider_source") == "openrouter":
            main_model_name = main_model_name or os.environ.get("OPENROUTER_VLM_MODEL", OPENROUTER_DEFAULT_VLM_MODEL)
            image_model_name = image_model_name or os.environ.get(
                "OPENROUTER_IMAGE_MODEL", OPENROUTER_DEFAULT_IMAGE_MODEL
            )
        if main_model_name:
            command.extend(["--vlm-model", main_model_name])
        if image_model_name:
            command.extend(["--image-model", image_model_name])
        if args.dry_run:
            command.append("--dry-run")
    else:
        command = [
            "uv",
            "run",
            "--python",
            "3.11",
            "python",
            str(Path(runtime["root"]) / "run.py"),
            "--content-file",
            str(content_file_path),
            "--caption",
            str(figure_plan["figure_caption"]),
            "--task",
            "diagram",
            "--output",
            str(output_path),
            "--aspect-ratio",
            str(figure_plan["aspect_ratio"]),
            "--num-candidates",
            str(figure_plan["candidate_count"]),
            "--retrieval-setting",
            str(figure_plan["retrieval_setting"]),
            "--exp-mode",
            str(figure_plan["pipeline_mode"]),
        ]
        main_model_name = str(figure_plan["main_model_name"]).strip()
        image_model_name = str(figure_plan["image_model_name"]).strip()
        if provider_overrides.get("provider_source") == "openrouter":
            main_model_name = main_model_name or os.environ.get("OPENROUTER_VLM_MODEL", OPENROUTER_DEFAULT_VLM_MODEL)
            image_model_name = image_model_name or os.environ.get(
                "OPENROUTER_IMAGE_MODEL", OPENROUTER_DEFAULT_IMAGE_MODEL
            )
        elif provider_overrides.get("provider_source") == "ark":
            main_model_name = main_model_name or os.environ.get("ARK_VLM_MODEL", ARK_DEFAULT_VLM_MODEL)
            image_model_name = image_model_name or os.environ.get("ARK_IMAGE_MODEL", ARK_DEFAULT_IMAGE_MODEL)
        if main_model_name:
            command.extend(["--main-model-name", main_model_name])
        if image_model_name:
            command.extend(["--image-gen-model-name", image_model_name])

    print("Running PaperBanana...")
    print(" ".join(command))
    result = subprocess.run(
        command,
        cwd=str(runtime["root"]),
        text=True,
        capture_output=True,
        env=paperbanana_subprocess_env(figure_plan, provider_overrides),
    )
    if result.stdout:
        print(result.stdout.strip())
    if result.returncode != 0:
        if result.stderr:
            print(result.stderr.strip(), file=sys.stderr)
        raise SystemExit(result.returncode)

    if args.dry_run:
        print("Dry run completed. No figure image was generated.")
        return 0

    if runtime_mode == "repo":
        plain_stdout = re.sub(r"\x1b\[[0-9;]*[A-Za-z]", "", result.stdout or "")
        reported_output = None
        for pattern in [
            r"(?m)^\s*Output:\s*(.+?)\s*$",
            r"(?ms)^\s*Output:\s*\n\s*(.+?)\s*$",
            r"(?m)^.*Output saved to:\s*(.+?)\s*$",
        ]:
            match = re.search(pattern, plain_stdout)
            if match:
                reported_output = Path(match.group(1).strip())
                break
        if reported_output is None:
            run_outputs = sorted(output_path.parent.glob("run_*/final_output.png"))
            if run_outputs:
                reported_output = run_outputs[-1]
        if reported_output and reported_output.exists() and reported_output != output_path:
            shutil.copy2(reported_output, output_path)

    if int(figure_plan["candidate_count"]) == 1:
        if not output_path.exists():
            raise SystemExit(f"PaperBanana reported success, but output is missing at {output_path}")
        print(f"Generated figure: {output_path}")
        return 0

    generated_candidates = sorted(output_path.parent.glob(f"{output_path.stem}_*{output_path.suffix}"))
    if not generated_candidates:
        raise SystemExit(
            "PaperBanana completed, but no candidate images were found. Check the output directory and plan settings."
        )
    print("Generated candidates:")
    for candidate in generated_candidates:
        print(candidate)
    return 0


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
    scaffold_project_files(project_dir, state, legacy_backfill=True)
    current = None
    for stage in state["workflow"]:
        complete = stage_complete(project_dir, stage)
        stage["status"] = "complete" if complete else "pending"
        if current is None and not complete:
            current = stage

    # Preserve data_mode from existing state
    if "data_mode" not in state:
        state["data_mode"] = None

    refresh_phase_statuses(state)
    gate_decision = novelty_gate_decision(project_dir)

    # Check whether the data-mode gate should fire: build stage is done but data_mode not yet chosen,
    # and the next incomplete stage is deployment or later in mid phase.
    build_stage = next((s for s in state["workflow"] if s["id"] == "build"), None)
    build_done = build_stage and build_stage["status"] == "complete"
    data_mode = state.get("data_mode")
    needs_data_mode_choice = build_done and data_mode is None and current and current["id"] in {"deployment", "analysis"}

    if gate_decision in {"pivot", "drop"}:
        state["current_phase"] = "pre"
        state["current_stage"] = "novelty"
        state["next_action"] = (
            f"Novelty gate decision: {gate_decision.upper()}. "
            "Stop before study design and reformulate the idea into a keep-worthy HCI direction."
        )
    elif needs_data_mode_choice:
        state["current_phase"] = current["phase"]
        state["current_stage"] = current["id"]
        state["next_action"] = (
            "DATA MODE REQUIRED: Study design is complete. Before proceeding to deployment, "
            "choose a data mode by running:\n"
            "  python3 scripts/autochi.py set-data-mode <project> synthetic\n"
            "  python3 scripts/autochi.py set-data-mode <project> real\n\n"
            "• synthetic — generate synthetic/simulated data to validate the full pipeline now.\n"
            "• real — pause and wait for the user to provide real participant data and/or a working prototype."
        )
    elif current:
        phase = PHASE_INDEX[current["phase"]]
        state["current_phase"] = current["phase"]
        state["current_stage"] = current["id"]
        if current["id"] == "paper":
            state["next_action"] = paper_stage_next_action(project_dir, project_dir / current["artifact"])
        elif data_mode == "real" and current["id"] in {"deployment", "analysis"}:
            state["next_action"] = (
                f"[REAL DATA MODE] Complete {current['label']} in {phase.label} phase at {current['artifact']}. "
                "Design the plan for real participant data collection. "
                "Do NOT generate synthetic data — wait for the user to supply real data or a working prototype."
            )
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
    scaffold_project_files(project_dir, state)

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

    data_mode = state.get("data_mode")
    print(f"Project:      {state['project']['name']}")
    print(f"Venue:        {state['project']['venue']}")
    print(f"DataMode:     {data_mode or 'not set'}")
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


def set_data_mode_cmd(args: argparse.Namespace) -> int:
    project_dir = resolve_project(args.project)
    state_path = project_dir / "STATE.json"
    if not state_path.exists():
        raise SystemExit(f"Missing STATE.json in {project_dir}")
    state = json.loads(state_path.read_text(encoding="utf-8"))
    mode = args.mode.lower()
    if mode not in {"synthetic", "real"}:
        raise SystemExit(f"Invalid data mode: {mode!r}. Must be 'synthetic' or 'real'.")
    state["data_mode"] = mode
    state["project"]["updated_at"] = now_iso()
    state_path.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Data mode set to: {mode}")
    if mode == "real":
        print(
            "The agent will design deployment and analysis plans for real data collection.\n"
            "It will NOT generate synthetic data. Provide your real data or prototype when ready."
        )
    else:
        print(
            "The agent will generate synthetic/simulated data to validate the full pipeline.\n"
            "You can switch to 'real' later with: set-data-mode <project> real"
        )
    # Re-sync to update next_action
    state = sync_project(project_dir)
    return print_status(state, project_dir)


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

    build_paper_parser = subparsers.add_parser(
        "build-paper",
        help="Compile paper/main.tex into output/exports/paper.pdf when a local TeX toolchain is available",
    )
    build_paper_parser.add_argument("project", help="Project path or slug")
    build_paper_parser.set_defaults(func=build_paper_cmd)

    figure_parser = subparsers.add_parser(
        "generate-paper-figure",
        help="Run PaperBanana from paper/figure-plan.md and write a paper figure under output/exports/figures",
    )
    figure_parser.add_argument("project", help="Project path or slug")
    figure_parser.add_argument("--dry-run", action="store_true", help="Validate the PaperBanana figure command without making API calls")
    figure_parser.set_defaults(func=generate_paper_figure_cmd)

    data_mode_parser = subparsers.add_parser(
        "set-data-mode",
        help="Choose synthetic or real data mode before deployment stage",
    )
    data_mode_parser.add_argument("project", help="Project path or slug")
    data_mode_parser.add_argument(
        "mode",
        choices=["synthetic", "real"],
        help="'synthetic' to generate fake data now, 'real' to wait for user-provided data",
    )
    data_mode_parser.set_defaults(func=set_data_mode_cmd)

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
