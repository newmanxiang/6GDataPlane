# 精读笔记：3gpp-rel-19-20-data-architecture-status

> 子题：3GPP Rel-19/20 数据架构标准化现状
> 调研日期：2026-06-23
> 搜索轮次：2 轮广度（Firecrawl + Exa 并行）+ 5 篇精读

## [3GPP Release 20 Official Page]（官方，持续更新）
URL: https://www.3gpp.org/specifications-technologies/releases/release-20

### 关键数据点
- Rel-20 包含 126 个 5G-A WI + 74 个 SI（截至 2026.03）
- 13 个 6G SI 列表明确
- Stage-1 冻结 2025.06，Stage-2 80% 完成目标 2026.06，最终冻结 2026.09
- Stage-3 目标 2027.03，ASN.1/OpenAPI 冻结 2027.06
- FS_6G_ARC 由 SA2 负责，工作项 #1080057

### 关键论断
- "Rel-20 is the final '5G-Advanced only' release"
- 6G 需要两个 Release：Rel-20 研究 + Rel-21 规范化
- ITU 目标：2029 年初提交 IMT-2030 技术提案

---

## [Samsung Research: AI in 6G Network]（厂商博客，2026-05-28）
URL: https://research.samsung.com/blog/AI-in-6G-network-Service-and-System-Aspect

### 关键数据点
- Rel-19 NWDAF 支持 23 个 Analytics ID
- 5G 数据收集走 CP，大数据量传输导致拥塞
- UP 数据对核心网"不可见"——跨域 AI 数据传输的根本障碍
- SA2 研究了 UP 数据收集方案但**决定不在 R19 规范化**

### 关键论断
- 6G 数据框架将实现"3GPP 系统内外实体间的无缝数据传输"
- 分布式 AI 使能 NF 是 6G 核心网基础使能器
- Agentic Core Network：AI Agent 自主执行任务、动态组合流程
- AI Agent 通信需要发现、认证、授权机制
- 数据框架覆盖 SA2（核心网）、RAN1/RAN2（物理层/无线层）、SA5（管理数据）

### 新发现术语
- AI-Enabled NFs：具备独立 AI 决策能力的 6G 核心网功能
- Agentic Core：基于 AI Agent 的 6G 核心网自治操作模式
- Intent-based Request：UE/AF 以意图表达需求，核心网自主解释执行

### 与其他来源的矛盾
- Samsung 强调"分布式 AI + 数据框架"而非华为的"独立数据面"概念，但两者目标一致

---

## [Ofinno: 6G Takes Shape - Standards Readout]（行业分析，2026-02-23）
URL: https://ofinno.com/standards-readout/6g-takes-shape-in-gothenburg-and-goa-first-solutions-emerge-as-3gpp-moves-past-problem-identification/

### 关键数据点
- SA2#173（2026.02 果阿）：首次从"问题识别"转向"方案探索"
- 讨论焦点：模块化 NAS 架构、分布式控制面信令
- 5G AMF 信令集中化是核心限制
- 6G 研究目标 2027.05 完成，当前约四分之一进度

### 关键论断
- "Companies moved beyond identifying architectural limitations to proposing specific solutions"
- SA2 仍处于"早期方案探索阶段"，无架构决策最终确定
- 从"首次提案"到"达成方向"窗口可能快速关闭（参考 RAN WG 经验）
- RAN2 同意对模块化 RRC 结构进行可行性研究

---

## [6G Futures: Outcomes from SA#111 Fukuoka]（分析，2026-04-26）
URL: https://6gfutures.substack.com/p/outcomes-from-the-3gpp-sa-meeting

### 关键数据点
- TR 22.870（FS_6G_REQ）100% 完成——首个完成的 6G SI
- Rel-21 WID 6G-REQ（TS 22.270）在 SA#111 获批——**首个 Rel-21 规范化工作项**
- SA1 Stage-1 冻结目标 2027.03
- SA2 6G 架构研究包含 24 个 KI
- SA2 ad-hoc e-meeting 计划：2026.06.24-30

### 关键论断
- "This is the first concrete Rel-21 deliverable in the SA domain"
- "The conversation has shifted from 'what could 6G do?' to 'what will 6G be required to do?'"
- SA2↔SA5 在数据集/模型参数交换方面存在"two-sided model checkpoint"待下选

---

## [FirstNet Authority: 3GPP Dec 2025 Recap]（官方，2026-03-19）
URL: https://firstnet.gov/newsroom/blog/3gpp-completes-release-19-while-progress-begins-6g-work

### 关键数据点
- SA2 FS_6G_ARC 完成度 20%（截至 2025.12）
- SA1 6G 研究 80% 完成，包含 200+ 用例
- SA2 考虑增加 ad-hoc 会议以保证 2027.03 完成
- FS_6G_ARC 包含"24 key aspects"

### 关键论断
- 6G 将是"AI-ready"，建立在 5G SBA 基础上演进
- Rel-20 产出仅为 TR，不产生规范性 TS
- Rel-21 提供首套 6G 规范化技术规范
- 业界期望 6G 设计"value-driven"，只引入经验证的特性

---

## [Qualcomm: 3GPP Release 20 Blog]（厂商博客，2025-06-25）
URL: https://www.qualcomm.com/news/onq/2025/06/3gpp-release-20-completing-5g-advanced-evolution-preparing-for-global-6g-standardization

### 关键数据点
- 布拉格 3GPP #108 全体会议 2025.06.09 周
- 6GR 研究范围频谱覆盖：FR1（≤7.125GHz）、FR2-1（24.25–52.6GHz）、FR3（7.125–25.25GHz）
- 6G 商用预期 ~2030

### 关键论断
- 6GR 应采用 SA 架构（standalone），简化系统设计
- 无线 AI 将"AI-native"，实现设备和网络间跨层自主 AI 操作
- 需要 AI 操作的回退机制（fallback without AI）
- 数据收集和管理是 AI 框架的核心组件

---

## [InterDigital: Paving the Path to 6G]（厂商博客，2025-06）
URL: https://www.interdigital.com/post/paving-the-path-to-6g-key-takeaways-for-3gpp-release-20

### 关键论断
- Rel-20 核心网研究将增强 5GC 以"pave the way for 6G data collection"
- AI 流量特征：上行主导、突发性、低延迟敏感
- 6G 系统架构 WG 将探索 AI/ML 和数据驱动方案支持 6G 性能
- 数据收集、计算、感知等服务可被运营商利用

---

## [GSMA 6G Community Progress Report]（行业组织，2026-05-26）
URL: https://www.gsma.com/solutions-and-impact/technologies/networks/gsma_resources/gsma-6g-community-industry-progress-report-may-2026/

### 关键数据点
- 覆盖 SA2#173（果阿，2026.02）到 SA2#174（马耳他，2026.04）
- FS_6G_ARC 现含 24 个 KI
- Rel-21 Stage 2 目标 2028.03，ASN.1/OpenAPI 冻结 2029.03
- 首个 3GPP 6G WI 在 SA#111 获批

### 关键论断
- "accelerating momentum behind Rel-21 and the transition from vision-setting into formal 6G specification work"

---

## [WirelessBrew: 6G Study Items Catalog]（技术博客，2026-03-02）
URL: https://wirelessbrew.com/6g/6G-Study-Items-Rel-20/

### 关键数据点
- SA2 TR 23.801 研究"System of Systems"概念、分布式 NAS、AI-native 控制面
- Rel-20 6G 研究截止 2027.03
- Rel-21 规范化 2027 年中启动
- Rel-21 冻结 2028 年底
- 首批 6G 商用部署 ~2030

---

## [CableLabs: 6G Study Phase]（行业组织，2026-03-10）
URL: https://www.cablelabs.com/blog/why-the-6g-study-phase-matters-now

### 关键论断
- FS_6G_ARC "目标完成日 2027.03，这是多年期工作"
- 非 3GPP 接入集成（Wi-Fi、有线）在 FS_6G_ARC 范围内
- 非 3GPP 感知集成也被纳入 SA2 研究范围
