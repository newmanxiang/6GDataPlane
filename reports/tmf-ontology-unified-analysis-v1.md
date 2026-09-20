# TMF 本体论统一分析：GB1093/1094、TR328/329、华为 CCSA 本体规范与 3GPP SA5

> 版本：v1 · 日期：2026-09-20 · 子题 slug：`tmf-ontology-3gpp-sa5-ccsa-unified`  
> 知识中台：[wiki/topics/tmf-ontology-3gpp-sa5-ccsa-unified.md](../wiki/topics/tmf-ontology-3gpp-sa5-ccsa-unified.md)  
> 映射矩阵：[analysis/matrices/ontology-standards-mapping.md](../analysis/matrices/ontology-standards-mapping.md)  
> 原料：`research/raw/2026-09-20-*` 与 [research/notes/tmf-ontology-3gpp-sa5-ccsa-unified.md](../research/notes/tmf-ontology-3gpp-sa5-ccsa-unified.md)

本文供洞察报告引用，不替代 `deep-insight-report-vN.md`。所有规范编号均经公开目录核实；会员墙文档只引用标题、摘要与版本历史。

## 1. 执行摘要

TM Forum 真正已经 GA、且公开可下载的「本体」是 **Intent Ontology（TIO，TR292 v3.6.0，2024-08-30 批准）**，用 RDF 为自智网络意图管理提供词汇；SID（GB922 v25.0，2025-07）仍是 UML 信息模型，不是 OWL 本体。[高]

用户点名的 **GB1093 / TR328 / TR329** 在 TM Forum Community 讨论中作为 Ontology tiger team 文档被列出，标题分别为联邦 TMF 本体（MODA-440）、本体路线图、本体计划治理（MOD-441）；公开 resources 目录无 PDF。**GB1094 未能核实**（须排除中国国标 GB 1094 电力变压器）。[中]/[低]

3GPP SA5 在意图层用 **TS 28.312** UML 模型，Annex C 对 TMF ICM 做 **informative 三元素映射**，并引用 TR290A/B v3.6.0；6G 管理研究规范官方编号为 **TR 32.801-01**（不是 TS 32.801），含 DMFW 与「Knowledge/semantic representation」KI，**rapporteur 为中兴**。[高]

所谓「华为 CCSA 本体规范」在公开目录中对应 **YD/T 7007 等 2026 年知识图谱系列**（知识建模含本体模型）。牵头单位是北邮/运营商，**华为与中兴同为起草方**，不存在华为独家 CCSA 本体标准。[高]

对 6G 数据面 × 数据编织：语义层应 **分层对接**——意图契约用 TIO↔28.312，运营知识用 YD/T + ITU-T M.3351，管理对象继续 NRM/SID，数据生命周期看 SA5 DMFW 与 SA2 WT#5（职责交叉见既有矛盾 11/31）。等待「一个全球电信本体」会错过 2026–2027 窗口。

## 2. 文档识别与核实清单

编号体系：TMF 的 `GB` = Guide Book，与中国国标 `GB/T` 无关；3GPP 研究产出是 `TR 28.xxx` / `TR 32.xxx`，「TR 328」不是 3GPP 编号；CCSA 行标为 `YD/T`。

| 编号 | 正式标题 | 版本·日期 | 组织·项目 | 公开性 | 核实 | 归档 |
|---|---|---|---|---|---|---|
| GB1093 | The Federated TM Forum Ontology (MODA-440) | 未知 | TMF MODA | 会员 Confluence | title-only | `research/raw/2026-09-20-tmf-gb1093/` |
| GB1094 | （无） | — | — | — | **not-found** | `…-tmf-gb1094/` |
| TR328 | The Case for Ontologies: A Roadmap for TM Forum | 未知 | TMF Ontology tiger team | 会员 | title-only | `…-tmf-tr328/` |
| TR329 | Ontology Programme Governance: Requirements and Feasibility (MOD-441) | 未知 | TMF MODA | 会员 | title-only | `…-tmf-tr329/` |
| GB922 | Information Framework Models Suite | v25.0 · 2025-07-18 | TMF ISA | 会员（目录公开） | confirmed | `…-tmf-gb922-sid/` |
| TR292 | TM Forum Intent Ontology (TIO) | v3.6.0 · 2024-08-30 Approved | TMF AN | 公开可下载 | confirmed | `…-tmf-intent-common-model/` |
| TR290A/B | Intent Common Model Expression / Reporting | v3.6.0（被 28.312 引用） | TMF AN | 会员 | confirmed（经 28.312） | 同上 |
| TR294A | Model Connection to 3GPP TS 28.312 | v1.0.0 · 2023-04-11 | TMF AN | 目录公开 | confirmed | `…-tmf-tr326-tr292-tr294/` |
| TR326 | Operationalizing Ontologies for AI-Native AN（Community 引 Confluence） | v2 Suite（标题） | TMF Components/Canvas | 会员 | title-only | 同上 |
| TS 28.312 | Intent driven management services | V19.5.0 Rel-19 | 3GPP SA5 | 公开（ETSI） | confirmed | `…-3gpp-ts28312-intent/` |
| 32.801-01 | Study on 6G Management and Orchestration | Draft Rel-20 · 建档 2026-01-12 | 3GPP SA5 / FS_6G_OAM | 元数据公开 | confirmed | `…-3gpp-sa5-6g-oam-study/` |
| TS 28.104 | Management Data Analytics | Rel-18/19 | 3GPP SA5 | 公开 | confirmed（**不是 DMFW**） | `…-3gpp-sa5-nrm-model-repertoire/` |
| YD/T 7007 | 网络运营管理知识图谱 知识建模方法 | 2026-06-01 / 实施 09-01 | CCSA | 目录公开、正文付费 | confirmed | `…-ccsa-huawei-ontology-spec/` |
| YD/T 7011 | 总体框架 | 同上 | CCSA（移动牵头） | 同上 | confirmed | 同上 |
| YD/T 7023 | 知识融合方法 | 同上 | CCSA（电信牵头） | 同上 | confirmed | 同上 |
| YD/T 7024 | 知识图谱构建 | 同上 | CCSA（北邮牵头） | 同上 | confirmed | 同上 |
| YD/T 7129 | 5G 无线故障管理知识建模 | 2026-07-15 / 实施 11-01 | CCSA（联通牵头） | 同上 | confirmed | 同上 |
| M.3351 | Knowledge management framework | 2024-08-13 | ITU-T SG2 | 公开 | confirmed | `…-itu-t-m3351/` |

**Fable 先验校正**：GB1093/1094 并非已核实的「AN 成对指南」；公开并列的是 TR328 + TR329 + GB1093。仓库既有「TS 32.801」「DMFW = TS 28.104」不准确：官方类型为 **TR 32.801-01**，TS 28.104 为 MDA。

## 3. TM Forum 本体体系

### 3.1 SID 不是本体

GB922 v25.0 提供 SID Excel 与 MODA UML 2.5.1/XMI。它解决 CSP 业务对象一致性（产品、客户、服务等 ABE），世界假设是封闭的实现模型。把 SID 口头称为「电信本体」会造成与 TIO/GB1093 的范畴混淆。

### 3.2 已落地：意图本体 TIO

TR292 公开摘要：意图管理功能实例构成意图控制环与生命周期，本模型为意图通用模型与扩展模型提供基础词汇。Toolkit 列出 TR292A–I、TR290、TR291、TR299、TMF921、IG1253、IG1358。Ericsson tio-shacl（arXiv:2604.27359）称 TIO v3.6.0 有 15 个规范性 RDF Turtle 模块。[中] 此统计非 TMF 官方，但与「RDF 本体」定性一致。

### 3.3 在路上：联邦本体与知识编织

Community 讨论把 TR328（为什么需要本体）、TR329（计划治理与可行性）、GB1093（联邦本体本身）与 TR326（如何运营化本体、联邦 Semantic Knowledge Fabric、知识平面与 AI/治理之间的 semantic contract）连在一起。TMF Inform（2026-07-01）从分析侧呼应：L4 必须从管数据转向管知识。

**已核实 vs 推断**：已核实的是标题、项目号（MODA-440/441）及 TIO 正文级公开信息。推断（[低]）是 GB1093 将吸收 SID 概念并 OWL 化——**未见官方语句**。

## 4. 3GPP SA5 语义载体

### 4.1 已规范：NRM 与意图 MnS

SA5 的系统之源是 NRM（TS 28.622/28.541）与模型规范（TS 32.156/32.160）。意图服务 TS 28.312 定义 Intent / IntentExpectation（动词 DELIVER、ENSURE、MAINTAIN）及场景专用期望（无线网、无线业务、5GC、维护等），编码 YAML/OpenAPI。

Annex C 映射：

| 3GPP | TMF ICM（TR290A） |
|---|---|
| expectationObject | icm:target |
| expectationTargets | icm:Expectation 实例属性 |
| expectationContexts | icm:context |

报告侧映射到 icm:ExpectationReport。Annex F.3：CSC–CSP 可用 TMF Intent API，CSP–NOP / NOP–NEP 用 3GPP MnS，中间做转换。这是 **跨 SDO 正式引用**，不是同一模型。

### 4.2 研究中：DMFW 与知识/语义

FS_6G_OAM（WI 1100014）2025-12 启动、目标 2027-06。规范 32.801-01 类型 TR，rapporteur Pengxiang Xie（ZTE）。公开 TOC：6.1.6/7.1 DMFW；**7.2.1 Knowledge/semantic representation and management**。SA5 Inbox 文件名出现 KSM1/2/3。正文解决方案未公开，不得虚构架构图。

DMFW 能力清单来自 Rel-20 工作区讨论稿：收集控制与上报、处理、分析、注册、发现、访问控制、发布、分发、暴露、编目、销毁、质量、变更，并讨论非 3GPP（O-RAN）数据与用户同意。这与 SA2 WT#5 交叉，分析见既有矛盾 11/31，本文不重复裁决。

## 5. 华为与 CCSA 本体相关规范

公开检索 **没有**「华为 CCSA 本体规范」这一单独标准号。可核实的对应物：

1. **YD/T 网络运营管理知识图谱系列（2026-06 发布）**，华为为主要起草单位之一。YD/T 7007 适用范围明确「知识模型组成及表示方法」；二手解读描述本体/实例双层与 RDF/OWL，**正文条款未读**。
2. **华为 ADN 白皮书**：知识图谱用于专家知识与故障传播，网络知识库与数据湖并列。属产品架构叙述，🏢。
3. **Huawei-IOAM IETF 示例仓**：IRI `http://www.huawei.com/ontology/ietf-network/`，RFC8345 拓扑 RDF，toy example，非行标。

同源性判断：与 ITU-T M.3351（ontology modelling + RDF/OWL + 融合/推理）**方向同构**，与 TMF TIO **对象不同**（运营知识 vs 意图）。未见 YD/T 声明等同采用 TMF GB1093。中兴同样出现在 7007/7011/7023/7129 起草名单。

## 6. 统一映射与差距

完整 8×4 矩阵见 M5。差距一句话：

- **意图**：有浅桥（TIO↔28.312），无一致性测试套件。
- **运营知识**：国内行标 + ITU-T 框架已在；TMF 联邦本体与 3GPP 知识 KI 落后一个发布周期。
- **资源对象**：SID/NRM 仍 UML，与 OWL 联邦本体的官方映射缺失。
- **数据面四类数据**（通信/感知/AI/管理）：上述本体/行标均未覆盖用户面/感知数据语义；那是 SA2 WT#5 与数据编织议题，见既有卡片。
- **Data Fabric 接口**：唯一在标准里写 Fabric 的仍是 ETSI ZSM GS 029；TMF 用 Knowledge Fabric 近义但无对等条款。

## 7. 与 6G 数据面 × 数据编织的关系

数据编织需要主动元数据与知识图谱做跨域语义。电信现场已有三套语义资产：BSS/OSS 的 SID、网管 NRM、AN 意图 TIO，再加上国内运营 KG。6G 若再叠加 SA2 数据框架与 SA5 DMFW 而不做映射，语义层会比 5G 更碎。

可执行架构（推断，标 [中]，供内部讨论而非标准原文）：

1. **契约层**：意图用 TIO/TMF921 与 28.312 转换（已有 Annex C/F.3）。
2. **知识层**：故障/质差/规则用 YD/T 7007 类本体 + M.3351 过程；对齐数据中枢已有本体图。
3. **对象层**：网元/切片继续 NRM；不把 OWL 实例直接当配置接口。
4. **数据层**：DMFW/WT#5 管生命周期与访问控制；编织引擎消费本体做发现与策略，而不是取代 3GPP 接口。

与既有矛盾 11/31 的关系：本文增加的是「知识/语义表示」这一新 KI，可能成为 SA5 侧与 SA2 数据框架的又一重叠带，需在 rapporteur 贡献中主动画界。

## 8. 对中兴的启示（D/R）

尺度：千万级/年、建议权、不碰合同与组织细节。

| 编号 | 类型 | 行动 | 窗口 |
|---|---|---|---|
| D1 | 直接 | 内部语义层术语对齐 YD/T 7007（网元/小区/告警/关系） | 6 个月 |
| D2 | 直接 | 基于公开 TR292 + 28.312 Annex C 做意图对象映射说明（内部白皮书） | 6 个月 |
| D3 | 直接 | 准备 SA5「知识架构 vs DMFW」边界贡献提纲（用 rapporteur 位） | 随 2026–2027 会次 |
| R1 | 上升 | 是否正式投入 TMF MODA/Ontology 以影响 GB1093 | 公司标准资源决策 |
| R2 | 上升 | 是否把「网络语义层」从故障 KG 升为数智引擎标准组件 | 产品路标 |

不建议自建全球电信 OWL 底座或用宣传口径「定义 6G 本体」。华为风险在叙事与 TC610 测评密度，不在独占 YD/T 著作权。

## 9. 矛盾、缺口与未核实项

矛盾 34–36 见 `analysis/contradictions.md`。P0 缺口：GB1093/TR328/TR329 正文、GB1094 存在性、YD/T 7007 OWL 条款、SA5 知识架构 pCR。完整表见 `analysis/gaps.md`「TMF 本体统一分析新增缺口」。

## 10. 来源

### 官方 ★
1. TR292 TIO v3.6.0 — https://www.tmforum.org/resources/introductory-guide/tr292-tm-forum-intent-ontology-tio-v3-6-0/ — 2024-08-30
2. GB922 Models Suite v25.0 — https://www.tmforum.org/resources/model/gb922-information-framework-models-suite-v25-0/ — 2025-07-18
3. Intent Toolkit — https://www.tmforum.org/toolkits/intent/
4. TR294A — https://www.tmforum.org/resources/technical-report/tr294a-model-connection-to-3gpp-ts-28-312-intent-extension-model-v1-0-0/ — 2023-04-11
5. ETSI TS 128 312 V19.5.0 — https://etsi.org/deliver/etsi_ts/128300_128399/128312/19.05.00_60/ts_128312v190500p.pdf
6. 3GPP Portal 32.801-01 — https://portal.3gpp.org/desktopmodules/Specifications/SpecificationDetails.aspx?specificationId=5491 — 2026-01-12
7. WI 1100014 FS_6G_OAM — https://portal.3gpp.org/desktopmodules/WorkItem/WorkItemDetails.aspx?workitemId=1100014
8. SA5#161 6G OAM 工作区讨论稿 — 3GPP FTP PDF
9. YD/T 7007-2026 — https://std.samr.gov.cn/hb/search/stdHBDetailed?id=5679B6F617894858E06397BE0A0AD0B8 — 2026-06-01
10. YD/T 7011/7023/7024/7129 目录页 — 国家数字标准馆 / SAMR
11. ITU-T M.3351 — 2024-08-13；M.3351.2 — 2025-10
12. MODA 项目页 — https://www.tmforum.org/master-oda-moda-project/

### 学术 📄
13. TIO-SHACL — https://arxiv.org/pdf/2604.27359 — Ericsson Research

### 厂商 🏢
14. 华为 ADN 白皮书 — https://carrier.huawei.com/~/media/cnbgv2/download/adn/autonomous-driving-network-overview-cn.pdf — 2020-05
15. Huawei-IOAM IETF KG — https://github.com/Huawei-IOAM/ietf-knowledge-graphs
16. 中兴自智网络白皮书 — 2022-05
17. 仓库内部上传 `zte/智能数据中枢方案.md`（非公开标准）

### 媒体 / 社区
18. TMF Community 讨论（GB1093/TR328/TR329 标题）— https://engage.tmforum.org/discussion/a-practical-hypothesis-operational-centricity-as-a-complementary-decision-context-dimension-for-an-transformation
19. TMF Inform knowledge planes — 2026-07-01
20. 通信世界网 CCSA TC7 立项报道等
