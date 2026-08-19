# Reports：交付层

## 三件套

| 文件 | 受众 | 长度 |
|---|---|---|
| `deep-insight-report-vN.md` | 同行 + 决策者 | 30-50 页（≈ 12000-20000 字） |
| `executive-summary.md` | 决策者 | 2-3 页 |
| `one-pager.md` | 高层 | 1 页（≤ 500 字） |

## 战略胶片

| 文件 | 说明 |
|---|---|
| `6g-data-fabric-strategy-deck.pptx` | 由 HTML 报告生成的 24 页完整论证版 PPT（非预览版） |
| `scripts/build_strategy_pptx.py` | 再生脚本：`python3 reports/scripts/build_strategy_pptx.py` |
| `6g-data-fabric-sections-234-deck.pptx` | 2.3 / 3 / 4 章金字塔洞察胶片（16 页）：2.3 每子节一页并嵌入厂商架构图；第3章按价值链编排；第4章一页收束时间窗 |
| `scripts/build_sections_234_pptx.py` | 再生脚本：`python3 reports/scripts/build_sections_234_pptx.py` |
| `6g-data-fabric-section-23-deck.pptx` | 2.3 六页独立胶片：提出分歧 → 划定边界 → 三家案例 → 归纳结论；不另设封面 |
| `scripts/build_section_23_pptx.py` | 再生脚本：`python3 reports/scripts/build_section_23_pptx.py` |
| `6g-data-fabric-section-3-deck.pptx` | 第三章六页独立胶片：趋势结构 → T2/T3 → T1/T6 → T4/T5 → T7双路径 → T8标准承载 |
| `scripts/build_section_3_pptx.py` | 再生脚本：`python3 reports/scripts/build_section_3_pptx.py` |
| `plan-section3.md` | 第三章胶片制作计划 |
| `plan-sections5-7.md` | 第5–7章六页决策胶片制作计划：2页现状定位、1页模式、2页机会选择、1页公司策略表 |
| `6g-data-fabric-sections-5-7-deck.pptx` | 第5–7章六页决策胶片：现状与缺口 → 目标定位 → 一横多纵模式 → 四类机会 → 优先/时间盒/扩展 → 公司策略表；文字写入形状卡片，不使用独立文本框 |
| `scripts/build_sections_5_7_pptx.py` | 再生脚本：`python3 reports/scripts/build_sections_5_7_pptx.py` |
| `6g-data-fabric-sections-5-9-deck.pptx` | 第5–8章五页内部策略胶片：5.1+5.2、5.3+5.4、第6章、第7章、第8章各一页；第9章仅作为HTML整体小结；文字写入形状卡片或表格单元格 |
| `scripts/build_sections_5_9_pptx.py` | 五页胶片再生脚本：`python3 reports/scripts/build_sections_5_9_pptx.py` |
| `6g-data-fabric-industry-trends-full-sections.html` | 完整 HTML 论证正文 |
| `6g-data-fabric-industry-trends-first-four-sections.html` | 对应完整 HTML 论证正文 |

## 版本规则

- 主报告以 `v1`、`v2`、`v3` 递增
- 每次重大改写另存一版，保留 v(N-1) 不删
- 执行摘要与一页纸跟随最新主报告，不带版本号（如需追溯查 git 历史）

## 写作顺序（参见 6g-insight-report SKILL）

1. `outline.md` ← 大纲先行
2. `deep-insight-report-v1.md` ← 章节正文
3. `executive-summary.md` ← 主报告完成后写
4. `one-pager.md` ← 最后写
5. 迭代 → v2、v3
