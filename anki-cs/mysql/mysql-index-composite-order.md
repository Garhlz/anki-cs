---
id: mysql-index-composite-order
domain: mysql
topic: index
priority: P0
type: mechanism
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

MySQL 8.0 InnoDB 中，普通联合 B+ 树索引 (a,b,c) 为什么优先支持最左前缀定位？

# Answer

索引按 a、再同 a 内的 b、再同 (a,b) 内的 c 排序；缺少前导列约束时，后续列通常不构成一个可直接定位的连续区间。

# Extra

这是普通前缀定位原理，不等于“未提供 a 就绝不使用索引”；覆盖扫描等路径仍可能被采用。WHERE 条件书写顺序不是索引列顺序。
