---
id: mysql-lock-unindexed-update
domain: mysql
topic: lock
priority: P0
type: application
tags:
- mysql
- lock
- innodb
- locking
sources:
- CS-Base/mysql/lock/how_to_lock.md
- CS-Base/mysql/lock/update_index.md
- CS-Base/mysql/lock/mysql_lock.md
---

# Question

MySQL 8.0 InnoDB RR 中，UPDATE 的过滤列无可用索引并全表扫描，为什么可能阻塞大量无关写入？

# Answer

InnoDB 会按实际扫描的聚簇索引记录及相关间隙加锁，导致广泛冲突；这不等于把行锁升级成一个表级排他锁。

# Extra

应检查真实访问计划和事务范围；WHERE 写有索引列并不保证优化器一定选择该索引。
