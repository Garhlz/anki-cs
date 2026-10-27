---
id: mysql-query-explain-evidence
domain: mysql
topic: query
priority: P0
type: application
tags:
- mysql
- query
- innodb
sources:
- CS-Base/mysql/base/how_select.md
---

# Question

MySQL 8.0 中，如何判断一条 SELECT 是否按预期使用索引，而不只凭 WHERE 字段猜测？

# Answer

查看 EXPLAIN 的访问类型、实际选择的 key、预计扫描行数和 Extra，结合查询条件与投影判断扫描范围及回表需求。

# Extra

EXPLAIN 是计划与估计信息，不能直接证明实际耗时；统计信息和数据分布会影响优化器选择。
