# 调研笔记：gtp-u-limitations-6g-alternatives

> 调研日期：2026-06-21
> 搜索引擎：Exa + Firecrawl
> 状态：完成

## 搜索记录

| # | Query | 引擎 | 结果数 | 有效 |
|---|-------|------|-------|------|
| 1 | GTP-U limitations 6G user plane protocol overhead scalability | Exa | 15 | 12 |
| 2 | SRv6 segment routing IPv6 mobile network 6G user plane replacement | Exa | 15 | 11 |
| 3 | IETF MUP mobile user plane draft architecture 6G GTP-U replacement | Exa | 15 | 13 |
| 4 | 6G user plane protocol evolution beyond GTP-U 2024 2025 | Exa | 15 | 10 |
| 5 | P4 programmable data plane 6G mobile network UPF hardware acceleration | Exa | 10 | 8 |
| 6 | Deutsche Telekom SRv6 replacement GTP-U 6G 3GPP study 2025 | Firecrawl | 5 | 4 |
| 7 | GTP-U encapsulation overhead bytes comparison SRv6 performance | Firecrawl | 5 | 5 |
| 8 | SRv6 mobile user plane SoftBank Cisco pilot deployment | Exa | 10 | 8 |

总候选 URL：~90 | 去重后：~55 | 精读：14

## 精读来源

### [RFC 9433: SRv6 for Mobile User Plane]（标准，2024-07）
URL: https://datatracker.ietf.org/doc/rfc9433/

#### 关键数据点
- 定义 Traditional / Enhanced / Interworking 三种部署模式
- SRGW 无状态，可扩展至百万 UE
- 定义 6 个 SRv6 endpoint behaviors（End.M.GTP4.E, End.M.GTP6.E, End.M.GTP6.D 等）

#### 关键论断
- "The statelessness of SRv6 and its ability to control both service layer path and underlying transport can be beneficial to the mobile user plane"
- 传统模式下 GTP-U 被 SRv6 一对一替换

### [draft-ietf-dmm-srv6mob-arch-03]（IETF WG draft，2025）
URL: https://datatracker.ietf.org/doc/html/draft-ietf-dmm-srv6mob-arch-03

#### 关键数据点
- 会话范式 O(N²) vs 路由范式 O(N) 的扩展性论证
- GTP-U 隧道叠加无底层网络感知 → 无法满足 URLLC SLA
- SRv6 uSID (RFC 9800) 压缩封装开销

#### 关键论断
- "Mobile session information is a function of M,N... whereas routing information is a function of N"
- "These issues can be solved more simply without GTP-U tunnel"
- TI-LFA 提供 <50ms 的拓扑无关快速保护

### [draft-ietf-dmm-5g-uplane-analysis-04]（IETF WG draft）
URL: https://datatracker.ietf.org/doc/html/draft-ietf-dmm-5g-uplane-analysis

#### 关键数据点
- GTP-U-5: IPv6 传输下 UDP 零校验和不可用（历史原因）
- GTP-U-6: 不支持 ICMP PTB 响应 → Path MTU Discovery 黑洞
- 3GPP RAN 和 CT4 选择 GTP-U 作为 5G UP 时"似乎只有这一个选项被选择"

### [SoftBank 商用部署]（运营商，2025-12）
URL: https://www.softbank.jp/en/corp/news/press/sbkk/2025/20251218_01/

#### 关键数据点
- 全球首个 SRv6 MUP 5G 商用部署（FWA 场景）
- 硬件：Broadcom Jericho2 + Arrcus ArcOS + VMware Telco Cloud
- 开发时间线：2019 SRv6 部署 → 2022 MUP 开发 → 2023.02 现场试验 → 2025.12 商用

### [SoftBank 4G 扩展试验]（运营商，2025-06）
URL: https://www.softbank.jp/en/corp/news/press/sbkk/2025/20250610_01/

#### 关键数据点
- 130km 新东名高速公路行驶测试（沼津-浜松）
- SRv6 MUP 启用后延迟改善 >10ms
- AI 行车记录仪视频流到 MEC 服务器的连续稳定通信

### [CNSM 2019 性能评估]（学术/会议，2019）
URL: https://dl.ifip.org/db/conf/cnsm/cnsm2019/1570585037.pdf

#### 关键数据点
- 使用 Intel Tofino P4 硬件的首次 GTP-U vs SRv6 定量测评
- SRv6 encap 延迟略高于 GTP-U encap（单次操作）
- 短包和长包场景下差异显著不同
- 无状态转换方案的可行性得到硬件验证

#### 与其他来源的矛盾
- 与 IETF slides 声称"SRv6 MTU 开销低于 GTP-U"存在细微差异：取决于 SID 数量

### [Deutsche Telekom IETF 123 提案]（运营商/标准，2025-07）
URL: https://mailarchive.ietf.org/arch/msg/dmm/hpnso-jy0p1Nll3uJQSH-o60Plw/

#### 关键数据点
- DT 正式提议在 3GPP 6G 研究阶段发起"SRv6 替换 GTP-U"课题
- 在 srv6ops session 展示动机幻灯片
- 正在寻找 3GPP 支持者扩大联盟

### [6G-RUPA 论文]（学术，2024）
URL: https://www.mdpi.com/2073-431X/13/8/186 (UPC Barcelona)

#### 关键论断
- "GTP-U 自 3G 以来基本未变"
- GTP-U 的虚电路交换方式导致 UPF 中存储大量状态
- 6G-RUPA 引入灵活层数 + 多层 QoS + 用户面层可编程性

### [IUP: Integrated User Plane]（学术，2025-03）
URL: https://arxiv.org/html/2503.09430v1 (EURECOM)

#### 关键数据点
- 消除 N3 接口和 GTP-U 处理
- 避免 MTU 不匹配导致的 IP 分片
- 引入 IDFC 子层替代 SDAP
- 延迟降低来源：(1) 减少回传传输延迟，(2) 绕过 N3 处理

### [HiP4-UPF]（学术，2024）
URL: https://par.nsf.gov/servlets/purl/10609313

#### 关键数据点
- P4 可编程交换机支持 2× UE 数量 vs 基线
- 比 SD-Fabric 多 1.9× UE 支持
- 三种 5G 呼叫流吞吐提升 9–619%
- 0.4 Mpps/USD 或 8.52 Mpps/Watt 的成本效率

### [draft-zzhang-dmm-mup-evolution-09]（IETF individual，2024-07）
URL: https://datatracker.ietf.org/doc/html/draft-zzhang-dmm-mup-evolution-09

#### 关键论断
- 6G 中提议将 AN (CU) 与 UPF 集成为 ANUP
- "AN-UPF connection and GTP-U encapsulation/decapsulation are not needed anymore"
- 性能显著提升，尤其当 AN/UPF 运行在服务器上时
- 任何隧道（MPLS/SRv6）都可用于 DN VPN，无需 UDP/GTP 开销

## 新发现的术语 / 人名 / 公司

- **ANUP**: Access Node User Plane — AN 和 UPF 的集成网络功能（6G 提案）
- **MUP Segment**: MUP 架构中的移动用户面抽象
- **ISD Route**: Interwork Segment Discovery Route（BGP-MUP）
- **ST Route**: Session Transformed Route（BGP-MUP）
- **IDFC**: Integrated Data Flow Control（IUP 中替代 SDAP 的子层）
- **6G-RUPA**: 6G Resilient User Plane Architecture
- **QUICUP**: QUIC-based User Plane tunneling
- **Markus Amend**: Deutsche Telekom，推动 3GPP SRv6 研究
- **Clarence Filsfils**: Cisco Fellow，SRv6 架构创始人
- **松嶋聡 (Satoru Matsushima)**: SoftBank，MUP 架构主要作者

## 关键矛盾

1. SRv6 封装开销 vs GTP-U：典型场景 uSID 后 SRv6 ≤ GTP-U，但多 SID TE 场景可能反超
2. SRv6 在 IETF 标准化完成 vs 3GPP 未采纳：标准轨道完整但 3GPP 采用仍是未知数

## 待追查

- [ ] Deutsche Telekom IETF 123 幻灯片具体内容（3 页动机）
- [ ] 3GPP CT/SA 对 SRv6 替代 GTP-U 的历史讨论记录
- [ ] SoftBank 商用部署后的大规模性能报告
- [ ] Linux kernel SRv6 MUP patch set 合入状态
