---
id: redis-cache-stale-refill-race
domain: redis
topic: cache
priority: P0
type: application
tags:
- redis
- cache
- cache-aside
sources:
- CS-Base/redis/architecture/mysql_redis_consistency.md
- CS-Base/redis/base/redis_interview.md
---

# Question

Cache Aside 中，即使先提交 MySQL 再删除 Redis 缓存，怎样仍可能发生旧值回填？

# Answer

读请求缓存未命中并读到旧数据库值；写请求随后提交新值并删除缓存；先前的读请求最后才把旧值写入缓存。

# Extra

需结合业务评估版本校验、读写协调和失效策略；不能用“数据库通常比缓存慢”排除时序。
