# TM Forum Intent Ontology（TIO）与 AN 意图工具包归档

## TR292 v3.6.0

- Created By: Autonomous Networks Project
- Status: TM Forum Approved / Production / GA
- Team approved: 2024-07-04；TM Forum Approved: 2024-08-30
- 公开摘要：

> Intent based operation is controlled by instances of intent management functions. Their interaction constitutes the intent control loop and intent life cycle management through the intent interface. This intent management ontology model introduces the categorization of functions and concepts of intent management. It provides basic vocabulary that can be used by other models, for example the intent common model and intent extension models.

## Intent Toolkit 资产表（2026-09-20 页面）

公开可下载（Available to all，仍需登录）的核心本体模块：

| 资产 | 版本 | Team Approved |
|---|---|---|
| TR292 TIO | 3.6.0 | 2024-07-04 |
| TR292A Intent Management Elements | 3.6.0 | 2024-07-04 |
| TR292C Function Definition Ontology | 3.6.0 | 2024-07-04 |
| TR292D Quantity Ontology | 3.6.0 | 2024-07-04 |
| TR292E Logical Operators | 3.6.0 | 2024-07-04 |
| TR292F Set Operators | 3.6.0 | 2024-07-04 |
| TR292G Metrics and Observations | 3.6.0 | 2024-07-04 |
| TR292R TIO References | 3.6.0 | 2024-07-04 |
| TR290A Intent Expression | 3.6.0 | 2024-07-04 |
| TR294A Model Connection to 3GPP TS 28.312 | 1.0.0 | 2023-04-11 |
| TR294B Model Connection to 3GPP TS 28.541 | 1.0.0 | 2023-04-11 |

会员件（更新更快）：

| 资产 | 版本 | Team Approved |
|---|---|---|
| TR290 Intent Common Model | 3.8.0 | 2026-03-27 |
| TR292B State Machines | 3.7.0 | 2025-11-21 |
| TR292H Mathematical Functions | 3.7.0 | 2025-11-21 |
| TR292I Security Ontology | 4.0.0 | 2026-03-27 |
| TR291A Intent Validity | 3.7.0 | 2026-03-27 |
| TR291I Utility | 3.7.0 | 2025-11-21 |
| IG1358 Intent Based Operation User Guide | 1.2.0 | 2026-03-27 |

## Turtle 文件可达性（engage.tmforum.org，Jörg 等）

- 规范文档引用 IRI：`http://tio.models.tmforum.org/tio/v3.6.0/IntentCommonModel/` 等 **并不解析为 RDF**。
- 团队已同意改为 `models.tmforum.org/tio`，已发布文档尚未全部改完。
- 实际 TTL 暂放 AN Project Confluence：`Turtle Files Collection TIO v3.6.0`。
- TIO 4 计划把 turtle 作为规范附录。
- TMF921 一致性要求：Expression 相对 TIO RDF 校验，序列化 JSON-LD / Turtle / XML / YAML-LD；JsonLdExpression 强制。

## TMF921 GitHub mirror

https://github.com/tmforum-apis/TMF921_Intent （2025-10-03 创建，Apache 2.0）

> The expression attribute of Intent contains a statement of the expectations for an intent in a particular ontology language and is validated by the TM Forum Intent Ontology (TIO).

## SID / MODA（对照：不是 OWL）

- GB922 Information Framework Models Suite v25.0（2025-07-18）
- MODA HTML/Sparx v25.5 Team Approved 2026-01-23
- 公开 GitHub：https://github.com/tmforum-rand/MODA （XMI zip，非 OWL）

## IG1421（2025-05-16 Team Approved，Alpha / Pre-production）

Created By: Technical Architecture & Components Project

> Defines a structured AI Agent MAS taxonomy and ontology using TMFIG1253 defined intent-based management functions (IMF).
