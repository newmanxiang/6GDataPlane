---
title: 跨域数据治理将成为 6G 部署的前置条件
slug: trend-cross-domain-governance
horizon: 24m
confidence: medium
direction: emerging
drivers:
  - ISAC 感知数据引入全新隐私风险类别
  - 联邦数据空间（GAIA-X/IDSA/Telco Data Space）成熟
  - 3GPP SA5 DMFW 与 SA2 WT#5 治理功能互补
  - 跨域 AI 训练对数据主权的刚性需求
  - ETSI PDL 区块链审计跟踪标准化
inhibitors:
  - SA2/SA5 治理框架职责边界模糊
  - 跨运营商/跨国数据共享的法律壁垒
  - 治理自动化成熟度不足
  - 运营商传统竖井组织结构阻力
evidence:
  - cross-domain-data-governance-6g
  - 3gpp-rel-19-20-data-architecture-status
  - data-fabric-for-ai-native-6g
  - 3gpp-sa2-6g-data-framework-wt5
counter_evidence:
  - cross-domain-data-governance-6g
  - 3gpp-sa2-6g-data-framework-wt5
companies_to_watch:
  - Deutsche Telekom
  - Vodafone
  - Fraunhofer
  - 华为
  - Nokia
my_company_relevance: medium
created: 2026-06-25
---

# 跨域数据治理将成为 6G 部署的前置条件

## 一句话总结

6G 多域异构架构（RAN/Core/Edge/NTN）使跨域数据治理从"运维优化"升级为"部署前置条件"。

## 论据（按强度排序）

1. **ISAC 感知数据引入全新隐私类别**：通感一体（ISAC）使网络产生高精度环境感知数据（定位、成像、运动检测），这类数据的隐私敏感度远超传统通信元数据。现有隐私框架（GDPR 等）对感知数据的适用性存在法律空白。6G 部署前必须解决感知数据的采集/存储/共享治理规则。→ [cross-domain-data-governance-6g](../../wiki/topics/cross-domain-data-governance-6g.md)

2. **联邦数据空间实践推进**：GAIA-X 数据空间联盟、IDSA (International Data Spaces Association)、Fraunhofer Telco Data Space 试点为跨运营商数据共享提供了技术和治理框架。DT 在 GAIA-X 中的领导地位使电信行业成为联邦数据空间的先行者之一。→ [cross-domain-data-governance-6g](../../wiki/topics/cross-domain-data-governance-6g.md)

3. **SA5 DMFW + SA2 WT#5 互补**：3GPP SA5 的 DMFW (Data Management Framework, TS 28.104) Rel-19 冻结，SA2 WT#5 正在研究 6G 数据框架。两者互补——SA5 聚焦 OAM 域数据治理，SA2 聚焦网络功能间数据服务治理。但职责边界需要协调。→ [3gpp-rel-19-20-data-architecture-status](../../wiki/topics/3gpp-rel-19-20-data-architecture-status.md), [3gpp-sa2-6g-data-framework-wt5](../../wiki/topics/3gpp-sa2-6g-data-framework-wt5.md)

4. **跨域 AI 训练需求**：AI 原生网络需要跨 RAN/Core/Edge 的训练数据，但数据主权（Data Sovereignty）要求数据不出域。联邦学习（3GPP Rel-18/19 HFL/VFL）、差分隐私、安全多方计算是技术路径，但治理框架（谁可以用什么数据、用于什么目的、多长时间）是前提。→ [data-fabric-for-ai-native-6g](../../wiki/topics/data-fabric-for-ai-native-6g.md)

5. **ETSI PDL 区块链审计标准化**：ETSI PDL GS 034 定义了基于区块链/DLT 的不可篡改审计跟踪，为数据治理决策提供可追溯的合规证据。这在监管日益严格的环境下具有实用价值。→ [cross-domain-data-governance-6g](../../wiki/topics/cross-domain-data-governance-6g.md)

## 反向证据 / 不确定性

- **SA2/SA5 边界模糊**：运营商在 3GPP 会议上多次提出 SA2 WT#5 与 SA5 DMFW 存在范围重叠，若不解决可能导致治理框架碎片化 → [3gpp-sa2-6g-data-framework-wt5](../../wiki/topics/3gpp-sa2-6g-data-framework-wt5.md)
- **跨国法律壁垒**：各国数据保护法（GDPR/PIPL/CCPA）差异巨大，跨国运营商的统一治理框架面临法律冲突。5G 时代已存在此问题，6G 多域架构将加剧 → [cross-domain-data-governance-6g](../../wiki/topics/cross-domain-data-governance-6g.md)
- **治理自动化不成熟**：DT MARA 的 Policy-as-Code 是唯一已知的电信治理自动化实践。自动化策略执行从 PoC 到生产级仍有较大距离 → [cross-domain-data-governance-6g](../../wiki/topics/cross-domain-data-governance-6g.md)

## 信号事件

- 2024-Q1：ETSI PDL GS 034 发布（ETSI ISG PDL）
- 2024-Q2：Fraunhofer Telco Data Space 试点启动（Fraunhofer ISST）
- 2024-Q3：3GPP Rel-18 HFL/VFL 标准化冻结（3GPP SA5）
- 2025-Q1：SA5 DMFW TS 28.104 Rel-19 冻结（3GPP SA5）
- 2025-H1：SA2 WT#5 治理相关议题讨论加速（3GPP SA2）
- 2025-H2：GAIA-X 电信行业数据空间规范更新（GAIA-X AISBL）

## 未来 12-24 月可观察的指标

- [ ] SA2/SA5 数据治理框架边界协议是否达成
- [ ] ISAC 感知数据隐私框架草案（3GPP 或 ETSI）
- [ ] Telco Data Space 试点是否扩展到第二家运营商
- [ ] 国家级 6G 数据治理法规/指南发布
- [ ] 跨运营商数据共享商业协议案例
- [ ] Policy-as-Code 在第二家运营商的部署

## 何时该被推翻

- 若 6G 架构最终选择中心化而非多域分布式方案（治理简化） → **弱化**
- 若 3GPP 将数据治理全部归入 SA5 DMFW 而 SA2 不涉及 → **变异**（仍需治理但路径改变）
- 若 ISAC 被从 6G 首版标准中移除 → **弱化**（一个主要驱动力消失）
- 若运营商选择封闭数据策略（不共享、不联邦） → **推翻**
