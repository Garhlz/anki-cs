---
id: mysql-index-prefix-index-cost
domain: mysql
topic: index
priority: P0
type: tradeoff
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

MySQL 8.0 InnoDB 中，字符串前缀索引节省空间的代价是什么？

# Answer

只保留前缀会降低区分度，可能增加候选行验证；也不能仅凭前缀还原完整字段，限制覆盖完整列和按完整值排序的能力。

# Extra

前缀长度应结合分布与查询需求选择，不背固定长度。
