---
title: 3GPP Rel-19/20 数据架构标准化现状
title_en: 3GPP Rel-19/20 Data Architecture Standardization Status
slug: 3gpp-rel-19-20-data-architecture-status
category: topic
status: reviewed
confidence: medium
sources:
  - 3gpp-release-19-page
  - 3gpp-release-20-page
  - 3gpp-fs-6g-arc-workitem
  - samsung-research-ai-6g-sa2
  - ofinno-standards-readout-feb2026
  - firstnet-3gpp-dec2025
  - qualcomm-rel20-blog
  - interdigital-rel20-blog
  - wirelessbrew-6g-si-catalog
  - gsma-6g-progress-may2026
  - 6gfutures-fukuoka-outcomes
  - cablelabs-6g-study-phase
related:
  - 6g-data-plane
  - 6g-overview
  - user-plane-evolution-upf-to-6g
  - network-data-analytics-evolution-nwdaf-to-6g
  - ai-native-air-interface
  - 6g-data-plane-architecture-2025
  - ai-native-data-plane-status
  - daas-interface-design
  - 3gpp-sa2-6g-data-framework-wt5
tags:
  - 3GPP
  - Rel-19
  - Rel-20
  - Rel-21
  - 6G
  - data-architecture
  - standardization
  - NWDAF
  - UPF
  - SA2
  - DCCF
  - MFAF
  - FS_6G_ARC
last_verified: 2026-06-23
owner: agent
---

# 3GPP Rel-19/20 数据架构标准化现状

## 核心结论（执行摘要）

3GPP 数据架构标准化正处于代际转换的关键窗口。**Rel-19（5G-Advanced 第二版）已于 2025 年 9 月功能冻结、2026 年 3 月 ASN.1 冻结**，其数据相关特性（NWDAF 增强、DCCF/MFAF 消息框架、VFL、UPEAS Phase 2）以渐进增强为主 [高信心]。**Rel-20 同时承载 5G-A 尾声和 6G 研究双重使命**，截至 2026 年 6 月包含 126 个 5G-A 工作项和 13 个 6G 研究项（含 FS_6G_ARC）[高信心]。SA2 6G 架构研究（FS_6G_ARC）当前进度约 30%（截至 2026-06），**已定义 24 个关键问题（KI），其中 KI#21 数据框架（WT#5）是数据面最直接相关的研究点** [中信心]。**第一个 Rel-21 规范化工作项（6G-REQ）已于 2026 年 3 月在 SA#111 获批**，标志着 6G 从研究阶段正式进入规范化 [高信心]。

## 1. 现状定义

### 术语与范围

- **Rel-19**：5G-Advanced 第二版（2024.3–2025.9 功能冻结），编号 3GPP Release 19
- **Rel-20**：双轨 Release——Rel-20_5GA（5G-A 收官）+ Rel-20_6G（6G 纯研究），2025.6 启动
- **Rel-21**：首个 6G 规范化 Release，预计 2027 年中启动，Stage 2 冻结目标 2028 年 3 月
- **数据架构**：本卡片定义为 3GPP 体系内与"数据收集、分析、暴露、传输框架"直接相关的 SI/WI，涵盖 NWDAF、DCCF/MFAF、UPF 事件暴露、AI/ML 系统支持、6G 数据框架研究

### 与相邻概念的边界

本卡片聚焦标准化进程和制度层面，与 `6g-data-plane-architecture-2025`（架构方案对比）、`ai-native-data-plane-status`（AI 原生数据面技术）互补但不重叠。

## 2. 标准与组织动态（2024–2026）

### 时间线关键节点

| 日期 | 事件 | 意义 |
|---|---|---|
| 2024.03 | Rel-19 WI/SI 范围在 SA#103 确定 | NWDAF enh、UPEAS Ph2 正式立项 |
| 2024.09 | SA#105 批准 6G SA1 研究（FS_6G_REQ） | Stage-1 6G 研究启动 |
| 2025.03 | 3GPP 全体 6G Workshop（巴塞罗那） | 各公司提交 6G 提案，定义 Rel-20 6G 研究范围 |
| 2025.06 | SA#108（布拉格）批准 FS_6G_ARC 等 13 个 6G SI | **6G 技术研究正式启动** |
| 2025.08 | SA2#170（哥德堡）首次讨论 WT#5 数据框架 | 数据框架进入 SA2 议程；WT#5 范围定义文稿（S2-2506446）多轮修订 |
| 2025.09 | Rel-19 功能冻结（Stage 3/RAN） | 5G-A 第二版技术内容定型 |
| 2025.10 | SA2#171（武汉）继续 WT#5 讨论 | 数据框架范围文稿合并完成（S2-2508225） |
| 2025.12 | SA2#175-AH-e（电子会议）推进 FS_6G_ARC | 进度从 5% 升至 20% |
| 2026.02 | SA2#173（果阿）首次提出具体方案 | 从问题识别转向方案探索；模块化 NAS 设计方案首次讨论 |
| 2026.03 | **SA#111（福冈）批准首个 Rel-21 WI（6G-REQ）** | **6G 规范化工作正式启动** |
| 2026.04 | SA2#174（马耳他）方案评估 | 24 个 KI 均有方案提案；Penholder 分配完成 |
| 2026.06 | FS_6G_ARC 进度 30%；SA2#175-AH-e（6.24-30） | 进入密集讨论期 |
| 2027.03 | **FS_6G_ARC 目标完成日** | SA2 6G 研究结论冻结 |
| 2027 中 | Rel-21 规范化工作启动 | 6G 技术规范（TS）开始撰写 |
| 2028.03 | Rel-21 Stage 2 冻结目标 | 首个 6G 系统架构规范定稿 |
| ~2030 | 商用部署 | 基于 Rel-21 的首批 6G 商用系统 |

### Rel-19 数据相关 WI/SI 完成状态

| 条目 | 工作组 | 类型 | 状态 | 关键产出 |
|---|---|---|---|---|
| eNWDAF（TS 23.288 R19） | SA2/CT3 | WI | ✅ 完成 | 23 个 Analytics ID；VFL 支持；NWDAF 辅助 QoS/策略；AI 定位增强；Bulked Data Collection |
| DCCF/MFAF 增强 | SA2/CT3 | WI | ✅ 完成 | 数据收集协调增强；DCCF 重选与重定位；消息框架历史数据查询 |
| UPEAS Phase 2（FS_UPEAS_Ph2） | SA2/SA6 | SI→WI | ✅ 完成 | UPF 事件暴露直接/间接订阅增强；SBI 方向暴露 QoS 监控事件 |
| FS_AIMLsys Phase 2 | SA2 | SI→WI | ✅ 完成 | 跨域 AI 操作：UE→LMF AI 定位数据收集；UP 数据收集方案研究（最终决定不在 R19 规范化）|
| AI/ML for NR Air Interface | RAN1 | WI | ✅ 完成 | CSI 反馈增强；波束管理 AI/ML；定位 AI/ML |

**关键发现**：Rel-19 在 SA2 域研究了通过用户面收集 UE 数据（用于 AI 模型训练）的可行性，但**决定不在 R19 进行规范化工作**——这一决策直接推动了 6G 数据框架的独立研究需求。Samsung Research 2026 年 5 月博文明确指出："5G UP 基础设计以 UE→DN 用户数据透明传输为目的，数据负载对核心网不可见——这是跨域 AI 数据传输的根本障碍。"

### Rel-20 6G 研究项（截至 2026.03）

| SID/WID | 缩写 | 工作组 | TR 编号 | 进度 | 与数据架构相关性 |
|---|---|---|---|---|---|
| 1080057 | **FS_6G_ARC** | SA2 | TR 23.801 | 30% | ⭐ 核心：WT#5 数据框架 + WT#1.2 用户面架构/SBA/暴露框架 |
| 1050110 | FS_6G_REQ | SA1 | TR 22.870 | ✅ 100% | 6G 用例和需求（含 AI、感知、泛在连接需求） |
| 1060079 | FS_6G_RAN_Scen_Req | TSG RAN | TR 38.914 | 60% | 6G 场景与需求（含数据收集、AI/ML 框架） |
| 1080072 | FS_6G_Radio | RAN1 | — | 12% | 6G 无线接口（含 AI/ML 数据收集需求） |
| 1100019 | FS_6G_APP | SA6 | — | 早期 | 6G 应用使能（含 GenAI、API 暴露） |
| 1100014 | FS_6G_OAM | SA5 | — | 早期 | 6G 管理与编排（含网络数据管理） |
| 1090013 | FS_6G_CH | SA5 | — | 早期 | 6G 计费（含 AI 流量计费模型） |
| 1090044 | FS_6G_SEC | SA3 | — | 早期 | 6G 安全（含 AI 操作安全） |

### FS_6G_ARC（SA2）详细结构

FS_6G_ARC 已定义 24 个关键问题（KI），按工作任务（WT）分组。与数据架构直接相关的包括：

- **WT#5 数据框架**：研究面向所有方面的高效可扩展数据处理框架，包括数据收集、分发、处理、存储、数据访问和数据暴露，兼顾访问控制/用户同意和隐私
- **WT#1.2**：增强 SBA 框架、用户面架构、QoS 框架、策略框架、网络暴露框架
- **WT#2**：AI/ML 与 6G 核心网（AI 使能 NF、Agentic Core、AI Agent 通信）
- **WT#4**：感知与通信集成（ISAC）——感知数据传输依赖数据框架
- **WT#6**：计算即服务——数据面对算力暴露的支撑

## 3. 关键玩家

### 标准组织工作组分工

| 工作组 | 数据架构职责 | 6G 研究焦点 |
|---|---|---|
| **SA2** | 核心网架构、数据框架、NWDAF 框架 | FS_6G_ARC（24 KI），重点 WT#5 数据框架 |
| **SA5** | 网络管理、OAM 数据采集 | FS_6G_OAM、FS_6G_CH |
| **SA6** | 应用使能、API 暴露 | FS_6G_APP（GenAI、CAPIF 下一代） |
| **CT3** | 协议细节（NWDAF/DCCF 接口） | 依赖 SA2 完成后启动 |
| **RAN1/RAN2** | 空口 AI/ML、数据收集 | FS_6G_Radio（数据收集框架需与 SA2 协调） |
| **RAN3** | RAN 架构、RAN-CN 接口 | 点对点 vs SBI 接口研究 |

### 企业/机构立场

- **Samsung**：推动 AI 使能 NF 分布式架构 + 统一数据框架（2026.05 博文详述 6G 数据框架对跨域 AI 的支撑角色）
- **Qualcomm**：主导 6G 无线 AI 框架、用户面优先设计；Rel-20 关注 CSI 双边模型标准化
- **InterDigital**：RAN2 WG 主席（Diana Pani）；强调 AI 流量上行特征对 RAN 协议设计的影响
- **Ericsson**：6G 标准化时间线定义；SBA 增强路线；能效优先
- **华为**：DaaS 白皮书推动独立数据面概念；WT#5 讨论中的主要贡献方
- **NGMN**：MNO 联盟发布《6G 网络架构演进》（2025.02），强调需在 3GPP 标准化前达成共识

## 4. 技术机制

### 4.1 5G 数据架构现状（Rel-19 基线）

Rel-19 数据架构的核心框架：

```
NWDAF (MTLF + AnLF)
  ├─ 23 个 Analytics ID
  ├─ ML 模型训练 / 推理 / 性能监控
  ├─ 水平联邦学习（HFL, R18）
  └─ 垂直联邦学习（VFL, R19）

DCCF (数据收集协调功能)
  ├─ 协调多数据源采集，避免重复
  ├─ 格式化/处理指令
  └─ 与 MFAF 配合实现消息框架交付

MFAF (消息框架适配功能)
  ├─ 3da/3ca 适配器
  └─ 消息分发/存储至 ADRF

UPF 事件暴露 (UPEAS)
  ├─ 直接/间接订阅模式
  └─ QoS 监控事件暴露
```

**核心局限**（驱动 6G 研究的因素）：
1. **NWDAF 中心化**：AI 能力集中于单一可选 NF，不适用于分布式 AI 需求
2. **数据收集走控制面**：大数据量传输导致 CP 拥塞
3. **用户面"黑箱"**：UP 数据对核心网不可见，无法支持 AI 数据采集
4. **跨域壁垒**：缺乏 RAN↔CN↔OAM↔AF 统一数据传输机制

### 4.2 6G 数据框架研究方向（WT#5）

SA2 WT#5 研究范围（基于 S2-2506446 文稿系列）：

> "Study data framework for all aspects related to efficient and scalable data handling including data collection, distribution, processing, storage, data access and data exposure, with consideration of access control/user consent and privacy."

关键技术方向：
- **独立数据面 vs 增强用户面**：3GPP 尚未定论（参见矛盾 5）
- **跨域统一数据传输**：核心网、RAN、OAM、AF 之间的灵活数据流
- **AI 数据管道**：支持分布式 AI 训练/推理的数据收集与分发
- **Pub/Sub vs SBA 接口**：数据交互范式选择（参见矛盾 7）

### 4.3 PFCP vs SBI 讨论

SA2#170 文稿（S2-2507126）讨论了 SBA 框架增强：
- 5G N4 接口使用 PFCP，UPF 仅部分支持 SBI（事件暴露）
- PFCP 与 SBI 共存导致效率低下
- 6G 可能统一为 SBI 化 UPF 控制接口，但需平衡性能与复杂性

## 5. 趋势驱动力

1. **AI/ML 全面渗透**：GenAI、Agentic AI 驱动的大规模数据传输需求，使 5G CP 数据收集模式不可持续
2. **ISAC 数据需求**：感知数据从 RAN 到 CN 到 AF 的端到端传输路径缺失
3. **运营商降本增效**：NGMN 调查显示成本效率是 MNO 对 6G 架构的首要关切
4. **物理 AI 上行翻转**：UL:DL 从传统 8:92 可能翻转至 70:30（特定物理 AI 场景），对数据面设计提出根本性挑战
5. **ITU IMT-2030 时间压力**：2029 年初需提交技术提案，倒推 3GPP 需在 2027 年完成研究、2028 年完成规范

## 6. 批评与风险

1. **时间紧张**：FS_6G_ARC 需在 2027.03 前完成 24 个 KI 研究，SA2 已考虑增加 ad-hoc 会议。2026.06 仅完成 30%，距目标仅余 9 个月
2. **范围膨胀**：24 个 KI 覆盖面极广，可能导致深度不足。数据框架（WT#5）仅是其中之一
3. **厂商分歧未收敛**：独立数据面 vs 增强用户面、PFCP vs SBI、模块化 NAS 等核心分歧仍处于"方案探索"阶段
4. **5G 教训未充分吸取**：Rel-15 NSA→SA 迁移困难在 6G 设计中被明确提出要避免，但具体避免方式仍模糊
5. **RAN-SA 协调挑战**：SA2 数据框架需与 RAN WG 数据收集需求对齐，跨 WG 协调效率是风险点
6. **仅研究不规范**：Rel-20 6G 产出仅为 TR（技术报告），不产生规范性 TS——真正的技术决策推迟至 Rel-21

## 7. 我司相关性（占位）

> 待读取 `ops/company-context.md` 后由 `6g-insight-report` 阶段填充。

初步映射方向：
- 数据框架（WT#5）定义了 6G 数据面的标准化边界，直接影响产品/解决方案定位
- NWDAF→分布式 AI NF 的演进路径决定了数据分析产品的适配策略
- PFCP/SBI 统一化影响控制面/用户面接口实现
- 跨域数据治理需求（SA2/SA5/SA6 交叉）是数据编织能力的天然映射点

## 矛盾与待核实

- **矛盾 5（已有）**：独立数据面 vs 增强用户面 — SA2 WT#5 正在研究，无结论
- **矛盾 7（已有）**：DaaS 接口 API 范式（Pub/Sub vs 增强 SBA）— SA2 WT#5 无定论
- **矛盾 10（已有）**：PFCP vs SBI 化 UPF 控制接口 — SA2#170 有讨论，未定论
- **新矛盾**：SA2 WT#5 数据框架 vs SA5 OAM 数据管理的职责边界 — 两个工作组均涉及数据管理，接口未明确
- **新矛盾**：Rel-21 时间线乐观 vs 6G 研究深度不足 — SA#111 批准首个 Rel-21 WI，但 FS_6G_ARC 仅完成 30%

## 数据缺口

- **P0**：SA2 WT#5 KI#21 数据框架的具体方案提案内容（文稿需 3GPP 会员账号）
- **P1**：SA2 各 KI 的 Penholder 公司清单（间接反映各厂商在数据框架中的投入方向）
- **P1**：FS_6G_ARC TR 23.801 正文内容（截至 V0.3.0 仅目录和初步框架可见）
- **P1**：SA5 FS_6G_OAM 与 SA2 WT#5 在数据管理/数据收集上的分工协议
- **P1**：RAN3 6G RAN-CN 接口研究中对数据收集通道的具体提案
- **P2**：SA6 FS_6G_APP 中 GenAI 使能层与数据框架的接口定义

## 来源

### 一手资料 / 官方
1. [3GPP Release 19 Official Page](https://www.3gpp.org/specifications-technologies/releases/release-19) — Rel-19 特性概览与冻结状态
2. [3GPP Release 20 Official Page](https://www.3gpp.org/specifications-technologies/releases/release-20) — Rel-20 5G-A/6G 双轨结构、13 个 6G SI 列表
3. [FS_6G_ARC Work Item Details](https://portal.3gpp.org/desktopmodules/WorkItem/WorkItemDetails.aspx?workitemId=1080057) — 工作项详情（进度 30%，2025.06–2027.03）
4. [3GPP SA2#170 FTP: WT#5 Data Framework Drafts](https://www.3gpp.org/FTP/tsg_sa/WG2_Arch/TSGS2_170_Goteborg_2025-08/INBOX/DRAFTS/FS_6G_ARC) — S2-2506446 系列文稿（数据框架范围定义）
5. [3GPP SA2#174 FTP: FS_6G_ARC Status](https://www.3gpp.org/ftp/tsg_sa/WG2_Arch/TSGS2_174_Malta_2026-04/INBOX/DRAFTS/FS_6G_ARC/General) — 马耳他会议状态与 KI 进展
6. [3GPP CT3 AI/ML Features](https://www.3gpp.org/technologies/ct3-aiml) — NWDAF Rel-19 协议增强总结

### 厂商博客 / 白皮书
7. [Samsung Research: AI in 6G Network (SA Aspect)](https://research.samsung.com/blog/AI-in-6G-network-Service-and-System-Aspect) — 2026.05，6G 数据框架对 AI 跨域支撑的详细分析
8. [Qualcomm: 3GPP Release 20 Blog](https://www.qualcomm.com/news/onq/2025/06/3gpp-release-20-completing-5g-advanced-evolution-preparing-for-global-6g-standardization) — 2025.06，Rel-20 范围和 6G SI 概览
9. [InterDigital: Paving the Path to 6G](https://www.interdigital.com/post/paving-the-path-to-6g-key-takeaways-for-3gpp-release-20) — 2025.06，Rel-20 技术优先级和核心网演进方向

### 分析机构 / 行业组织
10. [GSMA 6G Community Progress Report (May 2026)](https://www.gsma.com/solutions-and-impact/technologies/networks/gsma_resources/gsma-6g-community-industry-progress-report-may-2026/) — SA2#173/174 进展，Rel-21 首个 WI 批准
11. [6G Futures: Outcomes from SA#111 Fukuoka](https://6gfutures.substack.com/p/outcomes-from-the-3gpp-sa-meeting) — 2026.04，TR 22.870 完成、首个 Rel-21 WID 批准
12. [CableLabs: Why the 6G Study Phase Matters Now](https://www.cablelabs.com/blog/why-the-6g-study-phase-matters-now) — 2026.03，FS_6G_ARC 结构与非 3GPP 接入集成
13. [Ofinno: 6G Takes Shape (Standards Readout)](https://ofinno.com/standards-readout/6g-takes-shape-in-gothenburg-and-goa-first-solutions-emerge-as-3gpp-moves-past-problem-identification/) — 2026.02，SA2#173 首次方案探索详细分析
14. [FirstNet Authority: 3GPP Dec 2025 Recap](https://firstnet.gov/newsroom/blog/3gpp-completes-release-19-while-progress-begins-6g-work) — Rel-19 冻结确认、SA2 FS_6G_ARC 20% 进展
15. [WirelessBrew: Comprehensive 6G Study Items Catalog](https://wirelessbrew.com/6g/6G-Study-Items-Rel-20/) — 2026.03，Rel-20 全部 6G SI 列表与时间线
