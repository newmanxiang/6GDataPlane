---
title: 6G 总体愿景
title_en: 6G Overall Vision
slug: 6g-overview
category: concept
status: draft
confidence: low
sources:
  - https://www.itu.int/en/ITU-R/study-groups/rsg5/rwp5d/imt-2030/Pages/default.aspx
  - https://www.itu.int/hub/2026/03/imt-2030-technical-requirements-for-the-6g-future/
  - https://digitalregulation.org/overview-of-6g-imt-2030/
related:
  - 6g-data-plane
  - user-plane-evolution
  - ai-native-air-interface
  - imt-2030
  - imt-2030-usage-scenarios-data-needs
  - 6g-kpi-20-requirements
  - imt-2030-framework-data-needs
tags:
  - 6G
  - IMT-2030
  - ITU-R
  - 愿景
last_verified: 2026-06-20
owner: agent
---

# 6G 总体愿景（6G Overall Vision）

> 6G 是 ITU-R 定义的第六代移动通信系统（IMT-2030），目标在 2030 年商用，提供沉浸式通信、超大规模连接、AI 与通信融合等全新能力。

## 定义

6G（IMT-2030）是 ITU-R WP 5D 于 2023 年发布框架建议书（ITU-R M.2160）中定义的下一代移动通信系统，2026 年 2 月完成技术性能需求制定，定义了 20 项最低技术性能指标 [1][2]。

## 关键组成 / 子能力

- **沉浸式通信**：支持全息通信、扩展现实（XR），峰值速率目标 200 Gbps
- **超大规模连接**：连接密度达 10⁸ 设备/km²，支持物联网大规模部署
- **AI 与通信深度融合**：AI 原生空口，网络内生智能
- **通感一体（ISAC）**：通信与感知功能集成，厘米级定位精度
- **可持续性**：能效相比 5G 提升 100 倍，支撑绿色网络

## 与相邻概念的关系

- 与 [[6g-data-plane]]：6G 总体架构中数据面是核心功能平面之一，承载用户数据传输与数据服务
- 与 [[user-plane-evolution]]：6G 是用户面从 GTP-U/UPF 向新型数据面演进的目标系统
- 与 [[imt-2030]]：IMT-2030 是 ITU-R 对 6G 的正式技术命名与框架规范
- 与 [[imt-2030-usage-scenarios-data-needs]]：六大使用场景的数据面需求详细分析

## 常见误解

- **误解 1**："6G 只是速度更快的 5G"——实际上 6G 引入了全新的能力维度（感知、AI、计算），不仅是传统 KPI 的线性提升
- **误解 2**："6G 标准已冻结"——截至 2026 年中，ITU-R 已完成性能需求，但 3GPP 标准制定（Rel-22+）尚在早期阶段

## 待深挖子题

- [x] IMT-2030 六大使用场景及其对数据面的具体需求 → 已完成：[[imt-2030-usage-scenarios-data-needs]]
- [ ] 6G KPI 量化指标全表（20 项性能需求解读）
- [ ] 3GPP 6G 标准时间线与里程碑（Rel-22/23 规划）

## 来源

[1] [IMT towards 2030 and beyond](https://www.itu.int/en/ITU-R/study-groups/rsg5/rwp5d/imt-2030/Pages/default.aspx) — ITU-R WP 5D 官方页面，含 IMT-2030 技术性能需求
[2] [IMT-2030: Technical requirements for the 6G future](https://www.itu.int/hub/2026/03/imt-2030-technical-requirements-for-the-6g-future/) — ITU 新闻，2026 年 3 月发布
[3] [Overview of 6G (IMT-2030)](https://digitalregulation.org/overview-of-6g-imt-2030/) — Digital Regulation 综述
