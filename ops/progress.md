# 进度跟踪

> 每天末 Agent 更新本文件。

## 模板

```markdown
## D<N> · YYYY-MM-DD

### 计划
- ...

### 完成
- ...

### 未完成（滚到明日）
- ...

### 关键产出
- wiki/concepts/<...>.md
- wiki/topics/<...>.md
- analysis/...

### 数据/关键发现
- ...

### 阻塞 / 风险
- ...

### 明日要点
- ...
```

---

## D2 · 2026-06-20（B+C 类概念 + 概念地图 v1）

### 计划
- 调用 6g-onboarding 完成 B 类（数据编织侧 7 项）骨架卡片
- 调用 6g-onboarding 完成 C 类（交集 4 项）骨架卡片
- 刷新概念地图为 v1 全量版

### 完成
- B 类 7 张 concept 草稿卡片全部创建
- C 类 4 张 concept 草稿卡片全部创建
- Glossary 新增 10 条术语（data-fabric, data-mesh, active-metadata, knowledge-graph, data-virtualization, data-orchestration, federated-learning, differential-privacy, mec, tm-forum）
- 概念地图 v1 全量刷新（含 B 类内部协作链、C 类交集连线、研究空白标注）
- deep-dive-queue 累计子题入队

### 关键产出
- wiki/concepts/ × 11 张新卡片（B7 + C4）
- wiki/glossary/ × 10 条新术语
- wiki/concepts/README.md 概念地图 v1

### 数据/关键发现
- **B 类核心洞察**：数据编织七大能力形成"语义发现(KG) → 统一访问(虚拟化) → 自动流转(编排)"协作链，主动元数据是驱动引擎
- **Gartner vs Forrester**：前者侧重技术驱动（元数据分析+自动化），后者侧重业务价值（实时可信访问）
- **数据编织 vs 数据网格**：核心区分在治理模式（集中 vs 联邦），行业趋势是混合互补
- **C 类研究空白发现**：
  - `data-fabric-for-ai-native-6g` 文献极度稀缺，属开拓性议题（最具原创价值方向）
  - `privacy-preserving-data-fabric` 中 PETs 与 Data Fabric 的架构级融合缺乏系统性研究
  - 边缘数据编织在 ETSI MEC 标准体系中尚无对应规范
- **C 类已有实证**：TM Forum Catalyst C23.0.517 验证电信数据编织可降运营成本 51%

### 阻塞 / 风险
- 无

### 明日要点
- D3：调用 6g-source-radar 全量铺面（标准 11 + 厂商 8 + 分析机构 2）
- 每张源卡填 contact_topics、search_aliases、key_documents

---

## D1 · 2026-06-20（A 类概念入门）

### 计划
- 调用 6g-onboarding 完成 A 类（6G 数据面侧 9 项）骨架卡片
- 每张卡填最小定义（≤100 字），标待深挖子题
- 同步创建 glossary 术语条目

### 完成
- 9 张 A 类 concept 草稿卡片全部创建（draft 状态）
- 11 条 glossary 术语条目创建
- deep-dive-queue 汇入 27 个待深挖子题（P0×6 / P1×17 / P2×4）
- concepts/README.md 概念地图更新（新增概念间关系连线）

### 关键产出
- wiki/concepts/6g-overview.md
- wiki/concepts/6g-data-plane.md
- wiki/concepts/user-plane-evolution.md
- wiki/concepts/ai-native-air-interface.md
- wiki/concepts/ran-architecture-evolution.md
- wiki/concepts/network-data-analytics.md
- wiki/concepts/digital-twin-network.md
- wiki/concepts/isac.md
- wiki/concepts/non-terrestrial-network.md
- wiki/glossary/ × 11 条（6g, imt-2030, upf, gtp-u, ai-native-air-interface, o-ran, nwdaf, ai-ran, digital-twin-network, isac, ntn）

### 数据/关键发现
- 6G（IMT-2030）已于 2026-02 完成 20 项技术性能需求定义
- 华为提出 DaaS（数据即服务）概念，Hexa-X-II 定义四平面架构（数据面/智能面/计算面/安全面）
- 3GPP SA2 正讨论 6G 数据框架（WT#5）但尚未标准化
- GTP-U 灵活性不足已被识别为 6G 瓶颈，替代方案含 SRv6/IETF MUP
- AI-RAN Alliance（2024 MWC 成立）推动 GPU 共享 RAN+AI 推理
- ISAC 感知数据量可能超过通信数据本身，对数据面是全新高吞吐流量源
- NTN 长时延（20-40ms）要求数据面协议栈全面自适应

### 阻塞 / 风险
- company-context.md 仍全占位（不影响 D1-D10，但 D12 §8 需要填充）

### 明日要点
- D2：完成 B 类（数据编织侧 7 项）+ C 类（交集 4 项）概念骨架
- 调用 6g-wiki-curator 做首次治理（T1 + T7）
- 刷新概念地图 v1

---

## D0 · YYYY-MM-DD（工程初始化）

### 完成
- 工程目录骨架
- 6 个技能 SKILL.md
- Wiki / research / analysis / reports / ops 模板
- 两周路线 ops/plan.md

### 阻塞 / 风险
- 无

### 配置变更
- 2026-06-20 09:33 — Firecrawl MCP 已配置（~/.cursor/mcp.json，权限 600）
- 当前 MCP：Exa + Firecrawl 双引擎 + cursor-ide-browser

### 明日要点
- 启动 D1：6g-onboarding 完成 A 类必修概念骨架
