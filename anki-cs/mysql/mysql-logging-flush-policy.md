---
id: mysql-logging-flush-policy
domain: mysql
topic: logging
priority: P0
type: tradeoff
tags:
- mysql
- logging
- innodb
sources:
- CS-Base/mysql/log/how_update.md
---

# Question

MySQL 8.0 InnoDB 中，innodb_flush_log_at_trx_commit 的 1、2、0 分别在哪个层次完成提交时的 redo 处理？

# Answer

1：提交时写日志并刷盘；2：提交时写到操作系统，后台再刷盘；0：提交不要求主动写出，后台周期性写出并刷盘。

# Extra

2 主要暴露于 OS/掉电故障，0 还暴露于进程故障；后台间隔不能理解为精确无误的数据丢失上限。双日志一致性还需考虑 sync_binlog。
