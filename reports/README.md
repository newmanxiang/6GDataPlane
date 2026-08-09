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
