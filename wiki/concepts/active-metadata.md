---
title: 主动元数据
title_en: Active Metadata
slug: active-metadata
category: concept
status: draft
confidence: low
sources:
  - https://atlan.com/active-metadata-101/
  - https://bigid.com/blog/what-is-active-metadata/
  - https://promethium.ai/guides/active-vs-passive-metadata-management-guide/
related:
  - data-fabric-definition
  - data-fabric-capabilities
  - data-fabric-vs-data-mesh
tags:
  - metadata
  - active-metadata
  - AI
  - automation
  - data-governance
last_verified: 2026-06-20
owner: agent
---

# 主动元数据（Active Metadata）

> 主动元数据是经 AI/ML 增强的元数据，能实时感知变化、理解影响、自动触发操作，区别于仅用于记录和查询的被动元数据。

## 定义

主动元数据是经机器学习增强的元数据，可用于自动执行操作或做出基于元数据的决策 [2]。其"主动"体现在：被动元数据在数据出问题后才告知变化，而主动元数据能检测变化、通过血缘理解影响范围、并自动触发修复或告警 [1]。

核心区别：**被动元数据描述数据"是什么"（结构、定义、归属），主动元数据描述数据"做什么"（行为、流转、使用模式）** [3]。

## 关键组成 / 子能力

- **实时元数据采集**：从数据管道、查询日志、API调用等多源持续采集运行时元数据
- **元数据分析与推理**：利用 ML 发现数据使用模式、异常检测、血缘追踪
- **自动触发与编排**：基于元数据变化自动触发数据质量检查、治理策略执行、管道编排
- **上下文推荐**：根据用户行为和数据关系向数据消费者推荐相关数据集
- **影响分析**：变更发生时自动评估下游影响范围

## 与相邻概念的关系

- 与 [[data-fabric-capabilities]]：主动元数据是数据编织七大能力域中的核心引擎，驱动其他能力的智能化
- 与 [[data-fabric-definition]]：Gartner 将主动元数据列为数据编织区别于传统数据集成方案的关键特征
- 与数据目录（Data Catalog）：传统数据目录是被动元数据的载体，主动元数据将其升级为智能决策中枢

## 常见误解

- **误解：主动元数据只是给数据目录加了搜索功能**。实际上它的核心价值在于"驱动行动"——自动编排管道、执行治理策略、触发告警，而非仅仅改善发现能力
- **误解：主动元数据需要全新基础设施**。实际上它通常通过在现有元数据存储上叠加 ML 分析层和事件驱动层来实现

## 待深挖子题

- [ ] 主动元数据的技术实现架构（事件驱动 vs 轮询式） → 加入 ops/deep-dive-queue.md
- [ ] 主动元数据在数据质量自动修复中的应用案例 → 加入 ops/deep-dive-queue.md
- [ ] 6G 数据面中元数据的实时性要求与主动元数据的适配性 → 加入 ops/deep-dive-queue.md

## 来源

[1] [Active Metadata: The Complete 2026 Guide](https://atlan.com/active-metadata-101/) — Atlan 主动元数据完整指南
[2] [Active Metadata: Definition, Benefits, and More](https://bigid.com/blog/what-is-active-metadata/) — BigID 定义与收益分析
[3] [Active vs Passive Metadata Management: Guide for Data Teams](https://promethium.ai/guides/active-vs-passive-metadata-management-guide/) — Promethium 主被动元数据对比
