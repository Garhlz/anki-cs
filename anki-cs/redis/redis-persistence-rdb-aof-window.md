---
id: redis-persistence-rdb-aof-window
domain: redis
topic: persistence
priority: P0
type: tradeoff
tags:
- redis
- persistence
- aof
- rdb
sources:
- CS-Base/redis/storage/rdb.md
- CS-Base/redis/storage/bigkey_aof_rdb.md
---

# Question

Redis 7.x 仅用周期性 RDB，与使用 AOF 相比，崩溃后的数据损失窗口和恢复工作有何差异？

# Answer

RDB 只能恢复到最近成功快照，之后写入可能丢失；AOF 可按刷盘策略保留更近变更，但恢复需加载基础状态并重放相关增量。

# Extra

恢复快慢取决于数据与日志规模，不能给出普遍固定倍数。两者都不能代替备份和恢复演练。
