---
term_zh: 意图通用模型
term_en: Intent Common Model
abbr: ICM
slug: intent-common-model
category: term
sources:
  - title: TR292 TM Forum Intent Ontology (TIO) v3.6.0
    url: https://www.tmforum.org/resources/introductory-guide/tr292-tm-forum-intent-ontology-tio-v3-6-0/
  - title: 3GPP TS 28.312 V19.5.0 Annex C
    url: https://etsi.org/deliver/etsi_ts/128300_128399/128312/19.05.00_60/ts_128312v190500p.pdf
related:
  - ontology
  - telecom-network-ontology
  - dmfw
  - tm-forum
tags: [intent, TIO, TR290, TS28312]
---

# 意图通用模型（Intent Common Model，ICM）

**一句话定义**：TM Forum Intent Ontology 中用于表达意图与意图报告的核心 RDF 模型，规范编号为 TR290A（Expression）与 TR290B（Reporting）；3GPP TS 28.312 Annex C 将其与 UML IntentExpectation 做 informative 映射。

**来源**：[TR292](https://www.tmforum.org/resources/introductory-guide/tr292-tm-forum-intent-ontology-tio-v3-6-0/)；[TS 28.312 Annex C](https://etsi.org/deliver/etsi_ts/128300_128399/128312/19.05.00_60/ts_128312v190500p.pdf)

**相关概念**：
- [ontology]
- [telecom-network-ontology]
- TMF921 Intent Management API（意图接口，不是本体本身）

**易混淆点**：
- ICM ≠ 3GPP Intent IOC：后者是 TS 28.312 的 UML 类（Intent/IntentExpectation），YAML/OpenAPI 编码
- IG1253A 是 ICM 的旧编号，TS 28.312 参考文献仍同时引用 IG1253A 与 TR290A/B v3.6.0

**首次出现于本工程**：2026-09-20，wiki/topics/tmf-ontology-3gpp-sa5-ccsa-unified.md
