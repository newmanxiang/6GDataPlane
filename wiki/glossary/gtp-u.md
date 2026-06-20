---
term: GPRS Tunnelling Protocol - User Plane
abbr: GTP-U
cn: GPRS 隧道协议-用户面
slug: gtp-u
category: glossary
related:
  - user-plane-evolution
  - upf
source: https://www.3gpp.org/specifications/specifications-groups/ran-specifications/ran3-related/gtp-u
---

# GTP-U — GPRS Tunnelling Protocol - User Plane

> 3GPP 定义的用户面隧道协议，用于在移动网络节点间封装和转发用户数据包，从 3G 沿用至 5G。

**中文**：GPRS 隧道协议-用户面  
**英文**：GPRS Tunnelling Protocol - User Plane  
**缩写**：GTP-U

## 定义

GTP-U（3GPP TS 29.281）是移动核心网中用户面数据传输的隧道协议，通过 TEID（Tunnel Endpoint Identifier）在网络节点间建立隧道。该协议从 3G（UTRAN）开始使用，经 4G（EPC 中 S-GW/P-GW 间）延续至 5G（UPF 间），具有成熟稳定的优势，但在 6G 研究中被指出存在隧道开销大、灵活性不足、难以支持可编程转发等局限。

## 相关概念

- [[user-plane-evolution]] — GTP-U 是用户面演进中 4G/5G 阶段的核心承载协议
- [[upf]] — 5G UPF 网元内部使用 GTP-U 进行数据隧道封装
