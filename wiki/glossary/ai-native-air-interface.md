---
term: AI-Native Air Interface
abbr: AI-NativeAI
cn: AI 原生空口
slug: ai-native-air-interface
category: glossary
related:
  - ran-architecture-evolution
  - 6g-data-plane
  - network-data-analytics
source: https://techblog.comsoc.org/2026/01/15/comparing-ai-native-mode-in-6g-imt-2030-vs-ai-overlay-add-on-status-in-5g-imt-2020/
---

# AI-Native Air Interface — AI 原生空口

> 将 AI/ML 作为 6G 无线空中接口协议栈的原生设计要素，而非外挂附加模块的设计范式。

**中文**：AI 原生空口
**英文**：AI-Native Air Interface
**缩写**：—（无统一缩写）

## 定义
AI 原生空口是 6G 标准中提出的设计理念，将 AI/ML 深度嵌入物理层信道编解码、波束管理、资源调度等无线接入核心功能。与 5G 的 AI overlay 模式（如通过 RIC xApp 叠加智能）不同，AI 原生意味着空口协议栈在设计之初即考虑模型训练、推理与更新的原生支持。ITU-R IMT-2030（6G）框架将 AI 原生列为核心设计原则之一。

## 相关概念
- [[ran-architecture-evolution]] O-RAN/AI-RAN 提供 AI 原生空口的基础设施支撑
- [[6g-data-plane]] 数据面负责空口 AI 模型的训练数据传输与模型分发
- [[network-data-analytics]] 空口数据是网络分析功能的重要输入源
