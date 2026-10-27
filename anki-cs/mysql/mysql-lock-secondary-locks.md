---
id: mysql-lock-secondary-locks
domain: mysql
topic: lock
priority: P0
type: mechanism
tags:
- mysql
- lock
- innodb
- secondary-index
- locking
sources:
- CS-Base/mysql/lock/how_to_lock.md
- CS-Base/mysql/lock/update_index.md
- CS-Base/mysql/lock/mysql_lock.md
---

# Question

MySQL 8.0 InnoDB RR 中，经非唯一二级索引执行 SELECT ... FOR UPDATE，为什么不能只分析对应主键行的记录锁？

# Answer

还需保护扫描到的二级索引记录及相关间隙；匹配行通常也锁定对应聚簇记录，因此锁范围可能比业务行集合更大。

# Extra

精确端点依赖 SQL、索引、计划和版本，不能把来源单个实验当作所有范围查询的固定模板。
