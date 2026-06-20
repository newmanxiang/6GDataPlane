---
title: 用户面演进
title_en: User Plane Evolution
slug: user-plane-evolution
category: concept
status: draft
confidence: low
sources:
  - https://www.ietf.org/archive/id/draft-zzhang-dmm-mup-evolution-09.html
  - https://upcommons.upc.edu/bitstreams/cbf1149a-6615-4d7c-8818-0bb5bc5a4b5a/download
  - https://mvno-index.com/user-plane-function-upf/
related:
  - 6g-overview
  - 6g-data-plane
  - ran-architecture-evolution
tags:
  - 用户面
  - GTP-U
  - UPF
  - 演进
  - CUPS
last_verified: 2026-06-20
owner: agent
---

# 用户面演进（User Plane Evolution）

> 移动通信用户面从 4G 的 GTP-U 隧道承载，经 5G UPF 实现控制/用户面分离（CUPS），向 6G 灵活可编程数据面持续演进。

## 定义

用户面演进是指移动通信网络中负责实际用户数据传输的功能实体及协议栈的代际变迁。核心脉络为：4G EPC 中的 S-GW/P-GW 使用 GTP-U 隧道 → 5G 核心网 UPF 实现完整 CUPS → 6G 面向 AI 原生和多样化业务的新型可编程数据面 [1][2]。

## 关键组成 / 子能力

- **4G GTP-U 阶段**：S-GW/P-GW 基于 GTP-U（GPRS Tunnelling Protocol - User Plane）隧道转发，控制面与用户面耦合度高
- **5G UPF 阶段**：引入独立 UPF 网元，实现 CUPS 解耦；支持边缘部署（MEC）、网络切片、上行分类器（UL-CL）[3]
- **6G 新型数据面**：GTP-U 的固有限制（隧道开销、灵活性不足）被识别为 6G 瓶颈；6G-RUPA 等方案探索基于 SRv6/网络编程的替代架构 [2]
- **协议栈演进方向**：从固定隧道 → 可编程转发 → 数据服务化

## 与相邻概念的关系

- 与 [[6g-data-plane]]：6G 数据面是用户面演进的下一代目标形态，在转发基础上增加数据服务能力
- 与 [[6g-overview]]：用户面演进是 6G 系统架构变革的核心线索之一
- 与 **CUPS（Control and User Plane Separation）**：5G 阶段确立的基本原则，6G 将进一步深化

## 常见误解

- **误解 1**："5G UPF 已经够用，6G 不需要重新设计用户面"——6G-RUPA 研究表明 GTP-U 在灵活性、可扩展性和能效方面不满足 6G 需求 [2]
- **误解 2**："用户面只是'管道'"——6G 用户面将承担数据处理、AI 推理卸载等智能功能，不再是纯转发管道

## 待深挖子题

- [ ] GTP-U 具体局限性分析与 6G 替代方案（SRv6、网络编程）→ 加入 ops/deep-dive-queue.md
- [ ] IETF MUP（Mobile User Plane）草案解读与 6G 适用性
- [ ] UPF 分布式部署模式在 6G 中的延续与变革

## 来源

[1] [Mobile User Plane Evolution](https://www.ietf.org/archive/id/draft-zzhang-dmm-mup-evolution-09.html) — IETF 草案，描述 5G 用户面演进方向
[2] [6G-RUPA: Flexible, Scalable User Plane Architecture](https://upcommons.upc.edu/bitstreams/cbf1149a-6615-4d7c-8818-0bb5bc5a4b5a/download) — 学术论文，分析 GTP-U 局限与 6G 用户面新架构
[3] [User Plane Function UPF in 5G Core Explained](https://mvno-index.com/user-plane-function-upf/) — MVNO Index，5G UPF 功能详解
