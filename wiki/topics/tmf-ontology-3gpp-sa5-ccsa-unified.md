---
title: TMF 本体 × GB1093/1094/TR328/329 × 华为 CCSA 本体 × 3GPP SA5 统一分析
title_en: Unified Analysis of TMF Ontology, GB1093/1094, TR328/329, Huawei-CCSA Specs and 3GPP SA5
slug: tmf-ontology-3gpp-sa5-ccsa-unified
category: topic
status: reviewed
confidence: medium
sources:
  - title: TR292 TM Forum Intent Ontology (TIO) v3.6.0
    url: https://www.tmforum.org/resources/introductory-guide/tr292-tm-forum-intent-ontology-tio-v3-6-0/
    type: standard
    date: 2024-08-30
    archived: research/raw/2026-09-20-tmf-intent-common-model/
  - title: GB922 Information Framework Models Suite v25.0
    url: https://www.tmforum.org/resources/model/gb922-information-framework-models-suite-v25-0/
    type: standard
    date: 2025-07-18
    archived: research/raw/2026-09-20-tmf-gb922-sid/
  - title: 3GPP TS 28.312 V19.5.0
    url: https://etsi.org/deliver/etsi_ts/128300_128399/128312/19.05.00_60/ts_128312v190500p.pdf
    type: standard
    date: 2026-04-01
    archived: research/raw/2026-09-20-3gpp-ts28312-intent/
  - title: 3GPP 32.801-01 Study on 6G Management and Orchestration
    url: https://portal.3gpp.org/desktopmodules/Specifications/SpecificationDetails.aspx?specificationId=5491
    type: standard
    date: 2026-01-12
    archived: research/raw/2026-09-20-3gpp-sa5-6g-oam-study/
  - title: YD/T 7007-2026 知识建模方法
    url: https://std.samr.gov.cn/hb/search/stdHBDetailed?id=5679B6F617894858E06397BE0A0AD0B8
    type: standard
    date: 2026-06-01
    archived: research/raw/2026-09-20-ccsa-huawei-ontology-spec/
  - title: ITU-T M.3351 (08/2024)
    url: https://www.itu.int/epublications/publication/itu-t-m-3351-2024-08-framework-of-knowledge-management-for-telecom-operation-and-management
    type: standard
    date: 2024-08-13
    archived: research/raw/2026-09-20-itu-t-m3351/
  - title: TM Forum Community on ontology tiger team (GB1093/TR328/TR329)
    url: https://engage.tmforum.org/discussion/a-practical-hypothesis-operational-centricity-as-a-complementary-decision-context-dimension-for-an-transformation
    type: media
    date: 2026-09-01
    archived: research/raw/2026-09-20-tmf-gb1093/
related:
  - telecom-network-ontology
  - ontology
  - sid
  - intent-common-model
  - dmfw
  - nrm
  - ccsa
  - knowledge-graph-for-data
  - data-fabric-for-ai-native-6g
  - cross-domain-data-governance-6g
  - 3gpp-sa2-6g-data-framework-wt5
  - 3gpp-rel-19-20-data-architecture-status
tags:
  - ontology
  - TM-Forum
  - 3GPP-SA5
  - CCSA
  - TIO
  - SID
  - DMFW
  - knowledge-graph
  - 6G
last_verified: 2026-09-20
owner: agent
---

# TMF 本体 × GB1093/1094/TR328/329 × 华为 CCSA 本体 × 3GPP SA5 统一分析

## 核心结论（执行摘要，≤ 150 字）

TMF 已 GA 的本体是意图 RDF 模型 TIO（TR292 v3.6.0，2024-08 批准）及公开的 ICM TR290A/B v3.6.0 [高]；GB1093/TR328/TR329 是 Ontology tiger team 的标题级证据（TMF Chief Architect 回帖，单一来源），公开无 PDF，GB1094 未能核实 [低]。3GPP SA5 用 UML 意图模型（TS 28.312）与 TIO 做 informative 三元素映射；6G 研究 **TR 32.801-01 文档 rapporteur 为中兴，WI FS_6G_OAM rapporteur 为 AT&T**，并已在工作区草案中计划调研 TMF 本体 [高]。所谓「华为 CCSA 本体规范」对应的是 2026-06 发布的 YD/T 知识图谱系列（华为/中兴均为起草单位），不是华为单独立项 [高]。三套体系尚未互认，数据编织语义层应分层对接而非等待单一全球本体。

## 1. 现状定义

### 信息模型 vs 本体

| 维度 | 信息模型 | 本体 |
|---|---|---|
| 典型载体 | UML 类/属性（SID、NRM） | RDF/RDFS/OWL + SHACL |
| 世界假设 | 封闭世界、面向接口实现 | 开放世界、面向共享语义与推理 |
| TMF 实例 | GB922 SID v25.0（2025-07） | TIO TR292；计划中的 GB1093 联邦本体 |
| 3GPP SA5 实例 | NRM、TS 28.312 Intent IOC | 尚无；TR 32.801-01 KI「Knowledge/semantic representation」 |
| CCSA 实例 | 传统网管模型 | YD/T 7007 本体模型层（目录已确认） |

### 用户点名四文档分类

| 编号 | 正式标题（已核实部分） | 分类 | 核实 |
|---|---|---|---|
| GB1093 | The Federated TM Forum Ontology (MODA-440) | 联邦本体（计划/Confluence） | title-only |
| GB1094 | 未能核实；排除国标 GB 1094 变压器 | — | not-found |
| GB1089 | 检索摘要称 DEM Ontology；未打开官方页 | — | unverified（不作 GB1094 替代） |
| TR328 | The Case for Ontologies: A Roadmap for TM Forum | 本体路线图 TR | title-only |
| TR329 | Ontology Programme Governance: Requirements and Feasibility (MOD-441) | 本体计划治理 TR（帖文称 draft；MODA 归属为推断） | title-only |
| GB922 | Information Framework Models Suite v25.0 | UML 信息模型 | confirmed |
| TR292/TR290 | TIO / ICM | RDF 意图本体 | confirmed |
| TS 28.312 | Intent driven MnS | UML 意图信息模型 | confirmed |
| TR 32.801-01 | Study on 6G M&O | 6G 研究 TR（含 DMFW 与知识 KI） | confirmed |
| 32.801 / 32.801-02 | 旧「Performance management」已 WITHDRAWN；02 为 6G 计费研究 | 编号易混 | confirmed（排除） |
| YD/T 7007 等 | 知识图谱技术要求 | 知识建模/融合/构建行标 | confirmed（目录） |

Fable 先验「GB1093/1094 可能是 AN 成对框架」部分有误：成对出现的是 **GB1093 + TR328 + TR329**，不是 GB1093/GB1094。

## 2. 标准与组织动态（近 3 年）

- 2022-08：IG1253 Intent in Autonomous Networks v1.3.0 公开 [高]
- 2023-04：TR294A 发布，专门连接 TIO 扩展模型与 TS 28.312 [高]
- 2024-07/08：TR292 TIO v3.6.0 Team Approved / TMF Approved，公开可下载 [高]
- 2024-08：ITU-T M.3351 知识管理框架，ontology modelling + RDF/OWL [高]
- 2025-07：GB922 Models Suite v25.0（SID + MODA UML）[高]
- 2025-10：ITU-T M.3351.2 知识图谱九步构建过程 [高]
- 2025-12：FS_6G_OAM 启动；2026-01-12 创建规范 32.801-01（类型 TR）[高]
- 2026-05：SA5 Inbox 出现 KSM1/2/3（知识管理/场景/架构）草稿文件名 [中]
- 2026-06：YD/T 7007/7011/7023/7024 发布，2026-09-01 实施 [高]
- 2026-07：TMF Inform《Building knowledge planes…》将 knowledge plane 作为 L4 前提 [中]
- 2026-09（约）：Community 回帖列出 GB1093/TR328/TR329；hub 随后关闭 [低]
- 2026-07：YD/T 7129 5G 无线故障知识建模发布 [高]

## 3. 关键玩家

| 玩家 | 定位 | 差异化 | 来源 |
|---|---|---|---|
| TM Forum AN / MODA | TIO 已 GA；联邦本体仍在 Confluence | RDF 意图词汇 + 计划中的 Semantic Knowledge Fabric | TR292；Community 帖 |
| 3GPP SA5 | 管理意图 UML + 6G DMFW/知识研究 | 与 TMF 有 Annex C 浅映射；无 OWL | TS 28.312；Portal 32.801-01 |
| 3GPP SA2 | 网络数据框架 WT#5 | 与 SA5 DMFW 职责交叉，见矛盾 11/31 | 既有 topic |
| CCSA TC7/TC610 | 国内知识图谱行标 | 2026 已发布，目录首位为运营商/高校、厂商起草 | SAMR |
| 华为 | ADN 知识库 + 行标起草 + IETF RDF 示例 | 定义权在宣传侧强，行标非独家 | ADN 白皮书；YD/T 目录 |
| 中兴 | TR 32.801-01 **文档** rapporteur；WI 由 AT&T 牵头；YD/T 起草；数据中枢本体实践 | 6G OAM 研究笔杆（非 WI 主导）+ 国内行标席位 | Portal；内部方案 |
| Ericsson Research | tio-shacl 开源校验 | 证明 TIO 可 SHACL 化 | arXiv:2604.27359 [中] |

## 4. 技术机制

### 4.1 TMF：TIO 已落地，联邦本体在路上

TIO 分层：TR292 提供意图管理词汇；TR290 规定意图表达式与报告；TR291 扩展；TR292A–I 覆盖管理元素、状态机、函数、量、逻辑/集合算子、度量、安全。编码为 RDF Turtle（学术统计 15 模块）。TR294A 把无线网/无线业务意图 artifacts 接到 3GPP TS 28.312。注意版本漂移：TR290 v3.8.0、TR292I v4.0.0（2026-03-27）及 TR292B/H v3.7.0（2025-11）已超出 28.312 引用的 v3.6.0，映射维护有对齐风险。

GB1093/TR328/TR329/TR326 构成第二条线：为 AI Native AN 建立联邦 Semantic Knowledge Fabric 与治理。公开材料只到标题与一句「知识编织需要形式化本体」。

### 4.2 3GPP SA5：UML 意图 + 研究中的知识表示

TS 28.312：Intent → IntentExpectation（DELIVER/ENSURE/MAINTAIN）→ Object/Target/Context；OpenAPI YAML。Annex C 只映射三对元素到 ICM。Annex F.3 规定 CSC–CSP 用 TMF API、其下用 3GPP MnS，需要转换功能。

TR 32.801-01 TOC 将 DMFW 与 Data and Knowledge Management 并列，KI 明确写 Knowledge/semantic representation。文档 rapporteur 为中兴，WI rapporteur 为 AT&T。这是 3GPP 首次在 6G OAM 研究结构里给「语义」单列位置，但解决方案未公开。

Rel-20 工作区讨论稿 §2.2.4 Semantic Network Management 进一步列出 WT-4：*Survey existing related frameworks (e.g. RDF) and solutions (e.g. knowledge graphs, ontologies) defined in other fora (e.g. TM Forum)*。Ericsson 建议改名为 Knowledge Management；中兴反馈支持该工作区且 WT 1/2/4 OK。因此与 TMF 本体的桥梁不只 Annex C，6G 研究已计划调研可否借用，尚未成规范。

### 4.3 CCSA/华为：知识图谱行标中的本体层

YD/T 7007 目录确立知识建模准则与表示方法；二手解读描述本体/实例双层与 RDF。与 ITU-T M.3351 的 ontology modelling 步骤同构 [推断，同源性未在行标文本中声明]。华为 ADN 白皮书把知识图谱用于故障传播关系，不等于发布了可下载的领域 OWL。

### 4.4 统一映射（摘要，完整矩阵见 analysis/matrices/ontology-standards-mapping.md）

意图层：TMF TIO ↔ 3GPP 28.312 已有 informative 桥；SA5 §2.2.4 WT-4 计划调研 TMF 本体/RDF/KG 能否借用（研究级，非规范）。CCSA 7007 把「意图」列为七类建模对象之一，未见与 TIO 的 IRI 对齐。

知识/运营层：ITU-T M.3351 与 YD/T 系列同构；TMF TR326/GB1093 目标类似但会员墙；3GPP 刚立项 KI。

资源层：SID 与 NRM 仍是 UML，与 OWL 联邦本体如何对齐是 GB1093 必须回答、目前未公开回答的问题。

## 5. 趋势驱动力

- 业务：AN L4 要求 AI agent 理解跨域知识，而不只是调用 API（TMF Inform 2026-07）
- 技术：RDF 意图模型与 UML 管理模型并存，需要转换器与 SHACL 校验（tio-shacl）
- 政策：国内 2026 行标已实施，国际 TMF 联邦本体与 3GPP 知识 KI 窗口重叠在 2026–2027

## 6. 批评与风险

- 局限性：TIO 不覆盖 RAN/Core 资源语义与数据面四类数据；SID 未本体化；28.312 映射过粗
- 会员墙：GB1093/TR328/TR329/TR326 无法做条款级审计
- 商业风险：华为在 ADN/CCSA 叙事上占位；若 GB1093 由 MODA 少数公司定元模型，后来者只能做扩展
- 失败模式：三套「本体」并列导致 Agent 幻觉与集成成本——这正是数据编织语义层要消解的问题

## 7. 对我司的相关性

依据 `ops/company-context.md`：数据中台/战略专家组，千万级/年，仅建议权。

**D（可直接执行）**

1. 把数据中枢已有「统一语义层→本体建模」与 YD/T 7007 术语对齐，输出一页对照表（实体：网元/小区/告警），服务故障 Agent，不新建产品线
2. 以 **TR 32.801-01 文档 rapporteur**（WI 由 AT&T 牵头）跟踪并准备「知识/语义表示」KI 与 §2.2.4 WT-4 的公司贡献提纲（知识架构 vs DMFW 边界），对接 SA5 而非重复 SA2 WT#5
3. 预研公开 TIO（TR292 + TR290A/B v3.6.0）与内部本体图的最小映射：意图对象 ↔ 网元/切片/告警，形成内部白皮书

**R（需上升公司决策）**

1. 是否申请 TMF MODA/Ontology tiger team 正式席位以影响 GB1093
2. 是否将「网络语义层」列为 AN 数智引擎的标准组件（超出现有故障域 KG）

不建议：自建全球电信 OWL 底座、并购语义厂商、宣称「中兴定义 6G 本体」。

## 矛盾与待核实

- 信息模型 vs 本体路线（矛盾 34）
- TIO RDF vs 28.312 UML 映射过浅（矛盾 35）
- 「华为 CCSA 本体」独家叙事 vs 多单位起草事实（矛盾 36）
- 仓库「TS 32.801 / DMFW=TS 28.104」编号误差（见 gaps；关联矛盾 11/31 但不重复其 SA2/SA5 职责争论）

## 数据缺口

见 `analysis/gaps.md` 新增节。P0：GB1093/TR328/TR329 正文；YD/T 7007 OWL 条款；SA5 知识架构 pCR 正文。

## 来源

### 一手资料 / 官方 ★
1. [TR292 TIO v3.6.0](https://www.tmforum.org/resources/introductory-guide/tr292-tm-forum-intent-ontology-tio-v3-6-0/)
2. [GB922 v25.0](https://www.tmforum.org/resources/model/gb922-information-framework-models-suite-v25-0/)
3. [TS 28.312 V19.5.0](https://etsi.org/deliver/etsi_ts/128300_128399/128312/19.05.00_60/ts_128312v190500p.pdf)
4. [Portal 32.801-01](https://portal.3gpp.org/desktopmodules/Specifications/SpecificationDetails.aspx?specificationId=5491)
5. [YD/T 7007 目录](https://std.samr.gov.cn/hb/search/stdHBDetailed?id=5679B6F617894858E06397BE0A0AD0B8)
6. [ITU-T M.3351](https://www.itu.int/epublications/publication/itu-t-m-3351-2024-08-framework-of-knowledge-management-for-telecom-operation-and-management)
7. [FS_6G_OAM WI 1100014](https://portal.3gpp.org/desktopmodules/WorkItem/WorkItemDetails.aspx?workitemId=1100014)

### 学术 📄
8. [TIO-SHACL arXiv:2604.27359](https://arxiv.org/pdf/2604.27359)

### 厂商白皮书 🏢
9. [华为 ADN 白皮书](https://carrier.huawei.com/~/media/cnbgv2/download/adn/autonomous-driving-network-overview-cn.pdf)
10. [中兴自智网络白皮书 2022](https://www.zte.com.cn/content/dam/zte-site/res-www-zte-com-cn/mediares/zte/files/pdf/white_book/20220517.pdf)

### 分析机构 / 媒体
11. [TMF Inform knowledge planes](https://inform.tmforum.org/research-and-analysis/reports/building-knowledge-planes-to-scale-autonomous-networks)
12. [TMF Community ontology tiger team 引用](https://engage.tmforum.org/discussion/a-practical-hypothesis-operational-centricity-as-a-complementary-decision-context-dimension-for-an-transformation)
