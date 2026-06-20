---
title: 6G 数据面
title_en: 6G Data Plane
slug: 6g-data-plane
category: concept
status: draft
confidence: low
sources:
  - https://www.huawei.com/en/huaweitech/future-technologies/data-plane-design-ai-native-6g-networks
  - https://hexa-x-ii.eu/wp-content/uploads/2024/02/6G-Mobile-Network-Evolves-from-CommaaS-to-XaaS-V1.pdf
  - https://www.qualcomm.com/news/onq/2024/03/6g-foundry-rethinking-the-control-plane
related:
  - 6g-overview
  - user-plane-evolution
  - ai-native-air-interface
  - network-data-analytics
  - data-fabric-definition
tags:
  - 6G
  - 数据面
  - DaaS
  - 架构
last_verified: 2026-06-20
owner: agent
---

# 6G 数据面（6G Data Plane）

> 6G 数据面是 6G 网络架构中独立于控制面、智能面、计算面的功能平面，负责数据的采集、传输、存储与服务化供给（DaaS）。

## 定义

6G 数据面（Data Plane）是在传统用户面基础上扩展的新型功能平面。华为提出将其作为 AI 原生 6G 架构的独立组成部分，引入"数据即服务"（DaaS）概念 [1]。Hexa-X-II 项目指出，6G 将在 5G 通信面基础上新增数据面、智能面、计算面和安全面 [2]。

## 关键组成 / 子能力

- **数据采集与汇聚**：端到端数据收集（传感、AI 训练数据、网络遥测）
- **数据传输与转发**：高效用户面数据包转发，支持多样化 QoS
- **数据存储与缓存**：边缘/核心网数据暂存与分布式缓存
- **数据即服务（DaaS）**：向上层应用和 AI 功能提供标准化数据访问接口
- **数据编排与治理**：数据生命周期管理、隐私保护、数据质量保障

## 与相邻概念的关系

- 与 **控制面（Control Plane）**：控制面负责信令与连接管理，数据面负责实际数据承载；Qualcomm 提出 6G 采用"用户面优先"设计，控制面精简化 [3]
- 与 **智能面（Intelligence Plane）**：智能面提供 AI 模型训练/推理/决策服务，数据面为其供给训练数据和推理输入
- 与 **计算面（Computing Plane）**：计算面提供分布式算力，数据面提供计算所需的数据流
- 与 [[data-fabric-definition]]：数据编织是实现 6G 数据面中数据集成与编排能力的潜在技术路径

## 常见误解

- **误解 1**："数据面 = 用户面"——6G 数据面的范畴已超越传统用户面（仅做包转发），增加了数据服务化、数据治理等新职能
- **误解 2**："数据面是已确定的标准"——目前数据面概念仍处于产业研究阶段，3GPP SA2 正在讨论 6G 数据框架（WT#5），尚未标准化

## 待深挖子题

- [ ] 3GPP SA2 6G 数据框架工作项（WT#5）进展跟踪 → 加入 ops/deep-dive-queue.md
- [ ] DaaS 接口设计：数据面如何向智能面暴露数据服务
- [ ] 数据面与数据编织（Data Fabric）技术的映射关系

## 来源

[1] [Data Plane Design for AI-Native 6G Networks](https://www.huawei.com/en/huaweitech/future-technologies/data-plane-design-ai-native-6g-networks) — 华为技术白皮书，2025 年 2 月
[2] [6G Mobile Network: Evolves from CommaaS to XaaS](https://hexa-x-ii.eu/wp-content/uploads/2024/02/6G-Mobile-Network-Evolves-from-CommaaS-to-XaaS-V1.pdf) — Hexa-X-II 欧盟项目白皮书
[3] [6G foundry: Rethinking the control plane](https://www.qualcomm.com/news/onq/2024/03/6g-foundry-rethinking-the-control-plane) — Qualcomm 技术博客
