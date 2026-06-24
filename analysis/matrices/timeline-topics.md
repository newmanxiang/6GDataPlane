# M4. 时间 × 主题演进矩阵

> 生成日期：2026-06-25
> 来源：wiki/topics/ 16 张主题卡片交叉分析

## 说明

追踪 2024–2027 年间六大关键主题的演进状态。每格标注该时间段的里程碑事件和状态变化。

## 矩阵

| 年份 | 数据面架构 | DaaS 标准化 | GTP-U 替代 | AI 原生数据面 | 数据编织电信化 | 跨域治理 |
|:--|:--|:--|:--|:--|:--|:--|
| **2024** | 华为发布 DaaS 白皮书[^1]；vivo/ZJU 提出 DSAP 协议栈[^2]；中国移动三体四层五面架构[^3]；NGMN 6G 愿景[^4] | 华为 SA2 提交首批 DaaS 提案（S2-24xxxxx）[^5]；vivo 提交 Data Plane Protocol 提案[^6] | SoftBank 全球首商用 SRv6 MUP[^7]；IETF 123 DT 提交 MUP 移动性管理[^8]；EURECOM IUP 提出 N3 消除[^9] | O-RAN dApp/E3 接口提出[^10]；AI-RAN Alliance 成立[^11]；Samsung M-UP 发布[^12]；3GPP Rel-18 FL 冻结[^13] | LG U+ Nudge-B 平台上线[^14]；DT ODE 报告 22× 性能[^15]；Google TDF Private Preview 延续[^16] | ETSI PDL GS 034 发布[^17]；GAIA-X 数据空间扩展[^18]；Fraunhofer Telco Data Space 启动[^19] |
| **2025** | SA2 FS_6G_ARC 立项（SP-241657）[^20]；WT#5 数据框架 + KI#21 定义[^21]；多家厂商提交架构提案[^22] | SA2 WT#5 KI#21 收到约 90 篇贡献（截至 SA2#166）[^23]；DaaS vs 增强 NWDAF 路线之争浮现[^24] | NVIDIA dUPF 100 Gbps / 25μs 发布[^25]；P4 可编程管道方案增多[^26]；3GPP 未正式讨论 GTP-U 替代时间表[^27] | ETSI ZSM GS 029 通过（2026.04 采纳）[^28]；Rel-19 NWDAF 增强冻结[^29]；4 个 EU 项目发布中期成果[^30] | Gartner Data Fabric 进入幻灭低谷[^31]；Vodafone Italy Nucleus 试点[^32]；ETSI ZSM GS 029 引入 Fabric 概念[^33] | SA5 DMFW TS 28.104 Rel-19 冻结[^34]；SA2/SA5 职责边界讨论加剧[^35]；TM Forum Data Governance 更新[^36] |
| **2026** | FS_6G_ARC 目标 30%→100%（截止 2027.03）[^37]；KI#21 进入方案收敛阶段[^38]；迁移架构（Legacy interworking）决策窗口[^39] | **关键收敛期**：DaaS 独立功能面 vs UPF 增强 vs 混合方案三路线投票预期[^40]；运营商联合立场形成（Vodafone 警告延迟风险）[^41] | IETF MUP WG 持续推进[^42]；DT/SoftBank 期望 3GPP CT 启动替代方案讨论[^43]；向后兼容方案设计[^44] | ZSM GS 029 正式发布并进入实施指南阶段[^45]；O-RAN dApp 规范初版预期[^46]；NWDAF Rel-20 WI 推进[^47] | Google TDF GA 状态待确认[^48]；Amdocs/Mycom 电信 Fabric 产品迭代[^49]；首批 ROI 独立审计预期[^50] | Rel-20 数据治理增强 WI 启动预期[^51]；ISAC 感知数据隐私框架讨论预期[^52]；跨 SA2/SA5 数据治理协调[^53] |
| **2027（预测）** | 🔮 Rel-21 SI 完成 → WI 转化[^54]；6G 数据面架构基本定型[^55]；独立功能面 vs 增强型两路线二选一[^56] | 🔮 DaaS 接口规范初版（若被采纳）[^57]；或 NWDAF+DCCF 增强路线确认[^58]；Stage-2 规范草案[^59] | 🔮 GTP-U 演进路径基本明确[^60]；SRv6 MUP 在 3GPP 获得参考地位可能性[^61]；双栈过渡方案预期[^62] | 🔮 首批 AI-native 数据管道 PoC[^63]；dApp 商用试点[^64]；NWDAF Rel-20 冻结[^65] | 🔮 数据编织进入电信规模试点（2-3 家 Tier-1 运营商）[^66]；Mesh-on-Fabric 混合架构成形[^67] | 🔮 联邦数据空间 + 3GPP 治理框架初步对接[^68]；跨域数据契约标准化[^69] |

## 关键演进趋势

### 1. 标准化加速但充满不确定性
- 2024-2025 年：概念提出和研究立项阶段，多路线并存
- 2026 年：**关键收敛窗口**——FS_6G_ARC 截止、DaaS 路线投票、GTP-U 替代时间表
- 2027 年：预期输出规范草案，但 3GPP 历史上常延期 12-18 个月[^70]

### 2. 产业试点先于标准化
- 数据编织（DT ODE 2024）、SRv6 MUP（SoftBank 2024）、dApp（O-RAN 2024）均在标准冻结前已有试点
- 这种"先试点后标准化"的模式可能加速也可能碎片化技术路线

### 3. 两极分化风险
- 中国（华为/中兴/vivo + 中国移动/电信）推动激进的数据面革新（DaaS/三体架构）
- 欧美厂商（Ericsson/Nokia/Qualcomm）偏好渐进增强（UPF+NWDAF 演进）
- 2026-2027 的标准博弈将决定最终方向

## 脚注

[^1]: [6g-data-plane-architecture-2025](../../wiki/topics/6g-data-plane-architecture-2025.md) — 华为 DaaS 白皮书
[^2]: [daas-interface-design](../../wiki/topics/daas-interface-design.md) — vivo/ZJU DSAP 协议栈
[^3]: [6g-data-plane-architecture-2025](../../wiki/topics/6g-data-plane-architecture-2025.md) — 三体四层五面
[^4]: [6g-data-plane-architecture-2025](../../wiki/topics/6g-data-plane-architecture-2025.md) — NGMN 愿景
[^5]: [3gpp-sa2-6g-data-framework-wt5](../../wiki/topics/3gpp-sa2-6g-data-framework-wt5.md) — 华为 DaaS 提案
[^6]: [daas-interface-design](../../wiki/topics/daas-interface-design.md) — vivo 提案
[^7]: [gtp-u-limitations-6g-alternatives](../../wiki/topics/gtp-u-limitations-6g-alternatives.md) — SoftBank MUP 商用
[^8]: [gtp-u-limitations-6g-alternatives](../../wiki/topics/gtp-u-limitations-6g-alternatives.md) — DT IETF 123
[^9]: [gtp-u-limitations-6g-alternatives](../../wiki/topics/gtp-u-limitations-6g-alternatives.md) — EURECOM IUP
[^10]: [ai-native-data-plane-status](../../wiki/topics/ai-native-data-plane-status.md) — O-RAN dApp
[^11]: [ai-native-data-plane-status](../../wiki/topics/ai-native-data-plane-status.md) — AI-RAN Alliance
[^12]: [gtp-u-limitations-6g-alternatives](../../wiki/topics/gtp-u-limitations-6g-alternatives.md) — Samsung M-UP
[^13]: [cross-domain-data-governance-6g](../../wiki/topics/cross-domain-data-governance-6g.md) — Rel-18 FL
[^14]: [data-fabric-in-telecom-early-cases](../../wiki/topics/data-fabric-in-telecom-early-cases.md) — LG U+ Nudge-B
[^15]: [data-fabric-in-telecom-early-cases](../../wiki/topics/data-fabric-in-telecom-early-cases.md) — DT ODE
[^16]: [data-fabric-in-telecom-early-cases](../../wiki/topics/data-fabric-in-telecom-early-cases.md) — Google TDF
[^17]: [cross-domain-data-governance-6g](../../wiki/topics/cross-domain-data-governance-6g.md) — ETSI PDL
[^18]: [cross-domain-data-governance-6g](../../wiki/topics/cross-domain-data-governance-6g.md) — GAIA-X
[^19]: [cross-domain-data-governance-6g](../../wiki/topics/cross-domain-data-governance-6g.md) — Telco Data Space
[^20]: [3gpp-6g-timeline-rel22-23](../../wiki/topics/3gpp-6g-timeline-rel22-23.md) — FS_6G_ARC 立项
[^21]: [3gpp-sa2-6g-data-framework-wt5](../../wiki/topics/3gpp-sa2-6g-data-framework-wt5.md) — WT#5/KI#21
[^22]: [3gpp-sa2-6g-data-framework-wt5](../../wiki/topics/3gpp-sa2-6g-data-framework-wt5.md) — 多厂商提案
[^23]: [3gpp-sa2-6g-data-framework-wt5](../../wiki/topics/3gpp-sa2-6g-data-framework-wt5.md) — 90 篇贡献
[^24]: [3gpp-sa2-6g-data-framework-wt5](../../wiki/topics/3gpp-sa2-6g-data-framework-wt5.md) — 路线之争
[^25]: [user-plane-evolution-upf-to-6g](../../wiki/topics/user-plane-evolution-upf-to-6g.md) — NVIDIA dUPF
[^26]: [gtp-u-limitations-6g-alternatives](../../wiki/topics/gtp-u-limitations-6g-alternatives.md) — P4 方案
[^27]: [gtp-u-limitations-6g-alternatives](../../wiki/topics/gtp-u-limitations-6g-alternatives.md) — 时间表缺失
[^28]: [data-fabric-for-ai-native-6g](../../wiki/topics/data-fabric-for-ai-native-6g.md) — ZSM GS 029
[^29]: [3gpp-rel-19-20-data-architecture-status](../../wiki/topics/3gpp-rel-19-20-data-architecture-status.md) — Rel-19 冻结
[^30]: [data-fabric-for-ai-native-6g](../../wiki/topics/data-fabric-for-ai-native-6g.md) — EU 项目
[^31]: [data-fabric-definition-and-capabilities](../../wiki/topics/data-fabric-definition-and-capabilities.md) — Gartner 幻灭低谷
[^32]: [data-fabric-in-telecom-early-cases](../../wiki/topics/data-fabric-in-telecom-early-cases.md) — Vodafone Nucleus
[^33]: [data-fabric-for-ai-native-6g](../../wiki/topics/data-fabric-for-ai-native-6g.md) — ZSM Fabric 概念
[^34]: [3gpp-rel-19-20-data-architecture-status](../../wiki/topics/3gpp-rel-19-20-data-architecture-status.md) — DMFW 冻结
[^35]: [3gpp-sa2-6g-data-framework-wt5](../../wiki/topics/3gpp-sa2-6g-data-framework-wt5.md) — SA2/SA5 边界
[^36]: [data-fabric-in-telecom-early-cases](../../wiki/topics/data-fabric-in-telecom-early-cases.md) — TM Forum
[^37]: [3gpp-6g-timeline-rel22-23](../../wiki/topics/3gpp-6g-timeline-rel22-23.md) — FS_6G_ARC 进度
[^38]: [3gpp-sa2-6g-data-framework-wt5](../../wiki/topics/3gpp-sa2-6g-data-framework-wt5.md) — KI#21 收敛
[^39]: [3gpp-6g-timeline-rel22-23](../../wiki/topics/3gpp-6g-timeline-rel22-23.md) — 迁移架构决策
[^40]: [3gpp-sa2-6g-data-framework-wt5](../../wiki/topics/3gpp-sa2-6g-data-framework-wt5.md) — 三路线竞争
[^41]: [3gpp-6g-timeline-rel22-23](../../wiki/topics/3gpp-6g-timeline-rel22-23.md) — Vodafone 警告
[^42]: [gtp-u-limitations-6g-alternatives](../../wiki/topics/gtp-u-limitations-6g-alternatives.md) — IETF MUP
[^43]: [gtp-u-limitations-6g-alternatives](../../wiki/topics/gtp-u-limitations-6g-alternatives.md) — GTP-U 替代讨论
[^44]: [gtp-u-limitations-6g-alternatives](../../wiki/topics/gtp-u-limitations-6g-alternatives.md) — 向后兼容
[^45]: [data-fabric-for-ai-native-6g](../../wiki/topics/data-fabric-for-ai-native-6g.md) — ZSM 实施
[^46]: [ai-native-data-plane-status](../../wiki/topics/ai-native-data-plane-status.md) — dApp 规范
[^47]: [3gpp-rel-19-20-data-architecture-status](../../wiki/topics/3gpp-rel-19-20-data-architecture-status.md) — Rel-20 WI
[^48]: [data-fabric-in-telecom-early-cases](../../wiki/topics/data-fabric-in-telecom-early-cases.md) — Google TDF GA
[^49]: [data-fabric-in-telecom-early-cases](../../wiki/topics/data-fabric-in-telecom-early-cases.md) — 电信 Fabric 产品
[^50]: [data-fabric-in-telecom-early-cases](../../wiki/topics/data-fabric-in-telecom-early-cases.md) — ROI 审计
[^51]: [3gpp-rel-19-20-data-architecture-status](../../wiki/topics/3gpp-rel-19-20-data-architecture-status.md) — Rel-20 治理
[^52]: [cross-domain-data-governance-6g](../../wiki/topics/cross-domain-data-governance-6g.md) — ISAC 隐私
[^53]: [3gpp-sa2-6g-data-framework-wt5](../../wiki/topics/3gpp-sa2-6g-data-framework-wt5.md) — SA2/SA5 协调
[^54]: [3gpp-6g-timeline-rel22-23](../../wiki/topics/3gpp-6g-timeline-rel22-23.md) — Rel-21 SI→WI
[^55]: [6g-data-plane-architecture-2025](../../wiki/topics/6g-data-plane-architecture-2025.md) — 架构定型
[^56]: [3gpp-sa2-6g-data-framework-wt5](../../wiki/topics/3gpp-sa2-6g-data-framework-wt5.md) — 路线决策
[^57]: [daas-interface-design](../../wiki/topics/daas-interface-design.md) — DaaS 接口规范
[^58]: [3gpp-rel-19-20-data-architecture-status](../../wiki/topics/3gpp-rel-19-20-data-architecture-status.md) — NWDAF 增强
[^59]: [3gpp-6g-timeline-rel22-23](../../wiki/topics/3gpp-6g-timeline-rel22-23.md) — Stage-2 草案
[^60]: [gtp-u-limitations-6g-alternatives](../../wiki/topics/gtp-u-limitations-6g-alternatives.md) — GTP-U 路径
[^61]: [gtp-u-limitations-6g-alternatives](../../wiki/topics/gtp-u-limitations-6g-alternatives.md) — SRv6 MUP 地位
[^62]: [gtp-u-limitations-6g-alternatives](../../wiki/topics/gtp-u-limitations-6g-alternatives.md) — 双栈过渡
[^63]: [ai-native-data-plane-status](../../wiki/topics/ai-native-data-plane-status.md) — AI 数据管道 PoC
[^64]: [ai-native-data-plane-status](../../wiki/topics/ai-native-data-plane-status.md) — dApp 商用
[^65]: [3gpp-rel-19-20-data-architecture-status](../../wiki/topics/3gpp-rel-19-20-data-architecture-status.md) — Rel-20 冻结
[^66]: [data-fabric-in-telecom-early-cases](../../wiki/topics/data-fabric-in-telecom-early-cases.md) — 规模试点
[^67]: [data-fabric-vs-data-mesh](../../wiki/topics/data-fabric-vs-data-mesh.md) — Mesh-on-Fabric
[^68]: [cross-domain-data-governance-6g](../../wiki/topics/cross-domain-data-governance-6g.md) — 联邦数据空间
[^69]: [cross-domain-data-governance-6g](../../wiki/topics/cross-domain-data-governance-6g.md) — 数据契约
[^70]: [3gpp-6g-timeline-rel22-23](../../wiki/topics/3gpp-6g-timeline-rel22-23.md) — 历史延期模式
