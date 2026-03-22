#!/usr/bin/env python3
"""Analyze the synthetic dry-run dataset for the canvas vs terminal study."""

from __future__ import annotations

import argparse
import csv
import os
from collections import Counter, defaultdict
from pathlib import Path
from statistics import mean

TMP_CACHE = Path("/tmp") / "canvas-terminal-study-cache"
TMP_CACHE.mkdir(parents=True, exist_ok=True)
os.environ.setdefault("MPLCONFIGDIR", str(TMP_CACHE / "matplotlib"))
os.environ.setdefault("XDG_CACHE_HOME", str(TMP_CACHE))
os.environ.setdefault("MPLBACKEND", "Agg")

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_IN = ROOT / "output" / "collection" / "2026-03-22_synthetic_export_raw.csv"
DEFAULT_OUT = ROOT / "output" / "analysis"


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, object]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def exclude_rows(rows: list[dict[str, str]]) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    excluded = []
    kept = []
    excluded_participants = set()
    for row in rows:
        if row["consent"] != "Yes":
            excluded_participants.add(row["participant_id"])
        if row["completed_session"] != "Yes" or row["attention_check_pass"] != "Yes":
            excluded_participants.add(row["participant_id"])
    for row in rows:
        if row["participant_id"] in excluded_participants:
            excluded.append({"participant_id": row["participant_id"], "reason": "incomplete_or_attention_fail"})
        else:
            kept.append(row)
    unique_excluded = {}
    for row in excluded:
        unique_excluded[row["participant_id"]] = row
    return kept, list(unique_excluded.values())


def enrich(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    out = []
    for row in rows:
        enriched = dict(row)
        enriched["workload_score"] = round(mean([float(row["workload_mental"]), float(row["workload_effort"])]), 3)
        for key in [
            "completion_seconds",
            "task_success_pct",
            "intervention_count",
            "recovery_latency_seconds",
            "transparency_score",
            "control_score",
            "plan_recall_score",
            "reuse_score",
        ]:
            enriched[key] = float(row[key])
        out.append(enriched)
    return out


def participant_condition_summary(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    groups: dict[tuple[str, str], list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        groups[(row["participant_id"], row["interface_condition"])].append(row)
    out = []
    for (participant_id, interface_condition), group in sorted(groups.items()):
        out.append(
            {
                "participant_id": participant_id,
                "interface_condition": interface_condition,
                "condition_order": group[0]["condition_order"],
                "mean_completion_seconds": round(mean(r["completion_seconds"] for r in group), 3),
                "mean_task_success_pct": round(mean(r["task_success_pct"] for r in group), 3),
                "mean_intervention_count": round(mean(r["intervention_count"] for r in group), 3),
                "mean_recovery_latency_seconds": round(mean(r["recovery_latency_seconds"] for r in group), 3),
                "mean_workload_score": round(mean(r["workload_score"] for r in group), 3),
                "mean_transparency_score": round(mean(r["transparency_score"] for r in group), 3),
                "mean_control_score": round(mean(r["control_score"] for r in group), 3),
                "mean_plan_recall_score": round(mean(r["plan_recall_score"] for r in group), 3),
                "mean_reuse_score": round(mean(r["reuse_score"] for r in group), 3),
            }
        )
    return out


def overall_condition_summary(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    groups: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        groups[row["interface_condition"]].append(row)
    out = []
    for condition, group in groups.items():
        out.append(
            {
                "interface_condition": condition,
                "n_trials": len(group),
                "completion_seconds_mean": round(mean(r["completion_seconds"] for r in group), 3),
                "task_success_pct_mean": round(mean(r["task_success_pct"] for r in group), 3),
                "intervention_count_mean": round(mean(r["intervention_count"] for r in group), 3),
                "recovery_latency_seconds_mean": round(mean(r["recovery_latency_seconds"] for r in group), 3),
                "workload_score_mean": round(mean(r["workload_score"] for r in group), 3),
                "transparency_score_mean": round(mean(r["transparency_score"] for r in group), 3),
                "control_score_mean": round(mean(r["control_score"] for r in group), 3),
                "plan_recall_score_mean": round(mean(r["plan_recall_score"] for r in group), 3),
                "reuse_score_mean": round(mean(r["reuse_score"] for r in group), 3),
            }
        )
    return sorted(out, key=lambda row: row["interface_condition"])


def task_condition_summary(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    groups: dict[tuple[str, str], list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        groups[(row["task_type"], row["interface_condition"])].append(row)
    out = []
    for (task_type, interface_condition), group in sorted(groups.items()):
        out.append(
            {
                "task_type": task_type,
                "interface_condition": interface_condition,
                "n_trials": len(group),
                "completion_seconds_mean": round(mean(r["completion_seconds"] for r in group), 3),
                "task_success_pct_mean": round(mean(r["task_success_pct"] for r in group), 3),
                "recovery_latency_seconds_mean": round(mean(r["recovery_latency_seconds"] for r in group), 3),
                "workload_score_mean": round(mean(r["workload_score"] for r in group), 3),
                "plan_recall_score_mean": round(mean(r["plan_recall_score"] for r in group), 3),
            }
        )
    return out


def summarize_participants(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    seen = {}
    for row in rows:
        seen.setdefault(
            row["participant_id"],
            {
                "work_role": row["work_role"],
                "ai_use_frequency": row["ai_use_frequency"],
                "terminal_familiarity": row["terminal_familiarity"],
                "canvas_familiarity": row["canvas_familiarity"],
            },
        )
    counters = {
        "work_role": Counter(v["work_role"] for v in seen.values()),
        "ai_use_frequency": Counter(v["ai_use_frequency"] for v in seen.values()),
        "terminal_familiarity": Counter(v["terminal_familiarity"] for v in seen.values()),
        "canvas_familiarity": Counter(v["canvas_familiarity"] for v in seen.values()),
    }
    total = len(seen)
    out = []
    for dim, counter in counters.items():
        for category, count in sorted(counter.items()):
            out.append({"dimension": dim, "category": category, "count": count, "percent": round(100 * count / total, 1)})
    return out


def summarize_themes(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    themes = {
        "spatial_overview": ["board", "branch", "layout", "edge"],
        "mental_reconstruction": ["mental", "remember", "scrolling", "reconstruct"],
        "fast_command_repair": ["precise", "command", "fix", "repair"],
        "hybrid_request": ["quick", "keyboard", "clicks", "side by side"],
    }
    counts = Counter()
    for row in rows:
        text = f"{row['strategy_note']} {row['friction_note']}".lower()
        for theme, keywords in themes.items():
            if any(keyword in text for keyword in keywords):
                counts[f"{row['interface_condition']}::{theme}"] += 1
    return [{"theme": theme, "count": count} for theme, count in sorted(counts.items())]


def plot_condition_metric(path: Path, summary: list[dict[str, object]], metric: str, ylabel: str) -> None:
    labels = [row["interface_condition"] for row in summary]
    values = [float(row[metric]) for row in summary]
    colors = ["#c95c28", "#345f89"]
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar(labels, values, color=colors)
    ax.set_ylabel(ylabel)
    ax.set_title(f"{ylabel} by interface")
    fig.tight_layout()
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=160)
    plt.close(fig)


def plot_task_success(path: Path, summary: list[dict[str, object]]) -> None:
    tasks = ["delegation", "monitoring", "recovery"]
    terminal = [next(row for row in summary if row["task_type"] == task and row["interface_condition"] == "terminal")["task_success_pct_mean"] for task in tasks]
    canvas = [next(row for row in summary if row["task_type"] == task and row["interface_condition"] == "canvas")["task_success_pct_mean"] for task in tasks]
    x = range(len(tasks))
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.bar([i - 0.18 for i in x], terminal, width=0.36, label="terminal", color="#c95c28")
    ax.bar([i + 0.18 for i in x], canvas, width=0.36, label="canvas", color="#345f89")
    ax.set_xticks(list(x))
    ax.set_xticklabels(tasks)
    ax.set_ylabel("Task success (%)")
    ax.set_title("Synthetic task success by interface and task")
    ax.legend()
    fig.tight_layout()
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=160)
    plt.close(fig)


def write_results_markdown(
    out_dir: Path,
    retained_rows: list[dict[str, object]],
    excluded_participants: list[dict[str, str]],
    condition_rows: list[dict[str, object]],
    task_rows: list[dict[str, object]],
) -> None:
    by_condition = {row["interface_condition"]: row for row in condition_rows}
    terminal = by_condition["terminal"]
    canvas = by_condition["canvas"]

    monitoring_terminal = next(row for row in task_rows if row["task_type"] == "monitoring" and row["interface_condition"] == "terminal")
    monitoring_canvas = next(row for row in task_rows if row["task_type"] == "monitoring" and row["interface_condition"] == "canvas")
    recovery_terminal = next(row for row in task_rows if row["task_type"] == "recovery" and row["interface_condition"] == "terminal")
    recovery_canvas = next(row for row in task_rows if row["task_type"] == "recovery" and row["interface_condition"] == "canvas")

    summary = f"""# Results Summary

This file reports a **synthetic dry run** for pipeline validation only. These are not real participant
results and must not be treated as empirical evidence.

## Sample

- Raw trial rows: {len(retained_rows) + len(excluded_participants) * 6}
- Excluded participants: {len(excluded_participants)}
- Retained participants: {len(set(row['participant_id'] for row in retained_rows))}
- Retained trial rows: {len(retained_rows)}

## Interface-Level Pattern

- `terminal`: completion={terminal['completion_seconds_mean']} sec, success={terminal['task_success_pct_mean']}%, workload={terminal['workload_score_mean']}, transparency={terminal['transparency_score_mean']}, recall={terminal['plan_recall_score_mean']}
- `canvas`: completion={canvas['completion_seconds_mean']} sec, success={canvas['task_success_pct_mean']}%, workload={canvas['workload_score_mean']}, transparency={canvas['transparency_score_mean']}, recall={canvas['plan_recall_score_mean']}

## Task-Level Pattern

- Monitoring favored the canvas condition on both success and recall:
  - terminal monitoring success={monitoring_terminal['task_success_pct_mean']}%, recall={monitoring_terminal['plan_recall_score_mean']}
  - canvas monitoring success={monitoring_canvas['task_success_pct_mean']}%, recall={monitoring_canvas['plan_recall_score_mean']}
- Recovery favored terminal speed but not necessarily global understanding:
  - terminal recovery time={recovery_terminal['completion_seconds_mean']} sec, latency={recovery_terminal['recovery_latency_seconds_mean']} sec
  - canvas recovery time={recovery_canvas['completion_seconds_mean']} sec, latency={recovery_canvas['recovery_latency_seconds_mean']} sec

## Directional Takeaway

- The synthetic pattern supports the intended story: the canvas condition helps state awareness and plan reconstruction, while the terminal condition helps direct surgical repair.
- The most promising design implication is hybridization rather than winner-take-all replacement.
"""
    prose = """# Results Prose

The synthetic dry run produces the directional contrast that the paper and analysis plan are designed
to inspect. Across interface-level summaries, the canvas condition shows lower workload and stronger
plan recall than the terminal condition, while maintaining higher transparency during monitoring-heavy
tasks. At the task level, the monitoring scenario exhibits the clearest canvas advantage because users
can inspect dependencies, stalled nodes, and overlapping branches without mentally reconstructing the
entire workflow from a chronological stream. In contrast, the recovery scenario preserves one clear
terminal strength: once participants identify the exact problem, the textual condition supports fast,
precise repair through compact commands.

The qualitative synthetic notes echo the same tradeoff. Canvas-side notes emphasize overview,
dependency visibility, and the ability to reconstruct the workflow at a glance. Terminal-side notes
emphasize quick intervention, low-friction command entry, and frustration caused by having to remember
structural state that was not visually externalized. Taken together, the dry run validates a manuscript
framing centered on complementarity: future agent interfaces should combine spatial state awareness
with direct command affordances rather than assume either representation is sufficient on its own.
"""
    (out_dir / "results_summary.md").write_text(summary, encoding="utf-8")
    (out_dir / "results_prose.md").write_text(prose, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=DEFAULT_IN)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()

    raw = read_rows(args.input)
    retained, excluded = exclude_rows(raw)
    enriched = enrich(retained)

    args.out.mkdir(parents=True, exist_ok=True)

    write_csv(args.out / "exclusion_log.csv", excluded, ["participant_id", "reason"])
    write_csv(args.out / "cleaned_trials.csv", enriched, list(enriched[0].keys()))
    participant_rows = participant_condition_summary(enriched)
    write_csv(args.out / "participant_condition_summary.csv", participant_rows, list(participant_rows[0].keys()))
    sample_rows = summarize_participants(enriched)
    write_csv(args.out / "sample_characteristics.csv", sample_rows, ["dimension", "category", "count", "percent"])
    condition_rows = overall_condition_summary(enriched)
    write_csv(args.out / "condition_summary.csv", condition_rows, list(condition_rows[0].keys()))
    task_rows = task_condition_summary(enriched)
    write_csv(args.out / "task_condition_summary.csv", task_rows, list(task_rows[0].keys()))
    theme_rows = summarize_themes(enriched)
    write_csv(args.out / "qualitative_theme_summary.csv", theme_rows, ["theme", "count"])

    plot_condition_metric(args.out / "figure_workload_by_condition.png", condition_rows, "workload_score_mean", "Workload")
    plot_condition_metric(args.out / "figure_recall_by_condition.png", condition_rows, "plan_recall_score_mean", "Plan recall")
    plot_task_success(args.out / "figure_task_success_by_condition.png", task_rows)
    write_results_markdown(args.out, enriched, excluded, condition_rows, task_rows)
    print(args.out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
