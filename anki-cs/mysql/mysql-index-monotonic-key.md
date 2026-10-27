---
id: mysql-index-monotonic-key
domain: mysql
topic: index
priority: P0
type: tradeoff
tags:
- mysql
- index
- innodb
sources:
- CS-Base/mysql/index/why_index_chose_bpuls_tree.md
- CS-Base/mysql/index/page.md
- CS-Base/mysql/index/index_interview.md
- CS-Base/mysql/index/2000w.md
---

# Question

MySQL 8.0 InnoDB 中，相比随机主键，递增主键通常怎样影响聚簇索引插入？

# Answer

插入更集中于索引末端，通常减少随机位置插入造成的页分裂和碎片，提高空间与缓存利用率。

# Extra

高并发下末端页可能成为争用热点；递增主键不是所有负载的绝对最优解。
