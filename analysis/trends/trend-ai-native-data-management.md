---
title: AI 原生网络需要全新数据管理范式
slug: trend-ai-native-data-management
horizon: 24m
confidence: high
direction: accelerating
drivers:
  - ETSI ZSM GS 029 数据管理代理标准化
  - AI-RAN Alliance + O-RAN dApp 生态
  - 3GPP Rel-18/19 NWDAF/FL 能力积累
  - 4 个 EU 6G 项目聚焦 AI 数据管道
  - IMT-2030 将 AI 原生列为设计原则
inhibitors:
  - 企业 IT 数据编织在电信级性能上的鸿沟
  - AI 数据管道标准碎片化
  - AI 训练数据质量和可信度不确定性
  - 运营商 AI/ML 人才短缺
evidence:
  - ai-native-data-plane-status
  - data-fabric-for-ai-native-6g
  - imt-2030-framework-data-needs
  - 3gpp-rel-19-20-data-architecture-status
counter_evidence:
  - data-fabric-for-ai-native-6g
  - ai-native-data-plane-status
companies_to_watch:
  - NVIDIA
  - 华为
  - Nokia
  - Samsung
  - Google Cloud
  - AWS
my_company_relevance: high
created: 2026-06-25
---

# AI 原生网络需要全新数据管理范式

## 一句话总结

AI 原生 6G 网络产生的数据管理需求远超现有 NWDAF 能力，数据编织 + DaaS 融合的新范式正在成形。

## 论据（按强度排序）

1. **ETSI ZSM GS 029 标准化**：GS 029 定义了零接触网络中的数据管理代理（Data Management Agent），明确了 AI 闭环（Observe → Analyze → Decide → Act）中每个阶段的数据管理需求。这是 AI 原生数据管理从概念到标准的关键一步。→ [data-fabric-for-ai-native-6g](../../wiki/topics/data-fabric-for-ai-native-6g.md)

2. **三重 AI 数据路径并存**：当前 AI 原生数据面呈现三条并行路径——(a) In-datapath ML（P4/Pegasus 数据面内嵌推理）、(b) DaaS 数据管道（华为 DO/DA/DCP 体系的 AI 数据服务）、(c) dApp 实时推理（O-RAN E3 接口的数据面智能体）。三条路径的数据管理需求差异巨大，需要统一框架。→ [ai-native-data-plane-status](../../wiki/topics/ai-native-data-plane-status.md)

3. **IMT-2030 框架级要求**：ITU-R M.2160 将 AI 原生列为 6G 六大设计原则之一，AIAC（AI and Communication）是六大使用场景之一。框架层面的定位意味着数据管理不再是功能增强，而是基础架构要求。→ [imt-2030-framework-data-needs](../../wiki/topics/imt-2030-framework-data-needs.md)

4. **EU 6G 项目集群验证**：ROBUST-6G（KG-in-Fabric 知识图谱嵌入数据编织）、CANDIL（NGSI-LD 联邦知识图谱）、PREDICT-6G（预测性数据管道）、RIGOUROUS（可信 AI 数据质量）四个项目从不同角度验证了 AI 原生数据管理的可行性和必要性。→ [data-fabric-for-ai-native-6g](../../wiki/topics/data-fabric-for-ai-native-6g.md)

5. **NWDAF 能力天花板**：3GPP Rel-19 NWDAF 增强（Phase 3）虽然新增了联邦学习、根因分析等能力，但其"收集-存储-分析"的集中式架构在多域、实时、大规模 AI 训练场景下面临根本性的扩展性瓶颈。→ [3gpp-rel-19-20-data-architecture-status](../../wiki/topics/3gpp-rel-19-20-data-architecture-status.md)

## 反向证据 / 不确定性

- **企业 IT 数据编织的性能鸿沟**：现有数据编织平台（IBM/Informatica/Denodo）设计目标是企业 BI/分析级延迟（秒~分钟级），而电信 AI 推理需要亚毫秒级数据访问。这一鸿沟是否可通过电信适配弥合尚无定论 → [data-fabric-for-ai-native-6g](../../wiki/topics/data-fabric-for-ai-native-6g.md)
- **标准碎片化**：3GPP（NWDAF/DCCF）、ETSI ZSM（GS 029）、O-RAN（dApp/SMO）、TM Forum（ODA）各有数据管理框架，互不兼容。统一框架的形成需要跨组织协调 → [ai-native-data-plane-status](../../wiki/topics/ai-native-data-plane-status.md)
- **AWS "Fabric of Fabrics" 概念**：AWS 提出的多层数据编织概念虽有远见，但目前仍停留在白皮书阶段，缺乏电信网络实际验证 → [data-fabric-for-ai-native-6g](../../wiki/topics/data-fabric-for-ai-native-6g.md)

## 信号事件

- 2023-Q4：AI-RAN Alliance 成立，聚焦 RAN 域 AI 原生能力（AI-RAN Alliance）
- 2024-Q2：O-RAN 发布 dApp / E3 接口初步规范（O-RAN Alliance）
- 2024-Q3：3GPP Rel-18 NWDAF Phase 2 冻结含 FL 支持（3GPP）
- 2025-Q1：ETSI ZSM GS 029 通过投票（ETSI ISG ZSM）
- 2025-H1：ROBUST-6G 发布 KG-in-Fabric 中期报告（EU SNS JU）
- 2025-Q3：Rel-19 NWDAF Phase 3 冻结（3GPP）

## 未来 12-24 月可观察的指标

- [ ] ZSM GS 029 正式发布后的实施指南（Implementation Guide）进度
- [ ] O-RAN dApp 规范完整版发布及首批商用 PoC
- [ ] 3GPP SA2 WT#5 中 AI 数据管道相关的方案收敛
- [ ] 运营商发布 AI 原生网络 PoC 中的数据管理架构细节
- [ ] EU 6G 项目集群（ROBUST-6G/CANDIL 等）最终交付物
- [ ] 首个跨标准组织的 AI 数据管理互操作验证

## 何时该被推翻

- 若 AI 原生网络的实际部署表明 NWDAF + DCCF 增强已足够满足需求 → **推翻**
- 若 2027 年底无任何运营商在 AI 数据管道上采用数据编织架构 → **弱化**
- 若 AI 原生网络方向本身被 6G 标准化降级（从设计原则变为可选增强） → **推翻**
- 若企业 IT 数据编织供应商全面放弃电信垂直市场 → **弱化**
