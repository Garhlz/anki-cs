---
id: redis-sentinel-quorum-majority
domain: redis
topic: sentinel
priority: P1
type: application
tags:
- redis
- sentinel
sources:
- CS-Base/redis/cluster/sentinel.md
- CS-Base/redis/cluster/master_slave_replication.md
---

# Question

Redis 7.x 部署 5 个 Sentinel、quorum=2，仅剩 2 个能互通时，为什么可能判定主节点下线却无法自动切换？

# Answer

2 个可达到下线判断的 quorum，但故障转移授权还需要 Sentinel 多数派，5 个中的多数是 3，故不足以推进切换。

# Extra

quorum 与多数派承担不同职责。官方补证：[官方参考](https://redis.io/docs/latest/operate/oss_and_stack/management/sentinel/)
