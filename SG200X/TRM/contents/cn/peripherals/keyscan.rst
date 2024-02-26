按键扫描
--------

概述
~~~~

Keyscan 最多支援 8 x 8 = 64 个按键的矩阵。若按键不需要这么多，能自由决定要 mask 掉或保留哪些 row 或 column。视软件需要可以选用 snapshot 模式及 FIFO 模式来取得按键资讯。

工作方式
~~~~~~~~

.. _diagram_keyscan_construction:
.. figure:: ../../../../media/image136.png
	:align: center

	Keyscan 架构框图

状态机 (FSM) 在休息模式(没有按下任何键)时, 所有的 row 都输出 0, 而 col 都是输入模式并开启弱上拉 (弱上拉的设定在 ioblk 相映的寄存器, 不在 keyscan模块)。当任何一个按键被按下时, col 端经过 debounce 后会看到非全 1 的值，说明有按键被按着。这时 FSM 会启动一次扫描，依序让 Row [0] -> Row[7] 一次只有一个 bit 输出 0 (其余都在HiZ 高阻态)。每次的结果会更新入一个 array 中。

FSM 会不断的循环扫描, 直到所有 row 扫回的 col 又都是全 1 表示己没有按着的按键, 才会又会到休息模式下 (所有 row 输出 0)。

基本设定
~~~~~~~~

KEYSCAN0 里的 reg_row_mask, reg_col_mask 及 reg_enable 是当没有使用到 8x8 的矩阵时, 可以选择性把某些 IO 档掉, 不输出, 也不参考其输入。Default 是全关的。所以需要打开。KEYSCAN_CONFIG2 里的 reg_db_col 决定了 column input 需要经过多少时间的 debounce 才可以使用。

KEYSCAN_CONFIG1 里的 reg_slow_div 决定了 IP 的 FSM 每个 stage 在停留的时间。要记得这个数字一定要比 debounce 的时间大，不然 IO 上转态后未完成 debounce 就进行判读会错乱。

KEYSCAN_CONFIG3 里的 reg_wait_cntr 则可以用来降低扫描速度.因为只要按键按着, keyscan 模块就会不停的作扫描。这个 counter 可以控制在每次启动新一轮扫描前, 固定等待一定的时间，以减低扫描频率。

使用 FIFO 模式
~~~~~~~~~~~~~~

使用 FIFO 模式时, IP 每次扫进来的 64 个按键值会存在 array 里。每次只要有任何一个 key 的状态与上一次扫描内容不一样, 他就会把这个 key 的 index 及当下的值 (0/1) push 进 FIFO 内。所以 [5:0] 里的数字指定了是哪一个按键。 [6] 表明是按下 (0) 或是放开 (1) 。当 FIFO 不为空时, 就会发出 IRQ。这个模式的优点是省略掉软件一个一个 bit 作检查是哪个 bit 有改变的复锁工作。缺点是 KEY_SCAN_FIFO 是个 read 会自动 pop 的 register, 要小心操作。

打开 KEYSCAN_IRQ_ENABLE 的 reg_irq_fifo_not_empty_enable 收到 IRQ 后, 读取 KEYSCAN_IRQ_FLAG 里的 reg_irq_fifo_not_empty, 然后检查 KEYSCAN_FIFO_STATUS 的 reg_fifo_not_empty。则开始 read KEYSCAN_FIFO 里的内容。直到清干净后, 再把 KEY_SCAN_IRQ_CLEAR 清掉，结束 IRQ retine。

使用 snapshot array 模式
~~~~~~~~~~~~~~~~~~~~~~~~

使用 snapshot array 时, IP 内会目前扫进来的 64 按键的值存在一个 array 里。若这个 array 的内容与 KEYSCAN_SNAPSHOT_ARRAY 内容不一样，就会发 IRQ。而软件可以触发 KEYSCAN_SNAPSHOT_TRIG, 把当前的 array 内容捉到 snapshot array 后, 再慢慢比对甚么内容与之前的认知有改变。

打开 KEYSCAN_IRQ_ENABLE 的 reg_irq_snapshot_change_enable，收到 IRQ 后, 读取 trigger KEYSCAN_SNAPSHOT_TRIG, 然后解读 KEYSCAN_SNAPSHOT_ARRAY 的内容。再把 KEY_SCAN_IRQ_CLEAR 清掉，结束 IRQ retine。

Key scan 寄存器概览
~~~~~~~~~~~~~~~~~~~

.. 此表甚小，不再文件 include

.. _table_keyscan_register_overviews:
.. table:: Key scan Registers Overview
	:widths: 4 3 4

	+----------------------+---------+------------------------------------+
	| Name                 | Address | Description                        |
	|                      | Offset  |                                    |
	+======================+=========+====================================+
	| KEYSCAN_CONFIG0      | 0x000   |                                    |
	+----------------------+---------+------------------------------------+
	| KEYSCAN_CONFIG1      | 0x004   |                                    |
	+----------------------+---------+------------------------------------+
	| KEYSCAN_CONFIG2      | 0x008   |                                    |
	+----------------------+---------+------------------------------------+
	| KEYSCAN_CONFIG3      | 0x00c   |                                    |
	+----------------------+---------+------------------------------------+
	|KEYSCAN_SNAPSHOT_ARRAY| 0x014   |                                    |
	+----------------------+---------+------------------------------------+
	| KEYSCAN_SNAPSHOT_TRIG| 0x01c   |                                    |
	+----------------------+---------+------------------------------------+
	| KEYSCAN_FIFO_STATUS  | 0x020   |                                    |
	+----------------------+---------+------------------------------------+
	| KEYSCAN_FIFO         | 0x024   |                                    |
	+----------------------+---------+------------------------------------+
	| KEYSCAN_IRQ_ENABLE   | 0x028   |                                    |
	+----------------------+---------+------------------------------------+
	| KEYSCAN_IRQ_FLAG     | 0x02c   |                                    |
	+----------------------+---------+------------------------------------+
	| KEYSCAN_IRQ_CLEAR    | 0x030   |                                    |
	+----------------------+---------+------------------------------------+

Key scan 寄存器描述
~~~~~~~~~~~~~~~~~~~

.. include:: ./keyscan_registers_description.table.rst
