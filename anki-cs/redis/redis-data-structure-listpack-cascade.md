---
id: redis-data-structure-listpack-cascade
domain: redis
topic: data-structure
priority: P0
type: comparison
tags:
- redis
- data-structure
- listpack
sources:
- CS-Base/redis/data_struct/data_struct.md
- CS-Base/redis/data_struct/command.md
---

# Question

Redis 7.x 使用的 listpack 相比历史 ziplist，如何避免前驱长度变化造成的连锁更新？

# Answer

listpack 在元素尾部编码该元素自身的长度，后一个元素不再保存前驱长度，前驱变大不会递归改变后续元素的长度字段。

# Extra

仍可能需要内存搬移或重新分配，不等于插入变为 O(1)。源码补证：[官方参考](https://raw.githubusercontent.com/redis/redis/7.0/src/listpack.c)
