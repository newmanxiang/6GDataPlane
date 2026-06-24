---
title: 3GPP SA2 6G 数据框架工作项（WT#5）进展
title_en: 3GPP SA2 6G Data Framework Work Task #5 Progress
slug: 3gpp-sa2-6g-data-framework-wt5
category: topic
status: reviewed
confidence: medium
sources:
  - https://portal.3gpp.org/desktopmodules/WorkItem/WorkItemDetails.aspx?workitemId=1080057
  - https://itecspec.com/3gpp/23.801-01
  - https://www.3gpp.org/FTP/tsg_sa/WG2_Arch/TSGS2_170_Goteborg_2025-08/INBOX/DRAFTS/FS_6G_ARC
  - https://www.gsma.com/solutions-and-impact/technologies/networks/gsma_resources/gsma-6g-community-industry-progress-report-may-2026/
  - https://research.samsung.com/blog/AI-in-6G-network-Service-and-System-Aspect
  - https://www.ericsson.com/en/blog/2025/6/blog-6g-standardization-technology-step-to-publish
  - https://ofinno.com/standards-readout/6g-takes-shape-in-gothenburg-and-goa-first-solutions-emerge-as-3gpp-moves-past-problem-identification/
  - https://6gfutures.substack.com/p/outcomes-from-the-3gpp-sa-meeting
  - https://www.cablelabs.com/blog/why-the-6g-study-phase-matters-now
  - https://www.nokia.com/asset/i/212403/
  - https://www.huawei.com/en/huaweitech/future-technologies/data-plane-design-ai-native-6g-networks
  - https://docomolab-euro.com/en/gsma-6g-community-from-research-to-standards-shaping-future-networks/
  - https://datatracker.ietf.org/meeting/122/materials/slides-122-dmm-6g-workshop-summary-00
  - https://www.ngmn.org/wp-content/uploads/250218_Network_Architecture_Evolution_towards_6G_V1.0.pdf
related:
  - 3gpp-rel-19-20-data-architecture-status
  - 6g-data-plane-architecture-2025
  - daas-interface-design
  - ai-native-data-plane-status
  - cross-domain-data-governance-6g
  - data-fabric-for-ai-native-6g
tags: [3gpp, sa2, 6g, data-framework, wt5, dmfw, daas, standardization, FS_6G_ARC, KI21, TR-23.801]
last_verified: 2026-06-25
owner: agent
---

# 3GPP SA2 6G 数据框架工作项（WT#5）进展

## 核心结论（150 字内）

3GPP SA2 6G 架构研究项（FS_6G_ARC）中 **WT#5（6G Data Framework）对应 KI#21**，是 6G 数据面最直接的标准化入口。截至 2026 年 6 月，TR 23.801-01 已迭代至 V0.7.0（~16.7 MB），研究进度 30%。WT#5 研究范围涵盖数据收集、分发、处理、存储、访问与暴露的全生命周期框架，明确提出需覆盖跨域（RAN/CN/OAM/AF）数据传输。当前处于**方案提交阶段**，各公司（华为/vivo/Samsung/Nokia/Ericsson 等）已提交方案提案，Penholder 已于 SA2#174（2026.04）完成分配。核心分歧"独立数据面 vs 增强用户面"仍未收敛，预计 2027 年 3 月前完成研究结论。[信心：中等]

## 1. 现状定义

### 术语与范围

- **FS_6G_ARC**（Study on Architecture for 6G System）：3GPP SA2 Rel-20 6G 架构研究项，工作项编号 1080057，2025 年 6 月 5 日启动，目标完成日 2027 年 3 月 3 日
- **WT#5**（Work Task 5）：FS_6G_ARC 下属的"6G data framework in SA WG2"工作任务
- **KI#21**（Key Issue #21）：WT#5 对应的关键问题"6G data framework in SA2"，定义于 TR 23.801-01
- **TR 23.801-01**：FS_6G_ARC 产出的技术报告草案，截至 2026 年 6 月已版本至 V0.7.0
- **Rapporteur**：Dr. Malla Reddy Sama（DOCOMO Euro-Labs），负责整个 FS_6G_ARC 研究项的协调

### 与相邻概念的边界

- WT#5 聚焦**系统架构层面**的数据框架，不涉及空口协议栈（RAN WG2 管辖）
- 与 SA5 FS_6G_OAM 存在交叉：SA5 负责管理编排域的数据管理，SA2 负责核心网/应用域数据框架
- 与 WT#3（AI）高度关联：数据框架为 AI 模型训练/推理提供数据管道基础

## 2. 标准与组织动态（近 3 年）

### FS_6G_ARC 研究项全貌

FS_6G_ARC 包含 **8 个 Work Tasks** 和 **24 个 Key Issues**：

| WT# | 主题 | 对应 KI | 与数据框架关系 |
|-----|------|---------|--------------|
| WT#1.1 | 6G 控制信令 | KI#1 | 数据框架可能需要新控制信令支持 |
| WT#1.2 | SBA/UP/QoS/Policy/暴露/共享 | KI#2-#10 | UP 架构（KI#4）直接决定数据面设计 |
| WT#1.3 | 非 3GPP 接入 | KI#11 | 跨接入的数据收集需求 |
| WT#1.4 | 6G 基础服务 | KI#12-#16 | 语音/定位等服务的数据需求 |
| WT#2 | 迁移与互通 | KI#17 | 5G→6G 数据架构迁移策略 |
| WT#3 | AI | KI#18-#19 | ⭐ AI 数据管道为数据框架核心驱动 |
| WT#4 | 感知与通信集成（ISAC）| KI#20 | ⭐ 感知数据传输依赖数据框架 |
| **WT#5** | **6G 数据框架** | **KI#21** | **⭐ 核心研究对象** |
| WT#6 | 计算支持 | KI#22 | 计算任务的数据输入/输出需求 |
| WT#7 | 6G NTN | KI#23 | 卫星数据传输路径 |
| WT#8 | IoT 使能器 | KI#24 | IoT 海量数据采集 |

### 进度时间线

| 日期 | 会议 | 事件 | WT#5 相关进展 |
|------|------|------|--------------|
| 2025.06 | SA#108（布拉格）| FS_6G_ARC 获批启动（SP-250806）| WT#5 正式列入研究范围 |
| 2025.08 | SA2#170（哥德堡）| 首次 WT 范围定义讨论 | S2-2506446 系列文稿（v1→v3）定义 WT#5 范围 |
| 2025.10 | SA2#171（武汉）| WT/KI 范围合并与 Penholder 指南发布 | S2-2508225（合并稿）完成 WT#5 最终范围定义 |
| 2025.12 | SA2#172（达拉斯）| P-CR 提交启动 | KI#21 数据框架问题正式写入 TR；进度 5%→20% |
| 2026.02 | SA2#173（果阿）| 首次方案探索 | 公司开始提交方案提案（vivo 提交 S2-2510456 等）|
| 2026.04 | SA2#174（马耳他）| 方案评估 | **Penholder 分配完成**；24 KI 均有方案；进度 20%→30% |
| 2026.06 | SA2#175-AH-e | 密集讨论期 | 电子会议（6.24-30）推进方案合并与评审 |
| 2027.03 | — | **目标完成日** | 研究结论冻结 |

### TR 23.801-01 版本演进

| 版本 | 日期 | 会议 | 大小 | 备注 |
|------|------|------|------|------|
| V0.0.0 | 2025.09 | SA2#170 | ~100 KB | 骨架文档 |
| V0.2.0 | 2025.10 | SA2#171 | 223 KB | WT/KI 范围定稿 |
| V0.3.0 | 2025.12 | SA2#172 | 371 KB | 首批 P-CR 入库 |
| V0.4.0 | 2026.02 | SA2#173 | 1.8 MB | 首批方案提案 |
| V0.5.0 | 2026.04 | SA2#174 | 7.7 MB | 大量方案涌入 |
| V0.6.0 | 2026.06 | SA2#175 | 16.4 MB | 密集更新 |
| V0.7.0 | 2026.06 | SA2#175 | 16.8 MB | 最新版本 |

文件体积从初始 100 KB 暴增至 16.8 MB，反映出大量公司提案涌入方案阶段。

## 3. 关键玩家

### 标准组织内角色

| 角色 | 公司/人 | 备注 |
|------|---------|------|
| FS_6G_ARC Rapporteur | Dr. Malla Reddy Sama（DOCOMO Euro-Labs）| 统管 24 个 KI 进度协调 |
| 3GPP SA 副主席 | Dr. Tao Sun（中国移动）| 在 3GPP Highlights 撰文阐述 6G 架构 |
| WT#5 Penholder | 未公开（需会员账号）| SA2#174 完成分配（文件：Penholder assigned list for solution phase_r5.docx）|
| WT#5 活跃提案方 | vivo、华为、Samsung、Nokia、Ericsson、中国移动、DOCOMO 等 | 基于 SA2#172 Chairman Notes（S2-2510456 等）|

### 各方立场与提案

#### 华为：DaaS（Data as a Service）

- **核心主张**：6G 需要独立于 CP/UP 的专用数据面（DP），以 DO/DA/DCP 三组件架构实现
- **关键贡献**：DaaS 白皮书（2025.02）定义完整架构，DCP 原型验证延迟 ~2ms/吞吐 2.4 GB/s
- **标准化策略**：通过 3GPP 提案推动引入独立数据面概念

#### 中国移动："三体四层五面"

- **核心主张**：6G 架构应含 5 个功能面（控制/用户/数据/计算/安全），数据面独立于用户面
- **关键贡献**：IEEE ComMag 2023 发表、ITU-T SG13 提案、Springer 专著（2026.01）
- **标准化策略**：Dr. Tao Sun 作为 SA 副主席直接参与框架层决策

#### vivo：统一数据收集框架

- **核心主张**：基于数据面的统一数据收集框架，含 DSAP 新空口协议栈
- **关键贡献**：FITEE 论文（2025.03）、SA2#172 提交方案提案（S2-2510456）
- **标准化策略**：兼顾 UE 侧协议和核心网架构，提供端到端方案

#### Samsung：跨域 AI 数据框架

- **核心主张**：数据框架是 6G AI 使能的核心支撑，需解决 5G 跨域数据传输瓶颈
- **关键贡献**：2026.05 博文详述 6G 数据框架对 AI 跨域的支撑角色
- **标准化策略**：强调数据框架需覆盖 RAN/CN/OAM/AF 全域灵活数据传输

#### Nokia：数据与信息架构

- **核心主张**：6G 需要"dedicated data and information architecture"，采用 Pub/Sub 或 event stream 模式
- **关键贡献**：6G 白皮书（2025.03）定义数据暴露/注册/发现/交付通用框架
- **标准化策略**：主张模块化增强，在 5G 基础上演进；强调协议演进（HTTP/3+QUIC SBA）

#### Ericsson：演进增强路线

- **核心主张**：6G 应在现有 SBA 框架内增强数据支持能力，"collect data once for multiple uses"
- **关键贡献**：2025.06 博文明确 6G 数据架构应"agnostic to data use cases"
- **标准化策略**：倾向演进路线，反对过度新增独立功能面带来的复杂性

#### Qualcomm："用户面优先"

- **核心主张**：精简控制面，将新服务（含数据收集）作为 IP 服务运行在增强 UP 上，无需独立数据面
- **关键贡献**：6G Foundry 系列白皮书（2024.03 起），提出模块化 NAS + lean CP
- **标准化策略**：推动 3GPP 简化架构，"G-agnostic"服务设计

#### DOCOMO Euro-Labs

- **核心主张**：作为 Rapporteur 保持中立协调角色，推动共识形成
- **关键贡献**：Dr. Sama 主持所有 FS_6G_ARC 讨论，在 GSMA 活动阐述 6G 架构愿景
- **标准化策略**：确保研究按时完成（2027.03 硬截止日）

## 4. 技术机制

### 4.1 WT#5 研究范围（基于 S2-2506446/S2-2508225）

WT#5 正式研究范围（引用 SP-250806 WID）：

> "Study data framework for all aspects related to efficient and scalable data handling including data collection, distribution, processing, storage, data access and data exposure, with consideration of access control/user consent and privacy."

具体研究内容（基于 SA2#170 讨论）：
1. **跨域数据发现**：6G 服务功能与数据消费者/生产者之间的数据交换架构
2. **高效数据收集**：覆盖 UE、网络功能、第三方的流式数据采集
3. **数据分发与处理**：On-path 数据处理与多级分发
4. **数据存储**：分布式数据存储与检索
5. **数据暴露**：向 AI NF、RAN、AF、OAM 的统一暴露机制
6. **数据源/消费者认证**：可信认证与授权机制
7. **数据可追溯性**：确保透明、安全和可信的数据操作
8. **高效传输协议**：数据管理和传输协议设计

### 4.2 与 5G 数据层（NWDAF/DCCF/MFAF）的关系

5G Rel-17 引入的 Data Management Framework（TS 23.700-91）包含：
- **DCCF**（Data Collection Coordination Function）：协调数据采集，避免重复
- **MFAF**（Messaging Framework Adaptor Function）：消息框架适配
- **ADRF**（Analytics Data Repository Function）：分析数据存储

6G 数据框架的设计动机正是源于上述 5G 框架的**根本局限**：
- NWDAF 中心化设计不适应分布式 AI
- 数据收集走控制面导致 CP 拥塞
- 用户面"黑箱"无法支持 AI 数据采集
- 缺乏 RAN↔CN↔OAM↔AF 统一传输机制

Samsung Research 明确指出：*"5G UP 基础设计以 UE→DN 用户数据透明传输为目的，数据负载对核心网不可见——这是跨域 AI 数据传输的根本障碍。"*

### 4.3 核心架构分歧："独立数据面" vs "增强用户面"

| 维度 | 独立数据面路线 | 增强用户面路线 |
|------|--------------|--------------|
| 代表方 | 华为、中国移动、vivo | Qualcomm、Ericsson（倾向）|
| 核心论据 | 非连接数据（AI/感知/管理）需专用通道 | 复用 IP 生态降低复杂度和 TCO |
| 数据拓扑 | 多源多汇→需 Pub/Sub 消息模型 | 用 IP 层 + 标准互联网协议 |
| 与 5G 关系 | 新增面（变革性）| UP 扩展（演进性）|
| 中间路线 | Nokia/Hexa-X-II：承认需数据层但不一定是独立"面" | — |

SA2 WT#5 正在研究此问题但**尚未达成任何结论**。

### 4.4 SA5 DMFW 与 SA2 WT#5 的关系

| 维度 | SA2 WT#5 | SA5 FS_6G_OAM |
|------|----------|---------------|
| 聚焦层面 | 核心网系统架构层数据框架 | 网络管理编排层数据管理 |
| 数据类型 | AI 数据、感知数据、应用数据、网络事件 | OAM 性能数据、配置数据、故障数据 |
| 关键机制 | 数据暴露、跨域传输协议 | 数据目录、数据质量、数据访问控制 |
| 交叉地带 | 数据收集、数据暴露、访问控制 | 数据收集、数据暴露、访问控制 |

6G Futures（2026.04）指出：**SA2 与 SA5 需在"数据集和模型参数交换"上进行下选（down-selection）**，这是当前已识别的协调需求。

### 4.5 WT#5 关键输出文档状态

- **TR 23.801-01**：V0.7.0（2026-06-14 更新），Section 5.21 定义 KI#21，Section 6.21 收录方案提案，Annex A.5 定义 WT#5 范围
- **Penholder assigned list for solution phase_r5.docx**：2026-03-31 创建，SA2#174 使用
- **S2-2603384_FS_6G_ARC_SA2_174_Status_v02.pptx**：174 会议进度报告

## 5. 趋势驱动力

1. **AI 原生化压力**：GenAI/Agentic AI 驱动的大规模数据传输使 5G CP 数据收集模式不可持续；Samsung 明确 6G 数据框架是 AI 使能的必要条件
2. **ISAC 数据管道缺失**：感知数据从 RAN 到 CN 到 AF 的端到端路径在 5G 不存在；WT#4（ISAC）的技术实现依赖 WT#5 数据框架
3. **IMT-2030 时间倒逼**：ITU-R 2029 年初需收到技术提案→3GPP 需 2027 年完成研究→SA2 仅余 9 个月
4. **运营商降本诉求**：NGMN 报告（2025.02）78% 运营商将成本效率列为 6G 首要关切，架构简化是关键
5. **5G 数据收集复杂性教训**：IETF DMM WG 在 2025.03 总结 5G 数据收集五种方法（MDT/LPP/NWDAF/DCAF/UE-level）引入巨大复杂性，推动统一框架需求
6. **物理 AI 上行翻转**：部分场景 UL:DL 可能从 8:92 翻转至 70:30，对数据面设计提出根本挑战

## 6. 批评与风险

1. **时间紧张风险**：FS_6G_ARC 需在 2027.03 前完成 24 个 KI 研究，2026.06 仅 30%；SA2 已安排 ad-hoc 电子会议但仍紧张
2. **范围膨胀**：24 个 KI 覆盖面极广，WT#5 仅是其中之一，可能获得的讨论时间不足
3. **核心分歧未收敛**：独立数据面 vs 增强 UP 仍无共识；多家公司立场固定，短期内难以统一
4. **SA2/SA5 协调不力风险**：两个工作组对"数据管理/数据暴露"的职责边界未明确，可能导致重复或缺漏
5. **仅研究不规范**：Rel-20 产出仅为 TR（技术报告），不产生规范性 TS——真正技术决策推迟至 Rel-21（2027+）
6. **中西方路线分化**：独立数据面由中国系厂商主导，增强 UP 由美国系厂商倾向，欧洲居中——可能演变为标准化博弈
7. **部署可行性待验证**：华为 DCP 仅有消息代理原型，Qualcomm UP-first 无公开定量验证；方案缺乏端到端实证

## 7. 我司相关性（占位，由 6g-insight-report 阶段填充）

> 待读取 `ops/company-context.md` 后映射。

初步关联方向：
- WT#5 定义了 6G 数据面的标准化边界，直接影响产品/解决方案在标准中的定位
- Penholder 分配反映各厂商在数据框架中的投入和话语权，我司是否参与 SA2 直接决定影响力
- "独立数据面 vs 增强 UP"的最终结论将决定我司产品架构选择
- SA2/SA5 交叉地带是数据编织能力的天然映射点

## 矛盾与待核实

- **矛盾 5（已有）**：独立数据面 vs 增强用户面 — SA2 WT#5 正在研究，无结论
- **矛盾 7（已有）**：DaaS 接口 API 范式（Pub/Sub vs 增强 SBA）— 无定论
- **矛盾 11（已有）**：SA2 WT#5 vs SA5 DMFW 职责边界 — 需 TSG SA 协调
- **矛盾 12（已有）**：Rel-21 时间线乐观性 vs 研究深度 — FS_6G_ARC 仅 30%
- **新矛盾 33**：WT#5 数据框架"用例无关"原则 vs 各方案面向特定用例设计 — Ericsson 主张框架应"agnostic to data use cases"，而华为 DaaS 和 vivo DSAP 提案面向 AI/感知等特定用例优化，二者设计哲学存在张力

## 数据缺口

- **P0**：TR 23.801-01 Section 5.21（KI#21）和 Section 6.21（Solutions）的完整正文内容——需 3GPP 会员账号
- **P0**：WT#5 Penholder 公司及其负责方向——需会员账号获取 `Penholder assigned list for solution phase_r5.docx`
- **P1**：SA2#175-AH-e（2026.06.24-30）WT#5 讨论结果和方案合并进展
- **P1**：各公司提交的具体方案提案内容（S2-26xxxxx 系列文稿）
- **P1**：SA2 与 SA5 在数据治理/数据暴露上的正式分工协议
- **P2**：CT WG 对 6G 数据框架协议层面研究进展（CT 6G 研究 2026.03 才启动）

## 来源

### 一手资料 / 官方
1. [3GPP FS_6G_ARC Work Item Details](https://portal.3gpp.org/desktopmodules/WorkItem/WorkItemDetails.aspx?workitemId=1080057) — 工作项详情：进度 30%，Start 2025-06-05，End 2027-03-03
2. [TR 23.801-01 Table of Contents (iTecSpec)](https://itecspec.com/3gpp/23.801-01) — TR 目录结构：24 KI + 方案 + Annex A WT 定义
3. [SA2#170 FTP: WT#5 Data Framework Drafts](https://www.3gpp.org/FTP/tsg_sa/WG2_Arch/TSGS2_170_Goteborg_2025-08/INBOX/DRAFTS/FS_6G_ARC) — S2-2506446 系列（WT#5 范围定义 v1-v3）
4. [SA2#171 FTP: WT#5 Merged Scope](https://www.3gpp.org/ftp/tsg_sa/WG2_Arch/TSGS2_171_Wuhan_2025-10/INBOX/DRAFTS/FS_6G_ARC/Planning/CC_after_submission_deadline) — S2-2508225 合并稿
5. [SA2#174 FTP: Status & Penholder](https://www.3gpp.org/ftp/tsg_sa/WG2_Arch/TSGS2_174_Malta_2026-04/INBOX/DRAFTS/FS_6G_ARC/General) — 进度报告与 Penholder 分配列表
6. [IETF DMM 6G Workshop Summary (2025.03)](https://datatracker.ietf.org/meeting/122/materials/slides-122-dmm-6g-workshop-summary-00) — 3GPP 6G Workshop 要点含 Unified Data Management Framework 描述
7. [3GPP Rel-20 Planning and Progress](https://www.3gpp.org/news-events/3gpp-news/sa-rel20) — SA Rel-20 双轨结构与 6G 研究规划

### 厂商白皮书 / 博客
8. [Samsung Research: AI in 6G Network SA Aspect](https://research.samsung.com/blog/AI-in-6G-network-Service-and-System-Aspect) — 2026.05，6G 数据框架对 AI 跨域支撑分析
9. [Huawei: Data Plane Design for AI-Native 6G](https://www.huawei.com/en/huaweitech/future-technologies/data-plane-design-ai-native-6g-networks) — 2025.02，DaaS 概念与 DO/DA/DCP 架构
10. [Ericsson: 6G Standardization Technical Studies Starting](https://www.ericsson.com/en/blog/2025/6/blog-6g-standardization-technology-step-to-publish) — 2025.06，6G 数据架构"用例无关"原则
11. [Nokia: 6G System Architecture](https://www.nokia.com/asset/i/212403/) — 2025.03，数据与信息架构 + Pub/Sub 模式
12. [DOCOMO Euro-Labs: GSMA 6G Community Webinar](https://docomolab-euro.com/en/gsma-6g-community-from-research-to-standards-shaping-future-networks/) — 2026.02，Rapporteur 视角

### 分析机构 / 行业
13. [GSMA 6G Community Progress Report (May 2026)](https://www.gsma.com/solutions-and-impact/technologies/networks/gsma_resources/gsma-6g-community-industry-progress-report-may-2026/) — SA2#173/174 进展，24 KI 确认
14. [6G Futures: Outcomes from SA#111](https://6gfutures.substack.com/p/outcomes-from-the-3gpp-sa-meeting) — 2026.04，首个 Rel-21 WI、SA2↔SA5 下选需求
15. [Ofinno: 6G Takes Shape (Standards Readout)](https://ofinno.com/standards-readout/6g-takes-shape-in-gothenburg-and-goa-first-solutions-emerge-as-3gpp-moves-past-problem-identification/) — 2026.02，SA2#173 首次方案探索
16. [CableLabs: Why the 6G Study Phase Matters Now](https://www.cablelabs.com/blog/why-the-6g-study-phase-matters-now) — 2026.03，FS_6G_ARC 定位分析
17. [NGMN: Network Architecture Evolution towards 6G](https://www.ngmn.org/wp-content/uploads/250218_Network_Architecture_Evolution_towards_6G_V1.0.pdf) — 2025.02，运营商共识与关切

### 学术
18. [vivo/ZJU: A Unified Data Collection Framework Based on DP for 6G](https://jzus.zju.edu.cn/opentxt.php?doi=10.1631%2FFITEE.2400247) — FITEE 2025.03，DSAP 协议栈与原型验证
