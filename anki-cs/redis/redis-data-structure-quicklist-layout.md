---
id: redis-data-structure-quicklist-layout
domain: redis
topic: data-structure
priority: P0
type: tradeoff
tags:
- redis
- data-structure
- quicklist
sources:
- CS-Base/redis/data_struct/data_struct.md
- CS-Base/redis/data_struct/command.md
---

# Question

Redis 7.0 的 List 使用 quicklist，相比“每个元素一个链表节点”有什么空间优势？

# Answer

用链表串联分块，常见分块以 listpack 紧凑保存多个元素，摊薄节点指针和分配开销，同时限制单块连续内存的大小。

# Extra

大元素可用单独节点，不能说每个节点必然是多元素 listpack。源码补证：[官方参考](https://raw.githubusercontent.com/redis/redis/7.0/src/quicklist.h)；此卡明确限定 7.0，避免把不同 7.x 小版本编码路径一概而论。
