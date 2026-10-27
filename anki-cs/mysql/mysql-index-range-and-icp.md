---
id: mysql-index-range-and-icp
domain: mysql
topic: index
priority: P0
type: mechanism
tags:
- mysql
- index
- innodb
- index-condition-pushdown
sources:
- CS-Base/mysql/index/index_interview.md
- CS-Base/mysql/index/index_lose.md
- CS-Base/mysql/index/index_issue.md
---

# Question

MySQL 8.0 InnoDB 使用 (a,b) 索引执行 a > 10 AND b = 5 且需要非索引列时，ICP 为什么可能减少回表？

# Answer

a 的范围定位后，b 通常不能把整个扫描范围收缩为单一连续小区间；ICP 可先在二级索引记录上判断 b，仅对通过的记录回表。

# Extra

索引下推减少的是无效回表，不保证减少遍历的二级索引条目，也不等于覆盖索引。
