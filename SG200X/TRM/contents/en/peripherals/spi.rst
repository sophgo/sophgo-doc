SPI
---

Overview
~~~~~~~~

The system is configured with 4 SPI controller modules, which can be used as Master to conduct synchronous serial communication with external devices to achieve serial-to-parallel and parallel-to-serial conversion of data.

Features
~~~~~~~~

The features of the SPI controller module are as follows:

- Supports three serial peripheral interface protocols: Motorola SPI (full duplex), TI SSP (full duplex), and NS MicroWire (half duplex)

- Independent receive/transmit FIFO

- Programmable data frame length: 4~16 bits

- SPI interface clock frequency programmable

- Support DMA operation mode

- Support internal loopback test mode

- The working reference clock can be set to 187.5MHz or 100MHz, and the output SPI_SCK supports a maximum of 46.875MHz

Function Description
~~~~~~~~~~~~~~~~~~~~

Typical Application
^^^^^^^^^^^^^^^^^^^

The application block diagram when the SPI master connects to the external slave is as shown in the chart :ref:`diagram_application_praph`

.. _diagram_application_praph:
.. figure:: ../../../../media/image98.png
	:align: center

	SPI application block diagram

Way of Working
~~~~~~~~~~~~~~

Operating Mode
^^^^^^^^^^^^^^

The working modes of SPI are divided into:

- Data transmission in interrupt or query mode

- Data transfer in DMA mode

Clock
^^^^^

The SPI controller module reference clock can be set to 187.5MHz or 100MHz.

The output SPI_SCK supports up to 46.875MHz.

The calculation is as follows:

Output SPI_SCK = SPI working reference clock / BAUDR

SPI working reference clock : 187.5MHz or 100MHz.

BAUDR register : Set an even number between 2 and 65534.

Calculation example:

SPI working reference clock = 187.5MHz and BAUDR =4

Output SPI_SCK = 187.5MHz / 4 = 46.875MHz



Interrupt Handling
^^^^^^^^^^^^^^^^^^

The SPI controller module has 6 interrupts, the first 5 of which are active high maskable independent interrupt sources.

- RXFINTR
  
  Receive FIFO interrupt request. This interrupt is set when there is RXFTLR+1 or more valid data in the receive FIFO.

- RXOINTR

  When the receive FIFO is full and new data needs to be written to the FIFO, FIFO Overflow will occur and this interrupt is set. At this time data is written to the receive shift register instead of the FIFO.

- RXUINTR

  When the receive FIFO is read empty and no new data is written to the receive FIFO before a new read request occurs, FIFO Underflow will be caused and the interrupt will be set. The values read at this time are all 0. This interrupt can be cleared by reading register RXUICR.

- TXOINTR

  When the transmit FIFO is full and new data needs to be written to the FIFO, FIFO Overflow will occur and this interrupt will be set.

- TXEINTR

  Send FIFO interrupt request. This interrupt is set when there is TXFTLR or less valid data in the transmit FIFO.

- SPI_INTR

  The combined interrupt is the result of the "OR" operation of the above five interrupts. To mask this interrupt, register IMR must be set to mask the above 5 interrupts. This interrupt is set if any of the above 5 independent interrupts is set and enabled.





Initialization
^^^^^^^^^^^^^^

The SPI controller module initialization steps are as follows:

- Step 1: Set register SPIENR to "0", stop the SPI module.

- Step 2: Configure the register BAUDR to set the output clock frequency division divisor. The set value must be an even number.

- Step 3: Set register CTRLR0 to configure parameters such as transmission data bit width and transmission frame format.

- Step 4: In DMA operation mode, configure the register DMACR to enable the DMA function of SPI. When operating in DMA mode, the interrupt-related registers should be set to disable interrupt signal generation.

- Step 5: In interrupt operation mode, set the register IMR to generate the corresponding interrupt signal.

- Step 6: Set register SPIENR to "1" to enable the SPI module.

SPI data transmission process
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- The process when the SPI master connects to the external SPI/SSP slave is shown in the diagram :ref:`diagram_spissp_transmitting_form`.

.. _diagram_spissp_transmitting_form:
.. figure:: ../../../../media/image99.png
	:align: center

	Data transmission process when connecting to external SPI/SSP slave

- The process when the SPI master connects to the external Microwire slave is shown in the diagram :ref:`diagram_microwire_process`.

.. _diagram_microwire_process:
.. figure:: ../../../../media/image100.png
	:align: center

	Data transmission process when connecting to external Microwire slave

Data transfer in DMA mode
^^^^^^^^^^^^^^^^^^^^^^^^^

The SPI module uses two DMA channels, one for transmitting and one for receiving. The relevant registers for SPI DMA mode settings are DMACR, DMATDLR, and DMARDLR.

The steps to enable SPI DMA mode are as follows:

- Step 1: Get two DMA channels.

- Step 2: Set register DMACR [1:0] to enable SPI DMA transmission and reception.

- Step 3: Set register SPIENR to "1" to enable SPI.

- Step 4: Send data:

   1. Configure the control registers related to the sending DMA channel.

   2. Start the DMA controller and respond to the SPI send FIFO request.

   3. Use the DMA controller interrupt report to determine whether the transmission is completed. If it is completed, close the SPI transmission DMA function.

- Step 5: Receive data:

   1. Configure the control registers related to the receive DMA channel.

   2. Start the DMA controller and respond to the DMA request of the SPI receive FIFO.

   3. Use the DMA controller interrupt report to determine whether the data reception is completed. If it is completed, close the SPI receiving DMA function.

- Step 6: Set register SPIENR to "0" to stop SPI.

Three serial peripheral bus timing diagrams
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Motorola SPI interface
^^^^^^^^^^^^^^^^^^^^^^

The following figures represent the various data transmission formats of Motorola SPI. Among them, SCPH represents the SPI_SCK phase, and SCPOL represents the SPI_SCK polarity, which is set through the register CTRLR0[7:6].

(A) SCPH = 0
||||||||||||

  In this mode, SPI_CS_X is set to high level when in idle state and set to low level when transmitting. SPI_SCK is different through the SCPOL setting. SCPOL = 0, it is set to low level when in idle state. During transmission, data is captured on the rising edge of the clock. SCPOL = 1, set to high level when in idle state. , when transmitting, the data is captured on the falling edge of the clock.

- The single frame transmission format is shown in the diagram :ref:`diagram_transmitting_form`.

.. _diagram_transmitting_form:
.. figure:: ../../../../media/image101.png
	:align: center

	Motorola SPI single frame transmission format (SCPH = 0)

- The continuous frame transmission format is shown in the diagram :ref:`diagram_serial_transmitting_form`.

.. _diagram_serial_transmitting_form:
.. figure:: ../../../../media/image102.png
	:align: center

	Motorola SPI continuous frame transmission format (SCPH = 0)

(B) SCPH = 1
||||||||||||

  In this mode, SPI_CS_X is set to high level when in idle state and set to low level when transmitting. SPI_SCK is different through the SCPOL setting. SCPOL = 0, it is set to low level when in idle state, and data is captured on the falling edge of the clock during transmission. SCPOL = 1, set to high level when in idle state. , when transmitting, the data is captured on the rising edge of the clock.

- The single frame transmission format is shown in the diagram :ref:`diagram_scphone_transform`.

.. _diagram_scphone_transform:
.. figure:: ../../../../media/image103.png
	:align: center

	Motorola SPI single frame transmission format (SCPH = 1)

- The continuous frame transmission format is shown in the diagram :ref:`diagram_scphone_sertransform`.

.. _diagram_scphone_sertransform:
.. figure:: ../../../../media/image104.png
	:align: center

	Motorola SPI continuous frame transmission format (SCPH = 1)

TI Synchronous Serial Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In SSP mode, SPI_CS_X is set to high level when in idle state and set to low level during transmission. SPI_SCK is set to low level when in idle state, and data is captured on the falling edge of the clock during transmission.

The following figures represent the TI SSP data transfer format.

- The single frame transmission format is shown in the diagram :ref:`diagram_sspone_transform`.

.. _diagram_sspone_transform:
.. figure:: ../../../../media/image105.png
	:align: center

	TI SSP single frame transmission format

- The continuous frame transmission format is shown in the diagram :ref:`diagram_sspone_sertransform`.

.. _diagram_sspone_sertransform:
.. figure:: ../../../../media/image106.png
	:align: center

	TI SSP continuous frame transmission format

National Semiconductor Microwire Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In Microwire mode, SPI_CS_X is set to high level when in idle state and set to low level during transmission. SPI_SCK is set to low level when in idle state, and data is captured on the rising edge of the clock during transmission.

When transmitting data in this mode, a control word must be added first, and the external chip then responds to the data word required by the Master based on the control word. The control word length can be set through register CTRLR0[15:12], and other related parameters can be set through register MWCR.

The following figures represent the NS Microwire data transmission format.

- The single frame transmission format is shown in the diagram :ref:`diagram_ns_microwire_oneframe_transform`.

.. _diagram_ns_microwire_oneframe_transform:
.. figure:: ../../../../media/image106.png
	:align: center

	NS Microwire Single frame transmission format

- The continuous frame transmission format is shown in the diagram :ref:`diagram_ns_microwire_continusframe_transform`.

.. _diagram_ns_microwire_continusframe_transform:
.. figure:: ../../../../media/image107.png
	:align: center

	NS Microwire continuous frame transmission format

Register Overview
~~~~~~~~~~~~~~~~~

The four sets of SPI module base addresses of the chip are shown in the table :ref:`table_spi_module_address`.

.. This table is relatively small, so there is no need to include a separate file.

.. _table_spi_module_address:
.. table:: Base addresses for 4 sets of SPI module
	:widths: 1 1

	+----------------------------------+----------------------------------+
	| GPIO Module                      | Base Address                     |
	+==================================+==================================+
	| SPI0                             | 0x04180000                       |
	+----------------------------------+----------------------------------+
	| SPI1                             | 0x04190000                       |
	+----------------------------------+----------------------------------+
	| SPI2                             | 0x041A0000                       |
	+----------------------------------+----------------------------------+
	| SPI3                             | 0x041B0000                       |
	+----------------------------------+----------------------------------+

Table :ref:`table_spi0_register_overview` is the offset address and definition of the registers of the first group of SPI modules (SPI0). SPI0 ~ SPI3 have the same register definitions.

.. include:: ../../contents-share/peripherals/spi_registers_overview.table.rst

Register Description
~~~~~~~~~~~~~~~~~~~~

.. include:: ../../contents-share/peripherals/spi_registers_description.table.rst
