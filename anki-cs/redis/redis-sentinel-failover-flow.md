---
id: redis-sentinel-failover-flow
domain: redis
topic: sentinel
priority: P1
type: synthesis
tags:
- redis
- sentinel
sources:
- CS-Base/redis/cluster/sentinel.md
- CS-Base/redis/cluster/master_slave_replication.md
---

# Question

Redis 7.x Sentinel 完成一次主节点故障转移，主要协调哪些动作？

# Answer

1. **故障判断并取得转移授权**。
2. 筛选可用副本并 **晋升新主**。
3. 将其他副本 **改为复制新主**。
4. 更新客户端可发现的主地址，旧主恢复后 **重新配置为副本**。

# Extra

客户端需要支持 Sentinel 发现与重连，不是 Sentinel 自动替所有旧连接切换目的地。
