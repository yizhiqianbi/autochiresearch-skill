# AutoCHIResearch Skill

这个仓库现在是合并后的单一入口。以后以 `/Users/pencil/Documents/PrepareMLLM/autochiresearch-skill` 为准，它同时承担两件事：

1. `skills/` 下的 Codex skill 包
2. 一个可直接运行的 AutoCHIResearch workspace

不再需要先依赖旁边那个 `autochiresearch` 仓库。

## 仓库里有什么

- `skills/autochiresearch/`
  - 主 skill
- `skills/shared-references/`
  - 多个 skill 共用的流程规范
- `skills/chi-project-runner/`
  - 兼容旧名字的 alias
- `skills/chi-topic-scout/`
  - topic 和 novelty 检索辅助
- `skills/hci-study-designer/`
  - user study / questionnaire / prototype 设计辅助
- `skills/hci-analysis-writer/`
  - 分析与结果整理辅助
- `skills/study-deployment-ops/`
  - 本地预览、分发和收数准备辅助
- `skills/paper-compile/`
  - LaTeX 论文 PDF 构建辅助
- `scripts/autochi.py`
  - 项目初始化、状态机、阶段同步
- `templates/`
  - `autochi.py` 使用的项目脚手架模板
- `evals/`
  - 各个 skill 的评测工件和 benchmark 快照
- `docs/`
  - 架构说明和仓库布局说明
- `examples/`
  - 整理好的 demo case 和可分享项目快照
- `program.md` / `program.zh-CN.md`
  - 工作流总说明
- `projects/`
  - 仓库内保留的兼容/示例项目；新 run 默认不应落在这里

## 推荐一起安装的配套 Skill

这些已经装进你当前的 Codex 环境里，适合作为 `autochiresearch-skill` 的增强依赖：

- `frontend-skill`
  - 做更完整的 web prototype
- `spreadsheet`
  - 做 CSV 清洗、表格核对和结构化数据检查
- `transcribe`
  - 做访谈或研究音频转写
- `doc`
  - 处理 Word 类研究文档、说明稿和导出表单

## 怎么开始

先进入这个仓库：

```bash
cd /Users/pencil/Documents/PrepareMLLM/autochiresearch-skill
```

初始化一个项目：

```bash
python3 scripts/autochi.py init --idea "你的原始 HCI idea"
```

查看状态：

```bash
python3 scripts/autochi.py status <项目 slug 或路径>
```

现在 `init` 默认会把项目建到仓库外的同级目录 `../autochiresearch-projects/`，避免污染 skill 仓库。
如果你要统一改默认位置，设置 `AUTOCHI_PROJECTS_DIR` 即可。
如果你之前已经把项目建在仓库内，可以运行 `python3 scripts/autochi.py migrate-legacy-projects`
把旧项目迁到新的外部目录。
当论文主稿和 review 都准备好后，可以运行 `python3 scripts/autochi.py build-paper <project>`
尝试把 `paper/main.tex` 编译成 `output/exports/paper.pdf`。

如果你是通过 Codex 调用 skill，直接说：

```text
用 $autochiresearch 跑这个题，从 idea 一直到本地分析和成文。
```

## 设计原则

- 默认 local-first
- 人给一个 idea，剩下默认由 agent 推进
- 可以本地设计问卷、原型、分析和论文
- 可以人工把问卷发到外部平台，再把 CSV 导回本地
- 每次运行产物统一放到项目内的 `output/`
- 新项目默认放在 skill 仓库外，避免把运行产物和 skill 本体混在一起
- 论文阶段必须有一个独立的 sub-agent 评审产物 `paper/paper-review.md`，不能只靠主 agent 自判完成
- 运行时 skill、本地模板、共享规范、评测工件要分开放，避免所有东西都堆在 `skills/` 里
- demo case 可以作为快照放在 `examples/`，但活跃项目仍然默认放在仓库外

## 说明

这个仓库已经包含了 AutoCHIResearch 的关键工作区骨架和项目内 skill，不再依赖另一个本地仓库才能起步。对于 `citation-management`、`scientific-writing`、`playwright` 这类更通用的技能，仍然是“有则优先用，没有也可以按同样流程继续完成”的增强项。

## Demo Case

当前仓库已经带了一个整理好的 demo case：

- `examples/canvas-vs-terminal-multi-agent/`
  - 一个完整的本地研究包，主题是“无限画布 vs 终端的多 agent 使用模式比较”
  - 包含 prototype、synthetic 分析产物、`5000+` 词论文主稿和编译好的 PDF 快照
