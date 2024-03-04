Ethernet MAC
------------

概述
~~~~

芯片支持 1个 Ethernet MAC, 实现网路数据的接收与发送。

.. only:: sg2002

	这个 Ethernet MAC 搭配内建 10/100Mbps Fast Ethernet Transceiver, 可工作在 10/100Mbps 全双工或半工双模式。

.. only:: sg2000

	这个 Ethernet MAC 搭配内建 10/100Mbps Fast Ethernet Transceiver, 可工作在 10/100Mbps 全双工或半工双模式，支持通过 RMII 外挂 PHY。

功能描述
~~~~~~~~

以太网模块有如下功能特点 :

- Ethernet MAC0 搭配内建 10 / 100 Mbps Fast Ethernet Transceiver 搭配内建 Ethernet PHY 支持 10 / 100 Mbit/s 速率。

.. only:: sg2000

	- 支持通过 RMII 外挂PHY。

- 支持全双工或半双工工作模式。

- 支持对输入帧进行 CRC 校验。

- 支持对输出帧添加 CRC 校验。

- 支持短帧填充功能。

- 支持端口全双工模式下的内环回。

- 支持对接收和发送帧进行统计计数。

- 支持收发包缓存。

- 支持 COE (Checksum Offload Engine) 校验和卸载引擎功能。

总体数据流
~~~~~~~~~~

以太网交换接口的总体数据流如图表 :ref:`diagram_emac_data_flow` 所示。

.. _diagram_emac_data_flow:
.. figure:: ../../../../media/image27.png
	:align: center

	eMAC 总体数据流

单网口功能配置描述
~~~~~~~~~~~~~~~~~~

以太网收发帧管理功能
^^^^^^^^^^^^^^^^^^^^

CPU 先配置 Ethernet MAC 接收与发送 Descriptor List 缓存区与 Descriptor List 内容撰写例如,收发帧地址与封包种类大小参数的设定.

接收时, Ethernet MAC 接收收到的各种数据包, 并根据 CPU 配置在接收 Descriptor List 信息, 例如封包缓存资讯，包括封包缓存起始地址、封包缓存深度等，将收到的封包存放到 DDR中。再通知 CPU 做后续处理动作。

发送时, Ethernet MAC 根据CPU 配置在发送 Descriptor List 的封包缓存信息, 例如包括封包缓存起始地址、封包长度以及其他的封包信息等，将存于 DDR 的封包搬运过来，自行组装成包，然后发送到网络接口上。再通知 CPU 封包已传送完毕。

以太网收包中断管理功能
~~~~~~~~~~~~~~~~~~~~~~

中断产生
^^^^^^^^

设置接收方向中断, 配置 Re_Int_Enable bit[6] = 1, CPU 查询 接收中断状态 Reg_Int_Status bit[6] 。

中断清除
^^^^^^^^

CPU 查询 接收中断状态 Reg_Int_Status bit[6], 写 1 清除中断状态。

配置 PHY 芯片工作状态
~~~~~~~~~~~~~~~~~~~~~

Ethernet MAC 提供 MDIO 接口对 PHY 芯片的设定。MDIO 接口分为读操作和写操作，主要控制 MDIO 接口的寄存器为 Reg_MdioAddr 和 Reg_MdioData.

- 读操作的配置步骤如下：

  - 配置MDIO控制寄存器以下设定:

    - Reg_MdioAddr bit[15:11] 设定 PHY 芯片地址。请依据 PHY 芯片或板端规划。

    - Reg_MdioAddr bit[10:6] 设定要读写的 PHY 内部寄存器地址。

    - Reg_MdioAddr bit[1] 写入 0 (读的动作命令)。

  - 最后 设定 Reg_MdioAddr bit[0] = 1, 来启动 读的动作。

  MDIO 接口介面会将读回的数据接收到 Reg_MdioData bit[15:0], 并将 Reg_Mdi0Addr bit[0] 改变为0。

- 写操作的配置步骤如下：

  - 配置MDIO控制寄存器以下设定:

    - Reg_MdioAddr bit[15:11] 设定 PHY 芯片地址。请依据 PHY 芯片或板端规划。

    - Reg_MdioAddr bit[10:6] 设定要读写的 PHY 内部寄存器地址。

    - Reg_MdioAddr bit[1] 写入 1 (写的动作命令)。

  - 最后 设定 Reg_MdioAddr bit[0] = 1, 来启动写的动作。

  MDIO 接口会在写的动作完成后, 将 Reg_Mdi0Addr bit[0] 改变为 0。

工作模式切换
~~~~~~~~~~~~

Ethernet MAC 的工作模式: Ethernet MAC0 支持内建的 EPHY 功能。采用的工作模式是 RMII(10/100M)。

速度与模式切换寄存器设定如下步骤:

- 配置 ETH0 Reg_MacConfig bit[14] = (100M:1, 10M:0);

注意事项 : 芯片正常工作时不可进行此项配置，建议在初始化时进行配置。

典型应用
~~~~~~~~

寄存器偏移地址说明
~~~~~~~~~~~~~~~~~~

Ethernet MAC 0 寄存器偏移地址空间:

- ETH0_MAC : 0x0451_000~0x0451_FFFF

GMAC 寄存器概览
~~~~~~~~~~~~~~~

.. include:: ./gmac_registers_overview.table.rst

GMAC 寄存器描述
~~~~~~~~~~~~~~~

.. include:: ./gmac_registers_description.table.rst
