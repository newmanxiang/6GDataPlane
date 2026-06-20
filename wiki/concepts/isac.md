---
title: 通感一体化
title_en: Integrated Sensing and Communication
slug: isac
category: concept
status: draft
confidence: low
sources:
  - https://www.ericsson.com/en/reports-and-papers/ericsson-technology-review/articles/sensing-in-6g-use-cases-and-architecture
  - https://www.etsi.org/deliver/etsi_gr/isc/001_099/001/01.01.01_60/gr_isc001v010101p.pdf
  - https://www.3gpp.org/ftp/tsg_sa/wg2_arch/TSGS2_167_Athens_2025-02/INBOX/DRAFTS/Rel-20%20ISAC/Moderated_discussion_for_Rel-20_Integrated_Sensing_and_Communication-v0.0.2.pdf
related:
  - 6g-data-plane
  - ai-native-air-interface
  - digital-twin-network
  - ran-architecture-evolution
tags:
  - 6G
  - ISAC
  - sensing
  - 3GPP
  - ETSI
last_verified: 2026-06-20
owner: agent
---

# 通感一体化（Integrated Sensing and Communication）

> 在同一无线系统中同时实现通信与感知功能，使移动网络具备"感知物理世界"的原生能力。

## 定义
通感一体化（ISAC）是指将感知能力（如定位、追踪、成像、环境测绘）与通信功能集成到同一无线系统中，共享频谱、硬件和信号处理资源 [1]。3GPP 自 Release 19 起开始 ISAC 的可行性研究（TR 22.837），并在 Release 20 推进架构定义，预计 Release 21 实现完整规范 [3]。ETSI 已成立 ISG ISAC 专门工作组推进标准化 [2]。

## 关键组成 / 子能力
- **共享波形与信号设计**：通信信号同时用于感知（如 OFDM 雷达），实现频谱效率最大化
- **感知数据处理管道**：从原始回波信号中提取目标位置、速度、形状等感知信息
- **3GPP 与非 3GPP 感知数据融合**：结合蜂窝感知与外部传感器（雷达/LiDAR）数据，提升感知质量 [3]
- **感知即服务（Sensing-as-a-Service）**：将感知能力以网络服务形式暴露给上层应用
- **高精度定位与追踪**：6G ISAC 目标实现厘米级定位精度与实时目标追踪

## 与相邻概念的关系
- 与 [[6g-data-plane]]：ISAC 产生大量感知数据（回波信号、点云、特征图），对数据面提出高吞吐、低时延的传输需求
- 与 [[ai-native-air-interface]]：AI 原生空口为 ISAC 提供智能波束管理和感知-通信资源联合优化能力
- 与 [[digital-twin-network]]：ISAC 感知数据可作为 DTN 物理世界建模的重要输入源

## 常见误解
- **误解 1**：ISAC 只是"在基站旁边加个雷达"。实际上 ISAC 的核心是通信与感知在波形、频谱和硬件层面的深度融合，而非简单拼凑。
- **误解 2**：ISAC 的数据量可以忽略。实际上感知产生的原始数据量可能超过通信数据本身（尤其是高分辨率成像和环境测绘场景）。

## 待深挖子题
- [ ] ISAC 感知数据在数据面的传输协议与 QoS 需求分析 → 加入 ops/deep-dive-queue.md
- [ ] 3GPP Release 20 ISAC 架构中感知数据流的端到端路径设计
- [ ] ISAC 与隐私保护：感知数据中的个人信息识别与脱敏机制

## 来源
[1] [Sensing in 6G: Use cases and architecture](https://www.ericsson.com/en/reports-and-papers/ericsson-technology-review/articles/sensing-in-6g-use-cases-and-architecture) — Ericsson 6G 感知架构与用例分析
[2] [ETSI GR ISC 001](https://www.etsi.org/deliver/etsi_gr/isc/001_099/001/01.01.01_60/gr_isc001v010101p.pdf) — ETSI ISAC 工作组首份技术报告
[3] [3GPP SA2 Rel-20 ISAC Discussion](https://www.3gpp.org/ftp/tsg_sa/wg2_arch/TSGS2_167_Athens_2025-02/INBOX/DRAFTS/Rel-20%20ISAC/Moderated_discussion_for_Rel-20_Integrated_Sensing_and_Communication-v0.0.2.pdf) — 3GPP SA2 Release 20 ISAC 架构讨论文档
