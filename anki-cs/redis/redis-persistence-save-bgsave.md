---
id: redis-persistence-save-bgsave
domain: redis
topic: persistence
priority: P0
type: comparison
tags:
- redis
- persistence
sources:
- CS-Base/redis/storage/rdb.md
- CS-Base/redis/storage/bigkey_aof_rdb.md
---

# Question

Redis 7.x 的 SAVE 与 BGSAVE 生成快照时，对主线程的影响有何区别？

# Answer

SAVE 在主线程生成快照，期间阻塞命令处理；BGSAVE 由 fork 出的子进程生成，但 fork 本身和后续 COW 仍可能带来延迟。

# Extra

后台执行不等于完全无阻塞，也不意味着创建子进程会立即复制全部数据页。
