---
id: mysql-transaction-own-update-visible
domain: mysql
topic: transaction
priority: P0
type: application
tags:
- mysql
- transaction
- innodb
sources:
- CS-Base/mysql/transaction/phantom.md
- CS-Base/mysql/lock/lock_phantom.md
---

# Question

MySQL 8.0 InnoDB RR 中，A 快照读未见某行，B 插入并提交，A 随后成功更新该行；A 再普通 SELECT 能看到什么？

# Answer

A 能看到自己更新后的行。UPDATE 可操作当前记录，而自身修改对后续一致性读可见，因此结果不必与第一次快照查询完全相同。

# Extra

这说明混合读写不能理解为“永远看到数据库某一历史时刻的完整副本”。不要仅凭此反例把所有 RR 一致性读都说成不稳定。
