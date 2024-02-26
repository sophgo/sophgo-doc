AXI_CTRL0_1
^^^^^^^^^^^

.. _table_axi_ctrl0_1:
.. table:: AXI_CTRL0_1, Offset Address: 0x4b4
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 9:0  | axi1_rd_timeout_val  | R/W   | After an AXI read      | 0x0  |
	|      |                      |       | transaction is         |      |
	|      |                      |       | granted, a timeout     |      |
	|      |                      |       | counter starts to      |      |
	|      |                      |       | count. When it counts  |      |
	|      |                      |       | to                     |      |
	|      |                      |       | axi<n>_rd_timeout_val, |      |
	|      |                      |       | the corresponding      |      |
	|      |                      |       | channel has the        |      |
	|      |                      |       | highest priority.      |      |
	+------+----------------------+-------+------------------------+------+
	| 11:10| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 12   | axi1_rd_timeout_en   | R/W   | If set to 1, enables   | 0x0  |
	|      |                      |       | the timeout function   |      |
	|      |                      |       | for the read channel   |      |
	|      |                      |       | of port n.             |      |
	+------+----------------------+-------+------------------------+------+
	| 31:13| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

AXI_CTRL1_1
^^^^^^^^^^^

.. _table_axi_ctrl1_1:
.. table:: AXI_CTRL1_1, Offset Address: 0x4b8
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 9:0  | axi1_wr_timeout_val  | R/W   | After an AXI write     | 0x0  |
	|      |                      |       | transaction is         |      |
	|      |                      |       | granted, a timeout     |      |
	|      |                      |       | counter starts to      |      |
	|      |                      |       | count. When it counts  |      |
	|      |                      |       | to                     |      |
	|      |                      |       | axi<n>_wr_timeout_val, |      |
	|      |                      |       | the corresponding      |      |
	|      |                      |       | channel has the        |      |
	|      |                      |       | highest priority.      |      |
	+------+----------------------+-------+------------------------+------+
	| 11:10| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 12   | axi1_wr_timeout_en   | R/W   | If set to 1, enables   | 0x0  |
	|      |                      |       | the timeout function   |      |
	|      |                      |       | for the write channel  |      |
	|      |                      |       | of port n.             |      |
	+------+----------------------+-------+------------------------+------+
	| 31:13| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

AXI_CTRL0_2
^^^^^^^^^^^

.. _table_axi_ctrl0_2:
.. table:: AXI_CTRL0_2, Offset Address: 0x564
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 9:0  | axi2_rd_timeout_val  | R/W   | After an AXI read      | 0x0  |
	|      |                      |       | transaction is         |      |
	|      |                      |       | granted, a timeout     |      |
	|      |                      |       | counter starts to      |      |
	|      |                      |       | count. When it counts  |      |
	|      |                      |       | to                     |      |
	|      |                      |       | axi<n>_rd_timeout_val, |      |
	|      |                      |       | the corresponding      |      |
	|      |                      |       | channel has the        |      |
	|      |                      |       | highest priority.      |      |
	+------+----------------------+-------+------------------------+------+
	| 11:10| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 12   | axi2_rd_timeout_en   | R/W   | If set to 1, enables   | 0x0  |
	|      |                      |       | the timeout function   |      |
	|      |                      |       | for the read channel   |      |
	|      |                      |       | of port n.             |      |
	+------+----------------------+-------+------------------------+------+
	| 31:13| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

AXI_CTRL1_2
^^^^^^^^^^^

.. _table_axi_ctrl1_2:
.. table:: AXI_CTRL1_2, Offset Address: 0x568
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 9:0  | axi2_wr_timeout_val  | R/W   | After an AXI write     | 0x0  |
	|      |                      |       | transaction is         |      |
	|      |                      |       | granted, a timeout     |      |
	|      |                      |       | counter starts to      |      |
	|      |                      |       | count. When it counts  |      |
	|      |                      |       | to                     |      |
	|      |                      |       | axi<n>_wr_timeout_val, |      |
	|      |                      |       | the corresponding      |      |
	|      |                      |       | channel has the        |      |
	|      |                      |       | highest priority.      |      |
	+------+----------------------+-------+------------------------+------+
	| 11:10| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 12   | axi2_wr_timeout_en   | R/W   | If set to 1, enables   | 0x0  |
	|      |                      |       | the timeout function   |      |
	|      |                      |       | for the write channel  |      |
	|      |                      |       | of port n.             |      |
	+------+----------------------+-------+------------------------+------+
	| 31:13| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

AXI_CTRL0_3
^^^^^^^^^^^

.. _table_axi_ctrl0_3:
.. table:: AXI_CTRL0_3, Offset Address: 0x614
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 9:0  | axi3_rd_timeout_val  | R/W   | After an AXI read      | 0x0  |
	|      |                      |       | transaction is         |      |
	|      |                      |       | granted, a timeout     |      |
	|      |                      |       | counter starts to      |      |
	|      |                      |       | count. When it counts  |      |
	|      |                      |       | to                     |      |
	|      |                      |       | axi<n>_rd_timeout_val, |      |
	|      |                      |       | the corresponding      |      |
	|      |                      |       | channel has the        |      |
	|      |                      |       | highest priority.      |      |
	+------+----------------------+-------+------------------------+------+
	| 11:10| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 12   | axi3_rd_timeout_en   | R/W   | If set to 1, enables   | 0x0  |
	|      |                      |       | the timeout function   |      |
	|      |                      |       | for the read channel   |      |
	|      |                      |       | of port n.             |      |
	+------+----------------------+-------+------------------------+------+
	| 31:13| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

AXI_CTRL1_3
^^^^^^^^^^^

.. _table_axi_ctrl1_3:
.. table:: AXI_CTRL1_3, Offset Address: 0x618
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 9:0  | axi3_wr_timeout_val  | R/W   | After an AXI write     | 0x0  |
	|      |                      |       | transaction is         |      |
	|      |                      |       | granted, a timeout     |      |
	|      |                      |       | counter starts to      |      |
	|      |                      |       | count. When it counts  |      |
	|      |                      |       | to                     |      |
	|      |                      |       | axi<n>_wr_timeout_val, |      |
	|      |                      |       | the corresponding      |      |
	|      |                      |       | channel has the        |      |
	|      |                      |       | highest priority.      |      |
	+------+----------------------+-------+------------------------+------+
	| 11:10| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 12   | axi3_wr_timeout_en   | R/W   | If set to 1, enables   | 0x0  |
	|      |                      |       | the timeout function   |      |
	|      |                      |       | for the write channel  |      |
	|      |                      |       | of port n.             |      |
	+------+----------------------+-------+------------------------+------+
	| 31:13| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
