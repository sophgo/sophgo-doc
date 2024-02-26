Wiegand
-------

Overview
~~~~~~~~

.. _diagram_wiegand_trasfer:
.. figure:: ../../../../media/image137.png
	:align: center

	The way wiegand signal bus transmits 0/1

The Wiegand interface uses two single-ended signals, D0/D1. When the bus is idle, it is always high. A low pulse appears on D0, which means a "0" is transmitted. A low pulse is found on D1, which means a "1" is transmitted.

Wiegand is commonly used in access control systems. There are two commonly used formats, Wiegand 26/34, which represent the number of bits in the packet respectively. An introduction to these two formats is as follows.

Wiegand 26
^^^^^^^^^^

.. _diagram_wiegand26_format:
.. figure:: ../../../../media/image138.png
	:align: center

	Wiegand 26 format

Wiegand 34
^^^^^^^^^^

.. _diagram_wiegand_34_format:
.. figure:: ../../../../media/image139.png
	:align: center

	Wiegand 34 format

F = Facility Code

U = User code

Some access cards have a string of numbers behind them. After converting them into hex,

Dec 0002262506   Hex : 22_85_EA

0x22 is Facility code (Dec = 34)

0x85EA is user code (Dec = 34282)

.. _diagram_wiegand_meaning:
.. figure:: ../../../../media/image140.png
	:align: center

	Common magnetic cards, the digital meaning of magnetic buckles

The 34 and 34282 seen later are the Facility code & user code that were disassembled and expressed in decimal again.

Note: This IP TX RX does not handle parity insert or checking, which are all handled by software.

Way of Working
~~~~~~~~~~~~~~

.. _diagram_wiegand_block:
.. figure:: ../../../../media/image141.png
	:align: center

	wiegand architecture block diagram

The Wiegand module contains TX and RX and can be used in one or two directions. When TX goes out, RX will block it, so RX will not receive the signal it sends. The TX supports push pull mode or open drain mode.

TX
^^

Before TX, set the high time and low time of TX, and the number of bits in the packet is determined by MSB 1\ :sup:`st` or LSB 1\ :sup:`st`. Then put the data in the TX_BUFFER register and use TX_TRIG to send the data.

After the complete TX transmission is completed, you can rely on the interrupt of TX finish or the status of polling TX_BUSY to determine when the next packet can be sent.

RX
^^

Before RX, set the debounce time and the number of bits expected to receive the packet. When D0 D1 has a low pulse, RX starts pushing data into the temp buffer. When the number of received bits reaches the expected number of bits for a packet, the temp buffer will be pushed into RX_BUFFER, an interrupt will be issued, and the software will be asked to process it. The temp buffer continues to receive the next data.

If an idle timeout occurs on D0 D1, even if the number of bits has not been reached, it will be forced to be regarded as a packet.

The high bits of the RX BUFFER will record the total number of bits received by this packet, whether it is caused by timeout, or an overflow occurs before the software reads it.

Each time a packet is received, you can rely on the rx_buffer_rececived interrupt or RX_BUFFER_VALID to determine whether there is valid data in RX_BUFFER. After the RX Data is taken away, trigger RX_BUFFER_CLEAR to clear RX_BUFFER to receive the next packet.

Wiegand Register Overview
~~~~~~~~~~~~~~~~~~~~~~~~~

.. This table is very small and no longer included in the file

.. _table_wiegand_registers_overviews:
.. table:: Wiegand Registers Overview
	:widths: 3 3 4

	+----------------------+---------+------------------------------------+
	| Name                 | Address | Description                        |
	|                      | Offset  |                                    |
	+======================+=========+====================================+
	| TX_CONFIG0           | 0x000   |                                    |
	+----------------------+---------+------------------------------------+
	| TX_CONFIG1           | 0x004   |                                    |
	+----------------------+---------+------------------------------------+
	| TX_CONFIG2           | 0x008   |                                    |
	+----------------------+---------+------------------------------------+
	| TX_BUFFER            | 0x00c   |                                    |
	+----------------------+---------+------------------------------------+
	| TX_TRIG              | 0x014   |                                    |
	+----------------------+---------+------------------------------------+
	| TX_BUSY              | 0x018   |                                    |
	+----------------------+---------+------------------------------------+
	| TX_DEBUG             | 0x01c   |                                    |
	+----------------------+---------+------------------------------------+
	| RX_CONFIG0           | 0x020   |                                    |
	+----------------------+---------+------------------------------------+
	| RX_CONFIG1           | 0x024   |                                    |
	+----------------------+---------+------------------------------------+
	| RX_CONFIG2           | 0x028   |                                    |
	+----------------------+---------+------------------------------------+
	| RX_BUFFER            | 0x02c   |                                    |
	+----------------------+---------+------------------------------------+
	| RX_BUFFER_VALID      | 0x038   |                                    |
	+----------------------+---------+------------------------------------+
	| RX_BUFFER_CLEAR      | 0x03c   |                                    |
	+----------------------+---------+------------------------------------+
	| RX_DEBUG             | 0x040   |                                    |
	+----------------------+---------+------------------------------------+
	| IRQ_ENABLE           | 0x044   |                                    |
	+----------------------+---------+------------------------------------+
	| IRQ_FLAG             | 0x048   |                                    |
	+----------------------+---------+------------------------------------+
	| IRQ_CLEAR            | 0x04c   |                                    |
	+----------------------+---------+------------------------------------+

Wiegand Register Description
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../../contents-share/peripherals/wiegand_registers_description.table.rst
