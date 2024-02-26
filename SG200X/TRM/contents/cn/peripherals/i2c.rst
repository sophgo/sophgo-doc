I2C
---

概述
~~~~

本芯片配置 5 个 I2C 控制器, 可个别配置为 Master/Slave。IO 配置需参考 Function pin mux 做配置。

功能描述
~~~~~~~~

I2C 控制器具有以下功能特点：

- 支持标准地址 (7bit) 和扩展地址 (10bit)。

- 传输速率支持标准模式 (100kbit/s) 和快速模式 (400kbit/s)。

- 支持 General Call 和 Start Byte 功能。

- 不支持 CBUS 器件。

- 支持 DMA 操作。

- 支持 64 x 8bit 的 TX FIFO 和 64 x 8bit 的 RX FIFO。

功能框图
~~~~~~~~

:ref:`diagram_i2c_function_graph` 为 I2C 模块之功能框图。IIC_CLK 为模块时钟，芯片支持可配 25MHz 或 100MHz。CPU 通过 APB 总线配置寄存器以选择 I2C 各模式与时序，写 TXFIFO、读 RXFIFO，并触发 FSM 以发送、接收 SDA/SCL 相关 IO 信号。System DMA 亦可搭配 I2C。 DMA_IF，并通过 APB 总线写 TXFIFO、读 RXFIFO，以发送、接收 I2C信号。

.. _diagram_i2c_function_graph:
.. figure:: ../../../../media/image90.png
	:align: center

	I2C 功能框图

I2C 协议时序
~~~~~~~~~~~~

芯片 I2C 支持一般标准之 I2C 协议时序如 :ref:`diagram_i2c_time_sequence` 所示。

.. _diagram_i2c_time_sequence:
.. figure:: ../../../../media/image91.png
	:align: center

	I2C 协议时序

工作方式
~~~~~~~~

配置 I2C 时钟与时序参数
^^^^^^^^^^^^^^^^^^^^^^^

1. CLK_DIV CRG 寄存器章节，配置 clk_byp_0_31 可以选择 IIC_CLK 为 25MHz 预设时钟源或 100MH z时钟源。

2. 配置相关时序配置需要在模块不使能状态。需将 IC_ENABLE 设置为 0, 并查询 IC_ENABLE_STATUS[0] 确定为 0。

3. 参照表格 :ref:`table_i2c_register_relationship`，按 I2C 时钟选择，配置 I2C 时序计数寄存器。

.. 这个表格比较小，就不单独放文件 include 了

.. _table_i2c_register_relationship:
.. table:: I2C clock selection and related register configuration relationship table
	:widths: 2 2 2 4

	+-------------+-----------+-----------+------------------------------+
	| Register    | 25M       | 100M      | Description                  |
	|             | IIC_CLK   | IIC_CLK   |                              |
	+=============+===========+===========+==============================+
	| IC_SS\      | 115       | 460       | SCL high level time counting |
	| _SCL_HCNT   |           |           | in standard speed mode       |
	+-------------+-----------+-----------+------------------------------+
	| IC_SS\      | 135       | 540       | SCL low level time counting  |
	| _SCL_LCNT   |           |           | in standard speed mode       |
	+-------------+-----------+-----------+------------------------------+
	| IC_FS\      | 21        | 90        | SCL high level time counting |
	| _SCL_HCNT   |           |           | in fast speed mode           |
	+-------------+-----------+-----------+------------------------------+
	| IC_FS\      | 42        | 160       | SCL low level time counting  |
	| _SCL_LCNT   |           |           | in fast speed mode           |
	+-------------+-----------+-----------+------------------------------+
	| IC_SDA_HOLD | 1         | 1         | SDA hold time count, relative|
	|             |           |           | to SCL negative edge         |
	+-------------+-----------+-----------+------------------------------+
	| IC_SDA_SETUP| 6         | 25        | SDA time count, relative to  |
	|             |           |           | the positive edge of SCL     |
	+-------------+-----------+-----------+------------------------------+
	| IC_FS_SPKLEN| 2         | 5         | I2C glitch suppression time  |
	|             |           |           | count                        |
	+-------------+-----------+-----------+------------------------------+

非 DMA 方式下的数据传输
^^^^^^^^^^^^^^^^^^^^^^^

.. _diagram_i2c_nodma_software_process:
.. figure:: ../../../../media/image92.png
	:align: center

	I2C 非 DMA 方式下的数据传输软件流程

DMA 方式下的数据传输
^^^^^^^^^^^^^^^^^^^^

.. _diagram_i2c_dma_software_process:
.. figure:: ../../../../media/image93.png
	:align: center

	I2C DMA 方式下的数据传输软件流程

.. _section_i2c_register_overview:

I2C 寄存器概览
~~~~~~~~~~~~~~

包括 6 个 I2C, 5 个 Active Domain，1 个 No-die Domain。其基地址分别如下。每个 I2C 由一组控制寄存器组成，每组定义相同。

.. include:: ./i2c_registers_overview.table.rst

I2C 寄存器描述
~~~~~~~~~~~~~~

.. include:: ./i2c_registers_description.table.rst
