---
id: redis-persistence-snapshot-cow
domain: redis
topic: persistence
priority: P0
type: mechanism
tags:
- redis
- persistence
- mvcc
- snapshot
- copy-on-write
sources:
- CS-Base/redis/storage/rdb.md
- CS-Base/redis/storage/bigkey_aof_rdb.md
---

# Question

Redis 7.x 在 BGSAVE 期间如何既允许主进程修改数据，又让子进程读取稳定快照？

# Answer

fork 后父子共享数据页；主进程写共享页时触发 COW，保留子进程看到的旧页，主进程在私有副本上修改。

# Extra

COW 以内存页为单位，不是按 Redis 键整体复制；写入覆盖的页越多，额外内存和延迟压力越大。
