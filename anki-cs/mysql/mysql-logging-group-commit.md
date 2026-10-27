---
id: mysql-logging-group-commit
domain: mysql
topic: logging
priority: P0
type: tradeoff
tags:
- mysql
- logging
- innodb
sources:
- CS-Base/mysql/log/how_update.md
---

# Question

MySQL 8.0 中，组提交如何减少事务持久化开销，额外等待的代价是什么？

# Answer

将一组事务的日志写出和刷盘合并，摊薄同步 I/O 成本、提高吞吐；聚集更多事务的等待也可能增加单事务提交延迟。

# Extra

不要将“双 1”误解为每个事务必然独占一次物理 fsync；仍须保证提交与日志协调的顺序。
