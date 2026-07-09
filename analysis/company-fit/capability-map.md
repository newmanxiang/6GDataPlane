# Capability Map：中兴通讯（ZTE）在 6G 数据面 × 数据编织能力域的定位

> 生成日期：2026-07-05 | 输入：`ops/company-context.md`（ZTE 背景）+ `analysis/matrices/*` + `wiki/topics/*`
> 方法：以 M3 核心交集矩阵（6 项数据编织能力 × 4 个 6G 场景）+ M1 厂商矩阵为坐标系，标注中兴当前位置与差距。
> 信心标签：[高]=多源公开证据；[中]=部分证据+合理推断；[低]=推断为主待验证。

---

## 1. 一句话定位

中兴在**"网络智能/自智网络（AN）"与"AI-RAN 算力"两侧强**，在**"6G 数据面/数据服务化（DaaS 类）标准话语权"上落后华为**，在**"数据编织六大能力的电信化"整体处于早期**——其真实优势是**"AI 原生网络 + 承载/算力"**，数据编织是需要补齐的能力面。[中]

> **本报告视角（已确认）**：出发点是**数据中台团队 / 战略专家组**（年投入千万级、仅有建议权）。因此本图的落点不是"中兴公司整体如何做 6G 数据面"，而是"**数据中台如何借 6G 数据面机会深度嵌入 6G 业务**"。公司级优势（AI-RAN/承载/算力）在这里是**数据中台可借力的杠杆与可建议纳入路标的方向**，而非数据中台自担的战场。
>
> **架构锚点（关键）**：中兴自智网络（AIR Net）的**数智引擎 = 数据引擎 + 智能引擎（AI 大模型）+ 孪生引擎**三大组件（《自智网络白皮书 2025》）。**数据中台正是其中的"数据引擎"**。这给了数据中台一个明确的存量位置和演进路径：
> **数据引擎（自智网络内）→ 6G 数据面数据服务化组件（跨域/RAN/终端）**。
> 本报告所有机会/行动都应理解为"把数据引擎的能力沿 6G 数据面向外延伸"，而非另起炉灶。

---

## 2. 中兴 × 数据编织六大能力（对照 M1 厂商矩阵）

> 基线：M1 矩阵中中兴仅在"数据编排"🔬 与"AI 原生数据管理"🔬 有记录，其余为空（[vendor-capability](../matrices/vendor-capability.md) 第 18 行）。以下结合新调研细化。

| 数据编织能力 | 中兴当前位置 | 证据 | 信心 | 与领先者差距 |
|:--|:--|:--|:--:|:--|
| **主动元数据** | 🟡 弱：网络运维元数据管理有实践，无产品级主动元数据引擎 | uSmartNet 数据治理；对比 IBM Watson Knowledge Catalog ✅ | 中 | 大（IT 供应商产品级领先） |
| **知识图谱** | 🟢→🟡 相对亮点：AIR Net Fault Agent 已用**知识图谱+大模型**做跨域故障诊断 | [TMForum ZTE AN][^tm]；M3 边缘 KG 🟢 | 高 | 中（应用级已落地，语义层未标准化） |
| **数据虚拟化** | 🔴 空白：无公开数据虚拟化层产品 | 对比 Denodo/华为 DCP；M3 核心网 DCP 🟢 | 中 | 大 |
| **数据编排** | 🔬 研究/方案：uSmartNet 跨域协同 + SA2 WT#5 数据框架提案 | [vendor 脚注 7][^v7]；[3gpp-sa2-wt5][^sa2] | 中 | 中（华为 DO 体系更完整） |
| **联邦学习/隐私** | 🟡 探索：NWDAF 结合 FL 有探索，合规实践跟随国内法规 | 3GPP Rel-18/19 FL；M3 核心网 FL 🟢 | 中 | 中 |
| **语义互操作** | 🔴→🟡 早期：AN 跨域场景涉及语义，无统一 6G 数据语义模型贡献 | M3 语义互操作全域 🟡/🔴 | 低 | 大（全行业空白，机会大） |

**读法**：中兴唯一的**结构性亮点是"知识图谱驱动的 AN Fault Agent"**——这是把数据编织能力（KG+语义）真正落到电信生产场景的少数实例之一，可作为向 6G 数据面延伸的支点。

---

## 3. 中兴 × 6G 数据面（对照 wiki/topics）

| 6G 数据面议题 | 中兴位置 | 证据 | 信心 |
|:--|:--|:--|:--:|
| 6G 数据面架构（DaaS 独立面 vs 增强用户面） | **跟随中国阵营**（华为/中移/vivo）倾向独立/增强数据能力，但自身无 DaaS 级完整架构公开 | [6g-data-plane-architecture-2025][^arch]；预判 §9 中欧美路线分歧 | 中 |
| UPF→6G 用户面演进 | 有核心网（Common Core）+ 承载（SPN）全栈，具备演进载体 | [user-plane-evolution][^upf] | 中 |
| AI 原生数据面 | **强**：AIR/AIREngine 站点算力 + Native AI 6G 战略 | [ai-native-data-plane-status][^ain]；[RCR ZTE 6G][^rcr] | 高 |
| GTP-U 替代（SRv6/MUP） | 承载/SPN 领先，SRv6 有基础；与中移 800G MTN 首个 6G 传输标准 | [gtp-u-limitations][^gtpu]；[ZTE SPN][^spn] | 中 |
| NWDAF/网络智能 | Common Core 内含 NWDAF，"全栈 AI+ 核心网" | [3gpp-rel-19-20][^rel] | 高 |

---

## 4. 中兴 × 6G 四场景（叠加 M3 热力图）

> M3 结论：终端/NTN 全面空白（4/6 🔴）、边缘成熟度最高、RAN 有性能鸿沟、核心网等标准。中兴在各场景的相对位势：

```
              核心网      RAN         边缘        终端/NTN
数据编织综合   🟡 中       🟢 强(AN)   🟡 中       🔴 无
中兴相对优势   NWDAF/     AIR/        MEC/        (消费者终端
              Common     GigaMIMO    星云智算     业务可切入)
              Core       /AIREngine
```

- **RAN 是中兴主场**：AIR MAX + AIREngine + GigaMIMO 使其在"RAN 域数据/算力"上强于多数设备商——而 M3 显示 RAN 域数据编织正是"性能鸿沟 + 研究空白"区，**优势与空白重叠 = 差异化机会**。[高]
- **核心网靠标准**：位置取决于 SA2 WT#5 结论，中兴需在提案端加码。[中]
- **终端/NTN**：中兴有消费者终端业务，是**唯一能同时触达"网—端"的中国设备商之一**，可切入 M3 全面空白的"终端侧轻量数据编织"。[中]

---

## 5. 综合能力雷达（自评，0-5）

| 维度 | 中兴自评 | 行业领先 | 缺口 |
|:--|:--:|:--:|:--:|
| AI 原生网络 / AI-RAN | 4 | 4（华为/NVIDIA） | 小 |
| 承载/传输（6G Transport） | 4 | 4（自身领先） | 小 |
| 自智网络 AN（KG+大模型） | 4 | 4（华为/中兴并列） | 小 |
| 核心网数据智能（NWDAF） | 3 | 4（爱立信/华为） | 中 |
| 6G 数据面架构话语权（DaaS） | 2 | 4（华为） | 大 |
| 数据编织六大能力（IT 级） | 1.5 | 5（IBM/Informatica） | 大 |
| 跨域数据治理标准 | 3 | 3（中兴/中电信 ZSM 029 有位） | 中 |
| 终端侧数据能力 | 1 | 1（全行业空白） | — 机会区 |

---

## 6. 关键结论（给 §8 / opportunities 的锚点）

1. **数据中台的既定位置 = 自智网络"数据引擎"**（数智引擎三组件之一）。最优路径是**沿"数据引擎 → 6G 数据面数据服务化"外延**，借 AN/AI-RAN 势能，而不是与 IBM/Informatica 正面拼通用数据编织中台。[高]
2. **最大短板 = 6G 数据面架构话语权落后华为**。ETSI ZSM 029（中兴/中电信有位）+ 3GPP SA2 WT#5 是唯二可加码的标准入口。[中]
3. **最大空白机会 = RAN 域 + 终端侧数据编织**（M3 双 🔴 区），且与中兴"网+端"覆盖重叠。[中]

---

## 脚注

[^tm]: ZTE AIR Net 自智网络，Fault Agent 用知识图谱+大模型跨域诊断，对齐 TM Forum AN L4+ — TMForum, "ZTE's vision advances Autonomous Network innovation", 2025-05
[^rcr]: ZTE 6G 战略（Native AI / AIR MAX / GigaMIMO / AIREngine） — RCR Wireless, 2026-02-28
[^spn]: ZTE 与中国移动 ITU-T SG15 首个 800G MTN（首个 6G 传输国际标准） — zte.com.cn news
[^v7]: [vendor-capability](../matrices/vendor-capability.md) 脚注 7/8 — 中兴 SA2 数据框架提案、AI-RAN
[^arch]: [6g-data-plane-architecture-2025](../../wiki/topics/6g-data-plane-architecture-2025.md)
[^upf]: [user-plane-evolution-upf-to-6g](../../wiki/topics/user-plane-evolution-upf-to-6g.md)
[^ain]: [ai-native-data-plane-status](../../wiki/topics/ai-native-data-plane-status.md)
[^gtpu]: [gtp-u-limitations-6g-alternatives](../../wiki/topics/gtp-u-limitations-6g-alternatives.md)
[^rel]: [3gpp-rel-19-20-data-architecture-status](../../wiki/topics/3gpp-rel-19-20-data-architecture-status.md)
[^sa2]: [3gpp-sa2-6g-data-framework-wt5](../../wiki/topics/3gpp-sa2-6g-data-framework-wt5.md)
