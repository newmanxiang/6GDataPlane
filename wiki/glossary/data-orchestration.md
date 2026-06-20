---
term: Data Orchestration
cn: 数据编排
slug: data-orchestration
category: glossary
related:
  - data-orchestration
  - data-virtualization
  - knowledge-graph-for-data
source: https://www.getorchestra.io/guides/data-orchestration-vs-workflow-understanding-the-difference
---

# Data Orchestration

> 自动化协调和调度数据流水线中相互依赖的任务，确保数据按正确顺序可靠流转。

**中文**：数据编排
**英文**：Data Orchestration

## 定义
数据编排是对数据流水线（Data Pipeline）中提取、转换、加载、验证、发布等环节进行自动化协调与调度的技术实践。核心机制是通过有向无环图（DAG）定义任务依赖，配合调度器实现定时或事件驱动执行、故障重试和资源管理。数据编排是通用工作流编排（Workflow Orchestration）在数据领域的特化，增加了数据质量检查、Schema 演进等数据特有关注点。代表工具包括 Apache Airflow、Dagster、Prefect、Databricks Workflows 等。

## 相关概念
- [[data-orchestration]] 数据编排的完整概念卡片，含与工作流编排的区分
- [[data-virtualization]] 编排管理"搬运与加工"，虚拟化实现"不搬运即访问"
- [[knowledge-graph-for-data]] 图谱中的血缘信息可自动驱动编排 DAG 生成
