---
id: mysql-logging-redo-binlog
domain: mysql
topic: logging
priority: P0
type: comparison
tags:
- mysql
- logging
- innodb
- redo-log
- binlog
sources:
- CS-Base/mysql/log/how_update.md
- CS-Base/mysql/buffer_pool/buffer_pool.md
---

# Question

MySQL 8.0 开启 binlog 时，为什么 InnoDB redo 不能直接代替 binlog？

# Answer

redo 面向引擎页修改与崩溃恢复，循环复用；binlog 属于 Server 层，记录逻辑变更事件，用于复制与备份后的增量恢复。

# Extra

binlog 不一定是原始 SQL 文本，也可采用 ROW 格式。二者目标与保留方式不同。
