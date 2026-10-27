---
id: mysql-index-scan-versus-seek
domain: mysql
topic: index
priority: P0
type: application
tags:
- mysql
- index
- innodb
sources:
- CS-Base/mysql/index/index_interview.md
- CS-Base/mysql/index/index_lose.md
- CS-Base/mysql/index/index_issue.md
---

# Question

MySQL 8.0 中，LIKE '%abc' 无法利用普通 B+ 树索引定位匹配范围，为什么仍可能出现 type=index？

# Answer

无法范围定位不代表不能使用索引：若索引覆盖所需列，优化器可能选择扫描整棵较小的二级索引并过滤。

# Extra

type=index 是索引全扫描，不等于高选择性的索引查找；是否选择它仍取决于成本。
