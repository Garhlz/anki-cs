---
id: mysql-transaction-acid-responsibility
domain: mysql
topic: transaction
priority: P0
type: comparison
tags:
- mysql
- transaction
- innodb
sources:
- CS-Base/mysql/transaction/mvcc.md
---

# Question

MySQL 8.0 InnoDB 中，原子性、隔离性与持久性分别主要依赖什么机制？

# Answer

原子性依靠 undo 回滚；隔离性依靠锁与 MVCC；持久性依靠 redo 等日志及正确刷盘。

# Extra

业务一致性还依赖约束和正确事务逻辑，不能认为数据库自动保证所有业务不变量。
