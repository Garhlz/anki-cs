---
id: redis-cache-avalanche-defense
domain: redis
topic: cache
priority: P0
type: application
tags:
- redis
- cache
- cache-aside
sources:
- CS-Base/redis/cluster/cache_problem.md
---

# Question

Redis 缓存服务整体不可用时，为什么只给 TTL 加随机抖动不能保护数据库？

# Answer

TTL 抖动只分散过期时刻，不能阻止整层缓存失效的回源洪峰；还需限流、熔断、降级与后端容量保护。

# Extra

高可用缩短缓存不可用时间，但不替代回源保护。
