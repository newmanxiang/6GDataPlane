# 精读笔记：imt-2030-usage-scenarios-data-needs

> 调研日期：2026-06-21
> 调研代理：6g-deep-dive

## [ITU-R M.2160-0] (标准，2023-11)
URL: https://www.itu.int/dms_pubrec/itu-r/rec/m/R-REC-M.2160-0-202311-I!!PDF-E.pdf

### 关键数据点
- 6 个使用场景：IC、HRLLC、MC、UC、AIAC、ISAC
- 15 项能力指标（9 项量化 + 6 项定性）
- 峰值速率研究目标：50/100/200 Gbps
- 用户体验速率：300/500 Mbps
- 连接密度：10⁶–10⁸ devices/km²
- 时延：0.1–1 ms
- 可靠性：10⁻⁵ ~ 10⁻⁷
- 移动性：500–1000 km/h
- 定位精度：1–10 cm

### 关键论断
- IC 覆盖热点、城区、农村环境，需支持视频/音频/触觉等混合流量的时间同步传输
- HRLLC 面向时间同步操作场景，故障将导致严重后果
- MC 扩展 mMTC，支持无电池或长寿命电池设备
- UC 通过与卫星、HAPS、Wi-Fi 互通弥合数字鸿沟
- AIAC 涵盖数据采集、分布式 AI 模型训练、模型共享、分布式推理
- ISAC 提供高精度定位和环境感知（含姿态识别、运动检测、环境监测）
- "能力值仅适用于部分使用场景，不可在单一场景中同时达到"

### 新术语
- Overarching aspects（跨场景设计原则）
- Palette diagram（调色板图 — 能力可视化）

---

## [NGMN: ITU-R Framework Review] (产业联盟，2024-02)
URL: https://www.ngmn.org/wp-content/uploads/ITU-R_FRAMEWORK_FOR_IMT-2030.pdf

### 关键数据点
- NGMN 识别了 50 个 6G 用例，分四类：增强人类通信、增强机器通信、使能服务、网络演进
- 峰值速率目标：50/100/200 Gbps
- 用户体验速率：300/500 Mbps
- 频谱效率：1.5× 或 3× IMT-2020
- 空口时延：0.1–1 ms
- 许多 5G 极端能力"已被证明难以交付"（20 Gbps、1 ms 时延）

### 关键论断
- 6G 应通过软件升级逐步部署功能，不应损害语音等基础服务
- 新 RIT 必须在频谱效率和/或能效方面比 5G 有"显著提升"才能被广泛采用
- 报递的边际效应须被考虑（law-of-diminishing returns）
- 低时延目标对系统设计有重大影响，会妥协频谱效率和系统容量

### 与其他来源的矛盾
- NGMN 对极端指标持审慎态度，与 M.2160 框架的雄心有张力

---

## [6G-IA Contribution to WP 5D] (产业联盟，2025-06)
URL: https://6g-ia.eu/wp-content/uploads/2025/06/6g_ia-contribution_wp5d-120625.pdf

### 关键数据点（TPR 具体目标值）
- 峰值速率 DL：20–50 Gbps（仅 1–2.5× IMT-2020）
- 峰值速率 UL：10–25 Gbps
- 用户体验速率（密集城区 IC DL）：125–500 Mbps
- 区域流量容量（室内热点 IC DL）：10–50 Mbps/m²
- 连接密度（MC）：10⁶–10⁷ devices/km²
- 用户面时延 IC：2–8 ms（DL/UL）
- 用户面时延 HRLLC：1 ms（DL/UL）
- 控制面时延 IC/HRLLC：10–20 ms
- 可靠性 HRLLC：99.999%
- 定位精度：0.4 m（主选）/ <1 m（备选）
- 带宽：400 MHz
- 移动中断时间：0 ms

### 关键论断
- 感知、AI、能效指标的定义和目标值"需要进一步分析"
- 覆盖无需直接量化评估
- 安全和互操作性通过"检查"方式评估

### 与其他来源的矛盾
- 峰值速率：框架 200 Gbps vs TPR 50 Gbps（性质不同但差距显著）
- 连接密度：框架 10⁸ vs TPR 10⁷ 上限
- 定位精度：框架 1–10 cm vs TPR 0.4 m（40 cm）— 差距明显

---

## [IEEE ComSoc: WP 5D Feb 2026 Meeting] (媒体，2026-03)
URL: https://techblog.comsoc.org/2026/03/17/update-imt-2030-6g-minimum-technology-performance-requirements/

### 关键数据点
- 20 项 TPR 达成一致，其中 7 项为 6G 新增
- 正式批准预计 2026 年 12 月 SG5 会议

### 关键论断
- TPR 建立最低性能水平，不限制实现方式
- 3GPP 将单独制定 6G 核心网和架构性能需求

---

## [arXiv 2501.14552v2: 6G Cellular Networks Landscape] (学术，2025)
URL: https://arxiv.org/html/2501.14552v2

### 关键数据点（5G vs 6G 对比表）
| 指标 | 5G | 6G | 倍数 |
|------|-----|------|------|
| 峰值速率 | 20 Gbps | 200 Gbps | 10× |
| 用户体验速率 | ~100 Mbps | 300–500 Mbps | 3–5× |
| 频谱效率 | ~30 bps/Hz | 45–90 bps/Hz | 1.5–3× |
| 区域流量容量 | ~10 Mbps/m² | 30–50 Mbps/m² | 3–5× |
| 连接密度 | 10⁶/km² | 10⁸/km² | 100× |
| 时延 | 1 ms | 0.1–1 ms | ≤10× |
| 可靠性 | 10⁻⁵ | 10⁻⁷–10⁻⁹ | 100–10000× |
| 移动性 | 500 km/h | 500–1000 km/h | 2× |
| 定位精度 | ~10 m | 1–10 cm | ≥100× |
| 覆盖 | 空地有限 | 空-天-地-海全域 | 全球化 |

### 关键论断
- IMT-2030 定义 4 个核心设计原则：连接未连接者、泛在智能、安全韧性、可持续性
- 大部分 6G 文献（49.9%）聚焦技术使能器，应用场景研究（19.8%）相对不足

---

## [5G Americas: ITU's IMT-2030 Vision] (产业联盟，2024-08)
URL: https://www.5gamericas.org/wp-content/uploads/2024/08/ITUs-IMT-2030-Vision_Id.pdf

### 关键数据点
- 美国政府 NSF RINGS 计划：$44M 资助 37 个 6G 相关项目
- DoD MEC Hubs：$1.6B 半导体创新枢纽计划含 5G/6G 主题
- 6G 需"云原生"，计算和数据服务与通信紧密集成

### 关键论断
- 6G 必须确保从 5G 到 6G 的无缝高效迁移
- 美洲应以"用例和商业机会驱动"而非"为进步而进步"
- 传统语音和 SMS（含 E911、合法监听）的延续性是关键需求

---

## 搜索统计

| 搜索轮次 | 工具 | 候选 URL 数 |
|---------|------|------------|
| 第 1 轮（通用） | Exa | 15 |
| 第 2 轮（场景细节） | Exa | 15 |
| 第 3 轮（TPR/学术） | Exa | 15 |
| 第 4 轮（ISAC/数据面） | Exa | 15 |
| 第 5 轮（ITU 官方） | Firecrawl | 10 |
| 第 6 轮（批评/局限） | Firecrawl | 10 |
| 第 7 轮（3GPP/NGMN/Hexa-X） | Firecrawl | 10 |
| **去重后总计** | | **~65** |

精读来源：13 篇
