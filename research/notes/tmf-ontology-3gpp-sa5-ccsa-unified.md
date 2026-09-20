# 笔记：tmf-ontology-3gpp-sa5-ccsa-unified

## 调研窗口
2026-09-20 → 2026-09-20

## 已精读源

### [GB1093 The Federated TM Forum Ontology (MODA-440)]（标准/会员 Confluence，日期未知）
URL: https://engage.tmforum.org/discussion/a-practical-hypothesis-operational-centricity-as-a-complementary-decision-context-dimension-for-an-transformation
归档: research/raw/2026-09-20-tmf-gb1093/

#### 关键数据点
- 标题与工作项 MODA-440 仅出现在 TM Forum Community 讨论对 Confluence 的引用
- 与 TR328、TR329 并列，属 Ontology tiger team
- 公开 resources 目录无落地页

#### 关键论断
- TMF 正在从「意图本体 TIO」扩展到「联邦 TMF 本体 + Semantic Knowledge Fabric」
- GB1093 被定位为联邦本体本身，不是 SID 的别名

#### 待追查
- 会员账号获取 Confluence/PDF；版本、贡献公司、与 SID/TIO 映射

### [GB1094]（未能核实）
归档: research/raw/2026-09-20-tmf-gb1094/

#### 关键论断
- 公开检索无 TMF GB1094 本体文档；须排除中国国标 GB 1094 电力变压器
- Community 三件套未列 GB1094

### [TR328 The Case for Ontologies: A Roadmap for TM Forum]（标准/会员，日期未知）
归档: research/raw/2026-09-20-tmf-tr328/

#### 关键论断
- 路线图/论证类 TR，为本体计划提供 "why"
- 公开目录无 PDF

### [TR329 Ontology Programme Governance (MOD-441)]（标准/会员，日期未知）
归档: research/raw/2026-09-20-tmf-tr329/

#### 关键论断
- 治理与可行性，工作项号与 GB1093 的 MODA-440 连续

### [GB922 Information Framework Models Suite v25.0]（标准/2025-07-18）
URL: https://www.tmforum.org/resources/model/gb922-information-framework-models-suite-v25-0/
归档: research/raw/2026-09-20-tmf-gb922-sid/

#### 关键数据点
- v25.0.0，ISA 项目，含 SID Excel + MODA UML/XMI/HTML，会员墙
- SID 是 UML 信息模型，不是 OWL 本体

#### 与其他来源的矛盾
- 产业口头常把 SID 叫「本体」；TMF 自己把 ontology 一词主要用于 TIO（RDF）与 GB1093 联邦本体

### [TR292 TIO v3.6.0 + TR290 ICM + TR294A]（标准/2024-07–08）
URL: https://www.tmforum.org/resources/introductory-guide/tr292-tm-forum-intent-ontology-tio-v3-6-0/
归档: research/raw/2026-09-20-tmf-intent-common-model/

#### 关键数据点
- TIO v3.6.0 GA，AN 项目，公开可下载；Team 2024-07-04，TMF Approved 2024-08-30
- ICM 锚定 RDF；Ericsson tio-shacl 统计 15 模块、87 class / 109 property（学术 [中]）
- TR294A（2023-04-11）专门做与 TS 28.312 的模型连接

### [TS 28.312 V19.5.0]（标准/Rel-19，ETSI 镜像全文）
URL: https://etsi.org/deliver/etsi_ts/128300_128399/128312/19.05.00_60/ts_128312v190500p.pdf
归档: research/raw/2026-09-20-3gpp-ts28312-intent/

#### 关键数据点
- UML IOC + OpenAPI YAML，不是 RDF
- Annex C informative：expectationObject↔icm:target 等三对映射
- 引用 TR290A/B v3.6.0 与旧编号 IG1253A
- Annex F.3：TMF API 用于 CSC–CSP，3GPP MnS 用于 CSP–NOP / NOP–NEP

#### 关键论断
- 3GPP 与 TMF 意图对齐是正式的、但浅层的、informative 的桥接

### [TR 32.801-01 FS_6G_OAM]（标准/Draft Rel-20，2026-01-12 建档）
URL: https://portal.3gpp.org/desktopmodules/Specifications/SpecificationDetails.aspx?specificationId=5491
归档: research/raw/2026-09-20-3gpp-sa5-6g-oam-study/

#### 关键数据点
- 类型 TR 不是 TS；编号 32.801-01
- Rapporteur：中兴 Pengxiang Xie
- TOC 含 7.2.1 Knowledge/semantic representation and management
- WI 1100014，2025-12-03 至 2027-06-06

#### 与其他来源的矛盾
- 仓库既有「TS 32.801」与「DMFW = TS 28.104」混用；28.104 是 MDA

### [YD/T 7007/7011/7023/7024/7129-2026]（行标/2026-06–07）
URL: https://std.samr.gov.cn/hb/search/stdHBDetailed?id=5679B6F617894858E06397BE0A0AD0B8
归档: research/raw/2026-09-20-ccsa-huawei-ontology-spec/

#### 关键数据点
- 华为是主要起草单位之一，不是唯一牵头；北邮/移动/电信/联通分册牵头
- 中兴参与 7007、7011、7023、7129
- 7007 公开摘要含本体模型与 RDF；二手解读提 OWL

### [华为 ADN 白皮书 + IETF KG 仓]（厂商/2020–2025）
归档: research/raw/2026-09-20-huawei-adn-ontology/

#### 关键论断
- ADN 把知识图谱作为专家知识数字化手段
- `huawei.com/ontology/ietf-network/` 是 IETF 拓扑 RDF 示例，非 CCSA 标准

### [中兴数据中枢方案 + AN 白皮书]（厂商+内部上传）
归档: research/raw/2026-09-20-zte-an-whitepaper-ontology/

#### 关键数据点
- 内部方案已规划统一语义层 → 本体建模（网元/小区/告警等）
- TR 32.801-01 rapporteur 在中兴，是标准卡位事实而非产品成熟度证据

### [ITU-T M.3351 (2024-08) / M.3351.2 (2025-10)]（标准/全文）
归档: research/raw/2026-09-20-itu-t-m3351/

#### 关键数据点
- Knowledge modelling = ontology modelling + RDF/OWL 表示
- 九步构图流程；故障诊断与主动优化用例

### [TMF Inform knowledge planes, 2026-07-01]（分析/会员摘要）
URL: https://inform.tmforum.org/research-and-analysis/reports/building-knowledge-planes-to-scale-autonomous-networks

#### 关键论断
- L4 需要 knowledge plane；与 TR326 Semantic Knowledge Fabric 叙事一致

## 综合判断（写入 wiki/topics 前的草稿）

TMF 本体论当前是**双层**：已 GA 的意图本体 TIO（RDF，TR292/TR290）+ 仍在 MODA Confluence 的联邦本体计划（GB1093/TR328/TR329）。3GPP SA5 在意图层用 UML 与 TIO 做 informative 映射，在 6G OAM 研究中新开「知识/语义表示」KI，但没有 3GPP 本体。CCSA 2026 年落地的是运营管理知识图谱行标（含本体建模方法），华为/中兴均为起草方。统一分析的主结论：三套体系在「意图」上已有浅桥，在「网络运营本体/知识图谱」上并行且尚未互认；数据编织语义层应把 TIO 当意图契约、把 YD/T+M.3351 当运营知识建模、把 3GPP NRM/DMFW 当管理对象与数据框架，而不是幻想单一全球本体。

对中兴：已有 rapporteur 位 + 行标起草位 + 数据中枢本体建模实践，缺口是 TMF GB1093/TIO 贡献可见度与三套模型的显式映射表。

## 二轮深挖追查清单
- [ ] 会员获取 GB1093/TR328/TR329/TR326 正文
- [ ] YD/T 7007 正文中的 OWL 条款是否规范还是推荐
- [ ] SA5 KSM3 Knowledge architecture pCR 公司来源
- [ ] SID→OWL 是否进入 GB1093 范围
