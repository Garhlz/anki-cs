---
id: redis-replication-async-loss
domain: redis
topic: replication
priority: P0
type: tradeoff
tags:
- redis
- replication
sources:
- CS-Base/redis/cluster/master_slave_replication.md
---

# Question

Redis 7.x 主节点已回复写成功，为什么故障转移后该写入仍可能丢失？

# Answer

复制是异步的，主节点可能在写入到达或应用于被晋升副本前故障；新主节点没有这部分状态。

# Extra

主节点本地 AOF 持久化与副本获得该写入是两个保证，开启持久化不自动消除切换损失。
