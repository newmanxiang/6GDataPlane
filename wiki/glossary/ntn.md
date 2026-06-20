---
term: Non-Terrestrial Network
abbr: NTN
cn: 非地面网络
slug: non-terrestrial-network
category: glossary
related:
  - 6g-data-plane
  - user-plane-evolution
  - ran-architecture-evolution
source: https://www.3gpp.org/technologies/ntn-overview
---

# NTN — Non-Terrestrial Network

> 利用卫星、无人机等非地面平台承载蜂窝通信，实现全球无缝覆盖。

**中文**：非地面网络
**英文**：Non-Terrestrial Network
**缩写**：NTN

## 定义
非地面网络是指利用无人机系统（UAS，运行高度 8-50 km）或卫星系统（LEO/MEO/GEO）作为通信节点的网络或网络片段。3GPP 自 Release 17 起支持 NTN，通过对 NR 协议栈的适配（HARQ、定时提前、RLC 调整）实现地面与非地面网络的互操作。NTN 引入的长时延（LEO 约 20-40 ms 单程）和高抖动特性，要求数据面支持自适应协议选择和容延迟传输。

## 相关概念
- [[6g-data-plane]] — NTN 长时延特性要求数据面协议栈适配
- [[user-plane-evolution]] — NTN 是用户面演进的重要驱动力
- [[ran-architecture-evolution]] — NTN 节点影响 CU/DU 功能分割方案
