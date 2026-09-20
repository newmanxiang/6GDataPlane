# AsiaInfo AN-Ontology（GitHub 精读归档）

- Source: https://github.com/asiainfo/AN-Ontology
- Clone SHA: `d8bf5f73146e6acf50e72efb4dcaf1cac6c4fdde` (2025-10-24 21:05 +0800)
- Fetched: 2026-09-20
- License: CC BY 4.0（仓库 LICENSE）；各模块 README 另称 Apache 2.0

## 项目自我定位

> 自智网络本体项目旨在为自智网络（Autonomous Network, AN）领域构建统一的语义知识基础，通过形式化的本体模型表达网络专业知识，支撑智能体系统实现更准确的网络语境理解和决策推理。

宣称解决三类问题：LLM 网络语言幻觉、人机信任鸿沟、智能体协同语义不一致。

标准化推进表述（README 原文）：

- **TMF标准推广**：在TMF等标准组织推进本体应用
- **TMF自智网络标准**：参与TMF AN相关标准制定
- 相关项目：ODLM (Ontology for Data Lake Management)

## 目录与 README 漂移

README 目录仍写 `iot-complaint-tickets/`、`core-network-fault/`、`network-resource/`，且后两项勾选为未完成；实际仓库在 2025-10-24 提交了：

- `IoT Complaint Ticket Ontology/`
- `5G Core Network Ontology/`
- `Resource Manage Ontology/`

README 规划把核心网故障本体、网络资源本体标为「预计 2025 年发布」且 checkbox 未勾，与已提交的 5GC / Resource Manage 模块不一致。

## 三模块规模（本调研对 TTL 实计）

| 模块 | IRI | Classes | ObjectProp | DataProp | Individuals |
|---|---|---|---|---|---|
| IoT 投诉工单 | `iot-Complaint-ticket#` | 30 | 18 | 16 | 99 |
| 5GC 网元 | `ontology/5gc#` | 31 | 64 | 20 | 26 |
| 家客资源 | `Ontology/Resource-Manage#` | 28 | 39 | 56 | 0 |
| **合计** | 三套独立 ns | **89** | **121** | **92** | **125** |

## 质量观察（归档时核实）

1. **命名空间不统一**：根 README 用 `http://asiainfo.com/an-ontology#`；三模块分别用 `www.asiainfo.com/ontology/...` 与 `www.asiainfo.com/Ontology/...`（大小写不同），无 `owl:imports` 把三模块接到统一 upper ontology。
2. **5GC 拼写错误**：接口枚举一律写成 `InfterfaceN2` 等（Interface 缺字母 e），TTL 与文档示例同步复制该错误。
3. **文件名拼写**：`Resource-Manage-ontopology.ttl`（ontology 误写）。
4. **Resource Manage README.md 整文件复制了 5GC README**（标题、3GPP 5GC 背景、AMF 扩容用例均未改）；真正的资源本体说明在 `Resource-Manage-Ontology-Overview-CN.md`。
5. **词汇文档内链污染**：Resource Manage 词汇 TOC 指向 `https://www.doubao.com/chat/...` 豆包会话锚点。
6. **宣称存在但仓库没有的文件**：`examples/`、SHACL shapes、CONTRIBUTING.md、`5gc-ontology` 独立仓库链接。
7. **5GC 文档用例中的类未在 TTL 声明**：`5gc:ServiceFault`、`5gc:RegistrationFault`、`5gc:ExpansionAnalysis` 等出现在 README 示例，本体文件无对应 `owl:Class`。
8. **与 TMF SID / TIO 无形式化对齐**：全文检索仅 README 有「参与 TMF AN」叙述，TTL 无 SID ABE、无 TIO `Expectation`/`Intent`、无 `owl:equivalentClass` 指向 TMF/3GPP IRI。
9. **许可声明冲突**：根 LICENSE 为 CC BY 4.0；5GC/IoT README 写 Apache 2.0。

## 5GC 模块要点

- 基于 3GPP 5GC 网元：AMF / SMF / UPF / UDM（无 PCF/NSSF/AUSF 作为一类，仅接口注释提及）。
- 接口属性绑定在具体 NF 上（`5gc:n2Interface` domain=AMF），而非独立 Interface 与 NF 的通用关联。
- N12 注释写成「UDM-AUSF」却 domain 在 AMF 上，与 3GPP TS 23.501 参考点定义不一致。
- 文档引用 TS 23.501 / 23.502。

## 家客资源模块要点

- 覆盖 OLT/ONU/POS/光纤分纤、小区/客户/宽带/IMS/IPTV、地址/机房/站点。
- `belongsToDistrict` 的 domain 使用 `owl:unionOf` 覆盖十余类实体。
- 把 OWL 基数约束 `owl:cardinality` 等误标为 `owl:AnnotationProperty`（削弱推理语义）。

## IoT 工单模块要点

- 工单生命周期 + 设备/SIM + 故障分类 + SLA。
- 使用 SKOS/FOAF/vCard 前缀，实际对齐浅。
- 唯一使用 `owl:FunctionalProperty` / `owl:inverseOf`（`uses` ↔ `boundTo`）的模块。
