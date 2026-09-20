---
term_zh: 本体
term_en: Ontology
abbr: —
slug: ontology
category: term
sources:
  - title: TR292 TM Forum Intent Ontology (TIO) v3.6.0
    url: https://www.tmforum.org/resources/introductory-guide/tr292-tm-forum-intent-ontology-tio-v3-6-0/
    type: standard
    date: 2024-07-04
  - title: YD/T 7007-2026 知识建模方法（SAMR 元数据）
    url: https://std.samr.gov.cn/hb/search/stdHBDetailed?id=5679B6F617894858E06397BE0A0AD0B8
    type: standard
    date: 2026-06-01
  - title: TIO-SHACL arXiv:2604.27359
    url: https://arxiv.org/abs/2604.27359
    type: academic
    date: 2026-04-30
related:
  - knowledge-graph
  - knowledge-plane
  - tm-forum
  - ontology-standards-tmf-ccsa-3gpp
tags: [ontology, rdf, owl, shacl, tio, sid]
last_verified: 2026-09-20
owner: agent
---

# 本体（Ontology）

**一句话定义**：对某一领域共享概念（类、关系、公理）的形式化规格，使机器能一致地解释数据与意图；在电信标准中，真正以 RDF/OWL 交付的代表是 TM Forum TIO，而 SID/3GPP NRM 仍主要是信息模型。

**来源**：[TR292 TIO v3.6.0](https://www.tmforum.org/resources/introductory-guide/tr292-tm-forum-intent-ontology-tio-v3-6-0/)（2024-07-04）；[YD/T 7007-2026](https://std.samr.gov.cn/hb/search/stdHBDetailed?id=5679B6F617894858E06397BE0A0AD0B8)（解读层区分本体模型与实例化模型）；[tio-shacl](https://arxiv.org/abs/2604.27359)（2026-04-30）。

**相关概念**：
- [knowledge-graph](./knowledge-graph.md) — 实例层；本体是其模式
- [knowledge-plane](./knowledge-plane.md) — 把本体与运行时知识交给自治系统使用的架构层
- [tm-forum](./tm-forum.md) — TIO 与规划中的联邦/SID 本体
- [ontology-standards-tmf-ccsa-3gpp](../topics/ontology-standards-tmf-ccsa-3gpp.md) — 本轮主题卡

**易混淆点**：
- 与**信息模型**（SID/MODA UML、3GPP NRM、YANG）：信息模型回答"对象有哪些字段"；本体还要求 IRI、公理与（可选）SHACL 校验。把 SID 直接叫本体会高估其机器可推理程度。
- 与**知识图谱**：图谱是三元组/属性图实例库；YD/T 7007 将本体模型定义为类级模式，实例化模型才构成图谱。
- 与 **TIO**：TIO 是意图子域本体，不是 SID 全量 OWL 化。

**首次出现于本工程**：2026-09-20，wiki/glossary/ontology.md
