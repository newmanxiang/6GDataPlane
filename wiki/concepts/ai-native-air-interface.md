---
title: AI 原生空口
title_en: AI-Native Air Interface
slug: ai-native-air-interface
category: concept
status: draft
confidence: low
sources:
  - https://techblog.comsoc.org/2026/01/15/comparing-ai-native-mode-in-6g-imt-2030-vs-ai-overlay-add-on-status-in-5g-imt-2020/
  - https://www.huawei.com/en/huaweitech/future-technologies/data-plane-design-ai-native-6g-networks
  - https://www.telecomhall.net/t/6g-and-the-rise-of-the-ai-native-air-interface/34681
related:
  - 6g-data-plane
  - ran-architecture-evolution
  - network-data-analytics
tags:
  - 6G
  - AI
  - 空口
  - 数据面
last_verified: 2026-06-20
owner: agent
---

# AI 原生空口（AI-Native Air Interface）

> 将 AI/ML 作为 6G 无线空中接口（物理层与 MAC 层）的原生设计要素，而非 5G 时代的外挂附加模块。

## 定义
AI 原生空口是 6G 无线接入系统中，将 AI/ML 算法深度嵌入物理层信道编解码、波束管理、资源调度等核心功能的设计范式。与 5G 的"AI 叠加"（overlay/add-on）模式不同，6G 将 AI 视为空口协议栈的一等公民，从架构层面原生支持模型训练、推理与更新 [1][2]。

## 关键组成 / 子能力
- **AI 驱动的信道估计与编解码**：用神经网络替代传统 LDPC/Polar 编码的部分或全部流水线
- **端到端学习的收发机**：发射端与接收端联合优化，打破传统模块化设计边界
- **AI 辅助波束管理**：利用环境感知与预测模型实现低开销波束跟踪
- **自适应资源调度**：基于实时推理的动态频谱分配与功率控制
- **数据面交互**：空口 AI 模型的训练数据采集、模型分发与推理结果回传均依赖数据面承载 [2]

## 与相邻概念的关系
- 与 [6g-data-plane]：AI 原生空口是数据面的关键"数据生产者"与"数据消费者"——空口产生大量信道状态信息（CSI）等训练数据，同时依赖数据面分发模型与推理策略
- 与 [ran-architecture-evolution]：AI 原生空口的落地依赖 O-RAN/AI-RAN 的开放架构，RIC 提供模型生命周期管理
- 与 [network-data-analytics]：空口产生的数据是 NWDAF/6G 数据分析功能的重要数据源

## 常见误解
- **"AI 原生 = 全部用 AI 替代"**：实际上是 AI 与传统算法的混合架构，仅在 AI 有明确增益的环节替代传统方案
- **"5G 已经是 AI 原生"**：5G 的 AI 应用（如 RIC 上的 xApp）属于叠加模式，未改变空口协议栈本身的设计

## 待深挖子题
- [ ] AI 原生空口的标准化进展（3GPP Rel-19/20 AI/ML for NR Air Interface） → 加入 ops/deep-dive-queue.md
- [ ] 端到端学习收发机的数据需求与数据面承载方案
- [ ] AI 模型在空口的在线训练 vs 离线训练的数据流架构

## 来源
[1] [Comparing AI Native mode in 6G vs AI Overlay in 5G](https://techblog.comsoc.org/2026/01/15/comparing-ai-native-mode-in-6g-imt-2030-vs-ai-overlay-add-on-status-in-5g-imt-2020/) — IEEE ComSoc 技术博客，对比 6G AI 原生与 5G AI 叠加模式
[2] [Data Plane Design for AI-Native 6G Networks](https://www.huawei.com/en/huaweitech/future-technologies/data-plane-design-ai-native-6g-networks) — 华为技术白皮书，提出 AI 原生 6G 网络的数据面设计方案
[3] [6G and the Rise of the AI-Native Air Interface](https://www.telecomhall.net/t/6g-and-the-rise-of-the-ai-native-air-interface/34681) — telecomHall 技术论坛综述
