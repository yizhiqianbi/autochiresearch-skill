---
name: study-deployment-ops
description: >
  Prepare HCI studies for data collection: local preview and smoke-testing, manual distribution
  packaging, CSV export templates, collection monitoring, and data export workflows. Optionally
  deploy to a user-controlled server with HTTPS when explicitly requested. Use this skill whenever
  a study is ready to be distributed or needs collection infrastructure — whether the plan is to
  share a local URL manually, use an external survey platform, or self-host. Default to local-first:
  run the study locally, prepare materials for human distribution, and define the export path.
  Only provision server infrastructure if the user explicitly asks for it.
---

# Study Deployment Ops

This skill handles everything between "the study design is ready" and "data is flowing in." The
default approach is **local-first**: run the app locally, package materials for manual human
distribution, and set up clean data export. Server deployment is a secondary option available when
the user explicitly wants it.

## Default Path: Local Preview + Manual Distribution

Most HCI studies in this workflow use manual external distribution. The typical flow is:

1. **Confirm the distribution strategy**: local-only preview, manual link sharing, external platform
   (e.g. Qualtrics, Typeform, Google Forms), or self-hosted server.
2. **Local smoke test**:
   - Run the study app locally (`python3 prototype/app.py run --host 127.0.0.1 --port <port>`).
   - Walk through the full participant flow: landing → consent → study/survey → submission.
   - Use `playwright` to automate validation if available.
3. **Prepare manual distribution package**:
   - Generate a CSV template for manual data entry or external platform exports:
     `python3 analysis/import_flat_csv.py --write-template output/collection/manual_template.csv`
   - Write a distribution guide under `studies/distribution-guide.md` with:
     - participant instructions
     - the local or hosted URL
     - expected completion time
     - any screener or eligibility check
4. **Define data capture**:
   - Confirm the data model captures: session ID, timestamps, completion status,
     attention-check results, task outcomes if relevant.
   - If prototype and questionnaire are linked, preserve a stable session identifier across the handoff.
5. **Write the deployment plan** (`deploy/deployment-plan.md`):
   - Distribution method
   - Data storage location
   - Export and import procedure
   - Stop criteria (target N, deadline, or quality threshold)
6. **Document the export path**:
   - How to export collected data to `output/collection/`
   - How to import a returned flat CSV: `python3 analysis/import_flat_csv.py --csv <file> --db <db>`

## Optional Path: Server Deployment

Only follow this path when the user explicitly asks to deploy to a server.

1. Define the runtime stack and secrets.
2. Configure HTTPS, routing, logging, backups, and health checks.
3. Use `playwright` to validate the live flow end-to-end before opening collection.
4. Add monitoring and stop criteria.
5. Document how to export data for analysis.

## Rules

- Do not open collection before a smoke test passes.
- Default to local-first. Do not provision server infrastructure unless the user explicitly requests it.
- Treat privacy-sensitive data conservatively and document what is stored.
- Prefer simple, inspectable setups over heavy infrastructure for first-pass studies.
- If the study involves gameplay or interaction logging, log enough state to reconstruct a session
  without collecting unnecessary PII.
- Keep raw collected data under `output/collection/`; keep cleaned analysis outputs under
  `output/analysis/`.

## Outputs

Produce these artifacts:

- `deploy/deployment-plan.md`
- `studies/distribution-guide.md`
- `output/collection/manual_template.csv` (when using manual or external distribution)
- smoke-test steps or playwright script
- collection monitor notes
- export and re-import instructions
