---
id: redis-engineering-cow-memory-budget
domain: redis
topic: engineering
priority: P1
type: application
tags:
- redis
- engineering
- copy-on-write
sources:
- CS-Base/redis/storage/bigkey_aof_rdb.md
- CS-Base/redis/base/redis_interview.md
---

# Question

Redis 7.x 开启 BGSAVE 或 AOF 后台重写时，为什么 maxmemory 不能等于进程可用物理内存上限？

# Answer

除数据集外还需预留 COW、复制/客户端缓冲、分配器等开销；高写入会复制更多共享页，可能推高实际内存并触发 OOM。

# Extra

maxmemory 不是进程 RSS 的严格上限。容量预算不能只按键大小相加。
