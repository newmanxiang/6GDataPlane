# M2. 标准组织 × 议题矩阵

> 生成日期：2026-06-25
> 来源：wiki/topics/ 16 张主题卡片交叉分析

## 说明

- ✅ 已有正式标准/规范输出
- 🔬 研究/立项进行中（SI/WI/TR）
- 🟡 涉及讨论但非主要输出
- `-` 未明确涉及

## 矩阵

| 标准组织 | 6G 总愿景 | 数据面架构 | AI 原生网络 | 通感一体 (ISAC) | 数据治理 | 数据编织/Fabric | 用户面协议 |
|:--|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| **ITU-R** | ✅ [1] | 🟡 [2] | ✅ [3] | ✅ [4] | 🟡 [5] | - | - |
| **3GPP SA2** | 🔬 [6] | 🔬 [7] | 🔬 [8] | 🟡 [9] | 🔬 [10] | 🔬 [11] | 🟡 [12] |
| **3GPP SA5** | - | 🟡 [13] | 🔬 [14] | - | ✅ [15] | 🟡 [16] | - |
| **3GPP CT** | - | 🟡 [17] | - | - | - | - | ✅ [18] |
| **ETSI ISG ZSM** | - | 🟡 [19] | ✅ [20] | - | ✅ [21] | ✅ [22] | - |
| **ETSI ISG PDL** | - | - | - | - | ✅ [23] | - | - |
| **O-RAN Alliance** | 🟡 [24] | 🟡 [25] | ✅ [26] | - | 🟡 [27] | - | 🟡 [28] |
| **NGMN** | ✅ [29] | 🟡 [30] | 🔬 [31] | 🟡 [32] | 🔬 [33] | - | - |
| **TM Forum** | 🟡 [34] | - | 🟡 [35] | - | ✅ [36] | 🔬 [37] | - |
| **5G-IA / SNS JU** | 🔬 [38] | 🔬 [39] | 🔬 [40] | 🔬 [41] | 🔬 [42] | 🔬 [43] | - |
| **IEEE** | 🟡 [44] | 🔬 [45] | 🔬 [46] | 🔬 [47] | - | - | 🔬 [48] |

## 关键发现

1. **数据编织 (Data Fabric) 标准化仅 ETSI ZSM 有实质输出**：GS 029 是唯一明确将 Data Fabric 概念引入电信标准体系的文件[^zsm]
2. **3GPP SA2 vs SA5 职责交叉**：SA2 WT#5 的数据框架（KI#21）与 SA5 DMFW 存在范围重叠风险，运营商已提出关切[^wt5]
3. **AI 原生网络是最拥挤的赛道**：几乎所有组织都有相关工作项，但定义和范围差异大
4. **通感一体 (ISAC) 的数据治理缺口**：ITU-R 和 3GPP 都在推进 ISAC 场景，但感知数据的治理框架几乎空白[^gov]
5. **用户面协议标准化滞后**：GTP-U 替代方案的讨论分散在 3GPP CT、IETF（非本矩阵范围）和 O-RAN 之间

## 脚注

[1]: ITU-R M.2160 (IMT-2030 Framework) 定义 6G 总体愿景 → [imt-2030-framework-data-needs](../../wiki/topics/imt-2030-framework-data-needs.md)
[2]: ITU-R 框架中隐含数据面需求但未单独立项 → [imt-2030-framework-data-needs](../../wiki/topics/imt-2030-framework-data-needs.md)
[3]: ITU-R M.2160 将 AI 原生列为设计原则 → [imt-2030-framework-data-needs](../../wiki/topics/imt-2030-framework-data-needs.md)
[4]: ITU-R ISAC (Integrated Sensing and Communication) 作为 6G 场景 → [imt-2030-usage-scenarios-data-needs](../../wiki/topics/imt-2030-usage-scenarios-data-needs.md)
[5]: ITU-R 提及数据安全/隐私原则但无具体治理框架 → [imt-2030-framework-data-needs](../../wiki/topics/imt-2030-framework-data-needs.md)
[6]: 3GPP SA2 FS_6G_ARC Study Item（SP-241657）→ [3gpp-6g-timeline-rel22-23](../../wiki/topics/3gpp-6g-timeline-rel22-23.md)
[7]: SA2 WT#5 KI#21 6G Data Framework → [3gpp-sa2-6g-data-framework-wt5](../../wiki/topics/3gpp-sa2-6g-data-framework-wt5.md)
[8]: SA2 WT#3 AI-native 架构（KI#10-16）→ [3gpp-sa2-6g-data-framework-wt5](../../wiki/topics/3gpp-sa2-6g-data-framework-wt5.md)
[9]: SA2 ISAC 作为 6G 使用场景之一讨论 → [imt-2030-usage-scenarios-data-needs](../../wiki/topics/imt-2030-usage-scenarios-data-needs.md)
[10]: SA2 WT#5 数据治理功能（数据访问控制、质量管理）→ [3gpp-sa2-6g-data-framework-wt5](../../wiki/topics/3gpp-sa2-6g-data-framework-wt5.md)
[11]: SA2 WT#5 研究数据框架，含 Fabric 概念讨论 → [3gpp-sa2-6g-data-framework-wt5](../../wiki/topics/3gpp-sa2-6g-data-framework-wt5.md)
[12]: SA2 UPF 演进讨论（Rel-19 UPEAS）→ [3gpp-rel-19-20-data-architecture-status](../../wiki/topics/3gpp-rel-19-20-data-architecture-status.md)
[13]: SA5 数据分析管理涉及数据面管理维度 → [3gpp-rel-19-20-data-architecture-status](../../wiki/topics/3gpp-rel-19-20-data-architecture-status.md)
[14]: SA5 NWDAF 数据管理增强 → [3gpp-rel-19-20-data-architecture-status](../../wiki/topics/3gpp-rel-19-20-data-architecture-status.md)
[15]: SA5 DMFW (Data Management Framework) TS 28.104 → [3gpp-rel-19-20-data-architecture-status](../../wiki/topics/3gpp-rel-19-20-data-architecture-status.md)
[16]: SA5 DMFW 中的数据虚拟化概念初步讨论 → [3gpp-rel-19-20-data-architecture-status](../../wiki/topics/3gpp-rel-19-20-data-architecture-status.md)
[17]: CT 组协议实现涉及数据面优化 → [3gpp-rel-19-20-data-architecture-status](../../wiki/topics/3gpp-rel-19-20-data-architecture-status.md)
[18]: CT 负责 GTP-U 协议维护与演进 → [gtp-u-limitations-6g-alternatives](../../wiki/topics/gtp-u-limitations-6g-alternatives.md)
[19]: ZSM 闭环自动化涉及数据面观测 → [data-fabric-for-ai-native-6g](../../wiki/topics/data-fabric-for-ai-native-6g.md)
[20]: ZSM GS 009 AI/ML 闭环架构 → [ai-native-data-plane-status](../../wiki/topics/ai-native-data-plane-status.md)
[21]: ZSM GS 029 数据管理标准化 → [data-fabric-for-ai-native-6g](../../wiki/topics/data-fabric-for-ai-native-6g.md)
[22]: ZSM GS 029 明确引入 Data Fabric 概念 → [data-fabric-for-ai-native-6g](../../wiki/topics/data-fabric-for-ai-native-6g.md)
[23]: ETSI PDL GS 034 区块链治理审计跟踪 → [cross-domain-data-governance-6g](../../wiki/topics/cross-domain-data-governance-6g.md)
[24]: O-RAN Alliance 6G 愿景白皮书 → [ai-native-data-plane-status](../../wiki/topics/ai-native-data-plane-status.md)
[25]: O-RAN E3 接口与数据面功能扩展 → [ai-native-data-plane-status](../../wiki/topics/ai-native-data-plane-status.md)
[26]: O-RAN rApp/xApp/dApp AI 原生 RAN 智能 → [ai-native-data-plane-status](../../wiki/topics/ai-native-data-plane-status.md)
[27]: O-RAN 安全工作组数据访问策略 → [cross-domain-data-governance-6g](../../wiki/topics/cross-domain-data-governance-6g.md)
[28]: O-RAN 前传/中传接口协议（eCPRI 等） → [gtp-u-limitations-6g-alternatives](../../wiki/topics/gtp-u-limitations-6g-alternatives.md)
[29]: NGMN 6G 愿景白皮书（2025） → [6g-data-plane-architecture-2025](../../wiki/topics/6g-data-plane-architecture-2025.md)
[30]: NGMN 数据面架构建议 → [6g-data-plane-architecture-2025](../../wiki/topics/6g-data-plane-architecture-2025.md)
[31]: NGMN AI/ML 网络集成研究 → [ai-native-data-plane-status](../../wiki/topics/ai-native-data-plane-status.md)
[32]: NGMN 6G 场景中包含 ISAC → [imt-2030-usage-scenarios-data-needs](../../wiki/topics/imt-2030-usage-scenarios-data-needs.md)
[33]: NGMN 运营商数据策略讨论 → [cross-domain-data-governance-6g](../../wiki/topics/cross-domain-data-governance-6g.md)
[34]: TM Forum ODA/Open Digital Architecture → [data-fabric-in-telecom-early-cases](../../wiki/topics/data-fabric-in-telecom-early-cases.md)
[35]: TM Forum AI Catalyst 项目 → [data-fabric-in-telecom-early-cases](../../wiki/topics/data-fabric-in-telecom-early-cases.md)
[36]: TM Forum Data Governance Framework → [data-fabric-in-telecom-early-cases](../../wiki/topics/data-fabric-in-telecom-early-cases.md)
[37]: TM Forum Catalyst 项目中的数据编织探索 → [data-fabric-in-telecom-early-cases](../../wiki/topics/data-fabric-in-telecom-early-cases.md)
[38]: 5G-IA / SNS JU 6G 研究路线图 → [6g-data-plane-architecture-2025](../../wiki/topics/6g-data-plane-architecture-2025.md)
[39]: EU Hexa-X-II 数据面架构 → [6g-data-plane-architecture-2025](../../wiki/topics/6g-data-plane-architecture-2025.md)
[40]: RIGOUROUS / ROBUST-6G / PREDICT-6G AI 原生研究 → [data-fabric-for-ai-native-6g](../../wiki/topics/data-fabric-for-ai-native-6g.md)
[41]: EU 6G 项目中的 ISAC 研究 → [imt-2030-usage-scenarios-data-needs](../../wiki/topics/imt-2030-usage-scenarios-data-needs.md)
[42]: CANDIL 联邦治理研究 → [data-fabric-for-ai-native-6g](../../wiki/topics/data-fabric-for-ai-native-6g.md)
[43]: ROBUST-6G KG-in-Fabric、CANDIL 数据编织 → [data-fabric-for-ai-native-6g](../../wiki/topics/data-fabric-for-ai-native-6g.md)
[44]: IEEE 6G 技术愿景 → [6g-data-plane-architecture-2025](../../wiki/topics/6g-data-plane-architecture-2025.md)
[45]: IEEE 相关论文中的数据面研究 → [6g-data-plane-architecture-2025](../../wiki/topics/6g-data-plane-architecture-2025.md)
[46]: IEEE 发表的 AI-native 网络研究 → [ai-native-data-plane-status](../../wiki/topics/ai-native-data-plane-status.md)
[47]: IEEE ISAC 技术标准研究 → [imt-2030-usage-scenarios-data-needs](../../wiki/topics/imt-2030-usage-scenarios-data-needs.md)
[48]: IEEE Det-Net / TSN 确定性网络协议 → [gtp-u-limitations-6g-alternatives](../../wiki/topics/gtp-u-limitations-6g-alternatives.md)

[^zsm]: 参见 [data-fabric-for-ai-native-6g](../../wiki/topics/data-fabric-for-ai-native-6g.md) ETSI ZSM GS 029 详述
[^wt5]: 参见 [3gpp-sa2-6g-data-framework-wt5](../../wiki/topics/3gpp-sa2-6g-data-framework-wt5.md) SA2/SA5 职责重叠讨论
[^gov]: 参见 [cross-domain-data-governance-6g](../../wiki/topics/cross-domain-data-governance-6g.md) ISAC 治理空白分析
