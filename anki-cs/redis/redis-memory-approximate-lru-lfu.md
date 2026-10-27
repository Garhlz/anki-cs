---
id: redis-memory-approximate-lru-lfu
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

Redis 7.x 的 LRU 与 LFU 淘汰主要依据什么，为什么不应把 LFU 理解为永久累计访问次数？

# Answer

LRU 关注最近访问时间；LFU 关注带衰减的访问频率估计，旧热点会逐步降温。二者采用近似选择来控制维护成本。

# Extra

不是每次严格遍历全库挑出数学意义上的最冷键；LFU 也不保证对所有负载优于 LRU。
