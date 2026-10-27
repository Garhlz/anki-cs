---
id: mysql-buffer-pool-management-lists
domain: mysql
topic: buffer-pool
priority: P0
type: comparison
tags:
- mysql
- buffer-pool
- innodb
sources:
- CS-Base/mysql/buffer_pool/buffer_pool.md
---

# Question

MySQL 8.0 InnoDB 的 Free、Flush 和 LRU 链表各解决什么页管理问题？

# Answer

Free 管理空闲缓存页；Flush 跟踪需写回的脏页；LRU 管理已缓存页的冷热与替换顺序。

# Extra

脏页可同时在 Flush 与 LRU 中；三条链表不是互斥的三种页内容。
