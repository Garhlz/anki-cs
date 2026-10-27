---
id: mysql-lock-deadlock-retry
domain: mysql
topic: lock
priority: P1
type: application
tags:
- mysql
- lock
- innodb
- locking
- deadlock
sources:
- CS-Base/mysql/lock/mysql_lock.md
- CS-Base/mysql/lock/deadlock.md
- CS-Base/mysql/lock/show_lock.md
---

# Question

MySQL 8.0 InnoDB 检测到死锁并回滚某事务后，应用应怎样处理该事务？

# Answer

将该事务视为失败，按业务幂等与重试策略重试完整事务；通过统一加锁顺序和缩短事务降低复发概率。

# Extra

死锁是等待环，不是所有锁等待都是死锁；外部副作用也必须纳入重试设计。
