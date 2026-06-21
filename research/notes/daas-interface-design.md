# 精读笔记：daas-interface-design

> 调研日期：2026-06-21
> 搜索轮次：8 轮（Exa）
> 候选来源：~60 个 URL
> 精读来源：12 篇

## [华为 DaaS 白皮书]（厂商，2025-02）
URL: https://www.huawei.com/en/huaweitech/future-technologies/data-plane-design-ai-native-6g-networks

### 关键数据点
- DCP 消息转发延迟 ~2ms，较 RocketMQ 降低 65%
- DCP 吞吐 128KB 消息 + 10 broker 配置下达 2,394.6 MB/s（~2.4 Gbps）
- 消息成功率：103-105 字节范围内接近 100%
- 6G 感知数据量预估：QB 级/天（端侧）、ZB 级/天（云端）

### 关键论断
- 6G 需要专用数据面（DP），因为 CP（SBI）和 UP（PDU Session）无法处理非连接数据
- DO 包含四组件：DA 注册、数据流引擎、数据流管理、策略控制
- DA 分嵌入式（NE 内）和独立式（DPF/DSF）
- DCP 采用 CRT（中国剩余定理）实现无状态 Pub/Sub 消息转发
- 数据拓扑编码为模数集合嵌入数据包头部

### 新发现术语
- DCP（Data Communication Proxy）
- CRT-based stateless message broker
- RNS（Residue Number System）
- DPF（Data Processing Function）
- DSF（Data Storage Function）

## [华为专利 US20250097313A1]（专利，2025-03）
URL: https://www.patents-review.com/a/20250097313-communication-method-apparatus-system.html

### 关键论断
- DO 接收服务请求 → 匹配 DA 数据服务能力 → 下发操作配置 → DA 建立动态逻辑网络拓扑
- 数据管道（data pipeline）= 多 DA 按序连接，前一个 DA 输出为后一个 DA 输入
- 架构包含：DO、DA、TA（Trust Anchor）、服务请求网元、数据存储网元
- 发明人包括 Xueqiang Yan（与白皮书同一作者）

## [vivo/ZJU FITEE 论文]（学术，2025-03）
URL: https://jzus.zju.edu.cn/opentxt.php?doi=10.1631%2FFITEE.2400247

### 关键数据点
- UE 原型验证显示 DP 协议栈上行处理延迟优于 UP 协议栈
- 随数据包长度增加增益更显著（因跳过 ASN.1 编解码）

### 关键论断
- DSAP 协议栈包含 DCF/DPSF/DRF/DTF/DProcF 五子功能
- DPRB 三种类型：RAN 终止/RAN 透传/RAN 处理后转发
- DPRB 灵活优先级：可根据数据量和 UP 负载动态调整
- 二侧数据收集模式：通过奖励或数据交换激励数据提供者

## [三星 6G AI 博客]（厂商，2026）
URL: https://research.samsung.com/blog/AI-in-6G-network-Service-and-System-Aspect

### 关键论断
- 5G NWDAF 三大局限：(1) 集中式设计导致数据收集负载高；(2) NWDAF 是可选 NF 而非原生设计；(3) 缺乏跨域 AI 操作支持
- 6G 需要 AI-enabled NF（各 NF 可自主训练/推理）+ 统一数据框架（跨 UE/RAN/CN/OAM）
- SA2 正在研究 Agentic Core Network——AI Agent 自主执行任务、意图驱动请求
- SA2 6G 数据框架将是"significant topic"，支持跨域数据收集和 AI 服务

## [Nokia 6G 白皮书]（厂商，2025）
URL: https://www.nokia.com/asset/i/212403/

### 关键论断
- 提出专用"data and information architecture"
- 建议"publication-subscription pattern or event stream approach"替代 5G 订阅-通知机制
- 6G 需要收集更多参数、利用更多数据源、存储更长时间窗口

## [GTI 6G Native AI 白皮书]（产业联盟，2023-01）
URL: https://www.gtigroup.org/Uploads/File/2023/01/13/u63c154cb7e808.pdf

### 关键论断
- 5G 数据收集五大痛点：接口少、周期长（>15min）、格式不统一、质量差、预处理成本高
- 数据面基本服务技术特征：可信认证授权、高效存储管理、按需收集、预处理聚合、对外开放接口
- 数据覆盖内外部数据：服务数据、用户数据、网络数据、感知数据

## 与其他来源的矛盾
- 华为主张 Pub/Sub 消息接口（DCP），Ericsson 倾向在 SBA（HTTP/3）内解决 → 矛盾 7
- vivo 主张新空口协议栈（DSAP），Qualcomm 主张 UP 内承载 → 矛盾 8
