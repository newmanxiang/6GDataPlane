# M1. 厂商 × 数据编织能力矩阵

> 生成日期：2026-06-25
> 来源：wiki/topics/ 16 张主题卡片交叉分析

## 说明

- ✅ 产品/方案已公开发布
- 🔬 研究阶段/白皮书/标准提案
- 🟡 部分能力/间接覆盖
- `-` 未公开/无相关信息

## 矩阵

| 厂商/供应商 | 主动元数据 (Active Metadata) | 知识图谱 (Knowledge Graph) | 数据虚拟化 (Data Virtualization) | 数据编排 (Data Orchestration) | 隐私保护 (Privacy) | AI 原生数据管理 (AI-Native DM) |
|:--|:--:|:--:|:--:|:--:|:--:|:--:|
| **华为 (Huawei)** | 🔬 [1] | 🔬 [2] | 🟡 [3] | ✅ [4] | 🔬 [5] | 🔬 [6] |
| **中兴 (ZTE)** | - | - | - | 🔬 [7] | - | 🔬 [8] |
| **爱立信 (Ericsson)** | 🟡 [9] | - | - | 🟡 [10] | 🔬 [11] | 🟡 [12] |
| **诺基亚 (Nokia)** | 🟡 [13] | 🔬 [14] | - | 🟡 [15] | 🔬 [16] | 🟡 [17] |
| **三星 (Samsung)** | - | - | - | 🔬 [18] | - | 🔬 [19] |
| **NTT DoCoMo** | - | - | - | 🔬 [20] | - | 🔬 [21] |
| **Qualcomm** | - | - | - | - | 🔬 [22] | 🔬 [23] |
| **Intel** | - | - | - | 🟡 [24] | 🟡 [25] | 🔬 [26] |
| **Cisco** | 🟡 [27] | - | - | ✅ [28] | 🟡 [29] | 🟡 [30] |
| **IBM** | ✅ [31] | ✅ [32] | ✅ [33] | ✅ [34] | ✅ [35] | ✅ [36] |
| **Informatica** | ✅ [37] | ✅ [38] | 🟡 [39] | ✅ [40] | ✅ [41] | ✅ [42] |
| **Denodo** | 🟡 [43] | - | ✅ [44] | ✅ [45] | 🟡 [46] | 🟡 [47] |

## 关键发现

1. **电信设备商的数据编织能力普遍不成熟**：华为在数据编排（DO/DA/DCP 体系）最完整[^arch]，但知识图谱、数据虚拟化等能力仍处研究阶段
2. **IT 数据编织供应商遥遥领先**：IBM（Watson Knowledge Catalog + Cloud Pak）、Informatica（IDMC CLAIRE）在全部 6 个维度均有产品级能力
3. **关键差距在"电信适配"**：IT 供应商缺乏亚毫秒延迟处理、3GPP 协议栈集成、NFV/CNF 原生部署能力[^fabric-6g]
4. **AI 原生数据管理是竞争焦点**：几乎所有厂商都有研究布局，但成熟度差异显著

## 脚注

[1]: 华为 DaaS 架构中的 DA (Data Agent) 元数据管理 → [data-fabric-for-ai-native-6g](../../wiki/topics/data-fabric-for-ai-native-6g.md)
[2]: 华为 IMT-2030 白皮书中的网络知识图谱概念 → [ai-native-data-plane-status](../../wiki/topics/ai-native-data-plane-status.md)
[3]: 华为 DaaS DCP 数据连接点支持多协议适配，具有虚拟化特征 → [daas-interface-design](../../wiki/topics/daas-interface-design.md)
[4]: 华为 DaaS DO (Data Orchestrator) 是完整的数据编排引擎 → [6g-data-plane-architecture-2025](../../wiki/topics/6g-data-plane-architecture-2025.md)
[5]: 华为 6G 研究中的联邦学习支持 → [cross-domain-data-governance-6g](../../wiki/topics/cross-domain-data-governance-6g.md)
[6]: 华为 DaaS 体系 + AI 原生数据面一体化设计 → [ai-native-data-plane-status](../../wiki/topics/ai-native-data-plane-status.md)
[7]: 中兴 SA2 6G 贡献：数据框架提案 → [3gpp-sa2-6g-data-framework-wt5](../../wiki/topics/3gpp-sa2-6g-data-framework-wt5.md)
[8]: 中兴 AI-RAN 研究，含 AI 原生网络白皮书 → [ai-native-data-plane-status](../../wiki/topics/ai-native-data-plane-status.md)
[9]: 爱立信 Network Intelligence 平台中的元数据管理 → [data-fabric-in-telecom-early-cases](../../wiki/topics/data-fabric-in-telecom-early-cases.md)
[10]: 爱立信 Intelligent Automation Platform → [user-plane-evolution-upf-to-6g](../../wiki/topics/user-plane-evolution-upf-to-6g.md)
[11]: 爱立信联邦学习研究（3GPP Rel-18 FL） → [cross-domain-data-governance-6g](../../wiki/topics/cross-domain-data-governance-6g.md)
[12]: 爱立信 Network Analytics (NWDAF) 增强 → [3gpp-rel-19-20-data-architecture-status](../../wiki/topics/3gpp-rel-19-20-data-architecture-status.md)
[13]: Nokia AVA 数据分析平台含元数据功能 → [data-fabric-in-telecom-early-cases](../../wiki/topics/data-fabric-in-telecom-early-cases.md)
[14]: Nokia Bell Labs 端到端语义层研究 / CANDIL 项目知识图谱 → [data-fabric-for-ai-native-6g](../../wiki/topics/data-fabric-for-ai-native-6g.md)
[15]: Nokia NetGuard 自动化引擎含数据编排 → [user-plane-evolution-upf-to-6g](../../wiki/topics/user-plane-evolution-upf-to-6g.md)
[16]: Nokia 隐私增强技术研究 → [cross-domain-data-governance-6g](../../wiki/topics/cross-domain-data-governance-6g.md)
[17]: Nokia NWDAF / MantaRay 网络分析 → [ai-native-data-plane-status](../../wiki/topics/ai-native-data-plane-status.md)
[18]: Samsung M-UP (Merged User Plane) 统一数据路径 → [gtp-u-limitations-6g-alternatives](../../wiki/topics/gtp-u-limitations-6g-alternatives.md)
[19]: Samsung 6G AI-native 架构白皮书 → [ai-native-data-plane-status](../../wiki/topics/ai-native-data-plane-status.md)
[20]: NTT DoCoMo IOWN 数据中心化架构 → [6g-data-plane-architecture-2025](../../wiki/topics/6g-data-plane-architecture-2025.md)
[21]: NTT DoCoMo AI-native 网络愿景 → [ai-native-data-plane-status](../../wiki/topics/ai-native-data-plane-status.md)
[22]: Qualcomm 设备端隐私计算（on-device FL） → [cross-domain-data-governance-6g](../../wiki/topics/cross-domain-data-governance-6g.md)
[23]: Qualcomm AI Engine 端侧推理 → [ai-native-data-plane-status](../../wiki/topics/ai-native-data-plane-status.md)
[24]: Intel Smart Edge 平台数据编排 → [user-plane-evolution-upf-to-6g](../../wiki/topics/user-plane-evolution-upf-to-6g.md)
[25]: Intel SGX/TDX 硬件隐私保护 → [cross-domain-data-governance-6g](../../wiki/topics/cross-domain-data-governance-6g.md)
[26]: Intel oneAPI 加速 AI 推理 → [ai-native-data-plane-status](../../wiki/topics/ai-native-data-plane-status.md)
[27]: Cisco DNA Center 元数据驱动自动化 → [data-fabric-in-telecom-early-cases](../../wiki/topics/data-fabric-in-telecom-early-cases.md)
[28]: Cisco Crosswork Network Automation 完整编排栈 → [user-plane-evolution-upf-to-6g](../../wiki/topics/user-plane-evolution-upf-to-6g.md)
[29]: Cisco Trustworthy Systems 安全框架 → [cross-domain-data-governance-6g](../../wiki/topics/cross-domain-data-governance-6g.md)
[30]: Cisco Silicon One + AI 网络分析 → [ai-native-data-plane-status](../../wiki/topics/ai-native-data-plane-status.md)
[31]: IBM Watson Knowledge Catalog 主动元数据引擎 → [data-fabric-definition-and-capabilities](../../wiki/topics/data-fabric-definition-and-capabilities.md)
[32]: IBM Knowledge Graph / Cloud Pak for Data → [data-fabric-definition-and-capabilities](../../wiki/topics/data-fabric-definition-and-capabilities.md)
[33]: IBM Cloud Pak for Data 数据虚拟化模块 → [data-fabric-definition-and-capabilities](../../wiki/topics/data-fabric-definition-and-capabilities.md)
[34]: IBM DataStage / DataOps 编排 → [data-fabric-definition-and-capabilities](../../wiki/topics/data-fabric-definition-and-capabilities.md)
[35]: IBM Guardium 数据隐私保护 → [data-fabric-definition-and-capabilities](../../wiki/topics/data-fabric-definition-and-capabilities.md)
[36]: IBM watsonx.data AI 原生数据管理 → [data-fabric-definition-and-capabilities](../../wiki/topics/data-fabric-definition-and-capabilities.md)
[37]: Informatica CLAIRE AI 元数据引擎 → [data-fabric-definition-and-capabilities](../../wiki/topics/data-fabric-definition-and-capabilities.md)
[38]: Informatica Enterprise Data Catalog 知识图谱 → [data-fabric-definition-and-capabilities](../../wiki/topics/data-fabric-definition-and-capabilities.md)
[39]: Informatica 通过 API/连接器实现虚拟化访问 → [data-fabric-definition-and-capabilities](../../wiki/topics/data-fabric-definition-and-capabilities.md)
[40]: Informatica IDMC 编排引擎 → [data-fabric-definition-and-capabilities](../../wiki/topics/data-fabric-definition-and-capabilities.md)
[41]: Informatica Data Privacy Management → [data-fabric-definition-and-capabilities](../../wiki/topics/data-fabric-definition-and-capabilities.md)
[42]: Informatica CLAIRE GPT AI 增强数据管理 → [data-fabric-definition-and-capabilities](../../wiki/topics/data-fabric-definition-and-capabilities.md)
[43]: Denodo 元数据发现与管理（辅助能力） → [data-fabric-definition-and-capabilities](../../wiki/topics/data-fabric-definition-and-capabilities.md)
[44]: Denodo 数据虚拟化市场领导者 → [data-fabric-definition-and-capabilities](../../wiki/topics/data-fabric-definition-and-capabilities.md), [data-fabric-in-telecom-early-cases](../../wiki/topics/data-fabric-in-telecom-early-cases.md)
[45]: Denodo 联邦查询编排 → [data-fabric-definition-and-capabilities](../../wiki/topics/data-fabric-definition-and-capabilities.md)
[46]: Denodo 行级/列级安全策略 → [data-fabric-definition-and-capabilities](../../wiki/topics/data-fabric-definition-and-capabilities.md)
[47]: Denodo AI/ML 集成增强分析 → [data-fabric-definition-and-capabilities](../../wiki/topics/data-fabric-definition-and-capabilities.md)

[^arch]: 参见 [6g-data-plane-architecture-2025](../../wiki/topics/6g-data-plane-architecture-2025.md) 华为 DaaS 三层架构
[^fabric-6g]: 参见 [data-fabric-for-ai-native-6g](../../wiki/topics/data-fabric-for-ai-native-6g.md) 企业 IT vs 电信适配差距分析
