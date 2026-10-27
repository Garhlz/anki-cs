---
id: mysql-storage-overflow-row-format
domain: mysql
topic: storage
priority: P0
type: comparison
tags:
- mysql
- storage
- innodb
sources:
- CS-Base/mysql/base/row_format.md
- CS-Base/mysql/index/page.md
---

# Question

MySQL 8.0 InnoDB 中，长变长列被放到页外时，COMPACT 与 DYNAMIC 的本地记录保留内容有什么关键区别？

# Answer

COMPACT 通常保留字段前缀和页外指针；DYNAMIC 可将长字段完全移至页外，在本地仅保留指针。

# Extra

是否页外存储由行大小、列长度等共同决定，不是所有变长列都会溢出；默认 DYNAMIC 不应按 COMPACT 的前缀规则理解。
