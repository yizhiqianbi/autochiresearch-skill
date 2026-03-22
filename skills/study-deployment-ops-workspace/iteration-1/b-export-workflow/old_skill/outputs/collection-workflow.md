# 数据收集全流程：导出与导入工作手册
<!-- project: projects/llm -->
<!-- date: 2026-03-22 -->

## 概述

本项目（LLM 对大学生就业影响研究）采用无服务器、纯本地分析的模式：

- 问卷托管在第三方平台（如问卷星 / Qualtrics）
- 你负责发放链接，参与者填写后平台存储响应
- 你定期从平台下载 CSV，放入本项目的 `output/collection/` 目录
- 所有清洗和分析在本地用 Python 脚本完成

---

## 一、发布前检查（仅做一次）

在向参与者发送链接前，完成以下验证：

1. 打开公开问卷链接，用干净浏览器窗口走完全流程。
2. 确认以下环节均正常显示：知情同意、筛选题、矩阵题、注意力检查、开放题、人口统计、访谈意向题。
3. 用以下两种身份各提交一份测试响应：
   - 合格参与者（18 岁以上、正在进行求职准备）
   - 不合格参与者（选"Other"跳出筛选）
4. 导出平台 CSV，对照 `output/collection/manual_template.csv` 的列头，确认列名与顺序一致。
5. 如果启用了访谈意向收集，确认联系信息进入了单独的表单 / 导出，不与主响应合并。
6. **在正式收集开始前，从平台数据集中删除所有测试响应。**

---

## 二、链接发放（你自己操作）

按以下渠道逐步推送，每次推送在研究者笔记中记录日期和渠道（不要存入公开数据集）：

| 渠道 | 备注 |
|------|------|
| 院系/学院邮件列表 | 建议在工作日上午发送 |
| 班级/专业 WeChat 群 | 一次收集波次内使用同一条链接 |
| 就业中心公告或海报 | 附二维码，指向同一稳定链接 |
| 校友社区 | 毕业 12 个月内的校友符合纳入标准 |
| 实习/求职社群 | 同上 |

**发放原则：**

- 全程使用同一条稳定问卷链接，不要在数据收集期间修改问卷核心题项。
- 如有激励（礼品卡等），联系信息单独收集，永远不要和响应级数据合并。

---

## 三、每日监控

在主动收集期间每天检查一次，填入研究者日志：

| 监控项 | 警戒阈值 |
|--------|----------|
| 总响应数 | — |
| 完成率（提交 / 开始） | 低于 60% 需排查 |
| 中位完成时长 | 短于 3 分钟（180 秒）视为异常 |
| 注意力检查通过率 | — |
| 开放题中疑似机器生成或无意义答案 | 当日新增中超过 15% 则暂停收集 |
| 学历层次和求职方向的分布均衡度 | — |

若某天异常低时长响应超过 15%，**暂停收集**，检查来源渠道后再恢复。

---

## 四、导出数据（从平台到本地）

### 步骤

1. 登录你的问卷平台（问卷星 / Qualtrics 等）。
2. 进入"数据导出"或"下载数据"功能，选择 **CSV 格式，UTF-8 编码**。
3. 下载时勾选"包含标题行（列名）"，不选额外元数据列（如平台内部 ID 字段，除非你需要追踪）。
4. 保存文件到本项目目录，文件名格式严格遵循：

```
output/collection/YYYY-MM-DD_survey_export_raw.csv
```

例如：

```
output/collection/2026-04-10_survey_export_raw.csv
```

5. 如果存在访谈意向数据，单独命名：

```
output/collection/YYYY-MM-DD_interview_interest_raw.csv
```

6. **不要修改 raw 文件的任何内容**。这是唯一的原始存档。每次导出都保留一个新的日期戳文件，不覆盖旧文件。

### 列名对齐

平台导出的列名往往与项目的规范列名不同（如平台用"Q1"，项目用"consent"）。对齐方式：

- 用文本编辑器或 Excel 打开 raw CSV。
- 对照 `analysis/csv-schema.md` 中的规范字段列表，手动重命名每一列。
- 对照 `output/collection/manual_template.csv`（只有一行列头）确认顺序和拼写完全一致。
- 重命名后另存为同名文件（覆盖），或另起名如 `2026-04-10_survey_export_raw_renamed.csv` 后统一命名为 `_raw.csv` 使用。

规范字段完整列表（共 48 列，顺序如下）：

```
response_id, submitted_at, completion_seconds, source_channel,
consent, eligible_status, participant_stage, career_path_primary,
career_preparation_urgency, llm_used_any, llm_tools_used,
task_resume_freq, task_cover_letter_freq, task_interview_freq,
task_info_search_freq, task_skill_gap_freq, task_portfolio_freq,
task_offer_compare_freq, task_networking_freq,
p_confidence_support, p_employability_support, p_skill_gap_awareness,
p_polish_advantage, p_deskilling_risk, p_verification_behavior,
p_low_vs_high_stakes_trust, p_authenticity_tension,
p_interview_preparedness, p_uncertainty_reduction,
p_fast_acceptance_risk, p_guidance_need,
scenario_a_acceptability, scenario_b_acceptability,
scenario_c_acceptability, scenario_d_acceptability,
attention_check_1, attention_check_2,
open_benefit, open_risk, open_desired_features,
age_range, gender, field_of_study, degree_level,
first_gen_optional, economic_status_optional, background_optional,
interview_opt_in
```

### 编码规则（重要）

| 字段类型 | 期望格式 |
|----------|----------|
| `consent` | `Yes` 或 `No` |
| `eligible_status` | `Yes` 或 `No` |
| `llm_used_any` | `Yes` 或 `No` |
| `llm_tools_used` | 工具名以分号加空格分隔，例如 `ChatGPT; Kimi; Doubao` |
| 任务频率列（`task_*_freq`） | 整数 0–4（0=从不，1=一次，2=每月，3=每周，4=每周多次） |
| 感知题（`p_*`） | 整数 1–5 |
| 场景接受度（`scenario_*`） | 整数 1–5 |
| `attention_check_1` | `Agree`（正确答案）或其他 |
| `attention_check_2` | `Boiling water`（正确答案）或其他 |
| `submitted_at` | ISO 8601，如 `2026-04-10T14:23:00` |
| `completion_seconds` | 整数 |
| `interview_opt_in` | `Yes` 或 `No` |

---

## 五、导入：把 CSV 接入分析流程

### 单次运行（分析一个快照）

将 raw CSV 文件放到 `output/collection/` 后，在项目根目录运行：

```bash
# 如果 raw 文件名不是默认值，用 --input 指定
cd /Users/pencil/Documents/PrepareMLLM/autochiresearch-skill/projects/llm

python3 analysis/analyze_fake_data.py --input output/collection/YYYY-MM-DD_survey_export_raw.csv
```

脚本完成后，`output/analysis/` 目录下会生成以下文件：

| 文件 | 内容 |
|------|------|
| `cleaned_survey.csv` | 通过纳入标准后的有效样本，含衍生变量 |
| `exclusion_log.csv` | 每条被排除记录的 ID 和排除原因 |
| `sample_characteristics.csv` | 人口统计频数表（Table 1） |
| `task_usage_summary.csv` | 各任务 LLM 使用频率（Table 2） |
| `scales_summary.csv` | 量表均值、标准差、Cronbach α（Table 3） |
| `group_comparison_summary.csv` | 非用户 / 轻度 / 重度用户组间比较 |
| `regression_summary.csv` | 就业感知 & 自信支持的回归模型（Table 4） |
| `qualitative_theme_summary.csv` | 开放题主题频次 |
| `results_summary.md` | 可直接复制进稿件的结果段落草稿 |
| `figure_task_distribution.png` | Figure 1 |
| `figure_theme_prevalence.png` | Figure 2 |

### 分批导入多个快照

如果你在数据收集期间做了多次阶段性导出（推荐在达到目标样本量的 50% 和 100% 时各导出一次），每次导出保留独立文件：

```
output/collection/2026-04-10_survey_export_raw.csv   # 中期快照
output/collection/2026-05-01_survey_export_raw.csv   # 最终快照
```

分析时指向最终文件即可，旧快照作为存档保留：

```bash
python3 analysis/analyze_fake_data.py \
  --input output/collection/2026-05-01_survey_export_raw.csv \
  --out output/analysis/
```

---

## 六、排除逻辑说明

`analyze_fake_data.py` 自动按以下规则排除记录，所有排除均记入 `exclusion_log.csv`：

| 排除条件 | 原因代码 |
|----------|----------|
| `consent != "Yes"` | `no_consent` |
| `eligible_status != "Yes"` | `ineligible` |
| `attention_check_1 != "Agree"` 且 `attention_check_2 != "Boiling water"` | `failed_both_attention_checks` |
| `completion_seconds < 180` | `too_fast` |

注意：仅同时失败两项注意力检查才排除；单独失败一项不排除，但建议在 `results_summary.md` 中报告注意力检查通过率。

---

## 七、收集结束后的操作序列

```
1. 关闭问卷（在平台上将状态设为"暂停/停止"）
2. 做最终导出：output/collection/YYYY-MM-DD_survey_export_raw.csv
3. 列名对齐（参照第四节）
4. 运行 python3 analysis/analyze_fake_data.py --input output/collection/<最终文件>.csv
5. 检查 exclusion_log.csv，确认排除人数合理
6. 检查 results_summary.md，更新手稿中的数字
7. 如需跟进访谈，从 output/collection/YYYY-MM-DD_interview_interest_raw.csv
   中提取意向者联系方式（该文件永远不与主响应数据合并）
```

---

## 八、数据隐私备忘

- `output/collection/` 和 `output/analysis/` 中的文件包含参与者响应，不应推送到公开 Git 仓库。
  建议在 `.gitignore` 中添加 `output/collection/*.csv` 和 `output/analysis/*.csv`。
- 访谈联系方式只存在 `interview_interest_raw.csv` 中，与主数据物理隔离。
- 激励用联系信息单独保存在项目目录之外，永远不要出现在响应级 CSV 中。
- 平台上的原始响应在本地备份确认后可选择删除，但建议在报告提交前保留平台存档。

---

## 九、快速参考：目录结构

```
projects/llm/
├── output/
│   ├── collection/
│   │   ├── manual_template.csv               # 只含列头的参照模板
│   │   ├── YYYY-MM-DD_survey_export_raw.csv  # 你从平台下载的原始文件
│   │   └── YYYY-MM-DD_interview_interest_raw.csv  # 访谈意向（独立）
│   └── analysis/
│       ├── cleaned_survey.csv
│       ├── exclusion_log.csv
│       └── ...（分析产出）
├── analysis/
│   ├── csv-schema.md          # 规范列名说明
│   ├── analyze_fake_data.py   # 清洗 + 分析脚本（接受 --input 参数）
│   └── generate_fake_data.py  # 生成合成数据（用于流程测试）
└── studies/
    └── distribution-guide.md  # 发放渠道与命名规范
```

---

*本文档依据 `deploy/deployment-plan.md`、`analysis/csv-schema.md`、`studies/distribution-guide.md` 及分析脚本源码综合整理。*
