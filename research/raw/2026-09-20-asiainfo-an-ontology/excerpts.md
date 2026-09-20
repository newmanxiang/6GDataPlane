# 关键摘录：AsiaInfo AN-Ontology

## 项目目的（README）

> 自智网络本体项目旨在为自智网络（Autonomous Network, AN）领域构建统一的语义知识基础……支撑智能体系统实现更准确的网络语境理解和决策推理。

应用场景原文：

- 作为 AN Agent 架构中的长期记忆组件
- 为世界模型提供结构化的专业知识
- 支持智能体间的语义一致性通信

## 5GC Ontology IRI

```turtle
<http://www.asiainfo.com/ontology/5gc#> rdf:type owl:Ontology ;
    owl:versionInfo "1.0.0" ;
    dcterms:created "2025-10-11"^^xsd:date ;
    rdfs:comment "本体基于3GPP 5G核心网标准设计，提供标准化的概念模型和语义描述"@zh-CN .
```

## 接口枚举拼写（TTL 原文）

```turtle
5gc:InfterfaceN2 rdf:type owl:NamedIndividual , 5gc:InterfaceType .
```

## 家客资源本体自述

> 基于家客场景网络资源模型构建的完整Ontology，按类型划分实体后重新组织，覆盖所有实体及关联
