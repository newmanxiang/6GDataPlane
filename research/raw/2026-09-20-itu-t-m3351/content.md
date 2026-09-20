# ITU-T M.3351 / M.3351.2 电信运营管理知识管理

- M.3351：2024-08-13，SG2，Framework of knowledge management for telecom operation and management
- M.3351.2：2025-10，Process of telecommunication operation and management knowledge graph construction
- 全文：ITU 公开 PDF 已抓取

## 与本体直接相关的条款（M.3351 §8.2.3.2）

Knowledge modelling：

- Ontology modelling defines specific meanings and relations of knowledge（示例：fault cause / phenomenon / resolution）
- 支持 ontology creation, viewing, destruction, and quality management
- Knowledge representation：机器可处理的符号或数值表示，例如 RDF（ITU-T F.750）和 OWL（ITU-T Y.4563）

知识构建还包括 annotation、extraction、fusion、reasoning、validation。

M.3351.2 九步：knowledge modelling → raw data management → annotation → extraction → fusion → reasoning → validation → storage → knowledge service。附录用例：网络故障诊断、主动网络优化。

## 作为参照系的用途

ITU-T 把「本体建模」写成知识图谱构建的第一步，形式化语言明确为 RDF/OWL。这与 CCSA YD/T 7007 公开摘要、TMF TIO 的 RDF 路线同类，但 **ITU-T 不替代 TMF GB1093 或 3GPP NRM**。
