---
id: mysql-lock-gap-compatible
domain: mysql
topic: lock
priority: P1
type: mechanism
tags:
- mysql
- lock
- innodb
- gap-lock
- locking
sources:
- CS-Base/mysql/lock/mysql_lock.md
- CS-Base/mysql/lock/deadlock.md
- CS-Base/mysql/lock/show_lock.md
---

# Question

MySQL 8.0 InnoDB RR 中，两个事务为什么能同时持有同一间隙的纯 Gap Lock，却仍可能在后续插入时死锁？

# Answer

纯间隙锁彼此兼容，但插入需取得的插入意向会被对方间隙锁阻塞；若双方都持有间隙锁并尝试插入，就可能互相等待。

# Extra

不要由“间隙锁兼容”推导“间隙中的插入也兼容”。
