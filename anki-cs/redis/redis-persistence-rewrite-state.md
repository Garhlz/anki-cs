---
id: redis-persistence-rewrite-state
domain: redis
topic: persistence
priority: P0
type: mechanism
tags:
- redis
- persistence
sources:
- CS-Base/redis/storage/aof.md
- CS-Base/redis/base/redis_interview.md
---

# Question

Redis 7.x AOF 重写为什么能缩小日志，而不必逐条保留所有历史写命令？

# Answer

它基于当前内存状态生成可重建数据的基础文件，不再保留已被后续写覆盖的冗余历史；重写期间的新变更另行记录。

# Extra

重写不是事务回滚，也不是简单压缩旧文件字节。基础文件可为 RDB 或 AOF 格式。
