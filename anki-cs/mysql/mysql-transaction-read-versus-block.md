---
id: mysql-transaction-read-versus-block
domain: mysql
topic: transaction
priority: P0
type: comparison
tags:
- mysql
- transaction
- innodb
- locking
sources:
- CS-Base/mysql/transaction/phantom.md
- CS-Base/mysql/lock/lock_phantom.md
---

# Question

MySQL 8.0 InnoDB RR 下，普通一致性范围读与 FOR UPDATE 范围读，分别如何对待其他事务插入？

# Answer

普通一致性读通常不阻止插入，而是通过快照不看见后插入的行；锁定范围读通过记录及间隙锁阻止向受保护范围插入。

# Extra

锁范围依赖索引与访问路径。不可将“快照不见新行”解释成“MVCC 阻止插入”。
