---
id: mysql-logging-internal-two-phase
domain: mysql
topic: logging
priority: P0
type: synthesis
tags:
- mysql
- logging
- innodb
sources:
- CS-Base/mysql/log/how_update.md
---

# Question

MySQL 8.0 InnoDB 开启 binlog、采用双 1 持久化配置时，内部两阶段提交如何协调两类日志？

# Answer

1. 引擎进入 **prepare**，保存可恢复的事务状态。
2. 先保证相关 **redo 持久化**，再持久化含事务提交标识的 **binlog**。
3. 完成引擎 **commit**；崩溃时由日志协调提交决定。

# Extra

这是逻辑依赖顺序，不是每个事务单独做所有刷盘的物理时序；组提交可合并 I/O。双 1 指 innodb_flush_log_at_trx_commit=1、sync_binlog=1。
