USB DRD
-------

概述
~~~~

USB DRD 的功能为可分别担任 Host 或是 Device 的角色，可以通过软件的设定来改变，传输协议符合 USB 2.0 规格，最高传输速率可达 40MB/s 以上；Host/Device 的主要运作模式皆为分散/聚集 DMA 传输 (scatter gather DMA)，详细情况会分别在 Host 与 Device 的章节中描述；USB DRD 的功能简列如下：

- 控制传输 (Control Transfer)

- 批量传输 (Bulk Transfer)

- 实时传输 (Isochronous Transfer)

- Host 可连接 USB Hub，并且支持中断传输 (Interrupt Transfer)

- 通过 USB 电器特性测试 (USBET)，信号质量、兼容性良好

功能描述
~~~~~~~~

系统框图
^^^^^^^^

下方图片显示 USB DRD 内部的系统框图：

.. _diagram_usb_drd_system_block:
.. figure:: ../../../../media/image131.png
	:align: center

	USB DRD 内部的系统框图

功能特征
^^^^^^^^

USB DRD 的功能简列如下：

- 符合 USB2.0 传输协议规范。

- 向下兼容 USB1.1 传输协议规范。

- 支持 HS/FS/LS 三种速度模式。

- 支持 Host 或者是 Device 功能。

- 支持四种 USB 传输协订所规范的传输型态：控制传输、批量传输、实时传输、中断传输。

- 可连接 USB Hub，将单一接口扩展为多个 USB 接口。

- 通过 USB Hub 扩展，最多可连接 127 Device 装置。

- 支持 USB2.0 休眠/回复 (suspend/resume) 省电模式。

- 支持键盘、鼠标等 HID 装置。

- Device mode 主要用于下载更新内部软件之用，也可做其他功能，例如数据传输之用。

- 最大传输速率可达 40MB/s 以上。

USBC 功能与寄存器描述
~~~~~~~~~~~~~~~~~~~~~

USBC 功能描述
^^^^^^^^^^^^^

USB DRD 可以切换 Host 或是 Device 功能，可以择其一使用，但不能同时存在工作，其功能选择与管理就是靠 USBC 此区块来控制；另外 Host 与 device 有一些 Serial Bus 上面的事件与中断触发，也会将缓存器放置在此一区块。

USBC 寄存器摘要
^^^^^^^^^^^^^^^

.. 这个表格较小，不单独文件 include

.. _table_usbc_register_overview:
.. table:: USBC Registers Overview
	:widths: 3 3 4

	+----------------------+---------+------------------------------------+
	| Name                 | Address | Description                        |
	|                      | Offset  |                                    |
	+======================+=========+====================================+
	| GOTGCTL              | 0x000   | Control and Status Register        |
	+----------------------+---------+------------------------------------+
	| GOTGINT              | 0x004   | Interrupt Register                 |
	+----------------------+---------+------------------------------------+
	| GAHBCFG              | 0x008   | AHB Configuration Register         |
	+----------------------+---------+------------------------------------+
	| GUSBCFG              | 0x00c   | USB Configuration Register         |
	+----------------------+---------+------------------------------------+
	| GRSTCTL              | 0x010   | Reset Register                     |
	+----------------------+---------+------------------------------------+
	| GINTSTS              | 0x014   | Interrupt Status Register          |
	+----------------------+---------+------------------------------------+
	| GINTMSK              | 0x018   | Interrupt Mask Register            |
	+----------------------+---------+------------------------------------+
	| GUID                 | 0x03c   | User ID Register                   |
	+----------------------+---------+------------------------------------+
	| GLPMCFG              | 0x054   | Core LPM Configuration Register    |
	+----------------------+---------+------------------------------------+
	| GPWRDN               | 0x058   | Power Down Register                |
	+----------------------+---------+------------------------------------+

USBC 寄存器详细列表
^^^^^^^^^^^^^^^^^^^

USBC 的内存寻址位置为 0x0434_0000，在文中就以 USBC_BASE_ADDR 来表示，若要对其进行读写控制，则在内存空间中真实的寻址位置就会以 USBC_BASE_ADDR + Offset 来表示；每个寄存器都有其相对应的相对寻址 (Offset)，详细内容如下方所描述。

.. 为了下面表格显式正常，强制换页

.. raw:: latex

	\newpage

.. include:: ./usb_usbc_registers_description.table.rst

Host 初始化程序说明
~~~~~~~~~~~~~~~~~~~

完成【频率启动程序】和【模式切换与初始化程序】之后，需要接着执行 XHCI 的初始化程序，如下方所列，再来就可以依需求启动四种标准型态传输，启动标准传输的方法详细内容可参照 XHCI 规格书，在此就不多加赘述：

设定 GINTMSK.PrtInt 寄存器为 unmask 状态。

设定 HCFG register 为 FS device 或者是 HS device 装置。

设定 HPRT.PrtPwr 寄存器为 1，此一设定会打开 USB bus 上的V BUS。

等待 HPRT0.PrtConnDet 中断发生，代表有一个 device 连接到 USB downstream port。

设定 HPRT.PrtRst 寄存器为 1，开始进行 USB port reset。

等待至少 10ms 让 USB port reset 有足够的时间完成 handshake。

设定 HPRT.PrtRst 为 0，完成 USB port reset 程序。

等待 HPRT.PrtEnChng 中断发生。

读取 HPRT.PrtSpd 寄存器获取 enumeration speed 数值。

设定 HFIR 寄存器进而配置相对应的 PHY Clock。

设定 RXFSIZE 寄存器，配置 RXFIFO 的大小。

设定 GNPTXFSIZ 寄存器，配置非周期性传输 TXFIFO 的大小。

设定 HPTXFSIZ 寄存器，配置周期性传输 TXFIFO 的大小。

Host 寄存器说明
~~~~~~~~~~~~~~~

Host 寄存器的基础寻址 (baseaddress) 在整个内存空间的地址为 0x0434_0000 ，在文中此基础寻址将以 HOST_BASE_ADDR 做为代表，因此 Host 控制器的每个寄存器在内存空间中的真实寻址就会是【HOST_BASE_ADDR+相对地址】。

寄存器摘要
^^^^^^^^^^

.. 这个表较小，不单独文件 include

.. _table_usb_host_register_abstract:
.. table:: Host Registers Overview
	:widths: 3 3 4

	+----------------------+---------+------------------------------------+
	| Name                 | Address | Description                        |
	|                      | Offset  |                                    |
	+======================+=========+====================================+
	| HCFG                 | 0x400   | Host Configuration Register        |
	+----------------------+---------+------------------------------------+
	| HFIR                 | 0x404   | Host Frame Interval Register       |
	+----------------------+---------+------------------------------------+
	| HFNUM                | 0x408   | Host Frame Number/Frame Time       |
	|                      |         | Remaining Register                 |
	+----------------------+---------+------------------------------------+
	| HPTXSTS              | 0x410   | Host Periodic Transmit FIFO/Queue  |
	|                      |         | Status Register                    |
	+----------------------+---------+------------------------------------+
	| HAINT                | 0x414   | Host All Channels Interrupt        |
	|                      |         | Register                           |
	+----------------------+---------+------------------------------------+
	| HAINTMSK             | 0x418   | Host All Channels Interrupt Mask   |
	|                      |         | Register                           |
	+----------------------+---------+------------------------------------+
	| HFLBAddr             | 0x41c   | Host Frame List Base Address       |
	|                      |         | Register                           |
	+----------------------+---------+------------------------------------+
	| HCCHARn              | 0x500   | Host Channel-n Characteristics     |
	|                      |         | Register                           |
	+----------------------+---------+------------------------------------+
	| HCDMAn               | 0x514   | Host Channel-n DMA Address         |
	|                      |         | Register                           |
	+----------------------+---------+------------------------------------+
	| HCDMABn              | 0x51c   | Host Channel-n DMA Buffer Address  |
	|                      |         | Register                           |
	+----------------------+---------+------------------------------------+

寄存器详细列表
^^^^^^^^^^^^^^

.. include:: ./usb_host_registers_description.table.rst

Device 初始化程序
~~~~~~~~~~~~~~~~~

依照以下步骤：

设定 DCFG 寄存器中下列位:

DescDMA 为 1，启动 descriptor DMA mode

Device Speed 为 HS 或者是 FS

非 0 传输的状态位

周期性传输的 Interval 数值

设定在 DMA 传输中的 FIFO Threshold 大小

清除 DCTL.SftDiscon 位，让装置对 Host 开始进行 Connection 动作

清除 GINTMSK 以下位

USB Port Reset mask

Enumeration done mask

Early suspend mask

USB suspend mask

SOF mask

等待 GINTSTS.USBReset 中断发生，并且开始进行 USB Reset 初始化程序

等待 GINTSTS.EnumerationDone 中断发生，代表 USB Reset 程序已经完成，并且去读取 DSTS 寄存器，获取 enumeration speed，并进行 Enumeration 初始化程序

Device 寄存器说明
~~~~~~~~~~~~~~~~~

Device 寄存器的基础寻址 (address) 在整个内存空间的地址为 \ **0x0434_0000**\ ，在文中此基础寻址将以 DEV_BASE_ADDR 做为代表，因此每个寄存器在内存空间中的真实寻址就会是 【DEV_BASE_ADDR + 相对地址】。

寄存器摘要
^^^^^^^^^^

.. 该表较小，不单独文件 include

.. _table_usb_device_register_abs:
.. table:: Device Registers Overview
	:widths: 3 3 4

	+----------------------+---------+------------------------------------+
	| Name                 | Address | Description                        |
	|                      | Offset  |                                    |
	+======================+=========+====================================+
	| DCFG                 | 0x800   | Device Configuration Register      |
	+----------------------+---------+------------------------------------+
	| DCTL                 | 0x804   | Device Control Register            |
	+----------------------+---------+------------------------------------+
	| DSTS                 | 0x808   | Device Status Register             |
	+----------------------+---------+------------------------------------+
	| DIEPMSK              | 0x810   | Device IN Endpoint Common          |
	|                      |         | Interrupt Mask Register            |
	+----------------------+---------+------------------------------------+
	| DOEPMSK              | 0x814   | Device OUT Endpoint Common         |
	|                      |         | Interrupt Mask Register            |
	+----------------------+---------+------------------------------------+
	| DAINT                | 0x818   | Device All Endpoints Interrupt     |
	|                      |         | Register                           |
	+----------------------+---------+------------------------------------+
	| DAINTMSK             | 0x81c   | Device Endpoints Interrupt Mask    |
	|                      |         | Register                           |
	+----------------------+---------+------------------------------------+
	| DIEPEMPMSK           | 0x834   | Device IN Endpoint FIFO Empty      |
	|                      |         | Interrupt Mask Register            |
	+----------------------+---------+------------------------------------+
	| DEACHINT             | 0x838   | Device Each Endpoint Interrupt     |
	|                      |         | Register                           |
	+----------------------+---------+------------------------------------+
	| DEACHINTMSK          | 0x83c   | Device Each Endpoint Interrupt     |
	|                      |         | Register Mask                      |
	+----------------------+---------+------------------------------------+

寄存器详细列表
^^^^^^^^^^^^^^

.. include:: ./usb_device_registers_description.table.rst
