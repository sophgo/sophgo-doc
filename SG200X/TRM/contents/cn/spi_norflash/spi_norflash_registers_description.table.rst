SPI_CTRL
~~~~~~~~

.. _table_spi_ctrl:
.. table:: SPI_CTRL, Offset Address: 0x000
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 10:0 | sck_div              | R/W   | SPI Clock Divider      | 0x9  |
	|      |                      |       |                        |      |
	|      |                      |       | SCK frequency = HCLK   |      |
	|      |                      |       | frequency / (2(SckDiv+ |      |
	|      |                      |       | 1))                    |      |
	+------+----------------------+-------+------------------------+------+
	| 11   | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 12   | cpha                 | R/W   | Clock Phase            | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | 0: After the chip      |      |
	|      |                      |       | select is valid,       |      |
	|      |                      |       | starts sampling data   |      |
	|      |                      |       | at the first clock     |      |
	|      |                      |       | edge of SCK.           |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1: After the chip      |      |
	|      |                      |       | select is valid,       |      |
	|      |                      |       | starts sampling data   |      |
	|      |                      |       | at the second clock    |      |
	|      |                      |       | edge of SCK.           |      |
	+------+----------------------+-------+------------------------+------+
	| 13   | cpol                 | R/W   | Clock Polarity         | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | 0: SCK Low level when  |      |
	|      |                      |       | idle                   |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1: SCK High level when |      |
	|      |                      |       | idle                   |      |
	+------+----------------------+-------+------------------------+------+
	| 14   | hold_o               | R/W   | HOLD Pin output level  | 0x1  |
	+------+----------------------+-------+------------------------+------+
	| 15   | wp_o                 | R/W   | WP Pin output level    | 0x1  |
	+------+----------------------+-------+------------------------+------+
	| 19:16| frame_len            | R/W   | Frame length sent and  | 0x8  |
	|      |                      |       | received. 0 indicates  |      |
	|      |                      |       | that the frame length  |      |
	|      |                      |       | is 16 bits; a frame    |      |
	|      |                      |       | length of 1 is not     |      |
	|      |                      |       | supported.             |      |
	+------+----------------------+-------+------------------------+------+
	| 20   | lsb_first            | R/W   | LSBF: Least            | 0x0  |
	|      |                      |       | Significant Bit First  |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0: Frame MSB first     |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1: Frame LSB first     |      |
	+------+----------------------+-------+------------------------+------+
	| 21   | srst                 | R/W   | Write 1 to reset each  | 0x0  |
	|      |                      |       | state machine and      |      |
	|      |                      |       | interrupt flag bit     |      |
	+------+----------------------+-------+------------------------+------+
	| 31:22| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

CE_CTRL
~~~~~~~

.. _table_ce_ctrl:
.. table:: CE_CTRL, Offset Address: 0x004
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | ce_manual            | R/W   | Control the level value| 0x0  |
	|      |                      |       | of CE pin              |      |
	+------+----------------------+-------+------------------------+------+
	| 1    | ce_manual_en         | R/W   | CE Manual Enable       | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | 0: The level value of  |      |
	|      |                      |       | the CE pin is          |      |
	|      |                      |       | controlled by the      |      |
	|      |                      |       | hardware state machine.|      |
	|      |                      |       |                        |      |
	|      |                      |       | 1: The level value of  |      |
	|      |                      |       | CE pin is controlled by|      |
	|      |                      |       | CEManual register      |      |
	+------+----------------------+-------+------------------------+------+
	| 31:2 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

DLY_CTRL
~~~~~~~~

.. _table_dly_ctrl:
.. table:: DLY_CTRL, Offset Address: 0x008
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 3:0  | frame_interval       | R/W   | Control the frame      | 0x0  |
	|      |                      |       | spacing between two    |      |
	|      |                      |       | adjacent frames of data|      |
	|      |                      |       | : T= TSCK \* FmIntvl   |      |
	|      |                      |       | (no SCK pulse within   |      |
	|      |                      |       | the frame spacing).    |      |
	|      |                      |       | The frame spacing      |      |
	|      |                      |       | between two adjacent   |      |
	|      |                      |       | frames of data. When it|      |
	|      |                      |       | is 0, there is no frame|      |
	|      |                      |       | spacing.               |      |
	+------+----------------------+-------+------------------------+------+
	| 7:4  | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 11:8 | cet                  | R/W   | CET controls the time  | 0x3  |
	|      |                      |       | that CE is valid in    |      |
	|      |                      |       | advance relative to    |      |
	|      |                      |       | the first clock edge   |      |
	|      |                      |       | of SCK before a        |      |
	|      |                      |       | transmission starts and|      |
	|      |                      |       | the time that it       |      |
	|      |                      |       | continues to be valid  |      |
	|      |                      |       | relative to the last   |      |
	|      |                      |       | clock edge of SCK after|      |
	|      |                      |       | the transmission ends. |      |
	|      |                      |       | This time is calculated|      |
	|      |                      |       | as T= TSCK \* (CET+1)  |      |
	+------+----------------------+-------+------------------------+------+
	| 13:12| smp_en_dly           | R/W   | Receive sampling delay | 0x0  |
	|      |                      |       | option. Delay sample   |      |
	|      |                      |       | cycle (IP working      |      |
	|      |                      |       | clock) behind the      |      |
	|      |                      |       | positive edge of SCK to|      |
	|      |                      |       | perform sampling.      |      |
	+------+----------------------+-------+------------------------+------+
	| 14   | rx_pipe_ctrl         | R/W   | Receive sample clock   | 0x0  |
	|      |                      |       | edge option.           |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0: Normal sampling     |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1: Adopt SCK negative  |      |
	|      |                      |       | edge sampling to       |      |
	|      |                      |       | achieve high-speed     |      |
	|      |                      |       | transmission           |      |
	+------+----------------------+-------+------------------------+------+
	| 31:15| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

DMMR_CTRL
~~~~~~~~~

.. _table_dmmr_ctrl:
.. table:: DMMR_CTRL, Offset Address: 0x00c
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | dmmr_mode            | R/W   | dmmr_mode. When this   | 0x1  |
	|      |                      |       | bit is 1, the read     |      |
	|      |                      |       | address on the AHB will|      |
	|      |                      |       | be directly mapped to  |      |
	|      |                      |       | the SPI Flash, and the |      |
	|      |                      |       | controller             |      |
	|      |                      |       | automatically reads    |      |
	|      |                      |       | data from the          |      |
	|      |                      |       | corresponding address  |      |
	|      |                      |       | of the SPI Flash       |      |
	|      |                      |       | without the need for   |      |
	|      |                      |       | software to set related|      |
	|      |                      |       | commands and addresses.|      |
	|      |                      |       | At this time, the SPI  |      |
	|      |                      |       | Flash can be used as a |      |
	|      |                      |       | ROM. When DMMR is 1,   |      |
	|      |                      |       | the registers in the IP|      |
	|      |                      |       | can be written but not |      |
	|      |                      |       | read.                  |      |
	+------+----------------------+-------+------------------------+------+
	| 31:1 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

TRAN_CSR
~~~~~~~~

.. _table_tran_csr:
.. table:: TRAN_CSR, Offset Address: 0x010
	:widths: 1 1 1 5 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 1:0  | tran_mode            | R/W   | Transfer Mode          | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | 00: No Tx, No Rx       |      |
	|      |                      |       |                        |      |
	|      |                      |       | 01: Rx only            |      |
	|      |                      |       |                        |      |
	|      |                      |       | 10: Tx only            |      |
	|      |                      |       |                        |      |
	|      |                      |       | 11: Tx and Rx          |      |
	|      |                      |       |                        |      |
	|      |                      |       | TranMode indicates the |      |
	|      |                      |       | sending and receiving  |      |
	|      |                      |       | mode of transmitted    |      |
	|      |                      |       | data except commands   |      |
	|      |                      |       | and addresses.         |      |
	+------+----------------------+-------+------------------------+------+
	| 2    | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 3    | fast_mode            | R/W   | FastMode:              | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | 0: Normal Mode         |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1: Fast Mode           |      |
	+------+----------------------+-------+------------------------+------+
	| 5:4  | bus_width            | R/W   | Bus Width              | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | 00: 1 bit bus          |      |
	|      |                      |       |                        |      |
	|      |                      |       | 01: 2 bit bus          |      |
	|      |                      |       |                        |      |
	|      |                      |       | 10: 4 bit bus          |      |
	|      |                      |       |                        |      |
	|      |                      |       | 11: Reserved           |      |
	+------+----------------------+-------+------------------------+------+
	| 6    | dma_en               | R/W   | 0: DMA Disable         | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | 1: DMA Enable          |      |
	|      |                      |       |                        |      |
	|      |                      |       | When TranMode is 11    |      |
	|      |                      |       | (sending and receiving |      |
	|      |                      |       | at the same time), DMA |      |
	|      |                      |       | transmission is not    |      |
	|      |                      |       | supported.             |      |
	+------+----------------------+-------+------------------------+------+
	| 7    | miso_cked            | R/W   | miso_i pin level value | 0x0  |
	+------+----------------------+-------+------------------------+------+
	| 10:8 | addr_bn              | R/W   | Address Byte Number    | 0x3  |
	|      |                      |       |                        |      |
	|      |                      |       | Indicates the number of|      |
	|      |                      |       | bytes in the current   |      |
	|      |                      |       | Flash transmission     |      |
	|      |                      |       | address field, 0       |      |
	|      |                      |       | indicates no address   |      |
	|      |                      |       | field.                 |      |
	+------+----------------------+-------+------------------------+------+
	| 11   | with_cmd             | R/W   | With Command           | 0x1  |
	|      |                      |       |                        |      |
	|      |                      |       | 0: The current transfer|      |
	|      |                      |       | is without a command.  |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1: The current         |      |
	|      |                      |       | transport carries the  |      |
	|      |                      |       | command.               |      |
	+------+----------------------+-------+------------------------+------+
	| 13:12| ff_trg_lvl           | R/W   | FFTrgLvl controls the  | 0x3  |
	|      |                      |       | conditions under which |      |
	|      |                      |       | the FIFO generates     |      |
	|      |                      |       | interrupts and DMA     |      |
	|      |                      |       | requests.              |      |
	|      |                      |       |                        |      |
	|      |                      |       | 00: 1 Byte             |      |
	|      |                      |       |                        |      |
	|      |                      |       | 01: 2 Bytes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | 10: 4 Bytes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | 11: 8 Bytes            |      |
	|      |                      |       |                        |      |
	|      |                      |       | For Transmit,          |      |
	|      |                      |       | interrupts and DMA     |      |
	|      |                      |       | requests are generated |      |
	|      |                      |       | when the number of free|      |
	|      |                      |       | Bytes in the FIFO is   |      |
	|      |                      |       | greater than or equal  |      |
	|      |                      |       | to the number of Bytes |      |
	|      |                      |       | defined by FFTrgLvl;   |      |
	|      |                      |       |                        |      |
	|      |                      |       | For Receive, interrupts|      |
	|      |                      |       | and DMA requests are   |      |
	|      |                      |       | generated when the     |      |
	|      |                      |       | number of valid Bytes  |      |
	|      |                      |       | in the FIFO is greater |      |
	|      |                      |       | than or equal to the   |      |
	|      |                      |       | number of Bytes        |      |
	|      |                      |       | defined by FFTrgLvl.   |      |
	+------+----------------------+-------+------------------------+------+
	| 14   | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 15   | go_busy              | R/W   | Writing 0 to this bit  | 0x0  |
	|      |                      |       | has no effect, writing |      |
	|      |                      |       | 1 sets this bit to 1   |      |
	|      |                      |       | and starts a transfer, |      |
	|      |                      |       | and the bit is         |      |
	|      |                      |       | automatically cleared  |      |
	|      |                      |       | after the transfer is  |      |
	|      |                      |       | completed. Before      |      |
	|      |                      |       | initiating a new       |      |
	|      |                      |       | transfer, the software |      |
	|      |                      |       | should query this      |      |
	|      |                      |       | register. Only when the|      |
	|      |                      |       | register is 0 can a new|      |
	|      |                      |       | transfer be initiated. |      |
	+------+----------------------+-------+------------------------+------+
	| 19:16| dummy_cyc            | R/W   | dummy cycle count      | 0x0  |
	|      |                      |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 20   | byte4en              | R/W   | 4 bytes address cycle  | 0x0  |
	|      |                      |       | enable in dmmr_mode    |      |
	+------+----------------------+-------+------------------------+------+
	| 21   | byte4cmd             | R/W   | 4 bytes address cmd    | 0x0  |
	|      |                      |       | enable in dmmr_mode    |      |
	+------+----------------------+-------+------------------------+------+
	| 31:22| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

TRAN_NUM
~~~~~~~~

.. _table_tran_num:
.. table:: TRAN_NUM, Offset Address: 0x014
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 15:0 | rdat_tran_num        | R/W   | In non-dmmr_mode,      | 0x0  |
	|      |                      |       | TRAN_NUM is the number |      |
	|      |                      |       | of frames sent and     |      |
	|      |                      |       | received in one        |      |
	|      |                      |       | transmission.          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:16| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

FF_PORT
~~~~~~~

.. _table_ff_port:
.. table:: FF_PORT, Offset Address: 0x018
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 31:0 | rdat_ff_port         | R/W   | FIFO write read address| 0x0  |
	+------+----------------------+-------+------------------------+------+

FF_PT
~~~~~

.. _table_ff_pt:
.. table:: FF_PT, Offset Address: 0x020
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 3:0  | rdat_ff_pt           | R/W   | Read to get the number | 0x0  |
	|      |                      |       | of valid data bytes in |      |
	|      |                      |       | the FIFO, write to     |      |
	|      |                      |       | clear the FIFO.        |      |
	+------+----------------------+-------+------------------------+------+
	| 7:4  | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 9:8  | wrcnt                | R/W   | Current fifo, write    | 0x0  |
	|      |                      |       | byte offset indicator  |      |
	|      |                      |       | status.                |      |
	+------+----------------------+-------+------------------------+------+
	| 12:10| rdpt                 | R/W   | Current fifo, read byte| 0x0  |
	|      |                      |       | offset indicator status|      |
	+------+----------------------+-------+------------------------+------+
	| 31:13| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

INT_STS
~~~~~~~

.. _table_int_sts:
.. table:: INT_STS, Offset Address: 0x028
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | tran_done_int        | R/W   | This interrupt is      | 0x0  |
	|      |                      |       | generated every time a |      |
	|      |                      |       | frame of data is       |      |
	|      |                      |       | successfully sent.     |      |
	+------+----------------------+-------+------------------------+------+
	| 1    | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 2    | rdff_int             | R/W   | This interrupt is      | 0x0  |
	|      |                      |       | generated every time a |      |
	|      |                      |       | frame of data is       |      |
	|      |                      |       | successfully received. |      |
	+------+----------------------+-------+------------------------+------+
	| 3    | wrff_int             | R/W   | After receiving the    | 0x0  |
	|      |                      |       | interrupt, the CPU     |      |
	|      |                      |       | writes frame data to   |      |
	|      |                      |       | the FIFO.              |      |
	+------+----------------------+-------+------------------------+------+
	| 4    | rx_frame_int         | R/W   | After receiving the    | 0x0  |
	|      |                      |       | interrupt, the CPU     |      |
	|      |                      |       | reads the frame data   |      |
	|      |                      |       | from the FIFO.         |      |
	+------+----------------------+-------+------------------------+------+
	| 5    | tx_frame_int         | R/W   | This interrupt marks   | 0x0  |
	|      |                      |       | the completion of a    |      |
	|      |                      |       | transfer.              |      |
	+------+----------------------+-------+------------------------+------+
	| 31:6 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

INT_EN
~~~~~~

.. _table_int_en:
.. table:: INT_EN, Offset Address: 0x02c
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | tran_done_int_en     | R/W   | Enable Interrupt       | 0x0  |
	|      |                      |       | tran_done_int          |      |
	+------+----------------------+-------+------------------------+------+
	| 1    | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 2    | rdff_int_en          | R/W   | Enable Interrupt       | 0x0  |
	|      |                      |       | rdff_int               |      |
	+------+----------------------+-------+------------------------+------+
	| 3    | wrff_int_en          | R/W   | Enable Interrupt       | 0x0  |
	|      |                      |       | wrff_int               |      |
	+------+----------------------+-------+------------------------+------+
	| 4    | rx_frame_int_en      | R/W   | Enable Interrupt       | 0x0  |
	|      |                      |       | rx_frame_int           |      |
	+------+----------------------+-------+------------------------+------+
	| 5    | tx_frame_int_en      | R/W   | Enable Interrupt       | 0x0  |
	|      |                      |       | tx_frame_int           |      |
	+------+----------------------+-------+------------------------+------+
	| 31:6 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
