---
id: mysql-logging-prepared-recovery
domain: mysql
topic: logging
priority: P0
type: application
tags:
- mysql
- logging
- innodb
sources:
- CS-Base/mysql/log/how_update.md
---

# Question

MySQL 8.0 内部两阶段提交中，崩溃恢复发现 InnoDB 事务已 prepare 但未完成 commit，如何决定提交还是回滚？

# Answer

检查持久化 binlog 中是否存在该事务完整的提交记录及匹配 XID：存在则完成提交，不存在则回滚。

# Extra

限定 binlog 协调的内部事务；不要扩张为外部 XA 的所有恢复情形。
