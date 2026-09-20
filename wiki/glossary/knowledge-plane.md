---
term_zh: 知识面
term_en: Knowledge Plane
abbr: KP
slug: knowledge-plane
category: term
sources:
  - title: YD/T 6103-2024 IP自智网络 知识面技术要求
    url: https://std.samr.gov.cn/hb/search/stdHBDetailed?id=29962E7E064FA432E06397BE0A0A0BF0
    type: standard
    date: 2024-10-24
  - title: Building knowledge planes to scale autonomous networks
    url: https://inform.tmforum.org/research-and-analysis/reports/building-knowledge-planes-to-scale-autonomous-networks
    type: analyst
    date: 2026-07-01
  - title: ITU-T M.3351 Framework of knowledge management for telecom operation and management
    url: https://www.itu.int/epublications/publication/itu-t-m-3351-2024-08-framework-of-knowledge-management-for-telecom-operation-and-management
    type: standard
    date: 2024-08-01
related:
  - ontology
  - knowledge-graph
  - tm-forum
  - ontology-standards-tmf-ccsa-3gpp
tags: [knowledge-plane, autonomous-network, ontology, ccsa, tm-forum]
last_verified: 2026-09-20
owner: agent
---

# 知识面（Knowledge Plane，KP）

**一句话定义**：位于数据/控制机制之上、用结构化语义把碎片数据转化为可被 AI 与闭环使用的知识的架构层；国内以 YD/T 6103-2024 对 IP 自智网络给出可实施要求，TM Forum Inform 则将其视为到达 AN L4 的前提。

**来源**：[YD/T 6103-2024](https://std.samr.gov.cn/hb/search/stdHBDetailed?id=29962E7E064FA432E06397BE0A0A0BF0)（发布 2024-10-24，实施 2025-02-01）；[Inform 知识面报告](https://inform.tmforum.org/research-and-analysis/reports/building-knowledge-planes-to-scale-autonomous-networks)（2026-07-01，仅摘要）；相邻的运维知识管理框架见 [ITU-T M.3351](https://www.itu.int/epublications/publication/itu-t-m-3351-2024-08-framework-of-knowledge-management-for-telecom-operation-and-management)（2024-08）。

**相关概念**：
- [ontology](./ontology.md) — 知识面依赖形式化本体作为语义契约
- [knowledge-graph](./knowledge-graph.md) — 知识面常用图谱作为存储与推理载体
- [tm-forum](./tm-forum.md) — Semantic Knowledge Fabric / TR326 叙事（全文未公开核实）
- [ontology-standards-tmf-ccsa-3gpp](../topics/ontology-standards-tmf-ccsa-3gpp.md)

**易混淆点**：
- 与**数据面 / 6G Data Framework（SA2 WT#5）**：数据面解决数据搬运、暴露与访问；知识面解决语义、推理与策略生成。二者互补，不可互相替代。
- 与 **SA5 DMFW**：DMFW 管管理数据的生命周期与目录；知识面消费这些数据并产出可执行知识。Nokia 等主张在数据管理下讨论知识，Samsung 主张独立语义网管——名称尚未统一。
- 与 **YD/T 7019 知识管理**：7019 规范知识的分类、流程与信息模型（事实/原理/技能/人际）；6103 规范 IP AN 中知识面的功能模块（表征、知识库、策略生成与验证等）。前者是管理要求，后者是（IP 域）平面架构。

**首次出现于本工程**：2026-09-20，wiki/glossary/knowledge-plane.md
