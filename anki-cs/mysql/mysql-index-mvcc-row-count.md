---
id: mysql-index-mvcc-row-count
domain: mysql
topic: index
priority: P1
type: mechanism
tags:
- mysql
- index
- innodb
- mvcc
- read-view
- undo-log
sources:
- CS-Base/mysql/index/count.md
---

# Question

MySQL 8.0 InnoDB 为什么不能用一个全局行数直接回答所有事务的精确 COUNT(*)？

# Answer

不同事务的可见版本可能不同，同一时刻可见行数也可能不同；精确计数需按本次读取的可见性统计。

# Extra

不带过滤的精确计数也可能扫描较小的二级索引。估算行数与独立维护计数器各有精度及一致性代价。
