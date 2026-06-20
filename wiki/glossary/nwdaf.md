---
term: Network Data Analytics Function
abbr: NWDAF
cn: 网络数据分析功能
slug: nwdaf
category: glossary
related:
  - network-data-analytics
  - 6g-data-plane
  - ran-architecture-evolution
source: https://www.3gpp.org/technologies/nae-5gs-ct3
---

# NWDAF — Network Data Analytics Function

> 3GPP 定义的 5G 核心网网络功能，负责采集与分析网络数据以支持自动化决策。

**中文**：网络数据分析功能
**英文**：Network Data Analytics Function
**缩写**：NWDAF

## 定义
NWDAF 是 3GPP 在 5G 系统架构规范（TS 23.288）中定义的网络功能（NF），从 Rel-15 引入概念，Rel-16 具备基础分析能力，Rel-17 实现 MTLF（模型训练逻辑功能）与 AnLF（分析逻辑功能）的功能分离并支持 ML 推理，Rel-18 增加联邦学习等增强。NWDAF 通过服务化接口（Nnwdaf）采集 AMF、SMF、UPF 等网络功能的数据，输出异常检测、负载预测、QoS 评估等标准化分析结果，驱动网络自动化闭环。

## 相关概念
- [[network-data-analytics]] NWDAF 的完整概念卡片，含 6G 演进方向
- [[6g-data-plane]] NWDAF 是数据面数据的核心消费者与分析引擎
- [[ran-architecture-evolution]] NWDAF 与 O-RAN RIC 的分析能力互补
