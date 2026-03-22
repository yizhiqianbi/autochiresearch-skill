#!/usr/bin/env python3
"""Generate a synthetic dry-run dataset for the canvas vs terminal multi-agent study."""

from __future__ import annotations

import argparse
import csv
import random
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "output" / "collection" / "2026-03-22_synthetic_export_raw.csv"
DEFAULT_TEMPLATE = ROOT / "output" / "collection" / "manual_template.csv"
PARTICIPANTS = list(range(1, 25))
EXCLUDED_PARTICIPANTS = {7, 19}
TASKS = ["delegation", "monitoring", "recovery"]
CONDITIONS = ["terminal", "canvas"]

ROLE_OPTIONS = ["research", "engineering", "design", "product_analysis"]
USE_OPTIONS = ["weekly", "several_times_weekly", "daily"]
FAMILIARITY_OPTIONS = ["rarely", "sometimes", "often"]

CENTERS = {
    ("terminal", "delegation"): {
        "time": 625,
        "success": 80,
        "intervention": 3.2,
        "recovery": 82,
        "mental": 4.4,
        "effort": 4.3,
        "transparency": 5.7,
        "control": 5.5,
        "recall": 3.1,
        "reuse": 5.2,
    },
    ("terminal", "monitoring"): {
        "time": 905,
        "success": 73,
        "intervention": 4.8,
        "recovery": 142,
        "mental": 5.2,
        "effort": 5.1,
        "transparency": 4.8,
        "control": 4.7,
        "recall": 2.7,
        "reuse": 4.7,
    },
    ("terminal", "recovery"): {
        "time": 545,
        "success": 84,
        "intervention": 2.7,
        "recovery": 63,
        "mental": 4.5,
        "effort": 4.4,
        "transparency": 5.8,
        "control": 5.9,
        "recall": 3.2,
        "reuse": 5.1,
    },
    ("canvas", "delegation"): {
        "time": 705,
        "success": 84,
        "intervention": 3.0,
        "recovery": 92,
        "mental": 4.0,
        "effort": 4.0,
        "transparency": 5.7,
        "control": 5.6,
        "recall": 4.1,
        "reuse": 5.2,
    },
    ("canvas", "monitoring"): {
        "time": 770,
        "success": 86,
        "intervention": 3.6,
        "recovery": 96,
        "mental": 3.8,
        "effort": 3.9,
        "transparency": 6.0,
        "control": 5.8,
        "recall": 4.5,
        "reuse": 5.7,
    },
    ("canvas", "recovery"): {
        "time": 590,
        "success": 79,
        "intervention": 3.5,
        "recovery": 76,
        "mental": 4.3,
        "effort": 4.2,
        "transparency": 5.3,
        "control": 5.2,
        "recall": 3.9,
        "reuse": 5.0,
    },
}


def clamp(value: float, lo: float, hi: float) -> float:
    return max(lo, min(value, hi))


def likert(rng: random.Random, center: float, spread: float = 0.55) -> str:
    return str(round(clamp(rng.gauss(center, spread), 1, 7), 2))


def integerish(rng: random.Random, center: float, spread: float, lo: int, hi: int) -> str:
    return str(int(round(clamp(rng.gauss(center, spread), lo, hi))))


def role_for(pid: int) -> str:
    return ROLE_OPTIONS[pid % len(ROLE_OPTIONS)]


def note_bundle(condition: str, task: str) -> tuple[str, str]:
    if condition == "canvas":
        strategy = {
            "delegation": "I used the board layout to see whether any role or dependency was missing before launching agents.",
            "monitoring": "The spatial board let me compare branches without rereading the whole history.",
            "recovery": "I could see which stale branch fed the writer, then repair the connection after tracing the red edge.",
        }[task]
        friction = {
            "delegation": "I still wanted a quick keyboard action to insert a missing reviewer without dragging.",
            "monitoring": "The board was clearer, but moving between cards took longer than skimming a terminal pane.",
            "recovery": "I saw the causal structure quickly, but the repair took more clicks than a direct command.",
        }[task]
    else:
        strategy = {
            "delegation": "The command stream made assignment quick, but I kept a mental checklist of missing steps.",
            "monitoring": "I relied on log timestamps and repeated inspection commands to reconstruct state across agents.",
            "recovery": "The terminal made it easy to issue a precise fix once I figured out where the stale input lived.",
        }[task]
        friction = {
            "delegation": "I had to remember the whole plan because the log did not preserve structural gaps well.",
            "monitoring": "I felt like I was scrolling to compare branches that would have been easier to scan side by side.",
            "recovery": "The fix was fast, but reconstructing the upstream cause still required extra mental work.",
        }[task]
    return strategy, friction


def build_rows(rng: random.Random) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for pid in PARTICIPANTS:
        order = CONDITIONS if pid % 2 == 0 else list(reversed(CONDITIONS))
        for condition in order:
            for task in TASKS:
                center = CENTERS[(condition, task)]
                strategy, friction = note_bundle(condition, task)
                rows.append(
                    {
                        "participant_id": f"p{pid:02d}",
                        "condition_order": "terminal_first" if order[0] == "terminal" else "canvas_first",
                        "interface_condition": condition,
                        "task_type": task,
                        "consent": "Yes",
                        "completed_session": "No" if pid in EXCLUDED_PARTICIPANTS else "Yes",
                        "attention_check_pass": "No" if pid in EXCLUDED_PARTICIPANTS else "Yes",
                        "work_role": role_for(pid),
                        "ai_use_frequency": USE_OPTIONS[pid % len(USE_OPTIONS)],
                        "terminal_familiarity": FAMILIARITY_OPTIONS[(pid + 1) % len(FAMILIARITY_OPTIONS)],
                        "canvas_familiarity": FAMILIARITY_OPTIONS[(pid + 2) % len(FAMILIARITY_OPTIONS)],
                        "completion_seconds": integerish(rng, center["time"], 58, 320, 1350),
                        "task_success_pct": integerish(rng, center["success"], 6.2, 45, 99),
                        "intervention_count": integerish(rng, center["intervention"], 0.9, 1, 8),
                        "recovery_latency_seconds": integerish(rng, center["recovery"], 17, 20, 240),
                        "workload_mental": likert(rng, center["mental"]),
                        "workload_effort": likert(rng, center["effort"]),
                        "transparency_score": likert(rng, center["transparency"]),
                        "control_score": likert(rng, center["control"]),
                        "plan_recall_score": likert(rng, center["recall"]),
                        "reuse_score": likert(rng, center["reuse"]),
                        "strategy_note": strategy,
                        "friction_note": friction,
                    }
                )
    return rows


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def write_template(path: Path, fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=20260322)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--template", type=Path, default=DEFAULT_TEMPLATE)
    args = parser.parse_args()

    rng = random.Random(args.seed)
    rows = build_rows(rng)
    write_csv(args.out, rows)
    write_template(args.template, list(rows[0].keys()))
    print(args.out)
    print(args.template)
    print(f"Wrote {len(rows)} synthetic trial rows.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
