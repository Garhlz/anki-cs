---
id: mysql-buffer-pool-dirty-page
domain: mysql
topic: buffer-pool
priority: P0
type: mechanism
tags:
- mysql
- buffer-pool
- innodb
sources:
- CS-Base/mysql/buffer_pool/buffer_pool.md
---

# Question

MySQL 8.0 InnoDB 中，Buffer Pool 脏页意味着什么，为什么更新后不必立刻写回数据文件？

# Answer

脏页是内存内容已修改但尚未写回的页；延迟刷盘可合并更新，持久化 redo 为崩溃后重做提供依据。

# Extra

是否能保证已提交事务不丢失，还取决于日志刷盘配置与存储可靠性。
