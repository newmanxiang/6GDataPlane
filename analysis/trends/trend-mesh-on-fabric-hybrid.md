---
title: Mesh-on-Fabric 混合架构将成为电信数据管理主流
slug: trend-mesh-on-fabric-hybrid
horizon: 36m
confidence: low
direction: emerging
drivers:
  - 数据编织中心化 + 数据网格去中心化的互补性
  - 电信多域架构天然适配混合模式
  - AWS Fabric of Fabrics 概念验证思路可行性
  - DT MARA 策略即代码实现联邦治理
  - TM Forum ODA 域自治理念与 Mesh 契合
inhibitors:
  - 混合架构设计复杂度高
  - 无已知的电信级大规模实践
  - 数据编织本身在电信尚未成熟
  - 组织变革阻力（域团队自治 vs IT 统管）
evidence:
  - data-fabric-vs-data-mesh
  - data-fabric-for-ai-native-6g
  - cross-domain-data-governance-6g
  - data-fabric-in-telecom-early-cases
counter_evidence:
  - data-fabric-vs-data-mesh
  - data-fabric-in-telecom-early-cases
companies_to_watch:
  - Deutsche Telekom
  - AWS
  - Vodafone
  - TM Forum
  - Denodo
my_company_relevance: medium
created: 2026-06-25
---

# Mesh-on-Fabric 混合架构将成为电信数据管理主流

## 一句话总结

电信数据管理将采用 Mesh-on-Fabric 混合模式——域自治（Mesh）+ 统一元数据层（Fabric）的组合架构。

## 论据（按强度排序）

1. **架构互补性的理论共识**：Data Fabric（集中元数据、统一策略、自动化集成）和 Data Mesh（域自治、数据产品化、联邦治理）的互补性已成为行业共识。电信网络的多域特征（RAN/Core/Edge/OSS/BSS）天然适配"域内自治 + 跨域编织"的混合模式。→ [data-fabric-vs-data-mesh](../../wiki/topics/data-fabric-vs-data-mesh.md)

2. **AWS Fabric of Fabrics 概念**：AWS 提出的多层 Data Fabric 架构允许每个域维护本地 Fabric，通过上层联邦 Fabric 实现跨域协调。这与 Mesh-on-Fabric 概念高度契合，虽然仍处白皮书阶段，但提供了可参考的架构蓝图。→ [data-fabric-for-ai-native-6g](../../wiki/topics/data-fabric-for-ai-native-6g.md)

3. **DT MARA Policy-as-Code**：DT 的 MARA 实现了策略即代码的联邦治理——全局策略定义 + 域本地执行。这是 Mesh-on-Fabric 在治理层的实践原型，证明了"联邦定义、本地执行"的可行性。→ [cross-domain-data-governance-6g](../../wiki/topics/cross-domain-data-governance-6g.md)

4. **TM Forum ODA 域自治理念**：TM Forum 的 Open Digital Architecture 强调功能域（Core Commerce、Production、Party 等）的自治性，与 Data Mesh 的域自治理念一致。ODA + Data Fabric 的组合已在 TM Forum Catalyst 项目中探索。→ [data-fabric-in-telecom-early-cases](../../wiki/topics/data-fabric-in-telecom-early-cases.md)

5. **3GPP 多 WG 结构的现实映射**：3GPP 自身的组织结构（SA2 管核心网、SA5 管 OAM、CT 管协议、RAN 管无线）天然形成了"域"，标准化产出也按域组织。Data Mesh 的域自治映射到这种组织结构比纯 Fabric 的集中化更现实。→ [3gpp-sa2-6g-data-framework-wt5](../../wiki/topics/3gpp-sa2-6g-data-framework-wt5.md)

## 反向证据 / 不确定性

- **无电信级大规模实践**：Mesh-on-Fabric 在企业 IT 中也仅是新兴趋势，电信领域完全没有经过验证的大规模部署案例 → [data-fabric-vs-data-mesh](../../wiki/topics/data-fabric-vs-data-mesh.md)
- **数据编织本身尚未成熟**：在 Fabric 尚处电信早期试点阶段时，讨论 Mesh-on-Fabric 可能过于超前。必须先解决 Fabric 的电信适配问题 → [data-fabric-in-telecom-early-cases](../../wiki/topics/data-fabric-in-telecom-early-cases.md)
- **设计复杂度**：混合架构需要同时管理两套范式的接口、协议和治理规则，设计和运维复杂度远超单一方案
- **组织变革阻力**：Data Mesh 要求域团队承担数据产品责任，这需要运营商组织结构的根本变革，传统竖井式管理可能形成阻力

## 信号事件

- 2023：Zhamak Dehghani (Data Mesh 创始人) 在多个会议讨论 Mesh+Fabric 融合趋势
- 2024-Q1：AWS 发布 Fabric of Fabrics 白皮书（AWS Architecture Blog）
- 2024-Q2：DT MARA Policy-as-Code 实践报告（DT TechBlog）
- 2025-Q1：TM Forum Catalyst 数据编织项目含混合架构探索（TM Forum）

## 未来 12-24 月可观察的指标

- [ ] 是否有运营商明确采用 Mesh-on-Fabric 术语描述其数据架构战略
- [ ] AWS/Azure/GCP 是否推出面向电信的 Mesh-on-Fabric 产品
- [ ] TM Forum 是否将 Mesh-on-Fabric 纳入正式框架文件
- [ ] 3GPP SA2/SA5 是否在规范中引入域自治 + 联邦治理的架构模式
- [ ] 电信数据管理厂商（Amdocs/Mycom 等）产品路线图是否包含混合架构

## 何时该被推翻

- 若电信行业最终选择纯 Data Fabric 集中化方案（证明域自治不必要） → **推翻**
- 若 Data Mesh 概念在企业 IT 市场全面退潮 → **弱化**
- 若 2028 年底仍无运营商试点 Mesh-on-Fabric 架构 → **推翻**
- 若 3GPP 6G 架构明确选择集中式数据管理方案 → **弱化**
