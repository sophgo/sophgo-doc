CTRLR0
^^^^^^

.. _table_ctrlr0:
.. table:: CTRLR0, Offset Address: 0x000
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 15:0 | CTRLR0               | R/W   | [15:12] Control Frame  | 0x7  |
	|      |                      |       | Size.                  |      |
	|      |                      |       |                        |      |
	|      |                      |       | Selects the length of  |      |
	|      |                      |       | the control word for   |      |
	|      |                      |       | the Microwire frame    |      |
	|      |                      |       | format.                |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0000 1-bit control   |      |
	|      |                      |       |   word                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0001 2-bit control   |      |
	|      |                      |       |   word                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0010 3-bit control   |      |
	|      |                      |       |   word                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0011 4-bit control   |      |
	|      |                      |       |   word                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0100 5-bit control   |      |
	|      |                      |       |   word                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0101 6-bit control   |      |
	|      |                      |       |   word                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0110 7-bit control   |      |
	|      |                      |       |   word                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0111 8-bit control   |      |
	|      |                      |       |   word                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1000 9-bit control   |      |
	|      |                      |       |   word                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1001 10-bit control  |      |
	|      |                      |       |   word                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1010 11-bit control  |      |
	|      |                      |       |   word                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1011 12-bit control  |      |
	|      |                      |       |   word                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1100 13-bit control  |      |
	|      |                      |       |   word                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1101 14-bit control  |      |
	|      |                      |       |   word                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1110 15-bit control  |      |
	|      |                      |       |   word                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1111 16-bit control  |      |
	|      |                      |       |   word                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | [11] Shift Register    |      |
	|      |                      |       | Loop.                  |      |
	|      |                      |       |                        |      |
	|      |                      |       | Used for testing       |      |
	|      |                      |       | purposes only. When    |      |
	|      |                      |       | internally active,     |      |
	|      |                      |       | connects the transmit  |      |
	|      |                      |       | shift register output  |      |
	|      |                      |       | to the receive shift   |      |
	|      |                      |       | register input. Can be |      |
	|      |                      |       | used in both           |      |
	|      |                      |       | serialslave and        |      |
	|      |                      |       | serial-master modes.   |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0 - Normal Mode      |      |
	|      |                      |       |   Operation            |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1 - Test Mode        |      |
	|      |                      |       |   Operation            |      |
	|      |                      |       |                        |      |
	|      |                      |       | [10] only for slave    |      |
	|      |                      |       | mode.                  |      |
	+------+----------------------+-------+------------------------+------+

To be continued ......

.. _table_ctrlr0_contd_1:
.. table:: CTRLR0, Offset Address: 0x000 (continued)
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	|      |                      |       | [9:8] Transfer Mode.   |      |
	|      |                      |       |                        |      |
	|      |                      |       | Selects the mode of    |      |
	|      |                      |       | transfer for serial    |      |
	|      |                      |       | communication. This    |      |
	|      |                      |       | field does not affect  |      |
	|      |                      |       | the transfer           |      |
	|      |                      |       | duplicity. Only        |      |
	|      |                      |       | indicates whether the  |      |
	|      |                      |       | receive or transmit    |      |
	|      |                      |       | data are valid.        |      |
	|      |                      |       |                        |      |
	|      |                      |       | In transmit-only mode, |      |
	|      |                      |       | data received from the |      |
	|      |                      |       | external device is not |      |
	|      |                      |       | valid and is not       |      |
	|      |                      |       | stored in the receive  |      |
	|      |                      |       | FIFO memory; it is     |      |
	|      |                      |       | overwritten on the     |      |
	|      |                      |       | next transfer.         |      |
	|      |                      |       |                        |      |
	|      |                      |       | In receive-only mode,  |      |
	|      |                      |       | transmitted data are   |      |
	|      |                      |       | not valid. After the   |      |
	|      |                      |       | first write to the     |      |
	|      |                      |       | transmit FIFO, the     |      |
	|      |                      |       | same word is           |      |
	|      |                      |       | retransmitted for the  |      |
	|      |                      |       | duration of the        |      |
	|      |                      |       | transfer.              |      |
	|      |                      |       |                        |      |
	|      |                      |       | In                     |      |
	|      |                      |       | transmit-and-receive   |      |
	|      |                      |       | mode, both transmit    |      |
	|      |                      |       | and receive data are   |      |
	|      |                      |       | valid. The transfer    |      |
	|      |                      |       | continues until the    |      |
	|      |                      |       | transmit FIFO is       |      |
	|      |                      |       | empty. Data received   |      |
	|      |                      |       | from the external      |      |
	|      |                      |       | device are stored into |      |
	|      |                      |       | the receive FIFO       |      |
	|      |                      |       | memory, where it can   |      |
	|      |                      |       | be accessed by the     |      |
	|      |                      |       | host processor.        |      |
	|      |                      |       |                        |      |
	|      |                      |       | In eeprom-read mode,   |      |
	|      |                      |       | receive data is not    |      |
	|      |                      |       | valid while control    |      |
	|      |                      |       | data is being          |      |
	|      |                      |       | transmitted.           |      |
	|      |                      |       |                        |      |
	|      |                      |       | When all control data  |      |
	|      |                      |       | is sent to the EEPROM, |      |
	|      |                      |       | receive data becomes   |      |
	|      |                      |       | valid and transmit     |      |
	|      |                      |       | data becomes invalid.  |      |
	|      |                      |       | All data in the        |      |
	|      |                      |       | transmit FIFO is       |      |
	|      |                      |       | considered control     |      |
	|      |                      |       | data in this mode.     |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 00 - Transmit &      |      |
	|      |                      |       |   Receive              |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 01 - Transmit Only   |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 10 - Receive Only    |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 11 - EEPROM Read     |      |
	|      |                      |       |                        |      |
	|      |                      |       | [7] Serial Clock       |      |
	|      |                      |       | Polarity.              |      |
	|      |                      |       |                        |      |
	|      |                      |       | Valid when the frame   |      |
	|      |                      |       | format (FRF) is set to |      |
	|      |                      |       | Motorola SPI. Used to  |      |
	|      |                      |       | select the polarity of |      |
	|      |                      |       | the inactive serial    |      |
	|      |                      |       | clock, which is held   |      |
	|      |                      |       | inactive when the SPI  |      |
	|      |                      |       | master is not actively |      |
	|      |                      |       | transferring data on   |      |
	|      |                      |       | the serial bus.        |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0 - Inactive state of|      |
	|      |                      |       |   serial clock is low  |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1 - Inactive state of|      |
	|      |                      |       |   serial clock is high |      |
	+------+----------------------+-------+------------------------+------+

To be continued ......

.. _table_ctrlr0_contd_2:
.. table:: CTRLR0, Offset Address: 0x000 (continued)
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+	
	|      |                      |       | [6] Serial Clock       |      |
	|      |                      |       | Phase.                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | Valid when the frame   |      |
	|      |                      |       | format (FRF) is set to |      |
	|      |                      |       | Motorola SPI. The      |      |
	|      |                      |       | serial clock phase     |      |
	|      |                      |       | selects the            |      |
	|      |                      |       | relationship of the    |      |
	|      |                      |       | serial clock with the  |      |
	|      |                      |       | slave select signal.   |      |
	|      |                      |       | When SCPH = 0, data    |      |
	|      |                      |       | are captured on the    |      |
	|      |                      |       | first edge of the      |      |
	|      |                      |       | serial clock. When     |      |
	|      |                      |       | SCPH = 1, the serial   |      |
	|      |                      |       | clock starts toggling  |      |
	|      |                      |       | one cycle after the    |      |
	|      |                      |       | slave select line is   |      |
	|      |                      |       | activated, and data    |      |
	|      |                      |       | are captured on the    |      |
	|      |                      |       | second edge of the     |      |
	|      |                      |       | serial clock.          |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0: Serial clock      |      |
	|      |                      |       |   toggles in middle of |      |
	|      |                      |       |   first data bit       |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1: Serial clock      |      |
	|      |                      |       |   toggles at start of  |      |
	|      |                      |       |   first data bit       |      |
	|      |                      |       |                        |      |
	|      |                      |       | [5:4] Frame Format.    |      |
	|      |                      |       |                        |      |
	|      |                      |       | Selects which serial   |      |
	|      |                      |       | protocol transfers the |      |
	|      |                      |       | data.                  |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 00 - Motorola SPI    |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 01 - Texas           |      |
	|      |                      |       |   Instruments SSP      |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 10 - National        |      |
	|      |                      |       |   Semiconductors       |      |
	|      |                      |       |   Microwire            |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 11 - Reserved        |      |
	|      |                      |       |                        |      |
	|      |                      |       | [3:0] Data Frame Size. |      |
	|      |                      |       |                        |      |
	|      |                      |       | Selects the data frame |      |
	|      |                      |       | length. When the data  |      |
	|      |                      |       | frame size is          |      |
	|      |                      |       | programmed to be less  |      |
	|      |                      |       | than 16 bits, the      |      |
	|      |                      |       | receive data are       |      |
	|      |                      |       | automatically          |      |
	|      |                      |       | right-justified by the |      |
	|      |                      |       | receive logic, with    |      |
	|      |                      |       | the upper bits of the  |      |
	|      |                      |       | receive FIFO           |      |
	|      |                      |       | zero-padded. You must  |      |
	|      |                      |       | right-justify transmit |      |
	|      |                      |       | data before writing    |      |
	|      |                      |       | into the transmit      |      |
	|      |                      |       | FIFO. The transmit     |      |
	|      |                      |       | logic ignores the      |      |
	|      |                      |       | upper unused bits when |      |
	|      |                      |       | transmitting the data. |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0000 Reserved -      |      |
	|      |                      |       |   undefined operation  |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0001 Reserved -      |      |
	|      |                      |       |   undefined operation  |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0010 Reserved -      |      |
	|      |                      |       |   undefined operation  |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0011 4-bit serial    |      |
	|      |                      |       |   data transfer        |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0100 5-bit serial    |      |
	|      |                      |       |   data transfer        |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0101 6-bit serial    |      |
	|      |                      |       |   data transfer        |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0110 7-bit serial    |      |
	|      |                      |       |   data transfer        |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 0111 8-bit serial    |      |
	|      |                      |       |   data transfer        |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1000 9-bit serial    |      |
	|      |                      |       |   data transfer        |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1001 10-bit serial   |      |
	|      |                      |       |   data transfer        |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1010 11-bit serial   |      |
	|      |                      |       |   data transfer        |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1011 12-bit serial   |      |
	|      |                      |       |   data transfer        |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1100 13-bit serial   |      |
	|      |                      |       |   data transfer        |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1101 14-bit serial   |      |
	|      |                      |       |   data transfer        |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1110 15-bit serial   |      |
	|      |                      |       |   data transfer        |      |
	|      |                      |       |                        |      |
	|      |                      |       | - 1111 16-bit serial   |      |
	|      |                      |       |   data transfer        |      |
	+------+----------------------+-------+------------------------+------+
	| 31:16| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

CTRLR1
^^^^^^

.. _table_ctrlr1:
.. table:: CTRLR1, Offset Address: 0x004
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 15:0 | CTRLR1               | R/W   | Number of Data Frames. | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | When TMOD = 10 or TMOD |      |
	|      |                      |       | = 11, this register    |      |
	|      |                      |       | field sets the number  |      |
	|      |                      |       | of data frames to be   |      |
	|      |                      |       | continuously received  |      |
	|      |                      |       | by the SPI. The SPI    |      |
	|      |                      |       | continues to receive   |      |
	|      |                      |       | serial data until the  |      |
	|      |                      |       | number of data frames  |      |
	|      |                      |       | received is equal to   |      |
	|      |                      |       | this register value    |      |
	|      |                      |       | plus 1, which enables  |      |
	|      |                      |       | you to receive up to   |      |
	|      |                      |       | 64 KB of data in a     |      |
	|      |                      |       | continuous transfer.   |      |
	+------+----------------------+-------+------------------------+------+
	| 31:16| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

SPIENR
^^^^^^

.. _table_spienr:
.. table:: SPIENR, Offset Address: 0x008
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | SPIENR               | R/W   | SPI Enable.            | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | Enables and disables   |      |
	|      |                      |       | all SPI operations.    |      |
	|      |                      |       | When disabled, all     |      |
	|      |                      |       | serial transfers are   |      |
	|      |                      |       | halted immediately.    |      |
	|      |                      |       | Transmit and receive   |      |
	|      |                      |       | FIFO buffers are       |      |
	|      |                      |       | cleared when the       |      |
	|      |                      |       | device is disabled. It |      |
	|      |                      |       | is impossible to       |      |
	|      |                      |       | program some of the    |      |
	|      |                      |       | SPI control registers  |      |
	|      |                      |       | when enabled. When     |      |
	|      |                      |       | disabled, the          |      |
	|      |                      |       | spi_sleep output is    |      |
	|      |                      |       | set (after delay) to   |      |
	|      |                      |       | inform the system that |      |
	|      |                      |       | it is safe to remove   |      |
	|      |                      |       | the spi_clk, thus      |      |
	|      |                      |       | saving power           |      |
	|      |                      |       | consumption in the     |      |
	|      |                      |       | system.                |      |
	+------+----------------------+-------+------------------------+------+
	| 31:1 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+


MWCR
^^^^

.. _table_mwcr:
.. table:: MWCR, Offset Address: 0x00c
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 2:0  | MWCR                 | R/W   | [2] Microwire          | 0x0  |
	|      |                      |       | Handshaking.           |      |
	|      |                      |       |                        |      |
	|      |                      |       | Relevant only when the |      |
	|      |                      |       | SPI is configured as a |      |
	|      |                      |       | serial-master device.  |      |
	|      |                      |       | When configured as a   |      |
	|      |                      |       | serial slave, this bit |      |
	|      |                      |       | field has no           |      |
	|      |                      |       | functionality. Used to |      |
	|      |                      |       | enable and disable the |      |
	|      |                      |       | “busy/ready”           |      |
	|      |                      |       | handshaking interface  |      |
	|      |                      |       | for the Microwire      |      |
	|      |                      |       | protocol. When         |      |
	|      |                      |       | enabled, the SPI       |      |
	|      |                      |       | checks for a ready     |      |
	|      |                      |       | status from the target |      |
	|      |                      |       | slave, after the       |      |
	|      |                      |       | transfer of the last   |      |
	|      |                      |       | data/control bit,      |      |
	|      |                      |       | before clearing the    |      |
	|      |                      |       | BUSY status in the SR  |      |
	|      |                      |       | register.              |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0: handshaking         |      |
	|      |                      |       | interface is disabled  |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1: handshaking         |      |
	|      |                      |       | interface is enabled   |      |
	|      |                      |       |                        |      |
	|      |                      |       | [1] Microwire Control. |      |
	|      |                      |       |                        |      |
	|      |                      |       | Defines the direction  |      |
	|      |                      |       | of the data word when  |      |
	|      |                      |       | the Microwire serial   |      |
	|      |                      |       | protocol is used. When |      |
	|      |                      |       | this bit is set to 0,  |      |
	|      |                      |       | the data word is       |      |
	|      |                      |       | received by the SPI    |      |
	|      |                      |       | from the external      |      |
	|      |                      |       | serial device. When    |      |
	|      |                      |       | this bit is set to 1,  |      |
	|      |                      |       | the data word is       |      |
	|      |                      |       | transmitted from the   |      |
	|      |                      |       | SPI to the external    |      |
	|      |                      |       | serial device.         |      |
	|      |                      |       |                        |      |
	|      |                      |       | [0] Microwire Transfer |      |
	|      |                      |       | Mode.                  |      |
	|      |                      |       |                        |      |
	|      |                      |       | Defines whether the    |      |
	|      |                      |       | Microwire transfer is  |      |
	|      |                      |       | sequential or          |      |
	|      |                      |       | non-sequential. When   |      |
	|      |                      |       | sequential mode is     |      |
	|      |                      |       | used, only one control |      |
	|      |                      |       | word is needed to      |      |
	|      |                      |       | transmit or receive a  |      |
	|      |                      |       | block of data words.   |      |
	|      |                      |       | When non-sequential    |      |
	|      |                      |       | mode is used, there    |      |
	|      |                      |       | must be a control word |      |
	|      |                      |       | for each data word     |      |
	|      |                      |       | that is transmitted or |      |
	|      |                      |       | received.              |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 – non-sequential     |      |
	|      |                      |       | transfer               |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 – sequential         |      |
	|      |                      |       | transfer               |      |
	+------+----------------------+-------+------------------------+------+
	| 31:3 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

SER
^^^

.. _table_ser:
.. table:: SER, Offset Address: 0x010
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | SER                  | R/W   | Slave Select Enable    | 0x0  |
	|      |                      |       | Flag.                  |      |
	|      |                      |       |                        |      |
	|      |                      |       | This register          |      |
	|      |                      |       | corresponds to a slave |      |
	|      |                      |       | select line (ss_x_n])  |      |
	|      |                      |       | from the SPI master.   |      |
	|      |                      |       | When this register is  |      |
	|      |                      |       | set (1), the slave     |      |
	|      |                      |       | select line from the   |      |
	|      |                      |       | master is activated    |      |
	|      |                      |       | when a serial transfer |      |
	|      |                      |       | begins. It should be   |      |
	|      |                      |       | noted that setting or  |      |
	|      |                      |       | clearing this register |      |
	|      |                      |       | have no effect on the  |      |
	|      |                      |       | corresponding slave    |      |
	|      |                      |       | select outputs until a |      |
	|      |                      |       | transfer is started.   |      |
	|      |                      |       | Before beginning a     |      |
	|      |                      |       | transfer, you should   |      |
	|      |                      |       | enable this register   |      |
	|      |                      |       | that corresponds to    |      |
	|      |                      |       | the slave device with  |      |
	|      |                      |       | which the master wants |      |
	|      |                      |       | to communicate.        |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1: Selected            |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0: Not Selected        |      |
	+------+----------------------+-------+------------------------+------+
	| 31:1 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

BAUDR
^^^^^

.. _table_baudr:
.. table:: BAUDR, Offset Address: 0x014
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 15:0 | BAUDR                | R/W   | SPI Clock              | 0x0  |
	|      |                      |       | Divider(SCKDV).        |      |
	|      |                      |       |                        |      |
	|      |                      |       | The LSB for this field |      |
	|      |                      |       | is always set to 0 and |      |
	|      |                      |       | is unaffected by a     |      |
	|      |                      |       | write                  |      |
	|      |                      |       | operation, which       |      |
	|      |                      |       | ensures an even value  |      |
	|      |                      |       | is held in this        |      |
	|      |                      |       | register. If the value |      |
	|      |                      |       | is 0, the serial       |      |
	|      |                      |       | output clock           |      |
	|      |                      |       | (sclk_out) is          |      |
	|      |                      |       | disabled. The          |      |
	|      |                      |       | frequency of the       |      |
	|      |                      |       | sclk_out is derived    |      |
	|      |                      |       | from the following     |      |
	|      |                      |       | equation:              |      |
	|      |                      |       |                        |      |
	|      |                      |       | Fsclk_out/SCKDV =      |      |
	|      |                      |       | Fssi_clk               |      |
	|      |                      |       |                        |      |
	|      |                      |       | where SCKDV is any     |      |
	|      |                      |       | even value between 2   |      |
	|      |                      |       | and 65534. For         |      |
	|      |                      |       | example:               |      |
	|      |                      |       |                        |      |
	|      |                      |       | for Fssi_clk =         |      |
	|      |                      |       | 3.6864MHz and SCKDV =2 |      |
	|      |                      |       |                        |      |
	|      |                      |       | Fsclk_out = 3.6864/2 = |      |
	|      |                      |       | 1.8432MHz              |      |
	+------+----------------------+-------+------------------------+------+
	| 31:16| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

TXFTLR
^^^^^^

.. _table_txftlr:
.. table:: TXFTLR, Offset Address: 0x018
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 2:0  | TXFTLR               | R/W   | Transmit FIFO          | 0x0  |
	|      |                      |       | Threshold.             |      |
	|      |                      |       |                        |      |
	|      |                      |       | Controls the level of  |      |
	|      |                      |       | entries (or below) at  |      |
	|      |                      |       | which the transmit     |      |
	|      |                      |       | FIFO controller        |      |
	|      |                      |       | triggers an interrupt. |      |
	|      |                      |       | The FIFO depth is 8;   |      |
	|      |                      |       | If you attempt to set  |      |
	|      |                      |       | this value greater     |      |
	|      |                      |       | than or equal to the   |      |
	|      |                      |       | depth of the FIFO,     |      |
	|      |                      |       | this field is not      |      |
	|      |                      |       | written and retains    |      |
	|      |                      |       | its current value.     |      |
	|      |                      |       | When the number of     |      |
	|      |                      |       | transmit FIFO entries  |      |
	|      |                      |       | is less than or equal  |      |
	|      |                      |       | to this value, the     |      |
	|      |                      |       | transmit FIFO empty    |      |
	|      |                      |       | interrupt is           |      |
	|      |                      |       | triggered.             |      |
	+------+----------------------+-------+------------------------+------+
	| 31:3 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

RXFTLR
^^^^^^

.. _table_rxftlr:
.. table:: RXFTLR, Offset Address: 0x01c
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 2:0  | RXFTLR               | R/W   | Receive FIFO           | 0x0  |
	|      |                      |       | Threshold.             |      |
	|      |                      |       |                        |      |
	|      |                      |       | Controls the level of  |      |
	|      |                      |       | entries (or above) at  |      |
	|      |                      |       | which the receive FIFO |      |
	|      |                      |       | controller triggers an |      |
	|      |                      |       | interrupt. The FIFO    |      |
	|      |                      |       | depth is 8. If you     |      |
	|      |                      |       | attempt to set this    |      |
	|      |                      |       | value greater than the |      |
	|      |                      |       | depth of the FIFO,     |      |
	|      |                      |       | this field is not      |      |
	|      |                      |       | written and retains    |      |
	|      |                      |       | its current value.     |      |
	|      |                      |       | When the number of     |      |
	|      |                      |       | receive FIFO entries   |      |
	|      |                      |       | is greater than or     |      |
	|      |                      |       | equal to this value +  |      |
	|      |                      |       | 1, the receive FIFO    |      |
	|      |                      |       | full interrupt is      |      |
	|      |                      |       | triggered.             |      |
	+------+----------------------+-------+------------------------+------+
	| 31:3 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

TXFLR
^^^^^

.. _table_txflr:
.. table:: TXFLR, Offset Address: 0x020
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 3:0  | TXFLR                | RO    | Transmit FIFO Level.   |      |
	|      |                      |       |                        |      |
	|      |                      |       | Contains the number of |      |
	|      |                      |       | valid data entries in  |      |
	|      |                      |       | the transmit FIFO.     |      |
	+------+----------------------+-------+------------------------+------+
	| 31:4 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

RXFLR
^^^^^
.. _table_rxflr:
.. table:: RXFLR, Offset Address: 0x024
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 3:0  | RXFLR                | RO    | Receive FIFO Level.    |      |
	|      |                      |       |                        |      |
	|      |                      |       | Contains the number of |      |
	|      |                      |       | valid data entries in  |      |
	|      |                      |       | the receive FIFO.      |      |
	+------+----------------------+-------+------------------------+------+
	| 31:4 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

SR
^^
.. _table_sr:
.. table:: SR, Offset Address: 0x028
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 6:0  | SR                   | RO    | [6] Data Collision     |      |
	|      |                      |       | Error.                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | This bit is set if the |      |
	|      |                      |       | SPI master is actively |      |
	|      |                      |       | transmitting when      |      |
	|      |                      |       | another master selects |      |
	|      |                      |       | this device as a       |      |
	|      |                      |       | slave. This informs    |      |
	|      |                      |       | the processor that the |      |
	|      |                      |       | last data transfer was |      |
	|      |                      |       | halted before          |      |
	|      |                      |       | completion. This bit   |      |
	|      |                      |       | is cleared when read.  |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 - No error           |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 - Transmit data      |      |
	|      |                      |       | collision error        |      |
	|      |                      |       |                        |      |
	|      |                      |       | [5] Transmission       |      |
	|      |                      |       | Error.                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | Set if the transmit    |      |
	|      |                      |       | FIFO is empty when a   |      |
	|      |                      |       | transfer is started.   |      |
	|      |                      |       | Data from the previous |      |
	|      |                      |       | transmission is resent |      |
	|      |                      |       | on the txd line. This  |      |
	|      |                      |       | bit is cleared when    |      |
	|      |                      |       | read.                  |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 - No error           |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 - Transmission error |      |
	|      |                      |       |                        |      |
	|      |                      |       | [4] Receive FIFO Full. |      |
	|      |                      |       |                        |      |
	|      |                      |       | When the receive FIFO  |      |
	|      |                      |       | is completely full,    |      |
	|      |                      |       | this bit is set. When  |      |
	|      |                      |       | the receive FIFO       |      |
	|      |                      |       | contains one or more   |      |
	|      |                      |       | empty location, this   |      |
	|      |                      |       | bit is cleared.        |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 - Receive FIFO is    |      |
	|      |                      |       | not full               |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 - Receive FIFO is    |      |
	|      |                      |       | full                   |      |
	|      |                      |       |                        |      |
	|      |                      |       | [3] Receive FIFO Not   |      |
	|      |                      |       | Empty.                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | Set when the receive   |      |
	|      |                      |       | FIFO contains one or   |      |
	|      |                      |       | more entries and is    |      |
	|      |                      |       | cleared when the       |      |
	|      |                      |       | receive FIFO is empty. |      |
	|      |                      |       | This bit can be polled |      |
	|      |                      |       | by software to         |      |
	|      |                      |       | completely empty the   |      |
	|      |                      |       | receive FIFO.          |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 - Receive FIFO is    |      |
	|      |                      |       | empty                  |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 - Receive FIFO is    |      |
	|      |                      |       | not empty              |      |
	|      |                      |       |                        |      |
	|      |                      |       | [2] Transmit FIFO      |      |
	|      |                      |       | Empty.                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | When the transmit FIFO |      |
	|      |                      |       | is completely empty,   |      |
	|      |                      |       | this bit is set. When  |      |
	|      |                      |       | the transmit FIFO      |      |
	|      |                      |       | contains one or more   |      |
	|      |                      |       | valid entries, this    |      |
	|      |                      |       | bit is cleared. This   |      |
	|      |                      |       | bit field does not     |      |
	|      |                      |       | request an interrupt.  |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 - Transmit FIFO is   |      |
	|      |                      |       | not empty              |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 - Transmit FIFO is   |      |
	|      |                      |       | empty                  |      |
	|      |                      |       |                        |      |
	|      |                      |       | [1] Transmit FIFO Not  |      |
	|      |                      |       | Full.                  |      |
	|      |                      |       |                        |      |
	|      |                      |       | Set when the transmit  |      |
	|      |                      |       | FIFO contains one or   |      |
	|      |                      |       | more empty locations,  |      |
	|      |                      |       | and is cleared when    |      |
	|      |                      |       | the FIFO is full.      |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 - Transmit FIFO is   |      |
	|      |                      |       | full                   |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 - Transmit FIFO is   |      |
	|      |                      |       | not full               |      |
	|      |                      |       |                        |      |
	|      |                      |       | [0] SPI Busy Flag.     |      |
	|      |                      |       |                        |      |
	|      |                      |       | When set, indicates    |      |
	|      |                      |       | that a serial transfer |      |
	|      |                      |       | is in progress; when   |      |
	|      |                      |       | cleared indicates that |      |
	|      |                      |       | the SPI is idle or     |      |
	|      |                      |       | disabled.              |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 - SPI is idle or     |      |
	|      |                      |       | disabled               |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 - SPI is actively    |      |
	|      |                      |       | transferring data      |      |
	+------+----------------------+-------+------------------------+------+
	| 31:7 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

IMR
^^^
.. _table_imr:
.. table:: IMR, Offset Address: 0x02c
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 5:0  | IMR                  | R/W   | [5] Multi-Master       | 0x3F |
	|      |                      |       | Contention Interrupt   |      |
	|      |                      |       | Mask.                  |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 - spi_mst_intr       |      |
	|      |                      |       | interrupt is masked    |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 - spi_mst_intr       |      |
	|      |                      |       | interrupt is not       |      |
	|      |                      |       | masked                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | [4] Receive FIFO Full  |      |
	|      |                      |       | Interrupt Mask         |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 - spi_rxf_intr       |      |
	|      |                      |       | interrupt is masked    |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 - spi_rxf_intr       |      |
	|      |                      |       | interrupt is not       |      |
	|      |                      |       | masked                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | [3] Receive FIFO       |      |
	|      |                      |       | Overflow Interrupt     |      |
	|      |                      |       | Mask                   |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 - spi_rxo_intr       |      |
	|      |                      |       | interrupt is masked    |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 - spi_rxo_intr       |      |
	|      |                      |       | interrupt is not       |      |
	|      |                      |       | masked                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | [2] Receive FIFO       |      |
	|      |                      |       | Underflow Interrupt    |      |
	|      |                      |       | Mask                   |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 - spi_rxu_intr       |      |
	|      |                      |       | interrupt is masked    |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 - spi_rxu_intr       |      |
	|      |                      |       | interrupt is not       |      |
	|      |                      |       | masked                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | [1] Transmit FIFO      |      |
	|      |                      |       | Overflow Interrupt     |      |
	|      |                      |       | Mask                   |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 - spi_txo_intr       |      |
	|      |                      |       | interrupt is masked    |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 - spi_txo_intr       |      |
	|      |                      |       | interrupt is not       |      |
	|      |                      |       | masked                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | [0] Transmit FIFO      |      |
	|      |                      |       | Empty Interrupt Mask   |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 - spi_txe_intr       |      |
	|      |                      |       | interrupt is masked    |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 - spi_txe_intr       |      |
	|      |                      |       | interrupt is not       |      |
	|      |                      |       | masked                 |      |
	+------+----------------------+-------+------------------------+------+
	| 31:6 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

ISR
^^^
.. _table_isr:
.. table:: ISR, Offset Address: 0x030
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 5:0  | ISR                  | RO    | [5] Multi-Master       |      |
	|      |                      |       | Contention Interrupt   |      |
	|      |                      |       | Status.                |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = spi_mst_intr       |      |
	|      |                      |       | interrupt not active   |      |
	|      |                      |       | after masking          |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 = spi_mst_intr       |      |
	|      |                      |       | interrupt is active    |      |
	|      |                      |       | after masking          |      |
	|      |                      |       |                        |      |
	|      |                      |       | [4] Receive FIFO Full  |      |
	|      |                      |       | Interrupt Status       |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = spi_rxf_intr       |      |
	|      |                      |       | interrupt is not       |      |
	|      |                      |       | active after masking   |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 = spi_rxf_intr       |      |
	|      |                      |       | interrupt is full      |      |
	|      |                      |       | after masking          |      |
	|      |                      |       |                        |      |
	|      |                      |       | [3] Receive FIFO       |      |
	|      |                      |       | Overflow Interrupt     |      |
	|      |                      |       | Status                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = spi_rxo_intr       |      |
	|      |                      |       | interrupt is not       |      |
	|      |                      |       | active after masking   |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 = spi_rxo_intr       |      |
	|      |                      |       | interrupt is active    |      |
	|      |                      |       | after masking          |      |
	|      |                      |       |                        |      |
	|      |                      |       | [2] Receive FIFO       |      |
	|      |                      |       | Underflow Interrupt    |      |
	|      |                      |       | Status                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = spi_rxu_intr       |      |
	|      |                      |       | interrupt is not       |      |
	|      |                      |       | active after masking   |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 = spi_rxu_intr       |      |
	|      |                      |       | interrupt is active    |      |
	|      |                      |       | after masking          |      |
	|      |                      |       |                        |      |
	|      |                      |       | [1] Transmit FIFO      |      |
	|      |                      |       | Overflow Interrupt     |      |
	|      |                      |       | Status                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = spi_txo_intr       |      |
	|      |                      |       | interrupt is not       |      |
	|      |                      |       | active after masking   |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 = spi_txo_intr       |      |
	|      |                      |       | interrupt is active    |      |
	|      |                      |       | after masking          |      |
	|      |                      |       |                        |      |
	|      |                      |       | [0] Transmit FIFO      |      |
	|      |                      |       | Empty Interrupt Status |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = spi_txe_intr       |      |
	|      |                      |       | interrupt is not       |      |
	|      |                      |       | active after masking   |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 = spi_txe_intr       |      |
	|      |                      |       | interrupt is active    |      |
	|      |                      |       | after masking          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:6 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

RISR
^^^^
.. _table_risr:
.. table:: RISR, Offset Address: 0x034
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 5:0  | RISR                 | RO    | [5] Multi-Master       |      |
	|      |                      |       | Contention Raw         |      |
	|      |                      |       | Interrupt Status.      |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = spi_mst_intr       |      |
	|      |                      |       | interrupt is not       |      |
	|      |                      |       | active prior to        |      |
	|      |                      |       | masking                |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 = spi_mst_intr       |      |
	|      |                      |       | interrupt is active    |      |
	|      |                      |       | prior masking          |      |
	|      |                      |       |                        |      |
	|      |                      |       | [4] Receive FIFO Full  |      |
	|      |                      |       | Raw Interrupt Status   |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = spi_rxf_intr       |      |
	|      |                      |       | interrupt is not       |      |
	|      |                      |       | active prior to        |      |
	|      |                      |       | masking                |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 = spi_rxf_intr       |      |
	|      |                      |       | interrupt is active    |      |
	|      |                      |       | prior to masking       |      |
	|      |                      |       |                        |      |
	|      |                      |       | [3] Receive FIFO       |      |
	|      |                      |       | Overflow Raw Interrupt |      |
	|      |                      |       | Status                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = spi_rxo_intr       |      |
	|      |                      |       | interrupt is not       |      |
	|      |                      |       | active prior to        |      |
	|      |                      |       | masking                |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 = spi_rxo_intr       |      |
	|      |                      |       | interrupt is active    |      |
	|      |                      |       | prior masking          |      |
	|      |                      |       |                        |      |
	|      |                      |       | [2] Receive FIFO       |      |
	|      |                      |       | Underflow Raw          |      |
	|      |                      |       | Interrupt Status       |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = spi_rxu_intr       |      |
	|      |                      |       | interrupt is not       |      |
	|      |                      |       | active prior to        |      |
	|      |                      |       | masking                |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 = spi_rxu_intr       |      |
	|      |                      |       | interrupt is active    |      |
	|      |                      |       | prior to masking       |      |
	|      |                      |       |                        |      |
	|      |                      |       | [1] Transmit FIFO      |      |
	|      |                      |       | Overflow Raw Interrupt |      |
	|      |                      |       | Status                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = spi_txo_intr       |      |
	|      |                      |       | interrupt is not       |      |
	|      |                      |       | active prior to        |      |
	|      |                      |       | masking                |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 = spi_txo_intr       |      |
	|      |                      |       | interrupt is active    |      |
	|      |                      |       | prior masking          |      |
	|      |                      |       |                        |      |
	|      |                      |       | [0] Transmit FIFO      |      |
	|      |                      |       | Empty Raw Interrupt    |      |
	|      |                      |       | Status                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = spi_txe_intr       |      |
	|      |                      |       | interrupt is not       |      |
	|      |                      |       | active prior to        |      |
	|      |                      |       | masking                |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 = spi_txe_intr       |      |
	|      |                      |       | interrupt is active    |      |
	|      |                      |       | prior masking          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:6 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

TXOICR
^^^^^^
.. _table_txoicr:
.. table:: TXOICR, Offset Address: 0x038
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | TXOICR               | RO    | Clear Transmit FIFO    |      |
	|      |                      |       | Overflow Interrupt.    |      |
	|      |                      |       |                        |      |
	|      |                      |       | This register reflects |      |
	|      |                      |       | the status of the      |      |
	|      |                      |       | interrupt. A read from |      |
	|      |                      |       | this register clears   |      |
	|      |                      |       | the spi_txo_intr       |      |
	|      |                      |       | interrupt; writing has |      |
	|      |                      |       | no effect.             |      |
	+------+----------------------+-------+------------------------+------+
	| 31:1 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

RXOICR
^^^^^^
.. _table_rxoicr:
.. table:: RXOICR, Offset Address: 0x03c
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | RXOICR               | RO    | Clear Receive FIFO     |      |
	|      |                      |       | Overflow Interrupt.    |      |
	|      |                      |       |                        |      |
	|      |                      |       | This register reflects |      |
	|      |                      |       | the status of the      |      |
	|      |                      |       | interrupt.             |      |
	|      |                      |       |                        |      |
	|      |                      |       | A read from this       |      |
	|      |                      |       | register clears the    |      |
	|      |                      |       | spi_rxo_intr           |      |
	|      |                      |       | interrupt; writing has |      |
	|      |                      |       | no effect.             |      |
	+------+----------------------+-------+------------------------+------+
	| 31:1 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

RXUICR
^^^^^^
.. _table_rxuicr:
.. table:: RXUICR, Offset Address: 0x040
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | RXUICR               | RO    | Clear Receive FIFO     |      |
	|      |                      |       | Underflow Interrupt.   |      |
	|      |                      |       |                        |      |
	|      |                      |       | This register reflects |      |
	|      |                      |       | the status of the      |      |
	|      |                      |       | interrupt.             |      |
	|      |                      |       |                        |      |
	|      |                      |       | A read from this       |      |
	|      |                      |       | register clears the    |      |
	|      |                      |       | spi_rxu_intr           |      |
	|      |                      |       | interrupt; writing has |      |
	|      |                      |       | no effect.             |      |
	+------+----------------------+-------+------------------------+------+
	| 31:1 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

MSTICR
^^^^^^
.. _table_msticr:
.. table:: MSTICR, Offset Address: 0x044
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | MSTICR               | RO    | Clear Multi-Master     |      |
	|      |                      |       | Contention Interrupt.  |      |
	|      |                      |       |                        |      |
	|      |                      |       | This register reflects |      |
	|      |                      |       | the status of the      |      |
	|      |                      |       | interrupt.             |      |
	|      |                      |       |                        |      |
	|      |                      |       | A read from this       |      |
	|      |                      |       | register clears the    |      |
	|      |                      |       | spi_mst_intr           |      |
	|      |                      |       | interrupt; writing has |      |
	|      |                      |       | no effect.             |      |
	+------+----------------------+-------+------------------------+------+
	| 31:1 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

ICR
^^^
.. _table_icr:
.. table:: ICR, Offset Address: 0x048
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | ICR                  | RO    | Clear Interrupts.      |      |
	|      |                      |       |                        |      |
	|      |                      |       | This register is set   |      |
	|      |                      |       | if any of the          |      |
	|      |                      |       | interrupts below are   |      |
	|      |                      |       | active. A read clears  |      |
	|      |                      |       | the spi_txo_intr,      |      |
	|      |                      |       | spi_rxu_intr,          |      |
	|      |                      |       | spi_rxo_intr, and the  |      |
	|      |                      |       | spi_mst_intr           |      |
	|      |                      |       | interrupts. Writing to |      |
	|      |                      |       | this register has no   |      |
	|      |                      |       | effect.                |      |
	+------+----------------------+-------+------------------------+------+
	| 31:1 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

DMACR
^^^^^

.. _table_dmacr:
.. table:: DMACR, Offset Address: 0x04c
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 1:0  | DMACR                | R/W   | [1] Transmit DMA       | 0x0  |
	|      |                      |       | Enable.                |      |
	|      |                      |       |                        |      |
	|      |                      |       | This bit               |      |
	|      |                      |       | enables/disables the   |      |
	|      |                      |       | transmit FIFO DMA      |      |
	|      |                      |       | channel.               |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = Transmit DMA       |      |
	|      |                      |       | disabled               |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 = Transmit DMA       |      |
	|      |                      |       | enabled                |      |
	|      |                      |       |                        |      |
	|      |                      |       | [0] Receive DMA        |      |
	|      |                      |       | Enable.                |      |
	|      |                      |       |                        |      |
	|      |                      |       | This bit               |      |
	|      |                      |       | enables/disables the   |      |
	|      |                      |       | receive FIFO DMA       |      |
	|      |                      |       | channel                |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = Receive DMA        |      |
	|      |                      |       | disabled               |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 = Receive DMA        |      |
	|      |                      |       | enabled                |      |
	+------+----------------------+-------+------------------------+------+
	| 31:2 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+


DMATDLR
^^^^^^^

.. _table_dmatdlr:
.. table:: DMATDLR, Offset Address: 0x050
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 2:0  | DMATDLR              | R/W   | Transmit Data Level.   | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | This bit field         |      |
	|      |                      |       | controls the level at  |      |
	|      |                      |       | which a DMA request is |      |
	|      |                      |       | made by the transmit   |      |
	|      |                      |       | logic. It is equal to  |      |
	|      |                      |       | the watermark level;   |      |
	|      |                      |       | that is, the           |      |
	|      |                      |       | dma_tx_req signal is   |      |
	|      |                      |       | generated when the     |      |
	|      |                      |       | number of valid data   |      |
	|      |                      |       | entries in the         |      |
	|      |                      |       | transmit FIFO is equal |      |
	|      |                      |       | to or below this field |      |
	|      |                      |       | value, and TDMAE = 1.  |      |
	+------+----------------------+-------+------------------------+------+
	| 31:3 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

DMARDLR
^^^^^^^

.. _table_dmardlr:
.. table:: DMARDLR, Offset Address: 0x054
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 2:0  | DMARDLR              | R/W   | Receive Data Level.    | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | This bit field         |      |
	|      |                      |       | controls the level at  |      |
	|      |                      |       | which a DMA request is |      |
	|      |                      |       | made by the receive    |      |
	|      |                      |       | logic. The watermark   |      |
	|      |                      |       | level = DMARDL+1; that |      |
	|      |                      |       | is, dma_rx_req is      |      |
	|      |                      |       | generated when the     |      |
	|      |                      |       | number of valid data   |      |
	|      |                      |       | entries in the receive |      |
	|      |                      |       | FIFO is equal to or    |      |
	|      |                      |       | above this field value |      |
	|      |                      |       | + 1, and RDMAE=1.      |      |
	+------+----------------------+-------+------------------------+------+
	| 31:3 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

DR
^^

.. _table_dr:
.. table:: DR, Offset Address: 0x060
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 15:0 | DR                   | R/W   | Data Register.         | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | When writing to this   |      |
	|      |                      |       | register, you must     |      |
	|      |                      |       | right-justify the      |      |
	|      |                      |       | data. Read data are    |      |
	|      |                      |       | automatically          |      |
	|      |                      |       | right-justified.       |      |
	|      |                      |       |                        |      |
	|      |                      |       | Read = Receive FIFO    |      |
	|      |                      |       | buffer                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | Write = Transmit FIFO  |      |
	|      |                      |       | buffer                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | Note :                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | The DR register in the |      |
	|      |                      |       | SPI occupies           |      |
	|      |                      |       | thirty-six 32-bit      |      |
	|      |                      |       | address locations of   |      |
	|      |                      |       | the memory map to      |      |
	|      |                      |       | facilitate AHB burst   |      |
	|      |                      |       | transfers. Writing to  |      |
	|      |                      |       | any of these address   |      |
	|      |                      |       | locations has the same |      |
	|      |                      |       | effect as pushing the  |      |
	|      |                      |       | data from the pwdata   |      |
	|      |                      |       | bus into the transmit  |      |
	|      |                      |       | FIFO. Reading from any |      |
	|      |                      |       | of these locations has |      |
	|      |                      |       | the same effect as     |      |
	|      |                      |       | popping data from the  |      |
	|      |                      |       | receive FIFO onto the  |      |
	|      |                      |       | prdata bus.            |      |
	+------+----------------------+-------+------------------------+------+
	| 31:16| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

RX_SAMPLE_DLY
^^^^^^^^^^^^^

.. _table_rx_sample_dly:
.. table:: RX_SAMPLE_DLY, Offset Address: 0x0f0
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 7:0  | RX_SAMPLE_DLY        | R/W   | Receive Data (rxd)     | 0x0  |
	|      |                      |       | Sample Delay.          |      |
	|      |                      |       |                        |      |
	|      |                      |       | This register is used  |      |
	|      |                      |       | to delay the sample of |      |
	|      |                      |       | the rxd input signal.  |      |
	|      |                      |       | Each value represents  |      |
	|      |                      |       | a single ssi_clk delay |      |
	|      |                      |       | on the sample of the   |      |
	|      |                      |       | rxd signal.            |      |
	|      |                      |       |                        |      |
	|      |                      |       | NOTE: If this register |      |
	|      |                      |       | is programmed with a   |      |
	|      |                      |       | value that exceeds the |      |
	|      |                      |       | depth of the internal  |      |
	|      |                      |       | shift registers (DEPTH |      |
	|      |                      |       | = 8), a zero (0) delay |      |
	|      |                      |       | will be applied to the |      |
	|      |                      |       | rxd sample.            |      |
	+------+----------------------+-------+------------------------+------+
	| 31:8 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
