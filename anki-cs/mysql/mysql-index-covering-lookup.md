---
id: mysql-index-covering-lookup
domain: mysql
topic: index
priority: P0
type: comparison
tags:
- mysql
- index
- innodb
- covering-index
sources:
- CS-Base/mysql/index/index_interview.md
- CS-Base/mysql/index/index_lose.md
- CS-Base/mysql/index/index_issue.md
---

# Question

MySQL 8.0 InnoDB 的 SELECT 中，覆盖索引与回表的区别是什么？

# Answer

覆盖表示所需列能从选用索引取得；若二级索引缺少所需列，就需按其主键值再查聚簇索引，即回表。

# Extra

这是列覆盖层面的访问路径解释；不要扩张成任何一致性读场景都绝不访问聚簇记录的底层承诺。 官方补证：[MySQL 8.0 手册](https://dev.mysql.com/doc/refman/8.0/en/innodb-multi-versioning.html)。
