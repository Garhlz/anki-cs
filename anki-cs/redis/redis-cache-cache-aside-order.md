---
id: redis-cache-cache-aside-order
domain: redis
topic: cache
priority: P0
type: mechanism
tags:
- redis
- cache
- cache-aside
sources:
- CS-Base/redis/architecture/mysql_redis_consistency.md
- CS-Base/redis/base/redis_interview.md
---

# Question

Redis 缓存与 MySQL 使用 Cache Aside 时，为什么常先提交数据库更新，再删除缓存？

# Answer

先删缓存再更新数据库时，并发读可能从旧数据库取值并重新填回缓存；先提交再删除可减少这类旧值长期残留。

# Extra

这一顺序不是强一致性协议；并发回填与删除失败仍可能造成不一致。
