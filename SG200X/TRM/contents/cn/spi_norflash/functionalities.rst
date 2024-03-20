功能描述 
---------

接口描述
~~~~~~~~

SPI NOR Flash 控制器 可以支持三种 SPI NOR 接口类型，类型分别为 Standard SPI、Dual SPI 接口模式及 Qual SPI 接口模式。

Standard SPI 接口模式
^^^^^^^^^^^^^^^^^^^^^

Standard SPI 接口模式具有 1bit 数据输入线和 1bit 数据输出线。图表为 Standard SPI 接口模式写操作时序图，为 Standard SPI 接口模式读操作时序图。

.. _diagram_standard_spi_write_sequence:
.. figure:: ../../../../media/image17.png
	:align: center

	Standard SPI 接口模式写操作时序图

时序说明：

- command/address/dummy cycles 以单 bit 串行方式在 DO 线上输出。

- Data 以单 bit 串行方式在 DO 线上输出。

.. _diagram_standard_spi_read_sequence:
.. figure:: ../../../../media/image19.png
	:align: center

	Standard SPI 接口模式读操作时序图

时序说明：

- command/address/dummy cycles 以单 bit 串行方式在 DO 线上输出。

- Data 以单 bit 串行方式在 DI 线上输入。

Dual-Input SPI 接口模式
^^^^^^^^^^^^^^^^^^^^^^^

Dual Input SPI 接口模式，数据输入阶段并行 2bit 数据线。:ref:`diagram_dual_input_spi_sequence` 为 Dual Input SPI 接口模式操作时序图。

.. _diagram_dual_input_spi_sequence:
.. figure:: ../../../../media/image21.png
	:align: center

	Dual-Input SPI 接口时序

时序说明：

- Command/address/dummy cycles 以单 Bit 串行方式在 DO 线上输出。

- Data 以 2 Bits 方式在 DO/DI 线上或输入（读）。

Dual-IO SPI 接口模式
^^^^^^^^^^^^^^^^^^^^

Dual IO SPI 接口模式， 地址输出、数据输入阶段并行 2bit 数据线。:ref:`diagram_dual_io_spi_sequence` 为 Dual IO SPI 接口模式操作时序图。

.. _diagram_dual_io_spi_sequence:
.. figure:: ../../../../media/image23.png
	:align: center

	Dual-IO SPI 接口时序

时序说明：

- Command 以单 Bit 串行方式在 DO 线上输出。

- address/dummy cycles/Data以 2 Bits方式在 DO/DI 线上输出（写）或输入（读）。

Quad-Input SPI 接口模式
^^^^^^^^^^^^^^^^^^^^^^^

Quad Input SPI接口模式，数据输入阶段并行4bit数据线。:ref:`diagram_quad_input_spi_sequence` 为 Quad Input SPI 接口模式操作时序图。

.. _diagram_quad_input_spi_sequence:
.. figure:: ../../../../media/image24.png
	:align: center

	Quad-Input SPI 模式时序图

时序说明：

- Command/address/dummy cycles 以单 Bit 串行方式在 DO 线上输出。

- Data以4 Bits 方式在 DO/DI/WPN/HOLDN 输入（读）。

Quad-IO SPI 接口模式
^^^^^^^^^^^^^^^^^^^^

Quad IO SPI 接口模式， 地址输出、数据输入阶段并行 4bit 数据线。:ref:`diagram_quad_io_spi_sequence` 为 Quad IO SPI 接口模式操作时序图。

.. _diagram_quad_io_spi_sequence:
.. figure:: ../../../../media/image26.png
	:align: center

	Quad-IO SPI 模式时序图

时序说明：

- Command 以单 Bit 串行方式在 DO 线上输出。

- address/dummy cycles/Data 以 4 Bits 方式在 DO/DI/WPN/HOLDN 输出（写）或输入（读）。

Boot 功能
~~~~~~~~~

SPI NOR Boot 数据位于芯片地址 0x1000_0000~0x1FFF_FFFF,  直接映射到 SPI NOR Flash 的连续地址空间 0x0000_0000~0x0FFF_FFFF。SPI_NOR Flash最大可支持到 256MB, 其中若需使用大于 16MB SPI_NOR Flash ，需利用到 4 bytes 地址模式。芯片复位状态为 3bytes 地址模式，需通过配置使能 4bytes 地址模式，故 SPI_NOR Flash 需要能支持 3bytes/4bytes 地址模式。

寄存器操作
~~~~~~~~~~

软件配置操作相关寄存器, 如操作命令、地址等, 最后配置reg_go_busy寄存器下发操作, 控制器根据软件配置值，下发操作给器件。

DMA 操作
~~~~~~~~

- DMMR 读模式

  在 SPI_NOR Flash Controller 处于 DMMR 模式下，SPI_NOR Flash 空间直接映射至芯片地址空间0x1000_0000~0x1FFF_FFFF。系统 DMA 可使用 memory-to-memory 模式，将 SPI_NOR 数据搬移至 DDR。

- Non-DMMR 读写模式

  指令、地址和数据都需通过 FF_PORT 发送接收。需配置控制器寄存器选择读指令、写指令、指令长度、数据长度后通过 CPU 或 DMA 写 FF_PORT 以发出指令及地址，通过写、读 FF_PORT 以发送、接收数据。