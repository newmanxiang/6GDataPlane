---
title: DaaS 接口设计：6G 数据面的数据服务暴露
title_en: DaaS Interface Design - Data Service Exposure in 6G Data Plane
slug: daas-interface-design
category: topic
status: reviewed
confidence: medium
sources:
  - https://www.huawei.com/en/huaweitech/future-technologies/data-plane-design-ai-native-6g-networks
  - https://jzus.zju.edu.cn/opentxt.php?doi=10.1631%2FFITEE.2400247
  - https://research.samsung.com/blog/AI-in-6G-network-Service-and-System-Aspect
  - https://www.gtigroup.org/Uploads/File/2023/01/13/u63c154cb7e808.pdf
  - https://smart-networks.europa.eu/wp-content/uploads/2025/06/archwg-whitepaper-v1.3-final-23may_clean.pdf
  - https://www.nokia.com/asset/i/212403/
  - https://www.3gpp.org/technologies/ct3-exp-fr-apis
  - https://itecspec.com/3gpp/23.801-01
  - https://arxiv.org/html/2509.01276v1
  - https://www.patents-review.com/a/20250097313-communication-method-apparatus-system.html
  - https://arxiv.org/html/2507.08164v1
  - https://arxiv.org/html/2606.11877
  - https://www.oreateai.com/blog/research-white-paper-on-6g-ai-data-service-framework-and-enabling-technologies/f376eaadd386322abf9e97441848ef51
related:
  - 6g-data-plane
  - 6g-data-plane-architecture-2025
  - imt-2030-framework-data-needs
  - network-data-analytics
  - data-orchestration
  - user-plane-evolution
  - gtp-u-limitations-6g-alternatives
tags:
  - DaaS
  - 6G
  - 数据面
  - 接口设计
  - API
  - 数据服务
  - Pub/Sub
  - DO
  - DA
  - DCP
last_verified: 2026-06-21
owner: agent
---

# DaaS 接口设计：6G 数据面的数据服务暴露

## 核心结论（执行摘要）

6G DaaS（Data as a Service）接口设计正在从 5G NWDAF 的"订阅-通知"被动模式，向"发布/订阅（Pub/Sub）+ 数据编排"的主动数据服务模式演进。华为提出的 DO/DA/DCP 三组件架构是当前最具体的接口设计方案：DO 通过数据流引擎编排数据拓扑，DA 在各网络节点执行数据采集/处理，DCP 以无状态 Pub/Sub 消息代理实现多对多数据分发（原型验证延迟 ~2ms，较 RocketMQ 降低 65%）。3GPP SA2 WT#5 正在研究 6G 统一数据框架（KI#21），三星等厂商指出 5G CP 和 UP 均无法有效承载 AI/感知数据，需要新的数据服务接口。但具体 API 范式（RESTful SBA 扩展 vs Pub/Sub vs gRPC 流式）尚未形成标准共识，预计 2026-2027 年在 3GPP 中初步收敛。（信心：中等）

## 1. 现状定义

**DaaS 接口**是指 6G 数据面向智能面、应用层及其他网络功能暴露数据服务的标准化交互界面。其核心目标是将网络中的非连接数据（AI 数据、感知数据、管理数据）以"服务化"方式提供给数据消费者。

与相邻概念的边界：
- **数据面接口 vs 控制面 SBI**：5G 控制面 SBI 基于 HTTP/2 RESTful API（TS 29.500），承载小数据包短连接信令；DaaS 接口需承载大数据量、多拓扑、异步数据流
- **DaaS 接口 vs NWDAF Nnwdaf 接口**：Nnwdaf 是 5G 分析服务的请求-响应/订阅-通知接口，仅输出分析结果；DaaS 接口暴露原始数据、处理后数据及数据编排能力
- **DaaS 接口 vs NEF 数据暴露**：NEF 向外部 AF 暴露网络能力（通过 CAPIF 框架）；DaaS 接口面向网络内部跨域数据交换和外部数据服务双重需求

## 2. 标准与组织动态（近 3 年）

| 时间 | 里程碑 |
|------|--------|
| 2023-01 | GTI 白皮书首次定义 6G 数据面逻辑功能架构，明确数据服务需"开放接口供外部访问" |
| 2023-07 | 中国移动向 ITU-T SG13 提交"五面"架构，数据面包含数据采集、存储、访问、共享等服务接口 |
| 2024-07 | 中国移动 Lu Lu 向 ITU-T 提交"Data Plane enabled datasets for AI-native network"，阐述数据面数据集服务接口 |
| 2025-02 | 华为发布 DaaS 技术白皮书，定义 DO/DA/DCP 三组件及 Pub/Sub 消息接口架构 |
| 2025-03 | vivo/ZJU 发表基于数据面的统一数据收集框架论文（FITEE），定义 DSAP 协议栈和 DPRB 无线承载 |
| 2025-03 | Huawei Technologies 公开 US20250097313A1 专利，详述 DO-DA 接口交互流程和数据管道编排方法 |
| 2025-05 | SNS JU 架构白皮书 v1.3 定义 CCREF（Communication & Computing Resources Exposure Function），扩展 5G NEF 至资源/能力暴露 |
| 2025-06 | 3GPP SA2 批准 FS_6G_ARC 研究项，WT#5 专门研究 6G 数据框架，含数据暴露、发现、收集等 |
| 2025-08 | SA2#170 讨论 WT#5 数据框架范围文稿 S2-2506446，明确研究"数据收集/分发/处理/存储/暴露" |
| 2026-01 | 三星发文阐述 6G AI 数据框架，指出 5G CP/UP 均无法承载 AI 数据，需统一数据框架 |

## 3. 关键玩家

### 3.1 DaaS 接口提案方

- **华为**：最完整的接口设计方案——DO 编排数据拓扑，DA 执行数据处理，DCP 以 CRT（中国剩余定理）算法实现无状态 Pub/Sub 消息代理。已有原型验证和专利布局（US20250097313A1）
- **vivo / 浙江大学**：提出 DSAP（数据服务应用协议）协议栈，包含 DCF（数据控制功能）、DPSF（数据处理子功能）、DRF（数据路由功能）等，定义 DPRB（数据面无线承载）实现灵活优先级数据传输。UE 原型验证显示处理延迟增益随数据包增大更显著

### 3.2 数据框架演进方

- **三星**：在 3GPP SA2 推动 6G 数据框架研究（KI#21），明确指出 5G NWDAF 集中式设计的三大局限——数据收集负载高（须通过 CP 传输）、NWDAF 是可选 NF（非原生设计）、缺乏跨域 AI 操作支持
- **Nokia**：提出"发布/订阅模式或事件流"替代 5G 核心网的订阅-通知机制，专门应对海量数据交换需求
- **Ericsson**：在 SNS JU 白皮书中参与"Cloud Native Data Plane"章节，强调 6G 核心网将复用 5G SBA 框架并升级至 HTTP/3 或 QUIC

### 3.3 暴露框架演进方

- **3GPP CT3**：维护 CAPIF（Common API Framework）和 NEF 暴露框架。Rel-19/20 已支持 23 个分析服务 ID、DCCF（数据收集协调功能）、MFAF（消息框架适配功能）
- **GSMA / CAMARA**：定义运营商平台 API 标准化暴露框架（OPG.02），6G 预计整合至统一暴露框架
- **Lenovo（SA6）**：提议 Rel-20 研究"Service-oriented 6G Exposure framework"，推动 G-agnostic 统一暴露能力

## 4. 技术机制

### 4.1 DaaS 接口架构：DO/DA/DCP 三组件

**数据编排器（DO）** 四大组件：
1. **DA 注册**：记录各 DA 的数据服务能力（采集/处理/存储/转发），支持资源发现
2. **数据流引擎**：基于服务需求确定数据操作序列（过滤→聚合→转发）
3. **数据流管理**：监管数据包在编排拓扑中的实际路由，考虑拥塞/时延/资源可用性
4. **策略控制**：数据安全、访问控制和隐私策略决策

**数据代理（DA）** 两种实现：
- **嵌入式 DA**：嵌入现有 NE（UE/BS/CN），负责数据采集和预处理
- **独立式 DA**：专用部署，含数据处理功能（DPF）和数据存储功能（DSF）

**数据通信代理（DCP）** 两种模式：
- **有状态 DCP**：维护订阅/主题转发表，表查询路由（类似传统消息队列）
- **无状态 DCP**（华为推荐）：基于 CRT 模数运算的带内信息转发，无需本地状态表。DO 将数据拓扑编码为模数集合，嵌入数据包头部，DCP 执行简单模运算即可确定下游节点

### 4.2 API 范式对比

| 范式 | 5G 现状 | 6G DaaS 提案 | 优势 | 局限 |
|------|---------|------------|------|------|
| **RESTful（HTTP/2）** | SBI 标准范式（TS 29.500） | 基线延续，可能升级至 HTTP/3 | 生态成熟、OpenAPI 工具链完善、多厂商互操作 | 请求-响应模型不适合大数据量异步传输 |
| **Pub/Sub 消息** | DCCF/MFAF 消息框架（Rel-17+） | 华为 DCP 主推，Nokia 也建议采用 | 解耦生产者-消费者、支持多对多拓扑、天然异步 | 需新协议/NF，与现有 SBA 集成复杂度高 |
| **gRPC 流式** | 未纳入 3GPP CP（仅 gNMI 用于网管遥测） | SNS JU 建议支持多协议（REST/gRPC/gNMI） | 高吞吐、双向流、Protocol Buffers 高效编码 | 浏览器支持有限、与 3GPP SBI 不兼容 |
| **事件驱动** | NWDAF 订阅-通知（EventExposure 系列服务） | 扩展至全域事件流（含 RAN 和 UE） | 实时性强、按需推送 | 大规模事件风暴管控复杂 |
| **意图驱动** | 无 | SA2 6G 研究（SA6 Intent-based exposure） | 抽象层次高、开发者友好 | 意图解析准确性待验证 |

### 4.3 与 5G NWDAF 数据暴露接口的本质区别

| 维度 | 5G NWDAF/NEF（Rel-17/19） | 6G DaaS 接口（提案） |
|------|--------------------------|-------------------|
| **暴露内容** | 分析结果（Analytics ID，23 个）、事件通知 | 原始数据 + 处理后数据 + 数据编排能力 + AI 模型参数 |
| **数据流向** | NF→NWDAF→消费者（线性） | 任意拓扑（多源多汇，DO 编排） |
| **交互模式** | 请求-响应 / 订阅-通知 | Pub/Sub / 流式 / 事件驱动 / 意图驱动 |
| **协议** | HTTP/2 RESTful（SBI） | Pub/Sub 消息 + 增强 SBA + 新 DP 协议栈（DSAP） |
| **数据类型** | 网络事件和性能指标 | 四类数据（通信/感知/AI/管理） |
| **AI 支持** | NWDAF 集中式 ML 训练/推理 | 分布式 AI，各 NF 可自主训练/推理/协同 |
| **数据收集** | 各 NF EventExposure 接口（碎片化） | 统一数据收集框架（DSAP/DPRB），数据面协议栈 |
| **跨域能力** | 仅核心网内（RAN 数据需通过 OAM 间接获取） | 端到端跨域（UE-RAN-CN-Cloud），含空口数据面承载 |
| **标准定位** | NWDAF 是可选 NF | 数据框架是 6G 原生设计（Day 1 特性） |

### 4.4 数据面协议栈设计（vivo/ZJU 提案）

vivo/ZJU 提出的 DSAP（数据服务应用协议）包含五个子功能：
- **DCF**（Data Control Function）：数据控制
- **DPSF**（Data Processing Sub-Function）：数据处理
- **DRF**（Data Routing Function）：数据路由
- **DTF**（Data Transmission Function）：数据传输
- **DProcF**（Data Processing Function）：数据压缩（有损/无损算法）

DSAP 通过 RRC 建立 DPRB（数据面无线承载），支持三种类型：
1. 终止于 RAN 节点的承载（RAN 可见数据）
2. RAN 透传承载（RAN 不可见数据）
3. RAN 处理后转发承载（RAN 参与路径上处理）

DPRB 的关键创新是**灵活优先级**——可根据数据量、传输质量需求和用户面流量负载动态调整，避免与信令无线承载（SRB）固定高优先级的冲突。UE 原型验证显示：随数据包长度增加，DP 协议栈在上行处理延迟上的增益愈加显著（因跳过 ASN.1 编解码）。

### 4.5 开源原型与概念验证

| 原型 | 机构 | 技术要点 | 验证结果 |
|------|------|---------|---------|
| 无状态 DCP | 华为 | CRT 模数运算转发，10 broker 并行 | 延迟 ~2ms（vs RocketMQ 降低 65%）；吞吐 128KB 消息 2.4 Gbps |
| DSAP 协议栈 | vivo/ZJU | UE 侧 DP 协议栈原型 | 上行处理延迟优于传统 UP 协议栈，大包增益更显著 |
| 6G 数据收集测试床 | 中南大学/紫金山实验室 | OAI + Open5GS + Kubernetes + Prometheus | 并行数据采集 CPU 降低 32.7%，延迟降低 78.4%（vs Wireshark） |
| LLM-NWDAF | 学术界 | Free5GC + Prometheus + LLM RAG 接口 | 自然语言意图→REST API 调用，支持分析查询和事件订阅管理 |

## 5. 趋势驱动力

- **AI 原生要求统一数据框架**：三星明确指出 5G 的 NWDAF 集中式设计不可延续——NWDAF 是可选 NF、数据收集碎片化、缺乏跨域能力。6G 需要 Day 1 原生的统一数据框架
- **感知数据催生新传输范式**：ISAC 产生的 I/Q 原始数据、点云数据体量巨大，无法通过 CP 小包传输，需 Pub/Sub 或流式接口
- **5G 数据收集痛点**：GTI 白皮书列举 5G 数据收集的五大痛点——接口少、采集周期长（>15 分钟）、格式不统一、质量差（缺失/无标签）、预处理成本高
- **API 经济驱动暴露框架统一**：3GPP CAPIF + GSMA CAMARA + ETSI MEC API 的多头并行需要在 6G 中整合为统一暴露框架
- **分布式 AI 需要新交互模式**：6G AI-enabled NF 需要在本地训练/推理、跨域协同（联邦学习等），要求标准化的 AI 数据交换接口

## 6. 批评与风险

- **Pub/Sub 与 SBA 兼容性风险**：华为 DCP 的无状态 Pub/Sub 模式与 3GPP 现有 SBA（HTTP/2 RESTful）存在范式差异。Ericsson 等厂商倾向在演进的 SBA 框架（HTTP/3 + QUIC）内解决数据传输需求，而非引入全新协议
- **协议栈标准化前景不明**：vivo/ZJU 的 DSAP 协议栈目前仅有学术论文和 UE 原型，3GPP 尚未讨论空口数据面协议栈标准化
- **DO/DA/DCP 仅为华为单一厂商提案**：虽有专利和原型支撑，但尚未获得多厂商背书。3GPP SA2 WT#5 的研究范围是"统一数据框架"，并未预设采用 DO/DA/DCP 架构
- **开源验证规模有限**：华为 DCP 原型仅验证了消息转发层面（10 broker），未在端到端网络中集成 RAN/CN 验证；vivo UE 原型仅验证上行处理延迟
- **意图驱动接口可靠性存疑**：LLM 驱动的意图解析在学术原型中表现良好，但在电信级可靠性要求下，意图歧义处理和失败回退机制尚不成熟
- **多标准组织协调挑战**：DaaS 接口涉及 SA2（架构）、CT3（协议）、SA5（管理数据）、SA6（应用使能）、RAN（空口）多个工作组，跨域协调复杂度高

## 7. 我司相关性（占位）

> 待 6g-insight-report 阶段结合 ops/company-context.md 填充。关注方向：
> - 我司在消息中间件/数据转发领域的技术积累能否对标 DCP？
> - 我司网络设备的数据暴露接口能力（gRPC/gNMI/REST）如何映射到 6G DaaS 接口？
> - 是否应参与 3GPP SA2 WT#5 数据框架标准化？

## 矛盾与待核实

### 矛盾 7：DaaS 接口 API 范式分歧——Pub/Sub vs 增强 SBA

- **主张 A**：6G 数据面需要专用 Pub/Sub 消息接口（DCP），因为 HTTP/2 请求-响应模型无法处理多对多数据拓扑和大数据量异步传输 — 来源：华为 DaaS 白皮书 (厂商/2025-02)、Nokia 6G 数据信息架构 (厂商/2025)
- **主张 B**：6G 应在演进的 SBA 框架（HTTP/3 + QUIC）内支持数据服务，复用 5G 成熟的 RESTful API 生态 — 来源：Ericsson 6G 标准化解读 (厂商/2025-06)、3GPP SA2 基线讨论 (标准/2025)
- **现状**：3GPP SA2 WT#5 尚未就 API 范式做出选择。5G Rel-17 已引入 DCCF/MFAF 消息框架作为中间方案
- **本调研倾向**：不下结论。两种方案可能共存——SBA 延续处理控制类数据交互，Pub/Sub 专用于大数据量数据面传输
- **何时能解决**：3GPP SA2 6G 研究完成后（2026-12 或 2027-03）
- **关联章节**：wiki/topics/daas-interface-design.md §4.2

### 矛盾 8：数据面协议栈是否需要标准化新协议

- **主张 A**：需要新的空口数据面协议栈（DSAP/DPRB），因为现有 UP 协议栈（PDCP/RLC/MAC）为连接数据优化，ASN.1 编解码引入不必要的开销 — 来源：vivo/ZJU FITEE 论文 (学术/2025-03)
- **主张 B**：可通过增强现有 UP 协议栈或在应用层实现数据服务，无需引入新空口协议 — 来源：Qualcomm 用户面优先 (厂商/2024-03)、Ericsson 6G 演进路线 (厂商/2025)
- **现状**：3GPP 尚未讨论空口数据面协议栈标准化
- **本调研倾向**：不下结论
- **何时能解决**：3GPP RAN 6G 研究项推进后（2026+）

## 数据缺口

1. **P0**：3GPP SA2 WT#5 KI#21 数据框架研究的具体方案提案内容——SA2 文稿需 3GPP 会员账号访问
2. **P1**：DO/DA/DCP 接口的具体信令流程和消息格式定义——华为专利有部分描述，但缺乏完整的接口规范
3. **P1**：DSAP 协议栈的完整性能基准测试——当前仅有 UE 侧上行延迟数据，缺乏多节点端到端验证
4. **P1**：运营商对 DaaS 接口范式的偏好调研——NGMN 2025 报告未涉及此级别细节
5. **P2**：6G 数据服务的计费/计量接口设计——DaaS 商业化需要数据合约和定价机制，目前无标准化提案
6. **P2**：DaaS 接口的安全认证机制——DO 如何认证 DA、数据消费者如何获得数据访问授权的具体方案

## 来源

### 一手资料 / 官方
1. [3GPP TR 23.801-01: Study on Architecture for 6G System](https://itecspec.com/3gpp/23.801-01) — SA2 6G 架构研究（含 WT#5 数据框架 KI#21）
2. [SA2 #170 WT#5 Data Framework Scope (S2-2506446)](https://www.3gpp.org/FTP/tsg_sa/WG2_Arch/TSGS2_170_Goteborg_2025-08/INBOX/DRAFTS/FS_6G_ARC) — 数据框架范围讨论文稿目录
3. [3GPP Capability Exposure Frameworks and APIs](https://www.3gpp.org/technologies/ct3-exp-fr-apis) — CAPIF/NEF 暴露框架官方介绍
4. [3GPP OpenAPIs for SBA](https://www.3gpp.org/technologies/openapis-for-the-service-based-architecture) — SBA RESTful API 设计原则

### 厂商白皮书
5. [Huawei: Data Plane Design for AI-Native 6G Networks](https://www.huawei.com/en/huaweitech/future-technologies/data-plane-design-ai-native-6g-networks) — DO/DA/DCP 架构设计和 CRT 无状态消息代理原型，2025-02
6. [Huawei Patent US20250097313A1: Communication Method, Apparatus, and System](https://www.patents-review.com/a/20250097313-communication-method-apparatus-system.html) — DO-DA 数据管道编排方法专利，2025-03
7. [Samsung Research: AI in 6G Network - Service and System Aspect](https://research.samsung.com/blog/AI-in-6G-network-Service-and-System-Aspect) — 6G AI 数据框架和 NWDAF 局限性分析，2026
8. [Nokia: 6G Architecture White Paper](https://www.nokia.com/asset/i/212403/) — 提出 Pub/Sub 替代订阅-通知的数据信息架构，2025
9. [6G AI Data Service Framework White Paper](https://www.oreateai.com/blog/research-white-paper-on-6g-ai-data-service-framework-and-enabling-technologies/f376eaadd386322abf9e97441848ef51) — 6G AI 数据服务框架与使能技术，2026-01

### 产业联盟 / EU 项目
10. [GTI: 6G Native AI Architecture and Technologies White Paper](https://www.gtigroup.org/Uploads/File/2023/01/13/u63c154cb7e808.pdf) — 数据面数据服务接口技术特征，2023-01
11. [SNS JU: Towards 6G Architecture (v1.3)](https://smart-networks.europa.eu/wp-content/uploads/2025/06/archwg-whitepaper-v1.3-final-23may_clean.pdf) — CCREF 暴露功能和 DataOps 框架，2025-05
12. [Ericsson: Set the Right Migration Path to 6G](https://eu-assets.contentstack.com/v3/assets/blt23eb5bbc4124baa6/bltb5e3a312e7120c6b/68b579598e30617a3b2f4117/HR_Set_the_Right_Migration_Path_(September_2025).pdf) — 6G 核心网将复用 5G SBA + HTTP/3，2025-09

### 学术
13. [Yuan et al.: A Unified Data Collection Framework Based on the Data Plane for 6G](https://jzus.zju.edu.cn/opentxt.php?doi=10.1631%2FFITEE.2400247) — DSAP 协议栈和 DPRB 设计，FITEE 2025-03
14. [He et al.: A Real-time Data Collection Approach for 6G AI-native Networks](https://arxiv.org/html/2509.01276v1) — Prometheus 数据服务接口和并行采集架构，2025-09
15. [KP-A: A Unified Network Knowledge Plane for Agentic Network Intelligence](https://arxiv.org/html/2507.08164v1) — REST-style Knowledge Plane API 设计，2025-07
16. [LLM-Enabled NWDAF: A Step Toward AI-Native 6G Network Intelligence](https://arxiv.org/html/2606.11877) — LLM RAG 意图接口→NWDAF REST API 调用，2026-06
17. [Liu et al.: Toward Native AI in 6G Networks (arXiv:2103.02823)](https://ar5iv.labs.arxiv.org/html/2103.02823) — 独立数据面和智能面的早期学术提案
