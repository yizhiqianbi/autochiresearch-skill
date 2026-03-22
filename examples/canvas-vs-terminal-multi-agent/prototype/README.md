# Prototype Notes

This folder contains a local-first high-fidelity mockup for the matched interface comparison.

## File

- `modes_mockup.html`: side-by-side design concept with two interface tabs:
  - `Canvas Mode`
  - `Terminal Mode`

## Purpose

The mockup is not a full agent runtime. It exists to make the research comparison concrete, support pilot walkthroughs, and document the exact interface properties being compared.

## Local Preview

```bash
cd /Users/pencil/Documents/PrepareMLLM/autochiresearch-projects/canvas-vs-terminal-multi-agent/prototype
python3 -m http.server 4173
```

Open:

- `http://127.0.0.1:4173/modes_mockup.html`

## Compared Properties

- spatial overview versus linear log history
- visible dependencies versus textual command chaining
- card-level state inspection versus inline terminal inspection
- branch management versus explicit command redirection
