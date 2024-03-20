UART
----

Overview
~~~~~~~~

UART (Universal Asynchronous Receiver Transmitter) is an asynchronous serial communication interface. Its main function is to convert data from peripheral devices to serial and then transfer it to the internal bus, and to convert data from parallel to serial and then output it to external devices. The main function of UART is to interface with the UART of an external chip to achieve communication between the two chips.

This chip provides 5 UART controllers. The relevant overview is as follows:

.. This table is relatively small, so there is no need to include a separate file.

.. _table_uart_io_infodescribe:
.. table:: UART IO pin information
	:widths: 1 1 3

	+------------+-------------+----------------------------------------------+
	| Controller | Mode        | IO Pin                                       |
	+============+=============+==============================================+
	| UART0      | 2-line UART | UART0_TX/UART0_RX                            |
	+------------+-------------+----------------------------------------------+
	| UART1      |2/4-line UART| UART1_TX/UART1_RX/UART1_CTS/UART1_RTS        |
	|            |             +----------------------------------------------+
	|            |             | XGPIOA[20]/ XGPIOA[21]/ XGPIOA[22]/          |
	|            |             | XGPIOA[26]                                   |
	+------------+-------------+----------------------------------------------+
	| UART2      |2/4-line UART| UART2_TX/UART2_RX/UART2_CTS/UART2_RTS        |
	|            |             +----------------------------------------------+
	|            |             | XGPIOA[20]/ XGPIOA[21]/ XGPIOA[22]/          |
	|            |             | XGPIOA[26]                                   |
	|            |             +----------------------------------------------+
	|            |             | IIC2_SDA/IIC2_SCL                            |
	+------------+-------------+----------------------------------------------+
	| UART3      |2/4-line UART| SPI0_CS_X/SPI0_SCK/SPI0_SDI/SPI0_SDO         |
	|            |             +----------------------------------------------+
	|            |             | VI_DATA22/VI_DATA21/VI_DATA24/VI_DATA23      |
	|            |             +----------------------------------------------+
	|            |             | PWM3/PWM2                                    |
	+------------+-------------+----------------------------------------------+
	| UART4      | 2-line UART | XGPIOA[22]/ XGPIOA[26]                       |
	|            |             +----------------------------------------------+
	|            |             | UART1_RTS/UART1_CTS                          |
	+------------+-------------+----------------------------------------------+

Features
~~~~~~~~

The UART module has the following features:

- Supports 64 x 8bit transmit FIFO and 64 x 8bit receive FIFO.

- Supports programmable bit width of data bits and stop bits. The data bits can be set to 5/6/7/8 bits through the program.

- The stop bit can be set to 1bit, 1.5bit or 2bit through programming.

- Supports odd, even checksum or no checksum.

- Supports programmable transmission rate settings.

- Supports receive FIFO interrupt, transmit FIFO interrupt, and error interrupt.

- Supports initial interrupt status query and post-mask interrupt status query.

- Support DMA operation.

Function Description
~~~~~~~~~~~~~~~~~~~~

Application Block Diagram
^^^^^^^^^^^^^^^^^^^^^^^^^

UART is a universal point-to-point physical layer transmission protocol that can be used to interface with various systems, including PCs and various peripheral chips, and can be used as a communication interface between chips.

.. _diagram_uart_app_graph:
.. figure:: ../../../../media/image94.png
	:align: center

	UART application block diagram

Functional Principle
^^^^^^^^^^^^^^^^^^^^

- Baud Rate

   Since the UART interface does not have a reference clock and is an asynchronous transmission method, both parties need to use the same transmission speed, that is, the baud rate (buadrate) for communication. If there is an error, the error rate needs to be small enough to avoid misinformation. The rate of 1 bit is called baudrate. Typical baud rates are 300, 1200, 2400, 9600, 19200, 38400, 115200bps, etc.

- Frame Structure

   The UART transmission data structure is in frames. The frame structure includes start signal, data signal, check bit and end signal.

.. _diagram_uart_transmitting_structure:
.. figure:: ../../../../media/image95.png
	:align: center

	UART transfer data structure

- Start signal (start bit)

   The start signal is the mark of the beginning of a frame. The very beginning of initiating a frame transmission is to send a low-level signal bit on TXD. On RXD, if a low level signal bit is received in the idle state, it is judged as receiving the start of a detection transmission.

- Data signal (data bit)

   The data bit width can be adjusted according to different application requirements, and can be 5/6/7/8 bit data bit width. Typically 8-bit data width.

- Parity bit

   The check bit is a 1-bit error correction signal. The check bits of the UART include odd parity check, even parity and fixed check bits. It also supports the enable and disable of the check bit. For detailed description, please see the LCR register.

- End signal (stop bit)

   The end signal is the stop bit of the frame, supporting 1-bit, 1.5-bit and 2-bit stop bits. To send the end signal of a frame is to send TXD high level to complete the transmission and enter the idle state. After receiving a frame and counting the check bits, the end signal needs to be received.

Way of Working
~~~~~~~~~~~~~~

Baud Rate Configuration
^^^^^^^^^^^^^^^^^^^^^^^

- UART working clock (UART_SCLK) configuration

  You can refer to the CLK_DIV CRG register description to configure clk_sel_0_9~ clk_sel_0_13 to select the working clock of uart0~uart4. The default is 1: XTAL 25MHz. If configured as 0, the UART PLL divided clock source is selected. The PLL frequency division clock source is preset to 187.5MHz. If necessary, you can configure the frequency division register div_clk_187p5m to adjust the PLL frequency division clock to 1500/NMHz, up to 187.5MHz.

- UART baud rate configuration

  DLL and DLH are the baud rate division control registers inside the UART controller. DLH is the high 8 bits and DLL is the low 8 bits. Before configuring DLH and DLL, LCR[7] must be configured to 1. At this time, the registers RBR_THR_DLL(DLL) and IER_DLH(DLH) can be configured.

  After the configuration is completed, the baud rate is set. The formula is:

  .. math:: Baud\ rate = \ \frac{UART\_ SCLK}{16*(256*DLH + DLL)}

- Taking UART SCLK 25MHz as an example and configuring a baud rate of 115200, the formula is:

  .. math:: (256*DLH + DLL) = \ \frac{25M}{16*115200} = 13.5

  If you choose to configure DLL as 14 and DLH as 0, the actual baud rate is:

  .. math:: Baud\ rate = \ \frac{25M}{16*14} = 111607

  The one-bit time error is:

  .. math:: Bit\ Error = \ \frac{(115200 - 114286)}{115200} = 3.12\%

  The accumulated time error of one frame is: :math:`Frame\ Error = \ 3.12\%`\ \*10 = 31.2%

- Taking UART SCLK 187.5MHz as an example, configure a baud rate of 115200, and the formula is:

  .. math:: (256*DLH + DLL) = \ \frac{187.5M}{16*115200} = 101.7

  If you choose to configure DLL as 102 and DLH as 0, the actual baud rate is:

  .. math:: Baud\ rate = \ \frac{187.5M}{16*102} = 114890

  The one-bit time error is:

  .. math:: Bit\ Error = \ \frac{(115200 - 114890)}{115200} = 0.27\%

  The accumulated time error of one frame is: :math:`Frame\ Error = \ 3.12\%`\ \*10 = 2.7%

Data Sending Flow Chart
^^^^^^^^^^^^^^^^^^^^^^^

.. _diagram_uart_send_process:
.. figure:: ../../../../media/image96.png
	:align: center

	UART data sending flow chart

Data Receiving Flow Chart
^^^^^^^^^^^^^^^^^^^^^^^^^

.. _diagram_uart_receive_process:
.. figure:: ../../../../media/image97.png
	:align: center

	UART data Receiving Fflow chart

Data transfer in interrupt or query mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Initialization steps
''''''''''''''''''''

1. Write 1 to LCR[7]. Enable configuration of Divisor Latch Access.

2. Write the corresponding configuration values to the RBR_THR_DLL and IER_DLH registers to configure the transmission baud rate.

3. Write 0 to LCR[7].

4. Configure LCR and set the corresponding UART working mode

5. Configure FCR and set the corresponding transmit and receive FIFO thresholds.

6. If you use the interrupt mode, you need to set IER and enable the corresponding interrupt signal;

Data sending
''''''''''''

1. When LCR[7] is 0, write the transmission data to RBR_THR_DLL (Transmit Holding Register) to start data transmission.

2. If the query method is used, detect the TX_FIFO status by reading USR[1] (Transmit FIFO not full) and TFL (Transmit FIFO Level), and decide whether to continue writing data to RBR_THR_DLL based on the status of TX_FIFO;

3. If the interrupt mode is used, detect the corresponding interrupt status bit; decide whether to continue writing data to RBR_THR_DLL.

4. Determine whether the UART has completed sending all data by detecting USR[2] (Transmit FIFO Empty).

Data reception
''''''''''''''

1. If the query method is used, the RX_FIFO status is detected by reading USR[3] (Receive FIFO Not Empty) and RFL (Receive FIFO Level), and based on the status of RX_FIFO, it is decided whether to read RBR_THR_DLL (Receive Buffer Register) to obtain the data.

2. If the interrupt mode is used, the corresponding interrupt status bit detection is used to determine whether to read RBR_THR_DLL (Receive Buffer Register) and obtain the data.

Data transfer in DMA mode
^^^^^^^^^^^^^^^^^^^^^^^^^

Initialization steps
''''''''''''''''''''

1. Write 1 to LCR[7]. Enable configuration of Divisor Latch Access

2. Write the corresponding configuration values to the RBR_THR_DLL and IER_DLH registers to configure the transmission baud rate.

3. Write 0 to LCR[7].

4. Configure LCR and set the corresponding UART working mode

5. Configure FCR and set the corresponding transmit and receive FIFO thresholds.

6. Close ETBEI/ERBFI in IER;

Data sending
''''''''''''

1. Configure system DMA channel mapping. Refer to the system DMA channel mapping and configure the selected UART controller TX/RX request line number to the corresponding system DMA channel. For example: UART0 TX configures system DMA channel 3, then sdma_dma_ch_remap0[29:24]=9. After the configuration is completed, update_dma_remp_0_3 needs to be configured to make the configuration effective.

2. Configure the system DMA data channel, including data transmission source and destination addresses, data transmission number, transmission type and other parameters. Please refer to the DMA controller chapter for specific configuration.

3. Use the system DMA interrupt report to determine whether the data transmission is completed.

Data reception
''''''''''''''

1. Configure system DMA channel mapping. Refer to the DMA channel mapping and configure the selected UART controller TX/RX request line number to the corresponding system DMA channel. For example: UART0 RX configures system DMA channel 1, then sets sdma_dma_ch_remap0[13:8] = 8. After the configuration is completed, update_dma_remp_0_3 needs to be configured to make the configuration effective.

2. Configure the system DMA data channel, including data transmission source and destination addresses, data receiving area address, data transmission number, transmission type and other parameters. Please refer to the DMA controller chapter for specific configuration.

3. Determine whether data reception is completed through system DMA interrupt reporting.

.. _section_uart_register_overview:

UART Register Overview
~~~~~~~~~~~~~~~~~~~~~~

Includes 6 UARTs, 5 Active Domains, and 1 No-die Domain. Their base addresses are as follows. Each UART consists of a set of control registers, each set identically defined.

.. include:: ../../contents-share/peripherals/uart_registers_overview.table.rst

UART Register Description
~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../../contents-share/peripherals/uart_registers_description.table.rst
