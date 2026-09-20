# 3GPP SA5 6G OAM 研究：32.801-01 / FS_6G_OAM

- Portal 规范：https://portal.3gpp.org/desktopmodules/Specifications/SpecificationDetails.aspx?specificationId=5491
- WI：https://portal.3gpp.org/desktopmodules/WorkItem/WorkItemDetails.aspx?workitemId=1100014
- DynaReport：https://www.3gpp.org/DynaReport/32801-01.htm
- 目录镜像：https://itecspec.com/3gpp/32.801-01
- 抓取日期：2026-09-20
- 核实状态：confirmed（Portal 元数据 + 公开目录；正文草稿会员）

## 编号真伪（V8）

| 字段 | Portal 原文 |
|---|---|
| Reference | **32.801-01** |
| Title | Study on 6G Management and Orchestration |
| Type | **Technical report (TR)** |
| Status | Draft |
| Release | Rel-20 |
| 创建 | 2026-01-12 Dongwook Kim |
| 主责 | SA 5 |
| Rapporteur | **Pengxiang Xie, ZTE Corporation** |
| 关联 WI | UID 1100014 FS_6G_OAM |

WI FS_6G_OAM：Feature 级，PCG approved，Rel-20，Start 2025-12-03，End 2027-06-06，**WI Rapporteur Bahar Sadeghi (AT&T)**，Latest WID SP-251653。备注 2026-06-04：进度 5%→20%；**32.801-01 added**。DynaReport 另见：旧「32.801 Performance management」已 WITHDRAWN；**32.801-02 = Study on Charging Aspects of 6G System**，勿与 32.801-01 混用。

**结论：仓库既有卡片写 "TS 32.801" 不准确。官方类型是 TR，编号是 32.801-01。文档 rapporteur = 中兴；WI rapporteur = AT&T。iTecSpec 页面标题误用 "TS 32.801-01"。本调研统一称 TR 32.801-01。**

## 公开目录中的知识/数据相关章节（iTecSpec TOC）

- 6.1.6 Data Management Framework (DMFW)
- 6.1.9 Intent Driven Management
- 7.1 DMFW / 7.1.1 KI#1 DMFW Capabilities
- **7.2 Data and Knowledge Management**
  - **7.2.1 KI#1 Knowledge/semantic representation and management**
  - 7.2.2 KI#2 Data management – Concepts and terminology
- 7.3 Management Agent

正文解决方案条款未见公开全文。

## Rel-20 工作区讨论稿（公开 PDF）

来源：https://www.3gpp.org/ftp/Email_Discussions/SA5/SA5-level%20discussions/SA5%23161/SA5_NWM_Discussion_for_Rel-20_6G_OAM_Work_Areas-v0.0.7.pdf

### 2.2.9 Data Management

- WT-1 新数据/分析需求（AI/ML、Sensing、6G IoT）
- WT-2 统一数据管理机制（PM/CM/trace/alarms/UE data）：收集控制与上报、处理、分析、注册、发现、访问控制、发布、分发、暴露、编目、销毁、质量报告、变更管理
- WT-3 数据质量与审慎
- WT-4 非 3GPP 数据（如 O-RAN）
- WT-5 用户同意机制复用

### 2.2.4 Semantic Network Management

Study semantic network management for 6G network and service management including:

- WT-1 Study definitions of terminologies related to semantic and knowledge.
- WT-2 Study use cases and potential requirements supporting semantic and knowledge in 3GPP management system.
- WT-3 Study potential impact in management architecture for 6G, and the relationship with other management features including data management.
- **WT-4 Survey existing related frameworks (e.g. RDF) and solutions (e.g. knowledge graphs, ontologies) defined in other fora (e.g. TM Forum), and study how/if they can be leveraged to support the identified use cases and requirements.**
- WT-5 Study trade-offs or advantages/disadvantages of managing the knowledge and obtaining semantics for network management.

公司反馈（摘录）：

- **ZTE**：Q1 Yes, we support this work area. Q2: WT 1/2/4 are ok。对 WT-3「enhancing the management architecture」要求再讨论。
- **Ericsson LM**：建议工作区改名为 Knowledge Management；将 TMF/RDF/本体 survey 保留为独立 WT-x。
- Nokia Germany：认为 knowledge 属于 data management，应并入数据管理讨论。

## SA5 Inbox 草稿文件名（2026-05，仅标题级）

- KSM1 Knowledge management
- KSM2 Knowledge-based network management scenarios
- KSM3 Knowledge architecture（pCR TR32.801）
- DMFW-1 Use case potential requirements and solution
- DMFW-2 Key issues

证明 SA5 已把 **Knowledge architecture / semantic representation** 写入 6G OAM 研究结构，但 **尚未发布 3GPP 本体规范**。
