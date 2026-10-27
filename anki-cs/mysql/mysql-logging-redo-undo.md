---
id: mysql-logging-redo-undo
domain: mysql
topic: logging
priority: P0
type: comparison
tags:
- mysql
- logging
- innodb
- redo-log
- undo-log
sources:
- CS-Base/mysql/log/how_update.md
- CS-Base/mysql/buffer_pool/buffer_pool.md
---

# Question

MySQL 8.0 InnoDB 中，redo 与 undo 的恢复方向和主要用途有什么区别？

# Answer

redo 用于重放页修改，恢复崩溃前已记录的状态；undo 提供撤销修改的信息，用于事务回滚和一致性读的历史版本重建。

# Extra

两者不是“一个提交后才生成、一个提交前才生成”；事务执行期间可同时产生。
