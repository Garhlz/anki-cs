---
id: mysql-index-expression-boundary
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

MySQL 8.0 中，对普通索引列使用函数或隐式类型转换，为什么可能妨碍范围定位？

# Answer

普通索引按原列值排序，转换后比较结果未必能映射为原索引上的连续范围，因此可能需要扫描过滤。

# Extra

并非所有表达式都必然失效；匹配的函数索引、可改写条件等属于必要例外。函数索引在 8.0.13 起提供。
