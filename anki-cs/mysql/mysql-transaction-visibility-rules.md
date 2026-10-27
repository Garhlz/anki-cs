---
id: mysql-transaction-visibility-rules
domain: mysql
topic: transaction
priority: P0
type: synthesis
tags:
- mysql
- transaction
- innodb
sources:
- CS-Base/mysql/transaction/mvcc.md
- CS-Base/mysql/transaction/phantom.md
- CS-Base/mysql/log/how_update.md
---

# Question

MySQL 8.0 InnoDB 中，给定 Read View 的创建者 ID、活跃事务集合及上下界，如何判断某版本 trx_id 的可见性？

# Answer

1. **自身事务**的版本可见。
2. 小于**最小活跃 ID**的版本可见。
3. 大于等于**创建快照时下一个可分配 ID**的版本不可见。
4. 介于两界之间：在**活跃集合**中不可见，不在则可见；不可见时继续查旧版本。

# Extra

Read View 的活跃集合针对读写事务；上界不是“活跃集合最大值”。无活跃事务时下界与上界的处理由实现维护。
