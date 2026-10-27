---
id: redis-memory-lazy-active-expire
domain: redis
topic: memory
priority: P0
type: tradeoff
tags:
- redis
- memory
sources:
- CS-Base/redis/module/strategy.md
- CS-Base/redis/base/redis_interview.md
---

# Question

Redis 7.x 为什么组合惰性过期与主动过期，而不只采用其中一种？

# Answer

惰性过期在访问时检查，成本按需但不访问的过期键可能占内存；主动过期周期性检查并删除一部分键，回收冷键，同时限制 CPU 开销。

# Extra

到达 TTL 不意味着对应内存立即在那个时刻释放；主动周期也不是每轮遍历全部键。
