---
id: redis-persistence-write-fsync
domain: redis
topic: persistence
priority: P0
type: mechanism
tags:
- redis
- persistence
- fsync
- durability
sources:
- CS-Base/redis/storage/aof.md
- CS-Base/redis/base/redis_interview.md
---

# Question

Redis 7.x 中，把 AOF 缓冲写入文件与调用 fsync，在持久性上有什么区别？

# Answer

write 通常只把数据交给操作系统页缓存；fsync 请求将数据同步到持久存储，才跨过相应的掉电风险边界。

# Extra

仍依赖操作系统和存储设备正确实现持久化语义。
