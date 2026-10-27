---
id: redis-cache-cache-failures
domain: redis
topic: cache
priority: P0
type: comparison
tags:
- redis
- cache
- cache-aside
sources:
- CS-Base/redis/cluster/cache_problem.md
---

# Question

使用 Redis 缓存数据库数据时，缓存穿透、击穿和雪崩分别是哪种失效模式？

# Answer

穿透：反复查询数据库也不存在的数据；击穿：单个热点失效后并发回源；雪崩：大量键集中失效或缓存服务故障，引起广泛回源。

# Extra

应根据触发机制选保护措施，不将三者都简化成“缓存没命中”。
