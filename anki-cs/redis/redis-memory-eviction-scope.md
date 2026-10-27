---
id: redis-memory-eviction-scope
domain: redis
topic: memory
priority: P0
type: application
tags:
- redis
- memory
sources:
- CS-Base/redis/module/strategy.md
- CS-Base/redis/base/redis_interview.md
---

# Question

Redis 7.x 中，纯缓存场景为什么常需区分 volatile-* 与 allkeys-* 淘汰策略？

# Answer

volatile-* 只从设置过期时间的键中选候选，allkeys-* 可从所有键中选；未设 TTL 的键很多时，前者可能找不到足够可淘汰对象。

# Extra

noeviction 在达到限制时拒绝需要额外内存的相关操作，不等于 Redis 拒绝所有读取。
