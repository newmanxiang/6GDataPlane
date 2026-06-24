# 精读笔记：6G 跨域数据治理与数据编织融合

> 搜索日期：2026-06-24
> 搜索工具：Exa (web_search_exa) + Firecrawl (firecrawl_search)
> 精读数量：14 篇

---

## 1. 6G-TWIN D2.1: Data Governance, Privacy, and Harmonization (2025-12)

- **URL**: https://6g-twin.eu/wp-content/uploads/2025/12/6G-TWIN-D2.1-Deliverable-Data-governance-privacy-and-harmonization-final.pdf
- **类型**: EU SNS JU 项目交付件
- **核心内容**:
  - 提出 6G 网络数字孪生（NDT）场景下的全面数据治理、隐私和统一框架
  - 定义统一 NDT 数据空间（unified NDT data space），负责数据管理和网络生成数据分类
  - 包含数据和谐化（harmonization）和聚合层——清洗和标准化来自异构域/节点的数据输入
  - 考虑联邦环境中的互操作性和法规合规
  - 提出治理、存储和物理-虚拟访问策略
  - 包含隐私和安全机制
- **与本题相关性**: ⭐⭐⭐ 直接定义了 6G 跨域数据治理框架，是最直接的一手来源

## 2. 6G-DALI: Towards Secure and Interoperable Data Spaces for 6G (arXiv 2602.16386)

- **URL**: https://arxiv.org/html/2602.16386
- **类型**: EU SNS JU 项目论文
- **核心内容**:
  - 实现联邦数据空间（federated dataspace）和 DataOps 基础设施
  - 支持安全、合规、可扩展的 AI 驱动实验和服务编排数据共享
  - 基于 GAIA-X 和 IDSA 原则设计
  - 双层设计：Data Space（元数据治理）+ Data Lake（大规模数据处理）分离
  - 联邦身份管理、基于策略的数据合约、自动化数据管道
  - 与 EU Data Governance Act、Data Act、Digital Services Act 对齐
  - 集成 RAN 模型管理、测试平台连接器和策略治理
- **与本题相关性**: ⭐⭐⭐ 展示数据编织+治理在 6G 研究场景中的具体实现

## 3. Ericsson: Future-proof Data Management for AI Networks (2025/2026 白皮书)

- **URL**: https://www.ericsson.com/en/reports-and-papers/white-papers/future-proof-data-management-for-ai-networks
- **核心内容**:
  - CSP 数据管理架构需要战略性增强——原生预期域碎片化、保障无缝安全交换、保证多代理系统就绪
  - 数据岛（Data Islands）+ 数据网格（Data Mesh）模式用于远程分布式数据管理
  - 数据治理原则需在本地岛和全局网格两个层级实现
  - 语义互操作：利用本体和知识图谱实现跨 RAN/Core/OSS/BSS/CX 系统的跨域推理
  - 语义中介引擎将多域数据映射到统一知识模型
  - 参考架构四部分：数据源 → 数据摄入 → 数据精炼与治理 → 数据消费支撑
  - 治理需要贯穿数据摄入、存储、处理、共享和分析全链路
- **与本题相关性**: ⭐⭐⭐ Ericsson 对跨域数据治理的权威立场，直接映射到数据编织架构

## 4. Nokia: Data Mesh and Distributed Data Architecture for Telco Networks (白皮书)

- **URL**: https://www.nokia.com/asset/f/214288/
- **核心内容**:
  - 联邦计算治理：包含与组织政策和监管要求对齐的标准和策略集
  - Data Fabric 嵌入治理框架——强制数据质量、安全和合规，提供数据血缘可见性
  - 电信自治网络需要强健且可扩展的数据治理框架处理动态分布式数据
  - 联邦治理使各网段（RAN/Core）自主管理数据，同时遵守全局标准
  - 安全与合规：在域级别实现自动化合规检查和安全协议
  - 协作与协调：跨域数据倡议的最佳实践共享
- **与本题相关性**: ⭐⭐⭐ Nokia 明确将联邦治理与 Data Fabric 结合应用于电信自治网络

## 5. 3GPP SA5 TS 32.801: 6G Management and Orchestration Study

- **URL**: https://itecspec.com/3gpp/32.801-01
- **核心内容**:
  - 定义 6G OAM 数据管理框架（DMFW）
  - KI#1: DMFW 能力研究
  - KI#2: 数据和知识管理（知识/语义表征与管理、数据管理概念和术语）
  - 涵盖管理架构原则、AI agent 概念、云方面
  - 包含运营商设计原则附录
- **与本题相关性**: ⭐⭐⭐ 3GPP SA5 对 6G 数据治理的官方标准化入口

## 6. 3GPP SA5 Rel-20 6G OAM 工作领域讨论文稿

- **URL**: https://www.3gpp.org/ftp/Email_Discussions/SA5/SA5-level%20discussions/SA5%23161/SA5_NWM_Discussion_for_Rel-20_6G_OAM_Work_Areas-v0.0.7.pdf
- **核心内容**:
  - WT-7: 研究统一数据管理框架，支持不同管理数据类型
  - 数据管理覆盖：数据收集控制/报告、数据处理、数据分析、数据注册、数据发现、数据访问控制、数据发布、数据分发、数据暴露、数据编目、数据销毁（EOL）、数据质量报告、变更管理
  - WT-4: 研究非 3GPP 数据/方案（如 O-RAN）是否/如何被 3GPP 标准支持
  - WT-5: 研究是否/如何复用增强现有用户同意机制支持 6G 数据管理
- **与本题相关性**: ⭐⭐⭐ 直接反映 3GPP 对 6G 数据治理的具体工作方向

## 7. Network Data Sharing: Governance Framework (Optica JOCN, 2025-11)

- **URL**: https://opg.optica.org/jocn/abstract.cfm?uri=jocn-17-11-1019
- **核心内容**:
  - 利用 Eclipse Dataspace Components Connector 实现策略驱动的遥测数据交换
  - 多利益方电信生态中的安全、合规、主权数据共享
  - 高级匿名化机制和动态策略执行控制
  - 基于 IDSA 原则的两个新数据模型词汇表
  - 在 Fraunhofer HHI SDN 光子测试平台上实验验证
  - 性能分析：治理框架与传统不合规方案的延迟/通信开销对比
- **与本题相关性**: ⭐⭐⭐ 数据主权治理框架的实际实现和性能验证

## 8. Fraunhofer HHI: Telco Data Space

- **URL**: https://www.hhi.fraunhofer.de/en/telco-data-space.html
- **核心内容**:
  - 实现运营商、供应商、研究生态间的可信策略执行数据交换
  - 基于数据主权原则，支持 AI 驱动自动化、互操作性和新服务模式
  - 用例：跨测试平台数据交换、跨运营商服务供应、跨供应商 O-RAN 优化、运营商到供应商预测维护
  - 数据空间连接器（DSC）引入治理层：所有权感知交换、策略执行、联邦目录、实时性能数据暴露
  - 对齐 Gaia-X 和 IDSA 原则
- **与本题相关性**: ⭐⭐ 电信跨域数据治理的具体工业实践

## 9. Deutsche Telekom MARA 架构蓝图 (2026)

- **URL**: https://mara-tech-blueprint-fa2be5.pages.devops.telekom.de/blueprint/
- **参考**: https://inform.tmforum.org/features-and-opinion/why-governance-is-key-to-deutsche-telekoms-new-ai-architecture
- **核心内容**:
  - MARA = Magenta AI-centric Reference Architecture
  - 七层架构含"治理、信任与控制"层
  - Data as a Product——数据被作为受管治理产品对待，有明确所有权、合约和生命周期
  - MARA-Run 提供运行时治理：策略即代码、上下文感知授权、护栏、可观测性
  - 覆盖 agent 执行、编排流、工具调用、模型使用、数据访问的策略执行
  - 2026年4月获 P&T 领导层背书为集团生产级 AI 参考蓝图
  - 强调 EU AI Act 合规、安全护栏、供应商锁定规避
- **与本题相关性**: ⭐⭐⭐ 顶级运营商的 AI 时代数据治理实践蓝图

## 10. ETSI ISG PDL: Cross-Domain Data Governance (GS PDL 034)

- **URL**: https://www.lfdecentralizedtrust.org/blog/blockchain-enabled-trust-in-6g
- **核心内容**:
  - ETSI ISG PDL（许可分布式账本）正在制定跨域数据治理规范 GS PDL 034
  - 可信数据空间和跨域数据治理——覆盖电信、垂直行业、云和监管数据空间
  - 提供出处证明、访问策略执行、可互操作信任基础设施
  - 配合 GS PDL 033（AI/ML 模型出处和 O-RAN 安全）
  - 利用区块链/DLT 实现跨域审计性和策略控制
- **与本题相关性**: ⭐⭐ ETSI 对 6G 跨域数据治理的具体标准化工作

## 11. SNS JU 6G Architecture Whitepaper v1.3 (2025-05)

- **URL**: https://smart-networks.europa.eu/wp-content/uploads/2025/06/archwg-whitepaper-v1.3-final-23may_clean.pdf
- **核心内容**:
  - 数据管理框架集成 DataOps 在确保有效数据收集、处理、治理和数据质量方面发挥关键作用
  - 当前蜂窝网络的隐私、安全和数据表示方法不足以满足全球连接和 IoT 需求
  - 改进的数据治理和高质量数据供给对支持高级网络智能至关重要
  - 跨多域、多利益方、异构技术平台的网络应用管理
  - 更广泛的安全和隐私框架需要端到端设计
- **与本题相关性**: ⭐⭐⭐ 欧盟 6G 架构官方立场中的数据治理需求

## 12. O-RAN nGRG: Cross-domain AI Research Report (2024)

- **URL**: https://mediastorage.o-ran.org/ngrg-rr/nGRG-RR-2024-02-O-RAN%20Cross-domain%20AI%20v1.6.pdf
- **核心内容**:
  - 跨域数据分析服务利用 AI/ML 分析泛在数据
  - 提供端到端分析报告和优化建议
  - 研究跨 RAN-Core-Transport 域的 AI 协同
- **与本题相关性**: ⭐⭐ O-RAN 跨域 AI 数据需求反映治理挑战

## 13. CANDIL: A Federated Data Fabric for Network Analytics (ScienceDirect, 2024)

- **URL**: https://www.sciencedirect.com/science/article/pii/S0167739X24001420
- **核心内容**:
  - 设计联邦数据编织架构——集成边缘和云的网络遥测数据
  - 使用 ETSI NGSI-LD 标准实现联邦知识图谱
  - 为网络分析创建本体，遵循 LOT 方法论，源自标准 YANG 数据模型
  - 全容器化开源原型
  - 作者来自 Telefónica + Universidad Politécnica de Madrid
  - 一作在 IETF 和 ETSI 标准化活动中参与
  - Diego R. Lopez 目前担任 ETSI ISG ZSM 主席
- **与本题相关性**: ⭐⭐⭐ 电信数据编织+治理的学术实现，与 ETSI ZSM/NGSI-LD 直接关联

## 14. TM Forum Data Governance Framework

- **URL**: https://www.tmforum.org/data-governance-framework/
- **参考**: https://www.tmforum.org/playbook/modern-data-governance/
- **核心内容**:
  - 现代灵活数据治理框架——规定决策权和责任
  - 确保数据的可用性、质量和合规
  - Data Governance Maturity Model v3.0.0 (GB1025) 提供流程、人员和技术维度的成熟度评估
  - Modern Data Governance Masterclass 培训系列
  - 与 ODA 和 Modern Data Architecture 项目集成
- **与本题相关性**: ⭐⭐⭐ 电信行业数据治理的事实标准框架

## 15. IDSA Position Paper: Unified Sovereign Digital Infrastructure (2025/2026)

- **URL**: https://internationaldataspaces.org/wp-content/uploads/dlm_uploads/IDSA-Position-Paper-Establishing-a-Unified-sovereign-and-open-digital-infrastructure-1.pdf
- **核心内容**:
  - 电信运营商在数据空间中提供基础信任基础设施
  - 标准化 API 实现互操作、可信数字身份、跨境合规治理框架
  - T-Systems 与 NTT Communications 合作日欧数据空间测试环境
  - Dataspace Protocol (DSP) 实现参与者间完全互操作
  - 数据主权：参与者保留对数据的控制权
- **与本题相关性**: ⭐⭐ 运营商在跨域数据治理中的产业定位

---

## 综合发现

### 关键技术框架映射

| 标准/框架 | 组织 | 跨域治理角色 | 成熟度 |
|---|---|---|---|
| DMFW (Data Management Framework) | 3GPP SA5 | OAM 层数据治理 | 研究中 (Rel-20) |
| WT#5 数据框架 | 3GPP SA2 | 核心网层数据治理 | 研究中 (Rel-20) |
| ZSM 跨域管理 | ETSI | 端到端自治网络治理 | 成熟 (Rel-1/2) |
| GS PDL 034 | ETSI PDL | 区块链跨域治理 | 制定中 |
| Data Governance Framework | TM Forum | 运营治理成熟度 | 成熟 (v3.0) |
| ODA + MDA | TM Forum | 运营数据架构治理 | 部署中 |
| IDSA/GAIA-X 数据空间 | EU | 主权数据交换治理 | 原型阶段 |
| NGSI-LD 知识图谱 | ETSI | 语义互操作治理 | 成熟标准 |

### 核心矛盾发现

1. SA2 WT#5 vs SA5 DMFW 在数据治理职责上的交叉——两者都涉及数据管理/暴露/访问控制
2. 联邦治理（去中心化自治）vs 统一治理框架（全局一致性）在电信跨域场景的张力
3. 数据主权法规碎片化（GDPR vs 中国数据安全法 vs 各国本地化要求）vs 跨域数据流动需求

### 数据缺口发现

1. 中国运营商 6G 数据治理方案缺乏公开英文文献（中国移动/联通/电信）
2. 跨域数据治理框架的性能开销量化数据稀缺（仅 Fraunhofer HHI 有初步数据）
3. 3GPP SA5 DMFW 与 SA2 WT#5 的正式分工协议尚未发布
4. 数据编织架构在跨域治理中的具体集成规范不存在标准文档
