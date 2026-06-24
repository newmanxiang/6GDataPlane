---
title: 6G 数据面将从用户面独立为新功能面
slug: trend-independent-data-plane
horizon: 36m
confidence: medium
direction: emerging
drivers:
  - 华为 DaaS 三层架构（DO/DA/DCP）体系化设计
  - 中国移动三体四层五面架构中数据面独立
  - 3GPP SA2 WT#5 KI#21 正式立项研究
  - AI 原生网络对统一数据管道的刚性需求
  - vivo/ZJU DSAP 协议栈端到端覆盖
inhibitors:
  - Qualcomm/Nokia 用户面优先立场
  - 3GPP 标准收敛可能选择增强 NWDAF 路线
  - 独立功能面带来的复杂性增长和互操作成本
  - 运营商 CAPEX/OPEX 增长顾虑
evidence:
  - 6g-data-plane-architecture-2025
  - daas-interface-design
  - 3gpp-sa2-6g-data-framework-wt5
  - ai-native-data-plane-status
counter_evidence:
  - 3gpp-sa2-6g-data-framework-wt5
  - user-plane-evolution-upf-to-6g
companies_to_watch:
  - 华为
  - 中国移动
  - vivo
  - 中兴
  - Qualcomm
  - Nokia
my_company_relevance: high
created: 2026-06-25
---

# 6G 数据面将从用户面独立为新功能面

## 一句话总结

6G 数据面（Data Plane）有望从传统用户面中分化，成为与控制面、用户面并列的第三功能面。

## 论据（按强度排序）

1. **华为 DaaS 体系化设计**：DO (Data Orchestrator) → DA (Data Agent) → DCP (Data Connection Point) 三层架构形成了完整的独立数据面逻辑体系，覆盖编排、管理、接入三个层面。这是目前最成熟的独立数据面方案。→ [6g-data-plane-architecture-2025](../../wiki/topics/6g-data-plane-architecture-2025.md)

2. **3GPP SA2 WT#5 正式立项**：FS_6G_ARC Study Item（SP-241657）的 WT#5 数据框架及 KI#21 专门研究"6G 中的数据作为服务和数据管理"，标志着数据面议题已进入 3GPP 正式议程。截至 SA2#166 已收到约 90 篇贡献，活跃度在 WT#5 中最高。→ [3gpp-sa2-6g-data-framework-wt5](../../wiki/topics/3gpp-sa2-6g-data-framework-wt5.md)

3. **中国移动三体四层五面架构**：明确在控制面、用户面之外增设数据面/智能面，从运营商角度验证了独立数据面的需求逻辑。→ [6g-data-plane-architecture-2025](../../wiki/topics/6g-data-plane-architecture-2025.md)

4. **AI 原生网络的数据管道需求**：AI 模型训练/推理需要跨 NF、跨域的统一数据访问能力，现有 NWDAF/DCCF 的点对点数据收集架构难以满足。独立数据面可提供统一数据抽象层。→ [ai-native-data-plane-status](../../wiki/topics/ai-native-data-plane-status.md)

5. **vivo/ZJU DSAP 协议栈**：从终端侧提出 Data Service Access Protocol，端到端覆盖 UE 至核心网的数据服务访问，进一步强化了独立数据面的协议栈设计。→ [daas-interface-design](../../wiki/topics/daas-interface-design.md)

## 反向证据 / 不确定性

- **Qualcomm 用户面优先立场**：Qualcomm 在 SA2 中主张增强现有用户面功能（UPF+NWDAF）而非引入新功能面，认为独立数据面增加不必要的复杂性 → [3gpp-sa2-6g-data-framework-wt5](../../wiki/topics/3gpp-sa2-6g-data-framework-wt5.md)
- **标准收敛延迟风险**：FS_6G_ARC 目标 2027.03 完成，但 3GPP 历史上常延期。若 SI 阶段无法收敛，独立数据面可能被降级为增强型 NWDAF → [3gpp-6g-timeline-rel22-23](../../wiki/topics/3gpp-6g-timeline-rel22-23.md)
- **增强型 UPF 路线的惯性**：UPF 从 CUPS 到 Rel-19 UPEAS 的演进路径成熟，渐进增强的阻力更小 → [user-plane-evolution-upf-to-6g](../../wiki/topics/user-plane-evolution-upf-to-6g.md)

## 信号事件

- 2024-Q3：华为发布 DaaS 白皮书，首次系统阐述独立数据面架构（华为技术）
- 2024-Q4：3GPP SA2 WT#5/KI#21 正式立项（3GPP SA2#163）
- 2025-Q1：SA2#166 收到 90+ 篇 KI#21 贡献，活跃度持续攀升（3GPP SA2 meeting records）
- 2025-Q2：vivo/ZJU 提交 DSAP 协议栈提案至 SA2（3GPP SA2）
- 2026-H1：FS_6G_ARC 进度 30%→目标 100%（3GPP 项目管理）

## 未来 12-24 月可观察的指标

- [ ] 3GPP SA2 WT#5 KI#21 方案收敛结论（DaaS 独立面 vs 增强 NWDAF vs 混合）
- [ ] FS_6G_ARC Study Item 完成率（2027.03 截止）
- [ ] 运营商联合立场文件是否支持独立数据面
- [ ] 是否有厂商发布独立数据面原型验证结果
- [ ] Rel-21 WI 阶段是否正式纳入数据面功能面定义

## 何时该被推翻

- 若 SA2 WT#5 KI#21 最终结论明确选择"增强 NWDAF+DCCF"路线且不设独立功能面 → **推翻**
- 若 2027.03 FS_6G_ARC 完成后数据面相关条目被删除或大幅缩减 → **推翻**
- 若 Qualcomm/Nokia/Ericsson 联合发表反对独立数据面的贡献且获得多数运营商支持 → **弱化**
- 若 2027 年底仍无任何厂商发布独立数据面原型/PoC → **弱化**
