# M5. 本体 / 信息模型标准映射矩阵

> 生成日期：2026-09-20
> 主题卡：[tmf-ontology-3gpp-sa5-ccsa-unified](../../wiki/topics/tmf-ontology-3gpp-sa5-ccsa-unified.md)
> 符号：✅ 已有规范输出 · 🔬 研究/起草中 · 🟡 有讨论或浅映射 · `-` 未涉及
> 每格附信心 [高/中/低] 与脚注。

## 矩阵

| 维度 | TM Forum | 3GPP SA5 | CCSA / 华为起草行标 | ETSI / ITU-T 参照 |
|:--|:--|:--|:--|:--|
| 概念/术语体系 | ✅ 区分 SID（信息框架）与 Ontology（TIO）；计划中的 Federated Ontology [1] [高]/[中] | 🟡 使用 Information model / NRM / Intent IOC；研究中出现 knowledge/semantic；Rel-20 工作区 §2.2.4 WT-4 计划调研 TMF 本体/RDF/KG [2] [高] | ✅ 「本体模型 / 实例化模型 / 知识图谱」写入 YD/T 7007 目录与解读 [3] [中] | ✅ M.3351 定义 knowledge / knowledge graph / ontology modelling [4] [高] |
| 建模语言与形式化程度 | ✅ TIO = RDF；SID = UML 2.5.1/XMI；SHACL 非 TMF 官方、有 Ericsson 开源 [5] [高] | ✅ UML IOC + OpenAPI YAML（28.312）；NRM UML [6] [高] | 🟡 目录未强制语言；二手解读推荐 OWL/XML/JSON + RDF 三元组 [7] [中] | ✅ M.3351 点名 RDF 与 OWL [4] [高] |
| 顶层概念/核心类 | ✅ TIO：意图管理功能/控制环/生命周期词汇；SID：ABE/域 [8] [高]；GB1093 联邦顶层类 **未见正文** [低] | ✅ Intent、IntentExpectation、ExpectationObject/Target/Context [6] [高]；知识架构核心类 **未见正文** [低] | 🟡 运营七类数据（配置/性能/告警/故障/规则/意图/运营）来自二手解读 [7] [中] | ✅ 故障 cause/phenomenon/resolution 作为本体建模示例 [4] [高] |
| 意图表达 | ✅ ICM TR290A/B + TMF921 API + TR294A 连 3GPP [9] [高] | ✅ TS 28.312；Annex C 映射 ICM；F.3 部署场景 [6] [高] | 🟡 7007 将意图列为建模对象之一，无 TIO IRI 对齐证据 [3] [低] | 🟡 ETSI ENI/ZSM 有意图管理，非本矩阵精读范围 |
| 数据与知识管理框架 | 🔬 TR311 Knowledge Manager 组件需求；TR326 Semantic Knowledge Fabric 标题级 [10] [中] | 🔬 TR 32.801-01：DMFW + Data and Knowledge Management KI [2] [高] | ✅ YD/T 7011 总体框架 + 7023 融合 + 7024 构建 [3] [高] | ✅ M.3351 六块功能框架；M.3351.2 九步构图 [4] [高] |
| 与数据编织语义层接口 | 🔬 TMF 称 Semantic Knowledge Fabric；与 IT Data Fabric 术语邻近但无 ZSM 029 级条款 [10] [中] | `-` 无 Data Fabric 条款；DMFW 是管理数据生命周期 [2] [高] | `-` 行标定位运营知识图谱，未写 Data Fabric [3] [中] | ✅ ETSI ZSM GS 029 是电信标准中明确引入 Fabric 的文件（既有卡片）[11] [高] |
| 治理与成熟度评估 | 🔬 TR329 标题为 Ontology Programme Governance；GB1025 是数据治理成熟度（既有）[12] [中]/[高] | 🟡 访问控制/用户同意在 DMFW WT 列表中，非本体治理 [2] [中] | 🟡 质量评估出现在 7024 构建过程，无成熟度等级模型 [3] [中] | 🟡 M.3351 含 validation / quality of raw data [4] [中] |
| 发布状态/公开性/主导 | TIO 公开 GA；SID 会员；GB1093/TR328/329 会员 Confluence。主导：AN + MODA [1][8] [高] | 28.312 公开；32.801-01 草稿，rapporteur **中兴** [2] [高] | 2026-06/07 已发布，全文付费。牵头：北邮/移动/电信/联通；华为与中兴起草 [3] [高] | M.3351 公开。ITU-T SG2 [4] [高] |

## 关键发现

1. **唯一完全公开、可机器执行的「本体」是 TMF TIO**，且范围限于意图，不是全网资源/数据面本体。
2. **3GPP 与 TMF 的正式桥梁只在意图层 Annex C**，三对元素，informative。
3. **国内行标已实施，国际联邦本体仍在 Confluence**——时间差对中兴意味着：国内按 YD/T 落地语义层，国际用 rapporteur 位影响 32.801-01 知识 KI。
4. **华为不是 CCSA 本体的唯一作者**；中兴同等出现在多份起草名单，并额外拥有 SA5 研究报告 rapporteur。

## 脚注

[1]: GB1093/TR328/TR329 标题来自 TM Forum Community 对 Confluence 的引用 → [tmf-ontology-3gpp-sa5-ccsa-unified](../../wiki/topics/tmf-ontology-3gpp-sa5-ccsa-unified.md) §1–2；归档 `research/raw/2026-09-20-tmf-gb1093/`
[2]: Portal 32.801-01 类型 TR；TOC 7.1 DMFW / 7.2 Knowledge；SA5 NWM v0.0.7 §2.2.4 WT-4 原文含 "ontologies defined in other fora (e.g. TM Forum)" — https://www.3gpp.org/ftp/Email_Discussions/SA5/SA5-level%20discussions/SA5%23161/SA5_NWM_Discussion_for_Rel-20_6G_OAM_Work_Areas-v0.0.7.pdf → 归档 `research/raw/2026-09-20-3gpp-sa5-6g-oam-study/`
[3]: YD/T 7007/7011/7023/7024/7129 目录页 → 归档 `research/raw/2026-09-20-ccsa-huawei-ontology-spec/`
[4]: ITU-T M.3351 / M.3351.2 → 归档 `research/raw/2026-09-20-itu-t-m3351/`
[5]: TR292 资源页；tio-shacl arXiv:2604.27359 → `research/raw/2026-09-20-tmf-intent-common-model/`
[6]: ETSI TS 128 312 V19.5.0 Annex C/F.3 → `research/raw/2026-09-20-3gpp-ts28312-intent/`
[7]: antpedia 对 YD/T 7007 的解读，非标准正文 → gaps
[8]: GB922 v25.0 目录；TR292 摘要 → SID/TIO 归档
[9]: TR294A 资源页；TS 28.312 参考文献 [18][20]
[10]: TR311 资源页；TR326 仅 Community 标题；TMF Inform 2026-07-01 knowledge planes
[11]: [data-fabric-for-ai-native-6g](../../wiki/topics/data-fabric-for-ai-native-6g.md) ZSM GS 029
[12]: TR329 标题；GB1025 见 [cross-domain-data-governance-6g](../../wiki/topics/cross-domain-data-governance-6g.md)
