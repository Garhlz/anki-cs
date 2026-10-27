---
id: redis-event-loop-command-io-threads
domain: redis
topic: event-loop
priority: P0
type: comparison
tags:
- redis
- event-loop
sources:
- CS-Base/redis/base/redis_interview.md
---

# Question

Redis 7.x 所说的“命令主要由单线程执行”，与多线程 I/O 是否矛盾？

# Answer

不矛盾。普通键空间命令主要在主线程串行执行，配置启用后 I/O 线程可分担网络读写等工作，后台线程还承担刷盘和释放等任务。

# Extra

不是每个实例默认开启多线程网络 I/O，也不是所有模块工作都受此简化模型约束。7.0 配置补证：[官方参考](https://raw.githubusercontent.com/redis/redis/7.0/redis.conf)
