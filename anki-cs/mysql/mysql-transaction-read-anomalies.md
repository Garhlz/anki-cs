---
id: mysql-transaction-read-anomalies
domain: mysql
topic: transaction
priority: P0
type: comparison
tags:
- mysql
- transaction
- innodb
sources:
- CS-Base/mysql/transaction/mvcc.md
---

# Question

关系数据库并发事务中，脏读、不可重复读与幻读关注的变化分别是什么？

# Answer

脏读读取其他事务未提交的修改；不可重复读关注同一行的值变化；幻读关注相同查询条件下匹配记录集合的变化。

# Extra

这是异常分类，不直接等同于某产品某隔离级别的实现保证。
