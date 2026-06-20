---
term: Federated Learning
abbr: FL
cn: 联邦学习
slug: federated-learning
category: glossary
related:
  - privacy-preserving-data-fabric
  - network-data-analytics
  - data-fabric-for-ai-native-6g
source: https://cacm.acm.org/research/belt-and-braces-when-federated-learning-meets-differential-privacy/
---

# Federated Learning

> 一种分布式机器学习范式，允许多方在不共享原始数据的前提下协作训练共享模型。

**中文**：联邦学习
**英文**：Federated Learning
**缩写**：FL

## 定义
联邦学习由 Google 于 2016 年提出，核心思想是"数据不动模型动"——各参与方在本地数据上训练模型，仅将模型更新（梯度或参数）上传至聚合服务器，由服务器融合后下发全局模型。这一过程迭代进行直至收敛。FL 广泛应用于隐私敏感场景（医疗、金融、电信），3GPP 在 NWDAF Rel-18 中正式引入 FL 用于网络分析模型的跨域协作训练。在数据编织架构中，FL 是实现"数据可用不可见"的核心使能技术。

## 相关概念
- [[privacy-preserving-data-fabric]] 联邦学习是隐私保护数据编织的核心技术组件
- [[network-data-analytics]] NWDAF Rel-18 引入 FL 支持跨运营商/跨域网络模型训练
- [[data-fabric-for-ai-native-6g]] AI 原生 6G 的分布式训练场景高度依赖 FL
