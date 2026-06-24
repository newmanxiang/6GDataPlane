# 精读笔记：Data Fabric for AI-Native 6G

> 子题 slug: data-fabric-for-ai-native-6g
> 调研日期: 2026-06-24
> 精读来源: 15 篇

---

## [Ericsson: Future-proof Data Management for AI Networks]（厂商白皮书，2026-01/02）
URL: https://www.ericsson.com/en/reports-and-papers/white-papers/future-proof-data-management-for-ai-networks

### 关键数据点
- 白皮书编号 GFTL-26:000204Uen，2026 年 1 月发布
- 提出"From data mess to AI-ready data mesh"理念
- 参考架构基于 3GPP、O-RAN 和 Apache 开放数据湖仓标准
- 预计到 2026 年底约 80% 企业将加速自动化投入

### 关键论断
- "AI also further motivates the need to make data more accessible, which is a significant driver for the establishment of a data fabric, enabling a unified approach to data access through integrated catalogs and other federated services."（明确使用 data fabric 术语）
- 提出"策略驱动的数据集成编织层"（Data Integration Fabric），数据消费者只需定义所需内容，系统智能编排获取、转换和交付
- 四大架构领域：数据源、数据摄入、数据精炼与治理、数据消费支持
- 强调联邦化架构：数据保留在源系统，语义/治理/策略中央管理
- 知识图谱 + 语义建模是 AI-ready 数据管道的核心使能技术

### 与其他来源的矛盾
- Ericsson 使用"data mesh"作为品牌词但实际架构包含 data fabric 核心能力（虚拟化 + 联邦治理 + 知识图谱），与 Nokia 的 Mesh+Fabric 混合架构本质相似

---

## [Amazon Science: AI-native 6G: From Networks to Intelligence Fabrics]（厂商博客，2025-12）
URL: https://www.amazon.science/blog/ai-native-6g-from-networks-to-intelligence-fabrics

### 关键数据点
- 提出 Network Language Models (NLMs) 概念
- 四阶段部署路径：闭环自动化 → 跨域控制 → 联邦 NLMs → 完全自主编排
- 目标架构：动态组合计算、存储、网络、数据和 AI 资源

### 关键论断
- "6G will be AI native from the ground up, a distributed computation and communications fabric embedding intelligence into daily life like a utility"
- "Fabric of fabrics" — 层级化的"编织之编织"概念：本地主权的智能框架通过 NLM 协议联邦化实现全局优化
- 十大架构原则，核心包括：模型驱动抽象、上下文推理、协作智能、多域联邦
- 联邦学习架构使服务提供商可在本地数据上训练，共享梯度更新而不集中数据

### 新发现的术语
- NLM (Network Language Model)
- Hyper-composed Networks
- Fractal Emergence

---

## [Nokia: 6G System Architecture — Data Framework]（厂商博客，2026-06）
URL: https://www.nokia.com/6g/6g-system-architecture-where-innovation-meets-evolution-for-a-more-sustainable-and-connected-world/

### 关键数据点
- Nokia 定义 6G 架构的 4 个设计原则 + 6 个技术框架
- "Data" 是六大技术框架之一

### 关键论断
- "In the 6G ecosystem, collecting, consuming and exposure of data plays a vital role, making consistent data access and efficient data management of utmost importance."
- "6G relies on data as the fuel for AI training, inference, exposure, and monetization, as well as to achieve cognitive autonomy."
- "A lean, secure and holistic data framework is essential"
- Nokia 将数据框架视为 6G 系统级设计的一等公民

---

## [ETSI ZSM GS 029: Data Management Agent for Autonomous Networks]（标准组织，2026-04）
URL: https://portal.etsi.org/webapp/WorkProgram/Report_WorkItem.asp?WKI_ID=78246

### 关键数据点
- 工作项编号 DGS/ZSM-029，2026-04-10 采纳
- 支持组织：China Telecommunications, ZTE Corporation, CAICT, AsiaInfo Technologies Inc
- 当前状态：Work item adopted

### 关键论断
- 规范"自治网络数据管理代理"（Data Management Agent）的功能需求和应用场景
- 功能需求包括：数据注册与发现、数据资产管理、数据认证管理、数据收集与传输管理、数据工作流编排
- 聚焦跨域数据生命周期管理
- 这是 ETSI ZSM 框架中首个专门针对数据管理的规范性工作项

---

## [ETSI ZSM 012: AI Enablers for Network Automation]（标准组织，已发布）
URL: https://www.etsi.org/deliver/etsi_gs/ZSM/001_099/012/01.01.01_60/gs_ZSM012v010101p.pdf

### 关键数据点
- 定义 AI/ML 赋能自动化的管理服务
- 提出数据/动作管道的动态编排

### 关键论断
- "Data is the lifeblood of AI/ML empowered automation"
- 要求：聚合和复用多数据源、基于 AI/ML 模型数据需求收集数据、自动处理以提高数据质量和可信度
- 支持动态编排和管理数据/动作管道（Req-4）
- ZSM 框架中的数据服务实现跨域数据共享

---

## [ETSI ZSM 002: Reference Architecture — Integration Fabric & Data Services]（标准组织，已发布）
URL: https://www.etsi.org/deliver/etsi_gs/ZSM/001_099/002/01.01.01_60/gs_zsm002v010101p.pdf

### 关键数据点
- ZSM 框架由分布式管理和数据服务组成，通过集成编织（Integration Fabric）整合
- 跨域数据服务（Cross-domain data service）实现跨域数据共享

### 关键论断
- "Data services provide means of data persistence and enable data sharing with authorized consumers within and across management domains"
- 数据服务将数据持久化与数据处理解耦，使管理功能无状态化
- Integration Fabric 本质上是管理层面的"数据编织"概念雏形

---

## [6G-TWIN: NDT Architecture with Data Fabric]（学术/EU项目，2025-2026）
URL: https://ion-turcanu.net/publication/faye2026reference/faye2026reference.pdf

### 关键数据点
- 6G-TWIN EU 项目发布 NDT 参考功能架构
- 明确使用"data fabric"术语描述分布式数据存储

### 关键论断
- "Data storage follows a distributed design, where each network component maintains its own local repository, collectively forming a data fabric that ensures scalability, resilience, and fault tolerance."
- 分布式存储库联邦化为统一框架，实现异构数据源的统一访问
- 架构包含 Telemetry Data Layer (TDL) 和 Unified Data Repository (UDR)
- Data Communication Buses (DCBs) 确保域间可靠的自适应数据流

---

## [Digital-twin-enabled 6G network autonomy — Data Fabric Technology]（学术期刊，2025-05）
URL: https://digitaltwin1.org/articles/2-16

### 关键数据点
- 发表于 Digital Twin 开放获取平台
- 明确提出将数据编织技术应用于 6G 网络和数字孪生网络

### 关键论断
- "Data Fabric is defined as a design concept that serves as an integrated layer (fabric) of data and connecting processes"
- 列举数据编织核心能力：数据增强目录、语义知识图谱、主动元数据、推荐引擎、数据准备和交付、数据编排、DataOps
- "We propose to apply data fabric technology to 6G networks and the digital twin networks"
- 需要研究如何构建灵活可复用的异构数据集成管道和实时 ML 训练机制

---

## [CANDIL: A Federated Data Fabric for Network Analytics]（学术论文，2024-09）
URL: https://www.sciencedirect.com/science/article/pii/S0167739X24001420

### 关键数据点
- 发表于 Future Generation Computer Systems, Volume 158
- 使用 ETSI NGSI-LD 标准实现联邦知识图谱
- 开发基于开源技术的全容器化原型

### 关键论断
- 设计联邦数据编织架构，集成边缘和云的网络遥测数据
- 基于 LOT 方法论创建网络分析本体，从标准 YANG 数据模型派生
- 作者 Diego R. Lopez 是 ETSI ISG ZSM 主席
- 将数据编织概念直接应用于电信网络分析场景

---

## [6G-DALI: Federated Dataspace for 6G]（学术/EU项目，2026-02）
URL: https://arxiv.org/html/2602.16386

### 关键数据点
- SNS JU Horizon Europe 项目，Grant Agreement No 101192750
- 架构包含 Data Space + Data Lake 双核心

### 关键论断
- 联邦化、安全、语义丰富的框架，支持 6G 网络中的可信数据共享和 AI 实验
- 包含目录（数据集/服务/ML 模型）、市场、App Store、治理模块
- 语义互操作通过词汇中心（Vocabulary Hub）和 Schema 层实现
- 数据湖通过 dataspace connectors 执行策略控制的数据传输

---

## [ROBUST-6G: Knowledge Graph within Data Fabric]（EU项目交付件，2025-01）
URL: https://robust-6g.eu/wp-content/uploads/2025/01/ROBUST-6G-D2.2_v1.0-1.pdf

### 关键论断
- "A cornerstone of the ROBUST-6G architecture is its integration of a knowledge graph within the data fabric"
- 知识图谱支持 6G dataspace 的语义互操作和数据发现
- 6G dataspace 建立在 Data Fabric 和 Data Lake 基础模块之上

---

## [Ericsson + SAP: Business Data Fabric Deployment]（厂商新闻，2026-05）
URL: https://telconews.co.uk/story/ericsson-builds-sap-data-fabric-to-scale-ai-across-business

### 关键数据点
- Ericsson 在 180 个国家运营，承载全球 40%+ 移动数据流量
- 部署 SAP Business Data Cloud 作为统一数据编织

### 关键论断
- "Once you scale AI, it stops being an AI problem and becomes a data problem. That's why we invested early in a business data fabric."
- 联邦架构：数据保留在源系统，语义/治理/策略中央管理
- Ericsson 自身的数据编织实践验证了该架构对电信企业的适用性

---

## [PwC Global Telecom Outlook 2025-2029]（分析机构，2025）
URL: https://www.pwc.com/gx/en/industries/tmt/telecom-outlook-perspectives.html

### 关键论断
- "A semantic data fabric over telemetry, orders, trouble tickets, inventory, topology, and finance — so agents can reason over meaning, not just columns"
- 将语义数据编织视为 Agentic AI 运营的基础设施

---

## [FITEE: 6G Autonomous RAN Empowered by AI]（学术论文，2025）
URL: https://link.springer.com/content/pdf/10.1631/FITEE.2400569.pdf

### 关键论断
- "6G network with a built-in AI capability will leverage the data source and data fabric for AI data storage and transportation"
- 将数据编织定位为 6G 网络 AI 数据存储和传输的基础设施

---

## [Fortune Business Insights: Data Fabric Market]（市场分析，2025）
URL: https://www.fortunebusinessinsights.com/data-fabric-market-105979

### 关键数据点
- 全球数据编织市场规模：2025 年 33.7 亿美元，2026 年 41.1 亿美元，2034 年 164.6 亿美元
- CAGR 约 22%（2026-2034）

---

## [TM Forum IG1356: Data Architecture for AI-enabled Telecom Operations v3.0.0]（标准组织，2024-05）
URL: https://www.tmforum.org/resources/introductory-guide/ig1356-data-architecture-for-ai-enabled-telecom-operations-whitepaper-v3-0-0/

### 关键论断
- TM Forum 现代数据架构项目产出
- 定义 AI 赋能电信运营的数据架构范围和挑战
- 与 ODA 框架对齐
