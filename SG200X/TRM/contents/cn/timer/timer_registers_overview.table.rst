.. _table_timer_registers_overview:
.. table:: Timer Registers Overview (Base: 0x030A0000)
	:widths: 2 1 2

	+----------------------+---------+------------------------------------+
	| Name                 | Address | Description                        |
	|                      | Offset  |                                    |
	+======================+=========+====================================+
	| Timer1LoadCount      | 0x000   | Value to be loaded into Timer1     |
	+----------------------+---------+------------------------------------+
	| Timer1CurrentValue   | 0x004   | Current Value of Timer1            |
	+----------------------+---------+------------------------------------+
	| Timer1ControlReg     | 0x008   | Control Register for Timer1        |
	+----------------------+---------+------------------------------------+
	| Timer1EOI            | 0x00c   | Clears the interrupt from Timer1   |
	+----------------------+---------+------------------------------------+
	| Timer1IntStatus      | 0x010   | Contains the interrupt status for  |
	|                      |         | Timer1                             |
	+----------------------+---------+------------------------------------+
	| Timer2 Registers     | 0x014~  | There are 5 registers in total, the|
	|                      | 0x024   | contents are the same as Timer1.   |
	+----------------------+---------+------------------------------------+
	| Timer3 Registers     | 0x028~  | There are 5 registers in total, the|
	|                      | 0x038   | contents are the same as Timer1.   |
	+----------------------+---------+------------------------------------+
	| Timer4 Registers     | 0x03c~  | There are 5 registers in total, the|
	|                      | 0x04c   | contents are the same as Timer1.   |
	+----------------------+---------+------------------------------------+
	| Timer5 Registers     | 0x050~  | There are 5 registers in total, the|
	|                      | 0x060   | contents are the same as Timer1.   |
	+----------------------+---------+------------------------------------+
	| Timer6 Registers     | 0x064~  | There are 5 registers in total, the|
	|                      | 0x074   | contents are the same as Timer1.   |
	+----------------------+---------+------------------------------------+
	| Timer7 Registers     | 0x078~  | There are 5 registers in total, the|
	|                      | 0x088   | contents are the same as Timer1.   |
	+----------------------+---------+------------------------------------+
	| Timer8 Registers     | 0x08c~  | There are 5 registers in total, the|
	|                      | 0x09c   | contents are the same as Timer1.   |
	+----------------------+---------+------------------------------------+
	| TimersIntStatus      | 0x0a0   | Contains the interrupt status of   |
	|                      |         | all timers in the component.       |
	+----------------------+---------+------------------------------------+
	| TimersEOI            | 0x0a4   | Returns all zeroes (0) and clears  |
	|                      |         | all active interrupts.             |
	+----------------------+---------+------------------------------------+
	| TimersRawIntStatus   | 0x0a8   | Contains the unmasked interrupt    |
	|                      |         | status of all timers in the        |
	|                      |         | component.                         |
	+----------------------+---------+------------------------------------+
