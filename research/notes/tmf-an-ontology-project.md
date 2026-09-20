# 笔记：tmf-an-ontology-project

## 调研窗口
2026-09-20 → 2026-09-20

## 调研范围判定

用户指令「tmf an-ontology-project」在公开互联网上**没有**名为 `an-ontology-project` 的 TM Forum 官方 GitHub 仓。最接近的三条线：

1. **TM Forum Autonomous Networks Project 的官方本体族**：TIO（TR292）+ Intent Common Model（TR290）+ TMF921，Turtle 仍在成员 Confluence。
2. **OpenAN 规划中的第三奠基项目 AN Ontology**（LFN Candidate，对齐 TMF AN）：Phase 1 只开源了 A2A-T，**ontology 仓截至 2026-09-20 仍未出现**。
3. **可下载的 OWL 实现**：亚信 `asiainfo/AN-Ontology`（明确写参与 TMF AN）、Catalyst C26.0.910 承诺的 `sid-ontology`/`c-kg`（未公开）、Orange NORIA-O（已对齐 SID/TMF638）。

本子题按「TMF 自智网络本体工程」处理：官方词汇 + 开源实现竞赛 + 与数据编织/6G 数据面的接口。

---

## 已精读源

### [TR292 TM Forum Intent Ontology (TIO) v3.6.0]（标准，2024-08-30）
URL: https://www.tmforum.org/resources/introductory-guide/tr292-tm-forum-intent-ontology-tio-v3-6-0/
归档: research/raw/2026-09-20-tmf-tio-tr292/

#### 关键数据点
- Created By: Autonomous Networks Project；GA / Production
- 模块化：TR292 主干 + A/C/D/E/F/G/R（3.6.0 公开）+ B/H（3.7.0 会员，2025-11）+ I Security Ontology 4.0.0（2026-03-27 会员）
- TR290 Intent Common Model 已到 3.8.0（2026-03-27）
- TR294A/B 把 TIO 接到 3GPP TS 28.312 / 28.541

#### 关键论断
- TIO 是意图管理的**基础词汇**，供 Intent Common Model 与 extension models 使用，不是 SID 的 OWL 化。
- 意图控制环 = Intent Management Function 实例之间的交互。

#### 待追查
- Turtle 文件仍不解析 IRI；无会员账号无法做 triple 级审计。

---

### [TMF921 Intent + TMF921B Conformance v5.0]（标准，API）
URL: https://github.com/tmforum-apis/TMF921_Intent
归档: research/raw/2026-09-20-tmf-tio-tr292/

#### 关键数据点
- Intent.expression 必须用 TIO 校验；JSON-LD 强制，Turtle/XML/YAML-LD 可选序列化。
- GitHub mirror 2025-10-03 才出现，stars=0。

#### 关键论断
- 运行时意图是「API 信封（TMF921）+ RDF 正文（TIO）」。没有 TIO，TMF921 只是空壳。

---

### [Access to TIO models | TM Forum Community]（社区，~2024–2025）
URL: https://engage.tmforum.org/discussion/access-to-tio-models
归档: research/raw/2026-09-20-tmf-tio-tr292/

#### 关键数据点
- 旧 ns：`http://tio.models.tmforum.org/tio/v3.6.0/`
- 已同意 ns：`https://models.tmforum.org/tio/`
- TTL 托管：ANP Confluence「Turtle Files Collection TIO v3.6.0」
- TIO 4 计划把 turtle 附进规范

#### 与其他来源的矛盾
- 「Available to all」的 PDF 与「机器可读本体公开」不是一回事——ETSI OOP SDK 只能 hardcode 旧 prefix。

---

### [LFN OpenAN 公告]（开源治理，2026-06-25）
URL: https://lfnetworking.org/lf-networking-brings-a2a-t-to-live-network-through-openan-for-agent-driven-autonomous-networks/
归档: research/raw/2026-09-20-openan-an-ontology/

#### 关键数据点
- 三类组件：A2A-T common、Agent Framework、**AN ontology**
- Phase 1 只推 A2A-T
- 创始/支持含 **ZTE**
- Apache 2.0；商用验证目标 2027

#### 关键论断
- OpenAN 明确把 AN Ontology 列为与协议、Agent Framework 并列的奠基项目，但代码捐赠清单里没有它。

---

### [openan.dev + github.com/project-openan]（开源，2026-09-20 核实）
URL: https://openan.dev/ ; https://github.com/project-openan

#### 关键数据点
- 公开仓：a2a-t-sdk-{python,java}、registry-center、orchestration-center、docs、portal、workflow-engine-sdk-* 等
- **无 ontology 仓**（检索 name 含 ontology/sid/kg 为零）

#### 待追查
- 2026-12 IHPP 是否会放出 ontology 种子。

---

### [Agent Fabric / Catalyst C26.0.910]（Catalyst，DTW 2026）
URL: https://agent-fabric.github.io/ ; https://www.tmforum.org/catalysts/projects/C26.0.910
归档: research/raw/2026-09-20-agent-fabric-sid-kg/

#### 关键数据点
- `sid-ontology`：MODA 25.5 → OWL，SPARQL+MCP，Huawei
- `c-kg`：AN 用例 KG + 解耦 OWL，MCP，Vodafone+Huawei
- 声称 DTW 2026 前后公开；2026-09-20 仍未在 project-openan 出现
- 18 CSP + 7 vendors；ZTE 不在该 Catalyst vendor 表

#### 关键论断
- 产业正在把 SID 从 UML 信息框架改写成 Agent 可查询的 OWL KG，但这是 Catalyst/厂商实现，不是 TMF 官方 SID 发布格式。

---

### [asiainfo/AN-Ontology]（厂商开源，2025-09-11 创建，2025-10-24 最近推送）
URL: https://github.com/asiainfo/AN-Ontology
归档: research/raw/2026-09-20-asiainfo-an-ontology/

#### 关键数据点
- 13 stars / 2 forks / CC BY 4.0
- 三模块合计 89 class / 121 object prop / 92 data prop
- 自述参与 TMF AN；TTL 无 SID/TIO 映射
- AsiaInfo 同时是 OpenAN 支持方、ETSI ZSM-029 支持方（既有 topic 卡）
- 姊妹项目 ODLM-Ontology（数据湖本体，43 stars，2025-12 仍在推）

#### 关键论断
- 这是目前**唯一以 AN-Ontology 为名、可克隆的 OWL 工程**，但是厂商场景本体，不是 TMF 官方交付件。
- 工程质量：接口枚举拼写错误、README 复制粘贴、ns 分裂、文档类未进 TTL、无 SHACL、无 examples。适合当「国内厂商怎么做 AN 本体」的样本，不适合当行业权威 schema。

#### 与其他来源的矛盾
- README checkbox 仍显示核心网/资源本体未发布，仓库已有 5GC 与 Resource Manage。
- 根 LICENSE CC BY 4.0 vs 模块 README Apache 2.0。

---

### [Orange NORIA-O]（学术/开源，ESWC 2024）
URL: https://github.com/Orange-OpenSource/noria-ontology
归档: research/raw/2026-09-20-noria-o-sid-align/

#### 关键数据点
- 用 `equivalent` 注释对齐 SID Domain/ABE 与 TMF638 Service
- 有 w3id 稳定 IRI、CQ、authoring tests

#### 关键论断
- 欧洲路线是「复用上层本体 + 逐类对齐 TMF」，与亚信「从运维场景重建模、口头对接 TMF」形成对照。

---

### [IG1251 / IG1251C / IG1421 / Huawei Agents of ADN]（架构语境）
- IG1251：K 参考点 = 自治域 ↔ knowledge and intelligence platform
- IG1251C v1.1.0（2025-07）：L4 目标架构，agent 跨 Business/Service/Resource
- IG1421 v1.0.0（2025-05）：AI Agent MAS 意图本体，Alpha
- Huawei ADN 白皮书：知识与记忆模块（域知识建模/检索/更新 + 短长期记忆）；中国移动+华为故障 Agent 报告后台排障工作量 -80%、MTTR -27%

---

## 综合判断（写入 wiki/topics 前的草稿）

1. **不要把「TMF AN ontology project」误认成单一仓库。** 官方产物是 TIO（意图词汇，RDF，GA 但机器文件分发差）；SID 仍是 UML；AN 域本体被 OpenAN 列为第三奠基项目但尚未开源。
2. **语义栈应分三层**：TIO（意图/期望/约束）≠ SID（BSS/OSS 信息框架）≠ 域运维本体（5GC/家客/工单/故障）。Agent 要同时吃这三层。数据编织缺的「电信语义层」主要卡在后两层的 OWL 化与映射。
3. **2026 年竞赛窗口**：谁先把 SID→OWL + AN 用例 KG + MCP 做成可复用开源，谁就占据 Agent 互操作的语义入口。Huawei/Vodafone Catalyst 与 AsiaInfo AN-Ontology 走的是不同切面（前者 SID 全局，后者场景模块）。
4. **我司位置**：OpenAN 创始成员之一，Fault Agent 已有生产 KG，但 C26.0.910 vendor 表无 ZTE，OpenAN Phase 1 捐赠名单无 ZTE 代码。若不在 AN Ontology 工作流里交 OWL/映射，语义层会被华为/亚信定义。

信心：中。TIO TTL 未拿到；sid-ontology/c-kg 未公开；亚信本体未做推理/SHACL 验证。

## 二轮深挖追查清单
- [ ] 会员账号下载 TR292 TTL 与 TR292I Security Ontology 4.0.0
- [ ] 2026-12 IHPP / OpenAN 是否出现 ontology 仓
- [ ] sid-ontology 是否真从 MODA 25.5 XMI 自动生成（对照 tmforum-rand/MODA）
- [ ] 亚信是否把 AN-Ontology 贡献进 OpenAN 还是保持私有品牌
- [ ] Fault Agent / AIR Net 数据引擎 schema 与 TIO/SID 的可映射点（需内部资料）
- [ ] 3GPP TS 28.312 Intent NRM 与 TIO 的 TR294A 映射细节
