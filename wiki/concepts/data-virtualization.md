---
title: 数据虚拟化
title_en: Data Virtualization
slug: data-virtualization
category: concept
status: draft
confidence: low
sources:
  - https://www.denodo.com/en/data-management/data-virtualization
  - https://www.gartner.com/reviews/market/data-virtualization
  - https://www.datamanagementblog.com/beware-of-straw-man-stories-clearing-up-misconceptions-about-data-virtualization/
related:
  - knowledge-graph-for-data
  - data-orchestration
  - 6g-data-plane
  - edge-data-fabric
tags:
  - 数据虚拟化
  - 数据集成
  - 逻辑数据层
  - 数据编织
last_verified: 2026-06-20
owner: agent
---

# 数据虚拟化（Data Virtualization）

> 在不物理搬运数据的前提下，通过统一逻辑访问层实现多源异构数据的实时集成与交付。

## 定义
数据虚拟化是一种数据集成方法，通过建立统一的逻辑数据访问层，将分散在数据库、数据湖、云存储、API 等异构源中的数据以虚拟视图方式暴露给消费者——数据保留在原始位置，不进行物理复制或搬运。与传统 ETL（Extract-Transform-Load）的核心区别在于：ETL 将数据物理复制到目标仓库后再使用，而数据虚拟化在查询时实时联邦和转换 [1][2]。

## 关键组成 / 子能力
- **连接器层**：提供对关系型数据库、NoSQL、Hadoop/Spark、SaaS API、文件系统等数百种数据源的统一连接
- **查询联邦引擎**：将用户 SQL/API 查询分解为子查询下推至各源执行，汇总结果并返回——实现跨源 JOIN
- **语义抽象层**：将底层物理模式映射为面向业务的逻辑模型，屏蔽技术细节
- **查询优化与缓存**：智能查询优化器（Cost-based Optimizer）选择最优执行计划，结合缓存层提升重复查询性能
- **数据治理集成**：内置数据血缘、访问控制、行列级安全策略，满足合规需求

## 与相邻概念的关系
- 与 [knowledge-graph-for-data]：知识图谱提供语义发现能力（"数据在哪里、什么含义"），数据虚拟化提供统一访问能力（"如何高效获取"）；两者是数据编织架构的互补支柱
- 与 [data-orchestration]：数据编排管理批量数据流水线的调度与执行，数据虚拟化侧重实时查询联邦；前者适合批处理 ETL 场景，后者适合即席查询与实时分析
- 与 [6g-data-plane]：6G 数据面可借鉴数据虚拟化思想，实现对来自 RAN、核心网、边缘的数据无需搬运即可跨域查询

## 常见误解
- **"数据虚拟化会取代 ETL"**：两者互补而非替代——高频批量数据落盘场景仍需 ETL，虚拟化适合实时查询、快速原型和减少数据冗余 [3]
- **"虚拟化性能一定差"**：现代虚拟化平台通过查询下推、智能缓存和并行执行，性能可达到或接近物化视图水平

## 待深挖子题
- [ ] 数据虚拟化在 6G 跨域数据面中的架构适配 → 加入 ops/deep-dive-queue.md
- [ ] Denodo / Dremio / Trino 等主流平台能力对比
- [ ] 数据虚拟化与数据网格（Data Mesh）的结合模式

## 来源
[1] [What is Data Virtualization?](https://www.denodo.com/en/data-management/data-virtualization) — Denodo 官方定义，业界领先虚拟化厂商
[2] [Best Data Virtualization Reviews 2026](https://www.gartner.com/reviews/market/data-virtualization) — Gartner Peer Insights 数据虚拟化市场评价
[3] [Clearing up Misconceptions about Data Virtualization](https://www.datamanagementblog.com/beware-of-straw-man-stories-clearing-up-misconceptions-about-data-virtualization/) — 数据管理博客，澄清虚拟化常见误解
