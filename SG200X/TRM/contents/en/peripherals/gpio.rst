GPIO
----

The system includes 4 groups of GPIO (General Purpose Input/Output) under Active Domain, which are GPIO0 ~ GPIO3, and 1 group of GPIO under No-die Domain, RTCSYS_GPIO. Each group of GPIO provides 32 programmable input and output pins.

Note: In this manual, GPIOA is often used instead of GPIO0, GPIOB instead of GPIO1, GPIOC instead of GPIO2, and GPIOD instead of GPIO3.

The direction of each pin can be arbitrarily set as input or output, used to generate output signals for specific applications or collect input signals for specific applications. When set as an input pin, the GPIO can be used as an interrupt source; when set as an output pin, each GPIO can independently output 0 or 1.

GPIO can generate maskable interrupts based on the level or transition value of the input signal. The GPIOx_INTR_FLAG (x = 0 ~ 3) signal gives the interrupt controller an indication that an interrupt has occurred.

Features
~~~~~~~~

The direction of each pin can be arbitrarily set as input or output.

- When set as an input pin, GPIO can be used as an interrupt source.

- When set as an output pin, each GPIO can output 0 or 1 independently.

Way of Working
~~~~~~~~~~~~~~

Interface Reset
^^^^^^^^^^^^^^^

When the chip is powered on or the system is reset, the four GPIO modules will be reset at the same time, and the GPIO pins will be in the input state by default after reset.

General Purpose Input and Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Each pin can be set as input or output arbitrarily. The steps are as follows:

- Step 1: Configure the register GPIO_SWPORTA_DDR, set whether the GPIO is used as input or output.

- Step 2: When configured as an input pin, read the GPIO_EXT_PORTA register to view the input signal value; when configured as an output pin, write the output value to the GPIO_SWPORTA_DR register to control the GPIO output level.

Interrupt Operation
^^^^^^^^^^^^^^^^^^^

Each GPIO can be used as an interrupt source, controlled through 9 registers such as GPIO_INTEN. Through these registers the user can select the interrupt source, interrupt level polarity and edge triggering characteristics.

When multiple GPIO interrupts occur at the same time, they will be aggregated into one interrupt for reporting (each of the 4 groups of GPIOs will have a collective interrupt flag reported).

The characteristics of the interrupt source and the interrupt trigger category are determined by the five registers GPIO_INTTYPE_LEVEL, GPIO_INT_POLARITY, GPIO_INTMASK, GPIO_DEBOUNCE, and GPIO_LS_SYNC.

The original status and masked status of the interrupt are read through GPIO_RAW_INTSTATUS and GPIO_INTSTATUS. The clearing of interrupt status can be controlled by setting GPIO_PORTA_EOI.

Each GPIO can support interrupts. The setting steps are as follows:

- Step 1: Configure the register GPIO_INTTYPE_LEVEL, select level trigger or edge trigger.

- Step 2: Configure the register GPIO_INT_POLARITY, select low level/high level trigger and falling edge/rising edge trigger.

- Step 3: Write 0xFFFFFFFF to the register GPIO_PORTA_EOI to clear the interrupt.

- Step 4: Configure the GPIO_INTEN register; enable the GPIO pin interrupt function.

.. _section_gpio_register_overview:

GPIO Register Overview
~~~~~~~~~~~~~~~~~~~~~~

The chip includes 4 groups of GPIO under Active Domain and 1 group of GPIO under No-die Domain. The base address is shown in table :ref:`table_gpio_module_baseaddress`.

.. This table is relatively small, so there is no separate file include

.. _table_gpio_module_baseaddress:
.. table:: Base addresses of GPIO modules
	:widths: 1 1

	+----------------------------------+----------------------------------+
	| GPIO Module                      | Base Address                     |
	+==================================+==================================+
	| GPIO0                            | 0x03020000                       |
	+----------------------------------+----------------------------------+
	| GPIO1                            | 0x03021000                       |
	+----------------------------------+----------------------------------+
	| GPIO2                            | 0x03022000                       |
	+----------------------------------+----------------------------------+
	| GPIO3                            | 0x03023000                       |
	+----------------------------------+----------------------------------+
	| RTCSYS_GPIO                      | 0x05021000                       |
	+----------------------------------+----------------------------------+

Table :ref:`table_gpio0_registers_overview` is the offset address and definition of the registers of the GPIO module (GPIO0) in group 1. GPIOs in other groups have the same register definitions.

.. This table is relatively small, so there is no separate file include

.. _table_gpio0_registers_overview:
.. table:: GPIO Registers Overview
	:widths: 3 3 4

	+----------------------+---------+------------------------------------+
	| Name                 | Address | Description                        |
	|                      | Offset  |                                    |
	+======================+=========+====================================+
	| GPIO_SWPORTA_DR      | 0x000   | Port A data register               |
	+----------------------+---------+------------------------------------+
	| GPIO_SWPORTA_DDR     | 0x004   | Port A data direction register     |
	+----------------------+---------+------------------------------------+
	| GPIO_INTEN           | 0x030   | Interrupt enable register          |
	+----------------------+---------+------------------------------------+
	| GPIO_INTMASK         | 0x034   | Interrupt mask register            |
	+----------------------+---------+------------------------------------+
	| GPIO_INTTYPE_LEVEL   | 0x038   | Interrupt level register           |
	+----------------------+---------+------------------------------------+
	| GPIO_INT_POLARITY    | 0x03c   | Interrupt polarity register        |
	+----------------------+---------+------------------------------------+
	| GPIO_INTSTATUS       | 0x040   | Interrupt status of Port A         |
	+----------------------+---------+------------------------------------+
	| GPIO_RAW_INTSTATUS   | 0x044   | Raw interrupt status of Port A     |
	|                      |         | (pre-masking)                      |
	+----------------------+---------+------------------------------------+
	| GPIO_DEBOUNCE        | 0x048   | Debounce enable register           |
	+----------------------+---------+------------------------------------+
	| GPIO_PORTA_EOI       | 0x04c   | Port A clear interrupt register    |
	+----------------------+---------+------------------------------------+
	| GPIO_EXT_PORTA       | 0x050   | Port A external port register      |
	+----------------------+---------+------------------------------------+
	| GPIO_LS_SYNC         | 0x060   | Level-sensitive synchronization    |
	|                      |         | enable register                    |
	+----------------------+---------+------------------------------------+

GPIO Register Description
~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../../contents-share/peripherals/gpio_registers_description.table.rst
