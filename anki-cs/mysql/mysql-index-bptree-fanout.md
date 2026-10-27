---
id: mysql-index-bptree-fanout
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

为什么 MySQL 8.0 InnoDB 的 B+ 树比普通二叉搜索树更适合基于页的存储？

# Answer

内部页主要容纳导航键与子页指针，扇出高、树高通常较低，从根到叶所需访问的页数较少。

# Extra

访问页数不等于物理磁盘 I/O 次数；缓存命中时无需读盘。
