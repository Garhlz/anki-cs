---
id: redis-engineering-watch-cas
domain: redis
topic: engineering
priority: P0
type: mechanism
tags:
- redis
- engineering
- optimistic-lock
sources:
- CS-Base/redis/base/redis_interview.md
- CS-Base/redis/data_struct/command.md
---

# Question

Redis 7.x 使用 WATCH 实现读后条件更新时，如何防止读与 EXEC 之间的并发修改被忽略？

# Answer

先 WATCH 相关键再读值，MULTI 排队修改并 EXEC；若监视键期间被修改，EXEC 放弃执行，客户端需重新读取并重试。

# Extra

这是乐观并发控制，不是锁住键阻止别人写。此细节为官方补充：[官方参考](https://redis.io/docs/latest/develop/using-commands/transactions/)
