---
id: mysql-lock-intention-lock
domain: mysql
topic: lock
priority: P1
type: mechanism
tags:
- mysql
- lock
- innodb
- locking
sources:
- CS-Base/mysql/lock/mysql_lock.md
- CS-Base/mysql/lock/deadlock.md
- CS-Base/mysql/lock/show_lock.md
---

# Question

MySQL 8.0 InnoDB 的表级意向锁为什么不等于“锁住整张表的数据”？

# Answer

它声明事务计划在表内持有行级共享或排他锁，使表级锁请求可快速检查兼容性；不同事务的行操作仍可并发。

# Extra

意向锁 IS/IX 与插入意向锁不是同一层级的机制。
