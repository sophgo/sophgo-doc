Ethernet MAC
------------

Overview
~~~~~~~~

The chip supports 1 Ethernet MAC to receive and send network data.

.. only:: sg2002

	This Ethernet MAC is equipped with a built-in 10/100Mbps Fast Ethernet Transceiver, which can operate in 10/100Mbps, full-duplex or half-duplex mode.

.. only:: sg2000

	This Ethernet MAC is equipped with a built-in 10/100Mbps Fast Ethernet Transceiver, which can operate in 10/100Mbps, full-duplex or half-duplex mode and can support external PHY via RMII.

Function Description
~~~~~~~~~~~~~~~~~~~~

The Ethernet module has the following features:

- Ethernet MAC0 with built-in 10 / 100 Mbps Fast Ethernet Transceiver with built-in Ethernet PHY supports 10/100 Mbit/s rate.

.. only:: sg2000

	- Support external PHY via RMII.

- Support full-duplex or half-duplex working mode.

- Support CRC check for input frames.

- Support adding CRC check to output frames.

- Support short frame filling function.

- Support inner loopback in port full-duplex mode.

- Support statistical counting of received and sent frames.

- Support sending and receiving packet caching.

- Support COE (Checksum Offload Engine) checksum offload engine function.

Overall Data Flow
~~~~~~~~~~~~~~~~~

The overall data flow of an ethernet switched interface is shown in the diagram :ref:`diagram_emac_data_flow`.

.. _diagram_emac_data_flow:
.. figure:: ../../../../media/image27.png
	:align: center

	eMAC overall data flow

Single Network Port Function Configuration Description
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ethernet Transceiver Frame Management Function
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The CPU first configures the Ethernet MAC to receive and send the Descriptor List buffer area and the Descriptor List content, for example, the settings of the sending and receiving frame addresses and packet type and size parameters.

When receiving, the Ethernet MAC receives various received data packets, and receives Descriptor List information according to the CPU configuration, such as packet cache information, including packet cache starting address, packet cache depth, etc., and stores the received packets in the DDR. Then notify the CPU to perform subsequent processing actions.

When sending, the Ethernet MAC sends the packet cache information of the Descriptor List according to the CPU configuration, such as the packet cache starting address, packet length and other packet information, etc., moves the packets stored in the DDR, assembles them into packets by itself, and then sends to the network interface. Then notify the CPU that the packet has been transmitted.

Ethernet Packet Receiving Interrupt Management Function
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Interrupt Generation
^^^^^^^^^^^^^^^^^^^^

Set the receive direction interrupt, configure Re_Int_Enable bit[6] = 1, and the CPU queries the receive interrupt status Reg_Int_Status bit[6].

Interrupt Clear
^^^^^^^^^^^^^^^

CPU query receive interrupt status Reg_Int_Status bit[6], write 1 to clear the interrupt status.

Configure PHY Chip Working Status
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ethernet MAC provides MDIO interface settings for the PHY chip. The MDIO interface is divided into read operations and write operations. The registers that mainly control the MDIO interface are Reg_MdioAddr and Reg_MdioData.

- The configuration steps for read operations are as follows:

  - Configure the following settings in the MDIO control register:

    - Reg_MdioAddr bit[15:11] sets the PHY chip address. Please plan according to the PHY chip or board end.

    - Reg_MdioAddr bit[10:6] sets the PHY internal register address to be read and written.

    - Reg_MdioAddr bit[1] is written to 0 (read action command).

  - Finally, set Reg_MdioAddr bit[0] = 1 to start the read action.

  The MDIO interface will receive the read data into Reg_MdioData bit[15:0], and change Reg_Mdi0Addr bit[0] to 0.

- The configuration steps for write operations are as follows:

  - Configure the following settings in the MDIO control register:

    - Reg_MdioAddr bit[15:11] sets the PHY chip address. Please plan according to the PHY chip or board end.

    - Reg_MdioAddr bit[10:6] sets the PHY internal register address to be read and written.

    - Reg_MdioAddr bit[1] is written to 1 (write action command).

  - Finally, set Reg_MdioAddr bit[0] = 1 to start the writing action.

  The MDIO interface will change Reg_Mdi0Addr bit[0] to 0 after the writing action is completed.

Working Mode Switch
~~~~~~~~~~~~~~~~~~~

Ethernet MAC working mode: Ethernet MAC0 supports built-in EPHY function. The working mode adopted is RMII (10/100M).

The speed and mode switching register settings are as follows:

- Configure ETH0 Reg_MacConfig bit[14] = (100M:1, 10M:0);

Note: This configuration cannot be performed when the chip is working normally. It is recommended to configure it during initialization.

Typical Application
~~~~~~~~~~~~~~~~~~~

Register Offset Address Description
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ethernet MAC 0 register offset address space:

- ETH0_MAC : 0x0451_000~0x0451_FFFF

GMAC Register Overview
~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../../contents-share/network/gmac_registers_overview.table.rst

GMAC Register Description
~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../../contents-share/network/gmac_registers_description.table.rst
