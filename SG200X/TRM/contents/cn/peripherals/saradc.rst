SARADC
------

概述
~~~~

.. only:: sg2002

	SARADC 为模拟信号数字转换控制器。本芯片有最多 2 个 SARADC 控制器，每个提供 3 个独立通道。

.. only:: sg2000

	SARADC 为模拟信号数字转换控制器。本芯片有最多 2 个 SARADC 控制器，每个提供 6 个独立通道。

特点
~~~~

- 控制器工作频率 12.5MHz;

- 扫描频率不能高于 320K/s;

.. only:: sg2002

	- 12bit 采样精度, 3 个独立通道；

.. only:: sg2000

	- 12bit 采样精度, 6 个独立通道；

- 可一次触发三个信道依序扫描；

- 扫描完成自动上报中断;

工作方式
~~~~~~~~

.. only:: sg2002

	CPU 配置扫描信道，每个 SARADC 控制器可同时配置 3 个信道，启动 SARADC 进行通道扫描。通道扫描完成所有使能通道后, 通过中断通知系统扫描完成, CPU 可以获取转换结果。

.. only:: sg2000

	CPU 配置扫描信道，每个 SARADC 控制器可同时配置 6 个信道，启动 SARADC 进行通道扫描。通道扫描完成所有使能通道后, 通过中断通知系统扫描完成, CPU 可以获取转换结果。

.. _section_saradc_register_overview:

SARADC 寄存器概览
~~~~~~~~~~~~~~~~~

Active Domain 下 1 组，Base address：0x030F0000

No-die Domain 下 1 组（RTCSYS_SARADC），Base address：0x0502C000

每组寄存器定义相同，以 RTCSYS_SARADC 为例：

.. 该表格较小，不再文件 include

.. _table_rtcsys_saradc:
.. table:: Base address 0x0502C000
	:widths: 3 3 4

	+----------------------+---------+------------------------------------+
	| Name                 | Address | Description                        |
	|                      | Offset  |                                    |
	+======================+=========+====================================+
	| saradc_ctrl          | 0x004   | control register                   |
	+----------------------+---------+------------------------------------+
	| saradc_status        | 0x008   | staus register                     |
	+----------------------+---------+------------------------------------+
	| saradc_cyc_set       | 0x00c   | saradc waveform setting register   |
	+----------------------+---------+------------------------------------+
	| saradc_ch1_result    | 0x014   | channel 1 result register          |
	+----------------------+---------+------------------------------------+
	| saradc_ch2_result    | 0x018   | channel 2 result register          |
	+----------------------+---------+------------------------------------+
	| saradc_ch3_result    | 0x01c   | channel 3 result register          |
	+----------------------+---------+------------------------------------+
	| saradc_intr_en       | 0x020   | interrupt enable register          |
	+----------------------+---------+------------------------------------+
	| saradc_intr_clr      | 0x024   | interrupt clear register           |
	+----------------------+---------+------------------------------------+
	| saradc_intr_sta      | 0x028   | interrupt status register          |
	+----------------------+---------+------------------------------------+
	| saradc_intr_raw      | 0x02c   | interrupt raw status register      |
	+----------------------+---------+------------------------------------+

SARADC 寄存器描述
~~~~~~~~~~~~~~~~~

.. include:: ./saradc_registers_description.table.rst
