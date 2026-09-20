# 3GPP TS 28.312 / ETSI TS 128 312 V19.5.0 — Intent driven management services

- 全文（ETSI 镜像）：https://etsi.org/deliver/etsi_ts/128300_128399/128312/19.05.00_60/ts_128312v190500p.pdf
- 抓取日期：2026-09-20
- 核实状态：confirmed（全文可读）

## 范围与模型性质

TS 28.312 定义移动网意图驱动管理服务。意图信息模型是 **UML IOC**（Intent、IntentExpectation、ExpectationObject、ExpectationTarget、Context、IntentReport），解决方案集为 OpenAPI/YAML（`TS28312_IntentExpectations.yaml`），不是 RDF/OWL 本体。

核心类：

- Intent 含 1..* IntentExpectation
- IntentExpectation：expectationVerb（DELIVER / ENSURE / MAINTAIN）、expectationObject、expectationTargets、expectationContexts、preferenceWeight
- 场景专用期望：Radio Network、Radio Service、5GC Network、Edge Service Support、E2E Resource Optimization、Network Maintenance 等

## 与 TMF 的正式关系

### 规范性引用（References）

- [7] TM Forum IG1253A Intent Common Model v1.1.0（旧编号，仍被引用）
- [18] TM Forum TR290B Intent Common Model – Intent Reporting v3.6.0
- [20] TM Forum TR290A Intent Common Model – Intent Expression v3.6.0

### Annex C（informative）映射

3GPP IntentExpectation ↔ TMF ICM IntentExpression（TR290A）：

| 3GPP | TMF ICM |
|---|---|
| expectationObject | icm:target |
| expectationTargets | properties of icm:Expectation class instance |
| expectationContexts | icm:context |

3GPP IntentReport ↔ TMF ICM IntentReport（TR290B）：intentFulfilmentReport 等映射到 icm:ExpectationReport 属性；内容由 icm:ReportingExpectation 子类决定。

### Annex F.3 部署场景 #2

- 3GPP 意图 MnS：Intent-NOP（NOP–NEP）、Intent-CSP（CSP–NOP）
- TMF Intent Management API：Intent-CSC（CSC–CSP）
- CSC↔CSP 的 TMF API 与 CSP↔NOP 的 3GPP MnS 之间用 Annex C 映射做转换

结论：**正式对齐存在，但是信息模型（UML）↔ 本体（RDF）的桥接，而非 3GPP 采纳 TIO。** 映射表仅三对元素，粒度粗，Annex 为 informative。
