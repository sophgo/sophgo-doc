Function Description
~~~~~~~~~~~~~~~~~~~~

Interface Description
^^^^^^^^^^^^^^^^^^^^^

The SPI NAND Flash controller can support three SPI NAND interface types, namely Standard SPI, X2 interface mode and X4 interface mode.

Standard SPI Interface Mode
'''''''''''''''''''''''''''

Standard SPI interface mode has 1-bit data input line and 1-bit data output line. The chart :ref:`diagram_std_spi_write_sequence` is the write operation timing diagram of the Standard SPI interface mode, and the diagram :ref:`diagram_std_spi_read_sequence` is the read operation timing diagram of the Standard SPI interface mode.

.. _diagram_std_spi_write_sequence:
.. figure:: ../../../../media/image17.png
	:align: center

	Standard SPI interface mode write operation timing

Timing description:

- command/address/dummy cycles are output on the DO line in single-bit serial mode.

- Data is output on the DO line in single-bit serial mode.

.. _diagram_std_spi_read_sequence:
.. figure:: ../../../../media/image19.png
	:align: center

	Standard SPI interface mode read operation timing

Timing description:

- command/address/dummy cycles are output on the DO line in single-bit serial mode.

- Data is input on the DI line in single-bit serial mode.

X2 Interface Mode
'''''''''''''''''

X2 interface mode shares 2-bit data input and output lines. Diagram :ref:`diagram_spi_x2_operate_sequence` is the X2 interface mode operation sequence diagram.

.. _diagram_spi_x2_operate_sequence:
.. figure:: ../../../../media/image21.png
	:align: center

	SPI Nand X2 interface mode operation timing

Timing description:

- command/address/dummy cycles are output on the DO line in single-bit serial mode.

- Data is output (written) or input (read) on the DO/DI line in 2 Bits mode.

X4 Interface Mode
'''''''''''''''''

X4 interface mode shares 4-bit data input and output lines. Diagram :ref:`diagram_spi_x4_operate_sequence` is the X4 interface mode operation sequence diagram.

.. _diagram_spi_x4_operate_sequence:
.. figure:: ../../../../media/image24.png
	:align: center

	SPI Nand X4 interface mode operation timing

Timing description:

- command/address/dummy cycles are output on the DO line in single-bit serial mode.

- Data is output (written) or input (read) on the DO/DI/WPN/HOLDN line in 4 Bits mode.

SPI NAND FLASH Address Description
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When issuing SPI NAND Flash read and write operations, the column address is issued according to the specific operation.

- Write operation: Column address is configured during LOAD operation, row address is configured during PROGRAM operation.

- Read operation: configure the row address during PAGE READ TO CACHE operation and configure the column address during READ operation.

- Address issuance is completed by the controller, and the software needs to configure reg_trx_cmd_idx, and address configuration reg_trx_cmd_cnt0, reg_trx_cmd_cnt1 according to the operation instructions.

Boot Function
^^^^^^^^^^^^^

Since the SPI NAND Flash address space is discontinuous and there is the possibility of bad blocks, Boot data cannot be directly mapped to Flash.

Supports adaptive Boot function, which can automatically adapt hardware information based on Block0 data. The controller requires that physical Block0 must be a good block, and other blocks can be automatically skipped if they are bad blocks.

Register Operations
^^^^^^^^^^^^^^^^^^^

The software configures operation-related registers, such as operation commands, addresses, etc., and finally configures the reg_trx_start register to issue operations. The controller issues operations to the device based on the software configuration value. If data needs to be transferred to the device, an internal DMA operation is used to transfer the data.

Built-in DMA Operation Mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Supports built-in system DMA mode for read and write operations to increase access speed. In this way, on-chip or off-chip memory space can be directly accessed through the bus.

- Step 1: Configure the DMA channel to use.

- Step 2: Configure source and destination addresses.

- Step 3: Configure the transmission format and data length.

TIMEOUT Function
^^^^^^^^^^^^^^^^

The software sets a maximum 1 second TIMEOUT mechanism as a protection when the device does not respond normally.

