WDT_CR
~~~~~~

.. _table_wdt_cr:
.. table:: WDT_CR, Offset Address: 0x000
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 4:0  | WDT_CR               | R/W   | [4:2] Reset pulse      | 0x0  |
	|      |                      |       | length.                |      |
	|      |                      |       |                        |      |
	|      |                      |       | This is used to select |      |
	|      |                      |       | the number of pclk     |      |
	|      |                      |       | cycles for which the   |      |
	|      |                      |       | system reset stays     |      |
	|      |                      |       | asserted. The range of |      |
	|      |                      |       | values available is 2  |      |
	|      |                      |       | to 256 pclk cycles.    |      |
	|      |                      |       |                        |      |
	|      |                      |       | 000 - 2 pclk cycles    |      |
	|      |                      |       |                        |      |
	|      |                      |       | 001 - 4 pclk cycles    |      |
	|      |                      |       |                        |      |
	|      |                      |       | 010 - 8 pclk cycles    |      |
	|      |                      |       |                        |      |
	|      |                      |       | 011 - 16 pclk cycles   |      |
	|      |                      |       |                        |      |
	|      |                      |       | 100 - 32 pclk cycles   |      |
	|      |                      |       |                        |      |
	|      |                      |       | 101 - 64 pclk cycles   |      |
	|      |                      |       |                        |      |
	|      |                      |       | 110 - 128 pclk cycles  |      |
	|      |                      |       |                        |      |
	|      |                      |       | 111 - 256 pclk cycles  |      |
	|      |                      |       |                        |      |
	|      |                      |       | [1] Response mode.     |      |
	|      |                      |       |                        |      |
	|      |                      |       | Selects the output     |      |
	|      |                      |       | response generated to  |      |
	|      |                      |       | a timeout.             |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = Generate a system  |      |
	|      |                      |       | reset.                 |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 = First generate an  |      |
	|      |                      |       | interrupt and if it is |      |
	|      |                      |       | not cleared by the     |      |
	|      |                      |       | time a second timeout  |      |
	|      |                      |       | occurs then generate a |      |
	|      |                      |       | system reset.          |      |
	|      |                      |       |                        |      |
	|      |                      |       | [0] WDT enable.        |      |
	|      |                      |       |                        |      |
	|      |                      |       | This bit is used to    |      |
	|      |                      |       | enable and disable the |      |
	|      |                      |       | WatchDog. When         |      |
	|      |                      |       | disabled,              |      |
	|      |                      |       | the counter does not   |      |
	|      |                      |       | decrement. Thus, no    |      |
	|      |                      |       | interrupts or system   |      |
	|      |                      |       | resets are generated.  |      |
	|      |                      |       |                        |      |
	|      |                      |       | Once this bit has been |      |
	|      |                      |       | enabled, it can be     |      |
	|      |                      |       | cleared only by a      |      |
	|      |                      |       | system reset.          |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = WDT disabled.      |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 = WDT enabled.       |      |
	+------+----------------------+-------+------------------------+------+
	| 6    | TOR_MODE             | R/W   | The Mode of Timeout    | 0x0  |
	|      |                      |       | Period                 |      |
	+------+----------------------+-------+------------------------+------+
	| 7    | ITOR_MODE            | R/W   | The Mode of Timeout    | 0x0  |
	|      |                      |       | Period for             |      |
	|      |                      |       | initialization         |      |
	+------+----------------------+-------+------------------------+------+
	| 31:5 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

WDT_TORR
~~~~~~~~

.. _table_wdt_torr:
.. table:: WDT_TORR, Offset Address: 0x004
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 3:0  | WDT_TORR             | R/W   | [3:0] TOP(TimeOut      | 0x0  |
	|      |                      |       | Period).               |      |
	|      |                      |       |                        |      |
	|      |                      |       | This field is used to  |      |
	|      |                      |       | select the timeout     |      |
	|      |                      |       | period from which the  |      |
	|      |                      |       | watchdog counter       |      |
	|      |                      |       | restarts. A change of  |      |
	|      |                      |       | the timeout period     |      |
	|      |                      |       | takes effect only      |      |
	|      |                      |       | after the next counter |      |
	|      |                      |       | restart (kick).        |      |
	|      |                      |       |                        |      |
	|      |                      |       | The range of values is |      |
	|      |                      |       | limited by 32-bit      |      |
	|      |                      |       | width. If TOP is       |      |
	|      |                      |       | programmed to select a |      |
	|      |                      |       | range that is greater  |      |
	|      |                      |       | than the counter       |      |
	|      |                      |       | width, the timeout     |      |
	|      |                      |       | period is truncated    |      |
	|      |                      |       | to fit to the counter  |      |
	|      |                      |       | width. This affects    |      |
	|      |                      |       | only the non-user      |      |
	|      |                      |       | specified values as    |      |
	|      |                      |       | users are limited to   |      |
	|      |                      |       | these boundaries       |      |
	|      |                      |       | during configuration.  |      |
	|      |                      |       |                        |      |
	|      |                      |       | The range of values    |      |
	|      |                      |       | available for a 32-bit |      |
	|      |                      |       | watchdog counter are:  |      |
	|      |                      |       |                        |      |
	|      |                      |       | TOR_MODE = 0           |      |
	|      |                      |       |                        |      |
	|      |                      |       | T = 2^(16 + WDT_TORR)  |      |
	|      |                      |       |                        |      |
	|      |                      |       | TOR_MODE = 1           |      |
	|      |                      |       |                        |      |
	|      |                      |       | T = WDT_TOC <<(        |      |
	|      |                      |       | WDT_TORR +1)           |      |
	+------+----------------------+-------+------------------------+------+
	| 7:4  | WDT_ITORR            |       | Initial TimeOut Period |      |
	|      |                      |       |                        |      |
	|      |                      |       | ITOR_MODE = 0          |      |
	|      |                      |       |                        |      |
	|      |                      |       | T = 2^(16 + WDT_ITORR) |      |
	|      |                      |       |                        |      |
	|      |                      |       | ITOR_MODE = 1          |      |
	|      |                      |       |                        |      |
	|      |                      |       | T = WDT_TOC <<(        |      |
	|      |                      |       | WDT_ITORR +1)          |      |
	+------+----------------------+-------+------------------------+------+
	| 31:4 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

WDT_CCVR
~~~~~~~~

.. _table_wdt_ccvr:
.. table:: WDT_CCVR, Offset Address: 0x008
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 31:0 | WDT_CCVR             | RO    | This register, when    |      |
	|      |                      |       | read, is the current   |      |
	|      |                      |       | value of the internal  |      |
	|      |                      |       | counter.               |      |
	+------+----------------------+-------+------------------------+------+

WDT_CRR
~~~~~~~

.. _table_wdt_crr:
.. table:: WDT_CRR, Offset Address: 0x00c
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 7:0  | WDT_CRR              | R/W   | [7:0] Counter Restart  | 0x0  |
	|      |                      |       | Register               |      |
	|      |                      |       |                        |      |
	|      |                      |       | This register is used  |      |
	|      |                      |       | to restart the WDT     |      |
	|      |                      |       | counter. As a safety   |      |
	|      |                      |       | feature to prevent     |      |
	|      |                      |       | accidental restarts,   |      |
	|      |                      |       | the value 0x76 must be |      |
	|      |                      |       | written. A restart     |      |
	|      |                      |       | also clears the WDT    |      |
	|      |                      |       | interrupt. Reading     |      |
	|      |                      |       | this register returns  |      |
	|      |                      |       | zero.                  |      |
	+------+----------------------+-------+------------------------+------+
	| 31:8 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

WDT_STAT
~~~~~~~~

.. _table_wdt_stat:
.. table:: WDT_STAT, Offset Address: 0x010
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | WDT_STAT             | RO    | [0] Interrupt Status   |      |
	|      |                      |       | Register               |      |
	|      |                      |       |                        |      |
	|      |                      |       | This register shows    |      |
	|      |                      |       | the interrupt status   |      |
	|      |                      |       | of the WDT.            |      |
	|      |                      |       |                        |      |
	|      |                      |       | 1 = Interrupt is       |      |
	|      |                      |       | active regardless of   |      |
	|      |                      |       | polarity.              |      |
	|      |                      |       |                        |      |
	|      |                      |       | 0 = Interrupt is       |      |
	|      |                      |       | inactive.              |      |
	+------+----------------------+-------+------------------------+------+
	| 31:1 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

WDT_EOI
~~~~~~~

.. _table_wdt_eoi:
.. table:: WDT_EOI, Offset Address: 0x014
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 0    | WDT_EOI              | RO    | [0] Interrupt Clear    |      |
	|      |                      |       | Register               |      |
	|      |                      |       |                        |      |
	|      |                      |       | Clears the watchdog    |      |
	|      |                      |       | interrupt. This can be |      |
	|      |                      |       | used to clear the      |      |
	|      |                      |       | interrupt without      |      |
	|      |                      |       | restarting the         |      |
	|      |                      |       | watchdog counter.      |      |
	+------+----------------------+-------+------------------------+------+
	| 31:1 | Reserved             |       |                        |      |
	+------+----------------------+-------+------------------------+------+

WDT_TOC
~~~~~~~

.. _table_wdt_toc:
.. table:: WDT_TOC, Offset Address: 0x01C
	:widths: 1 2 1 4 1

	+------+----------------------+-------+------------------------+------+
	| Bits | Name                 |Access | Description            |Reset |
	+======+======================+=======+========================+======+
	| 15:0 | WDT_TOC              | R/W   | Time out counter       | 0x0  |
	+------+----------------------+-------+------------------------+------+
