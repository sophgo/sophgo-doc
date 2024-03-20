Timer1LoadCount
~~~~~~~~~~~~~~~

.. _table_timer1loadcount:
.. table:: Timer1LoadCount, Offset Address: 0x000
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 31:0 | Timer1LoadCount      | R/W   | Timer1 Load Count      | 0x0  |
	|      |                      |       | Register               |      |
	|      |                      |       |                        |      |
	|      |                      |       | Value to be loaded     |      |
	|      |                      |       | into Timer1. This is   |      |
	|      |                      |       | the value from which   |      |
	|      |                      |       | counting commences.    |      |
	|      |                      |       | Any value written to   |      |
	|      |                      |       | this register is       |      |
	|      |                      |       | loaded into the        |      |
	|      |                      |       | associated timer.      |      |
	+------+----------------------+-------+------------------------+------+

Timer1CurrentValue
~~~~~~~~~~~~~~~~~~

.. _table_timer1currentvalue:
.. table:: Timer1CurrentValue, Offset Address: 0x004
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 31:0 | Timer1CurrentValue   | RO    | Timer1 Current Value   |      |
	|      |                      |       |                        |      |
	|      |                      |       | Current Value of       |      |
	|      |                      |       | Timer1. This register  |      |
	|      |                      |       | is supported only when |      |
	|      |                      |       | timer_1_clk is         |      |
	|      |                      |       | synchronous to pclk.   |      |
	|      |                      |       | Reading this register  |      |
	|      |                      |       | when using independent |      |
	|      |                      |       | clocks results in an   |      |
	|      |                      |       | undefined value.       |      |
	+------+----------------------+-------+------------------------+------+

Timer1ControlReg
~~~~~~~~~~~~~~~~

.. _table_timer1controlreg:
.. table:: Timer1ControlReg, Offset Address: 0x008
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 2:0  | Timer1ControlReg     | R/W   | [2] Timer interrupt    | 0x0  |
	|      |                      |       | mask for Timer1        |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 - not masked         |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 - masked             |      |
	|      |                      |       |                        |      |
	|      |                      |       | [1] Timer mode for     |      |
	|      |                      |       | Timer1                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 - free-running mode  |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 - user-defined count |      |
	|      |                      |       | mode                   |      |
	|      |                      |       |                        |      |
	|      |                      |       | [0] Timer enable bit   |      |
	|      |                      |       | for Timer1             |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 - disable            |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 - enable             |      |
	+------+----------------------+-------+------------------------+------+
	| 31:3 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

Timer1EOI
~~~~~~~~~

.. _table_timer1eoi:
.. table:: Timer1EOI, Offset Address: 0x00c
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | Timer1EOI            | RO    | Reading from this      |      |
	|      |                      |       | register returns all   |      |
	|      |                      |       | zeroes (0) and clears  |      |
	|      |                      |       | the interrupt from     |      |
	|      |                      |       | Timer1.                |      |
	+------+----------------------+-------+------------------------+------+
	| 31:1 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

Timer1IntStatus
~~~~~~~~~~~~~~~

.. _table_timer1intstatus:
.. table:: Timer1IntStatus, Offset Address: 0x010
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | Timer1IntStatus      | RO    | Contains the interrupt |      |
	|      |                      |       | status for Timer1.     |      |
	+------+----------------------+-------+------------------------+------+
	| 31:1 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

TimersIntStatus
~~~~~~~~~~~~~~~

.. _table_timersintstatus:
.. table:: TimersIntStatus, Offset Address: 0x0a0
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 7:0  | TimersIntStatus      | RO    | Contains the interrupt |      |
	|      |                      |       | status of all timers.  |      |
	|      |                      |       |                        |      |
	|      |                      |       | Reading from this      |      |
	|      |                      |       | register does not      |      |
	|      |                      |       | clear any active       |      |
	|      |                      |       | interrupts:            |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 – either timer_intr  |      |
	|      |                      |       | or timer_intr_n is not |      |
	|      |                      |       | active after masking   |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 – either timer_intr  |      |
	|      |                      |       | or timer_intr_n is     |      |
	|      |                      |       | active after masking   |      |
	+------+----------------------+-------+------------------------+------+
	| 31:8 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

TimersEOI
~~~~~~~~~

.. _table_timerseoi:
.. table:: TimersEOI, Offset Address: 0x0a4
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 7:0  | TimersEOI            | RO    | Reading this register  |      |
	|      |                      |       | returns all zeroes (0) |      |
	|      |                      |       | and clears all active  |      |
	|      |                      |       | interrupts.            |      |
	+------+----------------------+-------+------------------------+------+
	| 31:8 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

TimersRawIntStatus
~~~~~~~~~~~~~~~~~~

.. _table_timersrawintstatus:
.. table:: TimersRawIntStatus, Offset Address: 0x0a8
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 7:0  | TimersRawIntStatus   | RO    | The register contains  |      |
	|      |                      |       | the unmasked interrupt |      |
	|      |                      |       | status of all timers.  |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 - either timer_intr  |      |
	|      |                      |       | or timer_intr_n is not |      |
	|      |                      |       | active prior to        |      |
	|      |                      |       | masking                |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 - either timer_intr  |      |
	|      |                      |       | or timer_intr_n is     |      |
	|      |                      |       | active prior to        |      |
	|      |                      |       | masking                |      |
	+------+----------------------+-------+------------------------+------+
	| 31:8 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+
