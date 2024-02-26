SPI
---

概述
~~~~

系统配置 4 个 SPI 控制器模块, 可以作为 Master 与外部设备进行同步串行通信，实现数据的串并、并串转换。

特点
~~~~

SPI 控制器模块的特点如下 :

- 支持 Motorola SPI (全双工) 、TI SSP (全双工) 、NS MicroWire (半双工) 三种串行外设接口协议

- 独立的收/发 FIFO

- 可编程的数据帧长度: 4~16 bits

- SPI 接口时钟频率可编程

- 支持 DMA 操作模式

- 支持内部环回测试模式

- 工作参考时钟可设置为 187.5MHz 或 100MHz, 输出的 SPI_SCK 最大支持 46.875MHz

功能描述
~~~~~~~~

典型应用
^^^^^^^^

SPI master 对接外部 slave 时的应用框图如图表 :ref:`diagram_application_praph`

.. _diagram_application_praph:
.. figure:: ../../../../media/image98.png
	:align: center

	SPI 应用框图

工作方式
~~~~~~~~

工作模式
^^^^^^^^

SPI 的工作模式分为 :

- 中断或查询方式下的数据传输

- DMA 方式下的数据传输

时钟
^^^^

SPI 控制器模块参考时钟可设置为 187.5MHz 或 100MHz。

输出的 SPI_SCK 最大支持 46.875MHz。

计算方式如下：

输出的 SPI_SCK = SPI 工作参考时钟 /BAUDR

SPI 工作参考时钟 : 187.5MHz 或 100MHz。

BAUDR 寄存器 : 设置介于 2 到 65534 之间的偶数.

计算范例 :

SPI 工作参考时钟 = 187.5MHz 与 BAUDR =4

输出的 SPI_SCK = 187.5MHz/4 = 46.875MHz

中断处理
^^^^^^^^

SPI 控制器模块有 6 个中断，其中前 5 个是高电平有效的可屏蔽独立中断源。

- RXFINTR
  
  接收 FIFO 中断请求。当接收 FIFO 中有 RXFTLR+1 个或更多的有效数据时，该中断置位。

- RXOINTR

  当接收 FIFO 已满，且又有新的数据需要写入 FIFO 时，会引起 FIFO Overflow, 该中断置位。此时数据被写入接收移位寄存器，而不是 FIFO。

- RXUINTR

  当接收 FIFO 被读空，没有新的数据被写入接收 FIFO 之前又有新的读取请求发生，会引起 FIFO Underflow, 该中断置位。此时读取的值全部为 0。可以通过读寄存器 RXUICR 清除该中断。

- TXOINTR

  当发送 FIFO 已满，且又有新的数据需要写入 FIFO 时，会引起 FIFO Overflow, 该中断置位。

- TXEINTR

  发送 FIFO 中断请求。当发送 FIFO 中有 TXFTLR 个或更少的有效数据时，该中断置位。

- SPI_INTR

  组合中断，为以上 5 个中断经过“或”运算后的结果。 若要屏蔽此中断，必须设置寄存器 IMR 屏蔽上述 5 个中断。 如果上述 5 个独立中断中任意一个置位且使能，该中断置位。

初始化
^^^^^^

SPI 控制器模块初始化步骤如下：

- 步骤 1: 寄存器 SPIENR 设置 "0",  停止 SPI 模块。

- 步骤 2: 配置寄存器 BAUDR, 设定输出时钟分频除数，设定值必须为偶数。

- 步骤 3: 设置寄存器 CTRLR0, 配置传输数据位宽及传输帧格式等参数。

- 步骤 4: DMA 操作模式下，配置寄存器 DMACR, 启用 SPI 的 DMA 功能。操作于 DMA 模式时，应设置中断相关寄存器以禁止产生中断信号。

- 步骤 5: 中断操作模式下，设置寄存器 IMR, 以产生相应的中断信号。

- 步骤 6: 寄存器 SPIENR 设置 "1"，使能 SPI 模块。

SPI 的数据传输流程
^^^^^^^^^^^^^^^^^^

- SPI master 对接外部 SPI/SSP slave 时的流程如图表 :ref:`diagram_spissp_transmitting_form` 所示。

.. _diagram_spissp_transmitting_form:
.. figure:: ../../../../media/image99.png
	:align: center

	对接外部 SPI/SSP slave 时的数据传输流程

- SPI master 对接外部 Microwire slave 时的流程如图表 :ref:`diagram_microwire_process` 所示。

.. _diagram_microwire_process:
.. figure:: ../../../../media/image100.png
	:align: center

	对接外部 Microwire slave 时的数据传输流程


DMA 方式下的数据传输
^^^^^^^^^^^^^^^^^^^^

SPI 模块使用两个 DMA 通道，一个用于发送，一个用于接收。 SPI DMA 模式设置的相关寄存器有 DMACR、DMATDLR、DMARDLR。

启用 SPI DMA 模式的步骤如下：

- 步骤 1: 获取两个 DMA 通道。

- 步骤 2: 设置寄存器 DMACR [1:0]，使能 SPI DMA 发送接收。

- 步骤 3: 寄存器 SPIENR 设置“1”, 使能SPI。

- 步骤 4: 发送数据：

  1. 配置发送 DMA 通道相关的控制寄存器。

  2. 启动 DMA 控制器，响应 SPI 发送 FIFO 的请求。

  3. 通过 DMA 控制器中断上报，判断发送是否完成，如果完成则关闭 SPI 的发送 DMA 功能。

- 步骤 5: 接收数据：

  1. 配置接收 DMA 通道相关的控制寄存器。

  2. 启动 DMA 控制器，响应 SPI 接收 FIFO 的 DMA 请求。

  3. 通过 DMA 控制器中断上报，判断数据是否接收完成，如果完成则关闭 SPI 的接收 DMA 功能。

- 步骤 6: 寄存器 SPIENR 设置 "0"，停止 SPI。

三种串行外设总线时序图
~~~~~~~~~~~~~~~~~~~~~~

Motorola SPI 接口
^^^^^^^^^^^^^^^^^

以下各图表示 Motorola SPI 各种数据传输格式。其中 SCPH 代表 SPI_SCK 相位，SCPOL 代表 SPI_SCK 极性，通过寄存器 CTRLR0[7:6] 进行设置。

(A) SCPH = 0
||||||||||||

  此模式下, SPI_CS_X 处于空闲状态时设置为高电平, 传输时则设置为低电平。SPI_SCK 则是通过 SCPOL 设置而有所不同, SCPOL = 0, 处于空闲状态时设置为低电平, 传输时则以时钟的上升沿抓取数据, SCPOL = 1, 处于空闲状态时设置为高电平, 传输时则以时钟的下降沿抓取数据。

- 单帧传输格式如图表 :ref:`diagram_transmitting_form` 所示。

.. _diagram_transmitting_form:
.. figure:: ../../../../media/image101.png
	:align: center

	Motorola SPI 单帧传输格式 (SCPH = 0)

- 连续帧传输格式如图表 :ref:`diagram_serial_transmitting_form` 所示。

.. _diagram_serial_transmitting_form:
.. figure:: ../../../../media/image102.png
	:align: center

	Motorola SPI 连续帧传输格式 (SCPH = 0)

(B) SCPH = 1
||||||||||||

  此模式下, SPI_CS_X 处于空闲状态时设置为高电平, 传输时则设置为低电平。SPI_SCK 则是通过 SCPOL 设置而有所不同, SCPOL = 0, 处于空闲状态时设置为低电平, 传输时则以时钟的下降沿抓取数据, SCPOL = 1, 处于空闲状态时设置为高电平, 传输时则以时钟的上升沿抓取数据。

- 单帧传输格式如图表 :ref:`diagram_scphone_transform` 所示。

.. _diagram_scphone_transform:
.. figure:: ../../../../media/image103.png
	:align: center

	Motorola SPI 单帧传输格式 (SCPH = 1)

- 连续帧传输格式如图表 :ref:`diagram_scphone_sertransform` 所示。

.. _diagram_scphone_sertransform:
.. figure:: ../../../../media/image104.png
	:align: center

	Motorola SPI 连续帧传输格式 (SCPH = 1)

TI 同步串行接口
^^^^^^^^^^^^^^^

SSP 模式下, SPI_CS_X 处于空闲状态时设置为高电平, 传输时则设置为低电平。SPI_SCK 处于空闲状态时设置为低电平，传输时则以时钟的下降沿抓取数据。

以下各图表示 TI SSP 数据传输格式。

- 单帧传输格式如图表 :ref:`diagram_sspone_transform` 所示。

.. _diagram_sspone_transform:
.. figure:: ../../../../media/image105.png
	:align: center

	TI SSP 单帧传输格式


- 连续帧传输格式如图表 :ref:`diagram_sspone_sertransform` 所示。

.. _diagram_sspone_sertransform:
.. figure:: ../../../../media/image106.png
	:align: center

	TI SSP 连续帧传输格式

National Semiconductor Microwire 接口
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Microwire 模式下, SPI_CS_X 处于空闲状态时设置为高电平, 传输时则设置为低电平。SPI_SCK 处于空闲状态时设置为低电平，传输时则以时钟的上升沿抓取数据。

此模式在进行数据传输时, 必须先加控制字 (control word),外部芯片再根据控制字响应 Master 所需求的数据 (data word)。控制字长度可通过寄存器 CTRLR0[15:12] 进行设置, 其它相关参数可通过寄存器 MWCR 进行设置。

以下各图表示 NS Microwire 数据传输格式。

- 单帧传输格式如图表 :ref:`diagram_ns_microwire_oneframe_transform` 所示。

.. _diagram_ns_microwire_oneframe_transform:
.. figure:: ../../../../media/image106.png
	:align: center

	NS Microwire 单帧传输格式

- 连续帧传输格式如图表 :ref:`diagram_ns_microwire_continusframe_transform` 所示。

.. _diagram_ns_microwire_continusframe_transform:
.. figure:: ../../../../media/image107.png
	:align: center

	NS Microwire 连续帧传输格式

寄存器概览
~~~~~~~~~~

芯片的 4 组 SPI 模块基地址如表格 :ref:`table_spi_module_address` 所示。

.. 这个表格比较小，就不单独文件 include 了

.. _table_spi_module_address:
.. table:: Base addresses for 4 sets of SPI module
	:widths: 1 1

	+----------------------------------+----------------------------------+
	| GPIO Module                      | Base Address                     |
	+==================================+==================================+
	| SPI0                             | 0x04180000                       |
	+----------------------------------+----------------------------------+
	| SPI1                             | 0x04190000                       |
	+----------------------------------+----------------------------------+
	| SPI2                             | 0x041A0000                       |
	+----------------------------------+----------------------------------+
	| SPI3                             | 0x041B0000                       |
	+----------------------------------+----------------------------------+

表格 :ref:`table_spi0_register_overview` 是第 1 组 SPI 模块 (SPI0) 寄存器的偏移地址以及定义，SPI0 ~ SPI3 具有相同的寄存器定义。

.. include:: ./spi_registers_overview.table.rst

寄存器描述
~~~~~~~~~~

.. include:: ./spi_registers_description.table.rst
