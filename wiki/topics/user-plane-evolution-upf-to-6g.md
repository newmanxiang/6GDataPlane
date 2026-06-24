---
title: 用户面从 UPF 到 6G 的演进路径
title_en: User Plane Evolution from UPF to 6G
slug: user-plane-evolution-upf-to-6g
category: topic
status: reviewed
confidence: high
sources:
  - https://www.3gpp.org/specifications-technologies/releases/release-20
  - https://www.3gpp.org/ftp/Information/presentations/presentations_2026/2026_04_Rel19.pdf
  - https://datatracker.ietf.org/doc/html/draft-zzhang-dmm-mup-evolution-09
  - https://developer.nvidia.com/blog/accelerated-and-distributed-upf-for-the-era-of-agentic-ai-and-6g/
  - https://research.samsung.com/blog/RAN-CN-Convergence-Towards-the-Next-Generation-Networks
  - https://www.nokia.com/6g/6g-system-architecture-where-innovation-meets-evolution-for-a-more-sustainable-and-connected-world/
  - https://www.ericsson.com/en/blog/2026/6/blog-6g-architecture-standalone-simpler-evolution-5g
  - https://arxiv.org/html/2503.09430
  - https://www.eurecom.fr/publication/7496/download/comsys-publi-7496.pdf
  - https://www.itu.int/rec/dologin_pub.asp?id=T-REC-Y.3169-202512-I!!PDF-E&lang=s&type=items
  - https://www.interdigital.com/post/paving-the-path-to-6g-key-takeaways-for-3gpp-release-20
  - https://publica.fraunhofer.de/handle/publica/485713
  - https://www.huawei.com/en/huaweitech/future-technologies/data-plane-design-ai-native-6g-networks
  - https://www.ngmn.org/wp-content/uploads/250218_Network_Architecture_Evolution_towards_6G_V1.0.pdf
related:
  - user-plane-evolution
  - 6g-data-plane
  - 6g-data-plane-architecture-2025
  - gtp-u-limitations-6g-alternatives
  - daas-interface-design
tags: [UPF, 用户面, CUPS, 6G, 演进, SBA, 可编程数据面, dUPF, ANUP, M-UP]
last_verified: 2026-06-22
owner: agent
---

# 用户面从 UPF 到 6G 的演进路径

## 核心结论（执行摘要）

5G UPF 向 6G 用户面的演进呈现清晰的五阶段路径：**CUPS 确立 → 分布式部署（dUPF）→ 可编程加速 → RAN-CN 融合 → 数据服务化范式转变**。当前处于第三阶段向第四阶段过渡期——3GPP Rel-19 已完成 UPEAS_Ph2（UPF 曝光与 SBA 扩展）和 AI 数据采集协议标准化，Rel-20（2025.6 启动）正式开展 6G 架构研究；产业侧 NVIDIA dUPF 已在 Grace+BF3 平台实现 100 Gbps/25μs 延迟（2025.10），SoftBank SRv6 MUP 完成首个商用部署（2025.12）。**核心分歧在于"融合路线"（Samsung M-UP/EURECOM IUP 消除 N3 隧道）vs "服务化路线"（华为 DaaS 独立数据面 / Qualcomm UP-first）**，预计 2027 年 3GPP Rel-21 规范化阶段形成最终结论。（信心：高）

## 1. 现状定义

**用户面演进**是指移动网络中承载用户数据转发的功能实体（UPF）及其协议栈从 4G 的耦合网关，经 5G 完整 CUPS 解耦，向 6G 多维增强的代际变迁过程。

本题关注"演进路径和里程碑"——即 UPF 如何分阶段向 6G 目标形态逼近，区别于已有 `gtp-u-limitations-6g-alternatives`（聚焦协议替代方案对比）和 `6g-data-plane-architecture-2025`（聚焦 6G 数据面架构提案对比）。

**五阶段演进框架：**

| 阶段 | 时间窗 | 核心变化 | 标志事件 |
|------|--------|---------|---------|
| 1. CUPS 确立 | 2017–2020 | CP/UP 分离从改造到原生 | Rel-14 CUPS → Rel-15 UPF |
| 2. 分布式部署 | 2020–2025 | UPF 从集中走向边缘 | Rel-17 MEC、dUPF 概念 |
| 3. 可编程加速 | 2023–2026 | 硬件加速 + SBA 扩展 | P4-UPF、UPEAS、SmartNIC |
| 4. RAN-CN 融合 | 2025–2028 | 消除 N3 隧道 / SRv6 替代 GTP-U | ANUP/IUP/M-UP、Rel-20/21 |
| 5. 数据服务化 | 2028–2030+ | 从包转发到 DaaS | 6G Rel-21+ 规范 |

## 2. 标准与组织动态（近 3 年）

| 时间 | 里程碑 | 阶段 |
|------|--------|------|
| 2023-01 | GTI 发布 6G Native AI 白皮书，首次系统化提出数据面概念 | 5 |
| 2024-07 | **RFC 9433** 发布：SRv6 Mobile User Plane（IETF 标准轨道） | 4 |
| 2024-12 | ITU-T Y.3169 批准：UPF 容器化资源效率优化（面向 IMT-2020 及以后） | 2 |
| 2025-03 | 3GPP Rel-19 完成 **UPEAS_Ph2**：UPF SBA 曝光扩展（N4 能力增强、DPI、payload header 处理） | 3 |
| 2025-03 | 3GPP Rel-19 完成 **PAIDC_UPF**：AI 数据从 UPF 采集协议（增强 UPF 事件曝光效率） | 3 |
| 2025-03 | 3GPP Rel-19 完成 **eEDGE_5GC_Ph3**：边缘计算第三阶段（轻量级本地卸载、N6 延迟感知 UPF 选择） | 2 |
| 2025-06 | **3GPP SA2 批准 6G 架构研究项 FS_6G_ARC**（TSG#108），WT#5 聚焦"统一数据框架" | 5 |
| 2025-06 | 3GPP Rel-20 scope 冻结：含 6G RAN 架构、用户面协议设计研究 | 4 |
| 2025-07 | Deutsche Telekom 在 IETF 123 正式提议 3GPP 6G 研究 SRv6 替换 GTP-U | 4 |
| 2025-10 | NVIDIA 发布 dUPF 参考实现（Grace+BF3，100Gbps，25μs） | 3 |
| 2025-12 | **SoftBank 实现 SRv6 MUP 5G 首个商用部署** | 4 |
| 2026-02 | 6WIND/Red Hat/Intel MWC 展示 SmartNIC 上云原生 dUPF | 3 |
| 2026-03 | Ericsson+Qualcomm 宣布 6G 商用路线图合作（2029+ 目标） | 4/5 |
| 2026-06 | Ericsson 发布 6G SA-only 架构博客：6G CN 基于 5GC 演进，UPF 保持用户面锚点 | 4 |
| 2026-06 | NGMN 发布《6G Architecture and Migration Options》：MRSS 为主迁移机制 | 4 |

## 3. 关键玩家

### 3.1 分布式 UPF / 硬件加速阵营

- **NVIDIA**：AI Aerial 平台 dUPF 参考实现（Grace+BF3 DPU）；联合 T-Mobile/Cisco/MITRE 的 6G AI-WIN 倡议
- **Cisco**：拥抱 dUPF 架构 + NVIDIA DOCA 加速作为 6G AI 核心网基石
- **6WIND**：高性能 UPF 软件，与 Red Hat/Intel 展示 SmartNIC dUPF
- **Napatech**：Link-Inline SmartNIC UPF 卸载，<4μs 快速路径延迟
- **Intel**：Netsec Accelerator 参考设计；前 Barefoot Tofino P4 芯片

### 3.2 RAN-CN 融合 / 用户面重构

- **Samsung**：Merged UP（M-UP）概念——合并 RAN UP 和 CN UP 为单一 NF，实测 CPU 处理量显著降低
- **EURECOM**：IUP（集成可编程用户面）——IDFC 子层替代 SDAP+GTP-U，消除 N3 隧道
- **NTT DOCOMO + Nokia**：In-Network Computing（INC）/ ISAP 平台，将计算集成到 UPF
- **Juniper（Zhaohui Zhang）**：IETF ANUP 提案，AN-UPF 完全集成消除 N3

### 3.3 标准演进主导者

- **Ericsson**：6G CN = 5GC 演进；SA-only 架构；保持 UPF 为用户面锚点
- **Nokia**：6G 模块化协议设计；新 6G SMF/AMF 为软件升级；SBA 扩展至 RAN-Core 接口
- **Qualcomm**：Rel-20 完成 5G-Advanced + 6G 研究启动；用户面优先设计；单一可扩展空口

### 3.4 协议替代推动者

- **SoftBank**：SRv6 MUP 首个商用部署；MUP 架构主要推动者
- **Deutsche Telekom**：正式推动 3GPP 6G 纳入 SRv6 替换 GTP-U

### 3.5 数据面范式转变

- **华为**：DaaS 独立数据面（DO/DA/DCP）——从 UPF 包转发到数据编排服务
- **中国移动**：三体四层五面架构，数据面独立于用户面

## 4. 技术机制

### 4.1 阶段 2：分布式 UPF（dUPF）

dUPF 将 UPF 从集中核心推向网络边缘（3GPP TS 23.501 §6.2.5），实现：
- **本地分流（LBO）**：AI/边缘业务流量就近卸载，无需回传
- **容器化部署**：ITU-T Y.3169 规范了容器化 UPF 在分布式边缘的弹性编排
- **多层 PSA 模型**：UL-CL（上行分类器）/ IPv6 多宿主实现选择性流量分流

NVIDIA dUPF 参考实现关键指标：
- 平台：Grace CPU + BF3 DPU（Supermicro 1U）
- 仅 2 CPU 核心实现 100 Gbps 线速转发、零丢包
- DOCA Flow 硬件加速：PDR/QER/URR/FAR 全卸载
- 延迟：25 μs（边缘 AI 推理场景）

### 4.2 阶段 3：可编程 UPF + SBA 扩展

**可编程加速技术栈对比：**

| 技术 | 代表实现 | 特点 | 吞吐 |
|------|---------|------|------|
| P4 交换机 | HiP4-UPF, SD-Fabric | 全流水线硬件处理 | 100 Gbps, <1μs |
| SmartNIC (P4) | Napatech, Netronome | NIC 内联处理 | 2×100G 线速 |
| DPDK/VPP | 6WIND, AMD EPYC | 用户态轮询 | 高但耗 CPU |
| eBPF/XDP | eUPF (NgKore) | 内核态可编程 | 接近 DPDK |
| DPU | NVIDIA BF3, Intel IPU | 控制+数据面卸载 | 100 Gbps |

**3GPP Rel-19 UPEAS_Ph2 关键增强：**
- UPF N4 能力扩展：DPI 级包检测、运营商自定义参数
- Payload Header 处理：应用与 UPF 之间端到端带内信令
- SBI 化 UPF 发现：基于 IP 的 UPF 发现机制
- Fraunhofer FOKUS 已实现 UPF 的 SBI 控制接口原型，替代 PFCP

### 4.3 阶段 4：RAN-CN 融合

三种主要路径消除 N3 隧道和 GTP-U：

**（1）ANUP（Integrated AN/UPF）**— IETF draft-zzhang-dmm-mup-evolution
- AN（CU）与 UPF 集成为单一网络功能
- 消除 N3 隧道和 GTP-U 封装/解封装
- 信令简化：从 7 步减为 2 步
- 天然本地分流（ANUP 内嵌路由功能）

**（2）IUP（Integrated User Plane）**— EURECOM (arXiv 2503.09430)
- IDFC 子层替代 SDAP，集成 UPF 功能到 RAN
- 可编程数据通路：从 IP 流到无线电资源端到端控制
- 实测：消除 GTP-U 处理开销，降低 L2 延迟

**（3）M-UP（Merged UP）**— Samsung Research
- 合并 RAN 高层 UP 和 CN UP 为单一 NF
- IP 包直接映射 DRB（跳过 QoS Flow 中间步骤）
- 实测 CPU 处理周期/包显著降低，系统吞吐提升

### 4.4 阶段 5：从 UPF 到 DaaS

华为提出从 UPF 包转发范式向数据服务化（DaaS）的转变：
- **现有 UPF**：会话导向（PDU Session → GTP-U 隧道 → QoS Flow → DRB）
- **6G 数据面**：数据拓扑任意（多对多）、非连接数据（AI/感知）、Pub/Sub 模式
- **关键转变**：UPF 处理连接性数据 → DP 处理非连接性数据（AI 梯度、感知原始数据等）

## 5. 趋势驱动力

- **AI 业务爆发**：Mobile AI 流量上行占 26%（vs 传统 8%），AI 推理需边缘卸载 → 驱动 dUPF + AI-DN
- **6G KPI 跃升**：峰值 >100 Gbps、延迟 <1ms → 传统集中式 UPF 不可持续
- **运营商降本**：NGMN 78% 运营商将成本效率列为 6G 首要目标 → SRv6 MUP 消除专用移动网设备
- **云原生深化**：Kubernetes 编排分布式 UPF 成为标配 → ITU-T Y.3169 规范容器化 UPF
- **频谱共享迁移**：MRSS（5G/6G 动态共频）需要 SA-only 架构 → 倒逼用户面统一演进
- **AI-RAN 兴起**：vRAN + AI 共址部署需 localized vUPF → NTT DOCOMO 白皮书明确提出 vUPF 与 AI 工作负载共存

## 6. 批评与风险

- **融合路线风险**：M-UP/IUP/ANUP 消除 N3 后安全边界模糊——RAN 与 CN 的信任域合并需重新定义安全模型
- **碎片化风险**：分布式 UPF（dUPF）、融合 UP（M-UP）、独立数据面（DaaS）三条路线并行，可能重演 5G NSA/SA 多选项混乱
- **演进 vs 革命之争**：Ericsson 坚持"6G CN 基于 5GC 演进、UPF 保持锚点"；Samsung/EURECOM 主张重构——3GPP 需在 Rel-21 前决断
- **硬件加速碎片化**：P4/DPDK/eBPF/DPU 多路径竞争，缺乏统一 API 标准（仅 rte_flow 有部分共识）
- **ANUP 标准化路径不清晰**：目前仅为 IETF 个人草案，3GPP 尚未正式讨论 AN-UPF 融合
- **DaaS 落地差距**：华为 DCP 原型仅验证消息转发延迟（2ms），端到端网络集成验证缺失
- **运营商投资保护**：已部署 5G UPF 数以千计，任何激进替换方案面临巨大迁移成本

## 7. 我司相关性（占位）

> 待 6g-insight-report 阶段结合 ops/company-context.md 填充。关注点：
> - 我司在 UPF/包处理/转发加速的现有产品能力如何映射到 dUPF/SmartNIC 加速场景？
> - 我司是否应投资 P4/DPU 可编程能力以适应阶段 3→4 的转变？
> - 在 RAN-CN 融合趋势下，我司 RAN 产品与 CN 产品的协同策略如何调整？
> - 我司在 3GPP Rel-20/21 标准化中应支持哪条演进路线？

## 矛盾与待核实

### 矛盾 9：6G 用户面"演进" vs "重构"路线分歧

- **主张 A**：6G CN 应基于 5GC 演进，UPF 保持用户面锚点角色不变，通过 SBA 扩展和硬件加速增强 — 来源：Ericsson 6G 博客 (厂商/2026-06)、Nokia 6G 架构提案 (厂商/2025-03)
- **主张 B**：6G 应根本性重构用户面——消除 N3 隧道，合并 RAN UP 和 CN UP 为统一实体 — 来源：Samsung M-UP (学术/2022)、EURECOM IUP (学术/2025-03)、IETF ANUP (标准/2025)
- **主张 C**：6G 应在 UPF 之外新增独立数据面（DP），UPF 继续处理连接数据，DP 处理非连接数据 — 来源：华为 DaaS (厂商/2025-02)、中国移动五面架构 (学术/2023)
- **现状**：3GPP Rel-20 6G 研究已启动（2025.6），尚无标准结论
- **本调研倾向**：不下结论。三种路线可能最终在不同场景下共存
- **何时能解决**：3GPP Rel-21 规范化（2028+）
- **关联章节**：本文 §4.3/4.4

### 矛盾 10：UPF SBI 化是否替代 PFCP

- **主张 A**：SBI（RESTful API）应替代 PFCP 作为 UPF 控制接口，以对齐 5G SBA 设计原则 — 来源：Fraunhofer FOKUS Open5GCore 实现 (学术/2024-12)
- **主张 B**：PFCP 已足够成熟且性能优化良好，6G 应继续使用并增强（如 Rel-19 UPEAS_Ph2） — 来源：3GPP Rel-19 标准基线 (标准/2025)
- **现状**：Rel-19 仍基于 PFCP，但 SBI 化 UPF 已有学术原型；3GPP 6G 阶段可能重新讨论
- **本调研倾向**：PFCP 短期保留，SBI 化可能在 6G 日一引入
- **何时能解决**：Rel-20/21 架构研究期间
- **关联章节**：本文 §4.2

## 数据缺口

1. **Samsung M-UP 大规模性能验证**：当前仅基于 Open5GS 仿真环境，缺乏商用级实测（P1）
2. **dUPF 多厂商互操作数据**：NVIDIA/Cisco/6WIND 各自实现，无公开互操作测试报告（P1）
3. **3GPP Rel-20 6G RAN 用户面协议研究进展**：RAN2 WG 刚启动（2025 Q4），具体方案不公开（P1）
4. **ANUP 对切片隔离的影响分析**：AN-UPF 合并后网络切片用户面隔离如何保证未讨论（P2）
5. **可编程 UPF 在商用网的 TCO 对比**：P4/SmartNIC vs 纯软件 UPF 的 TCO 定量对比缺公开数据（P1）
6. **6G 用户面能效基准**：各演进路径的每比特能效对比实测数据缺失（P2）

## 来源

### 一手资料 / 官方
1. [3GPP Release 20 Overview](https://www.3gpp.org/specifications-technologies/releases/release-20) — 6G 标准化时间表和 Rel-20 范围
2. [3GPP Rel-19 Summary (2026-04)](https://www.3gpp.org/ftp/Information/presentations/presentations_2026/2026_04_Rel19.pdf) — UPEAS_Ph2、PAIDC_UPF、eEDGE_5GC_Ph3 工作项描述
3. [ITU-T Y.3169: UPF Resource Efficiency Optimization (2025-12)](https://www.itu.int/rec/dologin_pub.asp?id=T-REC-Y.3169-202512-I!!PDF-E&lang=s&type=items) — 容器化 dUPF 资源编排标准

### IETF 标准/草案
4. [draft-zzhang-dmm-mup-evolution-09: Mobile User Plane Evolution](https://datatracker.ietf.org/doc/html/draft-zzhang-dmm-mup-evolution-09) — 5G 分布式 UPF 和 6G ANUP 提案
5. [RFC 9433: SRv6 for the Mobile User Plane](https://datatracker.ietf.org/doc/rfc9433/) — SRv6 移动用户面 IETF 标准

### 厂商/运营商
6. [NVIDIA: Accelerated and Distributed UPF for 6G (2025-10)](https://developer.nvidia.com/blog/accelerated-and-distributed-upf-for-the-era-of-agentic-ai-and-6g/) — dUPF 参考实现，Grace+BF3，100Gbps
7. [Samsung Research: RAN-CN Convergence](https://research.samsung.com/blog/RAN-CN-Convergence-Towards-the-Next-Generation-Networks) — M-UP 概念和实测结果
8. [Nokia: 6G System Architecture (2025-03)](https://www.nokia.com/6g/6g-system-architecture-where-innovation-meets-evolution-for-a-more-sustainable-and-connected-world/) — 6G 模块化协议设计和数据框架
9. [Ericsson: 6G Architecture Standalone Only (2026-06)](https://www.ericsson.com/en/blog/2026/6/blog-6g-architecture-standalone-simpler-evolution-5g) — 6G CN = 5GC 演进路线
10. [NTT DOCOMO: In-Network Computing PoC with Nokia (2025-03)](https://group.ntt/en/newsrelease/2025/03/03/250303a.html) — INC 集成计算到 UPF

### 学术
11. [IUP: Integrated and Programmable User Plane (arXiv 2503.09430, 2025-03)](https://arxiv.org/html/2503.09430) — EURECOM，IDFC 子层替代 SDAP+GTP-U
12. [EURECOM: 6G Service-Oriented Architecture](https://www.eurecom.fr/publication/7496/download/comsys-publi-7496.pdf) — SBA 扩展至 RAN 用户面
13. [Fraunhofer: SBI for UPF in Beyond 5G/6G (2024-12)](https://publica.fraunhofer.de/handle/publica/485713) — UPF SBI 控制接口原型
14. [6GUPF: DPU-based Programmable UPF (Zenodo, 2025-12)](https://zenodo.org/records/18018629) — EU DESIRE6G 项目 DPU 可编程 UPF

### 产业联盟
15. [NGMN: Network Architecture Evolution towards 6G (2025-02)](https://www.ngmn.org/wp-content/uploads/250218_Network_Architecture_Evolution_towards_6G_V1.0.pdf) — 运营商联盟架构演进框架
16. [InterDigital: Paving the Path to 6G in Rel-20 (2025-06)](https://www.interdigital.com/post/paving-the-path-to-6g-key-takeaways-for-3gpp-release-20) — Rel-20 核心网演进概览
