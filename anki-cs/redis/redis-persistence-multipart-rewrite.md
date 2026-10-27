---
id: redis-persistence-multipart-rewrite
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

Redis 7.0 起的多文件 AOF 重写，如何衔接子进程生成的基础状态和重写期间的新写入？

# Answer

子进程生成新 BASE 文件，主进程将新写入记入 INCR 文件，完成后通过 manifest 管理有效基础文件与增量序列的切换。

# Extra

本地 aof.md 的“重写缓冲区最终追加到单个新文件”属于旧版流程。7.0 源码补证：[官方参考](https://raw.githubusercontent.com/redis/redis/7.0/src/aof.c)
