---
id: mysql-index-count-null
domain: mysql
topic: index
priority: P1
type: comparison
tags:
- mysql
- index
- innodb
sources:
- CS-Base/mysql/index/count.md
---

# Question

MySQL 8.0 中，COUNT(*)、COUNT(1) 与 COUNT(nullable_col) 在统计语义上有什么区别？

# Answer

COUNT(*) 和 COUNT(1) 统计满足条件的行；COUNT(nullable_col) 只统计该表达式不为 NULL 的行。

# Extra

不要根据参数形式武断排列所有查询的性能；执行计划和访问成本更重要。
