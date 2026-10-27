---
id: redis-data-structure-zset-dual-index
domain: redis
topic: data-structure
priority: P0
type: mechanism
tags:
- redis
- data-structure
- sorted-set
sources:
- CS-Base/redis/data_struct/data_struct.md
- CS-Base/redis/data_struct/command.md
---

# Question

Redis 7.x 中，采用跳表编码的 Zset 为什么同时维护字典和跳表？

# Answer

字典支持按成员快速查分值；跳表维护按分值及成员顺序的访问，支持有序范围与排名操作，二者服务不同查询路径。

# Extra

小 Zset 可以使用紧凑编码，不是所有 Zset 都由字典加跳表实现。
