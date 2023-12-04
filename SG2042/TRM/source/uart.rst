UART
====

Registers
------------

This section describes the programmable registers of the UART.

Note:Since UART registers are only located 32-bit boundaries, paddr[1:0] may be tied low permanently, if so desired. This would allow backward compatibility with standard 16550 
UART programmability.

1 Register Memory Map
^^^^^^^^^^^^^^^^^^^^^^^

Table -1 summarizes the register memory map for the UART:

.. table:: UART Memory Map
  
  +---------+---------------+-------+-----+----------------------------------------------+
  | Name    | Address       | Width | R/W | Description                                  |
  |         | Offset        |       |     |                                              |
  +---------+---------------+-------+-----+----------------------------------------------+
  | RBR     | 0x00          |32 bits| R   | Receive Buffer Register.                     |
  +         +               +       +     +                                              +
  |         |               |       |     | Reset Value: 0x0                             |
  +         +               +       +     +                                              +
  |         |               |       |     | Dependencies: LCR[7] bit = 0                 |
  +---------+---------------+-------+-----+----------------------------------------------+
  | THR     |               |32 bits| W   | Transmit Holding Register                    |
  +         +               +       +     +                                              +
  |         |               |       |     | Reset Value: 0x0                             |
  +         +               +       +     +                                              +
  |         |               |       |     | Dependencies: LCR[7] bit = 0                 |
  +---------+---------------+-------+-----+----------------------------------------------+
  | DLL     |               |32 bits| R/W | Divisor Latch (Low)                          |
  +         +               +       +     +                                              +
  |         |               |       |     | Reset Value: 0x0                             |
  +         +               +       +     +                                              +
  |         |               |       |     | Dependencies: LCR[7] bit = 1                 |
  +---------+---------------+-------+-----+----------------------------------------------+
  | DLH     | 0x04          |32 bits| R/W | Divisor Latch (High)                         |
  +         +               +       +     +                                              +
  |         |               |       |     | Reset Value: 0x0                             |
  +         +               +       +     +                                              +
  |         |               |       |     | Dependencies: LCR[7] bit = 1                 |
  +---------+---------------+-------+-----+----------------------------------------------+


.. table::

  +---------+---------------+-------+-----+----------------------------------------------+
  | IER     |               |32 bits| R/W | Interrupt Enable Register                    |
  +         +               +       +     +                                              +
  |         |               |       |     | Reset Value: 0x0                             |
  +         +               +       +     +                                              +
  |         |               |       |     | Dependencies: LCR[7] bit = 0                 |
  +---------+---------------+-------+-----+----------------------------------------------+
  | IIR     | 0x08          |32 bits| R   | Interrupt Identification Register            |
  +         +               +       +     +                                              +
  |         |               |       |     | Reset Value: 0x01                            |
  +---------+---------------+-------+-----+----------------------------------------------+
  | FCR     | 0x08          |32 bits| W   | FIFO Control Register                        |
  +         +               +       +     +                                              +
  |         |               |       |     | Reset Value: 0x0                             |
  +---------+---------------+-------+-----+----------------------------------------------+
  | LCR     | 0x0C          |32 bits| R/W | Line Control Register                        |
  +         +               +       +     +                                              +
  |         |               |       |     | Reset Value: 0x0                             |
  +---------+---------------+-------+-----+----------------------------------------------+
  | MCR     | 0x10          |32 bits| R/W | Modem Control Register                       |
  +         +               +       +     +                                              +
  |         |               |       |     | Reset Value: 0x0                             |
  +---------+---------------+-------+-----+----------------------------------------------+
  | LSR     | 0x14          |32 bits| R   | Line Status Register                         |
  +         +               +       +     +                                              +
  |         |               |       |     | Reset Value: 0x60                            |
  +---------+---------------+-------+-----+----------------------------------------------+


.. table::
  +---------+---------------+-------+-----+----------------------------------------------+
  | MSR     | 0x18          |32 bits| R   | Modem Status Register                        |
  +         +               +       +     +                                              +
  |         |               |       |     | Reset Value: 0x0                             |
  +---------+---------------+-------+-----+----------------------------------------------+
  | SCR     | 0x1C          |32 bits| R/W | Scratchpad Register                          |
  +         +               +       +     +                                              +
  |         |               |       |     | Reset Value: 0x0                             |
  +---------+---------------+-------+-----+----------------------------------------------+
  | LPDLL   | 0x20          |32 bits| R/W | Low Power Divisor Latch (Low)                |
  +         +               +       +     +                                              +
  |         |               |       |     | Register Reset Value: 0x0                    |
  +         +               +       +     +                                              +
  |         |               |       |     | Dependencies: LCR[7] bit = 1                 |
  +---------+---------------+-------+-----+----------------------------------------------+
  | LPDLH   | 0x24          |32 bits| R/W | Low Power Divisor Latch (High)               |
  +         +               +       +     +                                              +
  |         |               |       |     | Register Reset Value: 0x0                    |
  +         +               +       +     +                                              +
  |         |               |       |     | Dependencies: LCR[7] bit = 1                 |
  +---------+---------------+-------+-----+----------------------------------------------+
  | Reserved| 0x28 - 0x2C   |——     | ——  | ——                                           |
  +---------+---------------+-------+-----+----------------------------------------------+


.. table::

  +---------+---------------+-------+-----+----------------------------------------------+
  | SRBR    | 0x30 - 0x6C   |32 bits| R   | Shadow Receive Buffer Register               |
  +         +               +       +     +                                              +
  |         |               |       |     | Reset Value: 0x0                             |
  +         +               +       +     +                                              +
  |         |               |       |     | Dependencies: LCR[7] bit = 0                 |
  +---------+---------------+-------+-----+----------------------------------------------+
  | STHR    | 0x70          |32 bits| W   | Shadow Transmit Holding Register             |
  +         +               +       +     +                                              +
  |         |               |       |     | Reset Value: 0x0                             |
  +         +               +       +     +                                              +
  |         |               |       |     | Dependencies: LCR[7] bit = 0                 |
  +---------+---------------+-------+-----+----------------------------------------------+
  | FAR     | 0x74          |32 bits| R/W | FIFO Access Register                         |
  +         +               +       +     +                                              +
  |         |               |       |     | Reset Value: 0x0                             |
  +---------+---------------+-------+-----+----------------------------------------------+
  | TFR     | 0x78          |32 bits| R   | Transmit FIFO Read                           |
  +         +               +       +     +                                              +
  |         |               |       |     | Reset Value: 0x0                             |
  +---------+---------------+-------+-----+----------------------------------------------+
  | RFW     | 0x7C          |32 bits| W   | Receive FIFO Write                           |
  +         +               +       +     +                                              +
  |         |               |       |     | Reset Value: 0x0                             |
  +---------+---------------+-------+-----+----------------------------------------------+
  | USR     | 0x7C          |32 bits| R   | UART Status Register                         |
  +         +               +       +     +                                              +
  |         |               |       |     | Reset Value: 0x6                             |
  +---------+---------------+-------+-----+----------------------------------------------+



.. table::

  +---------+---------------+-------+-----+----------------------------------------------+ 
  | TFL     | 0x80          | see   | R   | Transmit FIFO Level                          |
  |         |               | 2.21  |     |                                              |
  |         |               |       |     | Reset Value: 0x0                             |
  +---------+---------------+-------+-----+----------------------------------------------+
  | RFL     | 0x84          | see   | R   | Receive FIFO Level                           |
  |         |               | 2.22  |     |                                              |
  |         |               |       |     | Reset Value: 0x0                             |
  +---------+---------------+-------+-----+----------------------------------------------+
  | SRR     | 0x88          |32 bits| W   | Software Reset Register                      |
  +         +               +       +     +                                              +
  |         |               |       |     | Reset Value: 0x0                             |
  +---------+---------------+-------+-----+----------------------------------------------+
  | SRTS    | 0x8C          |32 bits| R/W | Shadow Request to Send                       |
  +         +               +       +     +                                              +
  |         |               |       |     | Reset Value: 0x0                             |
  +---------+---------------+-------+-----+----------------------------------------------+
  | SBCR    | 0x90          |32 bits| R/W | Shadow Break Control Register                |
  +         +               +       +     +                                              +
  |         |               |       |     | Reset Value: 0x0                             |
  +---------+---------------+-------+-----+----------------------------------------------+
  | SDMAM   | 0x94          |32 bits| R/W | Shadow DMA Mode                              |
  +         +               +       +     +                                              +
  |         |               |       |     | Reset Value: 0x0                             |
  +---------+---------------+-------+-----+----------------------------------------------+
  | SFE     | 0x98          |32 bits| R/W | Shadow FIFO Enable                           |
  +         +               +       +     +                                              +
  |         |               |       |     | Reset Value: 0x0                             |
  +---------+---------------+-------+-----+----------------------------------------------+


.. table::

  +---------+---------------+-------+-----+----------------------------------------------+
  | SRT     | 0x9C          |32 bits| R/W | Shadow RCVR Trigger                          |
  +         +               +       +     +                                              +
  |         |               |       |     | Reset Value: 0x0                             |
  +---------+---------------+-------+-----+----------------------------------------------+
  | STET    | 0xA0          |32 bits| R/W | Shadow TX Empty Trigger                      |
  +         +               +       +     +                                              +
  |         |               |       |     | Reset Value: 0x0                             |
  +---------+---------------+-------+-----+----------------------------------------------+
  | HTX     | 0xA4          |32 bits| R/W | Halt TX                                      |
  +         +               +       +     +                                              +
  |         |               |       |     | Reset Value: 0x0                             |
  +---------+---------------+-------+-----+----------------------------------------------+
  | DMASA   | 0xA8          |1 bit  | W   | DMA Software Acknowledge                     |
  +         +               +       +     +                                              +
  |         |               |       |     | Reset Value: 0x0                             |
  +---------+---------------+-------+-----+----------------------------------------------+
  | TCR     | 0xAC          |32 bits| R/W | Transceiver Control Register                 |
  +         +               +       +     +                                              +
  |         |               |       |     | Reset Value: 0x6                             |
  +         +               +       +     +                                              +
  |         |               |       |     | Dependencies: UART_RS485_INTERFACE_EN=1      |
  +---------+---------------+-------+-----+----------------------------------------------+


.. table::

  +---------+---------------+-------+-----+----------------------------------------------+ 
  | DE_EN   | 0xB0          |32 bits| R/W | Driver Output Enable Register                |
  +         +               +       +     +                                              +
  |         |               |       |     | Reset Value: 0x0                             |
  +         +               +       +     +                                              +
  |         |               |       |     | Dependencies: UART_RS485_INTERFACE_EN=1      |       
  +---------+---------------+-------+-----+----------------------------------------------+
  | RE_EN   | 0xB4          |32 bits| R/W | Receiver Output Enable Register              |
  +         +               +       +     +                                              +
  |         |               |       |     | Reset Value: 0x0                             |
  +         +               +       +     +                                              +
  |         |               |       |     | Dependencies: UART_RS485_INTERFACE_EN=1      |         
  +---------+---------------+-------+-----+----------------------------------------------+
  | DET     | 0xB8          |32 bits| R/W | Driver Output Enable Timing Register         |
  +         +               +       +     +                                              +
  |         |               |       |     | Reset Value: 0x0                             |
  +         +               +       +     +                                              +
  |         |               |       |     | Dependencies: UART_RS485_INTERFACE_EN=1      |
  +---------+---------------+-------+-----+----------------------------------------------+
  | TAT     | 0xBC          |32 bits| R/W | TurnAround Timing Register.                  |
  +         +               +       +     +                                              +
  |         |               |       |     | Reset Value: 0x0                             |
  +         +               +       +     +                                              +
  |         |               |       |     | Dependencies: UART_RS485_INTERFACE_EN=1      |
  +---------+---------------+-------+-----+----------------------------------------------+


.. table::

  +---------+---------------+-------+-----+----------------------------------------------+
  | DLF     | 0xC0          |32 bits| R/W | Divisor Latch Fractional Value.              |
  +         +               +       +     +                                              +
  |         |               |       |     | Reset Value: 0x0                             |
  +         +               +       +     +                                              +
  |         |               |       |     | Dependencies: FRACTIONAL_BAUD_DIVISOR_EN=1   |
  +---------+---------------+-------+-----+----------------------------------------------+
  | RAR     | 0xC4          |32 bits| R/W | Receive Address Register                     |
  +         +               +       +     +                                              +
  |         |               |       |     | Reset Value: 0x0                             |
  +         +               +       +     +                                              +
  |         |               |       |     | Dependencies: UART_                          |
  +         +               +       +     +                                              +
  |         |               |       |     | 9BIT_DATA_EN=1                               |
  +---------+---------------+-------+-----+----------------------------------------------+
  | TAR     | 0xC8          |32 bits| R/W | Transmit Address Register                    |
  +         +               +       +     +                                              +
  |         |               |       |     | Reset Value: 0x0                             |
  +         +               +       +     +                                              +
  |         |               |       |     | Dependencies: UART_9BIT_DATA_EN=1            |       
  +---------+---------------+-------+-----+----------------------------------------------+
  | LCR_EXT | 0xCC          |32 bits| R/W | Line Extended Control Register               |
  +         +               +       +     +                                              +
  |         |               |       |     | Reset Value: 0x0                             |
  +         +               +       +     +                                              +
  |         |               |       |     | Dependencies: UART_9BIT_DATA_EN=1            |        
  +---------+---------------+-------+-----+----------------------------------------------+



.. table::

  +---------+---------------+-------+-----+----------------------------------------------+
  | ——      | 0xD0 - 0xF0   | ——    | ——  | ——                                           |
  +---------+---------------+-------+-----+----------------------------------------------+
  | CPR     | 0xF4          |32 bits| R   | Component Parameter Register                 |
  +         +               +       +     +                                              +
  |         |               |       |     | Reset Value: Configuration-dependent         |
  +---------+---------------+-------+-----+----------------------------------------------+
  | UCV     | 0xF8          |32 bits| R   | UART Component Version                       |
  +         +               +       +     +                                              +
  |         |               |       |     | Reset Value: See the Releases table in the   |
  +         +               +       +     +                                              +
  |         |               |       |     | AMBA 2 release notes.                        |
  +---------+---------------+-------+-----+----------------------------------------------+
  | CTR     | 0xFC          |32 bits| R   | Component Type Register                      |
  +         +               +       +     +                                              +
  |         |               |       |     | Reset Value: 0x44570110                      |
  +---------+---------------+-------+-----+----------------------------------------------+
 
2 Register and Field Descriptions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following subsections describe the data fields of the UART registers.

2.1 RBR
"""""""
- Name: Receive Buffer Register
- Size: 32 bits
- Address Offset: 0x00
- Read/write access: read-only

This register can be accessed only when the DLAB bit (LCR[7]) is cleared.

.. table::  RBR Register Fields

  +------+-------------------------------------+-----+---------------------------------------------------------+
  | Bits | Name                                | R/W | Description                                             |
  +======+=====================================+=====+=========================================================+
  | 31:9 | Reserved and read as 0              |     |                                                         |
  +------+-------------------------------------+-----+---------------------------------------------------------+
  | 8    | Receive Buffer register (MSB 9th    | R   | Data byte received on the serial input port (sin) in    |
  +      +                                     +     +                                                         +
  |      | bit)                                |     | UART mode for the MSB 9th bit.                          |
  +      +                                     +     +                                                         +
  |      |                                     |     | It is applicable only when UART_9BIT_DATA_EN=1          |    
  +      +                                     +     +                                                         +  
  |      |                                     |     | Reset Value: 0x0                                        |
  +------+-------------------------------------+-----+---------------------------------------------------------+
  | 7:0  | Receive Buffer Register (LSB 8 bits)| R   | Data byte received on the serial input port (sin) in    |
  +      +                                     +     +                                                         +
  |      |                                     |     | UART mode, or the serial infrared input (sir_in) in     |
  +      +                                     +     +                                                         +
  |      |                                     |     | infrared mode. The data in this register is valid only  |
  +      +                                     +     +                                                         +
  |      |                                     |     | if the Data Ready (DR) bit in the Line Status Register  |
  +      +                                     +     +                                                         +
  |      |                                     |     | (LSR) is set.                                           |
  +      +                                     +     +                                                         +
  |      |                                     |     | If in non-FIFO mode (FIFO_MODE = NONE) or FIFOs are     |
  +      +                                     +     +                                                         +
  |      |                                     |     | disabled (FCR[0] set to 0), the data in the RBR must be |
  +      +                                     +     +                                                         +
  |      |                                     |     | read before the next data arrives, otherwise it is      |
  +      +                                     +     +                                                         +
  |      |                                     |     | overwritten, resulting in an over-run error.            |
  +      +                                     +     +                                                         +
  |      |                                     |     | If in FIFO mode (FIFO_MODE != NONE) and FIFOs are       |
  +      +                                     +     +                                                         +
  |      |                                     |     | enabled (FCR[0] set to 1), this register accesses the   |
  +      +                                     +     +                                                         +
  |      |                                     |     | head of the receive FIFO. If the receive FIFO is full   |
  +      +                                     +     +                                                         +
  |      |                                     |     | and this register is not read before the next data      |
  +      +                                     +     +                                                         +
  |      |                                     |     | character arrives, then the data already in the FIFO is |
  +      +                                     +     +                                                         +
  |      |                                     |     | preserved, but any incoming data are lost and an        |
  +      +                                     +     +                                                         +
  |      |                                     |     | over-run error occurs.                                  |
  +      +                                     +     +                                                         +
  |      |                                     |     | Reset Value: 0x0                                        |
  +------+-------------------------------------+-----+---------------------------------------------------------+

2.2 THR
"""""""
- Name: Transmit Holding Register
- Size: 32 bits
- Address Offset: 0x00
- Read/write access: write-only

This register can be accessed only when the DLAB bit (LCR[7]) is cleared.

.. table::  THR Register Fields

  +------+-----------------------------+-----+-------------------------------------------------------------------+
  | Bits | Name                        | R/W | Description                                                       |
  +======+=============================+=====+===================================================================+
  | 31:9 | Reserved and read as 0      |     |                                                                   |
  |      |                             |     |                                                                   |
  +------+-----------------------------+-----+-------------------------------------------------------------------+
  | 8    | Transmit Holding Register   | W   | Data to be transmitted on the serial output port (sout) in        |
  +      +                             +     +                                                                   +
  |      | (MSB 9th bit)               |     | UART mode for the MSB 9th bit.                                    |
  +      +                             +     +                                                                   +
  |      |                             |     | It is applicable only when UART_9BIT_DATA_EN=1.                   |
  +      +                             +     +                                                                   +
  |      |                             |     | Reset Value: 0x0                                                  |
  +------+-----------------------------+-----+-------------------------------------------------------------------+
  | 7:0  | Transmit Holding Register   | W   | Data to be transmitted on the serial output port (sout) in        |
  +      +                             +     +                                                                   +
  |      | (LSB 8 bits)                |     | UART mode or the serial infrared output (sir_out_n) in infrared   |
  +      +                             +     +                                                                   +
  |      |                             |     | mode. Data should only be written to the THR when the THR Empty   |
  +      +                             +     +                                                                   +
  |      |                             |     | (THRE) bit (LSR[5]) is set.                                       |
  +      +                             +     +                                                                   +
  |      |                             |     | If in non-FIFO mode or FIFOs are disabled (FCR[0] = 0) and THRE   |
  +      +                             +     +                                                                   +
  |      |                             |     | is set, writing a single character to the THR clears the THRE.    |
  +      +                             +     +                                                                   +
  |      |                             |     | Any additional writes to the THR before the THRE is set again     |
  +      +                             +     +                                                                   +
  |      |                             |     | causes the THR data to be overwritten.                            |
  +      +                             +     +                                                                   +
  |      |                             |     | If in FIFO mode and FIFOs are enabled (FCR[0] = 1) and THRE is    |
  +      +                             +     +                                                                   +
  |      |                             |     | set, x number of characters of data may be written to the THR     |
  +      +                             +     +                                                                   +
  |      |                             |     | before the FIFO is full. The number x (default=16) is determined  |
  +      +                             +     +                                                                   +
  |      |                             |     | by the value of FIFO Depth that you set during configuration.     |
  +      +                             +     +                                                                   +
  |      |                             |     | Any attempt to write data when the FIFO is full results in the    |
  +      +                             +     +                                                                   +
  |      |                             |     | write data being lost.                                            |
  +      +                             +     +                                                                   +
  |      |                             |     | Reset Value: 0x0                                                  |
  +------+-----------------------------+-----+-------------------------------------------------------------------+

2.3 DLH
"""""""
- Name: Divisor Latch High 
- Size: 32 bits
- Address Offset: 0x04
- Read/write access: read/write

If UART_16550_COMPATIBLE = No, then this register can be accessed only when the DLAB bit (LCR[7]) is 
set and the UART is not busy—that is, USR[0] is 0; otherwise this register can be accessed only when the 
DLAB bit (LCR[7]) is set.

.. table::  DLH Register Fields

  +------+-----------------------------+-----+------------------------------------------------------------------------+
  | Bits | Name                        | R/W | Description                                                            |
  +======+=============================+=====+========================================================================+
  | 31:8 | Reserved and read as 0      |     |                                                                        |
  +------+-----------------------------+-----+------------------------------------------------------------------------+
  | 7:0  | Divisor Latch (High)        | R/W | Upper 8-bits of a 16-bit, read/write, Divisor Latch register that      |
  +      +                             +     +                                                                        +
  |      |                             |     | contains the baud rate divisor for the UART. The output baud rate is   |
  +      +                             +     +                                                                        +
  |      |                             |     | equal to the serial clock (pclk if one clock design, sclk if two clock |
  +      +                             +     +                                                                        +
  |      |                             |     | design (CLOCK_MODE = Enabled)) frequency divided by sixteen times the  |
  +      +                             +     +                                                                        +
  |      |                             |     | value of the baud rate divisor, as follows: baud rate = (serial clock  |
  +      +                             +     +                                                                        +
  |      |                             |     | freq) / (16 * divisor). Note that with the Divisor Latch Registers     |
  +      +                             +     +                                                                        +
  |      |                             |     | (DLL and DLH) set to 0, the baud clock is disabled and no serial       |
  +      +                             +     +                                                                        +
  |      |                             |     | communications occur. Also, once the DLH is set, at least 8 clock      |
  +      +                             +     +                                                                        +
  |      |                             |     | cycles of the slowest UART clock should be allowed to pass             |
  +      +                             +     +                                                                        +
  |      |                             |     | before transmitting or receiving data.                                 |
  +      +                             +     +                                                                        +
  |      |                             |     | Reset Value: 0x0                                                       |
  +------+-----------------------------+-----+------------------------------------------------------------------------+

2.4 DLL
"""""""
- Name: Divisor Latch Low 
- Size: 32 bits
- Address Offset: 0x00
- Read/write access: read/write

If UART_16550_COMPATIBLE = No, then this register can be accessed only when the DLAB bit (LCR[7]) is 
set and the UART is not busy—that is, USR[0] is 0; otherwise this register can be accessed only when the 
DLAB bit (LCR[7]) is set.

.. table::  DLL Register Fields

  +------+-------------------------+-----+------------------------------------------------------------------------+
  | Bits | Name                    | R/W | Description                                                            |
  +======+=========================+=====+========================================================================+
  | 31:8 | Reserved and read as 0  |     |                                                                        |
  +------+-------------------------+-----+------------------------------------------------------------------------+
  | 7:0  | Divisor Latch (Low)     | R/W | Lower 8 bits of a 16-bit, read/write, Divisor Latch register that      |
  +      +                         +     +                                                                        +
  |      |                         |     | contains the baud rate divisor for the UART. The output baud rate is   |
  +      +                         +     +                                                                        +
  |      |                         |     | equal to the serial clock (pclk if one clock design, sclk if two clock |
  +      +                         +     +                                                                        +
  |      |                         |     | design (CLOCK_MODE = Enabled)) frequency divided by sixteen times the  |
  +      +                         +     +                                                                        +
  |      |                         |     | value of the baud rate divisor, as follows: baud rate = (serial clock  |
  +      +                         +     +                                                                        +
  |      |                         |     | freq) / (16 * divisor). Note that with the Divisor Latch Registers     |
  +      +                         +     +                                                                        +
  |      |                         |     | (DLL and DLH) set to 0, the baud clock is disabled and no serial       |
  +      +                         +     +                                                                        +
  |      |                         |     | communications occur. Also, once the DLL is set, at least 8 clock      |
  +      +                         +     +                                                                        +
  |      |                         |     | cycles of the slowest UART clock should be allowed to pass             |
  +      +                         +     +                                                                        +
  |      |                         |     | before transmitting or receiving data.                                 |
  +      +                         +     +                                                                        +
  |      |                         |     | Reset Value: 0x0                                                       |
  +------+-------------------------+-----+------------------------------------------------------------------------+

2.5 IER
"""""""
- Name: Interrupt Enable Register 
- Size: 32 bits
- Address Offset: 0x04
- Read/write access: read/write

This register can be accessed only when the DLAB bit (LCR[7]) is cleared.

.. table::  IER Register Fields

  +------+-----------------------+-----+------------------------------------------------------------------------------+
  | Bits | Name                  | R/W | Description                                                                  |
  +======+=======================+=====+==============================================================================+
  | 31:8 | Reserved and read as 0|     |                                                                              |
  +------+-----------------------+-----+------------------------------------------------------------------------------+
  | 7    | PTIME                 | R/W | Programmable THRE Interrupt Mode Enable that can be written to only when     |
  +      +                       +     +                                                                              +
  |      |                       |     | THRE_MODE_USER = Enabled, always readable. This is used to enable/disable    |
  +      +                       +     +                                                                              +
  |      |                       |     | the generation of THRE Interrupt.                                            |
  +      +                       +     +                                                                              +
  |      |                       |     | 0 - disabled                                                                 |
  +      +                       +     +                                                                              +
  |      |                       |     | 1 - enabled                                                                  |
  +      +                       +     +                                                                              +
  |      |                       |     | Reset Value: 0x0                                                             |
  +------+-----------------------+-----+------------------------------------------------------------------------------+
  | 6:4  | Reserved and read as 0|     |                                                                              |
  +------+-----------------------+-----+------------------------------------------------------------------------------+
  | 3    | EDSSI                 | R/W | Enable Modem Status Interrupt. This is used to enable/disable the            |
  +      +                       +     +                                                                              +
  |      |                       |     | generation of Modem Status Interrupt. This is the fourth highest priority    |
  +      +                       +     +                                                                              +
  |      |                       |     | interrupt.                                                                   |
  +      +                       +     +                                                                              +
  |      |                       |     | 0 - disabled                                                                 |
  +      +                       +     +                                                                              +
  |      |                       |     | 1 - enabled                                                                  |
  +      +                       +     +                                                                              +
  |      |                       |     | Reset Value: 0x0                                                             |
  +------+-----------------------+-----+------------------------------------------------------------------------------+


.. table::

  +------+-----------------------+-----+------------------------------------------------------------------------------+
  | 2    | ELSI                  | R/W | Enable Receiver Line Status Interrupt. This is used to enable/disable the    |
  +      +                       +     +                                                                              +
  |      |                       |     | generation of Receiver Line Status Interrupt. This is the highest priority   |
  +      +                       +     +                                                                              +
  |      |                       |     | interrupt.                                                                   |
  +      +                       +     +                                                                              +
  |      |                       |     | 0 - disabled                                                                 |
  +      +                       +     +                                                                              +
  |      |                       |     | 1 - enabled                                                                  |
  +      +                       +     +                                                                              +
  |      |                       |     | Reset Value: 0x0                                                             |
  +------+-----------------------+-----+------------------------------------------------------------------------------+
  | 1    | ETBEI                 | R/W | Enable Transmitter Holding Register Empty Interrupt. This is used to         |
  +      +                       +     +                                                                              +
  |      |                       |     | enable/disable the generation of Transmitter Holding Register Empty          |
  +      +                       +     +                                                                              +
  |      |                       |     | Interrupt. This is the third highest priority interrupt.                     |
  +      +                       +     +                                                                              +
  |      |                       |     | 0 - disabled                                                                 |
  +      +                       +     +                                                                              +
  |      |                       |     | 1 - enabled                                                                  |
  +      +                       +     +                                                                              +
  |      |                       |     | Reset Value: 0x0                                                             |
  +------+-----------------------+-----+------------------------------------------------------------------------------+
  | 0    | ERBFI                 | R/W | Enable Received Data Available Interrupt. This is used to enable/disable     |
  +      +                       +     +                                                                              +
  |      |                       |     | the generation of Received Data Available Interrupt and the Character        |
  +      +                       +     +                                                                              +
  |      |                       |     | Timeout Interrupt (if in FIFO mode and FIFOs enabled). These are the second  |
  +      +                       +     +                                                                              +
  |      |                       |     | highest priority interrupts.                                                 |
  +      +                       +     +                                                                              +
  |      |                       |     | 0 - disabled                                                                 |
  +      +                       +     +                                                                              +
  |      |                       |     | 1 - enabled                                                                  |
  +      +                       +     +                                                                              +
  |      |                       |     | Reset Value: 0x0                                                             |
  +------+-----------------------+-----+------------------------------------------------------------------------------+

2.6 IIR
"""""""
- Name: Interrupt Identity Register
- Size: 32 bits
- Address Offset: 0x08
- Read/write access: read-only

.. table::  IIR Register Fields

  +------+--------------------------+-----+-------------------------------------------------------------------+
  | Bits | Name                     | R/W | Description                                                       |
  +======+==========================+=====+===================================================================+
  | 31:8 | Reserved and read as 0   |     |                                                                   |
  +------+--------------------------+-----+-------------------------------------------------------------------+
  | 7:6  | FIFOs Enabled (or FIFOSE)| R   | FIFOs Enabled. This is used to indicate whether the FIFOs are     |
  +      +                          +     +                                                                   +
  |      |                          |     | enabled or disabled.                                              |
  +      +                          +     +                                                                   +
  |      |                          |     | 00 - disabled                                                     |
  +      +                          +     +                                                                   +
  |      |                          |     | 11 - enabled                                                      |
  +      +                          +     +                                                                   +
  |      |                          |     | Reset Value: 0x00                                                 |
  +------+--------------------------+-----+-------------------------------------------------------------------+
  | 5:4  | Reserved                 | N/A | Reserved and read as 0                                            |
  +------+--------------------------+-----+-------------------------------------------------------------------+
  | 3:0  | Interrupt ID (or IID)    | R   | Interrupt ID. This indicates the highest priority pending         |
  +      +                          +     +                                                                   +
  |      |                          |     | interrupt which can be one of the following types:                |
  +      +                          +     +                                                                   +
  |      |                          |     | 0000 - modem status                                               |
  +      +                          +     +                                                                   +
  |      |                          |     | 0001 - no interrupt pending                                       |
  +      +                          +     +                                                                   +
  |      |                          |     | 0010 - THR empty                                                  |
  +      +                          +     +                                                                   +
  |      |                          |     | 0100 - received data available                                    |
  +      +                          +     +                                                                   +
  |      |                          |     | 0110 - receiver line status                                       |
  +      +                          +     +                                                                   +
  |      |                          |     | 0111 - busy detect                                                |
  +      +                          +     +                                                                   +
  |      |                          |     | 1100 - character timeout                                          |
  +      +                          +     +                                                                   +
  |      |                          |     | The interrupt priorities are split into several levels that are   |
  +      +                          +     +                                                                   +
  |      |                          |     | detailed in Table -2 .                                            |
  +      +                          +     +                                                                   +
  |      |                          |     | **Note** :                                                        |
  |      |                          |     | An interrupt of type 0111 (busy detect) is never indicated if     |
  +      +                          +     +                                                                   +
  |      |                          |     | UART_16550_COMPATIBLE = YES in coreConsultant.                    |
  +      +                          +     +                                                                   +
  |      |                          |     | Bit 3 indicates an interrupt can only occur when the FIFOs are    |
  +      +                          +     +                                                                   +
  |      |                          |     | enabled and used to distinguish a Character Timeout condition     |
  +      +                          +     +                                                                   +
  |      |                          |     | interrupt.                                                        |
  +      +                          +     +                                                                   +
  |      |                          |     | Reset Value: 0x01                                                 |
  +------+--------------------------+-----+-------------------------------------------------------------------+

Table -2 summarizes the Interrupt Control Functions:

.. table::  Interrupt Control Functions

  +-------------+--------------+-------------+--------------+---------------------------------+---------------------+-------------------------------------------------+---------------------------------------------------+
  |Interrupt ID |              |             |              |Interrupt Set and Reset Functions|                     |                                                 |                                                   |
  +-------------+--------------+-------------+--------------+---------------------------------+---------------------+-------------------------------------------------+---------------------------------------------------+
  | Bit 3       | Bit 2        | Bit 1       | Bit 0        | Priority Level                  | Interrupt Type      | Interrupt Source                                | Interrupt Reset Control                           |
  +=============+==============+=============+==============+=================================+=====================+=================================================+===================================================+
  | 0           | 0            | 0           | 1            | ——                              | None                | None                                            | ——                                                |
  +-------------+--------------+-------------+--------------+---------------------------------+---------------------+-------------------------------------------------+---------------------------------------------------+
  | 0           | 1            | 1           | 0            | Highest                         | Receiver line status| Overrun/parity/ framing errors, break           | Reading the line status register.                 |
  |             |              |             |              |                                 |                     | interrupt, or address received interrupt        | In addition to LSR read, the Receiver line status |
  |             |              |             |              |                                 |                     |                                                 | is also cleared when RX_FIFO is read.             |
  +-------------+--------------+-------------+--------------+---------------------------------+---------------------+-------------------------------------------------+---------------------------------------------------+
  | 0           | 1            | 0           | 0            | Second                          | Received data       | Receiver data available (non-FIFO mode          | Reading the receiver buffer register (non-FIFO    |
  |             |              |             |              |                                 | available           | or FIFOs disabled) or RCVR FIFO trigger         | mode or FIFOs disabled) or the FIFO drops below   |
  |             |              |             |              |                                 |                     | level reached (FIFO mode and FIFOs enabled)     | the trigger level (FIFO mode and FIFOs enabled).  |
  +-------------+--------------+-------------+--------------+---------------------------------+---------------------+-------------------------------------------------+---------------------------------------------------+
  | 1           | 1            | 0           | 0            | Second                          | Character timeout   | No characters in or out of the RCVR FIFO        | Reading the receiver buffer register              |
  |             |              |             |              |                                 | indication          | during the last 4 character times and there     |                                                   |
  |             |              |             |              |                                 |                     | is at least 1 character in it during this time  |                                                   |
  +-------------+--------------+-------------+--------------+---------------------------------+---------------------+-------------------------------------------------+---------------------------------------------------+
  | 0           | 0            | 1           | 0            | Third                           | Transmit holding    | Transmitter holding register empty              | Reading the IIR register (if source of interrupt);|
  |             |              |             |              |                                 | register empty      | (Prog. THRE Mode disabled) or XMIT FIFO         | or, writing into THR (FIFOs or THRE Mode not      |
  |             |              |             |              |                                 |                     | above threshold (Prog. THRE Mode enabled)       | selected or disabled) or XMIT FIFO above threshold|
  |             |              |             |              |                                 |                     |                                                 | (FIFOs and THRE Mode selected and enabled).       |
  +-------------+--------------+-------------+--------------+---------------------------------+---------------------+-------------------------------------------------+---------------------------------------------------+
  | 0           | 0            | 0           | 0            | Fourth                          | Modem status        | Clear to send or data set ready or ring         | Reading the Modem status register                 |
  |             |              |             |              |                                 |                     | indicator or data carrier detect. Note          |                                                   |
  |             |              |             |              |                                 |                     | that if auto flow control mode is enabled,      |                                                   |
  |             |              |             |              |                                 |                     | a change in CTS auto enabled, a change in CTS   |                                                   |
  |             |              |             |              |                                 |                     | (that is, DCTS set) does not cause an interrupt.|                                                   |
  +-------------+--------------+-------------+--------------+---------------------------------+---------------------+-------------------------------------------------+---------------------------------------------------+
  | 0           | 1            | 1           | 1            | Fifth                           | Busy detect         | UART_16550_COMPATIBLE = NO and the              | Reading the UART status register                  |
  |             |              |             |              |                                 | indication          | Master has tried to write to the Line Control   |                                                   |
  |             |              |             |              |                                 |                     | Register while the UART is busy                 |                                                   |
  |             |              |             |              |                                 |                     | (USR[0] is set to 1).                           |                                                   |
  +-------------+--------------+-------------+--------------+---------------------------------+---------------------+-------------------------------------------------+---------------------------------------------------+

2.7 FCR
"""""""
- Name: FIFO Control Register
- Size: 32 bits
- Address Offset: 0x08
- Read/write access: write-only

This register is valid only when the UART is configured to have FIFOs implemented 
(FIFO_MODE != NONE). If FIFOs are not implemented, this register does not exist and writing to this 
register address has no effect.

.. table::  FCR Register Fields

  +------+----------------------------+-----+-----------------------------------------------------------------------------------------------------------------------------------------+
  | Bits | Name                       | R/W | Description                                                                                                                             |
  +======+============================+=====+=========================================================================================================================================+
  | 31:8 | Reserved and read as 0     |     |                                                                                                                                         |
  +------+----------------------------+-----+-----------------------------------------------------------------------------------------------------------------------------------------+
  | 7:6  | RCVR Trigger (or RT)       | W   | RCVR Trigger. This is used to select the trigger level in the receiver FIFO at which the Received Data Available Interrupt is generated.|
  +      +                            +     +                                                                                                                                         +
  |      |                            |     | In auto flow control mode, this trigger is used to determine when the rts_n signal is de-asserted only when RTC_FCT is disabled.        |
  +      +                            +     +                                                                                                                                         +
  |      |                            |     | It also determines when the dma_rx_req_n signal is asserted in certain modes of operation. The following trigger levels are supported:  |
  +      +                            +     +                                                                                                                                         +
  |      |                            |     | 00 - 1 character in the FIFO                                                                                                            |
  +      +                            +     +                                                                                                                                         +
  |      |                            |     | 01 - FIFO ¼ full                                                                                                                        |
  +      +                            +     +                                                                                                                                         +
  |      |                            |     | 10 - FIFO ½ full                                                                                                                        |
  +      +                            +     +                                                                                                                                         +
  |      |                            |     | 11 - FIFO 2 less than full                                                                                                              |
  +      +                            +     +                                                                                                                                         +
  |      |                            |     | Reset Value: 0x0                                                                                                                        |
  +------+----------------------------+-----+-----------------------------------------------------------------------------------------------------------------------------------------+
  | 5:4  | TX Empty Trigger (or TET)  | W   | TX Empty Trigger. Writes have no effect when THRE_MODE_USER = Disabled. This is used to select the empty threshold level at which the   |
  +      +                            +     +                                                                                                                                         +
  |      |                            |     | THRE Interrupts are generated when the mode is active. It also determines when the thre_dma_tx_req_n signal is asserted when            |
  +      +                            +     +                                                                                                                                         +
  |      |                            |     | in certain modes of operation. The following trigger levels are                                                                         |
  +      +                            +     +                                                                                                                                         +
  |      |                            |     | supported:                                                                                                                              |
  +      +                            +     +                                                                                                                                         +
  |      |                            |     | 00 - FIFO empty                                                                                                                         |
  +      +                            +     +                                                                                                                                         +
  |      |                            |     | 01 - 2 characters in the FIFO                                                                                                           |
  +      +                            +     +                                                                                                                                         +
  |      |                            |     | 10 - FIFO ¼ full                                                                                                                        |
  +      +                            +     +                                                                                                                                         +
  |      |                            |     | 11 - FIFO ½ full                                                                                                                        |
  +      +                            +     +                                                                                                                                         +
  |      |                            |     | Reset Value: 0x0                                                                                                                        |
  +------+----------------------------+-----+-----------------------------------------------------------------------------------------------------------------------------------------+


.. table::

  +------+----------------------------+-----+-----------------------------------------------------------------------------------------------------------------------------------------+
  | 3    | DMA Mode (or DMAM)         | W   | DMA Mode. This determines the DMA signalling mode used for the dma_tx_req_n and dma_rx_req_n output signals when additional DMA         |
  +      +                            +     +                                                                                                                                         +
  |      |                            |     | handshaking signals are not selected (DMA_EXTRA = No).                                                                                  |
  +      +                            +     +                                                                                                                                         +
  |      |                            |     | 0 - mode 0                                                                                                                              |
  +      +                            +     +                                                                                                                                         +
  |      |                            |     | 1 - mode 1                                                                                                                              |
  +      +                            +     +                                                                                                                                         +
  |      |                            |     | Reset Value: 0x0                                                                                                                        |
  +------+----------------------------+-----+-----------------------------------------------------------------------------------------------------------------------------------------+
  | 2    | XMIT FIFO Reset (or XIFOR) | W   | XMIT FIFO Reset. This resets the control portion of the transmit FIFO and treats the FIFO as empty. This also de-asserts the DMA TX     |
  +      +                            +     +                                                                                                                                         +
  |      |                            |     | request and single signals when additional DMA handshaking signals are selected (DMA_EXTRA = YES).                                      |
  +      +                            +     +                                                                                                                                         +
  |      |                            |     | Note that this bit is 'self-clearing'. It is not necessary to clear this bit.                                                           |
  +      +                            +     +                                                                                                                                         +
  |      |                            |     | Reset Value: 0x0                                                                                                                        |
  +------+----------------------------+-----+-----------------------------------------------------------------------------------------------------------------------------------------+
  | 1    | RCVR FIFO Reset (or RIFOR) | W   | RCVR FIFO Reset. This resets the control portion of the receive FIFO and treats the FIFO as empty. This also de-asserts the DMA RX      |
  +      +                            +     +                                                                                                                                         +
  |      |                            |     | request and single signals when additional DMA handshaking signals are selected (DMA_EXTRA = YES).                                      |
  +      +                            +     +                                                                                                                                         +
  |      |                            |     | Note that this bit is 'self-clearing'. It is not necessary to clear this bit.                                                           |
  +      +                            +     +                                                                                                                                         +
  |      |                            |     | Reset Value: 0x0                                                                                                                        |
  +------+----------------------------+-----+-----------------------------------------------------------------------------------------------------------------------------------------+
  | 0    | FIFO Enable (or FIFOE)     | W   | FIFO Enable. This enables/disables the transmit (XMIT) and receive (RCVR) FIFOs. Whenever the value of this bit is changed both the     |
  +      +                            +     +                                                                                                                                         +
  |      |                            |     | XMIT and RCVR controller portion of FIFOs is reset.                                                                                     |
  +      +                            +     +                                                                                                                                         +
  |      |                            |     | Reset Value: 0x0                                                                                                                        |
  +------+----------------------------+-----+-----------------------------------------------------------------------------------------------------------------------------------------+

2.8 LCR
"""""""
- Name: Line Control Register
- Size: 32 bits
- Address Offset: 0x0C
- Read/write access: read/write

.. table::  LCR Register Fields

  +------+-------------------------+-----+----------------------------------------------------------------------------------------------------------------------+
  | Bits | Name                    | R/W | Description                                                                                                          |
  +======+=========================+=====+======================================================================================================================+
  | 31:8 | Reserved and read as 0  |     |                                                                                                                      |
  +------+-------------------------+-----+----------------------------------------------------------------------------------------------------------------------+
  | 7    | DLAB                    | R/W | Divisor Latch Access Bit. If UART_16550_COMPATIBLE = NO, then writeable only when UART is not busy (USR[0] is 0);    |
  +      +                         +     +                                                                                                                      +
  |      |                         |     | otherwise always writable, always readable. This bit is used to enable reading and writing of the Divisor Latch      |
  +      +                         +     +                                                                                                                      +
  |      |                         |     | register (DLL and DLH/LPDLL and LPDLH) to set the baud rate of the UART. This bit must be cleared after initial      |
  +      +                         +     +                                                                                                                      +
  |      |                         |     | baud rate setup in order to access other registers.                                                                  |
  +      +                         +     +                                                                                                                      +
  |      |                         |     | Reset Value: 0x0                                                                                                     |
  +------+-------------------------+-----+----------------------------------------------------------------------------------------------------------------------+
  | 6    | Break (or BC)           | R/W | Break Control Bit. This is used to cause a break condition to be transmitted to the receiving device. If set to 1,   |
  +      +                         +     +                                                                                                                      +
  |      |                         |     | the serial output is forced to the spacing (logic 0) state. When not in Loopback Mode, as determined by MCR[4],      |
  +      +                         +     +                                                                                                                      +
  |      |                         |     | the sout line is forced low until the Break bit is cleared. If SIR_MODE = Enabled and active (MCR[6] set to 1)       |
  +      +                         +     +                                                                                                                      +
  |      |                         |     | the sir_out_n line is continuously pulsed. When in Loopback Mode, the break condition is internally looped back      |
  +      +                         +     +                                                                                                                      +
  |      |                         |     | to the receiver and the sir_out_n line is forced low.                                                                |
  +      +                         +     +                                                                                                                      +
  |      |                         |     | Reset Value: 0x0                                                                                                     |
  +------+-------------------------+-----+----------------------------------------------------------------------------------------------------------------------+


.. table::

  +------+-------------------------+-----+----------------------------------------------------------------------------------------------------------------------+
  | 5    | Stick Parity            | R/W | Stick Parity. If UART_16550_COMPATIBLE = NO, then writable only when UART is not busy (USR[0] is 0);                 |
  +      +                         +     +                                                                                                                      +
  |      |                         |     | otherwise always writable, always readable. This bit is used to force parity value. When PEN, EPS, and Stick Parity  |
  +      +                         +     +                                                                                                                      +
  |      |                         |     | are set to 1, the parity bit is transmitted and checked as logic 0. If PEN and Stick Parity are set to 1 and EPS     |
  +      +                         +     +                                                                                                                      +
  |      |                         |     | is a logic 0, then parity bit is transmitted and checked as a logic 1. If this bit is set to 0, Stick Parity is      |
  +      +                         +     +                                                                                                                      +
  |      |                         |     | disabled.                                                                                                            |
  +      +                         +     +                                                                                                                      +
  |      |                         |     | Reset Value: 0x0                                                                                                     |
  +------+-------------------------+-----+----------------------------------------------------------------------------------------------------------------------+
  | 4    | EPS                     | R/W | Even Parity Select. If UART_16550_COMPATIBLE = NO, then writable only when UART is not busy (USR[0] is 0);           |
  +      +                         +     +                                                                                                                      +
  |      |                         |     | otherwise always writable, always readable. This is used to select between even and odd parity, when parity is       |
  +      +                         +     +                                                                                                                      +
  |      |                         |     | enabled (PEN set to 1). If set to 1, an even number of logic 1s is transmitted or checked. If set to 0, an odd number|
  +      +                         +     +                                                                                                                      +
  |      |                         |     | of logic 1s is transmitted or checked.                                                                               |
  +      +                         +     +                                                                                                                      +
  |      |                         |     | Reset Value: 0x0                                                                                                     |
  +------+-------------------------+-----+----------------------------------------------------------------------------------------------------------------------+
  | 3    | PEN                     | R/W | Parity Enable. If UART_16550_COMPATIBLE = NO, then writable only when UART is not busy (USR[0] is 0);                |
  +      +                         +     +                                                                                                                      +
  |      |                         |     | otherwise always writable, always readable. This bit is used to enable and disable parity generation and detection   |
  +      +                         +     +                                                                                                                      +
  |      |                         |     | in transmitted and received serial character respectively.                                                           |
  +      +                         +     +                                                                                                                      +
  |      |                         |     | 0 - parity disabled                                                                                                  |
  +      +                         +     +                                                                                                                      +
  |      |                         |     | 1 - parity enabled                                                                                                   |
  +      +                         +     +                                                                                                                      +
  |      |                         |     | Reset Value: 0x0                                                                                                     |
  +------+-------------------------+-----+----------------------------------------------------------------------------------------------------------------------+
  
  
.. table::

  +------+-------------------------+-----+----------------------------------------------------------------------------------------------------------------------+
  | 2    | STOP                    | R/W | Number of stop bits. If UART_16550_COMPATIBLE = NO, then writable only when UART is not busy (USR[0] is 0);          |
  +      +                         +     +                                                                                                                      +
  |      |                         |     | otherwise always writable, always readable. This is used to select the number of stop bits per character that the    |
  +      +                         +     +                                                                                                                      +
  |      |                         |     | peripheral transmits and receives. If set to 0, one stop bit is transmitted in the serial data.                      |
  +      +                         +     +                                                                                                                      +
  |      |                         |     | If set to 1 and the data bits are set to 5 (LCR[1:0] set to 0) one and a half stop bits is transmitted. Otherwise,   |
  +      +                         +     +                                                                                                                      +
  |      |                         |     | two stop bits are transmitted. Note that regardless of the number of stop bits selected,  the receiver checks only   |
  +      +                         +     +                                                                                                                      +
  |      |                         |     | the first stop bit.                                                                                                  |
  +      +                         +     +                                                                                                                      +
  |      |                         |     | 0 - 1 stop bit                                                                                                       |
  +      +                         +     +                                                                                                                      +
  |      |                         |     | 1 - 1.5 stop bits when DLS (LCR[1:0]) is 0, else 2 stop bits                                                         |
  +      +                         +     +                                                                                                                      +
  |      |                         |     | **NOTE**: The STOP bit duration implemented by UART may appear longer due to idle time inserted between              |
  +      +                         +     +                                                                                                                      +
  |      |                         |     | characters for some configurations and baud clock divisor values in the transmit direction.                          |
  +      +                         +     +                                                                                                                      +
  |      |                         |     | Reset Value: 0x0                                                                                                     |
  +------+-------------------------+-----+----------------------------------------------------------------------------------------------------------------------+
  | 1:0  | DLS (or CLS, as used in | R/W | Data Length Select. If UART_16550_COMPATIBLE = NO, then writable only when UART is not busy (USR[0] is 0);           |
  +      +                         +     +                                                                                                                      +
  |      | legacy)                 |     | otherwise always writable, always readable. When DLS_E is in LCR_EXT is set to 0, this register is used to select    |
  +      +                         +     +                                                                                                                      +
  |      |                         |     | the number of data bits per character that the peripheral transmits and receives. The number of bits that may be     |
  +      +                         +     +                                                                                                                      +
  |      |                         |     | selected are as follows:                                                                                             |
  +      +                         +     +                                                                                                                      +
  |      |                         |     | 00 - 5 bits                                                                                                          |
  +      +                         +     +                                                                                                                      +
  |      |                         |     | 01 - 6 bits                                                                                                          |
  +      +                         +     +                                                                                                                      +
  |      |                         |     | 10 - 7 bits                                                                                                          |
  +      +                         +     +                                                                                                                      +
  |      |                         |     | 11 - 8 bits                                                                                                          |
  +      +                         +     +                                                                                                                      +
  |      |                         |     | Reset Value: 0x0                                                                                                     |
  +------+-------------------------+-----+----------------------------------------------------------------------------------------------------------------------+

2.9 MCR
"""""""
- Name: Modem Control Register
- Size: 32 bits
- Address Offset: 0x10
- Read/write access: read/write

.. table::  MCR Register Fields

  +------+-------------------------+-----+--------------------------------------------------------------------------------------------------------------------------------+
  | Bits | Name                    | R/W | Description                                                                                                                    |
  +======+=========================+=====+================================================================================================================================+
  | 31:7 | Reserved and read as 0  |     |                                                                                                                                |
  +------+-------------------------+-----+--------------------------------------------------------------------------------------------------------------------------------+
  | 6    | SIRE                    | R/W | SIR Mode Enable. Writeable only when SIR_MODE = Enabled, always readable.                                                      |
  +      +                         +     +                                                                                                                                +
  |      |                         |     | 0 - IrDA SIR Mode disabled                                                                                                     |
  +      +                         +     +                                                                                                                                +
  |      |                         |     | 1 - IrDA SIR Mode enabled                                                                                                      |
  +      +                         +     +                                                                                                                                +
  |      |                         |     | Reset Value: 0x0                                                                                                               |
  +      +                         +     +                                                                                                                                +
  |      |                         |     | **Note**: To enable SIR mode, write the appropriate value to the MCR register before writing to the LCR register.              |
  +------+-------------------------+-----+--------------------------------------------------------------------------------------------------------------------------------+
  | 5    | AFCE                    | R/W | Auto Flow Control Enable. Writeable only when AFCE_MODE = Enabled, always readable. When FIFOs are enabled and the             |
  +      +                         +     +                                                                                                                                +
  |      |                         |     | Auto Flow Control Enable (AFCE) bit is set, Auto Flow Control features are enabled.                                            |
  +      +                         +     +                                                                                                                                +
  |      |                         |     | 0 - Auto Flow Control Mode disabled                                                                                            |
  +      +                         +     +                                                                                                                                +
  |      |                         |     | 1 - Auto Flow Control Mode enabled                                                                                             |
  +      +                         +     +                                                                                                                                +
  |      |                         |     | Reset Value: 0x0                                                                                                               |
  +------+-------------------------+-----+--------------------------------------------------------------------------------------------------------------------------------+


.. table::

  +------+-------------------------+-----+--------------------------------------------------------------------------------------------------------------------------------+
  | 4    | LoopBack (or LB)        | R/W | LoopBack Bit. This is used to put the UART into a diagnostic mode for test purposes. If operating in UART mode                 |
  +      +                         +     +                                                                                                                                +
  |      |                         |     | (SIR_MODE = Enabled or not active, MCR[6] set to 0), data on the sout line is held high, while serial data output is looped    |
  +      +                         +     +                                                                                                                                +
  |      |                         |     | back to the sin line, internally. In this mode all the interrupts are fully functional. Also, in loopback mode, the modem      |
  +      +                         +     +                                                                                                                                +
  |      |                         |     | control inputs (dsr_n, cts_n, ri_n, dcd_n) are disconnected and the modem control outputs (dtr_n, rts_n, out1_n, out2_n) are   |
  +      +                         +     +                                                                                                                                +
  |      |                         |     | looped back to the inputs, internally. If operating in infrared mode (SIR_MODE = Enabled AND active, MCR[6] set to 1),         |
  +      +                         +     +                                                                                                                                +
  |      |                         |     | data on the sir_out_n line is held low, while serial data output is inverted and looped back to the sir_in line.               |
  +      +                         +     +                                                                                                                                +
  |      |                         |     | Reset Value: 0x0                                                                                                               |
  +------+-------------------------+-----+--------------------------------------------------------------------------------------------------------------------------------+
  | 3    | OUT2                    | R/W | OUT2. This is used to directly control the user-designated Output2 (out2_n) output. The value written to this location is      |
  +      +                         +     +                                                                                                                                +
  |      |                         |     | inverted and driven out on out2_n, that is:                                                                                    |
  +      +                         +     +                                                                                                                                +
  |      |                         |     | 0 - out2_n de-asserted (logic 1)                                                                                               |
  +      +                         +     +                                                                                                                                +
  |      |                         |     | 1 - out2_n asserted (logic 0)                                                                                                  |
  +      +                         +     +                                                                                                                                +
  |      |                         |     | Note that in Loopback mode (MCR[4] set to 1), the out2_n output is held inactive high while the value of this location is      |
  |      |                         |     | internally looped back to an input.                                                                                            |
  +      +                         +     +                                                                                                                                +
  |      |                         |     | Reset Value: 0x0                                                                                                               |
  +------+-------------------------+-----+--------------------------------------------------------------------------------------------------------------------------------+
  | 2    | OUT1                    | R/W | OUT1. This is used to directly control the user-designated Output1 (out1_n) output. The value written to this location is      |
  |      |                         |     | inverted and driven out on out1_n, that is:                                                                                    |
  +      +                         +     +                                                                                                                                +
  |      |                         |     | 0 - out1_n de-asserted (logic 1)                                                                                               |
  +      +                         +     +                                                                                                                                +
  |      |                         |     | 1 - out1_n asserted (logic 0)                                                                                                  |
  +      +                         +     +                                                                                                                                +
  |      |                         |     | Note that in Loopback mode (MCR[4] set to 1), the out1_n output is held inactive high while the value of this location is      |
  |      |                         |     | internally looped back to an input.                                                                                            |
  +      +                         +     +                                                                                                                                +
  |      |                         |     | Reset Value: 0x0                                                                                                               |
  +------+-------------------------+-----+--------------------------------------------------------------------------------------------------------------------------------+


.. table::

  +------+-------------------------+-----+--------------------------------------------------------------------------------------------------------------------------------+
  | 1    | RTS                     | R/W | Request to Send. This is used to directly control the Request to Send (rts_n) output. The Request To Send (rts_n) output is    |
  +      +                         +     +                                                                                                                                +
  |      |                         |     | used to inform the modem or data set that the UART is ready to exchange data. When Auto RTS Flow Control is not enabled        |
  +      +                         +     +                                                                                                                                +
  |      |                         |     | (MCR[5] set to 0),  the rts_n signal is set low by programming MCR[1] (RTS) to a high.In Auto Flow Control,  AFCE_MODE =       |
  +      +                         +     +                                                                                                                                +
  |      |                         |     | Enabled and active (MCR[5] set to 1) and FIFOs enable (FCR[0] set to 1),  the rts_n output is controlled in the same way,      |
  +      +                         +     +                                                                                                                                +
  |      |                         |     | but is also gated with the receiver FIFO threshold trigger (rts_n is inactive high when above the threshold) only when the RTC |
  +      +                         +     +                                                                                                                                +
  |      |                         |     | Flow Trigger is disabled; otherwise it is gated by the receiver FIFO almost-full trigger, where “almost full” refers to two    |
  +      +                         +     +                                                                                                                                +
  |      |                         |     | available slots in the FIFO (rts_n is inactive high when above the threshold).  The rts_n signal is de-asserted when MCR[1]    |
  +      +                         +     +                                                                                                                                +
  |      |                         |     | is set low. Note that in Loopback mode (MCR[4] set to 1), the rts_n output is held inactive high while the value of this       |
  +      +                         +     +                                                                                                                                +
  |      |                         |     | location is internally looped back to an input.                                                                                |
  +      +                         +     +                                                                                                                                +
  |      |                         |     | Reset Value: 0x0                                                                                                               |
  +------+-------------------------+-----+--------------------------------------------------------------------------------------------------------------------------------+
  | 0    | DTR                     | R/W | Data Terminal Ready. This is used to directly control the Data Terminal Ready (dtr_n) output. The value written to this        |
  +      +                         +     +                                                                                                                                +
  |      |                         |     | location is inverted and driven out on dtr_n, that is:                                                                         |
  +      +                         +     +                                                                                                                                +
  |      |                         |     | 0 - dtr_n de-asserted (logic 1)                                                                                                |
  +      +                         +     +                                                                                                                                +
  |      |                         |     | 1 - dtr_n asserted (logic 0)                                                                                                   |
  +      +                         +     +                                                                                                                                +
  |      |                         |     | The Data Terminal Ready output is used to inform the modem or data set that the UART is ready to establish communications.     |
  +      +                         +     +                                                                                                                                +
  |      |                         |     | Note that in Loopback mode (MCR[4] set to 1), the dtr_n output is held inactive high while the value of this location is       |
  +      +                         +     +                                                                                                                                +
  |      |                         |     | internally looped back to an input.                                                                                            |
  +      +                         +     +                                                                                                                                +
  |      |                         |     | Reset Value: 0x0                                                                                                               |
  +------+-------------------------+-----+--------------------------------------------------------------------------------------------------------------------------------+

2.10 LSR
""""""""
- Name: Line Status Register
- Size: 32 bits
- Address Offset: 0x14
- Read/write access: read-only

.. table::  LSR Register Fields

  +------+---------+-----+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | Bits | Name    | R/W | Description                                                                                                                                                      |
  +======+=========+=====+==================================================================================================================================================================+
  | 31:9 |Reserved |     |                                                                                                                                                                  |
  |      |and read |     |                                                                                                                                                                  |
  |      |as 0     |     |                                                                                                                                                                  |
  +------+---------+-----+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | 8    |ADDR_RCVD| R/W | Address Received bit                                                                                                                                             |
  +      +         +     +                                                                                                                                                                  +
  |      |         |     | If 9-bit data mode (LCR_EXT[0]=1) is enabled, this bit is used to indicate that the 9th bit of                                                                   |
  +      +         +     +                                                                                                                                                                  +
  |      |         |     | the receive data is set to 1. This bit can also be used to indicate whether the incoming                                                                         |
  +      +         +     +                                                                                                                                                                  +
  |      |         |     | character is an address or data.                                                                                                                                 |
  +      +         +     +                                                                                                                                                                  +
  |      |         |     | 1 - Indicates that the character is an address.                                                                                                                  |
  +      +         +     +                                                                                                                                                                  +
  |      |         |     | 0 - Indicates that the character is data.                                                                                                                        |
  +      +         +     +                                                                                                                                                                  +
  |      |         |     | In the FIFO mode, since the 9th bit is associated with the received character, it is revealed                                                                    |
  +      +         +     +                                                                                                                                                                  +
  |      |         |     | when the character with the 9th bit set to 1 is at the top of the FIFO list. Reading the LSR                                                                     |
  +      +         +     +                                                                                                                                                                  +
  |      |         |     | clears the 9th bit.                                                                                                                                              |
  +      +         +     +                                                                                                                                                                  +
  |      |         |     | **NOTE**: You must ensure that an interrupt gets cleared (reading LSR register) before the next                                                                  |
  +      +         +     +                                                                                                                                                                  +
  |      |         |     | address byte arrives. If there is a delay in clearing the interrupt, then software will not                                                                      |
  +      +         +     +                                                                                                                                                                  +
  |      |         |     | be able to distinguish between multiple address related interrupt.                                                                                               |
  +      +         +     +                                                                                                                                                                  +
  |      |         |     | Reset Value: 0x0                                                                                                                                                 |
  +------+---------+-----+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
  
  
.. table::

  +------+---------+-----+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | 7    | RFE     | R   | Receiver FIFO Error bit. This bit is only relevant when FIFO_MODE != NONE and FIFOs are enabled (FCR[0] set to 1). This is used to indicate if there             |
  +      +         +     +                                                                                                                                                                  +
  |      |         |     | is at least one parity error, framing error, or break indication in the FIFO.                                                                                    |
  +      +         +     +                                                                                                                                                                  +
  |      |         |     | 0 - no error in RX FIFO                                                                                                                                          |
  +      +         +     +                                                                                                                                                                  +
  |      |         |     | 1 - error in RX FIFO                                                                                                                                             |
  +      +         +     +                                                                                                                                                                  +
  |      |         |     | This bit is cleared when the LSR is read and the character with the error is at the top of the receiver FIFO and there are no subsequent errors in               |
  +      +         +     +                                                                                                                                                                  +
  |      |         |     | the FIFO.                                                                                                                                                        |  
  +      +         +     +                                                                                                                                                                  +
  |      |         |     | Reset Value: 0x0                                                                                                                                                 |
  +------+---------+-----+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | 6    | TEMT    | R   | Transmitter Empty bit. If in FIFO mode (FIFO_MODE != NONE) and FIFOs enabled (FCR[0] set to 1), this bit is set whenever the Transmitter Shift                   |
  +      +         +     +                                                                                                                                                                  +
  |      |         |     | Register and the FIFO are both empty. If in non-FIFO mode or FIFOs are disabled, this bit is set whenever the Transmitter Holding Register and the               |
  +      +         +     +                                                                                                                                                                  +
  |      |         |     | Transmitter Shift Register are both empty.                                                                                                                       |
  +      +         +     +                                                                                                                                                                  +
  |      |         |     | Reset Value: 0x1                                                                                                                                                 |
  +------+---------+-----+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | 5    | THRE    | R   | Transmit Holding Register Empty bit. If THRE_MODE_USER = Disabled or THRE mode is disabled (IER[7] set to 0) and regardless of FIFOs being                       |
  +      +         +     +                                                                                                                                                                  +
  |      |         |     | implemented/enabled or not, this bit indicates that the THR or TX FIFO is empty.                                                                                 |
  +      +         +     +                                                                                                                                                                  +
  |      |         |     | This bit is set whenever data is transferred from the THR or TX FIFO to the transmitter shift register and no new data has been written to the THR               |
  +      +         +     +                                                                                                                                                                  +
  |      |         |     | or TX FIFO. This also causes a THRE Interrupt to occur, if the THRE Interrupt is enabled. If THRE_MODE_USER = Enabled and FIFO_MODE != NONE                      |
  +      +         +     +                                                                                                                                                                  +
  |      |         |     | and both modes are active (IER[7] set to 1 and FCR[0] set to 1 respectively), the functionality is switched to indicate the transmitter FIFO                     |
  +      +         +     +                                                                                                                                                                  + 
  |      |         |     | is full, and no longer controls THRE interrupts, which are then controlled by the FCR[5:4] threshold setting.                                                    |
  +      +         +     +                                                                                                                                                                  +
  |      |         |     | Reset Value: 0x1                                                                                                                                                 |
  +------+---------+-----+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
  
  
.. table::

  +------+---------+-----+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | 4    | BI      | R   | Break Interrupt bit. This is used to indicate the detection of a break sequence on the serial input data.                                                        |
  +      +         +     +                                                                                                                                                                  +
  |      |         |     | If in UART mode (SIR_MODE = Disabled), it is set whenever the serial input, sin, is held in a 'logic 0' state for longer than the sum of start time              |
  +      +         +     +                                                                                                                                                                  +
  |      |         |     | \+\ data bits \+\ parity \+\ stop bits. If in infrared mode (SIR_MODE = Enabled), it is set whenever the serial input, sir_in, is continuously pulsed to         |
  +      +         +     +                                                                                                                                                                  +
  |      |         |     | logic '0' for longer than the sum of start time + data bits + parity + stop bits. A break condition on serial input causes one and only one                      |
  +      +         +     +                                                                                                                                                                  +
  |      |         |     | character, consisting of all 0s, to be received by the UART.                                                                                                     |
  +      +         +     +                                                                                                                                                                  +
  |      |         |     | In FIFO mode, the character associated with the break condition is carried through the FIFO and is revealed when the character is at the top of the              |
  +      +         +     +                                                                                                                                                                  +
  |      |         |     | FIFO list. Reading the LSR clears the BI bit. In non-FIFO mode, the BI indication occurs immediately and persists until the LSR is read.                         |
  +      +         +     +                                                                                                                                                                  +
  |      |         |     | **NOTE**: If a FIFO is full when a break condition is received, a FIFO overrun occurs. The break condition and all the information associated with               |
  +      +         +     +                                                                                                                                                                  +
  |      |         |     | it—parity and framing errors—is discarded; any information that a break character was received is lost.                                                          |
  +      +         +     +                                                                                                                                                                  +
  |      |         |     | Reset Value: 0x0                                                                                                                                                 |
  +------+---------+-----+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
  
  
.. table::

  +------+---------+-----+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | 3    | FE      | R   | Framing Error bit. This is used to indicate the occurrence of a framing error in the receiver. A framing error occurs when the receiver does not detect a        |
  +      +         +     +                                                                                                                                                                  +
  |      |         |     | valid STOP bit in the received data. In the FIFO mode, since the framing error is associated with a character received, it is revealed when the character with   |
  +      +         +     +                                                                                                                                                                  +
  |      |         |     | the framing error is at the top of the FIFO. When a framing error occurs, the UART tries to resynchronize. It does this by assuming that the error was due       |
  +      +         +     +                                                                                                                                                                  +
  |      |         |     | to the start bit of the next character and then continues receiving the other bit; that is, data, and/or parity and stop.                                        |
  +      +         +     +                                                                                                                                                                  +
  |      |         |     | It should be noted that the Framing Error (FE) bit (LSR[3]) is set if a break interrupt has occurred, as indicated by Break Interrupt (BI) bit (LSR[4]). This    |
  +      +         +     +                                                                                                                                                                  +
  |      |         |     | happens because the break character implicitly generates a framing error by holding the sin input to logic 0 for longer than the duration of a character.        |
  +      +         +     +                                                                                                                                                                  +
  |      |         |     | 0 - no framing error                                                                                                                                             |
  +      +         +     +                                                                                                                                                                  +
  |      |         |     | 1 - framing error                                                                                                                                                |
  +      +         +     +                                                                                                                                                                  +
  |      |         |     | Reading the LSR clears the FE bit.                                                                                                                               |
  +      +         +     +                                                                                                                                                                  +
  |      |         |     | Reset Value: 0x0                                                                                                                                                 |
  +------+---------+-----+------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. table::

  +------+---------+-----+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | 2    | PE      | R   | Parity Error bit. This is used to indicate the occurrence of a parity error in the receiver if the Parity Enable (PEN) bit (LCR[3]) is set.                      |
  +      +         +     +                                                                                                                                                                  +
  |      |         |     | In the FIFO mode, since the parity error is associated with a character received, it is revealed when the character with the parity error arrives at the top of  |
  +      +         +     +                                                                                                                                                                  +
  |      |         |     | the FIFO.                                                                                                                                                        |
  +      +         +     +                                                                                                                                                                  +
  |      |         |     | It should be noted that the Parity Error (PE) bit (LSR[2]) can be set if a break interrupt has occurred, as indicated by Break Interrupt (BI) bit (LSR[4]). In   |
  +      +         +     +                                                                                                                                                                  +
  |      |         |     | this situation, the Parity Error bit is set if parity generation and detection is enabled (LCR[3]=1) and the parity is set to odd (LCR[4]=0).                    |
  +      +         +     +                                                                                                                                                                  +
  |      |         |     | 0 - no parity error                                                                                                                                              |
  +      +         +     +                                                                                                                                                                  +
  |      |         |     | 1 - parity error                                                                                                                                                 |
  +      +         +     +                                                                                                                                                                  +
  |      |         |     | Reading the LSR clears the PE bit.                                                                                                                               |
  +      +         +     +                                                                                                                                                                  +
  |      |         |     | Reset Value: 0x0                                                                                                                                                 |
  +------+---------+-----+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
  
  
.. table::
  
  +------+---------+-----+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | 1    | OE      | R   | Overrun error bit. This is used to indicate the occurrence of an overrun error. This occurs if a new data character was received before the previous data was    |
  +      +         +     +                                                                                                                                                                  +
  |      |         |     | read. In the non-FIFO mode, the OE bit is set when a new character arrives in the receiver before the previous character was read from the RBR. When this        |
  +      +         +     +                                                                                                                                                                  +
  |      |         |     | happens, the data in the RBR is overwritten. In the FIFO mode, an overrun error occurs when the FIFO is full and a new character arrives at the receiver. The    |
  +      +         +     +                                                                                                                                                                  +
  |      |         |     | data in the FIFO is retained and the data in the receive shift register is lost.                                                                                 |
  +      +         +     +                                                                                                                                                                  +
  |      |         |     | 0 - no overrun error                                                                                                                                             |
  +      +         +     +                                                                                                                                                                  +
  |      |         |     | 1 - overrun error                                                                                                                                                |
  +      +         +     +                                                                                                                                                                  +
  |      |         |     | Reading the LSR clears the OE bit.                                                                                                                               |
  +      +         +     +                                                                                                                                                                  +
  |      |         |     | Reset Value: 0x0                                                                                                                                                 |
  +------+---------+-----+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | 0    | DR      | R   | Data Ready bit. This is used to indicate that the receiver contains at least one character in the RBR or the receiver FIFO.                                      |
  +      +         +     +                                                                                                                                                                  +
  |      |         |     | 0 - no data ready                                                                                                                                                |
  +      +         +     +                                                                                                                                                                  +
  |      |         |     | 1 - data ready                                                                                                                                                   |
  +      +         +     +                                                                                                                                                                  +
  |      |         |     | This bit is cleared when the RBR is read in non-FIFO mode, or when the receiver FIFO is empty, in FIFO mode.                                                     |
  +      +         +     +                                                                                                                                                                  +
  |      |         |     | Reset Value: 0x0                                                                                                                                                 |
  +------+---------+-----+------------------------------------------------------------------------------------------------------------------------------------------------------------------+

2.11 MSR
""""""""
- Name: Modem Status Register
- Size: 32 bits
- Address Offset: 0x18
- Read/write access: read-only

Whenever bits 0, 1, 2 or 3 are set to logic 1, to indicate a change on the modem control inputs, a modem 
status interrupt is generated if enabled through the IER, regardless of when the change occurred. The bits of 
this register can be set after a reset—even though their respective modem signals are inactive—because the 
synchronized version of the modem signals have a reset value of 0 and change to value 1 after reset. To 
prevent unwanted interrupts due to this change, a read of the MSR register can be performed after reset.

.. table::  MSR Register Fields

  +------+---------+-----+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | Bits | Name    | R/W | Description                                                                                                                                                 |
  +======+=========+=====+=============================================================================================================================================================+
  | 31:8 | Reserved|     |                                                                                                                                                             |
  |      | and read|     |                                                                                                                                                             |
  |      | as 0    |     |                                                                                                                                                             |
  +------+---------+-----+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | 7    | DCD     | R   | Data Carrier Detect. This is used to indicate the current state of the modem control line dcd_n. This bit is the complement of                              |
  +      +         +     +                                                                                                                                                             +
  |      |         |     | dcd_n. When the Data Carrier Detect input (dcd_n) is asserted it is an indication that the carrier has been detected by the                                 |
  |      |         |     | modem or data set.                                                                                                                                          |
  +      +         +     +                                                                                                                                                             +
  |      |         |     | 0 - dcd_n input is de-asserted (logic 1)                                                                                                                    |
  +      +         +     +                                                                                                                                                             +
  |      |         |     | 1 - dcd_n input is asserted (logic 0)                                                                                                                       |
  +      +         +     +                                                                                                                                                             +
  |      |         |     | In Loopback Mode (MCR[4] set to 1), DCD is the same as MCR[3] (Out2).                                                                                       |
  +      +         +     +                                                                                                                                                             +
  |      |         |     | Reset Value: 0x0                                                                                                                                            |
  +------+---------+-----+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | 6    | RI      | R   | Ring Indicator. This is used to indicate the current state of the modem control line ri_n. This bit is the complement of ri_n.                              |
  +      +         +     +                                                                                                                                                             +
  |      |         |     | When the Ring Indicator input (ri_n) is asserted it is an indication that a telephone ringing signal has been received by the                               |
  +      +         +     +                                                                                                                                                             +
  |      |         |     | modem or data set.                                                                                                                                          |
  +      +         +     +                                                                                                                                                             +
  |      |         |     | 0 - ri_n input is de-asserted (logic 1)                                                                                                                     |
  +      +         +     +                                                                                                                                                             +
  |      |         |     | 1 - ri_n input is asserted (logic 0)                                                                                                                        |
  +      +         +     +                                                                                                                                                             +
  |      |         |     | In Loopback Mode (MCR[4] set to 1), RI is the same as MCR[2] (Out1).                                                                                        |
  +      +         +     +                                                                                                                                                             +
  |      |         |     | Reset Value: 0x0                                                                                                                                            |
  +------+---------+-----+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
  
  
.. table::

  +------+---------+-----+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | 5    | DSR     | R   | Data Set Ready. This is used to indicate the current state of the modem control line dsr_n. This bit is the complement of dsr_n.                            |
  +      +         +     +                                                                                                                                                             +
  |      |         |     | When the Data Set Ready input (dsr_n) is asserted it is an indication that the modem or data set is ready to establish                                      |
  +      +         +     +                                                                                                                                                             +
  |      |         |     | communications with the UART.                                                                                                                               |
  +      +         +     +                                                                                                                                                             +
  |      |         |     | 0 - dsr_n input is de-asserted (logic 1)                                                                                                                    |
  +      +         +     +                                                                                                                                                             +
  |      |         |     | 1 - dsr_n input is asserted (logic 0)                                                                                                                       |
  +      +         +     +                                                                                                                                                             +
  |      |         |     | In Loopback Mode (MCR[4] set to 1), DSR is the same as MCR[0] (DTR).                                                                                        |
  +      +         +     +                                                                                                                                                             +
  |      |         |     | Reset Value: 0x0                                                                                                                                            |
  +------+---------+-----+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | 4    | CTS     | R   | Clear to Send. This is used to indicate the current state of the modem control line cts_n. This bit is the complement of cts_n. When the Clear to Send      |
  +      +         +     +                                                                                                                                                             +
  |      |         |     | input (cts_n) is asserted it is an indication that the modem or data set is ready to exchange data with the UART.                                           |
  +      +         +     +                                                                                                                                                             +
  |      |         |     | 0 - cts_n input is de-asserted (logic 1)                                                                                                                    |
  +      +         +     +                                                                                                                                                             +
  |      |         |     | 1 - cts_n input is asserted (logic 0)                                                                                                                       |
  +      +         +     +                                                                                                                                                             +
  |      |         |     | In Loopback Mode (MCR[4] = 1), CTS is the same as MCR[1] (RTS).                                                                                             |
  +      +         +     +                                                                                                                                                             +
  |      |         |     | Reset Value: 0x0                                                                                                                                            |
  +------+---------+-----+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | 3    | DDCD    | R   | Delta Data Carrier Detect. This is used to indicate that the modem control line dcd_n has changed since the last time the MSR was read.                     |
  +      +         +     +                                                                                                                                                             +
  |      |         |     | 0 - no change on dcd_n since last read of MSR                                                                                                               |
  +      +         +     +                                                                                                                                                             +
  |      |         |     | 1 - change on dcd_n since last read of MSR                                                                                                                  |
  +      +         +     +                                                                                                                                                             +
  |      |         |     | Reading the MSR clears the DDCD bit. In Loopback Mode (MCR[4] = 1), DDCD reflects changes on MCR[3] (Out2).                                                 |
  +      +         +     +                                                                                                                                                             +
  |      |         |     | Note, if the DDCD bit is not set and the dcd_n signal is asserted (low) and a reset occurs (software or otherwise), then the DDCD bit is set when the reset |
  +      +         +     +                                                                                                                                                             +
  |      |         |     | is removed if the dcd_n signal remains asserted.                                                                                                            |
  +      +         +     +                                                                                                                                                             +
  |      |         |     | Reset Value: 0x0                                                                                                                                            |
  +------+---------+-----+-------------------------------------------------------------------------------------------------------------------------------------------------------------+ 
  
.. table::

  +------+---------+-----+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | 2    | TERI    | R   | Trailing Edge of Ring Indicator. This is used to indicate that a change on the input ri_n (from an active-low to an inactive-high state) has occurred since |
  +      +         +     +                                                                                                                                                             +
  |      |         |     | the last time the MSR was read.                                                                                                                             |
  +      +         +     +                                                                                                                                                             +
  |      |         |     | 0 - no change on ri_n since last read of MSR                                                                                                                |
  +      +         +     +                                                                                                                                                             +
  |      |         |     | 1 - change on ri_n since last read of MSR                                                                                                                   |
  +      +         +     +                                                                                                                                                             +
  |      |         |     | Reading the MSR clears the TERI bit. In Loopback Mode (MCR[4] = 1), TERI reflects when MCR[2] (Out1) has changed state from a high to a low.                |
  +      +         +     +                                                                                                                                                             +
  |      |         |     | Reset Value: 0x0                                                                                                                                            |
  +------+---------+-----+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | 1    | DDSR    | R   | Delta Data Set Ready. This is used to indicate that the modem control line dsr_n has changed since the last time the MSR was read.                          |
  +      +         +     +                                                                                                                                                             +
  |      |         |     | 0 - no change on dsr_n since last read of MSR                                                                                                               |
  +      +         +     +                                                                                                                                                             +
  |      |         |     | 1 - change on dsr_n since last read of MSR                                                                                                                  |
  +      +         +     +                                                                                                                                                             +
  |      |         |     | Reading the MSR clears the DDSR bit. In Loopback Mode (MCR[4] = 1), DDSR reflects changes on MCR[0] (DTR).                                                  |
  +      +         +     +                                                                                                                                                             +
  |      |         |     | Note, if the DDSR bit is not set and the dsr_n signal is asserted (low) and a reset occurs (software or otherwise), then the DDSR bit is set when the reset |
  +      +         +     +                                                                                                                                                             +
  |      |         |     | is removed if the dsr_n signal remains asserted.                                                                                                            |
  +      +         +     +                                                                                                                                                             +
  |      |         |     | Reset Value: 0x0                                                                                                                                            |
  +------+---------+-----+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | 0    | DCTS    | R   | Delta Clear to Send. This is used to indicate that the modem control line cts_n has changed since the last time the MSR was read.                           |
  +      +         +     +                                                                                                                                                             +
  |      |         |     | 0 - no change on cts_n since last read of MSR                                                                                                               |
  +      +         +     +                                                                                                                                                             +
  |      |         |     | 1 - change on cts_n since last read of MSR                                                                                                                  |
  +      +         +     +                                                                                                                                                             +
  |      |         |     | Reading the MSR clears the DCTS bit. In Loopback Mode (MCR[4] = 1), DCTS reflects changes on MCR[1] (RTS).                                                  |
  +      +         +     +                                                                                                                                                             +
  |      |         |     | Note, if the DCTS bit is not set and the cts_n signal is asserted (low) and a reset occurs (software or otherwise), then the DCTS bit is set when the reset |
  +      +         +     +                                                                                                                                                             +
  |      |         |     | is removed if the cts_n signal remains asserted.                                                                                                            |
  +      +         +     +                                                                                                                                                             +
  |      |         |     | Reset Value: 0x0                                                                                                                                            |
  +------+---------+-----+-------------------------------------------------------------------------------------------------------------------------------------------------------------+

2.12 SCR
""""""""
- Name: Scratchpad Register
- Size: 32 bits
- Address Offset: 0x1C
- Read/write access: read/write

.. table::  SCR Register Fields

  +------+------------------------+-----+--------------------------------------------------------------------------------------------+
  | Bits | Name                   | R/W | Description                                                                                |
  +======+========================+=====+============================================================================================+
  | 31:8 | Reserved and read as 0 |     |                                                                                            |
  +------+------------------------+-----+--------------------------------------------------------------------------------------------+
  | 7:0  | Scratchpad Register    | R/W | This register is for programmers to use as a temporary storage space. It has no defined    |
  +      +                        +     +                                                                                            +
  |      |                        |     | purpose in the UART.                                                                       |
  +      +                        +     +                                                                                            +
  |      |                        |     | Reset Value: 0x0                                                                           |
  +------+------------------------+-----+--------------------------------------------------------------------------------------------+

2.13 LPDLL
""""""""""
- Name: Low Power Divisor Latch Low Register
- Size: 32 bits
- Address Offset: 0x20
- Read/write access: read/write

This register is only valid when the UART is configured to have SIR low-power reception 
capabilities implemented (SIR_LP_RX = Yes). If SIR low-power reception capabilities are not implemented, 
this register does not exist and reading from this register address returns 0.

If UART_16550_COMPATIBLE = No, then this register can be accessed only when the DLAB bit (LCR[7]) is 
set and the UART is not busy—that is, USR[0] is 0; otherwise this register can be accessed only when the 
DLAB bit (LCR[7]) is set.

.. table::  LPDLL Register Fields

  +------+------------------------+-----+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | Bits | Name                   | R/W | Description                                                                                                                                                                                                                                                           |                                                                                                                                                                                                                      
  +======+========================+=====+=======================================================================================================================================================================================================================================================================+
  | 31:8 | Reserved and read as 0 |     |                                                                                                                                                                                                                                                                       |                                                                                                                                                                                             
  +------+------------------------+-----+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | 7:0  | LPDLL                  | R/W | This register makes up the lower 8-bits of a 16-bit, read/write, Low Power Divisor Latch register that contains the baud rate divisor for the UART, which must give a baud rate of 115.2K. This is required for SIR Low Power (minimum pulse width) detection at the  |      
  +      +                        +     +                                                                                                                                                                                                                                                                       +                                                                                                                                                                                                                
  |      |                        |     | receiver.                                                                                                                                                                                                                                                             | 
  |      |                        |     |                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                    
  |      |                        |     | The output low-power baud rate is equal to the serial clock (sclk) frequency divided by sixteen times the value of the baud rate divisor, as follows:                                                                                                                 | 
  |      |                        |     |                                                                                                                                                                                                                                                                       |
  |      |                        |     | Low power baud rate = (serial clock frequency)/(16* divisor)                                                                                                                                                                                                          |
  |      |                        |     |                                                                                                                                                                                                                                                                       |
  |      |                        |     | Therefore, a divisor must be selected to give a baud rate of 115.2K.                                                                                                                                                                                                  |
  |      |                        |     |                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                   
  |      |                        |     | **NOTE**: When the Low Power Divisor Latch registers (LPDLL and LPDLH) are set to 0, the low-power baud clock is disabled and no low-power pulse detection (or any pulse detection) occurs at the receiver. Also, once the LPDLL is set, at least eight clock cycles  |
  +      +                        +     +                                                                                                                                                                                                                                                                       + 
  |      |                        |     | of the slowest UART clock should be allowed to pass before transmitting or receiving data.                                                                                                                                                                            |
  |      |                        |     |                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                       
  |      |                        |     | Reset Value: 0x0                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                    
  +------+------------------------+-----+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

2.14 LPDLH
""""""""""
- Name: Low Power Divisor Latch High Register
- Size: 32 bits
- Address Offset: 0x24
- Read/write access: read/write

This register is valid only when the UART is configured to have SIR low-power reception 
capabilities implemented (SIR_LP_RX = Yes). If SIR low-power reception capabilities are not implemented, 
this register does not exist and reading from this register address returns 0.

If UART_16550_COMPATIBLE = No, then this register can be accessed only when the DLAB bit (LCR[7]) is 
set and the UART is not busy—that is, USR[0] is 0; otherwise this register can be accessed only when the 
DLAB bit (LCR[7]) is set.

.. table::  LPDLH Register Fields

  +------+------------------------+-----+----------------------------------------------------------------------------------------------------+
  | Bits | Name                   | R/W | Description                                                                                        |
  +======+========================+=====+====================================================================================================+
  | 31:8 | Reserved and read as 0 |     |                                                                                                    |
  +------+------------------------+-----+----------------------------------------------------------------------------------------------------+
  | 7:0  | LPDLH                  | R/W | This register makes up the upper 8-bits of a 16-bit, read/write, Low Power Divisor Latch register  |
  +      +                        +     +                                                                                                    +
  |      |                        |     | that contains the baud rate divisor for the UART, which must give a baud rate of 115.2K. This is   |
  +      +                        +     +                                                                                                    +
  |      |                        |     | required for SIR Low Power (minimum pulse width) detection at the receiver.                        |
  +      +                        +     +                                                                                                    +
  |      |                        |     | The output low-power baud rate is equal to the serial clock (sclk) frequency divided by sixteen    |
  +      +                        +     +                                                                                                    +
  |      |                        |     | times the value of the baud rate divisor, as follows:                                              |
  +      +                        +     +                                                                                                    +
  |      |                        |     | Low power baud rate = (serial clock frequency)/(16* divisor)                                       |
  +      +                        +     +                                                                                                    +
  |      |                        |     | Therefore, a divisor must be selected to give a baud rate of 115.2K.                               |
  +      +                        +     +                                                                                                    +
  |      |                        |     | **NOTE**: When the Low Power Divisor Latch registers (LPDLL and LPDLH) are set to 0, the low-power |
  +      +                        +     +                                                                                                    +
  |      |                        |     | baud clock is disabled and no low-power pulse detection (or any pulse detection) occurs at the     |
  +      +                        +     +                                                                                                    +
  |      |                        |     | receiver. Also, once the LPDLH is set, at least eight clock cycles of the slowest UART             |
  +      +                        +     +                                                                                                    +
  |      |                        |     | clock should be allowed to pass before transmitting or receiving data.                             |
  +      +                        +     +                                                                                                    +
  |      |                        |     | Reset Value: 0x0                                                                                   |
  +------+------------------------+-----+----------------------------------------------------------------------------------------------------+

2.15 SRBR
"""""""""
- Name: Shadow Receive Buffer Register
- Size: 32 bits
- Address Offset: 0x30 - 0x6C
- Read/write access: read-only

This register is valid only when the UART is configured to have additional shadow registers 
implemented (SHADOW = YES). If shadow registers are not implemented, this register does not exist and 
reading from this register address returns 0.

This register can be accessed only when the DLAB bit (LCR[7]) is cleared.

.. table::  SRBR Register Fields

  +------+-----------------------------------+-----+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | Bits | Name                              | R/W | Description                                                                                                                                                     |
  +======+===================================+=====+=================================================================================================================================================================+
  | 31:9 | Reserved and read as 0            |     |                                                                                                                                                                 |
  +------+-----------------------------------+-----+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | 8    | Shadow Receive Buffer Register    |  R  | This is a shadow register for the RBR[8] bit. It is applicable only when UART_9BIT_DATA_EN=1.                                                                   |
  |      | (MSB 9th bit)                     |     |                                                                                                                                                                 |
  |      |                                   |     | Reset Value: 0x0                                                                                                                                                |
  +------+-----------------------------------+-----+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | 7:0  | Shadow Receive Buffer Register    | R   | This is a shadow register for the RBR and has been allocated sixteen 32-bit locations so as to accommodate burst accesses from the master. This register        |
  +      +                                   +     +                                                                                                                                                                 +
  |      | (LSB 8 bits)                      |     | contains the data byte received on the serial input port (sin) in UART mode or the serial infrared input (sir_in) in infrared mode. The data in this register   |
  +      +                                   +     +                                                                                                                                                                 +
  |      |                                   |     | is valid only if the Data Ready (DR) bit in the Line status Register (LSR) is set.                                                                              |
  +      +                                   +     +                                                                                                                                                                 +
  |      |                                   |     | If in non-FIFO mode (FIFO_MODE = NONE) or FIFOs are disabled (FCR[0] set to 0), the data in the RBR must be read before the next data arrives, otherwise it is  |
  +      +                                   +     +                                                                                                                                                                 +
  |      |                                   |     | overwritten, resulting in an overrun error.                                                                                                                     |
  +      +                                   +     +                                                                                                                                                                 +
  |      |                                   |     | If in FIFO mode (FIFO_MODE != NONE) and FIFOs are enabled (FCR[0] set to 1), this register accesses the head of the receive FIFO. If the receive FIFO is full   |
  +      +                                   +     +                                                                                                                                                                 +
  |      |                                   |     | and this register is not read before the next data character arrives, then the data already in the FIFO are preserved, but any incoming data is lost. An        |
  +      +                                   +     +                                                                                                                                                                 +
  |      |                                   |     | overrun error also occurs.                                                                                                                                      |
  +      +                                   +     +                                                                                                                                                                 +
  |      |                                   |     | Reset Value: 0x0                                                                                                                                                |
  +------+-----------------------------------+-----+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

2.16 STHR
"""""""""
- Name: Shadow Transmit Holding Register
- Size: 32 bits
- Address Offset: 0x30 - 0x6C
- Read/write access: write

This register is valid only when the UART is configured to have additional shadow registers 
implemented (SHADOW = YES). If shadow registers are not implemented, this register does not exist, and 
reading from this register address returns 0.

This register can be accessed only when the DLAB bit (LCR[7]) is cleared.

.. table::  STHR Register Fields

  +------+--------------------------------+-----+----------------------------------------------------------------+
  | Bits | Name                           | R/W | Description                                                    |
  +======+================================+=====+================================================================+
  | 31:9 | Reserved and read as 0         |     |                                                                |
  +------+--------------------------------+-----+----------------------------------------------------------------+
  | 8    | Shadow Transmit Holding        | W   | This is a shadow register for the THR[8] bit. It is applicable |
  +      +                                +     +                                                                +
  |      | Register (MSB 9th bit)         |     | only when UART_9BIT_DATA_EN=1.                                 |
  +      +                                +     +                                                                +
  |      |                                |     | Reset Value: 0x0                                               |
  +------+--------------------------------+-----+----------------------------------------------------------------+
  | 7:0  | Shadow Transmit Holding        | W   | This is a shadow register for the THR and has been allocated   |
  +      +                                +     +                                                                +
  |      | Register                       |     | sixteen 32-bit locations so as to accommodate burst accesses   |
  +      +                                +     +                                                                +
  |      |                                |     | from the master. This register contains data to be transmitted |
  +      +                                +     +                                                                +
  |      |                                |     | on the serial output port (sout) in UART mode or the serial    |
  +      +                                +     +                                                                +
  |      |                                |     | infrared output (sir_out_n) in infrared mode. Data should only |
  +      +                                +     +                                                                +
  |      |                                |     | be written to the THR when the THR Empty (THRE) bit (LSR[5]) is|
  +      +                                +     +                                                                +
  |      |                                |     | set. If in non-FIFO mode or FIFOs are disabled                 |
  +      +                                +     +                                                                +
  |      |                                |     | (FCR[0] set to 0) and THRE is set, writing a single character  |
  +      +                                +     +                                                                +
  |      |                                |     | to the THR clears the THRE. Any additional writes to the       |
  +      +                                +     +                                                                +
  |      |                                |     | THR before the THRE is set again causes the THR data to be     |
  +      +                                +     +                                                                +
  |      |                                |     | overwritten. If in FIFO mode and FIFOs are enabled             |
  +      +                                +     +                                                                +
  |      |                                |     | (FCR[0] set to 1) and THRE is set, x number of characters of   |
  +      +                                +     +                                                                +
  |      |                                |     | data may be written to the THR before the FIFO is full.        |
  +      +                                +     +                                                                +
  |      |                                |     | The number x (default=16) is determined by the value of FIFO   |
  +      +                                +     +                                                                +
  |      |                                |     | Depth that you set during configuration. Any attempt to write  |
  +      +                                +     +                                                                +
  |      |                                |     | data when the FIFO is full results in the write                |
  +      +                                +     +                                                                +
  |      |                                |     | data being lost.                                               |
  +      +                                +     +                                                                +
  |      |                                |     | Reset Value: 0x0                                               |
  +------+--------------------------------+-----+----------------------------------------------------------------+

2.17 FAR
""""""""
- Name: FIFO Access Register
- Size: 32 bits
- Address Offset: 0x70
- Read/write access: read/write

.. table::  FAR Register Fields

  +------+----------------------+-----+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | Bits | Name                 | R/W | Description                                                                                                                                                      |
  +======+======================+=====+==================================================================================================================================================================+
  | 31:1 | Reserved and read as |     |                                                                                                                                                                  |
  |      | 0                    |     |                                                                                                                                                                  |
  +------+----------------------+-----+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | 0    | FIFO Access Register | R/W | Writes have no effect when FIFO_ACCESS = No, always readable. This register is use to enable a FIFO access mode for testing, so that the receive FIFO can be     |
  +      +                      +     +                                                                                                                                                                  +
  |      |                      |     | written by the master and the transmit FIFO can be read by the master when FIFOs are implemented and enabled. When FIFOs are not implemented or not enabled it   |
  +      +                      +     +                                                                                                                                                                  +
  |      |                      |     | allows the RBR to be written by the master and the THR to be read by the master.                                                                                 |
  +      +                      +     +                                                                                                                                                                  +
  |      |                      |     | 0 - FIFO access mode disabled                                                                                                                                    |
  +      +                      +     +                                                                                                                                                                  +
  |      |                      |     | 1 - FIFO access mode enabled                                                                                                                                     |
  +      +                      +     +                                                                                                                                                                  +
  |      |                      |     | Note, that when the FIFO access mode is enabled/disabled, the control portion of the receive FIFO and transmit FIFO is reset and the FIFOs are treated as empty. |
  +      +                      +     +                                                                                                                                                                  +
  |      |                      |     | Reset Value: 0x0                                                                                                                                                 |
  +------+----------------------+-----+------------------------------------------------------------------------------------------------------------------------------------------------------------------+

2.18 TFR
""""""""
- Name: Transmit FIFO Read
- Size: 32 bits
- Address Offset: 0x74
- Read/write access: read-only

This register is valid only when the UART is configured to have the FIFO access test mode available 
(FIFO_ACCESS = YES). If not configured, this register does not exist and reading from this register address 
returns 0.

.. table::  TFR Register Fields

  +------+-------------------+-----+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | Bits | Name              | R/W | Description                                                                                                                                                                                                                        |
  +======+===================+=====+====================================================================================================================================================================================================================================+
  | 31:8 | Reserved and read |     |                                                                                                                                                                                                                                    |
  |      | as 0              |     |                                                                                                                                                                                                                                    |
  +------+-------------------+-----+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | 7:0  | Transmit FIFO     | R   | Transmit FIFO Read. These bits are only valid when FIFO access mode is enabled (FAR[0] is set to 1).                                                                                                                               |
  +      +                   +     +                                                                                                                                                                                                                                    +
  |      | Read              |     | When FIFOs are implemented and enabled, reading this register gives the data at the top of the transmit FIFO. Each consecutive read pops the transmit FIFO and gives the next data value that is currently at the top of the FIFO. |
  +      +                   +     +                                                                                                                                                                                                                                    +
  |      |                   |     | When FIFOs are not implemented or not enabled, reading this register gives the data in the THR.                                                                                                                                    |
  +      +                   +     +                                                                                                                                                                                                                                    +
  |      |                   |     | Reset Value: 0x0                                                                                                                                                                                                                   |
  +------+-------------------+-----+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

2.19 RFW
""""""""
- Name: Receive FIFO Write
- Size: 32 bits
- Address Offset: 0x78
- Read/write access: write-only

This register is valid only when the UART is configured to have the FIFO access test mode available 
(FIFO_ACCESS = YES). If not configured, this register does not exist and reading from this register address 
returns 0.

.. table::  RFW Register Fields

  +-------+------------------+-----+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | Bits  | Name             | R/W | Description                                                                                                                                                                             |
  +=======+==================+=====+=========================================================================================================================================================================================+
  | 31:10 | Reserved and     |     |                                                                                                                                                                                         |
  +       +                  +     +                                                                                                                                                                                         +             
  |       | read as 0        |     |                                                                                                                                                                                         |
  +-------+------------------+-----+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | 9     | RFFE             | W   | Receive FIFO Framing Error. These bits are only valid when FIFO access mode is enabled (FAR[0] is set to 1). When FIFOs are implemented and enabled, this bit is used to write framing  |
  +       +                  +     +                                                                                                                                                                                         + 
  |       |                  |     | error detection information to the receive FIFO. When FIFOs are not implemented or not enabled, this bit is used to write framing error detection information to the RBR.               |
  +       +                  +     +                                                                                                                                                                                         + 
  |       |                  |     | Reset Value: 0x0                                                                                                                                                                        |
  +-------+------------------+-----+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | 8     | RFPE             | W   | Receive FIFO Parity Error. These bits are only valid when FIFO access mode is enabled (FAR[0] is set to 1). When FIFOs are implemented and enabled, this bit is used to write parity    |
  +       +                  +     +                                                                                                                                                                                         + 
  |       |                  |     | error detection information to the receive FIFO. When FIFOs are not implemented or not enabled, this bit is used to write parity error detection information to the RBR.                |
  +       +                  +     +                                                                                                                                                                                         + 
  |       |                  |     | Reset Value: 0x0                                                                                                                                                                        |
  +-------+------------------+-----+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | 7:0   | RFWD             | W   | Receive FIFO Write Data. These bits are only valid when FIFO access mode is enabled (FAR[0] is set to 1). When FIFOs are implemented and enabled, the data that is written to the RFWD  |
  +       +                  +     +                                                                                                                                                                                         + 
  |       |                  |     | is pushed into the receive FIFO. Each consecutive write pushes the new data to the next write location in the receive FIFO. When FIFOs are not implemented or not enabled, the data that|
  +       +                  +     +                                                                                                                                                                                         + 
  |       |                  |     | is written to the RFWD is pushed into the RBR.                                                                                                                                          |
  +       +                  +     +                                                                                                                                                                                         + 
  |       |                  |     | Reset Value: 0x0                                                                                                                                                                        |
  +-------+------------------+-----+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

2.20 USR
""""""""
- Name: UART Status Register
- Size: 32 bits
- Address Offset: 0x7C
- Read/write access: read-only

.. table::  USR Register Fields

  +------+---------+-----+----------------------------------------------------------------------------------------------------------+
  | Bits | Name    | R/W | Description                                                                                              |
  +======+=========+=====+==========================================================================================================+
  | 31:5 | Reserved|     |                                                                                                          |
  |      | and read|     |                                                                                                          |
  |      | as 0    |     |                                                                                                          |
  +------+---------+-----+----------------------------------------------------------------------------------------------------------+
  | 4    | RFF     | R   | Receive FIFO Full. This bit is only valid when FIFO_STAT = YES. This is used to indicate that the receive|
  +      +         +     +                                                                                                          +
  |      |         |     | FIFO is completely full.                                                                                 |
  |      |         |     |                                                                                                          |
  |      |         |     | 0 - Receive FIFO not full                                                                                |
  |      |         |     |                                                                                                          |
  |      |         |     | 1 - Receive FIFO Full                                                                                    |
  |      |         |     |                                                                                                          |
  |      |         |     | This bit is cleared when the RX FIFO is no longer full.                                                  |
  |      |         |     |                                                                                                          |
  |      |         |     | Reset Value: 0x0                                                                                         |
  +------+---------+-----+----------------------------------------------------------------------------------------------------------+
  | 3    | RFNE    | R   | Receive FIFO Not Empty. This bit is only valid when FIFO_STAT = YES. This is used to indicate that the   |
  +      +         +     +                                                                                                          +
  |      |         |     | receive FIFO contains one or more entries.                                                               |
  |      |         |     |                                                                                                          |
  |      |         |     | 0 - Receive FIFO is empty                                                                                |
  |      |         |     |                                                                                                          |
  |      |         |     | 1 - Receive FIFO is not empty                                                                            |
  |      |         |     |                                                                                                          |
  |      |         |     | This bit is cleared when the RX FIFO is empty.                                                           |
  |      |         |     |                                                                                                          |
  |      |         |     | Reset Value: 0x0                                                                                         |
  +------+---------+-----+----------------------------------------------------------------------------------------------------------+


.. table::

  +------+---------+-----+----------------------------------------------------------------------------------------------------------+
  | 2    | TFE     | R   | Transmit FIFO Empty. This bit is only valid when FIFO_STAT = YES. This is used to indicate that the      |
  +      +         +     +                                                                                                          +
  |      |         |     | transmit FIFO is completely empty.                                                                       |
  |      |         |     |                                                                                                          |
  |      |         |     | 0 - Transmit FIFO is not empty                                                                           |
  |      |         |     |                                                                                                          |
  |      |         |     | 1 - Transmit FIFO is empty                                                                               |
  |      |         |     |                                                                                                          |
  |      |         |     | This bit is cleared when the TX FIFO is no longer empty.                                                 |
  |      |         |     |                                                                                                          |
  |      |         |     | Reset Value: 0x1                                                                                         |
  +------+---------+-----+----------------------------------------------------------------------------------------------------------+
  | 1    | TFNF    | R   | Transmit FIFO Not Full. This bit is only valid when FIFO_STAT = YES.                                     |
  +      +         +     +                                                                                                          +
  |      |         |     | This is used to indicate that the transmit FIFO is not full.                                             |
  |      |         |     |                                                                                                          |
  |      |         |     | 0 - Transmit FIFO is full                                                                                |
  |      |         |     |                                                                                                          |
  |      |         |     | 1 - Transmit FIFO is not full                                                                            |
  |      |         |     |                                                                                                          |
  |      |         |     | This bit is cleared when the TX FIFO is full.                                                            |
  |      |         |     |                                                                                                          |
  |      |         |     | Reset Value: 0x1                                                                                         |
  +------+---------+-----+----------------------------------------------------------------------------------------------------------+


.. table::

  +------+---------+-----+----------------------------------------------------------------------------------------------------------+
  | 0    | BUSY    | R   | UART Busy. This bit is valid only when UART_16550_COMPATIBLE = NO and indicates that a serial transfer   |
  +      +         +     +                                                                                                          +
  |      |         |     | is in progress; when cleared, indicates that the UART is idle or inactive.                               |
  |      |         |     |                                                                                                          |
  |      |         |     | 0 - UART is idle or inactive                                                                             |
  |      |         |     |                                                                                                          |
  |      |         |     | 1 - UART is busy (actively transferring data)                                                            |
  |      |         |     |                                                                                                          |
  +      +         +     +                                                                                                          +
  |      |         |     | This bit will be set to 1 (busy) under any of the following conditions:                                  |
  +      +         +     +                                                                                                          +
  |      |         |     | 1 Transmission in progress on serial interface.                                                          |
  +      +         +     +                                                                                                          +
  |      |         |     | 2 Transmit data present in THR, when FIFO access mode is not being used (FAR = 0)                        |
  +      +         +     +                                                                                                          +
  |      |         |     | and the baud divisor is non-zero (\{DLH,DLL\} does not equal 0) when the divisor latch                   |
  +      +         +     +                                                                                                          +
  |      |         |     | access bit is 0 (LCR.DLAB = 0).                                                                          |
  +      +         +     +                                                                                                          +
  |      |         |     | 3 Reception in progress on the interface.                                                                |
  +      +         +     +                                                                                                          +
  |      |         |     | 4 Receive data present in RBR, when FIFO access mode is not being used (FAR = 0)                         |
  +------+---------+-----+----------------------------------------------------------------------------------------------------------+


.. table::

  +------+---------+-----+----------------------------------------------------------------------------------------------------------+
  |      |         |     | **NOTE**: It is possible for the UART Busy bit to be cleared even though a new character may have        |
  +      +         +     +                                                                                                          +
  |      |         |     | been sent from another device. That is, if the UART has no data in THR and RBR and there                 |
  +      +         +     +                                                                                                          +
  |      |         |     | is no transmission in progress and a start bit of a new character has just reached the UART.             |
  +      +         +     +                                                                                                          +
  |      |         |     | This is due to the fact that a valid start is not seen until the middle of the bit period and this       |
  +      +         +     +                                                                                                          +
  |      |         |     | duration is dependent on the baud divisor that has been programmed. If a second system clock has been    |
  +      +         +     +                                                                                                          +
  |      |         |     | implemented (CLOCK_MODE = Enabled), the assertion of this bit is also delayed by several cycles of the   |
  +      +         +     +                                                                                                          +
  |      |         |     | slower clock.                                                                                            |
  +      +         +     +                                                                                                          +
  |      |         |     | Reset Value: 0x0                                                                                         |
  +------+---------+-----+----------------------------------------------------------------------------------------------------------+

2.21 TFL
""""""""
- Name: Transmit FIFO Level
- Size: FIFO_ADDR_WIDTH + 1
- Address Offset: 0x80
- Read/write access: read-only

This register is valid only when the UART is configured to have additional FIFO status registers 
implemented (FIFO_STAT = YES). If status registers are not implemented, this register does not exist and 
reading from this register address returns 0.

.. table::  TFL Register Fields

  +----------------------+----------------+-----+---------------------------------------------------------------------+
  | Bits                 | Name           | R/W | Description                                                         |
  +======================+================+=====+=====================================================================+
  | 31:FIFO_ADDR_WIDTH+1 | Reserved and   |     |                                                                     |
  +                      +                +     +                                                                     +
  |                      | read as 0      |     |                                                                     |
  +----------------------+----------------+-----+---------------------------------------------------------------------+
  | FIFO_ADDR_WIDTH:0    | Transmit FIFO  | R   | Transmit FIFO Level. This indicates the number of data entries in   |
  +                      +                +     +                                                                     +
  |                      | Level          |     | the transmit FIFO.                                                  |
  +                      +                +     +                                                                     +
  |                      |                |     | Reset Value: 0x0                                                    |
  +----------------------+----------------+-----+---------------------------------------------------------------------+

2.22 RFL
""""""""
- Name: Receive FIFO Level
- Size: FIFO_ADDR_WIDTH + 1
- Address Offset: 0x84
- Read/write access: read-only

This register is valid only when the UART is configured to have additional FIFO status registers 
implemented (FIFO_STAT = YES). If status registers are not implemented, this register does not exist and 
reading from this register address returns 0.

.. table::  RFL Register Fields

  +----------------------+----------------+-----+---------------------------------------------------------------------+
  | Bits                 | Name           | R/W | Description                                                         |
  +======================+================+=====+=====================================================================+
  | 31:FIFO_ADDR_WIDTH+1 | Reserved and   |     |                                                                     |
  +                      +                +     +                                                                     +
  |                      | read as 0      |     |                                                                     |
  +----------------------+----------------+-----+---------------------------------------------------------------------+
  | FIFO_ADDR_WIDTH:0    | Receive FIFO   | R   | Receive FIFO Level. This indicates the number of data entries in    |
  +                      +                +     +                                                                     +
  |                      | Level          |     | the receive FIFO.                                                   |
  |                      |                |     |                                                                     |
  |                      |                |     | Reset Value: 0x0                                                    |
  +----------------------+----------------+-----+---------------------------------------------------------------------+

2.23 SRR
""""""""
- Name: Software Reset Register
- Size: 32 bits
- Address Offset: 0x88
- Read/write access: write-only

This register is valid only when the UART is configured to have additional shadow registers 
implemented (SHADOW = YES). If shadow registers are not implemented, this register does not exist and 
reading from this register address returns 0.

.. table::  SRR Register Fields

  +------+---------+-----+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | Bits | Name    | R/W | Description                                                                                                                                                                                                                                                                                                                    |
  +======+=========+=====+================================================================================================================================================================================================================================================================================================================================+
  | 31:3 | Reserved|     |                                                                                                                                                                                                                                                                                                                                |
  +      +         +     +                                                                                                                                                                                                                                                                                                                                + 
  |      | and read|     |                                                                                                                                                                                                                                                                                                                                |
  +      +         +     +                                                                                                                                                                                                                                                                                                                                + 
  |      | as 0    |     |                                                                                                                                                                                                                                                                                                                                |
  +------+---------+-----+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | 2    | XFR     | W   | XMIT FIFO Reset. This is a shadow register for the XMIT FIFO Reset bit (FCR[2]). This can be used to remove the burden on software having to store previously written FCR values (which are pretty static) just to reset the transmit FIFO. This resets the control portion of the transmit FIFO and treats the FIFO as empty. |
  +      +         +     +                                                                                                                                                                                                                                                                                                                                + 
  |      |         |     | This also de-asserts the DMA TX request and single signals when additional DMA handshaking signals are selected (DMA_EXTRA = YES). Note that this bit is 'self-clearing'. It is not necessary to clear this bit.                                                                                                               |
  +      +         +     +                                                                                                                                                                                                                                                                                                                                +               
  |      |         |     | Reset Value: 0x0                                                                                                                                                                                                                                                                                                               |
  +      +         +     +                                                                                                                                                                                                                                                                                                                                + 
  |      |         |     | Dependencies: Writes have no effect when FIFO_MODE = None.                                                                                                                                                                                                                                                                     |
  +------+---------+-----+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | 1    | RFR     | W   | RCVR FIFO Reset. This is a shadow register for the RCVR FIFO Reset bit (FCR[1]). This can be used to remove the burden on software having to store previously written FCR values (which are pretty static) just to reset the receive FIFO. This resets the control portion of the receive FIFO and treats the FIFO as empty.   |
  +      +         +     +                                                                                                                                                                                                                                                                                                                                + 
  |      |         |     | This also de-asserts the DMA RX request and single signals when additional DMA handshaking signals are selected (DMA_EXTRA = YES). Note that this bit is 'self-clearing'. It is not necessary to clear this bit.                                                                                                               |
  |      |         |     |                                                                                                                                                                                                                                                                                                                                |
  |      |         |     | Reset Value: 0x0                                                                                                                                                                                                                                                                                                               |
  |      |         |     |                                                                                                                                                                                                                                                                                                                                |
  |      |         |     | Dependencies: Writes have no effect when FIFO_MODE = None.                                                                                                                                                                                                                                                                     |
  +------+---------+-----+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | 0    | UR      | W   | UART Reset. This asynchronously resets the UART and synchronously removes the reset assertion.                                                                                                                                                                                                                                 |
  +      +         +     +                                                                                                                                                                                                                                                                                                                                + 
  |      |         |     | For a two clock implementation both pclk and sclk domains are reset.                                                                                                                                                                                                                                                           |
  |      |         |     |                                                                                                                                                                                                                                                                                                                                |
  |      |         |     | Reset Value: 0x0                                                                                                                                                                                                                                                                                                               |
  +------+---------+-----+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

2.24 SRTS
"""""""""
- Name: Shadow Request to Send
- Size: 32 bits
- Address Offset: 0x8C
- Read/write access: read/write

This register is valid only when the UART is configured to have additional shadow registers 
implemented (SHADOW = YES). If shadow registers are not implemented, this register does not exist and 
reading from this register address returns 0.

.. table::  SRTS Register Fields

  +------+------------------+-----+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | Bits | Name             | R/W | Description                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
  +======+==================+=====+==================================================================================================================================================================================================================================================================================================================================================+
  | 31:1 | Reserved and     |     |                                                                                                                                                                                                                                                                                                                                                  |   
  +      +                  +     +                                                                                                                                                                                                                                                                                                                                                  +                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
  |      | read as 0        |     |                                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
  +------+------------------+-----+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | 0    | Sha-             | R/W | Shadow Request to Send. This is a shadow register for the RTS bit (MCR[1]), this can be used to remove the burden of having to performing a read-modify-write on the MCR. This is used to directly control the Request to Send (rts_n) output. The Request To Send (rts_n) output is used to inform the modem or data set that the UART is ready |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
  +      +                  +     +                                                                                                                                                                                                                                                                                                                                                  +  
  |      | dow Request      |     | to exchange data. When Auto RTS Flow Control is off (MCR[5] = 0), set rts_n low by setting MCR[1] (RTS) high.                                                                                                                                                                                                                                    |  
  +      +                  +     +                                                                                                                                                                                                                                                                                                                                                  +                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
  |      | to Send          |     | In Auto Flow Control, AFCE_MODE = Enabled and active (MCR[5] = 1) and FIFOs enable (FCR[0] = 1), the rts_n output is controlled in the same way, but is also gated with the receiver FIFO threshold trigger (rts_n is inactive high when above the threshold) only when RTC Flow Trigger is disabled; otherwise it is gated by the receiver FIFO |  
  +      +                  +     +                                                                                                                                                                                                                                                                                                                                                  +                                                                                                                                                                                
  |      |                  |     | almost-full trigger, where “almost full” refers to two available slots in the FIFO (rts_n is inactive high when above the threshold). Note that in Loopback mode (MCR[4] = 1), the rts_n output is held inactive-high while the value of this location is internally looped back to an input.                                                    |
  +      +                  +     +                                                                                                                                                                                                                                                                                                                                                  +                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
  |      |                  |     | Reset Value: 0x0                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
  +------+------------------+-----+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

2.25 SBCR
"""""""""
- Name: Shadow Break Control Register
- Size: 32 bits
- Address Offset: 0x90
- Read/write access: read/write

This register is valid only when the UART is configured to have additional shadow registers 
implemented (SHADOW = YES). If shadow registers are not implemented, this register does not exist and 
reading from this register address returns 0.

.. table::  SBCR Register Fields

  +------+-------------------------+-----+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | Bits | Name                    | R/W | Description                                                                                                                                                                                                                                                                                                                                                |
  +======+=========================+=====+============================================================================================================================================================================================================================================================================================================================================================+
  | 31:1 | Reserved and            |     |                                                                                                                                                                                                                                                                                                                                                            |
  +      +                         +     +                                                                                                                                                                                                                                                                                                                                                            +  
  |      | read as 0               |     |                                                                                                                                                                                                                                                                                                                                                            |      
  +------+-------------------------+-----+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | 0    | Shadow Break Control    | R/W | Shadow Break Control Bit. This is a shadow register for the Break bit (LCR[6]), this can be used to remove the burden of having to performing a read modify write on the LCR. This is used to cause a break condition to be transmitted to the receiving device. If set to 1, the serial output is forced to the spacing (logic 0) state.  When not in     |
  |      | Register                |     | Loopback Mode,  as determined by MCR[4], the sout line is forced low until the Break bit is cleared. If SIR_MODE = Enabled and active (MCR[6] = 1) the sir_out_n line is continuously pulsed.  When in Loopback Mode, the break condition is internally looped back to the receiver.                                                                       |
  |      |                         |     |                                                                                                                                                                                                                                                                                                                                                            |
  |      |                         |     | Reset Value: 0x0.                                                                                                                                                                                                                                                                                                                                          |
  +------+-------------------------+-----+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

2.26 SDMAM
""""""""""
- Name: Shadow DMA Mode
- Size: 32 bits
- Address Offset: 0x94
- Read/write access: read/write

This register is valid only when the UART is configured to have additional FIFO registers 
implemented (FIFO_MODE != None) and additional shadow registers implemented (SHADOW = YES). If
these registers are not implemented, this register does not exist and reading from this register address 
returns 0. 

.. table::  SDMAM Register Fields

  +------+----------------+-----+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | Bits | Name           | R/W | Description                                                                                                                                                                          |
  +======+================+=====+======================================================================================================================================================================================+
  | 31:1 | Reserved and   |     |                                                                                                                                                                                      |
  +      +                +     +                                                                                                                                                                                      +                
  |      | read as 0      |     |                                                                                                                                                                                      |
  +------+----------------+-----+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | 0    | Shadow DMA     | R/W | Shadow DMA Mode. This is a shadow register for the DMA mode bit (FCR[3]). This can be used to remove the burden of having to store the previously written value to the FCR in memory |
  +      +                +     +                                                                                                                                                                                      + 
  |      | Mode           |     | and having to mask this value so that only the DMA Mode bit gets updated. This determines the DMA signalling mode for dma_tx_req_n and dma_rx_req_n output signals when additional   |
  +      +                +     +                                                                                                                                                                                      + 
  |      |                |     | DMA handshaking signals are not selected (DMA_EXTRA = NO).                                                                                                                           |
  |      |                |     |                                                                                                                                                                                      |
  |      |                |     | 0 - mode 0                                                                                                                                                                           |
  |      |                |     |                                                                                                                                                                                      |
  |      |                |     | 1 - mode 1                                                                                                                                                                           |
  |      |                |     |                                                                                                                                                                                      |
  |      |                |     | Reset Value: 0x0                                                                                                                                                                     |
  +------+----------------+-----+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

2.27 SFE
""""""""
- Name: Shadow FIFO Enable
- Size: 32 bits
- Address Offset: 0x98
- Read/write access: read/write

This register is valid only when the UART is configured to have additional FIFO registers 
implemented (FIFO_MODE != None) and additional shadow registers implemented (SHADOW = YES). If 
these registers are not implemented, this register does not exist and reading from this register address 
returns 0.

.. table::  SFE Register Fields

  +------+----------------+-----+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | Bits | Name           | R/W | Description                                                                                                                                                                                      |                                                                                                                                          
  +======+================+=====+==================================================================================================================================================================================================+
  | 31:1 | Reserved and   |     |                                                                                                                                                                                                  |                                                                                                                                          
  +      +                +     +                                                                                                                                                                                                  +                                                                                                                                          
  |      | read as 0      |     |                                                                                                                                                                                                  |
  +------+----------------+-----+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+              
  | 0    | Shadow         | R/W | Shadow FIFO Enable. This is a shadow register for the FIFO enable bit (FCR[0]). This can be used to remove the burden of having to store the previously written value to the FCR in memory and   |
  +      +                +     +                                                                                                                                                                                                  +
  |      | FIFO Enable    |     | having to mask this value so that only the FIFO enable bit gets updated.This enables/disables the transmit (XMIT) and receive (RCVR) FIFOs.                                                      |
  +      +                +     +                                                                                                                                                                                                  +                                                                                                                                          
  |      |                |     | If this bit is set to 0 (disabled) after being enabled then both the XMIT and RCVR controller portion of FIFOs are reset. If this bit is set to 0 (disabled) after being enabled then both the   |    
  |      |                |     | XMIT and RCVR controller portion of FIFOs are reset.                                                                                                                                             |
  +      +                +     +                                                                                                                                                                                                  +                                                                                                                                         
  |      |                |     | Reset Value: 0x0                                                                                                                                                                                 |                                                                                                                                          
  +------+----------------+-----+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

2.28 SRT
""""""""
- Name: Shadow RCVR Trigger
- Size: 32 bits
- Address Offset: 0x9C
- Read/write access: read/write

This register is valid only when the UART is configured to have additional FIFO registers 
implemented (FIFO_MODE != None) and additional shadow registers implemented (SHADOW = YES). If
these registers are not implemented, this register does not exist and reading from this register address 
returns 0.

.. table::  SRT Register Fields

  +------+----------------+-----+-----------------------------------------------------------------------------------------------------------------------------+
  | Bits | Name           | R/W | Description                                                                                                                 |                                                                                                                                                                                                                                                                                     
  +======+================+=====+=============================================================================================================================+
  | 31:2 | Reserved and   |     |                                                                                                                             |                                                                                                                                                                                                                                                                                     
  +      +                +     +                                                                                                                             |                                                                                                                                                                                                                                                                                     
  |      | read as 0      |     |                                                                                                                             |                                                                                                                                                                                                                                                                                     
  +------+----------------+-----+-----------------------------------------------------------------------------------------------------------------------------+
  | 1:0  | Shadow RCVR    | R/W | Shadow RCVR Trigger. This is a shadow register for the RCVR trigger bits (FCR[7:6]). This can be used to remove the burden  |
  +      +                +     +                                                                                                                             +
  |      |                |     | of having to store the previously written value to the FCR in memory and having to mask this value so that only the RCVR    |  
  +      +                +     +                                                                                                                             +                                                                                                     
  |      | Trigger        |     | trigger bit gets updated.                                                                                                   |
  +      +                +     +                                                                                                                             + 
  |      |                |     | This is used to select the trigger level in the receiver FIFO at which the Received Data Available Interrupt is generated.  |
  +      +                +     +                                                                                                                             +
  |      |                |     | It also determines when the dma_rx_req_n signal is asserted when DMA Mode (FCR[3]) = 1. The following trigger levels are    |
  +      +                +     +                                                                                                                             +   
  |      |                |     | supported:                                                                                                                  |
  +      +                +     +                                                                                                                             +                     
  |      |                |     | 00 - 1 character in the FIFO                                                                                                |                                                                                                                                                                                                                                                                                     
  |      |                |     |                                                                                                                             |                                                                                                                                                                                                                                                                                     
  |      |                |     | 01 - FIFO ¼ full                                                                                                            |                                                                                                                                                                                                                                                                                     
  |      |                |     |                                                                                                                             |                                                                                                                                                                                                                                                                                     
  |      |                |     | 10 - FIFO ½ full                                                                                                            |                                                                                                                                                                                                                                                                                     
  |      |                |     |                                                                                                                             |                                                                                                                                                                                                                                                                                     
  |      |                |     | 11 - FIFO 2 less than full                                                                                                  |                                                                                                                                                                                                                                                                                     
  |      |                |     |                                                                                                                             |                                                                                                                                                                                                                                                                                     
  |      |                |     | Reset Value: 0x0                                                                                                            |                                                                                                                                                                                                                                                                                     
  +------+----------------+-----+-----------------------------------------------------------------------------------------------------------------------------+

2.29 STET
"""""""""
- Name: Shadow TX Empty Trigger
- Size: 32 bits
- Address Offset: 0xA0
- Read/write access: read/write

This register is valid only when the UART is configured to have FIFOs implemented 
(FIFO_MODE != NONE) and THRE interrupt support implemented (THRE_MODE_USER = Enabled) and 
additional shadow registers implemented (SHADOW = YES). If FIFOs are not implemented or THRE
interrupt support is not implemented or shadow registers are not implemented, this register does not exist 
and reading from this register address returns 0.

.. table::  STET Register Fields

  +------+---------------------+-----+---------------------------------------------------------------------------------------------------------------------------------+
  | Bits | Name                | R/W | Description                                                                                                                     |                                                                                                                                                                                                                                                                               
  +======+=====================+=====+=================================================================================================================================+
  | 31:2 | Reserved and        |     |                                                                                                                                 | 
  +      +                     +     +                                                                                                                                 +                                                                                                                                                                                                                                                                              
  |      | read as 0           |     |                                                                                                                                 |                                                                                                                                                                                                                                                                               
  +------+---------------------+-----+---------------------------------------------------------------------------------------------------------------------------------+
  | 1:0  | Shadow TX           | R/W | Shadow TX Empty Trigger. This is a shadow register for the TX empty trigger bits (FCR[5:4]). This can be used to remove the     |
  +      +                     +     +                                                                                                                                 +
  |      |                     |     | burden of having to store the previously written value to the FCR in memory and having to mask this value so that only the TX   |
  +      +                     +     +                                                                                                                                 +
  |      |                     |     | empty trigger bit gets updated.                                                                                                 |
  +      +                     +     +                                                                                                                                 +
  |      |                     |     | This is used to select the empty threshold level at which the THRE Interrupts are generated when the mode is active.            |
  |      |                     |     |                                                                                                                                 |
  |      | Empty Trigger       |     | The following trigger levels are supported:                                                                                     |                                                                                                                                                                                                                                                                               
  |      |                     |     |                                                                                                                                 |                                                                                                                                                                                                                                                                               
  |      |                     |     | 00 - FIFO empty                                                                                                                 |                                                                                                                                                                                                                                                                               
  |      |                     |     |                                                                                                                                 |                                                                                                                                                                                                                                                                               
  |      |                     |     | 01 - 2 characters in the FIFO                                                                                                   |                                                                                                                                                                                                                                                                               
  |      |                     |     |                                                                                                                                 |                                                                                                                                                                                                                                                                               
  |      |                     |     | 10 - FIFO ¼ full                                                                                                                |                                                                                                                                                                                                                                                                               
  |      |                     |     |                                                                                                                                 |                                                                                                                                                                                                                                                                               
  |      |                     |     | 11 - FIFO ½ full                                                                                                                |                                                                                                                                                                                                                                                                               
  |      |                     |     |                                                                                                                                 |                                                                                                                                                                                                                                                                               
  |      |                     |     | Reset Value: 0x0                                                                                                                |                                                                                                                                                                                                                                                                               
  |      |                     |     |                                                                                                                                 |                                                                                                                                                                                                                                                                               
  |      |                     |     | Dependencies: Writes have no effect when THRE_MODE_USER = Disabled                                                              |                                                                                                                                                                                                                                                                               
  +------+---------------------+-----+---------------------------------------------------------------------------------------------------------------------------------+

2.30 HTX
""""""""
- Name: Halt TX
- Size: 32 bits
- Address Offset: 0xA4
- Read/write access: read/write

.. table::  HTX Register Fields

  +------+------------------------+-----+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | Bits | Name                   | R/W | Description                                                                                                                                                                    |
  +======+========================+=====+================================================================================================================================================================================+
  | 31:1 | Reserved and read as 0 |     |                                                                                                                                                                                |
  +------+------------------------+-----+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | 0    | Halt TX                | R/W | This register is used to halt transmissions for testing, so that the transmit FIFO can be filled by the master when FIFOs are implemented and enabled.                         |
  |      |                        |     |                                                                                                                                                                                |
  |      |                        |     | 0 - Halt TX disabled                                                                                                                                                           |
  |      |                        |     |                                                                                                                                                                                |
  |      |                        |     | 1 - Halt TX enabled                                                                                                                                                            |
  |      |                        |     |                                                                                                                                                                                |
  |      |                        |     | Note, if FIFOs are implemented and not enabled, the setting of the halt TX register has no effect on operation.                                                                |
  |      |                        |     |                                                                                                                                                                                |
  |      |                        |     | Reset Value: 0x0                                                                                                                                                               |
  |      |                        |     |                                                                                                                                                                                |
  |      |                        |     | Dependencies: Writes have no effect when FIFO_MODE = None.                                                                                                                     |
  +------+------------------------+-----+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

2.31 DMASA
""""""""""
- Name: DMA Software Acknowledge
- Size: 32 bits
- Address Offset: 0xA8
- Read/write access: write

.. table::  DMASA Register Fields

  +------+------------------------+-----+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | Bits | Name                   | R/W | Description                                                                                                                                                                                                                                                                                                                                                                                               |
  +======+========================+=====+===========================================================================================================================================================================================================================================================================================================================================================================================================+
  | 31:1 | Reserved and read as 0 |     |                                                                                                                                                                                                                                                                                                                                                                                                           |
  +------+------------------------+-----+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | 0    | DMA Software           | W   | This register is used to perform a DMA software acknowledge if a transfer needs to be terminated due to an error condition. For example, if the DMA disables the channel, then the UART should clear its request. This causes the TX request, TX single, RX request and RX single signals to de-assert. Note that this bit is 'self-clearing'. It is not necessary to clear this bit.                     |
  |      | Acknowledge            |     |                                                                                                                                                                                                                                                                                                                                                                                                           |
  |      |                        |     | Reset Value: 0x0                                                                                                                                                                                                                                                                                                                                                                                          |
  |      |                        |     |                                                                                                                                                                                                                                                                                                                                                                                                           |
  |      |                        |     | Dependencies: Writes have no effect when DMA_EXTRA = No.                                                                                                                                                                                                                                                                                                                                                  |
  +------+------------------------+-----+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

2.32 TCR
""""""""
- Name: Transceiver Control Register (TCR)
- Size: 32 bits
- Address Offset: 0xAC
- Read/write access: read/write

This register is used to enable or disable RS485 mode and also control the polarity values for Driven enable 
(de) and Receiver Enable (re) signals. 

This register is only valid when the UART is configured to have RS485 interface implemented 
(UART_RS485_INTERFACE_EN = ENABLED). If RS485 interface is not implemented, this register does not 
exist and reading from this register address returns zero.

.. table::  TCR Register Fields

  +------+------------------------+-----+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | Bits | Name                   | R/W | Description                                                                                                                                                                                            |                                                                                                                                                                                                   
  +======+========================+=====+========================================================================================================================================================================================================+
  | 31:5 | Reserved and           |     |                                                                                                                                                                                                        |                                                                                                                                                                                                   
  |      |                        |     |                                                                                                                                                                                                        |
  |      | read as 0              |     |                                                                                                                                                                                                        |
  +------+------------------------+-----+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | 4:3  | XFE                    | R/W | Transfer Mode                                                                                                                                                                                          |                                                                                                                                                                                                   
  +      +                        +     +                                                                                                                                                                                                        +                                                                                                                                                                                                  
  |      | R_MODE                 |     | 0 :                                                                                                                                                                                                    |                                                                                                                                                                                                   
  +      +                        +     +                                                                                                                                                                                                        +                                                                                                                                                                                                   
  |      |                        |     | In this mode, transmit and receive can happen simultaneously. You can enable DE_EN and RE_EN at any point of time. Turn around timing as programmed in the TAT register is not applicable in this mode.|                                                                                                                                                                                                   
  +      +                        +     +                                                                                                                                                                                                        +                                                                                                                                                                                                   
  |      |                        |     | 1 :                                                                                                                                                                                                    |                                                                                                                                                                                                   
  +      +                        +     +                                                                                                                                                                                                        +                                                                                                                                                                                                   
  |      |                        |     | In this mode, DE and RE are mutually exclusive. The hardware considers the turnaround timings that are programmed in the TAT register while switching from RE to DE or from DE to RE. Ensure that      |
  |      |                        |     |                                                                                                                                                                                                        |
  |      |                        |     | either DE or RE is expected to be enabled while programming.For transmission, hardware waits if it is in the midst of receiving any transfer, before it starts transmitting.                           | 
  +      +                        +     +                                                                                                                                                                                                        +                                                                                            
  |      |                        |     | 2 :                                                                                                                                                                                                    |                                                                                                                                                                                                   
  +      +                        +     +                                                                                                                                                                                                        +                                                                                                                                                                                                   
  |      |                        |     | In this mode, DE and RE are mutually exclusive. Once DE_EN or RE_EN is programed, 're' is enabled by default and UART controller will be ready to receive. If the user programs the TX FIFO with data, |
  |      |                        |     |                                                                                                                                                                                                        |
  |      |                        |     | then UART, after ensuring no receive is in progress, disables the 're' and enables the 'de' signal.Once the TX FIFO becomes empty, the 're' signal gets enabled and the 'de' signal will be            |
  +      +                        +     +                                                                                                                                                                                                        +                                                                                                                                         
  |      |                        |     | disabled. In this mode of operation, the hardware considers the turnaround timings that are programmed in the TAT register while switching from RE to DE or from DE to RE. In this mode, 'de' and 're' |
  +      +                        +     +                                                                                                                                                                                                        +   
  |      |                        |     | signals are strictly complementary to each other.                                                                                                                                                      |
  +      +                        +     +                                                                                                                                                                                                        +                                                                                                                                                                                                
  |      |                        |     | Reset Value: 0x0                                                                                                                                                                                       |                                                                                                                                                                                                   
  +------+------------------------+-----+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. table::

  +------+------------------------+-----+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | 2    | DE_POL                 | R/W | Driver Enable Polarity                                                                                                                                                                                 |                                                                                                                                                                                                   
  +      +                        +     +                                                                                                                                                                                                        +                                                                                                                                                                                                   
  |      |                        |     | 1 : DE signal is active high                                                                                                                                                                           |                                                                                                                                                                                                   
  +      +                        +     +                                                                                                                                                                                                        +                                                                                                                                                                                                   
  |      |                        |     | 0 : DE signal is active low                                                                                                                                                                            |                                                                                                                                                                                                   
  +      +                        +     +                                                                                                                                                                                                        +                                                                                                                                                                                                   
  |      |                        |     | Reset Value: UART_DE_POL                                                                                                                                                                               |                                                                                                                                                                                                   
  +------+------------------------+-----+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | 1    | RE_POL                 | R/W | Receiver Enable Polarity                                                                                                                                                                               |                                                                                                                                                                                                  
  +      +                        +     +                                                                                                                                                                                                        +                                                                                                                                                                                                  
  |      |                        |     | 1 : RE signal is active high                                                                                                                                                                           |                                                                                                                                                                                                  
  +      +                        +     +                                                                                                                                                                                                        +                                                                                                                                                                                                 
  |      |                        |     | 0 : RE signal is active low                                                                                                                                                                            |                                                                                                                                                                                                  
  +      +                        +     +                                                                                                                                                                                                        +                                                                                                                                                                                                  
  |      |                        |     | Reset Value: UART_RE_POL                                                                                                                                                                               |                                                                                                                                                                                                  
  +------+------------------------+-----+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | 0    | RS                     | R/W | RS485 Transfer Enable                                                                                                                                                                                  |                                                                                                                                                                                                  
  +      + 485_EN                 +     +                                                                                                                                                                                                        +                                                                                                                                                                                                  
  |      |                        |     | 0 :                                                                                                                                                                                                    |                                                                                                                                                                                                  
  +      +                        +     +                                                                                                                                                                                                        +                                                                                                                                                                                                  
  |      |                        |     | In this mode, the transfers are still in the RS232 mode. All other fields in this register are reserved and registers DE_EN, RE_EN, DET and TAT are reserved.                                          |                                                                                                                                                                                                  
  +      +                        +     +                                                                                                                                                                                                        +                                                                                                                                                                                                  
  |      |                        |     | 1 :                                                                                                                                                                                                    |                                                                                                                                                                                                  
  +      +                        +     +                                                                                                                                                                                                        +                                                                                                                                                                                                  
  |      |                        |     | In this mode, the transfers will happen in RS485 mode. All other fields of this register are applicable.                                                                                               |                                                                                                                                                                                                  
  +      +                        +     +                                                                                                                                                                                                        +                                                                                                                                                                                                  
  |      |                        |     | Reset Value: 0x0                                                                                                                                                                                       |                                                                                                                                                                                                  
  +------+------------------------+-----+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

2.33 DE_EN
""""""""""
- Name: Driver Output Enable Register (DE_EN)
- Size: 32 bits
- Address Offset: 0xB0
- Read/write access: read/write

The Driver Output Enable Register (DE_EN) is used to control the assertion and de-assertion of the DE 
signal.

This register is only valid when the UART is configured to have RS485 interface implemented 
(UART_RS485_INTERFACE_EN = ENABLED). If RS485 interface is not implemented, this register does not 
exist and reading from this register address will return zero.

.. table::  DE_EN Register Fields

  +------+----------------+-----+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | Bits | Name           | R/W | Description                                                                                                                                                                                                                                                                                                                                |
  +======+================+=====+============================================================================================================================================================================================================================================================================================================================================+
  | 31:1 | Reserved and   |     |                                                                                                                                                                                                                                                                                                                                            |
  |      | read as 0      |     |                                                                                                                                                                                                                                                                                                                                            |
  +------+----------------+-----+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | 0    |  DE Enable     | R/W | DE Enable control                                                                                                                                                                                                                                                                                                                          |
  +      +                +     +                                                                                                                                                                                                                                                                                                                                            +
  |      |                |     | The 'DE Enable' register bit is used to control assertion and de-assertion of 'de' signal.                                                                                                                                                                                                                                                 |
  +      +                +     +                                                                                                                                                                                                                                                                                                                                            +
  |      |                |     | 0 : De-assert 'de' signal                                                                                                                                                                                                                                                                                                                  |
  +      +                +     +                                                                                                                                                                                                                                                                                                                                            +
  |      |                |     | 1 : Assert 'de' signal                                                                                                                                                                                                                                                                                                                     |
  +      +                +     +                                                                                                                                                                                                                                                                                                                                            +
  |      |                |     | Reset Value: 0x0                                                                                                                                                                                                                                                                                                                           |
  +------+----------------+-----+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

2.34 RE_EN
""""""""""
- Name: Receiver Output Enable Register (RE_EN)
- Size: 32 bits
- Address Offset: 0xB4
- Read/write access: read/write

The Receiver Output Enable Register (RE_EN) is used to control the assertion and de-assertion of the RE 
signal.

This register is only valid when the UART is configured to have RS485 interface implemented 
(UART_RS485_INTERFACE_EN = ENABLED). If the RS485 interface is not implemented, this register does 
not exist and reading from this register address will return zero.

.. table::  RE_EN Register Fields

  +------+----------------+-----+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | Bits | Name           | R/W | Description                                                                                                                                                                                                                                                                                                                                |
  +======+================+=====+============================================================================================================================================================================================================================================================================================================================================+
  | 31:1 | Reserved and   |     |                                                                                                                                                                                                                                                                                                                                            |
  |      | read as 0      |     |                                                                                                                                                                                                                                                                                                                                            |
  +------+----------------+-----+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | 0    |  RE Enable     | R/W | RE Enable control                                                                                                                                                                                                                                                                                                                          |
  +      +                +     +                                                                                                                                                                                                                                                                                                                                            +
  |      |                |     | The 'RE Enable' register bit is used to control assertion and de-assertion of 're' signal.                                                                                                                                                                                                                                                 |
  +      +                +     +                                                                                                                                                                                                                                                                                                                                            +
  |      |                |     | 0 : De-assert 're' signal                                                                                                                                                                                                                                                                                                                  |
  +      +                +     +                                                                                                                                                                                                                                                                                                                                            +
  |      |                |     | 1 : Assert 're' signal                                                                                                                                                                                                                                                                                                                     |
  +      +                +     +                                                                                                                                                                                                                                                                                                                                            +
  |      |                |     | Reset Value: 0x0                                                                                                                                                                                                                                                                                                                           |
  +------+----------------+-----+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

2.35 DET
""""""""
- Name: Driver Output Enable Timing Register (DET)
- Size: 32 bits
- Address Offset: 0xB8
- Read/write access: read/write

The Driver Output Enable Timing Register (DET) is used to control the DE assertion and de-assertion 
timings of 'de' signal.

This register is only valid when the UART is configured to have RS485 interface implemented 
(UART_RS485_INTERFACE = ENABLED). If RS485 interface is not implemented, this register does not 
exist and reading from this register address will return zero.

.. table::  DET Register Fields

  +-------+----------------+-----+------------------------------------------------------------------------------------------------------------------------------------+
  | Bits  | Name           | R/W | Description                                                                                                                        |                                                                                                                                                                                                        
  +=======+================+=====+====================================================================================================================================+
  |31:24  | Reserved and   |     |                                                                                                                                    |                                                                                                                                                                                                        
  +       +                +     +                                                                                                                                    +                                                                                                                                                                                                     
  |       | read as 0      |     |                                                                                                                                    |                                                                                                                                                                                                        
  +-------+----------------+-----+------------------------------------------------------------------------------------------------------------------------------------+
  |23:16  | DE de-assertion| R/W | Driver enable de-assertion time.                                                                                                   |                                                                                                                                                                                                        
  +       +                +     +                                                                                                                                    +                                                                                                                                                                                                       
  |       | time           |     | This field controls the amount of time (in terms of number of serial clock periods) between the end of stop bit on the serial      |
  +       +                +     +                                                                                                                                    + 
  |       |                |     | output (sout) to the falling edge of Driver output enable signal.                                                                  |                                                                                                                                                                                                             
  +       +                +     +                                                                                                                                    + 
  |       |                |     | Reset Value: 0x0                                                                                                                   |                                                                                                                                                                                                        
  +       +                +     +                                                                                                                                    +                                                                                                                                                                                                       
  +-------+----------------+-----+------------------------------------------------------------------------------------------------------------------------------------+
  | 15:8  | Reserved and   |     |                                                                                                                                    |                                                                                                                                                                                                        
  +       +                +     +                                                                                                                                    +                                                                                                                                                                                                       
  |       | read as 0      |     |                                                                                                                                    |                                                                                                                                                                                                        
  +-------+----------------+-----+------------------------------------------------------------------------------------------------------------------------------------+
  | 7:0   | DE assertion   | R/W | Driver enable assertion time.                                                                                                      |                                                                                                                                                                                                        
  +       +                +     +                                                                                                                                    +                                                                                                                                                                                                       
  |       | time           |     |                                                                                                                                    |                                                                                                                                                                                                        
  |       |                |     | This field controls the amount of time (in terms of number of serial clock periods) between the assertion of rising edge of Driver |
  +       +                +     +                                                                                                                                    +
  |       |                |     | output enable signal to serial transmit enable. Any data in transmit buffer, will start on serial output                           |
  +       +                +     +                                                                                                                                    + 
  |       |                |     | (sout) after the transmit enable.                                                                                                  |  
  +       +                +     +                                                                                                                                    +                                                                                                                                                                                                       
  |       |                |     | Reset Value: 0x0                                                                                                                   |                                                                                                                                                                                                        
  +-------+----------------+-----+------------------------------------------------------------------------------------------------------------------------------------+

2.36 TAT
""""""""
- Name: TurnAround Timing Register (TAT)
- Size: 32 bits
- Address Offset: 0xBC
- Read/write access: read/write

The TurnAround Timing Register (TAT) is used to hold the turnaround time between switching of 're' and 
'de' signals.

This register is only valid when the UART is configured to have the RS485 interface implemented 
(UART_RS485_INTERFACE_EN = ENABLED). If RS485 interface is not implemented, this register does not 
exist and reading from this register address will return zero.

.. table::  TAT Register Fields

  +-------+----------------+-----+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | Bits  | Name           | R/W | Description                                                                                                                                                                                                                                                                                                                                |
  +=======+================+=====+============================================================================================================================================================================================================================================================================================================================================+
  | 31:16 | RE to DE       | R/W | Receiver Enable to Driver Enable TurnAround time.                                                                                                                                                                                                                                                                                          |
  +       +                +     +                                                                                                                                                                                                                                                                                                                                            +
  |       |                |     | Turnaround time (in terms of serial clock) for RE de-assertion to DE assertion.                                                                                                                                                                                                                                                            |
  +       +                +     +                                                                                                                                                                                                                                                                                                                                            +
  |       |                |     | **NOTE**:                                                                                                                                                                                                                                                                                                                                  |
  +       +                +     +                                                                                                                                                                                                                                                                                                                                            +
  |       |                |     | If the DE assertion time in the DET register is 0, then the actual value is the programmed value + 3.                                                                                                                                                                                                                                      |
  +       +                +     +                                                                                                                                                                                                                                                                                                                                            +
  |       |                |     | If the DE assertion time in the DET register is 1, then the actual value is the programmed value + 2.                                                                                                                                                                                                                                      |
  +       +                +     +                                                                                                                                                                                                                                                                                                                                            +
  |       |                |     | If the DE assertion time in the DET register is greater than 1, then the actual value is the programmed value + 1.                                                                                                                                                                                                                         |
  +       +                +     +                                                                                                                                                                                                                                                                                                                                            +
  |       |                |     | Reset Value: 0x0                                                                                                                                                                                                                                                                                                                           |
  +-------+----------------+-----+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | 15:0  |  DE to RE      | R/W | Driver Enable to Receiver Enable TurnAround time.                                                                                                                                                                                                                                                                                          |
  +       +                +     +                                                                                                                                                                                                                                                                                                                                            +
  |       |                |     | Turnaround time (in terms of serial clock) for DE de-assertion to RE assertion.                                                                                                                                                                                                                                                            |
  +       +                +     +                                                                                                                                                                                                                                                                                                                                            +
  |       |                |     | **NOTE**:                                                                                                                                                                                                                                                                                                                                  |
  +       +                +     +                                                                                                                                                                                                                                                                                                                                            +
  |       |                |     | The actual time is the programmed value + 1.                                                                                                                                                                                                                                                                                               |
  +       +                +     +                                                                                                                                                                                                                                                                                                                                            +
  |       |                |     | Reset Value: 0x0                                                                                                                                                                                                                                                                                                                           |
  +-------+----------------+-----+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

2.37 DLF
""""""""
- Name: Divisor Latch Fraction Register (DLF)
- Size: 32 bits
- Address Offset: 0xC0
- Read/write access: read/write

This register is only valid when the UART is configured to have Fractional Baud rate Divisor 
implemented (FRACTIONAL_BAUD_DIVISOR_EN = ENABLED). If Fractional Baud rate divisor is not 
implemented, this register does not exist and reading from this register address will return zero.

.. table::  DLF Register Fields

  +-------------+---------------+-----+---------------------------------------------------------------+
  | Bits        | Name          | R/W | Description                                                   |
  +=============+===============+=====+===============================================================+
  | 31:DLF_SIZE | Reserved and  |     |                                                               |
  +             +               +     +                                                               +
  |             | read as zero  |     |                                                               |
  +-------------+---------------+-----+---------------------------------------------------------------+
  | DLF_SIZE-1:0| DLF           | R/W | Fractional part of divisor.                                   |
  +             +               +     +                                                               +
  |             |               |     | The fractional value is added to                              |
  +             +               +     +                                                               +
  |             |               |     | integer value set by DLH, DLL. Fractional value is determined |
  +             +               +     +                                                               +
  |             |               |     | by (Divisor Fraction value)/(2^DLF_SIZE). Table -3 describes  |
  +             +               +     +                                                               +
  |             |               |     | the DLF Values to be programmed for DLF_SIZE=4.               |
  +             +               +     +                                                               +
  |             |               |     | Reset Value: 0x0                                              |
  +-------------+---------------+-----+---------------------------------------------------------------+

Table -3 summarizes the  Divisor Latch Fractional Values:

.. table:: Divisor Latch Fractional Values

  +-----------+----------+-----------------+
  | DLF Value | Fraction | Fractional Value|
  +===========+==========+=================+
  | 0000      | 0/16     | 0.0000          |
  +-----------+----------+-----------------+
  | 0001      | 1/16     | 0.0625          |
  +-----------+----------+-----------------+
  | 0010      | 2/16     | 0.1250          |
  +-----------+----------+-----------------+
  | 0011      | 3/16     | 0.1875          |
  +-----------+----------+-----------------+
  | 0100      | 4/16     | 0.2500          |
  +-----------+----------+-----------------+
  | 0101      | 5/16     | 0.3125          |
  +-----------+----------+-----------------+
  | 0110      | 6/16     | 0.3750          |
  +-----------+----------+-----------------+
  | 0111      | 7/16     | 0.4375          |
  +-----------+----------+-----------------+
  | 1000      | 8/16     | 0.5000          |
  +-----------+----------+-----------------+
  | 1001      | 9/16     | 0.5625          |
  +-----------+----------+-----------------+
  | 1010      | 10/16    | 0.6250          |
  +-----------+----------+-----------------+
  | 1011      | 11/16    | 0.6875          |
  +-----------+----------+-----------------+
  | 1100      | 12/16    | 0.7500          |
  +-----------+----------+-----------------+
  | 1101      | 13/16    | 0.8125          |
  +-----------+----------+-----------------+
  | 1110      | 14/16    | 0.8750          |
  +-----------+----------+-----------------+
  | 1111      | 15/16    | 0.9375          |
  +-----------+----------+-----------------+


2.38 RAR
""""""""
- Name: Receive Address Register (RAR)
- Size: 32 bits
- Address Offset: 0xC4
- Read/write access: read/write

.. table::  RAR Register Fields

  +------+----------------+-----+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | Bits | Name           | R/W | Description                                                                                                                                                                                                                                                                                                                                |
  +======+================+=====+============================================================================================================================================================================================================================================================================================================================================+
  | 31:8 | Reserved and   |     |                                                                                                                                                                                                                                                                                                                                            |
  +      +                +     +                                                                                                                                                                                                                                                                                                                                            +
  |      | read as 0      |     |                                                                                                                                                                                                                                                                                                                                            |
  +------+----------------+-----+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | 7:0  |  RAR           | R/W | This is an address matching register during receive mode. If the 9-th bit is set in the incoming character then the remaining 8-bits will be checked against this register value. If the match happens then sub-sequent characters with 9-th bit set to 0 will be treated as data byte until the next address byte is received.            |
  +      +                +     +                                                                                                                                                                                                                                                                                                                                            +
  |      |                |     | **NOTE**:                                                                                                                                                                                                                                                                                                                                  |
  +      +                +     +                                                                                                                                                                                                                                                                                                                                            +
  |      |                |     | This register is applicable only when 'ADDR_MATCH' (LCR_EXT[1]) and 'DLS_E' (LCR_EXT[0]) bits are set to 1.                                                                                                                                                                                                                                |
  +      +                +     +                                                                                                                                                                                                                                                                                                                                            +
  |      |                |     | If UART_16550_COMPATIBLE is configured to 0, then RAR should be programmed only when UART is not busy.                                                                                                                                                                                                                                     |
  +      +                +     +                                                                                                                                                                                                                                                                                                                                            +
  |      |                |     | If UART_16550_COMPATIBLE is configured to 0, then RAR can be programmed at any point of the time. However, user must not change this register value when any receive is in progress.                                                                                                                                                       |
  +      +                +     +                                                                                                                                                                                                                                                                                                                                            +
  |      |                |     | Reset Value: 0x0                                                                                                                                                                                                                                                                                                                           |
  +------+----------------+-----+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

2.39 TAR
""""""""
- Name: Transmit Address Register (TAR)
- Size: 32 bits
- Address Offset: 0xC8
- Read/write access: read/write

.. table::  TAR Register Fields

  +------+----------------+-----+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | Bits | Name           | R/W | Description                                                                                                                                                                                                                                                                                                                                |
  +======+================+=====+============================================================================================================================================================================================================================================================================================================================================+
  | 31:8 | Reserved and   |     |                                                                                                                                                                                                                                                                                                                                            |
  +      +                +     +                                                                                                                                                                                                                                                                                                                                            +
  |      | read as 0      |     |                                                                                                                                                                                                                                                                                                                                            |
  +------+----------------+-----+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | 7:0  |  TAR           | R/W | This is an address matching register during transmit mode. If DLS_E (LCR_EXT[0]) bit is enabled, then UART sends the 9-bit character with 9-th bit set to 1 and remaining 8-bit address will be sent from this register provided 'SEND_ADDR' (LCR_EXT[2]) bit is set to 1.                                                                 |
  +      +                +     +                                                                                                                                                                                                                                                                                                                                            +
  |      |                |     | **NOTE**:                                                                                                                                                                                                                                                                                                                                  |
  +      +                +     +                                                                                                                                                                                                                                                                                                                                            +
  |      |                |     | This register is used only to send the address. The normal data should be sent by programming THR register.                                                                                                                                                                                                                                |
  +      +                +     +                                                                                                                                                                                                                                                                                                                                            +
  |      |                |     | Once the address is started to send on the UART serial lane, then 'SEND_ADDR' bit will be auto-cleared by the hardware.                                                                                                                                                                                                                    |
  +      +                +     +                                                                                                                                                                                                                                                                                                                                            +
  |      |                |     | Reset Value: 0x0                                                                                                                                                                                                                                                                                                                           |
  +------+----------------+-----+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

2.40 LCR_EXT
""""""""""""
- Name: Line Extended Control Register (LCR_EXT)
- Size: 32 bits
- Address Offset: 0xCC
- Read/write access: read/write

.. table::  LCR_EXT Register Fields

  +------+--------------+-----+------------------------------------------------------------------------+
  | Bits | Name         | R/W | Description                                                            |
  +======+==============+=====+========================================================================+
  | 31:4 | Reserved and |     |                                                                        |
  +      +              +     +                                                                        +
  |      | read as 0    |     |                                                                        |
  +------+--------------+-----+------------------------------------------------------------------------+
  | 3    | TRANSMIT_MODE| R/W | Transmit mode control bit. This bit is used to control the type of     |
  +      +              +     +                                                                        +
  |      |              |     | transmit mode during 9-bit data transfers.                             |
  +      +              +     +                                                                        +
  |      |              |     | 1 : In this mode of operation, Transmit Holding Register (THR) and     |
  +      +              +     +                                                                        +
  |      |              |     | Shadow Transmit Holding Register (STHR) are 9-bit wide. You must ensure|
  +      +              +     +                                                                        +
  |      |              |     | that the THR/STHR register is written correctly for address/data.      |
  +      +              +     +                                                                        +
  |      |              |     | Address: 9th bit is set to 1,                                          |
  +      +              +     +                                                                        +
  |      |              |     | Data: 9th bit is set to 0.                                             |
  +      +              +     +                                                                        +
  |      |              |     | NOTE: Transmit address register (TAR) is not applicable in this mode   |
  +      +              +     +                                                                        +
  |      |              |     | of operation.                                                          |
  +      +              +     +                                                                        +
  |      |              |     | 0 : In this mode of operation, Transmit Holding Register (THR) and     |
  +      +              +     +                                                                        +
  |      |              |     | Shadow Transmit Holding Register (STHR) are 8-bit wide. The user needs |
  +      +              +     +                                                                        +
  |      |              |     | to program the address into Transmit Address Register (TAR) and data   |
  +      +              +     +                                                                        +
  |      |              |     | into the THR/STHR register. SEND_ADDR bit is used as a control knob to |
  +      +              +     +                                                                        +
  |      |              |     | indicate the UART on when to send the address.                         |
  +      +              +     +                                                                        +
  |      |              |     | Reset Value: 0x0                                                       |
  +------+--------------+-----+------------------------------------------------------------------------+


.. table::

  +------+--------------+-----+------------------------------------------------------------------------+
  | 2    | SEND_ADDR    | R/W | Send address control bit. This bit is used as a control knob for the   |
  +      +              +     +                                                                        +
  |      |              |     | user to determine when to send the address during transmit mode.       |
  +      +              +     +                                                                        +
  |      |              |     | 1 - 9-bit character will be transmitted with 9th bit set to 1 and the  |
  +      +              +     +                                                                        +
  |      |              |     | remaining 8-bits will match to what is being programmed in "Transmit   |
  +      +              +     +                                                                        +
  |      |              |     | Address Register".                                                     |
  +      +              +     +                                                                        +
  |      |              |     | 0 - 9-bit character will be transmitted with 9th bit set to 0 and the  |
  +      +              +     +                                                                        +
  |      |              |     | remaining 8-bits will be taken from the TxFIFO which is programmed     |
  +      +              +     +                                                                        +
  |      |              |     | through 8-bit wide THR/STHR register.                                  |
  +      +              +     +                                                                        +
  |      |              |     | NOTE:                                                                  |
  +      +              +     +                                                                        +
  |      |              |     | 1 This bit is auto-cleared by the hardware, after sending out the      |
  +      +              +     +                                                                        +
  |      |              |     | address character. User is not expected to program this bit to 0.      |
  +      +              +     +                                                                        +
  |      |              |     | 2 This field is applicable only when DLS_E bit is set to 1 and         |
  +      +              +     +                                                                        +
  |      |              |     | TRANSMIT_MODE is set to 0.                                             |
  +      +              +     +                                                                        +
  |      |              |     | Reset Value: 0x0                                                       |
  +------+--------------+-----+------------------------------------------------------------------------+


.. table::

  +------+--------------+-----+------------------------------------------------------------------------+
  | 1    | ADDR_MATCH   | R/W | Address Match Mode. This bit is used to enable the address match       |
  +      +              +     +                                                                        +
  |      |              |     | feature during receive.                                                |
  +      +              +     +                                                                        +
  |      |              |     | 1 - Address match mode; UART will wait until the incoming              |
  +      +              +     +                                                                        +
  |      |              |     | character with 9-th bit set to 1. And, further checks to see if the    |
  +      +              +     +                                                                        +
  |      |              |     | address matches with what is programmed in "Receive Address Match      |
  +      +              +     +                                                                        +
  |      |              |     | Register". If match is found, then sub-sequent characters will be      |
  +      +              +     +                                                                        +
  |      |              |     | treated as valid data and UART starts receiving data.                  |
  +      +              +     +                                                                        +
  |      |              |     | 0 - Normal mode; UART will start to receive the data and 9-bit         |
  +      +              +     +                                                                        +
  |      |              |     | character will be formed and written into the receive Rx FIFO. User is |
  +      +              +     +                                                                        +
  |      |              |     | responsible to read the data and differentiate b/n address and data.   |
  +      +              +     +                                                                        +
  |      |              |     | NOTE: This field is applicable only when DLS_E is set to 1.            |
  +      +              +     +                                                                        +
  |      |              |     | Reset Value: 0x0                                                       |
  +------+--------------+-----+------------------------------------------------------------------------+
  | 0    | DLS_E        | R/W | Extension for DLS. This bit is used to enable 9-bit data for transmit  |
  +      +              +     +                                                                        +
  |      |              |     | and receive transfers.                                                 |
  +      +              +     +                                                                        +
  |      |              |     | 1 = 9 bits per character                                               |
  +      +              +     +                                                                        +
  |      |              |     | 0 = Number of data bits selected by DLS                                |
  +      +              +     +                                                                        +
  |      |              |     | Reset Value: 0x0                                                       |
  +------+--------------+-----+------------------------------------------------------------------------+

2.41 CPR
""""""""
- Name: Component Parameter Register
- Size: 32 bits
- Address Offset: 0xF4
- Read/write access: read-only

This register is valid only when UART_ADD_ENCODED_PARAMS = 1. If the 
UART_ADD_ENCODED_PARAMS parameter is not set, this register does not exist and reading from this 
register address returns 0.

.. table::  CPR Register Fields

  +------+-------------------------+-----+------------------------------------------------+
  | Bits | Name                    | R/W | Description                                    |
  +======+=========================+=====+================================================+
  | 31:24| Reserved and read as 0  |     |                                                |
  +------+-------------------------+-----+------------------------------------------------+
  | 23:16| FIFO_MODE               | R   | 0x00 = 0                                       |
  |      |                         |     |                                                |
  |      |                         |     | 0x01 = 16                                      |
  |      |                         |     |                                                |
  |      |                         |     | 0x02 = 32                                      |
  |      |                         |     |                                                |
  |      |                         |     | to                                             |
  |      |                         |     |                                                |
  |      |                         |     | 0x80 = 2048                                    |
  |      |                         |     |                                                |
  |      |                         |     | 0x81-0xff = reserved                           |
  +------+-------------------------+-----+------------------------------------------------+
  | 15:14| Reserved and read as 0  |     |                                                |
  +------+-------------------------+-----+------------------------------------------------+
  | 13   | DMA_EXTRA               | R   | 0 - FALSE                                      |
  |      |                         |     |                                                |
  |      |                         |     | 1 - TRUE                                       |
  +------+-------------------------+-----+------------------------------------------------+
  | 12   | UART_ADD_ENCODED_PARAMS | R   | 0 - FALSE                                      |
  |      |                         |     |                                                |
  |      |                         |     | 1 - TRUE                                       |
  +------+-------------------------+-----+------------------------------------------------+
  | 11   | SHADOW                  | R   | 0 - FALSE                                      |
  |      |                         |     |                                                |
  |      |                         |     | 1 - TRUE                                       |
  +------+-------------------------+-----+------------------------------------------------+
  | 10   | FIFO_STAT               | R   | 0 - FALSE                                      |
  |      |                         |     |                                                |
  |      |                         |     | 1 - TRUE                                       |
  +------+-------------------------+-----+------------------------------------------------+
  | 9    | FIFO_ACCESS             | R   | 0 - FALSE                                      |
  |      |                         |     |                                                |
  |      |                         |     | 1 - TRUE                                       |
  +------+-------------------------+-----+------------------------------------------------+
  | 8    | ADDITIONAL_FEAT         | R   | 0 - FALSE                                      |
  |      |                         |     |                                                |
  |      |                         |     | 1 - TRUE                                       |
  +------+-------------------------+-----+------------------------------------------------+
  | 7    | SIR_LP_MODE             | R   | 0 - FALSE                                      |
  |      |                         |     |                                                |
  |      |                         |     | 1 - TRUE                                       |
  +------+-------------------------+-----+------------------------------------------------+
  | 6    | SIR_MODE                | R   | 0 - FALSE                                      |
  |      |                         |     |                                                |
  |      |                         |     | 1 - TRUE                                       |
  +------+-------------------------+-----+------------------------------------------------+
  | 5    | THRE_MODE               | R   | 0 - FALSE                                      |
  |      |                         |     |                                                |
  |      |                         |     | 1 - TRUE                                       |
  +------+-------------------------+-----+------------------------------------------------+
  | 4    | AFCE_MODE               | R   | 0 - FALSE                                      |
  |      |                         |     |                                                |
  |      |                         |     | 1 - TRUE                                       |
  +------+-------------------------+-----+------------------------------------------------+
  | 3:2  | Reserved and read as 0  |     |                                                |
  +------+-------------------------+-----+------------------------------------------------+
  | 1:0  | APB_DATA_WIDTH          | R   | 00 - 8 bits                                    |
  |      |                         |     |                                                |
  |      |                         |     | 01 - 16 bits                                   |
  |      |                         |     |                                                |
  |      |                         |     | 10 - 32 bits                                   |
  |      |                         |     |                                                |
  |      |                         |     | 11 - reserved                                  |
  +------+-------------------------+-----+------------------------------------------------+

2.42 UCV
""""""""
- Name: UART Component Version
- Size: 32 bits
- Address Offset: 0xF8
- Read/write access: read-only

This register is valid only when the UART is configured to have additional features implemented 
(ADDITIONAL_FEATURES = YES). If additional features are not implemented, this register does not exist 
and reading from this register address returns 0.

.. table::  UCV Register Fields

  +------+-------------------+-----+------------------------------------------------------------+
  | Bits | Name              | R/W | Description                                                |
  +======+===================+=====+============================================================+
  | 31:0 | UART Component    | R   | ASCII value for each number in the version, followed by\*\ |
  |      | Version           |     | . For example 32_30_31_2A represents the version 2.01\*\   |
  |      |                   |     |                                                            |
  |      |                   |     | Reset Value: See the releases table in the AMBA 2 release  |
  |      |                   |     | notes.                                                     |
  +------+-------------------+-----+------------------------------------------------------------+

2.43 CTR
""""""""
- Name: Component Type Register
- Size: 32 bits
- Address Offset: 0xFC
- Read/write access: read-only

This register is valid only when the UART is configured to have additional features implemented 
(ADDITIONAL_FEATURES = YES). If additional features are not implemented, this register does not exist 
and reading from this register address returns 0.

.. table::  CTR Register Fields

  +------+-------------------+-----+------------------------------------------------------------+
  | Bits | Name              | R/W | Description                                                |
  +======+===================+=====+============================================================+
  | 31:0 | Peripheral ID     | R   | This register contains the peripherals identification code.|
  |      |                   |     |                                                            |
  |      |                   |     | Reset Value: 0x44570110                                    |
  +------+-------------------+-----+------------------------------------------------------------+
