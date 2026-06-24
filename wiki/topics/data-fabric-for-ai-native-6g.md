---
title: 服务 AI 原生 6G 的数据编织
title_en: Data Fabric for AI-Native 6G Networks
slug: data-fabric-for-ai-native-6g
category: topic
status: reviewed
confidence: medium
sources:
  - https://www.ericsson.com/en/reports-and-papers/white-papers/future-proof-data-management-for-ai-networks
  - https://www.nokia.com/6g/6g-system-architecture-where-innovation-meets-evolution-for-a-more-sustainable-and-connected-world/
  - https://www.amazon.science/blog/ai-native-6g-from-networks-to-intelligence-fabrics
  - https://portal.etsi.org/webapp/WorkProgram/Report_WorkItem.asp?WKI_ID=78246
  - https://www.etsi.org/deliver/etsi_gs/ZSM/001_099/012/01.01.01_60/gs_ZSM012v010101p.pdf
  - https://ion-turcanu.net/publication/faye2026reference/faye2026reference.pdf
  - https://digitaltwin1.org/articles/2-16
  - https://www.sciencedirect.com/science/article/pii/S0167739X24001420
  - https://arxiv.org/html/2602.16386
  - https://robust-6g.eu/wp-content/uploads/2025/01/ROBUST-6G-D2.2_v1.0-1.pdf
  - https://onestore.nokia.com/asset/f/214288/
  - https://www.huawei.com/en/huaweitech/future-technologies/data-plane-design-ai-native-6g-networks
  - https://cloud.google.com/telecom-data-fabric
  - https://www.fortunebusinessinsights.com/data-fabric-market-105979
related:
  - data-fabric-definition-and-capabilities
  - ai-native-data-plane-status
  - data-fabric-in-telecom-early-cases
  - data-fabric-vs-data-mesh
  - 6g-data-plane
  - ai-native-air-interface
  - network-data-analytics
  - active-metadata
  - digital-twin-network
  - daas-interface-design
tags: [data-fabric, AI-native, 6G, cross-domain, data-management, telecom, knowledge-graph, digital-twin, ETSI-ZSM]
last_verified: 2026-06-24
owner: agent
---

# 服务 AI 原生 6G 的数据编织

## 核心结论（150 字内）

"数据编织服务 AI 原生 6G"尚无统一标准定义，但从多个独立方向正在快速汇聚。Ericsson 2026 年白皮书明确将 data fabric 视为 AI-ready 数据管理的核心使能技术；ETSI ZSM 于 2026 年 4 月采纳 GS 029"数据管理代理"规范；至少 4 个 EU 6G 项目（6G-TWIN、6G-DALI、ROBUST-6G、CANDIL）在架构中显式使用"data fabric"术语；全球数据编织市场预计从 2025 年 33.7 亿美元增至 2034 年 164.6 亿美元（CAGR ~22%）。该交叉议题的核心挑战在于：如何将企业 IT 领域成熟的数据编织方法论，适配到电信网络亚毫秒延迟、ZB 级数据量和多厂商跨域场景。[信心：中等——概念方向明确但标准化和部署验证不足]

## 1. 现状定义

**"服务 AI 原生 6G 的数据编织"**指将数据编织（Data Fabric）架构理念——主动元数据、知识图谱、AI/ML 自动化编排、数据虚拟化——从企业 IT 域延伸到 6G 网络内部，为分布式 AI 智能体提供统一、智能、实时的数据管理基础设施。

**为什么传统方案不够？** 5G 时代的数据管理存在三重瓶颈：

1. **NWDAF 仅覆盖核心网分析**：3GPP NWDAF 是可选 NF，数据收集碎片化（各 NF 独立 EventExposure 接口），缺乏跨域能力（Samsung 2026 明确指出三大局限）。
2. **数据孤岛跨五大域**：RAN/Core/Transport/BSS/OSS 产生异构数据，缺乏统一语义层和跨域编排（Nokia 白皮书、TM Forum 调查均证实）。
3. **AI 原生需求质变**：6G 将 AI/ML 嵌入各层，AI 数据（训练数据、模型参数、推理结果）的多对多拓扑、实时性和质量要求远超 5G PDU 会话模型。

**与相邻概念的边界**：
- 与 **6G 数据面（DaaS）**：数据面是传输非连接数据的管道，数据编织是管理和编排数据的智能层，二者互补
- 与 **数据网格（Data Mesh）**：数据编织提供技术集成层，数据网格提供组织运营模型；Nokia/Ericsson 均提出混合架构
- 与 **网络数字孪生**：数字孪生消费数据编织提供的统一数据，6G-TWIN 项目将 data fabric 作为 NDT 数据存储的核心模式

## 2. 标准与组织动态（近 3 年）

| 时间 | 组织 | 进展 |
|------|------|------|
| 2026-04 | **ETSI ZSM** | GS 029 "Data Management Agent for Autonomous Networks" 工作项采纳，由中国电信/ZTE/CAICT/亚信主导。定义数据注册/发现、资产管理、认证管理、收集传输管理、工作流编排 |
| 2026-02 | Ericsson | "Future-proof Data Management for AI Networks" 白皮书（GFTL-26:000204Uen），提出 AI-ready data mesh 参考架构，明确引用 data fabric 概念 |
| 2025-06 | 3GPP SA2 | FS_6G_ARC WT#5 "数据框架"研究启动，覆盖数据收集/分发/处理/存储/暴露，尚未引用 Data Fabric 术语但功能需求高度重合 |
| 2025-05 | SNS JU | 6G 架构白皮书 v1.3，含 "Cloud Native Data Plane" 和 "AI/ML Framework" 章节 |
| 2024-09 | 学术 | CANDIL 联邦数据编织论文发表（FGCS），使用 ETSI NGSI-LD 标准实现联邦知识图谱 |
| 2024-05 | TM Forum | IG1356 "Data Architecture for AI-enabled Telecom Operations" v2.0 发布，与 ODA 框架对齐 |
| 已发布 | ETSI ZSM | GS 012 "AI Enablers" 定义数据/动作管道编排；GS 002 参考架构定义 Integration Fabric + Cross-domain Data Services |
| 已发布 | ETSI ZSM | GR 021 "Automation to Autonomy" 研究，含 MDA/NWDAF 协同数据分析框架 |

**关键观察**：截至 2026 年中，没有任何标准组织正式采纳"Data Fabric for 6G"作为标准术语。但 ETSI ZSM 的 Integration Fabric + Data Services 组合，以及 3GPP SA2 WT#5 的数据框架研究，在功能上与数据编织高度重合。ZSM GS 029 是最接近"6G 数据编织标准化"的工作项。

## 3. 关键玩家

### 厂商/运营商

| 玩家 | 方案定位 | 核心贡献 |
|------|----------|----------|
| **Ericsson** | AI-ready Data Mesh 参考架构 + Telco DataOps 平台 | 2026 白皮书定义数据联邦/知识图谱/语义建模；ESPE 流处理组件实现 RAN+Core 统一遥测；Ericsson 自身部署 SAP 数据编织 |
| **Nokia** | Data Framework（6G 六大技术框架之一）+ Mesh+Fabric 混合 | 6G 架构白皮书将数据框架列为设计核心；2024 白皮书明确提出端到端数据编织层连接 RAN/Core/Transport |
| **AWS/Amazon** | Intelligence Fabrics / "Fabric of Fabrics" | 2025-12 提出 NLM（Network Language Models）+ 分层智能编织概念，四阶段演进路径 |
| **Google Cloud** | Telecom Data Fabric | MWC 2023 发布专为 CSP 设计的数据编织产品，含预置电信适配器；截至 2026-06 仍处 Private Preview |
| **华为** | DaaS 数据面 + DO/DA/DCP | 2025 白皮书提出独立数据面架构，DCP 消息转发延迟 ~2ms；聚焦网络内部数据管道而非 IT 层数据编织 |
| **Amdocs** | Network Data Fabric (NDF) | Kafka-based 流处理 + TM Forum 认证数据模型，已部署于 Vodafone Italy 等 |

### 学术机构/EU 项目

| 项目/机构 | 与数据编织的关系 |
|-----------|-----------------|
| **6G-TWIN**（SNS JU） | NDT 参考架构明确使用"data fabric"描述分布式联邦数据存储 |
| **6G-DALI**（SNS JU） | 联邦数据空间 + DataOps 基础设施，含目录/市场/语义互操作 |
| **ROBUST-6G**（SNS JU） | 架构核心是"知识图谱嵌入数据编织"，支持 6G 数据空间 |
| **CANDIL**（UPM/Telefónica） | 联邦数据编织原型，使用 ETSI NGSI-LD + YANG 派生本体 |
| **ADROIT6G**（SNS JU） | 分布式 AI 驱动可编程 6G 架构，含数据管理与分发机制 |

### 标准组织

| 组织 | 角色 |
|------|------|
| **ETSI ZSM** | GS 029 Data Management Agent；GS 012 AI Enablers；GS 002 Integration Fabric + Data Services |
| **3GPP SA2** | FS_6G_ARC WT#5 数据框架研究（KI#21），覆盖数据收集/暴露/编排 |
| **TM Forum** | 现代数据架构项目、IG1356 白皮书、ODA Canvas 数据架构 |
| **O-RAN** | SMO 数据管理与暴露功能（Ericsson 参与标准化） |

## 4. 技术机制

### 4.1 数据编织核心能力到 6G 的映射

| 数据编织能力（Gartner 定义） | 6G 网络对应需求 | 已有方案/原型 |
|-----|------|------|
| **主动元数据** | 网络遥测数据自动分类、标注和路由 | Ericsson Telco DataOps + 语义建模；ETSI ZSM GS 029 数据注册/发现 |
| **知识图谱** | 网络拓扑/数据资产/AI 模型间语义关系表达 | CANDIL NGSI-LD 联邦知识图谱；ROBUST-6G KG-in-Fabric；KP-A 知识面 |
| **AI/ML 增强** | 智能数据管道编排、异常检测、特征工程 | Ericsson AI-ready data pipeline；ETSI ZSM 012 数据/动作管道编排 |
| **数据虚拟化** | 跨 RAN/Core/Transport 联邦查询 | Nokia 端到端数据编织层；6G-TWIN 分布式 UDR |
| **自动数据集成** | 多厂商多域数据源自动接入和 schema 对齐 | Ericsson Mediation → DataOps 平台；Google TDF 预置电信适配器 |
| **数据编排** | 端到端 DataOps 管道协调 | 华为 DO 数据流引擎；ETSI ZSM 闭环自动化 |
| **隐私与治理** | 跨域数据主权、GDPR 合规 | Deutsche Telekom 数据边界 + EKM；ETSI ZSM 安全策略 |

### 4.2 三层架构融合

综合 Ericsson、Nokia、6G-TWIN 等方案，"6G 数据编织"呈现三层融合架构：

**底层——分布式数据基础设施**：各网络域（RAN/Core/Transport/Edge）维护本地数据存储库，形成联邦化数据编织（6G-TWIN 方案）。数据通过 Data Communication Buses 或 Pub/Sub 机制在域间流动。

**中层——统一数据管理平面**：
- 元数据驱动的数据目录（自动发现、标注、血缘追踪）
- 知识图谱 / 语义层（ETSI NGSI-LD、YANG 数据模型、TM Forum SID）
- 策略即代码的数据治理引擎
- 联邦查询 / 数据虚拟化能力

**上层——AI-ready 数据消费**：
- 特征存储与语义增强的特征工程
- 数据产品市场化暴露（Data Products + Marketplace）
- AI Agent 接口（意图驱动的数据发现与订阅）

### 4.3 与华为 DaaS 的关系

华为 DaaS（DO/DA/DCP）聚焦**网络内部数据管道**——在数据面层实现多对多数据拓扑编排和 on-path 数据处理。数据编织架构则从**管理层**角度提供跨域数据统一视图、元数据管理和 AI-ready 数据准备。二者互补：DaaS 解决"数据如何在网络中高效传输"，数据编织解决"数据如何被发现、理解和信任"。在完整的 6G 数据架构中，DaaS 可作为数据编织的底层传输引擎，而数据编织为 DaaS 提供语义上下文和治理策略。

## 5. 趋势驱动力

1. **AI 数据爆炸**：6G 感知数据预估达 quettabyte（10³⁰）/天（设备侧），联邦学习/协作推理要求多对多数据拓扑——传统 NWDAF 集中式设计无法承载（Samsung 2026、华为 2025）
2. **自治网络 Level 5 愿景**：到 2030 年实现零接触自治网络，需要 AI-ready 数据管理基础设施（Ericsson 白皮书、ETSI ZSM GR 021）
3. **Agentic AI 驱动**：PwC 提出"语义数据编织"是 Agentic AI 运营的基础；AWS 提出"智能编织"支持多 Agent 协作推理
4. **跨域数据碎片化**：RAN/Core/Transport/BSS/OSS 数据孤岛是电信行业最大痛点——TM Forum 2025 调查显示仅 2/87 位高管认为实现数据完全民主化
5. **市场高速增长**：全球数据编织市场 CAGR ~22%（2026-2034），电信是重要垂直行业
6. **EU 6G 项目集群效应**：至少 4 个 SNS JU 项目在架构中显式使用 data fabric，形成技术路径共识

## 6. 批评与风险

1. **术语混淆风险**：Ericsson 用"data mesh"、Nokia 用"data framework"、AWS 用"intelligence fabric"、ETSI 用"integration fabric"——概念高度重叠但命名不统一，可能导致标准化碎片化
2. **企业 IT → 电信网络的适配鸿沟**：企业数据编织处理 GB/s 级批量数据（Gartner Hype Cycle 仍在"幻灭低谷"）；6G 网络要求 TB/s 级流式数据和亚毫秒延迟——现有数据虚拟化技术可能引入不可接受的延迟
3. **标准化远未成熟**：ETSI ZSM GS 029 刚采纳（2026-04），3GPP SA2 WT#5 仅启动研究——最快 2027-2028 年才有规范性标准
4. **缺乏端到端验证**：CANDIL 是唯一公开的联邦数据编织原型（学术规模）；6G-TWIN/ROBUST-6G 的 data fabric 组件尚无性能数据
5. **知识图谱构建成本高**：电信网络本体复杂（YANG 数据模型、3GPP 信息模型、TM Forum SID），自动本体构建工具不成熟
6. **数据治理文化障碍**：TM Forum 2025 调查显示电信行业数据文化仍"风险规避、孤岛化"——技术架构无法解决组织问题
7. **与 DaaS 独立数据面的整合路径不清**：数据编织（管理层）与 DaaS（数据面）之间的接口和交互模式无标准定义

## 7. 我司相关性（占位，由 6g-insight-report 阶段填充）

> 待读取 ops/company-context.md 后映射。初步关联点：
> - 数据编织的联邦架构和知识图谱能力对我司跨域数据统一的参考价值
> - ETSI ZSM GS 029 数据管理代理规范对产品设计的影响
> - Ericsson Telco DataOps / Google TDF 等竞品方案的对标分析
> - 数据编织 + DaaS 数据面的整合架构是否构成差异化技术路线

## 矛盾与待核实

### 矛盾 28：6G "数据编织"术语使用不一致

- **主张 A**：6G 需要"data fabric"作为统一数据管理架构 — 来源：6G-TWIN (学术/2026)、Digital Twin 6G 论文 (学术/2025)、CANDIL (学术/2024)、ROBUST-6G (EU/2025)
- **主张 B**：6G 需要"data mesh"/"AI-ready data mesh"架构 — 来源：Ericsson 白皮书 (厂商/2026-01)
- **主张 C**：6G 需要"data framework"/"intelligence fabric" — 来源：Nokia (厂商/2026)、AWS (厂商/2025)、3GPP SA2 (标准/2025)
- **现状**：概念实质高度重合（联邦化 + 知识图谱 + AI 编排 + 统一治理），但术语分歧可能影响标准化路径选择
- **本调研倾向**：不下结论。功能需求一致，术语将在标准化过程中收敛
- **何时能解决**：3GPP SA2 WT#5 和 ETSI ZSM GS 029 术语确定后（2027+）

### 矛盾 29：ETSI ZSM Integration Fabric 定位——管理层编织 vs 网络层编织

- **主张 A**：ZSM Integration Fabric 仅用于管理服务之间的集成（管理面数据编织） — 来源：ETSI GS ZSM 002 (标准/已发布)
- **主张 B**：6G 数据编织需要深入网络数据面，实现实时遥测数据的跨域编织 — 来源：6G-TWIN (学术/2026)、CANDIL (学术/2024)
- **现状**：ZSM 框架在管理面运行，ETSI ZSM GS 029 可能扩展到网络层数据管理，但尚未明确
- **本调研倾向**：不下结论。管理面编织和网络面编织可能共存但需不同技术栈
- **何时能解决**：ETSI ZSM GS 029 完成后

## 数据缺口

1. **P1**：ETSI ZSM GS 029 "Data Management Agent" 规范正文内容——目前仅有工作项描述，无草案文本
2. **P1**：6G 场景下数据编织虚拟化层的端到端延迟影响——无公开 benchmark 数据
3. **P1**：CANDIL 联邦数据编织原型在电信规模（百万级数据源）下的性能验证
4. **P1**：数据编织（管理层）与 DaaS 数据面（网络层）之间的接口定义——无标准化提案
5. **P2**：6G-TWIN / ROBUST-6G 中 data fabric 组件的实现细节和性能数据
6. **P2**：中国运营商对数据编织/数据网格在网络域的采纳意向——无公开信息
7. **P2**：知识图谱自动构建在电信网络本体场景的成熟度评估

## 来源

### 一手资料 / 官方
1. [ETSI ZSM GS 029 — Data Management Agent for Autonomous Networks](https://portal.etsi.org/webapp/WorkProgram/Report_WorkItem.asp?WKI_ID=78246) — ETSI, 2026-04, 数据管理代理规范工作项
2. [ETSI GS ZSM 012 — AI Enablers for Network Automation](https://www.etsi.org/deliver/etsi_gs/ZSM/001_099/012/01.01.01_60/gs_ZSM012v010101p.pdf) — ETSI, 数据管道编排能力
3. [ETSI GS ZSM 002 — Reference Architecture](https://www.etsi.org/deliver/etsi_gs/ZSM/001_099/002/01.01.01_60/gs_zsm002v010101p.pdf) — ETSI, Integration Fabric + Data Services
4. [Nokia 6G System Architecture](https://www.nokia.com/6g/6g-system-architecture-where-innovation-meets-evolution-for-a-more-sustainable-and-connected-world/) — Nokia, 2026-06, Data Framework 作为六大技术框架之一

### 学术
5. [CANDIL: A Federated Data Fabric for Network Analytics](https://www.sciencedirect.com/science/article/pii/S0167739X24001420) — FGCS Vol.158, 2024-09, 联邦数据编织 + ETSI NGSI-LD 知识图谱
6. [6G-TWIN: NDT Reference Architecture with Data Fabric](https://ion-turcanu.net/publication/faye2026reference/faye2026reference.pdf) — 2026, 分布式数据编织支撑 6G 网络数字孪生
7. [Digital-twin-enabled 6G Network Autonomy — Data Fabric Technology](https://digitaltwin1.org/articles/2-16) — Digital Twin Journal, 2025-05, 提出将 data fabric 应用于 6G
8. [6G-DALI: Federated Dataspace for 6G](https://arxiv.org/html/2602.16386) — arXiv, 2026-02, 联邦数据空间 + DataOps
9. [ROBUST-6G D2.2: Knowledge Graph within Data Fabric](https://robust-6g.eu/wp-content/uploads/2025/01/ROBUST-6G-D2.2_v1.0-1.pdf) — EU 项目交付件, 2025-01
10. [FITEE: 6G Autonomous RAN — Data Fabric for AI](https://link.springer.com/content/pdf/10.1631/FITEE.2400569.pdf) — Springer FITEE, 2025

### 厂商白皮书
11. [Ericsson: Future-proof Data Management for AI Networks](https://www.ericsson.com/en/reports-and-papers/white-papers/future-proof-data-management-for-ai-networks) — 2026-01, AI-ready data mesh 参考架构
12. [AWS: AI-native 6G — From Networks to Intelligence Fabrics](https://www.amazon.science/blog/ai-native-6g-from-networks-to-intelligence-fabrics) — 2025-12, NLM + Fabric of Fabrics 概念
13. [Nokia: Data Mesh and Distributed Data Architecture for Telco](https://onestore.nokia.com/asset/f/214288/) — 2024, Mesh+Fabric 混合架构
14. [Huawei: Data Plane Design for AI-Native 6G Networks](https://www.huawei.com/en/huaweitech/future-technologies/data-plane-design-ai-native-6g-networks) — 2025-02, DaaS 数据面
15. [Google Cloud Telecom Data Fabric](https://cloud.google.com/telecom-data-fabric) — Private Preview, 电信专项产品
16. [Ericsson builds SAP data fabric to scale AI](https://telconews.co.uk/story/ericsson-builds-sap-data-fabric-to-scale-ai-across-business) — 2026-05, Ericsson 自身数据编织部署

### 分析机构 / 媒体
17. [Fortune Business Insights: Data Fabric Market 2025-2034](https://www.fortunebusinessinsights.com/data-fabric-market-105979) — $3.37B → $16.46B
18. [PwC Global Telecom Outlook 2025-2029](https://www.pwc.com/gx/en/industries/tmt/telecom-outlook-perspectives.html) — 语义数据编织支撑 Agentic AI
19. [TM Forum IG1356: Data Architecture for AI-enabled Telecom](https://www.tmforum.org/resources/introductory-guide/ig1356-data-architecture-for-ai-enabled-telecom-operations-whitepaper-v3-0-0/) — 2024-05
