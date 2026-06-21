# 精读笔记：6g-data-plane-architecture-2025

> 调研时间：2026-06-21
> 搜索轮次：8 轮广度 + 2 轮深挖
> 精读来源：16 篇

---

## [华为: Data Plane Design for AI-Native 6G Networks]（厂商白皮书，2025-02）
URL: https://www.huawei.com/en/huaweitech/future-technologies/data-plane-design-ai-native-6g-networks

### 关键数据点
- 6G 感知数据量预估：1% 网络容量用于感知 → 设备端 AI 模型达 QB（10³⁰）级/天，基站侧云 AI 达 ZB（10²¹）级/天
- DCP 原型延迟 ~2ms（所有消息大小），较 RocketMQ 降低 65%
- DCP 10 broker 配置下吞吐达 2,394.6 MB/s（128 KB 消息）

### 关键论断
- 传统 CP（SBI 小数据包）和 UP（PDU 会话一对一）均无法承载非连接数据
- DaaS 三组件：DO（数据编排）→ DA（数据代理）→ DCP（数据通信代理）
- DCP 采用无状态 Pub/Sub 模式，基于中国剩余定理（CRT）实现免查表路由
- 两种 DCP 实现：有状态（表查询）和无状态（带内信息），推荐无状态

### 与其他来源的矛盾
- 与 Qualcomm 根本冲突：华为主张新增独立面，Qualcomm 主张在 UP 上扩展

---

## [Qualcomm: 6G Foundry - Rethinking the Control Plane]（厂商白皮书，2024-03）
URL: https://www.qualcomm.com/content/dam/qcomm-martech/dm-assets/documents/6G-Foundry-1-Rethinking-the-control-plane.pdf

### 关键论断
- "User Plane First"：精简 CP 至仅保留安全/移动性/会话管理三项核心功能
- 新服务（定位、数据收集、IoT）应作为 IP 服务运行在 UP 上
- 好处：利用互联网生态、"G 无关"、云原生友好、可回溯至 5G/Wi-Fi
- 5G CP 复杂度已成为运营负担——不应在 6G 中重复

### 与其他来源的矛盾
- 与华为/中国移动的"独立数据面"路线根本冲突

---

## [中国移动: "三体四层五面" 6G 网络架构]（IEEE ComMag + 白皮书，2022-06/2023）
URL: 多来源（IEEE ComMag 论文、Springer 专著、ITU-T 贡献）

### 关键数据点
- 业界首个系统化 6G 网络架构设计（2022-06 首发）
- 六大设计理念：前后兼容、跨域融合、分布自治、网络内生、至简统一、低碳熵减
- IEEE Communications Magazine 正式发表（2023）

### 关键论断
- 三体：网络本体、管理编排体、数字孪生体
- 四层：资源与算力层、路由与连接层、服务化功能层、开放使能层
- 五面：控制面、用户面、数据面、计算面、安全面
- 数据面目标：统一管理庞大用户数据、为 AI 原生和数字孪生提供数据服务
- 组网设计：DAN（分布式自治网络）、SCU（分布式微云单元）

---

## [SNS JU: Towards 6G Architecture v1.3.1]（产业白皮书，2025-05）
URL: https://publications.aston.ac.uk/id/eprint/48294/3/ArchWG-WhitePaper_v1.3.1-FINAL.pdf

### 关键论断
- 6G 系统蓝图四层：基础设施层、网络层、应用层、普适功能层
- 包含"Cloud Native Data Plane"专章（§5.1.4）
- 6G Core 应基于演进的 5GC（evolved 5GC），而非全新设计
- 数据管理框架整合 DataOps，是普适 AI/ML 运行的基础
- 感知数据需独立于 UP/CP 的数据通道（raw I/Q 数据）
- 提出 GSBA（Global Service-Based Architecture）概念

---

## [Hexa-X-II D3.5]（EU 项目交付件，2025-03）
URL: https://hexa-x-ii.eu/hexa-x-ii-unveils-deliverable-d3-5-advancing-the-6g-architectural-framework/

### 关键论断
- AIaaS、感知、计算三大新服务对架构提出不同于通信服务的需求
- 感知功能：SU（感知单元）+ SeMF（感知管理功能）
- AI 功能：AI data and model bus、MLOps、DataOps
- 计算功能：ON（卸载节点）+ CCN（计算控制节点）+ CMF（计算管理功能）
- 5G→6G 迁移建议：MRSS（多 RAT 频谱共享）为主要机制

---

## [NGMN: Network Architecture Evolution towards 6G]（运营商联盟，2025-02）
URL: https://www.ngmn.org/wp-content/uploads/250218_Network_Architecture_Evolution_towards_6G_V1.0.pdf

### 关键数据点
- 78% 运营商选择"自治网络管理"为 6G 架构变革关键驱动力
- 67% 选择"AI 原生设计"
- 56% 选择 ISAC 和网络韧性/弹性
- 约半数运营商认为 VR/AR、自动驾驶、智慧交通、工业 4.0 等可通过 5G 实现

### 关键论断
- "6G 架构共识尚未达成"（原文）
- 必须避免 5G NSA/SA 多选项复杂性的重演
- 应确保标准化过程有充足时间
- 运营商处于不同 5G 演进阶段 → 对 6G 路径观点分化

---

## [3GPP SA2 FS_6G_ARC]（标准化，2025-06 批准）
URL: https://www.3gpp.org/technologies/sa2-role-rel-19

### 关键数据点
- SI 批准：TSG#108（2025-06）
- 完成目标：2026-12 或 2027-03
- WT 数量：至少 8 个工作任务（WT#1.1/1.2/2/3/4/5/6/7/8）

### 关键论断
- WT#5 明确研究"统一数据框架"
- KI#21 专门研究 6G 数据框架系统架构
- SA2 和 SA5 协作：SA5 管理数据 + SA2 AI/感知数据
- 工作从 2025-08 开始

---

## [vivo: Unified Data Collection Framework]（学术，FITEE 2025-03）
URL: https://link.springer.com/article/10.1631/FITEE.2400247

### 关键论断
- 5G 数据收集碎片化：针对不同用例的方案标准开销高、可能重复收集
- 提出基于 6G 数据面的统一数据收集框架
- 数据面协议栈原型验证：随包长增加，数据面处理延迟优势更显著
- 双端数据收集模式：通过激励提高数据提供者意愿
- 来自 vivo（中国厂商），支持独立数据面路线

---

## [arXiv:2103.02823: Toward Native AI in 6G]（学术，2021/2024 更新）
URL: https://ar5iv.labs.arxiv.org/html/2103.02823

### 关键论断
- 独立数据面和智能面的早期学术论证
- 提出 XaaS（Everything as a Service）平台概念
- 融合通信和计算服务供给
- 作者来自中国移动研究院，是"三体四层五面"的理论基础
