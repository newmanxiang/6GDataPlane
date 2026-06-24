# Trends：趋势卡片

> 每张趋势卡是一个**判断**而非话题。

## 模板（参见 6g-trend-synth SKILL）

```markdown
---
title: <趋势标题>
slug: trend-<kebab>
horizon: 12m | 24m | 36m
confidence: high | medium | low
direction: emerging | accelerating | mainstream | declining | uncertain
drivers: []
inhibitors: []
evidence: [<wiki/topics slug>]
counter_evidence: [<wiki/topics slug>]
companies_to_watch: []
my_company_relevance: high | medium | low | tbd
created: YYYY-MM-DD
---

# <趋势标题>

## 一句话总结
[≤ 40 字]

## 论据（按强度排序）
1. ...
2. ...

## 反向证据 / 不确定性
- ...

## 信号事件
- YYYY-MM：[事件]（来源）

## 未来 12-24 月可观察的指标
- [ ] ...

## 何时该被推翻
- [若 X 发生 → 推翻；若 Y 持续不发生 → 弱化]
```

## 索引

> 由 trend-synth 维护，最后更新：2026-06-25

| # | 趋势卡 | 信心 | 方向 | 时间窗 |
|:--|:--|:--:|:--:|:--:|
| 1 | [6G 数据面将从用户面独立为新功能面](trend-independent-data-plane.md) | medium | emerging | 36m |
| 2 | [数据编织将在 2027-2028 进入电信规模试点](trend-data-fabric-telecom-adoption.md) | medium | emerging | 24m |
| 3 | [GTP-U 将在 6G 时代被 SRv6/MUP 替代](trend-gtp-u-sunset.md) | medium | emerging | 36m |
| 4 | [AI 原生网络需要全新数据管理范式](trend-ai-native-data-management.md) | high | accelerating | 24m |
| 5 | [6G 数据面标准化窗口在 2026-2027 关键收敛](trend-standardization-race.md) | high | accelerating | 12m |
| 6 | [跨域数据治理将成为 6G 部署的前置条件](trend-cross-domain-governance.md) | medium | emerging | 24m |
| 7 | [Mesh-on-Fabric 混合架构将成为电信数据管理主流](trend-mesh-on-fabric-hybrid.md) | low | emerging | 36m |

### 信心分布
- **High (2)**：AI 原生数据管理、标准化竞赛
- **Medium (4)**：独立数据面、数据编织电信化、GTP-U 替代、跨域治理
- **Low (1)**：Mesh-on-Fabric 混合架构
