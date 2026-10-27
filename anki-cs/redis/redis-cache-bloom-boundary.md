---
id: redis-cache-bloom-boundary
domain: redis
topic: cache
priority: P0
type: tradeoff
tags:
- redis
- cache
- cache-aside
sources:
- CS-Base/redis/cluster/cache_problem.md
---

# Question

缓存穿透治理中，布隆过滤器的“可能存在”和“不存在”应怎样解释才安全？

# Answer

对已正确加入且未因维护失误遗漏的集合，“不存在”可用于拒绝，“可能存在”仍需后续查询；新增数据未及时加入会造成业务上的误拒绝。

# Extra

经典布隆过滤器有假阳性，不应直接证明数据库当前存在。它是额外组件，不是所有 Redis 7.x 核心部署默认提供的类型。
