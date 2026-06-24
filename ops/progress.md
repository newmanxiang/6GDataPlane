# 进度跟踪

> 每天末 Agent 更新本文件。

## 模板

```markdown
## D<N> · YYYY-MM-DD

### 计划
- ...

### 完成
- ...

### 未完成（滚到明日）
- ...

### 关键产出
- wiki/concepts/<...>.md
- wiki/topics/<...>.md
- analysis/...

### 数据/关键发现
- ...

### 阻塞 / 风险
- ...

### 明日要点
- ...
```

---

## D11 · 2026-06-25（标准 P0 补完 + 趋势综合日 ⭐）

### 计划
- 补完最后 2 个标准 P0：`3gpp-6g-timeline-rel22-23` + `3gpp-sa2-6g-data-framework-wt5`
- 6g-trend-synth 全流程趋势综合（主题聚类 → 矩阵 M1-M4 → 趋势卡 → 矛盾归并 → 预判）

### 完成
- 2 张标准 P0 topic 卡全部创建（reviewed 状态）
- **P0 全部清零：16/16 done**
- 7 张趋势卡创建（2 high / 4 medium / 1 low 信心）
- 4 张对比矩阵创建（M1-M4，共 197 格）
- 主题聚类图创建（Mermaid）
- 12-24 月预判报告创建（4 高信心 / 4 中信心 / 4 不确定 / 9 黑天鹅候选）
- 矛盾归并：新增 3 条（标准时间线）+ 1 条（WT#5）+ 5 条跨主题矛盾 → 累计 38 条
- 缺口归并：新增 6 条 + 5 条 + 8 条 → 累计 110+ 行

### 关键产出
- wiki/topics/3gpp-6g-timeline-rel22-23.md
- wiki/topics/3gpp-sa2-6g-data-framework-wt5.md
- analysis/topic-clusters.md（主题聚类图）
- analysis/matrices/vendor-capability.md（M1 厂商×能力，12×6）
- analysis/matrices/standards-topics.md（M2 标准组织×议题，11×7）
- analysis/matrices/core-intersection.md（M3 数据编织能力×6G场景 ⭐，6×4）
- analysis/matrices/timeline-topics.md（M4 时间×主题，4×6）
- analysis/trends/ × 7 张趋势卡
- analysis/forecast.md（12-24 月预判）
- analysis/contradictions.md 更新（+9 矛盾 → 38 条）
- analysis/gaps.md 更新（+19 缺口）
- research/notes/ × 2 份精读笔记
- research/search-log.md 更新

### 数据/关键发现

**标准 · 3GPP 6G 时间线**
- Rel-21 时间线于 2026.06.10（TSGs#112 新加坡）正式批准，ASN.1 冻结 2029.03
- Rel-22/23 无正式规划，行业推测 2030-2032 为"6G 增强阶段"
- 迁移架构决策从 TSG#111 → #112 → RAN#113（2026.09 马德里）连续推迟，Vodafone 警告"窗口正在关闭"

**标准 · SA2 WT#5 数据框架**
- TR 23.801-01 已迭代至 V0.7.0（16.8 MB），WT#5 对应 KI#21
- Penholder 于 SA2#174（2026.04 马耳他）完成分配，进入方案评估阶段
- "独立数据面 vs 增强用户面"核心分歧仍未收敛，进度 30%，时间压力大

**趋势综合**
- 7 大趋势中 2 个高信心：AI 原生数据管理范式变革（accelerating）、标准化窗口关键收敛（accelerating）
- 核心交集矩阵 M3 揭示多个"研究空白"象限（终端侧数据编织能力几乎未探索）
- 5 条跨主题矛盾（企业 IT vs 电信实时性鸿沟、ETSI vs 3GPP 术语分裂、产业先行 vs 标准滞后、四套并行框架互操作缺失、终端侧空白）

### 阻塞 / 风险
- company-context.md §4-6 仍有待填写项，D12 我司适配日需用户补充
- 趋势卡中 2 个 low/medium 信心趋势（Mesh-on-Fabric、独立数据面）证据链偏弱，后续可补强

### 明日要点
- D12：我司适配日 — 调用 6g-insight-report（仅 §8 准备阶段）
- 在 analysis/company-fit/ 输出 capability-map / opportunities / threats / actions
- 前提：用户需补充 company-context.md §4-6（短/中/长期战略、团队规模、报告受众）
- 若 §4-6 未填，可基于已有 §1-3 先产出初版，后续迭代

---

## D10 · 2026-06-24（交集议题专题日 ⭐：C 类 P0 ×2）

### 计划
- 深调 P0: `data-fabric-for-ai-native-6g` ⭐（本调研最关键交集议题）
- 深调 P0: `cross-domain-data-governance-6g`

### 完成
- 2 张交集 topic 卡全部创建（reviewed 状态）
- 精读来源 29 篇（data-fabric-for-ai-native-6g 15 篇 + cross-domain-data-governance-6g 14 篇），权威源 10+ 篇
- 矛盾记录新增 5 条（#28-#32）
- 数据缺口新增 14 条（7 + 7）
- Queue P0 累计 done: 14/16（剩余 2 个标准 P0 被 D8 遗留）

### 关键产出
- wiki/topics/data-fabric-for-ai-native-6g.md（⭐ 核心交集，19 个来源）
- wiki/topics/cross-domain-data-governance-6g.md（14 个来源）
- research/notes/data-fabric-for-ai-native-6g.md
- research/notes/cross-domain-data-governance-6g.md
- analysis/contradictions.md 更新（+5 矛盾 → 累计 32 条）
- analysis/gaps.md 更新（+14 缺口）
- research/search-log.md 更新（+20 条搜索记录）

### 数据/关键发现

**C 类 · 数据编织×AI 原生 6G ⭐**
- ETSI ZSM GS 029（2026-04 采纳）是首个 6G 数据管理标准规范，由中国电信/ZTE 主导，功能需求与数据编织高度重合
- 至少 4 个 EU SNS JU 6G 项目（6G-TWIN/6G-DALI/ROBUST-6G/CANDIL）在架构中显式使用"data fabric"
- Ericsson 2026 白皮书明确将 data fabric 列为 AI-ready 数据管理核心使能技术
- Nokia 将 Data Framework 列为 6G 六大技术框架之一
- AWS 提出"Fabric of Fabrics"概念——层级化智能编织支撑 6G 多 Agent 协作
- 核心适配挑战：企业 IT 级数据编织（GB/s）如何适配电信（TB/s + 亚毫秒）场景
- 术语混淆是最大标准化风险：Ericsson "data mesh" vs Nokia "data framework" vs AWS "intelligence fabric" vs ETSI "integration fabric"

**C 类 · 6G 跨域数据治理**
- 3GPP SA5 已启动 DMFW 研究，SA2 WT#5 也涵盖治理维度，两者存在职责交叉
- 三大治理范式并存：联邦治理（Nokia/Ericsson）、数据空间治理（IDSA/GAIA-X/6G-DALI）、策略即代码治理（DT MARA）
- ETSI ISG PDL 正制定 GS PDL 034 跨域数据治理规范（区块链驱动审计）
- 数据主权法规碎片化（GDPR vs 中国数据安全法）是核心挑战
- Deutsche Telekom MARA 蓝图（2026-04）是运营商 AI 时代数据治理的最先进实践

### 阻塞 / 风险
- 标准 P0 剩余 2 个（`3gpp-6g-timeline-rel22-23` + `3gpp-sa2-6g-data-framework-wt5`），被 D8 遗留，需 D11 前补完
- company-context.md §4-6 仍有待填项，D12 前需用户补充

### 明日要点
- D11：趋势综合日（6g-trend-synth 全流程）
- 前提：先补完 2 个遗留标准 P0，否则 §5 标准章节素材不足
- 建议：D11 开头先快速补标准 P0，再进入趋势综合

---

## D9 · 2026-06-23（深调 ×4 + 全量治理：B 类 + C 类 + 标准 P0）

### 计划
- 深调 P0: `data-fabric-definition-and-capabilities`
- 深调 P0: `data-fabric-vs-data-mesh`
- 深调 P0: `data-fabric-in-telecom-early-cases`
- 深调 P0: `3gpp-rel-19-20-data-architecture-status`
- wiki-curator 全量治理 T1-T7

### 完成
- 4 张 topic 卡全部创建（reviewed 状态）
- 精读来源 50+ 篇（定义与能力 12 + Fabric vs Mesh 11 + 电信实践 12 + 3GPP 标准 15），权威源 20+ 篇
- 矛盾记录新增 13 条（B 类 7 + 电信 4 + 标准 2）
- 数据缺口新增 20 条
- Queue P0 累计 done: 12/16
- **wiki-curator 全量治理 T1-T7 完成**：扫描 30 张卡片，变更 12 张；修复 11 条缺失回链、清理 1 条死链 + 1 条自引用；发现 4 个孤儿概念、7 个未登记高频域名

### 关键产出
- wiki/topics/data-fabric-definition-and-capabilities.md
- wiki/topics/data-fabric-vs-data-mesh.md
- wiki/topics/data-fabric-in-telecom-early-cases.md
- wiki/topics/3gpp-rel-19-20-data-architecture-status.md
- research/notes/ × 4 份精读笔记
- analysis/contradictions.md 更新（+13 矛盾）
- analysis/gaps.md 更新（+20 缺口）
- research/search-log.md 更新
- ops/curator-reports/2026-06-23-d9.md（全量治理报告）
- wiki/concepts/README.md 概念地图刷新
- wiki/README.md 统计表刷新

### 数据/关键发现

**B 类 · 数据编织定义与能力全景**
- Gartner Hype Cycle 2024：Data Fabric 处于"幻灭低谷"，维持"变革性"评级，2-5 年到达成熟期
- Gartner 2025 提出"Multimodal Data Fabric"，扩展至向量/非结构化数据
- 市场高度分散：Top 10 供应商仅占 ~22%，IBM/Informatica/Denodo 为 MQ 连续 Leader
- GenAI 成为采纳催化剂："成功的 GenAI 产品需要 Data Fabric 交付 Active Metadata"

**B 类 · Fabric vs Mesh 对比**
- Mesh-on-Fabric 混合模式已成共识；Gartner 预测 2028 年 80% AI-Ready 数据产品产自互补架构
- Nokia/Ericsson/Google Cloud/TM Forum 四方验证电信混合架构适用性
- 建议路径：Fabric-first → Mesh-layered

**C 类 · 电信早期实践**
- 至少 12 家 CSP 启动数据编织或等效项目，但端到端 Data Fabric 显式部署仅少数
- Deutsche Telekom ODE：22× 性能提升、计划淘汰 40% 旧基础设施
- LG U+ Nudge-B：唯一显式以 Data Fabric 命名的运营商部署
- TM Forum 2025 调查：87 位高管中仅 2 人认为实现数据完全民主化——行业仍在早期
- 量化 ROI 数据多来自供应商宣传，缺乏独立审计（幸存者偏差）

**标准 · 3GPP Rel-19/20**
- Rel-19 已冻结（2025.09），NWDAF/DCCF/MFAF/UPEAS Ph2 全部完成
- Rel-20 双轨制：126 个 5G-A WI + 13 个 6G SI 并行
- FS_6G_ARC 进度 30%（2026.06），WT#5 数据框架是 6G 数据面最直接标准化入口
- 首个 Rel-21 WI（6G-REQ TS 22.270）已于 2026.03 获批——6G 从研究进入规范化
- 新术语：AI-Enabled NFs、Agentic Core、Intent-based Request

### 阻塞 / 风险
- 无

### 明日要点
- D10：交集专题日——`data-fabric-for-ai-native-6g`⭐ + `cross-domain-data-governance-6g`
- D10 允许超时间盒（最多 4 小时），这两个是最关键的交集子题
- P0 剩余 4 个（C 类 2 + 标准 2），D10 完成 C 类后标准 P0 可安排至 D11 前

---

## D8 · 2026-06-22（深调：UPF→6G 演进 + AI 原生数据面）

### 计划
- 深调 P0: `user-plane-evolution-upf-to-6g`
- 深调 P0: `ai-native-data-plane-status`

### 完成
- 2 张 topic 卡全部创建（reviewed 状态）
- 精读来源 24 篇（UPF 演进 12 + AI 原生 12），权威源 10 篇
- 矛盾记录新增 4 条（演进 vs 重构路线分歧、PFCP vs SBI 化、DCP vs dApp 时延不可比、AI 原生定义边界三派）
- 数据缺口新增 12 条
- Queue P0 累计 done: 8/16

### 关键产出
- wiki/topics/user-plane-evolution-upf-to-6g.md
- wiki/topics/ai-native-data-plane-status.md
- research/notes/ × 2 份精读笔记
- analysis/contradictions.md 更新（+4 矛盾）
- analysis/gaps.md 更新（+12 缺口）

### 数据/关键发现
- **UPF 演进五阶段**：CUPS 确立 → 分布式 dUPF → 可编程加速 → RAN-CN 融合 → 数据服务化；当前处第 3→4 阶段过渡期
- **dUPF 里程碑**：NVIDIA dUPF 实现 100 Gbps/25μs（2025.10），SoftBank SRv6 MUP 首个商用（2025.12）
- **核心分歧**：融合路线（M-UP/IUP/ANUP）vs 服务化路线（DaaS/UP-first），3GPP Rel-20 尚未收敛
- **AI 原生数据面三重路径**：华为独立 DP（DaaS DO/DA/DCP，延迟 ~2ms）、O-RAN dApp 实时 AI（<1ms）、学术可编程 ML（P4 Pegasus SIGCOMM 2025 线速推理）
- **关键术语发现**：AI-WIN、M-UP、IDFC、Modular UPF、dApp/E3 接口、QoAIS

### 阻塞 / 风险
- 无

### 明日要点
- D9：深调 B 类 P0 `data-fabric-definition-and-capabilities` + `data-fabric-vs-data-mesh` + 标准 P0 `3gpp-rel-19-20-data-architecture-status`
- 累计 8 topic 完成（上次治理后 +2），D9 再完成 2-3 题后触发 curator 治理（规则 #11 阈值 ≥ 3）

---

## D7 · 2026-06-21（深调：DaaS 接口设计 + GTP-U 替代方案）

### 计划
- 深调 P0: `daas-interface-design`
- 深调 P0: `gtp-u-limitations-6g-alternatives`

### 完成
- 2 张 topic 卡全部创建（reviewed 状态）
- 精读来源 26 篇（DaaS 12 + GTP-U 14），权威源 8 篇
- 矛盾记录新增 3 条（API 范式分歧、协议栈标准化、封装开销对比）
- 数据缺口新增 11 条
- Queue P0 累计 done: 6/16

### 关键产出
- wiki/topics/daas-interface-design.md
- wiki/topics/gtp-u-limitations-6g-alternatives.md
- research/notes/ × 2 份精读笔记

### 数据/关键发现
- **DaaS 接口**：华为 DO/DA/DCP 三组件是最完整的设计，DCP 无状态 Pub/Sub 原型延迟 ~2ms（降 65%）；5G NWDAF → 6G DaaS 范式转变已成共识，但 API 范式（Pub/Sub vs 增强 SBA）存在路线分歧
- **GTP-U 替代**：5 种方案并存（SRv6/MUP/P4-UPF/6G-RUPA/QUICUP），SRv6 MUP（RFC 9433）成熟度最高，SoftBank 已于 2025.12 全球首商用；Deutsche Telekom 于 IETF 123 正式提议 3GPP 6G 研究阶段纳入 SRv6
- **GTP-U 三大瓶颈量化**：O(N²) 状态爆炸、36-56B 封装开销、传输网无感知

### 阻塞 / 风险
- 无

### 明日要点
- D8：深调 `user-plane-evolution-upf-to-6g` + `ai-native-data-plane-status` + 标准 P0
- 累计 6 topic 完成（上次治理后 +4），下次应触发 curator 治理（规则 #11）

---

## D6 · 2026-06-21（治理 + 深调：数据面架构 + 框架设计约束）

### 计划
- wiki-curator 轻治理（T1+T3+T4）
- 深调 P0: `6g-data-plane-architecture-2025`
- 深调 P0: `imt-2030-framework-data-needs`

### 完成
- 轻治理：修复 52 条缺失回链，发现 1 条死链，2 张 reviewed 卡信心等级验证通过
- 2 张 topic 卡全部创建（reviewed 状态）
- 精读来源 27 篇（架构 16 + 框架 15，去重后），权威源 10 篇
- 矛盾记录新增 4 条（架构路线分歧、功能面数量、数据面独立性、上行流量预测）
- 数据缺口新增 11 条
- deep-dive-queue 中 4 个 P0 累计标记 done（D5: 2 + D6: 2）

### 关键产出
- ops/curator-reports/2026-06-21.md（治理报告）
- wiki/topics/6g-data-plane-architecture-2025.md
- wiki/topics/imt-2030-framework-data-needs.md
- research/notes/ × 2 份精读笔记

### 数据/关键发现
- **架构核心分歧**："独立数据面"（华为/中国移动/GTI）vs "增强用户面"（Qualcomm），3GPP SA2 WT#5 正在正式讨论
- **4 种架构提案并存**：华为 DaaS（DO/DA/DCP）、中国移动"三体四层五面"、Hexa-X-II DataOps、Qualcomm 用户面优先
- **范式转变**：6G 数据面从"包转发管道"到"数据服务平台（DaaS）"，需处理四类数据（通信/感知/AI/管理），5G 仅处理通信数据
- **上行流量结构性反转**：AI 驱动的物理智能将 UL:DL 从 90:10 向 50:50 甚至 30:70 迁移
- **标准化窗口紧迫**：3GPP SA2 研究项 2025-08 启动、2026-12 至 2027-03 完成

### 阻塞 / 风险
- 无

### 明日要点
- D7：深调 `daas-interface-design` + `gtp-u-limitations-6g-alternatives`
- 累计 4 个 topic 完成，下次深调后可能触发 curator 治理（规则 #11 阈值 ≥ 3）

---

## D5 · 2026-06-21（首批 P0 深调：IMT-2030 使用场景 + 6G KPI）

### 计划
- 深调 P0: `imt-2030-usage-scenarios-data-needs`
- 深调 P0: `6g-kpi-20-requirements`

### 完成
- 2 张 topic 卡全部创建（reviewed 状态）
- 精读来源 26 篇（每子题 13 篇），权威源 10 篇
- 矛盾记录 7 条追加至 analysis/contradictions.md
- 数据缺口 10 条追加至 analysis/gaps.md
- 精读笔记 2 份写入 research/notes/
- deep-dive-queue 中 2 个 P0 标记 done

### 关键产出
- wiki/topics/imt-2030-usage-scenarios-data-needs.md
- wiki/topics/6g-kpi-20-requirements.md
- research/notes/ × 2 份精读笔记
- analysis/contradictions.md 更新（+7 矛盾）
- analysis/gaps.md 更新（+10 缺口）

### 数据/关键发现
- **使用场景质变**：6G 新增 3 个全新场景（泛在连接 UC / AI 集成通信 AIAC / 通感一体 ISAC），对数据面提出根本性新需求（分布式 AI 管道、感知数据通道、跨接入互通）
- **愿景 vs 现实落差**：M.2160 框架 200 Gbps 峰值 vs 产业 TPR 提案 20-50 Gbps，差距 4-10 倍，正向保守收敛
- **Top 5 数据面影响 KPI**：峰值速率(200Gbps) · 用户面时延(0.1ms) · 可靠性(10⁻⁷) · 连接密度(10⁸/km²) · 能效(100×)
- **NGMN 警告**：5G 极端指标已被证明"难以交付"，6G 更激进目标商业可行性存疑
- **TPR 尚未最终批准**：20 项需求 2026-02 达成一致，待 2026-12 SG5 批准，期间值可能微调

### 阻塞 / 风险
- 无

### 明日要点
- D6：深调 `6g-data-plane-architecture-2025` + `imt-2030-framework-data-needs`
- 已完成 2 个 P0，按 plan 每深调 2 个后需调用 6g-wiki-curator T1+T3+T4 治理

---

## D4 · 2026-06-21（学术源铺面 + Queue 最终排序）

### 计划
- 调用 6g-source-radar 完成学术与会议铺面（10 个会议/期刊）
- 对 deep-dive-queue.md 做最终排序（A→C→B，P0→P1→P2）
- 为 P0 子题填写拟分配日（D5-D10）

### 完成
- 学术会议/期刊 10 张源卡全部创建：IEEE INFOCOM · ICC · Globecom · ACM SIGCOMM · USENIX NSDI · ACM MobiCom · VLDB · ACM SIGMOD/ICDE · IEEE Network/Comm. Magazine · arXiv
- deep-dive-queue.md 排序完成：62 条子题，按 A→C→B 类目 + P0→P1→P2 优先级排列
- 推荐子题清单中 26 个子题全部合并入队列表格
- P0 日程分配完毕（D5-D10 每日 2-4 个）
- wiki/sources/README.md 覆盖检查表全绿

### 关键产出
- wiki/sources/academia/ × 10 张源卡
- ops/deep-dive-queue.md v2（排序版）
- wiki/sources/README.md 全量更新

### 数据/关键发现
- **源卡总量达 31 张**：标准 11 + 厂商 8 + 学术 10 + 分析 2 = 全部类目满覆盖
- **Queue 规模**：62 条子题（P0=16 / P1=38 / P2=8）
- **按类目**：A 类 25 项 · C 类 13 项 · B 类 12 项 · 标准专项 12 项
- **P0 日程**：D5-D7 覆盖 6 个 A 类核心（2/天），D8-D9 覆盖 B+标准 P0，D10 交集专题日

### 阻塞 / 风险
- 无

### 明日要点
- D5：启动 deep-dive，取队首 P0 `imt-2030-usage-scenarios-data-needs` + `6g-kpi-20-requirements`
- 每深调 2 个后调用 6g-wiki-curator T1+T3+T4 治理

---

## D3 · 2026-06-21（源卡全量铺面：标准+厂商+分析）

### 计划
- 调用 6g-source-radar 全量铺面 标准组织 11 张 + 厂商 8 张 + 分析机构 2 张
- 每张源卡填 contact_topics、search_aliases、key_documents

### 完成
- 标准组织 11 张源卡全部创建：ITU-R · 3GPP · ETSI · IEEE · O-RAN Alliance · NGMN · TM Forum · 5G-IA/SNS JU · Hexa-X · Next G Alliance · IMT-2030 推进组
- 厂商 8 张源卡全部创建：华为 · 中兴 · 爱立信 · 诺基亚 · 三星 · NTT DoCoMo · Intel · 思科
- 分析机构 2 张源卡创建：Gartner · Forrester
- wiki/sources/README.md 覆盖检查表更新

### 关键产出
- wiki/sources/standards/ × 11 张源卡
- wiki/sources/vendors/ × 8 张源卡
- wiki/sources/analysts/ × 2 张源卡
- wiki/sources/README.md 覆盖率更新

### 数据/关键发现
- D3 目标（标准 11 + 厂商 8 + 分析 2 = 21 张）已 100% 完成
- 每张源卡含 3-5 条 search_aliases，可直接用于 deep-dive 的定向搜索
- 学术源（10 个会议/期刊）留待 D4 铺面
- 覆盖率：标准 11/11 ✅ | 厂商 8/8 ✅ | 分析 2/2 ✅ | 学术 0/10 ⬜

### 阻塞 / 风险
- 无

### 明日要点
- D4：调用 6g-source-radar 完成学术与会议铺面（10 个会议/期刊）
- D4：汇总 deep-dive-queue 排序，标记 P0/P1/P2 优先级
- D4：准备进入 D5 deep-dive 阶段

---

## D2 · 2026-06-20（B+C 类概念 + 概念地图 v1）

### 计划
- 调用 6g-onboarding 完成 B 类（数据编织侧 7 项）骨架卡片
- 调用 6g-onboarding 完成 C 类（交集 4 项）骨架卡片
- 刷新概念地图为 v1 全量版

### 完成
- B 类 7 张 concept 草稿卡片全部创建
- C 类 4 张 concept 草稿卡片全部创建
- Glossary 新增 10 条术语（data-fabric, data-mesh, active-metadata, knowledge-graph, data-virtualization, data-orchestration, federated-learning, differential-privacy, mec, tm-forum）
- 概念地图 v1 全量刷新（含 B 类内部协作链、C 类交集连线、研究空白标注）
- deep-dive-queue 累计子题入队

### 关键产出
- wiki/concepts/ × 11 张新卡片（B7 + C4）
- wiki/glossary/ × 10 条新术语
- wiki/concepts/README.md 概念地图 v1

### 数据/关键发现
- **B 类核心洞察**：数据编织七大能力形成"语义发现(KG) → 统一访问(虚拟化) → 自动流转(编排)"协作链，主动元数据是驱动引擎
- **Gartner vs Forrester**：前者侧重技术驱动（元数据分析+自动化），后者侧重业务价值（实时可信访问）
- **数据编织 vs 数据网格**：核心区分在治理模式（集中 vs 联邦），行业趋势是混合互补
- **C 类研究空白发现**：
  - `data-fabric-for-ai-native-6g` 文献极度稀缺，属开拓性议题（最具原创价值方向）
  - `privacy-preserving-data-fabric` 中 PETs 与 Data Fabric 的架构级融合缺乏系统性研究
  - 边缘数据编织在 ETSI MEC 标准体系中尚无对应规范
- **C 类已有实证**：TM Forum Catalyst C23.0.517 验证电信数据编织可降运营成本 51%

### 阻塞 / 风险
- 无

### 明日要点
- D3：调用 6g-source-radar 全量铺面（标准 11 + 厂商 8 + 分析机构 2）
- 每张源卡填 contact_topics、search_aliases、key_documents

---

## D1 · 2026-06-20（A 类概念入门）

### 计划
- 调用 6g-onboarding 完成 A 类（6G 数据面侧 9 项）骨架卡片
- 每张卡填最小定义（≤100 字），标待深挖子题
- 同步创建 glossary 术语条目

### 完成
- 9 张 A 类 concept 草稿卡片全部创建（draft 状态）
- 11 条 glossary 术语条目创建
- deep-dive-queue 汇入 27 个待深挖子题（P0×6 / P1×17 / P2×4）
- concepts/README.md 概念地图更新（新增概念间关系连线）

### 关键产出
- wiki/concepts/6g-overview.md
- wiki/concepts/6g-data-plane.md
- wiki/concepts/user-plane-evolution.md
- wiki/concepts/ai-native-air-interface.md
- wiki/concepts/ran-architecture-evolution.md
- wiki/concepts/network-data-analytics.md
- wiki/concepts/digital-twin-network.md
- wiki/concepts/isac.md
- wiki/concepts/non-terrestrial-network.md
- wiki/glossary/ × 11 条（6g, imt-2030, upf, gtp-u, ai-native-air-interface, o-ran, nwdaf, ai-ran, digital-twin-network, isac, ntn）

### 数据/关键发现
- 6G（IMT-2030）已于 2026-02 完成 20 项技术性能需求定义
- 华为提出 DaaS（数据即服务）概念，Hexa-X-II 定义四平面架构（数据面/智能面/计算面/安全面）
- 3GPP SA2 正讨论 6G 数据框架（WT#5）但尚未标准化
- GTP-U 灵活性不足已被识别为 6G 瓶颈，替代方案含 SRv6/IETF MUP
- AI-RAN Alliance（2024 MWC 成立）推动 GPU 共享 RAN+AI 推理
- ISAC 感知数据量可能超过通信数据本身，对数据面是全新高吞吐流量源
- NTN 长时延（20-40ms）要求数据面协议栈全面自适应

### 阻塞 / 风险
- company-context.md 仍全占位（不影响 D1-D10，但 D12 §8 需要填充）

### 明日要点
- D2：完成 B 类（数据编织侧 7 项）+ C 类（交集 4 项）概念骨架
- 调用 6g-wiki-curator 做首次治理（T1 + T7）
- 刷新概念地图 v1

---

## D0 · YYYY-MM-DD（工程初始化）

### 完成
- 工程目录骨架
- 6 个技能 SKILL.md
- Wiki / research / analysis / reports / ops 模板
- 两周路线 ops/plan.md

### 阻塞 / 风险
- 无

### 配置变更
- 2026-06-20 09:33 — Firecrawl MCP 已配置（~/.cursor/mcp.json，权限 600）
- 当前 MCP：Exa + Firecrawl 双引擎 + cursor-ide-browser

### 明日要点
- 启动 D1：6g-onboarding 完成 A 类必修概念骨架
