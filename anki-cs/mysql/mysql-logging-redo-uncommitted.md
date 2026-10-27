---
id: mysql-logging-redo-uncommitted
domain: mysql
topic: logging
priority: P0
type: mechanism
tags:
- mysql
- logging
- innodb
- redo-log
sources:
- CS-Base/mysql/log/how_update.md
- CS-Base/mysql/buffer_pool/buffer_pool.md
---

# Question

MySQL 8.0 InnoDB 中，未提交事务的 redo 能否已经落盘，为什么恢复时不能只重做而不处理事务状态？

# Answer

能。日志缓冲可能在提交前刷出；恢复需重做必要修改，并按事务提交状态处理未完成事务，利用 undo 撤销应回滚的修改。

# Extra

redo 持久化不等于事务已经提交，不能把两者作为同一事实。 官方补证：[MySQL 8.0 手册](https://dev.mysql.com/doc/refman/8.0/en/innodb-recovery.html)。
