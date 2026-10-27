---
id: mysql-logging-wal-order
domain: mysql
topic: logging
priority: P0
type: mechanism
tags:
- mysql
- logging
- innodb
- wal
sources:
- CS-Base/mysql/log/how_update.md
- CS-Base/mysql/buffer_pool/buffer_pool.md
---

# Question

MySQL 8.0 InnoDB 的 WAL 对数据页写回与对应 redo 持久化规定了什么关键顺序？

# Answer

数据页写回持久存储前，覆盖其修改的 redo 必须先持久化；这样即使数据页状态不完整，也有日志支持恢复。

# Extra

WAL 不要求每次修改立刻刷数据页，也不等于“先改磁盘日志，再改内存页”的机械顺序。
