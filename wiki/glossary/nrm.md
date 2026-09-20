---
term_zh: 网络资源模型
term_en: Network Resource Model
abbr: NRM
slug: nrm
category: term
sources:
  - title: 3GPP SA5 28 series NRM
    url: https://www.3gpp.org/ftp/Specs/archive/28_series/
related:
  - dmfw
  - sid
  - intent-common-model
tags: [NRM, SA5, UML]
---

# 网络资源模型（Network Resource Model，NRM）

**一句话定义**：3GPP SA5 用 UML 定义的管理对象类及其关系（通用 NRM TS 28.622/28.623，5G NRM TS 28.541），是管理服务操作的对象树，不是 RDF 本体。

**来源**：3GPP 28 series；归档 research/raw/2026-09-20-3gpp-sa5-nrm-model-repertoire/

**相关概念**：
- [sid] CSP 业务信息模型 vs 网络管理对象模型
- [intent-common-model] TS 28.312 的 expectationObject 常指向 NRM 对象类型
- [dmfw] 6G 管理数据框架研究

**易混淆点**：
- NRM ≠ 知识图谱本体：NRM 服务配置/性能/告警 IRP，不定义故障传播语义

**首次出现于本工程**：2026-09-20，wiki/topics/tmf-ontology-3gpp-sa5-ccsa-unified.md
