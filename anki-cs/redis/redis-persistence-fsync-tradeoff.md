---
id: redis-persistence-fsync-tradeoff
domain: redis
topic: persistence
priority: P0
type: tradeoff
tags:
- redis
- persistence
- fsync
- durability
sources:
- CS-Base/redis/storage/aof.md
- CS-Base/redis/base/redis_interview.md
---

# Question

Redis 7.x AOF 的 always、everysec、no 三种刷盘策略如何权衡性能与数据风险？

# Answer

always 更频繁同步，延迟成本较高；everysec 后台约每秒同步，存在近期写入丢失窗口；no 交由 OS 刷盘，持久化时机更不可控。

# Extra

“约一秒”不是所有故障与磁盘阻塞情况下的严格最大损失上限；额外跳过刷盘配置也会改变风险。
