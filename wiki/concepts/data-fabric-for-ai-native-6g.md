---
title: 服务 AI 原生 6G 的数据编织
title_en: Data Fabric for AI-Native 6G
slug: data-fabric-for-ai-native-6g
category: concept
status: stub
confidence: medium
sources:
  - https://www.ericsson.com/en/reports-and-papers/white-papers/6g-connectivity-and-beyond-for-the-2030s
  - https://www.nokia.com/blog/ai-native-6g-is-now-the-industry-direction/
  - https://www.sciencedirect.com/science/article/pii/S2095809925005673
  - https://www.list.lu/media-event/news/news-detail/cybersecurity-and-6g-the-challenge-of-ultra-distributed-systems
related:
  - data-fabric-definition
  - data-fabric-capabilities
  - 6g-data-plane
  - ai-native-air-interface
  - network-data-analytics
  - data-fabric-in-telecom
  - active-metadata
  - digital-twin-network
  - data-fabric-definition-and-capabilities
tags:
  - 数据编织
  - AI原生
  - 6G
  - 数据基础设施
  - 前沿议题
last_verified: 2026-06-20
owner: agent
---

# 服务 AI 原生 6G 的数据编织（Data Fabric for AI-Native 6G）

> 为 AI 原生 6G 网络提供统一、智能、实时的数据管理基础设施，使网络 AI 能在任意层级获取所需训练与推理数据。

## 定义
AI 原生 6G 要求网络在设计之初就将 AI/ML 嵌入各层（空口、RAN、Core、管理面），这对数据的实时采集、跨域流通与质量保障提出前所未有的要求。数据编织架构通过主动元数据、知识图谱与自动化数据编排，为分布式 AI 智能体提供"随需即得"的数据服务。Ericsson 将 6G 定位为"AI 原生智能织物（AI-native intelligent fabric）"[1]，Nokia 强调 AI 原生网络织物是 6G 基础 [2]。**注：目前尚无直接以"Data Fabric for AI-Native 6G"为题的标准或论文，本概念属开拓性交叉议题，文献稀缺。**

## 关键组成 / 子能力
- **实时数据采集与流水线**：支持空口 AI 训练所需的无损数据采集（参见 [3] 提出的 6G 实时数据采集方法）
- **跨层数据编排**：从物理层、MAC 层到应用层的垂直数据贯通
- **AI 模型生命周期数据管理**：训练数据版本化、推理数据缓存、模型漂移检测数据
- **联邦化数据治理**：支持网络 AI 在隐私合规下的跨域数据共享
- **零接触自动化数据供给**：意图驱动的数据发现与自动配送

## 与相邻概念的关系
- 与 [[6g-data-plane]]：数据面是产生与传输数据的管道，数据编织是管理与编排数据的智能层
- 与 [[ai-native-air-interface]]：AI 原生空口的模型训练高度依赖数据编织提供的高质量标注数据
- 与 [[data-fabric-in-telecom]]：后者解决运营域数据统一，本概念将数据编织扩展至网络内部 AI 闭环
- 与 [[network-data-analytics]]：NWDAF 可视为 5G 时代的初步尝试，6G 数据编织是其全面升级
- 与 [[active-metadata]]：主动元数据是实现网络数据自动分类与路由的核心技术

## 常见误解
- **误解1**：6G AI 原生只需要更大的算力，数据管理不是瓶颈。实际上数据质量、时效性和可达性是 AI 模型性能的决定因素
- **误解2**：现有 5G NWDAF 足以支撑 6G AI 需求。NWDAF 仅覆盖核心网分析，6G 需要端到端跨域数据编织

## 详细 Topic 卡片

> 本概念的完整深调已完成，详见 [[data-fabric-for-ai-native-6g]]（wiki/topics/data-fabric-for-ai-native-6g.md）。

## 待深挖子题
- [ ] 6G AI 原生架构中数据面与智能面（AI Plane）的接口定义 → 加入 ops/deep-dive-queue.md
- [ ] 空口 AI 模型训练的数据采集时延与吞吐量要求
- [ ] 网络数字孪生所需的数据编织能力（实时同步、多保真度）
- [ ] ETSI ZSM GS 029 Data Management Agent 规范正文跟踪
- [ ] 意图驱动的网络数据编排（Intent-Based Data Orchestration）设计模式

## 来源
[1] [6G – connectivity and beyond for the 2030's - Ericsson](https://www.ericsson.com/en/reports-and-papers/white-papers/6g-connectivity-and-beyond-for-the-2030s) — Ericsson 6G 白皮书，提出 AI-native intelligent fabric 概念
[2] [AI-native 6G is now the industry direction - Nokia](https://www.nokia.com/blog/ai-native-6g-is-now-the-industry-direction/) — Nokia 博客，阐述 AI 原生网络织物作为 6G 基础
[3] [A Task-Driven Design Approach for 6G AI-Native Architecture - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2095809925005673) — 学术论文，提出 6G AI 原生架构的任务驱动设计方法
[4] [Cybersecurity and 6G - LIST](https://www.list.lu/media-event/news/news-detail/cybersecurity-and-6g-the-challenge-of-ultra-distributed-systems) — 指出 6G 将是前所未有密度的数据基础设施
