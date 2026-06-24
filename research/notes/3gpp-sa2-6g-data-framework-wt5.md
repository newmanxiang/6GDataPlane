# 精读笔记：3GPP SA2 6G Data Framework WT#5

> 子题：3gpp-sa2-6g-data-framework-wt5
> 调研日期：2026-06-25
> 状态：完成

## [TR 23.801-01 Table of Contents]（一手资料，2025-09 至今）
URL: https://itecspec.com/3gpp/23.801-01

### 关键数据点
- TR 23.801-01 共定义 24 个 Key Issues（KI#1 至 KI#24）
- KI#21 明确标题为 "6G data framework in SA2"
- Section 6.21 收录 KI#21 的方案提案（Solutions to KI#21）
- Annex A.5 定义 Work Task 5 范围
- Annex C.21 列出所有提交的方案清单

### 关键论断
- WT#5 是 FS_6G_ARC 8 个 WT 中唯一聚焦数据处理的工作任务
- KI#21 与 KI#18/19（AI）、KI#20（ISAC）、KI#22（Computing）存在数据依赖关系

---

## [Samsung Research: AI in 6G Network SA Aspect]（厂商博客，2026-05）
URL: https://research.samsung.com/blog/AI-in-6G-network-Service-and-System-Aspect

### 关键数据点
- 引用 3GPP TR 23.801-01 V0.3.0（2025-11）和 SP-250806
- 明确 6G Data Framework 将覆盖 SA2/RAN1/RAN2/SA5 多域

### 关键论断
- "5G UP 基础设计以 UE→DN 用户数据透明传输为目的，数据负载对核心网不可见——这是跨域 AI 数据传输的根本障碍"
- "Data framework aims to provide flexible data or related information collection and transfer across different domains"
- "This approach will play a crucial role in enabling AI services in 6G networks"

### 新发现的术语
- "AI-enabled NFs"：6G 中每个 NF 均可内嵌 AI 能力
- "AI Agent communication"：6G 核心网支持 AI Agent 注册/发现/通信

---

## [Ericsson: 6G Standardization Technical Studies Starting]（厂商博客，2025-06）
URL: https://www.ericsson.com/en/blog/2025/6/blog-6g-standardization-technology-step-to-publish

### 关键论断
- "6G is envisioned to support a data architecture for many different data types from the RAN and core networks"
- "That data architecture should be agnostic to data use cases and support the principle of collecting data once for multiple uses"
- 明确将"efficient data handling"列为 6G 系统架构研究的核心议题之一

### 与其他来源的矛盾
- Ericsson 主张"用例无关"原则，与华为 DaaS（面向 AI/感知用例优化）存在设计哲学差异 → 已记录为矛盾 33

---

## [IETF DMM WG: 6G Workshop Summary]（标准/2025-03）
URL: https://datatracker.ietf.org/meeting/122/materials/slides-122-dmm-6g-workshop-summary-00

### 关键数据点
- 3GPP 6G Workshop（2025.03.10-11）明确提出"Unified Data Management Framework for 6G"
- 框架覆盖：cross domain data discovery, collection, storage, transmission, correlation, exposure
- 5G 数据收集方法已达 5 种（MDT/LPP/NWDAF/DCAF/UE-level），复杂性是 6G 统一框架的驱动力

### 关键论断
- "Complexity in 5G Data Collection" 被正式列为 6G 架构改进的核心动机
- SA2 6G SI 完成目标确认为 "Dec 2026 or Mar 2027"

---

## [SA2#174 FTP General Folder]（一手资料，2026-04）
URL: https://www.3gpp.org/ftp/tsg_sa/WG2_Arch/TSGS2_174_Malta_2026-04/INBOX/DRAFTS/FS_6G_ARC/General

### 关键数据点
- Penholder assigned list for solution phase_r5.docx 创建于 2026-03-31（20 KB）
- S2-2603384_FS_6G_ARC_SA2_174_Status_v02.pptx（520 KB）为进度报告
- FS_6G_ARC_SA2_174_per_KI_Status_v2.pptx 为逐 KI 进度状态
- S2-26xxxxx_SA2#174_Company_contribution_r1.pptx 为公司贡献统计

### 待追查
- Penholder 列表正文——确认 WT#5/KI#21 由哪家公司担任 Penholder
- Per_KI_Status 中 KI#21 的具体进度百分比

---

## [Nokia 6G White Paper]（厂商白皮书，2025-03）
URL: https://www.nokia.com/asset/i/212403/

### 关键论断
- "A dedicated data and information architecture is envisioned for 6G to collect, store and expose this data across the domains"
- "Different to the subscription-notify approach currently specified for the core network, a publication-subscription pattern or event stream approach might be better suited"
- "The NWDAF also comes with the capability to (re-)train the AI/ML model(s) it is employing, where again, it needs to collect a large amount of training data from various data sources"

### 新发现的术语
- "data and information architecture"：Nokia 对 6G 数据层的命名
- "publication-subscription pattern"：Nokia 明确支持 Pub/Sub 用于数据层

---

## [6G Futures: SA#111 Outcomes]（分析，2026-04）
URL: https://6gfutures.substack.com/p/outcomes-from-the-3gpp-sa-meeting

### 关键数据点
- SA#111 批准首个 Rel-21 WI（6G-REQ，TS 22.270）
- SA WG1 Stage-1 freeze 目标 2027.03
- SA WG2 需在 SA#112（2026.06）报告 FS_6G_ARC 进度与风险

### 关键论断
- "Two-sided model checkpoint. Down-selection between SA WG2 and SA WG5 options for dataset and model parameter exchange is due" — 确认 SA2/SA5 需要下选
- SA2 ad-hoc e-meeting（2026.06.24-30）是 2026 Q2 的关键里程碑

---

## [DOCOMO Euro-Labs: GSMA 6G Webinar]（厂商，2026-02）
URL: https://docomolab-euro.com/en/gsma-6g-community-from-research-to-standards-shaping-future-networks/

### 关键数据点
- Dr. Malla Reddy Sama（DOCOMO Euro-Labs）确认为 3GPP SA2 6G Study Item Rapporteur
- 参与者包括 Dr. Tao Sun（China Mobile/SA 副主席）和 Dr. Wen Tong（Huawei CTO Wireless）

### 关键论断
- "shaping industry-wide consensus on the expected architecture and capabilities of future 6G mobile networks"
- Rapporteur 角色由 DOCOMO 担任，意味着日本运营商在中立协调中有话语权
