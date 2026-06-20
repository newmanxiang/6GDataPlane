# Concepts：核心概念地图

> 由 `6g-wiki-curator` 维护。每加入新概念卡片后刷新这张图。

## 概念地图

```mermaid
graph TD
    %% 6G 数据面侧（A类）
    DP[6G 数据面]
    DP --> UPE[用户面演进 UPF→6G DP]
    DP --> AIA[AI 原生空口]
    DP --> DTN[数字孪生网络]
    DP --> ISAC[通感一体]
    DP --> NTN[非地面网络]
    DP --> RAN[O-RAN/AI-RAN]
    DP --> NWDA[网络数据分析]

    %% A类内部关系
    DTN --> NWDA
    ISAC --> AIA
    ISAC -.-> DTN
    NTN --> UPE
    AIA --> RAN

    %% 数据编织侧（B类）
    DF[数据编织]
    DF --> AM[主动元数据]
    DF --> KG[数据知识图谱]
    DF --> DV[数据虚拟化]
    DF --> DO[数据编排]
    DF --> PP[隐私保护数据编织]
    DF --> DMESH[数据网格对比]

    %% B类内部关系（协作链条）
    AM -->|驱动| KG
    KG -->|语义发现| DV
    DV -->|统一访问| DO

    %% 交集议题（C类）
    DP -.->|TM Forum 实证| DF_TEL[数据编织在电信场景]
    DF_TEL -.-> DF
    DP -.->|⭐ 开拓性议题| DF_AIN[数据编织×AI 原生 6G]
    DF_AIN -.-> DF
    DF_AIN -.-> AIA
    DP -.-> EDGE[边缘数据编织]
    EDGE -.-> DF
    EDGE -.-> NTN
    PP -.-> DF_AIN
    NWDA -.-> DF_TEL
    DTN -.-> KG

    classDef dp fill:#e1f5ff,stroke:#0288d1;
    classDef df fill:#fff3e0,stroke:#f57c00;
    classDef cross fill:#f3e5f5,stroke:#7b1fa2;
    classDef gap fill:#ffebee,stroke:#c62828;
    class DP,UPE,AIA,DTN,ISAC,NTN,RAN,NWDA dp;
    class DF,AM,KG,DV,DO,PP,DMESH df;
    class DF_TEL,EDGE cross;
    class DF_AIN gap;
```

## 概念清单

### A. 6G 数据面侧
- [x] `6g-overview` — 6G 总体愿景 (draft)
- [x] `6g-data-plane` — 6G 数据面 (draft)
- [x] `user-plane-evolution` — 用户面演进 (draft)
- [x] `ai-native-air-interface` — AI 原生空口 (draft)
- [x] `ran-architecture-evolution` — RAN 架构演进 (draft)
- [x] `network-data-analytics` — 网络数据分析 (draft)
- [x] `digital-twin-network` — 数字孪生网络 (draft)
- [x] `isac` — 通感一体 (draft)
- [x] `non-terrestrial-network` — 非地面网络 (draft)

### B. 数据编织侧
- [x] `data-fabric-definition` — 数据编织定义 (draft)
- [x] `data-fabric-vs-data-mesh` — 数据编织 vs 数据网格 (draft)
- [x] `data-fabric-capabilities` — 数据编织核心能力域 (draft)
- [x] `active-metadata` — 主动元数据 (draft)
- [x] `knowledge-graph-for-data` — 数据知识图谱 (draft)
- [x] `data-virtualization` — 数据虚拟化 (draft)
- [x] `data-orchestration` — 数据编排 (draft)

### C. 交集议题（W2 重点）
- [x] `data-fabric-in-telecom` — 数据编织在电信场景 (draft)
- [x] `data-fabric-for-ai-native-6g` — 数据编织×AI原生6G (draft) ⚠️ 文献稀缺
- [x] `edge-data-fabric` — 边缘数据编织 (draft)
- [x] `privacy-preserving-data-fabric` — 隐私保护数据编织 (draft)

> 由 `6g-onboarding` 创建占位卡片，由 `6g-deep-dive` 充实内容，由 `6g-wiki-curator` 治理。
