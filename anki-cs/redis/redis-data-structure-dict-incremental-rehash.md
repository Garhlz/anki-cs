---
id: redis-data-structure-dict-incremental-rehash
domain: redis
topic: data-structure
priority: P0
type: tradeoff
tags:
- redis
- data-structure
- dict
- rehash
sources:
- CS-Base/redis/data_struct/data_struct.md
- CS-Base/redis/data_struct/command.md
---

# Question

Redis 7.x 的 Dict 为什么采用渐进式 rehash，而不是一次迁移全部键？

# Answer

把旧哈希表向新表的迁移分散到多次工作中，降低一次迁移造成的长阻塞；代价是迁移期同时维护两张表和更复杂的访问逻辑。

# Extra

渐进迁移缓解延迟，不保证分配、单桶迁移等所有步骤都是严格恒定时间。
