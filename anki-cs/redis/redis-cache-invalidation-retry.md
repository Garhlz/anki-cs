---
id: redis-cache-invalidation-retry
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

MySQL 更新成功但 Redis 缓存删除失败时，可靠重试或订阅 binlog 解决了什么，尚未解决什么？

# Answer

它们可补偿遗漏的失效操作，推动缓存最终收敛；异步传播仍有时间窗口，也需保证事件可靠交付、重试与幂等。

# Extra

不能只写“加消息队列即可保证一致性”；数据库提交与发消息之间本身也可能失败。延迟双删的固定等待时间不能覆盖所有竞态。
