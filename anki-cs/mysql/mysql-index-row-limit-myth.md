---
id: mysql-index-row-limit-myth
domain: mysql
topic: index
priority: P0
type: application
tags:
- mysql
- index
- innodb
sources:
- CS-Base/mysql/index/why_index_chose_bpuls_tree.md
- CS-Base/mysql/index/page.md
- CS-Base/mysql/index/index_interview.md
- CS-Base/mysql/index/2000w.md
---

# Question

MySQL 8.0 InnoDB 表超过 2000 万行，是否应仅凭行数立即分表？

# Answer

不应。应依据查询负载、索引与行宽、缓存命中、延迟和容量评估；B+ 树容量取决于扇出和页容纳记录数，不存在统一的 2000 万行性能断点。

# Extra

来源中的估算依赖特定页大小、键宽和行宽，不能当作硬限制。
