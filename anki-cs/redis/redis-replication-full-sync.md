---
id: redis-replication-full-sync
domain: redis
topic: replication
priority: P0
type: synthesis
tags:
- redis
- replication
sources:
- CS-Base/redis/cluster/master_slave_replication.md
---

# Question

Redis 7.x 副本需要全量同步时，如何衔接基础数据与同步过程中的新写入？

# Answer

1. **协商全量同步**与复制进度。
2. 传送并加载 **RDB 基础快照**。
3. 补发快照之后的 **复制流增量**。
4. 继续接收持续的变更传播。

# Extra

可采用磁盘或无盘传输；fork、加载和带宽成本不能忽略。本卡考察阶段衔接，不限定必须落地一个临时 RDB 文件。
