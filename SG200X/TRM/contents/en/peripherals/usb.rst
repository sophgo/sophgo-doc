USB DRD
-------

Overview
~~~~~~~~

The function of USB DRD is to play the role of Host or Device respectively, which can be changed through software settings. The transmission protocol complies with the USB 2.0 specification, and the maximum transfer rate can reach more than 40MB/s; the main operating modes of Host/Device are Scatter gather DMA transfer (scatter gather DMA), details will be described in the Host and Device chapters respectively; the functions of USB DRD are briefly listed as follows:

- Control Transfer

- Bulk Transfer

- Isochronous Transfer

- Host can connect to USB Hub and supports Interrupt Transfer

- Passed the USB Electrical Characteristics Test (USBET), with good signal quality and compatibility

Function Description
~~~~~~~~~~~~~~~~~~~~

System Block Diagram
^^^^^^^^^^^^^^^^^^^^

The picture below shows the system block diagram inside the USB DRD:

.. _diagram_usb_drd_system_block:
.. figure:: ../../../../media/image131.png
	:align: center

	USB DRD internal system block diagram

Functional Features
^^^^^^^^^^^^^^^^^^^

The functions of USB DRD are briefly listed as follows:

- Comply with USB2.0 transmission protocol specification.

- Backwards compatible with USB1.1 transmission protocol specification.

- Supports HS/FS/LS three speed modes.

- Support Host or Device function.

- Supports four transmission types specified by the USB transmission protocol: control transmission, batch transmission, real-time transmission, and interrupt transmission.

- Can be connected to a USB Hub to expand a single interface into multiple USB interfaces.

- Connect up to 127 Devices via USB Hub expansion.

- Support USB2.0 sleep/resume (suspend/resume) power saving mode.

- Support HID devices such as keyboard and mouse.

- Device mode is mainly used for downloading and updating internal software, and can also be used for other functions, such as data transmission.

- The maximum transfer rate can reach more than 40MB/s.

USBC Function and Register Description
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

USBC Functional Description
^^^^^^^^^^^^^^^^^^^^^^^^^^^

USB DRD can switch between Host or Device functions. You can choose to use either one, but it cannot work at the same time. Its function selection and management are controlled by the USBC block; in addition, Host and device are triggered by some events and interrupts on the Serial Bus. , the register will also be placed in this block.

USBC Register Overview
^^^^^^^^^^^^^^^^^^^^^^

.. This table is smaller and does not require a separate file include

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

USBC Register Description
^^^^^^^^^^^^^^^^^^^^^^^^^

The memory addressing location of USBC is 0x0434_0000, which is represented by USBC_BASE_ADDR in this article. If it is to be read and written, the real addressing location in the memory space will be represented by USBC_BASE_ADDR + Offset; each register has Its corresponding relative addressing (Offset), the details are described below.

.. In order for the following table to display normally, force page break

.. raw:: latex

	\newpage

.. include:: ../../contents-share/peripherals/usb_usbc_registers_description.table.rst






Host Initialization Program Description
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After completing the [Frequency Startup Procedure] and [Mode Switching and Initialization Procedure], you need to execute the XHCI initialization procedure, as listed below. Then you can start the four standard types of transmission according to your needs. The details of the method of starting standard transmission can be Refer to the XHCI specification book, so I won’t go into details here:

Set the GINTMSK.PrtInt register to unmask state.

Set HCFG register to FS device or HS device.

Set the HPRT.PrtPwr register to 1. This setting will turn on V BUS on the USB bus.

Wait for the HPRT0.PrtConnDet interrupt to occur, which means there is a device connected to the USB downstream port.

Set the HPRT.PrtRst register to 1 and start the USB port reset.

Wait at least 10ms to allow the USB port reset enough time to complete the handshake.

Set HPRT.PrtRst to 0 to complete the USB port reset procedure.

Wait for the HPRT.PrtEnChng interrupt to occur.

Read the HPRT.PrtSpd register to obtain the enumeration speed value.

Set the HFIR register to configure the corresponding PHY Clock.

Set the RXFSIZE register to configure the RXFIFO size.

Set the GNPTXFSIZ register to configure the size of the aperiodic transmission TXFIFO.

Set the HPTXFSIZ register to configure the size of the TXFIFO for periodic transmission.

Host Registers
~~~~~~~~~~~~~~

The base-address of the Host register in the entire memory space is 0x0434_0000. In this article, this base address will be represented by HOST_BASE_ADDR. Therefore, the actual addressing of each register of the Host controller in the memory space will be [HOST_BASE_ADDR+relative address].

Register Overview
^^^^^^^^^^^^^^^^^

.. This table is smaller and does not require a separate file include

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

Register Description
^^^^^^^^^^^^^^^^^^^^^

.. include:: ../../contents-share/peripherals/usb_host_registers_description.table.rst

Device Initialization
~~~~~~~~~~~~~~~~~~~~~

Follow these steps:

Set the following bits in the DCFG register:

DescDMA is 1, start descriptor DMA mode

Device Speed is HS or FS

Status bits of non-zero transfers

Periodically transmitted Interval value

Set the FIFO Threshold size in DMA transfers

Clear the DCTL.SftDiscon bit to allow the device to start the Connection action to the Host

Clear GINTMSK following bits

USB Port Reset mask

Enumeration done mask

Early suspend mask

USB suspend mask

SOF mask

Wait for the GINTSTS.USBReset interrupt to occur and start the USB Reset initialization process

Wait for the GINTSTS.EnumerationDone interrupt to occur, which means the USB Reset program has been completed, and read the DSTS register, obtain the enumeration speed, and perform the Enumeration initialization program

Device Registers
~~~~~~~~~~~~~~~~

The basic-address of the Device register in the entire memory space is \**0x0434_0000**\. In this article, this basic addressing will be represented by DEV_BASE_ADDR, so the actual addressing of each register in the memory space is It will be [DEV_BASE_ADDR + relative address].

Register Overview
^^^^^^^^^^^^^^^^^

.. The table is smaller, no separate file include

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

Register Description
^^^^^^^^^^^^^^^^^^^^

.. include:: ../../contents-share/peripherals/usb_device_registers_description.table.rst
