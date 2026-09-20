# 本体标准统一分析 · 计划与审核记录

> 任务：对 TM Forum 本体论进行深度调研，结合 GB1093 / GB1094 / TR328 / TR329、华为主导的 CCSA 本体相关规范、3GPP SA5 的工作，做统一分析。
> 分工：**Fable（Claude Fable 5.1）负责计划制定与审核**；**Grok（cursor-grok-4.6-high）负责具体检索、精读与撰写**。审核不通过则由 Fable 给出具体修改指令，Grok 迭代。
> 日期：2026-09-20

---

## 1. Fable 侦察基线（计划前置事实，已联网核实）

| 编号 | 名称（核实结果） | 状态 | 来源 |
|---|---|---|---|
| GB1093 | The Federated TM Forum Ontology（MODA-440） | 2026 年 TM Forum 本体 tiger team 工作文档，Confluence 内部页 | engage.tmforum.org 社区讨论帖引用 |
| GB1094 | **未能在公开检索中核实标题**（搜索结果均为电力变压器国标 GB 1094） | 待 Grok 二次核实；若仍无法核实须显式登记为缺口 | — |
| TR328 | The Case for Ontologies: A Roadmap for TM Forum | tiger team 技术文档 | 同上 |
| TR329 | TM Forum Ontology Programme Governance: Requirements and Feasibility（MOD-441） | tiger team 技术文档 | 同上 |
| TR326 v2 Suite | Operationalizing Ontologies for AI-Native Autonomous Networks – Components and Canvas（Semantic Knowledge Fabric） | 2026-06 发布 | tmforum.org / inform.tmforum.org |
| TR292 系列 | TM Forum Intent Ontology（TIO）v3.6.0，15 个本体模块（TR290/TR291x/TR292A–I/TR299） | GA，2024-07；TR290 v3.8.0 与 TR292I v4.0.0 于 2026-03-27 更新 | tmforum.org/toolkits/intent |
| TMF448 | AI Native ODA Roadmap v1.0：优先事项含"基于 SID/eTOM 的 BSS/OSS 本体" | 2026 | inform.tmforum.org |
| CCSA | YD/T 7007-2026《网络运营管理知识图谱技术要求 知识建模方法》（本体模型 + 实例化模型，RDF 三元组/多元组）；YD/T 7011-2026 总体框架；YD/T 7024-2026 知识图谱构建；YD/T 7019-2026《自智网络 知识管理技术要求》；YD/T 6103-2024《IP 自智网络 知识面技术要求》 | 2026-06-01 发布，2026-09-01 实施；华为为起草单位之一（中国移动牵头） | std.samr.gov.cn / ndls.org.cn / C114 |
| 3GPP SA5 | FS_6G_OAM（WI 1100014，TR 32.801-01，2025-12 → 2027-06）含"Semantic Network Management"工作域 WT-1~WT-5，WT-4 明确要调研 RDF/知识图谱/本体（TM Forum 等）；TS 28.312 Annex C 已含 3GPP IntentExpectation ↔ TM Forum ICM 映射；TR 28.881（IDMS_Ph4，2025-08 → 2026-06） | 进行中 | 3gpp.org FTP / portal.3gpp.org / ETSI |

## 2. 交付物清单（Grok 产出，Fable 审核）

| # | 路径 | 内容 |
|---|---|---|
| D1 | `research/notes/ontology-standards-tmf-ccsa-3gpp.md` | 精读笔记（按 research/notes/README.md 模板） |
| D2 | `research/search-log.md` | 追加检索记录（≥ 12 行） |
| D3 | `wiki/topics/ontology-standards-tmf-ccsa-3gpp.md` | 主题卡（按 wiki/templates/topic-card.md，frontmatter 合规） |
| D4 | `analysis/ontology-standards-unified-analysis.md` | **主交付**：TM Forum × CCSA × 3GPP SA5 本体标准统一分析 |
| D5 | `wiki/glossary/ontology.md`、`wiki/glossary/knowledge-plane.md` | 术语卡 |
| D6 | `analysis/gaps.md`、`analysis/contradictions.md` | 追加缺口与矛盾（编号从"矛盾 33"起） |
| D7 | `wiki/topics/README.md` | 在"已完成主题"表追加一行 |

## 3. 审核标准（Acceptance Criteria）

**A. 事实与可溯源**
- A1 每个标准编号（GB/TR/YD/T/TS/TR）必须给出可访问 URL 或明确"未能核实 + 已尝试的 query"。**禁止编造文档标题或版本号**。
- A2 每条关键论断旁标 [高]/[中]/[低]；[高] 需 ≥ 2 个独立权威来源。
- A3 来源总数 ≥ 25，其中官方一手（tmforum.org / inform.tmforum.org / 3gpp.org / portal.3gpp.org / etsi.org / std.samr.gov.cn / ndls.org.cn / ccsa.org.cn）≥ 8。
- A4 涉及"现状/进展"的论断优先使用 2024-01 之后来源，并写明日期。

**B. 分析深度（D4）**
- B1 对比矩阵：至少 3 个组织（TM Forum / CCSA / 3GPP SA5）× ≥ 8 个维度（定位、范围与层级、建模语言与形式化程度、联邦/治理机制、与意图/数据管理的关系、与数据编织/6G 数据面的关系、成熟度与时间线、主导玩家、开放性/获取方式）。
- B2 三方关系图（Mermaid）：说明 TM Forum 本体（TIO / SID-MODA / 联邦本体）、CCSA 知识图谱本体、3GPP SA5 语义网管三者的引用、映射与空白。
- B3 时间线 2022–2027（含 FS_6G_OAM 2027-06、TR 28.881 2026-06、CCSA 2026-09-01 实施、TR326 2026-06、TIO 版本节点）。
- B4 "本体 vs 信息模型 vs 知识图谱"三层辨析，说明 SID/MODA（UML）→ OWL/RDF 的转译问题与 Ericsson openapi-to-rdf / tio-shacl 等实证工具。
- B5 矛盾与缺口章节（同步到 D6）。
- B6 对我司（中兴数据中台 / 自智网络"数据引擎"）的启示：区分【可直接执行（千万级/年内）】与【需向公司建议】两类；**不得**使用"公司级底座"等过强定位（参见 ops/company-context.md 口径）。

**C. 形式与一致性**
- C1 全部简体中文；文件、frontmatter 与 README 约定一致（title/title_en/slug/category/status/confidence/sources/related/tags/last_verified/owner）。
- C2 search-log 使用现有表格格式，工具列填 `web-search` / `web-fetch`。
- C3 不修改本清单之外的既有文件；不得删除既有内容。
- C4 内部引用使用相对路径链接到 wiki/analysis 文件。

## 4. 审核记录

> 每轮由 Fable 填写：通过项 / 不通过项 / 修改指令。

（待填写）
