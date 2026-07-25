# 数据基础设施硬技术趋势（面向 6G 数据编织）

> 调研日期：2026-07-25 ｜ 用途：支撑 deep-insight-report-v6 趋势三/四/五的技术层证据
> 视角：站在数据编织（数据工程技术栈）看 6G——编织自身的底座、内核与数据类型体系正在发生什么

## 一、物理底座开放化：开放表格式 + 流式湖仓，"流"与"表"在存储层合一

### 开放表格式成为事实标准
- **Apache Iceberg 已是事实标准表格式**：AWS（S3 Tables）、Snowflake、Databricks（收购 Tabular）、Cloudera、Dremio 全线一等公民支持；TreeHive Strategy（Donald Farmer）评论："Iceberg 已成为事实上的行业标准表格式，供应商已别无选择，只能支持它……Iceberg 将成为数据的通用语（lingua franca）"。
  - 来源：TechTarget, "Why Apache Iceberg is the Center of Attention in Data Platforms"
- **Iceberg v3 关键特性**：Variant 半结构化数据类型、行级血缘（row lineage）——表格式本身开始承载血缘与半结构化，与编织的元数据/血缘能力出现交叠。
- **开放目录成为新战场**：Iceberg REST Catalog、Unity Catalog、Apache Polaris、BigLake 竞争；目录即元数据入口——与编织的目录能力直接对位。

### 流式湖仓与流表合一
- **Apache Paimon**：LSM 树流式湖仓表格式，1.0 于 2025 发布；提供 Iceberg 兼容模式（Paimon 表以 Iceberg 可读元数据发布）；Flink 2.x + Paimon 成为"流式湖仓"组合标配；阿里/字节大规模生产。
- **Apache Fluss（孵化中）**：亚秒级流存储热层；`table.datalake.enabled` 时自动创建对应 Paimon 表并按 freshness 分层（默认 3 分钟），可查询"Fluss+Paimon 合并视图"（秒级新鲜度）或 Paimon 单独视图（分钟级）。
  - 来源：VeloDB glossary "What Is Apache Paimon"; Jaehyeon Kim, "Meet the Streamhouse Trio"（2025-05）; dev.to "Lakehouse Table Formats in 2026"
- **Confluent Tableflow（GA）**：Kafka 主题一键物化为 Iceberg/Delta 表，Schema Registry 作为 schema/演进的单一事实源，"数据质量规则作为流的合约在源头执行"；元数据发布到 REST Catalog，Trino/Snowflake/Spark/Athena 零拷贝直查。
  - 来源：Confluent 官方博客与文档；IBM 社区（Tableflow + watsonx.data 零拷贝，2026-03）
- **电信侧实证**：Deutsche Telekom ODE 采用三层 Iceberg 架构（Raw → Atomic → Analytic），见 data-fabric-in-telecom-early-cases 卡。

### 对编织的含义
底座开放后，编织不再靠"连接器阵列缝合私有系统"取胜——任何引擎（Flink/Spark/Trino/DuckDB）可直查开放表；编织的重心上移到**目录、语义与治理**。

## 二、计算向数据移动：可组合、可嵌入的查询与执行内核

- **Apache Arrow**：统一内存列式格式，组件间零拷贝/零序列化（IPC 传指针不搬数据）；Arrow Flight 提供跨网络零拷贝传输协议。
- **Apache DataFusion**（SIGMOD 2024 论文）：Rust 可嵌入模块化查询引擎，10+ 扩展 API，被大量商业数据库/ML 管道内核化采用；`datafusion-federation` 支持把子计划下推到远端系统执行（Spice AI 生产实践：SQL 源直接下推方言 SQL）。
- **Substrait**：跨语言查询计划交换格式——一条查询可拆分给 DataFusion（Rust）/Velox（C++）/DuckDB 分段执行。
- **单节点能力跃升**：DuckDB/Polars/DataFusion 等单节点引擎可处理数百 GB–TB 级——执行单元可嵌入任何 CNF/站点算力进程（MB 级足迹）。
  - 来源：iceberglakehouse.com "Building Composable Query Engines"（2026-05）; dev.to "Single-Node Data Engineering"
- **采集沉入内核**：OpenTelemetry eBPF Instrumentation（OBI）2026 路线图冲 1.0（零代码内核级遥测、网络属性对齐 OTel 语义约定）；New Relic 等厂商 eBPF 代理 GA；INT 带内遥测提供逐包可见性；5G 侧已有 eBPF 观测 GTP-U/PFCP 与 eUPF（NgKore）内核态数据面实践。
  - 来源：opentelemetry.io/blog/2026/obi-goals；New Relic eBPF Network Metrics GA

### 对编织的含义
"把数据拉到中心处理"反转为"把查询/标注/策略推到数据产生点执行"——编织成为"逻辑集中（目录/语义/策略）、物理分布（边缘执行单元）"的平面；6G 边缘原生编织（议程 4）首次具备工程可行的开源组装路径。

## 三、数据类型体系扩展：时序、多模态感知与向量嵌入成为一等公民

- **向量嵌入一等公民化**：pgvector 使嵌入成为 Postgres 原生数据类型并主流化（2026 社区共识"默认先用 pgvector"）；LanceDB/Lance 格式（Arrow 系）把多模态数据（文本/图像/音频/视频）+ 嵌入 + 元数据作为一等公民，且 Iceberg 开始支持 Lance 文件格式；Iceberg v3 Variant 承载半结构化。
  - 来源：atlan.com 企业向量库对比（2026）；medium 生产选型指南（2026）
- **6G ISAC 多模态感知数据**：
  - DeepSense 6G 数据集：CSI/波束索引/SNR + RGB/LiDAR/GPS/IMU，30+ 场景——通信与感知模态的真实组合（IEEE Network 2026, "Large AI Model for Multimodal ISAC"）。
  - 多模态融合的通行架构：每模态专用编码器 → 统一映射为共享维度向量嵌入（如 256 维）→ transformer 融合（arXiv 2601.01033）——**嵌入成为跨模态通用中间表示**。
  - **SDSF（Sensing Data Storage Function）提案**（arXiv 2603.22488）：新增逻辑网元存储历史感知数据，与实时感知融合以减少重复感知——网络侧开始为感知数据定义存储架构。
  - **O-RAN E2SM-SENS**（arXiv 2603.03607）：E2 接口上的感知 KPI 结构化上报/配置服务模型（时延/多普勒/AoA/多径扩展等），需扩展 O-FH U-Plane 头（波形标识、波束关联元数据）。
- **空白**：感知数据的元数据模型、语义描述与索引（模态/采样参数/坐标系/隐私等级/嵌入指针）无人定义——编织可抢先占领的条目。

## 反向信号与限制

- 开放表格式为对象存储/分析负载设计，亚秒以下实时路径仍在其外（Fluss 热层是分层补丁）；电信私有 OSS 存储替换周期长。
- 开放目录标准未收敛（REST Catalog/Unity/Polaris/BigLake），押错生态有切换成本。
- 可组合引擎生态面向分析负载，电信协议解析/I/Q 级算子需自建；边缘执行单元的规模化运维（版本/安全/资源）是新复杂度；eBPF 绑定 Linux 内核。
- 多模态感知数据管理的付费需求依赖 ISAC 商用节奏（Rel-21 后）；嵌入模型版本漂移使血缘管理复杂化。
