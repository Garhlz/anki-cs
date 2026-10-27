---
id: redis-data-structure-sds-growth
domain: redis
topic: data-structure
priority: P0
type: mechanism
tags:
- redis
- data-structure
- sds
sources:
- CS-Base/redis/data_struct/data_struct.md
- CS-Base/redis/data_struct/command.md
---

# Question

Redis 的 SDS 在追加字符串时，如何降低越界风险和频繁分配成本？

# Answer

根据已用长度与可用容量检查空间，不足时先扩容；预留空间可摊薄后续追加的分配开销。

# Extra

这是 SDS API 的容量管理，不是说任意绕过 API 的 C 指针写入都不会越界。
