---
id: redis-data-structure-skiplist-search
domain: redis
topic: data-structure
priority: P0
type: mechanism
tags:
- redis
- data-structure
- skiplist
sources:
- CS-Base/redis/data_struct/data_struct.md
- CS-Base/redis/data_struct/command.md
---

# Question

Redis 7.x Zset 的跳表如何利用多层链接加快定位，并支持后续范围扫描？

# Answer

从高层向前跳过大片区间，接近目标时逐层下降，定位起点后沿底层有序链表扫描后续元素。

# Extra

随机层高带来通常 O(log N) 的定位效率；不是每个节点都有最高层，也不能把平均复杂度说成任意输入的严格保证。
