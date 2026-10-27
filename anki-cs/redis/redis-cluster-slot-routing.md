---
id: redis-cluster-slot-routing
domain: redis
topic: cluster
priority: P1
type: mechanism
tags:
- redis
- cluster
sources:
- CS-Base/redis/base/redis_interview.md
---

# Question

Redis 7.x Cluster 为什么通过“键到哈希槽、槽到节点”两层映射，而非把键直接固定到节点？

# Answer

槽作为稳定分区单位，使扩缩容时可移动部分槽及其键来重新分配负载；客户端按槽归属路由到对应节点。

# Extra

普通键按 CRC16 计算后映射到 16384 槽；hash tag 可指定参与计算的子串。官方补证：[官方参考](https://redis.io/docs/latest/operate/oss_and_stack/reference/cluster-spec/)
