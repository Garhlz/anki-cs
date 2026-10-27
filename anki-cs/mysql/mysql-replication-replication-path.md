---
id: mysql-replication-replication-path
domain: mysql
topic: replication
priority: P1
type: synthesis
tags:
- mysql
- replication
- innodb
sources:
- CS-Base/mysql/log/how_update.md
---

# Question

MySQL 8.0 的典型 binlog 主从复制，变更从源库传到副本的主要链路是什么？

# Answer

1. 源库记录 **binlog**。
2. 副本接收线程获取事件并写入 **relay log**。
3. 副本应用线程重放事件，更新本地数据。

# Extra

线程名称与并行应用配置可变化；不要求背旧版线程名。
