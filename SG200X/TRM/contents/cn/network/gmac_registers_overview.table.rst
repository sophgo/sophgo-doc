.. _table_gmac_registers_overview:
.. table:: GMAC Registers Overview
	:widths: 2 1 2

	+----------------------+---------+------------------------------------+
	| Name                 | Address | Description                        |
	|                      | Offset  |                                    |
	+======================+=========+====================================+
	| Reg_MacConfig        | 0x000   | Local MAC Operation                |
	|                      |         | Configuration Register             |
	+----------------------+---------+------------------------------------+
	| Reg_MdioAddr         | 0x010   | MDIO Operation Register            |
	+----------------------+---------+------------------------------------+
	| Reg_MdioData         | 0x014   | MDIO Data Read and                 |
	|                      |         | Write Register                     |
	+----------------------+---------+------------------------------------+
	| Reg_MacAddr0_High    | 0x040   | Local MAC Address Register#0       |
	|                      |         | High 16bit                         |
	+----------------------+---------+------------------------------------+
	| Reg_MacAddr0_Low     | 0x044   | Local MAC Address Register#0       |
	|                      |         | Low 32bit                          |
	+----------------------+---------+------------------------------------+
	| Reg_MacAddr1_High    | 0x048   | Local MAC Address Register#1       |
	|                      |         | High 16bit                         |
	+----------------------+---------+------------------------------------+
	| Reg_MacAddr1_Low     | 0x04c   | Local MAC Address Register#1       |
	|                      |         | Low 32bit                          |
	+----------------------+---------+------------------------------------+
	| Reg_Tx\              | 0x118   | Tranmit Good and Bad Packet        |
	| _Packet_Num_Good_Bad |         | Num Count Register                 |
	+----------------------+---------+------------------------------------+
	| Reg_T\               | 0x11c   | Tranmit Good Bad Packet            |
	| x_Bcast_Packets_Good |         | Broadcast Count Register           |
	+----------------------+---------+------------------------------------+
	| Reg_T\               | 0x120   | Tranmit Good Bad Packet            |
	| x_Mcast_Packets_Good |         | Multicast Count Register           |
	+----------------------+---------+------------------------------------+
	| Reg_Tx_Uc\           | 0x13c   | Tranmit Good and Bad Packet        |
	| ast_Packets_Good_Bad |         | Unicast Count Register             |
	+----------------------+---------+------------------------------------+
	| Reg_Tx_Mc\           | 0x140   | Tranmit Good and Bad Packet        |
	| ast_Packets_Good_Bad |         | Multicast Count Register           |
	+----------------------+---------+------------------------------------+
	| Reg_Tx_Bc\           | 0x144   | Tranmit Good and Bad Packet        |
	| ast_Packets_Good_Bad |         | Broadcast Count Register           |
	+----------------------+---------+------------------------------------+
	| Reg_Rx\_\            | 0x180   | Receive Good and Bad Packet        |
	| Packets_Num_Good_Bad |         | Count Register                     |
	+----------------------+---------+------------------------------------+
	| Reg_R\               | 0x18c   | Receive Good Packet                |
	| x_Bcast_Packets_Good |         | Broadcast Count Register           |
	+----------------------+---------+------------------------------------+
	| Reg_R\               | 0x190   | Receive Good Packet                |
	| x_Mcast_Packets_Good |         | Multicast Count Register           |
	+----------------------+---------+------------------------------------+
	| Reg\_\               | 0x194   | Receive CRC Error Packet           |
	| Rx_CRC_Error_Packets |         | Count Register                     |
	+----------------------+---------+------------------------------------+
	| Reg_R\               | 0x1c4   | Receive Good Packet                |
	| x_Ucast_Packets_Good |         | Unicast Count Register             |
	+----------------------+---------+------------------------------------+
	| Reg_Int_Enable       | 0x101c  | Interrupt Enable Register          |
	+----------------------+---------+------------------------------------+
	| Reg_Int_Status       | 0x1014  | Interrupt Status Register          |
	+----------------------+---------+------------------------------------+
