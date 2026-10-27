---
id: mysql-index-bptree-range
domain: mysql
topic: index
priority: P0
type: mechanism
tags:
- mysql
- index
- innodb
- bplus-tree
sources:
- CS-Base/mysql/index/why_index_chose_bpuls_tree.md
- CS-Base/mysql/index/page.md
- CS-Base/mysql/index/index_interview.md
- CS-Base/mysql/index/2000w.md
---

# Question

MySQL 8.0 InnoDB 的 B+ 树为什么适合范围扫描？

# Answer

叶子记录按索引键有序组织，叶子页之间有链接；定位范围起点后可沿叶子页继续扫描，不必为每个键重新从根查找。

# Extra

有序不代表各叶子页在磁盘物理位置上必然连续。
