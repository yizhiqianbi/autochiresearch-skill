# Distribution Guide — LLM Career Study
<!-- project: projects/llm -->
<!-- study: Phase 1 Survey — Manual Distribution, No Server -->

## Approach

The researcher distributes a survey link personally, through existing social networks and institutional channels. There is no automated recruitment funnel, email campaign tool, or server-side tracking. The platform (Wenjuanxing or Qualtrics) generates one stable HTTPS link that is copied into messages and group posts.

---

## Pre-Distribution Requirements

Before sending a single message:

1. Pilot is complete and the survey wording is frozen.
2. Smoke test has passed (see `deployment-plan.md`).
3. Pilot rows have been deleted from the live dataset.
4. The stable survey link is confirmed to open with HTTPS.
5. The interview opt-in form is live on a separate URL.

---

## Target Channels

Send recruitment messages to the following channels in order of expected yield:

| Priority | Channel | Notes |
|---|---|---|
| 1 | WeChat group chats — active job-search groups | Highest response speed for China sample |
| 2 | WeChat group chats — class and cohort groups | Broad demographic coverage |
| 3 | University career center mailing lists | Reach motivated career-prep users |
| 4 | Department or advisor-forwarded emails | Adds disciplinary diversity |
| 5 | Alumni group chats (within 12 months of graduation) | Captures recent-graduate segment |
| 6 | Student organization networks (career clubs, consulting clubs) | Heavy LLM-user segment |
| 7 | Internship and job-search community forums (e.g., Maimai, BOSS Zhipin community boards) | If institutional approval allows |

---

## Recruitment Message Templates

### Short version (WeChat / group chat)

> 同学好，我们正在做一项关于大学生如何使用 AI 工具（如 ChatGPT、Kimi、豆包等）辅助求职的学术研究。问卷约 10–12 分钟，不需要上传简历或 offer。年满 18 周岁且正在准备实习、工作或升学的同学均可参与。
>
> 问卷链接：[在此处插入链接]
>
> 感谢支持！

### Long version (email / mailing list)

> 你好，
>
> 我们正在开展一项学术研究，探究大学生在求职准备过程中使用大型语言模型（LLM，如 ChatGPT、Kimi、豆包、通义等）的方式，以及这些工具对求职信心、感知就业能力和技能发展的影响。
>
> 参与条件：年满 18 周岁；目前在读（本科、硕士或博士）或毕业不超过 12 个月；正在准备实习、正式工作、升学或其他职业过渡。
>
> 问卷约需 10–12 分钟，完全匿名，不收集简历、offer 或其他个人敏感文件。
>
> 如有意愿参与后续 20–30 分钟访谈，可在问卷末尾单独留下联系方式（与问卷回答分开存储）。
>
> 问卷链接：[在此处插入链接]
>
> 如有任何问题，欢迎回复本邮件。感谢您的支持！

### English version (for bilingual channels or international students)

> We are conducting academic research on how university students use AI tools such as ChatGPT, Kimi, and Doubao during career preparation. The survey takes about 10–12 minutes and asks about resume writing, interview preparation, and career planning. We do not ask for resumes or offer letters. If you are 18 or older and currently preparing for internships, jobs, or graduate school, you are welcome to participate.
>
> Survey link: [insert link here]
>
> Thank you for your support.

---

## Distribution Rules

- Use one and only one stable survey link throughout the entire collection wave. Do not generate a second link or start a duplicate survey form.
- Do not revise core scale items or skip logic after the survey goes live.
- Send the recruitment message to each channel only once per wave, with a single follow-up reminder after 7–10 days if the target is not yet reached.
- Record each distribution push in the researcher's log (channel, date, approximate audience size). Do not include this log in the public dataset.
- If a channel moderator asks for IRB documentation or ethics approval, provide a brief summary and the consent language from `studies/survey.md`. Do not promise incentives that were not pre-approved.

---

## Researcher Distribution Log Template

Keep a private note (e.g., a local text file not committed to git) with the following format:

```
Date        | Channel                          | Audience est. | Sent by
------------|----------------------------------|---------------|--------
2026-MM-DD  | WeChat job-search group A        | ~200          | [initials]
2026-MM-DD  | Department mailing list B        | ~150          | [initials]
2026-MM-DD  | Reminder: WeChat group A         | ~200          | [initials]
```

---

## Interview Opt-In Handling

The interview opt-in link must be a separate form from the main survey. After survey closure:

1. Export the interview interest file as `output/collection/YYYY-MM-DD_interview_interest_raw.csv`.
2. Use the survey platform's response IDs (not names or contact details) to draw a purposive sample for interviews.
3. Contact selected volunteers via their provided method (WeChat, email, phone).
4. Collect interview consent separately before scheduling.
5. Store interview notes or transcripts under `output/collection/interviews/` in a subfolder, never merged with the main CSV.

---

## Incentives (If Used)

If you decide to offer an incentive (e.g., a small red-envelope raffle):

- Do not attach the incentive-contact sheet to the main survey form.
- Create a separate short form that only asks for contact details for the draw.
- Store the incentive list in a file that has no `response_id` linkage to the survey export.
- Do not name the file in a way that implies it contains survey data.

---

## Stopping Distribution

Stop sending new recruitment messages when either:

- The survey has accumulated 250+ valid responses (after attention-check filtering), or
- The survey is paused due to quality issues (see `deployment-plan.md` stop criteria).

Notify all channels that the survey is closed with a brief thank-you message.
