---
id: redis-engineering-transaction-errors
domain: redis
topic: engineering
priority: P0
type: comparison
tags:
- redis
- engineering
sources:
- CS-Base/redis/base/redis_interview.md
- CS-Base/redis/data_struct/command.md
---

# Question

Redis 7.x 的 MULTI/EXEC 遇到入队错误和执行时类型错误时，处理有何区别？

# Answer

入队阶段错误会使 EXEC 拒绝执行该事务；执行时某命令类型错误则只返回该命令错误，其余命令仍执行，不回滚已完成修改。

# Extra

DISCARD 只放弃尚未执行的命令队列，不是执行后撤销。官方补证：[官方参考](https://redis.io/docs/latest/develop/using-commands/transactions/)
