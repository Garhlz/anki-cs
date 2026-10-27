---
id: mysql-transaction-version-chain
domain: mysql
topic: transaction
priority: P0
type: mechanism
tags:
- mysql
- transaction
- innodb
sources:
- CS-Base/mysql/transaction/mvcc.md
- CS-Base/mysql/transaction/phantom.md
- CS-Base/mysql/log/how_update.md
---

# Question

MySQL 8.0 InnoDB 一致性读遇到当前记录版本不可见时，如何寻找可读版本？

# Answer

依据记录的事务 ID 判断可见性；若不可见，沿回滚指针利用 undo 重建旧版本，直到找到可见版本或确认该行对快照不存在。

# Extra

Read View 不是全表数据副本，而是判断版本可见性的快照信息。
