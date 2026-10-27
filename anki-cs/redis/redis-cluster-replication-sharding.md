---
id: redis-cluster-replication-sharding
domain: redis
topic: cluster
priority: P1
type: comparison
tags:
- redis
- cluster
sources:
- CS-Base/redis/base/redis_interview.md
---

# Question

Redis 7.x 中，主从复制加 Sentinel 与 Redis Cluster 解决的数据组织问题有何区别？

# Answer

复制加 Sentinel 主要为同一数据集提供副本和故障转移；Cluster 将键空间分片到多个主节点，并为各分片配置副本与故障转移。

# Extra

本地 cluster.md 仅占位，分类依据来自 redis_interview.md；完整迁槽状态机未制卡。
