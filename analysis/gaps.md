# Gaps：数据缺口与待核实清单

> 由 6g-deep-dive、6g-wiki-curator、6g-trend-synth 共同写入。
> 按优先级排序：P0（阻塞报告）/ P1（影响某节）/ P2（锦上添花）。
> 报告 §7.2 直接引用本文件。

## 清单

| 优先级 | 缺口 | 影响章节 | 建议补救 | 状态 |
|---|---|---|---|---|
| P1 | AIAC 场景 AI 模型数据流量定量估算缺乏公开研究 | imt-2030-usage-scenarios §4.5 | 追踪 3GPP SA2 6G 数据框架 WT#5 讨论 | 待解决 |
| P1 | ISAC 感知数据在核心网数据面的传输方案（多个竞争方案未定） | imt-2030-usage-scenarios §4.6 | 追踪 3GPP SA2/SA5 ISAC 架构研究 | 待解决 |
| P1 | 六个场景对应的数据类型（结构化/非结构化、流式/批量）无标准分类 | imt-2030-usage-scenarios §4 | 深调 6g-data-plane 子题时补充 | 待解决 |
| P2 | TPR 最终确认值待 2026-12 SG5 批准，当前值可能调整 | imt-2030-usage-scenarios §4 全部 | 2026-12 后更新 | 待解决 |
| P2 | Hexa-X-II D1.4 交付件具体场景需求数据未精读 | imt-2030-usage-scenarios §3 | 后续深调时精读该交付件 | 待解决 |
| P0 | TPR 草案中多项核心指标最终值标注 TBD（峰值速率、用户体验速率、时延具体数值），正式报告仅对 TIES 用户开放 | 6g-kpi-20-requirements §1 | 等待 2026-12 ITU-R SG5 批准后获取公开版报告 | 等待中 |
| P1 | 新增 7 项 TPR 中 5 项（AI/安全/韧性/互操作/覆盖）仅定性评估，缺乏公认量化方法论 | 6g-kpi-20-requirements §1 | 跟踪 Report ITU-R M.[IMT-2030.EVAL] 评估指南定义进展 | 等待中 |
| P1 | 3GPP Rel-21/22 如何将 ITU-R TPR 映射为具体 RAN/Core 技术规范尚不明确 | 6g-kpi-20-requirements §2 | 跟踪 3GPP RAN#106 6G Study Item (RP-243327) 后续输出 | 等待中 |
| P2 | 尚无公开文献系统分析 20 项 TPR 对 6G 数据面架构的逐项定量影响 | 6g-kpi-20-requirements §4 | 基于 topic 卡分析框架自行建模 | 可补 |
| P2 | IEEE Xplore 文章 "From Vision to Design Targets: TPR for IMT-2030" 全文未能提取 | 6g-kpi-20-requirements 来源 | 通过 IEEE 会员账号获取 DOI:11550739 | 可补 |
| P0 | 3GPP SA2 WT#5 数据框架技术报告正文（S2-2506446 等文稿内容），仅目录可见 | 6g-data-plane-architecture-2025 §4.3 | 通过 3GPP 会员账号获取；持续跟踪 SA2#172+ 会议 | 等待中 |
| P1 | 华为 DCP 端到端网络验证数据（目前仅消息转发原型，缺乏 RAN/CN 集成验证） | 6g-data-plane-architecture-2025 §4.1 | 追踪华为后续技术发布 | 待解决 |
| P1 | Qualcomm 用户面优先方案的 TCO 定量对比分析 | 6g-data-plane-architecture-2025 §4.2 | 追踪 Qualcomm 6G Foundry 系列后续文章 | 待解决 |
| P1 | 运营商对"独立数据面 vs 增强 UP"路线的具体偏好调研（NGMN 现有调研未涉及此级别细节） | 6g-data-plane-architecture-2025 §3.4 | NGMN 后续发布或 SA2 讨论记录 | 待解决 |
| P2 | 中国移动 DAN（分布式自治网络）实测性能数据 | 6g-data-plane-architecture-2025 §4.1 | 追踪中国移动研究院后续发表 | 待解决 |
| P1 | 6G DP 协议栈（DSAP/DPRB）标准化进展——仅华为/ZJU 论文描述，3GPP 尚未讨论 | imt-2030-framework-data-needs §4.3 | 跟踪 3GPP SA2 WT#5 后续输出 | 待解决 |
| P1 | AI 数据（模型参数/梯度）的定量流量估算——缺乏公开实测数据 | imt-2030-framework-data-needs §4.2 | 跟踪学术界分布式 ML 流量测量研究 | 待解决 |
| P1 | 四类数据（通信/感知/AI/管理）的 QoS 差异化框架——无标准化提案 | imt-2030-framework-data-needs §4.1 | 跟踪 3GPP SA2 WT#5 QoS 扩展讨论 | 待解决 |
| P2 | 数据面对能效的量化贡献——无公开研究分析 DP vs UP 能效对比 | imt-2030-framework-data-needs §4.5 | 基于 DP 原型数据自行估算 | 可补 |
| P2 | 数据市场化（DaaS 定价/数据合约）技术实现方案——TSDSI 提出概念但无标准化 | imt-2030-framework-data-needs §4.5 | 跟踪 TSDSI 和 3GPP SA5 数据暴露工作 | 可补 |
| P1 | SRv6 MUP vs GTP-U 大规模商用性能对比数据——SoftBank FWA 场景有限，缺乏高密度 eMBB 数据 | gtp-u-limitations-6g-alternatives §4.1 | 跟踪 SoftBank 扩展部署报告 | 待解决 |
| P1 | 3GPP 是否正式讨论 SRv6 替代 GTP-U——Deutsche Telekom IETF 123 提议后 3GPP CT/SA 反馈不公开 | gtp-u-limitations-6g-alternatives §2 | 跟踪 3GPP SA2/CT4 6G 讨论 | 待解决 |
| P1 | 多厂商 SRv6 MUP 互操作测试结果——目前仅 Arrcus/Broadcom 组合经验证 | gtp-u-limitations-6g-alternatives §6 | 跟踪 IETF plugfest 和运营商多厂商测试 | 待解决 |
| P2 | ANUP 概念的端到端安全影响分析——AN-UPF 融合后安全边界变化未充分讨论 | gtp-u-limitations-6g-alternatives §4.2 | 跟踪 IETF DMM WG 和 3GPP SA3 | 待解决 |
| P2 | SRv6 MUP 能耗对比数据——缺乏 SRv6 vs GTP-U 每比特能效对比实测 | gtp-u-limitations-6g-alternatives §6 | 学术文献追踪 | 可补 |
| P1 | 华为 DaaS（DO/DA/DCP）端到端 RAN+CN 集成验证数据——目前仅有消息代理转发原型 | ai-native-data-plane-status §4.1 | 追踪华为后续技术发布和 3GPP 提案 | 待解决 |
| P1 | AI-RAN 共享基础设施下 AI 负载对 RAN 通信 QoS 干扰的定量评估——缺乏公开实测数据 | ai-native-data-plane-status §6 | 追踪 AI-RAN Alliance 测试方法论工作组输出 | 待解决 |
| P1 | In-network ML 从流量分类扩展到通信层决策（调度/功控）的可行性论证——学术原型仅限 traffic classification | ai-native-data-plane-status §4.2 | 追踪 SIGCOMM/NSDI 后续研究 | 待解决 |
| P2 | 不同 AI 原生数据面方案（DaaS/dApp/P4 ML）间的统一性能对比基准——缺乏 benchmark | ai-native-data-plane-status §4 | 学术/标准组织定义评估框架 | 可补 |
| P2 | 端到端学习收发机在商用硬件上的能效与吞吐对比实测——仅有仿真数据 | ai-native-data-plane-status §4.4 | 追踪 SDR-based OTA 实验 | 可补 |
| P1 | 3GPP SA2 WT#5 对数据面 AI 能力的具体需求提案——需会员账号获取文稿 | ai-native-data-plane-status §2 | 持续跟踪 SA2#172+ 会议 | 等待中 |
| P0 | 3GPP SA2 WT#5 KI#21 数据框架的具体方案提案内容（文稿需会员账号） | daas-interface-design §2 | 通过 3GPP 会员账号获取；持续跟踪 SA2#172+ | 等待中 |
| P1 | DO/DA/DCP 接口的具体信令流程和消息格式定义——华为专利有部分描述但缺完整规范 | daas-interface-design §4.1 | 追踪华为后续技术发布和 3GPP 提案 | 待解决 |
| P1 | DSAP 协议栈完整性能基准测试——当前仅 UE 侧上行延迟数据 | daas-interface-design §4.4 | 追踪 vivo/ZJU 后续发表 | 待解决 |
| P1 | 运营商对 DaaS 接口 API 范式（Pub/Sub vs SBA）的偏好调研 | daas-interface-design §4.2 | NGMN 后续发布或 SA2 讨论记录 | 待解决 |
| P2 | DaaS 接口安全认证机制（DO-DA 认证、数据消费者授权）具体方案 | daas-interface-design §6 | 跟踪 3GPP SA3 6G 安全研究 | 可补 |
| P1 | Samsung M-UP 大规模性能验证——当前仅 Open5GS 仿真，缺乏商用级实测 | user-plane-evolution-upf-to-6g §4.3 | 跟踪 Samsung 后续发表和 3GPP 贡献 | 待解决 |
| P1 | dUPF 多厂商互操作数据——NVIDIA/Cisco/6WIND 各自实现，无公开互操作报告 | user-plane-evolution-upf-to-6g §4.1 | 跟踪 MWC/3GPP plugfest | 待解决 |
| P1 | 3GPP Rel-20 6G RAN 用户面协议研究进展——RAN2 WG 刚启动，方案不公开 | user-plane-evolution-upf-to-6g §2 | 跟踪 RAN2 后续会议 | 待解决 |
| P1 | 可编程 UPF 商用 TCO 对比——P4/SmartNIC vs 纯软件 UPF 的定量 TCO 分析缺失 | user-plane-evolution-upf-to-6g §4.2 | 跟踪厂商/运营商部署报告 | 待解决 |
| P2 | ANUP 对网络切片用户面隔离的影响分析 | user-plane-evolution-upf-to-6g §4.3 | 跟踪 IETF DMM WG 和 3GPP SA2 | 待解决 |
| P2 | 6G 用户面各演进路径的每比特能效对比实测数据 | user-plane-evolution-upf-to-6g §6 | 学术文献追踪 | 可补 |

| P1 | SA2 各 KI 的 Penholder 公司清单（反映各厂商在数据框架中的投入方向） | 3gpp-rel-19-20-data-architecture-status §3 | 跟踪 SA2 后续会议公开文稿 | 待解决 |
| P1 | FS_6G_ARC TR 23.801 正文内容（截至 V0.3.0 仅目录/框架可见） | 3gpp-rel-19-20-data-architecture-status §4.2 | 通过 3GPP 会员账号获取 | 等待中 |
| P1 | SA5 FS_6G_OAM 与 SA2 WT#5 在数据管理/数据收集上的分工协议 | 3gpp-rel-19-20-data-architecture-status §2 | 跟踪 SA2/SA5 联合讨论 | 待解决 |
| P1 | RAN3 6G RAN-CN 接口研究中对数据收集通道的具体提案 | 3gpp-rel-19-20-data-architecture-status §4 | 跟踪 RAN3 后续会议 | 待解决 |
| P2 | SA6 FS_6G_APP 中 GenAI 使能层与数据框架的接口定义 | 3gpp-rel-19-20-data-architecture-status §2 | 跟踪 SA6 FS_6G_APP 进展 | 待解决 |
| P1 | Gartner Hype Cycle for Data Management 2025 中 Data Fabric 具体定位（仅获取 2024 版） | data-fabric-definition-and-capabilities §2 | 等待 Gartner 2025 HC 发布或通过订阅获取 | 等待中 |
| P1 | Forrester Wave Data Fabric Platforms Q4 2025 具体供应商排名（付费报告） | data-fabric-definition-and-capabilities §3 | 通过 Forrester 订阅获取 | 等待中 |
| P1 | 电信行业 Data Fabric 具体部署案例数量和 ROI 数据 | data-fabric-definition-and-capabilities §3.3 | 跟踪 Google Cloud / Amdocs / Ericsson 案例发布 | 待解决 |
| P1 | 中国市场数据编织供应商格局（华为/阿里云/腾讯/中兴在 Data Fabric 领域的定位） | data-fabric-definition-and-capabilities §3 | 跟踪国内分析机构报告 | 待解决 |
| P1 | 3GPP / O-RAN 对 Data Fabric 的标准化条款细节 | data-fabric-definition-and-capabilities §2 | 跟踪 3GPP SA2/SA5 和 O-RAN 工作组 | 待解决 |
| P1 | 2025-2026 年主动元数据工具市场成熟度最新评估 | data-fabric-definition-and-capabilities §4.1 | 跟踪 Gartner/Forrester 主动元数据相关报告 | 待解决 |
| P1 | 6G 数据面场景中 Mesh+Fabric 混合架构的基准性能数据（延迟/吞吐量） | data-fabric-vs-data-mesh §4 | 跟踪学术界/Nokia/Ericsson 性能验证 | 待解决 |
| P1 | 中国电信运营商（移动/联通/电信）对 Data Mesh / Data Fabric 的采纳情况 | data-fabric-vs-data-mesh §3 | 跟踪运营商技术发布 | 待解决 |
| P2 | Gartner "80% by 2028" Fabric+Mesh 互补预测的方法论和统计基础未公开 | data-fabric-vs-data-mesh §2 | Gartner 付费报告可能披露 | 待解决 |
| P2 | Data Mesh 在超大规模实时流数据场景（如 6G RAN 毫秒级遥测）的适用性验证 | data-fabric-vs-data-mesh §4 | 学术/标准组织验证 | 可补 |
| P1 | 中国运营商（移动/联通/电信）Data Fabric 部署案例缺失——无公开来源 | data-fabric-in-telecom-early-cases §3 | 跟踪运营商技术发布和国内会议 | 待解决 |
| P1 | CSP Data Fabric 量化 ROI 方法论不透明——几乎所有数据来自供应商/咨询公司宣传 | data-fabric-in-telecom-early-cases §矛盾 | 等待独立分析机构专项报告 | 待解决 |
| P1 | 网络域 Data Fabric 虚拟化层实时性 benchmark——无公开数据对比 RAN 遥测延迟影响 | data-fabric-in-telecom-early-cases §4.2 | 学术或厂商实测 | 待解决 |
| P1 | NWDAF 与 Data Fabric 标准化集成规范——3GPP 未发布相关 TR/TS | data-fabric-in-telecom-early-cases §4.3 | 跟踪 3GPP SA2/SA5 | 待解决 |
| P2 | 电信 Data Fabric 失败案例报告缺失——幸存者偏差风险 | data-fabric-in-telecom-early-cases §6 | 行业匿名调研 | 可补 |

| P1 | ETSI ZSM GS 029 "Data Management Agent" 规范正文内容——仅有工作项描述，无草案 | data-fabric-for-ai-native-6g §2 | 跟踪 ETSI ZSM 后续发布 | 等待中 |
| P1 | 6G 场景下数据编织虚拟化层的端到端延迟影响——无公开 benchmark 数据 | data-fabric-for-ai-native-6g §6 | 学术/厂商实测 | 待解决 |
| P1 | CANDIL 联邦数据编织原型在电信规模（百万级数据源）下的性能验证 | data-fabric-for-ai-native-6g §4 | 跟踪 CANDIL/Telefónica 后续发表 | 待解决 |
| P1 | 数据编织（管理层）与 DaaS 数据面（网络层）之间的接口定义——无标准化提案 | data-fabric-for-ai-native-6g §4.3 | 跟踪 3GPP SA2 / ETSI ZSM 讨论 | 待解决 |
| P2 | 6G-TWIN / ROBUST-6G 中 data fabric 组件的实现细节和性能数据 | data-fabric-for-ai-native-6g §4 | 跟踪 EU 项目交付件 | 待解决 |
| P2 | 中国运营商对数据编织/数据网格在网络域的采纳意向——无公开信息 | data-fabric-for-ai-native-6g §3 | 跟踪运营商技术发布 | 待解决 |
| P2 | 知识图谱自动构建在电信网络本体场景的成熟度评估 | data-fabric-for-ai-native-6g §4.1 | 学术文献追踪 | 可补 |

| P1 | 3GPP SA5 DMFW 与 SA2 WT#5 在数据治理（访问控制/数据暴露）上的正式分工协议 | cross-domain-data-governance-6g §2 | 跟踪 SA2/SA5 联合讨论或 TSG SA 层面协调 | 待解决 |
| P1 | 跨域数据治理框架在实时 RAN 遥测场景的端到端性能基准——仅 Fraunhofer HHI 有光网络测试数据 | cross-domain-data-governance-6g §4 | 跟踪学术/厂商 RAN 场景测试 | 待解决 |
| P1 | 中国运营商 6G 数据治理技术路线——缺乏公开英文文献 | cross-domain-data-governance-6g §3 | 跟踪国内会议/YD/T 标准发布 | 待解决 |
| P1 | 数据编织架构与 3GPP DMFW/NWDAF 的集成规范——不存在任何标准化文档 | cross-domain-data-governance-6g §4 | 跟踪 3GPP SA5 和厂商提案 | 待解决 |
| P2 | Nokia "Built-In Data Governance & Discovery" 6G 方案完整内容——仅有 EuCNC 2025 演讲标题 | cross-domain-data-governance-6g §3 | 跟踪 Nokia 后续发表 | 待解决 |
| P2 | 联邦治理模式在超大规模（100+ 域/10,000+ 数据源）环境下的可扩展性验证 | cross-domain-data-governance-6g §6 | 学术/标准组织验证 | 可补 |
| P2 | ETSI GS PDL 034 跨域数据治理规范具体技术内容——仍在制定中 | cross-domain-data-governance-6g §2 | 跟踪 ETSI PDL 发布 | 等待中 |

| P0 | TR 23.801-01 Section 5.21（KI#21）和 Section 6.21（Solutions to KI#21）完整正文——V0.7.0 已 16.8 MB 但需会员账号 | 3gpp-sa2-6g-data-framework-wt5 §4 | 通过 3GPP 会员账号获取 | 等待中 |
| P0 | WT#5 Penholder 公司及其负责方向——Penholder assigned list for solution phase_r5.docx 需会员账号 | 3gpp-sa2-6g-data-framework-wt5 §3 | 通过 3GPP 会员账号获取 | 等待中 |
| P1 | SA2#175-AH-e（2026.06.24-30）WT#5 讨论结果和方案合并进展 | 3gpp-sa2-6g-data-framework-wt5 §2 | 会议结束后跟踪 | 待解决 |
| P1 | 各公司提交的 KI#21 具体方案提案内容（S2-26xxxxx 系列文稿） | 3gpp-sa2-6g-data-framework-wt5 §4 | 持续跟踪 SA2 会议 | 待解决 |
| P1 | CT WG 6G 数据框架协议层面研究进展（TR 29.840/29.841 于 2026.03 启动） | 3gpp-sa2-6g-data-framework-wt5 §2 | 跟踪 CT1/CT3 会议 | 待解决 |

## 类别

- **数据缺口**：找不到具体数字 / 实测数据
- **来源缺口**：观点只有单一来源
- **覆盖缺口**：某个必要维度没有调研
- **时效缺口**：只有 ≥ 2023 之前的数据
- **我司缺口**：缺乏对我司情况的对照

| P1 | Rel-22 正式启动时间和范围讨论——3GPP 尚未在任何公开文档中提及 | 3gpp-6g-timeline-rel22-23 §2 | 跟踪 TSG 全会后续议题 | 待解决 |
| P1 | FS_6G_ARC 2026 下半年加速计划——SA2 ad-hoc 日程和 WT#5 完成进度 | 3gpp-6g-timeline-rel22-23 §2 | 跟踪 SA2#175+ 会议 | 待解决 |
| P1 | TSG RAN#113（2026.09 马德里）迁移架构决策结果——直接影响数据面协议设计 | 3gpp-6g-timeline-rel22-23 §3 | 2026.09 会后跟踪 | 等待中 |
| P1 | Rel-21 6G WI 候选清单——数据框架是否获得独立 WI | 3gpp-6g-timeline-rel22-23 §4 | 跟踪 2027.03 Package 批准 | 等待中 |
| P2 | ITU-R WP 5D 对 3GPP 首次提交（2027 中）的评估反馈 | 3gpp-6g-timeline-rel22-23 §5 | 跟踪 WP 5D 54th+ 会议 | 等待中 |
| P2 | 各公司在 CT 用户面研究（TR 29.841）中的具体提案方向 | 3gpp-6g-timeline-rel22-23 §4 | 跟踪 CT4 后续会议 | 待解决 |

## trend-synth 新增缺口（2026-06-25）

| 优先级 | 缺口 | 影响章节 | 建议补救 | 状态 |
|---|---|---|---|---|
| P1 | 终端侧轻量元数据管理方案——无已知研究或提案 | core-intersection 矩阵 终端/NTN 行 | 跟踪 3GPP RAN 6G 终端能力研究 | 待解决 |
| P1 | RAN 域数据虚拟化的性能可行性验证——10 Gbps+ 吞吐 / <1ms 延迟下的虚拟化方案 | core-intersection 矩阵 RAN 行 | 跟踪学术界流式虚拟化研究 | 待解决 |
| P1 | 四套数据管理框架（NWDAF/DaaS/ZSM/O-RAN）互操作规范——完全不存在 | trend-ai-native-data-management | 跟踪 3GPP SA2 WT#5 和跨组织协调 | 待解决 |
| P1 | 电信专用数据编织产品的延迟/吞吐量 benchmark——IT 级 Fabric vs 电信级需求差距未量化 | trend-data-fabric-telecom-adoption | 跟踪 Denodo/Amdocs/Google TDF 性能报告 | 待解决 |
| P1 | Mesh-on-Fabric 混合架构在电信网络的可行性验证——无已知原型 | trend-mesh-on-fabric-hybrid | 跟踪 DT/AWS/TM Forum 进展 | 待解决 |
| P2 | ISAC 感知数据的数据编织集成方案——数据类型特殊（高维度、高频率、隐私敏感） | trend-cross-domain-governance | 跟踪 3GPP ISAC 研究和 ETSI ISG 讨论 | 待解决 |
| P2 | 跨标准组织（3GPP/ETSI/O-RAN/TM Forum）的数据管理术语统一进展 | trend-standardization-race | 跟踪联合研讨会和交叉引用文件 | 待解决 |
| P2 | SRv6 MUP 双栈过渡方案（与 GTP-U 共存）的设计详情和 OPEX 估算 | trend-gtp-u-sunset | 跟踪 IETF MUP WG 和 3GPP CT | 待解决 |

## 处理流程

1. 调研中发现缺口 → 立即登记到本文件
2. 周巡检（curator）→ 优先级排序
3. 报告写作前：P0 必须解决，P1 至少有一句话说明，P2 可作为"调研局限"披露
