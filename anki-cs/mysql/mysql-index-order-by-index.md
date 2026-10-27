---
id: mysql-index-order-by-index
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

MySQL 8.0 InnoDB 有索引 (a,b)，WHERE a = 常量 ORDER BY b 为什么可能避免额外排序？

# Answer

固定 a 后，该段索引记录已经按 b 排序；若执行路径保持这一顺序，就可按索引顺序输出。

# Extra

a 为范围或存在其他排序列时不能照搬结论，仍应查看执行计划。
