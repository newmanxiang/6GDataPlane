---
title: 数据编排
title_en: Data Orchestration
slug: data-orchestration
category: concept
status: draft
confidence: low
sources:
  - https://www.getorchestra.io/guides/data-orchestration-vs-workflow-understanding-the-difference
  - https://www.databricks.com/product/data-engineering/lakeflow-jobs
  - https://branchboston.com/workflow-orchestration-vs-traditional-job-scheduling-in-data-pipelines/
related:
  - data-virtualization
  - knowledge-graph-for-data
  - network-data-analytics
tags:
  - 数据编排
  - 数据流水线
  - 工作流调度
  - 自动化
last_verified: 2026-06-20
owner: agent
---

# 数据编排（Data Orchestration）

> 自动化协调、调度和管理数据流水线中相互依赖的任务，确保数据从源到消费端按正确顺序可靠流转。

## 定义
数据编排是指对数据流水线（Data Pipeline）中的提取、转换、加载、验证、发布等环节进行自动化协调与调度的技术实践。它专注于数据生命周期的端到端管理——定义任务依赖关系（DAG）、监控执行状态、处理失败重试、管理资源分配，使数据按业务 SLA 可靠交付。数据编排区别于通用工作流编排（Workflow Orchestration）：后者覆盖任意业务流程（审批、DevOps、微服务调用等），前者专注于数据流水线场景 [1][2]。

## 关键组成 / 子能力
- **DAG 定义与管理**：以有向无环图（DAG）声明任务间的依赖关系和执行顺序，支持代码化（如 Airflow Python DSL）或可视化编排
- **调度与触发**：支持 cron 定时调度、事件驱动（数据到达触发）、手动触发等多种模式
- **执行引擎**：跨环境（本地、云、Kubernetes）分发任务，管理并行度、资源配额和计算隔离
- **可观测性**：实时任务状态监控、日志聚合、血缘可视化、SLA 告警
- **故障处理**：自动重试、断点续跑、失败通知和回退策略

## 与相邻概念的关系
- 与 [data-virtualization]：数据编排管理数据的"搬运与加工"（批处理 ETL/ELT），数据虚拟化实现"不搬运即访问"（实时查询联邦）；两者在数据编织架构中互补
- 与 [knowledge-graph-for-data]：知识图谱中的数据血缘和依赖关系可自动生成编排 DAG，减少手工定义成本
- 与通用工作流编排：数据编排是工作流编排在数据领域的特化——增加了数据质量检查、Schema 演进、数据版本管理等数据特有关注点 [1]

## 常见误解
- **"数据编排就是 cron 定时任务"**：传统 cron 仅支持时间触发且缺乏依赖管理；现代编排引擎支持复杂 DAG、事件驱动、动态参数化和跨系统协调
- **"数据编排 = 工作流编排"**：数据编排是工作流编排的子集/特化，专注数据流水线的端到端生命周期管理，包含数据质量、Schema 验证等数据特有功能 [1]

## 待深挖子题
- [ ] 主流数据编排引擎对比（Apache Airflow / Dagster / Prefect / Databricks Workflows） → 加入 ops/deep-dive-queue.md
- [ ] 数据编排在 6G 网络数据面中的角色——跨域数据流水线自动调度
- [ ] 事件驱动编排（Event-driven Orchestration）与流式数据管道的融合趋势

## 来源
[1] [Data Orchestration vs Workflow: Understanding the Difference](https://www.getorchestra.io/guides/data-orchestration-vs-workflow-understanding-the-difference) — Orchestra，数据编排与工作流编排的区别解析
[2] [Lakeflow Jobs - Databricks](https://www.databricks.com/product/data-engineering/lakeflow-jobs) — Databricks 数据编排产品，含编排定义
[3] [Workflow Orchestration vs Traditional Job Scheduling](https://branchboston.com/workflow-orchestration-vs-traditional-job-scheduling-in-data-pipelines/) — 工作流编排与传统调度的对比分析
