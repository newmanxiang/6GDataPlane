# 笔记：ontology-standards-tmf-ccsa-3gpp

## 调研窗口
2026-09-20 → 2026-09-20

## 已精读源

### [A practical hypothesis: Operational Centricity…]（社区讨论，日期未在正文标明；检索日 2026-09-20）
URL: https://engage.tmforum.org/discussion/a-practical-hypothesis-operational-centricity-as-a-complementary-decision-context-dimension-for-an-transformation
归档: 未能本地归档（WebFetch 被 Cloudflare/站点改写拦截，仅搜索摘要可见）

#### 关键数据点
- 明确列出 tiger team 技术文档三件套标题：TR328 *The Case for Ontologies: A Roadmap for TM Forum*；TR329 *TM Forum Ontology Programme Governance: Requirements and Feasibility (MOD-441)*；GB1093 *The Federated TM Forum Ontology (MODA-440)*（标注为 MODA Confluence 页）。
- 将 TR326 v2 Suite 标题写为 *Operationalizing Ontologies for AI-Native Autonomous Networks – Components and Canvas*，并称其描述如何创建联邦 Semantic Knowledge Fabric，作为知识面与 AI/人类推理、治理功能之间的"语义契约"技术基础。
- 未出现 GB1094 标题或编号。

#### 关键论断
- 知识编织需要形式化本体；TM Forum 正以短期 tiger team 推进 SID/eTOM/Open API 之上的语义 enrichment。[中]
- TR328/TR329/GB1093 处于 tiger team / Confluence 内部工作文档状态，非公开 GA 资源页。[中]

#### 新发现的术语 / 人名 / 公司
- Semantic Contract；Semantic Knowledge Fabric；MODA-440；MOD-441；Ontology tiger team

#### 与其他来源的矛盾
- 公开 tmforum.org 资源目录（搜索可见 GB1072、GB922 v25.0 等）未列出 GB1093/TR328/TR329 独立资源页；与社区帖"正在产出有用技术文档"并存，说明获取方式为会员/内部。

#### 待追查
- GB1093/TR328/TR329 全文、版本号、Team Approved 日期。
- GB1094 是否存在（见下方多次检索）。

---

### [TM Forum Intent Toolkit]（标准目录，检索日 2026-09-20；仅摘要可见）
URL: https://www.tmforum.org/toolkits/intent/
归档: WebFetch 被 Cloudflare 拦截

#### 关键数据点
- TR292 TIO v3.6.0、TR292A/C/D/E/F/G、TR292R、TR299：Team approved / 公开日 2024-07-04，多数 "Available to all"。
- TR292H Mathematical Functions v3.7.0：2025-11-21，会员。
- TR290 Intent Common Model v3.8.0、TR292I Security Ontology v4.0.0、IG1358 v1.2.0、TR291A Intent Validity v3.7.0：2026-03-27，会员。
- TR293 Connector Model v2.0.0：2023-04-11，公开。
- TR294A Model Connection to 3GPP TS 28.312 v1.0.0：2023-04-11。
- IG1253 Intent in Autonomous Networks v1.3.0：2022-08-01。
- TR291B Intent Probing v3.6.0、TR291C Proposal of Best Intent v3.6.0：2024-07-04。
- TR291D Intent Acceptance Control v1.1.0、TR291E Intent Compliance Latency v1.1.0：2022-06-01。

#### 关键论断
- TIO 是 TM Forum 目前唯一达到 GA、带 RDF 规范性词汇的本体族；SID/MODA 仍以 UML/XMI 交付（GB922 v25.0，Team Approved 2025-07-18）。[高]

#### 新发现的术语
- ICM（Intent Common Model）；Connector Model；Intent Extension Model

#### 与其他来源的矛盾
- Ericsson tio-shacl 论文把 15 个模块描述为 TR290 + TR292A–E + TR291 系列 + TR299 的规范性 Turtle；toolkit 同时列出 TR292F/G/H/I、TR290A/B。模块计数口径不完全一致（论文称 15 个 ontology modules）。

#### 待追查
- "15 个模块"的官方枚举清单（TIO 发布说明 RN）。

---

### [TR292 TIO v3.6.0 资源页]（官方，2024-07-04 / TM Forum Approved 2024-08-30）
URL: https://www.tmforum.org/resources/introductory-guide/tr292-tm-forum-intent-ontology-tio-v3-6-0/

#### 关键数据点
- 文档类型 Technical Report；成熟度 GA；项目 Autonomous Networks Project。
- 摘要：意图管理本体引入意图管理功能与概念分类，提供可被 ICM 与扩展模型使用的基本词汇。

#### 关键论断
- TIO 定位为意图控制环与生命周期管理的词汇层，而非 SID 全量 OWL 化。[高]

---

### [TR293 Connector Model v2.0.0]（官方，2023-04-11）
URL: https://www.tmforum.org/resources/technical-report/tr293-connector-model-v2-0-0/

#### 关键数据点
- 为面向不同 SDO 的意图扩展模型提供基础词汇；对应扩展模型在另一套模型中定义。状态 Member Evaluated / Beta。

#### 关键论断
- TIO 通过 Connector + Extension 机制连接外部 SDO 模型，而非把外部模型吞并进 SID。[中]

---

### [TR294A Model Connection to 3GPP TS 28.312]（官方，2023-04-11）
URL: https://www.tmforum.org/resources/technical-report/tr294a-model-connection-to-3gpp-ts-28-312-intent-extension-model-v1-0-0/

#### 关键数据点
- 3GPP 专用意图扩展模型套件之一；定义可用于无线网络与无线服务（radio network as a service）意图的 artifacts。状态 Member Evaluated / Alpha。

#### 关键论断
- 这是 TM Forum→3GPP 方向的正式模型连接件；与 TS 28.312 Annex C（3GPP→TMF ICM 映射）构成双向但层级不对称的互引。[高]

---

### [AI Native ODA: The path to open digital autonomy / Andy Tiller]（官方媒体，2026-06-18）
URL: https://inform.tmforum.org/features-and-opinion/ai-native-oda-the-path-to-open-digital-autonomy

#### 关键数据点
- 文章明确分享 AI Native ODA Roadmap v1.0（任务称 TMF448；本文正文未出现 "TMF448" 编号，编号未能在本页核实）。
- 优先事项含："Telecoms BSS / OSS ontologies based on ODA's frameworks (e.g., SID, eTOM)"。
- 已有能力含 SID、eTOM、TIO；原则 2.6 要求 ODA 提供 ontology-driven semantics。
- 强调 agent 互操作需要 shared semantic understanding，不只是 shared context。

#### 关键论断
- SID/eTOM 本体化被列为 Roadmap 优先事项，说明当前 SID 仍非可执行 OWL 本体。[高]

---

### [Building knowledge planes to scale autonomous networks / Charlotte Patrick]（分析报告摘要，2026-07-01）
URL: https://inform.tmforum.org/research-and-analysis/reports/building-knowledge-planes-to-scale-autonomous-networks

#### 关键数据点
- 知识面 = 将碎片数据转化为上下文化、可复用知识的结构化语义层，供 AI agent 理解、推理与行动。
- 宣称到达 AN L4 需要从管理数据/流程转向管理知识。
- 全文付费/会员，仅摘要可见。

#### 关键论断
- 知识面被定位为 L4 的架构前提，而非可选分析组件。[中]（单一 Inform 报告）

---

### [Catalyst C26.0.910 Agent Fabric / agent-fabric.github.io]（厂商+社区实现，DTW 2026）
URL: https://www.tmforum.org/catalysts/projects/C26.0.910 ；https://agent-fabric.github.io/

#### 关键数据点
- Huawei 贡献 SID Ontology：TM Forum SID 表达为 OWL KG，派生自 MODA 25.5，可 SPARQL/MCP 查询。
- Vodafone+Huawei：AN Ontology / Knowledge Graph。
- 携带 TIO、TMF921、3GPP TS 28.312，而非替换。
- IG1453 v2.1.0（站点自称 Authored；公开资源页可见 IG1453 v1.0.0）。
- 18 CSP champions、7 vendors；开源仓 sid-ontology / c-kg 计划 DTW 2026 公开。

#### 关键论断
- SID→OWL 转译已有 Catalyst 实证，但尚未成为 TM Forum 规范性 SID 交付物（官方 SID 仍是 GB922 UML/XMI/Excel）。[高]

#### 矛盾
- 联邦本体（GB1093）叙事 vs Catalyst 把 SID 做成单一 OWL KG：一个强调联邦，一个强调 SID 可查询化。

---

### [TIO-SHACL, arXiv:2604.27359]（学术，2026-04-30）
URL: https://arxiv.org/abs/2604.27359
作者: Jean Martins, Leonid Mokrushin, Marin Orlic（Ericsson Research）

#### 关键数据点
- 15 个 tio v3.6.0 模块；56 node shapes / 69 property shapes / 147 constraint instances。
- 词汇覆盖 87 classes、109 properties、72 functions。
- 25 parameterized SPARQL constraint components；133 测试（67 valid / 66 invalid）。
- 引用模块：TR290；TR292A–E；TR291A/C/G/H/I；TR299；IG1253；IG1358。
- MIT：https://github.com/EricssonResearch/tio-shacl

#### 关键论断
- TIO 有 RDF 规范性文件但缺少正式校验机制；SHACL 可补这一工程缺口。[高]（论文+GitHub）

---

### [EricssonResearch/openapi-to-rdf]（开源，README 检索 2026-09-20）
URL: https://github.com/EricssonResearch/openapi-to-rdf

#### 关键数据点
- OpenAPI schema → 分离的 RDF vocabulary + SHACL shapes；测试输入为 3GPP SA5 MnS Rel-18/Rel-19（forge.3gpp.org/rep/sa5/MnS/）。
- Rel-19 预生成输出；38+ schema 文件。
- PyPI openapi-to-rdf v0.1.1。

#### 关键论断
- 3GPP 现有 solution set 是 OpenAPI/YANG/UML，RDF 是研究/开源转译，不是 SA5 规范性 solution set。[高]

---

### [YD/T 7007-2026]（官方元数据 + 第三方解读）
官方: https://std.samr.gov.cn/hb/search/stdHBDetailed?id=5679B6F617894858E06397BE0A0AD0B8
NDLS: https://www.ndls.org.cn/standard/detail/16edb0b14d6e859da98799325baee2f7
解读: https://www.antpedia.com/standard/1835576687-10.html （第三方，不等同原文）

#### 关键数据点
- 发布 2026-06-01，实施 2026-09-01；归口 CCSA；主管部门工信部；备案号 106655-2026。
- 起草单位：北京邮电大学、中国电信、华为、浪潮通信技术、中国联通、中兴、中通服咨询设计研究院。**第一起草单位为北邮，非华为。**
- 解读（需标 [低]/[中]）：本体模型 vs 实例化模型；RDF 三元组/多元组；七类专项建模（配置/性能/告警/故障/规则/意图/运营）；五项准则；形式化可用 OWL/XML/JSON。

#### 关键论断
- 这是国内对"网络运营管理知识图谱建模"最接近本体规范的行业标准；华为为参与起草单位。[高]（SAMR+NDLS）

---

### [YD/T 7011-2026 / 7024-2026 / 7019-2026 / 6103-2024]
7011 NDLS: https://www.ndls.org.cn/standard/detail/9ac2589d993f0934f2fc975ebf03cac2
7024 NDLS: https://www.ndls.org.cn/standard/detail/73501cf26bf8261dd993a6eb2ea47396
7019 SAMR: https://std.samr.gov.cn/hb/search/stdHBDetailed?id=5679B6F617964858E06397BE0A0AD0B8
6103 SAMR: https://std.samr.gov.cn/hb/search/stdHBDetailed?id=29962E7E064FA432E06397BE0A0A0BF0

#### 关键数据点
- 7011 总体框架：中国移动、北邮、中兴、华为等；发布/实施同 7007。
- 7024 知识图谱构建：北邮、中国电信、华为、浪潮；覆盖建模、抽取、存储、融合、推理、质量评估。
- 7019 知识管理：中国移动牵头起草单位列表首位；华为/中兴均为起草单位。四类知识（事实/原理/技能/人际）、DIKW、元知识、集中+分布式分层。解读来自 antpedia，非原文。
- 6103：发布 2024-10-24，实施 2025-02-01；中国移动首位；华为、中兴参与。知识面六大模块：策略生成、策略验证、知识库、网络仿真验证、知识表征、网络数据。适用于 **IP 自智网络** 知识面。

#### 关键论断
- CCSA 路径是"知识图谱/知识管理/知识面"，几乎不使用"本体标准"作为标准名；公开信息中华为均为参与起草而非明确牵头方。[高]

---

### [华为牵头 CCSA 本体标准检索]
- 未找到名为"通信网络本体技术要求"且华为为第一起草单位的 YD/T。
- T/CCSA 690-2025《数字孪生网络 基础网络资产管理总体技术要求》：起草单位列表华为列首位（团体标准，非本体规范）。
- 信通院《本体智能研究报告（1.0）》将"华为行业本体"列为国内平台实践，属产品/平台而非 CCSA 标准。
- ADN 白皮书强调把专家知识注入知识图谱，未给出 CCSA 本体标准编号。

#### 待追查
- CCSA 内部在研立项清单（需会员）。

---

### [FS_6G_OAM / TR 32.801-01 / WI 1100014]（3GPP 官方）
Portal WI: https://portal.3gpp.org/desktopmodules/WorkItem/WorkItemDetails.aspx?workitemId=1100014
Spec: https://portal.3gpp.org/desktopmodules/Specifications/SpecificationDetails.aspx?specificationId=5491
讨论文稿: https://www.3gpp.org/ftp/Email_Discussions/SA5/OAM%20rapporteur%20calls/Rapporteur%20call%20%23161/SA5_NWM_Discussion_for_Rel-20_6G_OAM_Work_Areas-v0.0.7.pdf

#### 关键数据点
- WI：Study on 6G Management and Orchestration；Start 2025-12-03，End 2027-06-06；Rapporteur Bahar Sadeghi (AT&T)；TR rapporteur Pengxiang Xie (ZTE)。
- TR 32.801-01 状态 Draft；2026-06-04 进度备注 5%→20。
- Semantic Network Management WT-1~5 原文见讨论文稿 2.2.4；WT-4 明确 survey RDF、KG、ontologies（e.g. TM Forum）。
- 并行工作域 2.2.9 Data Management（统一数据管理机制，即 DMFW 讨论范围）。

#### 公司立场（精读 PDF / 讨论文稿）
- Samsung：把 Semantic Network Management 列为 Rel-20 优先；引用 ITU-T SG2 Q6/2（M.3351）与 IEEE KG framework；主张语义信息替代句法管理数据。
- Ericsson：Knowledge-Assisted/Semantic mgmt；意图新 solution set 举例 RDF；建议工作域名改为 Knowledge Management。
- Nokia：知识应放在 data management 下讨论；支持定义 APIs/Models/LCM/formats。
- ZTE：支持语义工作域 WT1/2/4；WT-3 若涉及架构演进应并入 6G management architecture；workshop PDF 强调 unified data framework、Large Model+Agent、知识管理作为 Agent 赋能 OAM 的并列能力，但未把本体作为独立优先项。
- Huawei：workshop 重点 Intent-driven Agentic Autonomous Management、Agent Fabric、统一数据管理；未在已抓取 PDF 中把 SNM 列为独立头条。
- China Mobile：讨论文稿支持研究语义工作域（Q1 yes）。

---

### [TS 28.312 Rel-19 Annex C]（ETSI/3GPP 官方，V19.5.0）
URL: https://etsi.org/deliver/etsi_ts/128300_128399/128312/19.05.00_60/ts_128312v190500p.pdf

#### 关键数据点
- Annex C 信息性映射：3GPP IntentExpectation ↔ TM Forum ICM IntentExpression（TR290A）：expectationObject↔icm:target；expectationTargets↔icm:Expectation 属性；expectationContexts↔icm:context。
- IntentReport ↔ ICM IntentReport（TR290B）。
- Annex F.3 部署场景 2：TMF Intent API 用于 Intent-CSC；3GPP IDMS 用于 Intent-CSP/NOP；转换指南引用 Annex C。
- 形式：3GPP 侧 UML/YAML/OpenAPI；TMF 侧 RDF/TIO。映射是信息模型级，不是 OWL 对齐。

---

### [TR 28.914 V19.0.0 / TR 28.881]
TR 28.914: https://www.etsi.org/deliver/etsi_tr/128900_128999/128914/19.00.00_60/tr_128914v190000p.pdf
TR 28.881 portal: https://portal.3gpp.org/desktopmodules/Specifications/SpecificationDetails.aspx?specificationId=4433
WI 1080006: https://portal.3gpp.org/desktopmodules/WorkItem/WorkItemDetails.aspx?workitemId=1080006

#### 关键数据点
- TR 28.914 引用 TM Forum IG1253、ETSI GR ZSM 011；研究 IDMS phase 3。
- FS_IDMS_MN_Ph4 WI start 2025-06-05，portal end 2026-03-03，2026-03-05 进度 100%；TR 28.881 2025-07-07 创建，2026-03-16 Under change control；ZSM 联合研讨 PDF 称研究 2025-08→2026-06、目标 2026-06 发布。日期口径不完全相同，以 portal 为准并注明研讨材料口径。
- Rapporteur（WI）：Ruiyue Xu (Huawei)；Spec rapporteur：Mark Scott (Ericsson)。

---

### [SA5–ETSI ZSM 联合研讨 2025-07-03]
目录: https://www.3gpp.org/FTP/tsg_sa/WG5_TM/Joint_meetings/2025_07_ZSM_SA5_WS
SA5 意图材料: 同目录 PDF

#### 关键数据点
- 3GPP 表示可基于选定用例与其他 SDO 协作意图管理。
- ZSM 材料引用 TM Forum 意图元模型（ICM + extension，基于本体）与 3GPP 声明式意图模型。
- 未将 RDF 定为 3GPP 新 solution set。

---

### [ITU-T M.3351 (08/2024)]（官方）
URL: https://www.itu.int/epublications/publication/itu-t-m-3351-2024-08-framework-of-knowledge-management-for-telecom-operation-and-management

#### 关键数据点
- SG2 电信运维知识管理框架；六功能块：scenario application / knowledge service / construction / storage / maintenance / raw data management。
- Samsung SA5 workshop 明确引用。IEEE P2807-2022 KG framework 同被引用。

---

### [Appledore/Vitria Semantic Knowledge Plane 白皮书]（分析，2026-04）
URL: https://vitria.com/wp-content/uploads/2026/04/Semantic-Knowledge-Plane-Appledore-Whitepaper-0426.pdf

#### 关键数据点
- 知识面 = 网络状态、业务意图、运营策略的统一语义实时模型（形式化本体）。
- 建议知识面与 data fabric **并行建设**，不必等完整 fabric。
- 对齐 TM Forum SID（适用处）+ W3C RDF。厂商白皮书，证据 [低]/[中]。

## 综合判断（写入 wiki/topics 前的草稿）

1. TM Forum 本体体系呈"两层"：已 GA 的 TIO（意图 RDF 词汇）vs 正在内部推进的联邦本体/SID-eTOM 本体化（GB1093、TMF448 优先事项、Catalyst SID OWL）。不可把 TIO 等同于 SID 本体。[高]
2. CCSA 已发布可实施的知识图谱/知识管理/知识面行业标准（2026-09-01 实施），形式化走 RDF 三元组+工程化建模，华为/中兴均为起草单位但牵头多为运营商或北邮。[高]
3. 3GPP SA5 已有 IntentExpectation↔ICM 信息性映射，Rel-20 才把 RDF/本体列为调研对象（WT-4）；RDF 作为新 solution set 仅为 Ericsson 等公司提议，尚未标准化。[高]
4. "语义层是数据编织的核心能力"在电信标准中得到间接支持（TMF 知识面/SKF、CCSA 知识面、SA5 SNM↔DMFW），但三方均未把 Data Fabric 写成规范术语并与本体互引；证据强度为中等。[中]
5. GB1094 公开检索无法核实标题，禁止猜测。[高]

## 二轮深挖追查清单
- [ ] 会员账号获取 GB1093 / TR328 / TR329 / TR326 v2 全文与版本页
- [ ] 用 Confluence/成员目录确认 GB1094 是否为内部编号
- [ ] TIO v3.6.0 官方 15 模块枚举（RN/发布说明）
- [ ] YD/T 7007/7019 正式文本（本体模型章节、六大功能模块原文）
- [ ] CCSA 立项系统检索"本体"在研项目
- [ ] SA5 对 TM Forum 本体的 liaison（除 TR294A / Annex C / WT-4 调研表述外）
- [ ] TR 32.801-01 草案正文（现仅 Draft + pCR 文件名）
- [ ] sid-ontology / tio-shacl 与 MODA 25.5 的类覆盖率对比
- [ ] TMF448 作为文档编号的官方资源页
- [ ] ETSI ZSM GS 029 与知识面/本体的交叉引用
