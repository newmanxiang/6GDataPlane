# Research：原料层

> 凡 wiki/report 中的论断都必须能在这里找到原始证据。
> 这一层**不直接被报告引用**，但是被 wiki 引用、被报告通过 wiki 间接引用。

## 子目录

| 目录 | 内容 |
|---|---|
| `raw/` | 抓取/精读的全文片段，按 `YYYY-MM-DD-<source-slug>/` 归档 |
| `notes/` | 阅读笔记，按子题归档：`<topic-slug>.md` |
| `search-log.md` | 搜索日志：query / database / date / results，可复现 |

## raw/ 归档约定

每次精读后：

```
research/raw/
  2026-06-20-3gpp-tr22870/
    content.md         # 主体抓取内容（保留 source URL、抓取日期）
    metadata.yaml      # url / title / authors / date / hash
    excerpts.md        # 关键摘录（供 wiki/notes 引用）
```

`metadata.yaml` 模板：
```yaml
url: https://...
title: ...
authors: [...]
publisher: 3GPP
publication_date: YYYY-MM-DD
fetched_at: YYYY-MM-DD HH:MM
fetched_by: exa | firecrawl | browser
content_sha256: <hash>
tags: []
```

## notes/ 阅读笔记约定

每个子题一份 markdown，结构见 `6g-deep-dive` SKILL.md 阶段 3 描述。

## search-log.md

见同目录文件，每次搜索后追加一行。
