# Deep Dive Queue（子题待办队列）

> 由 6g-onboarding（D2 末）建立初版，由 6g-deep-dive 持续追加。

## 状态分类

| 状态 | 含义 |
|---|---|
| `pending` | 待办 |
| `in-progress` | 当前正在调研 |
| `done` | 完成（已产出 wiki/topics/<slug>.md） |
| `deferred` | 推迟到下一阶段 |
| `skipped` | 不在本次范围 |

## 优先级

- **P0** — 报告必须章节的直接素材
- **P1** — 强相关，能显著提升报告深度
- **P2** — 锦上添花，时间充裕再做

## 队列

| 优先级 | 子题 slug | 类目 | 状态 | 拟分配日 | 备注 |
|---|---|---|---|---|---|
| P0 | `imt-2030-usage-scenarios-data-needs` | 6G数据面 | pending | - | IMT-2030 六大使用场景及其对数据面的具体需求 |
| P0 | `6g-kpi-20-requirements` | 6G数据面 | pending | - | 6G KPI 量化指标全表（20 项性能需求解读） |
| P0 | `3gpp-6g-timeline-rel22-23` | 标准 | pending | - | 3GPP 6G 标准时间线与里程碑（Rel-22/23 规划） |
| P0 | `3gpp-sa2-6g-data-framework-wt5` | 标准 | pending | - | 3GPP SA2 6G 数据框架工作项（WT#5）进展 |
| P0 | `daas-interface-design` | 6G数据面 | pending | - | DaaS 接口设计：数据面如何向智能面暴露数据服务 |
| P0 | `gtp-u-limitations-6g-alternatives` | 6G数据面 | pending | - | GTP-U 局限性与 6G 替代方案（SRv6、网络编程） |
| P1 | `data-plane-data-fabric-mapping` | 交集 | pending | - | 数据面与数据编织技术的映射关系 |
| P1 | `ietf-mup-draft-6g` | 标准 | pending | - | IETF MUP 草案解读与 6G 适用性 |
| P1 | `upf-distributed-6g` | 6G数据面 | pending | - | UPF 分布式部署模式在 6G 中的延续与变革 |
| P1 | `3gpp-rel19-20-ai-ml-air-interface` | 标准 | pending | - | 3GPP Rel-19/20 AI/ML for NR Air Interface 标准化进展 |
| P1 | `e2e-learnable-transceiver-data-needs` | 6G数据面 | pending | - | 端到端学习收发机的数据需求与数据面承载方案 |
| P1 | `ai-model-training-data-flow` | 6G数据面 | pending | - | AI 模型在空口的在线/离线训练数据流架构 |
| P1 | `o-ran-ngrg-6g-ran-whitepaper` | 标准 | pending | - | O-RAN nGRG 6G RAN 架构白皮书详细分析 |
| P1 | `ai-ran-gpu-sharing-data-plane-impact` | 6G数据面 | pending | - | AI-RAN GPU 共享算力模型对数据面的影响 |
| P1 | `ric-data-plane-role` | 6G数据面 | pending | - | RIC 作为数据面数据消费/生产节点的角色定位 |
| P1 | `nwdaf-rel18-19-enhancements` | 标准 | pending | - | NWDAF Rel-18/19 新增分析用例与 ML 增强特性 |
| P1 | `6g-distributed-analytics-nwdaf-ric` | 6G数据面 | pending | - | 6G 分布式数据分析架构（NWDAF + RIC 融合） |
| P1 | `nwdaf-data-fabric-integration` | 交集 | pending | - | NWDAF 与数据编织的集成路径 |
| P1 | `dtn-realtime-sync-bandwidth-latency` | 6G数据面 | pending | - | DTN 对数据面实时同步带宽与时延的量化需求分析 |
| P1 | `dtn-data-fabric-integration` | 交集 | pending | - | DTN 与数据编织集成：主动元数据驱动孪生模型更新 |
| P2 | `dtn-multi-domain-data-consistency` | 6G数据面 | pending | - | DTN 多域（RAN/传输/核心网）数据一致性保障 |
| P1 | `isac-sensing-data-qos` | 6G数据面 | pending | - | ISAC 感知数据在数据面的传输协议与 QoS 需求 |
| P1 | `isac-rel20-sensing-data-path` | 6G数据面 | pending | - | 3GPP R20 ISAC 感知数据流端到端路径设计 |
| P2 | `isac-privacy-sensing-data` | 隐私/治理 | pending | - | ISAC 感知数据中的个人信息识别与脱敏 |
| P1 | `ntn-user-plane-protocol-adaptation` | 6G数据面 | pending | - | NTN 透明 vs 再生模式的用户面协议栈适配对比 |
| P1 | `ntn-multi-layer-routing` | 6G数据面 | pending | - | 多层 NTN 架构数据路由与星地协同调度 |
| P2 | `ntn-onboard-mec-data-plane` | 边缘 | pending | - | NTN 星上 MEC 的数据面架构设计 |
| P1 | `kg-for-6g-data-fabric-scenarios` | 交集 | pending | - | 数据知识图谱在 6G 网络数据编织中的具体应用场景 |
| P1 | `active-metadata-kg-integration` | 数据编织 | pending | - | 主动元数据引擎与知识图谱的集成模式 |
| P2 | `data-kg-open-source-comparison` | 数据编织 | pending | - | 开源数据知识图谱工具链（Atlas/Amundsen/DataHub）能力对比 |
| P1 | `data-virt-6g-cross-domain` | 交集 | pending | - | 数据虚拟化在 6G 跨域数据面中的架构适配 |
| P2 | `data-virt-platform-comparison` | 数据编织 | pending | - | Denodo/Dremio/Trino 等数据虚拟化平台能力对比 |
| P1 | `data-virt-data-mesh-patterns` | 数据编织 | pending | - | 数据虚拟化与数据网格的结合模式 |
| P1 | `data-orch-engine-comparison` | 数据编织 | pending | - | 主流数据编排引擎对比（Airflow/Dagster/Prefect/Databricks） |
| P1 | `data-orch-6g-cross-domain-scheduling` | 交集 | pending | - | 数据编排在 6G 网络数据面中的跨域流水线自动调度 |
| P2 | `event-driven-orch-streaming` | 数据编排 | pending | - | 事件驱动编排与流式数据管道的融合趋势 |

## 推荐子题清单（D1-D2 onboarding 完成后从这里挑入队列）

### A 类 · 6G 数据面侧 P0/P1
- `6g-data-plane-architecture-2025` [P0]
- `imt-2030-framework-data-needs` [P0]
- `user-plane-evolution-upf-to-6g` [P0]
- `ai-native-data-plane-status` [P0]
- `network-data-analytics-evolution-nwdaf-to-6g` [P1]
- `digital-twin-network-data-requirements` [P1]
- `isac-data-characteristics` [P1]
- `ntn-data-plane-differences` [P2]

### B 类 · 数据编织侧 P0/P1
- `data-fabric-definition-and-capabilities` [P0]
- `data-fabric-vs-data-mesh` [P0]
- `active-metadata-state-of-art` [P1]
- `knowledge-graph-for-data-management` [P1]
- `data-virtualization-and-orchestration` [P1]
- `data-fabric-products-2024-2025` [P1]

### C 类 · 交集议题 P0 ⭐
- `data-fabric-for-ai-native-6g` [P0] ⭐
- `cross-domain-data-governance-6g` [P0]
- `data-fabric-in-telecom-early-cases` [P0]
- `edge-data-fabric` [P1]
- `privacy-preserving-data-fabric-for-6g` [P1]
- `closed-loop-automation-data-fabric` [P1]

### 标准与厂商专项 P1/P2
- `3gpp-rel-19-20-data-architecture-status` [P0]
- `o-ran-ai-ml-data-architecture` [P1]
- `etsi-zsm-data-fabric-mapping` [P1]
- `huawei-zte-6g-data-stories` [P1]
- `ericsson-nokia-cognitive-network-data` [P1]
- `samsung-ntt-docomo-6g-data-vision` [P2]
