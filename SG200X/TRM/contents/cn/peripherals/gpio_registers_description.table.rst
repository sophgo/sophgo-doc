GPIO_SWPORTA_DR
^^^^^^^^^^^^^^^
.. _table_gpio_swporta_dr:
.. table:: GPIO_SWPORTA_DR, Offset Address: 0x000
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 31:0 | GPIO_SWPORTA_DR      | R/W   | Values written to this | 0x0  |
	|      |                      |       | register are output on |      |
	|      |                      |       | the I/O signals for    |      |
	|      |                      |       | Port A if the          |      |
	|      |                      |       | corresponding data     |      |
	|      |                      |       | direction bits for     |      |
	|      |                      |       | Port A are set to      |      |
	|      |                      |       | Output mode and the    |      |
	|      |                      |       | corresponding control  |      |
	|      |                      |       | bit for Port A is      |      |
	|      |                      |       | set to Software mode.  |      |
	|      |                      |       | The value read back is |      |
	|      |                      |       | equal to the last      |      |
	|      |                      |       | value written to this  |      |
	|      |                      |       | register.              |      |
	+------+----------------------+-------+------------------------+------+

GPIO_SWPORTA_DDR
^^^^^^^^^^^^^^^^
.. _table_gpio_swporta_ddr:
.. table:: GPIO_SWPORTA_DDR, Offset Address: 0x004
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 31:0 | GPIO_SWPORTA_DDR     | R/W   | Values written to this | 0x0  |
	|      |                      |       | register independently |      |
	|      |                      |       | control the direction  |      |
	|      |                      |       | of the corresponding   |      |
	|      |                      |       | data bit in Port A.    |      |
	|      |                      |       | The default direction  |      |
	|      |                      |       | can be configured as   |      |
	|      |                      |       | input or output after  |      |
	|      |                      |       | system reset through   |      |
	|      |                      |       | the GPIO_DFLT_DIR_A    |      |
	|      |                      |       | parameter.             |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 - Input (default)    |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 - Output             |      |
	+------+----------------------+-------+------------------------+------+

GPIO_INTEN
^^^^^^^^^^
.. _table_gpio_inten:
.. table:: GPIO_INTEN, Offset Address: 0x030
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 31:0 | GPIO_INTEN           | R/W   | Allows each bit of     | 0x0  |
	|      |                      |       | Port A to be           |      |
	|      |                      |       | configured for         |      |
	|      |                      |       | interrupts. By default |      |
	|      |                      |       | the generation of      |      |
	|      |                      |       | interrupts is          |      |
	|      |                      |       | disabled. Whenever a 1 |      |
	|      |                      |       | is written to a bit of |      |
	|      |                      |       | this register, it      |      |
	|      |                      |       | configures the         |      |
	|      |                      |       | corresponding bit on   |      |
	|      |                      |       | Port A to become an    |      |
	|      |                      |       | interrupt; otherwise,  |      |
	|      |                      |       | Port A operates as a   |      |
	|      |                      |       | normal GPIO signal.    |      |
	|      |                      |       | Interrupts are         |      |
	|      |                      |       | disabled on the        |      |
	|      |                      |       | corresponding bits of  |      |
	|      |                      |       | Port A if the          |      |
	|      |                      |       | corresponding data     |      |
	|      |                      |       | direction register is  |      |
	|      |                      |       | set to Output or if    |      |
	|      |                      |       | Port A mode is set to  |      |
	|      |                      |       | Hardware.              |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 - Configure Port A   |      |
	|      |                      |       | bit as normal GPIO     |      |
	|      |                      |       | signal (default)       |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 - Configure Port A   |      |
	|      |                      |       | bit as interrupt       |      |
	+------+----------------------+-------+------------------------+------+

GPIO_INTMASK
^^^^^^^^^^^^
.. _table_gpio_intmask:
.. table:: GPIO_INTMASK, Offset Address: 0x034
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 31:0 | GPIO_INTMASK         | R/W   | Controls whether an    | 0x0  |
	|      |                      |       | interrupt on Port A    |      |
	|      |                      |       | can create an          |      |
	|      |                      |       | interrupt for the      |      |
	|      |                      |       | interrupt controller   |      |
	|      |                      |       | by not masking it. By  |      |
	|      |                      |       | default, all           |      |
	|      |                      |       | interrupts bits are    |      |
	|      |                      |       | unmasked. Whenever a 1 |      |
	|      |                      |       | is written to a bit in |      |
	|      |                      |       | this register, it      |      |
	|      |                      |       | masks the interrupt    |      |
	|      |                      |       | generation capability  |      |
	|      |                      |       | for this signal;       |      |
	|      |                      |       | otherwise interrupts   |      |
	|      |                      |       | are allowed through.   |      |
	|      |                      |       | The unmasked status    |      |
	|      |                      |       | can be read as well as |      |
	|      |                      |       | the resultant status   |      |
	|      |                      |       | after masking.         |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 - Interrupt bits are |      |
	|      |                      |       | unmasked (default)     |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 - Mask interrupt     |      |
	+------+----------------------+-------+------------------------+------+

GPIO_INTTYPE_LEVEL
^^^^^^^^^^^^^^^^^^
.. _table_gpio_inttype_level:
.. table:: GPIO_INTTYPE_LEVEL, Offset Address: 0x038
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 31:0 | GPIO_INTTYPE_LEVEL   | R/W   | Controls the type of   | 0x0  |
	|      |                      |       | interrupt that can     |      |
	|      |                      |       | occur on Port A.       |      |
	|      |                      |       |                        |      |
	|      |                      |       | Whenever a 0 is        |      |
	|      |                      |       | written to a bit of    |      |
	|      |                      |       | this register, it      |      |
	|      |                      |       | configures the         |      |
	|      |                      |       | interrupt type to be   |      |
	|      |                      |       | level-sensitive;       |      |
	|      |                      |       | otherwise, it is       |      |
	|      |                      |       | edge-sensitive.        |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 - Level-sensitive    |      |
	|      |                      |       | (default)              |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 - Edge-sensitive     |      |
	+------+----------------------+-------+------------------------+------+

GPIO_INT_POLARITY
^^^^^^^^^^^^^^^^^
.. _table_gpio_int_polarity:
.. table:: GPIO_INT_POLARITY, Offset Address: 0x03c
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 31:0 | GPIO_INT_POLARITY    | R/W   | Controls the polarity  | 0x0  |
	|      |                      |       | of edge or level       |      |
	|      |                      |       | sensitivity that can   |      |
	|      |                      |       | occur on input of Port |      |
	|      |                      |       | A. Whenever a 0 is     |      |
	|      |                      |       | written to a bit of    |      |
	|      |                      |       | this register, it      |      |
	|      |                      |       | configures the         |      |
	|      |                      |       | interrupt type to      |      |
	|      |                      |       | falling-edge or        |      |
	|      |                      |       | active-low sensitive;  |      |
	|      |                      |       | otherwise, it is       |      |
	|      |                      |       | rising-edge or         |      |
	|      |                      |       | active-high sensitive. |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 - Active-low         |      |
	|      |                      |       | (default)              |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 - Active-high        |      |
	+------+----------------------+-------+------------------------+------+

GPIO_INTSTATUS
^^^^^^^^^^^^^^
.. _table_gpio_intstatus:
.. table:: GPIO_INTSTATUS, Offset Address: 0x040
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 31:0 | GPIO_INTSTATUS       | RO    | Interrupt status of    |      |
	|      |                      |       | Port A                 |      |
	+------+----------------------+-------+------------------------+------+

GPIO_RAW_INTSTATUS
^^^^^^^^^^^^^^^^^^

.. _table_gpio_raw_intstatus:
.. table:: GPIO_RAW_INTSTATUS, Offset Address: 0x044
	:widths: 1 3 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 31:0 | GPIO_RAW_INTSTATUS   | RO    | Raw interrupt of       |      |
	|      |                      |       | status of Port A       |      |
	|      |                      |       | (premasking bits)      |      |
	+------+----------------------+-------+------------------------+------+

GPIO_DEBOUNCE
^^^^^^^^^^^^^
.. _table_gpio_debounce:
.. table:: GPIO_DEBOUNCE, Offset Address: 0x048
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 31:0 | GPIO_DEBOUNCE        | R/W   | Controls whether an    | 0x0  |
	|      |                      |       | external signal that   |      |
	|      |                      |       | is the source of an    |      |
	|      |                      |       | interrupt needs to be  |      |
	|      |                      |       | debounced to remove    |      |
	|      |                      |       | any spurious glitches. |      |
	|      |                      |       | Writing a 1 to a bit   |      |
	|      |                      |       | in this register       |      |
	|      |                      |       | enables the debouncing |      |
	|      |                      |       | circuitry. A signal    |      |
	|      |                      |       | must be valid for two  |      |
	|      |                      |       | periods of an external |      |
	|      |                      |       | clock before it is     |      |
	|      |                      |       | internally processed.  |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 - No debounce        |      |
	|      |                      |       | (default)              |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 - Enable debounce    |      |
	+------+----------------------+-------+------------------------+------+

GPIO_PORTA_EOI
^^^^^^^^^^^^^^
.. _table_gpio_porta_eoi:
.. table:: GPIO_PORTA_EOI, Offset Address: 0x04c
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 31:0 | GPIO_PORTA_EOI       | R/W   | Controls the clearing  | 0x0  |
	|      |                      |       | of edge type           |      |
	|      |                      |       | interrupts from Port   |      |
	|      |                      |       | A.                     |      |
	|      |                      |       |                        |      |
	|      |                      |       | When a 1 is written    |      |
	|      |                      |       | into a corresponding   |      |
	|      |                      |       | bit of this register,  |      |
	|      |                      |       | the                    |      |
	|      |                      |       | interrupt is cleared.  |      |
	|      |                      |       | All interrupts are     |      |
	|      |                      |       | cleared when Port A is |      |
	|      |                      |       | not configured for     |      |
	|      |                      |       | interrupts.            |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 - No interrupt clear |      |
	|      |                      |       | (default)              |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 - Clear interrupt    |      |
	+------+----------------------+-------+------------------------+------+

GPIO_EXT_PORTA
^^^^^^^^^^^^^^

.. _table_gpio_ext_porta:
.. table:: GPIO_EXT_PORTA, Offset Address: 0x050
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 31:0 | GPIO_EXT_PORTA       | RO    | When Port A is         |      |
	|      |                      |       | configured as Input,   |      |
	|      |                      |       | then reading this      |      |
	|      |                      |       | location reads the     |      |
	|      |                      |       | values on the signal.  |      |
	|      |                      |       | When the data          |      |
	|      |                      |       | direction of Port A is |      |
	|      |                      |       | set as Output, reading |      |
	|      |                      |       | this location reads    |      |
	|      |                      |       | the data               |      |
	|      |                      |       | register for Port A.   |      |
	+------+----------------------+-------+------------------------+------+

GPIO_LS_SYNC
^^^^^^^^^^^^

.. _table_gpio_ls_sync:
.. table:: GPIO_LS_SYNC, Offset Address: 0x060
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 | Access| Description            | Reset|
	+======+======================+=======+========================+======+
	| 0    | GPIO_LS_SYNC         | R/W   | [0] Synchronization    | 0x0  |
	|      |                      |       | level                  |      |
	|      |                      |       |                        |      |
	|      |                      |       | Writing a 1 to this    |      |
	|      |                      |       | register results in    |      |
	|      |                      |       | all level-sensitive    |      |
	|      |                      |       | interrupts being       |      |
	|      |                      |       | synchronized to        |      |
	|      |                      |       | pclk_intr.             |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 - No synchronization |      |
	|      |                      |       | to pclk_intr (default) |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 - Synchronize to     |      |
	|      |                      |       | pclk_intr              |      |
	+------+----------------------+-------+------------------------+------+
	| 31:1 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
