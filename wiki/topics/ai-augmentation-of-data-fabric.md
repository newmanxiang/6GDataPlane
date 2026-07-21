---
title: AI 对数据编织的加持——从工具增强到 Agentic 数据管理
title_en: AI Augmentation of Data Fabric - From Copilot to Agentic Data Management
slug: ai-augmentation-of-data-fabric
category: topic
status: reviewed
confidence: medium-high
sources:
  - https://www.gartner.com/en/newsroom/press-releases/2025-02-26-lack-of-ai-ready-data-puts-ai-projects-at-risk
  - https://www.gartner.com/en/newsroom/press-releases/2025-06-02-gartner-predicts-by-2028-80-percent-of-genai-business-apps-will-be-developed-on-existing-data-management-platforms
  - https://www.gartner.com/en/newsroom/press-releases/2026-03-11-gartner-announces-top-predictions-for-data-and-analytics-in-2026
  - https://www.computerweekly.com/news/366645295/Gartner-declares-agentic-AI-the-next-step-function
  - https://www.informatica.com/blogs/introducing-agentic-goal-driven-data-management-with-claire-gpt.html
  - https://www.informatica.com/about-us/news/news-releases/2026/05/20260520-informatica-from-salesforce-delivers-the-trusted-data-foundation-every-ai-agent-needs-now-across-every-surface-every-platform-everywhere.html
  - https://community.ibm.com/community/user/blogs/diana-toma/2026/04/23/ibm-introduces-agentic-data-intelligence
  - https://www.eurecom.fr/en/publication/8732
  - https://arxiv.org/abs/2601.13114
  - https://arxiv.org/abs/2607.16066
  - https://huggingface.co/datasets/GSMA/oran_spec_knowledge_graph
  - https://huggingface.co/datasets/KU-DFI/telecom-knowledge-graph-rel19
  - https://ar5iv.labs.arxiv.org/html/2503.24245
  - https://illumex.ai/blog/active-metadata-your-secret-weapon-for-data-driven-success/
related:
  - data-fabric-definition-and-capabilities
  - data-fabric-for-ai-native-6g
  - ai-native-data-plane-status
  - cross-domain-data-governance-6g
tags: [data-fabric, AI, GenAI, agentic-AI, active-metadata, knowledge-graph, LLM, MCP, NWDAF]
last_verified: 2026-07-21
owner: agent
---

# AI 对数据编织的加持——从工具增强到 Agentic 数据管理

## 核心结论（150 字内）

AI 与数据编织的关系是双向的：数据编织为 AI 供数（AI-ready data），AI 反过来正在重构数据编织的实现方式。2025-2026 年证据显示三条加持路径已成型：①LLM 大幅降低元数据标注与知识图谱构建成本（电信标准 KG 已有开源实证）；②数据管理头部厂商（Informatica/IBM）已把多智能体架构产品化（GA 级）；③Gartner 判断"元数据爆炸使 Agentic 数据管理不可避免"，并预测语义层将在 2030 年成为与数据平台并列的关键基础设施。电信侧 Agentic-NWDAF/IntAgent 原型证明该范式可下沉到网络数据场景。[信心：中高]

## 1. 现状定义

"AI 对数据编织的加持"指用 GenAI/LLM/AI Agent 技术**实现或增强**数据编织的各能力域，而非（仅）用数据编织为 AI 供数。可分三代：

| 代际 | 形态 | 典型实现 | 状态（2026 中） |
|---|---|---|---|
| 一代：AI 辅助 | ML 驱动的推荐/检测（Gartner 原始定义中的 AI/ML 增强） | 集成路径推荐、质量异常检测、NL2SQL | 产品成熟 |
| 二代：GenAI 增强 | LLM 做元数据富化、语义标注、对话式数据发现 | Informatica CLAIRE GPT（2025-11）、IBM watsonx Data Intelligence Chat Agent | GA |
| 三代：Agentic 数据管理 | 多智能体自主执行数据集成/质量/治理任务，人只审批例外 | Informatica Headless CLAIRE 多智能体层（2026 春 GA）、IBM Agentic Data Intelligence（2026-04） | GA 初期/预览 |

## 2. 标准与组织动态

- **Gartner AI-ready data 调查（2025-02）**：对 1,203 名数据管理负责人的调查（2024-07 执行）显示 **63% 组织没有或不确定是否有支撑 AI 的数据管理实践**；预测到 2026 年 **60% 缺乏 AI-ready 数据支撑的 AI 项目将被放弃**。核心建议：元数据从被动转主动。
- **Gartner（2025-06）**：预测到 2028 年 **80% 的 GenAI 业务应用将构建在既有数据管理平台之上**；RAG 精度依赖目录/元数据提供的语义。
- **Gartner D&A Summit 2025（Beyer）**：仅 **12%** 公司实现了主动元数据分析；64% 使用元数据治理方案但很少是 AI 驱动的——供需缺口显著。
- **Gartner Top D&A Predictions 2026（2026-03）**：①到 2030 年**通用语义层（universal semantic layer）将被视为与数据平台、网络安全并列的关键基础设施**；②组织将使用自主 AI Agent 把政策/技术标准转译为**机器可验证的数据合约**，自动化合规与治理策略执行；③到 2029 年 AI Agent 从物理环境产生的数据将达数字 AI 应用总和的 10 倍。
- **Gartner D&A Summit 2026 悉尼（Beyer）**："每次数据复用产生约 100 个新元数据点"，元数据以人力不可及的速度爆炸，因此 **Agentic AI 进入数据生态是不可避免的**；未来的建设对象"不再是数据管道，而是理解数据如何被使用的智能体"。
- **MCP（Model Context Protocol）事实标准化**：IBM 与 Informatica 均以 MCP 作为 AI Agent 访问数据编织能力（目录/血缘/治理策略）的接口协议；电信学术界（Agentic-NWDAF、IntAgent）同样采用 MCP 连接 LLM Agent 与 NWDAF。MCP 正在成为"Agent-数据平台"接口的事实标准。

## 3. 关键玩家

### IT 数据管理厂商（产品化最快）

| 厂商 | 产品动作 | 时间 |
|---|---|---|
| Informatica（Salesforce） | CLAIRE GPT 升级为 agentic 目标驱动数据管理（监督者 Agent 编排 Discovery/Integration/Quality 等专职 Agent） | 2025-11 |
| Informatica | Headless CLAIRE 多智能体层 GA；Data Quality Agent GA；Metadata Enrichment Agent（Q4 2026）；Agent Fabric Context Catalog（统一治理数据资产+AI Agent 的目录） | 2026-05 |
| IBM | watsonx.data intelligence 推出 Agentic Data Intelligence：托管 MCP Server 向外部 Agent 暴露目录/血缘/治理；Data Intelligence Chat Agent | 2026-04 |

### 电信侧（学术原型领先、产品跟进中）

| 玩家/项目 | 动作 |
|---|---|
| EURECOM Agentic-NWDAF（ICC 2026） | 意图驱动编排层：自然语言意图→NWDAF 服务调用，MCP 架构，100 条 3GPP 意图基准验证 |
| IntAgent（arXiv 2601.13114） | 在 NWDAF 分析引擎内构建意图工具引擎，LLM Agent 用实时网络分析驱动推理与工具选择 |
| LLM-Powered Agentic AI for 5G/6G survey（arXiv 2607.16066） | 系统综述 LLM Agent 在 RAN/CN/TN 各域的数据操作（telemetry 收集、日志语义化）架构与协议 |
| GSMA Open Telco Assets / KU-DFI | 开源电信知识图谱：O-RAN 规范 KG（25,103 节点/98,679 关系，GPT-4.1 抽取）；3GPP Rel-19 KG（21,540 节点/31,718 边） |

## 4. 技术机制：AI 加持数据编织的四条路径

### 4.1 LLM 驱动的元数据与知识图谱自动构建

传统数据编织最大成本项是本体设计与元数据人工维护。LLM 实体/关系抽取使 KG 构建成本数量级下降：企业场景 LLM 抽取精度约 85-92%（对比五年前规则系统 60-70%，单一来源引述 Microsoft Research 2025 [中]）；电信场景已有直接实证——GSMA 用 GPT-4.1 从 O-RAN 规范全自动抽取 2.5 万节点级 KG 并开源。这直接回应了"电信本体三套并存（3GPP/O-RAN/TM Forum SID）、自动本体构建不成熟"的历史断点：**LLM 正在把"电信语义层"从人力密集型工程变为可自动化管道**。[中高]

### 4.2 元数据富化直接提升 AI 供数质量（闭环证据）

IEEE CAI 2026 研究（arXiv 2512.05411，经 Atlan 转述 [仅一源]）：仅在检索前做 LLM 元数据富化，RAG 精度从 73.3% 提升至 82.5%（+9.2pp），检索算法/嵌入模型不变——证明"编织层语义投入→AI 输出质量"存在可量化的正反馈闭环。

### 4.3 Agentic 数据管理：编织能力的执行主体从人变为 Agent

Gartner 自动化三阶段（Alert→Recommendation→Autonomous）正在被多智能体架构实现：监督者 Agent 编排专职 Agent（发现/集成/质量/治理），经 MCP 调用编织层的目录/血缘/策略工具。驱动力是元数据爆炸（复用一次×100 元数据点）超出人力极限。厂商已 GA（Informatica/IBM），但自治程度仍以"推荐+人审批"为主，全自治处早期。[中]

### 4.4 意图接口：数据消费方式从查询变为意图

数据编织的消费接口从 SQL/API 演进为自然语言意图：Agentic-NWDAF 证明电信网络分析可用"意图→MCP→NWDAF 服务调用"链路实现，并以 LLM-as-a-Judge 验证可靠性。这为 6G"智能体自主发现/订阅网络数据"提供了具体技术形态。[中]

## 5. 趋势驱动力

1. **元数据爆炸**：数据复用频率×元数据增殖率超出人工管理极限（Gartner 2026）
2. **AI 项目高失败率倒逼**：60% AI 项目因缺 AI-ready 数据被弃（Gartner 预测）——供数质量成为 AI 落地瓶颈，编织层被推向前台
3. **语义层基础设施化**：Gartner 预测 2030 年通用语义层成为关键基础设施——语义能力从"锦上添花"变为"必须预算项"
4. **MCP 生态汇聚**：Agent-数据接口协议事实收敛，降低编织层对接 Agent 生态的成本
5. **电信 KG 开源化**：GSMA Open Telco Assets 等开源电信 KG 降低网络语义层冷启动成本

## 6. 批评与风险

1. **自治可信度**：Gartner 同时警告需在低风险管道先试验治理 Agent、验证其对上下文/协议的理解后再扩大——全自治数据管理的错误成本在电信网络场景被放大
2. **LLM 抽取质量的领域衰减**：85-92% 精度来自通用企业实体；电信协议实体（参数/IE/接口）的抽取精度缺公开基准
3. **供应商叙事超前**：Agentic 数据管理产品多为 2026 年 GA 初期，独立客户验证数据几乎为零
4. **精度提升数据单一来源**：RAG +9.2pp 证据链依赖单一研究转述，需追踪原文
5. **电信侧仍是原型**：Agentic-NWDAF/IntAgent 为学术验证，无运营商生产部署报告

## 数据缺口

1. **P1**：Agentic 数据管理产品（CLAIRE Agents/IBM ADI）的独立客户 ROI 数据
2. **P1**：LLM 对电信协议实体抽取精度的公开基准
3. **P2**：MCP 在电信网络数据场景的安全模型评估（Agent 越权访问网络数据的风险）
4. **P2**：arXiv 2512.05411 原文精读（当前经 Atlan 转述）

## 来源

### 分析机构 / 官方
1. [Gartner: Lack of AI-Ready Data Puts AI Projects at Risk](https://www.gartner.com/en/newsroom/press-releases/2025-02-26-lack-of-ai-ready-data-puts-ai-projects-at-risk) — 2025-02-26，63%/60% 调查数据
2. [Gartner: 80% of GenAI Business Apps on Existing Data Management Platforms by 2028](https://www.gartner.com/en/newsroom/press-releases/2025-06-02-gartner-predicts-by-2028-80-percent-of-genai-business-apps-will-be-developed-on-existing-data-management-platforms) — 2025-06-02
3. [Gartner: Top Predictions for Data and Analytics in 2026](https://www.gartner.com/en/newsroom/press-releases/2026-03-11-gartner-announces-top-predictions-for-data-and-analytics-in-2026) — 2026-03-11，通用语义层/治理 Agent/物理 AI 数据预测
4. [Computer Weekly: Gartner declares 'agentic AI' the next step function](https://www.computerweekly.com/news/366645295/Gartner-declares-agentic-AI-the-next-step-function) — 2026，D&A Summit 悉尼 Beyer 观点（100 元数据点/复用）
5. [illumex: Gartner D&A Summit 2025 Beyer 主动元数据演讲纪要](https://illumex.ai/blog/active-metadata-your-secret-weapon-for-data-driven-success/) — 12% 主动元数据采纳率（转述 [中]）

### 厂商
6. [Informatica: Introducing Agentic, Goal-Driven Data Management with CLAIRE GPT](https://www.informatica.com/blogs/introducing-agentic-goal-driven-data-management-with-claire-gpt.html) — 2025-11-25
7. [Informatica from Salesforce: Trusted Data Foundation for Every AI Agent](https://www.informatica.com/about-us/news/news-releases/2026/05/20260520-informatica-from-salesforce-delivers-the-trusted-data-foundation-every-ai-agent-needs-now-across-every-surface-every-platform-everywhere.html) — 2026-05-20，Headless CLAIRE / Agent Fabric Context Catalog 路标
8. [IBM: Agentic Data Intelligence in watsonx.data intelligence](https://community.ibm.com/community/user/blogs/diana-toma/2026/04/23/ibm-introduces-agentic-data-intelligence) — 2026-04-23，托管 MCP Server

### 学术 / 电信
9. [EURECOM: Agentic-NWDAF（ICC 2026）](https://www.eurecom.fr/en/publication/8732) — 意图驱动 NWDAF 编排，MCP 架构
10. [IntAgent: NWDAF-Based Intent LLM Agent](https://arxiv.org/abs/2601.13114) — 2026-01
11. [LLM-Powered Agentic AI for 5G/6G Networks: Tutorial and Survey](https://arxiv.org/abs/2607.16066) — 2026-07
12. [GSMA O-RAN Spec Knowledge Graph（Hugging Face）](https://huggingface.co/datasets/GSMA/oran_spec_knowledge_graph) — GPT-4.1 自动抽取，25,103 节点
13. [KU-DFI 3GPP Rel-19 Telecom Knowledge Graph（Hugging Face）](https://huggingface.co/datasets/KU-DFI/telecom-knowledge-graph-rel19) — 2026，GSMA Open Telco Assets Initiative
14. [Enhancing LLMs for Telecommunications using KG and RAG](https://ar5iv.labs.arxiv.org/html/2503.24245) — arXiv 2503.24245
15. [Atlan: LLM Knowledge Base Data Quality](https://atlan.com/know/llm-knowledge-base-data-quality/) — 转述 IEEE CAI 2026 RAG 元数据富化 +9.2pp（[仅一源]）
