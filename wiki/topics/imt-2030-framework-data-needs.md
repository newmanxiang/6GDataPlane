---
title: IMT-2030 框架的数据面设计约束
title_en: IMT-2030 Framework - Data Plane Design Constraints
slug: imt-2030-framework-data-needs
category: topic
status: reviewed
confidence: medium
sources:
  - https://www.huawei.com/en/huaweitech/future-technologies/data-plane-design-ai-native-6g-networks
  - https://jzus.zju.edu.cn/opentxt.php?doi=10.1631%2FFITEE.2400247
  - https://www.itu.int/dms_pubrec/itu-r/rec/m/R-REC-M.2160-0-202311-I!!PDF-E.pdf
  - https://www.itu.int/en/ITU-T/Workshops-and-Seminars/2023/0724/Documents/LuLuV2.pdf
  - https://research.samsung.com/blog/AI-in-6G-network-Service-and-System-Aspect
  - https://www.qualcomm.com/content/dam/qcomm-martech/dm-assets/documents/6G-Foundry-1-Rethinking-the-control-plane.pdf
  - https://smart-networks.europa.eu/wp-content/uploads/2025/06/archwg-whitepaper-v1.3-final-23may_clean.pdf
  - https://www.ngmn.org/wp-content/uploads/250218_Network_Architecture_Evolution_towards_6G_V1.0.pdf
  - https://www.ietf.org/archive/id/draft-zzhang-dmm-mup-evolution-09.html
  - https://www.lightreading.com/6g/ericsson-has-pinned-its-6g-hopes-on-ais-rising-uplink-demands
  - https://www.aethaconsulting.com/ai-and-the-new-uplink-challenge-how-mobile-traffic-patterns-are-shifting/
  - https://arxiv.org/html/2604.07212v1
  - https://itecspec.com/3gpp/23.801-01
related:
  - 6g-overview
  - 6g-data-plane
  - imt-2030-usage-scenarios-data-needs
  - 6g-kpi-20-requirements
  - user-plane-evolution
  - data-fabric-definition
  - isac
  - ai-native-air-interface
  - daas-interface-design
tags:
  - IMT-2030
  - 数据面
  - 设计约束
  - 数据类型
  - 流量模型
  - DaaS
  - 用户面演进
last_verified: 2026-06-21
owner: agent
---

# IMT-2030 框架的数据面设计约束

## 核心结论（执行摘要）

IMT-2030 框架（M.2160）对数据面的核心影响是驱动其从"连接管道"向"数据服务平台"的范式转变。6G 数据面需处理四类数据——通信数据、感知数据、AI 数据、管理数据——而 5G 用户面仅承载通信数据。流量模型方面，AI 驱动的物理智能正将上下行比从 5G 的 90:10 向 6G 的 50:50 甚至 30:70（上行主导）迁移。端到端数据路径从 5G 的会话隧道模型（GTP-U）演进为发布/订阅的数据拓扑模型，支持任意拓扑的数据编排。3GPP SA2 已于 2025 年启动 WT#5（6G 数据框架）研究，华为、中国移动、三星等均提出独立数据面架构方案。

## 1. 现状定义

**数据面设计约束**指 IMT-2030 框架中对数据采集、传输、处理、存储全流程的技术要求，以及这些要求对 6G 数据面架构设计的直接制约。

与 D5 子题（[[imt-2030-usage-scenarios-data-needs]]）的关键区分：
- D5 回答"六大场景需要什么数据能力"（需求侧）
- 本子题回答"这些需求如何转化为数据面的架构约束"（设计侧）

核心概念边界：
- **用户面（User Plane, UP）**：5G 定义的数据包转发面，通过 GTP-U 隧道在 UE-RAN-UPF 之间传输连接数据
- **数据面（Data Plane, DP）**：6G 提出的新功能面，在 UP 基础上扩展为数据采集、编排、处理、服务化的完整数据管理平面
- **数据即服务（DaaS）**：6G 数据面的核心范式，将数据作为可编排、可暴露、可交易的服务资源

## 2. 标准与组织动态（近 3 年）

| 时间 | 进展 | 机构 |
|------|------|------|
| 2023-07 | ITU-T SG13 研讨会提出 IMT-2030"3 体 4 层 5 面"架构概念，明确新增独立数据面、计算面、安全面 | ITU-T / 中国移动 |
| 2023-11 | M.2160 发布，框架中隐含数据面需求：6 大场景 + 15 项能力 + 4 项跨场景原则 | ITU-R WP 5D |
| 2024-03 | Qualcomm 发布 6G Foundry 系列，提出"用户面优先"设计理念 | Qualcomm |
| 2025-02 | 华为发布"Data Plane Design for AI-Native 6G Networks"，提出 DO/DA/DCP 架构 | 华为 |
| 2025-02 | NGMN 发布"Network Architecture Evolution towards 6G"，78% MNO 优先自治网络管理 | NGMN |
| 2025-03 | ZJU/华为发表基于数据面的统一数据收集框架论文，验证 DP 协议栈 UE 侧增益 | 浙大/华为 |
| 2025-05 | SNS JU 架构工作组发布 6G 架构白皮书 v1.3，含数据管理框架（DataOps）与 AI 框架 | SNS JU |
| 2025-06 | 3GPP SA2 启动 TR 23.801（6G 架构研究），WT#5 专门研究 6G 数据框架 | 3GPP SA2 |
| 2025-08 | SA2 #170 哥德堡会议讨论 WT#5 数据框架范围文档（S2-2506446） | 3GPP SA2 |
| 2026-01 | ITU-T SG13 发布 YSTR.IMT2030-req 技术报告草案，含网络需求考量 | ITU-T SG13 |
| 2026-04 | 3GPP TR 38.914（Release 20）场景与需求研究，采用定性设计驱动而非固定量化目标 | 3GPP RAN |

## 3. 关键玩家

| 玩家 | 定位 | 数据面相关贡献 |
|------|------|--------------|
| **华为** | 数据面独立架构的核心推动者 | 提出 DO/DA/DCP 三组件架构、DaaS 范式、基于 CRT 的无状态消息代理（DCP 转发时延降低 65%） |
| **中国移动** | "3 体 4 层 5 面"架构提出者 | 在 ITU-T SG13 推动独立数据面、计算面、安全面，主张全域端到端架构 |
| **Qualcomm** | 用户面优先设计理念倡导者 | 提出精简控制面、将定位/数据采集/IoT 等服务迁移至用户面，实现"G 无关"服务 |
| **三星** | AI 数据框架推动者 | 在 3GPP SA2 推动 6G 数据框架支持 AI 用例，强调 5G CP/UP 均无法有效承载 AI 数据 |
| **Ericsson** | 上行流量范式转变倡导者 | 物理 AI 场景下上下行解耦，预测 UL:DL 可达 70:30，推动 FDD massive MIMO |
| **Nokia** | 数据与信息架构设计者 | 提出 6G 专用数据信息架构，发布/订阅模式替代现有订阅通知机制 |
| **SNS JU** | 欧盟 6G 架构标准协调 | 架构工作组白皮书定义 DataOps + MLOps 集成框架，云原生数据面 |
| **3GPP SA2** | 6G 数据框架标准化主体 | WT#5 研究数据收集/分发/处理/存储/暴露全流程，预计 2027 年完成研究 |
| **IETF** | 用户面协议演进 | draft-zzhang-dmm-mup-evolution 提出 AN-UPF 集成（ANUP），消除 GTP-U 隧道开销 |
| **TSDSI/ArtPark** | 感知数据架构提出者 | 提出集成 3GPP/non-3GPP 传感器的感知数据架构，数据市场化概念 |

## 4. 技术机制

### 4.1 数据类型分类体系

6G 数据面需处理四类本质不同的数据，而 5G 用户面仅承载第一类：

| 数据类型 | 5G 处理方式 | 6G 数据面要求 | 典型数据特征 |
|---------|-----------|-------------|------------|
| **通信数据** | UP（GTP-U 隧道转发） | 增强转发（更高速率/更低时延） | 会话导向、点对点、QoS 分流 |
| **感知数据** | 无原生支持 | 新增感知数据通道（I/Q 采样、点云、雷达回波） | 大数据量、周期性采集、多终端点、灵活终止节点 |
| **AI 数据** | 无原生支持（NWDAF 有限分析） | 模型参数/梯度/训练数据/推理 I/O 的端到端管道 | 大批量传输、分布式同步、非连接导向 |
| **管理数据** | CP（SBI 小包传输）/OAM | 统一数据收集、存储、暴露框架 | 网络遥测、性能测量、配置数据 |

**核心约束**：5G 的 CP 仅支持小数据包短连接、UP 仅支持一对一会话隧道——AI 和感知数据的海量非连接数据无法被这两个面有效承载（三星，2025）。华为估算，仅 6G 感知数据量（若分配 1% 网络容量）即可达 ZB/天（云端）至 QB/天（端侧），远超当前 UP 设计能力。

### 4.2 数据流量模型

IMT-2030 框架对数据面流量模型的核心颠覆体现在三个维度：

**上下行比反转**：
- 5G 实测：下行占 90%，上行仅 8%（Ericsson Mobility Report）；视频 97:3，云存储 46:54
- 6G 预期：物理 AI 设备 UL:DL 可达 70:30（Ericsson，2026）；GenAI 流量上行占比已达 26%（Aetha，2026）
- 设计约束：需实现上下行解耦（Ericsson）、TDD 时隙比动态调整、子带全双工（SBFD）、FDD massive MIMO 强化上行

**突发特性变化**：
- 5G：视频流为主，下行突发占主导，上行稀疏
- 6G：AI 推理请求突发（毫秒级）、感知数据周期采集（高占空比）、分布式训练同步（大批量脉冲）、VR 多模态混合流（3GPP Rel-16 已定义 XR 流量模型含抖动/包延迟预算/到达动态）

**数据拓扑复杂化**：
- 5G：点对点（UE↔UPF），线性隧道
- 6G：多对多（多数据源↔多处理节点↔多数据消费者），任意拓扑，需 Pub/Sub 数据分发

### 4.3 端到端数据路径设计约束

| 设计维度 | 5G（IMT-2020） | 6G（IMT-2030）| 核心差异 |
|---------|---------------|-------------|---------|
| **转发模型** | 会话隧道（PDU Session/GTP-U） | 数据拓扑编排（DO/DA/DCP） + 增强 UP | 从"连接后通信"到"数据流编排" |
| **协议栈** | IP/GTP-U/PDCP/RLC/MAC | 新增 DSAP（数据服务应用协议）+ 数据面无线承载（DPRB） | DP 协议栈独立于 UP，优先级灵活可调 |
| **转发引擎** | 基于 PDR 的包分类（链表查找） | 无状态模数运算转发（CRT）/ SmartNIC 硬件卸载 | 时延从 ms 级降至亚 ms 级 |
| **数据处理** | 透明转发（UPF 不处理用户数据内容） | 路径上数据处理（on-path processing）：过滤/聚合/压缩/推理 | 数据面兼具传输与计算职能 |
| **RAN-CN 边界** | CU-UPF 通过 N3 接口分离 | AN-UPF 集成（ANUP）消除 N3 隧道；或保留但协议栈精简 | 吞吐提升显著（消除 GTP-U 封装开销）|
| **数据暴露** | NWDAF 订阅-通知（被动） | 发布/订阅模式 + 统一数据暴露注册发现框架 | 数据从被动采集到主动服务化 |

**关键性能约束**（源自 [[6g-kpi-20-requirements]]）：
- 转发引擎需支持 ≥200 Gbps 线速处理（峰值速率约束）
- 协议栈端到端时延 ≤0.1 ms（空口单向时延约束）
- 支持 10⁸ 设备/km² 的会话/流状态管理（连接密度约束）
- 确定性转发 + 多路径冗余（可靠性 10⁻⁷ 约束）
- 能效 100× 提升要求按需激活/深度睡眠（可持续性约束）

### 4.4 数据质量要求

M.2160 框架中对数据质量的要求分散在安全性、可靠性与 AI 能力三个维度中：

- **完整性（Integrity）**：M.2160 明确将"信息的机密性、完整性和可用性的保持"列为安全性定义核心。6G 数据面需在传输全链路保证数据不被篡改。
- **时效性（Timeliness）**：0.1–1 ms 空口时延约束 + 确定性通信要求，对感知数据和 AI 推理输入设置严格的时效窗口（如自动驾驶 30 ms 推理时延、近 100% 准确率）
- **可信度（Trustworthiness）**：ITU-T 研讨会（2023-07）明确"AI 能力需要可信，遵循基本原则和可信度公认指标"。SNS JU 白皮书强调数据治理（DataOps）确保数据质量对 AI/ML 操作至关重要。FAIR 原则（可发现、可访问、可互操作、可复用）被 6G-MIRAI 等项目采纳。
- **隐私保护**：ISAC 感知数据引发隐私风险；KOMSENS-6G 项目提出 PIF（隐私强制功能）和数据最小化原则

### 4.5 与 5G 数据面需求的本质差异

| 差异维度 | 5G（IMT-2020） | 6G（IMT-2030） |
|---------|---------------|-------------|
| **功能定位** | 用户面 = 包转发管道 | 数据面 = 数据服务平台（DaaS） |
| **面数量** | 2 面（控制面 + 用户面） | ≥5 面（控制 + 用户 + 数据 + 计算 + 安全） |
| **数据类型** | 单一（连接数据） | 四类（通信/感知/AI/管理） |
| **数据拓扑** | 点对点隧道 | 任意拓扑（多源多汇） |
| **数据处理** | 透明转发 | 路径上处理（on-path processing） |
| **设计范式** | 连接优先（connect-then-communicate） | 数据优先（data-centric / UP-first） |
| **标准化路径** | 3GPP SA2 单一工作组 | SA2 WT#5 + RAN + SA5 跨域协调 |
| **商业模式** | 按连接/流量收费 | 数据市场化（数据交易/DaaS 定价） |

本质上，5G→6G 的数据面演进是从**"为连接服务的传输优化"**到**"为数据价值服务的全栈平台化"**的范式转变。

## 5. 趋势驱动力

- **AI 渗透率飙升**：AI 原生设计使数据成为网络的"第一等公民"，数据面从辅助功能升级为核心功能面
- **感知融合（ISAC）**：通信网络兼具雷达功能，催生全新感知数据类型与处理流程，需独立数据通道
- **上行流量结构性增长**：物理 AI（机器人、智能眼镜、自动驾驶）驱动上行数据量指数增长，80% 运营商上行增速已超下行
- **数据主权与治理**：GDPR 等法规推动数据最小化、本地处理、隐私保护嵌入数据面架构
- **运营商商业转型**：从"卖连接"到"卖数据/算力/智能"，数据面是 DaaS 商业模式的技术基座
- **5G 用户面瓶颈**：GTP-U 协议栈未随代际演进（3G 至今基本不变），扩展性/能效/灵活性均不足（6G-RUPA 论文）

## 6. 批评与风险

- **数据面定义尚未标准化**：独立数据面概念主要由华为和中国移动推动，3GPP SA2 WT#5 仍在研究阶段（预计 2026-12 或 2027-03 完成），业界对是否需要独立数据面（vs 增强现有 UP）尚无共识
- **感知数据传输方案竞争**：3GPP 正在讨论感知数据在控制面（通过 AMF）vs 数据面传输的多个竞争方案，KOMSENS-6G 与其他项目提案存在分歧
- **上行流量预测不确定性**：Ericsson 的 70:30 UL:DL 基于特定物理 AI 场景，批评者指出智能眼镜/头显大部分时间在室内使用 Wi-Fi，且上行流量增长与运营商收入无关联
- **DaaS 商业模式待验证**：NGMN 指出许多 6G 用例"可通过高级 5G 网络实现"，数据服务化的额外投资回报尚不清晰
- **架构复杂度风险**：从 2 面扩展到 5 面增加了系统复杂度，与 6G 设计原则中的"极简主义"（Simplicity）存在张力
- **数据质量量化困难**：7 项新增 TPR 中 5 项（含 AI 能力）仅定性评估，数据质量的标准化度量方法仍缺失

## 7. 我司相关性（占位）

> 待 6g-insight-report 阶段结合 ops/company-context.md 填充。关注方向：数据面转发引擎能力、DaaS 接口设计、感知数据处理链路。

## 矛盾与待核实

1. **数据面是否应独立于用户面**：华为/中国移动主张独立 DP（与 UP 并列），Qualcomm 主张"用户面优先"（在 UP 内承载数据服务），Nokia 倾向增强现有 UP + 新增数据信息层。3GPP SA2 WT#5 未做结论。→ 记入 contradictions.md
2. **感知数据传输路径**：方案 A 通过控制面（AMF），方案 B 通过数据面/用户面（可能共用 AI 数据传输通道）。→ 已在 D5 记录，本题补充设计侧视角
3. **上行流量模型分歧**：Ericsson 预测 AI 场景下 UL 可占 70%；Aetha 实测当前 GenAI 仅 26%；传统实测仅 8%。差异源于场景假设不同。→ 记入 contradictions.md

## 数据缺口

1. **P1**：6G 数据面协议栈（DSAP/DPRB）的标准化进展——目前仅有华为/ZJU 论文描述，3GPP 尚未讨论
2. **P1**：AI 数据（模型参数/梯度）的定量流量估算——缺乏公开实测数据
3. **P1**：四类数据的 QoS 差异化框架——目前无标准化提案定义感知/AI 数据的 QoS 等级
4. **P2**：数据面对能效的量化贡献——无公开研究分析 DP vs UP 在能效方面的对比
5. **P2**：数据市场化（DaaS 定价/数据合约）的技术实现方案——TSDSI 提出概念，无标准化进展

## 来源

### 一手资料 / 官方
1. [ITU-R M.2160-0 (11/2023)](https://www.itu.int/dms_pubrec/itu-r/rec/m/R-REC-M.2160-0-202311-I!!PDF-E.pdf) — IMT-2030 框架建议书
2. [ITU-T SG13 Workshop on IMT-2030 Architecture (2023-07)](https://www.itu.int/en/ITU-T/Workshops-and-Seminars/2023/0724/Documents/LuLuV2.pdf) — 中国移动"3 体 4 层 5 面"架构提案
3. [3GPP TS 23.801-01: Study on Architecture for 6G System](https://itecspec.com/3gpp/23.801-01) — SA2 6G 架构研究（含 WT#5 数据框架）
4. [SA2 #170 WT#5 Data Framework Scope (S2-2506446)](https://www.3gpp.org/FTP/tsg_sa/WG2_Arch/TSGS2_170_Goteborg_2025-08/INBOX/DRAFTS/FS_6G_ARC) — 数据框架范围讨论
5. [ITU-T YSTR.IMT2030-req Draft (2026-01)](http://www.itu.int/md/meetingdoc.asp?lang=en&parent=T25-SG13-260227-TD-WP1-0367) — 网络需求考量报告

### 学术
6. [A unified data collection framework based on the data plane for 6G](https://jzus.zju.edu.cn/opentxt.php?doi=10.1631%2FFITEE.2400247) — Yuan et al., Front. Inform. Technol. Electron. Eng., 2025
7. [From 6G Scenarios and Requirements to Design Drivers (TR 38.914)](https://arxiv.org/html/2604.07212v1) — 3GPP Release 20 场景设计驱动分析, 2026
8. [Mobile User Plane Evolution (IETF Draft)](https://www.ietf.org/archive/id/draft-zzhang-dmm-mup-evolution-09.html) — AN-UPF 集成提案, 2024

### 厂商白皮书 / 产业联盟
9. [Data Plane Design for AI-Native 6G Networks](https://www.huawei.com/en/huaweitech/future-technologies/data-plane-design-ai-native-6g-networks) — 华为, 2025-02
10. [6G Foundry: Rethinking the Control Plane](https://www.qualcomm.com/content/dam/qcomm-martech/dm-assets/documents/6G-Foundry-1-Rethinking-the-control-plane.pdf) — Qualcomm, 2024
11. [AI in 6G Network: Service and System Aspect](https://research.samsung.com/blog/AI-in-6G-network-Service-and-System-Aspect) — Samsung Research, 2025
12. [Towards 6G Architecture (v1.3)](https://smart-networks.europa.eu/wp-content/uploads/2025/06/archwg-whitepaper-v1.3-final-23may_clean.pdf) — SNS JU Architecture WG, 2025
13. [Network Architecture Evolution Towards 6G](https://www.ngmn.org/wp-content/uploads/250218_Network_Architecture_Evolution_towards_6G_V1.0.pdf) — NGMN, 2025-02

### 分析机构 / 媒体
14. [Ericsson has pinned its 6G hopes on AI's rising 'uplink' demands](https://www.lightreading.com/6g/ericsson-has-pinned-its-6g-hopes-on-ais-rising-uplink-demands) — Light Reading, 2026-03
15. [AI and the New Uplink Challenge](https://www.aethaconsulting.com/ai-and-the-new-uplink-challenge-how-mobile-traffic-patterns-are-shifting/) — Aetha Consulting, 2026-03
