---
id: redis-replication-backlog-versus-output
domain: redis
topic: replication
priority: P0
type: comparison
tags:
- redis
- replication
sources:
- CS-Base/redis/cluster/master_slave_replication.md
---

# Question

Redis 复制中，用于部分重同步的 backlog 与面向副本发送积压的缓冲，在逻辑职责上有什么区别？

# Answer

backlog 保留有限的近期复制历史，支持断线续传；发送积压跟踪副本尚未发送完的数据，反映慢副本的传输压力。

# Extra

Redis 7.x 可共享底层复制缓冲块；不要照搬旧资料“一从一份完全独立物理 buffer”的断言。 源码补证：[官方参考](https://raw.githubusercontent.com/redis/redis/7.0/src/replication.c)
