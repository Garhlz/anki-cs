---
id: redis-replication-lag-write-guard
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

Redis 7.x 的 min-replicas-to-write 与 min-replicas-max-lag 为什么只能降低分区写入风险，不能证明强一致性？

# Answer

它们依据足够数量、近期响应的副本来限制主节点接受写入，但并不要求每条写入得到同步持久化确认，仍有复制与故障窗口。

# Extra

本地资料有“配置后不会脑裂或丢失”的过强结论，本卡收窄为风险控制。官方补证：[官方参考](https://redis.io/docs/latest/operate/oss_and_stack/management/replication/)
