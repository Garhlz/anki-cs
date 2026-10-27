---
id: mysql-storage-page-directory
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

MySQL 8.0 InnoDB 的索引页内，如何避免从头遍历整条有序记录链表来定位键？

# Answer

通过页目录的槽进行二分定位，找到目标所属的小记录分组，再沿记录链表在该组内查找。

# Extra

索引顺序是逻辑顺序，不意味着行在页内物理字节位置按键连续排列。
