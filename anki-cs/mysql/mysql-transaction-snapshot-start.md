---
id: mysql-transaction-snapshot-start
domain: mysql
topic: transaction
priority: P0
type: application
tags:
- mysql
- transaction
- innodb
- mvcc
- snapshot
sources:
- CS-Base/mysql/transaction/mvcc.md
---

# Question

MySQL 8.0 InnoDB RR 中，普通 BEGIN 后尚未读表，其他事务已提交；此时首次一致性 SELECT 使用哪个时点的快照？

# Answer

通常使用首次一致性读建立 Read View 时的快照，而不是 BEGIN 语句执行时的快照。

# Extra

START TRANSACTION WITH CONSISTENT SNAPSHOT 可提前建立一致性快照。来源有“启动事务时”这一简化说法，本卡保留精确边界。官方补证：[官方参考](https://dev.mysql.com/doc/refman/8.0/en/innodb-consistent-read.html)
