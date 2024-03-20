MIPI Tx
-------

概述
~~~~

The Display Serial Interface (DSI) 接口是移动行业处理器接口联盟 (Mobile Industry Processor Interface alliance, MIPI 联盟) 定义的一种高速串行接口, 主要用于处理器和显示模块之间的连接。MIPI Tx接口实现DSI接口, 持 MIPI D-PHY V1.0 串行信号输出。

MIPI Tx 包含模拟 PHY 和数字 Controller 两部分，系统架构及功能框图如图所示。

.. _diagram_mipi_tx_function_block:
.. figure:: ../../../../media/image76.png
	:align: center

	MIPI TX 功能框图

特点
~~~~

MIPI Tx 有以下特点：

- 支持 1/2/4 Data Lane MIPI D-PHY接口, 顺序, PN极可配置。

- 高速模式最大支持 2500Mbps/Lane。

- 仅 Data Lane0 支持低速发送及接收、BTA (Bus Turn-Around) 功能，低速模式速度最高 10Mbps。

- 支持 DSI RGB16/18/24/30 bit 数据类形输出。

- 支持 DSI video mode 和 command mode, video mode 支持 Burst mode、Non-burst mode with Sync Events 和 Non-burst mode with Sync pulses。

功能描述
~~~~~~~~

MIPI Tx 包括 Tx D-PHY 和 Tx Controller 两部分

- Tx D-PHY 支持 MIPI D-PHY ver2.1 协议，主要实现了物理层的传输规范。

- Tx Controller 根据 MIPI DSI 协议对数据格式进行封装。

Tx D-PHY
^^^^^^^^

Tx D-PHY 有两种工作模式，高速 (High Speed, HS) 和低速 (Low Power, LP):

- Video mode 的数据通过高速模式传输。

- Command mode 的数据通过低速模式来传输。

高速模式每个通道 (Lane) 的数率范围为 80~2500Mbps, 低速模式的最大速率为 10Mbps。

高速模式最大支持 4 个 data lane, 实际使用的 data lane 个数可以为 1/2/4, 顺序及极性可配置。低速模式的发送、接收及 Bus Turn-Around (BTA) 仅配置后的 data lane0 支持。

Tx Controller
^^^^^^^^^^^^^

数据包的发送
^^^^^^^^^^^^

当有复数个高速封包而要传送时, Tx D-PHY 会依据 Tx Controller 送出来高速资料传输需求自动进行 HS 和 LP 模式的切换。Tx Controller 支持 HS 传输结束时是否发送 EoT 包 (End of Transmission, EoT)。

数据类型
^^^^^^^^

控制器支持 DSI RGB16/18/24/30 bit 的发送，各种数据类型的组成格式如图所示。

.. _diagram_rgb16_format:
.. figure:: ../../../../media/image77.png
	:align: center

	RGB 16-bit 格式 (Data type = 0x0E)

.. _diagram_rgb18_format:
.. figure:: ../../../../media/image78.png
	:align: center

	RGB 18-bit 格式 (Data type = 0x1E)

注意 : RGB 18-bit 仅支持 data type = 0x0E, 不支持 loosely Packet 模式 (data type = 0x2E)

.. _diagram_rgb24_format:
.. figure:: ../../../../media/image79.png
	:align: center

	RGB 24-bit 格式 (Data type = 0x3E)

.. _diagram_rgb30_format:
.. figure:: ../../../../media/image80.png
	:align: center

	RGB 30-bit 格式 (Data type = 0x0D)

接口时序
^^^^^^^^

时序标记如下

.. _diagram_mipi_tx_timesequence:
.. figure:: ../../../../media/image81.png
	:align: center

	MIPI TX 时序标记

- VSA: 帧同步行数

- VBP: 帧后消隐行数

- VACT: 帧有效数据行

- VFP: 帧前消隐行

- VSS: 帧同步信号

- HSS: 行同步信号

- HBP: 行后消隐区

- RGB: 行有效数据

- HFP: 行前消隐区

- BLLP: Blanking or Low-Power Interval

Video 垂直时序为

帧同步信号 (VSS)，帧后消隐区 (VBP)，有效行区 (VACT)，帧前消隐区 (VFP)，帧同步信号。

水平时序为

行同步信号 (HSS)，行后消隐区 (HBP), 有效画素 (HACT)，行前消隐区 (HFP)，行同步信号。

有效同步信号为 VSS, HSS, 有效画素为 有效行区(VACT) 和 有效画素 (HACT) 之交集。

Video mode Burst Transmission 时序如下

.. _diagram_mipi_tx_video_mode_burst_transmission_timesequence:
.. figure:: ../../../../media/image82.png
	:align: center

	MIPI TX Video mode Burst Transmission 时序

MIPI Tx 只传输有效同步信号及数据，其余时间进入 BLLP 区以降低功耗。

MIPI Tx 寄存器概览
~~~~~~~~~~~~~~~~~~

MIPI Tx Control 寄存器位置为 0x0A08A000

.. include:: ./mipi_tx_control_registers_overview.table.rst

MIPI Tx 寄存器描述
~~~~~~~~~~~~~~~~~~

.. include:: ./mipi_tx_control_registers_description.table.rst

MIPI Tx PHY 寄存器概览
~~~~~~~~~~~~~~~~~~~~~~

MIPI Tx PHY 寄存器位置为 0x0A0D_1000

.. include:: ./mipi_tx_phy_registers_overview.table.rst

MIPI Tx PHY 寄存器描述
~~~~~~~~~~~~~~~~~~~~~~

.. include:: ./mipi_tx_phy_registers_description.table.rst
