# 精读笔记：AI 原生数据面现状与研究进展

> 子题 slug: ai-native-data-plane-status
> 调研日期: 2026-06-22
> 搜索引擎: Exa (web_search_exa + web_fetch_exa)

---

## [华为 - Data Plane Design for AI-Native 6G Networks]（厂商白皮书，2025-02）
URL: https://www.huawei.com/en/huaweitech/future-technologies/data-plane-design-ai-native-6g-networks
归档: research/raw/2026-06-22-huawei-daas-dp/

### 关键数据点
- 6G 感知数据量预估：quettabyte (10³⁰) /天（设备端 AI 模型），zettabyte (10²¹) /天（基站端 AI 模型）—— 假设分配 1% 网络容量用于感知
- DCP 消息转发延迟：~2ms，对所有测试消息大小稳定（101-105 bytes）
- DCP 相比 RocketMQ 平均延迟降低 >65%
- DCP 吞吐：228 MB/s（1 broker, 1KB msg）→ 2394.6 MB/s（10 brokers, 128KB msg）
- 消息成功率：103-105 bytes 范围内接近 100%；105+ bytes 短间隔时下降

### 关键论断
- 传统 CP+UP 架构无法承载"beyond-connectivity services"（AI 数据/感知数据）
- 提出独立 DP 的三层理由：massive data volume、complex data topologies、data orchestration requirement
- DCP 基于 CRT/RNS 实现无状态 Pub/Sub——拓扑信息编码为数据包内带信息
- stateless DCP 优于 stateful DCP：超低延迟（模运算 vs 表查找）+ 高可扩展性

### 新发现术语
- DO (Data Orchestration)
- DA (Data Agent) — embedded DA vs standalone DA
- DCP (Data Communication Proxy) — stateless vs stateful
- DPF (Data Processing Function)
- DSF (Data Storage Function)
- CRT-based stateless message broker

### 与其他来源矛盾
- 与 Qualcomm UP-first：华为主张独立 DP，Qualcomm 主张增强 UP 即可
- DCP 延迟 ~2ms vs O-RAN dApp <1ms——不同层级/场景的度量

### 待追查
- DCP 端到端集成测试（含 RAN 侧）
- CRT 编码的最大拓扑规模限制

---

## [GTI/CMRI - 6G Native AI Architecture and Technologies]（产业联盟白皮书，2023-01）
URL: https://www.gtigroup.org/Uploads/File/2023/01/13/u63c154cb7e808.pdf
归档: research/raw/2026-06-22-gti-native-ai/

### 关键数据点
- 5G 数据收集周期 >15 分钟（管理面采集）
- 5G 网络自治等级约 2.2（满分 5）

### 关键论断
- 6G Native AI 定义：在架构层面原生支持 AI 全生命周期（数据采集/预处理/训练/推理/评估），而非 5G 的补丁式/插件式
- 新架构三面：数据面（data plane）+ 智能面（smart plane）+ 扩展的控制面和用户面
- QoAIS（Quality of AI Service）：多维评估（性能/开销/安全/隐私/自治度）
- 5G AI 挑战：缺乏统一框架、插件模式难以实现全自动闭环、跨系统协作延迟秒~分钟级

### 新发现术语
- QoAIS (Quality of AI Service)
- NAMO (Network AI Management and Orchestration)
- DAN (Distributed Autonomous Network)

### 与其他来源矛盾
- 无显著矛盾，但 QoAIS 概念目前仅有 CMRI 系统性提出，尚无标准化提案

---

## [3GPP - AI/ML for NG-RAN & 5G-Advanced towards 6G]（标准组织，2026-01）
URL: https://www.3gpp.org/technologies/ai-ml-ngran
归档: research/raw/2026-06-22-3gpp-aiml-ngran/

### 关键数据点
- Rel-18：RAN3 完成规范工作 Q4 2023
- Rel-19：Q2 2024 启动 WI（网络切片/CCO/连续 MDT）
- Rel-20：5G-A AI/ML 基于现有 5G 架构和接口

### 关键论断
- 明确区分两个维度：AI4Net（AI 赋能网络）vs Net4AI（网络赋能 AI）
- 6G 将超越基本连接，实现"智能实体的高效互联"
- Agentic AI 与 6G 网络集成是未来重要研究方向
- 跨层数据采集和管理（UE/RAN/CN + 应用层信息交换）是重要待研课题

### 新发现术语
- AI4Net / Net4AI（3GPP 官方区分）

---

## [O-RAN - dApp Architecture and Interfaces]（标准研究，2025+）
URL: https://www.o-ran.org/research-reports/dapp-architecture-and-interfaces
归档: research/raw/2026-06-22-oran-dapp/

### 关键数据点
- dApp 闭环控制延迟：亚毫秒级（<1ms），实验验证
- 解决 O-RAN 现有系统两个关键限制：(1) 缺乏对用户面数据的直接访问 (2) 无法实现 sub-10ms 控制闭环

### 关键论断
- dApp 通过 service-based interface 实现 dApp 与 RAN/RIC/SMO 的实时通信
- 相比其他 real-time RIC 架构，dApp 更具可扩展性和更低复杂度
- 利用现有 O-RAN 接口（E3 接口为新增），渐进式增强

### 新发现术语
- dApp (distributed App)
- E3 接口（DU-dApp 之间）

---

## [AI-RAN Alliance - Building Open Architecture for AI-RAN Convergence in 6G]（产业+学术，2025）
URL: https://arxiv.org/html/2507.06911v1
归档: research/raw/2026-06-22-ai-ran-architecture/

### 关键数据点
- AI-RAN Alliance 成立于 2024，2026-02 达 132 成员
- 三个核心维度：AI-for-RAN / AI-and-RAN / AI-on-RAN

### 关键论断
- RAN 从传统通信基底 → 可编程、智能、有感知、算力可用的平台
- AI-RAN Orchestrator 扩展 O-RAN SMO 框架
- AI-RAN Sites 增强 O-RAN O-Cloud 以支持 AI 工作负载
- AI workload 在 RAN 内部通过 UPF 保持与 RAN 协议栈的逻辑隔离

### 与其他来源矛盾
- AI-RAN 明确声称"不做标准化"（与 3GPP/O-RAN 互补），但其架构提案实质上影响标准方向

---

## [Pegasus - SIGCOMM 2025 (清华 CSNet)]（学术，2025）
URL: http://www.thucsnet.com/wp-content/papers/yinchao_sigcomm2025.pdf
归档: research/raw/2026-06-22-pegasus-sigcomm/

### 关键数据点
- 支持模型类型：MLP/RNN/CNN/AutoEncoder
- 精度提升：平均最高 22.8%（vs 现有方案）
- 模型规模扩大：248×
- 输入规模扩大：212×

### 关键论断
- 提出三种数据面友好原语：Partition / Map / SumReduce
- Fuzzy Matching 技术处理低维向量并行计算
- Primitive Fusion 合并计算提升可扩展性
- 全精度权重 + 定点激活值平衡精度和硬件限制

### 新发现术语
- Intelligent DataPlane (IDP)
- Partition-Map-SumReduce 范式

---

## [Ericsson - 6G standardization: Technical studies starting]（厂商，2025-06）
URL: https://www.ericsson.com/en/blog/2025/6/blog-6g-standardization-technology-step-to-publish
归档: research/raw/2026-06-22-ericsson-6g-std/

### 关键数据点
- 6G 技术研究：2025-08 启动，持续 18-21 个月
- Rel-21 WI 交付第一批 6G 规范
- 3GPP/O-RAN 2025-04 联合研讨会确认 O-RAN 继续负责 lower-layer split

### 关键论断
- 6G AI/ML 框架将考虑 5G 已有框架基础上的演进
- AI 生命周期管理（训练/部署/推理/监控）需 3GPP 规范化
- 用户面设计是 6G 技术研究的核心议题之一

---

## [P4.org - In-network inference with P4]（学术综述/教程，2026-01）
URL: https://p4.org/wp-content/uploads/sites/53/2026/01/in-network-ml-with-p4-from-stateless-to-hybrid.pdf
归档: research/raw/2026-06-22-p4-in-network-ml/

### 关键数据点
- 方案分类：Packet-level (Planter/Mousika) → Flow-level (Flowrest) → Hybrid (NetBeacon/Jewel)
- 硬件平台：Intel Tofino ASIC（核心）

### 关键论断
- In-network ML 是网络自动化管理的基础
- 从无状态推理→有状态推理→混合推理的演进路径清晰
- 实验全部在商用硬件（Intel Tofino FN-T10-03）上验证

---

## [OPPO - 6G AI-Cube Intelligent Networking]（厂商白皮书，2023+）
URL: https://www.oppo.com/content/dam/oppo/en/mkt/newsroom/press/oppo-unveils-6g-white-paper/6G%20AI-Cube%20Intelligent%20Networking.pdf
归档: research/raw/2026-06-22-oppo-ai-cube/

### 关键论断
- 提出 AI 功能面（AI Functional Plane）概念
- AI 数据连接的三个特征：(1) 按需确定传输路径 (2) 途径组件可感知并处理内容 (3) 支持多对多路由
- 与华为 DaaS 方向一致但命名不同

---

## 搜索策略总结

| 维度 | Query 数 | 命中有效源 |
|------|----------|-----------|
| 定义/范围 | 3 | 8 |
| 标准进展 | 3 | 6 |
| 关键玩家 | 2 | 7 |
| 技术机制 | 4 | 12 |
| 趋势驱动 | 2 | 4 |
| 批评/风险 | 2 | 3 |
| 可编程数据面+AI | 3 | 10 |

总计精读：12 篇核心来源，其中权威源 5 个（3GPP/ITU/O-RAN/SNS JU/AI-RAN Alliance）。
