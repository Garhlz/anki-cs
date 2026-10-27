---
id: redis-replication-partial-resync
domain: redis
topic: replication
priority: P0
type: mechanism
tags:
- redis
- replication
sources:
- CS-Base/redis/cluster/master_slave_replication.md
---

# Question

Redis 7.x 副本断线后，什么条件下可做部分重同步而不重传整个数据集？

# Answer

副本报告的复制历史标识必须可被主节点接受，且所需偏移之后的复制流仍保留在 backlog 中；否则需全量重同步。

# Extra

不能只比较两个 offset 数字而忽略复制历史。现代 Redis 使用 replication ID，不能简单等同于进程 run ID。官方补证：[官方参考](https://redis.io/docs/latest/operate/oss_and_stack/management/replication/)
