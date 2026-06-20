# 两周路线图（Plan）

> 起点：YYYY-MM-DD（你确认开始日，写入此处） | 终点：起点 + 14 天
> 进度跟踪：`ops/progress.md` | 决策记录：`ops/decisions.md`

## 调用约定

### 最常用：让调度器自己决定

每次推进只需一句：
> "调度一下"

`6g-conductor` 会扫描当前状态、对照本路线图、派遣下一个该跑的子技能。

### 替代用法（你明确知道做什么时）

> "按 ops/plan.md 推进，当前在第 N 天，请执行今日任务。"
> "在 6g-<skill> 下，<具体动作>"

### 每天结束前 Agent 必须做

1. 把今日产出登记到 `ops/progress.md`
2. 把未完成事项滚到明日
3. 把新发现的子题加入 `ops/deep-dive-queue.md`
4. （可选）让 conductor 输出"明日预派遣"快照

---

## W1：奠基与铺面

### D1（启动）
- [ ] 阅读 `README.md` 与所有 6 个技能 SKILL.md
- [ ] 阅读 `ops/company-context.md`（如已填）
- [ ] 调用 **6g-onboarding** 完成必修概念清单中 **A 类（6G 数据面侧 9 项）** 的骨架卡片
- [ ] 每张骨架卡填 ≤ 100 字的"最小定义"，列待深挖子题

**产出**：9 张 A 类 concept 草稿 + glossary 雏形

### D2
- [ ] 调用 **6g-onboarding** 完成 **B 类（数据编织侧 7 项）** 骨架卡片
- [ ] 完成 **C 类（交集 4 项）** 骨架卡片
- [ ] 调用 **6g-wiki-curator** 做 T1（frontmatter）+ T7（统计快照）
- [ ] 刷新 `wiki/concepts/README.md` 的概念地图

**产出**：20 张 concept 草稿 + 概念地图 v1

### D3
- [ ] 调用 **6g-source-radar** 全量铺面 标准 + 厂商
- [ ] 至少：11 个标准组织 + 8 个厂商 + 2 个分析机构
- [ ] 每张源卡填 contact_topics、search_aliases、key_documents（≥ 1）

**产出**：≥ 21 张 source 卡

### D4
- [ ] 完成 **6g-source-radar** 学术与会议铺面（10 个会议/期刊）
- [ ] 把所有 concept 卡片的"待深挖子题"汇总到 `ops/deep-dive-queue.md`
- [ ] 对 queue 排序：先 A 类（6G 数据面），再 C 类（交集），最后 B 类（数据编织）
- [ ] 优先级标记：P0（报告必须） / P1（强相关） / P2（锦上添花）

**产出**：deep-dive-queue.md v1（≥ 25 个候选子题）

### D5-D7
- [ ] 调用 **6g-deep-dive** 每天 1-2 个 P0 子题
- [ ] 推荐子题（W1 D5-D7）：
  - `6g-data-plane-architecture-2025`（核心定义子题）
  - `imt-2030-framework-data-needs`
  - `user-plane-evolution-upf-to-6g`
  - `ai-native-data-plane-status`
- [ ] 每深调 2 个后调用 **6g-wiki-curator** T1+T3+T4 治理

**产出**：4-6 张 topic 卡 + 持续治理

---

## W2：深挖、综合、报告

### D8-D9
- [ ] 继续 **6g-deep-dive** P0 子题
  - `data-fabric-definition-and-capabilities`（数据编织定义子题）
  - `data-fabric-vs-data-mesh`
  - `data-fabric-in-telecom-early-cases`
- [ ] 中段调用 **6g-source-radar** 流程 D 周巡检
- [ ] D9 末调用 **6g-wiki-curator** 全量治理（T1-T7）

**产出**：7-9 张 topic 卡

### D10（交集议题专题日）⭐
- [ ] 调用 **6g-deep-dive** 专攻交集议题：
  - `data-fabric-for-ai-native-6g`（**最关键的交集子题**）
  - `cross-domain-data-governance-6g`
- [ ] 这两个主题允许超时间盒（最多 4 小时）

**产出**：交集议题 ≥ 2 张高质量 topic 卡

### D11（趋势综合日）
- [ ] 调用 **6g-trend-synth** 全流程
  - 主题聚类
  - 矩阵 M1-M4
  - 趋势卡 ≥ 5 张
  - 矛盾汇总
  - forecast.md

**产出**：analysis/ 全套加工件

### D12（我司适配日）
- [ ] 调用 **6g-insight-report**（仅 §8 准备阶段）
- [ ] 在 `analysis/company-fit/` 输出 capability-map / opportunities / threats / actions
- [ ] 严格遵守"我司可执行尺度"、短/中/长期分级

**产出**：company-fit 全套

### D13（报告 v1）
- [ ] 调用 **6g-insight-report** 阶段 1（大纲核查 → 素材覆盖 ≥ 80%）
- [ ] 不满足覆盖率：回到 deep-dive 补料（提前预留 2 小时缓冲）
- [ ] 启动阶段 2 章节写作（§1-§4 必须完成）

**产出**：outline v1 + 报告 §1-§4

### D14（定稿与三件套）
- [ ] 完成报告 §5-§9
- [ ] 阶段 3 执行摘要
- [ ] 阶段 4 一页纸
- [ ] **6g-wiki-curator** 报告前最终核查
- [ ] **6g-insight-report** 自检清单全过
- [ ] 输出 `deep-insight-report-v1.md` + `executive-summary.md` + `one-pager.md`

**产出**：三件套 v1

---

## 缓冲与应急

- 每个 D5-D10 预留 30 分钟用于矛盾追查
- 若 D11 时主题 < 6 张，延后趋势综合 1 天，压缩 D14 缓冲
- D10（交集议题日）可主动使用 `firecrawl_deep_research` 作为"第二意见"，与人工迭代结果对照
- 当出现需要批量从多份白皮书提取相同字段时（如填厂商×能力矩阵 M1），优先使用 `firecrawl_extract` 替代逐篇人工读
- **每日红线**：若调研 < 4 小时实质产出，停下来到 `ops/decisions.md` 复盘
