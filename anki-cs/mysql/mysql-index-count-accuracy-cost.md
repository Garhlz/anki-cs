---
id: mysql-index-count-accuracy-cost
domain: mysql
topic: index
priority: P1
type: tradeoff
tags:
- mysql
- index
- innodb
sources:
- CS-Base/mysql/index/count.md
---

# Question

MySQL 8.0 InnoDB 需要快速展示大表数量时，统计估算和单独维护计数器各有什么关键代价？

# Answer

统计估算速度快但不精确；计数器可避免反复扫描，但必须处理并发更新、事务一致性和热点争用，否则会漂移。

# Extra

先区分业务需要精确值还是近似值。不能把 SHOW TABLE STATUS 等估计行数当作精确 COUNT 的等价替代。
