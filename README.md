# 6G 数据面 × 数据编织 深度洞察工程

> 目标：在两周内，输出一份面向我司决策的《6G 数据面的数据编织技术洞察》深度报告。
> 方法：原料 → 知识 → 分析 → 交付，四层分离、强证据链、可复现。

## 目录约定

| 目录 | 角色 | 何时读写 |
|---|---|---|
| `.cursor/skills/` | 项目级技能族（6 个互相协作的技能） | 由 Agent 自动加载 |
| `wiki/` | **已蒸馏**的可复用知识（带 frontmatter 元数据） | 所有报告论点的"知识中台" |
| `research/` | **原始证据**：抓取/精读全文 + 阅读笔记 + 搜索日志 | 凡 wiki/report 的论点都应能溯源到此 |
| `analysis/` | 跨主题的加工制品：趋势、矩阵、矛盾、缺口、我司适配 | 报告章节的直接素材 |
| `reports/` | 最终交付：执行摘要、一页纸、完整报告 | 周期末产出，多版本迭代 |
| `ops/` | 项目运营：路线、进度、决策日志、公司背景 | 全程维护 |

## 关键约定

### Wiki frontmatter 规范

每张 wiki 卡片（包括 concepts、topics、players、glossary 条目）必须带 YAML frontmatter：

```yaml
---
title: <中文标题>
title_en: <English Title>
slug: <kebab-case-id>
category: concept | topic | player | source | term | timeline
status: draft | reviewed | contested        # 草稿 / 已核对 / 有争议
confidence: high | medium | low              # 论断强度
sources:                                     # 必须列出至少 1 个来源
  - title: <来源标题>
    url: <URL>
    type: standard | vendor | academic | media | analyst
    date: YYYY-MM-DD
    archived: research/raw/<slug>/           # 本地归档路径（可选）
related:                                     # 双向链：相关卡片的 slug
  - <other-slug>
tags: [6g, data-fabric, ai-native, ...]
last_verified: YYYY-MM-DD
owner: agent | human
---
```

### 证据等级（写在每个论断旁）

- **[高]** 至少 2 个独立权威来源（标准组织、顶会论文、官方公告）一致
- **[中]** 1 个权威 + 1 个佐证，或多个分析师/媒体一致
- **[低]** 单一来源、推测、未核实 → 必须在 `analysis/gaps.md` 列入待核实

### 调研近时性

凡涉及"现状/趋势/数字"的论断，**优先使用 2023-01-01 之后**的来源；引用更老资料时必须显式标注日期与"截至 …"。

## 工作流（Agent 视角）

```
Day 1-2:  6g-onboarding   → 概念地图 + 术语词典
Day 3-4:  6g-source-radar → 标准/厂商/学术信息源全覆盖
Day 5-9:  6g-deep-dive    → 子题逐个深调（每题 → wiki/topics/）
          6g-wiki-curator → 每写入 3-5 张卡片做一次治理
Day 10:   6g-trend-synth  → 跨主题趋势、矩阵、矛盾
Day 11:   company-fit 映射
Day 12-13:6g-insight-report → 报告 v1
Day 14:   迭代与定稿
```

## 启动指令（给 Agent）

**最简单 —— 一键调度（推荐）**：

> "调度一下"

会自动调用 `6g-conductor` 扫状态、判断下一步、给出确切启动指令。

**按计划推进**：

> "按 ops/plan.md 推进，当前在第 N 天，请执行今日任务。"

**指名执行**（你已经知道要做什么）：

> "在 6g-deep-dive 下，深调子题 <slug>。"
> "在 6g-trend-synth 下，全流程综合。"
> "在 6g-insight-report 下，写大纲 v1。"


## 仓库

https://github.com/newmanxiang/6GDataPlane
