# Results Summary

This file reports a **synthetic dry run** for pipeline validation only. These are not real participant
results and must not be treated as empirical evidence.

## Sample

- Raw trial rows: 144
- Excluded participants: 2
- Retained participants: 22
- Retained trial rows: 132

## Interface-Level Pattern

- `terminal`: completion=684.621 sec, success=79.303%, workload=4.681, transparency=5.41, recall=2.989
- `canvas`: completion=684.848 sec, success=82.5%, workload=4.114, transparency=5.638, recall=4.206

## Task-Level Pattern

- Monitoring favored the canvas condition on both success and recall:
  - terminal monitoring success=72.364%, recall=2.751
  - canvas monitoring success=85.227%, recall=4.573
- Recovery favored terminal speed but not necessarily global understanding:
  - terminal recovery time=539.409 sec, latency=61.773 sec
  - canvas recovery time=584.182 sec, latency=72.955 sec

## Directional Takeaway

- The synthetic pattern supports the intended story: the canvas condition helps state awareness and plan reconstruction, while the terminal condition helps direct surgical repair.
- The most promising design implication is hybridization rather than winner-take-all replacement.
