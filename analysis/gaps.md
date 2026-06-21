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
| P0 | 3GPP SA2 WT#5 KI#21 数据框架的具体方案提案内容（文稿需会员账号） | daas-interface-design §2 | 通过 3GPP 会员账号获取；持续跟踪 SA2#172+ | 等待中 |
| P1 | DO/DA/DCP 接口的具体信令流程和消息格式定义——华为专利有部分描述但缺完整规范 | daas-interface-design §4.1 | 追踪华为后续技术发布和 3GPP 提案 | 待解决 |
| P1 | DSAP 协议栈完整性能基准测试——当前仅 UE 侧上行延迟数据 | daas-interface-design §4.4 | 追踪 vivo/ZJU 后续发表 | 待解决 |
| P1 | 运营商对 DaaS 接口 API 范式（Pub/Sub vs SBA）的偏好调研 | daas-interface-design §4.2 | NGMN 后续发布或 SA2 讨论记录 | 待解决 |
| P2 | DaaS 接口安全认证机制（DO-DA 认证、数据消费者授权）具体方案 | daas-interface-design §6 | 跟踪 3GPP SA3 6G 安全研究 | 可补 |

## 类别

- **数据缺口**：找不到具体数字 / 实测数据
- **来源缺口**：观点只有单一来源
- **覆盖缺口**：某个必要维度没有调研
- **时效缺口**：只有 ≥ 2023 之前的数据
- **我司缺口**：缺乏对我司情况的对照

## 处理流程

1. 调研中发现缺口 → 立即登记到本文件
2. 周巡检（curator）→ 优先级排序
3. 报告写作前：P0 必须解决，P1 至少有一句话说明，P2 可作为"调研局限"披露
