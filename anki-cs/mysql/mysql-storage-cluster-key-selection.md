---
id: mysql-storage-cluster-key-selection
domain: mysql
topic: storage
priority: P0
type: mechanism
tags:
- mysql
- storage
- innodb
sources:
- CS-Base/mysql/base/row_format.md
- CS-Base/mysql/index/page.md
---

# Question

MySQL 8.0 InnoDB 在表未声明主键时，如何确定聚簇索引键？

# Answer

优先选择首个所有索引列均为 NOT NULL 的唯一索引；若没有合适索引，则生成隐藏行 ID 作为聚簇键。

# Extra

可空唯一索引不能直接替代此要求。显式设计主键更利于控制二级索引大小和写入行为。
