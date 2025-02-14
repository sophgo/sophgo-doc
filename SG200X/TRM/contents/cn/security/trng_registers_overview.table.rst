.. _table_trng_registers_overview:
.. table:: TRNG Registers Overview
	:widths: 3 3 4

	+----------------------+---------+------------------------------------+
	| Name                 | Address | Description                        |
	|                      | Offset  |                                    |
	+======================+=========+====================================+
	| CTRL                 | 0x000   | Used to cause TRNG to execute one  |
	|                      |         | of a number of actions.            |
	+----------------------+---------+------------------------------------+
	| STAT                 | 0x00c   | Allows the user to monitor the     |
	|                      |         | internal status of the TRNG.       |
	+----------------------+---------+------------------------------------+
	| ISTAT                | 0x014   | Allows the user to monitor the     |
	|                      |         | interrupt status of the TRNG       |
	+----------------------+---------+------------------------------------+
	| RAND0                | 0x024   | Used by the host to read bits      |
	|                      |         | [31:0] of the newly generated      |
	|                      |         | 128-bit random.                    |
	+----------------------+---------+------------------------------------+
	| RAND1                | 0x028   | Used by the host to read bits      |
	|                      |         | [63:32] of the newly generated     |
	|                      |         | 128-bit random.                    |
	+----------------------+---------+------------------------------------+
	| RAND2                | 0x02c   | Used by the host to read bits      |
	|                      |         | [95:64] of the newly generated     |
	|                      |         | 128-bit random.                    |
	+----------------------+---------+------------------------------------+
	| RAND3                | 0x030   | Used by the host to read bits      |
	|                      |         | [127:96] of the newly generated    |
	|                      |         | 128-bit random.                    |
	+----------------------+---------+------------------------------------+
