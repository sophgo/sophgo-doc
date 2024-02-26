Function Description
--------------------

Interface Description
~~~~~~~~~~~~~~~~~~~~~

The SPI NOR Flash controller can support three SPI NOR interface types, which are Standard SPI, Dual SPI interface mode and Qual SPI interface mode.

Standard SPI Interface Mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Standard SPI interface mode has 1bit data input line and 1bit data output line. The chart shows the write operation timing diagram of the Standard SPI interface mode, and the read operation timing diagram of the Standard SPI interface mode.

.. _diagram_standard_spi_write_sequence:
.. figure:: ../../../../media/image17.png
	:align: center

	Standard SPI interface mode write operation timing diagram

Timing description:

- command/address/dummy cycles are output on the DO line in single-bit serial mode.

- Data is output on the DO line in single-bit serial mode.

.. _diagram_standard_spi_read_sequence:
.. figure:: ../../../../media/image19.png
	:align: center

	Standard SPI interface mode read operation timing diagram

Timing description:

- command/address/dummy cycles are output on the DO line in single-bit serial mode.

- Data is input on the DI line in single-bit serial mode.

Dual-Input SPI Interface Mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Dual Input SPI interface mode, parallel 2bit data line in the data input stage. :ref:`diagram_dual_input_spi_sequence` is the operation sequence diagram of Dual Input SPI interface mode.

.. _diagram_dual_input_spi_sequence:
.. figure:: ../../../../media/image21.png
	:align: center

	Dual-Input SPI interface timing

Timing description:

- command/address/dummy cycles are output on the DO line in single-bit serial mode.

- Data is input (read) on the DO/DI line in 2 Bits.

Dual-IO SPI Interface Mode
^^^^^^^^^^^^^^^^^^^^^^^^^^

Dual IO SPI interface mode, parallel 2-bit data lines in the address output and data input stages. :ref:`diagram_dual_io_spi_sequence` is the operation sequence diagram of Dual IO SPI interface mode.

.. _diagram_dual_io_spi_sequence:
.. figure:: ../../../../media/image23.png
	:align: center

	Dual-IO SPI interface timing

Timing description:

- Command is output on the DO line in single-bit serial mode.

- address/dummy cycles/Data is output (written) or input (read) on the DO/DI line in 2 Bits mode.

Quad-Input SPI Interface Mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Quad Input SPI interface mode, parallel 4bit data lines in the data input stage. :ref:`diagram_quad_input_spi_sequence` is the Quad Input SPI interface mode operation sequence diagram.

.. _diagram_quad_input_spi_sequence:
.. figure:: ../../../../media/image24.png
	:align: center

	Quad-Input SPI mode timing diagram

Timing description:

- command/address/dummy cycles are output on the DO line in single-bit serial mode.

- Data is input (read) in DO/DI/WPN/HOLDN in 4 Bits mode.

Quad-IO SPI Interface Mode
^^^^^^^^^^^^^^^^^^^^^^^^^^

Quad IO SPI interface mode, parallel 4bit data lines in the address output and data input stages. :ref:`diagram_quad_io_spi_sequence` is the Quad IO SPI interface mode operation sequence diagram.

.. _diagram_quad_io_spi_sequence:
.. figure:: ../../../../media/image26.png
	:align: center

	Quad-IO SPI mode timing diagram

Timing description:

- Command is output on the DO line in single-bit serial mode.

- address/dummy cycles/Data is output (write) or input (read) in DO/DI/WPN/HOLDN in 4 Bits mode.

Boot Function
~~~~~~~~~~~~~

The SPI NOR Boot data is located at the chip address 0x1000_0000~0x1FFF_FFFF, which is directly mapped to the continuous address space 0x0000_0000~0x0FFF_FFFF of the SPI NOR Flash. SPI_NOR Flash can support up to 256MB. If you need to use SPI_NOR Flash larger than 16MB, you need to use the 4 bytes address mode. The reset state of the chip is 3bytes address mode, and the 4bytes address mode needs to be enabled through configuration, so SPI_NOR Flash needs to support 3bytes/4bytes address mode.

Register Operations
~~~~~~~~~~~~~~~~~~~

The software configures operation-related registers, such as operation commands, addresses, etc., and finally configures the reg_go_busy register to issue operations. The controller issues operations to the device based on the software configuration value.

DMA Operations
~~~~~~~~~~~~~~

- DMMR read mode

  When the SPI_NOR Flash Controller is in DMMR mode, the SPI_NOR Flash space is directly mapped to the chip address space 0x1000_0000~0x1FFF_FFFF. System DMA can use memory-to-memory mode to move SPI_NOR data to DDR.

- Non-DMMR read and write mode

  Instructions, addresses and data need to be sent and received through FF_PORT. It is necessary to configure the controller register to select read instructions, write instructions, instruction length, and data length, then write FF_PORT through CPU or DMA to issue instructions and addresses, and write/read FF_PORT to send/receive data.