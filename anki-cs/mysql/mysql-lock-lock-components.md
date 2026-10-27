---
id: mysql-lock-lock-components
domain: mysql
topic: lock
priority: P0
type: comparison
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

MySQL 8.0 InnoDB RR 中，Record Lock、Gap Lock 与 Next-Key Lock 分别保护什么？

# Answer

记录锁保护索引记录；间隙锁阻止向索引间隙插入；next-key 锁组合记录及其前方间隙，通常表示前开后闭的区间。

# Extra

纯间隙锁不是“把间隙两端记录都锁住”。锁附着于索引而非抽象的 WHERE 文本。
