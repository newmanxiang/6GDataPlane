---
title: 数据编织核心能力域
title_en: Data Fabric Core Capabilities
slug: data-fabric-capabilities
category: concept
status: draft
confidence: low
sources:
  - https://www.ibm.com/think/topics/data-fabric
  - https://www.denodo.com/en/glossary/data-fabric-definition-benefits-key-components
  - https://www.qlik.com/us/data-management/data-fabric
related:
  - data-fabric-definition
  - active-metadata
  - data-fabric-vs-data-mesh
tags:
  - data-fabric
  - capabilities
  - metadata
  - knowledge-graph
  - data-virtualization
last_verified: 2026-06-20
owner: agent
---

# 数据编织核心能力域（Data Fabric Core Capabilities）

> 数据编织的核心能力包括主动元数据激活、知识图谱、AI/ML增强、数据虚拟化、自动数据集成、数据编排以及隐私与治理七大领域。

## 定义

数据编织不是单一技术，而是一组协同工作的能力域。IBM 将其定义为利用主动元数据（结合知识图谱、语义和AI）实时组织数据资产的架构 [1]。Denodo 强调通过元数据激活减少人工干预、加速数据工程工作流 [2]。

## 关键组成 / 子能力

### 1. 主动元数据激活（Active Metadata Activation）
将被动的元数据目录转变为主动的决策引擎，持续采集、分析并利用元数据驱动自动化操作。详见 [[active-metadata]]。

### 2. 知识图谱（Knowledge Graph）
以图结构表达数据资产间的语义关系，提供数据血缘、业务上下文和影响分析能力 [1]。

### 3. AI/ML 增强（AI/ML Augmentation）
利用机器学习自动发现数据模式、推荐集成路径、检测数据质量异常，减少人工数据工程工作量 [2]。

### 4. 数据虚拟化（Data Virtualization）
在不移动数据的前提下，跨多个异构数据源提供统一的逻辑访问层，支持实时联邦查询 [2]。

### 5. 自动数据集成（Automated Data Integration）
基于元数据分析自动生成 ETL/ELT 管道，适配不同数据格式和协议 [3]。

### 6. 数据编排（Data Orchestration）
协调数据在不同处理阶段和系统之间的流转，确保数据管道的可靠性和时效性。

### 7. 隐私与治理（Privacy & Governance）
嵌入式数据治理策略执行，包括访问控制、数据分类、合规审计和隐私保护（如数据脱敏、差分隐私）。

## 与相邻概念的关系

- 与 [[data-fabric-definition]]：能力域是数据编织定义的具体技术落地
- 与 [[active-metadata]]：主动元数据是贯穿所有能力域的核心引擎
- 与 [[data-fabric-vs-data-mesh]]：数据编织能力域可为数据网格提供底层技术基础设施

## 常见误解

- **误解：所有能力必须同时具备**。实际上组织可以根据成熟度分阶段构建，通常从元数据管理和数据虚拟化开始
- **误解：知识图谱是可选组件**。Gartner 明确将知识图谱列为数据编织的必要核心，而非可选增强

## 待深挖子题

- [ ] 各能力域的技术成熟度评估（Gartner Hype Cycle 对照） → 加入 ops/deep-dive-queue.md
- [ ] 数据虚拟化 vs 数据物化（Materialization）的性能权衡 → 加入 ops/deep-dive-queue.md
- [ ] 隐私增强技术（PETs）在数据编织中的集成模式 → 加入 ops/deep-dive-queue.md

## 来源

[1] [What Is a Data Fabric?](https://www.ibm.com/think/topics/data-fabric) — IBM Think 综述
[2] [Data Fabric: Definition, Benefits, and Key Components](https://www.denodo.com/en/glossary/data-fabric-definition-benefits-key-components) — Denodo 术语定义
[3] [What is Data Fabric? Why You Need It & Best Practices](https://www.qlik.com/us/data-management/data-fabric) — Qlik 最佳实践指南
