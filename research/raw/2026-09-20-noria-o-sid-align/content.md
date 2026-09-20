# Orange NORIA-O（SID 对齐对照样本）

NORIA-O 是面向 ICT 异常检测与事件管理的 RDFS/OWL 本体，复用 SEAS、FOLIO、UCO、ORG、BOT 等，并在类/属性级对齐 TM Forum 与 IETF。

稳定入口：https://w3id.org/noria/

与 TMF 的显式对齐（TTL 注释，v0.3）：

- `noria:applicationFunctionalDomain` ≡ ODA Functional Framework 的 Domain；`rdfs:isDefinedBy` 指向 SID 页面
- `noria:applicationFunctionalSubDomain` ≡ SID ABE / BE
- `noria:Service` ≡ TMF638 Service Inventory 的 Service 对象
- `noria:serviceType` 对应 CustomerFacingService / ResourceFacingService

这是目前公开 OWL 里**真正写出 TMF 等价关系**的少数样本，对比 AsiaInfo AN-Ontology（无 SID 映射）和 TMF 官方 SID（仍是 UML/XMI）。
