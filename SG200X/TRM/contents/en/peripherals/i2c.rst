I2C
---

Overview
~~~~~~~~

This chip is equipped with 6 I2C controllers (5 in Active Domain, 1 in No-die Domain), which can be individually configured as Master/Slave. For IO configuration, please refer to Function pin mux for configuration.

Function Description
~~~~~~~~~~~~~~~~~~~~

The I2C controller has the following features:

- Supports standard address (7bit) and extended address (10bit).

- The transfer rate supports standard mode (100kbit/s) and fast mode (400kbit/s).

- Support General Call and Start Byte functions.

- CBUS devices are not supported.

- Support DMA operation.

- Support 64 x 8bit TX FIFO and 64 x 8bit RX FIFO.


Functional Block Diagram
~~~~~~~~~~~~~~~~~~~~~~~~

:ref:`diagram_i2c_function_graph` is the functional block diagram of the I2C module. IIC_CLK is the module clock, and the chip supports 25MHz or 100MHz. The CPU selects various I2C modes and timings through the APB bus configuration register, writes TXFIFO, reads RXFIFO, and triggers FSM to send and receive SDA/SCL related IO signals. System DMA can also be used with I2C. DMA_IF, and write TXFIFO and read RXFIFO through the APB bus to send and receive I2C signals.

.. _diagram_i2c_function_graph:
.. figure:: ../../../../media/image90.png
	:align: center

	I2C functional block diagram

I2C Protocol Timing
~~~~~~~~~~~~~~~~~~~

The chip I2C supports the general standard I2C protocol timing as shown in :ref:`diagram_i2c_time_sequence`.

.. _diagram_i2c_time_sequence:
.. figure:: ../../../../media/image91.png
	:align: center

	I2C Protocol Timing

Way of Working
~~~~~~~~~~~~~~

Configure I2C Clock and Timing Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. CLK_DIV CRG register chapter, configure clk_byp_0_31 to select IIC_CLK as the 25MHz default clock source or 100MHz z clock source.

2. The module should be in disabled state when configuring related timing configuration. IC_ENABLE needs to be set to 0, and query IC_ENABLE_STATUS[0] to confirm it is 0.

3. Refer to the table :ref:`table_i2c_register_relationship`, select according to the I2C clock, and configure the I2C timing count register.

.. This table is relatively small, so I won’t put the file include separately.

.. _table_i2c_register_relationship:
.. table:: I2C clock selection and related register configuration relationship table
	:widths: 2 2 2 4

	+-------------+-----------+-----------+------------------------------+
	| Register    | 25M       | 100M      | Description                  |
	|             | IIC_CLK   | IIC_CLK   |                              |
	+=============+===========+===========+==============================+
	| IC_SS\      | 115       | 460       | SCL high level time counting |
	| _SCL_HCNT   |           |           | in standard speed mode       |
	+-------------+-----------+-----------+------------------------------+
	| IC_SS\      | 135       | 540       | SCL low level time counting  |
	| _SCL_LCNT   |           |           | in standard speed mode       |
	+-------------+-----------+-----------+------------------------------+
	| IC_FS\      | 21        | 90        | SCL high level time counting |
	| _SCL_HCNT   |           |           | in fast speed mode           |
	+-------------+-----------+-----------+------------------------------+
	| IC_FS\      | 42        | 160       | SCL low level time counting  |
	| _SCL_LCNT   |           |           | in fast speed mode           |
	+-------------+-----------+-----------+------------------------------+
	| IC_SDA_HOLD | 1         | 1         | SDA hold time count, relative|
	|             |           |           | to SCL negative edge         |
	+-------------+-----------+-----------+------------------------------+
	| IC_SDA_SETUP| 6         | 25        | SDA time count, relative to  |
	|             |           |           | the positive edge of SCL     |
	+-------------+-----------+-----------+------------------------------+
	| IC_FS_SPKLEN| 2         | 5         | I2C glitch suppression time  |
	|             |           |           | count                        |
	+-------------+-----------+-----------+------------------------------+

Data transfer in non-DMA mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _diagram_i2c_nodma_software_process:
.. figure:: ../../../../media/image92.png
	:align: center

	I2C Data transfer software process in non-DMA mode

Data transfer in DMA mode
^^^^^^^^^^^^^^^^^^^^^^^^^

.. _diagram_i2c_dma_software_process:
.. figure:: ../../../../media/image93.png
	:align: center

	I2C Data transmission software process in DMA mode

.. _section_i2c_register_overview:

I2C Register Overview
~~~~~~~~~~~~~~~~~~~~~

Includes 6 I2C, 5 Active Domain, 1 No-die Domain. Their base addresses are as follows. Each I2C consists of a set of control registers, each set identically defined.

.. include:: ../../contents-share/peripherals/i2c_registers_overview.table.rst

I2C Register Description
~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../../contents-share/peripherals/i2c_registers_description.table.rst
