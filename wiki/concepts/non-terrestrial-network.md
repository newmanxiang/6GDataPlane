---
title: 非地面网络
title_en: Non-Terrestrial Network
slug: non-terrestrial-network
category: concept
status: draft
confidence: low
sources:
  - https://www.3gpp.org/technologies/ntn-overview
  - https://www.sciencedirect.com/science/article/pii/S2095809925002917
  - https://connectivity.esa.int/wp-content/uploads/2026/01/ESA_6G_NTN_White_Paper_v8.0_2025-11-11.pdf
related:
  - 6g-data-plane
  - user-plane-evolution
  - ran-architecture-evolution
  - digital-twin-network
tags:
  - 6G
  - NTN
  - satellite
  - UAV
  - 3GPP
last_verified: 2026-06-20
owner: agent
---

# 非地面网络（Non-Terrestrial Network）

> 利用卫星、无人机等非地面平台承载移动通信，实现全球无缝覆盖。

## 定义
非地面网络（NTN）是指利用无人机系统（UAS，运行高度 8-50 km）或卫星系统（LEO/MEO/GEO）作为通信节点的网络或网络片段 [1]。3GPP 自 Release 17 起支持 NTN，通过对 NR 协议栈的适配实现地面与非地面网络的无缝互操作。在 6G 中，NTN 将演进为多层异构非地面架构，与地面网络深度融合 [2]。

## 关键组成 / 子能力
- **多层架构**：LEO（低轨）、MEO（中轨）、GEO（高轨）卫星与 HAPS（高空平台）、UAV 构成分层覆盖体系
- **协议栈适配**：针对大传播时延（LEO 约 20-40 ms 单程）进行 HARQ、定时提前（TA）、RLC 等协议调整 [3]
- **透明/再生转发模式**：透明模式卫星仅做信号中继，再生模式卫星具备星上基带处理能力
- **地面-非地面网络融合**：NTN 可替代地面物理链路承载用户面或控制面数据传输
- **星间链路（ISL）**：LEO 星座间的光/射频链路，实现空间路由与星上组网

## 与相邻概念的关系
- 与 [[6g-data-plane]]：NTN 引入长时延、高抖动的传输特性，要求数据面支持自适应协议选择和容延迟传输（DTN 协议）
- 与 [[user-plane-evolution]]：NTN 用户面需在 GTP-U 隧道协议上叠加时延补偿机制，是用户面演进的重要驱动力
- 与 [[ran-architecture-evolution]]：NTN 节点可作为分布式 RAN 的延伸，影响 CU/DU 功能分割方案

## 常见误解
- **误解 1**：NTN 只是卫星互联网的别名（如 Starlink）。实际上 3GPP NTN 强调与蜂窝网络的标准化集成，包括 UAS/HAPS 等多种非地面平台。
- **误解 2**：NTN 只影响接入层，与核心网数据面无关。实际上 NTN 的长时延特性贯穿端到端数据路径，对核心网 UPF 的缓冲、调度和 QoS 策略均有影响。

## 待深挖子题
- [ ] NTN 场景下用户面协议栈适配方案对比（透明 vs 再生模式的数据面差异）→ 加入 ops/deep-dive-queue.md
- [ ] 多层 NTN 架构中的数据路由与星地协同调度策略
- [ ] NTN 与边缘计算的结合：星上 MEC 的数据面架构设计

## 来源
[1] [Non-Terrestrial Networks (NTN)](https://www.3gpp.org/technologies/ntn-overview) — 3GPP 官方 NTN 技术概览
[2] [Non-Terrestrial Networking for 6G: Evolution, Opportunities, and Challenges](https://www.sciencedirect.com/science/article/pii/S2095809925002917) — 面向 6G 的 NTN 技术演进综述
[3] [ESA 6G NTN White Paper](https://connectivity.esa.int/wp-content/uploads/2026/01/ESA_6G_NTN_White_Paper_v8.0_2025-11-11.pdf) — ESA 6G 非地面网络白皮书
