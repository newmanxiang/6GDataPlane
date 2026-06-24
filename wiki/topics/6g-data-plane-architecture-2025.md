---
title: 6G 数据面整体架构（2025 年共识与分歧）
title_en: 6G Data Plane Architecture - 2025 Consensus and Divergence
slug: 6g-data-plane-architecture-2025
category: topic
status: reviewed
confidence: medium
sources:
  - https://www.huawei.com/en/huaweitech/future-technologies/data-plane-design-ai-native-6g-networks
  - https://www.qualcomm.com/content/dam/qcomm-martech/dm-assets/documents/6G-Foundry-1-Rethinking-the-control-plane.pdf
  - https://publications.aston.ac.uk/id/eprint/48294/3/ArchWG-WhitePaper_v1.3.1-FINAL.pdf
  - https://ar5iv.labs.arxiv.org/html/2103.02823
  - https://www.gtigroup.org/Uploads/File/2023/01/13/u63c154cb7e808.pdf
  - https://www.ngmn.org/wp-content/uploads/250218_Network_Architecture_Evolution_towards_6G_V1.0.pdf
  - https://www.3gpp.org/technologies/sa2-role-rel-19
  - https://www.ericsson.com/en/blog/2025/6/blog-6g-standardization-technology-step-to-publish
  - https://arxiv.org/html/2412.14538v4
  - https://link.springer.com/article/10.1631/FITEE.2400247
  - https://www.engineering.org.cn/engi/EN/10.1016/j.eng.2025.09.005
  - https://hexa-x-ii.eu/wp-content/uploads/2025/06/08-Hexa-X-II-EuCNC-WS-June-2025-E2E-and-network-architecture-enablers.pdf
related:
  - 6g-data-plane
  - 6g-overview
  - user-plane-evolution
  - ai-native-air-interface
  - network-data-analytics
  - imt-2030-usage-scenarios-data-needs
  - 6g-kpi-20-requirements
  - daas-interface-design
  - gtp-u-limitations-6g-alternatives
  - 3gpp-sa2-6g-data-framework-wt5
tags:
  - 6G
  - 数据面
  - 架构
  - DaaS
  - Hexa-X-II
  - 3GPP
  - Qualcomm
  - 中国移动
last_verified: 2026-06-21
owner: agent
---

# 6G 数据面整体架构

## 核心结论（执行摘要）

截至 2025 年底，业界对"6G 必须在传统用户面之外增强数据处理能力"已有共识，但**如何实现**存在根本分歧。至少存在四种架构提案：华为 DaaS 独立数据面（DO/DA/DCP 三组件）、中国移动"三体四层五面"（独立数据面 + 计算面 + 安全面）、Hexa-X-II 数据驱动架构（DataOps/MLOps + 云原生数据面）、以及 Qualcomm "用户面优先"（精简控制面、将数据服务迁移到用户面）。3GPP SA2 于 2025 年 6 月批准 6G 架构研究项（FS_6G_ARC），其中 **WT#5 专题聚焦"统一数据框架"**，正式讨论是否引入独立数据面。**核心分歧在于"增设独立数据面" vs "增强既有用户面"两条路线**，预计 2026–2027 年在 3GPP 中形成初步结论。（信心：中等）

## 1. 现状定义

**6G 数据面**（Data Plane）是指在 6G 网络架构中专门负责"非连接数据"（感知数据、AI 训练/推理数据、网络遥测数据等）的采集、传输、存储与服务化供给的功能平面。它超越了 5G 用户面（UP）仅做"包转发"的定义范畴。

与相邻概念的边界：
- **用户面（User Plane）**：5G 定义的 UP 专注连接性数据传输（PDU 会话、GTP-U 隧道）；数据面概念涵盖 UP 并扩展至非连接数据
- **控制面（Control Plane）**：负责信令与连接管理；数据面处理的数据量远超 CP
- **智能面（Intelligence Plane）**：提供 AI 模型生命周期管理；数据面为其供给数据
- **管理面（Management Plane）**：5G OAM 数据收集（如 MDT/NWDAF）是碎片化的；数据面旨在统一这些机制

## 2. 标准与组织动态（近 3 年）

| 时间 | 里程碑 |
|------|--------|
| 2022-06 | 中国移动首发《6G 网络架构技术白皮书》，提出"三体四层五面"，业界首个系统化 6G 架构设计 |
| 2023-01 | GTI 联合中国移动、华为等发布《6G Native AI Architecture and Technologies White Paper》，明确数据面概念 |
| 2023-03 | 中国移动"三体四层五面"在 IEEE Communications Magazine 发表 |
| 2024-02 | Hexa-X-II D3.2 交付件定义 6G 数据驱动架构，引入 DataOps/MLOps 概念 |
| 2024-03 | Qualcomm 发布 6G Foundry 系列第一篇"Rethinking the Control Plane"，提出用户面优先 |
| 2024-07 | ABI Research 分析报告指出 6G 核心架构轮廓正在形成 |
| 2025-02 | 华为发布 DaaS 技术白皮书，提出 DO/DA/DCP 数据面三组件 |
| 2025-02 | NGMN 发布《Network Architecture Evolution towards 6G》，强调共识尚未达成 |
| 2025-03 | SNS JU 发布 6G 架构白皮书（v1.3），包含"Cloud Native Data Plane"专章 |
| 2025-03 | Hexa-X-II 发布 D3.5（最终架构框架），提出感知数据需独立数据面 |
| 2025-06 | **3GPP SA2 批准 6G 架构研究项 FS_6G_ARC**（TSG#108），WT#5 聚焦统一数据框架 |
| 2025-08 | SA2#170（Gothenburg）开始讨论 WT#5 数据框架范围（文件 S2-2506446） |
| 2025-10 | SA2#171（Wuhan）继续 WT#5 讨论（文件 S2-2508225 合并稿） |
| 2026-01 | 中国移动团队在 Springer 出版《6G Migrates from Communication to XaaS》专著 |

## 3. 关键玩家

### 3.1 主张"独立数据面"阵营

- **华为**：提出 DaaS 概念和专用数据面（DP），设计 DO/DA/DCP 三组件架构；已有原型验证（DCP 延迟较 RocketMQ 降低 65%）
- **中国移动**：提出"五面"架构（控制面 / 用户面 / 数据面 / 计算面 / 安全面），数据面独立于用户面；通过 IEEE ComMag 和 Springer 专著系统阐述
- **中国电信**：提出"三层三域"架构，包含数据融合域
- **中国联通**：提出智能融合绿色可信架构，含感知资源域
- **GTI（全球 TD-LTE 发展倡议）**：联合中国运营商和厂商发布 6G Native AI 白皮书，明确支持独立数据面
- **vivo**：提出基于数据面的统一数据收集框架，含数据面协议栈原型验证

### 3.2 主张"增强用户面"阵营

- **Qualcomm**："用户面优先"（User Plane First），精简控制面至仅保留安全/移动性/会话管理，所有新服务（定位、数据收集、IoT）作为 IP 服务运行在用户面上；强调"G 无关"（G-agnostic）和互联网生态兼容性

### 3.3 中间路线

- **Hexa-X-II / SNS JU（欧洲）**：承认需要"数据面"概念（特别是感知原始 I/Q 数据需独立通道），但架构上更强调 DataOps/MLOps 框架整合而非新增独立功能面；在 D3.5 中建议"6G Core 应基于演进的 5GC"
- **Ericsson**：在 SNS JU 白皮书中参与 Cloud Native Data Plane 章节撰写；标准策略上更倾向演进路线
- **Nokia**：参与 SNS JU 白皮书和 3GPP 联合贡献；倾向模块化增强

### 3.4 运营商联盟视角

- **NGMN**：明确指出"6G 架构共识尚未达成"；强调避免 5G 时代 NSA/SA 多选项复杂性；主张"单一架构"目标；78% 受调研运营商认为自治网络管理和 AI 原生设计是关键驱动力

### 3.5 标准化机构

- **3GPP SA2**：FS_6G_ARC 研究项 WT#5 明确讨论"是否以及如何支持 6G 服务功能与数据消费者/生产者之间的数据交换（研究新数据面 vs 用户面）"
- **ITU-T SG13**：在 IMT-2030 网络架构中承认"五面"概念（包含独立数据面）

## 4. 技术机制（各架构提案对比）

### 4.1 四种主要提案对比

| 维度 | 华为 DaaS | 中国移动"五面" | Hexa-X-II / SNS JU | Qualcomm 用户面优先 |
|------|----------|---------------|---------------------|-------------------|
| **核心理念** | 专用数据面处理非连接数据 | 五个独立功能面全覆盖 | 数据驱动架构 + 云原生 | 精简 CP，扩展 UP |
| **数据面定位** | 独立于 CP/UP 的第三面 | 五面之一（与计算面/安全面并列） | DataOps 框架 + 感知数据通道 | 无独立数据面，服务运行在 UP 上 |
| **关键组件** | DO（数据编排）、DA（数据代理）、DCP（数据通信代理） | SCU（分布式微云单元）、DAN（分布式自治网络） | AIaaS、MLOps、DataOps、SeMF | 模块化 NAS、SBA 扩展至 RAN |
| **数据传输范式** | Pub/Sub 消息模式（无状态） | 多面协同、分层自治 | API 驱动 + CAMARA 暴露 | IP 服务 + 标准互联网协议 |
| **与 5G 关系** | 新增面（变革性） | 新增三面（变革性） | 演进 5GC + 新功能（增量性） | 复用 5G NF + UP 扩展（演进性） |
| **标准化策略** | 推动 3GPP 引入独立数据面 | 推动 3GPP 多面架构 | 输入 3GPP 作为 SNS JU 贡献 | 推动 3GPP 简化 CP |
| **原型验证** | DCP 延迟 ~2ms（65% 降低）、吞吐 2.4 Gbps | DAN 概念验证 | 3 个 System PoC（A/B/C） | 无公开原型数据 |

### 4.2 根本分歧："独立数据面" vs "增强用户面"

这是当前最核心的架构路线分歧：

**独立数据面路线**（华为、中国移动、GTI）的论据：
- 6G 非连接数据量将达 ZB/QB 级，远超 CP/UP 设计承载能力
- 数据拓扑复杂（多源多汇），PDU 会话的点对点模型不适用
- 数据编排需求（AI 工作流、传感器融合）需要专用协调机制
- 类比：5G 将 CP 和 UP 解耦带来了灵活性，6G 应进一步解耦出数据面

**增强用户面路线**（Qualcomm）的论据：
- 利用 IP 协议生态和互联网服务体系，降低开发和运维成本
- 实现"G 无关"服务——可回溯至 5G、可跨 Wi-Fi/有线
- 减少架构复杂度（新增功能面意味着新增接口、协议、互操作要求）
- 云原生部署友好，无需额外硬件

### 4.3 3GPP SA2 WT#5 的关键讨论

3GPP SA2 FS_6G_ARC 研究项将"统一数据框架"列为独立工作任务（WT#5），明确研究范围包括：

- 6G 服务功能与数据消费者/生产者之间的数据交换架构
- 高效的数据发现、收集、存储、处理和暴露机制
- 数据源和消费者的可信认证机制
- 数据可追溯机制
- 高效的数据管理和传输协议

SA2 和 SA5 正在协作：SA5 负责管理数据方面，SA2 负责 AI 数据、感知数据及其他方面。关键问题 #21（KI#21）专门研究"6G 数据框架系统架构"。

## 5. 趋势驱动力

- **AI 原生需求**：AI 模型分布式训练/推理产生海量非连接数据（梯度、参数、token），需要专用传输机制
- **感知融合（ISAC）**：6G 网络兼具雷达功能，感知原始数据（I/Q 信号、点云）的传输方案尚无共识
- **数据量爆发**：华为估算 6G 感知数据量达 ZB 级/天（基站侧），传统会话模型无法承载
- **5G 数据收集痛点**：GTI 白皮书指出 5G 数据收集困难（接口少、格式不统一、质量难保证），推动 6G 从设计阶段解决
- **运营商降本增效**：NGMN 多数运营商将成本效率列为 6G 顶级优先事项，架构简化是关键
- **云原生演进**：SNS JU 强调 6G 需端到端云原生，数据面设计必须适配容器化/微服务部署

## 6. 批评与风险

- **架构碎片化风险**：NGMN 明确警告"6G 架构共识尚未达成"，多种提案并存可能导致 5G NSA/SA 多选项混乱的重演
- **复杂性陷阱**：新增独立数据面意味着新增协议、接口和互操作需求；Qualcomm 认为这会增加 TCO
- **标准化时间压力**：3GPP SA2 6G 研究项完成目标为 2026-12 或 2027-03，留给架构共识的时间有限
- **实施落地差距**：华为 DCP 原型仅验证了消息转发延迟，尚未在端到端网络中验证；中国移动 DAN 概念验证规模有限
- **地缘技术分化**：中国阵营（华为/中国移动/中国电信）倾向独立数据面，美国阵营（Qualcomm）倾向用户面优先，欧洲（Hexa-X-II）居中——可能导致标准化博弈
- **"多面"是否必要**的学术质疑：部分 NGMN 运营商认为"所有新服务都可通过高级 5G 网络实现"，质疑是否需要根本性架构变革

## 7. 我司相关性（占位）

> 待 6g-insight-report 阶段结合 ops/company-context.md 填充。关注点：我司在数据面/用户面转发领域的现有产品与技术能力如何映射到上述架构提案？我司应支持哪条架构路线？

## 矛盾与待核实

### 矛盾 5：独立数据面 vs 增强用户面（根本性路线分歧）

- **主张 A**：6G 需要独立于 CP/UP 的专用数据面（DP）来处理非连接数据 — 来源：华为 DaaS 白皮书 (厂商/2025-02)、中国移动"五面"架构 (IEEE ComMag/2023)、GTI 白皮书 (产业联盟/2023-01)
- **主张 B**：6G 应采用"用户面优先"设计，将新服务迁移到增强的用户面上，无需独立数据面 — 来源：Qualcomm 6G Foundry (厂商/2024-03)
- **现状**：3GPP SA2 WT#5 正在研究此问题，尚无标准结论
- **本调研倾向**：不下结论，双方论据均有支撑
- **何时能解决**：3GPP SA2 6G 研究项完成后（2026-12 或 2027-03）
- **关联章节**：wiki/topics/6g-data-plane-architecture-2025.md §4.2

### 矛盾 6：功能面数量分歧

- **主张 A**：6G 需要 5 个功能面（控制/用户/数据/计算/安全） — 来源：中国移动 (IEEE ComMag/2023)、ITU-T SG13 贡献 (2023-07)
- **主张 B**：6G 保持 2 面（精简 CP + 增强 UP），以模块化方式按需加载新功能 — 来源：Qualcomm (厂商/2024-03)
- **主张 C**：6G 在 5G CP/UP 基础上新增数据面和感知相关功能，但不必引入独立计算面/安全面 — 来源：Hexa-X-II D3.5 (EU 项目/2025-03)
- **现状**：无共识。SA2 WT#5 仅聚焦数据框架，未扩展至计算面/安全面的讨论
- **本调研倾向**：不下结论
- **何时能解决**：3GPP SA2 研究期间（2025-08 至 2027-03）
- **关联章节**：wiki/topics/6g-data-plane-architecture-2025.md §4.1

## 数据缺口

1. **3GPP SA2 WT#5 技术报告内容**：SA2 讨论文稿（S2-2506446 等）仅目录可见，正文需 3GPP 会员账号访问（P1）
2. **华为 DCP 端到端网络验证数据**：当前仅有消息转发层面的原型数据，缺乏与 RAN/CN 集成的端到端验证（P1）
3. **Qualcomm 用户面优先的定量分析**：Qualcomm 主张降低 TCO，但未公开 TCO 对比数据（P1）
4. **中国移动 DAN 实测数据**：分布式自治网络概念验证规模和性能数据未公开（P2）
5. **运营商对各架构提案的偏好调研**：NGMN 调研仅涉及高层设计原则，未具体到"独立数据面 vs 增强 UP"的选择（P1）
6. **3GPP SA2 2026 下半年讨论结果**：WT#5 的关键方案比较和初步结论预计 2026 年形成（P0，需持续跟踪）

## 来源

### 一手资料 / 官方
1. [3GPP SA2 FS_6G_ARC FTP 目录](https://www.3gpp.org/FTP/tsg_sa/WG2_Arch/TSGS2_170_Goteborg_2025-08/INBOX/DRAFTS/FS_6G_ARC) — SA2#170 6G 架构研究文稿目录，含 WT#5 数据框架讨论
2. [SA2 Roles & Responsibilities: 6G](https://www.3gpp.org/technologies/sa2-role-rel-19) — 3GPP SA2 官方 6G 工作计划说明
3. [ITU-T SG13 6G Architecture Contribution](https://www.itu.int/en/ITU-T/Workshops-and-Seminars/2023/0724/Documents/LuLuV2.pdf) — 中国移动向 ITU-T 提交的"三体四层五面"架构提案

### 厂商白皮书
4. [Huawei: Data Plane Design for AI-Native 6G Networks](https://www.huawei.com/en/huaweitech/future-technologies/data-plane-design-ai-native-6g-networks) — DaaS 概念和 DO/DA/DCP 架构设计，2025-02
5. [Qualcomm 6G Foundry: Rethinking the Control Plane](https://www.qualcomm.com/content/dam/qcomm-martech/dm-assets/documents/6G-Foundry-1-Rethinking-the-control-plane.pdf) — 用户面优先设计提案，2024-03
6. [Qualcomm: Designing 6G for AI-Driven Future](https://www.qualcomm.com/content/dam/qcomm-martech/dm-assets/documents/Enabling-scalable-mobile-connectivity-for-our-AI-driven-future.pdf) — 6G 架构详细设计，含模块化 NAS 和 UP 扩展方案

### 产业联盟 / EU 项目
7. [SNS JU: Towards 6G Architecture - Key Concepts, Challenges, and Building Blocks](https://publications.aston.ac.uk/id/eprint/48294/3/ArchWG-WhitePaper_v1.3.1-FINAL.pdf) — 欧洲 6G 架构白皮书 v1.3.1，含 Cloud Native Data Plane 专章，2025-05
8. [GTI: 6G Native AI Architecture and Technologies White Paper](https://www.gtigroup.org/Uploads/File/2023/01/13/u63c154cb7e808.pdf) — 数据面概念的早期定义和产业共识，2023-01
9. [NGMN: Network Architecture Evolution towards 6G](https://www.ngmn.org/wp-content/uploads/250218_Network_Architecture_Evolution_towards_6G_V1.0.pdf) — 运营商联盟架构演进框架，2025-02
10. [Hexa-X-II D3.5 Announcement](https://hexa-x-ii.eu/hexa-x-ii-unveils-deliverable-d3-5-advancing-the-6g-architectural-framework/) — 最终架构框架交付件说明，2025-03

### 学术
11. [Liu et al.: Toward Native AI in 6G Networks (arXiv:2103.02823)](https://ar5iv.labs.arxiv.org/html/2103.02823) — 独立数据面和智能面的早期学术提案，中国移动研究院
12. [Overview of AI and Communication for 6G Network (arXiv:2412.14538)](https://arxiv.org/html/2412.14538v4) — 综合调研含中国三大运营商 6G 架构方案对比
13. [vivo: A Unified Data Collection Framework Based on the Data Plane for 6G](https://link.springer.com/article/10.1631/FITEE.2400247) — 数据面协议栈原型与双端数据收集验证，FITEE 2025-03
14. [A Task-Driven Design Approach for 6G AI-Native Architecture](https://www.engineering.org.cn/engi/EN/10.1016/j.eng.2025.09.005) — 任务驱动 6G AI 原生架构设计方法论，Engineering 2026-01

### 分析机构 / 媒体
15. [Ericsson: 6G Standardization - Technical Studies Starting](https://www.ericsson.com/en/blog/2025/6/blog-6g-standardization-technology-step-to-publish) — 3GPP 6G 技术研究启动解读，2025-06
16. [ATIS Webinar: 3GPP Release 20 Update on 6G Studies](https://www.youtube.com/watch?v=mT5q_9uz9rM) — SA2 WT#5 数据框架讨论进展报道，2026-04
