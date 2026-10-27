---
id: redis-event-loop-multiplexing
domain: redis
topic: event-loop
priority: P0
type: mechanism
tags:
- redis
- event-loop
sources:
- CS-Base/redis/base/redis_interview.md
---

# Question

Redis 7.x 为什么可以用事件循环服务许多连接，而不为每个连接建立线程？

# Answer

I/O 多路复用报告就绪连接，事件循环按就绪事件处理非阻塞读写和命令，避免每个连接长期占用一个线程等待网络。

# Extra

多路复用降低等待成本，不会让一个昂贵命令自动并行执行。
