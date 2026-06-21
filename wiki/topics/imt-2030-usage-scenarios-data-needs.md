---
title: IMT-2030 使用场景及其数据面需求
title_en: IMT-2030 Usage Scenarios and Data Plane Requirements
slug: imt-2030-usage-scenarios-data-needs
category: topic
status: reviewed
confidence: high
sources:
  - https://www.itu.int/dms_pubrec/itu-r/rec/m/R-REC-M.2160-0-202311-I!!PDF-E.pdf
  - https://www.itu.int/hub/2026/03/imt-2030-technical-requirements-for-the-6g-future/
  - https://www.itu.int/en/ITU-R/study-groups/rsg5/rwp5d/imt-2030/Pages/default.aspx
  - https://www.ngmn.org/wp-content/uploads/ITU-R_FRAMEWORK_FOR_IMT-2030.pdf
  - https://6g-ia.eu/wp-content/uploads/2025/06/6g_ia-contribution_wp5d-120625.pdf
  - https://arxiv.org/html/2501.14552v2
  - https://techblog.comsoc.org/2026/03/17/update-imt-2030-6g-minimum-technology-performance-requirements/
  - https://techblog.comsoc.org/2025/02/13/itu-r-wp-5d-progresses-reports-on-imt-2030-6g-minimum-technology-performance-requirements-evaluation-criteria-methodology/
  - https://www.5gamericas.org/wp-content/uploads/2024/08/ITUs-IMT-2030-Vision_Id.pdf
  - https://www.iafi.in/system/static/uploads/pdf/8-WORKING-DOCUMENTI-TECH-PERF-RFQ.pdf
  - https://digitalregulation.org/overview-of-6g-imt-2030/
  - https://www.mdpi.com/1999-5903/18/1/63
related:
  - 6g-overview
  - 6g-data-plane
  - user-plane-evolution
  - isac
  - ai-native-air-interface
  - non-terrestrial-network
tags:
  - IMT-2030
  - 6G
  - 使用场景
  - 数据面
  - ITU-R
  - M.2160
  - 技术性能需求
last_verified: 2026-06-21
owner: agent
---

# IMT-2030 使用场景及其数据面需求

## 核心结论（执行摘要）

ITU-R 建议书 M.2160（2023 年 11 月）定义了 IMT-2030 的六大使用场景，其中三个扩展自 5G（沉浸式通信、超可靠低时延通信、大规模通信），三个为全新场景（泛在连接、AI 与通信融合、通感一体）。2026 年 2 月 ITU-R WP 5D 就 20 项技术性能需求（TPR）达成一致，其中 7 项为 6G 新增指标。关键数据面参数包括：峰值速率目标 50–200 Gbps（5G 的 2.5–10 倍）、用户体验速率 300–500 Mbps、空口时延 0.1–1 ms、连接密度 10⁶–10⁸ 设备/km²、定位精度 1–10 cm。这些场景对 6G 数据面提出了根本性新要求——不仅需要更高吞吐和更低时延，还需原生支持感知数据、AI 模型数据等全新数据类型。

## 1. 现状定义

IMT-2030 是 ITU-R 为 2030 年及以后的移动通信系统制定的框架，正式发布为建议书 ITU-R M.2160（2023 年 11 月）。该框架将使用场景从 IMT-2020（5G）的三个扩展为六个：

| 场景 | 缩写 | 继承关系 | 典型用例 |
|------|------|---------|---------|
| 沉浸式通信 | IC | eMBB 扩展 | XR、全息通信、远程临场 |
| 超可靠低时延通信 | HRLLC | URLLC 扩展 | 工业全自动化、远程医疗、应急服务 |
| 大规模通信 | MC | mMTC 扩展 | 智慧城市、交通物流、环境监测 |
| 泛在连接 | UC | 全新 | 弥合数字鸿沟、卫星-地面融合 |
| AI 与通信融合 | AIAC | 全新 | 分布式 AI 训练/推理、算力编排 |
| 通感一体 | ISAC | 全新 | 高精度定位、环境感知、目标追踪 |

四个跨场景设计原则（overarching aspects）贯穿所有场景：可持续性、安全与韧性、连接未连接者、泛在智能。

## 2. 标准与组织动态（近 3 年）

- **2023-11**：ITU-R RA-23 批准 M.2160，确认"IMT-2030"名称与六大使用场景框架
- **2024-01**：WP 5D 启动技术性能需求（TPR）制定，Apple、中国、印度分别提交提案
- **2024-12**：3GPP RAN#106 批准 6G 研究项（RP-243327），基于 M.2160 研究最低 TPR 候选项
- **2025-02**：WP 5D 会议讨论 TPR 草案，形成 20 项需求初步清单；3GPP 计划于 RAN#112（2026 年 6 月）产出 TR 38 系列"6G 场景与需求研究"
- **2025-06**：6G-IA 代表欧洲产业向 WP 5D 提交具体 TPR 目标值提案
- **2026-02**：WP 5D 就 IMT-2030 的 20 项 TPR 达成一致，7 项为 6G 新增（含感知、AI、能效等），待 2026 年 12 月 ITU-R SG5 正式批准

## 3. 关键玩家

- **ITU-R WP 5D**：框架制定与 TPR 定义的核心机构，协调全球共识
- **3GPP**：负责详细技术规范（Rel-22/23），将 ITU-R 框架转化为可实现的标准；6G 研究项 RP-243327 为关键衔接点
- **NGMN**：运营商联盟，2024 年 2 月发布 M.2160 评估报告，识别 50 个 6G 用例并分四类（增强人类通信、增强机器通信、使能服务、网络演进），对极端指标提出商业可行性质疑
- **6G-IA / SNS JU**：欧洲产业协会，2025 年提交具体 TPR 目标值，代表 Ericsson、Nokia、Orange、Telefónica、TIM
- **Hexa-X / Hexa-X-II**：欧盟旗舰 6G 研究项目，发布 D1.4 交付件定义 6G 价值与需求
- **5G Americas / Next G Alliance**：美洲视角，关注频谱策略与区域商业化路径
- **主要厂商**：Nokia、Apple、Huawei、Qualcomm、Samsung、Ericsson、ZTE、InterDigital 联合提交 WP 5D 贡献（文件 5D/C-1031，2026-01）

## 4. 技术机制：各场景的数据面需求分析

### 4.1 沉浸式通信（IC）

对数据面冲击最大的场景。需要同步传输视频、音频、触觉等多模态数据流。

| 指标 | 目标值 | 对比 5G |
|------|--------|---------|
| 峰值速率（DL） | 20–50 Gbps | 1–2.5× |
| 用户体验速率（密集城区 DL） | 125–500 Mbps | 1.25–5× |
| 区域流量容量（室内热点 DL） | 10–50 Mbps/m² | 1–5× |
| 用户面时延 | 2–8 ms | — |
| 控制面时延 | 10–20 ms | — |

数据面影响：需支持时间同步的多流混合传输、超高吞吐的边缘缓存与分发。

### 4.2 超可靠低时延通信（HRLLC）

| 指标 | 目标值 | 对比 5G |
|------|--------|---------|
| 用户面时延 | 1 ms | ≤ 5G |
| 可靠性 | 99.999%（10⁻⁵） | 比 5G 更严格 |

数据面影响：需在极低时延下保证数据交付确定性，对转发路径、缓存策略提出苛刻要求。

### 4.3 大规模通信（MC）

| 指标 | 目标值 | 对比 5G |
|------|--------|---------|
| 连接密度 | 10⁶–10⁷ 设备/km² | 1–10× |

数据面影响：海量小数据包的高效聚合、低功耗数据采集通道。

### 4.4 泛在连接（UC）

非量化场景，重点在覆盖扩展与异构网络互通（NTN、Wi-Fi、广播）。数据面需支持跨接入技术的无缝数据会话迁移。

### 4.5 AI 与通信融合（AIAC）

全新数据类型涌入数据面：AI 模型参数、训练数据集、推理请求/响应。需要数据采集-预处理-分发的端到端管道、分布式模型训练的大规模数据同步、以及计算资源与数据的联合编排。

### 4.6 通感一体（ISAC）

引入感知数据流作为全新数据类型：点云、雷达回波、环境地图。ETSI ISC 组识别了 18 个 ISAC 用例，要求定位精度 1–10 cm。3GPP 正讨论感知管理功能（SeMF）和感知数据在用户面/SBI 中的传输方案。数据面需新增感知数据通道。

## 5. 趋势驱动力

- **沉浸式体验需求**：XR、全息通信推动峰值速率与时延的同步提升
- **AI 渗透**：AI 原生设计理念要求数据面从"纯转发"转向"数据服务化"（DaaS）
- **感知融合**：ISAC 使通信网络兼具雷达功能，催生全新数据类型与处理流程
- **数字鸿沟**：UC 场景推动 NTN 融合与跨接入互通
- **可持续性**：能效目标（100× 于 5G）约束数据面设计必须兼顾性能与能耗
- **垂直行业数字化**：工业 4.0/5.0、自动驾驶、智慧医疗对确定性数据面提出刚性需求

## 6. 批评与风险

- **极端指标难以商用**：NGMN 明确指出 5G 的极端能力（20 Gbps、1 ms 时延）"已被证明难以交付"，IMT-2030 更极端的目标面临同样风险（NGMN 2024）
- **框架 vs 最低需求的落差**：M.2160 框架的研究目标（如 200 Gbps 峰值速率）与 6G-IA 提交的 TPR 值（20–50 Gbps）差距显著，表明产业共识正向保守收敛
- **新场景商业模式不清**：AIAC、ISAC 作为全新场景，缺乏成熟的商业模式论证；NGMN 指出许多用例"可通过高级 5G 网络实现"
- **能效悖论**：更高能力（大带宽、massive MIMO）与更低能耗目标之间的固有矛盾
- **感知隐私**：ISAC 引入的环境感知能力触发隐私与安全合规风险，ETSI 和 3GPP 正在研究对策
- **定量指标因场景而异**：ITU-R 明确"能力值仅适用于部分使用场景，不可在单一场景中同时达到"——可能造成对 6G 能力的过度期望

## 7. 我司相关性（占位）

> 待 6g-insight-report 阶段结合 ops/company-context.md 填充。

## 矛盾与待核实

1. **峰值速率目标分歧**：M.2160 框架给出 50/100/200 Gbps 作为研究目标，但 6G-IA（2025-06）提交 TPR 仅为 20–50 Gbps（DL）。二者性质不同（框架愿景 vs 最低技术需求），但差异可能引发对 6G 实际能力的认知偏差。→ 已记入 analysis/contradictions.md
2. **连接密度范围**：M.2160 给出 10⁶–10⁸ devices/km²，6G-IA 提交 10⁶–10⁷，上限差 10 倍。→ 已记入 analysis/contradictions.md

## 数据缺口

1. 各使用场景对应的数据类型（结构化 vs 非结构化、流式 vs 批量）尚无标准化分类
2. AIAC 场景的 AI 模型数据流量定量估算缺乏公开研究
3. ISAC 感知数据在核心网数据面中的传输方案仍在 3GPP 讨论中（多个竞争方案）
4. 六个场景的 TPR 最终确认值待 2026 年 12 月 SG5 正式批准

## 来源

### 一手资料 / 官方
1. [ITU-R M.2160-0 (11/2023)](https://www.itu.int/dms_pubrec/itu-r/rec/m/R-REC-M.2160-0-202311-I!!PDF-E.pdf) — IMT-2030 框架建议书，定义六大使用场景与 15 项能力
2. [IMT-2030 官方页面](https://www.itu.int/en/ITU-R/study-groups/rsg5/rwp5d/imt-2030/Pages/default.aspx) — ITU-R WP 5D 工作门户
3. [IMT-2030: Technical requirements for the 6G future (2026-03)](https://www.itu.int/hub/2026/03/imt-2030-technical-requirements-for-the-6g-future/) — 20 项 TPR 达成一致的官方公告
4. [WP 5D Contribution 1031 (2026-01)](https://www.itu.int/md/R23-WP5D-C-1031/en) — Nokia/Apple/Huawei/Qualcomm/Samsung/Ericsson/ZTE 联合提交的 TPR 贡献
5. [IAFI Working Document on TPR](https://www.iafi.in/system/static/uploads/pdf/8-WORKING-DOCUMENTI-TECH-PERF-RFQ.pdf) — 含 15 项能力值表与评估方法论

### 学术
6. [6G Cellular Networks: Mapping the Landscape for the IMT-2030 Framework (arXiv 2501.14552)](https://arxiv.org/html/2501.14552v2) — 综合文献综述，含 5G/6G 对比表
7. [Synthetizing 6G KPIs for Diverse Future Use Cases (Future Internet, 2026-01)](https://www.mdpi.com/1999-5903/18/1/63) — 跨 3GPP Release 分析 6G KPI 框架

### 厂商白皮书 / 产业联盟
8. [NGMN: ITU-R Framework for IMT-2030 Review (2024-02)](https://www.ngmn.org/wp-content/uploads/ITU-R_FRAMEWORK_FOR_IMT-2030.pdf) — 运营商联盟对 M.2160 的评估与批评
9. [6G-IA Contribution to WP 5D on TPR (2025-06)](https://6g-ia.eu/wp-content/uploads/2025/06/6g_ia-contribution_wp5d-120625.pdf) — 欧洲产业界 TPR 具体目标值提案
10. [5G Americas: ITU's IMT-2030 Vision (2024-08)](https://www.5gamericas.org/wp-content/uploads/2024/08/ITUs-IMT-2030-Vision_Id.pdf) — 美洲视角白皮书

### 分析机构 / 媒体
11. [IEEE ComSoc: IMT-2030 TPR Update (2026-03)](https://techblog.comsoc.org/2026/03/17/update-imt-2030-6g-minimum-technology-performance-requirements/) — WP 5D 2026-02 会议成果报道
12. [IEEE ComSoc: WP 5D TPR Progress (2025-02)](https://techblog.comsoc.org/2025/02/13/itu-r-wp-5d-progresses-reports-on-imt-2030-6g-minimum-technology-performance-requirements-evaluation-criteria-methodology/) — WP 5D 2025-02 会议成果报道
13. [Overview of 6G (IMT-2030) — Digital Regulation Platform](https://digitalregulation.org/overview-of-6g-imt-2030/) — 综合概述
