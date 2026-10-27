---
id: redis-persistence-post-write-log
domain: redis
topic: persistence
priority: P0
type: comparison
tags:
- redis
- persistence
sources:
- CS-Base/redis/storage/aof.md
- CS-Base/redis/base/redis_interview.md
---

# Question

Redis 7.x 的 AOF 写后记录与数据库 WAL 的关键时序区别是什么？

# Answer

AOF 在命令修改内存后记录对应变更；WAL 的核心要求是数据页持久化前先保证对应日志持久化。不能把 AOF 写后日志直接称为同样的页级 WAL。

# Extra

AOF 是否保住已确认写入，还取决于 fsync 策略与故障时机。
