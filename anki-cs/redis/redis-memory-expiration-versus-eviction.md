---
id: redis-memory-expiration-versus-eviction
domain: redis
topic: memory
priority: P0
type: comparison
tags:
- redis
- memory
sources:
- CS-Base/redis/module/strategy.md
- CS-Base/redis/base/redis_interview.md
---

# Question

Redis 7.x 中，过期删除与 maxmemory 内存淘汰的触发条件和候选键有什么区别？

# Answer

过期删除依据 TTL，处理已过期键；内存淘汰在内存压力下按策略选键，可能删除尚未过期的键。

# Extra

不要用“配置过期时间”代替容量管理，也不要认为所有淘汰都只处理过期键。
