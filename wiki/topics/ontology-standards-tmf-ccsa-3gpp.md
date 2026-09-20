---
title: TM Forum、CCSA 与 3GPP SA5 本体标准统一分析
title_en: Unified Analysis of Ontology Standards across TM Forum, CCSA and 3GPP SA5
slug: ontology-standards-tmf-ccsa-3gpp
category: topic
status: reviewed
confidence: medium
sources:
  - title: TR292 TM Forum Intent Ontology (TIO) v3.6.0
    url: https://www.tmforum.org/resources/introductory-guide/tr292-tm-forum-intent-ontology-tio-v3-6-0/
    type: standard
    date: 2024-07-04
  - title: TM Forum Intent Toolkit
    url: https://www.tmforum.org/toolkits/intent/
    type: standard
    date: 2026-03-27
  - title: TR294A Model Connection to 3GPP TS 28.312
    url: https://www.tmforum.org/resources/technical-report/tr294a-model-connection-to-3gpp-ts-28-312-intent-extension-model-v1-0-0/
    type: standard
    date: 2023-04-11
  - title: AI Native ODA Roadmap v1.0 (Andy Tiller)
    url: https://inform.tmforum.org/features-and-opinion/ai-native-oda-the-path-to-open-digital-autonomy
    type: standard
    date: 2026-06-18
  - title: Building knowledge planes to scale autonomous networks
    url: https://inform.tmforum.org/research-and-analysis/reports/building-knowledge-planes-to-scale-autonomous-networks
    type: analyst
    date: 2026-07-01
  - title: YD/T 7007-2026 知识建模方法
    url: https://std.samr.gov.cn/hb/search/stdHBDetailed?id=5679B6F617894858E06397BE0A0AD0B8
    type: standard
    date: 2026-06-01
  - title: YD/T 7019-2026 自智网络知识管理技术要求
    url: https://std.samr.gov.cn/hb/search/stdHBDetailed?id=5679B6F617964858E06397BE0A0AD0B8
    type: standard
    date: 2026-06-01
  - title: YD/T 6103-2024 IP自智网络知识面技术要求
    url: https://std.samr.gov.cn/hb/search/stdHBDetailed?id=29962E7E064FA432E06397BE0A0A0BF0
    type: standard
    date: 2024-10-24
  - title: 3GPP WI 1100014 FS_6G_OAM
    url: https://portal.3gpp.org/desktopmodules/WorkItem/WorkItemDetails.aspx?workitemId=1100014
    type: standard
    date: 2025-12-03
  - title: SA5 Rel-20 6G OAM Work Areas v0.0.7
    url: https://www.3gpp.org/ftp/Email_Discussions/SA5/OAM%20rapporteur%20calls/Rapporteur%20call%20%23161/SA5_NWM_Discussion_for_Rel-20_6G_OAM_Work_Areas-v0.0.7.pdf
    type: standard
    date: 2025-08-05
  - title: ETSI TS 128 312 V19.5.0 Annex C (2026-04)
    url: https://etsi.org/deliver/etsi_ts/128300_128399/128312/19.05.00_60/ts_128312v190500p.pdf
    type: standard
    date: 2026-04-01
  - title: TIO-SHACL arXiv 2604.27359
    url: https://arxiv.org/abs/2604.27359
    type: academic
    date: 2026-04-30
  - title: EricssonResearch/openapi-to-rdf
    url: https://github.com/EricssonResearch/openapi-to-rdf
    type: vendor
    date: 2025-11-03
  - title: Catalyst C26.0.910 Agent Fabric
    url: https://www.tmforum.org/catalysts/projects/C26.0.910
    type: vendor
    date: 2026-06-01
  - title: ITU-T M.3351 Knowledge management framework
    url: https://www.itu.int/epublications/publication/itu-t-m-3351-2024-08-framework-of-knowledge-management-for-telecom-operation-and-management
    type: standard
    date: 2024-08-01
related:
  - 3gpp-sa2-6g-data-framework-wt5
  - data-fabric-for-ai-native-6g
  - cross-domain-data-governance-6g
  - knowledge-graph
  - tm-forum
  - ontology
  - knowledge-plane
tags:
  - ontology
  - tm-forum
  - tio
  - ccsa
  - 3gpp-sa5
  - knowledge-graph
  - knowledge-plane
  - semantic-network-management
  - sid
  - moda
last_verified: 2026-09-20
owner: agent
---

# TM Forum、CCSA 与 3GPP SA5 本体标准统一分析

## 核心结论（执行摘要，≤ 150 字）

TM Forum 已 GA 的本体是 TIO（RDF，v3.6.0），SID 仍是 UML；联邦本体 GB1093 仅核实到标题。CCSA YD/T 7007 簇于 2026-09-01 实施，华为为参与起草而非牵头。3GPP 仅有 IntentExpectation↔ICM 信息性映射，RDF 在 FS_6G_OAM WT-4 仍是调研项。GB1094 未能公开核实。[高]/[中] 见正文。

## 1. 现状定义

**范围**：电信运维与自治网络语境下的**本体、信息模型、知识图谱**标准，覆盖 TM Forum（TIO / SID-MODA / 联邦本体规划）、CCSA（知识图谱与知识面行业标准）、3GPP SA5（IDMS 与 Rel-20 语义网管）。

**边界**：
- 不把 SID/NRM/YANG 直接称作本体（见 [ontology](../glossary/ontology.md)）。
- 不把知识图谱实例库等同于本体规范。
- 6G 用户面/数据面协议不在本卡；与数据框架的接口见 [3gpp-sa2-6g-data-framework-wt5](./3gpp-sa2-6g-data-framework-wt5.md) 与 [data-fabric-for-ai-native-6g](./data-fabric-for-ai-native-6g.md)。

**三层工作定义**：信息模型描述对象与属性；本体给出共享形式化词汇与公理；知识图谱存储与查询实例。TIO 已在本体层；SID 在信息模型层；YD/T 7007 同时规范本体模型与实例化模型。

## 2. 标准与组织动态（近 3 年）

- 2023-04：TR293 Connector、TR294A（TIO 连接 TS 28.312）发布。
- 2024-07/08：TIO v3.6.0 GA；ITU-T M.3351 知识管理框架。
- 2024-10 / 2025-02：YD/T 6103 发布并实施（IP 自智网络知识面）。
- 2025-06-23~26：SA5 Rel-20 6G workshop 材料上传 FTP；Samsung/Ericsson 将语义/知识管理列为优先；Ericsson 举例 RDF 作新 intent solution set。
- 2025-06-30→08-05：SA5 NWM 6G OAM 工作域讨论（含 SNM WT-1~5），v0.0.7 于 2025-08-05 锁定。
- 2025-07：SA5–ETSI ZSM 联合研讨；TR 28.881 创建。
- 2025-12：FS_6G_OAM（WI 1100014）启动，计划至 2027-06-06；SNM WT-4 调研 RDF/KG/本体（含 TM Forum）。
- 2026-03-27：TR290 v3.8.0、TR292I v4.0.0（会员）；TR 28.881 UCC。
- 2026-04-30：Ericsson tio-shacl 论文（56/69 shapes，87 类）。
- 2026-06：YD/T 7007/7011/7024/7019 发布；AI Native ODA Roadmap v1.0 将 BSS/OSS 本体列为优先事项。
- 2026-07-01：Inform 知识面报告。
- 2026-09-01：上述 CCSA 2026 标准实施。
- **GB1094**：标题与内容未能公开核实（已尝试四组 query，见笔记）。

## 3. 关键玩家

| 玩家 | 定位 | 差异化 | 来源 |
|---|---|---|---|
| TM Forum AN/MODA | 意图本体 + 规划中的联邦/SID 本体 | TIO 已 RDF；SID 仍 UML | TR292、GB922、社区帖 GB1093 |
| Ericsson | TIO 工程化（SHACL、OpenAPI→RDF） | 唯一系统校验框架；SA5 上提 RDF solution set | arXiv 2604.27359、GitHub、workshop PDF |
| Huawei | Catalyst SID OWL、Agent Fabric；CCSA 起草单位；SA5 Agent 路线 | SID→OWL 实证；非 CCSA 本体牵头 | C26.0.910、SAMR 起草列表 |
| 中国移动 | YD/T 7011/7019/6103 起草列表首位 | 国内知识管理/知识面规范入口 | SAMR/NDLS |
| 北京邮电大学 | YD/T 7007 第一起草单位 | 知识建模方法 | SAMR |
| 中兴 | CCSA 多份起草单位；TR 32.801-01 rapporteur | 数据引擎可嵌入 7007/SNM，非本体标准主导者 | SAMR、3GPP spec 页 |
| Samsung | SA5 SNM 优先倡议方 | 引用 ITU-T SG2 与 IEEE KG 框架 | workshop PDF |
| Nokia | 主张知识并入数据管理 | 与 Samsung/Ericsson 分名分域 | 讨论文稿反馈 |

## 4. 技术机制

1. **TIO 栈**：ICM（TR290）+ 管理元素/函数/量/逻辑算子（TR292x）+ 扩展（TR291x）+ Connector（TR293）+ 3GPP 扩展（TR294A）；TMF921 的 expression 由 TIO 校验。
2. **校验缺口补丁**：tio-shacl 将 15 个 v3.6.0 模块变成 SHACL；无此层则"合法 RDF ≠ 合法意图"。
3. **SID→OWL**：仍属 Catalyst（MODA 25.5 派生），不是 GB922 规范性交付。
4. **CCSA 建模**：本体模型约束实例三元组；七类运维数据分项建模（第三方解读）。
5. **3GPP 桥**：Annex C 映射 Expectation 结构到 ICM；Stage-3 仍 YAML。语义网管若引入 RDF，需新 solution set 决策，当前未做。

## 5. 趋势驱动力

- 业务：AN L4 与多厂商 agent 互操作要求共享语义，而非共享自然语言上下文（ODA Roadmap 原则 2.4/2.6）。
- 技术：LLM/Agent 放大幻觉与不可审计风险，推动 OWL/SHACL 门禁（tio-shacl、Agent Fabric SID KG）。
- 政策：国内 YD/T 2026-09-01 实施形成采购与测评压力；3GPP Rel-20 研究窗到 2027-06。

## 6. 批评与风险

- **获取壁垒**：GB1093/TR328/TR329/TR326 全文会员或 Confluence；TIO 最新增量会员墙。
- **形式化断层**：UML SID 与 RDF TIO 并存，联邦机制未公开，存在"两个语义源"。
- **标准名碎片**：知识面 / SKF / SNM / 知识管理 / Data Fabric 语义层五词并行。
- **GB1094 未核实**：不得在路线图中当作已存在文档。
- **第三方解读风险**：YD/T 条款细节大量来自 antpedia，正式文本未购得。

## 7. 对我司的相关性

数据中台作为自智网络**数据引擎**的支撑角色：年内可做 YD/T 7007 小样例、TIO+SHACL 校验 PoC、openapi-to-rdf 陪跑 SA5 WT-4；公司级 SID 全量本体化与跨 WG 联合提案须上升决策。详见 [统一分析 §9](../../analysis/ontology-standards-unified-analysis.md)。禁止表述为公司级数据底座。

## 矛盾与待核实

- 联邦本体 vs SID 单一 OWL（矛盾 34）
- 本体驱动 vs 数据/LLM 驱动自治（矛盾 35）
- 复用 TMF 本体 vs SA5 自建知识模型（矛盾 36）
- TMF448 编号未在 Roadmap 正文出现；TR 28.881 结束日 portal 与研讨材料不一致
- GB1094 标题未能核实

（已同步 `analysis/contradictions.md`、`analysis/gaps.md`）

## 数据缺口

- GB1094 公开核实失败
- GB1093/TR328/TR329/TR326 全文
- 华为牵头 CCSA 本体规范（公开为参与起草）
- SA5 对 TMF 本体除 Annex C/TR294A/WT-4 外的正式互引
- TR 32.801-01 与 YD/T 正文

## 来源

### 一手资料 / 官方 ★

1. [TR292 TIO v3.6.0](https://www.tmforum.org/resources/introductory-guide/tr292-tm-forum-intent-ontology-tio-v3-6-0/) — GA 意图本体
2. [Intent Toolkit](https://www.tmforum.org/toolkits/intent/) — 模块与 2026-03-27 更新（仅摘要可见）
3. [TR294A](https://www.tmforum.org/resources/technical-report/tr294a-model-connection-to-3gpp-ts-28-312-intent-extension-model-v1-0-0/) — 连接 TS 28.312
4. [AI Native ODA Roadmap 文](https://inform.tmforum.org/features-and-opinion/ai-native-oda-the-path-to-open-digital-autonomy) — 2026-06-18，BSS/OSS 本体优先事项
5. [YD/T 7007 SAMR](https://std.samr.gov.cn/hb/search/stdHBDetailed?id=5679B6F617894858E06397BE0A0AD0B8) — 发布/实施/起草单位
6. [YD/T 7019 SAMR](https://std.samr.gov.cn/hb/search/stdHBDetailed?id=5679B6F617964858E06397BE0A0AD0B8)
7. [YD/T 6103 SAMR](https://std.samr.gov.cn/hb/search/stdHBDetailed?id=29962E7E064FA432E06397BE0A0A0BF0)
8. [FS_6G_OAM WI](https://portal.3gpp.org/desktopmodules/WorkItem/WorkItemDetails.aspx?workitemId=1100014)
9. [SA5 Work Areas PDF](https://www.3gpp.org/ftp/Email_Discussions/SA5/OAM%20rapporteur%20calls/Rapporteur%20call%20%23161/SA5_NWM_Discussion_for_Rel-20_6G_OAM_Work_Areas-v0.0.7.pdf) — SNM WT-1~5
10. [TS 28.312 V19.5.0](https://etsi.org/deliver/etsi_ts/128300_128399/128312/19.05.00_60/ts_128312v190500p.pdf) — Annex C
11. [ITU-T M.3351](https://www.itu.int/epublications/publication/itu-t-m-3351-2024-08-framework-of-knowledge-management-for-telecom-operation-and-management)

### 学术 📄

12. [tio-shacl arXiv:2604.27359](https://arxiv.org/abs/2604.27359) — 2026-04-30

### 厂商白皮书 🏢

13. [openapi-to-rdf](https://github.com/EricssonResearch/openapi-to-rdf)
14. [C26.0.910](https://www.tmforum.org/catalysts/projects/C26.0.910) / [agent-fabric.github.io](https://agent-fabric.github.io/)
15. Ericsson / Samsung / ZTE / Huawei SA5 workshop PDF（3gpp.org FTP）

### 分析机构 / 媒体

16. [Inform 知识面报告](https://inform.tmforum.org/research-and-analysis/reports/building-knowledge-planes-to-scale-autonomous-networks) — 2026-07-01
17. engage.tmforum.org 社区讨论（GB1093/TR328/TR329/TR326 标题，仅摘要可见）
