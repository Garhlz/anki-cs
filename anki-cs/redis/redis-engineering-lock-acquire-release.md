---
id: redis-engineering-lock-acquire-release
domain: redis
topic: engineering
priority: P0
type: mechanism
tags:
- redis
- engineering
- locking
- lease
sources:
- CS-Base/redis/base/redis_interview.md
- CS-Base/redis/data_struct/command.md
---

# Question

Redis 7.x 单节点租约锁，为什么要用 SET key token NX PX ttl，并用 Lua 比较 token 后删除？

# Answer

SET 把不存在检查与带过期写入合为一个操作；唯一 token 标识持有者，Lua 原子比较并删除，防止旧持有者误删已被他人取得的新锁。

# Extra

不应将 SETNX 与单独设置过期分成两个可能中断的步骤。脚本不被其他命令穿插，但仍需控制执行时长。
