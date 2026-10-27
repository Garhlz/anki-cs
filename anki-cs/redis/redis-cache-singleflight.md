---
id: redis-cache-singleflight
domain: redis
topic: cache
priority: P0
type: mechanism
tags:
- redis
- cache
- cache-aside
sources:
- CS-Base/redis/cluster/cache_problem.md
---

# Question

Redis 中某个热点缓存失效时，为什么按键合并回源请求能缓解缓存击穿？

# Answer

只允许一个请求加载并回填该键，其余等待或使用可接受的旧值，避免同一热点的并发请求同时压向数据库。

# Extra

还需超时、失败释放、二次检查和降级，不能用无限等待的全局锁串行化所有键。
