---
id: redis-persistence-hybrid-format
domain: redis
topic: persistence
priority: P0
type: mechanism
tags:
- redis
- persistence
sources:
- CS-Base/redis/storage/rdb.md
- CS-Base/redis/storage/bigkey_aof_rdb.md
---

# Question

Redis 7.x 使用 RDB 格式 AOF 基础文件时，混合持久化怎样兼顾基础状态加载与近期写入恢复？

# Answer

先加载 RDB 格式的基础状态，再重放后续 AOF 增量，在较紧凑的基础状态之上保留后续变更。

# Extra

7.x 以 manifest 管理多文件，不能照搬旧版“一个文件前半 RDB、后半 AOF”的文件布局。补证：[官方参考](https://raw.githubusercontent.com/redis/redis/7.0/redis.conf)
