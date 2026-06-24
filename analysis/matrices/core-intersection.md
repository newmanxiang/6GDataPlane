# M3. 数据编织能力 × 6G 场景矩阵（核心交集 ⭐）

> 生成日期：2026-06-25
> 来源：wiki/topics/ 16 张主题卡片交叉分析
> **这是本项目的核心分析矩阵**——映射数据编织 (Data Fabric) 每项能力在 6G 四大场景中的适用性与成熟度。

## 说明

每格包含：适用性描述 + 成熟度标签 + 来源链接。成熟度标签：
- 🟢 有实证/原型验证
- 🟡 有理论/方案设计
- 🔴 研究空白

## 矩阵

### 主动元数据 (Active Metadata)

| 6G 场景 | 适用性描述 | 成熟度 | 来源 |
|:--|:--|:--:|:--|
| **核心网（DaaS/NWDAF/UPF）** | DaaS DA (Data Agent) 承担元数据管理职责，跟踪数据血缘、质量和生命周期。NWDAF Rel-19 增加元数据驱动的分析协调（DCCF 路由）。主动元数据可实现数据资产自动发现与服务注册。 | 🟡 | [6g-data-plane-architecture-2025][^a1], [3gpp-rel-19-20-data-architecture-status][^a2] |
| **RAN（O-RAN RIC/dApp）** | dApp E3 接口需要实时元数据标注（数据源、采样率、时效性）。O-RAN R1 接口元数据标准化尚不充分。RAN 数据的时间序列特征要求亚秒级元数据更新。 | 🔴 | [ai-native-data-plane-status][^a3] |
| **边缘（MEC）** | 边缘节点动态部署导致元数据拓扑频繁变化。Google TDF 的元数据发现机制可作参考，但 Private Preview 状态限制验证。元数据联邦同步是关键挑战。 | 🟡 | [data-fabric-in-telecom-early-cases][^a4] |
| **终端/NTN** | vivo DSAP 协议栈在终端侧引入数据层，但元数据管理能力极其有限。NTN 高延迟环境下元数据同步成本高。**研究空白：终端侧轻量元数据方案。** | 🔴 | [daas-interface-design][^a5] |

### 知识图谱 (Knowledge Graph)

| 6G 场景 | 适用性描述 | 成熟度 | 来源 |
|:--|:--|:--:|:--|
| **核心网（DaaS/NWDAF/UPF）** | 华为 DaaS 设计中知识图谱用于网络拓扑建模和数据关系发现。CANDIL 项目使用 NGSI-LD 联邦知识图谱实现跨域数据语义统一。 | 🟡 | [data-fabric-for-ai-native-6g][^b1] |
| **RAN（O-RAN RIC/dApp）** | ROBUST-6G 提出 KG-in-Fabric 方案在 RAN 域使用知识图谱进行资源关系建模。Nokia Bell Labs 端到端语义层概念涵盖 RAN 数据。 | 🟡 | [data-fabric-for-ai-native-6g][^b2] |
| **边缘（MEC）** | 边缘知识图谱用于本地化服务发现和数据源关联。Vodafone Italy Nucleus 平台含知识图谱模块。 | 🟢 | [data-fabric-in-telecom-early-cases][^b3] |
| **终端/NTN** | **研究空白：**无已知的终端侧知识图谱轻量化方案。NTN 场景下知识图谱分片与同步机制缺失。 | 🔴 | [cross-domain-data-governance-6g][^b4] |

### 数据虚拟化 (Data Virtualization)

| 6G 场景 | 适用性描述 | 成熟度 | 来源 |
|:--|:--|:--:|:--|
| **核心网（DaaS/NWDAF/UPF）** | DaaS DCP (Data Connection Point) 本质上是数据虚拟化层——提供统一数据访问接口而不移动原始数据。Denodo 在电信核心网已有部署案例（LG U+ Nudge-B）。 | 🟢 | [daas-interface-design][^c1], [data-fabric-in-telecom-early-cases][^c2] |
| **RAN（O-RAN RIC/dApp）** | RAN 数据的高吞吐量（10 Gbps+）和低延迟（<1 ms）要求对传统数据虚拟化是根本性挑战。需要专用的流式虚拟化机制。**关键差距。** | 🔴 | [data-fabric-for-ai-native-6g][^c3] |
| **边缘（MEC）** | 边缘数据虚拟化可减少回传带宽消耗。DT ODE 实现了 22× 性能提升的数据虚拟化层。延迟影响待量化。 | 🟢 | [data-fabric-in-telecom-early-cases][^c4] |
| **终端/NTN** | 终端计算资源限制使完整数据虚拟化不可行。NTN 场景仅适合轻量级数据代理（Proxy）模式。 | 🔴 | [6g-kpi-20-requirements][^c5] |

### 数据编排自动化 (Data Orchestration)

| 6G 场景 | 适用性描述 | 成熟度 | 来源 |
|:--|:--|:--:|:--|
| **核心网（DaaS/NWDAF/UPF）** | 华为 DO (Data Orchestrator) 是最完整的电信数据编排提案——支持 Pub/Sub、Req/Res、Streaming 三种模式。NWDAF DCCF 也承担部分编排职能。3GPP WT#5 正在标准化。 | 🟡 | [6g-data-plane-architecture-2025][^d1], [3gpp-sa2-6g-data-framework-wt5][^d2] |
| **RAN（O-RAN RIC/dApp）** | O-RAN SMO 平台的数据编排。Non-RT RIC → Near-RT RIC → dApp 的三级数据流编排。E3 接口定义正在推进。 | 🟡 | [ai-native-data-plane-status][^d3] |
| **边缘（MEC）** | 边缘数据编排需处理动态计算资源分配。NVIDIA dUPF 展示了 100 Gbps 吞吐下的数据管道编排能力。 | 🟢 | [user-plane-evolution-upf-to-6g][^d4] |
| **终端/NTN** | 终端数据编排限于本地缓存和预取策略。NTN 不确定延迟下的编排容错机制是开放问题。 | 🔴 | [6g-kpi-20-requirements][^d5] |

### 联邦学习 / 隐私 (Federated Learning / Privacy)

| 6G 场景 | 适用性描述 | 成熟度 | 来源 |
|:--|:--|:--:|:--|
| **核心网（DaaS/NWDAF/UPF）** | 3GPP Rel-18/19 HFL (Horizontal FL) 和 VFL (Vertical FL) 已标准化到 NWDAF。联邦计算作为数据不出域的核心手段。 | 🟢 | [cross-domain-data-governance-6g][^e1] |
| **RAN（O-RAN RIC/dApp）** | RAN 域联邦学习用于干扰管理、波束预测。AI-RAN Alliance 推动联邦 AI 训练。数据异构性（non-IID）是 RAN FL 的主要挑战。 | 🟡 | [ai-native-data-plane-status][^e2] |
| **边缘（MEC）** | 边缘 FL 聚合器是自然架构选择。差分隐私 + FL 组合。Fraunhofer Telco Data Space 试点。 | 🟡 | [cross-domain-data-governance-6g][^e3] |
| **终端/NTN** | Qualcomm 设备端 FL 已有 AI Engine 支持。终端隐私计算受电池和算力制约。ISAC 感知数据的终端隐私保护是新增需求。 | 🟡 | [cross-domain-data-governance-6g][^e4] |

### 语义互操作 (Semantic Interoperability)

| 6G 场景 | 适用性描述 | 成熟度 | 来源 |
|:--|:--|:--:|:--|
| **核心网（DaaS/NWDAF/UPF）** | 6G 统一语义模型是 SA2 WT#5 讨论主题之一。DaaS 数据模型需要跨 NF 语义一致性。现有 3GPP 数据模型碎片化严重（SA2/SA5/CT 各有数据模型）。 | 🟡 | [3gpp-sa2-6g-data-framework-wt5][^f1] |
| **RAN（O-RAN RIC/dApp）** | O-RAN 与 3GPP 数据模型不兼容。CANDIL NGSI-LD 试图建立跨域语义桥梁。RAN-Core 语义翻译层是必要组件。 | 🟡 | [data-fabric-for-ai-native-6g][^f2] |
| **边缘（MEC）** | 边缘多标准共存（ETSI MEC / 3GPP / O-RAN）需要语义中间层。TM Forum ODA 数据模型可作为参考。 | 🟡 | [data-fabric-in-telecom-early-cases][^f3] |
| **终端/NTN** | **研究空白：**终端数据语义标准不存在。UE 与网络间的语义协商机制未被研究。NTN 多制式（LEO/GEO/HAPS）语义差异。 | 🔴 | [imt-2030-usage-scenarios-data-needs][^f4] |

## 综合热力图

```
               核心网    RAN      边缘     终端/NTN
主动元数据      🟡       🔴       🟡        🔴
知识图谱        🟡       🟡       🟢        🔴
数据虚拟化      🟢       🔴       🟢        🔴
数据编排        🟡       🟡       🟢        🔴
联邦学习/隐私   🟢       🟡       🟡        🟡
语义互操作      🟡       🟡       🟡        🔴
```

## 关键洞察

1. **终端/NTN 是全面空白区**：6 项数据编织能力中 4 项为🔴（研究空白），终端侧数据管理完全缺位
2. **边缘场景成熟度最高**：3 项🟢（已有原型验证），得益于 MEC 领域的产业试点（DT ODE、Vodafone Nucleus、NVIDIA dUPF）
3. **RAN 域的性能鸿沟**：数据虚拟化和主动元数据在 RAN 场景面临根本性的延迟/吞吐量挑战
4. **核心网标准化是瓶颈**：多数能力处于🟡（方案设计阶段），等待 3GPP SA2 WT#5 结论
5. **联邦学习/隐私最均衡**：四个场景均有一定进展，受益于 3GPP Rel-18/19 FL 标准化的拉动

## 脚注

[^a1]: [6g-data-plane-architecture-2025](../../wiki/topics/6g-data-plane-architecture-2025.md) — DaaS DA 元数据管理
[^a2]: [3gpp-rel-19-20-data-architecture-status](../../wiki/topics/3gpp-rel-19-20-data-architecture-status.md) — NWDAF/DCCF Rel-19 增强
[^a3]: [ai-native-data-plane-status](../../wiki/topics/ai-native-data-plane-status.md) — O-RAN dApp E3 接口
[^a4]: [data-fabric-in-telecom-early-cases](../../wiki/topics/data-fabric-in-telecom-early-cases.md) — Google TDF Private Preview
[^a5]: [daas-interface-design](../../wiki/topics/daas-interface-design.md) — vivo DSAP 协议栈
[^b1]: [data-fabric-for-ai-native-6g](../../wiki/topics/data-fabric-for-ai-native-6g.md) — CANDIL NGSI-LD 知识图谱
[^b2]: [data-fabric-for-ai-native-6g](../../wiki/topics/data-fabric-for-ai-native-6g.md) — ROBUST-6G KG-in-Fabric
[^b3]: [data-fabric-in-telecom-early-cases](../../wiki/topics/data-fabric-in-telecom-early-cases.md) — Vodafone Nucleus
[^b4]: [cross-domain-data-governance-6g](../../wiki/topics/cross-domain-data-governance-6g.md) — 终端侧治理空白
[^c1]: [daas-interface-design](../../wiki/topics/daas-interface-design.md) — DaaS DCP 数据虚拟化层
[^c2]: [data-fabric-in-telecom-early-cases](../../wiki/topics/data-fabric-in-telecom-early-cases.md) — LG U+ Nudge-B / Denodo
[^c3]: [data-fabric-for-ai-native-6g](../../wiki/topics/data-fabric-for-ai-native-6g.md) — RAN 实时数据性能挑战
[^c4]: [data-fabric-in-telecom-early-cases](../../wiki/topics/data-fabric-in-telecom-early-cases.md) — DT ODE 22× 提升
[^c5]: [6g-kpi-20-requirements](../../wiki/topics/6g-kpi-20-requirements.md) — 终端计算约束
[^d1]: [6g-data-plane-architecture-2025](../../wiki/topics/6g-data-plane-architecture-2025.md) — 华为 DO 编排引擎
[^d2]: [3gpp-sa2-6g-data-framework-wt5](../../wiki/topics/3gpp-sa2-6g-data-framework-wt5.md) — WT#5 数据编排标准化
[^d3]: [ai-native-data-plane-status](../../wiki/topics/ai-native-data-plane-status.md) — O-RAN 三级编排
[^d4]: [user-plane-evolution-upf-to-6g](../../wiki/topics/user-plane-evolution-upf-to-6g.md) — NVIDIA dUPF 100Gbps
[^d5]: [6g-kpi-20-requirements](../../wiki/topics/6g-kpi-20-requirements.md) — NTN 延迟不确定性
[^e1]: [cross-domain-data-governance-6g](../../wiki/topics/cross-domain-data-governance-6g.md) — 3GPP FL 标准化
[^e2]: [ai-native-data-plane-status](../../wiki/topics/ai-native-data-plane-status.md) — AI-RAN Alliance FL
[^e3]: [cross-domain-data-governance-6g](../../wiki/topics/cross-domain-data-governance-6g.md) — Telco Data Space
[^e4]: [cross-domain-data-governance-6g](../../wiki/topics/cross-domain-data-governance-6g.md) — 终端隐私计算
[^f1]: [3gpp-sa2-6g-data-framework-wt5](../../wiki/topics/3gpp-sa2-6g-data-framework-wt5.md) — 语义模型讨论
[^f2]: [data-fabric-for-ai-native-6g](../../wiki/topics/data-fabric-for-ai-native-6g.md) — NGSI-LD 语义桥
[^f3]: [data-fabric-in-telecom-early-cases](../../wiki/topics/data-fabric-in-telecom-early-cases.md) — TM Forum ODA
[^f4]: [imt-2030-usage-scenarios-data-needs](../../wiki/topics/imt-2030-usage-scenarios-data-needs.md) — NTN 多制式差异
