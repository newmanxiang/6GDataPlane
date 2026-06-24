---
title: AI 原生数据面现状与研究进展
title_en: AI-Native Data Plane - Current Status and Research Progress
slug: ai-native-data-plane-status
category: topic
status: reviewed
confidence: medium
sources:
  - https://www.huawei.com/en/huaweitech/future-technologies/data-plane-design-ai-native-6g-networks
  - https://www.gtigroup.org/Uploads/File/2023/01/13/u63c154cb7e808.pdf
  - https://www.3gpp.org/technologies/ai-ml-ngran
  - https://ai-ran.org/
  - https://www.o-ran.org/research-reports/o-ran-native-ai-architecture-description
  - https://www.sciencedirect.com/science/article/pii/S2095809925005673
  - https://arxiv.org/html/2507.06911v1
  - https://arxiv.org/html/2507.08403
  - https://smart-networks.europa.eu/wp-content/uploads/2025/06/archwg-whitepaper-v1.3-final-23may_clean.pdf
  - https://www.ericsson.com/en/blog/2025/6/blog-6g-standardization-technology-step-to-publish
  - https://www.itu.int/hub/2026/03/imt-2030-technical-requirements-for-the-6g-future/
  - https://p4.org/wp-content/uploads/sites/53/2026/01/in-network-ml-with-p4-from-stateless-to-hybrid.pdf
related:
  - ai-native-air-interface
  - 6g-data-plane
  - 6g-data-plane-architecture-2025
  - daas-interface-design
  - network-data-analytics
  - imt-2030-usage-scenarios-data-needs
tags: [AI原生, 数据面, 机器学习, 可编程, 6G, AI-RAN, P4, in-network inference]
last_verified: 2026-06-22
owner: agent
---

# AI 原生数据面现状与研究进展

## 核心结论（执行摘要）

AI 原生数据面（AI-Native Data Plane）是 6G 网络架构中最具争议但演进方向最明确的前沿领域之一。截至 2026 年中，该领域呈现三重路径并行态势：（1）华为/中国移动主导的**独立数据面**方案（DaaS + DO/DA/DCP 架构）已有原型验证，DCP 消息转发延迟稳定在 ~2ms、吞吐最高 2.4 GB/s（10 broker 配置）；（2）O-RAN/AI-RAN Alliance 推动的**RAN 内嵌 AI 推理**方案（dApp + E3 接口）已在开源测试床验证亚毫秒控制闭环；（3）学术界的**可编程数据面 ML**（P4/FPGA SmartNIC）已实现线速 CNN/RNN 推理（SIGCOMM 2025 Pegasus 框架，精度提升 22.8%，模型规模扩大 248×）。3GPP 6G 技术研究（Rel-20）已于 2025 年 8 月启动，AI/ML 框架是核心议题之一，但尚未就数据面 AI 原生化方案形成共识。[信心：中等——产业方案多元且标准化未定]

## 1. 现状定义

**AI 原生数据面**指在 6G 网络数据面（用户面/数据面）中原生嵌入 AI/ML 能力的设计范式，涵盖两个互补方向：

- **AI for Data Plane（AI 赋能数据面）**：利用 AI 优化数据面自身的转发决策、流量调度、QoS 保障。典型技术包括 ML 驱动的流量分类、智能路由、异常检测，运行于可编程交换机或 SmartNIC 中。
- **Data Plane for AI（数据面服务 AI）**：数据面作为 AI 应用的数据供给基础设施，提供高效数据采集、模型参数分发、分布式训练/推理的数据流编排。典型方案是华为 DaaS 的 DO/DA/DCP 架构。

**与 NWDAF 的根本区别**：5G NWDAF（网络数据分析功能）在**控制面**层运行 AI 分析，通过管理接口收集数据、离线/近实时推理，然后向 PCF/SMF 提供策略建议。AI 原生数据面则将 AI 推理**嵌入数据转发路径本身**，实现逐包/逐流的实时决策，或将数据面重构为原生支持 AI 工作流的数据管道。

## 2. 标准与组织动态（近 3 年）

| 时间 | 组织 | 进展 |
|------|------|------|
| 2026-06 | 3GPP RAN | RAN1#122+ 讨论 6G AI/ML 用例（48 家公司、1000+ 页贡献），重点含参考信号开销削减、AI 非线性处理 |
| 2025-08 | 3GPP | Rel-20 6G 技术研究启动，含 AI/ML 框架、用户面设计、控制面等多个 SI |
| 2025-06 | 3GPP RAN#109 | 6G RAN 架构协议：支持 CP/UP 分离、开放多厂商接口、standalone 6G |
| 2025-11 | O-RAN R005 | 完成 AI/ML 工作流规范（Non-RT/Near-RT RIC 训练/推理部署场景 1.1-1.5） |
| 2025-05 | SNS JU | 6G 架构白皮书 v1.3 发布，含"Cloud Native Data Plane"和"AI/ML Framework"章节 |
| 2025-03 | O-RAN nGRG | 发布"Native AI Architecture Description"研究报告 |
| 2024-07 | AI-RAN Alliance | 正式成立（SoftBank 发起），MWC 2024 发布；2026-02 达 132 成员 |
| 2024-Q2 | 3GPP | Rel-19 AI/ML for NG-RAN WI 启动（网络切片、CCO 新用例） |
| 2023-12 | ITU-R | M.2160 发布 IMT-2030 框架，定义 AIAC 场景，提出 AI-native 空口 |
| 2023-01 | GTI/CMRI | 发布《6G Native AI Architecture and Technologies》白皮书，首次系统定义数据面 |

**关键标准化走向**：3GPP SA2 WT#5 正在研究 6G 数据框架（是否需独立 DP vs 增强 UP），预计 2026-12 至 2027-03 完成研究。O-RAN 聚焦 RIC 层 AI/ML 工作流标准化，已有成熟规范（R005），对数据面直接 AI 嵌入尚在研究阶段（dApp 方案）。

## 3. 关键玩家

### 厂商/运营商

| 玩家 | 方案定位 | 核心贡献 |
|------|----------|----------|
| **华为** | 独立数据面 + DaaS | DO/DA/DCP 架构、CRT 无状态消息代理、原型验证（延迟 2ms、吞吐 2.4GB/s） |
| **中国移动** | 5 面架构（含数据面/智能面）| GTI 白皮书、DAN 分布式自治网络、QoAIS 概念 |
| **SoftBank/NVIDIA** | AI-RAN（AI-and-RAN 共享基础设施）| AITRAS 平台、GPU-based vRAN（gRAN）、AI-RAN Alliance 创始 |
| **Qualcomm** | 用户面优先（UP-first）| 6G Foundry 系列，精简 CP、增强 UP 承载 AI 服务 |
| **Nokia** | 数据信息架构 | 6G 白皮书提出通用数据暴露/注册/发现/交付框架 |
| **Ericsson** | 演进式增强 | HTTP/3+QUIC SBA 内支持数据服务，关注 AI/ML 框架标准化 |
| **OPPO/vivo** | AI 功能面/DSAP 协议 | AI-Cube 白皮书（AI 功能连接）、DSAP/DPRB 新空口协议栈提案 |

### 学术机构/项目

| 机构/项目 | 研究方向 |
|-----------|----------|
| 浙江大学（Rongpeng Li 团队）| TONA 任务导向原生 AI 网络架构、QoAIS |
| Oxford/IMDEA Networks | P4 数据面 ML（Planter/Flowrest/DUNE/MUTA 框架，Intel Tofino 部署） |
| 清华大学（THU CSNet）| Pegasus 数据面深度学习框架（SIGCOMM 2025）|
| 6G-GOALS（SNS JU）| 语义面 + O-RAN 架构融合 |
| 6GARROW（SNS JU）| AI-native RAN + 设备-网络集成 |
| ADROIT6G（SNS JU）| 分布式 AI 驱动可编程 6G 架构 |

### 产业联盟

- **AI-RAN Alliance**（132 成员，2026-02）：三工作组（AI-for-RAN / AI-and-RAN / AI-on-RAN）+ Data-for-AI 任务组
- **O-RAN Alliance**：nGRG 负责 6G 方向研究，R005 已规范 AI/ML 工作流
- **GTI**：中国移动主导，发布 Native AI 白皮书

## 4. 技术机制

### 4.1 华为 DaaS 数据面架构

核心组件：
- **DO（Data Orchestration）**：数据面"指挥者"，含 DA 注册、数据流引擎、数据流管理、策略控制
- **DA（Data Agent）**：部署于 UE/BS/边缘/核心网的智能中介，执行预处理/转换/本地决策/缓存/安全
- **DCP（Data Communication Proxy）**：无状态 Pub/Sub 消息代理，基于 CRT（中国剩余定理）/ RNS 实现拓扑编码和模运算转发

技术特点：异步解耦生产者/消费者、支持任意数据拓扑、on-path 数据处理、无需维护转发表。

### 4.2 可编程数据面 + AI（In-Network ML）

代表性工作：
- **Pegasus**（SIGCOMM 2025）：将 DL 操作翻译为三种数据面原语（Partition/Map/SumReduce），支持 MLP/RNN/CNN/AutoEncoder，精度提升最高 22.8%
- **BoS**（NSDI 2024）：数据面友好型 RNN 架构 + 离线 Transformer 混合，实现线速神经网络流量分析
- **FENIX**：Tofino ASIC + FPGA 混合架构，微秒级延迟、Tbps 吞吐、>90% 分类精度
- **P4AI**（AMD/Xilinx）：开源 P4 数据面 AI 框架，SmartNIC 上部署 DNN 推理

当前局限：仅适用于轻量模型（流量分类/异常检测），大模型推理仍需卸载。

### 4.3 O-RAN dApp 实时用户面 AI

O-RAN 提出 **dApp**（distributed App）架构：
- 与 DU 共置，通过 **E3 接口**直接访问用户面数据（I/Q 样本、CSI、SRS）
- 实现亚毫秒闭环控制（实验验证 <1ms）
- 与 xApp/rApp 形成层级 AI 推理链
- 支持 ISAC 感知功能的实时执行

### 4.4 端到端学习收发机

- AI autoencoder 替代传统编解码/调制解调的完整流水线
- 语义通信（SemCom）将任务相关语义压缩嵌入数据面传输
- 关键影响：打破传统数据面"比特管道"范式，使数据面具备语义理解能力
- 标准化距离：3GPP Rel-18/19 仅在 CSI/beam/定位用例验证 AI/ML，完整替代需等 6G

## 5. 趋势驱动力

1. **AI 数据爆炸**：6G 感知数据预估达 quettabyte（10³⁰）/天（设备侧），zettabyte/天（基站侧），传统 UP 无法承载
2. **分布式 AI 训练需求**：联邦学习、协作推理要求多对多数据拓扑，非 PDU session 一对一模型
3. **ISAC 融合**：感知数据需要独立于通信连接的传输路径和 on-path 处理
4. **边缘 AI 推理**：GenAI/LLM 推理部署到 RAN 边缘（AI-on-RAN），需要数据面与计算面深度协同
5. **运营商增收诉求**：AI-RAN 将 RAN 基础设施从成本中心转为收入来源（GPU 共享、AI 服务托管）
6. **能效压力**：in-network 推理避免数据往返，可降低传输能耗
7. **语义通信成熟**：任务导向的语义编码使"传输含义而非比特"成为可能

## 6. 批评与风险

1. **标准碎片化风险**：华为独立 DP vs Qualcomm UP-first vs O-RAN dApp，三条路径缺乏收敛迹象
2. **数据面复杂性爆炸**：引入 AI 推理使数据面从确定性转发变为概率性决策，调试和故障定位困难
3. **部署成本**：AI-RAN 需 GPU 加速器（Grace Hopper/Blackwell 单台超 $300K），中小运营商难以负担
4. **可编程数据面局限**：P4 交换机仅支持轻量模型（kB-MB 级参数），无法运行 LLM 等大模型
5. **安全边界模糊**：in-network AI 推理模糊了传统数据面安全模型，零信任架构需重新设计
6. **产业利益分歧**：独立数据面（中国系厂商主导）vs 增强用户面（西方系厂商倾向）反映产业政治
7. **缺乏端到端验证**：华为 DCP 仅有消息转发原型，未集成 RAN/CN；学术 P4 ML 仅在实验室环境
8. **AI 可信度**：数据面 AI 决策的可解释性、鲁棒性（对抗攻击）、公平性尚未充分研究

## 7. 我司相关性（占位，由 6g-insight-report 阶段填充）

待读取 ops/company-context.md 后映射。初步关联点：
- DaaS 数据管道设计对我司数据业务的参考价值
- 可编程数据面 AI 对我司网络设备产品线的技术选型影响
- AI-RAN 共享基础设施模式对运营商客户商业模式的影响

## 矛盾与待核实

1. **数据面 AI 推理时延声明不一致**：华为 DCP 声称 ~2ms 转发延迟，O-RAN dApp 声称 <1ms 闭环控制，但二者场景和度量标准不同（消息转发 vs 控制闭环），不具直接可比性
2. **"AI 原生"定义边界模糊**：NWDAF 增强版（如 ZTE 论文）是否算"AI 原生数据面"？部分文献将 NWDAF 对 UPF 的垂直扩缩容决策也归入此类
3. **3GPP 对独立数据面的态度不明**：SA2 WT#5 同时研究"新数据面"和"增强 UP"两种方案，目前无明确倾向信号

## 数据缺口

1. **P1**：华为 DaaS 端到端（RAN+CN）集成验证数据——目前仅有消息代理原型
2. **P1**：AI-RAN 共享基础设施下 RAN 性能影响的定量评估——AI 负载对通信 QoS 的干扰量化
3. **P1**：In-network ML 从流量分类扩展到通信决策（如调度/功控）的可行性论证
4. **P2**：3GPP SA2 WT#5 对数据面 AI 能力的具体需求提案内容（需会员账号）
5. **P2**：端到端学习收发机在商用硬件上的能效与吞吐对比数据
6. **P1**：不同方案（DaaS/dApp/P4 ML）间的定量性能对比基准——目前缺乏统一 benchmark

## 来源

### 一手资料 / 官方
1. [AI/ML for NG-RAN & 5G-Advanced towards 6G](https://www.3gpp.org/technologies/ai-ml-ngran) — 3GPP RAN3 官方文章，Rel-18/19/20 AI/ML 进展
2. [IMT-2030: Technical requirements for the 6G future](https://www.itu.int/hub/2026/03/imt-2030-technical-requirements-for-the-6g-future/) — ITU-R WP5D，6G 性能需求定义
3. [O-RAN Native AI Architecture Description](https://www.o-ran.org/research-reports/o-ran-native-ai-architecture-description) — O-RAN nGRG 研究报告
4. [6G Agreements from RAN Plenary 109](https://www.6gran.info/6G_agreements_RAN_109/) — 3GPP 6G RAN 架构协议

### 学术
5. [Pegasus: Universal Framework for Scalable Deep Learning Inference on the Dataplane](http://www.thucsnet.com/wp-content/papers/yinchao_sigcomm2025.pdf) — SIGCOMM 2025，清华大学
6. [Brain-on-Switch: NN-Driven Traffic Analysis at Line-Speed](https://www.usenix.org/system/files/nsdi24-yan.pdf) — NSDI 2024
7. [A Task-Driven Design Approach for 6G AI-Native Architecture](https://www.sciencedirect.com/science/article/pii/S2095809925005673) — Engineering（中国工程院院刊）2025
8. [Towards AI-Native RAN: Operator's Perspective of 6G Day 1](https://arxiv.org/html/2507.08403) — 中国移动研究院 2025
9. [Building An Open Architecture for AI-RAN Convergence in 6G](https://arxiv.org/html/2507.06911v1) — AI-RAN Alliance/Northeastern 2025

### 厂商白皮书
10. [Data Plane Design for AI-Native 6G Networks](https://www.huawei.com/en/huaweitech/future-technologies/data-plane-design-ai-native-6g-networks) — 华为 2025
11. [6G Native AI Architecture and Technologies White Paper](https://www.gtigroup.org/Uploads/File/2023/01/13/u63c154cb7e808.pdf) — GTI/中国移动 2023
12. [Towards 6G Architecture (SNS JU v1.3)](https://smart-networks.europa.eu/wp-content/uploads/2025/06/archwg-whitepaper-v1.3-final-23may_clean.pdf) — 欧盟 SNS JU 2025

### 分析机构 / 产业
13. [AI-RAN Alliance](https://ai-ran.org/) — 产业联盟官网（132 成员，2026-02）
14. [AI-RAN architecture: A practical guide for operators](https://stlpartners.com/articles/ai-ran/ai-ran-architecture/) — STL Partners 分析 2026
15. [6G standardization: Technical studies starting](https://www.ericsson.com/en/blog/2025/6/blog-6g-standardization-technology-step-to-publish) — Ericsson 2025
