---
id: mysql-replication-async-read-lag
domain: mysql
topic: replication
priority: P1
type: application
tags:
- mysql
- replication
- innodb
sources:
- CS-Base/mysql/log/how_update.md
---

# Question

MySQL 8.0 默认异步复制中，为什么主库提交成功后立即读副本可能读到旧值？

# Answer

主库提交不等待副本完成应用；事件可能仍在传输或排队执行，因此副本读存在复制延迟。

# Extra

提交到日志、传给副本和副本应用完成是不同阶段。读己之写需要额外路由或同步约束，不能仅依赖异步复制。
