功能描述
~~~~~~~~

接口描述
^^^^^^^^

SPI NAND Flash 控制器 可以支持三种 SPI NAND 接口类型，类型分别为 Standard SPI、X2 接口模式及 X4 接口模式。

Standard SPI 接口模式
'''''''''''''''''''''

Standard SPI 接口模式具有 1bit 数据输入线和 1bit 数据输出线。图表 :ref:`diagram_std_spi_write_sequence` 为 Standard SPI 接口模式写操作时序图，图表 :ref:`diagram_std_spi_read_sequence` 为 Standard SPI 接口模式读操作时序图。

.. _diagram_std_spi_write_sequence:
.. figure:: ../../../../media/image17.png
	:align: center

	Standard SPI 接口模式写操作时序

时序说明：

- command/address/dummy cycles 以单 bit 串行方式在 DO 线上输出。

- Data 以单 bit 串行方式在 DO 线上输出。

.. _diagram_std_spi_read_sequence:
.. figure:: ../../../../media/image19.png
	:align: center

	Standard SPI 接口模式读操作时序

时序说明：

- command/address/dummy cycles 以单bit串行方式在DO 线上输出。

- Data 以单 bit 串行方式在 DI 线上输入。

X2 接口模式
'''''''''''

X2 接口模式共用 2bit 数据输入输出输出线。图表 :ref:`diagram_spi_x2_operate_sequence` 为 X2 接口模式操作时序图。

.. _diagram_spi_x2_operate_sequence:
.. figure:: ../../../../media/image21.png
	:align: center

	SPI Nand x2 接口模式操作时序

时序说明：

- command/address/dummy cycles 以单 Bit 串行方式在 DO 线上输出。

- Data 以 2 Bits 方式在 DO/DI 线上输出（写）或输入（读）。

X4 接口模式
'''''''''''

X4 接口模式共用 4bit 数据输入输出输出线。图表 :ref:`diagram_spi_x4_operate_sequence` 为 X4 接口模式操作时序图。

.. _diagram_spi_x4_operate_sequence:
.. figure:: ../../../../media/image24.png
	:align: center

	SPI Nand x4 接口模式操作时序

时序说明：

- command/address/dummy cycles 以单 Bit 串行方式在 DO 线上输出。

- Data 以 4 Bits 方式在 DO/DI/WPN/HOLDN 线上输出（写）或输入（读）。

SPI NAND FLASH 地址说明
^^^^^^^^^^^^^^^^^^^^^^^

在下发 SPI NAND Flash 的读写操作时，操作时根据具体的操作下发行列地址。

- 写操作: 在 LOAD 操作时配置列地址, 在 PROGRAM 操作时配置行地址。

- 读操作：在 PAGE READ TO CACHE 操作时配置行地址，在 READ 操作时配置列地址。

- 地址下发由控制器完成，软件需要根据操作指令配置 reg_trx_cmd_idx, 及地址配置 reg_trx_cmd_cnt0、reg_trx_cmd_cnt1。

Boot 功能
^^^^^^^^^

由于 SPI NAND Flash 地址空间不连续且存在坏块的可能，因此 Boot 数据不能直接映射到 Flash 中。

支持自适应 Boot 功能，能够根据 Block0 的数据自动适配器件的信息。控制器要求物理 Block0 必须为好块，其他块为坏块则可以自动跳过。

寄存器操作
^^^^^^^^^^

软件配置操作相关寄存器，如操作命令、地址等，最后配置 reg_trx_start 寄存器下发操作，控制器根据软件配置值，下发操作给器件。如果还需要向器件传输数据，那会使用内部的 DMA 操作来传输数据。

内置 DMA 操作方式
^^^^^^^^^^^^^^^^^

支持使用内置系统 DMA 模式进行读写操作以提高访问速度。通过此种方式，可以通过总线直接访问片内或片外存储空间。

- 步骤 1: 配置 DMA 使用通道。

- 步骤 2: 配置来源及目标地址。

- 步骤 3: 配置传输格式及数据长度。

TIMEOUT 功能
^^^^^^^^^^^^

软件设置最大 1 秒 TIMEOUT 机制，做为器件无正常响应时之保护。

