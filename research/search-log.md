# Search Log

> 可复现性保障。每次有意义的搜索追加一行。
> 由 6g-deep-dive、6g-source-radar、6g-onboarding 共同维护。

## 格式

```markdown
| 日期 | 工具 | Query | 过滤/参数 | 结果数 | 子题 | 备注 |
|---|---|---|---|---|---|---|
```

## 记录

| 日期 | 工具 | Query | 过滤/参数 | 结果数 | 子题 | 备注 |
|---|---|---|---|---|---|---|
| 2026-06-21 | exa | 6G data plane architecture design proposals 2024 2025 comprehensive survey | numResults:15 | 15 | 6g-data-plane-architecture-2025 | 获取 MDPI 综述、SNS JU 白皮书、FITEE 论文等 |
| 2026-06-21 | exa | Huawei DaaS data as a service 6G data plane design AI native | numResults:15 | 15 | 6g-data-plane-architecture-2025 | 获取华为 DaaS 白皮书、GTI 白皮书、NET4AI 等 |
| 2026-06-21 | exa | Hexa-X-II 6G architecture four planes data plane intelligence plane XaaS | numResults:15 | 15 | 6g-data-plane-architecture-2025 | 获取 Hexa-X-II D3.5、EuCNC 演示、SNS JU 白皮书等 |
| 2026-06-21 | exa | Qualcomm 6G user plane first design rethinking control plane | numResults:15 | 15 | 6g-data-plane-architecture-2025 | 获取 6G Foundry 系列全部文章、经济分析等 |
| 2026-06-21 | exa | 3GPP SA2 6G data framework work task study item WT#5 | numResults:15 | 12 | 6g-data-plane-architecture-2025 | 获取 SA2 FTP 目录、Ericsson 博客、ATIS Webinar 等 |
| 2026-06-21 | fc-search | 6G data plane architecture comparison Huawei DaaS Hexa-X Qualcomm | limit:10 | 10 | 6g-data-plane-architecture-2025 | 补充 3GPP 讨论文稿链接、arXiv 综述 |
| 2026-06-21 | exa | China Mobile 6G network architecture three layers six planes data plane | numResults:15 | 15 | 6g-data-plane-architecture-2025 | 获取中国移动"三体四层五面"全套来源 |
| 2026-06-21 | exa | NGMN 6G network architecture evolution 2025 consensus standardization | numResults:15 | 15 | 6g-data-plane-architecture-2025 | 获取 NGMN 全部 6G 架构相关出版物 |
| 2026-06-21 | exa | GTP-U limitations 6G user plane protocol overhead scalability | numResults:15 | 15 | gtp-u-limitations-6g-alternatives | 获取 6G-RUPA、IUP、UPF 性能分析、IETF 分析草案 |
| 2026-06-21 | exa | SRv6 segment routing IPv6 mobile network 6G user plane replacement | numResults:15 | 15 | gtp-u-limitations-6g-alternatives | 获取 RFC 9433、CNSM 2019、SRv6ops slides、VPP 文档 |
| 2026-06-21 | exa | IETF MUP mobile user plane draft architecture 6G GTP-U replacement | numResults:15 | 15 | gtp-u-limitations-6g-alternatives | 获取 MUP arch draft、MUP evolution、BGP-MUP SAFI |
| 2026-06-21 | exa | 6G user plane protocol evolution beyond GTP-U 2024 2025 | numResults:15 | 15 | gtp-u-limitations-6g-alternatives | 获取 QUICUP、ANUP signaling、MUP IETF 124 slides |
| 2026-06-21 | exa | P4 programmable data plane 6G mobile network UPF hardware acceleration | numResults:10 | 10 | gtp-u-limitations-6g-alternatives | 获取 HiP4-UPF、AccelUPF、SD-Fabric P4-UPF |
| 2026-06-21 | fc-search | Deutsche Telekom SRv6 replacement GTP-U 6G 3GPP study 2025 | limit:5 | 5 | gtp-u-limitations-6g-alternatives | 获取 DT IETF 123 提案、Heavy Reading 报告链接 |
| 2026-06-21 | fc-search | GTP-U encapsulation overhead bytes comparison SRv6 performance | limit:5 | 5 | gtp-u-limitations-6g-alternatives | 获取 CNSM 2019 PDF、VPP 延迟特性、IMDEA 实验 |
| 2026-06-21 | exa | SRv6 mobile user plane SoftBank Cisco pilot deployment | numResults:10 | 10 | gtp-u-limitations-6g-alternatives | 获取 SoftBank 全系列部署新闻（2019-2025） |

## 工具简写

| 缩写 | 工具 |
|---|---|
| `exa` | `web_search_exa` |
| `exa-adv` | `web_search_advanced_exa`（带日期过滤） |
| `exa-crawl` | `crawling_exa` |
| `exa-code` | `get_code_context_exa` |
| `fc-search` | `firecrawl_search` |
| `fc-scrape` | `firecrawl_scrape` |
| `fc-map` | `firecrawl_map`（站点 URL 发现） |
| `fc-crawl` | `firecrawl_crawl`（多页爬取） |
| `fc-extract` | `firecrawl_extract`（LLM 结构化提取） |
| `fc-research` | `firecrawl_deep_research`（AI 深研） |
| `browser` | cursor-ide-browser |
