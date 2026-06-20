---
term: User Plane Function
abbr: UPF
cn: 用户面功能
slug: upf
category: glossary
related:
  - user-plane-evolution
  - 6g-data-plane
  - gtp-u
source: https://www.3gpp.org/technologies/5g-system-overview
---

# UPF — User Plane Function

> 5G 核心网中负责用户数据包转发、QoS 执行和流量检测的独立网元，是 CUPS 架构的核心实现。

**中文**：用户面功能  
**英文**：User Plane Function  
**缩写**：UPF

## 定义

UPF 是 3GPP 5G 核心网（5GC）架构中的用户面网元，实现了控制面与用户面的完整分离（CUPS）。其主要功能包括：PDU 会话锚点、数据包转发与路由、QoS 策略执行、流量检测与计费、上行分类器（UL-CL）以及边缘计算（MEC）分流。UPF 可灵活部署于中心或边缘位置。

## 相关概念

- [[user-plane-evolution]] — UPF 是用户面演进中 5G 阶段的关键里程碑
- [[gtp-u]] — UPF 内部仍使用 GTP-U 隧道协议进行数据封装
- [[6g-data-plane]] — 6G 数据面是 UPF 的下一代演进形态
