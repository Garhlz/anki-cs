---
id: redis-data-structure-sds-binary
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

Redis 7.x 的 SDS 为什么能保存含零字节的二进制内容，并以 O(1) 得到字节长度？

# Answer

SDS 显式记录内容长度，不依赖零字节判断结束；读取长度字段即可获得字节数，数据中的零字节不会截断内容。

# Extra

字节长度不等于 Unicode 字符数。SDS 仍可在尾部保留终止零以兼容部分 C 操作。
