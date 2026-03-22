---
name: study-deployment-ops
description: Deploy HCI surveys and web prototypes to a user-controlled server with HTTPS, logging, health checks, collection monitoring, and data export. Validate the live flow with playwright before opening data collection.
---

# Study Deployment Ops

Use this skill when a study is ready to go live on a server.

## Workflow

1. Confirm what is being deployed: survey, prototype, or prototype plus linked questionnaire.
2. Define the runtime stack and secrets needed.
3. Configure HTTPS, routing, logging, backups, and health checks.
4. Ensure the data model captures:
   - session ID
   - timestamps
   - completion status
   - attention-check results
   - task outcomes or gameplay events if relevant
5. If the flow includes both prototype and questionnaire, preserve a stable session identifier across the handoff.
6. Use `playwright` to test:
   - landing page
   - consent
   - prototype task flow
   - questionnaire submission
   - data write path
7. Add monitoring and stop criteria for sample collection.
8. Document how to export data for analysis.

## Rules

- Do not open collection before a smoke test passes.
- Treat privacy-sensitive data conservatively and document what is stored.
- Prefer simple, inspectable deployments over heavy infrastructure for first-pass studies.
- If the study is gameplay-like, log enough state to reconstruct a session without collecting unnecessary PII.

## Outputs

Produce these artifacts whenever possible:

- deployment checklist
- environment variable list
- smoke-test steps
- collection monitor notes
- export instructions
