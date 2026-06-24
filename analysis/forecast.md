# 12-24 个月预判

> 生成日期：2026-06-25
> 基于：16 张主题卡片 + 7 张趋势卡 + 4 张对比矩阵 + 37 条矛盾记录 + 100+ 条缺口记录
> 预判窗口：2026.07 — 2028.06

---

## 高信心

> 有多个独立证据支撑、核心驱动力已确立、阻力可量化但不改变方向。

### 1. 3GPP SA2 WT#5 数据框架将在 2027.03 前给出方向性结论

FS_6G_ARC Study Item 目标 2027.03 完成，KI#21 已积累 90+ 篇贡献，三条路线（DaaS 独立面 / 增强 NWDAF / 混合）的方案竞争已充分展开。即便延期 3-6 个月，方向性结论（非最终规范）大概率在 2027 年内产出。

**依据**：[trend-standardization-race](trends/trend-standardization-race.md)、[3gpp-sa2-6g-data-framework-wt5](../wiki/topics/3gpp-sa2-6g-data-framework-wt5.md)、[3gpp-6g-timeline-rel22-23](../wiki/topics/3gpp-6g-timeline-rel22-23.md)

**翻车条件**：FS_6G_ARC 延期超过 12 个月；或 3GPP 决定将数据框架移出 Rel-21 范围

### 2. AI 原生网络数据管理将产生首批跨标准组织协调需求

ETSI ZSM GS 029（Data Fabric）、3GPP SA2 WT#5（Data Framework）、O-RAN dApp 数据管道三套框架的功能重叠已不可忽视。12-24 月内预计出现首批交叉引用或联合讨论。

**依据**：[trend-ai-native-data-management](trends/trend-ai-native-data-management.md)、矛盾 CT-2（ETSI/3GPP 术语分离）、矛盾 CT-4（四套框架互操作缺失）

**翻车条件**：各标准组织选择独立演进，不发生协调

### 3. ETSI ZSM GS 029 正式发布并引发电信数据编织实施热潮

GS 029 已通过投票（2026.04），正式发布在即。作为首个明确引入 Data Fabric 的电信标准，将催化供应商产品适配和运营商评估。但从标准到部署仍需 18-24 月。

**依据**：[data-fabric-for-ai-native-6g](../wiki/topics/data-fabric-for-ai-native-6g.md)、[trend-data-fabric-telecom-adoption](trends/trend-data-fabric-telecom-adoption.md)

**翻车条件**：GS 029 因缺乏产业支持而被搁置

### 4. GTP-U 替代方案讨论将正式进入 3GPP 议程

SoftBank SRv6 MUP 商用已超过 2 年（至 2026），NVIDIA dUPF 性能验证、DT IETF 推动形成充分的外部压力。3GPP CT 或 SA2 预计在 2027 年启动相关 Study Item 或至少产生正式讨论记录。

**依据**：[trend-gtp-u-sunset](trends/trend-gtp-u-sunset.md)、[gtp-u-limitations-6g-alternatives](../wiki/topics/gtp-u-limitations-6g-alternatives.md)

**翻车条件**：3GPP 明确延续 GTP-U 至 6G 且无演进计划

---

## 中信心

> 有显著证据但存在关键不确定性，结果取决于特定事件或决策。

### 5. DaaS 将以某种形式被 3GPP 6G 架构采纳（但可能不是独立功能面）

华为 DaaS 概念（数据编排 + 数据代理 + 数据连接点）的核心理念——网络应具备统一的数据服务能力——已获广泛认同。但"独立功能面"形态面临 Qualcomm/Nokia 反对。最可能的结果是：数据服务功能被采纳为核心网增强能力，但不一定定义为与 CP/UP 并列的第三面。

**依据**：[trend-independent-data-plane](trends/trend-independent-data-plane.md)、矛盾 5（三路线分歧）

**关键变量**：2026 下半年至 2027 上半年 SA2 方案投票结果

### 6. 2-3 家 Tier-1 运营商将启动数据编织规模试点

DT ODE（22× 性能提升）、LG U+ Nudge-B（生产上线）、Vodafone Nucleus（试点启动）已形成先行者集群。ZSM GS 029 发布将进一步降低决策门槛。预计 2027-2028 年新增 2-3 家 Tier-1 运营商进入规模试点。

**依据**：[trend-data-fabric-telecom-adoption](trends/trend-data-fabric-telecom-adoption.md)、[data-fabric-in-telecom-early-cases](../wiki/topics/data-fabric-in-telecom-early-cases.md)

**关键变量**：Google TDF 是否 GA；独立 ROI 审计报告是否发布

### 7. SA2/SA5 数据治理框架边界将在 2027 年达成初步协议

矛盾 31（SA2 WT#5 vs SA5 DMFW 职责重叠）已被运营商在多次会议上提出。TSG SA 层面协调的压力增大。预计 2027 年产出"SA2 负责网络架构层数据框架、SA5 负责 OAM 层数据治理"的分工协议。

**依据**：[trend-cross-domain-governance](trends/trend-cross-domain-governance.md)、矛盾 11/31

**关键变量**：是否有运营商联合提出正式 LS（联络声明）要求协调

### 8. O-RAN dApp 规范初版发布并催生首批商用 PoC

O-RAN dApp/E3 接口概念提出已 2 年，AI-RAN Alliance 持续推动。规范初版预计 2027 年发布，至少 2-3 家设备商发布 PoC。但从 PoC 到商用仍有距离。

**依据**：[trend-ai-native-data-management](trends/trend-ai-native-data-management.md)、[ai-native-data-plane-status](../wiki/topics/ai-native-data-plane-status.md)

**关键变量**：O-RAN 规范制定速度；Samsung/Nokia 在 dApp 上的投入

---

## 不确定 / 监控中

> 证据不充分或方向可能反转，需持续跟踪。

### 9. 中国/欧美 6G 数据面技术路线是否会分裂

中国阵营（华为/中兴/中国移动/vivo）推动 DaaS/独立数据面，欧美阵营（Qualcomm/Nokia/Ericsson）偏好渐进增强。地缘政治紧张可能加剧技术分歧。最坏情况下形成双标准体系。

**监控信号**：SA2 投票中的阵营分化程度；是否出现"某阵营集体退出某 KI 讨论"事件

### 10. Mesh-on-Fabric 混合架构是否获得产业采纳

理论互补性已有共识（Gartner/Forrester/AWS），但电信领域零实践。Data Mesh 本身在企业 IT 的采纳率仍低（13% 双模式使用）。可能过于超前。

**监控信号**：运营商是否在架构文件中使用 Mesh-on-Fabric 术语；TM Forum 是否纳入正式框架

### 11. ISAC 感知数据治理框架的推进速度

ISAC 作为 6G 六大场景之一已确立，但感知数据的采集/存储/共享治理框架完全空白。若 ISAC 从 6G 首版标准延期，治理需求的紧迫性将下降。

**监控信号**：3GPP ISAC Study Item 进展；国家级感知数据隐私法规动向

### 12. Google Cloud Telecom Data Fabric 命运

TDF 自 Private Preview 以来已超过 3 年未 GA。可能的结果：(a) 正式 GA 并成为标杆、(b) 被拆分为独立组件、(c) 静默下线。任何一种结果都会影响电信数据编织的产业叙事。

**监控信号**：Google Cloud 产品页更新；Google Cloud Next 电信专场内容

---

## 黑天鹅候选

> 低概率但一旦发生将根本改变格局的事件。

### 政策类
- **6G 标准化分裂**：地缘政治导致 3GPP 分裂为两个竞争性标准体系（如中国 + 俄罗斯 vs 西方），数据面架构出现双轨制
- **数据主权强制令**：某主要市场（EU/中国/印度）出台强制性网络数据本地化法规，禁止跨境数据编织，使联邦数据架构失去法律基础
- **AI 监管收紧**：AI 安全立法（如 EU AI Act 扩展）将 AI 原生网络数据面定义为"高风险 AI 系统"，大幅增加合规成本

### 技术类
- **量子计算突破**：实用量子计算提前到来（2028-2029），使当前所有加密/隐私保护方案失效，数据治理框架需要全面重设计
- **颠覆性传输协议**：基于新原理（如语义通信、全息通信）的传输协议使 GTP-U 和 SRv6 的讨论全部过时
- **边缘 AI 芯片突破**：终端 AI 算力突破使数据不需出终端即可完成 90%+ 处理，集中式/联邦式数据管理需求大幅下降

### 商业类
- **超大规模云商收购电信厂商**：如 Google/AWS 收购 Nokia/Ericsson，使云原生数据编织直接进入电信网络核心，跳过标准化路径
- **6G 投资寒冬**：全球经济衰退导致运营商大幅削减 6G 研发投入，标准化时间表整体后移 3-5 年
- **开源数据编织平台崛起**：开源社区（如 Apache 基金会）推出电信专用数据编织平台，打破 IBM/Informatica 等供应商主导格局

---

## 监控指标

> 以下指标用于判断预判兑现/翻车的可观察信号。按季度/事件驱动跟踪。

### 标准化进度指标
| 指标 | 跟踪频率 | 数据源 | 预判关联 |
|:--|:--|:--|:--|
| FS_6G_ARC 完成率 | 每次 SA2 会议后 | 3GPP PMO | 预判 1 |
| KI#21 方案候选数 | 每次 SA2 会议后 | 3GPP SA2 记录 | 预判 1, 5 |
| SA2/SA5 联合讨论次数 | 季度 | 3GPP LS 记录 | 预判 7 |
| GTP-U 替代相关 SI/WI 状态 | 每次 CT 会议后 | 3GPP CT 记录 | 预判 4 |
| ETSI ZSM GS 029 实施指南发布 | 事件驱动 | ETSI 发布列表 | 预判 3 |
| O-RAN dApp 规范版本 | 季度 | O-RAN Alliance | 预判 8 |

### 产业部署指标
| 指标 | 跟踪频率 | 数据源 | 预判关联 |
|:--|:--|:--|:--|
| 电信数据编织部署运营商数 | 半年 | 供应商/运营商公告 | 预判 6 |
| SRv6 MUP 部署运营商数 | 半年 | 运营商公告 | 预判 4 |
| Google TDF 状态（Preview/GA/退市） | 事件驱动 | Google Cloud 产品页 | 预判 12 |
| 数据编织独立 ROI 审计报告数 | 半年 | Gartner/Forrester/IDC | 预判 6 |

### 市场/生态指标
| 指标 | 跟踪频率 | 数据源 | 预判关联 |
|:--|:--|:--|:--|
| Gartner Data Fabric Hype Cycle 位置 | 年度 | Gartner HC for DM | 预判 6 |
| SA2 投票中阵营分化程度 | 每次 SA2 会议后 | 3GPP SA2 记录 | 预判 9 |
| Mesh-on-Fabric 术语使用频率 | 季度 | 运营商/供应商文档 | 预判 10 |
| ISAC 隐私框架提案数 | 半年 | 3GPP/ETSI/国家级法规 | 预判 11 |

### 预判置信度更新规则

- **高信心 → 确认**：2+ 个监控指标连续 2 季度正向 → 预判确认
- **高信心 → 降级**：翻车条件触发 → 降级为中信心或不确定
- **中信心 → 升级**：关键变量明确 + 2 个指标正向 → 升级为高信心
- **不确定 → 方向明确**：3 个月内出现 2+ 个方向性信号 → 升级或删除
- **黑天鹅 → 触发**：相关事件发生 → 立即重评所有预判

---

*下次预判更新建议时间：2026.12（SA2#176 后）或重大事件发生时*
