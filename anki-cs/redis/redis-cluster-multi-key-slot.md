---
id: redis-cluster-multi-key-slot
domain: redis
topic: cluster
priority: P1
type: application
tags:
- redis
- cluster
sources:
- CS-Base/redis/base/redis_interview.md
---

# Question

Redis 7.x Cluster 中，为什么同一事务访问 user:{42}:profile 和 user:{42}:quota 比访问任意两个用户键更容易满足多键限制？

# Answer

相同的有效 hash tag {42} 让两个键进入同一槽，可满足要求同槽的多键事务限制；跨槽操作不能直接当作单节点事务执行。

# Extra

本地材料未展开该限制，官方补证：[官方参考](https://redis.io/docs/latest/operate/oss_and_stack/reference/cluster-spec/)。Cluster 仍使用异步复制，不提供无损切换承诺。
