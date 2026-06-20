---
term: Data Virtualization
cn: 数据虚拟化
slug: data-virtualization
category: glossary
related:
  - data-virtualization
  - knowledge-graph-for-data
  - data-orchestration
source: https://www.denodo.com/en/data-management/data-virtualization
---

# Data Virtualization

> 通过统一逻辑访问层在不搬运数据的前提下实现多源异构数据的实时集成与查询。

**中文**：数据虚拟化
**英文**：Data Virtualization

## 定义
数据虚拟化通过建立统一的逻辑数据访问层，将分散在数据库、数据湖、云存储、API 等异构源中的数据以虚拟视图方式暴露给消费者。数据保留在原始位置，不进行物理复制或搬运——查询时实时联邦和转换。与 ETL 的核心区别：ETL 将数据物理复制到目标仓库后使用，虚拟化在查询时实时拉取和整合。代表厂商包括 Denodo、Dremio、Trino 等。

## 相关概念
- [[data-virtualization]] 数据虚拟化的完整概念卡片，含与 ETL 的对比
- [[knowledge-graph-for-data]] 知识图谱提供语义发现，虚拟化提供统一访问
- [[data-orchestration]] 编排管理批处理流水线，虚拟化侧重实时查询联邦
