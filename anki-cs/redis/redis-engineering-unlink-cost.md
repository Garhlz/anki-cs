---
id: redis-engineering-unlink-cost
domain: redis
topic: engineering
priority: P1
type: tradeoff
tags:
- redis
- engineering
sources:
- CS-Base/redis/storage/bigkey_aof_rdb.md
- CS-Base/redis/base/redis_interview.md
---

# Question

Redis 7.x 删除大集合键时，相比 DEL，UNLINK 怎样减少主线程停顿？

# Answer

先从键空间移除键，将适合异步释放的对象内存回收交给后台线程，避免主线程同步遍历并释放大量元素。

# Extra

不是“零主线程成本”，也不保证内存立刻归还操作系统；最终释放工作仍须完成。
