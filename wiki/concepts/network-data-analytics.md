---
title: 网络数据分析功能
title_en: Network Data Analytics Function
slug: network-data-analytics
category: concept
status: draft
confidence: low
sources:
  - https://arxiv.org/html/2506.04860v1
  - https://www.3gpp.org/technologies/nae-5gs-ct3
  - https://www.ericsson.com/en/core-network/5g-core/network-data-analytics-function
related:
  - 6g-data-plane
  - ai-native-air-interface
  - ran-architecture-evolution
tags:
  - NWDAF
  - 3GPP
  - 数据分析
  - 5G
  - 6G
last_verified: 2026-06-20
owner: agent
---

# 网络数据分析功能（Network Data Analytics Function）

> 3GPP 定义的网络自动化分析框架，从 5G NWDAF 演进至 6G 的分布式智能数据分析体系。

## 定义
网络数据分析功能（NWDAF）是 3GPP 在 5G 系统架构（TS 23.288）中定义的网络功能，负责采集、关联和分析来自核心网与 RAN 的数据，输出分析结果与预测以支持网络自动化决策。NWDAF 从 Rel-15 引入概念，在 Rel-16/17 逐步完善分析能力与 ML 框架，Rel-18 增加联邦学习等增强功能。面向 6G，该功能预计将向分布式、跨域、AI 原生的数据分析体系演进 [1][2]。

## 关键组成 / 子能力
- **数据采集**：通过 Nnwdaf 服务化接口从 AMF、SMF、PCF、UPF、OAM 等采集网络事件与性能数据
- **分析与推理**：提供标准化分析 ID（如异常检测、负载预测、QoS 可持续性评估、用户数据拥塞分析等）
- **ML 模型生命周期管理**：Rel-17 引入 MTLF（模型训练逻辑功能）与 AnLF（分析逻辑功能）的功能分离
- **联邦学习支持**：Rel-18 增加跨 NWDAF 实例的联邦学习框架，支持数据不出域的协同训练
- **6G 演进方向**：从集中式单节点向边缘分布式部署演进，与 RAN 数据分析（RIC）深度协同

## 与相邻概念的关系
- 与 [6g-data-plane]：NWDAF 是数据面数据的核心消费者，其分析结果又反馈驱动数据面的路径优化与 QoS 调整
- 与 [ai-native-air-interface]：空口 AI 模型产生的 CSI/波束数据是 NWDAF 分析的重要输入；NWDAF 的预测输出可指导空口资源分配
- 与 [ran-architecture-evolution]：NWDAF 与 O-RAN RIC 的分析能力存在互补与重叠，6G 需要统一的跨域分析框架

## 常见误解
- **"NWDAF 只做统计报表"**：NWDAF 从 Rel-17 起已具备 ML 推理能力，可输出预测类分析（如网络切片负载预测）
- **"NWDAF 与 RIC 功能重复"**：两者侧重不同——NWDAF 面向核心网维度分析，RIC 面向 RAN 维度优化，6G 趋向整合

## 待深挖子题
- [ ] NWDAF Rel-18/19 新增分析用例与 ML 增强特性 → 加入 ops/deep-dive-queue.md
- [ ] 6G 分布式数据分析架构设计（NWDAF + RIC 融合方案）
- [ ] NWDAF 与数据编织（Data Fabric）的集成路径

## 来源
[1] [Towards Network Data Analytics in 5G Systems and Beyond](https://arxiv.org/html/2506.04860v1) — arXiv 综述论文，全面梳理 NWDAF 演进
[2] [Network Automation Enablers in 5GS](https://www.3gpp.org/technologies/nae-5gs-ct3) — 3GPP 官方页面，网络自动化使能技术概述
[3] [5G Network Data Analytics Function](https://www.ericsson.com/en/core-network/5g-core/network-data-analytics-function) — Ericsson NWDAF 产品介绍
