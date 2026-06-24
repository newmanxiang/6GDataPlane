# Wiki：6G 数据面 × 数据编织 知识中台

> 已蒸馏、可复用、可被报告引用的知识。原料请见 `research/`。

## 目录结构

| 目录 | 内容 | 命名 |
|---|---|---|
| `glossary/` | 术语词典（中英对照） | `<slug>.md` |
| `concepts/6g-data-plane/` | 6G 数据面侧核心概念 | 同上 |
| `concepts/data-fabric/` | 数据编织侧核心概念 | 同上 |
| `sources/standards/` | 标准组织登记 | `<org-slug>.md` |
| `sources/vendors/` | 厂商登记 | `<vendor-slug>.md` |
| `sources/academia/` | 学术与会议登记 | `<venue-slug>.md` |
| `topics/` | 子题深调产出 | `<topic-slug>.md` |
| `players/` | 关键玩家档案（厂商 / 实验室 / 项目） | `<player-slug>.md` |
| `timeline/` | 关键事件时间线 | `<year>-<event-slug>.md` |
| `templates/` | 各类卡片模板 | - |

## 卡片状态约定

| status | 含义 |
|---|---|
| `draft` | 占位/初稿，未必充分核实 |
| `reviewed` | 已经至少 1 轮核对，可被报告引用 |
| `contested` | 存在矛盾或争议，需要谨慎引用并配合 `analysis/contradictions.md` |

## 信心等级

| confidence | 要求 |
|---|---|
| `high` | ≥ 2 个独立权威来源（标准 / 顶会 / 官方公告） |
| `medium` | 1 个权威 + ≥ 1 个佐证 |
| `low` | 单一来源或推测，禁止直接用于结论 |

## 统计快照（由 6g-wiki-curator 维护）

> 最后更新：2026-06-23 D9 全量治理

| 类别 | 数量 | draft / reviewed / contested |
|---|---|---|
| concept | 20 | 20 / 0 / 0 |
| topic | 10 | 0 / 10 / 0 |
| player | 0 | - |
| source | 31 | - |
| term | 21 | - |

## 双向链约定

- 在 `related:` 字段引用其他卡片时用 **slug**（不带路径），不用相对路径
- Curator 会在治理时自动维护双向链对称性
