---
id: mysql-storage-page-unit
domain: mysql
topic: storage
priority: P0
type: mechanism
tags:
- mysql
- storage
- innodb
sources:
- CS-Base/mysql/base/row_format.md
- CS-Base/mysql/index/page.md
---

# Question

MySQL 8.0 InnoDB 为什么以页而非单行作为数据缓存和常规磁盘读写的组织单位？

# Answer

页将多条记录组织在一起，摊薄访问开销并利用局部性；读一行通常需要先将其所在页载入 Buffer Pool。

# Extra

默认页大小为 16 KiB，但可配置；不要把页组织单位说成所有系统调用或日志写入的固定大小。
