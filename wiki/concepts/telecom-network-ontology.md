---
title: 电信网络本体
title_en: Telecom Network Ontology
slug: telecom-network-ontology
category: concept
status: draft
confidence: medium
sources:
  - title: TR292 TM Forum Intent Ontology (TIO) v3.6.0
    url: https://www.tmforum.org/resources/introductory-guide/tr292-tm-forum-intent-ontology-tio-v3-6-0/
    type: standard
    date: 2024-08-30
    archived: research/raw/2026-09-20-tmf-intent-common-model/
  - title: ITU-T M.3351 Framework of knowledge management for telecom operation and management
    url: https://www.itu.int/epublications/publication/itu-t-m-3351-2024-08-framework-of-knowledge-management-for-telecom-operation-and-management
    type: standard
    date: 2024-08-13
    archived: research/raw/2026-09-20-itu-t-m3351/
  - title: YD/T 7007-2026 网络运营管理知识图谱技术要求 知识建模方法
    url: https://std.samr.gov.cn/hb/search/stdHBDetailed?id=5679B6F617894858E06397BE0A0AD0B8
    type: standard
    date: 2026-06-01
    archived: research/raw/2026-09-20-ccsa-huawei-ontology-spec/
related:
  - tmf-ontology-3gpp-sa5-ccsa-unified
  - knowledge-graph-for-data
  - sid
  - ontology
  - intent-common-model
  - nrm
  - data-fabric-for-ai-native-6g
tags:
  - ontology
  - SID
  - TIO
  - knowledge-graph
  - 6G
last_verified: 2026-09-20
owner: agent
---

# 电信网络本体（Telecom Network Ontology）

> 用形式语义（通常 RDF/OWL）描述电信业务、网络与运营概念及其关系，使机器可推理；不同于 UML 信息模型（SID/NRM）。

## 定义

电信网络本体是对通信网络与运营管理领域中的实体、关系、属性与约束的形式化规范。ITU-T M.3351 把 ontology modelling 定义为知识构建的第一步，并用 RDF/OWL 作为机器可处理表示 [1]。TM Forum 已发布的规范本体是 **Intent Ontology (TIO / TR292)**，为意图管理提供 RDF 词汇 [2]。CCSA YD/T 7007-2026 在行业标准层规定知识图谱的**本体模型与实例化模型**分层 [3]。

## 关键组成 / 子能力

- **顶层/联邦本体**：TMF GB1093「The Federated TM Forum Ontology」(MODA-440) 被 Community 讨论列为联邦本体，公开目录尚未挂 PDF [低]
- **意图本体**：TIO + Intent Common Model（TR290），RDF 表达目标、约束、报告
- **运营知识本体**：故障原因/现象/解决、配置/性能/告警等（M.3351、YD/T 7007）
- **资源/信息模型**：SID（GB922 UML）、3GPP NRM（TS 28.622/28.541 UML）——是实现导向的信息模型，不是 OWL 本体
- **实例知识图谱**：本体约束下的运行时三元组/属性图

## 与相邻概念的关系

- 与 [sid]：SID 提供 CSP 业务对象的 UML 类模型；本体提供可推理的开放世界语义。二者可映射，不可等同
- 与 [knowledge-graph-for-data]：本体是 schema，知识图谱是 schema + 实例
- 与 [intent-common-model]：ICM 是 TIO 中用于表达意图的核心 RDF 模型
- 与 [nrm]：NRM 是 3GPP 管理对象树，意图 MnS（TS 28.312）引用 NRM 对象类型
- 与 [data-fabric-for-ai-native-6g]：数据编织语义层需要本体作为跨域互操作契约

## 常见误解

- 「SID 就是电信本体」：SID 是 Information Framework（UML），TMF 把 ontology 一词主要用于 TIO 与正在起草的联邦本体
- 「3GPP 已经有网络本体」：SA5 有 NRM 与意图 IOC，6G 研究刚列入 Knowledge/semantic representation KI，尚无 OWL 规范
- 「华为 CCSA 本体规范」是单一文件：公开对应的是 YD/T 知识图谱系列中的知识建模分册，华为为起草单位之一

## 待深挖子题

- [ ] GB1093 联邦本体与 SID/TIO 的正式映射（会员文档）
- [ ] YD/T 7007 正文中 OWL 的规范力度（推荐 vs 强制）
- [ ] SA5 TR 32.801-01 知识架构解决方案收敛

## 来源

[1] [ITU-T M.3351](https://www.itu.int/epublications/publication/itu-t-m-3351-2024-08-framework-of-knowledge-management-for-telecom-operation-and-management) — 知识建模含 ontology + RDF/OWL
[2] [TR292 TIO v3.6.0](https://www.tmforum.org/resources/introductory-guide/tr292-tm-forum-intent-ontology-tio-v3-6-0/) — 意图管理本体
[3] [YD/T 7007-2026](https://std.samr.gov.cn/hb/search/stdHBDetailed?id=5679B6F617894858E06397BE0A0AD0B8) — 知识建模方法目录页
