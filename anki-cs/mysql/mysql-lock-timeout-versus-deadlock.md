---
id: mysql-lock-timeout-versus-deadlock
domain: mysql
topic: lock
priority: P1
type: comparison
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

MySQL 8.0 InnoDB 默认 innodb_rollback_on_timeout=OFF 时，锁等待超时与死锁牺牲者的回滚范围有什么区别？

# Answer

锁等待超时通常只回滚当前语句，事务仍需应用处理；死锁牺牲者会被回滚整个事务。

# Extra

本地 deadlock.md 将超时回滚范围说得过宽。官方补证：[官方参考](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/innodb-parameters.html)
