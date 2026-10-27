---
id: redis-sentinel-sdown-odown
domain: redis
topic: sentinel
priority: P1
type: comparison
tags:
- redis
- sentinel
sources:
- CS-Base/redis/cluster/sentinel.md
- CS-Base/redis/cluster/master_slave_replication.md
---

# Question

Redis 7.x Sentinel 中，主观下线与客观下线有什么区别？

# Answer

主观下线是单个 Sentinel 的本地故障判断；客观下线是对主节点结合其他 Sentinel 意见，达到配置 quorum 后形成的判断。

# Extra

网络延迟可能产生误判；客观下线不等于已经完成选主和切换。
