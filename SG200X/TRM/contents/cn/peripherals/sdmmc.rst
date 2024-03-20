eMMC/SD/SDIO 控制器
-------------------

功能描述
~~~~~~~~

功能框图
^^^^^^^^

EMMC/SD/SDIO 控制器 (简称 SDMMC 控制器) 用于处理 SD 卡与 eMMC 的资料读写等操作，以及基于 SDIO 协议所支持的外部装置 (如蓝牙、WIFI 等)。本芯片提供了三套 SDMMC 控制器。其中:

- EMMC 支持符合 eMMC4.1 与 eMMC4.5 协议的设备。

- SDIO0 支持符合 Secure Digital Memory (SD 3.0) 协议的设备。

- SDIO1 支持符合 Secure Digital I/O (SDIO 3.0) 协议的设备。

芯片中 3 个 SDMMC 控制器对应的功能信号和脚位，如下表所示。

.. 这个单独的表不大，就不单独文件 include 了

.. _table_sdmmc_controller_pins_signals:
.. table:: Corresponding function signals and pin mapping table of SDMMC controller
	:widths: 3 3 4

	+---------------+---------------------+-------------------------------+
	| SDMMC         | Functional Signal   | Pin                           |
	| Controller    |                     |                               |
	+===============+=====================+===============================+
	| eMMC          | EMMC_CLK            | EMMC_CLK                      |
	|               +---------------------+-------------------------------+
	|               | EMMC_CMD            | EMMC_CMD                      |
	|               +---------------------+-------------------------------+
	|               | EMMC_DATA0          | EMMC_DAT0                     |
	|               +---------------------+-------------------------------+
	|               | EMMC_DATA1          | EMMC_DAT1                     |
	|               +---------------------+-------------------------------+
	|               | EMMC_DATA2          | EMMC_DAT2                     |
	|               +---------------------+-------------------------------+
	|               | EMMC_DATA3          | EMMC_DAT3                     |
	|               +---------------------+-------------------------------+
	|               | EMMC_RSTn           | EMMC_RSTN                     |
	+---------------+---------------------+-------------------------------+
	| SDIO0         | SD_CLK              | SD0_CLK                       |
	|               +---------------------+-------------------------------+
	|               | SD_CMD              | SD0_CMD                       |
	|               +---------------------+-------------------------------+
	|               | SD_DATA0            | SD0_D0                        |
	|               +---------------------+-------------------------------+
	|               | SD_DATA1            | SD0_D1                        |
	|               +---------------------+-------------------------------+
	|               | SD_DATA2            | SD0_D2                        |
	|               +---------------------+-------------------------------+
	|               | SD_DATA3            | SD0_D3                        |
	|               +---------------------+-------------------------------+
	|               | SD_CARD_DETECT      | SD0_CD                        |
	|               +---------------------+-------------------------------+
	|               | SD_POWER_EN         | SD0_PWR_EN                    |
	+---------------+---------------------+-------------------------------+
	| SDIO1         | SDIO_CLK            | SD1_CLK                       |
	|               +---------------------+-------------------------------+
	|               | SDIO_CMD            | SD1_CMD                       |
	|               +---------------------+-------------------------------+
	|               | SDIO_DATA0          | SD1_D0                        |
	|               +---------------------+-------------------------------+
	|               | SDIO_DATA1          | SD1_D1                        |
	|               +---------------------+-------------------------------+
	|               | SDIO_DATA2          | SD1_D2                        |
	|               +---------------------+-------------------------------+
	|               | SDIO_DATA3          | SD1_D3                        |
	+---------------+---------------------+-------------------------------+


.. _diagram_sdmmc_controller:
.. figure:: ../../../../media/image109.png
	:align: center

	SDMMC 控制器的功能框图

SDMMC 的功能：

1.  支持 SD 卡，SDIO 装置与 eMMC。

2.  通过内部的 DMA 控制器，在 eMMC/SD/SDIO 与系统记忆体资料之间传输资料。

3.  支持命令与数据的 CRC 产生与检查。

4.  可通过内部除频器产生不同模式间需要的频率。

5.  提供关闭内部时钟与接口上时钟的机制来达到省电需求。

6.  提供 1-bit 与 4-bit 数据传输接口来与装置沟通。

7.  支持 block_size 等于 1~2048byte 的数据读写操作。

8.  支持 SDIO 协议，包含中断区间，suspend，resume 与 read wait等操作。

9.  支持 AXI/AHB 接口，可通过内部 DMA 来存取系统记忆体。

10. 支持 AHB 接口，可通过 CPU 来存取内部的寄存器。

.. _diagram_sdmmc_typical_usecase:
.. figure:: ../../../../media/image110.png
	:align: center

	典型应用

指令与响应
^^^^^^^^^^

eMMC/SD 的总线封包主要由三者组成: 指令，响应与数据。

其中指令与响应封包是通过 CMD 讯号线传输。

- 指令封包

  指令封包由主控端传送给装置，用来指示一个操作的开始。封包格式由起始位元，传输位元，指令编号，指令参数，CRC 验证码和结束位元共 48 位元组成。如 :ref:`diagram_emmc_command_format` 所示。

.. _diagram_emmc_command_format:
.. figure:: ../../../../media/image111.png
	:align: center

	eMMC/SD/SDIO 指令格式

- 响应封包

  装置端接受到指令后，会根据不同指令类别返回响应，用来显示装置端的状态或参数。其长度为 48 位元或 136 位元。如 :ref:`diagram_emmc_response_format` 所示。

.. _diagram_emmc_response_format:
.. figure:: ../../../../media/image112.png
	:align: center

	eMMC/SD/SDIO 响应格式

- 数据封包:
  
  资料封包用来交换主控端与装置间的数据，根据不同需求可选择 1-bit (DATA0), 4-bit (DATA0-DATA3) 或者 7-bit (DATA0-DATA7)，在每一时钟区间，每一条数据信号线可选择传输 (single data rate) 或者 (dual data rate)。其封包格式分别如图表 :ref:`diagram_emmc_1bit_dataform` ~ 图表 :ref:`diagram_emmc_8bit_dual_dataform` 所示。

.. _diagram_emmc_1bit_dataform:
.. figure:: ../../../../media/image113.png
	:align: center

	eMMC/SD/SDIO 1-bit 数据封包格式

.. _diagram_emmc_4bit_dataform:
.. figure:: ../../../../media/image114.png
	:align: center

	eMMC/SD/SDIO 4-bit 数据封包格式

.. _diagram_emmc_8bit_dataform:
.. figure:: ../../../../media/image115.png
	:align: center

	eMMC/SD/SDIO 8-bit 数据封包格式

.. _diagram_emmc_4bit_dual_dataform:
.. figure:: ../../../../media/image116.png
	:align: center

	4-bit dual data rate 数据封包格式

.. _diagram_emmc_8bit_dual_dataform:
.. figure:: ../../../../media/image117.png
	:align: center

	8-bit dual data rate 数据封包格式

根据是否有资料传输，指令可再分为以下两种:

- 非数据传输指令:通过信号线 CMD 来完成指令传送与接收响应。

.. _diagram_nondata_transfer_cmd:
.. figure:: ../../../../media/image118.png
	:align: center

	非数据传输指令:通过信号线 CMD 来完成指令传送与接收响应

-  数据传输指令:除了信号线 CMD 上的交互外，还有数据线 DAT0~DAT3 的数据传输

数据传输
^^^^^^^^

在主控端与装置端的数据传输主要以块 (block) 为单位，除了数据外还会夹带 CRC 检查位元来验证数据的正确性。比较常用的有单块数据读写和多块数据读写方式，相较于单块数据传输而言，多块数据传输有比较高的效率。其中, EMMC 与 SD 卡的块大小为 512byte，SDIO 比较特殊，可支援 1~2048byte 的块大小，使用者可根据不同的装置来定义块大小的数值。

(1) 单块与多块读操作如图表 :ref:`diagram_emmc_read_operation` ，单块传输由指令，响应，数据与 CRC 组成。多块传输最后可靠 STOP CMD 来中止传输。

.. _diagram_emmc_read_operation:
.. figure:: ../../../../media/image119.png
	:align: center

	单块与多块读操作

(2) 单块与多块写操作如图表 :ref:`diagram_emmc_write_operation`，传输过程会通过 DAT0 讯号线来发 BUSY 讯号，通知主控端写入装置正在进行。

.. _diagram_emmc_write_operation:
.. figure:: ../../../../media/image120.png
	:align: center

	单块与多块写操作

SD3.0 支持的速度模式及电压切换
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- 电压切换程序 (1.8V -> 3.3V)

  - 步骤一: 设定 PWRSW 成 3.3V。
    => sd_pwrsw_ctrl (0x030001F4) = 0x00000009 
    (reg_pwrsw_auto=1, reg_pwrsw_disc=0, reg_pwrsw_vsel=0(3.0v), reg_en_pwrsw=1)

  - 步骤二: 等待 1ms 来完成电压切换。

- 电压切换程序 (3.3V -> 1.8V)

  - 步骤一: 设定 PWRSW 成 1.8V。
    => sd_pwrsw_ctrl (0x030001F4) = 0x0000000B 
    (reg_pwrsw_auto=1, reg_pwrsw_disc=0, reg_pwrsw_vsel=1(1.8v), reg_en_pwrsw=1)

  - 步骤二: 等待 1ms 来完成电压切换。

- 支持速度模式与电压

  SD3.0 所支持速度模式与电压如下表格。

.. 这个表不大，就不单独文件 include 了

.. _table_sd3_spreed_voltage:
.. table:: SD3.0 supported speeds and voltages
	:widths: 3 3 4

	+----------------------+---------+------------------------------------+
	| Mode                 | Speed   | Voltage                            |
	+======================+=========+====================================+
	| DS (default speed)   | 25Mhz   | 1.8V/3.3V                          |
	+----------------------+---------+------------------------------------+
	| HS (high speed)      | 50Mhz   | 1.8V/3.3V                          |
	+----------------------+---------+------------------------------------+
	| SDR12                | 25Mhz   | 1.8V                               |
	+----------------------+---------+------------------------------------+
	| SDR25                | 50Mhz   | 1.8V                               |
	+----------------------+---------+------------------------------------+
	| DRR50                | 50Mhz   | 1.8V                               |
	+----------------------+---------+------------------------------------+
	| SDR50                | 100Mhz  | 1.8V                               |
	+----------------------+---------+------------------------------------+
	| SDR104               | 187.5Mhz| 1.8V                               |
	+----------------------+---------+------------------------------------+

eMMC 支持的速度模式及电压
^^^^^^^^^^^^^^^^^^^^^^^^^

eMMC 所支持速度模式与电压如下表。

.. 这个表不大，就不单独文件 include 了

.. _table_emmc_speed_mode_voltage:
.. table::  eMMC supported speeds and voltages
	:widths: 3 3 4

	+----------------------+---------+------------------------------------+
	| Mode                 | Speed   | Voltage                            |
	+======================+=========+====================================+
	| DS (default speed)   | 26Mhz   | 1.8V/3.3V                          |
	+----------------------+---------+------------------------------------+
	| HS (high speed)      | 52Mhz   | 1.8V/3.3V                          |
	+----------------------+---------+------------------------------------+
	| DRR52                | 52Mhz   | 1.8V                               |
	+----------------------+---------+------------------------------------+
	| HS200                | 187.5Mhz| 1.8V                               |
	+----------------------+---------+------------------------------------+

应用说明
~~~~~~~~

时钟关控
^^^^^^^^

.. _diagram_emmc_clock_transaction_procedure:
.. figure:: ../../../../media/image121.png
	:align: center
	:scale: 60%

	时钟关控程序

如图表 :ref:`diagram_emmc_clock_transaction_procedure` 为时钟关控程序，主控端必须确保在汇流排上没有传输进行才能关闭时钟。

(1) 读取寄存器 PRESENT_STS。

(2) 检查位元 CMD_INHIBIT 与 DAT_INHIBIT 是否都是 0。

(3) 如果有任一位元不为 0, 代表传输仍在进行，需要延迟等待。

(4) 如果皆为 0，则可以设定 CLK_CTL[SD_CLK_EN]=0 来关闭时钟。


软复位
^^^^^^

当控制器操作异常时，可靠复位配置寄存器 (base address = 0x0300_3000) 来进行软复位。其使用的寄存器位址分别如下所示:

1. EMMC : SOFT_RSTN_0[reg_soft_reset_x_emmc] (address offset : 0x000, Bit15)

2. SDIO0 : SOFT_RSTN_0[reg_soft_reset_x_sd0] (address offset : 0x000, Bit16)

3. SDIO1 : SOFT_RSTN_0[reg_soft_reset_x_sd1] (address offset : 0x000, Bit17)

接口时钟配置
^^^^^^^^^^^^

图表 :ref:`diagram_emmc_clock_config` 为接口时钟配置流程图。SDMMC 控制器内部提供一个除频器，让使用者根据不同协议与速度模式，来调整所需要的时钟频率。其关系式为:

F\ :sub:`SD_CLK_OUT` = F\ :sub:`INT_CARD_CLK`/ (2 * clk_divisor)

当 SDMMC 改变频率时除了要确保没有指令与数据仍在传输中之外，还必须按照接口时钟配置流程图的步骤来设定，避免输出到 eMMC/SD 装置的时钟产生毛刺。

(1) 关闭接口时钟。

(2) 计算分频因子。

(3) 设置分频因子。将 (2) 计算出来的参数填入 CLK_CTL[FREQ_SEL]，并且启动打开内部时钟开关 (CLK_CTL[INT_CLK_EN]=1)。

(4) 检查 CLK_CTL[INT_CLK_STABLE] 来确认频率是否切换完成。

(5) 如果还未完成 (CLK_CTL[INT_CLK_STABLE]=0)，则延迟等待。

(6) 如果切换时钟频率完成，则打开接口时钟。

.. _diagram_emmc_clock_config:
.. figure:: ../../../../media/image122.png
	:align: center

	时钟配置流程图

非数据传输指令
^^^^^^^^^^^^^^

- 指令传输程序

  指令传输程序如图表 :ref:`diagram_emmc_transmitting_config`。

  (1) 首先必须检查寄存器位元 PRESENT[CMD_INHIBIT]是否为 0 来确认 CMD Line 是否仍在使用中。

  (2) 如果 CMD Line 是空闲的，则进一步确认是否为带 busy 的指令。如果非 busy 指令，则不需要检查 DATA Line 上的状况，直接执行步骤 (5)，反之如果为带 busy 的指令，则必须执行步骤 (3) 确认是否为 Abort 指令。

  (3) 如果为 Abort 指令，代表 CMD line 完成传输时，DATA line 也同时是闲置的，可直接进入步骤(5)；反之，如果不是 Abort 指令，则必须执行步骤(4)确认 DATA Line 上 busy 是否已经释放。

  (4) 检查寄存器位元 PRESENT[DAT_INHIBIT] 是否为 0 来确认 DATA Line 上是否仍在使用中，如果仍在使用中则持续等待直到传输结束，然后再执行步骤(5)。

  (5) 根据指令需求来设定 ARGUMENT 寄存器与 CMD 寄存器的值。

.. _diagram_emmc_transmitting_config:
.. figure:: ../../../../media/image123.png
	:align: center

	指令传输程序

- 指令完成程序 (Command Complete Sequence)

  指令完成程序如图表 :ref:`diagram_emmc_complete_procedure`。

  (1) 首先会等待 Command 完成的中断 NORM_INT_STS[CMD_CMPL]。

  (2) 收到中断后设定 NORM_INT_STS[CMD_CMPL]=1 来清除 CMD_CMPL 中断状态。

  (3) 接着读取 RESP1_0，RESP3_2，RESP5_4，RESP7_6 等寄存器来获取响应值。

  (4) 如果是一个包含资料传输的指令，会执行步骤 (5)，否则跳到步骤 (8)。

  (5) 等待资料传输中断 NORM_INT_STS[XFER_CMPL]。

  (6) 收到中断后设定 NORM_INT_STS[XFER_CMPL]=1 来清除 XFER_CMPL 中断状态。

  (7) 检查 RESP1_0，RESP3_2，RESP5_4，RESP7_6 等寄存器确认是否有错误状态。如果没错误状态则执行步骤 (8)，回报没有错误。有错误则执行步骤 (9) 来回报错误。

.. _diagram_emmc_complete_procedure:
.. figure:: ../../../../media/image124.png
	:align: center

	指令完成程序

停止或中止数据传输
^^^^^^^^^^^^^^^^^^

- 中止 (Abort) 指令程序

  中止指令对于 eMMC/SD 装置是靠 CMD12, 而 SDIO 装置则是 CMD52 来完成。使用时机主要有两种状况，

  (1) 停止无限模块数据传输。

  (2) 停止多模块数据传输。

  中止指令程序如图表 :ref:`diagram_emmc_stop_procedure`，详细步骤如下:

  .. _diagram_emmc_stop_procedure:
  .. figure:: ../../../../media/image125.png
  	:align: center

  	中止指令程序

  中止指令有两种方式: 同步中止指令与非同步中止指令。

- 非同步中止指令程序

  图表 :ref:`diagram_emmc_nonsync_stop_procedure` 为非同步中止指令的程序图。详细步骤如下:

  (1) 根据不同传输模式执行中止指令。

  (2) 设定 SW_RESET 寄存器中的 SW_RST_CMD 与 SW_RST_DAT 来重置 CMD 与 DAT 信号线。

  (3) 检查位元 SW_RESET[SW_RST_CMD] 与 SW_RESET[SW_RST_DAT] 确认是否重置完成。若两者皆为 0，则结束程序。若其中之一为 1，则回到步骤 (3) 延迟等待。

.. _diagram_emmc_nonsync_stop_procedure:
.. figure:: ../../../../media/image126.png
	:align: center

	非同步中止指令的程序图

- 同步中止指令程序

  图表 :ref:`diagram_emmc_sync_stop_procedure` 为同步中止指令的程序图。详细步骤如下:

  (1) 写入位元 BG_CTL[STOP_BG_REQ] 在 Block Gap 区间停止传输动作。

  (2) 等待传输完成的中断 NORM_INT_STS[XFER_CMPL]。

  (3) 收到中断后设定 NORM_INT_STS[XFER_CMPL]=1 来清除 XFER_CMPL 中断状态。

  (4) 根据不同传输模式执行中止指令。

  (5) 设定 SW_RESET 寄存器中的 SW_RST_CMD与SW_RST_DAT 来重置 CMD 与 DAT 信号线。

  (6) 检查位元 SW_RESET[SW_RST_CMD] 与 SW_RESET[SW_RST_DAT] 确认是否重置完成。若两者皆为 0，则结束程序。若其中之一为 1，则回到步骤 (6) 延迟等待。

.. _diagram_emmc_sync_stop_procedure:
.. figure:: ../../../../media/image127.png
	:align: center

	同步中止指令的程序图

非 DMA 数据传输模式
^^^^^^^^^^^^^^^^^^^

非 DMA 数据传输模式的程序如图表 :ref:`diagram_nodma_data_transfer`。详细步骤如下所示:

(1)  写入 BLK_SIZE 寄存器来设定块大小。

(2)  写入 BLK_CNT 寄存器来设定块数目。

(3)  写入 ARGUMENT 寄存器来设定指令参数。

(4)  写入 XFER_MODE 寄存器来设定传输模式。主控端可根据使用情境来决定设定。包含 Single or Multiple Block Select, DMA Enable, Block Count Enable, Data Transfer Direction, Auto CMD Enable。

(5)  写入 CMD 寄存器来设定指令与响应的类型。

(6)  等待 Command 完成的中断 NORM_INT_STS[CMD_CMPL]。

(7)  收到中断后设定 NORM_INT_STS[CMD_CMPL]=1 来清除 CMD_CMPL 中断状态。

(8)  接着读取 RESP1_0，RESP3_2，RESP5_4，RESP7_6 等寄存器来获取响应值。

(9)  如果是读取操作将执行步骤 (14)，如果是写入操作将执行步骤 (10)。

(10) 等待 Buffer Write Ready 的中断 NORM_INT_STS[BUF_WRDY]。

(11) 收到中断后设定 NORM_INT_STS[BUFF_WRDY]=1 来清除 BUFF_WRDY 中断状态。

(12) 将想要写入装置的数据依序写入 BUF_DATA 寄存器。

(13) 如果还有更多的 block 要写入，则回到步骤(10)，直到最后一个 block 写完后，则进入步骤(18)。

(14) 等待 Buffer Read Ready 的中断 NORM_INT_STS[BUF_RRDY]。

(15) 收到中断后设定 NORM_INT_STS[BUFF_RRDY]=1 来清除 BUFF_RRDY 中断状态。

(16) 依序从 BUF_DATA 寄存器读取从装置端接收回来的资料。

(17) 如果还有更多的 block 要读取，则回到步骤 (14)，直到最后一个 block 读完后，则进入步骤(18)。

(18) 判断是单一模块传输，多模块传输或者无限模块传输。如果是单模块或者多模块传输则跳至步骤 (19)。如果是无限模块传输则跳至步骤 (21)，执行中止传输的动作。

(19) 等待数据传输完成的中断 NORM_INT_STS[XFER_CMPL]。

(20) 收到中断后设定 NORM_INT_STS[CMD_XFER]=1 来清除 XFER_CMPL中断状态。

(21) 执行中止传输程序。

.. _diagram_nodma_data_transfer:
.. figure:: ../../../../media/image128.png
	:align: center

	非DMA数据传输模式的程序

SDMA 数据传输模式
^^^^^^^^^^^^^^^^^

SDMA 数据传输模式程序如图表 :ref:`diagram_sdma_data_transfer`，详细步骤如下所示:

(1)  写入 SDMA_SA 寄存器来设定数据传输时所使用的系统记忆体起始位址。

(2)  写入 BLK_SIZE 寄存器来设定块大小。

(3)  写入 BLK_CNT 寄存器来设定块数目。

(4)  写入 ARGUMENT 寄存器来设定指令参数。

(5)  写入 XFER_MODE 寄存器来设定传输模式。主控端可根据使用情境来决定设定。包含 Single or Multiple Block Select, DMA Enable, Block Count Enable, Data Transfer Direction, Auto CMD Enable。

(6)  写入 CMD 寄存器来设定指令与响应的类型。

(7)  等待 Command 完成的中断 NORM_INT_STS[CMD_CMPL]。

(8)  收到中断后设定 NORM_INT_STS[CMD_CMPL]=1 来清除 CMD_CMPL 中断状态。

(9)  接着读取 RESP1_0，RESP3_2，RESP5_4，RESP7_6 等寄存器来获取响应值。

(10) 等待数据传输中断与 DMA 中断。

(11) 读取中断状态寄存器 NORM_INT_STS 来判断中断类型。如果是 DMA 中断则跳至步骤 (12)，如果是数据传输中断则跳至步骤 (14)。

(12) 设定 NORM_INT_STS[DMA_INT]=1 来清除 DMA_INT 状态值。

(13) 写入 SDMA_SA 寄存器重新设定下一次 DMA 的系统记忆体起始位址。然后跳至步骤 (10)。

(14) 设定 NORM_INT_STS[DMA_INT]=1 与 [NORM_INT_STS[XFER_CMPL]=1 来清除 DMA_INT 与 XFER_CMPL 状态值。然后结束程序。

.. _diagram_sdma_data_transfer:
.. figure:: ../../../../media/image129.png
	:align: center

	SDMA 数据传输模式程序

ADMA 数据传输模式
^^^^^^^^^^^^^^^^^

ADMA 数据传输模式程序如图表 :ref:`diagram_adma_data_transfer`，详细步骤如下所示:

(1)  将 ADMA 描述表填入系统记忆体。

(2)  写入 ADMA_SA_L 与 ADMA_SA_H 寄存器来设定描述表所使用的系统记忆体起始位址。

(3)  写入 BLK_SIZE 寄存器来设定块大小。

(4)  写入 BLK_CNT 寄存器来设定块数目。

(5)  写入 ARGUMENT 寄存器来设定指令参数。

(6)  写入 XFER_MODE 寄存器来设定传输模式。主控端可根据使用情境来决定设定。包含Single or Multiple Block Select, DMA Enable, Block Count Enable, Data Transfer Direction, Auto CMD Enable。

(7)  写入 CMD 寄存器来设定指令与响应的类型。

(8)  等待 Command 完成的中断 NORM_INT_STS[CMD_CMPL]。

(9)  收到中断后设定 NORM_INT_STS[CMD_CMPL]=1 来清除 CMD_CMPL 中断状态。

(10) 接着读取 RESP1_0，RESP3_2，RESP5_4，RESP7_6 等寄存器来获取响应值。

(11) 等待数据传输中断或者 ADMA 错误 (ADMA Error)中断。

(12) 读取中断状态寄存器 NORM_INT_STS 与 ERR_INT_STS 来判断中断类型。如果是 ADMA 错误中断则跳至步骤 (13)，如果是数据传输中断则跳至步骤 (15)。

(13) 设定 ERR_INT_STS[ADMA_ERR]=1 来清除 ADMA_ERR 状态值。

(14) 进入 ADMA 中止传输程序 (ADMA Abort Transaction)，执行 Abort Command 来中止与装置端的资料传输，必要的时候可以检查 ADMA Error Status 寄存器来检查错误发生的原因。

(15) 设 NORM_INT_STS[XFER_CMPL]=1 来清 XFER_CMPL 状态值。然后结束程序。

.. _diagram_adma_data_transfer:
.. figure:: ../../../../media/image130.png
	:align: center

	ADMA 数据传输模式程序

寄存器概览
~~~~~~~~~~

表格 :ref:`table_sdmmc_register_overview` 为 SDMMC 寄存器概览( EMMC 的基本位址为 0x0430_0000, SDIO0 为 0x0431_0000, SDIO1 为 0x0500_0000 )

.. include:: ./sdmmc_register_overview.table.rst

寄存器描述
~~~~~~~~~~

下面为详细的寄存器描述。

.. include:: ./sdmmc_register_description.table.rst
