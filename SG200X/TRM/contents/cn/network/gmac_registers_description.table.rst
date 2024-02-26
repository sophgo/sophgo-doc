Reg_MacConfig
^^^^^^^^^^^^^

.. _table_reg_macconfig:
.. table:: Reg_MacConfig, Offset Address: 0x000
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 1:0  | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 2    | RX_EN                | R/W   | MAC Receive            | 0x0  |
	|      |                      |       | Enable Register        |      |
	+------+----------------------+-------+------------------------+------+
	| 3    | TX_EN                | R/W   | MAC Transmit           | 0x0  |
	|      |                      |       | Enable Register        |      |
	+------+----------------------+-------+------------------------+------+
	| 6:4  | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 7    | APCS_EN              | R/W   | Automatic Pad/CRC Strip| 0x0  |
	|      |                      |       | Control Enable Register|      |
	+------+----------------------+-------+------------------------+------+
	| 9:8  | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 10   | CHKS_EN              | R/W   | IP checksum Auxiliary  | 0x0  |
	|      |                      |       | Enable Register        |      |
	+------+----------------------+-------+------------------------+------+
	| 11   | DUPLEX_MODE          | R/W   | Full/Half Duplex Mode  | 0x0  |
	|      |                      |       | Register(1enables full |      |
	|      |                      |       | duplex mode)           |      |
	+------+----------------------+-------+------------------------+------+
	| 12   | LPBK_MODE            | R/W   | Loopback Mode          | 0x0  |
	|      |                      |       | Control Register       |      |
	+------+----------------------+-------+------------------------+------+
	| 13   | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 14   | SPEED_MODE           | R/W   | Speed Mode Register    | 0x0  |
	|      |                      |       | 1'b1:100M, 1'b0:10M    |      |
	+------+----------------------+-------+------------------------+------+
	| 16:15| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 19:17| IPG_VAL              | R/W   | Inter-packet Gap Value | 0x0  |
	|      |                      |       | Control Register       |      |
	+------+----------------------+-------+------------------------+------+
	| 22:20| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 23   | WD_DISABLE           | R/W   | Watchdog Disable       | 0x0  |
	|      |                      |       | Register               |      |
	+------+----------------------+-------+------------------------+------+
	| 24   | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 25   | CRC_STRIP_EN         | R/W   | CRC Strip Type Control | 0x0  |
	|      |                      |       | Enable Register        |      |
	+------+----------------------+-------+------------------------+------+
	| 31:26| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

Reg_MdioAddr
^^^^^^^^^^^^

.. _table_reg_mdioaddr:
.. table:: Reg_MdioAddr, Offset Address: 0x010
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | GO                   | R/W   | MDIO Operation         | 0x0  |
	|      |                      |       | Completion Indicator   |      |
	|      |                      |       | 1: Start operation     |      |
	|      |                      |       | 0: Operation completed |      |
	+------+----------------------+-------+------------------------+------+
	| 1    | CMD                  | R/W   | MDIO Operation Command | 0x0  |
	|      |                      |       | Type Write (1'b1),     |      |
	|      |                      |       | Read (1'b0)            |      |
	+------+----------------------+-------+------------------------+------+
	| 5:2  | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 10:6 | RegAddr              | R/W   | External PHY Address   | 0x0  |
	|      |                      |       | Configuration Register |      |
	+------+----------------------+-------+------------------------+------+
	| 15:11| PhyAddr              | R/W   | PHY Device Internal    | 0x0  |
	|      |                      |       | Address Register       |      |
	+------+----------------------+-------+------------------------+------+
	| 31:16| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

Reg_MdioData
^^^^^^^^^^^^

.. _table_reg_mdiodata:
.. table:: Reg_MdioData, Offset Address: 0x014
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 15:0 | MdioData             | R/W   | MDIO Data Register     | 0x0  |
	|      |                      |       | Write or Read Data     |      |
	|      |                      |       | from PHY Register      |      |
	+------+----------------------+-------+------------------------+------+
	| 31:16| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

Reg_MacAddr0_High
^^^^^^^^^^^^^^^^^

.. _table_reg_macaddr0_high:
.. table:: Reg_MacAddr0_High, Offset Address: 0x040
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 15:0 | Addr0_High           | R/W   | MAC Address Register#0 | 0x0  |
	|      |                      |       | bit[47:32]             |      |
	+------+----------------------+-------+------------------------+------+
	| 30:16| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 31   | Addr0_EN             | R/W   | Addr0 Enable           | 0x0  |
	+------+----------------------+-------+------------------------+------+

Reg_MacAddr0_Low
^^^^^^^^^^^^^^^^

.. _table_reg_macaddr0_low:
.. table:: Reg_MacAddr0_Low, Offset Address: 0x044
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 31:0 | Addr0_Low            | R/W   | MAC Address Register#0 | 0x0  |
	|      |                      |       | bit[31:0]              |      |
	+------+----------------------+-------+------------------------+------+

Reg_MacAddr1_High
^^^^^^^^^^^^^^^^^

.. _table_reg_macaddr1_high:
.. table:: Reg_MacAddr1_High, Offset Address: 0x048
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 15:0 | Addr1_High           | R/W   | MAC Address Register#1 | 0x0  |
	|      |                      |       | bit[47:32]             |      |
	+------+----------------------+-------+------------------------+------+
	| 23:16| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 29:24| Addr1_MASK           | R/W   | Addr1 Mask Byte        | 0x0  |
	+------+----------------------+-------+------------------------+------+
	| 30   | Addr1_TYPE           | R/W   | 1'b1: compare SA       | 0x0  |
	|      |                      |       | 1'b0: compare DA       |      |
	+------+----------------------+-------+------------------------+------+
	| 31   | Addr1_EN             | R/W   | Addr1 Enable           | 0x0  |
	+------+----------------------+-------+------------------------+------+

Reg_MacAddr1_Low
^^^^^^^^^^^^^^^^

.. _table_reg_macaddr1_low:
.. table:: Reg_MacAddr1_Low, Offset Address: 0x04c
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 31:0 | Addr1_Low            | R/W   | MAC Address Register#1 | 0x0  |
	|      |                      |       | bit[31:0]              |      |
	+------+----------------------+-------+------------------------+------+

Reg_Tx_Packet_Num_Good_Bad
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _table_reg_tx_packet_num_good_bad:
.. table:: Reg_Tx_Packet_Num_Good_Bad, Offset Address: 0x118
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 31:0 | TxPktNumGB           | RO    | Tranmit Good and Bad   |      |
	|      |                      |       | Packet Count Register  |      |
	+------+----------------------+-------+------------------------+------+

Reg_Tx_Bcast_Packets_Good
^^^^^^^^^^^^^^^^^^^^^^^^^

.. _table_reg_tx_bcast_packets_good:
.. table:: Reg_Tx_Bcast_Packets_Good, Offset Address: 0x11c
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 31:0 | TxBcG                | RO    | Tranmit Good and Bad   |      |
	|      |                      |       | Packet Unicast         |      |
	|      |                      |       | Count Register         |      |
	+------+----------------------+-------+------------------------+------+

Reg_Tx_Mcast_Packets_Good
^^^^^^^^^^^^^^^^^^^^^^^^^

.. _table_reg_tx_mcast_packets_good:
.. table:: Reg_Tx_Mcast_Packets_Good, Offset Address: 0x120
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 31:0 | TxMcG                | RO    | Tranmit Good and Bad   |      |
	|      |                      |       | Packet Multicast       |      |
	|      |                      |       | Count Register         |      |
	+------+----------------------+-------+------------------------+------+

Reg_Tx_Ucast_Packets_Good_Bad
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _table_reg_tx_ucast_packets_good_bad:
.. table:: Reg_Tx_Ucast_Packets_Good_Bad, Offset Address: 0x13c
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 31:0 | TxUcGB               | RO    | Tranmit Good and Bad   |      |
	|      |                      |       | Packet Unicast         |      |
	|      |                      |       | Count Register         |      |
	+------+----------------------+-------+------------------------+------+

Reg_Tx_Mcast_Packets_Good_Bad
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _table_reg_tx_mcast_packets_good_bad:
.. table:: Reg_Tx_Mcast_Packets_Good_Bad, Offset Address: 0x140
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 31:0 | TxMcGB               | RO    | Tranmit Good and Bad   |      |
	|      |                      |       | Packet Multicast       |      |
	|      |                      |       | Count Register         |      |
	+------+----------------------+-------+------------------------+------+

Reg_Tx_Bcast_Packets_Good_Bad
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _table_reg_tx_bcast_packets_good_bad:
.. table:: Reg_Tx_Bcast_Packets_Good_Bad, Offset Address: 0x144
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 31:0 | TxBcGB               | RO    | Tranmit Good and Bad   |      |
	|      |                      |       | Packet Broadcast       |      |
	|      |                      |       | Count Register         |      |
	+------+----------------------+-------+------------------------+------+

Reg_Rx_Packets_Num_Good_Bad
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _table_reg_rx_packets_num_good_bad:
.. table:: Reg_Rx_Packets_Num_Good_Bad, Offset Address: 0x180
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 31:0 | RxPktGB              | RO    | Receive Good and Bad   |      |
	|      |                      |       | Packet Count Register  |      |
	+------+----------------------+-------+------------------------+------+

Reg_Rx_Bcast_Packets_Good
^^^^^^^^^^^^^^^^^^^^^^^^^

.. _table_reg_rx_bcast_packets_good:
.. table:: Reg_Rx_Bcast_Packets_Good, Offset Address: 0x18c
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 31:0 | RxBcG                | RO    |Receive Good Packet     |      |
	|      |                      |       |Broadcast Count Register|      |
	+------+----------------------+-------+------------------------+------+

Reg_Rx_Mcast_Packets_Good
^^^^^^^^^^^^^^^^^^^^^^^^^

.. _table_reg_rx_mcast_packets_good:
.. table:: Reg_Rx_Mcast_Packets_Good, Offset Address: 0x190
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 31:0 | RxMcG                | RO    |Receive Good Packet     |      |
	|      |                      |       |Multicast Count Register|      |
	+------+----------------------+-------+------------------------+------+

Reg_Rx_CRC_Error_Packets
^^^^^^^^^^^^^^^^^^^^^^^^

.. _table_reg_rx_crc_error_packets:
.. table:: Reg_Rx_CRC_Error_Packets, Offset Address: 0x194
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 31:0 | RxCrcERR             | RO    | Receive CRC Error      |      |
	|      |                      |       | Packet Count Register  |      |
	+------+----------------------+-------+------------------------+------+

Reg_Rx_Ucast_Packets_Good
^^^^^^^^^^^^^^^^^^^^^^^^^

.. _table_reg_rx_ucast_packets_good:
.. table:: Reg_Rx_Ucast_Packets_Good, Offset Address: 0x1c4
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 31:0 | RxUcG                | RO    | Receive Good Packet    |      |
	|      |                      |       | Unicast Count Register |      |
	+------+----------------------+-------+------------------------+------+

Reg_Int_Enable
^^^^^^^^^^^^^^

.. _table_reg_int_enable:
.. table:: Reg_Int_Enable, Offset Address: 0x101c
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | TxInt_EN0            | R/W   | Transmit Interrupt     | 0x0  |
        |      |                      |       | Enable Register        |      |
	+------+----------------------+-------+------------------------+------+
	| 5:1  | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 6    | RxInt_EN0            | R/W   | Receive Interrupt      | 0x0  |
	|      |                      |       | Enable Register        |      |
	+------+----------------------+-------+------------------------+------+
	| 31:7 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

Reg_Int_Status
^^^^^^^^^^^^^^

.. _table_reg_int_status:
.. table:: Reg_Int_Status, Offset Address: 0x1014
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | TxInt_ST0            | RO    | Transmit Interrupt     |      |
	|      |                      |       | Status Register        |      |
	+------+----------------------+-------+------------------------+------+
	| 5:1  | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 6    | RxInt_ST0            | RO    | Receive Interrupt      |      |
	|      |                      |       | Status Register        |      |
	+------+----------------------+-------+------------------------+------+
	| 31:7 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
