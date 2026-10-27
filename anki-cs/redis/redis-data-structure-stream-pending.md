---
id: redis-data-structure-stream-pending
domain: redis
topic: data-structure
priority: P1
type: mechanism
tags:
- redis
- data-structure
- stream
- consumer-group
sources:
- CS-Base/redis/data_struct/command.md
---

# Question

Redis 7.x Stream 消费组中，PEL 与 XACK 如何帮助处理消费者读取后崩溃的情况？

# Answer

消息投递后记录在待确认列表 PEL，处理成功再 XACK；消费者失败时可检查、接管未确认消息并重试。

# Extra

这不自动提供 exactly-once：业务处理后确认前崩溃会导致重试，需幂等；PEL 也不代替持久化与正确裁剪策略。
