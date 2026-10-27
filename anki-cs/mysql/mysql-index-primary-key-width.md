---
id: mysql-index-primary-key-width
domain: mysql
topic: index
priority: P0
type: tradeoff
tags:
- mysql
- index
- innodb
sources:
- CS-Base/mysql/index/why_index_chose_bpuls_tree.md
- CS-Base/mysql/index/page.md
- CS-Base/mysql/index/index_interview.md
- CS-Base/mysql/index/2000w.md
---

# Question

MySQL 8.0 InnoDB 中，使用很宽的主键为什么会放大二级索引开销？

# Answer

二级索引记录也要保存主键。主键越宽，每条二级索引记录通常越大，页内可容纳的记录越少，增加空间和缓存压力。

# Extra

主键选择还要考虑业务稳定性和写入模式，不能只看主键索引本身。
