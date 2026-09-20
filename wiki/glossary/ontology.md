---
term_zh: 本体
term_en: Ontology
abbr: —
slug: ontology
category: term
sources:
  - title: ITU-T M.3351
    url: https://www.itu.int/epublications/publication/itu-t-m-3351-2024-08-framework-of-knowledge-management-for-telecom-operation-and-management
  - title: TR292 TM Forum Intent Ontology
    url: https://www.tmforum.org/resources/introductory-guide/tr292-tm-forum-intent-ontology-tio-v3-6-0/
related:
  - telecom-network-ontology
  - knowledge-graph
  - sid
  - intent-common-model
tags: [ontology, RDF, OWL, SHACL]
---

# 本体（Ontology）

**一句话定义**：对某一领域中概念、关系与约束的形式化规范，常用 RDF/RDFS/OWL 表达，并用 SHACL 做形状约束，使机器可共享词汇并做有限推理。

**来源**：[ITU-T M.3351 §8.2.3.2](https://www.itu.int/epublications/publication/itu-t-m-3351-2024-08-framework-of-knowledge-management-for-telecom-operation-and-management)；[TR292 TIO](https://www.tmforum.org/resources/introductory-guide/tr292-tm-forum-intent-ontology-tio-v3-6-0/)

**相关概念**：
- [telecom-network-ontology] 电信领域应用
- [knowledge-graph] 本体 + 实例
- [sid] UML 信息模型，常被误称为本体

**易混淆点**：
- 与信息模型：信息模型（SID/NRM）面向实现与接口，封闭世界；本体面向共享语义与推理，开放世界
- OWL / RDF / SHACL：RDF 是图数据模型，OWL 是本体语言，SHACL 是约束/校验语言

**首次出现于本工程**：2026-09-20，wiki/concepts/telecom-network-ontology.md
