CTRL
^^^^

.. _table_trng_ctrl:
.. table:: CTRL, Offset Address: 0x000
	:widths: 1 2 1 4 1

	+------+-------------------+-------+---------------------------+------+
	| Bits | Name              | Access| Description               | Reset|
	+======+===================+=======+===========================+======+
	| 31:4 |                   |       | Reserved                  |      |
	+------+-------------------+-------+---------------------------+------+
	| 3:0  | CMD               | R/W   | Execute a command. CMD can|      |
	|      |                   |       | only be written when the  |      |
	|      |                   |       | core is idle (see         |      |
	|      |                   |       | STAT.BUSY)                |      |
	|      |                   |       |                           |      |
	|      |                   |       | Enumerated values not     |      |
	|      |                   |       | listed are 'reserved'.    |      |
	|      |                   |       |                           |      |
	|      |                   |       | 0x0 (NOP): Execute a NOP  |      |
	|      |                   |       |                           |      |
	|      |                   |       | 0x1 (GEN_NOISE): Generate |      |
	|      |                   |       | full-entropy seed from    |      |
	|      |                   |       | noise                     |      |
	|      |                   |       |                           |      |
	|      |                   |       | 0x3 (CREATE_STATE): Move  |      |
	|      |                   |       | DRBG to create state      |      |
	|      |                   |       |                           |      |
	|      |                   |       | 0x6 (GEN_RANDOM): Generate|      |
	|      |                   |       | a random number           |      |
	+------+-------------------+-------+---------------------------+------+

STAT
^^^^

.. _table_trng_stat:
.. table:: STAT, Offset Address: 0x00c
	:widths: 1 2 1 4 1

	+------+----------------+-------+---------------------------+------+
	| Bits | Name           | Access| Description               | Reset|
	+======+================+=======+===========================+======+
	| 31   | BUST           | R     | Indicates the state of the|      |
	|      |                |       | core.                     |      |
	|      |                |       |                           |      |
	|      |                |       | 0x0 (BUSY_NOT): Idle      |      |
	|      |                |       |                           |      |
	|      |                |       | 0x1 (BUSY_EXEC): Currently|      |
	|      |                |       | executing a command       |      |
	+------+----------------+-------+---------------------------+------+
	| 30:0 |                |       | Reserved                  |      |
	+------+----------------+-------+---------------------------+------+

ISTAT
^^^^^

.. _table_trng_istat:
.. table:: ISTAT, Offset Address: 0x014
	:widths: 1 2 1 4 1

	+------+-------------+-------+--------------------------------+------+
	| Bits | Name        | Access| Description                    | Reset|
	+======+=============+=======+================================+======+
	| 31:5 |             |       | Reserved                       |      |
	+------+-------------+-------+--------------------------------+------+
	| 4    | DONE        |R/W    | When Read                      |      |
	|      |             |       |                                |      |
	|      |             |       | 0x0 (DONE_R0):No unacknowledged|      |
	|      |             |       | command completion             |      |
	|      |             |       |                                |      |
	|      |             |       | 0x1 (DONE_R1):                 |      |
	|      |             |       | Unacknowledged command         |      |
	|      |             |       | completion                     |      |
	|      |             |       |                                |      |
	|      |             |       | When Written                   |      |
	|      |             |       |                                |      |
	|      |             |       | 0x0 (DONE_W0): NOP             |      |
	|      |             |       |                                |      |
	|      |             |       | 0x1 (DONE_W1): Clear DONE Flag |      |
	+------+-------------+-------+--------------------------------+------+
	| 3:0  |             |       | Reserved                       |      |
	+------+-------------+-------+--------------------------------+------+

RAND0
^^^^^

.. _table_trng_rand0:
.. table:: RAND0, Offset Address: 0x024
	:widths: 1 2 1 4 1

	+------+-------------+-------+--------------------------------+------+
	| Bits | Name        | Access| Description                    | Reset|
	+======+=============+=======+================================+======+
	| 31:0 | RAND        | R     | Random data word 0.            |      |
	+------+-------------+-------+--------------------------------+------+

RAND1
^^^^^

.. _table_trng_rand1:
.. table:: RAND1, Offset Address: 0x028
	:widths: 1 2 1 4 1

	+------+-------------+-------+--------------------------------+------+
	| Bits | Name        | Access| Description                    | Reset|
	+======+=============+=======+================================+======+
	| 31:0 | RAND        | R     | Random data word 1.            |      |
	+------+-------------+-------+--------------------------------+------+

RAND2
^^^^^

.. _table_trng_rand2:
.. table:: RAND2, Offset Address: 0x02c
	:widths: 1 2 1 4 1

	+------+-------------+-------+--------------------------------+------+
	| Bits | Name        | Access| Description                    | Reset|
	+======+=============+=======+================================+======+
	| 31:0 | RAND        | R     | Random data word 2.            |      |
	+------+-------------+-------+--------------------------------+------+

RAND3
^^^^^

.. _table_trng_rand3:
.. table:: RAND3, Offset Address: 0x030
	:widths: 1 2 1 4 1

	+------+-------------+-------+--------------------------------+------+
	| Bits | Name        | Access| Description                    | Reset|
	+======+=============+=======+================================+======+
	| 31:0 | RAND        | R     | Random data word 3.            |      |
	+------+-------------+-------+--------------------------------+------+

