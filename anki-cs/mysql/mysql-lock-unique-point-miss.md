---
id: mysql-lock-unique-point-miss
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

MySQL 8.0 InnoDB RR 中，主键等值 SELECT ... FOR UPDATE 未找到记录，为什么仍可能阻止其他事务插入该键？

# Answer

没有现存记录可锁，但会锁住目标键所在间隙，以防其他事务插入满足该查询的行。

# Extra

例如已有 10、20，查询不存在的 15 可保护 (10,20)；边界与 supremum 情况需按实际索引分析。
