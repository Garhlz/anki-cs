---
id: redis-data-structure-hash-versus-json
domain: redis
topic: data-structure
priority: P1
type: tradeoff
tags:
- redis
- data-structure
sources:
- CS-Base/redis/data_struct/command.md
---

# Question

Redis 7.x 缓存对象时，何时更适合 Hash，而非把整个对象序列化到一个 String？

# Answer

经常单独访问或更新字段时，Hash 可避免每次读取、反序列化和重写整个对象；整体读写或嵌套结构则常更适合序列化 String。

# Extra

应按访问模式与编码开销评估，不按“Hash 一定更省内存”选择。
