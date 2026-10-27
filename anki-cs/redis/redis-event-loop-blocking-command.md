---
id: redis-event-loop-blocking-command
domain: redis
topic: event-loop
priority: P0
type: application
tags:
- redis
- event-loop
- locking
sources:
- CS-Base/redis/base/redis_interview.md
---

# Question

Redis 7.x 中，为什么一个很慢的大集合命令可能拖慢操作其他键的客户端？

# Answer

命令执行主要串行，长时间计算或大规模遍历会占住主线程，使其他客户端的就绪请求也要等待。

# Extra

内存数据库不代表无阻塞；应区分命令执行、网络传输、持久化和系统调度的延迟来源。
