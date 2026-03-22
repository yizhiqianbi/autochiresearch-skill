# Deployment Plan

## Idea Anchor
无限画布 vs 终端界面下的多 agent 使用模式对比：研究知识工作者在协调多个 AI agent 时的策略、认知负荷与产出质量差异

## Runtime Stack
- Local-first static prototype in `prototype/modes_mockup.html`
- Optional local server via `python3 -m http.server 4173` from the `prototype/` directory
- Synthetic CSV generation and analysis scripts in `analysis/`
- No external server is required for the current package

## Server / Host
Default path: local preview only.

- Host: `127.0.0.1`
- Port: `4173`
- Command:

```bash
cd /Users/pencil/Documents/PrepareMLLM/autochiresearch-projects/canvas-vs-terminal-multi-agent/prototype
python3 -m http.server 4173
```

If the project later moves to real participant sessions, deploy behind a simple authenticated study launcher rather than exposing raw logs publicly.

## Study Routes and Session Flow
- `/modes_mockup.html`
  - landing view describing the shared scenario
  - tab switch between `Canvas Mode` and `Terminal Mode`
  - scenario switch between `delegation`, `monitoring`, and `recovery`
- Researcher opens the corresponding task sheet and observes participant actions
- After each condition, questionnaire data can be recorded manually or through a lightweight form that writes to the canonical CSV schema

## Operational Checklist
- HTTPS: not required for local pilot mode
- Logging: manual observer notes plus optional browser-local export of synthetic interaction traces
- Backups: keep generated CSV snapshots under `output/collection/`
- Health checks: confirm the local page loads, tabs switch, and task panels render before any session
- Session linking: assign a local participant code and keep any identity mapping outside the repo

## Smoke Test Script
1. Run local server from `prototype/`
2. Open `http://127.0.0.1:4173/modes_mockup.html`
3. Verify:
   - both interface tabs render
   - scenario buttons switch content
   - the summary panel updates when a scenario changes
4. Capture one screenshot of each interface under `output/playwright/` for documentation
5. Run synthetic analysis scripts to ensure downstream files are regenerated successfully

## Collection Monitor Rules
- For real sessions, inspect exports after every `5` participants
- Validate that each participant has:
  - both conditions
  - all three task records
  - a valid condition-order marker
  - questionnaire completion
- Pause collection if more than `10%` of sessions show missing task logs or mismatched condition labels

## Sample Target
- Pilot validation in this repository: synthetic data only
- Real study target: `24` to `30` participants with balanced order
- Minimum viable dataset for initial analysis: `20` fully completed participant sessions

## Data Export Plan
- Store the canonical raw export under `output/collection/`
- Store cleaned analysis outputs under `output/analysis/`
- Keep paper-ready figures under `output/analysis/`
- For this local package, regenerate outputs with:

```bash
python3 analysis/generate_fake_data.py
python3 analysis/analyze_fake_data.py
```
