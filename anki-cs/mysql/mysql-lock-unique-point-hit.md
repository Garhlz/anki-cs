---
id: mysql-lock-unique-point-hit
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

MySQL 8.0 InnoDB RR 中，按主键完整等值执行 SELECT ... FOR UPDATE，且记录存在时，通常需要哪种行级锁？

# Answer

对找到的主键索引记录加排他记录锁，无须为了该唯一点查锁住其前方间隙。

# Extra

限定完整唯一键等值且命中；非唯一条件、复合唯一索引部分列匹配不适用。
