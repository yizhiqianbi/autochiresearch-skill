# Distribution Guide — LLM Study, Phase 1
<!-- Study: LLM对大学生就业的影响 -->
<!-- Generated: 2026-03-22 -->

## Distribution Strategy

The researcher manually shares one stable survey link. No automated mass-mailing tool is used. Distribution happens through direct researcher-controlled channels in waves.

## Pre-Distribution Checklist

Before sending the link to any channel, confirm:

- [ ] Pilot with 8–12 students is complete and any wording issues are resolved.
- [ ] The survey link is final and stable. All distribution will use this single link — do not create multiple version links.
- [ ] The interview opt-in form uses a different URL from the main survey.
- [ ] The researcher has a note-taking file (outside the dataset) to record which channel each wave went to and on which date.

## Recommended Distribution Channels

Prioritize channels where participants are actively preparing for internships, full-time jobs, or graduate school. Reach out in this order:

1. **University career-center mailing lists** — highest trust context; ask the career center to forward a short paragraph.
2. **WeChat class and department groups** — highest reach for current students; post during weekday evenings when activity is highest.
3. **Student organization and career club WeChat groups** — members are likely to be actively job-searching.
4. **Alumni communities (graduated within the past 12 months)** — essential for capturing recent-graduate experience.
5. **Internship and job-search communities** — supplement if response count is below target after the first two weeks.

Keep a log of the date and channel for each distribution push. This is needed to later flag clustering effects and to audit the source_channel column in exported data.

## Recruitment Text (Chinese — WeChat / Mailing List)

```
我们正在开展一项研究，了解大学生在求职准备过程中如何使用 AI 工具（如 ChatGPT、Kimi、豆包等）。问卷大约需要 10–12 分钟，涉及简历写作、面试准备和职业规划等话题。

参与条件：18 岁及以上，目前在读高校或毕业不超过 12 个月，正在准备实习、校招或考研等。

我们不会要求你上传简历或录取通知书，数据仅做匿名学术分析使用。

问卷链接：[INSERT LINK]

如有意愿参加 20–30 分钟的后续访谈，问卷末尾有单独的报名入口。
```

## Recruitment Text (English — International Channels)

```
We are running a research study on how university students use AI tools such as ChatGPT, Kimi, and Doubao during career preparation. The survey takes about 10–12 minutes and covers resume writing, interview practice, and career planning.

Eligibility: age 18 or older, currently enrolled in higher education or graduated within the past 12 months, and currently engaged in at least one career-preparation activity.

We do not ask you to upload resumes or offer letters. Responses are analyzed in aggregate only.

Survey link: [INSERT LINK]

If you are interested in a 20–30 minute follow-up interview, an opt-in form is available at the end of the survey.
```

## Manual Distribution Rules

- Use one stable link for the entire collection wave. Changing the link mid-study fragments the data.
- Do not revise any core scale items (P1–P12, scenario items, attention checks) after the first real participant completes the survey.
- Eligibility check S2 must exclude participants who select "None of the above" — confirm the platform terminates early for that path.
- If you use WeChat messages, save a screenshot or copy of each push with the date and group name in a researcher notes file (not in the dataset).
- If incentives are offered, collect contact information in a separate sheet with no response-level data.

## Participant Instructions

Include the following text at the start of the survey (before the consent item):

```
欢迎参与本研究。本研究关注大学生在求职准备中使用大语言模型工具的实际情况与感受。

预计完成时间：10–12 分钟。
请在安静、专注的环境中作答，避免中途长时间中断。
所有问题均无对错之分，请根据你的真实情况作答。
部分问题设有注意力检查项，请仔细阅读题目说明。
如需了解本研究，可在完成后联系研究团队。
```

## Interview Opt-In Separation

The interview opt-in page must be on a separate form that does NOT export to the same CSV as the main survey responses. Recommended approach:

- At the end of the main survey, show a final page with a link to a separate Wenjuanxing / Tencent form (or any platform) for interview volunteers.
- The separate form collects: preferred contact method, contact detail, and a random respondent code if linkage is ever needed.
- The main survey response export must never include a contact email or phone number.

## Source Channel Tagging

If the survey platform supports UTM-style source parameters (e.g., `?source=wechat_cs_dept`), use them to pre-fill the `source_channel` field in the export. If not available, collect source channel as a self-report item at the start of the screener:

```
你是通过以下哪个渠道看到本问卷的？
- 院系/学院微信群
- 就业指导中心通知
- 班级群或同学转发
- 校友群
- 其他
```

Map these to short canonical values in the export: `dept_wechat`, `career_center`, `class_group`, `alumni`, `other`.

## Distribution Log Template

Keep a plain-text note outside the dataset with entries like:

```
2026-03-25  WeChat group: CS Department 2025 届就业群 (~180 members)
2026-03-26  WeChat group: 商学院 MBA 秋招群 (~95 members)
2026-03-28  Career center email: [University name] forwarded to ~1200 students
2026-04-03  Follow-up reminder in CS group (first push was 9 days ago, response slowed)
```
