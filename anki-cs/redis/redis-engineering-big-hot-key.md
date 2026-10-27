---
id: redis-engineering-big-hot-key
domain: redis
topic: engineering
priority: P1
type: comparison
tags:
- redis
- engineering
sources:
- CS-Base/redis/storage/bigkey_aof_rdb.md
- CS-Base/redis/base/redis_interview.md
---

# Question

Redis 7.x 中，大 key 和热 key 为什么是两个不同的性能维度？

# Answer

大 key 关注值的体积或集合元素量，影响操作、传输和释放成本；热 key 关注访问频率，小值也可能因集中访问形成热点。

# Extra

不能用固定字节数定义所有工作负载的大 key；应结合延迟、带宽、内存与频率诊断。
