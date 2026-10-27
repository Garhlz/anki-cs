---
id: redis-data-structure-dict-dual-table
domain: redis
topic: data-structure
priority: P0
type: mechanism
tags:
- redis
- data-structure
- dict
- rehash
sources:
- CS-Base/redis/data_struct/data_struct.md
- CS-Base/redis/data_struct/command.md
---

# Question

Redis Dict 在渐进式 rehash 期间，查找与新增键如何处理新旧两张表？

# Answer

查找需考虑旧表和新表；新增键放入新表，旧表逐步搬空，迁移结束后释放旧表并切换。

# Extra

这与持久化子进程的 COW 是不同机制。
