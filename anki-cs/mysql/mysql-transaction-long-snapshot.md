---
id: mysql-transaction-long-snapshot
domain: mysql
topic: transaction
priority: P0
type: tradeoff
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

MySQL 8.0 InnoDB 中，长期保留一致性读快照为什么可能增加 undo 和版本维护成本？

# Answer

旧快照仍可能需要历史版本，使相关 undo 无法及时清理，增加历史版本与存储压力，并可能使版本回溯更长。

# Extra

不是事务一提交 undo 就必定立即删除；还需考虑其他快照的需求。 官方补证：[MySQL 8.0 手册](https://dev.mysql.com/doc/refman/8.0/en/innodb-multi-versioning.html)。
