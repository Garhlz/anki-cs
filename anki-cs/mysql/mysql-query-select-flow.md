---
id: mysql-query-select-flow
domain: mysql
topic: query
priority: P0
type: synthesis
tags:
- mysql
- query
- innodb
sources:
- CS-Base/mysql/base/how_select.md
---

# Question

MySQL 8.0 中，一条普通 SELECT 从收到请求到返回行，主要经历哪些处理阶段？

# Answer

1. **连接与权限检查**。
2. **解析与预处理**：检查语法、解析对象及列。
3. **优化**：选择访问路径与执行计划。
4. **执行**：调用引擎取数、完成剩余处理并返回结果。

# Extra

此卡只要求阶段与职责，不背源码函数名。MySQL 8.0 已移除 Server 层 Query Cache。
