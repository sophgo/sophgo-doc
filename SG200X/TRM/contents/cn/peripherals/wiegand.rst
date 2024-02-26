Wiegand
-------

概述
~~~~

.. _diagram_wiegand_trasfer:
.. figure:: ../../../../media/image137.png
	:align: center

	wiegand 信号总线传输 0/1 的方式

Wiegand 接口使用两根单端的信号, D0/D1。当总线 idle 时都是 high, 在 D0 上出现一个 low pulse 表示传送了一个 ”0”, 在 D1 上发现 low pulse, 就是传送一个 “1”。

Wiegand 常用在门禁系统上, 有两种常用 format, Wiegand 26/34, 分别代表封包的 bit 数。这两种 format 简介如下。

Wiegand 26
^^^^^^^^^^

.. _diagram_wiegand26_format:
.. figure:: ../../../../media/image138.png
	:align: center

	Wiegand 26 格式

Wiegand 34
^^^^^^^^^^

.. _diagram_wiegand_34_format:
.. figure:: ../../../../media/image139.png
	:align: center

	Wiegand 34 format

F = Facility Code

U = User code

有些门禁卡背后有一串数字, 把他转成 hex 后,

Dec 0002262506   Hex : 22_85_EA

0x22 是他的 Facility code (Dec = 34)

0x85EA 是他的 user code (Dec = 34282)

.. _diagram_wiegand_meaning:
.. figure:: ../../../../media/image140.png
	:align: center

	常见的磁卡, 磁扣的数字意义

后面看到的 34, 34282 是拆开后重新用十进制表示的 Facility code & user code。

注: 本 IP TX RX 均不处理 parity 的 insert 或 checking，均由软件处理。

工作方式
~~~~~~~~

.. _diagram_wiegand_block:
.. figure:: ../../../../media/image141.png
	:align: center

	wiegand 架构框图

Wiegand 模块包含 TX 和 RX, 可单向或双向使用。自己 TX 出去的时候, RX 会挡住不看，所以 RX 不会收到自己发出去的信号。而 TX 支持 push pull mode 或是 open drain mode。

TX
^^

TX 前, 设好 TX 的 high time 和 low time, packet 的bit 数, 是由 MSB 1\ :sup:`st` or LSB 1\ :sup:`st`。然后把 data 放在 TX_BUFFER 寄存器后, 用 TX_TRIG 把 data 发出去。

TX 完整传输结束后, 可以靠 TX finish 的中断, 或是 polling TX_BUSY 的 status 来确定甚么时候可以发送下一个 packet。

RX
^^

RX 前, 设定好 debounce time, 预期接收 packet 的 bit 数。当 D0 D1 出现 low pulse 时, RX 即开始把 data push 进 temp buffer 中。当接收到 bit 数达到一个 packet 的预期 bit 数时, 会把 temp buffer 推到 RX_BUFFER 中, 发出中断, 请软件处理。而 temp buffer 则继续接收下一笔 data。

如果 D0 D1 上出现 idle timeout 时, 即使 bit 数未到, 也会强迫视为一个 packet。

RX BUFFER 的高位元会记录这个 packet 一共收到的 bit 数, 是否是因为 timeout 造成的, 或是在软件读取前, 有发生 overflow。

每收到一个 packet, 可以靠 rx_buffer_rececived 的中断, 或是 RX_BUFFER_VALID 来判定 RX_BUFFER 中是否有有效的 data。RX Data 取走之后, 再 trigger RX_BUFFER_CLEAR 去清空 RX_BUFFER以接收下一个 packet。

Wiegand 寄存器概览
~~~~~~~~~~~~~~~~~~

.. 此表甚小，不再文件 include

.. _table_wiegand_registers_overviews:
.. table:: Wiegand Registers Overview
	:widths: 3 3 4

	+----------------------+---------+------------------------------------+
	| Name                 | Address | Description                        |
	|                      | Offset  |                                    |
	+======================+=========+====================================+
	| TX_CONFIG0           | 0x000   |                                    |
	+----------------------+---------+------------------------------------+
	| TX_CONFIG1           | 0x004   |                                    |
	+----------------------+---------+------------------------------------+
	| TX_CONFIG2           | 0x008   |                                    |
	+----------------------+---------+------------------------------------+
	| TX_BUFFER            | 0x00c   |                                    |
	+----------------------+---------+------------------------------------+
	| TX_TRIG              | 0x014   |                                    |
	+----------------------+---------+------------------------------------+
	| TX_BUSY              | 0x018   |                                    |
	+----------------------+---------+------------------------------------+
	| TX_DEBUG             | 0x01c   |                                    |
	+----------------------+---------+------------------------------------+
	| RX_CONFIG0           | 0x020   |                                    |
	+----------------------+---------+------------------------------------+
	| RX_CONFIG1           | 0x024   |                                    |
	+----------------------+---------+------------------------------------+
	| RX_CONFIG2           | 0x028   |                                    |
	+----------------------+---------+------------------------------------+
	| RX_BUFFER            | 0x02c   |                                    |
	+----------------------+---------+------------------------------------+
	| RX_BUFFER_VALID      | 0x038   |                                    |
	+----------------------+---------+------------------------------------+
	| RX_BUFFER_CLEAR      | 0x03c   |                                    |
	+----------------------+---------+------------------------------------+
	| RX_DEBUG             | 0x040   |                                    |
	+----------------------+---------+------------------------------------+
	| IRQ_ENABLE           | 0x044   |                                    |
	+----------------------+---------+------------------------------------+
	| IRQ_FLAG             | 0x048   |                                    |
	+----------------------+---------+------------------------------------+
	| IRQ_CLEAR            | 0x04c   |                                    |
	+----------------------+---------+------------------------------------+

Wiegand 寄存器描述
~~~~~~~~~~~~~~~~~~

.. include:: ./wiegand_registers_description.table.rst
