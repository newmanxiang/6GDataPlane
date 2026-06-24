---
title: GTP-U 将在 6G 时代被 SRv6/MUP 等方案逐步替代
slug: trend-gtp-u-sunset
horizon: 36m
confidence: medium
direction: emerging
drivers:
  - GTP-U 状态爆炸和封装开销的根本性局限
  - SoftBank SRv6 MUP 全球首商用验证
  - NVIDIA dUPF 100 Gbps 高性能替代验证
  - DT 在 IETF 123 推动 MUP 移动性管理
  - RAN-CN 融合趋势消除 N3 接口需求
inhibitors:
  - GTP-U 20+ 年部署基础的向后兼容压力
  - 3GPP CT 未启动 GTP-U 替代正式讨论
  - 运营商网络改造投资的巨大沉没成本
  - SRv6 IPv6 部署先决条件
evidence:
  - gtp-u-limitations-6g-alternatives
  - user-plane-evolution-upf-to-6g
  - 6g-data-plane-architecture-2025
counter_evidence:
  - gtp-u-limitations-6g-alternatives
  - 3gpp-6g-timeline-rel22-23
companies_to_watch:
  - SoftBank
  - Deutsche Telekom
  - NVIDIA
  - Samsung
  - EURECOM
  - Cisco
my_company_relevance: high
created: 2026-06-25
---

# GTP-U 将在 6G 时代被 SRv6/MUP 等方案逐步替代

## 一句话总结

GTP-U 协议在 6G 环境下的根本性局限已有共识，SRv6 MUP 是最有力替代者，但过渡路径仍高度不确定。

## 论据（按强度排序）

1. **GTP-U 根本性局限已达共识**：GTP-U 的隧道状态爆炸（O(N×M) 复杂度）、8 字节封装开销导致 MTU 浪费（~1.5%）、缺乏传输层感知能力（无法区分时延敏感流与尽力而为流）是 6G 高性能数据面无法接受的。学术界和多家厂商已形成共识。→ [gtp-u-limitations-6g-alternatives](../../wiki/topics/gtp-u-limitations-6g-alternatives.md)

2. **SoftBank SRv6 MUP 全球首商用**：SoftBank 2024 年实现 SRv6 MUP 商用部署，将 GTP-U 隧道状态从 O(N×M) 降至 O(N+M)，验证了 SRv6 在移动网络的可行性。这是迄今最强的产业验证信号。→ [gtp-u-limitations-6g-alternatives](../../wiki/topics/gtp-u-limitations-6g-alternatives.md)

3. **NVIDIA dUPF 高性能验证**：基于 NVIDIA DOCA/BlueField 的 dUPF 实现 100 Gbps 吞吐 / 25μs 延迟，使用 P4 可编程数据面绕过 GTP-U 传统处理流水线，证明硬件加速替代方案的性能优势。→ [user-plane-evolution-upf-to-6g](../../wiki/topics/user-plane-evolution-upf-to-6g.md)

4. **IETF MUP 架构推进**：DT 在 IETF 123 提交的 MUP 架构提案获关注，将移动用户面功能映射到 SRv6 Segment，实现传输与移动性的统一编程模型。IETF 与 3GPP 的联动是关键推动力。→ [gtp-u-limitations-6g-alternatives](../../wiki/topics/gtp-u-limitations-6g-alternatives.md)

5. **RAN-CN 融合消除 N3**：Samsung M-UP (Merged User Plane) 和 EURECOM IUP (Integrated User Plane) 从架构层面消除 RAN-Core 之间的 N3 接口，使 GTP-U 在接入侧失去存在基础。→ [gtp-u-limitations-6g-alternatives](../../wiki/topics/gtp-u-limitations-6g-alternatives.md)

## 反向证据 / 不确定性

- **20+ 年部署基础的惯性**：GTP 从 2G GPRS 时代延续至今，全球移动网络深度依赖 GTP-U。替代意味着所有 RAN-Core 接口、漫游接口、互联互通协议的全面改造 → [gtp-u-limitations-6g-alternatives](../../wiki/topics/gtp-u-limitations-6g-alternatives.md)
- **3GPP 正式讨论推迟**：截至 2026 年中，3GPP CT 组未启动 GTP-U 替代的正式 Study Item。历史上 3GPP 倾向于渐进演进而非革命替代 → [3gpp-6g-timeline-rel22-23](../../wiki/topics/3gpp-6g-timeline-rel22-23.md)
- **SRv6 依赖全面 IPv6 部署**：MUP 方案以 SRv6 为基础，而全球 IPv6 部署进度不一致。部分市场（日本/欧洲/中国先进，中东/非洲滞后）可能形成替代速度分化 → [gtp-u-limitations-6g-alternatives](../../wiki/topics/gtp-u-limitations-6g-alternatives.md)
- **过渡期双栈成本**：即便 6G 采用 SRv6 MUP，与 4G/5G 互操作的过渡期（预计 10+ 年）仍需 GTP-U 双栈运行，增加运营复杂度

## 信号事件

- 2024-Q2：SoftBank 全球首个 SRv6 MUP 商用部署（SoftBank）
- 2024-Q3：IETF 123 DT 提交 MUP 移动性管理提案（IETF draft）
- 2024-Q4：EURECOM 发布 IUP 概念验证，消除 N3 接口（EURECOM）
- 2025-Q1：NVIDIA dUPF 100Gbps / 25μs 基准发布（NVIDIA GTC）
- 2025-Q2：Samsung M-UP 方案更新（Samsung Research）

## 未来 12-24 月可观察的指标

- [ ] 3GPP CT 是否启动 GTP-U 替代/演进的正式 Study Item
- [ ] SoftBank SRv6 MUP 的商用规模扩展（用户数/流量占比）
- [ ] 是否有第二家运营商部署 SRv6 MUP
- [ ] IETF MUP WG 的 RFC 发布进度
- [ ] 6G 架构讨论中 GTP-U 替代方案的提案数量趋势
- [ ] 双栈过渡方案的设计进展

## 何时该被推翻

- 若 3GPP Rel-21/22 明确决定延续 GTP-U 作为 6G 用户面隧道协议 → **推翻**
- 若 SoftBank MUP 商用后报告严重性能/兼容性问题 → **弱化**
- 若 2027 年底无第二家运营商跟进 SRv6 MUP 部署 → **弱化**
- 若 GTP-U 出现 v3 增强版本解决核心痛点（状态爆炸、传输感知） → **推翻**
