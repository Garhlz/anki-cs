---
id: mysql-lock-rc-gap-boundary
domain: mysql
topic: lock
priority: P0
type: comparison
tags:
- mysql
- lock
- innodb
- gap-lock
- locking
sources:
- CS-Base/mysql/lock/how_to_lock.md
- CS-Base/mysql/lock/update_index.md
- CS-Base/mysql/lock/mysql_lock.md
---

# Question

MySQL 8.0 InnoDB 中，RC 相比 RR 的普通搜索和索引扫描，间隙锁使用有什么重要变化？

# Answer

RC 通常不为普通搜索和索引扫描保留间隙锁，减少范围阻塞；但外键检查和重复键检查仍有例外。

# Extra

因此不能记为“RC 完全没有间隙锁”。官方补证：[官方参考](https://dev.mysql.com/doc/refman/8.0/en/innodb-locking.html)
