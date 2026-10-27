---
id: redis-sentinel-replica-selection
domain: redis
topic: sentinel
priority: P1
type: mechanism
tags:
- redis
- sentinel
sources:
- CS-Base/redis/cluster/sentinel.md
- CS-Base/redis/cluster/master_slave_replication.md
---

# Question

Redis 7.x Sentinel 选新主时，为什么不是无条件选择复制 offset 最大的副本？

# Answer

先排除不适合晋升的副本，再按配置优先级等规则排序；在优先级相同时才比较复制进度等条件。

# Extra

replica-priority=0 不参与晋升；选主机制权衡可用性和配置意图，不能保证绝无数据损失。
