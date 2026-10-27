---
id: mysql-buffer-pool-midpoint-lru
domain: mysql
topic: buffer-pool
priority: P0
type: mechanism
tags:
- mysql
- buffer-pool
- innodb
sources:
- CS-Base/mysql/buffer_pool/buffer_pool.md
---

# Question

MySQL 8.0 InnoDB 如何降低预读无效和大扫描对 Buffer Pool 热页的污染？

# Answer

新读入页先进入 LRU 的 old 区，避免直接挤占 young 热区；通过访问及停留时间条件限制晋升，抑制一次性扫描污染。

# Extra

old 区比例和晋升时间可配置；结果集很小的查询也可能扫描大量页。
