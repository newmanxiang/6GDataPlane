---
term: Differential Privacy
abbr: DP
cn: 差分隐私
slug: differential-privacy
category: glossary
related:
  - privacy-preserving-data-fabric
  - federated-learning
  - data-fabric-capabilities
source: https://cacm.acm.org/research/belt-and-braces-when-federated-learning-meets-differential-privacy/
---

# Differential Privacy

> 一种形式化的隐私保护框架，通过向查询结果中添加可控噪声，确保单条记录的存在与否不会显著影响输出结果。

**中文**：差分隐私
**英文**：Differential Privacy
**缩写**：DP

## 定义
差分隐私由 Cynthia Dwork 于 2006 年提出，提供可数学证明的隐私保证。其核心参数 ε（epsilon）量化隐私保护强度——ε 越小隐私保护越强，但数据可用性越低。在数据编织场景中，DP 可应用于数据虚拟化查询层，使跨域数据聚合结果满足隐私合规要求而无需暴露个体记录。与联邦学习结合时，DP 可防止通过梯度反推原始数据的攻击。Apple、Google 等已在产品级系统中部署 DP。

## 相关概念
- [[privacy-preserving-data-fabric]] 差分隐私是隐私保护数据编织的查询层核心技术
- [[federated-learning]] DP 与 FL 结合提供端到端的隐私保证
- [[data-fabric-capabilities]] DP 扩展了数据编织"治理"能力域
