# TM Forum Intent Ontology (TIO) 与 Intent Common Model

- 工具包：https://www.tmforum.org/toolkits/intent/
- TR292：https://www.tmforum.org/resources/introductory-guide/tr292-tm-forum-intent-ontology-tio-v3-6-0/
- 抓取日期：2026-09-20
- 核实状态：confirmed

## 已核实文档（Intent Toolkit 目录）

| 编号 | 标题 | 版本 | 日期 | 公开性 |
|---|---|---|---|---|
| IG1253 | Intent in Autonomous Networks | 1.3.0 | 2022-08-01 | 公开可下载 |
| TR292 | TM Forum Intent Ontology (TIO) | 3.6.0 | Team 2024-07-04；TMF Approved 2024-08-30 | 公开可下载 |
| TR292R | TIO References | 3.6.0 | 2024-07-04 / 2024-08-30 | 会员 |
| TR292A | Intent Management Elements | 3.6.0 production（检索见 3.5.0 归档页） | 2024-05–06 | 会员 |
| TR292B | Intent Management State Machines | 3.7.0 | 2025-11-21 | 会员 |
| TR292C | Function Definition Ontology | 3.6.0 | 2024-07-04 | 公开 |
| TR292D | Quantity Ontology | 3.6.0 | 2024-07-04 | 公开 |
| TR292E | Logical Operators | 3.6.0 | 2024-07-04 | 公开 |
| TR292F | Set Operators | 3.6.0 | 2024-07-04 | 公开 |
| TR292G | Metrics and Observations | 3.6.0 | 2024-07-04 | 公开 |
| TR292H | Mathematical Functions | 3.7.0 | 2025-11-21 | 会员 |
| TR292I | Security Ontology | 4.0.0 | 2026-03-27 | 会员 |
| TR290A | Intent Common Model – Intent Expression | 3.6.0（TS 28.312 引用） | 见 28.312 参考文献 | **公开**（Toolkit Available to all） |
| TR290B | Intent Common Model – Intent Reporting | 3.6.0 | 同上 | **公开** |
| TR290 | Intent Common Model（后续整本） | 3.8.0 | 2026-03-27 | 会员 |
| TR290V | Intent Common Model – Vocabulary Reference | 3.6.0 production | 旧版 3.0.0 于 2023-02 | 会员 |
| TR291 | Intent Extension Models | 系列 | 持续 | 会员 |
| TR294A | Model Connection to 3GPP TS 28.312 – Intent Extension Model | 1.0.0 | 2023-04-11 Team Approved | 公开目录页存在，下载需登录 |
| TR294B | Model Connection to 3GPP TS 28.541 | 1.0.0 | 2023-04-11 | 工具包列出 |
| TR299 | Intent Specification | 3.6.0 | 2024-07-04 | 公开 |
| TMF921 | Intent Management API | 工具包列出 | 持续 | Open API |
| IG1358 | Intent Based Operation User Guide | 1.2.0 | 2026-03-27 | 会员 |
| IG1421 | AI Agent MAS Intent-based Ontology Operation Service Management Model | 1.0.0 | 2025-05-16 | 预生产 |

## TR292 公开摘要（资源页原文）

Created By: Autonomous Networks Project。成熟度 GA。文档类型 Technical Report。IPR: RAND。

> Intent based operation is controlled by instances of intent management functions. Their interaction constitutes the intent control loop and intent life cycle management through the intent interface. This intent management ontology model introduces the categorization of functions and concepts of intent management. It provides basic vocabulary that can be used by other models, for example the intent common model and intent extension models.

## TR290V 公开摘要（旧版 3.0.0 页）

Intent common model 是 TIO 的一部分；Vocabulary Reference 按字母序列出命名空间内全部模型与意图规约语言元素，定义锚定在底层 RDF 标准与更广的 TIO。

## TR294A 公开摘要

AN 项目。Alpha。为一套面向 3GPP 的意图扩展模型之一，定义可用于为 radio network 与 radio service（radio network as a service）创建意图的 artifacts。

## 学术佐证（Ericsson Research，非 TMF 官方）

arXiv:2604.27359 TIO-SHACL（EricssonResearch/tio-shacl）：TIO v3.6.0 共 **15 个本体模块、规范性 RDF Turtle**；作者统计 87 classes / 109 properties / 72 functions。用于证明 TIO 的形式化载体是 RDF/OWL 族，而非 UML SID。
