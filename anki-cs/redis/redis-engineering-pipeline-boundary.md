---
id: redis-engineering-pipeline-boundary
domain: redis
topic: engineering
priority: P1
type: tradeoff
tags:
- redis
- engineering
- pipelining
sources:
- CS-Base/redis/storage/bigkey_aof_rdb.md
- CS-Base/redis/base/redis_interview.md
---

# Question

Redis 7.x 客户端 Pipeline 主要节省什么成本，为什么不能代替事务或 Lua？

# Answer

批量发送命令并集中读取响应，摊薄网络往返等待；它本身不保证多条命令不可被其他客户端插入，也不提供条件更新逻辑。

# Extra

批次过大可能增加响应缓冲和延迟，依赖前一条结果的操作也不能直接盲目流水化。
