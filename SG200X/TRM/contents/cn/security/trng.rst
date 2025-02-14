TRNG
----

概述
~~~~

真随机数生成器 (True Random Number Generator，简称 TRNG) 生成的随机数在统计上等同于均匀分布的随机数据流。该电路包括一个确定性随机位生成器 (Deterministic Random Bit Generator，简称 DRBG)。当创建种子并将其输入到 DRBG 中时，TRNG 会生成随机数。

功能特性
~~~~~~~~

TRNG 模块具有以下功能特点：

- 内部随机种子操作
- 128 位随机数生成
- 128 位安全强度

工作方式
~~~~~~~~

循环测试 STAT.BUSY，直到它空闲。

将 GEN_NOISE 写入 CTRL.CMD，从噪声中生成全熵种子。

循环测试 ISTAT.DONE，直到上一个命令完成。

通过将 1 写入 ISTAT.DONE 来清除它。

将 CREATE_STATE 写入 CTRL.CMD，将 DRBG 移至创建状态。

循环测试 ISTAT.DONE，直到上一个命令完成。

通过将 1 写入 ISTAT.DONE 来清除它。

将 GEN_RANDOM 写入 CTRL.CMD，生成随机数。

循环测试 ISTAT.DONE，直到上一个命令完成。

通过将 1 写入 ISTAT.DONE 来清除它。

从 RAND0 读取第一个随机数据 WORD。

从 RAND1 读取第二个随机数据 WORD。

从 RAND2 读取第三个随机数据 WORD。

从 RAND3 读取第四个随机数据 WORD。

TRNG 寄存器概览
~~~~~~~~~~~~~~~~~~~~

.. include:: ./trng_registers_overview.table.rst

TRNG 寄存器描述
~~~~~~~~~~~~~~~~~~~~

(基址 0x02070000)

.. include:: ./trng_registers_description.table.rst
