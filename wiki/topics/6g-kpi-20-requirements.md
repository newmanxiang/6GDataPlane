---
title: 6G KPI 量化指标全表（IMT-2030 技术性能需求）
title_en: 6G KPI - IMT-2030 Technical Performance Requirements
slug: 6g-kpi-20-requirements
category: topic
status: reviewed
confidence: high
sources:
  - https://www.itu.int/hub/2026/03/imt-2030-technical-requirements-for-the-6g-future/
  - https://www.itu.int/en/ITU-R/study-groups/rsg5/rwp5d/imt-2030/Pages/default.aspx
  - https://www.itu.int/dms_pubrec/itu-r/rec/m/R-REC-M.2160-0-202311-I!!PDF-E.pdf
  - https://techblog.comsoc.org/2026/03/17/update-imt-2030-6g-minimum-technology-performance-requirements/
  - https://6g-ia.eu/wp-content/uploads/2025/06/6g_ia-contribution_wp5d-120625.pdf
  - https://arxiv.org/html/2501.14552
  - https://smart-networks.europa.eu/wp-content/uploads/2025/02/white-paper-kpis_17_2_2025_for-rel_.pdf
  - https://techblog.comsoc.org/2025/09/30/should-peak-data-rates-ds-us-be-specified-for-5g-imt-2020-and-6g-imt-2030-networks/
  - https://www.ngmn.org/wp-content/uploads/ITU-R_FRAMEWORK_FOR_IMT-2030.pdf
  - https://www.iafi.in/system/static/uploads/pdf/8-WORKING-DOCUMENTI-TECH-PERF-RFQ.pdf
related:
  - 6g-overview
  - 6g-data-plane
  - user-plane-evolution
  - ai-native-air-interface
  - isac
  - non-terrestrial-network
tags:
  - 6G
  - KPI
  - IMT-2030
  - 性能需求
  - ITU-R
  - TPR
last_verified: 2026-06-21
owner: agent
---

# 6G KPI 量化指标全表

## 核心结论

ITU-R WP 5D 于 2026 年 2 月达成共识，制定了 IMT-2030（6G）无线接口的 **20 项最低技术性能需求（TPR）**，其中 **7 项为 6G 新增**（感知、AI、可持续性、安全与韧性、互操作性、覆盖、定位）。核心量化指标包括：峰值速率研究目标 50/100/200 Gbps（DL）、空口时延 0.1–1 ms、可靠性 1−10⁻⁵ 至 1−10⁻⁷、连接密度 10⁶–10⁸ 设备/km²。该报告将提交 ITU-R SG5 于 2026 年 12 月正式批准，并作为评估 6G 候选无线接口技术（RIT/SRIT）的统一基准。

## 1. 现状定义

### 20 项 TPR 完整列表

| # | 性能需求 | 6G 研究目标值 | 5G 基准值 (M.2410) | 提升幅度 | 来源场景 | 新增? |
|---|---------|-------------|-------------------|---------|---------|------|
| 1 | 峰值速率 (Peak data rate) | 50/100/200 Gbps (DL) | 20 Gbps (DL), 10 Gbps (UL) | 2.5–10× | IC | 否 |
| 2 | 用户体验速率 (User experienced data rate) | 300–500 Mbps | 100 Mbps (DL) | 3–5× | IC | 否 |
| 3 | 峰值频谱效率 (Peak spectral efficiency) | 45–60 bps/Hz (DL), 22.5–30 bps/Hz (UL) | 30 bps/Hz (DL), 15 bps/Hz (UL) | 1.5–2× | IC | 否 |
| 4 | 平均频谱效率 (Average spectral efficiency) | 1.5–3× IMT-2020 | 见 M.2410 各场景值 | 1.5–3× | IC | 否 |
| 5 | 第 5 百分位用户频谱效率 | 1.5–3× IMT-2020 | 见 M.2410 各场景值 | 1.5–3× | IC/UC | 否 |
| 6 | 区域流量容量 (Area traffic capacity) | 30–50 Mbit/s/m² | 10 Mbit/s/m² | 3–5× | IC | 否 |
| 7 | 连接密度 (Connection density) | 10⁶–10⁸ 设备/km² | 10⁶ 设备/km² | 1–100× | MC | 否 |
| 8 | 移动性 (Mobility) | 500–1000 km/h | 500 km/h | 1–2× | IC/UC | 否 |
| 9 | 移动性中断时间 (Mobility interruption time) | TBD (目标 0 ms) | 0 ms | — | IC | 否 |
| 10 | 用户面时延 (User plane latency) | 0.1–1 ms（空口单向） | 4 ms (eMBB), 1 ms (URLLC) | 1–10× | IC/HRLLC | 否 |
| 11 | 控制面时延 (Control plane latency) | 10–20 ms | 20 ms | 1–2× | IC/HRLLC | 否 |
| 12 | 可靠性 (Reliability) | 1−10⁻⁵ 至 1−10⁻⁷ (99.999%–99.99999%) | 1−10⁻⁵ (99.999%) | 1–100× | HRLLC | 否 |
| 13 | 带宽 (Bandwidth) | TBD（6G-IA 建议 ≥400 MHz） | 支持最大 1 GHz 聚合 | 扩展 | 所有 | 否 |
| 14 | **覆盖 (Coverage)** | 定性评估（链路预算分析） | 未作为 TPR | **新增** | UC | **是** |
| 15 | **定位 (Positioning)** | 1–10 cm（水平/垂直） | ~10 m | 100–1000× | ISAC | **是** |
| 16 | **感知相关能力 (Sensing)** | 检测率、精度、分辨率（定性/TBD） | 无 | **全新维度** | ISAC | **是** |
| 17 | **AI 相关能力 (AI capabilities)** | 定性评估（推理即服务、自动化） | 无 | **全新维度** | AIAC | **是** |
| 18 | **可持续性 (Sustainability)** | 能效：研究目标 100× 提升 (1 Gbps/J) | ~10 Mbps/J | 100× | 所有 | **是** |
| 19 | **安全与韧性 (Security & resilience)** | 定性评估（检查/自报告） | 无 | **全新维度** | 所有 | **是** |
| 20 | **互操作性 (Interoperability)** | 定性评估（检查/自报告） | 无 | **全新维度** | UC | **是** |

> **使用场景缩写**: IC = 沉浸式通信, HRLLC = 超高可靠低时延通信, MC = 大规模通信, UC = 泛在连接, AIAC = AI 与通信, ISAC = 通信感知一体化

### 关键说明

- M.2160 中的值是**研究目标范围**，TPR 中的最终"最低需求"数值在 2026-02 草案中仍有部分 TBD，将在 3GPP 评估与后续 WP 5D 会议中确定
- 20 项 TPR 中，13 项继承自 IMT-2020 (M.2410) 并予以增强，7 项为 6G 新增
- 新增 7 项中，定位和感知为可量化指标，其余 5 项以定性方式评估（通过检查或自报告）

## 2. 标准与组织动态

| 时间 | 里程碑 |
|------|--------|
| 2023-11 | ITU-R RA-23 批准 Rec. M.2160（IMT-2030 框架），确认"IMT-2030"命名，定义 6 大使用场景与 15 项能力 |
| 2024-02 | WP 5D #45 启动 TPR 制定，Apple、中国、印度分别提交工作文档提案 |
| 2024-10 | WP 5D 发布联络声明，邀请外部组织提供 TPR 目标值 |
| 2025-02 | WP 5D #47 大量输入文稿讨论，初步 TPR 列表形成 |
| 2025-06 | 6G-IA 提交详细 KPI 目标值提案 (20+ 项指标量化值) |
| **2026-02** | **WP 5D #49 共识达成：20 项 TPR 草案完成**，提交 SG5 审批 |
| 2026-12 | ITU-R SG5 会议计划正式批准 TPR 报告 |
| 2027+ | 候选无线接口技术征集与评估阶段 |

## 3. 关键玩家

- **ITU-R WP 5D**：TPR 制定的唯一权威机构，负责全球统一的 6G 无线接口评估标准
- **3GPP**：将基于 TPR 制定具体 6G RAN/Core 规范（Rel-21 起），3GPP RAN#106 已批准 6G 研究项 (RP-243327)
- **6G-IA / SNS JU（欧盟）**：提供了最详细的量化 KPI 提案；SNS JU 项目验证了多项 KPI 的实验值
- **贡献方**：Nokia、Apple、Huawei、Qualcomm、Samsung、Ericsson、ZTE、InterDigital 联合提交 WP 5D Contribution 1031
- **NGMN**：发布 IMT-2030 框架分析，指出极端需求的商业可行性需审慎评估

## 4. 技术机制：对数据面的影响

### 核心 KPI 对数据面影响矩阵

| KPI | 6G 目标值 | 5G 参考值 | 提升倍数 | 对数据面的影响 |
|-----|----------|----------|---------|--------------|
| **峰值速率** | 200 Gbps (DL) | 20 Gbps | 10× | 转发引擎需支持 >200 Gbps 线速处理；协议栈需极度精简（零拷贝、硬件卸载）；GTP-U 隧道开销可能成为瓶颈 |
| **用户面时延** | 0.1–1 ms | 1–4 ms | 4–40× | 用户面协议栈层数压缩；数据面功能需下沉至边缘；UPF 需亚毫秒级转发 |
| **可靠性** | 99.999%–99.99999% | 99.999% | 1–100× | 数据面需支持包复制、多路径冗余转发、确定性网络（DetNet）机制 |
| **区域流量容量** | 30–50 Mbit/s/m² | 10 Mbit/s/m² | 3–5× | 数据面需支持超密集部署下的海量并发流处理 |
| **连接密度** | 10⁶–10⁸/km² | 10⁶/km² | 1–100× | 会话状态管理扩展性挑战；轻量级协议栈（非 IP 方案）；数据面状态压缩 |
| **移动性中断时间** | 0 ms | 0 ms | — | 先连后断（Make-before-break）机制；数据面需支持无缝切换不丢包 |
| **能效** | 100× 提升 | 基准 | 100× | 数据面需支持深度睡眠、按需激活、流量自适应功率管理 |
| **感知/定位** | cm 级 | 无/10m 级 | 新增 | 数据面需同时承载通信数据与感知数据，协议栈需融合处理 |

### Top 5 对数据面影响最大的指标

1. **峰值速率 (200 Gbps)**：直接决定数据面转发架构的硬件能力上限
2. **用户面时延 (0.1 ms)**：要求数据面协议栈极度精简，功能下沉至网络边缘
3. **可靠性 (10⁻⁷)**：要求数据面实现确定性转发、冗余路径、包级保护
4. **连接密度 (10⁸/km²)**：要求数据面会话管理具备超大规模扩展性
5. **能效 (100×)**：要求数据面实现按需激活、绿色转发架构

## 5. 趋势驱动力

- **沉浸式体验**：全息通信、XR 要求 >200 Gbps 速率 + <1 ms 时延 + >99.999% 可靠性的联合需求
- **AI/ML 大规模部署**：AI 模型分布式训练/推理需要数据面提供高带宽、低时延、确定性的数据传输通道
- **IoT 规模爆发**：2030 年全球联网设备预计超 500 亿，连接密度从 10⁶ 向 10⁸ 扩展
- **通感融合 (ISAC)**：自动驾驶、智慧城市要求通信与感知一体化，数据面需同时处理两种数据流
- **可持续发展**：ESG 压力驱动能效 100× 提升，数据面从"永远在线"转向"智能按需"
- **非地面网络 (NTN)**：卫星/HAPS/无人机扩展覆盖，数据面需适应异构传输介质和高时延链路

## 6. 批评与风险

- **可实现性争议**：NGMN 指出 IMT-2020 的多项极端指标（20 Gbps 峰值、1 ms URLLC 时延）在商用网络中从未实现；多家公司（Apple、Nokia、Deutsche Telekom 等）建议不再为 IMT-2030 定义峰值速率具体数值 [8]
- **理论与实际的鸿沟**：5G 商用网络典型下行速率仅 100–500 Mbps，远低于 20 Gbps 规范值；5G 时延实测 5–20 ms，远高于 1 ms URLLC 目标 [8]
- **新增指标量化困难**：7 项新增 TPR 中有 5 项仅能定性评估（AI、安全、韧性、互操作性、覆盖），缺乏公认的量化方法
- **评估复杂度激增**：20 项 TPR × 6 大使用场景的交叉映射导致评估矩阵急剧扩大
- **频谱挑战**：200 Gbps 峰值速率依赖 >100 GHz 频段（亚太赫兹），该频段传播损耗大、器件成熟度低

## 7. 我司相关性（占位）

> 待补充：我司产品/技术在数据面转发速率、时延、可靠性等维度的现有能力与 6G TPR 的差距分析。

## 矛盾与待核实

1. **峰值速率数值分歧**：M.2160 框架给出"50/100/200 Gbps"作为研究目标范围；6G-IA 2025-06 提案的最低 TPR 值仅 20–50 Gbps（[1-2.5]× IMT-2020）；而学术文献常引用 200 Gbps 作为标志性数字。原因：M.2160 的"研究目标"与 TPR 的"最低需求"是不同层级 → 详见 contradictions.md
2. **可靠性范围分歧**：M.2160 定义 1−10⁻⁵ 到 1−10⁻⁷；个别学术论文引用至 1−10⁻⁹ → 超出官方框架 → 详见 contradictions.md
3. **连接密度**：M.2160 目标 10⁶–10⁸；6G-IA TPR 提案仅 10⁶–10⁷；SNS JU 项目实测更低（0.1–10 设备/m²）

## 数据缺口

1. **TPR 最终数值**：草案中多项指标标注"TBD"，最终值待 2026-12 SG5 批准后公开
2. **新增 7 项指标的量化方法**：感知、AI、安全等指标的评估方法论仍在制定中
3. **3GPP 对应需求**：3GPP Rel-21/22 如何将 ITU-R TPR 映射为具体技术规范尚不明确
4. **数据面专项分析**：尚无公开文献系统分析 20 项 TPR 对 6G 数据面架构的逐项影响

## 来源

### 一手资料 / 官方
- [1] [IMT-2030: Technical requirements for the 6G future](https://www.itu.int/hub/2026/03/imt-2030-technical-requirements-for-the-6g-future/) — ITU 官方博客, 2026-03-17
- [2] [IMT towards 2030 and beyond](https://www.itu.int/en/ITU-R/study-groups/rsg5/rwp5d/imt-2030/Pages/default.aspx) — ITU-R WP 5D 官方门户
- [3] [Rec. ITU-R M.2160-0](https://www.itu.int/dms_pubrec/itu-r/rec/m/R-REC-M.2160-0-202311-I!!PDF-E.pdf) — IMT-2030 框架建议书, 2023-11
- [4] [WP 5D Contribution 1031](https://www.itu.int/md/R23-WP5D-C-1031/en) — Nokia, Apple, Huawei 等 8 家联合提交, 2026-01
- [5] [IAFI Working Document: TPR for IMT-2030](https://www.iafi.in/system/static/uploads/pdf/8-WORKING-DOCUMENTI-TECH-PERF-RFQ.pdf) — 含 20 项 TPR 完整结构

### 行业组织
- [6] [6G-IA Contribution to WP 5D: KPI Target Values](https://6g-ia.eu/wp-content/uploads/2025/06/6g_ia-contribution_wp5d-120625.pdf) — 6G-IA/SNS JU, 2025-06
- [7] [NGMN: ITU-R Framework for IMT-2030](https://www.ngmn.org/wp-content/uploads/ITU-R_FRAMEWORK_FOR_IMT-2030.pdf) — NGMN 分析, 2024-02
- [8] [SNS JU: 6G KPIs – Definitions and Target Values](https://smart-networks.europa.eu/wp-content/uploads/2025/02/white-paper-kpis_17_2_2025_for-rel_.pdf) — SNS JU TMV WG 白皮书, 2025-02

### 学术
- [9] [6G Cellular Networks: Mapping the Landscape for IMT-2030](https://arxiv.org/html/2501.14552) — Hossain et al., IEEE Trans. Technology & Society, 2025
- [10] [Synthetizing 6G KPIs for Diverse Future Use Cases](https://www.mdpi.com/1999-5903/18/1/63) — Future Internet, 2026-01

### 技术博客 / 分析
- [11] [IMT-2030 ("6G") Minimum TPR](https://techblog.comsoc.org/2026/03/17/update-imt-2030-6g-minimum-technology-performance-requirements/) — IEEE ComSoc Tech Blog, 2026-03
- [12] [Should Peak Data Rates be specified for 6G?](https://techblog.comsoc.org/2025/09/30/should-peak-data-rates-ds-us-be-specified-for-5g-imt-2020-and-6g-imt-2030-networks/) — IEEE ComSoc Tech Blog, 2025-09
- [13] [IMT-2030 TPR from ITU-R WP5D](https://techblog.comsoc.org/2024/01/19/imt-2030-technical-performance-requirements-tpr-from-itu-r-wp5d/) — IEEE ComSoc Tech Blog, 2024-01
