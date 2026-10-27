---
id: redis-data-structure-compact-encoding
domain: redis
topic: data-structure
priority: P0
type: tradeoff
tags:
- redis
- data-structure
sources:
- CS-Base/redis/data_struct/data_struct.md
- CS-Base/redis/data_struct/command.md
---

# Question

Redis 7.x 为什么让小 Hash 或小 Zset 使用 listpack，而不始终使用完整哈希表或跳表结构？

# Answer

连续紧凑编码减少指针和分配开销、改善局部性；但查找和插入可能涉及线性扫描或搬移，因此更适合小对象。

# Extra

对象类型不等于底层编码；编码转换阈值依赖版本和配置，不要求背固定数字。
