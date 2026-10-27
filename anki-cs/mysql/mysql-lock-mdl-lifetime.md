---
id: mysql-lock-mdl-lifetime
domain: mysql
topic: lock
priority: P1
type: application
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

MySQL 8.0 中，为什么一个只做 SELECT 后长期未结束的显式事务也可能阻塞 ALTER TABLE？

# Answer

读表会取得保护表定义的元数据锁，通常持有到事务结束；ALTER TABLE 所需的冲突 MDL 因此要等待。

# Extra

MDL 保护对象定义，不等同于 InnoDB 数据行锁。
