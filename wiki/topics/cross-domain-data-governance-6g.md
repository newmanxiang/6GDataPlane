---
title: 6G 跨域数据治理与数据编织融合
title_en: Cross-Domain Data Governance for 6G with Data Fabric Integration
slug: cross-domain-data-governance-6g
category: topic
status: reviewed
confidence: medium
sources:
  - https://6g-twin.eu/wp-content/uploads/2025/12/6G-TWIN-D2.1-Deliverable-Data-governance-privacy-and-harmonization-final.pdf
  - https://arxiv.org/html/2602.16386
  - https://www.ericsson.com/en/reports-and-papers/white-papers/future-proof-data-management-for-ai-networks
  - https://www.nokia.com/asset/f/214288/
  - https://itecspec.com/3gpp/32.801-01
  - https://opg.optica.org/jocn/abstract.cfm?uri=jocn-17-11-1019
  - https://www.sciencedirect.com/science/article/pii/S0167739X24001420
  - https://www.tmforum.org/data-governance-framework/
  - https://smart-networks.europa.eu/wp-content/uploads/2025/06/archwg-whitepaper-v1.3-final-23may_clean.pdf
  - https://inform.tmforum.org/features-and-opinion/why-governance-is-key-to-deutsche-telekoms-new-ai-architecture
  - https://www.hhi.fraunhofer.de/en/telco-data-space.html
  - https://www.lfdecentralizedtrust.org/blog/blockchain-enabled-trust-in-6g
related:
  - data-fabric-in-telecom-early-cases
  - data-fabric-definition-and-capabilities
  - data-fabric-for-ai-native-6g
  - 6g-data-plane
  - network-data-analytics
  - privacy-preserving-data-fabric
  - active-metadata
  - ai-native-data-plane-status
  - 3gpp-rel-19-20-data-architecture-status
tags:
  - data-governance
  - cross-domain
  - 6G
  - data-fabric
  - privacy
  - telecom
  - data-sovereignty
  - federated-governance
last_verified: 2026-06-24
owner: agent
---

# 6G 跨域数据治理与数据编织融合

## 核心结论（150 字内）

6G 网络的跨域数据治理正从"运营侧治理"向"网络原生治理"演进。3GPP SA5 已启动 6G 数据管理框架（DMFW）研究，SA2 WT#5 数据框架也涵盖访问控制和隐私维度，两者存在职责交叉但互补。产业界形成三大治理范式：联邦治理（Nokia/Ericsson）、数据空间治理（IDSA/GAIA-X/6G-DALI）、策略即代码治理（Deutsche Telekom MARA）。数据编织架构通过主动元数据和知识图谱为跨域治理提供技术底座——统一语义层实现 RAN/Core/OSS/BSS 数据的自动化策略执行，但端到端集成规范尚不存在。

## 1. 现状定义

### 什么是 6G 跨域数据治理

6G 跨域数据治理是指在 6G 网络多域异构环境中，对数据的所有权、访问权、质量保障和合规性进行统一管理的体系。其"跨域"涵盖至少七个治理域：

| 域 | 数据特征 | 治理挑战 |
|---|---|---|
| RAN 域（O-RAN/AI-RAN）| 实时遥测、CSI、波束数据 | 亚毫秒级时效性 vs 合规审计需求 |
| 核心网域（5GC/6GC）| 会话数据、NWDAF 分析、用户上下文 | 用户隐私、数据最小化 |
| 传输域 | 光/IP 性能数据 | 多供应商互操作治理 |
| 边缘/MEC 域 | AI 推理数据、本地化服务数据 | 数据本地化法规、边缘安全 |
| 终端/UE 域 | 用户行为、设备遥测、AI 模型参数 | 用户同意、设备隐私 |
| BSS 域 | 客户数据、计费、CRM | GDPR/个人信息保护 |
| OSS 域 | 网络配置、告警、PM/FM 数据 | 跨厂商数据格式统一 |

### 为什么 5G 治理方式不够

5G 数据治理存在三个根本性不足（Samsung Research 2026、SNS JU 白皮书 2025）：

1. **域内孤岛治理**：5G 各 WG 独立定义数据管理（SA2 管 NWDAF、SA5 管 OAM、RAN 管 MDT），缺乏跨域统一框架
2. **用户面"黑箱"**：UP 数据对核心网不可见，无法对传输中的 AI 数据实施治理策略
3. **缺乏原生数据主权机制**：5G 架构假设单一运营商控制，6G 的多利益方联邦环境（运营商+垂直行业+云+监管者）需要原生主权保障

## 2. 标准与组织动态（近 3 年）

### 3GPP

| 工作组 | 进展 | 时间 |
|---|---|---|
| **SA5** | TS 32.801 定义 6G DMFW（数据管理框架）研究：覆盖数据收集、处理、注册、发现、访问控制、发布、分发、暴露、编目、销毁、质量报告 | 2025-2026 |
| **SA5** | WT-4 研究非 3GPP 数据（如 O-RAN）整合、WT-5 研究用户同意机制复用 | 2025-2026 |
| **SA2** | FS_6G_ARC WT#5 数据框架：研究数据收集/分发/处理/存储/访问/暴露，**含访问控制/用户同意和隐私** | 2025-2027 |
| **SA2** | KI#21 数据框架明确将隐私和治理纳入研究范围 | 2025-08 启动 |

### ETSI

| ISG | 进展 | 时间 |
|---|---|---|
| **ZSM** | 端到端跨域网络和服务自动化方案，含可持续性和能力暴露考量；Diego R. Lopez（Telefónica）任主席 | 持续活跃 |
| **PDL** | GS PDL 034（进行中）：跨域数据治理——覆盖电信/垂直/云/监管数据空间的出处、策略执行、可互操作信任 | 2025-2026 |
| **PDL** | GS PDL 033：AI/ML 模型出处和 O-RAN 安全 | 2025 发布 |
| **ENI** | AI 驱动自治网络的数据治理能力，跨域意图管理 | 持续演进 |

### TM Forum

| 项目 | 进展 | 时间 |
|---|---|---|
| **Data Governance Framework** | 现代灵活治理框架 v3.0——决策权和责任规定，确保数据可用性/质量/合规 | 成熟产品 |
| **GB1025** | Data Governance Maturity Model v3.0.0——流程/人员/技术三维度成熟度评估 | 成熟标准 |
| **MDA** | Modern Data Architecture 项目——探索电信数据架构升级，含 Data Fabric/Mesh 治理讨论 | 2023-2026 |
| **ODA** | Open Digital Architecture 将治理嵌入 API 层，Canvas 商用化加速治理落地 | 2025 商用 |

### O-RAN Alliance

| 研究 | 进展 | 时间 |
|---|---|---|
| **nGRG Cross-domain AI** | 研究跨 RAN-Core-Transport 域的 AI 数据协同，含数据质量和访问控制 | 2024 |
| **R005 AI/ML 工作流** | 规范训练/推理部署场景中的数据供给和模型治理 | 2025 完成 |

### 其他

- **IDSA/GAIA-X**：Dataspace Protocol (DSP) 定义参与者间主权数据交换协议；T-Systems + NTT Communications 日欧跨境数据空间测试
- **ITU-T**：Y.4560/Y.4561 定义可信数据空间和数据治理机制

## 3. 关键玩家

### 标准/产业组织

| 组织 | 治理贡献 |
|---|---|
| 3GPP SA5 | DMFW 标准化（统一数据管理框架） |
| 3GPP SA2 | 数据框架隐私/访问控制 |
| ETSI ZSM | 跨域自动化治理 |
| ETSI PDL | 区块链分布式治理 |
| TM Forum | Data Governance Framework + ODA 商用 |
| IDSA | Dataspace Protocol + 主权治理 |
| GAIA-X | 欧洲数据主权联邦架构 |

### 厂商

| 厂商 | 方案 | 特点 |
|---|---|---|
| **Nokia** | 联邦治理 + Data Fabric/Mesh | "Built-In Data Governance & Discovery"（EuCNC 2025 演讲），6G 数据技术框架包含治理 |
| **Ericsson** | Data Islands + Mesh 双层治理 | 本地岛治理 + 全局网格治理原则，语义中介引擎跨域映射 |
| **Deutsche Telekom** | MARA 架构（策略即代码治理）| 运行时治理层、AI Agent 认证、EU AI Act 合规 |
| **Telefónica** | CANDIL 联邦数据编织 + ETSI ZSM/NGSI-LD | 联邦知识图谱治理 + YANG 数据模型本体 |
| **Fraunhofer HHI** | Telco Data Space | IDSA 对齐的实测数据主权治理平台 |
| **Huawei** | DaaS 数据面 + 访问控制 | DO 层策略控制（隐含治理） |

### 学术/EU 项目

| 项目 | 研究方向 |
|---|---|
| **6G-TWIN** (SNS JU) | NDT 数据治理、隐私和统一框架（D2.1 交付件） |
| **6G-DALI** (SNS JU) | 联邦数据空间 + DataOps 治理基础设施 |
| **CANDIL** (UPM/Telefónica) | 联邦数据编织 + NGSI-LD 知识图谱治理 |
| **SAFE-6G** (SNS JU) | 可信 6G 数据空间 + 可解释 AI |

## 4. 技术机制

### 4.1 跨域数据治理框架设计

综合 Nokia、Ericsson 和 6G-TWIN 项目，6G 跨域数据治理框架呈现以下技术层次：

```
┌─────────────────────────────────────────────────────┐
│ 全局治理策略层（Global Governance Policy Layer）      │
│ - 合规规则引擎（GDPR/数据安全法/行业法规）          │
│ - 数据分类与分级策略                                 │
│ - 跨域访问控制矩阵                                   │
├─────────────────────────────────────────────────────┤
│ 联邦治理执行层（Federated Governance Execution）     │
│ - 域内自主治理 + 全局策略继承                        │
│ - 策略即代码（Policy-as-Code）自动化执行             │
│ - 数据合约（Data Contracts）跨域协商                  │
├─────────────────────────────────────────────────────┤
│ 数据编织语义层（Data Fabric Semantic Layer）          │
│ - 主动元数据管理 → 自动发现/分类/标注               │
│ - 知识图谱 → 跨域数据血缘/影响分析                  │
│ - 本体映射 → RAN/Core/OSS/BSS 语义统一              │
├─────────────────────────────────────────────────────┤
│ 数据主权保障层（Data Sovereignty Layer）             │
│ - 联邦学习 / 差分隐私 / 同态加密                    │
│ - 数据空间连接器（DSC）+ 数据使用策略               │
│ - 出处追踪 / 审计日志 / 区块链锚定                   │
├─────────────────────────────────────────────────────┤
│ 域数据管理层（Domain Data Management）               │
│ - RAN: O-RAN R005 AI/ML 工作流数据治理               │
│ - Core: NWDAF/DCCF 数据收集协调                      │
│ - OAM: SA5 MDAF/MDA 管理数据分析                     │
│ - BSS: TM Forum SID + Data Governance Maturity       │
└─────────────────────────────────────────────────────┘
```

### 4.2 关键技术与集成点

**数据编织在跨域治理中的角色**：

1. **统一语义发现**：通过知识图谱和主动元数据，自动发现并关联 RAN PM 数据、核心网 CDR、BSS 客户数据的语义关系，无需人工映射
2. **策略自动执行**：基于元数据分析自动识别敏感字段（如定位数据、IMSI），施加相应治理策略（匿名化/访问限制/数据最小化）
3. **跨域数据血缘**：追踪数据从 RAN 采集→Core 汇聚→OAM 分析→BSS 变现的完整流转路径，支持合规审计
4. **联邦查询治理**：数据虚拟化层在执行跨域联邦查询时内嵌治理检查——验证请求者权限、检查数据分级、应用匿名化

**CANDIL 实现参考**（Telefónica/UPM）：
- ETSI NGSI-LD 标准实现联邦知识图谱——每个域维护本地知识图谱，通过链接数据（Linked Data）实现跨域语义发现
- YANG 数据模型映射为网络分析本体——利用 LOT 方法论从标准数据模型派生治理规则
- 全容器化部署——支持边缘到云的分布式治理执行

**Deutsche Telekom MARA 治理实践**：
- Policy-as-Code 运行时治理：对 AI Agent 的数据访问、模型调用、工具执行实施细粒度策略控制
- 数据作为产品（Data as a Product）：明确所有权、合约、生命周期管理
- 上下文感知授权：根据请求上下文（谁/何时/从何处/为何目的）动态授权

### 4.3 隐私保护技术在跨域治理中的应用

| 技术 | 跨域治理应用 | 标准化现状 |
|---|---|---|
| 联邦学习（FL）| 跨运营商模型协作训练，数据不出域 | 3GPP Rel-18 HFL、Rel-19 VFL |
| 差分隐私（DP）| 聚合分析添加噪声，保护个体隐私 | NIST 指南已发布 |
| 安全多方计算（MPC）| 跨域联合计算，数据加密不暴露 | 中国 YD/T 3758.5 |
| 同态加密（HE）| 密态数据上直接计算 | 学术成熟，工程化进展中 |
| 数据空间连接器 | 策略驱动主权数据交换 | IDSA DSP、Eclipse EDC |
| 区块链/DLT | 跨域审计、模型出处、不可否认 | ETSI GS PDL 034 |

## 5. 趋势驱动力

1. **AI 原生化驱动数据需求爆发**：6G 的 AI-native 设计要求 ZB 级数据跨域流动，传统逐案审批治理模式不可持续，需要自动化策略执行
2. **多利益方生态碎片化**：6G 的运营商+CSP+云+垂直行业+设备商多方生态，数据所有权和使用权远比 5G 复杂
3. **数据主权法规全球碎片化**：GDPR（欧盟）、中国数据安全法/个人信息保护法、各国数据本地化要求，迫使跨域治理必须支持差异化策略
4. **自治网络 Level 4/5 需求**：TM Forum/ETSI ZSM 定义的 Level 4/5 自治网络要求跨域实时数据决策——治理必须内嵌于数据流而非外挂
5. **数据变现机会**：运营商将网络数据资产化（Deutsche Telekom Dataplex、KPN Data Service Hub），需要治理框架保障合规变现
6. **AI 伦理与可信 AI 要求**：EU AI Act 等法规要求 AI 训练数据可追溯、模型决策可解释——跨域数据治理是合规基础

## 6. 批评与风险

### 6.1 技术挑战

| 挑战 | 说明 |
|---|---|
| **治理性能开销** | Fraunhofer HHI 实测显示策略执行引入额外延迟和通信开销；实时 RAN 遥测场景中治理延迟可能不可接受 |
| **语义异构性** | RAN 域（3GPP YANG/O-RAN 数据模型）vs BSS 域（TM Forum SID）vs 传输域（IETF YANG）语义对齐极其复杂 |
| **治理策略冲突** | 不同域/不同法规的治理策略可能相互矛盾（如某数据在域 A 可共享但在域 B 需本地化） |
| **元数据爆炸** | 跨 7 域的元数据管理本身可能成为新的复杂性来源 |
| **动态数据分类** | 同一数据在不同上下文中敏感度不同（聚合后的网络统计 vs 单用户粒度数据） |

### 6.2 标准碎片化

- **SA2 vs SA5 职责重叠**：WT#5 数据框架和 DMFW 在数据管理/暴露/访问控制上存在交叉，协调机制不明确
- **3GPP vs ETSI vs TM Forum 治理标准不统一**：三大组织各有数据治理规范，缺乏明确分工或互引
- **区域法规差异导致技术方案碎片化**：GDPR 合规方案 vs 中国数据安全法方案 vs 其他国家方案难以用单一技术框架覆盖

### 6.3 产业实施挑战

- **文化障碍**：TM Forum 2025 调查显示运营商数据治理成熟度极低（87 位高管中仅 2 人认为实现数据民主化）
- **组织孤岛**：RAN 团队、核心网团队、IT 团队、合规团队各自为政，跨域治理需要深层组织变革
- **技能缺口**：需要同时掌握网络技术、数据管理、隐私工程和合规的复合人才，极度稀缺
- **投资回报不确定**：治理投入短期内难以量化 ROI，运营商投资意愿有限

## 7. 我司相关性（占位）

> 待填充：结合公司在 6G 数据面的研究定位，分析以下方向：
> - 跨域数据治理是 DaaS 架构（DO/DA/DCP）的必要补充——数据面不仅需要"流通"能力，还需"治理"能力
> - 3GPP SA5 DMFW 和 SA2 WT#5 的交叉点正是数据编织架构的切入机会
> - Deutsche Telekom MARA 的 Policy-as-Code 模式对我司 AI 数据治理产品设计的启示
> - 联邦知识图谱（CANDIL 模式）作为跨域语义统一治理的技术选型参考
> - 数据主权保障（Telco Data Space 模式）对运营商客户合规需求的响应

## 矛盾与待核实

1. **SA2 WT#5 vs SA5 DMFW 职责边界不清**：两者都涉及数据访问控制和数据暴露，正式分工协议尚未发布。SA2 偏向"网络数据框架"，SA5 偏向"管理数据治理"，但实际边界模糊 [已登入 contradictions.md]
2. **联邦治理 vs 统一治理的有效性争论**：Nokia 推联邦治理（域自治+全局标准），但 TM Forum GB1025 隐含偏向集中式成熟度评估。6G 多利益方场景中二者如何平衡无共识
3. **数据编织治理能力的成熟度存疑**：Gartner 2024 将 Data Fabric 治理相关组件（主动元数据、增强数据目录）定位在"幻灭低谷"，电信跨域场景的复杂度远超企业 IT 场景
4. **"Built-In Governance"概念定义不清晰**：Nokia EuCNC 2025 提出"内置数据治理与发现"，但该概念与 3GPP 标准化路径的映射关系不明确

## 数据缺口

1. **P1**：3GPP SA5 DMFW 与 SA2 WT#5 的正式分工协议——尚未发布任何公开文档
2. **P1**：跨域数据治理框架在实时 RAN 遥测场景的端到端性能基准——仅 Fraunhofer HHI 有光网络测试数据，无 RAN 场景数据
3. **P1**：中国运营商 6G 数据治理技术路线——缺乏公开英文文献
4. **P1**：数据编织架构与 3GPP DMFW/NWDAF 的集成规范——不存在任何标准化文档
5. **P2**：Nokia "Built-In Data Governance" 完整方案内容——仅有 EuCNC 2025 演讲标题，无公开论文或白皮书
6. **P2**：联邦治理模式在超大规模（100+ 域/10,000+ 数据源）环境下的可扩展性验证

## 来源

### 一手资料 / 官方
1. [6G-TWIN D2.1: Data Governance, Privacy, and Harmonization](https://6g-twin.eu/wp-content/uploads/2025/12/6G-TWIN-D2.1-Deliverable-Data-governance-privacy-and-harmonization-final.pdf) — SNS JU 项目交付件, 2025-12, 6G NDT 数据治理全面框架
2. [3GPP TS 32.801: Study on 6G Management and Orchestration](https://itecspec.com/3gpp/32.801-01) — 3GPP SA5, 2025-2026, 含 DMFW 数据管理框架研究
3. [3GPP SA5 Rel-20 6G OAM Work Areas Discussion](https://www.3gpp.org/ftp/Email_Discussions/SA5/SA5-level%20discussions/SA5%23161/) — SA5 统一数据管理框架 WT 定义
4. [SNS JU 6G Architecture Whitepaper v1.3](https://smart-networks.europa.eu/wp-content/uploads/2025/06/archwg-whitepaper-v1.3-final-23may_clean.pdf) — EU, 2025-05, 数据治理和高质量数据供给要求
5. [TM Forum Data Governance Framework](https://www.tmforum.org/data-governance-framework/) — TM Forum, 电信数据治理成熟度标准

### 学术
6. [6G-DALI: Towards Secure and Interoperable Data Spaces for 6G](https://arxiv.org/html/2602.16386) — SNS JU 项目, 2026, 联邦数据空间 + DataOps 治理
7. [CANDIL: A Federated Data Fabric for Network Analytics](https://www.sciencedirect.com/science/article/pii/S0167739X24001420) — Telefónica/UPM, FGCS 2024, 联邦知识图谱数据编织
8. [Network Data Sharing: Governance Framework for Data Sovereignty](https://opg.optica.org/jocn/abstract.cfm?uri=jocn-17-11-1019) — Fraunhofer HHI, Optica JOCN 2025-11, 策略驱动主权治理框架

### 厂商白皮书
9. [Ericsson: Future-proof Data Management for AI Networks](https://www.ericsson.com/en/reports-and-papers/white-papers/future-proof-data-management-for-ai-networks) — Ericsson, 2025/2026, 跨域治理双层原则
10. [Nokia: Data Mesh and Distributed Data Architecture for Telco Networks](https://www.nokia.com/asset/f/214288/) — Nokia, 2024, 联邦治理 + Data Fabric 方案
11. [Deutsche Telekom MARA Technology Blueprint](https://inform.tmforum.org/features-and-opinion/why-governance-is-key-to-deutsche-telekoms-new-ai-architecture) — DT/TM Forum, 2026-06, 策略即代码运行时治理
12. [Fraunhofer HHI: Telco Data Space](https://www.hhi.fraunhofer.de/en/telco-data-space.html) — Fraunhofer, 2025, IDSA 对齐数据主权平台

### 分析机构 / 产业
13. [Blockchain-Enabled Trust in 6G (ETSI PDL)](https://www.lfdecentralizedtrust.org/blog/blockchain-enabled-trust-in-6g) — LF Decentralized Trust, 2026-06, ETSI GS PDL 034 跨域治理
14. [EuCNC 2025 Workshop: Data for 6G](https://www.eucnc.eu/programme/workshops/workshop-6/) — Nokia "Built-In Data Governance & Discovery" 演讲列表
