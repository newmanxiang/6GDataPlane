# Catalyst C26.0.910 / Agent Fabric 本体相关归档

Project site: https://agent-fabric.github.io/
Catalyst: https://www.tmforum.org/catalysts/projects/C26.0.910 （Winner）

## 语义主张

A2A-T 把每个任务绑定到 AN High-Value Scenario 与共享电信词汇（SID），使 intent 在执行前类型化、无歧义。

OpenAN 运行时中的 Knowledge Graph：组织 SID、BPMN 语料、Task-T 历史为机器可用语义。

能力演示：

- **10 SID Ontology**：TM Forum SID as OWL knowledge graph, queryable via SPARQL and MCP（Huawei）
- **11 AN Ontology / Knowledge Graph**：AN use cases as knowledge graph, MCP-accessible（Vodafone + Huawei）

计划开源仓库（Phase III，DTW 2026 前后毕业）：

- `sid-ontology`：SID Information Model 的形式化 OWL KG，源自 MODA 25.5，SPARQL + MCP
- `c-kg`：自智网络知识图谱 + 解耦 OWL 本体，经 MCP server 暴露用例

## 与 TMF 资产的关系（项目自称）

Carries: TMF921, TMF641/621/642, TIO, 3GPP TS 28.312。
Anchors: IG1251 / IG1251C / IG1251D / IG1251E。
Authored: IG1453 v2.1.0 A2A-T、IG1453A v1.1.0 realisation guide。

CSP Champions 含 Orange、Telefónica、DT、Vodafone、China Unicom、China Mobile、LG U+ 等 18 家。Vendors 含 Huawei、Amdocs、RADCOM、MEF.DEV、Infosys、Infovista、Iquall。未见 ZTE 列在该 Catalyst vendor 表。

## 截至 2026-09-20 的公开状态

`sid-ontology` 与 `c-kg` **未出现在** `github.com/project-openan`。DTW Copenhagen 已于 2026-06 举办，开源承诺与实际仓库不一致，记为缺口。
