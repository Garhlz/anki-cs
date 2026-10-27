---
id: redis-data-structure-bitmap-hll
domain: redis
topic: data-structure
priority: P1
type: comparison
tags:
- redis
- data-structure
sources:
- CS-Base/redis/data_struct/command.md
---

# Question

Redis 7.x 中，需要精确查询用户是否签到，与只需估算独立访客数量，为什么分别考虑 Bitmap 和 HyperLogLog？

# Answer

Bitmap 按位保存明确的布尔状态，适合稠密编号的精确成员判断；HyperLogLog 节省基数统计空间但有估算误差，不能回答具体成员是否存在。

# Extra

稀疏且编号很大的 Bitmap 可能浪费空间，不能只看单个位的成本。
