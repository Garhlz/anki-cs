---
id: mysql-transaction-snapshot-current
domain: mysql
topic: transaction
priority: P0
type: comparison
tags:
- mysql
- transaction
- innodb
- mvcc
- snapshot
sources:
- CS-Base/mysql/transaction/mvcc.md
- CS-Base/mysql/transaction/phantom.md
- CS-Base/mysql/log/how_update.md
---

# Question

MySQL 8.0 InnoDB RR 中，普通 SELECT 与 SELECT ... FOR UPDATE 的读取语义有什么区别？

# Answer

普通一致性 SELECT 按 Read View 读取可见版本；FOR UPDATE 是锁定读，读取可锁定的当前记录并加锁，遇到冲突可能等待。

# Extra

“当前”不表示可以读到其他事务尚未提交的版本；UPDATE/DELETE 也不能简单按普通 SELECT 的旧快照推理。
