---
id: mysql-index-index-cost
domain: mysql
topic: index
priority: P0
type: tradeoff
tags:
- mysql
- index
- innodb
sources:
- CS-Base/mysql/index/index_interview.md
- CS-Base/mysql/index/index_lose.md
- CS-Base/mysql/index/index_issue.md
---

# Question

MySQL 8.0 InnoDB 中，为什么有匹配索引时优化器仍可能选择全表扫描？

# Answer

若预计匹配行很多，扫描二级索引再大量回表的成本可能高于顺序遍历聚簇索引；还取决于统计信息与数据分布。

# Extra

索引存在、能够用于定位和最终被选择是三个不同问题。应通过执行计划验证。
