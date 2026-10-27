---
id: redis-engineering-lease-expiry
domain: redis
topic: engineering
priority: P0
type: application
tags:
- redis
- engineering
- lease
sources:
- CS-Base/redis/base/redis_interview.md
- CS-Base/redis/data_struct/command.md
---

# Question

Redis 单节点租约锁中，持有者暂停超过 TTL 后继续执行，为什么唯一 token 和原子解锁仍不足以保证业务互斥？

# Answer

租约可能已到期并被他人重新取得，旧持有者仍可能操作业务资源；token 只防误删锁，不能阻止过期持有者的业务写入。

# Extra

需要结合业务资源提供额外的版本/栅栏或幂等约束；不把单节点锁方案推广为故障转移下的严格安全证明。
