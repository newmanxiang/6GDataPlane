---
title: RAN 架构演进
title_en: RAN Architecture Evolution
slug: ran-architecture-evolution
category: concept
status: draft
confidence: low
sources:
  - https://mediastorage.o-ran.org/ngrg-rr/nGRG-RR-2024-01-O-RAN%20Cloud%20Friendly%20Future%206G%20RAN-v1.2.1.pdf
  - https://dl.acm.org/doi/10.1145/3636534.3701550
  - https://ai-ran.org/
  - https://www.softbank.jp/corp/set/data/technology/research/story-event/Whitepaper_Download_Location/pdf/SoftBank_AI_RAN_Whitepaper_December2024.pdf
related:
  - ai-native-air-interface
  - 6g-data-plane
  - network-data-analytics
tags:
  - O-RAN
  - Cloud RAN
  - AI-RAN
  - 架构
  - RAN
last_verified: 2026-06-20
owner: agent
---

# RAN 架构演进（RAN Architecture Evolution）

> 从传统封闭基站到 O-RAN 开放解耦、Cloud RAN 云化部署、再到 AI-RAN 智能融合的无线接入网架构演进路径。

## 定义
RAN 架构演进描述了无线接入网从单体封闭式基站（传统 RAN）经由功能解耦与接口开放（O-RAN），到基于云原生/容器化的集中处理部署（Cloud RAN），再到以 GPU 加速和 AI 原生为核心的新一代架构（AI-RAN）的技术路线。O-RAN Alliance 的 nGRG 已明确提出面向 6G 的"云友好 RAN"架构原则 [1]，AI-RAN Alliance 则推动 AI 与 RAN 基础设施的深度融合 [3]。

## 关键组成 / 子能力
- **O-RAN（Open RAN）**：定义开放前传/中传接口（F1/E2/A1），将 RAN 分解为 O-CU、O-DU、O-RU 三层，引入 RIC（RAN 智能控制器）
- **Cloud RAN / vRAN**：将 BBU（基带处理单元）功能云化部署于通用服务器，支持资源弹性伸缩与多厂商协同
- **AI-RAN**：基于 GPU 的软件定义 RAN（gRAN），在同一硬件平台上共享算力处理 RAN 信号与 AI 推理负载 [4]
- **RIC 平台**：Near-RT RIC 与 Non-RT RIC 提供 AI/ML 模型的部署、推理和闭环优化能力
- **6G 云友好架构**：O-RAN nGRG 提出的面向 6G 的云原生 RAN 参考架构，强调微服务化与意图驱动 [1]

## 与相邻概念的关系
- 与 [ai-native-air-interface]：AI-RAN 和 O-RAN RIC 是 AI 原生空口落地的基础设施支撑，提供模型训练/推理的算力平台
- 与 [6g-data-plane]：RAN 架构的云化与功能解耦直接影响数据面的分布式处理能力和数据流路径设计
- 与 [network-data-analytics]：RIC 采集的 RAN 数据是 NWDAF/数据分析功能的关键输入源

## 常见误解
- **"O-RAN = Open RAN"**：O-RAN 特指 O-RAN Alliance 定义的规范体系；Open RAN 是更广义的开放 RAN 理念，TIP OpenRAN 等也在推进
- **"AI-RAN 是 O-RAN 的竞争者"**：AI-RAN 是 O-RAN 的演进方向之一，两者互补而非替代关系

## 待深挖子题
- [ ] O-RAN nGRG 6G RAN 架构白皮书详细分析 → 加入 ops/deep-dive-queue.md
- [ ] AI-RAN 中 GPU 共享算力模型（RAN + AI workload co-hosting）的数据面影响
- [ ] RIC 作为数据面数据消费/生产节点的角色定位

## 来源
[1] [Architecture principles for a cloud-friendly future 6G RAN architecture](https://mediastorage.o-ran.org/ngrg-rr/nGRG-RR-2024-01-O-RAN%20Cloud%20Friendly%20Future%206G%20RAN-v1.2.1.pdf) — O-RAN Alliance nGRG 研究报告
[2] [The Architecture of AI and Communication Integration towards 6G](https://dl.acm.org/doi/10.1145/3636534.3701550) — ACM 会议论文，O-RAN 视角的 6G 架构融合
[3] [AI-RAN Alliance](https://ai-ran.org/) — AI-RAN Alliance 官方网站
[4] [AI-RAN: Telecom Infrastructure for the Age of AI](https://www.softbank.jp/corp/set/data/technology/research/story-event/Whitepaper_Download_Location/pdf/SoftBank_AI_RAN_Whitepaper_December2024.pdf) — SoftBank AI-RAN 白皮书（2024.12）
