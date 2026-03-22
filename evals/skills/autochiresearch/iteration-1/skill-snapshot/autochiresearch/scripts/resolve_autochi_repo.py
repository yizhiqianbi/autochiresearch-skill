#!/usr/bin/env python3
"""Resolve an AutoCHIResearch workspace without hardcoding one machine path."""

from __future__ import annotations

import os
import sys
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent


def is_repo_root(path: Path) -> bool:
    return (path / "scripts" / "autochi.py").exists() and (path / "program.md").exists()


def candidates() -> list[Path]:
    found: list[Path] = []

    env_path = os.environ.get("AUTOCHI_REPO")
    if env_path:
        found.append(Path(env_path).expanduser())

    cwd = Path.cwd().resolve()
    found.extend([cwd, *cwd.parents])

    for base in [cwd, *cwd.parents]:
        sibling = base / "autochiresearch"
        found.append(sibling)

    # Repo-local copy when the skill lives inside the workspace repository.
    found.extend([SKILL_DIR.parents[1], SKILL_DIR.parents[2] if len(SKILL_DIR.parents) > 2 else SKILL_DIR])

    return found


def main() -> int:
    seen: set[Path] = set()
    for candidate in candidates():
        try:
            resolved = candidate.resolve()
        except FileNotFoundError:
            continue
        if resolved in seen:
            continue
        seen.add(resolved)
        if is_repo_root(resolved):
            print(resolved)
            return 0
    print("AutoCHIResearch workspace not found", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
