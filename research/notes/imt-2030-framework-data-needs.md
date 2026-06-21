# 调研笔记：imt-2030-framework-data-needs

> 深调日期：2026-06-21
> 搜索轮次：8 轮（Exa 7 轮 + Firecrawl 1 轮）
> 候选源：~65 个 URL，精读 12 篇

## 精读来源汇总

### [1] 华为 - Data Plane Design for AI-Native 6G Networks（厂商白皮书，2025-02）
URL: https://www.huawei.com/en/huaweitech/future-technologies/data-plane-design-ai-native-6g-networks

#### 关键数据点
- 6G 感知数据量（1% 容量分配）：QB/天（端侧）至 ZB/天（云端）
- DCP 转发时延：稳定 ~2 ms，比 RocketMQ 降低 65%+
- DCP 吞吐量：1 KB 消息 1 broker=228 MB/s，10 brokers=1061 MB/s；128 KB 消息 10 brokers=2395 MB/s

#### 关键论断
- 5G CP（SBI）仅支持小数据包短连接，UP（PDU Session）仅支持一对一会话隧道——均无法承载 6G 的海量非连接数据
- 提出 DO（数据编排）/ DA（数据代理）/ DCP（数据通信代理）三组件架构
- DCP 采用基于 CRT（中国剩余定理）的无状态消息代理，支持任意数据拓扑
- Pub/Sub 范式实现数据生产者与消费者解耦

#### 与其他来源的矛盾
- Qualcomm 主张"用户面优先"而非独立数据面

### [2] ZJU/华为 - 统一数据收集框架（学术论文，2025-03）
URL: https://jzus.zju.edu.cn/opentxt.php?doi=10.1631%2FFITEE.2400247

#### 关键数据点
- 提出 DSAP（数据服务应用协议）协议栈，含 DCF/DPSF/DRF/DTF/DProcF 五个子功能
- 新型无线承载 DPRB（数据面无线承载），优先级灵活可调
- 基于 6G UE 原型验证，DP 协议栈在上行处理时延方面优于传统方案，数据包越大优势越显著
- 双端数据收集模式支持数字孪生 UE

#### 关键论断
- 5G 数据收集方案碎片化（MDAF/NWDAF/MDT 各自为政），导致标准开销高、重复采集
- 6G 需要统一的数据收集框架，DP 是最佳承载面
- DPRB 无需 ASN.1 处理，直接压缩传输

### [3] 三星 - AI in 6G Network（技术博客，2025）
URL: https://research.samsung.com/blog/AI-in-6G-network-Service-and-System-Aspect

#### 关键论断
- 5G CP 处理 AI 大数据量会导致拥塞
- 5G UP 虽能处理较大数据量，但缺乏核心网层面的数据可控性与可见性
- UP 机制难以从 UE/基站向网络功能传输数据（如 UE 模型训练数据、RAN 感知数据）
- 6G 数据框架将成为 SA2 研究重要议题

### [4] Qualcomm - 6G Foundry: Rethinking the Control Plane（技术白皮书，2024-03）

#### 关键论断
- 提出"用户面优先"设计：定位、数据采集、IoT 等服务从控制面迁移至用户面
- 精简控制面仅保留安全、移动性、会话管理
- IP 服务模型可实现"G 无关"（跨代/跨技术通用）
- 5G NAS/RRC 协议规模指数增长（从 Rel-8 到 Rel-17 页数增长 3-4 倍），但采纳率有限

### [5] Ericsson - 上行流量趋势（行业报道，2026-03）

#### 关键数据点
- 物理 AI 机器人 UL:DL = 70:30
- 80% 运营商上行流量增速超过下行
- 预期 UL 每 5 年增长 3 倍（2025 起）

### [6] Aetha Consulting - AI 上行挑战（分析报告，2026-03）

#### 关键数据点
- 当前移动网络 DL:UL = 90:10
- GenAI 流量上行占比 26%
- ChatGPT 月访问量 53.5 亿，27% 来自移动端
- 视频 GenAI 应用（如 Invideo AI）用户月均 504 MB

### [7] SNS JU Architecture WG - 6G 架构白皮书 v1.3（产业联盟，2025-05）

#### 关键论断
- 数据管理框架集成 DataOps，确保数据采集/处理/治理/质量
- 6G 系统架构将 AI/ML 集成到每一层
- 云原生数据面（Cloud Native Data Plane）作为独立章节讨论
- 提出基于 intent 的管理框架

### [8] 中国移动 - 3 体 4 层 5 面架构（ITU-T 提案，2023-07）

#### 关键论断
- 5 面 = 控制面 + 用户面 + 数据面 + 计算面 + 安全面
- 分布式自治网络（DAN）设计
- 暴露使能层提供 7 类服务（通信/计算/连接/功能/数据/AI/安全）
- HSBA（整体服务化架构）扩展 SBA

### [9] IETF - Mobile User Plane Evolution（协议草案，2024-07）

#### 关键论断
- 提出 AN-UPF 集成（ANUP）：消除 N3 GTP-U 隧道
- 直接在 AN 协议栈上做 UE-DN 路由
- 显著提升吞吐量（尤其在服务器实现场景）

### [10] 3GPP SA2 WT#5 - 6G 数据框架（标准研究，2025-08 启动）

#### 关键论断
- 研究数据收集/分发/处理/存储/访问/暴露
- 含 DaaS 支持
- 跨域数据传输（CN/RAN/SA5/外部）
- 考虑访问控制/用户同意/隐私

### [11] NGMN - Network Architecture Evolution towards 6G（运营商联盟，2025-02）

#### 关键数据点
- 78% MNO 优先自治网络管理
- 67% MNO 优先 AI 原生设计
- 56% MNO 优先 ISAC

### [12] 3GPP TR 38.914 Release 20 分析（学术论文，2026-04）

#### 关键论断
- 采用定性设计维度而非固定量化目标
- 6G 要求的多样性与矛盾性使同时实现所有性能目标不可行
- 设计导向的需求定义取代 5G 的僵化量化基准

## 新发现的术语
- **DO** (Data Orchestration) — 数据编排
- **DA** (Data Agent) — 数据代理
- **DCP** (Data Communication Proxy) — 数据通信代理
- **DSAP** (Data Service Application Protocol) — 数据服务应用协议
- **DPRB** (Data Plane Radio Bearer) — 数据面无线承载
- **ANUP** (AN-UPF Integration) — 接入网-用户面功能集成
- **SBFD** (Sub-Band Full Duplex) — 子带全双工
- **SeMF** (Sensing Management Function) — 感知管理功能
- **DataOps** — 数据运维

## 待追查
- 3GPP SA2 #172+ 会议 WT#5 讨论记录
- Hexa-X-II 数据面相关交付件
- KOMSENS-6G 感知数据传输方案详细提案
