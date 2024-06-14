UART
----

概述
~~~~

UART (Universal Asynchronous Receiver Transmitter) 是一个非同步串行的通信接口, 主要功能是将来自外围设备的资料进行串并转换之后传入内部总线, 以及将资料进行并串转换之后输出到外部设备。UART 的主要功能是和外部芯片的 UART 进行对接，从而实现两芯片间的通信。

本芯片提供 5 个 UART 控制器，相关概述如下表。注意：使用前以具体的引脚输出定义为准。因为芯片不同的封装（QFN/BGA），某些功能可能未导出。引脚定义参考 :ref:`section_pinmux_pinctrl`。

.. 这个表比较小，就不单独文件 include 了

.. _table_uart_io_infodescribe:
.. table:: UART IO pin information
	:widths: 1 1

	+------------+-------------+
	| Controller | Mode        |
	+============+=============+
	| UART0      | 2-line UART |
	+------------+-------------+
	| UART1      |2/4-line UART|
	|            |             +
	|            |             |
	|            |             |
	+------------+-------------+
	| UART2      |2/4-line UART|
	|            |             +
	|            |             |
	|            |             |
	|            |             +
	|            |             |
	+------------+-------------+
	| UART3      |2/4-line UART|
	|            |             +
	|            |             |
	|            |             +
	|            |             |
	+------------+-------------+
	| UART4      | 2-line UART |
	|            |             +
	|            |             |
	+------------+-------------+

特点
~~~~

UART 模组有以下特点：

- 支持 64 x 8bit 的发送 FIFO 和 64 x 8bit 的接收 FIFO。

- 支持数据比特位和停止比特位的位宽可编程。数据比特位可通过程序设定为 5/6/7/8 比特。

- 停止位可通过编程设定为 1bit, 1.5bit 或 2bit。

- 支持奇、偶校验方式或者无校验。

- 支持传输速率可编程设置。

- 支持接收 FIFO 中断、发送 FIFO 中断、错误中断。

- 支持初始中断状态查询和 mask 后中断状态查询。

- 支持 DMA 操作。

功能描述
~~~~~~~~

应用框图
^^^^^^^^

UART 是一普遍通用之点对点物理层传输协议，可以用来对接各种系统，包含 PC、各种周边芯片，可作为芯片与芯片中间之沟通接口。

.. _diagram_uart_app_graph:
.. figure:: ../../../../media/image94.png
	:align: center

	UART 应用框图

功能原理
^^^^^^^^

- 波特率 (buad rate)

  由于 UART 接口没有参考时钟，属于异步传输方式，需要双方采用相同传输速度亦即波特率 (buadrate) 以进行沟通。若有误差，误差率需够小使不致误传。1 比特之速率称为波特率 (buadrate)。典型之波特率有 300, 1200, 2400, 9600, 19200, 38400, 115200bps 等。

- 帧结构 (frame structure)

  UART 传输数据结构以帧为单位。帧结构包含起始信号、资料信号、校验位元和结束信号。

.. _diagram_uart_transmitting_structure:
.. figure:: ../../../../media/image95.png
	:align: center

	UART 传输数据结构

- 起始信号（start bit）

  起始信号为一帧开始的标志。发动一个帧传输的最开头，就是在 TXD 上发送一低电平信号位。在 RXD 上，若在闲置状态接收到一低电平之信号位则判断为接收到一个侦传输之起始。

- 资料信号（data bit）

  资料位元宽可以根据不同的应用要求进行调整，可为 5/6/7/8 比特资料位元宽。典型为 8 比特资料位宽。

- 校验位元（parity bit）

  校验位元是 1 比特纠错信号，UART 的校验位元有奇数同位检查、偶校验和固定校验位，同时支持校验位的使能和禁止，详细描述请见 LCR 寄存器。

- 结束信号（stop bit）

  结束信号即帧的停止位元，支援 1 比特、 1.5 比特和 2 比特停止位元。发送一帧的结束信号就是把 TXD 发送高电平完成传输，进入闲置状态。接收一帧在计数到校验位元之后，需接收到结束信号。

工作方式
~~~~~~~~

波特率配置
^^^^^^^^^^

- UART 工作时钟 (UART_SCLK) 配置

  可参考 CLK_DIV CRG 寄存器描述，配置 clk_sel_0_9~ clk_sel_0_13 选择 uart0~uart4 的工作时钟。预设为 1: XTAL 25MHz，配置为 0 即选择 UART PLL 分频时钟源。 PLL 分频时钟源预设为 187.5MHz ，若有需要可以配置分频寄存器 div_clk_187p5m 调整 PLL 分频时钟为 1500/NMHz，最高达 187.5MHz。

- UART 波特率配置

  DLL、DLH 为 UART 控制器内部之波特率分频控制寄存器，DLH 为高 8 位、DLL 为低 8 位。配置 DLH、DLL 前须先配置 LCR[7] 为 1。此时可配置寄存器 RBR_THR_DLL(DLL)， IER_DLH(DLH)。

  配置完成后，波特率即设定完成，公式为：

  .. math:: Baud\ rate = \ \frac{UART\_ SCLK}{16*(256*DLH + DLL)}

- 以 UART SCLK 25MHz 为例，配置 115200 波特率，算式为：

  .. math:: (256*DLH + DLL) = \ \frac{25M}{16*115200} = 13.5

  若选择配置 DLL 为 14、DLH 为 0，则实际波特率为：

  .. math:: Baud\ rate = \ \frac{25M}{16*14} = 111607

  一比特时间误差为：

  .. math:: Bit\ Error = \ \frac{(115200 - 114286)}{115200} = 3.12\%

  累积一帧时间误差为：:math:`Frame\ Error = \ 3.12\%`\ \*10 = 31.2%

- 以 UART SCLK 187.5MHz 为例，配置 115200 波特率，算式为：

  .. math:: (256*DLH + DLL) = \ \frac{187.5M}{16*115200} = 101.7

  若选择配置 DLL 为 102、 DLH 为 0，则实际波特率为：

  .. math:: Baud\ rate = \ \frac{187.5M}{16*102} = 114890

  一比特时间误差为：

  .. math:: Bit\ Error = \ \frac{(115200 - 114890)}{115200} = 0.27\%

  累积一帧时间误差为：:math:`Frame\ Error = \ 3.12\%`\ \*10 = 2.7%

数据发送流程图
^^^^^^^^^^^^^^
.. _diagram_uart_send_process:
.. figure:: ../../../../media/image96.png
	:align: center

	UART 数据发送流程图

数据接收流程图
^^^^^^^^^^^^^^
.. _diagram_uart_receive_process:
.. figure:: ../../../../media/image97.png
	:align: center

	UART 数据接收流程图

中断或查询方式下的数据传输
^^^^^^^^^^^^^^^^^^^^^^^^^^

初始化步骤
''''''''''

1. 向 LCR[7] 写 1。使能配置 Divisor Latch Access。

2. 写相应的配置值到 RBR_THR_DLL、IER_DLH 寄存器，配置传输波特率。

3. 向 LCR[7] 写 0。

4. 配置 LCR，设定相应的 UART 工作模式

5. 配置 FCR，设定相应的发送及接收 FIFO 阈值。

6. 若使用中断方式，则需设定 IER ，使能相应中断信号；

数据发送
''''''''

1. 在 LCR[7] 为 0 状态下，将发送数据写入 RBR_THR_DLL(Transmit Holding Register)，启动数据发送。

2. 若使用查询方式，则通过读取 USR[1](Transmit FIFO not full) 与 TFL (Transmit FIFO Level) 检测 TX_FIFO 状态，根据 TX_FIFO 的状态决定是否继续向 RBR_THR_DLL 中写入数据；

3. 若使用中断方式，则根据相应中断状态位检测；决定是否继续向 RBR_THR_DLL 中写入数据。

4. 通过检测 USR[2](Transmit FIFO Empty)，判断UART是否完成全部数据发送。

数据接收
''''''''

1. 若使用查询方式，则通过读取 USR[3](Receive FIFO Not Empty) 与 RFL(Receive FIFO Level) 检测 RX_FIFO 状态，根据 RX_FIFO 的状态决定是否读取 RBR_THR_DLL(Receive Buffer Register)，取得数据。

2. 若使用中断方式，则根据相应中断状态位检测决定是否读取 RBR_THR_DLL(Receive Buffer Register)，取得数据。

DMA 方式下的数据传输
^^^^^^^^^^^^^^^^^^^^

初始化步骤
''''''''''

1. 向 LCR[7] 写 1。使能配置 Divisor Latch Access

2. 写相应的配置值到 RBR_THR_DLL、IER_DLH 寄存器，配置传输波特率。

3. 向 LCR[7] 写 0。

4. 配置 LCR，设定相应的 UART 工作模式

5. 配置 FCR，设定相应的发送及接收 FIFO 阈值。

6. 关闭 IER 中的 ETBEI/ERBFI；

数据发送
''''''''

1. 配置系统 DMA 通道映射。参照系统 DMA 通道映射，将选取之 UART 控制器 TX/RX 请求线号配置到对应的系统 DMA 通道。例如： UART0 TX 配置系统 DMA 通道 3 则 sdma_dma_ch_remap0[29:24]=9 。配置完成需配置 update_dma_remp_0_3 使配置生效。

2. 配置系统 DMA 数据通道，包括数据传输源和目的地址、数据传输个数、传输类型等参数。具体配置时请参见 DMA 控制器章节。

3. 通过系统 DMA 中断上报，判断数据是否发送完成。

数据接收
''''''''

1. 配置系统 DMA 通道映射。参照 DMA 通道映射 ，将选取之 UART 控制器 TX/RX 请求线号配置到对应的系统 DMA 通道。例如：UART0 RX 配置系统 DMA 通道1 则设置 sdma_dma_ch_remap0[13:8] = 8配置完成需配置 update_dma_remp_0_3 使配置生效。

2. 配置系统 DMA 数据通道，包括数据传输源和目的地址、数据接收区地址、数据传输个数、传输类型等参数。具体配置时请参见 DMA 控制器章节。

3. 通过系统 DMA 中断上报，判断数据是否接收完成。

.. _section_uart_register_overview:

UART 寄存器概览
~~~~~~~~~~~~~~~

包括 6 个 UART, 5 个 Active Domain, 1 个 No-die Domain。其基地址分别如下。每个 UART 由一组控制寄存器组成，每组定义相同。

.. include:: ./uart_registers_overview.table.rst

UART 寄存器描述
~~~~~~~~~~~~~~~

.. include:: ./uart_registers_description.table.rst
