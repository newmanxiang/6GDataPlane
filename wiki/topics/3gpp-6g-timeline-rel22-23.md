---
title: 3GPP 6G 标准时间线与里程碑（Rel-22/23 规划）
title_en: 3GPP 6G Standardization Timeline and Milestones (Rel-22/23 Roadmap)
slug: 3gpp-6g-timeline-rel22-23
category: topic
status: reviewed
confidence: medium
sources:
  - 3gpp-rel21-timeline-official
  - 3gpp-release-20-page
  - 3gpp-release-21-page
  - 3gpp-fukuoka-tsg111
  - 3gpp-singapore-tsg112-6g-38914
  - ieee-comsoc-rel21-timeline-blog
  - tecknexus-3gpp-6g-timeline
  - lightreading-6g-specs-2029
  - ericsson-6g-timeline-blog
  - cafetele-6g-timeline
  - qualcomm-rel20-pdf
  - 6gfutures-fukuoka-ran
  - itu-r-imt2030-submission
  - techtimes-6g-fork
  - fierce-mwc2026-6g
  - 6g-ai-roadmap
related:
  - 3gpp-rel-19-20-data-architecture-status
  - 6g-data-plane-architecture-2025
  - imt-2030-usage-scenarios-data-needs
  - 6g-kpi-20-requirements
  - ai-native-data-plane-status
tags:
  - 3gpp
  - 6g
  - standardization
  - rel-21
  - rel-22
  - rel-23
  - timeline
  - imt-2030
  - migration
last_verified: 2026-06-25
owner: agent
---

# 3GPP 6G 标准时间线与里程碑（Rel-22/23 规划）

## 核心结论（执行摘要）

3GPP 于 **2026 年 6 月 10 日（TSGs#112 新加坡）正式批准了 Rel-21 时间线**，确立首个 6G 规范版本的 ASN.1/OpenAPI 冻结日期为 **2029 年 3 月**——这是芯片设计和设备认证的关键锚点 [高信心]。从 Rel-19（已冻结）到 Rel-21（首个 6G 规范），3GPP 采取"**两个 Release 完成 6G**"策略：Rel-20 承载研究（14 个 6G SI），Rel-21 承载规范化工作 [高信心]。**Rel-22/23 目前无正式时间线**，行业共识将其定位为 2030-2032 年的 6G 增强版本，类比 5G 中 Rel-16/17 对 Rel-15 的增强角色 [中信心]。6G 数据面最直接标准化入口为 FS_6G_ARC **WT#5 数据框架**（KI#21）和 CT 用户面协议研究（TR 29.841），前者目标 2027.03 完成 [高信心]。

## 1. 现状定义

### 术语与范围

- **Rel-21**：首个包含规范性（normative）6G 技术规范的 Release，同时包含 5G-Advanced 收尾工作
- **Rel-22/23**：尚未正式启动的后续 Release，预计为 6G 增强/优化版本
- **IMT-2030**：ITU-R 对 6G 的正式命名（Recommendation M.2160，2023-12 发布）
- **ASN.1/OpenAPI 冻结**：芯片和设备可据此实现互操作的协议编码定型点
- **6G 术语**（TSGs#112 批准）：6GR（6G Radio）、6G RAT、6G RAN、6GC/6G CN（6G Core Network）、6GS（6G System）

### 与相邻卡片的边界

本卡片聚焦 **整体时间线路线图与里程碑**，与 `3gpp-rel-19-20-data-architecture-status`（侧重 Rel-19/20 技术内容）、`6g-data-plane-architecture-2025`（侧重架构方案）互补。

## 2. 标准与组织动态（2023–2029）

### 完整时间线路线图

| 阶段 | Release | 时间跨度 | 关键里程碑 | 6G 定位 |
|---|---|---|---|---|
| **准备期** | Rel-19 | 2024.03–2025.12 | 功能冻结 2025.09；ASN.1 冻结 2025.12 | 5G-A 第二版 + 6G 初步需求研究启动 |
| **研究期** | Rel-20 | 2024.03–2027.06 | Stage-2 冻结 2026.09；Stage-3 冻结 2027.03；ASN.1 2027.06 | **双轨制**：5G-A 收官 + 14 个 6G SI |
| **规范化期** | Rel-21 | 2025.11–2029.03 | Package 2027.03；Stage-2 2028.06；Stage-3 2028.12；ASN.1 **2029.03** | **首个 6G 规范版本** + 5G-A 最终增强 |
| **增强期** | Rel-22 | ~2029–2031（推测） | 未定 | 6G 增强优化，可能补充 ITU 提交 |
| **成熟期** | Rel-23 | ~2031–2032（推测） | 未定 | 6G 高级特性、商用反馈迭代 |

### Rel-21 确认时间线（2026.06.10 批准）

| 里程碑 | 目标日期 | TSG# | 说明 |
|---|---|---|---|
| 5G-A/6G Package 批准 & Stage-1 冻结 | **2027.03** | TSG#115 | WI/SI 选定，服务需求定型 |
| Stage-2 冻结 | **2028.06** | TSG#120 | 系统架构定型 |
| Stage-2 80% 检查点 | 2028.03 | TSG#119 | 进度监控 |
| Stage-3 冻结 | **2028.12** | TSG#122 | 协议规范定型 |
| ASN.1/OpenAPI 冻结 | **2029.03** | TSG#123 | 编码定型，设备可据此制造 |

### 当前（2026.06）6G 研究进展快照

| 研究项 | 工作组 | 进度 | 目标完成 | 产出 |
|---|---|---|---|---|
| FS_6G_REQ（TR 22.870） | SA1 | **100%** ✅ | 2026.03 | 590+ 页，6G 用例与需求 |
| FS_6G_RAN_Scen_Req（TR 38.914） | TSG RAN | **100%** ✅ | 2026.06 | 6G 场景、KPI、迁移需求 |
| FS_6G_ARC（TR 23.801） | SA2 | **30%** | 2027.03 | 24 个 KI，含 WT#5 数据框架 |
| FS_6G_Radio（TR 38.960） | RAN1/2/3/4 | ~15% | 2027.06 | 6G 无线技术方案 |
| CT 6G 协议研究 | CT1/CT4 | 早期 | 2027.09 | TR 29.840/841/842（CP/UP/韧性） |
| FS_6G_SEC / FS_6G_OAM / FS_6G_APP 等 | SA3/5/6 | 早期 | 2027+ | 安全/管理/应用使能 |

### Rel-22/23 现状评估

**关键判断**：Rel-22/23 尚无任何正式 3GPP 规划文档或时间线讨论。当前信息源均为行业推测：

- **IEEE ComSoc**（2026.01）：将 Rel-22+ 定位为"扩展互操作性、优化和生态兼容性"
- **6G-AI.com**：将 Rel-22/23 定位为"2030-2031 增强阶段"
- **arXiv 综述**（2024.07）："尚不确定 Rel-22 是否会像 Rel-16 补充 Rel-15 那样补充 ITU 提交"
- **Qualcomm Rel-20 白皮书**：路线图中标注"Release 22 and beyond"位于 2029+ 区间

**历史类比**：5G 标准化中，Rel-15（首个 5G 版本，2018）→ Rel-16（第二版，2020）→ Rel-17（第三版，2022），每版间隔约 18-24 个月。若同模式，Rel-22 ASN.1 冻结预计 **~2031 年中**。

## 3. 关键玩家

### 标准化竞争格局

| 参与方 | 角色/立场 | 影响力指标 |
|---|---|---|
| **中国移动** | 首个 6G 场景标准化项目的 Lead Rapporteur | TR 22.870 中 6G 需求定义影响力最大 |
| **Samsung** | TSG RAN 主席（Younsun Kim）；推动 AI 使能 NF | 程序性影响力极高 |
| **Ericsson** | 保守"演进"路线；主张 OFDM 延续；强调时间线纪律 | 白皮书/标准化时间线定义领导者 |
| **华为** | 激进路线："新空口" + DaaS/DCP；WT#5 主要贡献方 | 5G SEP 数量第一，6G 延续进攻 |
| **Qualcomm** | "用户面优先"架构；Modem IP 不可替代 | 设备侧标准化话语权 |
| **Nokia** | 中间路线；数据信息层增强 | 6G 架构白皮书系列 |
| **Vodafone** | 运营商代表；要求加速迁移决策 | 直接影响部署时间线 |
| **Korea（TTA）** | 国家 6G 计划 + 5G SA 先发优势 | 2030 商用目标匹配 3GPP 时间线 |
| **中国** | U6GHz 频段率先分配 6G 测试 | 实测数据支撑标准化提案 |

### 迁移决策的关键分歧

TSG RAN#112（2026.06）**未能就迁移架构达成决策**。三个主要选项：
1. **Option 1**：6G 锚定双连接（6G-anchored DC with NR）
2. **Option 3**：双栈（Dual Stack）
3. 其他方案待讨论

决策推迟至 **TSG RAN#113（2026.09 马德里）**。Vodafone 明确警告："9 月做出好的迁移决策需要现在就做出硬件影响决策"。

## 4. 技术机制

### 6G 数据面标准化入口

从 Rel-20 研究到 Rel-21 规范的数据面相关路径：

```
Rel-20（研究）                    Rel-21（规范化）
────────────────────────────────────────────────────────
FS_6G_ARC WT#5 ──────────────→ 6G 数据框架 TS（2027-2028）
  └─ KI#21: 数据收集/分发/处理/     └─ 数据收集接口
       存储/访问/暴露框架            └─ AI 数据管道规范
                                    └─ 跨域数据传输机制

FS_6G_ARC WT#1.2 ─────────────→ 增强 SBA/暴露框架 TS
  └─ SBA 框架增强                    └─ SBI 化 UPF 控制接口
  └─ 用户面架构增强                  └─ 统一数据暴露 API

CT 用户面研究 ─────────────────→ 6G UP 协议 TS
  └─ TR 29.841（2027.09）            └─ 6G N4 替代方案

FS_6G_Radio RAN2/3 ───────────→ RAN-CN 接口 TS
  └─ 数据收集通道                    └─ AI 数据上行协议
```

### Rel-22/23 可能承载的数据面增强（推测）

基于 5G 先例（Rel-16/17 增强 Rel-15）：
- **Rel-22**：数据框架 Phase 2（高级 AI 数据管道、联邦学习支持增强、ISAC 数据融合）
- **Rel-23**：数据面高级特性（语义通信数据管道、量子安全数据传输、超大规模 IoT 数据聚合）

## 5. 趋势驱动力

1. **ITU IMT-2030 时间压力**：技术提案窗口 2027.02–2029.02，3GPP 需在此期间提交基于 Rel-21 的自评估。Rel-22 可能补充提交（如 Rel-16 补充 Rel-15）
2. **WRC-27 频谱决策**：6G 频段（含 U6GHz、sub-THz）分配将直接影响 Rel-21/22 技术选择
3. **芯片开发窗口**：ASN.1 冻结（2029.03）后需 12-18 个月完成芯片流片，2030 商用部署可行
4. **"单次交付"策略**：Rel-21 采用单一 code freeze（非分阶段交付），增加时间压力
5. **AI/ML 全面渗透**：每一层标准（RAN/SA/CT）都在讨论 AI 集成，增加跨 WG 协调复杂度
6. **地缘竞争加速**：中国 U6GHz 频段先发 + 标准化席位优势迫使其他区域加速参与

## 6. 批评与风险

1. **时间线极紧**：从 Package 批准（2027.03）到 Stage-3 冻结（2028.12）仅 21 个月，与 5G 相当但 6G 复杂度更高
2. **研究深度不足风险**：FS_6G_ARC 截至 2026.06 仅完成 30%（距 2027.03 目标仅 9 个月），SA2 需大量 ad-hoc 会议
3. **迁移决策持续推迟**：从 TSG#111 推迟至 TSG#112，再推迟至 TSG#113——硬件影响决策的时间窗正在关闭
4. **Rel-22 定义真空**：无任何官方文档讨论 Rel-22 时间线和范围，产业界对"6G 增强路径"缺乏可规划性
5. **地缘碎片化风险**：Ericsson（OFDM 演进）vs 华为（新空口）的技术路线分歧叠加政治因素，可能导致 6G 标准分叉
6. **Rel-21 容量限制**：单一 Release 需同时容纳 6G + 5G-A 工作项，资源分配竞争激烈
7. **研究→规范转化不确定性**：WT#5 数据框架目前仅是研究报告中的一个 KI，能否在 Rel-21 获得独立 WI 立项未定

## 7. 我司相关性（占位）

> 待读取 `ops/company-context.md` 后由 `6g-insight-report` 阶段填充。

初步映射方向：
- **标准化参与窗口**：2026 Q3–2027 Q1 是影响 Rel-21 6G 数据面规范的最后窗口（Package 批准前）
- **WT#5 数据框架**：直接关联产品/方案的标准化锚点，需跟踪 SA2 后续输出
- **CT 用户面研究（TR 29.841）**：决定 6G 用户面协议栈设计方向
- **Rel-22 规划参与**：提前 3 年准备 Rel-22 增强提案可获得先发优势

## 矛盾与待核实

### 矛盾 13：Rel-21 "首个 6G 规范" vs "首个 6G 规范版本"定义分歧

- **主张 A**：Rel-21 是"首个包含 6G 规范的 Release"（也包含大量 5G-A 内容）— 来源 3GPP 官方 Rel-21 页面 (标准/2026-06)
- **主张 B**：Rel-21 是"首个 6G Release"（暗示主要内容为 6G）— 来源 多家媒体报道 (媒体/2026)
- **现状**：3GPP 明确说"Release 21 will be the first normative 6G release, but will also see a lot of 5G-Advanced specification work"
- **本调研倾向**：A——Rel-21 是混合 Release，非纯 6G Release
- **何时能解决**：Rel-21 WI 清单确定后（2027.03）
- **关联章节**：本卡片 §2

### 矛盾 14：Rel-22 是否补充 ITU IMT-2030 提交

- **主张 A**：3GPP 可能像 Rel-16 补充 IMT-2020 那样，用 Rel-22 更新 IMT-2030 提交 — 来源 arXiv 2407.09398 (学术/2024-07)
- **主张 B**：ITU 最终提交截止 2030 年中，仅 Rel-21 即可满足 — 来源 3GPP Release 20 页面 (标准/2026)
- **现状**：无官方表态。ITU 允许 2030 年中前提交完整系统定义
- **本调研倾向**：不下结论。取决于 Rel-21 完成度和 ITU 评估反馈
- **何时能解决**：2029 年 ITU 评估反馈后
- **关联章节**：本卡片 §2, §5

### 矛盾 15：6G 商用时间分歧

- **主张 A**：首批商用 6G 网络 ~2030 年 — 来源 Ericsson/3GPP/多数行业共识 (多源/2024-2026)
- **主张 B**：可能提前至 2028-2029 年（部分区域试点）— 来源 arXiv 2407.09398 (学术/2024-07)
- **主张 C**：实际大规模商用可能需要 2031+ — 来源 Light Reading 分析 (媒体/2026-06)
- **现状**：ASN.1 冻结 2029.03 → 芯片 12-18 月 → 2030 中大规模可行是共识时间线
- **本调研倾向**：A（~2030 首批商用），依据 ASN.1 → 芯片 → 部署的固有周期
- **何时能解决**：Rel-21 时间线按计划执行后（2028-2029）
- **关联章节**：本卡片 §2, §5

## 数据缺口

- **P1**：Rel-22 正式启动时间和范围讨论——3GPP 尚未在任何公开文档中提及 Rel-22 规划
- **P1**：FS_6G_ARC 2026 下半年加速计划细节——SA2 ad-hoc 会议日程和 WT#5 完成进度指标
- **P1**：TSG RAN#113（2026.09 马德里）迁移架构决策结果——直接影响数据面协议设计
- **P1**：Rel-21 6G WI 候选清单——Package 批准前需确认数据框架是否获得独立 WI
- **P2**：ITU-R WP 5D 对 3GPP 首次提交（2027 中）的评估反馈——影响后续 Release 方向
- **P2**：各公司在 CT 用户面研究（TR 29.841）中的具体提案方向

## 来源

### 一手资料 / 官方
1. [3GPP: Timeline for Release 21](https://www.3gpp.org/news-events/3gpp-news/rel21-timeline) — 2026.06.10，Rel-21 时间线正式批准公告
2. [3GPP: Release 21 Official Page](https://www.3gpp.org/specifications-technologies/releases/release-21) — 首个 6G 规范 Release 描述
3. [3GPP: Release 20 Official Page](https://www.3gpp.org/specifications-technologies/releases/release-20) — Rel-20 双轨结构、14 个 6G SI 列表
4. [3GPP: First 6G RAN Study Approved (TR 38.914)](https://www.3gpp.org/news-events/3gpp-news/6g-38914) — 2026.06.14，6G 术语、RAN 研究完成
5. [3GPP: First Study, New Generation (TSGs#111 Fukuoka)](https://www.3gpp.org/news-events/3gpp-news/fukuoka-tsg111) — TR 22.870 批准、CT 研究启动、Rel-21 时间线讨论
6. [3GPP Portal: Release Details](https://portal.3gpp.org/Releases.aspx) — Release 状态表（Rel-21 Open since 2025-11-04）
7. [ITU-R: Submission & Evaluation Process for IMT-2030](https://www.iafi.in/system/static/uploads/pdf/9-WORKING-DOCUMENTI-IMT-PROCESS.pdf) — WP 5D 提交窗口 2027.02–2029.02

### 厂商白皮书 / 博客
8. [Ericsson: 6G Standardization Timeline and Principles](https://www.ericsson.com/en/blog/2024/3/6g-standardization-timeline-and-technology-principles) — 2024.03，Rel-21 目标 2028 年底
9. [Qualcomm: 3GPP Release 20 PDF](https://www.qualcomm.com/content/dam/qcomm-martech/dm-assets/documents/3GPP-Release-20.pdf) — 2025.06，Rel-20/21/22 路线图

### 分析机构 / 媒体
10. [IEEE ComSoc: 3GPP Approves Timelines for Release 21](https://techblog.comsoc.org/2026/06/16/3gpp-approves-timelines-for-release-21-which-will-specify-6g-ran-and-5g-advanced/) — 2026.06.16，TSG#112 决策详述
11. [TecKNexus: 3GPP 6G Timeline Confirmed](https://tecknexus.com/3gpp-6g-standardization-timeline-singapore-2026/) — 2026.06.16，企业规划视角
12. [Light Reading: It's Official – 6G Specs Set for Early 2029](https://www.lightreading.com/6g/it-s-official-6g-specs-are-set-for-early-2029) — 2026.06.16，"单次交付"策略分析
13. [6G Futures: Outcomes from 3GPP RAN Meeting in Fukuoka](https://6gfutures.substack.com/p/outcomes-from-the-3gpp-ran-meeting) — 2026.04.05，TSG#111 深度分析
14. [CafeTele: 6G Standardisation Timeline](https://www.cafetele.com/articles/article-6g-standardisation-timeline-3gpp.html) — 2026.06.03，ITU-3GPP 时间线对齐综述
15. [Light Reading: 6G is Forking](https://www.lightreading.com/6g/6g-is-forking-with-consequences-for-ericsson-huawei-and-nokia) — 2026，OFDM vs 新空口分歧
16. [6G-AI.com: 3GPP 6G Standardization Roadmap](https://6g-ai.com/news/3gpp-6g-standardization-roadmap-release-21) — Rel-22/23 增强阶段定位

### 学术
17. [arXiv 2407.09398: 6G The Intelligent Network of Everything](https://arxiv.org/pdf/2407.09398) — 2024.07，Rel-22 补充 ITU 提交假设分析
