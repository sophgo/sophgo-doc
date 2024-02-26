IC_CON
^^^^^^

.. _table_ic_conb:
.. table:: RTC_IC_CON, Offset Address: 0x000
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | MASTER_MODE          | R/W   | enable master mode     | 0x1  |
	+------+----------------------+-------+------------------------+------+
	| 2:1  | SPEED                | R/W   | 1: standard mode (~100 | 0x3  |
	|      |                      |       | kbit/s)                |      |
	|      |                      |       |                        |      |
	|      |                      |       | 2: fast mode (~400     |      |
	|      |                      |       | kbit/s)                |      |
	+------+----------------------+-------+------------------------+------+
	| 3    | IC_10BITADDR_SLAVE   | R/W   | enable 10bit slave     | 0x1  |
	|      |                      |       | address mode           |      |
	+------+----------------------+-------+------------------------+------+
	| 4    | IC_10BITADDR_MASTER  | R/W   | enable 10bit master    | 0x1  |
	|      |                      |       | address mode           |      |
	+------+----------------------+-------+------------------------+------+
	| 5    | IC_RESTART_EN        | R/W   | enable I2C master to   | 0x1  |
	|      |                      |       | be able generate       |      |
	|      |                      |       | restart                |      |
	+------+----------------------+-------+------------------------+------+
	| 6    | IC_SLAVE_DISABLE     | R/W   | 0: slave is enabled    | 0x1  |
	|      |                      |       |                        |      |
	|      |                      |       | 1: slave is disabled   |      |
	+------+----------------------+-------+------------------------+------+
	| 31:7 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+


IC_TAR
^^^^^^

.. _table_ic_tar:
.. table:: IC_TAR, Offset Address: 0x004
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 9:0  | IC_TAR               | R/W   | I2C Target Address     | 0x55 |
	|      |                      |       | Register               |      |
	+------+----------------------+-------+------------------------+------+
	| 10   | GC_OR_START          | R/W   | If bit SPECIAL is set  | 0x0  |
	|      |                      |       | to 1, then this bit    |      |
	|      |                      |       | indicates whether a    |      |
	|      |                      |       | General Call or START  |      |
	|      |                      |       | byte command           |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0: general call        |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1: start byte          |      |
	+------+----------------------+-------+------------------------+------+
	| 11   | SPECIAL              | R/W   | Used to issue General  | 0x0  |
	|      |                      |       | Call or START BYTE     |      |
	+------+----------------------+-------+------------------------+------+
	| 31:12| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+



IC_SAR
^^^^^^

.. _table_ic_sar:
.. table:: IC_SAR, Offset Address: 0x008
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 9:0  | IC_SAR               | R/W   | I2C Slave Address      | 0x55 |
	|      |                      |       | Register               |      |
	+------+----------------------+-------+------------------------+------+
	| 31:10| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

IC_DATA_CMD
^^^^^^^^^^^

.. _table_ic_data_cmd:
.. table:: IC_DATA_CMD, Offset Address: 0x010
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 7:0  | DAT                  | R/W   | transmitted or         | 0x0  |
	|      |                      |       | received data port     |      |
	+------+----------------------+-------+------------------------+------+
	| 8    | CMD                  | R/W   | 0: Write               | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | 1: Read                |      |
	+------+----------------------+-------+------------------------+------+
	| 9    | STOP                 | R/W   | issue stop             | 0x0  |
	+------+----------------------+-------+------------------------+------+
	| 10   | RESTART              | R/W   | issue restart          | 0x0  |
	+------+----------------------+-------+------------------------+------+
	| 31:11| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+


IC_SS_SCL_HCNT
^^^^^^^^^^^^^^

.. _table_ic_ss_scl_hcnt:
.. table:: IC_SS_SCL_HCNT, Offset Address: 0x014
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 15:0 | IC_SS_SCL_HCNT       | R/W   | Standard Speed I2C     |0x0190|
	|      |                      |       | Clock SCL High Count   |      |
	|      |                      |       | Register               |      |
	+------+----------------------+-------+------------------------+------+
	| 31:16| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

IC_SS_SCL_LCNT
^^^^^^^^^^^^^^

.. _table_ic_ss_scl_lcnt:
.. table:: IC_SS_SCL_LCNT, Offset Address: 0x018
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 15:0 | IC_SS_SCL_LCNT       | R/W   | Standard Speed I2C     |0x01d6|
	|      |                      |       | Clock SCL Low Count    |      |
	|      |                      |       | Register               |      |
	+------+----------------------+-------+------------------------+------+
	| 31:16| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

IC_FS_SCL_HCNT
^^^^^^^^^^^^^^

.. _table_ic_fs_scl_hcnt:
.. table:: IC_FS_SCL_HCNT, Offset Address: 0x01c
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 15:0 | IC_FS_SCL_HCNT       | R/W   | Fast Speed I2C Clock   |0x003C|
	|      |                      |       | SCL High Count         |      |
	|      |                      |       | Register               |      |
	+------+----------------------+-------+------------------------+------+
	| 31:16| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

IC_FS_SCL_LCNT
^^^^^^^^^^^^^^

.. _table_ic_fs_scl_lcnt:
.. table:: IC_FS_SCL_LCNT, Offset Address: 0x020
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 15:0 | IC_FS_SCL_LCNT       | R/W   | Fast Speed I2C Clock   |0x0082|
	|      |                      |       | SCL Low Count Register |      |
	+------+----------------------+-------+------------------------+------+
	| 31:16| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

IC_INTR_STAT
^^^^^^^^^^^^

.. _table_ic_intr_stat:
.. table:: IC_INTR_STAT, Offset Address: 0x02c
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | R_RX_UNDER           | RO    | corresponding masked   |      |
	|      |                      |       | interrupt staus,       |      |
	|      |                      |       | please reference I2C   |      |
	|      |                      |       | Raw Interrupt Status   |      |
	+------+----------------------+-------+------------------------+------+
	| 1    | R_RX_OVER            | RO    | corresponding masked   |      |
	|      |                      |       | interrupt staus,       |      |
	|      |                      |       | please reference I2C   |      |
	|      |                      |       | Raw Interrupt Status   |      |
	+------+----------------------+-------+------------------------+------+
	| 2    | R_RX_FULL            | RO    | corresponding masked   |      |
	|      |                      |       | interrupt staus,       |      |
	|      |                      |       | please reference I2C   |      |
	|      |                      |       | Raw Interrupt Status   |      |
	+------+----------------------+-------+------------------------+------+
	| 3    | R_TX_OVER            | RO    | corresponding masked   |      |
	|      |                      |       | interrupt staus,       |      |
	|      |                      |       | please reference I2C   |      |
	|      |                      |       | Raw Interrupt Status   |      |
	+------+----------------------+-------+------------------------+------+
	| 4    | R_TX_EMPTY           | RO    | corresponding masked   |      |
	|      |                      |       | interrupt staus,       |      |
	|      |                      |       | please reference I2C   |      |
	|      |                      |       | Raw Interrupt Status   |      |
	+------+----------------------+-------+------------------------+------+
	| 5    | R_RD_REQ             | RO    | corresponding masked   |      |
	|      |                      |       | interrupt staus,       |      |
	|      |                      |       | please reference I2C   |      |
	|      |                      |       | Raw Interrupt Status   |      |
	+------+----------------------+-------+------------------------+------+
	| 6    | R_TX_ABRT            | RO    | corresponding masked   |      |
	|      |                      |       | interrupt staus,       |      |
	|      |                      |       | please reference I2C   |      |
	|      |                      |       | Raw Interrupt Status   |      |
	+------+----------------------+-------+------------------------+------+
	| 7    | R_RX_DONE            | RO    | corresponding masked   |      |
	|      |                      |       | interrupt staus,       |      |
	|      |                      |       | please reference I2C   |      |
	|      |                      |       | Raw Interrupt Status   |      |
	+------+----------------------+-------+------------------------+------+
	| 8    | R_ACTIVITY           | RO    | corresponding masked   |      |
	|      |                      |       | interrupt staus,       |      |
	|      |                      |       | please reference I2C   |      |
	|      |                      |       | Raw Interrupt Status   |      |
	+------+----------------------+-------+------------------------+------+
	| 9    | R_STOP_DET           | RO    | corresponding masked   |      |
	|      |                      |       | interrupt staus,       |      |
	|      |                      |       | please reference I2C   |      |
	|      |                      |       | Raw Interrupt Status   |      |
	+------+----------------------+-------+------------------------+------+
	| 10   | R_START_DET          | RO    | corresponding masked   |      |
	|      |                      |       | interrupt staus,       |      |
	|      |                      |       | please reference I2C   |      |
	|      |                      |       | Raw Interrupt Status   |      |
	+------+----------------------+-------+------------------------+------+
	| 11   | R_GEN_CALL           | RO    | corresponding masked   |      |
	|      |                      |       | interrupt staus,       |      |
	|      |                      |       | please reference I2C   |      |
	|      |                      |       | Raw Interrupt Status   |      |
	+------+----------------------+-------+------------------------+------+
	| 31:12| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+


IC_INTR_MASK
^^^^^^^^^^^^

.. _table_ic_intr_mask:
.. table:: IC_INTR_MASK, Offset Address: 0x030
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | M_RX_UNDER           | R/W   | corresponding          | 0x1  |
	|      |                      |       | interrupt staus mask,  |      |
	|      |                      |       | please reference I2C   |      |
	|      |                      |       | Raw Interrupt Status   |      |
	+------+----------------------+-------+------------------------+------+
	| 1    | M_RX_OVER            | R/W   | corresponding          | 0x1  |
	|      |                      |       | interrupt staus mask,  |      |
	|      |                      |       | please reference I2C   |      |
	|      |                      |       | Raw Interrupt Status   |      |
	+------+----------------------+-------+------------------------+------+
	| 2    | M_RX_FULL            | R/W   | corresponding          | 0x1  |
	|      |                      |       | interrupt staus mask,  |      |
	|      |                      |       | please reference I2C   |      |
	|      |                      |       | Raw Interrupt Status   |      |
	+------+----------------------+-------+------------------------+------+
	| 3    | M_TX_OVER            | R/W   | corresponding          | 0x1  |
	|      |                      |       | interrupt staus mask,  |      |
	|      |                      |       | please reference I2C   |      |
	|      |                      |       | Raw Interrupt Status   |      |
	+------+----------------------+-------+------------------------+------+
	| 4    | M_TX_EMPTY           | R/W   | corresponding          | 0x1  |
	|      |                      |       | interrupt staus mask,  |      |
	|      |                      |       | please reference I2C   |      |
	|      |                      |       | Raw Interrupt Status   |      |
	+------+----------------------+-------+------------------------+------+
	| 5    | M_RD_REQ             | R/W   | corresponding          | 0x1  |
	|      |                      |       | interrupt staus mask,  |      |
	|      |                      |       | please reference I2C   |      |
	|      |                      |       | Raw Interrupt Status   |      |
	+------+----------------------+-------+------------------------+------+
	| 6    | M_TX_ABRT            | R/W   | corresponding          | 0x1  |
	|      |                      |       | interrupt staus mask,  |      |
	|      |                      |       | please reference I2C   |      |
	|      |                      |       | Raw Interrupt Status   |      |
	+------+----------------------+-------+------------------------+------+
	| 7    | M_RX_DONE            | R/W   | corresponding          | 0x1  |
	|      |                      |       | interrupt staus mask,  |      |
	|      |                      |       | please reference I2C   |      |
	|      |                      |       | Raw Interrupt Status   |      |
	+------+----------------------+-------+------------------------+------+
	| 8    | M_ACTIVITY           | R/W   | corresponding          | 0x0  |
	|      |                      |       | interrupt staus mask,  |      |
	|      |                      |       | please reference I2C   |      |
	|      |                      |       | Raw Interrupt Status   |      |
	+------+----------------------+-------+------------------------+------+
	| 9    | M_STOP_DET           | R/W   | corresponding          | 0x0  |
	|      |                      |       | interrupt staus mask,  |      |
	|      |                      |       | please reference I2C   |      |
	|      |                      |       | Raw Interrupt Status   |      |
	+------+----------------------+-------+------------------------+------+
	| 10   | M_START_DET          | R/W   | corresponding          | 0x0  |
	|      |                      |       | interrupt staus mask,  |      |
	|      |                      |       | please reference I2C   |      |
	|      |                      |       | Raw Interrupt Status   |      |
	+------+----------------------+-------+------------------------+------+
	| 11   | M_GEN_CALL           | R/W   | corresponding          | 0x1  |
	|      |                      |       | interrupt staus mask,  |      |
	|      |                      |       | please reference I2C   |      |
	|      |                      |       | Raw Interrupt Status   |      |
	+------+----------------------+-------+------------------------+------+
	| 31:12| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+


IC_RAW_INTR_STAT
^^^^^^^^^^^^^^^^

.. _table_ic_raw_intr_stat:
.. table:: IC_RAW_INTR_STAT, Offset Address: 0x034
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | IST_RX_UNDER         | RO    | when receive buffer is |      |
	|      |                      |       | empty by reading from  |      |
	|      |                      |       | the IC_DATA_CMD        |      |
	|      |                      |       | register               |      |
	+------+----------------------+-------+------------------------+------+
	| 1    | IST_RX_OVER          | RO    | receive buffer is      |      |
	|      |                      |       | oveflow (64Bytes)      |      |
	+------+----------------------+-------+------------------------+------+
	| 2    | IST_RX_FULL          | RO    | receive buffer reaches |      |
	|      |                      |       | or goes above the      |      |
	|      |                      |       | RX_TL threshold        |      |
	+------+----------------------+-------+------------------------+------+
	| 3    | IST_TX_OVER          | RO    | transmit buffer is     |      |
	|      |                      |       | oveflow (64Bytes)      |      |
	+------+----------------------+-------+------------------------+------+
	| 4    | IST_TX_EMPTY         | RO    | transmit buffer is at  |      |
	|      |                      |       | or below the TX_TL     |      |
	|      |                      |       | threshold              |      |
	+------+----------------------+-------+------------------------+------+
	| 5    | IST_RD_REQ           | RO    | In slave mode, I2C     |      |
	|      |                      |       | hold SCL and wait for  |      |
	|      |                      |       | the response from      |      |
	|      |                      |       | processor              |      |
	+------+----------------------+-------+------------------------+------+
	| 6    | IST_TX_ABRT          | RO    | In master or slave     |      |
	|      |                      |       | mode, when transmitter |      |
	|      |                      |       | is unable to complete  |      |
	|      |                      |       | the action             |      |
	+------+----------------------+-------+------------------------+------+
	| 7    | IST_RX_DONE          | RO    | In slave-transmitter   |      |
	|      |                      |       | mode, a NACK is        |      |
	|      |                      |       | received               |      |
	+------+----------------------+-------+------------------------+------+
	| 8    | IST_ACTIVITY         | RO    | I2C activity is        |      |
	|      |                      |       | detected               |      |
	+------+----------------------+-------+------------------------+------+
	| 9    | IST_STOP_DET         | RO    | STOP occurred          |      |
	+------+----------------------+-------+------------------------+------+
	| 10   | IST_START_DET        | RO    | START or RESTART       |      |
	|      |                      |       | occurred               |      |
	+------+----------------------+-------+------------------------+------+
	| 11   | IST_GEN_CALL         | RO    | General Call address   |      |
	|      |                      |       | is received            |      |
	+------+----------------------+-------+------------------------+------+
	| 31:12| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+


IC_RX_TL
^^^^^^^^

.. _table_ic_rx_tl:
.. table:: IC_RX_TL, Offset Address: 0x038
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 7:0  | RX_TL                | R/W   | Receive FIFO Threshold | 0x0  |
	|      |                      |       | Level                  |      |
	+------+----------------------+-------+------------------------+------+
	| 31:8 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

IC_TX_TL
^^^^^^^^

.. _table_ic_tx_tl:
.. table:: IC_TX_TL, Offset Address: 0x03c
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 7:0  | TX_TL                | R/W   | Transmit FIFO          | 0x0  |
	|      |                      |       | Threshold Level        |      |
	+------+----------------------+-------+------------------------+------+
	| 31:8 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+


IC_CLR_INTR
^^^^^^^^^^^

.. _table_ic_clr_intr:
.. table:: IC_CLR_INTR, Offset Address: 0x040
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | CLR_INTR             | RO    | read to clear          |      |
	|      |                      |       | corresponding all raw  |      |
	|      |                      |       | staus                  |      |
	+------+----------------------+-------+------------------------+------+
	| 31:1 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

IC_CLR_RX_UNDER
^^^^^^^^^^^^^^^

.. _table_ic_clr_rx_under:
.. table:: IC_CLR_RX_UNDER, Offset Address: 0x044
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | CLR_RX_UNDER         | RO    | read to clear          |      |
	|      |                      |       | corresponding interupt |      |
	|      |                      |       | raw staus, please      |      |
	|      |                      |       | reference I2C Raw      |      |
	|      |                      |       | Interrupt Status       |      |
	+------+----------------------+-------+------------------------+------+
	| 31:1 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+


IC_CLR_RX_OVER
^^^^^^^^^^^^^^

.. _table_ic_clr_rx_over:
.. table:: IC_CLR_RX_OVER, Offset Address: 0x048
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | CLR_RX_OVER          | RO    | read to clear          |      |
	|      |                      |       | corresponding interupt |      |
	|      |                      |       | raw staus, please      |      |
	|      |                      |       | reference I2C Raw      |      |
	|      |                      |       | Interrupt Status       |      |
	+------+----------------------+-------+------------------------+------+
	| 31:1 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

IC_CLR_TX_OVER
^^^^^^^^^^^^^^

.. _table_ic_clr_tx_over:
.. table:: IC_CLR_TX_OVER, Offset Address: 0x04c
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | CLR_TX_OVER          | RO    | read to clear          |      |
	|      |                      |       | corresponding interupt |      |
	|      |                      |       | raw staus, please      |      |
	|      |                      |       | reference I2C Raw      |      |
	|      |                      |       | Interrupt Status       |      |
	+------+----------------------+-------+------------------------+------+
	| 31:1 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

IC_CLR_RD_REQ
^^^^^^^^^^^^^

.. _table_ic_clr_rd_req:
.. table:: IC_CLR_RD_REQ, Offset Address: 0x050
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | CLR_RD_REQ           | RO    | read to clear          |      |
	|      |                      |       | corresponding interupt |      |
	|      |                      |       | raw staus, please      |      |
	|      |                      |       | reference I2C Raw      |      |
	|      |                      |       | Interrupt Status       |      |
	+------+----------------------+-------+------------------------+------+
	| 31:1 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

IC_CLR_TX_ABRT
^^^^^^^^^^^^^^

.. _table_ic_clr_tx_abrt:
.. table:: IC_CLR_TX_ABRT, Offset Address: 0x054
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | CLR_TX_ABRT          | RO    | read to clear          |      |
	|      |                      |       | corresponding interupt |      |
	|      |                      |       | raw staus, please      |      |
	|      |                      |       | reference I2C Raw      |      |
	|      |                      |       | Interrupt Status       |      |
	+------+----------------------+-------+------------------------+------+
	| 31:1 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+


IC_CLR_RX_DONE
^^^^^^^^^^^^^^

.. _table_ic_clr_rx_done:
.. table:: IC_CLR_RX_DONE, Offset Address: 0x058
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | CLR_RX_DONE          | RO    | read to clear          |      |
	|      |                      |       | corresponding interupt |      |
	|      |                      |       | raw staus, please      |      |
	|      |                      |       | reference I2C Raw      |      |
	|      |                      |       | Interrupt Status       |      |
	+------+----------------------+-------+------------------------+------+
	| 31:1 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+


IC_CLR_ACTIVITY
^^^^^^^^^^^^^^^

.. _table_ic_clr_activity:
.. table:: IC_CLR_ACTIVITY, Offset Address: 0x05c
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | CLR_ACTIVITY         | RO    | read to clear          |      |
	|      |                      |       | corresponding interupt |      |
	|      |                      |       | raw staus, please      |      |
	|      |                      |       | reference I2C Raw      |      |
	|      |                      |       | Interrupt Status       |      |
	+------+----------------------+-------+------------------------+------+
	| 31:1 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

IC_CLR_STOP_DET
^^^^^^^^^^^^^^^

.. _table_ic_clr_stop_det:
.. table:: IC_CLR_STOP_DET, Offset Address: 0x060
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | CLR_STOP_DET         | RO    | read to clear          |      |
	|      |                      |       | corresponding interupt |      |
	|      |                      |       | raw staus, please      |      |
	|      |                      |       | reference I2C Raw      |      |
	|      |                      |       | Interrupt Status       |      |
	+------+----------------------+-------+------------------------+------+
	| 31:1 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

IC_CLR_START_DET
^^^^^^^^^^^^^^^^

.. _table_ic_clr_start_det:
.. table:: IC_CLR_START_DET, Offset Address: 0x064
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | CLR_START_DET        | RO    | read to clear          |      |
	|      |                      |       | corresponding interupt |      |
	|      |                      |       | raw staus, please      |      |
	|      |                      |       | reference I2C Raw      |      |
	|      |                      |       | Interrupt Status       |      |
	+------+----------------------+-------+------------------------+------+
	| 31:1 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

IC_CLR_GEN_CALL
^^^^^^^^^^^^^^^

.. _table_ic_clr_gen_call:
.. table:: IC_CLR_GEN_CALL, Offset Address: 0x068
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | CLR_GEN_CALL         | RO    | read to clear          |      |
	|      |                      |       | corresponding interupt |      |
	|      |                      |       | raw staus, please      |      |
	|      |                      |       | reference I2C Raw      |      |
	|      |                      |       | Interrupt Status       |      |
	+------+----------------------+-------+------------------------+------+
	| 31:1 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

IC_ENABLE
^^^^^^^^^

.. _table_ic_enable:
.. table:: IC_ENABLE, Offset Address: 0x06c
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | ENABLE               | R/W   | Enables I2C controller | 0x0  |
	+------+----------------------+-------+------------------------+------+
	| 31:1 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

IC_STATUS
^^^^^^^^^

.. _table_ic_status:
.. table:: IC_STATUS, Offset Address: 0x070
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | ST_ACTIVITY          | RO    | I2C Activity Status.   |      |
	+------+----------------------+-------+------------------------+------+
	| 1    | ST_TFNF              | RO    | Transmit FIFO Not Full |      |
	+------+----------------------+-------+------------------------+------+
	| 2    | ST_TFE               | RO    | Transmit FIFO          |      |
	|      |                      |       | Completely Empty       |      |
	+------+----------------------+-------+------------------------+------+
	| 3    | ST_RFNE              | RO    | Receive FIFO Not Empty |      |
	+------+----------------------+-------+------------------------+------+
	| 4    | ST_RFF               | RO    | Receive FIFO           |      |
	|      |                      |       | Completely Full        |      |
	+------+----------------------+-------+------------------------+------+
	| 5    | ST_MST_ACTIVITY      | RO    | Master FSM Activity    |      |
	|      |                      |       | Status                 |      |
	+------+----------------------+-------+------------------------+------+
	| 6    | ST_SLV_ACTIVITY      | RO    | Slave FSM Activity     |      |
	|      |                      |       | Status                 |      |
	+------+----------------------+-------+------------------------+------+
	| 31:7 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

IC_TXFLR
^^^^^^^^

.. _table_ic_txflr:
.. table:: IC_TXFLR, Offset Address: 0x074
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 6:0  | TXFLR                | RO    | I2C Transmit FIFO      |      |
	|      |                      |       | Level                  |      |
	+------+----------------------+-------+------------------------+------+
	| 31:7 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

IC_RXFLR
^^^^^^^^

.. _table_ic_rxflr:
.. table:: IC_RXFLR, Offset Address: 0x078
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 6:0  | RXFLR                | RO    | I2C Receive FIFO Level |      |
	|      |                      |       | Register               |      |
	+------+----------------------+-------+------------------------+------+
	| 31:7 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

IC_SDA_HOLD
^^^^^^^^^^^

.. _table_ic_sda_hold:
.. table:: IC_SDA_HOLD, Offset Address: 0x07c
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 15:0 | IC_SDA_HOLD          | R/W   | Sets the required SDA  | 0x1  |
	|      |                      |       | hold time in units of  |      |
	|      |                      |       | IP clock.              |      |
	+------+----------------------+-------+------------------------+------+
	| 31:16| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

IC_TX_ABRT_SOURCE
^^^^^^^^^^^^^^^^^

.. _table_ic_tx_abrt_source:
.. table:: IC_TX_ABRT_SOURCE, Offset Address: 0x080
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 15:0 | TX_ABRT_SOURCE       | RO    | I2C Transmit Abort     |      |
	|      |                      |       | Source Register        |      |
	+------+----------------------+-------+------------------------+------+
	| 31:16| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+


IC_SLV_DATA_NACK_ONLY
^^^^^^^^^^^^^^^^^^^^^

.. _table_ic_slv_data_nack_only:
.. table:: IC_SLV_DATA_NACK_ONLY, Offset Address: 0x084
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | NACK                 | R/W   | generate a NACK in     | 0x0  |
	|      |                      |       | slave-receiver mode    |      |
	+------+----------------------+-------+------------------------+------+
	| 31:1 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

IC_DMA_CR
^^^^^^^^^

.. _table_ic_dma_cr:
.. table:: IC_DMA_CR, Offset Address: 0x088
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | RDMAE                | R/W   | Receive DMA Enable     | 0x0  |
	+------+----------------------+-------+------------------------+------+
	| 1    | TDMAE                | R/W   | Transmit DMA Enable    | 0x0  |
	+------+----------------------+-------+------------------------+------+
	| 31:2 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

IC_DMA_TDLR
^^^^^^^^^^^

.. _table_ic_dma_tdlr:
.. table:: IC_DMA_TDLR, Offset Address: 0x08c
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 5:0  | DMATDL               | R/W   | the dma_tx_req signal  | 0x0  |
	|      |                      |       | is generated when the  |      |
	|      |                      |       | number of              |      |
	|      |                      |       | valid data entries in  |      |
	|      |                      |       | the transmit FIFO is   |      |
	|      |                      |       | equal to or below this |      |
	|      |                      |       | field value            |      |
	+------+----------------------+-------+------------------------+------+
	| 31:6 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

IC_DMA_RDLR
^^^^^^^^^^^

.. _table_ic_dma_rdlr:
.. table:: IC_DMA_RDLR, Offset Address: 0x090
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 5:0  | DMARDL               | R/W   | dma_rx_req is          | 0x0  |
	|      |                      |       | generated when the     |      |
	|      |                      |       | number of valid data   |      |
	|      |                      |       | entries in             |      |
	|      |                      |       | the receive FIFO is    |      |
	|      |                      |       | equal to or more than  |      |
	|      |                      |       | this field value + 1   |      |
	+------+----------------------+-------+------------------------+------+
	| 31:6 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

IC_SDA_SETUP
^^^^^^^^^^^^

.. _table_ic_sda_setup:
.. table:: IC_SDA_SETUP, Offset Address: 0x094
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | SDA_SETUP            | R/W   | SDA Setup time config  | 0x64 |
	|      |                      |       | register               |      |
	+------+----------------------+-------+------------------------+------+
	| 31:1 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

IC_ACK_GENERAL_CALL
^^^^^^^^^^^^^^^^^^^

.. _table_ic_ack_general_call:
.. table:: IC_ACK_GENERAL_CALL, Offset Address: 0x098
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | ACK_GEN_CALL         | R/W   | When set to 1,         | 0x1  |
	|      |                      |       | DW_apb_i2c responds    |      |
	|      |                      |       | with a ACK when it     |      |
	|      |                      |       | receives a General     |      |
	|      |                      |       | Call. When set to 0,   |      |
	|      |                      |       | the IP does not        |      |
	|      |                      |       | generate General Call  |      |
	|      |                      |       | interrupts             |      |
	+------+----------------------+-------+------------------------+------+
	| 31:1 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

IC_ENABLE_STATUS
^^^^^^^^^^^^^^^^

.. _table_ic_enable_status:
.. table:: IC_ENABLE_STATUS, Offset Address: 0x09c
	:widths: 1 4 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | IC_EN                | RO    | I2C Enable Status      |      |
	|      |                      |       | Register               |      |
	+------+----------------------+-------+------------------------+------+
	| 1    | SLV\                 | RO    | Slave Disabled While   |      |
	|      | _DISABLED_WHILE_BUSY |       | Busy (Transmit,        |      |
	|      |                      |       | Receive)               |      |
	+------+----------------------+-------+------------------------+------+
	| 2    | SLV_RX_DATA_LOST     | RO    | Slave Received Data    |      |
	|      |                      |       | Lost.                  |      |
	+------+----------------------+-------+------------------------+------+
	| 31:3 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

IC_FS_SPKLEN
^^^^^^^^^^^^

.. _table_IC_FS_SPKLEN:
.. table:: ic_fs_spklen, Offset Address: 0x0a0
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 7:0  | IC_FS_SPKLEN         | R/W   | I2C SS and FS Spike    | 0x5  |
	|      |                      |       | Suppression Limit      |      |
	|      |                      |       | Register               |      |
	+------+----------------------+-------+------------------------+------+
	| 31:8 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

IC_HS_SPKLEN
^^^^^^^^^^^^

.. _table_ic_hs_spklen:
.. table:: IC_HS_SPKLEN, Offset Address: 0x0a4
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 7:0  | IC_HS_SPKLEN         | R/W   | I2C HS Spike           | 0x1  |
	|      |                      |       | Suppression Limit      |      |
	|      |                      |       | Register               |      |
	+------+----------------------+-------+------------------------+------+
	| 31:8 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
