---
id: mysql-query-server-engine
domain: mysql
topic: query
priority: P0
type: comparison
tags:
- mysql
- query
- innodb
sources:
- CS-Base/mysql/base/how_select.md
---

# Question

MySQL 8.0 中，Server 层与 InnoDB 在 SELECT 查询中的职责如何划分？

# Answer

Server 层负责解析、优化和执行协调；InnoDB 负责按访问路径读取索引和数据，并提供事务、锁及版本可见性等存储引擎能力。

# Extra

不要把 MySQL 通用 SQL 层与 InnoDB 特有的索引和并发实现混同。
