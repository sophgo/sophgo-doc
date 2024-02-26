RBR_THR_DLL
^^^^^^^^^^^

.. _table_uart_rbr_thr_dll:
.. table:: RBR_THR_DLL, Offset Address: 0x000
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 7:0  | RBR_THR_DLL          | R/W   | LCR[7] bit = 0 : (R)   | 0x0  |
	|      |                      |       | Receive Buffer         |      |
	|      |                      |       | Register ,Data byte    |      |
	|      |                      |       | received on the serial |      |
	|      |                      |       | input port             |      |
	|      |                      |       |                        |      |
	|      |                      |       | (W)Transmit Holding    |      |
	|      |                      |       | Register,Data to be    |      |
	|      |                      |       | transmitted on the     |      |
	|      |                      |       | serial output port     |      |
	|      |                      |       |                        |      |
	|      |                      |       | LCR[7] bit = 1 : Lower |      |
	|      |                      |       | 8 bits of a 16-bit     |      |
	|      |                      |       | Divisor Latch register |      |
	|      |                      |       | that contains the baud |      |
	|      |                      |       | rate                   |      |
	|      |                      |       |                        |      |
	|      |                      |       | divisor for the UART   |      |
	+------+----------------------+-------+------------------------+------+
	| 31:8 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

IER_DLH
^^^^^^^

.. _table_uart_ier_dlh:
.. table:: IER_DLH, Offset Address: 0x004
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 7:0  | IER_DLH              | R/W   | LCR[7] bit = 0 :       | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | IER[0] : Enable        |      |
	|      |                      |       | Received Data          |      |
	|      |                      |       | Available Interrupt.   |      |
	|      |                      |       |                        |      |
	|      |                      |       | IER[1] : Enable        |      |
	|      |                      |       | Transmit Holding       |      |
	|      |                      |       | Register Empty         |      |
	|      |                      |       | Interrupt.             |      |
	|      |                      |       |                        |      |
	|      |                      |       | IER[2] : Enable        |      |
	|      |                      |       | Receiver Line Status   |      |
	|      |                      |       | Interrupt.             |      |
	|      |                      |       |                        |      |
	|      |                      |       | IER[3] : Enable Modem  |      |
	|      |                      |       | Status Interrupt.      |      |
	|      |                      |       |                        |      |
	|      |                      |       | IER[7] : Programmable  |      |
	|      |                      |       | THRE Interrupt Mode    |      |
	|      |                      |       | Enable                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | LCR[7] bit = 1 : Upper |      |
	|      |                      |       | 8-bits of a 16-bit     |      |
	|      |                      |       | Divisor Latch register |      |
	|      |                      |       | that contains the baud |      |
	|      |                      |       | rate                   |      |
	|      |                      |       |                        |      |
	|      |                      |       | divisor for the UART.  |      |
	+------+----------------------+-------+------------------------+------+
	| 31:8 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

FCR_IIR
^^^^^^^

.. _table_uart_fcr_iir:
.. table:: FCR_IIR, Offset Address: 0x008
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 7:0  | FCR_IIR              | R/W   | (R) interrupt          | 0x1  |
	|      |                      |       | Identification         |      |
	|      |                      |       | Register               |      |
	|      |                      |       |                        |      |
	|      |                      |       | [3:0] Interrupt ID     |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0000 : modem status    |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0001 : no interrupt    |      |
	|      |                      |       | pending                |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0010 : THR empty       |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0100 : received data   |      |
	|      |                      |       | available              |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0110 : receiver line   |      |
	|      |                      |       | status                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0111 : busy detect     |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1100 : character       |      |
	|      |                      |       | timeout                |      |
	|      |                      |       |                        |      |
	|      |                      |       | [7:6] FIFOs Enabled    |      |
	|      |                      |       |                        |      |
	|      |                      |       | 00 - disabled          |      |
	|      |                      |       |                        |      |
	|      |                      |       | 11 - enable            |      |
	|      |                      |       |                        |      |
	|      |                      |       | (W) FIFO Control       |      |
	|      |                      |       | Register               |      |
	|      |                      |       |                        |      |
	|      |                      |       | [0] FIFO Enable        |      |
	|      |                      |       |                        |      |
	|      |                      |       | [1] RCVR FIFO Reset    |      |
	|      |                      |       |                        |      |
	|      |                      |       | [2] XMIT FIFO Reset    |      |
	|      |                      |       |                        |      |
	|      |                      |       | [3] DMA Mode           |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 - mode 0, single DMA |      |
	|      |                      |       | data transfers at a    |      |
	|      |                      |       | time                   |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 - mode 1, multi DMA  |      |
	|      |                      |       | data transfers are     |      |
	|      |                      |       | made continuously      |      |
	|      |                      |       |                        |      |
	|      |                      |       | [5:4] TX Empty         |      |
	|      |                      |       |                        |      |
	|      |                      |       | 00 - FIFO empty        |      |
	|      |                      |       |                        |      |
	|      |                      |       | 01 - 2 characters in   |      |
	|      |                      |       | the FIFO               |      |
	|      |                      |       |                        |      |
	|      |                      |       | 10 - FIFO ¼ full       |      |
	|      |                      |       |                        |      |
	|      |                      |       | 11 - FIFO ½ full       |      |
	|      |                      |       |                        |      |
	|      |                      |       | [7:6] RCVR Trigger     |      |
	|      |                      |       |                        |      |
	|      |                      |       | 00 - 1 character in    |      |
	|      |                      |       | the FIFO               |      |
	|      |                      |       |                        |      |
	|      |                      |       | 01 - FIFO ¼ full       |      |
	|      |                      |       |                        |      |
	|      |                      |       | 10 - FIFO ½ full       |      |
	|      |                      |       |                        |      |
	|      |                      |       | 11 - FIFO 2 less than  |      |
	|      |                      |       | full                   |      |
	+------+----------------------+-------+------------------------+------+
	| 31:8 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+


LCR
^^^

.. _table_uart_lcr:
.. table:: LCR, Offset Address: 0x00c
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 7:0  | LCR                  | R/W   | Line Control Register  | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | [1:0] Data Length      |      |
	|      |                      |       | Select. (00:5          |      |
	|      |                      |       | bits,01:6 bits,10:7    |      |
	|      |                      |       | bits,11:8 bits)        |      |
	|      |                      |       |                        |      |
	|      |                      |       | [2] Number of stop     |      |
	|      |                      |       | bits. (0:1 stop        |      |
	|      |                      |       | bit,1:1.5 stop bits    |      |
	|      |                      |       | when Data Length       |      |
	|      |                      |       | Select is 0, else 2    |      |
	|      |                      |       | stop bits)             |      |
	|      |                      |       |                        |      |
	|      |                      |       | [3] Parity Enable      |      |
	|      |                      |       |                        |      |
	|      |                      |       | [4] Even Parity Select |      |
	|      |                      |       |                        |      |
	|      |                      |       | [5] Stick Parity       |      |
	|      |                      |       |                        |      |
	|      |                      |       | [6] Break Control Bit  |      |
	|      |                      |       |                        |      |
	|      |                      |       | [7] Divisor Latch      |      |
	|      |                      |       | Access Bit             |      |
	+------+----------------------+-------+------------------------+------+
	| 31:8 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

MCR
^^^

.. _table_uart_mcr:
.. table:: MCR, Offset Address: 0x010
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 7:0  | MCR                  | R/W   | Modem Control Register | 0x0  |
	|      |                      |       |                        |      |
	|      |                      |       | [0] reserved           |      |
	|      |                      |       |                        |      |
	|      |                      |       | [1] Request to Send.   |      |
	|      |                      |       | This is used to        |      |
	|      |                      |       | directly control the   |      |
	|      |                      |       | Request to Send        |      |
	|      |                      |       | (rts_n) output         |      |
	|      |                      |       |                        |      |
	|      |                      |       | [2] reserved           |      |
	|      |                      |       |                        |      |
	|      |                      |       | [3] reserved           |      |
	|      |                      |       |                        |      |
	|      |                      |       | [4] reserved           |      |
	|      |                      |       |                        |      |
	|      |                      |       | [5] Auto Flow Control  |      |
	|      |                      |       | Enable.                |      |
	|      |                      |       |                        |      |
	|      |                      |       | [6] reserved           |      |
	+------+----------------------+-------+------------------------+------+
	| 31:8 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

LSR
^^^

.. _table_uart_lsr:
.. table:: LSR, Offset Address: 0x014
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 7:0  | LSR                  | RO    | Line Status Register   |      |
	|      |                      |       |                        |      |
	|      |                      |       | [0] Data Ready bit.    |      |
	|      |                      |       | there is at least one  |      |
	|      |                      |       | character in the RBR   |      |
	|      |                      |       | or the receiver FIFO.  |      |
	|      |                      |       |                        |      |
	|      |                      |       | [1] Overrun error bit. |      |
	|      |                      |       | This is used to        |      |
	|      |                      |       | indicate the           |      |
	|      |                      |       | occurrence of an       |      |
	|      |                      |       | overrun error.         |      |
	|      |                      |       |                        |      |
	|      |                      |       | [2] Parity Error bit.  |      |
	|      |                      |       |                        |      |
	|      |                      |       | [3] Framing Error      |      |
	|      |                      |       | bit..                  |      |
	|      |                      |       |                        |      |
	|      |                      |       | [4] Break Interrupt    |      |
	|      |                      |       | bit.                   |      |
	|      |                      |       |                        |      |
	|      |                      |       | [5] Transmit Holding   |      |
	|      |                      |       | Register Empty bit.    |      |
	|      |                      |       |                        |      |
	|      |                      |       | [6] Transmitter Empty  |      |
	|      |                      |       | bit.                   |      |
	|      |                      |       |                        |      |
	|      |                      |       | [7] Receiver FIFO      |      |
	|      |                      |       | Error bit.             |      |
	+------+----------------------+-------+------------------------+------+
	| 31:8 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

MSR
^^^

.. _table_uart_msr:
.. table:: MSR, Offset Address: 0x018
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 7:0  | MSR                  | RO    | Modem Status Register  |      |
	|      |                      |       |                        |      |
	|      |                      |       | [0] Delta Clear to     |      |
	|      |                      |       | Send.                  |      |
	|      |                      |       |                        |      |
	|      |                      |       | [1] reserved           |      |
	|      |                      |       |                        |      |
	|      |                      |       | [2] reserved           |      |
	|      |                      |       |                        |      |
	|      |                      |       | [3] reserved           |      |
	|      |                      |       |                        |      |
	|      |                      |       | [4] CTS                |      |
	|      |                      |       |                        |      |
	|      |                      |       | [5] reserved           |      |
	|      |                      |       |                        |      |
	|      |                      |       | [6] reserved           |      |
	|      |                      |       |                        |      |
	|      |                      |       | [7] reserved           |      |
	+------+----------------------+-------+------------------------+------+
	| 31:8 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

LPDLL
^^^^^

.. _table_uart_lpdll:
.. table:: LPDLL, Offset Address: 0x020
	:widths: 1 2 1 4 1


	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 7:0  | LPDLL                | R/W   | LCR[7] bit = 1 : Low   | 0x0  |
	|      |                      |       | Power Divisor Latch    |      |
	|      |                      |       | (Low) Register         |      |
	+------+----------------------+-------+------------------------+------+
	| 31:8 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

LPDLH
^^^^^

.. _table_uart_lpdlh:
.. table:: LPDLH, Offset Address: 0x024
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 7:0  | LPDLH                | R/W   | LCR[7] bit = 1 : Low   | 0x0  |
	|      |                      |       | Power Divisor Latch    |      |
	|      |                      |       | (High) Register        |      |
	+------+----------------------+-------+------------------------+------+
	| 31:8 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+


SRBR_STHR
^^^^^^^^^

.. _table_uart_srbr_sthr:
.. table:: SRBR_STHR, Offset Address: 0x030
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 7:0  | SRBR_STHR            | R/W   | LCR[7] bit = 0 : (R)   | 0x0  |
	|      |                      |       | Shadow Receive Buffer  |      |
	|      |                      |       | Register               |      |
	|      |                      |       |                        |      |
	|      |                      |       | (W) Shadow Transmit    |      |
	|      |                      |       | Holding Register       |      |
	+------+----------------------+-------+------------------------+------+
	| 31:8 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

FAR
^^^

.. _table_uart_far:
.. table:: FAR, Offset Address: 0x070
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | FAR                  | R/W   | FIFO Access            | 0x0  |
	|      |                      |       | Register,This register |      |
	|      |                      |       | is                     |      |
	|      |                      |       |                        |      |
	|      |                      |       | use to enable a FIFO   |      |
	|      |                      |       | access mode for        |      |
	|      |                      |       | testing                |      |
	+------+----------------------+-------+------------------------+------+
	| 31:1 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

TFR
^^^

.. _table_uart_tfr:
.. table:: TFR, Offset Address: 0x074
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 7:0  | TFR                  | R/W   | Transmit FIFO Read.    | 0x0  |
	|      |                      |       | These bits are only    |      |
	|      |                      |       | valid when FIFO access |      |
	|      |                      |       | mode is enabled        |      |
	+------+----------------------+-------+------------------------+------+
	| 31:8 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+


RFW
^^^

.. _table_uart_rfw:
.. table:: RFW, Offset Address: 0x078
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 9:0  | RFW                  | R/W   | Receive FIFO Write.    | 0x0  |
	|      |                      |       | These bits are only    |      |
	|      |                      |       | valid when FIFO access |      |
	|      |                      |       | mode is enabled        |      |
	|      |                      |       |                        |      |
	|      |                      |       | [7:0] Receive FIFO     |      |
	|      |                      |       | Write Data.            |      |
	|      |                      |       |                        |      |
	|      |                      |       | [8] Receive FIFO       |      |
	|      |                      |       | Parity Error.          |      |
	|      |                      |       |                        |      |
	|      |                      |       | [9] Receive FIFO       |      |
	|      |                      |       | Framing Error.         |      |
	+------+----------------------+-------+------------------------+------+
	| 31:10| Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

USR
^^^

.. _table_uart_usr:
.. table:: USR, Offset Address: 0x07c
	:widths: 1 2 1 4 1


	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 4:0  | USR                  | RO    | UART Status Register   |      |
	|      |                      |       |                        |      |
	|      |                      |       | [0] UART Busy.         |      |
	|      |                      |       |                        |      |
	|      |                      |       | [1] Transmit FIFO Not  |      |
	|      |                      |       | Full.                  |      |
	|      |                      |       |                        |      |
	|      |                      |       | [2] Transmit FIFO      |      |
	|      |                      |       | Empty.                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | [3] Receive FIFO Not   |      |
	|      |                      |       | Empty.                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | [4] Receive FIFO Full. |      |
	+------+----------------------+-------+------------------------+------+
	| 31:5 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

TFL
^^^

.. _table_uart_tfl:
.. table:: TFL, Offset Address: 0x080
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 5:0  | TFL                  | RO    | Transmit FIFO Level.   |      |
	|      |                      |       | This is indicates the  |      |
	|      |                      |       | number of              |      |
	|      |                      |       | data entries in the    |      |
	|      |                      |       | transmit FIFO.         |      |
	+------+----------------------+-------+------------------------+------+
	| 31:6 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

RFL
^^^

.. _table_uart_rfl:
.. table:: TFL, Offset Address: 0x084
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 5:0  | RFL                  | RO    | Receive FIFO Level.    |      |
	|      |                      |       | This is indicates the  |      |
	|      |                      |       | number of data         |      |
	|      |                      |       | entries in the receive |      |
	|      |                      |       | FIFO.                  |      |
	+------+----------------------+-------+------------------------+------+
	| 31:6 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

SRR
^^^

.. _table_uart_srr:
.. table:: SRR, Offset Address: 0x088
	:widths: 1 2 1 4 1


	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 2:0  | SRR                  | R/W   | Software Reset         | 0x0  |
	|      |                      |       | Register               |      |
	|      |                      |       |                        |      |
	|      |                      |       | [0] UART Reset.        |      |
	|      |                      |       |                        |      |
	|      |                      |       | [1] RCVR FIFO Reset.   |      |
	|      |                      |       |                        |      |
	|      |                      |       | [2] XMIT FIFO Reset.   |      |
	+------+----------------------+-------+------------------------+------+
	| 31:3 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

SRTS
^^^^

.. _table_uart_srts:
.. table:: SRTS, Offset Address: 0x08c
	:widths: 1 2 1 4 1


	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | SRTS                 | R/W   | Shadow Request to      | 0x0  |
	|      |                      |       | Send. This is a shadow |      |
	|      |                      |       | register for the RTS   |      |
	|      |                      |       | bit (MCR[1])           |      |
	+------+----------------------+-------+------------------------+------+
	| 31:1 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

SBCR
^^^^

.. _table_uart_sbcr:
.. table:: SBCR, Offset Address: 0x090
	:widths: 1 2 1 4 1


	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | SBCR                 | R/W   | Shadow Break Control   | 0x0  |
	|      |                      |       | Bit. This is a shadow  |      |
	|      |                      |       | register for the Break |      |
	|      |                      |       | bit (LCR[6]).          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:1 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

SDMAM
^^^^^

.. _table_uart_sdmam:
.. table:: SDMAM, Offset Address: 0x094
	:widths: 1 2 1 4 1


	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | SDMAM                | R/W   | Shadow DMA Mode. This  | 0x0  |
	|      |                      |       | is a shadow register   |      |
	|      |                      |       | for the DMA mode bit   |      |
	|      |                      |       | (FCR[3]).              |      |
	+------+----------------------+-------+------------------------+------+
	| 31:1 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

SFE
^^^

.. _table_uart_sfe:
.. table:: SFE, Offset Address: 0x098
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | SFE                  | R/W   | Shadow FIFO Enable.    | 0x0  |
	|      |                      |       | This is a shadow       |      |
	|      |                      |       | register for the FIFO  |      |
	|      |                      |       | enable bit (FCR[0]).   |      |
	+------+----------------------+-------+------------------------+------+
	| 31:1 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

SRT
^^^

.. _table_uart_srt:
.. table:: SRT, Offset Address: 0x09c
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 1:0  | SRT                  | R/W   | Shadow RCVR Trigger.   | 0x0  |
	|      |                      |       | This is a shadow       |      |
	|      |                      |       | register for the RCVR  |      |
	|      |                      |       | trigger bits           |      |
	|      |                      |       | (FCR[7:6]).            |      |
	+------+----------------------+-------+------------------------+------+
	| 31:2 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

STET
^^^^

.. _table_uart_stet:
.. table:: STET, Offset Address: 0x0a0
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 1:0  | STET                 | R/W   | Shadow TX Empty        | 0x0  |
	|      |                      |       | Trigger. This is a     |      |
	|      |                      |       | shadow register for    |      |
	|      |                      |       | the TX empty trigger   |      |
	|      |                      |       | bits (FCR[5:4]).       |      |
	+------+----------------------+-------+------------------------+------+
	| 31:2 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

HTX
^^^

.. _table_uart_htx:
.. table:: HTX, Offset Address: 0x0a4
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | HTX                  | R/W   | This register is use   | 0x0  |
	|      |                      |       | to halt transmissions  |      |
	|      |                      |       | for testing,           |      |
	+------+----------------------+-------+------------------------+------+
	| 31:1 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

DMASA
^^^^^

.. _table_uart_dmasa:
.. table:: DMASA, Offset Address: 0x0a8
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | DMASA                | R/W   | This register is use   | 0x0  |
	|      |                      |       | to perform a DMA       |      |
	|      |                      |       | software acknowledge   |      |
	|      |                      |       | if a transfer needs to |      |
	|      |                      |       | be terminated due to   |      |
	|      |                      |       | an error condition.    |      |
	+------+----------------------+-------+------------------------+------+
	| 31:1 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
