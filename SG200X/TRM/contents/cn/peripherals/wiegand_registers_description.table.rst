TX_CONFIG0
^^^^^^^^^^

.. _table_wiegand_tx_config0:
.. table:: TX_CONFIG0, Offset Address: 0x000
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 23:0 | reg_tx_lowtime       | R/W   | TX Low width , unit =  | 0xff |
	|      |                      |       | cycle                  |      |
	+------+----------------------+-------+------------------------+------+
	| 31:24| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

TX_CONFIG1
^^^^^^^^^^

.. _table_wiegand_tx_config1:
.. table:: TX_CONFIG1, Offset Address: 0x004
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 23:0 | reg_tx_hightime      | R/W   | TX High width , unit = | 0xff |
	|      |                      |       | cycle                  |      |
	+------+----------------------+-------+------------------------+------+
	| 31:24| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

TX_CONFIG2
^^^^^^^^^^

.. _table_wiegand_tx_config2:
.. table:: TX_CONFIG2, Offset Address: 0x008
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 6:0  | reg_tx_bitcount      | R/W   | TX Frame bit count per | 0x18 |
	|      |                      |       | transmit , unit = bit  |      |
	+------+----------------------+-------+------------------------+------+
	| 7    | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 8    | reg_tx_msb1st        | R/W   | TX Transmit from MSB   | 0x0  |
	|      |                      |       | or LSB                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 : LSB 1st , from     |      |
	|      |                      |       | tx_buffer[0] -->       |      |
	|      |                      |       | tx_b                   |      |
	|      |                      |       | uffer[reg_tx_bitcount] |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 : MSB 1st , from     |      |
	|      |                      |       | tx_b                   |      |
	|      |                      |       | uffer[reg_tx_bitcount] |      |
	|      |                      |       | --> tx_buffer[0]       |      |
	+------+----------------------+-------+------------------------+------+
	| 15:9 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 16   | reg_tx_opendrain     | R/W   | TX using push-pull     | 0x0  |
	|      |                      |       | mode or opendrain mode |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 : push-pull mode     |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 : opendrain mode     |      |
	+------+----------------------+-------+------------------------+------+
	| 31:17| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

TX_BUFFER
^^^^^^^^^

.. _table_wiegand_tx_buffer:
.. table:: TX_BUFFER, Offset Address: 0x00c
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 63:0 | reg_tx_buffer        | R/W   | TX buffer content      | 0x00 |
	+------+----------------------+-------+------------------------+------+

TX_TRIG
^^^^^^^

.. _table_wiegand_tx_trig:
.. table:: TX_TRIG, Offset Address: 0x014
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 0    | reg_tx_trig_w1t      | W1T   | Trigger transmittion   |      |
	|      |                      |       |                        |      |
	|      |                      |       | Write 1 trigger        |      |
	|      |                      |       | (please check          |      |
	|      |                      |       | reg_tx_busy before     |      |
	|      |                      |       | transmit)              |      |
	+------+----------------------+-------+------------------------+------+
	| 31:1 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

TX_BUSY
^^^^^^^

.. _table_wiegand_tx_busy:
.. table:: TX_BUSY, Offset Address: 0x018
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 0    | reg_tx_busy          | RO    | 0 = idle, allow to     |      |
	|      |                      |       | trigger transmission   |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 = busy, do not       |      |
	|      |                      |       | trigger any more       |      |
	|      |                      |       | tranmission or it will |      |
	|      |                      |       | be ignore.             |      |
	+------+----------------------+-------+------------------------+------+
	| 31:1 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

TX_BUSY
^^^^^^^

.. _table_wiegand_tx_debug:
.. table:: TX_DEBUG, Offset Address: 0x01c
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 2:0  | reg_tx_fsm           | RO    | TX Finite State        |      |
	|      |                      |       | Machine current state  |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 : idle               |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 : wait bus idle      |      |
	|      |                      |       |                        |      |
	|      |                      |       | 2 : tx_start           |      |
	|      |                      |       |                        |      |
	|      |                      |       | 3 : transmit low       |      |
	|      |                      |       |                        |      |
	|      |                      |       | 4 : transmit high      |      |
	|      |                      |       |                        |      |
	|      |                      |       | 5 : tx_stop            |      |
	+------+----------------------+-------+------------------------+------+
	| 7:3  | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 14:8 | reg_tx_pointer       | RO    | TX pointer current     |      |
	|      |                      |       | position               |      |
	|      |                      |       |                        |      |
	|      |                      |       | indicate how many bit  |      |
	|      |                      |       | is still not yet send  |      |
	+------+----------------------+-------+------------------------+------+
	| 31:15| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

RX_CONFIG0
^^^^^^^^^^

.. _table_wiegand_rx_config0:
.. table:: RX_CONFIG0, Offset Address: 0x020
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 15:0 | reg_rx_debounce      | R/W   | RX input debounce time | 0xff |
	|      |                      |       | (unit is cycle)        |      |
	+------+----------------------+-------+------------------------+------+
	| 31:16| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

RX_CONFIG1
^^^^^^^^^^

.. _table_wiegand_rx_config1:
.. table:: RX_CONFIG1, Offset Address: 0x024
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 31:0 | reg_idle_timeout     | R/W   | Bus timeout cycle      | 0    |
	|      |                      |       | count                  | xfff |
	|      |                      |       |                        |      |
	|      |                      |       | When bus is idle for   |      |
	|      |                      |       | idle_timeout cycle,    |      |
	|      |                      |       | bus is expected to be  |      |
	|      |                      |       | back to idle           |      |
	|      |                      |       |                        |      |
	|      |                      |       | If some bit has        |      |
	|      |                      |       | received but not yet   |      |
	|      |                      |       | accumulate to          |      |
	|      |                      |       | rx_bitcount, it will   |      |
	|      |                      |       | also treat as a        |      |
	|      |                      |       | complete packet.       |      |
	+------+----------------------+-------+------------------------+------+


RX_CONFIG2
^^^^^^^^^^

.. _table_wiegand_rx_config2:
.. table:: RX_CONFIG2, Offset Address: 0x028
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 6:0  | reg_rx_bitcount      | R/W   | RX Expected Frame bit  | 0x18 |
	|      |                      |       | count , unit = bit     |      |
	+------+----------------------+-------+------------------------+------+
	| 7    | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 8    | reg_rx_msb1st        | R/W   | RX Received sequence   | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | 0 : LSB 1st, 1st data  |      |
	|      |                      |       | is put in              |      |
	|      |                      |       | reg_rx                 |      |
	|      |                      |       | _buffer[0]->[1]->[2]…. |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 : MSB 1st, 1st data  |      |
	|      |                      |       | is put in              |      |
	|      |                      |       | reg_rx_buffer          |      |
	|      |                      |       | [reg_rx_bitcount]->[0] |      |
	+------+----------------------+-------+------------------------+------+
	| 11:9 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 12   | reg_rx_enable        | R/W   | RX Enable              | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | 0 : disable            |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 : Enable             |      |
	+------+----------------------+-------+------------------------+------+
	| 31:13| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

RX_BUFFER
^^^^^^^^^

.. _table_wiegand_rx_buffer:
.. table:: RX_BUFFER, Offset Address: 0x02c
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 72:0 | reg_rx_buffer        | RO    | RX Buffer              |      |
	|      |                      |       |                        |      |
	|      |                      |       | [63:0] = fifo =        |      |
	|      |                      |       | Indicate received      |      |
	|      |                      |       | content                |      |
	|      |                      |       |                        |      |
	|      |                      |       | [70:64] =              |      |
	|      |                      |       | fifo_bit_count = How   |      |
	|      |                      |       | many effective bit is  |      |
	|      |                      |       | in rx_buffer[63:0]     |      |
	|      |                      |       |                        |      |
	|      |                      |       | [71] = idle_reach =    |      |
	|      |                      |       | This RX is terminate   |      |
	|      |                      |       | by bus idle timeout    |      |
	|      |                      |       |                        |      |
	|      |                      |       | [72] = overflow = This |      |
	|      |                      |       | RX just overwrite an   |      |
	|      |                      |       | un-read message        |      |
	+------+----------------------+-------+------------------------+------+
	| 95:73| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

RX_BUFFER_VALID
^^^^^^^^^^^^^^^

.. _table_wiegand_rx_buffer_valid:
.. table:: RX_BUFFER_VALID, Offset Address: 0x038
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 0    | reg_rx_buffer_valid  | RO    | reg_rx_buffer          |      |
	|      |                      |       | validness              |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 : not valid          |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 : valid              |      |
	+------+----------------------+-------+------------------------+------+
	| 31:1 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

RX_BUFFER_CLEAR
^^^^^^^^^^^^^^^

.. _table_wiegand_rx_buffer_clear:
.. table:: RX_BUFFER_CLEAR, Offset Address: 0x03c
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 0    | reg\                 | W1T   | reg_rx_buffer clear    |      |
	|      | _rx_buffer_clear_w1t |       | (write 1 clear)        |      |
	+------+----------------------+-------+------------------------+------+
	| 31:1 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

RX_DEBUG
^^^^^^^^

.. _table_wiegand_rx_debug:
.. table:: RX_DEBUG, Offset Address: 0x040
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 0    | reg_businidle        | RO    | bus in idle indication |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 : bus is not in idle |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 : bus is in idle     |      |
	|      |                      |       | more than              |      |
	|      |                      |       | reg_rx_idle_timeout    |      |
	|      |                      |       | cycle                  |      |
	+------+----------------------+-------+------------------------+------+
	| 31:1 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

IRQ_ENABLE
^^^^^^^^^^

.. _table_wiegand_irq_enable:
.. table:: IRQ_ENABLE, Offset Address: 0x044
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 0    | reg_irq\             | R/W   | TX Finish IRQ Enable   | 0x0  |
	|      | _tx_finish_enable    |       | (to inform all data    |      |
	|      |                      |       | has being transmit,    |      |
	|      |                      |       | ready for next)        |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 : Disable            |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 : Enable             |      |
	+------+----------------------+-------+------------------------+------+
	| 3:1  | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 4    | reg_ir\              | R/W   | RX Overflow IRQ Enable | 0x0  |
	|      | q_rx_overflow_enable |       |                        |      |
	|      |                      |       | 0 : Disable            |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 : Enable             |      |
	+------+----------------------+-------+------------------------+------+
	| 7:5  | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 8    | reg_ir\              | R/W   | RX Received IRQ Enable | 0x0  |
	|      | q_rx_received_enable |       |                        |      |
	|      |                      |       | 0 : Disable            |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 : Enable             |      |
	+------+----------------------+-------+------------------------+------+
	| 31:9 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

IRQ_FLAG
^^^^^^^^

.. _table_wiegand_irq_flag:
.. table:: IRQ_FLAG, Offset Address: 0x048
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 0    | reg_irq_tx_finish    | RO    | TX Finish IRQ Flag     |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 : no IRQ             |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 : IRQ (one           |      |
	|      |                      |       | tranmission has being  |      |
	|      |                      |       | completed)             |      |
	+------+----------------------+-------+------------------------+------+
	| 3:1  | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 4    | reg_irq_rx_overflow  | RO    | RX overflow IRQ Flag   |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 : no IRQ             |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 : IRQ (rx buffer is  |      |
	|      |                      |       | not pop and new data   |      |
	|      |                      |       | has overwrited)        |      |
	+------+----------------------+-------+------------------------+------+
	| 7:5  | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 8    | reg_irq_rx_received  | RO    | RX received IRQ Flag   |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 : no IRQ             |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 : RX buffer has new  |      |
	|      |                      |       | data                   |      |
	+------+----------------------+-------+------------------------+------+
	| 31:9 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

IRQ_CLEAR
^^^^^^^^^

.. _table_wiegand_irq_clear:
.. table:: IRQ_CLEAR, Offset Address: 0x04c
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 0    | reg_irq\             | W1T   | TX Finish IRQ Clear ,  |      |
	|      | _tx_finish_clear_w1t |       | Write 1 to clear       |      |
	|      |                      |       | reg_irq_tx_finish flag |      |
	+------+----------------------+-------+------------------------+------+
	| 3:1  | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 4    | reg_irq_r\           | W1T   | RX Overflow IRQ Clear  |      |
	|      | x_overflow_clear_w1t |       | . Write 1 to clear     |      |
	|      |                      |       | reg_irq_rx_overflow    |      |
	|      |                      |       | flag                   |      |
	+------+----------------------+-------+------------------------+------+
	| 7:5  | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
	| 8    | reg_irq_r\           | W1T   | RX Received IRQ Clear  |      |
	|      | x_received_clear_w1t |       | . Write 1 to clear     |      |
	|      |                      |       | reg_irq_rx_received    |      |
	|      |                      |       | flag                   |      |
	+------+----------------------+-------+------------------------+------+
	| 31:9 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
