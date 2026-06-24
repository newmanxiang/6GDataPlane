---
title: 数据知识图谱
title_en: Knowledge Graph for Data Management
slug: knowledge-graph-for-data
category: concept
status: draft
confidence: low
sources:
  - https://graphwise.ai/blog/how-knowledge-graphs-power-data-mesh-and-data-fabric/
  - https://www.topquadrant.com/resources/knowledge-graphs-are-key-to-data-fabric/
  - https://www.ontotext.com/knowledgehub/fundamentals/what-is-a-semantic-layer/
related:
  - data-virtualization
  - data-orchestration
  - network-data-analytics
  - data-fabric-definition-and-capabilities
tags:
  - 知识图谱
  - 数据编织
  - 语义层
  - 元数据管理
last_verified: 2026-06-20
owner: agent
---

# 数据知识图谱（Knowledge Graph for Data Management）

> 以图结构建模数据资产间语义关系，为数据编织（Data Fabric）提供自动化数据发现与治理的核心语义层。

## 定义
数据知识图谱是将组织内数据资产（表、字段、指标、数据流水线等）及其语义关系以图谱形式建模和管理的技术。它区别于通用知识图谱（如 Wikidata），专注于数据管理领域——通过本体和元数据构建语义层（Semantic Layer），实现跨源数据的自动发现、血缘追踪和智能推荐 [1][2]。

## 关键组成 / 子能力
- **语义层建模**：基于本体（Ontology）将业务概念映射为图节点与关系，使数据消费者以业务语言而非技术术语查询数据 [3]
- **自动化数据发现**：利用图遍历和推理自动发现数据资产间的隐含关系（如来源-派生、同义字段、质量依赖）
- **数据血缘追踪**：在图谱中记录数据从源到终端报表的完整流转路径，支持影响分析与合规审计
- **主动元数据管理**：通过主动元数据（Active Metadata）持续采集、关联和更新元数据图谱，驱动自动化治理策略
- **跨域数据联邦**：作为数据编织架构的"粘合剂"，统一描述分布在数据湖、数据仓库、API 等异构源中的数据资产

## 与相邻概念的关系
- 与 [data-virtualization]：数据知识图谱提供"应该查什么"的语义层，数据虚拟化提供"如何查"的统一访问层；两者共同构成数据编织的核心组件
- 与 [data-orchestration]：图谱中的血缘和依赖关系可驱动编排引擎自动生成和优化数据流水线的执行顺序
- 与 [network-data-analytics]：6G 网络数据面的知识图谱可建模网络功能、数据流、分析模型间的关系，支持 NWDAF 的智能数据路由

## 常见误解
- **"数据知识图谱 = 通用知识图谱"**：数据 KG 聚焦元数据和数据资产关系建模，而非百科式实体知识；其核心价值在于数据治理而非问答
- **"有了数据目录就不需要知识图谱"**：传统数据目录是扁平列表，缺乏关系推理能力；知识图谱能自动推断隐含关联并支持复杂查询

## 待深挖子题
- [ ] 数据知识图谱在 6G 网络数据编织中的具体应用场景 → 加入 ops/deep-dive-queue.md
- [ ] 主动元数据（Active Metadata）引擎与知识图谱的集成模式
- [ ] 开源数据知识图谱工具链（Apache Atlas、Amundsen、DataHub）的能力对比

## 来源
[1] [How Knowledge Graphs Power Data Mesh and Data Fabric](https://graphwise.ai/blog/how-knowledge-graphs-power-data-mesh-and-data-fabric/) — Graphwise 博文，阐述 KG 在 Data Fabric/Mesh 中的核心角色
[2] [Knowledge Graphs are Key to Data Fabric](https://www.topquadrant.com/resources/knowledge-graphs-are-key-to-data-fabric/) — TopQuadrant，知识图谱作为数据编织关键技术的分析
[3] [What Is a Semantic Layer](https://www.ontotext.com/knowledgehub/fundamentals/what-is-a-semantic-layer/) — Ontotext，知识图谱驱动的语义层基础概念
