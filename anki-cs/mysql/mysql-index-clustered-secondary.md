---
id: mysql-index-clustered-secondary
domain: mysql
topic: index
priority: P0
type: comparison
tags:
- mysql
- index
- innodb
- clustered-index
- secondary-index
sources:
- CS-Base/mysql/index/why_index_chose_bpuls_tree.md
- CS-Base/mysql/index/page.md
- CS-Base/mysql/index/index_interview.md
- CS-Base/mysql/index/2000w.md
---

# Question

MySQL 8.0 InnoDB 中，聚簇索引和二级索引的叶子记录保存内容有什么区别？

# Answer

聚簇索引叶子记录保存行数据；二级索引叶子记录保存二级索引键及聚簇键，用于定位对应行。

# Extra

显式主键存在时聚簇键就是主键。一张表只有一个聚簇索引，可有多个二级索引。
