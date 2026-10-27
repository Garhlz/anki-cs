---
id: mysql-transaction-rc-rr-readview
domain: mysql
topic: transaction
priority: P0
type: comparison
tags:
- mysql
- transaction
- innodb
- mvcc
- read-view
sources:
- CS-Base/mysql/transaction/mvcc.md
---

# Question

MySQL 8.0 InnoDB 中，RC 与 RR 的普通一致性 SELECT 如何区别使用 Read View？

# Answer

RC 每次一致性读使用新的 Read View；RR 通常复用首次一致性读建立的 Read View，因此不因其他事务后来提交而更新快照。

# Extra

限定普通一致性读；锁定读和 DML 不按该旧快照执行。
