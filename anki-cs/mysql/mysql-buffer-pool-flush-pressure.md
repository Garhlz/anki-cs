---
id: mysql-buffer-pool-flush-pressure
domain: mysql
topic: buffer-pool
priority: P0
type: application
tags:
- mysql
- buffer-pool
- innodb
sources:
- CS-Base/mysql/buffer_pool/buffer_pool.md
---

# Question

MySQL 8.0 InnoDB 中，为什么刷脏压力可能造成间歇性的查询或更新延迟升高？

# Answer

redo 可复用空间不足或缓存缺少可用页时，刷脏可能进入关键路径，与前台争用 I/O，甚至使前台等待页写回。

# Extra

先结合缓存、redo 与磁盘指标定位，不能仅凭偶发慢 SQL 就断言需要扩大 Buffer Pool。
