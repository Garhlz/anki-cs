# 初版审查报告

## 结果与统计

本版已完成本地资料扫描、全局规划、按知识单元分批落盘、各 Topic 内容复核与全局格式检查。范围是筛选后的核心学习目标；资料缺口仍保留，不声明整个数据库领域已覆盖。

扫描 Markdown：MySQL 22 份，Redis 13 份，共 35 份；包含介绍页和占位页。
知识单元 39 个：P0 20、P1 13、P2 6。
覆盖状态：covered 27、partial 0、skipped 10、uncovered 2；P0 均已筛选制卡。
独立卡片 115 张：MySQL 60、Redis 55；卡片优先级 P0 91、P1 24、P2 0。

MySQL 卡片数低于最初参考区间，原因是合并重复目标并跳过低收益枚举，而非为达到数量拆分。数量不是覆盖率。

### Topic 分布

| Domain / Topic | 卡片数 |
|---|---:|
| mysql/buffer-pool | 4 |
| mysql/index | 17 |
| mysql/lock | 11 |
| mysql/logging | 9 |
| mysql/query | 3 |
| mysql/replication | 2 |
| mysql/storage | 4 |
| mysql/transaction | 10 |
| redis/cache | 7 |
| redis/cluster | 3 |
| redis/data-structure | 12 |
| redis/engineering | 8 |
| redis/event-loop | 3 |
| redis/memory | 4 |
| redis/persistence | 9 |
| redis/replication | 5 |
| redis/sentinel | 4 |

### Type 分布

| Type | 卡片数 |
|---|---:|
| application | 23 |
| comparison | 29 |
| concept | 0 |
| mechanism | 37 |
| synthesis | 6 |
| tradeoff | 20 |

## 批次审查与语义去重

先建立知识地图，再依次处理查询/页组织、索引结构/访问路径、计数、缓存、事务/MVCC、锁、日志/提交、复制，以及 Redis 的结构、事件循环、内存、持久化、复制/哨兵/分片、缓存与工程场景。每个知识单元落盘后运行全库格式检查、更新地图，并对照已有回忆目标判断重叠。最终复核了全部题干和答案的条件、粒度及对应目标。

| Topic 组 | 内容审查重点与处理 |
|---|---|
| MySQL query / storage | 去掉旧 Query Cache 阶段；区分逻辑有序与物理连续，修正聚簇键的 NOT NULL 前提 |
| MySQL index | 合并多篇的 B+ 树、聚簇/二级说明；覆盖与 ICP 分开，区分索引扫描/定位；不传播固定行数上限 |
| MySQL buffer-pool | 冷热晋升与刷脏压力各保留一个目标，WAL 顺序交给 logging，避免重复解释 |
| MySQL transaction | RC/RR 时机、可见性算法、读类型及混合读写反例独立处理；综合算法不拆成若干无意义判断题 |
| MySQL lock | 基本锁、典型点查、扫描范围、协调与死锁分别处理；跳过逐端点规则全集 |
| MySQL logging / replication | 分清 redo 已持久化与事务已提交；逻辑提交流程与组提交的物理时序区分 |
| Redis data-structure / event-loop | 对象类型与编码分开；SDS、rehash、listpack、quicklist 和跳表只保留机制；网络 I/O 并行不等于命令并行 |
| Redis memory / persistence | 过期与淘汰分开；COW 的工作机制与容量预算分别考察，旧 AOF 文件流程不套用到 7.x |
| Redis replication / sentinel / cluster | 区分复制历史与进度、下线判断与授权、复制与分片；不承诺无损故障转移 |
| Redis cache / engineering | 三类缓存故障合为一张区别卡，再保留有边界价值的场景；Pipeline、事务和租约锁不混同 |

跨来源合并的具体例子：索引综述与 page.md 的聚簇/二级区别；事务文章与日志文章的版本链；锁总览与加锁案例的 gap/next-key 机制；Redis 总览与持久化专篇的 AOF/RDB；总览与 strategy.md 的淘汰；总览与 cache_problem.md 的缓存故障。合并发生于规划阶段，没有删除已有卡片。

全局程序检查未发现重复 ID、相同题干、相同规范化问答或完全相同文件。内容复核未发现需要再合并的同目标卡；这属于语义审查判断，不是可证明的零冗余保证。未虚构“原有多少张、删除多少张”的压缩统计。

## 自动校验与原始资料保护

使用 PyYAML 6.0.3 实际解析全部 Front Matter；执行 `python3 anki-cs/validate.py` 检查：字段结构与枚举、ID/文件名、来源真实且位于输入目录、标题数量与顺序、非空问答、重复、地图 ID 及状态一致性、报告统计一致性。最终结果：通过。

开始时不存在 anki-cs 卡片；本次新建独立文件，未覆盖历史卡片，没有人工修改冲突。生成助手采用“已有文件内容不同即停止并保留”的策略；最终目录未留生成框架。未来重跑仍需人工/代理识别编辑，不能声称已实现通用自动三方合并。

在任务开始时记录 CS-Base 全部非 Git 文件 SHA-256；结束时重新计算，125 个文件的路径集合及哈希完全一致。MySQL/Redis 输入集合摘要（对排序后的路径→SHA-256 映射作 JSON 编码再 SHA-256）：

`0bf90079ec1240115d6564cdeec8ccc901da22f9e2e732f2c842d42f075504b7`

格式检查不等于技术验证；本次未运行 MySQL/Redis 实例、并发 SQL 实验、故障注入、性能基准或 Anki 导入测试。

## 技术准确性审查与官方补证

审查采用本地来源核对与必要的官方文档/7.0 分支源码补查，未进行逐行数据库内核源码证明。在线 latest 文档只用于与 7.x 相符的稳定语义，不把后续版本新特性写入基线。

| 核查事项 | 实际参考与处理 |
|---|---|
| RR 快照时机与自身修改 | [MySQL 8.0 一致性读](https://dev.mysql.com/doc/refman/8.0/en/innodb-consistent-read.html)：BEGIN 不等于普通首次快照建立时点，自身写入可见 |
| 旧版本保留与覆盖边界 | [MySQL 8.0 多版本](https://dev.mysql.com/doc/refman/8.0/en/innodb-multi-versioning.html)：长快照影响 purge；列覆盖不是所有底层场景绝不查聚簇记录的保证 |
| 锁范围与 RC 例外 | [InnoDB 锁](https://dev.mysql.com/doc/refman/8.0/en/innodb-locking.html)、[语句加锁](https://dev.mysql.com/doc/refman/8.0/en/innodb-locks-set.html)：保留完整唯一键与隔离级别条件 |
| 超时回滚范围 | [8.0 参数手册](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/innodb-parameters.html)：修正本地“等待超时回滚事务”的宽泛说法 |
| checkpoint 与恢复 | [检查点](https://dev.mysql.com/doc/refman/8.0/en/innodb-checkpoints.html)、[崩溃恢复](https://dev.mysql.com/doc/refman/8.0/en/innodb-recovery.html)：区分刷脏推进与未提交事务回滚 |
| Redis 7.0 编码与网络线程 | [quicklist.h](https://raw.githubusercontent.com/redis/redis/7.0/src/quicklist.h)、[t_list.c](https://raw.githubusercontent.com/redis/redis/7.0/src/t_list.c)、[listpack.c](https://raw.githubusercontent.com/redis/redis/7.0/src/listpack.c)、[redis.conf](https://raw.githubusercontent.com/redis/redis/7.0/redis.conf)：分块可有 plain 节点，不把配置示例 io-threads 4 当默认值 |
| 多文件 AOF | [7.0 aof.c](https://raw.githubusercontent.com/redis/redis/7.0/src/aof.c)：BASE/INCR/manifest 替代旧版重写缓冲区拼接描述；不再把混合持久化写成必然同一个文件 |
| 复制身份与缓冲 | [复制文档](https://redis.io/docs/latest/operate/oss_and_stack/management/replication/)、[7.0 replication.c](https://raw.githubusercontent.com/redis/redis/7.0/src/replication.c)：replid 不等于进程 run ID，副本与 backlog 可共享缓冲块 |
| Sentinel 与 Cluster | [哨兵文档](https://redis.io/docs/latest/operate/oss_and_stack/management/sentinel/)、[Cluster 规范](https://redis.io/docs/latest/operate/oss_and_stack/reference/cluster-spec/)：区分 quorum/多数派，补证多键同槽限制与异步复制边界 |
| 事务与脚本 | [事务文档](https://redis.io/docs/latest/develop/using-commands/transactions/)、[Lua 说明](https://redis.io/docs/latest/develop/programmability/eval-intro/)：补证 WATCH、错误阶段与不被穿插的执行语义 |

核验过程中旧持久化 URL 部分正文抓取为空，因此 AOF 7.0 文件组织的补证最终以实际可读的版本源码与配置为依据，未把空页面算作完整核验。

## 未覆盖内容与需人工复核事项

知识地图保留两个 uncovered 的 P1 单元：

- `mysql-advanced-buffer-gap`：Doublewrite、Change Buffer、AHI 仅有待写提示，未据模型记忆制卡。
- `mysql-ha-gap`：GTID、半同步复制与完整故障切换协议缺少充分本地展开；本版只覆盖 binlog 异步复制链路。

其他范围限制：Redis Cluster 专篇为空，本版仅由总览与官方资料支持基础分片/同槽目标，迁槽、MOVED/ASK 状态机不在覆盖承诺内。历史编码阈值、命令全集、布局字节、完整加锁端点枚举等已列为 skipped。

人工复核建议：涉及精确锁端点的拓展题需在指定 8.0 小版本与执行计划下复现实验；更新到具体 Redis 7.x 小版本前检查 List/Set 编码路径变化；部署时核对日志策略、存储刷盘语义及故障模型。上述运行行为本次未实验核实，不能把卡片当成部署安全性证明。没有把未确认的高级协议写成已核实卡片。

## 颗粒度与维护评价

115 张卡片围绕 27 个已覆盖单元组织，保留 6 张综合流程卡；机制、比较和权衡是主体。所有 Answer 均不超过 150 个字符（含标记与空白），没有靠冗长 Extra 隐藏必答信息。三个链表、可见性规则等保留为一个可整体评分的结构，避免拆成低信息量事实。

实际复习耗时尚未测量，个别算法/步骤卡可能超过 30 秒；应在真实复习中依据可评分性调整。修订保留 ID，不因答错而立即扩增同义卡。后续优先补足地图缺口，不以总张数为目标。

## 可重算统计快照

下列 JSON 由实际卡片和知识地图统计得到，校验器会重新计算并逐项比对。

<!-- stats -->
```json
{
  "source_files": {
    "mysql": 22,
    "redis": 13
  },
  "knowledge_units": 39,
  "unit_priority": {
    "P0": 20,
    "P1": 13,
    "P2": 6
  },
  "coverage": {
    "covered": 27,
    "skipped": 10,
    "uncovered": 2
  },
  "cards": 115,
  "domain": {
    "mysql": 60,
    "redis": 55
  },
  "topic": {
    "mysql/buffer-pool": 4,
    "mysql/index": 17,
    "mysql/lock": 11,
    "mysql/logging": 9,
    "mysql/query": 3,
    "mysql/replication": 2,
    "mysql/storage": 4,
    "mysql/transaction": 10,
    "redis/cache": 7,
    "redis/cluster": 3,
    "redis/data-structure": 12,
    "redis/engineering": 8,
    "redis/event-loop": 3,
    "redis/memory": 4,
    "redis/persistence": 9,
    "redis/replication": 5,
    "redis/sentinel": 4
  },
  "type": {
    "application": 23,
    "comparison": 29,
    "concept": 0,
    "mechanism": 37,
    "synthesis": 6,
    "tradeoff": 20
  },
  "card_priority": {
    "P0": 91,
    "P1": 24
  }
}
```
