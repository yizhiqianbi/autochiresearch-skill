# Workspace Bootstrap

Use this note only when `scripts/resolve_autochi_repo.py` cannot find an AutoCHIResearch workspace.

## Minimum Workspace Shape

An AutoCHIResearch workspace should contain:

- `program.md`
- `program.zh-CN.md`
- `README.md`
- `README.zh-CN.md`
- `scripts/autochi.py`
- `skills/`

Projects do not need to live inside the workspace repository. New runs should default to a separate
projects directory, for example a sibling `autochiresearch-projects/` directory or whatever
`AUTOCHI_PROJECTS_DIR` points to.

## Preferred Resolution

1. If the current repository already contains `scripts/autochi.py` and `program.md`, use it.
2. If the user has a local clone elsewhere, set `AUTOCHI_REPO=/abs/path/to/autochiresearch`.
3. If no workspace exists yet, clone or create one in the current environment before continuing.

## After Bootstrap

Run:

```bash
python3 scripts/autochi.py status <project-path-or-slug>
```

Then continue the normal phase workflow.
